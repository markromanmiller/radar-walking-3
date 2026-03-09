#!/usr/bin/env python3
"""
Button Image Generator for Radar Stack

Creates button images for the FrameVR radar walking project:
- X button: 512x512, white on dark blue (#00008B)
- REF button: 512x512, white on dark red (#8B0000)
- VEL button: 512x512, white on dark green (#006400)
- KFDR label: 512x256, white on black (#000000)
- Pressed versions: light backgrounds with black text for visual feedback

Usage:
    python3 create_buttons.py
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Button specifications: (text, bg_color, text_color, size, font_size, filename)
buttons = [
    # Normal buttons (white text on dark backgrounds)
    ("X", "#00008B", "white", (512, 512), 200, "button_x.png"),
    ("REF", "#8B0000", "white", (512, 512), 200, "button_ref.png"),
    ("VEL", "#006400", "white", (512, 512), 200, "button_vel.png"),
    ("KFDR", "#000000", "white", (512, 256), 120, "button_kfdr.png"),
    # Pressed buttons (black text on light backgrounds)
    ("X", "#B0C4DE", "black", (512, 512), 200, "button_x_pressed.png"),
    ("REF", "#FFB6C1", "black", (512, 512), 200, "button_ref_pressed.png"),
    ("VEL", "#90EE90", "black", (512, 512), 200, "button_vel_pressed.png"),
]

output_dir = os.path.dirname(os.path.abspath(__file__))

for text, bg_color, text_color, size, font_size, filename in buttons:
    # Create image with background color
    img = Image.new('RGB', size, bg_color)
    draw = ImageDraw.Draw(img)

    # Use DejaVu Sans Bold font
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
    except:
        font = ImageFont.load_default()

    # Get text bounding box and center it
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    x = (size[0] - text_width) // 2 - bbox[0]
    y = (size[1] - text_height) // 2 - bbox[1]

    # Draw text
    draw.text((x, y), text, fill=text_color, font=font)

    # Save
    filepath = os.path.join(output_dir, filename)
    img.save(filepath)
    print(f"✓ Created {filename} ({size[0]}x{size[1]}, font {font_size})")

print(f"\nAll buttons saved to: {output_dir}")
