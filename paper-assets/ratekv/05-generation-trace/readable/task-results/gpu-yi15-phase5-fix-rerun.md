# gpu yi15 phase5 fix rerun

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_yi15_phase5_fix_rerun_20260514T182903_result.json`
- **Structured JSON:** [`bd1c11e86c0e42043e19.json`](../../sessions/bd/bd1c11e86c0e42043e19.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pipeline 已重跑完成，`yi15_full_results.json` 完整。无需再修复或重跑。

## Yi-1.5-9B 完整结果

### 架构
- 48 layers, 4 KV heads/layer, GQA 8:1, 192 total KV heads, head_dim=128

### PPL
| Method | WikiText-2 PPL | Delta vs Uniform |
|--------|---------|---------|
| Baseline (bf16) | 7.0157 | — |
| MCKP (k=8) | 7.3129 | **-0.0958** |
| Uniform 4-bit | 7.2171 | — |

**Verdict: FAIL** — MCKP 比 uniform 4-bit 还差 0.096，没有任何改善。

### Bit Distribution (k=8)
- 4-bit: 180 heads, 2-bit: 8 heads, 8-bit: 4 heads

### K Ablation
| k | PPL | n_2bit |
|---|-----|--------|
| 2 | **7.2209** | 2 |
| 4 | 7.2788 | 4 |
| 6 | 7.2874 | 6 |
| 8 | 7.3129 | 8 |
| 10 | 7.4164 | 10 |
| 12 | 7.5869 | 12 |
| 14 | 7.6612 | 14 |
| 16 | 7.6925 | 16 |

Best k=2 (PPL=7.2209)，但仍不如 uniform 4-bit（7.2171）。PPL 随 k 单调递增——更多 2-bit heads 只会更差。

### Heterogeneity Analysis (Claim 3 相关)
- **Top-5% concentration: 0.4934** (9 heads / 192 total)
- CV of delta(2bit): 4.7938
- Layer 0 dominance ratio: 0.07x (layer 0 反而是最不敏感的)
- All 192 heads have positive delta
- Most sensitive head: **L4H3** (delta_2bit = +5.6523，极端异常值)

### 与其他模型对比
| Model | GQA Ratio | Top-5% Conc. | MCKP vs Uniform | Verdict |
|-------|-----------|-------------|-----------------|---------|
| Qwen2.5-7B | 7:1 | ~0.42 (std) / ~0.59 (hires) | PASS | PASS |
| Yi-1.5-9B | 8:1 | **0.4934** | -0.096 | FAIL |

Yi 的 top-5% concentration (0.4934) 确实比 Qwen standard 的 ~0.42 更高，符合"高 GQA ratio → 高 heterogeneity"的趋势。但 MCKP 无法利用这个 heterogeneity——因为 sensitivity 过度集中在少数 outlier heads（L4H3 贡献了 delta_2bit 总量的极大比例），使得 MCKP 的 2-bit allocation 几乎无处可用而不严重损害质量。

---
