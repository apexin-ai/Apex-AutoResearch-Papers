# ssh update ci coverage appendix

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_update-ci-coverage-appendix_20260524T091324_result.json`
- **Structured JSON:** [`c7acd16a3f42b6ae2884.json`](../../sessions/c7/c7acd16a3f42b6ae2884.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Appendix Q (CI Coverage) 已更新，编译通过（仅有图片文件缺失的预期错误，无语法错误）。

**更新内容：**
- 旧数据（exp-009）：N=8 (49 seeds) θ=90.1%, c_n=67.9%; N=50 (50 seeds) c_n=71%
- 新数据（exp-017）：N=8 (200 seeds) θ=90.0%, c_n=65.6%; N=20 (51 seeds) θ=89.1%, c_n=64.7%
- 叙事重点：c_n 的 ~30pp 欠覆盖在 N=8→20 之间几乎不变，确认 undershoot 是结构性的（Murphy-Topel 渐近校正收敛慢 + HalfNormal 先验边界约束），而非样本量不足

---
