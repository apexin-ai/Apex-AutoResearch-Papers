# fix resubmit imm v2 conda

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_resubmit_imm_v2_conda_20260516T204132_result.json`
- **Structured JSON:** [`5e075c03847ee5945b30.json`](../../sessions/5e/5e075c03847ee5945b30.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 产出汇总

| 项目 | 状态 |
|------|------|
| **旧 session 清理** | 已清理（共清理 3 次，原始 + 两次重试） |
| **训练启动** | 成功。Stage 1 已在运行：step 150/10000, margin_loss=0.2799, sps=5.5 |
| **GPU 0 显存** | 3445 MiB，正常 |
| **libero_goal eval** | 没有在运行。无 eval 进程，无相关 tmux session |

**修复过程中遇到的 3 个问题：**
1. `--checkpoint` 参数不存在 → 去掉，checkpoint 路径已在 config yaml 中配置（`twostage.baseline_checkpoint`）
2. 网络不通（`Network is unreachable`）→ 加了 `source /etc/network_turbo` + SSL 证书环境变量
3. wandb 未登录 → 设置 `WANDB_MODE=offline`

---
