CIVO Detector Implementation Summary (2026-05-17)

Files modified:
- dreamer.py: CIVODetector class (L29-79), instantiation (L367-370), integration (L390-399)
- configs.yaml: civo_detector=True, civo_ve_threshold=0.49, civo_delta_threshold=0.1

Formula: r = abs(V - E) / max(E, 1.0)
Conditions: magnitude r≥0.49, velocity Δr>0.1, acceleration (positive), eval decline ≥2/3 of last 3 checkpoints
Output: [CIVO DETECTOR] WARNING step=... CIVO pattern detected!

Disable: --civo_detector False (zero overhead)
Does not affect already-running experiments.