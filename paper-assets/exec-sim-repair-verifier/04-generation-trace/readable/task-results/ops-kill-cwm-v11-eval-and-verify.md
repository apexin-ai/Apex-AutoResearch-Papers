# ops kill cwm v11 eval and verify

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-cwm-v11-eval-and-verify_20260513T220556_result.json`
- **Structured JSON:** [`f289774fb809675d9ebc.json`](../../sessions/f2/f289774fb809675d9ebc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息收集完毕。

## 操作结果
- CWM v11 eval PID 180344: **已 kill**（SIGTERM 成功）
- Chain 脚本: **无**。无 crontab，无 chain 进程。两个 tmux session 存在但无自动重启逻辑：
  - `cwm_seed123`: CWM seed123 训练（看起来已挂起/崩溃，输出停在 data loading 后）
  - `repo-level-cwm-v12`: 空输出（对应 PID 181202 的 v12 训练）

## 全量 GPU 状态

### westd-48478 (4×5090)
| GPU | Memory Used | Util% | PID | 实验 |
|-----|------------|-------|-----|------|
| 0 | 0 / 32607 MiB | 0% | — | **空闲**（刚释放 CWM v11 eval） |
| 1 | 23261 / 32607 MiB | 95% | 181202 | `train_repo_cwm.py --seed 42 --no_wandb` → CWM v12 训练（tmux: `repo-level-cwm-v12`） |
| 2 | 0 / 32607 MiB | 0% | — | **空闲** |
| 3 | 0 / 32607 MiB | 0% | — | **空闲** |

### home-1x5090 (1×5090)
| GPU | Memory Used | Util% | PID | 实验 |
|-----|------------|-------|-----|------|
| 0 | 19879 / 32607 MiB | 91% | 3001112 | `train_repo_verifier.py --seed 123` → Verifier seed123 训练 |

## 备注
- `cwm_seed123` tmux session 的训练似乎已停滞（输出停在 data loading 阶段，GPU 0 已空闲）——可能需要检查是否崩溃
- westd 有 3 个 GPU 空闲（0/2/3），可安排新任务

---
