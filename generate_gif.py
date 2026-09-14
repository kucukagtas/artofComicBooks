"""
art of Comic Books - Animated GIF Preview Generator
---------------------------------------------------
This script uses the project's design tokens and images to generate
a high-resolution animated showcase GIF (img/preview.gif) for the README.

Usage:
    python3 generate_gif.py
"""

import os
import sys
import subprocess

try:
    from PIL import Image, ImageDraw, ImageFont, ImageOps
except ImportError:
    print("Pillow library is required. Installing pillow...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow"])
    from PIL import Image, ImageDraw, ImageFont, ImageOps

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(CURRENT_DIR, "img")
OUTPUT_GIF = os.path.join(IMG_DIR, "preview.gif")

WIDTH = 840
HEIGHT = 500

# Project Brand Colors
PRIMARY = (178, 102, 178)       # #b266b2
SECONDARY = (102, 178, 178)     # #66b2b2
DARK_BLUE = (46, 76, 109)       # #2e4c6d
LIGHT_BG = (237, 245, 247)      # #edf5f7
WHITE = (255, 255, 255)
DARK_TEXT = (40, 44, 52)
MUTED_TEXT = (100, 110, 125)

def get_font(size, bold=False):
    font_paths = [
        "/System/Library/Fonts/SFProText-Bold.otf" if bold else "/System/Library/Fonts/SFProText-Regular.otf",
        "/System/Library/Fonts/Helvetica.ttc",
        "/Library/Fonts/Arial.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf"
    ]
    for path in font_paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                continue
    return ImageFont.load_default()

font_title = get_font(28, bold=True)
font_subtitle = get_font(18, bold=True)
font_body = get_font(14, bold=False)
font_small = get_font(12, bold=False)
font_badge = get_font(13, bold=True)
font_btn = get_font(14, bold=True)

def draw_header(draw):
    draw.rectangle([0, 0, WIDTH, 54], fill=PRIMARY)
    draw.text((56, 17), "art of Comic Books", fill=WHITE, font=get_font(16, bold=True))
    nav_items = [("Ongoing", 540), ("Archive", 620), ("Register", 710)]
    for name, x in nav_items:
        if name == "Register":
            draw.rounded_rectangle([x - 12, 12, x + 68, 42], radius=4, fill=SECONDARY)
            draw.text((x, 18), name, fill=WHITE, font=font_btn)
        else:
            draw.text((x, 18), name, fill=WHITE, font=get_font(14, bold=False))

def create_base():
    img = Image.new("RGB", (WIDTH, HEIGHT), WHITE)
    draw = ImageDraw.Draw(img)
    draw_header(draw)
    logo_path = os.path.join(IMG_DIR, "logo.png")
    if os.path.exists(logo_path):
        try:
            logo_img = Image.open(logo_path).convert("RGBA")
            logo_img = logo_img.resize((24, 24), Image.Resampling.LANCZOS)
            img.paste(logo_img, (24, 15), logo_img)
        except Exception:
            pass
    return img, draw

frames = []

# --- SLIDE 1: Hero Showcase ---
slide1, d1 = create_base()
main_img_path = os.path.join(IMG_DIR, "main.jpeg")
if os.path.exists(main_img_path):
    main_img = Image.open(main_img_path).convert("RGB")
    main_img = ImageOps.fit(main_img, (WIDTH, HEIGHT - 54), Image.Resampling.LANCZOS)
    overlay = Image.new("RGBA", (WIDTH, HEIGHT - 54), (250, 81, 30, 45))
    main_img = Image.alpha_composite(main_img.convert("RGBA"), overlay).convert("RGB")
    slide1.paste(main_img, (0, 54))

hero_card = Image.new("RGBA", (580, 200), (46, 76, 109, 210))
slide1.paste(hero_card, (130, 160), hero_card)
d1_card = ImageDraw.Draw(slide1)
d1_card.text((160, 185), "Welcome!", fill=WHITE, font=get_font(32, bold=True))
d1_card.text((160, 235), "Millions of completed or ongoing comic book", fill=WHITE, font=get_font(18, bold=False))
d1_card.text((160, 262), "series and new friends to discover.", fill=WHITE, font=get_font(18, bold=False))
d1_card.text((160, 290), "Start exploring now!", fill=(255, 215, 0), font=get_font(18, bold=True))
d1_card.rounded_rectangle([160, 320, 290, 350], radius=4, fill=SECONDARY)
d1_card.text((176, 326), "Discover Now", fill=WHITE, font=font_btn)
d1_card.rounded_rectangle([30, 70, 160, 95], radius=12, fill=PRIMARY)
d1_card.text((45, 75), "★ HERO SHOWCASE", fill=WHITE, font=font_small)
frames.append(slide1)

# --- SLIDE 2: How It Works & Features ---
slide2, d2 = create_base()
d2.rectangle([0, 54, WIDTH, HEIGHT], fill=(248, 250, 252))
d2.rounded_rectangle([30, 70, 150, 95], radius=12, fill=PRIMARY)
d2.text((45, 75), "★ HOW IT WORKS", fill=WHITE, font=font_small)
d2.text((320, 75), "How it works?", fill=DARK_TEXT, font=font_title)
d2.text((220, 115), "Start discovering your favorite comic book series in 3 simple steps!", fill=MUTED_TEXT, font=font_body)

steps = [
    ("1. Register", "Create your account in seconds", (220, 235, 245)),
    ("2. Choose Plan", "Select Starter, Reader or Collector", (245, 235, 245)),
    ("3. Enjoy Reading", "Immerse yourself into stories", (230, 245, 240))
]
for i, (title, desc, bg_color) in enumerate(steps):
    x = 60 + i * 250
    y = 150
    d2.rounded_rectangle([x, y, x + 220, y + 140], radius=8, fill=WHITE, outline=SECONDARY, width=2)
    d2.rounded_rectangle([x + 10, y + 15, x + 210, y + 55], radius=6, fill=bg_color)
    d2.text((x + 25, y + 25), title, fill=DARK_BLUE, font=font_subtitle)
    d2.text((x + 15, y + 80), desc, fill=MUTED_TEXT, font=font_small)

d2.rounded_rectangle([60, 310, WIDTH - 60, 470], radius=8, fill=LIGHT_BG)
d2.text((85, 335), "Stay instantly updated on new series releases!", fill=DARK_BLUE, font=get_font(20, bold=True))
d2.text((85, 370), "Join our growing community of comic enthusiasts! Subscribe to our newsletter to get", fill=MUTED_TEXT, font=font_body)
d2.text((85, 395), "exclusive sneak peeks and release dates delivered straight to your inbox.", fill=MUTED_TEXT, font=font_body)
d2.rounded_rectangle([85, 425, 215, 455], radius=4, fill=SECONDARY)
d2.text((105, 432), "View Features", fill=WHITE, font=font_btn)

sec_path = os.path.join(IMG_DIR, "secondary.jpg")
if os.path.exists(sec_path):
    sec_img = Image.open(sec_path).convert("RGB")
    sec_img = ImageOps.fit(sec_img, (180, 140), Image.Resampling.LANCZOS)
    slide2.paste(sec_img, (WIDTH - 250, 320))
frames.append(slide2)

# --- SLIDE 3: Subscription Plans ---
slide3, d3 = create_base()
d3.rectangle([0, 54, WIDTH, HEIGHT], fill=(245, 247, 250))
d3.rounded_rectangle([30, 70, 160, 95], radius=12, fill=PRIMARY)
d3.text((45, 75), "★ PRICING PLANS", fill=WHITE, font=font_small)
d3.text((280, 72), "Become a Premium Member", fill=DARK_TEXT, font=font_title)

plans = [
    ("Starter", "$0/month", ["Rotating free collection", "Ad-supported reading", "Standard resolution", "1 screen at a time"], False),
    ("Reader", "$9.99/month", ["Unlimited comic library", "Ad-free experience", "HD quality artwork", "Download 50 issues", "2 screens at once"], True),
    ("Collector", "$19.99/month", ["Unlimited comic library", "4K Ultra HD artwork", "Unlimited downloads", "Day-one new releases", "4 screens at once"], False)
]

for i, (pname, pprice, feats, is_featured) in enumerate(plans):
    x = 55 + i * 250
    y = 120
    card_h = 280
    if is_featured:
        d3.rounded_rectangle([x - 5, y - 10, x + 235, y + card_h + 10], radius=8, fill=SECONDARY)
        d3.rounded_rectangle([x + 40, y - 5, x + 190, y + 18], radius=4, fill=WHITE)
        d3.text((x + 55, y - 2), "RECOMMENDED", fill=PRIMARY, font=font_badge)
        d3.text((x + 75, y + 25), pname, fill=WHITE, font=get_font(22, bold=True))
        d3.text((x + 60, y + 55), pprice, fill=(255, 255, 210), font=get_font(18, bold=True))
        for idx, feat in enumerate(feats):
            d3.text((x + 20, y + 90 + idx * 25), f"✓ {feat}", fill=WHITE, font=font_small)
        d3.rounded_rectangle([x + 30, y + card_h - 45, x + 200, y + card_h - 15], radius=4, fill=PRIMARY)
        d3.text((x + 65, y + card_h - 38), "Choose Plan", fill=WHITE, font=font_btn)
    else:
        d3.rounded_rectangle([x, y, x + 230, y + card_h], radius=8, fill=WHITE, outline=(220, 225, 230), width=1)
        d3.text((x + 75, y + 20), pname, fill=DARK_TEXT, font=get_font(22, bold=True))
        d3.text((x + 65, y + 50), pprice, fill=PRIMARY, font=get_font(18, bold=True))
        for idx, feat in enumerate(feats):
            d3.text((x + 20, y + 90 + idx * 25), f"• {feat}", fill=MUTED_TEXT, font=font_small)
        d3.rounded_rectangle([x + 30, y + card_h - 45, x + 200, y + card_h - 15], radius=4, fill=PRIMARY)
        d3.text((x + 65, y + card_h - 38), "Choose Plan", fill=WHITE, font=font_btn)

d3.rectangle([0, 425, WIDTH, 495], fill=PRIMARY)
counters = [("2,495+", "Comic Books"), ("93,502+", "Ratings"), ("12,856+", "Active Users")]
for i, (cval, clabel) in enumerate(counters):
    cx = 100 + i * 260
    d3.text((cx, 435), cval, fill=WHITE, font=get_font(20, bold=True))
    d3.text((cx + 10, 465), clabel, fill=(240, 220, 240), font=font_small)
frames.append(slide3)

# --- SLIDE 4: Comics Showcase ---
slide4, d4 = create_base()
d4.rectangle([0, 54, WIDTH, HEIGHT], fill=(245, 247, 250))
d4.rounded_rectangle([30, 70, 165, 95], radius=12, fill=PRIMARY)
d4.text((45, 75), "★ COMICS SHOWCASE", fill=WHITE, font=font_small)
d4.text((340, 72), "Featured Issues", fill=DARK_TEXT, font=font_title)

cards_data = [
    ("Silver Surfer", "silversurfer.jpeg", "A noble alien roaming the cosmos seeking redemption."),
    ("Ghost Rider", "ghostRider.jpeg", "A hellfire-fueled vigilante on a motorcycle punishing evil."),
    ("The Amazing Spider-Man", "venom.webp", "Balancing superhero battles with daily teenage struggles.")
]

for i, (c_title, c_img_name, c_desc) in enumerate(cards_data):
    cx = 45 + i * 255
    cy = 115
    cw = 240
    ch = 360
    d4.rounded_rectangle([cx, cy, cx + cw, cy + ch], radius=8, fill=WHITE, outline=(220, 225, 230), width=1)
    c_path = os.path.join(IMG_DIR, c_img_name)
    if os.path.exists(c_path):
        try:
            c_img = Image.open(c_path).convert("RGB")
            c_img = ImageOps.fit(c_img, (cw, 175), Image.Resampling.LANCZOS)
            slide4.paste(c_img, (cx, cy))
        except Exception:
            pass
    d4.text((cx + 15, cy + 188), c_title[:20], fill=DARK_TEXT, font=get_font(16, bold=True))
    words = c_desc.split()
    line1 = " ".join(words[:5])
    line2 = " ".join(words[5:])
    d4.text((cx + 15, cy + 218), line1, fill=MUTED_TEXT, font=font_small)
    d4.text((cx + 15, cy + 236), line2, fill=MUTED_TEXT, font=font_small)
    d4.rounded_rectangle([cx + 15, cy + 310, cx + 115, cy + 342], radius=4, fill=PRIMARY)
    d4.text((cx + 35, cy + 318), "Details", fill=WHITE, font=font_btn)
frames.append(slide4)

# --- SLIDE 5: Registration Portal ---
slide5, d5 = create_base()
d5.rectangle([0, 54, WIDTH, HEIGHT], fill=(245, 247, 250))
d5.rounded_rectangle([30, 70, 165, 95], radius=12, fill=PRIMARY)
d5.text((45, 75), "★ REGISTER PAGE", fill=WHITE, font=font_small)

fw = 420
fx = (WIDTH - fw) // 2
fy = 90
d5.rounded_rectangle([fx, fy, fx + fw, fy + 380], radius=8, fill=WHITE, outline=(210, 220, 230), width=1)
d5.text((fx + 100, fy + 20), "Create Your Account", fill=DARK_BLUE, font=get_font(22, bold=True))

form_fields = [
    ("First Name", "Peter"),
    ("Last Name", "Parker"),
    ("Email", "spidey@dailybugle.com"),
    ("Password", "••••••••••••")
]
for idx, (label, placeholder) in enumerate(form_fields):
    field_y = fy + 65 + idx * 58
    d5.text((fx + 30, field_y), label, fill=DARK_TEXT, font=get_font(12, bold=True))
    d5.rounded_rectangle([fx + 30, field_y + 18, fx + fw - 30, field_y + 48], radius=4, fill=(250, 252, 255), outline=(200, 210, 220))
    d5.text((fx + 40, field_y + 25), placeholder, fill=MUTED_TEXT, font=font_small)

cb_y = fy + 305
d5.ellipse([fx + 30, cb_y, fx + 46, cb_y + 16], fill=SECONDARY)
d5.text((fx + 34, cb_y + 1), "✓", fill=WHITE, font=font_small)
d5.text((fx + 55, cb_y + 1), "Agree to Terms & Conditions", fill=DARK_TEXT, font=font_small)
d5.rounded_rectangle([fx + 30, fy + 335, fx + fw - 30, fy + 368], radius=4, fill=PRIMARY)
d5.text((fx + 175, fy + 343), "Sign Up", fill=WHITE, font=font_btn)
frames.append(slide5)

# Save animated GIF
print(f"Generating animated GIF with {len(frames)} slides...")
frames[0].save(
    OUTPUT_GIF,
    save_all=True,
    append_images=frames[1:],
    duration=2200,
    loop=0,
    optimize=True
)

print(f"Preview GIF successfully saved to: {OUTPUT_GIF}")
print(f"File size: {os.path.getsize(OUTPUT_GIF):,} bytes")
