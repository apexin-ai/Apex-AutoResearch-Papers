# write experiments skeleton

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_write_experiments-skeleton_20260514T225046_result.json`
- **Structured JSON:** [`4ee3aa15027ea81937f2.json`](../../sessions/4e/4ee3aa15027ea81937f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `artifacts/paper_drafts/experiments_v1.md` 并注册（`art_20260514_25f2bc`）。

**已填入的确认数据：**
- §4.4 Table 4: neg_difficulty 全部 6 个 cell（2 encoder × 3 strategy 的 pos_sim/neg_sim/margin），含 saturation asymmetry 分析和 margin ratio 2.6–4.1×
- §4.4 Table 6: CodeQL scalability 全部数据（0% timeout, 123 repos, 4 tiers 的 coverage/Z%）
- §4.3 Table 2: pilot 结果（Qwen +2.0pp, StarCoder +1.6pp embedding vs random）
- §4.2: 所有训练配置（LoRA, InfoNCE, optimizer, dual checkpoint, 硬件）

**`\placeholder{}` 标记的待填项：**
- Table 1 主结果（18 runs 的 mean±std，M2 尚在跑）
- Table 3 pool size sensitivity（plan_019 未执行）
- Dynamic mining control（plan_015 未执行）
- SWE-bench Lite downstream（plan_003 未执行）
- Table 5 stratified analysis（plan_005 待 M2 checkpoint）
- BM25 baseline 和 BM25-mined negatives 训练结果（plan_018 Phase 2 待执行）

---
