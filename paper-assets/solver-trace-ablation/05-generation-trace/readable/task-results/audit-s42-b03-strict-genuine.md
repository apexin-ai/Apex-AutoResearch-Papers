# audit s42 b03 strict genuine

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_s42-b03-strict-genuine_20260518T094352_result.json`
- **Structured JSON:** [`1b532eac40bcab01491a.json`](../../sessions/1b/1b532eac40bcab01491a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

12 H1, 5 genuine confirmed。现在分析这 5 个 genuine 样本的谓词。

```
=== s42 β=0.3 strict genuine audit ===
Total proved: 17
H1 (exact match): 12
H7: 0
H8: 0
Content-independent (in H1 bucket): 1 (folio_888, uses G/W/C/P/A single-letter predicates)
Genuine (taxonomy): 5

Genuine 样本明细:

  Sample 1 — Idx 30, folio_769 (ISR=0.125)
    predicates=[Advocate, Tipped, FederalMinWageEntitled, WhiteCollarWorker, Lawyer]
    content_dependent=True
    Notes: conclusion extends P5 with extra conjunct, requires reasoning

  Sample 2 — Idx 45, folio_1371 (ISR=0.231)
    predicates=[IsPet, IsGhost, IsCat, IsDog, Barks, IsDead, IsAlive]
    content_dependent=True
    Notes: combines P0+P4 to derive disjunction, genuine multi-step reasoning

  Sample 3 — Idx 54, folio_499 (ISR=0.250)
    predicates=[IsRacehorse, IsInRace, IsHorse, IsSafeForRider, DetroitCity]
    content_dependent=True
    ⚠️ H1-near: conclusion = P4 with conjunction order swapped (IsHorse∧IsInRace vs IsInRace∧IsHorse)

  Sample 4 — Idx 69, folio_755 (ISR=0.714)
    predicates=[Rec, NegRev, Rating, TakeOut, Popular, Popularity]
    content_dependent=True
    Notes: abbreviated but semantic (Rec=Recommended, NegRev=NegativeReview); highest ISR, requires multi-premise reasoning

  Sample 5 — Idx 70, folio_167 (ISR=0.250)
    predicates=[LeaderOfCountryForLife, HasPower, IsKing, IsQueen, IsFemale, IsMale, Elizabeth]
    content_dependent=True
    ⚠️ H1-near: conclusion = P0 instantiated with constant "Elizabeth" (trivial universal instantiation)

Strict genuine (genuine AND content-dependent) = 5/17 (29.4%)
```

**关键发现：**

1. **5 个 genuine 全部 content-dependent**——1 个 content-independent 样本 (folio_888) 在 H1 bucket 内，不影响 genuine 计数。

2. **但 5 个中有 2 个是 H1-near**（C013 规定保留为 genuine 但单独标记）：
   - folio_499：conclusion = premise 的 conjunction 重排序
   - folio_167：conclusion = premise 的 universal instantiation
   
3. **真正需要多步推理的 genuine 只有 3 个**：folio_769、folio_1371、folio_755。

如果区分 strict-genuine 和 H1-near：**strict genuine (excluding H1-near) = 3/17 (17.6%)**。

---
