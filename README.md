# 📚 art of Comic Books

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![FontAwesome](https://img.shields.io/badge/Font_Awesome-528DD7?style=for-the-badge&logo=font-awesome&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)

> **art of Comic Books** is a modern, responsive landing page and web application interface crafted for comic book enthusiasts, collectors, and casual readers to explore ongoing and archived comic series, choose subscription tiers, and join an active community.

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Technologies & Libraries Used](#-technologies--libraries-used)
- [Pages & Structure](#-pages--structure)
- [File & Directory Architecture](#-file--directory-architecture)
- [Design System & Responsive Architecture](#-design-system--responsive-architecture)
- [Getting Started & Local Setup](#-getting-started--local-setup)
- [Future Roadmap](#-future-roadmap)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🌟 Overview

**art of Comic Books** provides an engaging digital gateway into the comic book multiverse. The platform enables comic lovers to:
- Browse popular and legendary comic titles and superhero origins.
- Understand subscription options from free entry to ultra-high-definition collector memberships.
- Sign up effortlessly via a dedicated registration page.
- Experience a smooth, mobile-friendly interface with sleek animations and micro-interactions.

The project is built purely with **Vanilla Web Technologies** (semantic HTML5, modular CSS3, and lightweight Vanilla JavaScript) without bulky external frontend frameworks.

---

## ✨ Key Features

- **📱 Fully Responsive Design:** Fluid layout adapting seamlessly across mobile phones, tablets, laptops, and ultra-wide desktop monitors.
- **🍔 Interactive Mobile Navigation:** Toggleable responsive hamburger menu for touch devices powered by clean JavaScript.
- **🦸 Hero / Showcase Section:** Engaging full-width visual hero banner with a tinted gradient overlay and call-to-action typography.
- **🚀 "How It Works" 3-Step Guide:** Visual onboarding cards highlighting Registration, Plan Selection, and Comic Reading.
- **💎 Multi-Tier Subscription Plans:**
  - **Starter ($0/mo):** Ad-supported, rotating free collection, standard resolution, single-screen access.
  - **Reader ($9.99/mo - Recommended):** Ad-free, unlimited library, HD artwork, up to 50 offline issue downloads, dual-screen access.
  - **Collector ($19.99/mo):** Day-one new releases, 4K Ultra HD artwork, unlimited offline downloads, 4 simultaneous screens.
- **📊 Live Statistics & Counters:** Visual metric counters showcasing 2,495+ comic books, 93,500+ community ratings, and 12,800+ active users.
- **🃏 Comic Card Showcase:**
  - Interactive profile cards for legendary icons like *Silver Surfer*, *Ghost Rider*, and *The Amazing Spider-Man*.
  - Smooth lift-on-hover effects (`transform: translateY(-10px)`), shadow depth, and full-bleed cover imagery.
- **📝 User Registration Portal (`register.html`):**
  - Form validation structure containing inputs for first name, last name, email, password, gender dropdown, and terms agreement.
  - Custom circular-styled checkboxes and focused input states with accessibility in mind.
- **⏳ "Coming Soon" Route (`notyet.html`):**
  - A stylized placeholder page with full-screen thematic artwork for routes in development (Archive, Ongoing, Blog, Forum, Contact).
- **⬆️ Back-to-Top Navigation:** Sticky floating button with smooth scroll behavior for quick upward navigation.
- **🔗 Social Footers:** Styled brand links for Facebook, Twitter, and Instagram with brand-accurate hover transitions.

---

## 🛠️ Technologies & Libraries Used

| Technology / Resource | Usage & Purpose |
| :--- | :--- |
| **HTML5** | Clean, accessible, semantic structure (`<header>`, `<main>`, `<section>`, `<nav>`, `<footer>`). |
| **CSS3 (Modular Architecture)** | Custom Properties (variables), Flexbox, multi-column grid, keyframe transitions, and media queries. |
| **Vanilla JavaScript** | Zero-dependency DOM manipulation for mobile navigation toggling (`displayMenu`). |
| **Google Fonts** | Modern web typography: `Lato` (body text) and `Roboto` (navigation, titles). |
| **Font Awesome 5** | CDN icon pack (`v5.15.4`) for navigation icons, process indicators, and social logos. |

---

## 📄 Pages & Structure

1. **`index.html` (Landing Page):**
   - Fixed header with branding and navigation menu
   - Hero banner with welcoming heading and CTA
   - How It Works process section
   - Newsletter / Feature spotlight
   - Membership pricing cards with a recommended highlight badge
   - Platform stats and counter display
   - Featured comic books cards
   - Footer with sitemap links and social media channels

2. **`register.html` (Sign-Up Page):**
   - Clean, centered form layout
   - Input fields: First Name, Last Name, Email, Password
   - Gender selector dropdown (`<select>`)
   - Custom styled checkbox for Terms & Conditions agreement
   - Responsive submit button and unified navigation header/footer

3. **`notyet.html` (Under Construction / Placeholder):**
   - Minimalist full-screen graphic background (`img/notyet.jpeg`)
   - Shared persistent header for uninterrupted site navigation

---

## 📂 File & Directory Architecture

```text
artofComicBooks/
│
├── index.html              # Main landing page
├── register.html           # User account registration page
├── notyet.html             # Placeholder page for unfinished routes
├── README.md               # Project documentation
│
├── css/                    # Modular CSS stylesheets
│   ├── base.css            # Root resets, fluid rem scaling, and responsive grid helpers
│   ├── buttons.css         # Reusable button styles (primary, secondary, outline)
│   ├── forms.css           # Form controls, custom checkboxes, and input focus styles
│   ├── notyet.css          # Dedicated background styling for the placeholder view
│   └── styles.css          # Primary bundle importing partials, tokens, and page components
│
└── img/                    # Graphic assets and comic book imagery
    ├── logo.png            # Application logo & favicon
    ├── main.jpeg           # Hero background banner image
    ├── secondary.jpg       # Features section background image
    ├── ghostRider.jpeg     # Ghost Rider showcase card thumbnail
    ├── silversurfer.jpeg   # Silver Surfer showcase card thumbnail
    ├── venom.webp          # Spider-Man / Venom showcase card thumbnail
    └── notyet.jpeg         # Full-screen coming soon background artwork
```

---

## 🎨 Design System & Responsive Architecture

### Design Tokens (CSS Variables)
Colors and recurring styles are centralized in `styles.css`:
```css
:root {
    --primary-color: #b266b2;    /* Vibrant Purple / Magenta Accent */
    --secondary-color: #66b2b2;  /* Teal / Sea Green Secondary Accent */
    --premium-color: #66b2b2;    /* Highlight for Featured Tier */
}
```

### Fluid Typography & Viewport Scaling
By setting `html { font-size: 62.5%; }`, `1rem` conveniently maps to `10px`. Fluid typography scales progressively with device breakpoints:
- **Base (< 576px):** `font-size: 62.5%` (Mobile-optimized)
- **Small (≥ 576px):** `font-size: 68%`, Container width `540px`
- **Medium (≥ 768px):** `font-size: 72%`, Container width `720px`
- **Large (≥ 992px):** `font-size: 74%`, Container width `960px`
- **X-Large (≥ 1200px):** `font-size: 78%`, Container width `1140px`
- **XX-Large (≥ 1400px):** `font-size: 80%`, Container width `1320px`

---

## 🚀 Getting Started & Local Setup

Because this project is built entirely on native web standards, no compilation, npm packages, or build tools are required.

### Method 1: Direct Browser Launch
1. Clone or download this repository:
   ```bash
   git clone https://github.com/your-username/artofComicBooks.git
   ```
2. Navigate to the project directory:
   ```bash
   cd artofComicBooks
   ```
3. Open `index.html` in your favorite web browser (Chrome, Firefox, Safari, Edge).

### Method 2: VS Code Live Server (Recommended)
1. Open the project folder in **Visual Studio Code**.
2. Install the **Live Server** extension by *Ritwick Dey*.
3. Right-click `index.html` and select **"Open with Live Server"**.
4. The site will automatically open at `http://127.0.0.1:5500` with live reload enabled.

### Method 3: Lightweight Local Python Server
Run one of the following commands in the project root:
```bash
# Python 3
python3 -m http.server 8000
```
Then visit `http://localhost:8000` in your browser.

---

## 🔮 Future Roadmap

Potential future enhancements to extend this project:

- [ ] **Interactive Comic Reader:** In-browser panel-by-panel or double-page reader with keyboard navigation (arrow keys) and zoom capabilities.
- [ ] **Search & Categorization:** Dynamic search bar and filtering by publisher (Marvel, DC, Image, Dark Horse, Manga) or genre.
- [ ] **Dark Mode Toggle:** Native light/dark theme switch using CSS variables and `prefers-color-scheme`.
- [ ] **Authentication & Database Backend:** Connecting `register.html` to a REST API or Firebase/Supabase for user authentication and profile management.
- [ ] **My Library & Bookmarking:** Allowing users to save favorites and track reading progress using `localStorage` or user accounts.
- [ ] **Third-Party API Integration:** Dynamic comic issues and character data fetched via the Marvel Comics API or Comic Vine API.

---

## 🤝 Contributing

Contributions, suggestions, and feedback are always welcome!
1. **Fork** the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a **Pull Request**.

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for more information (or reference [MIT Open Source](https://opensource.org/licenses/MIT)).
