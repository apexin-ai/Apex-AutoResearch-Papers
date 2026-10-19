# code check 41718 benchmark readiness

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_check_41718_benchmark_readiness_20260519T164341_result.json`
- **Structured JSON:** [`7bf4257e4630256c9043.json`](../../sessions/7b/7bf4257e4630256c9043.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

检查结果汇总：

| 项目 | 状态 | 说明 |
|------|------|------|
| **LLaMA-3.1-8B 模型** | ✅ 存在 | `/root/autodl-tmp/models/llama-3.1-8b/`，4 个 safetensors 分片完整 |
| **KL predictor (30%, s42)** | ✅ 存在 | `/root/distill_sparse_swiglu/checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt` |
| **KL predictor (50%, s42)** | ✅ 存在 | `/root/distill_sparse_swiglu/checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt` |
| **benchmark_flashinfer.py** | ❌ 缺失 | `src/` 下不存在此脚本 |
| **flashinfer 包** | ❌ 缺失 | site-packages 中未找到 flashinfer |
| **evaluate.py** | ✅ 存在 | `/root/distill_sparse_swiglu/src/evaluate.py` |
| **磁盘空间** | ✅ 充裕 | `/root/autodl-tmp/` 250G 总量，已用 47G，剩余 204G (19%) |

**需要同步/安装的内容：**

1. **`benchmark_flashinfer.py`** — 从 westd-34887 rsync 或从本地 push 后 git pull（脚本级别，<100KB）
2. **`flashinfer` Python 包** — 需要 `pip install flashinfer`（编译型包，需确认 CUDA 版本匹配，预估安装大小 ~200-500MB）

注：`src/` 下有 `latency_benchmark.py` 和 `benchmark_speedup.py`，如果 flashinfer benchmark 逻辑在这两个文件里可能不需要额外脚本，需确认。

---
