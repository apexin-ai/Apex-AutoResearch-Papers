# ops verify 15s1s2 fixed

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-15s1s2-fixed_20260522T202953_result.json`
- **Structured JSON:** [`89bb98a7521f02756245.json`](../../sessions/89/89bb98a7521f02756245.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果完全一致：

```
15% s1 θ-fixed: old=4.77, recalc=4.7695 (lz_fixed=10.1196, CI=[3.97, 7.79])
15% s2 θ-fixed: old=7.79, recalc=7.7869 (lz_fixed=11.8704, CI=[6.51, 13.05])

一致性判断：一致
```

验证确认：
- Clean baseline 完全匹配 (mean=7.3522, std=0.5802, n=10)
- θ_fixed = -0.1022（10个clean seed的MLE均值）
- 15% s3 也精确匹配 JSON 中的 7.9938
- s1 和 s2 使用了相同的基线、相同的方法、相同的 theta，不存在 reviewer 担心的"不同基线"问题

s1 (d=4.77) 和 s2 (d=7.79) 的差异是真实的 seed 间变异——不同 contamination seed 导致被污染的题目不同，从而 lz_fixed 不同。这与 s3 (d=7.99) 幅度接近 s2，进一步说明 s1 是偏低的 seed，而非方法不一致。

---
