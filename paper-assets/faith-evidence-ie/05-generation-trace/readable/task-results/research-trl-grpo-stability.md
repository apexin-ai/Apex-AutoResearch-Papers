# research trl grpo stability

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_trl-grpo-stability_20260514T102228_result.json`
- **Structured JSON:** [`7b46e3a84db73c7033c4.json`](../../sessions/7b/7b46e3a84db73c7033c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已完成并注册。核心结论：

**clip_ratio=0.0 是正常行为** — `num_iterations=1`（默认值）下是纯 on-policy，ratio 恒为 1.0，clipping 永远不触发。同时 `beta=0.0`（默认）意味着也没有 KL 惩罚。**你的 GRPO 训练目前没有任何显式 policy drift 约束。**

**推荐第一轮修复**（最小改动）：
1. `mask_truncated_completions=True` — 40% 截断率是最大噪声源
2. `beta=0.04` — 启用 KL 惩罚，直接约束策略偏移
3. `max_grad_norm=0.1` — 梯度安全网

如果仍不稳定，第二轮加 `num_iterations=2` + `epsilon_high=0.28`（DAPO 非对称 clipping）。

---
