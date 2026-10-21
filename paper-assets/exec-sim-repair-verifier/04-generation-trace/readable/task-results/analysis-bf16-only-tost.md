# analysis bf16 only tost

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bf16-only-tost_20260519T100402_result.json`
- **Structured JSON:** [`f8974ac598bde6df0fbe.json`](../../sessions/f8/f8974ac598bde6df0fbe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## TOST 结果

```
bf16-only TOST (3 seeds, df=2): mean=-0.45pp, SE=0.98pp, TOST p=0.128 at ±2pp, equivalent=NO
```

3 seeds 的方差太大（SD=1.70pp），在 df=2 下无法在 ±2pp margin 内建立等价性。瓶颈在 lower test（p=0.128），即不能排除真实差异低于 -2pp 的可能。

## BibTeX

```bibtex
@article{lakens2017equivalence,
  author    = {Lakens, Daniel},
  title     = {Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses},
  journal   = {Social Psychological and Personality Science},
  year      = {2017},
  volume    = {8},
  number    = {4},
  pages     = {355--362},
  doi       = {10.1177/1948550617697177}
}

@article{hoenig2001abuse,
  author    = {Hoenig, John M. and Heisey, Dennis M.},
  title     = {The Abuse of Power: The Pervasive Fallacy of Power Calculations for Data Analysis},
  journal   = {The American Statistician},
  year      = {2001},
  volume    = {55},
  number    = {1},
  pages     = {19--24},
  doi       = {10.1198/000313001300339897}
}
```

两篇均已通过 SAGE Journals / Taylor & Francis 验证真实存在。

---
