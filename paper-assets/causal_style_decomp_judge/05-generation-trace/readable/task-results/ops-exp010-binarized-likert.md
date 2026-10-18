# ops exp010 binarized likert

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp010_binarized_likert_20260520T233854_result.json`
- **Structured JSON:** [`73c1076986216c3dd3b0.json`](../../sessions/73/73c1076986216c3dd3b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-010 完整结果

```
Loaded 100 scored records

============================================================
  Binarized Likert Sign Test (all, n=100)
============================================================
  formal > casual: 22
  casual > formal: 18
  Ties (equal):    60 (60.0%)
  Non-tie pairs:   40

  formal win rate (non-tie): 0.5500 (22/40)
  95% CI (Wilson):  [0.3983, 0.6929]
  Sign test p:      0.635828
  Significant:      NO (α=0.05)

  --- Comparison with Pairwise ---
  Pairwise (reference): 69.1% win rate, p=0.006
  Binarized Likert:     55.0% win rate, p=0.6358
  → Binarized Likert NOT significant: confirms pairwise structural advantage
  → C2 (Likert Blindspot) validated — forced choice matters, not just test choice

============================================================
  Binarized Likert Sign Test (NLI≥0.9, n=88)
============================================================
  formal > casual: 20
  casual > formal: 13
  Ties (equal):    55 (62.5%)
  Non-tie pairs:   33

  formal win rate (non-tie): 0.6061 (20/33)
  95% CI (Wilson):  [0.4368, 0.7532]
  Sign test p:      0.296206
  Significant:      NO (α=0.05)

============================================================
  Binarized Likert Sign Test (NLI≥0.85, n=89)
============================================================
  formal > casual: 20
  casual > formal: 13
  Ties (equal):    56 (62.9%)
  Non-tie pairs:   33

  formal win rate (non-tie): 0.6061 (20/33)
  Sign test p:      0.296206
  Significant:      NO (α=0.05)

============================================================
  Binarized Likert Sign Test (NLI≥0.8, n=89)
============================================================
  (same as NLI≥0.85)

============================================================
  Directional Breakdown (all records)
============================================================

  --- formal→casual (n=59) ---
  formal > casual: 9
  casual > formal: 14
  Ties (equal):    36 (61.0%)
  Non-tie pairs:   23

  formal win rate (non-tie): 0.3913 (9/23)
  Sign test p:      0.404873
  Significant:      NO

  --- casual→formal (n=41) ---
  formal > casual: 13
  casual > formal: 4
  Ties (equal):    24 (58.5%)
  Non-tie pairs:   17

  formal win rate (non-tie): 0.7647 (13/17)
  Sign test p:      0.049042
  Significant:      YES (α=0.05)
```

### 关键发现

1. **Tie rate 极高：60%**（100 对中 60 对 Likert 分数相同）——这是 Likert 量表的核心问题，pairwise 强制二选一不存在 tie

2. **全量 sign test：p=0.636，完全不显著**——同样用 sign test，binarized Likert 的 win rate 仅 55.0%，远低于 pairwise 的 69.1%/p=0.006。说明 sensitivity gap 不是统计检验选择的问题，而是测量结构本身的差异

3. **NLI 过滤后仍不显著**：NLI≥0.9 时 win rate 升到 60.6%，但 p=0.296，仍不显著。有效样本只剩 33 对

4. **方向不对称**：
   - formal→casual（59 对）：formal win rate 仅 39.1%，甚至反向偏——formal 原文降级为 casual 后分数没降反升
   - casual→formal（41 对）：formal win rate 76.5%，p=0.049，勉强显著——casual 原文升级为 formal 后分数确实上升

5. **C2 (Likert Blindspot) 得到验证**：即使将 Likert 分数 binarize 后用相同的 sign test，仍无法检出 pairwise 能检出的偏差。60% 的 tie rate 直接证明了 Likert 量表在 style bias 检测上的 sensitivity 不足是测量结构问题，不是统计方法问题。

---
