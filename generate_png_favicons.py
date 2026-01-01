#!/usr/bin/env python3
"""
Generate 32x32 and 16x16 PNG favicon files without PIL.
Creates simple geometric designs suitable for favicon use.
"""

import struct
import zlib


def create_png(width, height, pixels):
    """
    Create a PNG file from pixel data.
    pixels should be a list of (r, g, b) tuples for each pixel.
    """
    # PNG signature
    png_signature = b'\x89PNG\r\n\x1a\n'

    # IHDR chunk (image header)
    def make_chunk(chunk_type, data):
        chunk = chunk_type + data
        crc = zlib.crc32(chunk) & 0xffffffff
        return struct.pack('>I', len(data)) + chunk + struct.pack('>I', crc)

    # IHDR: width, height, bit_depth=8, color_type=2 (RGB), compression=0, filter=0, interlace=0
    ihdr_data = struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0)
    ihdr_chunk = make_chunk(b'IHDR', ihdr_data)

    # IDAT chunk (image data)
    # Build raw image data with filter byte (0 = no filter) for each scanline
    raw_data = b''
    for y in range(height):
        raw_data += b'\x00'  # filter type for this scanline
        for x in range(width):
            r, g, b = pixels[y * width + x]
            raw_data += bytes([r, g, b])

    # Compress the raw data
    compressed_data = zlib.compress(raw_data, 9)
    idat_chunk = make_chunk(b'IDAT', compressed_data)

    # IEND chunk (end of file)
    iend_chunk = make_chunk(b'IEND', b'')

    # Combine all chunks
    png_data = png_signature + ihdr_chunk + idat_chunk + iend_chunk
    return png_data


def create_favicon(size):
    """
    Create a favicon with a simple, professional design.
    Uses a gradient background with a centered circle pattern.

    Args:
        size: The width and height of the square favicon (16 or 32)
    """
    width = size
    height = size

    # Define color palette - professional blue/teal gradient (matching apple-touch-icon)
    bg_color_top = (52, 152, 219)      # Blue
    bg_color_bottom = (41, 128, 185)   # Darker blue
    accent_color = (255, 255, 255)     # White

    # Scale the circle radius based on size
    circle_radius = size // 2.5  # Inner circle radius

    pixels = []

    for y in range(height):
        # Create vertical gradient
        t = y / height
        bg_r = int(bg_color_top[0] * (1 - t) + bg_color_bottom[0] * t)
        bg_g = int(bg_color_top[1] * (1 - t) + bg_color_bottom[1] * t)
        bg_b = int(bg_color_top[2] * (1 - t) + bg_color_bottom[2] * t)

        for x in range(width):
            # Create a simple centered circle design
            center_x = width // 2
            center_y = height // 2

            # Distance from center
            dx = x - center_x
            dy = y - center_y
            distance = (dx * dx + dy * dy) ** 0.5

            # Create circle pattern
            if distance < circle_radius:
                # Inner circle - white/accent
                pixels.append(accent_color)
            else:
                # Background with gradient
                pixels.append((bg_r, bg_g, bg_b))

    return create_png(width, height, pixels)


if __name__ == '__main__':
    # Generate 32x32 favicon
    print("Generating 32x32 PNG favicon...")
    png_32 = create_favicon(32)
    output_32 = './images/favicon-32x32.png'
    with open(output_32, 'wb') as f:
        f.write(png_32)
    print(f"✓ Created {output_32}")
    print(f"  File size: {len(png_32)} bytes")

    # Generate 16x16 favicon
    print("\nGenerating 16x16 PNG favicon...")
    png_16 = create_favicon(16)
    output_16 = './images/favicon-16x16.png'
    with open(output_16, 'wb') as f:
        f.write(png_16)
    print(f"✓ Created {output_16}")
    print(f"  File size: {len(png_16)} bytes")

    print("\n✓ All PNG favicons generated successfully!")
