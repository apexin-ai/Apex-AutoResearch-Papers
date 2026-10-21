# code verbosity 7method sensitivity

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_verbosity_7method_sensitivity_20260521T130722_result.json`
- **Structured JSON:** [`8877dc7eaa093eba6c2e.json`](../../sessions/88/8877dc7eaa093eba6c2e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过：

| Method | Statistic | p-value | Effect Size | Sig? |
|--------|-----------|---------|-------------|------|
| Paired t-test | 0.5163 | 0.607 | d=0.056 | No |
| Mann-Whitney U | 3868.0 | 0.578 | r=-0.046 | No |
| Ordinal logistic | 0.1592 | 0.575 | OR=1.173 | No |
| Cohen's d | — | — | 0.036 | No |
| Binarized χ² | 1.5512 | 0.213 | OR=2.162 | No |
| Likert ATE | 0.0581 | 0.691 | d=0.056 [-0.16, 0.27] | No |
| Bradley-Terry | 0.7732 | 0.0 | P(v)=77.3% [70.3, 84.3] | **Yes** |

结果符合预期：
- 6/6 Likert 方法全部 NS（p 远大于 0.05，effect size 均 negligible）
- BT 显著检出 verbosity bias（P(verbose)=77.3%, p<0.001, CI 不含 50%）
- 86 对 NLI-filtered pairs，JSON 格式正确，已保存到 `data/verbosity_7method_sensitivity.json`

---
