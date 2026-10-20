# tau fix: remove contamination_ratio dependency

**Date**: 2026-05-15
**File**: `training/pretrain_weighted.py` on westd-47453

## Problem

L278-279: `tau = 1.0 - contamination_ratio * 0.5` made tau directly depend on the known contamination ratio, contradicting the paper's Claim 3 ("unknown contamination proportion").

## Changes

### 1. `--tau` argument (L235-236)
```diff
-    parser.add_argument("--tau", type=float, default=None,
-                        help="Alpha_eff target threshold (adaptive). "
-                             "Defaults to 1 - contamination_ratio * 0.5")
+    parser.add_argument("--tau", type=float, default=0.8,
+                        help="Controls target effective human proportion (default 0.8)")
```

### 2. `--contamination_ratio` help text (L219-220)
```diff
-    parser.add_argument("--contamination_ratio", type=float, default=0.2,
-                        help="Expected contamination ratio (for adaptive tau)")
+    parser.add_argument("--contamination_ratio", type=float, default=0.2,
+                        help="Synthetic data proportion in mixture (data generation only)")
```

### 3. `main()` tau computation (L278-279) — deleted
```diff
-    if args.tau is None:
-        args.tau = 1.0 - args.contamination_ratio * 0.5
```

## Verification

- `contamination_ratio` no longer referenced in training logic (only in argparse definition and config_summary logging)
- `--tau` defaults to 0.8 (matches old value at contamination_ratio=0.4)
- `--help` output confirmed correct
- No running experiments affected (code already loaded in memory)
