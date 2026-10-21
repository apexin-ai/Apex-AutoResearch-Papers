# analysis teal ppl source investigation

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_teal_ppl_source_investigation_20260516T000027_result.json`
- **Structured JSON:** [`0b26688aaedf4a79ef9e.json`](../../sessions/0b/0b26688aaedf4a79ef9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

**`kl_sparsity70_s42_v2` 的 `teal_sparse_ppl=17.91` 调用的是 `teal_global_masks`（predictor-based），不是 `vanilla_teal_global_masks`。**

### 代码证据

`/root/distill_sparse_swiglu/src/quick_sp70.py` 是产生 17.913 的脚本：

- **L10**: `from evaluate import teal_global_masks` — 导入 predictor-based 版本
- **L53-54**: 加载 `kl_sparsity70_s42/predictor_kl_normalized.pt` 到 `PredictorWrapper`
- **L60**: `sp70_masks = teal_global_masks(wrapper, calib_ids, 0.7)` — 用 predictor 生成 mask
- **L85/L115**: 结果写入 `plan_007_sparsity70.json`

`teal_global_masks`（evaluate.py L64-95）的逻辑：
- 对每个 neuron，score = `mean(|act(gate(x))*up(x)| * (predictor_logit > 0))`
- 即用 predictor 做门控，只对 predictor 保留的 neuron 计算 magnitude score
- 然后 `_global_topk_masks` 做跨层 global topk，保留 top 30%

### 判定

| 指标 | 方法 | 值 |
|------|------|-----|
| `teal_sparse_ppl` (kl_sparsity70_s42_v2) | Predictor TEAL: predictor-gated magnitude + global topk @70% | 17.91 |
| vanilla TEAL 70% (re-run) | Vanilla TEAL: pure activation magnitude + global topk @70% | 100.11 |

**两者是不同方法，5.6x 差距合理。** Predictor 显著改善了 neuron importance scoring，即使最终都用 static mask 做 inference。

### 注意

`plan_007_all_ppl_fixed.json` 中标注 `"mode": "static_mask_70pct"` 是误导性 metadata — 实际 eval 代码用了 predictor-based scoring（非 vanilla）。两个数字可作为 ablation 对比：predictor guidance 在 70% sparsity 下将 PPL 从 100.11 降到 17.91。

---
