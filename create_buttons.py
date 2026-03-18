#!/usr/bin/env python3
"""
Button Image Generator for Radar Stack

Creates button images for the FrameVR radar walking project:
- X button: 512x512, white on dark blue (#00008B)
- REF button: 512x512, white on dark red (#8B0000)
- VEL button: 512x512, white on dark green (#006400)
- Site label (e.g. KFDR): 512x256, white on black (#000000)
- Pressed versions: light backgrounds with black text for visual feedback

Usage:
    python3 create_buttons.py           # create X/REF/VEL buttons only
    python3 create_buttons.py KBYX      # create button_kbyx.png
    python3 create_buttons.py KBYX KAMX # create multiple site buttons
"""

from PIL import Image, ImageDraw, ImageFont
import os
import sys

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

CONTROL_BUTTONS = [
    ("X",   "#00008B", "white", (512, 512), 200, "button_x.png"),
    ("REF", "#8B0000", "white", (512, 512), 200, "button_ref.png"),
    ("VEL", "#006400", "white", (512, 512), 200, "button_vel.png"),
    ("X",   "#B0C4DE", "black", (512, 512), 200, "button_x_pressed.png"),
    ("REF", "#FFB6C1", "black", (512, 512), 200, "button_ref_pressed.png"),
    ("VEL", "#90EE90", "black", (512, 512), 200, "button_vel_pressed.png"),
]


def create_button(text, bg_color, text_color, size, font_size, filename):
    img = Image.new('RGB', size, bg_color)
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
    except:
        font = ImageFont.load_default()

    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (size[0] - text_width) // 2 - bbox[0]
    y = (size[1] - text_height) // 2 - bbox[1]

    draw.text((x, y), text, fill=text_color, font=font)

    filepath = os.path.join(OUTPUT_DIR, filename)
    img.save(filepath)
    print(f"✓ Created {filename} ({size[0]}x{size[1]}, font {font_size})")


def create_site_button(site_code):
    """Create a 512x256 label button for a NEXRAD site code (e.g. 'KBYX')."""
    code = site_code.upper()
    filename = f"button_{code.lower()}.png"
    create_button(code, "#000000", "white", (512, 256), 120, filename)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for site_code in sys.argv[1:]:
            create_site_button(site_code)
    else:
        for args in CONTROL_BUTTONS:
            create_button(*args)
        print(f"\nAll control buttons saved to: {OUTPUT_DIR}")
