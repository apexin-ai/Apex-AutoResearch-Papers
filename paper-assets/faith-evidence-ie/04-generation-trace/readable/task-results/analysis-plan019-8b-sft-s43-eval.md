# analysis plan019 8b sft s43 eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan019_8b_sft_s43_eval_20260519T154301_result.json`
- **Structured JSON:** [`9cd7b040e63636205de9.json`](../../sessions/9c/9cd7b040e63636205de9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

**8B SFT s43 Ign-F1 = 0.5324**（三 seed 最高）

**3-seed 8B SFT: mean = 0.5019 ± 0.0372**

关键影响：

- **Claim 3 "1.7B RSFT surpasses 8B SFT" 统计上不成立。** 差值仅 +0.0103，t=0.48, p≈0.34。1.7B RSFT 的 0.5122 甚至低于 8B SFT 最佳 seed（0.5324）。建议弱化为 "comparable / on par with"。
- **8B RSFT vs 8B SFT (+0.0395)** 更有说服力，但因 SFT 方差过大（0.037），Welch's t=1.81 仍只 p≈0.10。建议补 RSFT s43 凑齐 3-seed。
- **稳定性是可独立 claim 的发现：** SFT std=0.037 vs RSFT std=0.005，方差比约 50:1。RSFT 的 reward filtering 显著降低了 seed 敏感性。

报告已写入 `artifacts/plan019_8b_sft_s43_eval_analysis.md`。

---
