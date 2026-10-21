# analysis grpo rasp 25 qwen math

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_grpo_rasp_25_qwen_math_20260516T154226_result.json`
- **Structured JSON:** [`982608ab8c1c24766fab.json`](../../sessions/98/982608ab8c1c24766fab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。

## 实验结论：**success** — C2 hypothesis validated

**grpo_rasp_25_qwen_math** (Qwen2.5-Math-7B, RASP 25%, GRPO 100 steps) 确认了跨模型×跨稀疏度的 RASP collapse pattern：

| 指标 | 值 | 含义 |
|------|-----|------|
| collapse_onset | ≤ step 10 | frac_zero_std 初始即 0.575 |
| collapse_type | immediate_chronic | 无急性下坠，从头到尾 stuck |
| reward range | 0.111–0.225 | 无上升趋势，纯震荡 |
| entropy | 0.117→0.090 | 持续下降，多样性丧失 |
| 最终生成 | 纯重复循环 | "Alwyn's distance..." 无限重复 |

**对比 DeepSeek RASP 20%**（onset ~step 10, permanent collapse）：Qwen RASP 25% 呈现更严重的立即性 collapse（初始 frac_zero_std 更高），符合"更高稀疏度 → 更早/更严重 collapse"的预期。

---
