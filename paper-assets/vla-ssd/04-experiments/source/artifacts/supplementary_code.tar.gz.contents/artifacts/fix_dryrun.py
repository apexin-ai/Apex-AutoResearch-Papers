#!/usr/bin/env python3
SCRIPT_PATH = "/root/autodl-tmp/vla-ssd/scripts/libero_object_full_pipeline.py"
code = open(SCRIPT_PATH).read()

# Fix 1: Change dry-run to 2 tasks
code = code.replace(
    'nt = 1 if args.dry_run else len(TASKS)',
    'nt = 2 if args.dry_run else len(TASKS)'
)

# Fix 2: Add guard in run_classification for < 2 classes
old_cls = '    n_cls = int(labels.max()) + 1\n    results = {"chance": round(1.0 / n_cls, 4)}'
new_cls = '    n_cls = int(labels.max()) + 1\n    if n_cls < 2:\n        log("  Skipping: need >= 2 classes")\n        return {"chance": 1.0, "skipped": True}\n    results = {"chance": round(1.0 / n_cls, 4)}'
code = code.replace(old_cls, new_cls)

open(SCRIPT_PATH, 'w').write(code)
import ast; ast.parse(code)
print("FIX_OK")
