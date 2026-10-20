# wandb training trajectory loop4

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_wandb_training-trajectory-loop4_20260514T230459_result.json`
- **Structured JSON:** [`cb86a227425c875cff99.json`](../../sessions/cb/cb86a227425c875cff99.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/training_trajectory_loop4.md`。

核心结论：

**Step 100 出现了真实的 f1_reward 拐点**（0.016→0.093，5.8x），f1 和 ced 同步上升说明模型确实在学抽取而非纯 format hacking。但 eval 数据 (ckpt-20: 0.0077, ckpt-40: 0.0071) 表明训练 reward 尚未转化为实际抽取能力。

最大风险是 **training reward 与 eval F1 脱节**。ckpt-100 的 eval 是决定性验证点——如果 eval F1 > 0.15 说明拐点真实，< 0.05 则判定 reward hacking。

rel_f1 > 0.30 的概率 < 5%。建议优先 eval ckpt-100 和 ckpt-120。

---
