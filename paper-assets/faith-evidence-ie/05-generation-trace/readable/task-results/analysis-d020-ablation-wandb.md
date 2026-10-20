# analysis d020 ablation wandb

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d020_ablation_wandb_20260514T180226_result.json`
- **Structured JSON:** [`bc55af64e3d3b10ae2e7.json`](../../sessions/bc/bc55af64e3d3b10ae2e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。memory.md 已更新，新增 "D020 Ablation 训练曲线深度分析" 部分。

核心发现总结：

**分化点**：step 15-20。两个实验在 step 10 都 collapse，但只有 CED 实验在 step 20 恢复。

**因果链**：CED reward 提供与 F1 正交的 reward 维度 → 增加 reward variance（step 10: 0.070 vs 0.039）→ 维持 nonzero GRPO advantage → 梯度流不断 → 多样性恢复（step 20）→ 有效学习重新启动（step 30+）。

**双面性**：CED 在有 KL 约束时是 stabilizer，无 KL 时是 hacking target。论文需要同时讲这两面。

**论文 claim 强度**："CED 防止 GRPO collapse" 作为 empirical finding 足够强（干净 A/B 对比）。机制假说（reward variance）有 reward_std 数据支持但 n=1。建议 framing 为 dual role：task improvement + training stabilization。

---
