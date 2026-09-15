# 📚 art of Comic Books — Digital Comic Platform

<div align="center">

[![Live Demo](https://img.shields.io/badge/Live_Demo-artofcomicbooks.netlify.app-00C7B7?style=for-the-badge&logo=netlify&logoColor=white)](https://artofcomicbooks.netlify.app)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

<p align="center">
  <strong>A sleek, modern, and fully responsive web platform crafted for comic book enthusiasts, collectors, and readers worldwide.</strong>
</p>

[🌐 Visit Live Website](https://artofcomicbooks.netlify.app) • [✨ Key Features](#-key-features) • [🛠️ Tech Stack](#️-tech-stack) • [🚀 Getting Started](#-getting-started) • [📄 License](#-license)

---

</div>

## 📖 Overview

**art of Comic Books** is an immersive, modern landing page and web application interface designed to connect readers with the vast comic book multiverse. Whether discovering classic storylines, following ongoing releases, or joining a vibrant community of comic enthusiasts, the platform offers an intuitive, visually striking gateway.

Built entirely with **Vanilla Web Technologies** (semantic HTML5, modular CSS3, and lightweight JavaScript), the project emphasizes fast load speeds, fluid animations, and flawless responsiveness across all screen sizes.

🔗 **Live Deployment:** [https://artofcomicbooks.netlify.app](https://artofcomicbooks.netlify.app)

---

## ✨ Key Features

- **📱 Fully Responsive Design:** Fluid layouts optimized for mobile phones, tablets, laptops, and ultra-wide desktop monitors using responsive CSS grid and flexbox.
- **🍔 Interactive Mobile Navigation:** Seamless hamburger menu toggle for small screens powered by vanilla JavaScript.
- **🦸 High-Impact Hero Showcase:** Full-width hero banner with textured artwork, gradient overlays, and engaging call-to-action typography.
- **🚀 "How It Works" Onboarding:** Clear 3-step visual guide outlining Registration, Plan Selection, and Reading.
- **💎 Multi-Tier Membership Plans:**
  - **Free Tier:** Ad-supported access with standard resolution and rotating issues.
  - **Recommended Tier ($9.99/mo):** Ad-free HD reading, dual-device streaming, and offline downloads.
  - **Ultimate Tier ($19.99/mo):** 4K Ultra HD artwork, 4 simultaneous screens, day-one releases, and unlimited downloads.
- **📊 Real-Time Platform Statistics:** Metric counter counters displaying thousands of available issues, community ratings, and active members.
- **🃏 Character & Series Spotlight Cards:**
  - Interactive profile cards featuring comic legends such as *Ghost Rider*, *Silver Surfer*, and *The Amazing Spider-Man*.
  - Smooth hover transformations (`translateY`), dynamic drop shadows, and full-bleed cover imagery.
- **📝 User Registration Portal (`register.html`):** Clean sign-up page with responsive form inputs, gender selector, and custom circular agreement checkboxes.
- **⏳ Thematic Placeholder Route (`notyet.html`):** Atmospheric, full-screen coming soon page for routes under active development.
- **⚡ Pure Vanilla Web Tech:** Zero runtime framework dependencies for instantaneous page loads and optimal Core Web Vitals.

---

## 🛠️ Tech Stack

| Technology             | Purpose                                                                                |
| :--------------------- | :------------------------------------------------------------------------------------- |
| **HTML5**              | Clean semantic structure, accessibility (`aria-label`, meta viewport, SEO)           |
| **CSS3**               | Modular stylesheets, CSS custom variables (design tokens), Flexbox, and CSS Grid       |
| **Vanilla JavaScript** | Lightweight DOM manipulation for mobile navigation toggling                           |
| **Google Fonts**       | Typography using [Lato](https://fonts.google.com/specimen/Lato) and [Roboto](https://fonts.google.com/specimen/Roboto) |
| **Font Awesome**       | Scalable vector icons for navigation, feature indicators, ratings, and social links    |
| **Netlify**            | Continuous deployment and static site hosting                                          |

---

## 📁 Project Structure

```text
artofComicBooks/
├── css/
│   ├── base.css          # Resets, fluid rem scaling, and responsive grid system
│   ├── buttons.css       # Reusable button components (primary, secondary, outline)
│   ├── forms.css         # Form controls, custom checkboxes, and input focus states
│   ├── notyet.css        # Background styling for the placeholder route
│   └── styles.css        # Main stylesheet importing partials, tokens, and page styles
├── img/                  # High-resolution comic book artwork, logos, and banners
│   ├── logo.png
│   ├── main.jpeg
│   ├── secondary.jpeg
│   ├── secondary.jpg
│   ├── ghostRider.jpeg
│   ├── silversurfer.jpeg
│   ├── venom.webp
│   └── notyet.jpeg
├── index.html            # Main landing page
├── register.html         # User sign-up and registration page
├── notyet.html           # Under construction / placeholder page
├── LICENSE               # MIT License
└── README.md             # Project documentation
```

---

## 🚀 Getting Started

To run this project locally on your machine:

### 1. Clone the repository

```bash
git clone https://github.com/kucukagtas/artofComicBooks.git
```

### 2. Navigate to the project folder

```bash
cd artofComicBooks
```

### 3. Open in your browser

- Simply double-click `index.html` to open it in your default web browser.
- **Or** run a local development server (such as VS Code's **Live Server** extension or `npx serve`):

  ```bash
  npx serve .
  ```

---

## 🌐 Deployment

This project is deployed and hosted on **Netlify** with automated continuous integration directly connected to GitHub.

👉 **Live URL:** [https://artofcomicbooks.netlify.app](https://artofcomicbooks.netlify.app)

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
