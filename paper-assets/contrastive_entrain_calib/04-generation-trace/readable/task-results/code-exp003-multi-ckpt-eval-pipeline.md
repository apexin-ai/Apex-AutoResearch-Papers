# code exp003 multi ckpt eval pipeline

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp003-multi-ckpt-eval-pipeline_20260520T124658_result.json`
- **Structured JSON:** [`6e71728e9c162365b551.json`](../../sessions/6e/6e71728e9c162365b551.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报如下：

---

### SCP 状态
3 个 checkpoint 从 westd-29046 成功传输到 westd-28034：
| Checkpoint | 大小 | 路径 |
|---|---|---|
| checkpoint-1000 | 718MB | `/root/autodl-tmp/checkpoints/exp003/checkpoint-1000` |
| checkpoint-2000 | 718MB | `/root/autodl-tmp/checkpoints/exp003/checkpoint-2000` |
| checkpoint-3000 | 718MB | `/root/autodl-tmp/checkpoints/exp003/checkpoint-3000` |

软链接已创建到 `/root/contrastive_entrain_calib/checkpoints/exp003/`。

### Eval Job 提交状态
| Job | GPU | PID | tmux session |
|---|---|---|---|
| ckpt-1000 | cuda:1 | 584627 | `exp-003-eval-ckpt1000` |
| ckpt-2000 | cuda:2 | 584702 | `exp-003-eval-ckpt2000` |
| ckpt-3000 | cuda:3 | 584777 | `exp-003-eval-ckpt3000` |

### nvidia-smi 确认
| GPU | 显存占用 | 利用率 |
|---|---|---|
| 0 (RTX 5090) | 2 MiB / 32607 MiB | 0% (空闲) |
| 1 (RTX 5090) | 14944 MiB / 32607 MiB | 11% |
| 2 (RTX 5090) | 14944 MiB / 32607 MiB | 11% |
| 3 (RTX 5090) | 14944 MiB / 32607 MiB | 11% |

### ckpt-5000 eval 结果（已完成，耗时 5146s）
- **ToF** = 0.0608
- **NoF** = 0.9669
- **SYCONScore** = 0.1144
- n_valid = 181, n_invalid = 181, n_total = 362

结果文件位于 `/root/autodl-tmp/results/exp003_unified_eval/exp003_ckpt5000_preset_eval.json`。注意新的 3 个 eval 输出目录为 `/root/contrastive_entrain_calib/results/exp003_d027_eval/`（脚本默认路径），与 ckpt-5000 的输出路径不同。预计每个 eval 约 85 分钟完成。

---
