# paper headline consistency verify

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_headline_consistency_verify_20260516T042410_result.json`
- **Structured JSON:** [`110469f5c4379728811b.json`](../../sessions/11/110469f5c4379728811b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## PASS — 全文数字一致性验证通过

**旧数字（n=50 pilot）**：`0.32`, `9.94`, `0.048`, `2.619` — 在所有 .tex 文件和 paper_framing.md 中**零匹配**，已完全清除。

**新数字（n=500 正式）出现位置**：

| 数字 | 文件 |
|------|------|
| DS 0.39 (s015) | abstract.tex:4, introduction.tex:14/23, results.tex:19/42/117, appendix_moved.tex:27/83, appendix_robustness.tex:42/82, appendix_disc_analysis.tex:106 |
| DS 8.48 (s030) | abstract.tex:4, introduction.tex:14/23, results.tex:19/51/120, appendix_moved.tex:83, appendix_robustness.tex:45/85 |
| QW 0.07 (s015) | abstract.tex:6, introduction.tex:15/24, results.tex:55/117, appendix_moved.tex:84, appendix_robustness.tex:194 |
| QW 3.16 (s030) | abstract.tex:6, introduction.tex:15/24, results.tex:64/120, appendix_moved.tex:84/100, appendix_disc_analysis.tex:52(间接) |

**paper_framing.md**：更新头标注明 n=500 数值（DS 0.39/1.21/3.99/8.48; QW 0.07/0.31/1.07/3.16），与论文一致。

---
