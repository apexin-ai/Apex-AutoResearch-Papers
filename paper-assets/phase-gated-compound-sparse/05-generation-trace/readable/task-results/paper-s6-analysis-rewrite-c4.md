# paper s6 analysis rewrite c4

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_s6_analysis_rewrite_c4_20260514T092438_result.json`
- **Structured JSON:** [`a219c1b3569a3131e9a3.json`](../../sessions/a2/a219c1b3569a3131e9a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件均已验证，内容正确。

---

### §6 Analysis 重写摘要

**结构变化**: 原来的 "Entropy-Discrimination Collapse" 单一机制 → 两层机制框架：

- **§6.1 Discrimination Collapse** (primary) — Gini/CV 下降，16/16 条件方向一致（两模型×4 sparsity×2 策略）。新增 Table `discrimination-metrics`（8 行：importance-based eviction 下的 Gini Δ 和 CV Δ）。文中额外引用 random eviction 的 Gini 一致性作为"head pruning per se"证据。
- **§6.2 Entropy Redistribution** (secondary, model-dependent) — DeepSeek 4/4 一致负值，Qwen 2/4 负值 + s025 反转 (+0.045, 22/30 positive) + s030 近零。新增 Table `entropy-deltas`（8 行）。s025 反转的三 phase 一致性（+0.042/+0.034/+0.017）诚实报告，mid-phase power 作为 confound 之一但非唯一解释。
- **§6.3 Implications** — "Architecture generality" 加了 entropy 模型依赖的 qualifier；"Reframing" 保留 "emergent phase-strategy interaction" 必用短语。

**移除**: 两个 `\placeholder{}` 全部替换为实际数据表格。原 §6.1 理论叙述（"high-sparsity phase, attention is concentrated..."）删除，由实证数据直接支撑。

### Conclusion 修改

1. **C4 条目** (line 18): "Entropy-discrimination collapse...partially confirmed" → discrimination collapse robustly confirmed (Gini/CV 16 conditions) + entropy redistribution partially replicates (2/4 Qwen)
2. **Limitations 段** (line 25-26): 原"entropy-discrimination"→"discrimination"；新增一句显式承认 Qwen 跨模型不一致

### Placeholder 状态

§6 **零 placeholder**。所有数字均追溯到 `c4_entropy_deepseek` / `c4_entropy_qwen` exp_id，24 个 table cell 已注册 provenance。

---
