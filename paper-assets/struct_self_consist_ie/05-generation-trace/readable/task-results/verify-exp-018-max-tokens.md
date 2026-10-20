# verify exp 018 max tokens

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_exp_018_max_tokens_20260515T061147_result.json`
- **Structured JSON:** [`07fb6e1585961831a0cd.json`](../../sessions/07/07fb6e1585961831a0cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有证据已收集完毕。

## 确认结果

- **exp_018_llama_scierc_seed123**: max_tokens=**1024**
- **exp_018_llama_scierc_seed456**: max_tokens=**1024**

### 依据

| 证据 | 详情 |
|------|------|
| **代码默认值** | `run_mvp_pilot.py:57` → `--max_tokens` default=1024；`sampling.py:149,522` → `max_tokens: int = 1024` |
| **日志无覆盖** | 两个实验的日志均不包含 "max_tokens" 字符串，vLLM 日志仅记录了 `max_model_len=4096`，未见命令行覆盖 |
| **实际 token 分布一致** | seed123 最长=834 tokens，seed456 最长=823 tokens，无任何 sample 达到或接近 1024 截断边界（>=1000: 0个） |
| **对照组验证** | exp_012_rerun_1024（已知 max_tokens=1024）最长=1024（恰好 1 个被截断），top-10 分布 [1024, 986, 984, 976, ...]，说明 SciERC 数据上模型在 1024 以内自然终止是正常行为 |

**结论**：两个实验均使用 max_tokens=1024（代码默认值），且无输出被截断。

---
