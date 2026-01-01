#!/bin/bash
# Script to optimize profile.jpg using macOS sips command
# This must be run manually due to tool restrictions in the automated environment

set -e

INPUT="images/profile.jpg"
BACKUP="images/profile-original.jpg"
TEMP="images/profile-temp.jpg"

echo "=== Profile Image Optimization Script ==="
echo ""

# Check if file exists
if [ ! -f "$INPUT" ]; then
    echo "ERROR: $INPUT not found"
    exit 1
fi

# Get current file size
BEFORE_SIZE=$(ls -lh "$INPUT" | awk '{print $5}')
echo "Current file size: $BEFORE_SIZE"

# Get current dimensions
echo "Current dimensions:"
sips -g pixelWidth -g pixelHeight "$INPUT"

# Create backup
echo ""
echo "Creating backup at $BACKUP..."
cp "$INPUT" "$BACKUP"

# Resize to 800px width (maintaining aspect ratio)
echo "Resizing to 800px width..."
sips -Z 800 "$INPUT"

# Compress by setting JPEG quality to 85%
echo "Compressing to quality 85%..."
sips -s format jpeg -s formatOptions 85 "$INPUT" --out "$TEMP"
mv "$TEMP" "$INPUT"

# Show new file size
AFTER_SIZE=$(ls -lh "$INPUT" | awk '{print $5}')
echo ""
echo "=== Optimization Complete ==="
echo "Before: $BEFORE_SIZE"
echo "After:  $AFTER_SIZE"
echo ""
echo "New dimensions:"
sips -g pixelWidth -g pixelHeight "$INPUT"
echo ""
echo "Backup saved to: $BACKUP"
echo ""
echo "If you're satisfied with the result, you can delete the backup:"
echo "  rm $BACKUP"
echo ""
echo "If you want to restore the original:"
echo "  mv $BACKUP $INPUT"
