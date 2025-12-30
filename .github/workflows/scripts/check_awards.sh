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
  # Check external_url if present
  if echo "$fm" | grep -q "external_url:"; then
    url=$(echo "$fm" | sed -n 's/^[[:space:]]*external_url:[[:space:]]*"\?\(.*\)"\?$/\1/p' | head -n1)
    if [[ -n "$url" ]]; then
      if [[ ! "$url" =~ ^https:// ]]; then
        echo "ERROR: $f external_url is not https: $url"
        errs=$((errs+1))
      fi
    fi
  fi
done

if [ "$errs" -ne 0 ]; then
  echo "$errs errors found"
  exit 1
fi

echo "All award posts passed validation"
