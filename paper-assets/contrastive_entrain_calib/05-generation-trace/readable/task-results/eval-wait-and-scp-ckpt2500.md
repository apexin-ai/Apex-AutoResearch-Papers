# eval wait and scp ckpt2500

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_wait-and-scp-ckpt2500_20260522T115050_result.json`
- **Structured JSON:** [`0f8a44415c5a940ce784.json`](../../sessions/0f/0f8a44415c5a940ce784.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 已成功启动，正在对 362 个 eval pairs 进行推理。模型和 LoRA adapter 都已加载。

**当前状态汇总：**

| 项目 | 状态 |
|------|------|
| **ckpt-2500** | ❌ 训练在 step 2500 保存时因根分区磁盘满崩溃，权重丢失 |
| **ckpt-2000** | ✅ 完整，已 SCP 到 28034 |
| **eval ckpt-2000** | 🔄 已在 28034 GPU1 启动 (exp-004-s2-eval-ckpt2000) |
| **ckpt-3000** | ❌ 训练已终止，不会产出 |

**需要你决定的事项：**
1. **29046 根分区磁盘满**（30G 用了 28G），训练脚本把 checkpoint 写到了 `/root/contrastive_entrain_calib/outputs/`（根分区）而非 `/root/autodl-tmp/`（数据盘，194G 空闲）。需要修改输出路径并重启训练才能拿到 ckpt-2500+。
2. 根分区主要占用：`.cache` 5.9G、`contrastive_entrain_calib` 9.9G（含 ckpt-2000 约 700MB）、`tbab_multi_turn` 2.0G、`mvp_v2` 1.5G、`/tmp` 1.7G。

---
