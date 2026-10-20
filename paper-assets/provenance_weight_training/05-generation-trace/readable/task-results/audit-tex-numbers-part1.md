# audit tex numbers part1

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_tex_numbers_part1_20260524T042835_result.json`
- **Structured JSON:** [`7f6933563ba7250b7806.json`](../../sessions/7f/7f6933563ba7250b7806.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告已保存到 `artifacts/audit_part1_numbers.md`。

**汇总**: 检查 ~124 个定量数字，发现 **6 个问题**：

| # | 严重度 | 问题 |
|---|--------|------|
| 1 | **中** | results.tex L10: "4.7× higher variance" 实际是标准差比，方差比为 ~22× → 改 "variance" → "standard deviation" |
| 2 | 低 | intro L22: ≈5.9× sharpening ratio vs Figure caption overall mean ratio ≈3.9×，定义不明 |
| 3 | 低 | results.tex L124: gap 0.040 (B=4) vs 主表算得 0.054 |
| 4 | 低 | results.tex L95: ESS-only ρ=0.6 mean 论文 17.763 vs registry ~17.765 |
| 5 | 低 | results.tex L109: 2.7× ECE gap 实际为 2.62 |
| 6 | 低 | experiments.tex L3: 55.6% 文档比例 vs 均值推算 55.1% |

**#1 建议提交前必须修复**（reviewer 可能直接指出术语错误）。其余为低严重度，建议有时间时确认来源。

跨位置一致性（abstract ↔ intro ↔ results ↔ tables）全部通过，ROADMAP 交叉验证全部通过。

---
