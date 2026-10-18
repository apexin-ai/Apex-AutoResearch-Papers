# fix figure2 v4 latex ref

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_figure2_v4_latex_ref_20260528T174620_result.json`
- **Structured JSON:** [`ee969e452a75408575bc.json`](../../sessions/ee/ee969e452a75408575bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`method.tex:19` already correctly references `fig_architecture_v4.pdf`. The log (from 15:56) is from a prior compilation before the fix was made.

The two `background.tex` files referencing the old `fig_architecture.pdf` are **not included** in the compilation chain (no `\input{background}` or `\input{sections/background}` anywhere). They're dead files.

**Summary:**
- `method.tex:19` — already points to `fig_architecture_v4.pdf` ✓
- `background.tex:17` and `sections/background.tex:17` — reference old version but are **not compiled** (not `\input`'d by any file)
- The `main.log` showing v2 is stale (compiled before the method.tex update)

No changes needed. Recompiling the paper will produce the correct output with v4. If you want, I can also update the two orphan `background.tex` files for consistency, but they don't affect the build.

---
