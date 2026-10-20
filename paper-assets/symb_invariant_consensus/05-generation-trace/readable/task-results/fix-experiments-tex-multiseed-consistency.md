# fix experiments tex multiseed consistency

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_experiments-tex-multiseed-consistency_20260523T001421_result.json`
- **Structured JSON:** [`0f6e930b0dde506171fd.json`](../../sessions/0f/0f6e930b0dde506171fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。

**Diff**: experiments.tex L57
```
- $\bar\Delta=-1.79\pm0.25$
+ $\bar\Delta=-1.24\pm0.86$
```

**附录 vs 主文对照（全部一致）**:

| 条件 | 附录 tab:multi-seed | experiments.tex（修复后） |
|------|-------------------|------------------------|
| Mistral-7B × PW (4s) | -2.38±1.12 | -2.38±1.12 ✓ |
| Qwen2.5-14B × FOLIO (4s) | -1.24±0.86 | -1.24±0.86 ✓ |
| Mistral-7B × FOLIO (3s) | +0.16±2.70 | "near-zero...mixed signs" ✓ |
| LLaMA-8B × FOLIO (3s) | -0.98±2.25 | "near-zero...mixed signs" ✓ |

编译成功，27 页，无错误。

---
