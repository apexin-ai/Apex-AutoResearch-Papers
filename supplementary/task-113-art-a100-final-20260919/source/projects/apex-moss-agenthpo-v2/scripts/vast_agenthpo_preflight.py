#!/usr/bin/env python3
"""Read-only Vast.ai offer selector for AgentHPOBench qualification.

This command never creates or destroys an instance.  It requires no API key for
the public offer list; ``VAST_API_KEY`` is intentionally not read until a
future, separately reviewed create command is implemented.
"""

from __future__ import annotations

import argparse
import json
import urllib.request
from typing import Any


def fetch_offers() -> list[dict[str, Any]]:
    request = urllib.request.Request(
        "https://console.vast.ai/api/v0/bundles/",
        headers={"Accept": "application/json", "User-Agent": "moss-agenthpo-preflight/1"},
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        payload = json.load(response)
    offers = payload.get("offers")
    if not isinstance(offers, list):
        raise RuntimeError("Vast offer response has no offers list")
    return [offer for offer in offers if isinstance(offer, dict)]


def select_offers(
    offers: list[dict[str, Any]],
    *,
    gpu: str,
    min_vram_gb: float,
    min_ram_gb: float,
    min_disk_gb: float,
    max_dph: float | None,
) -> list[dict[str, Any]]:
    needle = gpu.lower()

    def number(offer: dict[str, Any], key: str) -> float:
        try:
            return float(offer.get(key, 0.0))
        except (TypeError, ValueError):
            return 0.0

    selected = []
    for offer in offers:
        name = str(offer.get("gpu_name", ""))
        if needle not in name.lower():
            continue
        if number(offer, "gpu_ram") < min_vram_gb * 1024:
            continue
        if number(offer, "cpu_ram") < min_ram_gb * 1024:
            continue
        if number(offer, "disk_space") < min_disk_gb:
            continue
        price = number(offer, "dph_total")
        if max_dph is not None and price > max_dph:
            continue
        selected.append(offer)
    return sorted(
        selected,
        key=lambda offer: (
            float(offer.get("dph_total", 1e9) or 1e9),
            -float(offer.get("reliability", 0.0) or 0.0),
        ),
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--gpu", default="H100")
    parser.add_argument("--min-vram-gb", type=float, default=80.0)
    parser.add_argument("--min-ram-gb", type=float, default=64.0)
    parser.add_argument("--min-disk-gb", type=float, default=300.0)
    parser.add_argument("--max-dph", type=float)
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()
    offers = select_offers(
        fetch_offers(),
        gpu=args.gpu,
        min_vram_gb=args.min_vram_gb,
        min_ram_gb=args.min_ram_gb,
        min_disk_gb=args.min_disk_gb,
        max_dph=args.max_dph,
    )
    fields = (
        "id",
        "gpu_name",
        "gpu_ram",
        "cpu_cores_effective",
        "cpu_ram",
        "disk_space",
        "dph_total",
        "geolocation",
        "reliability",
    )
    print(json.dumps([{key: offer.get(key) for key in fields} for offer in offers[: args.limit]], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
