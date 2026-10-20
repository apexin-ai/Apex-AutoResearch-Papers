# code prep random reweight v2

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_random_reweight_v2_20260516T142848_result.json`
- **Structured JSON:** [`07eb039952917c8fd4f8.json`](../../sessions/07/07eb039952917c8fd4f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

| 项目 | 状态 |
|------|------|
| 上次运行 | **失败**。跑到 step ~499（共需 6103），无 checkpoint 产出。output 写根分区 + WANDB_MODE=offline，大概率磁盘满崩溃 |
| v2 脚本 | **Ready** — `/root/provenance_weight_training/scripts/run_random_reweight_v2_seed42.sh` |
| 磁盘 | 根分区 7.1GB 可用（77%），数据盘 45GB 可用（83%） |

**v2 修正点：**
- `WANDB_MODE=disabled`（零磁盘写入）
- `output_dir` → `/root/autodl-tmp/output/models/random_reweight_v2_seed42/`（数据盘）
- `CUDA_VISIBLE_DEVICES=-1`（提交时替换）
- 无 `--use_wandb` 参数

Dry-run 确认数据/模型/参数全部解析正确，只差分配 GPU 即可启动。

---
