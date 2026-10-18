# code benchmark visualization

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_benchmark_visualization_20260518T191343_result.json`
- **Structured JSON:** [`46576d77f4a930db28c6.json`](../../sessions/46/46576d77f4a930db28c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**CSV**: 16 行，覆盖所有模型（GDN 5 + RetNet 5 + HGRN2 5 + Transformer 1）

**生成的图表** (6 个文件):
- `fig1_lambada_vs_attn.pdf/png` — LAMBADA acc vs attention layer count
- `fig2_all_benchmarks.pdf/png` — 6 panel (LAMBADA acc/ppl, HellaSwag, Winogrande, ARC-E, ARC-C)
- `fig3_delta_heatmap.pdf/png` — 各 hybrid 相对 pure 的 delta heatmap

**关键发现**:
- GDN pure (0 attn) 的 LAMBADA acc 最高 (0.543)，优于 Transformer baseline (0.480)
- 所有 3 个 linear model family 在 LAMBADA 上都超过 Transformer baseline
- HGRN2 随 attention 层数增加有稳定提升趋势
- GDN 和 RetNet 的 hybrid 版本反而不如 pure，增加 attention 层没有带来一致的增益

---
