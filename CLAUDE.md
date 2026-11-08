# Corsinura

## Animation
Pick the lightest tool that does the job:
1. CSS transitions/keyframes for hovers, fades, slides, simple loops. No library.
2. Web Animations API (element.animate) for JS-triggered one-off animations. No library.
3. anime.js (v4) for timelines, staggers, SVG path drawing, scroll-linked effects.
   - Plain HTML pages: import from https://cdn.jsdelivr.net/npm/animejs@4.5.0/+esm
   - Projects with package.json: npm i animejs
4. Canvas/requestAnimationFrame for live data such as waveforms or EKG traces. Never animate DOM elements for this.

Always respect prefers-reduced-motion, and animate only transform and opacity for smooth 60fps.
