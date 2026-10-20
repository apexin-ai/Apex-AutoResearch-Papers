# research plan 001 literature linkage

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_plan_001_literature_linkage_20260515T070550_result.json`
- **Structured JSON:** [`0d24e4fd103f3728ad7e.json`](../../sessions/0d/0d24e4fd103f3728ad7e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**文献联动结论：plan_001 的发现与现有文献高度一致，无矛盾。**

新增 4 篇论文到 literature_map.yaml（12→16 篇）：

| 论文 | 关系 | 核心证据 |
|------|------|---------|
| Ferrando et al. 2025 (scratchpad) | **强支持** | Compact scratchpad（仅变化量）≥ Regular（全部值），直接印证 actual/expected 冗余 |
| TraceCoder (ICSE 2026) | 支持 | 选择性 probe 优于全量 trace，Pass@1 +34.43% |
| TraceRepair (2026) | 支持 | Critical variables snapshots > 全量，392 缺陷修复 |
| Demystifying Errors (2025) | 间接支持 | LLM 值追踪能力弱，提供了"为什么值冗余"的机制解释 |

**plan_001 的独特贡献定位**：现有文献在 code repair / output prediction 上验证了 trace 信息精简有效，plan_001 首次在 **verdict classification** 场景验证，且降幅几乎为零（99.4% vs 99.2%）。

产出：
- `artifacts/plan_001_literature_linkage.md` — 完整分析报告
- `literature_map.yaml` — 已更新

---
