#!/bin/bash
#
# WordPress Image Download and Organization Script
# For laurenceputra.github.io migration
#
# Usage: ./download-wordpress-images.sh [migrated-content-directory]
#
# This script:
# 1. Extracts image URLs from migrated markdown files
# 2. Downloads images from WordPress site
# 3. Organizes images in Hugo's /static/img/ directory
# 4. Updates image paths in markdown files
#

set -e  # Exit on error

# Configuration
WORDPRESS_DOMAIN="https://laurenceputra.com"
CONTENT_DIR="${1:-migrated-content}"
STATIC_IMG_DIR="static/img"

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo "================================================"
echo "WordPress Image Migration Script"
echo "================================================"
echo ""

# Check if content directory exists
if [ ! -d "$CONTENT_DIR" ]; then
    echo -e "${RED}Error: Content directory not found: $CONTENT_DIR${NC}"
    echo "Usage: $0 [migrated-content-directory]"
    exit 1
fi

# Create image directories
echo -e "${GREEN}Creating image directories...${NC}"
mkdir -p "$STATIC_IMG_DIR"/{awards,media,posts,pages}
echo "✓ Created directories in $STATIC_IMG_DIR/"
echo ""

# Extract image URLs from markdown files
echo -e "${GREEN}Extracting image URLs from markdown files...${NC}"
IMAGE_LIST_FILE="wordpress-images.txt"

# Find all image URLs in markdown files
# Looks for patterns like: ![alt](url) or ![alt](/path/to/image.jpg)
grep -ohr 'https://laurenceputra\.com/wp-content/uploads/[^)]*' "$CONTENT_DIR/" 2>/dev/null | sort -u > "$IMAGE_LIST_FILE" || true

# Also check for images with WordPress domain variations
grep -ohr 'http://laurenceputra\.com/wp-content/uploads/[^)]*' "$CONTENT_DIR/" 2>/dev/null | sort -u >> "$IMAGE_LIST_FILE" || true

# Remove duplicates
sort -u "$IMAGE_LIST_FILE" -o "$IMAGE_LIST_FILE"

IMAGE_COUNT=$(wc -l < "$IMAGE_LIST_FILE" | tr -d ' ')

if [ "$IMAGE_COUNT" -eq 0 ]; then
    echo -e "${YELLOW}Warning: No WordPress images found in markdown files${NC}"
    echo "This could mean:"
    echo "  - Images already use local paths"
    echo "  - No images in content"
    echo "  - Image URLs use different format"
    echo ""
    echo "Checking for other image patterns..."
    
    # Check for any image references
    grep -rh '!\[.*\](.*)' "$CONTENT_DIR/" | head -10
    echo ""
    rm "$IMAGE_LIST_FILE"
    exit 0
fi

echo "✓ Found $IMAGE_COUNT unique image URLs"
echo ""

# Download images
echo -e "${GREEN}Downloading images from WordPress...${NC}"
DOWNLOADED=0
FAILED=0
SKIPPED=0

while IFS= read -r url; do
    # Skip empty lines
    [ -z "$url" ] && continue
    
    # Extract filename and path
    filename=$(basename "$url")
    
    # Determine section from URL or filename
    section="posts"  # default
    if [[ "$url" == *"/awards/"* ]] || [[ "$filename" == *"award"* ]]; then
        section="awards"
    elif [[ "$url" == *"/media/"* ]] || [[ "$filename" == *"media"* ]] || [[ "$filename" == *"interview"* ]]; then
        section="media"
    fi
    
    # Target path
    target_path="$STATIC_IMG_DIR/$section/$filename"
    
    # Check if already exists
    if [ -f "$target_path" ]; then
        echo "⊘ Skipping (exists): $filename"
        ((SKIPPED++))
        continue
    fi
    
    # Download with retry logic
    echo "⬇ Downloading: $filename"
    
    if curl -f -s -L -o "$target_path" "$url" 2>/dev/null; then
        # Verify file is not empty and is actually an image
        if [ -s "$target_path" ]; then
            file_type=$(file -b --mime-type "$target_path")
            if [[ "$file_type" == image/* ]]; then
                echo "  ✓ Saved to: $target_path"
                ((DOWNLOADED++))
            else
                echo -e "  ${YELLOW}✗ Not an image: $file_type${NC}"
                rm "$target_path"
                ((FAILED++))
            fi
        else
            echo -e "  ${YELLOW}✗ Empty file${NC}"
            rm "$target_path"
            ((FAILED++))
        fi
    else
        echo -e "  ${RED}✗ Download failed${NC}"
        ((FAILED++))
    fi
    
    # Be polite to server
    sleep 0.5
    
done < "$IMAGE_LIST_FILE"

echo ""
echo "================================================"
echo "Download Summary"
echo "================================================"
echo "✓ Downloaded: $DOWNLOADED images"
echo "⊘ Skipped: $SKIPPED images (already exist)"
echo "✗ Failed: $FAILED images"
echo ""

# Update image paths in markdown files
echo -e "${GREEN}Updating image paths in markdown files...${NC}"

# Backup original files
echo "Creating backup of migrated content..."
cp -r "$CONTENT_DIR" "${CONTENT_DIR}.backup"
echo "✓ Backup created: ${CONTENT_DIR}.backup"
echo ""

UPDATED_FILES=0

# Update paths in all markdown files
while read -r file; do
    # Replace WordPress URL patterns with Hugo static paths
    # Pattern: https://laurenceputra.com/wp-content/uploads/YYYY/MM/filename.jpg
    # Replace with: /img/section/filename.jpg
    
    # Detect section from file path
    if [[ "$file" == *"/awards/"* ]]; then
        section="awards"
    elif [[ "$file" == *"/media"* ]]; then
        section="media"
    elif [[ "$file" == *"/pages/"* ]]; then
        section="pages"
    else
        section="posts"
    fi
    
    # Update image paths
    if grep -q "https\?://laurenceputra\.com/wp-content/uploads/" "$file"; then
        sed -i.bak "s|https\?://laurenceputra\.com/wp-content/uploads/[0-9]*/[0-9]*/|/img/$section/|g" "$file"
        rm "${file}.bak"
        echo "✓ Updated: $file"
        ((UPDATED_FILES++))
    fi
done < <(find "$CONTENT_DIR" -name "*.md" -type f)

echo ""
echo "✓ Updated image paths in $UPDATED_FILES files"
echo ""

# Summary report
echo "================================================"
echo "Migration Complete"
echo "================================================"
echo ""
echo "Images downloaded to:"
echo "  $STATIC_IMG_DIR/awards/"
echo "  $STATIC_IMG_DIR/media/"
echo "  $STATIC_IMG_DIR/posts/"
echo "  $STATIC_IMG_DIR/pages/"
echo ""
echo "Next steps:"
echo "  1. Review downloaded images in $STATIC_IMG_DIR/"
echo "  2. Test Hugo build: hugo server -D"
echo "  3. Verify images load correctly in browser"
echo "  4. Optimize images if needed (see WORDPRESS_MIGRATION_GUIDE.md)"
echo "  5. Copy updated content to main content/ directory"
echo ""
echo "Commands to copy content:"
echo "  cp -r $CONTENT_DIR/posts/* content/posts/"
echo "  cp -r $CONTENT_DIR/pages/* content/pages/"
echo "  cp -r $CONTENT_DIR/awards/* content/awards/"
echo "  cp -r $CONTENT_DIR/media-posts/* content/media/"
echo ""

# Optional: Image optimization recommendation
if command -v identify &> /dev/null; then
    echo "Image optimization available (ImageMagick detected)"
    echo "To optimize all images, run:"
    echo "  find $STATIC_IMG_DIR -name '*.jpg' -exec mogrify -resize 1920x1920\> -quality 85 {} \;"
    echo ""
fi

# Cleanup
rm "$IMAGE_LIST_FILE"

echo "================================================"
echo "✓ Image migration complete!"
echo "================================================"
