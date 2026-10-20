# research next batch planning

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_next-batch-planning_20260521T061905_result.json`
- **Structured JSON:** [`421df4510b0fc5ff1610.json`](../../sessions/42/421df4510b0fc5ff1610.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已生成并注册。核心发现：

**截断审计:**
- **Qwen 8B SFT**: 31.8% vs 22.8% (9pp 不对称) — D139 确认，@1024 tax 不可信
- **Qwen 1.7B SFT**: 32-48% with-evi vs 51% no-evi — 两边都极高，@2048 刚完成 s42：ign_f1=0.4806, trunc 降至 27.1%
- **14B RSFT**: 10.7% vs 10.8% — 完美对称，@1024 tax=-4.54pp 可信
- **LLaMA RSFT**: 16-17% vs 18-19% — 2pp 小不对称，@1024 tax=-1.14pp 可信
- **1.7B RSFT**: 24-25%，显著低于 SFT (32-48%)

**Matched@2048 状态:**
- LLaMA SFT 3-seed: ✅ 全完成，fair_tax 全负 (evidence helps)
- 1.7B SFT s42: ✅ 刚完成，tax=-8.81pp
- 14B RSFT @2048: 🔄 ~30min
- LLaMA RSFT s42 @2048: 🔄 ~25min
- 8B Qwen SFT @2048: 🔄 ~2.5h (with-evi)，**no-evi 缺失**

**立即可做:**
- cuda:2 已空闲 → 可提交 **8B SFT no-evi@2048**（Tier 1 最高优先）
- cuda:0/1 约 30min 后释放 → 可提交 LLaMA RSFT s43/s44 with-evi@2048

---
