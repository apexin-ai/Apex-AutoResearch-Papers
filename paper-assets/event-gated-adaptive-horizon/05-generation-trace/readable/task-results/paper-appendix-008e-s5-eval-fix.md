# paper appendix 008e s5 eval fix

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_appendix_008e_s5_eval_fix_20260525T165455_result.json`
- **Structured JSON:** [`c93fbd4701d64a574184.json`](../../sessions/c9/c93fbd4701d64a574184.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

正文和 appendix 均引用 mean=775.6。验证：(876.7 + 597.1 + 853.1) / 3 = 2326.9 / 3 = 775.63，与 775.6 一致。

**Diff:**
```
- 008e\_v3 s5 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.60$\times$ & Healthy \\
+ 008e\_v3 s5 & Mitigation & trn & ON & 15 & 853.1 @105K & 0.60$\times$ & Healthy \\
```

修正完成：
- `appendix.tex` L57: eval 869.9 → 853.1
- 869.9 已从 appendix.tex 中完全移除（无其他出现）
- 正文 mean 775.6 = (876.7 + 597.1 + 853.1)/3 = 775.63，四舍五入一致
- 该行 NVE (0.60×) 和 outcome (Healthy) 未变，与 NVE 表 (L163: 008e\_v3\_s5 = 0.60) 一致

---
