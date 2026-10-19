# ops data archive westd15904

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_data-archive-westd15904_20260525T204340_result.json`
- **Structured JSON:** [`dad24f24595027cdcc93.json`](../../sessions/da/dad24f24595027cdcc93.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

归档完成。

## 归档报告

**路径**: `~/contrastive_trace_safety_archive/` (westd-15904)
**总大小**: 7.5G

| 目录 | 大小 | 内容 |
|------|------|------|
| `code/` | 280K | scripts/ 下 16 个实验脚本（.py, .sh） |
| `data/` | 7.5G | hidden_states × 6 套（r1_8b_full, advbench_r1_8b/gemma2/gemma4, ot7b_verify, r1_32b_verify）+ advbench_traces × 3 套 + advbench/harmful_behaviors.csv |
| `results/` | 308K | 12 个 JSON 结果文件 + 1 个 TXT 日志 + verification/（5 个验证 JSON）+ random_cp_control/ |
| `paper/` | 256K | figures/（fig_cosine_cross_arch.pdf/png） |

**跳过的内容**:
- `models/bge-large-en-v1.5/` (3.8G) — 公开预训练模型，无需归档
- `.git/` — 原项目不存在 git 仓库
- `wandb/` — 不存在
- `checkpoints/` — 不存在训练 checkpoint，未创建此子目录

---
