#!/usr/bin/env python3
"""
Downloads the 3 missing map-layout images (Ascent, Split, Sunset) into your
anti-strat-vault repo folder as minimap-ascent.png / minimap-split.png /
minimap-sunset.png, matching the existing minimap-<map>.png files already
in the repo.

Run this from inside your repo folder:
    cd path\\to\\anti-strat-vault
    python download_missing_minimaps.py

Safe to re-run — it skips any file that already exists.
"""
import os
import urllib.request

MAPS = [
    {
        "id": "ascent",
        "uuid": "7eaecc1b-4337-bbf6-6ab9-04b8f06b3319",
    },
    {
        "id": "split",
        "uuid": "d960549e-485c-e861-8d71-aa9d1aed12a2",
    },
    {
        "id": "sunset",
        "uuid": "92584fbe-486a-b1b2-9faa-39b0f486b498",
    },
]

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"


def download(url, dest):
    if os.path.exists(dest):
        print(f"  skip (already exists): {dest}")
        return
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=20) as resp:
        data = resp.read()
    with open(dest, "wb") as f:
        f.write(data)
    print(f"  saved: {dest} ({len(data):,} bytes)")


def main():
    print(f"Working in: {os.getcwd()}")
    ok, failed = 0, []
    for m in MAPS:
        url = f"https://media.valorant-api.com/maps/{m['uuid']}/displayicon.png"
        dest = f"minimap-{m['id']}.png"
        print(f"{m['id']}:")
        try:
            download(url, dest)
            ok += 1
        except Exception as e:
            print(f"  FAILED: {e}")
            failed.append(m["id"])

    print()
    print(f"Done. {ok}/{len(MAPS)} map layouts present.")
    if failed:
        print(f"Failed: {', '.join(failed)} — check your internet connection and re-run.")


if __name__ == "__main__":
    main()
