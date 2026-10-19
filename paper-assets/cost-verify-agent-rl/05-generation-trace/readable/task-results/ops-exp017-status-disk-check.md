# ops exp017 status disk check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp017_status_disk_check_20260514T160632_result.json`
- **Structured JSON:** [`9cb6f91682abd9bd3670.json`](../../sessions/9c/9cb6f91682abd9bd3670.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个任务结果汇总：

**任务 1 — exp017 训练**: ✅ 已完成。PID 353947 已退出，3 epochs/462 steps 耗时 26 分钟，final train_loss=0.1434（末尾 step loss ~0.04，token_acc ~0.983）。最终 checkpoint 在 `/root/autodl-tmp/checkpoints/exp017_expert_sft/final/`（3.44GB）。

**任务 2 — 磁盘**: 146GB 可用（42% 使用），无清理需求。如需腾空间可删 exp015 (21G) + exp016 (21G) 共 42GB（旧失败实验）。exp008_sft 被软链引用，**勿删**。

**任务 3 — exp018**: ✅ 就绪。脚本 `scripts/run_exp018.sh` + config `RAGEN/config/_alfworld_exp018_sft_grpo.yaml` 已存在，`model_path` 正确指向 exp017 final，GPU=0,1 合规 C001。启动前需 `nvidia-smi` 确认 GPU 空闲 + alfworld 数据目录存在。

报告已写入 `artifacts/exp017_status_check.md`。

---
