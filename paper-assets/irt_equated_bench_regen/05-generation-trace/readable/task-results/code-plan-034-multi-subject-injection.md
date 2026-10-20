# code plan 034 multi subject injection

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_034_multi_subject_injection_20260521T154505_result.json`
- **Structured JSON:** [`1f8d0c9910037d2df3c0.json`](../../sessions/1f/1f8d0c9910037d2df3c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Plan 034 完成。核心结果：

**Proposition 1 的 validity boundary 在 k ≈ 5–10 个 subjects：**

- **k ≤ 5**（≤ 8.8% subjects 被污染）：non-target ΔFPR < 0.007，与噪声无异。Proposition 1 实际成立。
- **k = 10**（17.5%）：p ≥ 0.3 时 ΔFPR 开始显著（+0.026 ~ +0.069）。
- **k = 20**（35.1%）：ΔFPR 大幅膨胀（p=0.5 时 +0.167，绝对 FPR 从 0.31 升到 0.49）。

其他发现：
- 低注入强度 p=0.1 在所有 k 值下都 robust（ΔFPR ≈ 0）
- Target-subject TPR 随 k 增大而下降（matching variable 吸收了部分 DIF 信号）

所有输出文件已保存并注册：脚本、3 个 CSV（target results / non-target FPR / summary）、report。

---
