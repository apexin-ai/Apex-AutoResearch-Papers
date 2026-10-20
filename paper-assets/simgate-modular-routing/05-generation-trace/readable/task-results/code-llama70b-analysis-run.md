# code llama70b analysis run

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama70b-analysis-run_20260524T135758_result.json`
- **Structured JSON:** [`22e0a8e45b7c51a4faff.json`](../../sessions/22/22e0a8e45b7c51a4faff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果摘要：

**Llama-70B DAF = 101.0% [95.3, 107.5] → Hypothesis SUCCESS**

关键发现：
- 70B 模型展现了所有测试模型中最强的 death dominance（Δ death rate = 28.6pp）
- DAF > 100% 意味着 death avoidance 解释了超过 100% 的确定性 agent 优势——当双方都存活时，内部 agent 反而略好（delta_nd = −0.30）
- Label fraction 91.3%，其中 97.1% 偏好确定性 agent（67:2）
- 除 find-non-living-thing（零死亡 task）外，所有 task 都一致显示强 death dominance

Cross-model 排序：Llama-70B (101.0%) > Qwen-72B (92.4%) > Qwen-7B (90.4%) > Gemma-9B (89.7%) > Llama-8B (88.2%)。Death dominance 在更大模型上不仅保持而且增强。

---
