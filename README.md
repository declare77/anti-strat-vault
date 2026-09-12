# Anti-Strat Vault

A note-taking app for Valorant esports coaches to organize anti-strat notes on enemy teams, map by map, side by side (Attack/Defense).

- Pure static site — no server, no database, no monthly cost.
- Everything is saved in the browser's local storage on whatever device you're using it on.
- Use the **Export** button (bottom of the sidebar) to download a backup file, and **Import** to load it on another device or browser.

## Hosting

This is deployed as a free static site on GitHub Pages. To update it after Claude (or anyone) makes changes to `index.html`, `splash/`, or `minimaps/`, just commit and push to the `main` branch — Pages redeploys automatically within a minute or two.

## Local preview

No build step needed. From this folder, run:

```
python3 -m http.server 8000
```

then open `http://localhost:8000/` in a browser.
