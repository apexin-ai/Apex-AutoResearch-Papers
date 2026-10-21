# analysis 4seed fisher prep

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_4seed-fisher-prep_20260516T153855_result.json`
- **Structured JSON:** [`995da11dad162c9e1a28.json`](../../sessions/99/995da11dad162c9e1a28.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果出来了，但 p 值与预期不一致。3-seed pooled Fisher exact test 得到的是 **p=0.035 (one-sided)**，而非预期的 ≈0.091。

实际输出：

```
Seeds: [42, 43, 44] (3-seed pooled)

Seed    obs_only SR       argmin SR         Δ
42      44/200 = 22.0%    24/200 = 12.0%    +10.0%
43      32/200 = 16.0%    34/200 = 17.0%    -1.0%
44      32/200 = 16.0%    26/200 = 13.0%    +3.0%
POOLED  108/600 = 18.0%    84/600 = 14.0%    +4.0%

Fisher exact test (one-sided: obs > argmin)
Odds ratio: 1.3484
p (two-sided): 0.069931
p (one-sided): 0.034966

→ p = 0.0350 < 0.05 → SIGNIFICANT (Narrative A)
```

p≈0.091 可能来自不同的检验方法（如 per-seed Fisher 合并、z-test with continuity correction 等）。标准的 pooled counts Fisher exact test 给出 p=0.035。

脚本路径：`/root/acr-vla-conformal-refinement/analysis/pooled_fisher_test.py`

用法：
- `python pooled_fisher_test.py` — 自动检测所有可用 seeds
- `python pooled_fisher_test.py 42 43 44` — 指定 seeds
- seed45 完成后直接 `python pooled_fisher_test.py` 即可跑 4-seed 分析

---
