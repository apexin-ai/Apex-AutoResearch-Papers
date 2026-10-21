# diag gpu state check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gpu-state-check_20260516T035035_result.json`
- **Structured JSON:** [`4ba0c3ff4fed49232a52.json`](../../sessions/4b/4ba0c3ff4fed49232a52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### sweep-isr-b005-s42
| 项目 | 状态 |
|------|------|
| tmux session | **已退出**（ps 中无对应进程） |
| 训练进程 | **已完成** — 500/500 steps, EXIT_CODE=0 |
| 完成时间 | 2026-05-16 11:50 UTC |
| GPU | 无占用 |
| 最终指标 | prove_rate=0.888, mean_isr=0.577, parse_rate=1.0 |
| W&B | **未记录** — 日志中零 wandb 字符串，无 wandb/ 目录 |
| 输出目录 | `/root/autodl-tmp/outputs/sweep_isr_b005_s42/` — 完整模型 + checkpoint-500 |
| 启动时间 | 11:21 UTC（今天） |

### sweep-isr-b01-s45
| 项目 | 状态 |
|------|------|
| tmux session | **活跃** |
| 训练进程 | PID 604569, **正在运行** — step 178/500 (36%) |
| GPU | GPU 0, 79538 MiB, 92% util |
| W&B run name | `sweep-isr-b01-s45-r3`（命令行传入，但**日志无 wandb 初始化记录**） |
| W&B | **未记录** — 日志中零 wandb 字符串，无 wandb/ 目录 |
| 预计完成 | ~45 min（based on ~8s/step × 322 remaining steps） |
| 启动时间 | 11:21 UTC（今天） |

### 关键发现

1. **这两个是 D098 后重新提交的实验**（11:21 UTC 启动），不是孤儿进程。命令行包含 `--wandb_run` 和 `--wandb_project` 参数。

2. **但 W&B 仍然未生效。** 两个实验的日志中零 wandb 字符串，服务器上无 `wandb/` 目录。D098 修复可能没有完全解决问题——`--wandb_run` 和 `--wandb_project` 通过命令行传入，但 `train_grpo.py` 内部可能仍有逻辑跳过了 W&B 初始化（例如还有一个 `--no_wandb` 默认值为 True 的 argparse flag 未被覆盖）。

3. **GPU 1 空闲。** 之前 03:49 UTC 观测到双卡各 ~80GB 的状态已不存在。现在只有 GPU 0 被 b01-s45 占用。

### 结论

- **sweep-isr-b005-s42**: 已成功完成，registry 应更新为 `DONE(success)`。但无 W&B 数据，需要从本地 `reward_log.jsonl` 提取指标。
- **sweep-isr-b01-s45**: 正常训练中，registry 应更新为 `RUNNING`。预计 ~45 min 内完成。同样无 W&B。
- **D098 修复不完全**: W&B 仍未生效，需要排查 `train_grpo.py` 中 wandb 初始化的实际逻辑。不过当前 cron 没有误杀这些 session，训练本身正常推进。

---
