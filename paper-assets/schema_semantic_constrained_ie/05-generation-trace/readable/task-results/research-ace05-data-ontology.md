# research ace05 data ontology

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ace05_data_ontology_20260517T141431_result.json`
- **Structured JSON:** [`6fd792bcf159d9b240e4.json`](../../sessions/6f/6fd792bcf159d9b240e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**已产出文件（westd-16980:/root/schema_semantic_constrained_ie/data/ace05/）：**

1. **`ontology_constraints_ace05.json`** — 完整 ACE05 event ontology 约束，包含：
   - 33 event types（8 supertypes: Life/Movement/Transaction/Business/Conflict/Contact/Personnel/Justice）
   - 22 unique argument roles
   - 7 entity types（PER, ORG, GPE, LOC, FAC, VEH, WEA）
   - `argument_constraints`: 每个 event type 的 role → 允许 entity types 映射
   - `role_entity_constraints`: 全局 role → entity types 映射
   - `event_supertypes`: 层级结构

2. **`sample_data.jsonl`** — 10 条合成示例，覆盖 Attack/Be-Born/Sentence/Transport/Arrest-Jail/Meet/Transfer-Ownership/Die/Elect/Demonstrate

3. **`artifacts/_project/report/ace05_schema_design.md`** — 完整报告（已注册），含 33 types × roles × entity type 约束表 + JSON 输出格式 + SFT prompt 模板

**JSON 输出格式（与现有 RE 兼容）：**
- RE: `{"entities": [...], "relations": [...]}`
- EE: `{"entities": [...], "events": [{"trigger": "...", "event_type": "...", "arguments": [...]}]}`

**数据获取：** ACE05 是 LDC 付费数据集（LDC2006T06），两台服务器均无。需要 LDC 许可证后用 OneIE 脚本预处理。合成数据可先用于开发验证 pipeline。

---
