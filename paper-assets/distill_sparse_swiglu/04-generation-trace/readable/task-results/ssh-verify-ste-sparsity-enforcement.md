# ssh verify ste sparsity enforcement

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify_ste_sparsity_enforcement_20260520T183930_result.json`
- **Structured JSON:** [`b5fd0a69abb61ab21344.json`](../../sessions/b5/b5fd0a69abb61ab21344.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据齐了。

---

## 结论

### Part 1: Mask 生成代码（核心逻辑）

`evaluate.py` 中 `teal_global_masks` → `_uniform_topk_masks` 的流程：

```python
# evaluate.py:57 - teal_global_masks
# 1. 用 calibration data 跑 predictor，收集 per-neuron sigmoid 均值作为 score
scores = torch.sigmoid(logits).mean(dim=(0, 1))

# evaluate.py:140 - _uniform_topk_masks (allocation="uniform" 时调用)
# 2. 每层独立取 top-k，强制恰好 sparsity_target 的 neuron 被 mask
num_keep = int(len(s) * (1.0 - sparsity_target))   # 70% neurons kept
thr = torch.topk(s, num_keep).values[-1]
masks[li] = (s >= thr).to(torch.bfloat16)
```

**这是 top-k 强制 enforcement，不是 threshold。** Predictor 的 sigmoid 输出仅用作排序分数，实际 sparsity 由 `num_keep` 硬性控制，每层恰好 30%。

### Part 2: STE (C1 ablation) 30% eval 配置

`c1_ablation_30pct_s42_eval/results.json` 确认：
- `sparsity_mode: "teal_global"`
- `sparsity_target: 0.3`
- `allocation: "uniform"`
- checkpoint: `c1_ablation_30pct_s42/predictor_bce_kl_targets.pt`

### Part 3: 两个实验 eval 对比

| Metric | KL+Gumbel 30% (`d030_kl30_uniform`) | STE/C1 30% (`c1_ablation_30pct_s42_eval`) |
|--------|------|------|
| **Eval sparsity** | **uniform 30% top-k** | **uniform 30% top-k** |
| WikiText-2 PPL | 8.8157 | 9.4463 |
| ARC (acc_norm) | 40.78% | 40.27% |
| WinoGrande | 68.59% | 67.40% |
| MMLU | 40.61% | 42.29% |
| GSM8K | 7.35% | 7.58% |

### Part 4: 结论

**Eval 用 TEAL top-k 强制了每层恰好 30%。** 两个实验在 eval 时 sparsity 完全一致。

STE 训练时的 sparsity 失衡（13/32 层偏低、有效 ~23.5%）**不影响 eval**——predictor 输出仅用作 neuron 重要性排序，实际 sparsity 由 `_uniform_topk_masks` 的 per-layer top-k 硬性保证。

STE 30% 结果有效，与 KL 30% 的对比是公平的（同为 uniform 30% eval sparsity）。训练时 sparsity 不均只影响了 predictor 学到的排序质量，这反映在 PPL 差距上（9.45 vs 8.82），但不存在 sparsity 不对等的混淆因素。

---
