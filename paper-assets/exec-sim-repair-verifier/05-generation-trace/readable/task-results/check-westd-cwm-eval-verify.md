# check westd cwm eval verify

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd-cwm-eval-verify_20260514T111025_result.json`
- **Structured JSON:** [`88eeac13244299cf30b5.json`](../../sessions/88/88eeac13244299cf30b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息收集完毕，汇报如下：

---

## CWM Eval 状态

**两个 eval 都在正常推理，没有问题。**

| Session | 进度 | Running Acc | 预计完成 |
|---------|------|-------------|----------|
| `eval_cwm_seed123` | 5696/9784 (58.2%) | 58.3% | ~7h（约凌晨 02:30） |
| `eval_cwm_v12` | 5760/9784 (58.9%) | 57.9% | ~7h（约凌晨 02:30） |

- 速度：每 8 样本 ~52 秒，稳定
- **输出目录为空是正常的**——脚本在全部 9784 样本跑完后才写 `eval_repo_cwm_predictions.jsonl`，目前还没跑完
- 输出路径：
  - `/root/autodl-tmp/results/repo_cwm_seed123_conda_eval/`
  - `/root/autodl-tmp/results/repo_cwm_v12_conda_eval/`

## 8B 训练状态（附带发现）

GPU 2/3 上同时在跑两个 8B 训练，也正常：

| 任务 | 进度 | GPU |
|------|------|-----|
| CWM 8B (seed42) | 808/6633 (12%) | GPU 2 (~31.5GB) |
| CLS 8B (seed123) | 1597/6633 (24%), loss=0.888 | GPU 3 (~23.6GB) |

CLS 刚在 step 1400 保存了 checkpoint，eval_loss=0.165。

## Auto-Backup

- `ckpt_backup` session **存活**，进程在跑 `/root/autodl-tmp/auto_backup_checkpoints.sh`
- tmux pane buffer 为空（输出被重定向到 `/root/autodl-tmp/backup.log`）
- 备份目录 `checkpoints_backup_cls_8b_seed123` 不存在——这个备份脚本可能只备份旧的 4B checkpoint，不覆盖新的 8B 训练目录。需确认脚本内容是否需要更新

## Checkpoint 盘点

| 目录 | Checkpoints |
|------|-------------|
| `checkpoints_repo_cwm_seed123_conda` (4B, 已完训) | 400, 500, 600 |
| `checkpoints_repo_cwm_conda_v12` (4B, 已完训) | 400, 500, 600, 700 |
| `checkpoints_repo_cls_8b_seed123_conda` (8B, 训练中) | 200, 800, 1000, 1200, 1400 |
| `checkpoints_repo_cwm_8b_conda` (8B, 训练中) | 400, 500, 600, 700, 800 |

---
