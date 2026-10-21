# ops kill s3 and archive

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-s3-and-archive_20260525T204639_result.json`
- **Structured JSON:** [`1fd441e7aa441eb28d55.json`](../../sessions/1f/1fd441e7aa441eb28d55.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-act-256-v2 (PID 2117, cuda:0) 正常运行，未受影响。

## Kill 结果
- 进程状态: PID 2191 + 子进程 PID 2196 已 kill，**DEAD**
- cuda:1 状态: **已释放**（0 MiB），cuda:0 上 exp-act-256-v2 正常运行

## 归档结果
总大小: **30 GB**
归档路径: `/root/autodl-tmp/contrastive_entrain_calib_archive/`（`~/contrastive_entrain_calib_archive` 为软链接）

| 子目录 | 大小 | 内容 |
|--------|------|------|
| code/ | 84 MB | 项目全部代码（无 .git，源目录本身非 git 仓库） |
| checkpoints/ | 30 GB | exp003_r3only_seed1/seed2/seed3, exp008_sft_seed42/43/44, act_256_ablation |
| results/ | 427 MB | 实验结果（exp001-008 eval）、日志（logs/）、eval_results/、run_logs/ |
| data/ | 1.1 MB | contrastive pairs + eval 数据 |
| paper/ | 224 KB | figures_data/（fig_teaser.pdf/png） |

磁盘剩余: **127 GB**（/root/autodl-tmp/ 数据盘）

## 注意事项
- 源目录 `/root/contrastive_entrain_calib/` 无 .git 目录（代码通过其他方式同步，非 git clone）
- 无 wandb 本地目录
- 服务器上无 paper/main.tex（论文在本地，需单独处理）
- 无 vanilla baseline checkpoint 目录（可能模型文件在其他路径或已被清理）
- `probe_trap_data.json` / `fig_layer_auroc_data.json` 在服务器上未找到（可能在本地 artifacts 目录）
- exp-act-256-v2 (cuda:0, PID 2117) 未受影响，正常训练中

---
