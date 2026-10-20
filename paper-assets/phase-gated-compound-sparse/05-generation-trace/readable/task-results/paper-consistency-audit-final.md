# paper consistency audit final

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_consistency_audit_final_20260514T112604_result.json`
- **Structured JSON:** [`a76ab49431577061c86e.json`](../../sessions/a7/a76ab49431577061c86e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审查完成。报告写入 `artifacts/consistency_audit_final.md`。

核心发现：

**❌ 必须修复（1项）：**
- Table 4 (cross-model) Qwen s020 值：论文写 0.24，数据源是 0.234979 → 应为 0.23

**⚠️ 需要决策（2项）：**
1. **Table 5 (cohens-d) 数据源冲突**：论文使用 `rebootstrap_b10000_results.json`，而非 `canonical_bf16_stats.json`。两者 B=10000 但随机种子不同，导致 6 个 Δ̃/CI 值有差异。最关键的是 Qwen s015 CI：rebootstrap 跨零（→ marginal），canonical 不跨零。d_z CI 跨零支撑 "marginal" 判断，但 Δ̃ 源需要统一。
2. **s035 II_high = 0.105**（discussion 引用）不在任何 canonical JSON 中，需补充数据源或注释。

**✅ 其余 83 个数值全部一致。** 所有 framing 合规项均通过（cross-model 而非 cross-architecture、7/8 FAIL、emergent phase-strategy interaction、Qwen s015 marginal、C4 entropy 仅在 §6）。

---
