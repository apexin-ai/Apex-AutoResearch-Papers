# analysis table1 numerical audit

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_table1_numerical_audit_20260521T194500_result.json`
- **Structured JSON:** [`a1cc7058d8f50d034595.json`](../../sessions/a1/a1cc7058d8f50d034595.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 审计结果：Table 1 数值全部匹配，0 处不一致

全量交叉验证了 20 个数值条目（4 模型 × 5 条件）+ 6 条脚注 + 所有 σ 值 + † / ‡ 标记：

| 检查项 | 数量 | 结果 |
|--------|------|------|
| 主表准确率 | 20 | ✅ 全部匹配 |
| 脚注 per-seed 值 | 6 条 | ✅ 全部匹配 |
| σ 计算 | 16 个 | ✅ 样本标准差正确 |
| † / ‡ 标记 | 4 处 | ✅ 与 seed 数量一致 |

**两个边界注意点**（不影响正确性）：
1. Registry 存 CL-13B no_trace 为 `0.765`（3 位截断），原始 eval 为 `0.76471`，论文 76.47% 正确
2. Qwen-7B ae_only σ 精确值 0.485，论文写 0.49，处于舍入边界

报告已注册为 artifact `table1_numerical_audit`（art_20260521_7d103d）。可安全提交。

---
