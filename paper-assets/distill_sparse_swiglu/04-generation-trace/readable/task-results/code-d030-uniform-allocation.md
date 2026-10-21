# code d030 uniform allocation

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d030_uniform_allocation_20260516T033012_result.json`
- **Structured JSON:** [`29bbed213cd600ed3917.json`](../../sessions/29/29bbed213cd600ed3917.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

---

### 产出总结

**修改的文件**：

1. **`src/evaluate.py`** — 核心 mask 模块
   - 新增 `_uniform_topk_masks(layer_scores, sparsity_target)`：每层独立 top-k，确保各层 sparsity 相同
   - 新增 `_dispatch_masks(layer_scores, sparsity_target, allocation)`：路由到 global/uniform
   - 修改 4 个 mask 函数签名添加 `allocation="global_topk"` 参数：`teal_global_masks`, `vanilla_teal_global_masks`, `wina_global_masks`, `rsparse_global_masks`
   - 所有函数内部的 `_global_topk_masks` 调用替换为 `_dispatch_masks`

2. **`src/benchmark_eval.py`** — 统一评测脚本
   - 新增 `--allocation {global_topk,uniform}` CLI 参数（默认 `global_topk`）
   - `compute_baseline_masks` 接受并传递 `allocation`
   - predictor `teal_global` 路径传递 `allocation`
   - `mode_info` 和打印信息包含 allocation

**使用方式**：
```bash
# Uniform per-layer allocation (predictor)
python src/benchmark_eval.py --exp_id test_uniform \
    --checkpoint ... --sparsity_mode teal_global \
    --allocation uniform --tasks wikitext2,mmlu

# Uniform per-layer allocation (baseline)
python src/benchmark_eval.py --exp_id teal_vanilla_uniform \
    --baseline_mode teal_vanilla --allocation uniform --tasks wikitext2,mmlu
```

**不适用 uniform 的模式**（已是 per-layer）：`teal_greedy`, `wina_greedy`, `per_token`。传了 `--allocation uniform` 不会报错，但对这些模式无效（它们不走 `_dispatch_masks`）。

**待做事项**：`src/evaluate.py` 的 `main()` 函数（独立 PPL eval 脚本）没有添加 `--allocation` 参数。如果需要在那个路径也支持 uniform，需要单独加。

---
