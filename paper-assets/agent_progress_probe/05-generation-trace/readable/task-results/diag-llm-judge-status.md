# diag llm judge status

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_llm-judge-status_20260514T140547_result.json`
- **Structured JSON:** [`90ca1c5b5b9ea339f164.json`](../../sessions/90/90ca1c5b5b9ea339f164.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**baseline-llm-judge 已完成。**

结果（`results/llm_judge_full_zeroshot.json`）：

| Metric | Value |
|--------|-------|
| **macro_f1** | **0.6625** |
| accuracy | 0.6721 |
| precision_macro | 0.7062 |
| recall_macro | 0.7596 |
| f1_stagnation | 0.6055 |
| f1_progress | 0.7195 |

模型：`anthropic/claude-sonnet-4.6`，zero-shot，1824 个 windows 全部完成，0 次解析失败。

与 GRU Probe 对比：**macro_f1 差 0.2430**（0.6625 vs 0.9055），probe 大幅领先。

预估 API 花费：$11.66（~306 万 tokens）。

另外注意：当前服务器上正在运行 `fewshot_probe.py`（GPU 1，tmux session `openhands-fewshot-probe`）。

---
