# ssh check floor 0p3 0p5 progress

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_floor_0p3_0p5_progress_20260523T101329_result.json`
- **Structured JSON:** [`545bb790dc7cc6ce6d0b.json`](../../sessions/54/545bb790dc7cc6ce6d0b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

## floor=0.3 pipeline (PID 120742, GPU 0)

| 步骤 | 状态 |
|------|------|
| ① Prune | ✅ 完成 (15:51) |
| ② SFT (2ep) | ✅ 完成 (16:21) |
| ③ GRPO (100 steps) | ✅ 完成 (17:48), checkpoint-100 已保存 |
| ④ GSM8K eval | **进行中** — 247/1319 (18.7%), 均速 ~2.8s/it |

200 样本时中间 acc = **70.5%**。按当前速度剩余 1072 条约 50 分钟，预计 **~19:10 CST** 完成。

## floor=0.5 pipeline (PID 120474, GPU 3)

| 步骤 | 状态 |
|------|------|
| ① Prune | ✅ 完成 (17:23) |
| ② SFT (2ep) | ✅ 完成 (17:54) |
| ③ GRPO (100 steps) | **进行中** — 79/100 (79%), ~12.5s/step |

剩余 21 steps 约 4.5 分钟，GRPO 约 **~18:19 CST** 结束。之后还有 GSM8K eval (~1319 条, ~70min)，整个 pipeline 预计 **~19:30 CST** 完成。

## 资源

- GPU 0: 92% util, 29.6/97.9 GB 显存 (eval 推理中)
- GPU 3: 90% util, 56.1/97.9 GB 显存 (GRPO 训练中)
- 磁盘: 542G/650G used (84%), 109G 可用，充足

---
