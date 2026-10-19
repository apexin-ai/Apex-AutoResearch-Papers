# code fix benchmark script

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_benchmark_script_20260519T163114_result.json`
- **Structured JSON:** [`a79cb3929a9b5daef021.json`](../../sessions/a7/a79cb3929a9b5daef021.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三项验证全部通过：

1. **文件部署** — 21815 bytes 写入 `/root/distill_sparse_swiglu/src/benchmark_flashinfer.py`
2. **语法检查** — `import src.benchmark_flashinfer` 无报错
3. **--help** — argparse 正常输出所有参数

三个 fix 总结：
- **P0 (full-sparse)**: `sparse_gather_ffn` 现在对 gate_proj、up_proj、down_proj 三个投影都做 gather-matmul，`patch_model_sparse_gather` 预切 3 个权重矩阵 `[K,H]`, `[K,H]`, `[H,K]`
- **P1 (mask 生成)**: 删除了 `patch_model_with_predictor`（用 `mask[0,0]` 的 bug 版本），`compute_teal_masks` 改为在所有 calibration token 上平均 `sigmoid(logits)` 后做 global top-k
- **P2 (calibration 数据)**: 新增 `load_calibration_data()`，优先加载 WikiText-2（离线缓存），fallback HellaSwag → 合成文本

---
