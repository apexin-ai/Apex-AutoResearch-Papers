# ssh verify watch scripts

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify-watch-scripts_20260521T181016_result.json`
- **Structured JSON:** [`61a81a7739d60b02a45a.json`](../../sessions/61/61a81a7739d60b02a45a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the report:

---

## 检查报告

### 1. Qwen s456 (GPU 3) — watch 自动触发 eval？ ❌

**没有 watch 脚本在运行。** 磁盘上存在 `watch_qwen_train_then_eval.sh`（同时监控 s123 和 s456），但当前没有对应进程。训练完成后不会自动触发 eval。

### 2. Qwen s123 (GPU 0) — watch 自动触发 eval？ ❌

同上。`watch_qwen_train_then_eval.sh` 未运行。

**额外注意**：该 watcher 的默认 batch_size 是 `${1:-1}`（即 1），它调用的是 `run_qwen_cwm_s123_eval.sh` / `run_qwen_cwm_s456_eval.sh`（不是 `eval_qwen_cwm_*.sh`）。如果后续要启动 watcher，需传参 `bash watch_qwen_train_then_eval.sh 4` 确保 batch=4。

### 3. DS s123 (GPU 2) — PID 817 ✅

PID 817 确认存活：`bash watch_s123_eval_then_resume.sh`

该脚本的逻辑：
- Phase 1: 等 eval PID 978461 退出
- Phase 2: `GPU=2 bash resume_deepseek_s123_v2.sh` 恢复训练
- Phase 3: 训练成功后调 `bash eval_deepseek_cwm_s123_v2.sh` 做最终 eval

### 4. Eval 脚本参数验证

#### `eval_qwen_cwm_s123.sh`
| 项目 | 要求 | 实际 | 状态 |
|------|------|------|------|
| checkpoint sort | awk -F'checkpoint-' ... sort -n | `awk -F'checkpoint-' '{print $NF, $0}' \| sort -n \| tail -1 \| cut -d' ' -f2-` | ✅ |
| CUDA_VISIBLE_DEVICES | 0 | `CUDA_VISIBLE_DEVICES=0` | ✅ |
| batch_size | 4 | `--batch_size 4` | ✅ |
| checkpoint dir | — | `/root/autodl-tmp/checkpoints_repo_cwm_8b_s123` | ✅ |

#### `eval_qwen_cwm_s456.sh`
| 项目 | 要求 | 实际 | 状态 |
|------|------|------|------|
| checkpoint sort | awk -F'checkpoint-' ... sort -n | 同上 | ✅ |
| CUDA_VISIBLE_DEVICES | 3 | `CUDA_VISIBLE_DEVICES=3` | ✅ |
| batch_size | 4 | `--batch_size 4` | ✅ |
| checkpoint dir | — | `/root/autodl-tmp/checkpoints_repo_cwm_8b_s456` | ✅ |

#### `eval_deepseek_cwm_s123_v2.sh`
| 项目 | 要求 | 实际 | 状态 |
|------|------|------|------|
| checkpoint sort | awk -F'checkpoint-' ... sort -n | 同上 | ✅ |
| CUDA_VISIBLE_DEVICES | 2 | `CUDA_VISIBLE_DEVICES=2` | ✅ |
| batch_size | 1 (默认) | `--batch_size 4` | ❌ |
| checkpoint dir | `checkpoints_deepseek_cwm_repo_s123_v2/` | `/root/autodl-tmp/checkpoints_deepseek_cwm_repo_s123_v2` (v2) | ✅ |

**❌ DS s123 eval 的 batch_size 错误**：脚本写的是 `--batch_size 4`，要求是 DS 用默认 batch=1。

### 5. 进程存活确认 ✅

| PID | 运行时间 | 任务 |
|-----|----------|------|
| 4271 | 20h31m | Qwen s123 train (GPU 0) |
| 4561 | 20h30m | Qwen s456 train (GPU 1→实际用 `--device cuda:0` 配合 CVD) |
| 28200 | 13h46m | DS s123 train v2 (GPU 2) |
| 63490 | 4h23m | DS s456 eval v2 (GPU 1, `--batch_size 4`) |

全部存活。

---

**总结：2 个问题需处理**
1. ❌ Qwen s123/s456 没有 watch 脚本在跑——训练完成后不会自动触发 eval
2. ❌ `eval_deepseek_cwm_s123_v2.sh` 的 `--batch_size 4` 应改为去掉该参数或改为 1

---
