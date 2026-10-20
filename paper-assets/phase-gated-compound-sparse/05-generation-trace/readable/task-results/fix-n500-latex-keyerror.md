# fix n500 latex keyerror

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_n500_latex_keyerror_20260515T044357_result.json`
- **Structured JSON:** [`d100b4bad627d99d8e25.json`](../../sessions/d1/d100b4bad627d99d8e25.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

无 traceback，输出正确。所有 importance 和 random 条件的表格行完整。

修复内容：
- **main() summary（行 581）**: `else:` → `elif "median_ii_diff_ci" in c:`，避免条件字典缺少该 key 时 KeyError
- **main() CSV（行 635）**: `if "error" in c:` → `if "error" in c or "median_ii_diff_ci" not in c:`，与 `latex_output` Table 1 的 guard 保持一致
- `latex_output()` 本身（行 438）已有 `"median_ii_diff_ci" not in c` guard，无需改动

---
