# analysis table5 cross env validation

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_table5-cross-env-validation_20260527T173249_result.json`
- **Structured JSON:** [`04b7ac5aa0fabc4ba0a7.json`](../../sessions/04/04b7ac5aa0fabc4ba0a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。Table 5 有 7 个问题：

**需要修复的错误：**
1. **Cheetah trigger std ±33.9** 用了 population std（其他所有行用 sample std）→ 应为 **±47.9**
2. **Walker CIVO "8/8"** 无数据支撑 → CSV 是 **5/5**，complete table 有 6 个 trigger seed 也全部 CIVO

**跨表不一致：**
3. **Cheetah baseline 593.9** 来自 exp_023 系列（5 seeds），但 complete table 和 results.tex 用 exp_077/083（mean=**446.1**）。差 ~148 分。
4. **Walker baseline s3/s4** (869.03, 922.80) 不在 appendix Table 4 中，是未文档化的实验。
5. Eval 和 NVE 的 seed 数不统一（Walker trigger: eval N=3, NVE N=5）。

**新数据未纳入：**
6. exp_097 Cheetah trigger s3: eval=61.67（第 3 个 trigger seed）
7. exp_092/093 Cheetah control s1/s2: eval=77.26/151.18（2 个新 control seed）

报告中给出了三个修正方案（minimal fix / 对齐 complete table / 纳入新数据），详见 `artifacts/_project/report/table5_full_validation.md`。

---
