# infra westd 41718 setup

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd-41718-setup_20260517T150631_result.json`
- **Structured JSON:** [`15ac85297f84832f2b9e.json`](../../sessions/15/15ac85297f84832f2b9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。汇总：

## westd-41718 部署结果

| 项目 | 状态 |
|------|------|
| GPU | 2× NVIDIA RTX PRO 6000 Blackwell, 97GB each |
| Python | 3.12.3 (miniconda3) |
| PyTorch | 2.8.0+cu128 |
| transformers | 5.8.1 |
| accelerate | 1.13.0 |
| lm-eval | 0.4.12 |
| datasets | 4.8.5 |
| CUDA | 13.0, Driver 580.95 |

**磁盘：**
- `/` (overlay): 29G 可用 (6% used)
- `/root/autodl-tmp`: 233G 可用 (7% used)

**已同步文件：**
- 代码: `/root/distill_sparse_swiglu/` (40 py files in src/)
- 模型: `/root/autodl-tmp/models/llama-3.1-8b/` (15GB)
- Checkpoint: `checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt` (145MB)
- HF cache: `/root/autodl-tmp/.hf_cache/` (2.5GB)

**验证通过：**
- `nvidia-smi` ✓
- `python -c "import torch; torch.cuda.device_count()"` → 2 ✓
- `python src/benchmark_eval.py --help` ✓

服务器已就绪，可直接跑 benchmark eval。

---
