# ops wandb auth check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_wandb_auth_check_20260515T143228_result.json`
- **Structured JSON:** [`96649bc35dbd41269a86.json`](../../sessions/96/96649bc35dbd41269a86.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

**服务器有 W&B 认证，状态正常。**

| 检查项 | 结果 |
|--------|------|
| `~/.netrc` | **有认证** — `machine api.wandb.ai`, key = `wandb_v1_IWkdvG...` |
| `~/.bashrc` 中 WANDB 变量 | 无 |
| `~/.bash_profile` | 不存在 |
| `/etc/environment` | 无 WANDB 相关 |
| `~/.config/wandb/` | 不存在 |
| 项目 `.env` | 不存在 |
| `scripts/init_wandb.sh` | 存在 — 启动训练前 source 它，会检查 `.netrc` 或 `WANDB_API_KEY` 环境变量，设置 `WANDB_PROJECT=cost-verify-agent-rl` |

**认证位置**: `~/.netrc`，通过 `wandb login` 写入，包含有效的 API key。训练脚本 `init_wandb.sh` 会自动检测到它。

---
