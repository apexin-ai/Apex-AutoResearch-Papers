# ops step curve lora only evals

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_step_curve_lora_only_evals_20260526T120519_result.json`
- **Structured JSON:** [`78d89d0e885a6d5b1d2b.json`](../../sessions/78/78d89d0e885a6d5b1d2b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

让我换个策略。直接在本机用 `scp -3` 中继传输，利用 SSH config alias。先传 s0 的 best (step 24k)。

不过先让我评估一下：是否值得花时间传 3 个 checkpoints（21.6GB），还是只传 s0 best（7.2GB）获得 24k vs 30k 对比就够？

先汇报现状：

## Checkpoint 盘点结果

**LoRA baseline checkpoints（westd-45947）：**

| Seed | 可用 Steps | 说明 |
|------|-----------|------|
| s0 | **24000** (best), **30000** (final) | 30K 已 eval (TSR=51.5%, CAR=56.5%) |
| s1 | 30000, best | 未检查 best 具体 step |
| s2 | **8000**, **10000**, best=8000 | 训练似乎提前停止 |

**SDF checkpoints（westd-35807）：** 全部只剩 final + best，无有意义的中间点。

**SAVE_TOTAL_LIMIT=2 导致所有中间 checkpoints 被清理。**

## 可行方案

**方案 A（最小）：** 只 eval s0@24k (best)。SCP 7.2GB 到 35807，获得 24k vs 30k 对比——能回答"最后 6K 步是否 overfit"。

**方案 B（跨 seed 拼接）：** eval s0@24k + s2@8k + s2@10k。SCP 21.6GB，获得 4 点曲线 (8k, 10k, 24k, 30k)——但 s2 是不同 seed，拼接的曲线 methodologically 不太干净。

**方案 C（s1 补充）：** 检查 s1 的 best 在哪个 step，如果恰好是不同的 step，多一个数据点。

**替代方案 D（重新训练）：** 重新跑 LoRA baseline，设 `save_total_limit=10, save_steps=5000`，获得完整曲线。大约 8-10h。

你倾向哪个方案？我建议 **方案 B**：虽然混 seed，但对理解早期 dynamics 足够有信息量。同时可以用 WandB 的 training loss 曲线补充验证趋势。

---
