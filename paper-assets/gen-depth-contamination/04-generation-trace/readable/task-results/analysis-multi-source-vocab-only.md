# analysis multi source vocab only

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_multi_source_vocab_only_20260520T073227_result.json`
- **Structured JSON:** [`df62086ecfb2767df16b.json`](../../sessions/df/df62086ecfb2767df16b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果已保存到 `multi_source_vocab_only_results.json`。

```
=== Vocab-Only Multi-Source Results ===

v1 (Qwen+Pythia+OLMo):
  0v1 AUC: 0.8675  CI=[0.8586, 0.8763]
  1v2 AUC: 0.6760  CI=[0.6617, 0.6903]
  2v3 AUC: 0.4938  CI=[0.4799, 0.5075]
  K* (θ=0.60): 2

v2 (Qwen+Pythia+LLaMA-8B):
  0v1 AUC: 0.8296  CI=[0.8201, 0.8391]
  1v2 AUC: 0.6830  CI=[0.6693, 0.6969]
  2v3 AUC: 0.5057  CI=[0.4920, 0.5195]
  K* (θ=0.60): 2

Full-feature comparison:
  v1 full K*: 2 vs vocab-only K*: 2  ✓ 一致
  v2 full K*: N/A (未跑 v2 full-feature) vs vocab-only K*: 2
```

**关键发现：K\*=2 在仅用 6 个 scorer-independent vocabulary features 时仍然成立。** 这排除了 scorer confound 的解释——即使完全不使用任何 OBD/surprisal 特征（由 scorer 模型计算），LightGBM 仍然在 depth 0→1 和 1→2 检测到显著差异，2→3 之后退化到随机。

注意 vocab-only 的 0v1 AUC（v1: 0.8675, v2: 0.8296）比 full-feature（v1: 0.9929）明显低，说明 OBD features 确实贡献了区分能力，但不影响 K\* 的判断。1v2 AUC 差异更小（vocab-only 0.676 vs full 0.700），K\* 边界一致。

---
