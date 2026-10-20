# code anonymous repo

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_anonymous_repo_20260524T124841_result.json`
- **Structured JSON:** [`ebbe2711abe2e2d008f2.json`](../../sessions/eb/ebbe2711abe2e2d008f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

匿名仓库已完成。位置：`artifacts/anonymous_repo/`

**内容概览（27 files, 3.8K lines）：**

| 目录 | 文件 | 说明 |
|------|------|------|
| `src/` | `threadgate.py` | ThreadGatedModel, TurnEmbedding, GateNetwork |
| | `gar.py` | GAR measurement + 6 种辅助 loss mode |
| | `turn_utils.py` | ChatML / Llama-3 turn boundary detection |
| | `model_loader.py` | Checkpoint loading + KV cache gate hooks |
| | `attention_steering.py` | Pre-softmax attention bias |
| | `split_softmax.py` | Li et al. 2024 baseline |
| | `trc_measure.py` | Turn Representation Coherence metric |
| | `train.py` | 基础训练（TG/UG/LoRA-only） |
| | `train_pcgrad.py` | PCGrad 梯度冲突解决 |
| | `train_scheduled_sampling.py` | Scheduled Sampling |
| | `eval_gar.py` / `eval_multiturn.py` | GAR + 多轮评估 |
| | `gradient_conflict_analysis.py` | NTP-GAR 梯度冲突分析 |
| `scripts/` | 8 个 `.sh` | 训练（5 条件）+ 评估（3 脚本） |
| `data/` | `download_ultrachat.py`, `convert_to_eval.py` | 数据准备 |

**匿名化检查通过：** 无 `/root/`、wandb、邮箱、机构名、服务器地址。所有 Python 文件语法验证通过。

下一步：你可以用这个目录初始化匿名 GitHub 仓库（如 Anonymous GitHub 或 OpenReview 匿名提交），在 rebuttal 中提供链接给 Reviewer。

---
