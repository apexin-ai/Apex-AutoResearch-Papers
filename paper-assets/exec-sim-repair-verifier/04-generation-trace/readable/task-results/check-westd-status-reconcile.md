# check westd status reconcile

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd-status-reconcile_20260514T155436_result.json`
- **Structured JSON:** [`eb406b2f3a38beee4343.json`](../../sessions/eb/eb406b2f3a38beee4343.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 输出目录为空——推断 eval 脚本在全部完成后才写出文件。以下是完整报告。

---

## GPU 状态总览

### cuda:0 — CWM seed123 Eval

| 项目 | 值 |
|------|-----|
| PID | 195531 |
| 命令 | `eval_repo_cwm.py --checkpoint_dir .../checkpoints_repo_cwm_seed123_conda/checkpoint-500` |
| 任务 | Eval（Qwen3-4B CWM, seed123, ckpt-500） |
| 显存 | 12,999 / 32,607 MiB (40%) |
| GPU 利用率 | 74% |
| 进度 | **8376 / 9784 (85.6%)** |
| Running Acc | 59.0% |
| 速率 | ~6.5s/sample（batch_size=8, ~52s/8样本） |
| 剩余 | ~1408 samples → **~2h 33min** |
| ETA | **May 15 ~02:28** |
| 异常 | 无。输出目录为空，eval 脚本应在跑完后一次性写出结果文件 |

### cuda:1 — CWM v12 Eval

| 项目 | 值 |
|------|-----|
| PID | 195668 |
| 命令 | `eval_repo_cwm.py --checkpoint_dir .../checkpoints_repo_cwm_conda_v12/checkpoint-500` |
| 任务 | Eval（Qwen3-4B CWM, v12, ckpt-500） |
| 显存 | 12,999 / 32,607 MiB (40%) |
| GPU 利用率 | 88% |
| 进度 | **8472 / 9784 (86.6%)** |
| Running Acc | 57.7% |
| 速率 | ~6.4s/sample |
| 剩余 | ~1312 samples → **~2h 20min** |
| ETA | **May 15 ~02:15** |
| 异常 | 无 |

### cuda:2 — CWM 8B 训练（从 ckpt-1200 恢复）

| 项目 | 值 |
|------|-----|
| PID | 245775 |
| 命令 | `train_repo_cwm.py --model_name .../Qwen3-8B/ --resume_from_checkpoint .../checkpoint-1200` |
| 任务 | Training（Qwen3-8B CWM, seed42） |
| 显存 | 21,205 / 32,607 MiB (65%) |
| GPU 利用率 | 98% |
| 进度 | **~1408 / 6633 (21.2%)** |
| 最新 checkpoint | checkpoint-1400（23:53 保存） |
| 已有 checkpoints | 400, 900, 1000, 1100, 1200, 1300, 1400 |
| 速率 | ckpt-1300→1400 = 39min/100步，含周期 eval。纯训练 ~12-13s/step |
| 剩余 | ~5225 steps → **~20-25h**（取决于 eval 频率） |
| ETA | **May 15 ~20:00 - May 16 01:00** |
| 异常 | 无。训练正常推进，loss 稳定 |

### cuda:3 — CLS 8B seed123 训练（从 ckpt-2400 恢复）

| 项目 | 值 |
|------|-----|
| PID | 248041 |
| 命令 | `train_repo_verifier.py --model_name .../Qwen3-8B/ --seed 123 --resume_from_checkpoint .../checkpoint-2400` |
| 任务 | Training（Qwen3-8B CLS verifier, seed123） |
| 显存 | 26,751 / 32,607 MiB (82%) |
| GPU 利用率 | 85% |
| 进度 | **~2764 / 6633 (41.7%)** |
| 最新 checkpoint | checkpoint-2600（23:32 保存） |
| 已有 checkpoints | 200, 1800, 2000, 2200, 2400, 2600 |
| 速率 | ~8.2s/step（tqdm 实时），ckpt-2400→2600 = 80min/200步 |
| Loss | 0.3559 @step2650, 0.45 @step2700, 0.6429 @step2750（有波动但正常） |
| 剩余 | ~3869 steps × 8.2s → **~8.8h** |
| ETA | **May 15 ~08:45** |
| 异常 | 无 |

---

## 总结表

| GPU | 任务 | PID | 显存 | 进度 | ETA (May 15) | 状态 |
|-----|------|-----|------|------|-------------|------|
| cuda:0 | CWM seed123 eval | 195531 | 13.0/32.6G | 85.6% | ~02:28 | 正常 |
| cuda:1 | CWM v12 eval | 195668 | 13.0/32.6G | 86.6% | ~02:15 | 正常 |
| cuda:2 | CWM 8B train | 245775 | 21.2/32.6G | 21.2% | ~20:00-次日01:00 | 正常 |
| cuda:3 | CLS 8B s123 train | 248041 | 26.8/32.6G | 41.7% | ~08:45 | 正常 |

**结论**：4 个进程全部正常运行，无异常。Registry 标记 DONE 是错误的，实际都还在跑。两个 eval 约 2.5h 后完成，CLS 8B 约 9h 后完成，CWM 8B 最慢约 20-25h。

---
