# paper mistral hires table3 patch

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_mistral-hires-table3-patch_20260514T223738_result.json`
- **Structured JSON:** [`2431547c2d76c4acd01a.json`](../../sessions/24/2431547c2d76c4acd01a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已存在于 `projects/ratekv/docs/paper/analysis.tex`。检查后发现 4 处修改已全部到位：

1. **Table 3 (line 43)**: Mistral 已是 `0.24` / `0.41`，`$^\dagger$` 在此文件中表示 hires profiling（见 line 33 caption），保留正确。
2. **Line 28**: 已拆分为 `Mistral-7B-v0.3 ($t_1/t_5{=}0.41$) and Gemma-2-9B ($t_1/t_5{=}0.18$)`。
3. **Line 72 Diagnostic**: 已是 `Mistral (0.24, $t_1/t_5{=}0.41$)`。
4. **Flat 类别 (line 72)**: 已是 `(concentration $\lesssim 0.50$)`，无 "low t1/t5" 限定。

文件无需修改，所有值已是最新 hires 数据。

---
