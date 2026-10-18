# figure scatter concentration fix

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_scatter_concentration_fix_20260514T220428_result.json`
- **Structured JSON:** [`2ed978b9e27350de8be3.json`](../../sessions/2e/2ed978b9e27350de8be3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本和图都已经是最新状态：

**Concentration 值**（已是正确的 hires 值）：
- Gemma-2-9B: 0.223
- Mistral-7B-v0.3: 0.231
- Llama-3.1-8B: 0.575
- Qwen2.5-7B: 0.616
- Yi-1.5-9B: 0.714

**验证通过**：
- x 轴顺序：Gemma-2 (0.223) ≈ Mistral (0.231) < Llama (0.575) < Qwen (0.616) < Yi-1.5 (0.714) ✓
- Llama MCKP benefit = 0.019，接近 0 ✓
- 本地 PDF/PNG 与服务器文件大小一致（29836 / 125157 bytes），已同步 ✓

无需修改，所有值和图已经是正确的。

---
