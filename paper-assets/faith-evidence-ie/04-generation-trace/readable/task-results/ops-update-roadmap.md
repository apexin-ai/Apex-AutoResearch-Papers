# ops update roadmap

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_update_roadmap_20260519T171259_result.json`
- **Structured JSON:** [`be77f19c98f03c3180ce.json`](../../sessions/be/be77f19c98f03c3180ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

ROADMAP.md 已更新。主要变更：

- **Scaling table**: 新增 14B 行 (0.5507)，8B SFT 从 2-seed 0.4866 更新为 3-seed 0.5019，4B 加入 D112 Method B 结果 (0.5152)，8B Δ 从 +5.48pp 修正为 +3.95pp
- **D112**: 标记完成，ign_f1=0.5152 (+4.18pp over s44 baseline)
- **14B evidence tax (D117)**: tax=0.03pp≈0，14B 容量足够
- **1.7B claim (D118)**: "surpasses" 降级为 "comparable"，variance stabilization 独立化
- **Tier 1 实验**: D112、8B SFT s43、14B SFT 全部标记 ✅；8B RSFT s43 移入 Tier 2
- **GPU 分布**: 更新为当前状态（cuda:2 空闲）
- **关键风险**: D112 标记已解决，1.7B/14B 风险项更新为最新结论

---
