# fix nscaling table gf maxlp

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_nscaling_table_gf_maxlp_20260518T053259_result.json`
- **Structured JSON:** [`536140e8c9e9c045f82f.json`](../../sessions/53/536140e8c9e9c045f82f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Full-set greedy = 0.6141 matches the footnote's 0.614. Gold-filtered greedy = 0.6397.

Now let me produce the final output. Here are the current (old) vs new values side by side:

## N-scaling 表重算 (SciERC NER, gold-filtered, max_LP)

### 数据源
| N | Samples 文件 | Gold-filtered n |
|---|-------------|-----------------|
| 2 | exp_025_n32/samples.jsonl (first 2) | 529 |
| 4 | exp_025_n32/samples.jsonl (first 4) | 529 |
| 8 | exp_025_n32/samples.jsonl (first 8) | 529 |
| 16 | exp_025_n32/samples.jsonl (first 16) | 529 |
| 32 | exp_025_n32/samples.jsonl (all 32) | 529 |

### LP Δ 新旧对比
| N | 旧 LP Δ (full-set, n=551) | 新 LP Δ (gf, max_LP, n=529) |
|---|--------------------------|----------------------------|
| 2 | −0.75 | −0.89 |
| 4 | −0.01 | +0.03 |
| 8 | +0.42 | +0.39 |
| 16 | +0.63 | +0.78 |
| 32 | +0.91 | +0.95 |

### 完整 N-scaling 指标（供 Paper Agent 用）
| N | n_gf | greedy | oracle | headroom | degen% | LP Δ | SJ Δ | FK Δ | EM Δ | VC Δ | Best Δ |
|---|------|--------|--------|----------|--------|------|------|------|------|------|--------|
| 2 | 529 | 0.6397 | 0.6832 | +4.4 | 42.7% | −0.89 | −2.72 | −2.72 | −2.72 | −2.66 | −0.89 |
| 4 | 529 | 0.6397 | 0.7421 | +10.2 | 21.0% | +0.03 | −0.31 | −0.40 | −0.74 | −2.16 | +0.03 |
| 8 | 529 | 0.6397 | 0.7848 | +14.5 | 11.0% | +0.39 | +0.20 | +0.15 | −0.77 | −2.87 | +0.39 |
| 16 | 529 | 0.6397 | 0.8169 | +17.7 | 7.4% | +0.78 | +0.24 | −0.02 | −0.06 | −3.95 | +0.78 |
| 32 | 529 | 0.6397 | 0.8396 | +20.0 | 4.0% | +0.95 | +0.35 | +0.65 | +0.22 | −4.35 | +0.95 |

### 关键变化
- Greedy F1: 0.614 (full-set) → 0.640 (gold-filtered)
- Oracle headroom 略增（移除 22 个无 gold 实例后信息密度更高）
- LP Δ 趋势不变：N≥4 时 LP 为最优信号，N=2 时所有信号均为负
- 脚注需要更新：n=551 → n=529, greedy F1 0.614 → 0.640

JSON 结果已保存: `/root/autodl-tmp/struct_self_consist_ie/output/n_scaling_gf_maxlp.json`

---
