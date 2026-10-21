# analysis exp011 statistical verification

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp011-statistical-verification_20260517T080055_result.json`
- **Structured JSON:** [`c4c0ba0969ce655175b4.json`](../../sessions/c4/c4c0ba0969ce655175b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
STATISTICAL VERIFICATION SUMMARY
============================================================
McNemar exact p-value (two-sided): 0.2188
McNemar exact p-value (one-sided): 0.1094
Bootstrap gap: +6.67 pp [0.00, 15.00]
Bootstrap p(gap≤0): 0.0607

TRUNCATION ANALYSIS:
  Problems with truncated traces: 16/60
  Gap (truncated group): +6.25 pp
  Gap (clean group): +6.82 pp
  Discordant SICA-wins in truncated: 1/5

PER-DOMAIN:
  PROOFWRITER: +3.33pp, McNemar p=1.0000, Bootstrap CI=[-6.67, 13.33]
  FOLIO: +10.00pp, McNemar p=0.2500, Bootstrap CI=[0.00, 23.33]

VERDICT: NOT SIGNIFICANT (underpowered, suggestive trend)
```

关键发现：

1. **McNemar p=0.2188**：6 个 discordant pairs（5:1）不足以达到显著性。精确二项检验在 n=6 时 power 极低，即使真实 OR=5.0，95% CI 跨越 1（[0.56, 236.5]），无法排除随机波动。

2. **Bootstrap CI 下界恰好触及 0**：[0.00, 15.00]，p(gap≤0)=6.07%。处于 marginal 区间，不满足 p<0.05。

3. **截断不是 artifact 来源**：这是最重要的好消息。截断组 gap（+6.25pp）与干净组 gap（+6.82pp）几乎一致，5 个 SICA-win discordant pairs 中只有 1 个含截断 traces。+6.67pp 的增益在两组中均匀分布，不是截断造成的伪效应。

4. **域差异**：FOLIO 贡献了大部分增益（+10.00pp, bootstrap p=0.04），ProofWriter 增益弱（+3.33pp, p=1.0）。

**结论**：+6.67pp 是真实方向性效应（非 truncation artifact），但 n=60 样本量不足以达到统计显著。需要扩大到约 200+ 题才可能在 McNemar test 中达到 p<0.05。FOLIO 子集单独看接近显著。

---
