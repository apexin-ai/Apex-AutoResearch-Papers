# code dryrun v2 cf diagnosis

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dryrun_v2_cf_diagnosis_20260517T203301_result.json`
- **Structured JSON:** [`805b3e8ee521fb3d12da.json`](../../sessions/80/805b3e8ee521fb3d12da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。以下是完整报告。

---

## CF 违规诊断

### CF 检查逻辑

`violation_checker_wikievents.py` 的 CF 检查逻辑（第 150-170 行）：
1. 从 `entities[]` 收集 `text→type` 映射
2. 从所有 event `arguments[]` 收集 `text→entity_type` 映射
3. 同一 text（case-insensitive）如果映射到多个不同类型 → CF 违规

### 违规 Pattern

- 共 **37 个 CF 违规**，分布在 **9/14** 个成功解析的 doc 中
- 重灾区 doc: `JC002YBW0`(7), `wiki_drone_strikes_0_news_1`(8), `wiki_mass_car_bombings_0_news_9`(8)

**按 role 分布**（同一 entity 在 entity list 和 argument 中类型不一致的次数）：

| Role | 次数 | 主要模式 |
|------|------|----------|
| Place | 46 | constrained→FAC/GPE，real→PER/ORG |
| Artifact | 15 | constrained→MON/NAT，real→PER/ORG |
| 其他 | 6 | Instrument, PassengerArtifact 等 |

**Top 3 具体 pattern**：
1. `(Place, FAC, real→PER)` = **26 次** — 人名被放到 Place role，grammar 强制为 FAC
2. `(Place, GPE, real→ORG)` = 5 次 — 组织被放到 Place role，grammar 强制为 GPE
3. `(Place, GPE, real→PER)` = 5 次 — 同上，人名强制为 GPE

**具体案例**：

1. **`JC002YBW0`** — "dzhokhar tsarnaev"：entity list 中标为 PER，但在 11 个 event argument 中被填到 Place role，grammar 强制 entity_type=FAC。同一 doc 中 "stephen silva"、"tamerlan tsarnaev"、"fbi" 也是同样问题。

2. **`wiki_mass_car_bombings_0_news_9`** — "duque"(PER)、"eln"(ORG)、"rebels"(ORG) 被填到 Place role，grammar 强制 entity_type=GPE。"2016 peace accord"(EVENT) 也被放到 Place role→GPE。

3. **`wiki_drone_strikes_0_news_1`** — "president barack obama"(PER) 在某些 event 中 entity_type=MON，"george w. bush"(PER) 被标为 LOC/MON/PER 三种类型。

### 根因分析

**两层问题叠加**：

1. **模型 hallucination（根本原因）**：模型把 PER/ORG 实体错误地填到 `Place` role 中（如人名 "dzhokhar tsarnaev" 作为 ManufactureAssemble 事件的 Place）。这在 unconstrained 模式下同样存在，但无法观测。

2. **Grammar 类型强制（直接原因）**：Place role 在 ontology 中只允许 `{FAC, GPE, LOC}`。当模型把 PER 填到 Place role 时，grammar 强制 entity_type 从允许集合中选择，导致与 entity list 中正确类型（PER）冲突。

**为什么 unconstrained CF≈0%**：unconstrained 模式下 (1) 不输出 entities list（entities=[]），(2) 模型自由选择 entity_type，基于实体本身而非 role 约束，所以 "dzhokhar tsarnaev" 无论在什么 role 都会被标为 PER → 无冲突。

**核心矛盾**：constrained grammar 在 **per-argument** 层面保证 AC（Argument Constraint）合规，但没有 **cross-argument** 的一致性约束。这是 Layer 2 的设计盲区。

### Parse Failure 分析

6 个 failure 全是 **max_new_tokens 截断**：
- raw_output 长度：13,548 ~ 16,740 字符，全部在 JSON 中间截断（末尾是不完整的 key-value）
- wikievents 模式 max_new_tokens=4096（从默认 2048 自动提升）
- 耗时全部在 77-79 秒，推测触及 token 上限
- 与 constrained decoding 逻辑无关，是长文档输出超长的问题

| Doc ID | raw_output 长度 | 截断位置 |
|--------|----------------|----------|
| backpack_ied_13 | 16,023 | `"text": "Chelsea` |
| backpack_ied_20 | 16,740 | `"role": "` |
| 23_VOA_EN_NW_2015.11.24.3071320 | 14,744 | `Yusufu", "` |
| K0C041O37 | 13,548 | `"type": "` |
| wiki_mass_car_bombings_7_news_2 | 15,209 | `"text": "May` |
| wiki_ied_bombings_5_news_3 | 15,547 | `{"text` |

### 建议

**1. CF 修复 — 需要扩展 TypeConsensusProcessor（Layer 3）到 EE 格式**

现有 `--type_consensus` 和 `TypeConsensusProcessor` 是为 RE 格式设计的（匹配 `head_type`/`tail_type`），无法直接用于 EE 格式（`entities[].type` 和 `arguments[].entity_type`）。需要：
- 添加正则匹配 EE 的 `"entity_type"` 字段
- 从 entities section 建立 `text→type` 注册表
- 在生成 argument 的 `entity_type` 时，强制与注册表一致
- DR-aware：如果注册类型不在 (event_type, role) 的允许集合中，跳过强制（避免引入 AC 违规）

**2. 更深层的问题**

CF 违规暴露了模型把实体填错 role 的 hallucination 问题。即使加了 type consensus（强制 entity_type 一致），模型仍然会把人名放在 Place role 里——只是 entity_type 不再冲突了。这意味着 AC 违规可能回升（PER 不在 Place 的允许类型中）。

**可能的解法**：在 Layer 3 中，当注册类型与当前 role 允许类型冲突时，不仅跳过 type consensus，还可以考虑对当前 argument 降低置信度或触发 re-generation。

**3. Parse failure — 增加 max_new_tokens**

wikievents 长文档需要 max_new_tokens=8192。或者实现 JSON 截断恢复（截断位置尝试补全闭合括号）。

**4. 对全量实验的影响**

- CF 22.3% 在当前 20 doc 样本中较高，但不影响核心 claim（EV=0%, RoV=0%）
- 全量实验中 CF 比例可能更低（长文档更容易有冲突，但短文档贡献更多样本）
- 建议先实现 Layer 3 EE 版本再跑全量

---
