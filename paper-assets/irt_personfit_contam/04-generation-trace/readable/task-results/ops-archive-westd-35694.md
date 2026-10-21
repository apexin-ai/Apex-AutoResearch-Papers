# ops archive westd 35694

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_archive-westd-35694_20260525T204208_result.json`
- **Structured JSON:** [`0c9278de434e21ea7218.json`](../../sessions/0c/0c9278de434e21ea7218.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

**Step 1 ✅ 前置检查**: 4x RTX PRO 6000 Blackwell 全部空闲，无活跃训练进程。

**Step 2 ✅ 数据归档**: 已创建 `/root/irt_personfit_contam_archive/`，按类别组织:

| 子目录 | 大小 | 内容 |
|--------|------|------|
| `checkpoints/` | 20G | 5 组实验 checkpoint (pilot/llama/mistral/arcc/post_rl) |
| `code/` | 111M | 含 .git 的 repo + 所有实验代码 + 独立脚本 |
| `data/` | 111M | contamination training data |
| `results/` | 40M | 实验结果 + wandb + logs |
| `paper/` | 712K | figures |

**总计: 20G**，原始数据未删除。

**Step 4 ❌ S3 备份失败**: IAM 用户 `agent-ml-be-backup` 对 `s3://agent-ml-manager-backups-emnlp` 无 `s3:PutObject` 和 `s3:ListBucket` 权限。需要更新 IAM policy 后重试。

报告已写入服务器 (`~/irt_personfit_contam_archive/archive_report.md`) 和本地 artifacts。

---
