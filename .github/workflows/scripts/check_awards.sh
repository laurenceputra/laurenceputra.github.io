#!/usr/bin/env bash
set -euo pipefail

errs=0
shopt -s nullglob
for f in content/posts/awards/*.md; do
  echo "Checking $f"
  fm=$(sed -n '1,200p' "$f" | sed -n '/^---$/,/^---$/p' | sed '1d;$d')
  if ! echo "$fm" | grep -q "categories:"; then
    echo "ERROR: $f missing 'categories' front matter"
    errs=$((errs+1))
    continue
  fi
  # Check that 'Awards' is in the categories array
  if ! echo "$fm" | awk 'BEGIN{found=0} /categories:/{flag=1; next} /^$/{flag=0} flag{ if ($0 ~ /Awards/){found=1}} END{exit !found}'; then
    echo "ERROR: $f categories does not include 'Awards'"
    errs=$((errs+1))
  fi
  # Check external_url presence and value
  if echo "$fm" | grep -q "external_url:"; then
    url=$(echo "$fm" | sed -n 's/^[[:space:]]*external_url:[[:space:]]*"\?\(.*\)"\?$/\1/p' | head -n1)
    if [[ -z "$url" ]]; then
      echo "WARNING: $f has empty external_url"
    else
      if [[ ! "$url" =~ ^https:// ]]; then
        echo "ERROR: $f external_url is not https: $url"
        errs=$((errs+1))
      fi
    fi
  else
    echo "WARNING: $f missing 'external_url' front matter (optional; add if public announcement exists)"
  fi
done

# Validate referenced pages in content/_index.md
if grep -q "page:" content/_index.md; then
  while IFS= read -r line; do
    page=$(echo "$line" | sed -E 's/^[[:space:]]*page:[[:space:]]*"?([^"]*)"?$/\1/')
    if [[ -n "$page" ]]; then
      if [[ ! -f "content/posts/awards/$page.md" ]]; then
        echo "ERROR: content/_index.md references page '$page' but content/posts/awards/$page.md not found"
        errs=$((errs+1))
      fi
    fi
  done < <(grep "^[[:space:]]*page:" content/_index.md)
fi

if [ "$errs" -ne 0 ]; then
  echo "$errs errors found"
  exit 1
fi

echo "All award posts passed validation"
