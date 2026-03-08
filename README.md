# Radar Stack Button Images

Button images for the FrameVR Radar Walking project.

## Files

- `button_x.png` - Hide button (512x512, white on dark blue #00008B)
- `button_ref.png` - Reflectivity button (512x512, white on dark red #8B0000)
- `button_vel.png` - Velocity button (512x512, white on dark green #006400)
- `button_kfdr.png` - Site label (512x256, white on black #000000)
- `create_buttons.py` - Script to regenerate button images

## Usage

These images are hosted on GitHub and used via raw URLs in the FrameVR API for radar stack creation.

## Regenerating

```bash
python3 create_buttons.py
```

Requires: Pillow (PIL)
