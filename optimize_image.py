#!/usr/bin/env python3
"""Optimize profile image to reduce file size"""

from PIL import Image
import sys

def optimize_image(input_path, output_path, max_width=800, quality=85):
    """
    Optimize an image by resizing and compressing

    Args:
        input_path: Path to input image
        output_path: Path to save optimized image
        max_width: Maximum width in pixels (default 800)
        quality: JPEG quality 1-100 (default 85)
    """
    try:
        # Open the image
        img = Image.open(input_path)

        # Get current dimensions
        width, height = img.size
        print(f"Original size: {width}x{height}")

        # Calculate new dimensions maintaining aspect ratio
        if width > max_width:
            ratio = max_width / width
            new_width = max_width
            new_height = int(height * ratio)

            # Resize image with high-quality resampling
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            print(f"Resized to: {new_width}x{new_height}")
        else:
            print(f"Image width ({width}px) is already <= {max_width}px, skipping resize")

        # Convert to RGB if necessary (removes alpha channel)
        if img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')

        # Save with optimization
        img.save(output_path, 'JPEG', quality=quality, optimize=True)
        print(f"Saved optimized image to: {output_path}")
        print(f"Quality setting: {quality}")

        return True

    except Exception as e:
        print(f"Error optimizing image: {e}", file=sys.stderr)
        return False

if __name__ == "__main__":
    input_file = "images/profile.jpg"
    output_file = "images/profile.jpg"

    success = optimize_image(input_file, output_file, max_width=800, quality=85)
    sys.exit(0 if success else 1)
