# code mvp foreground validation

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp-foreground-validation_20260513T213800_result.json`
- **Structured JSON:** [`bdc5610b822fcb3de63a.json`](../../sessions/bd/bdc5610b822fcb3de63a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pipeline 完整运行成功。完整输出如下：

---

```
`torch_dtype` is deprecated! Use `dtype` instead!
Token indices sequence length is longer than the specified maximum sequence length for this model (298938 > 131072). Running this sequence through the model will result in indexing errors
Loading model /root/autodl-tmp/models/Qwen2.5-1.5B...
Loading existing profiles from profiles.json

=== Crossover Analysis ===
  Memory 0.125: 89.3% heads prefer eviction (50/56)
  Memory 0.25: 0.0% heads prefer eviction (0/56)
  Memory 0.5: 0.0% heads prefer eviction (0/56)

=== Solver Results ===
  Full MCKP @ 0.5: {'full': 1, 'quant': 55}, dist=0.006528, mem=0.5000
  Quant-only @ 0.5: {'full': 1, 'quant': 55}, dist=0.006528, mem=0.5000
  Full MCKP @ 0.25: {'quant': 54, 'evict': 2}, dist=0.539991, mem=0.2478
  Quant-only @ 0.25: {'quant': 56}, dist=0.552362, mem=0.2478
  Full MCKP @ 0.125: {'evict': 38, 'quant': 18}, dist=3.395526, mem=0.1239
  Quant-only @ 0.125: {'quant': 56}, dist=14.286242, mem=0.1250

=== Perplexity Evaluation ===
Evaluating baseline (no compression)...
  Baseline PPL: 12.46

Evaluating full MCKP @ budget=0.5...
  Full MCKP PPL: 12.52
Evaluating quant-only MCKP @ budget=0.5...
  Quant-only PPL: 12.52

Evaluating full MCKP @ budget=0.25...
  Full MCKP PPL: 22.67
Evaluating quant-only MCKP @ budget=0.25...
  Quant-only PPL: 19.91

Evaluating full MCKP @ budget=0.125...
  Full MCKP PPL: 14065.01
Evaluating quant-only MCKP @ budget=0.125...
  Quant-only PPL: 14700.47

Evaluating uniform 4-bit...
  Uniform 4-bit PPL: 19.26

================================================================================
RESULTS SUMMARY
================================================================================
  Budget |    Full MCKP |   Quant-only |   Uniform 4b |      Delta
------------------------------------------------------------------
      2x |        12.52 |        12.52 |          N/A |      +0.00
      4x |        22.67 |        19.91 |        19.26 |      -2.77
      8x |     14065.01 |     14700.47 |          N/A |    +635.46

Crossover criterion (>=10% heads prefer eviction): PASS
PPL improvement criterion (>=0.5 at any budget):  PASS
Overall: PASS

Generating figures...
Saved crossover_scatter.pdf/png
Saved ppl_comparison.pdf/png
Saved allocation_heatmap_full_0.5.pdf/png
Saved allocation_heatmap_full_0.25.pdf/png
Saved allocation_heatmap_full_0.125.pdf/png

Saved all results to sanity_foreground_results.json
```

---

**关键结果**：

- **Crossover**: 在 0.125 memory budget 下，89.3% (50/56) 的 KV heads 偏好 eviction — PASS
- **Solver**: Full MCKP 在 0.125x 时选择 38 evict + 18 quant（distortion 3.40），而 quant-only 的 distortion 是 14.29，差 4.2x
- **PPL**: Baseline 12.46 → 2x 压缩 12.52（几乎无损），4x 压缩 22.67 (full) vs 19.91 (quant-only)，8x 压缩两者都崩溃（~14000+）
- **Uniform 4-bit PPL**: 19.26（在 4x budget 下优于 Full MCKP 的 22.67）
- **Overall: PASS**

注意 4x budget 下 Full MCKP (22.67) 反而比 Quant-only (19.91) 和 Uniform 4-bit (19.26) 差（Delta=-2.77），说明 solver 的 eviction 选择在这个 budget 点不优。这加载的是之前已有的 profiles.json，可能需要用新 calibration 数据重新 profile。

---
