# audit tex numbers part2

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_tex_numbers_part2_20260524T042846_result.json`
- **Structured JSON:** [`34bc286507b2a0a94092.json`](../../sessions/34/34bc286507b2a0a94092.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。158 个定量数字的追溯结果：

**需要提交前修复的 2 个问题**:

1. **确认错误** — `appendix.tex` L487: "compared to ~2% at ρ=0.4" 应为 **~6%**。results.tex §4.3 明确报告 5.8%，per-seed table 确认 5.7%−5.9%。

2. **p-value 精度不一致** — `checklist.tex` L48 写 p=0.004 (full-precision)，而 results/conclusion 统一用 p=0.010 (3dp-rounded)。建议统一。

**5 个可追溯性缺口**（非数值错误）：τ=0.8 from-scratch seeds、detector table TF-IDF at τ=0.8、Llama MMLU/HellaSwag 指标、hybrid ρ=0.6 (17.530 vs registry 17.526) 无法清晰映射到 registry experiment_id。

所有核心结论数字（Δ=−0.020, Δ=−0.032, >95%, 1.0×−3.4×, p_BH values）跨文件完全一致。报告已写入 `artifacts/audit_part2_numbers.md`。

---
