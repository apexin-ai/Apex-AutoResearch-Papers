# writing experiments quick fixes 0515

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_experiments-quick-fixes-0515_20260515T140220_result.json`
- **Structured JSON:** [`d4e87d90c770056488a7.json`](../../sessions/d4/d4e87d90c770056488a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。修改汇总：

**experiments_v1.md** (3 项):
- §4.1 StarCoder pos_sim: `0.798` → `0.799`
- §4.1 train/val 数量: `approximately 11,300 training and 3,000 validation instances` → `11,236–11,308 training and 2,980–3,052 validation instances (varying by seed due to stratified splitting)`
- §4.3 新增 "Structural Extraction Scalability" 小节（段落形式，含 93.9% coverage、处理时间统计、tier-wise Z% 梯度，标注 M1v2 待更新）

**abstract_v2.md** (2 项):
- `entirely unexploited` → `largely unexploited for training-time negative selection`
- `at zero additional computational cost` → `at negligible additional cost (a single forward pass over the corpus)`

**未执行 — Item 1** (StarCoder random_s43): Table 1 全部为 `\placeholder{X.XX±X.XX}` 聚合格式，无逐 seed 分列，无法定位 s43 单独条目。需要 Table 1 填入实际数值后再处理，或改为逐 seed 表格格式。

`paper_drafts/` 目录下的副本已同步修复（abstract_v2 两处 + experiments_v1 的 0.798→0.799）。

---
