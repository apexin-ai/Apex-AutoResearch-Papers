# code deploy metrics fix start v7 2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_deploy-metrics-fix-start-v7_2_20260515T191834_result.json`
- **Structured JSON:** [`0d55d33a77d784964cdc.json`](../../sessions/0d/0d55d33a77d784964cdc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**metrics.py 修复**: 已在 `compute_empirical_lipschitz()` 中添加 `was_training = acis_module.training` 保存状态，函数末尾 `if was_training: acis_module.train()` 恢复。语法验证通过。

**v7.1**: 已终止（原 PID 53510）。

**v7.2 启动成功**:
- 主进程 PID: **54978**（cuda:0）
- tmux session: `mvp_imm_anchor_v7_2`
- 配置: `configs/imm_anchor_v7_1.yaml`（lambda=0.20, delta=0.30）
- 训练已开始: `step=0/30000, loss=0.2770, margin_loss=0.2976, grad=1.60`
- v7（cuda:1, PID 41303）不受影响，继续运行

---
