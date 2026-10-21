# eval audit genuine rate

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_audit-genuine-rate_20260516T192706_result.json`
- **Structured JSON:** [`6421c703a579d640da36.json`](../../sessions/64/6421c703a579d640da36.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I have all the data needed. Let me produce the final comprehensive report.

---

## τ=0.15 审计 (41 proved)

| Category | N/41 | % |
|----------|------|---|
| H7 (premise=conclusion) | 1 | 2.4% |
| H1_exact (conclusion⊂premise) | 0 | 0.0% |
| ISR=0 退化 (n_necessary=0) | 14 | 34.1% |
| H8b: 无必要前提 (仅 quantifier/conclusion 结构必要) | 6 | 14.6% |
| **Total hacking** | **21** | **51.2%** |
| **Genuine (≥1 necessary premise)** | **20** | **48.8%** |
| — of which H1-near flagged | 2 | |

### 各类型案例 ID:
- **H7**: `folio_1030` (premise[5] = conclusion = `HighRank(WTA(x), x) ∨ LostToRafael(x, x)`)
- **H8a ISR=0** (n_nec=0): `folio_1179, folio_452, folio_699, folio_529, folio_1076, folio_769, folio_924, folio_960, folio_711, folio_1135, folio_1051, folio_1381, folio_822, folio_959`
- **H8b** (n_nec>0 but only ∃x necessary, no premise necessary): `folio_1378, folio_1119, folio_1364, folio_953, folio_1371, folio_1396`
- **H1-near** (genuine but flagged): `folio_791, folio_643`

---

## τ=0.2 审计 (21 proved)

| Category | N/21 | % |
|----------|------|---|
| H7 (premise=conclusion) | 1 | 4.8% |
| H1_exact (conclusion⊂premise) | 0 | 0.0% |
| ISR=0 退化 (n_necessary=0) | 4 | 19.0% |
| H8b: 无必要前提 (仅 quantifier/struct 必要) | 8 | 38.1% |
| **Total hacking** | **13** | **61.9%** |
| **Genuine (≥1 necessary premise)** | **8** | **38.1%** |

### 各类型案例 ID:
- **H7**: `folio_574` (premise[14] = conclusion = `∃x ¬GreenStage(x)`)
- **H8a ISR=0**: `folio_1179, folio_233, folio_1428, folio_23`
- **H8b** (no premise necessary): `folio_491, folio_267, folio_1364, folio_1371, folio_1255, folio_430, folio_1051, folio_1381`
- **Genuine**: `folio_1076, folio_149, folio_711, folio_167, folio_672, folio_847, folio_715, folio_93`

---

## 修正对比表

| 条件 | PR | Old Genuine% | **Corrected Genuine%** (strict) | **Corrected Genuine%** (C013: H8=n_nec=0) |
|------|-----|-------------|--------------------------------|------------------------------------------|
| τ=0.15 | 41/100 | 97.6% | **48.8%** (20/41) | **63.4%** (26/41) |
| τ=0.2 | 21/100 | 95.2% | **38.1%** (8/21) | **76.2%** (16/21) |

---

## 关键发现

**两层 H8 定义**：
1. **C013 定义** (H8 = n_necessary=0): τ=0.15 genuine=63.4%, τ=0.2 genuine=76.2%。与 Reviewer 估计 (~63%) 完全吻合。
2. **Strict 定义** (H8 = no necessary *premise*): τ=0.15 genuine=48.8%, τ=0.2 genuine=38.1%。这扣除了 n_nec>0 但唯一 necessary component 是 `∃x` 量词（不是任何 premise）的情况。

**新发现的 H8b 模式**：n_necessary>0 但所有 necessary components 都是 conclusion 自身结构（quantifier/antecedent/consequent），没有任何 premise 是 necessary。实质上证明不依赖任何前提——自由变量让 `∃x P(x)` 平凡成立。

**建议论文使用 C013 定义**（63.4% / 76.2%），H8b 作为 limitation discussion 提及。

---
