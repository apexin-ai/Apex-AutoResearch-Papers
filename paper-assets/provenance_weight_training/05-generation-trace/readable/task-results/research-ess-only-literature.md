# research ess only literature

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ess_only_literature_20260515T125335_result.json`
- **Structured JSON:** [`aa965da58b5452b234cb.json`](../../sessions/aa/aa965da58b5452b234cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 memory.md 的 `## ESS-only 文献联动` 小节。核心结论：

**literature_map 中 4 篇已有论文**（Vehtari/PSIS、Wang/收敛理论、Kimura/IS survey、Drayson/竞争者）均与 ESS 约束相关。

**补充 2 篇新论文**：
- **Elvira et al. 2022** (ISR)：Kish ESS 近似作为单一指标不可靠，多重假设下失效
- **Ionides 2008** (JCGS)：过度截断（over-truncation）增加 bias，最优截断率为 √n

**文献一致支持 min-intervention > max-intervention**：ESS-only 等价于 aggressive truncation（仅有 ESS 下限约束，b 可无限增长），缺少对权重质量的直接保证。Dual-constraint 通过 α_eff ≥ τ 补充了 ESS 约束的理论缺陷。

**建议**：在 literature_map.yaml 中新增 Elvira et al. 2022 和 Ionides 2008 两个 method-component 条目。

---
