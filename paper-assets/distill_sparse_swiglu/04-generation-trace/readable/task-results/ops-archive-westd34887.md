# ops archive westd34887

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_archive_westd34887_20260525T204209_result.json`
- **Structured JSON:** [`1dd85549315ba4894916.json`](../../sessions/1d/1dd85549315ba4894916.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

归档完成。汇总：

**归档位置：** `/root/autodl-tmp/distill_sparse_swiglu_archive/`（根分区空间不足，改用数据盘）

| 目录 | 大小 | 内容 |
|------|------|------|
| `code/` | 12G | 完整项目代码（含 checkpoints 副本），无 .git（服务器原始就没有） |
| `checkpoints/` | 11G | 68个实验目录 + `predictor_perlayer_kl.pt` |
| `results/` | 54M | `results_dir/` + `run_logs/`（~/runs/） + `wandb/` |
| `paper/` | 708K | 论文 LaTeX + `figures/`（8个 PDF/PNG 图表） |
| `data/` | 0 | 空（autodl-tmp 下只有公开数据集，未复制） |
| **总计** | **23G** | |

**备注：**
- 原始数据未删除
- `.git` 在服务器端不存在（代码是 sync 过去的），完整 git 历史在本地仓库
- `/root/autodl-tmp/data/`（c4_val, wikitext103, wikitext2）为公开评估数据集，未归档
- `/root/autodl-tmp/models/`（66G HF 模型）未归档

---
