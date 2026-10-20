# ops retrain checkpoint save

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_retrain_checkpoint_save_20260523T052430_result.json`
- **Structured JSON:** [`5c6cb6b8f7c30633c602.json`](../../sessions/5c/5c6cb6b8f7c30633c602.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**状态汇总：**

| 实验 | 当前 step | 进度 | 速度 |
|------|----------|------|------|
| vanilla_retrain_s0 | ~6222/50005 | 12% | 1.09 it/s |
| full_occ_retrain_s0 | ~6266/50005 | 13% | 1.09 it/s |

**Checkpoint 目录：** 两个目录下只有 `dataset_statistics.json`，尚无模型 checkpoint（首次保存在 step 10000）。

**关键结论：**
- **Step 5000：已错过。** save_freq=10000，训练已过 6200 步，无法追溯保存。
- **Step 10000：将自动保存。** 预计 ~58 分钟后到达。

**Step 5000 的补救方案：**

1. **接受损失** — 只用 step 10000 做梯度分析。OCC weight 指数衰减步数为 50000，step 10000 时 weight 仍有约 `0.01 * exp(-10000/50000) ≈ 0.0082`，OCC 梯度信号仍然有意义。

2. **重启训练 + 修改保存点** — 修改代码添加 `extra_save_steps=[5000, 10000]`，从头训练。代价：两个实验各损失 ~1.6 小时（6200 步）。

3. **折中：保存一个"近早期"checkpoint** — 修改代码添加比如 step 7000 或 7500 作为额外保存点，然后重启。同样损失 ~1.6 小时，但能拿到一个比 10000 更早的 checkpoint。

你怎么选？如果 step 5000 对审稿回复至关重要（需要精确到 5000），只能选方案 2/3 重启。如果 step 10000 能凑合用，等 ~1 小时即可。

---
