# code wikievents complete data download

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_wikievents_complete_data_download_20260517T170038_result.json`
- **Structured JSON:** [`7c36eaed878c1cc52f3a.json`](../../sessions/7c/7c36eaed878c1cc52f3a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。汇总报告：

---

## WikiEvents 数据集下载完成

### 数据统计

| Split | Documents | Events | Arguments | Entities |
|-------|-----------|--------|-----------|----------|
| train | 206 | 3,241 | 4,542 | 28,296 |
| dev | 20 | 345 | 428 | 2,256 |
| test | 20 | 365 | 566 | 2,673 |
| **total** | **246** | **3,951** | **5,536** | **33,225** |

- 平均每文档 events: 16.1
- 平均每 event arguments: 1.40
- 唯一 event types: 50
- 唯一 entity types: 17

### Event Type 分布 (Top 10)
1. Conflict.Attack.DetonateExplode: 823
2. Life.Die.Unspecified: 525
3. Conflict.Attack.Unspecified: 411
4. Life.Injure.Unspecified: 301
5. Contact.Contact.Unspecified: 202
6. Contact.Contact.Broadcast: 195
7. Justice.ArrestJailDetain.Unspecified: 188
8. Movement.Transportation.Unspecified: 156
9. Justice.ChargeIndict.Unspecified: 104
10. Justice.InvestigateCrime.Unspecified: 92

### Ontology Constraints 一致性

**Event Type 映射**: 45/50 已映射，5 个缺失：
- `Contact.RequestCommand.{Broadcast, Correspondence, Meet}`
- `Contact.ThreatenCoerce.{Broadcast, Correspondence}`

**Entity Types**: 数据中的 `CRM` 不在 ontology 中（ontology 多出 10 个未在数据中出现的类型）

**Role Constraints**: `Justice.InvestigateCrime` 的 `ObservedEntity` 和 `Observer` 角色不在 constraints 中

### 数据加载兼容性

`load_wikievents_data()` 完全兼容，**不需要修改代码**。通过 `--data_path` 参数可切换 train/dev/test。

---
