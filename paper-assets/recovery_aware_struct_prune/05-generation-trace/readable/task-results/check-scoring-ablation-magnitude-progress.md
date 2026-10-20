# check scoring ablation magnitude progress

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_scoring_ablation_magnitude_progress_20260518T042555_result.json`
- **Structured JSON:** [`8322ee9ae3977e9902de.json`](../../sessions/83/8322ee9ae3977e9902de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**scoring_ablation_magnitude_20 状态：**

| 项目 | 状态 |
|------|------|
| **当前阶段** | Step 2: GSM8K eval（剪枝已完成） |
| **剪枝结果** | magnitude 模式，目标 20%，实际 18.99%，MLP 199/784 groups pruned，Attn 0 pruned |
| **评估进度** | **99/200** (49.5%) |
| **已运行时长** | 1h 35m |
| **当前 accuracy** | 0.0000（前 50 样本，模型几乎没产出正确答案） |
| **平均速度** | ~56.5s/sample |
| **剩余样本** | 101 个 |
| **预估剩余时间** | ~95 min（约 1h 35m） |
| **预估完成时间** | ~2026-05-18 13:30 UTC |

注意：acc=0.0000 且 eos_rate=2.00%、avg_len=4054，说明 magnitude pruning 20% 后模型基本丧失 GSM8K 推理能力，输出大量无效 token 且几乎不终止。这与 recovery-aware 方法形成对照。

---
