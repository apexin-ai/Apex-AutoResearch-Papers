# analysis parse failure denominator check

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_parse_failure_denominator_check_20260516T181758_result.json`
- **Structured JSON:** [`509b2e6dd92cf3639ebf.json`](../../sessions/50/509b2e6dd92cf3639ebf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已完成：`artifacts/parse_failure_denominator_analysis.md`

核心结论：

1. **当前计算方式**：violation rates 分母仅含 parsed docs（parse failure 文档被 `continue` 跳过，不进分母）
2. **All-set 调整公式**：`all_set_rate = current_rate × (1 − parse_fail_rate)`
3. **差异不 material**：
   - 最大影响案例 Llama DocRED ZS（parse fail 9.12%）：DR 从 2.55% → 2.32%，降 0.23 pp
   - FT 实验绝对调整量 < 0.01 pp
   - Constrained vs Unconstrained 的相对 reduction 比例几乎不变（如 Qwen DocRED FT 始终 98.7%）
4. **建议**：保持 parsed-only 方式，论文注明分母定义并单独报 parse failure rate

---
