# infra check westd41718 status

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check_westd41718_status_20260517T231335_result.json`
- **Structured JSON:** [`df2df068608e8b8f45b6.json`](../../sessions/df/df2df068608e8b8f45b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-41718 服务器状态汇报

### GPU 状态：完全空闲
- 2× NVIDIA RTX PRO 6000 Blackwell (各 97.8 GB VRAM)
- 0% utilization，0 MiB 显存占用
- 无运行中的 GPU 进程

### 磁盘空间
- `/root` 挂载点：30G 总量，已用 2.2G，**可用 28G (92%)**

### 工作目录 `/root/distill_sparse_swiglu/`：已存在
完整项目结构就绪，包含 src/、scripts/、tests/、artifacts/、results/、wandb/ 等。

### Checkpoints（3 个）
| 目录 | 最后修改 |
|------|----------|
| `kl_sparsity30_s42_v3` | May 16 05:48 |
| `mvp_kl_norm_v2_s42` | May 17 23:34 |
| `mvp_kl_norm_v2_s123` | May 18 01:51 |

### 模型权重：已就绪
- `/root/autodl-tmp/models/qwen2.5-14b/` — 8 个 safetensors 分片，完整
- `/root/autodl-tmp/models/llama-3.1-8b/` — 4 个 safetensors 分片，完整

### C4 数据集：已缓存
- HF cache 中有 `datasets--allenai--c4`（两个路径：`/root/autodl-tmp/.hf_cache/hub/` 和 `/root/.cache/huggingface/hub/`）
- HF datasets cache 大小：1.8G
- 相关评估脚本和日志已存在（`eval_c4_ood.py`、`c4_ood_ppl.json` 等）

### 活跃 Python 进程：无训练进程
仅有系统服务（jupyter-lab、tensorboard、autopanel），无用户训练进程。

---

**总结：westd-41718 双卡完全空闲，磁盘充足，模型/数据/checkpoints 均已就绪，可立即启动实验。**

---
