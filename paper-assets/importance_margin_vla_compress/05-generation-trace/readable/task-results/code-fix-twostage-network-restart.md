# code fix twostage network restart

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_twostage_network_restart_20260516T042513_result.json`
- **Structured JSON:** [`210e9590fc88e4387bc5.json`](../../sessions/21/210e9590fc88e4387bc5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Final summary:

## 结果

| 项目 | 值 |
|------|-----|
| **新 PID** | 136367 (python) / 136351 (bash wrapper) |
| **训练状态** | Stage 1 正常运行，step 100/10000 |
| **速度** | 4.3 steps/sec |
| **margin_loss** | 0.2969 → 0.2770（正常下降） |
| **GPU 1 显存** | 3362 MiB / 97887 MiB |
| **修复内容** | 1) Kill 卡死进程 133659；2) 清理残留进程 135409；3) 添加 `network_turbo` + `WANDB_MODE=offline` 重启 |

注意：wandb 在 offline 模式运行，数据保存在 `/root/autodl-tmp/importance_margin_vla_compress/wandb/offline-run-20260516_122925-2t4p795u`，后续可用 `wandb sync` 上传。

---
