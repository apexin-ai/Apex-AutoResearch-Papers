# analysis m004 persist batch2

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_m004_persist_batch2_20260518T111756_result.json`
- **Structured JSON:** [`96c739d5cacbf0af1748.json`](../../sessions/96/96c739d5cacbf0af1748.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

持久化完成。以下是完整结果：

---

## 条件 4: Scale 1.4B s43

| Pair | Naive | Diff | Thresh | PG_fwd_p | PG_fwd | PG_rev_p | PG_rev | TY |
|------|-------|------|--------|----------|--------|----------|--------|-----|
| ent→d1 | Y | Y | Y | 0.0022 | ✓ | 0.1546 | ✗ | Y |
| ent→d2 | Y | Y | Y | 0.0046 | ✓ | 0.1460 | ✗ | N |
| ent→d3 | Y | Y | Y | 0.0080 | ✓ | 0.1254 | ✗ | N |
| ent→ppl | Y | N | Y | 0.5485 | ✗ | 0.2839 | ✗ | N |
| ece→d1 | Y | Y | Y | 0.0044 | ✓ | 0.0644 | ✗ | Y |
| ece→d2 | Y | Y | Y | 0.0100 | ✓ | 0.0372 | ✓ | Y |
| ece→d3 | Y | Y | Y | 0.0142 | ✓ | 0.0224 | ✓ | Y |
| ece→ppl | Y | N | Y | 0.5035 | ✗ | 0.3765 | ✗ | N |

**Summary**: Naive=8/8, Diff=6/8, Thresh=8/8, PG_fwd=6/8, PG_rev=2/8, TY=4/8, K≥4=6/8

**Old**:   Naive=8/8, Diff=6/8, Thresh=8/8, PG_fwd=6/8, PG_rev=2/8, TY=4/8, K≥4=6/8

**Flip: 无** — n_perm=5000 与旧值完全一致。

---

## 条件 5: C4 s42

| Pair | Naive | Diff | Thresh | PG_fwd_p | PG_fwd | PG_rev_p | PG_rev | TY |
|------|-------|------|--------|----------|--------|----------|--------|-----|
| ent→d1 | Y | Y | Y | 0.0082 | ✓ | 0.4983 | ✗ | N |
| ent→d2 | Y | Y | Y | 0.0126 | ✓ | 0.3661 | ✗ | N |
| ent→d3 | Y | Y | Y | 0.0262 | ✓ | 0.2889 | ✗ | N |
| ent→ppl | Y | N | Y | 0.6753 | ✗ | 0.1428 | ✗ | N |
| ece→d1 | Y | Y | Y | 0.0012 | ✓ | 0.0046 | ✓ | Y |
| ece→d2 | Y | Y | Y | 0.0036 | ✓ | 0.0022 | ✓ | Y |
| ece→d3 | Y | Y | Y | 0.0078 | ✓ | 0.0024 | ✓ | Y |
| ece→ppl | Y | N | Y | 0.6409 | ✗ | 0.3907 | ✗ | N |

**Summary**: Naive=8/8, Diff=6/8, Thresh=8/8, PG_fwd=6/8, PG_rev=3/8, TY=3/8, K≥4=6/8

**Old**:   Naive=8/8, Diff=8/8, Thresh=6/8, PG_fwd=8/8, PG_rev=4/8, TY=4/8, K≥4=7/8

⚠️ **多处 flip 检测到**：
- **Diff**: 8/8 → 6/8（ent→ppl, ece→ppl 两对翻 N）
- **Thresh**: 6/8 → 8/8（翻转方向相反，两对翻 Y）
- **PG_fwd**: 8/8 → 6/8（ent→ppl, ece→ppl 翻 N）
- **PG_rev**: 4/8 → 3/8（1 对翻 N）
- **TY**: 4/8 → 3/8（1 对翻 N）
- **K≥4**: 7/8 → 6/8

旧值可能用的是不同的 n_perm（1000）或不同的 xcorr_lag/granger_lag 参数。perplexity pairs 在 PG 中一致不显著，这是 n_perm=5000 下的稳定结论。

---

## 条件 6: C4 s43（首次完整出数）

| Pair | Naive | Diff | Thresh | PG_fwd_p | PG_fwd | PG_rev_p | PG_rev | TY |
|------|-------|------|--------|----------|--------|----------|--------|-----|
| ent→d1 | Y | Y | Y | 0.0072 | ✓ | 0.5893 | ✗ | N |
| ent→d2 | Y | Y | Y | 0.0374 | ✓ | 0.7357 | ✗ | N |
| ent→d3 | Y | Y | Y | 0.0500 | ✓ | 0.8844 | ✗ | N |
| ent→ppl | Y | N | Y | 0.5531 | ✗ | 0.4231 | ✗ | N |
| ece→d1 | Y | Y | Y | 0.0022 | ✓ | 0.3517 | ✗ | Y |
| ece→d2 | Y | Y | Y | 0.0098 | ✓ | 0.1614 | ✗ | Y |
| ece→d3 | Y | Y | Y | 0.0290 | ✓ | 0.0770 | ✗ | Y |
| ece→ppl | Y | N | Y | 0.4903 | ✗ | 0.9124 | ✗ | N |

**Summary**: Naive=8/8, Diff=6/8, Thresh=8/8, PG_fwd=6/8, PG_rev=0/8, TY=3/8, K≥4=6/8

**Old**: TBD（首次完整出数）— 以此为 n_perm=5000 新基准。

注意 ent→d3 的 PG_fwd_p=0.0500 恰好在边界。

---

### 产出文件

```
artifacts/M004_nperm5000/
├── pythia14b_s43/
│   ├── analysis_log.txt
│   └── generalize_5method_results.json
├── pythia1b_c4_s42/
│   ├── analysis_log.txt
│   └── generalize_5method_results.json
├── pythia1b_c4_s43/
│   ├── analysis_log.txt
│   └── generalize_5method_results.json
└── table7_canonical_8pairs.txt
```

**关键发现**：条件 4（Scale 1.4B s43）n_perm 从 1000→5000 无任何 flip。条件 5（C4 s42）有多处 flip，旧值可能基于不同参数。条件 6 是新基准。三个条件的 perplexity pairs 在 PG 中一致不显著。

---
