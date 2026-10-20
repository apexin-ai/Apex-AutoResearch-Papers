# code accuracy eval r9c2 v2

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_accuracy_eval_r9c2_v2_20260515T201814_result.json`
- **Structured JSON:** [`8ef219debb93a61d5d32.json`](../../sessions/8e/8ef219debb93a61d5d32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## R9-C2 Spike Test Results (10 problems, 2 conditions)

### Accuracy

| Condition | Correct | Total | Accuracy | Delta |
|-----------|---------|-------|----------|-------|
| dense | 4 | 10 | **40.0%** | — |
| importance_s025 | 1 | 10 | **10.0%** | **-30.0%** |

### Per-problem breakdown

| # | Problem | Dense | importance_s025 |
|---|---------|-------|-----------------|
| 1 | precalculus/807 | ✓ (19.9s, 1114tok) | ✗ pred=None (41.8s, 2048tok) |
| 2 | intermediate_algebra/1994 | ✗ pred=None (36.1s, 2048tok) | ✗ pred=None (41.3s, 2048tok) |
| 3 | algebra/2584 | ✗ pred=None (36.0s, 2048tok) | ✗ pred=-9/2 (10.2s, 517tok) |
| 4 | number_theory/572 | ✓ pred=9 (19.5s, 1124tok) | ✓ pred=9 (8.6s, 439tok) |
| 5 | algebra/1349 | ✗ pred=None (36.3s, 2048tok) | ✗ pred=None (41.6s, 2048tok) |
| 6 | prealgebra/1622 | ✓ pred=42 (15.1s, 881tok) | ✗ pred=None (41.2s, 2048tok) |
| 7 | number_theory/515 | ✗ pred=None (35.9s, 2048tok) | ✗ pred=None (41.2s, 2048tok) |
| 8 | precalculus/927 | ✗ pred=None (36.0s, 2048tok) | ✗ pred=None (41.2s, 2048tok) |
| 9 | algebra/2036 | ✓ pred=3√13 (6.7s, 384tok) | ✗ pred=6 (8.0s, 406tok) |
| 10 | prealgebra/1139 | ✗ pred=None (36.1s, 2048tok) | ✗ pred=None (41.3s, 2048tok) |

### Timing

- Dense avg: **27.8s/gen** (correct answers ~15s, None/wrong ~36s hitting 2048 tokens)
- importance_s025 avg: **31.6s/gen** (mostly ~41s hitting 2048 tokens)
- Overall avg: **30.0s/gen**
- Total spike time: **600s** (10 min)

### Key observations

1. **pred=None 问题严重**: Dense 有 6/10 problems 生成 2048 tokens 但未产生 `\boxed{}`，importance_s025 有 8/10。DeepSeek-R1 reasoning model 的 chain-of-thought 经常超过 2048 tokens 才得出结论。
2. **Sparsity 使模型更 verbose**: 在 sparse 条件下，模型更容易 hit token limit（41s vs 36s），因为 attention 被扰乱后推理链变得更冗长。
3. **仅 1 个问题(#4)在 sparse 下仍正确**，且该问题较简单（单一数字答案）。问题 #6（dense ✓, sparse ✗）和 #9（dense ✓, sparse 给出错误数值）展示了真实的 accuracy degradation。
4. **建议考虑 max_new_tokens=4096**: 当前 2048 限制下 dense baseline 只有 40%，可能低于该模型在 MATH-500 上的真实能力（文献报告 ~70%+）。增大 token limit 能更好区分"模型能力不足"和"sparsity 导致的降级"。

### Full-run estimate

| 配置 | 值 |
|------|-----|
| Problems | 500 |
| Conditions | 9 (dense + 4×importance + 4×random) |
| Total generations | 4,500 |
| Avg time/gen | ~30s |
| Single-GPU time | **~37.5 hours** |

### Proposed 4-GPU parallel plan

| GPU | Conditions | Est. generations | Est. time |
|-----|-----------|-----------------|-----------|
| cuda:0 | dense, random_s030 | 1,000 | ~8.3h |
| cuda:1 | importance_s015, importance_s020 | 1,000 | ~8.3h |
| cuda:2 | importance_s025, importance_s030 | 1,000 | ~8.3h |
| cuda:3 | random_s015, random_s020, random_s025 | 1,500 | ~12.5h |

**Bottleneck: ~12.5 hours** (GPU 3 with 3 conditions).

### Decision needed before full-run

1. **max_new_tokens**: 保持 2048 还是增大到 4096？（4096 会使 bottleneck 从 ~12.5h 增到 ~20-25h，但 dense baseline 和 degradation 信号会更可靠）
2. **GPU 分配方案**是否 OK？
3. 确认后我立即提交 4 个 `submit_training_job`。

---
