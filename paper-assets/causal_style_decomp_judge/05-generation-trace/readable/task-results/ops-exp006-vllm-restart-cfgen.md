# ops exp006 vllm restart cfgen

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp006_vllm_restart_cfgen_20260521T055327_result.json`
- **Structured JSON:** [`431155f1172b91a96464.json`](../../sessions/43/431155f1172b91a96464.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

稳定增长中（230/400）。

**产出汇总：**

| 项目 | 值 |
|------|-----|
| vLLM PID | **114900** (cuda:2, port 8002) |
| CF gen PID | **115974** |
| CF gen 进度 | **230/400** (剩余 170 条，预计 ~5-6 分钟完成) |
| 输入文件 | `data/scaled_formality_input.jsonl` (400 条) |
| 输出文件 | `data/counterfactuals_scaled_formality.jsonl` |

脚本内置 resume 逻辑（`load_processed_ids`），自动跳过已处理的 224 条，从断点恢复。当前正常推进中，无异常。

---
