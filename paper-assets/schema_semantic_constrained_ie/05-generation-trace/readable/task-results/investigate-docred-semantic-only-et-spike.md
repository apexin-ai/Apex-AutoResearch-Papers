# investigate docred semantic only et spike

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_docred_semantic_only_et_spike_20260514T143836_result.json`
- **Structured JSON:** [`56c7ed5ecbb1aa9da80e.json`](../../sessions/56/56c7ed5ecbb1aa9da80e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据完全清晰了。以下是完整排查结论。

---

## 排查结论：DocRED semantic_only ET violation 暴涨

### 数字分解

| 层级 | semantic_only ET | 与 unconstrained 差值 |
|------|------------------|-----------------------|
| 当前 checker (`.upper()`) | **18.44%** (3722) | +10.26pp (+2072) |
| Fix1: 加 `.strip()` | **15.93%** (3215) | +7.75pp (+1565) |
| Fix2: strip + PERSON→PER alias | **10.57%** (2134) | +2.40pp (+484) |
| unconstrained 基线 | **8.18%** (1650) | — |

### 三层归因

**1. Checker bug：缺 `.strip()` — 贡献 2.51pp (507 violations)**
- `violation_checker_docred.py:104-106` 对 head_type/tail_type 做 `h_type.upper()` 判断，但**没有 `.strip()`**
- TypeConstraintProcessor 的 logit masking 在 token 边界引入前导空格：` TIME`(180), ` LOC`(114), ` MISC`(99), ` PER`(69), ` NUM`(42)
- unconstrained 输出中无此问题（零个带空格的类型）
- **修复：`h_type.strip().upper()`**

**2. 缺 PERSON→PER alias — 贡献 5.36pp (1081 violations)**
- TypeConstraintProcessor 把模型从生成 "PER" 推向了完整英文 "PERSON"
- unconstrained 零个 PERSON，semantic_only 有 1081 个（head 710 + tail 371）
- 这是最大单一贡献因素。是否算 checker 缺陷有争议——严格来说 DocRED schema 就是 PER 不是 PERSON
- **如果要修 checker：加 `{'PERSON': 'PER'}` alias map**

**3. 真实退化 — 贡献 2.40pp (484 violations)**
- 即使 checker 完全 normalize 后，semantic_only 仍比 unconstrained 高 2.40pp
- 具体来源：
  - **截断类型** (token masking 切断生成)：`ORGB` 85 次, `OR` 62 次 = 147
  - **非标类型频率上升**：WORK +218, EVENT +65, ETHNIC_GROUP +6, 新增 ENTITY_TYPE(26)/JOB(22)/GENRE(21) 等
- 这是 TypeConstraintProcessor 的 logit masking 对 relation 字段中 entity type token 的干扰，**真实退化**

### Top 15 semantic_only 违规类型

| 类型 | 次数 | 分类 |
|------|------|------|
| `PERSON` | 1081 | alias 缺失 |
| `WORK` | 823 | 非标类型 (unconstrained ~605) |
| `EVENT` | 743 | 非标类型 (unconstrained ~678) |
| ` TIME` | 180 | 前导空格 |
| `ETHNIC_GROUP` | 137 | 非标类型 |
| ` LOC` | 114 | 前导空格 |
| ` MISC` | 99 | 前导空格 |
| `ORGB` | 85 | 截断 |
| ` PER` | 69 | 前导空格 |
| `OR` | 62 | 截断 |
| ` NUM` | 42 | 前导空格 |
| `SERIES` | 32 | 非标类型 |
| `ENTITY_TYPE` | 26 | 非标类型 |
| `JOB` | 22 | 非标类型 |
| `GENRE` | 21 | 非标类型 |

### 判定

**混合问题：77% 是 checker normalization 不足，23% 是真实退化。**

- checker 加 `.strip()` + PERSON alias 后，semantic_only ET 从 18.44% 降到 10.57%
- 残余 2.40pp 高于 unconstrained 的 8.18%，是 TypeConstraintProcessor 的 logit masking 副作用（截断类型 + 非标类型频率上升）
- SciERC 上无此问题因为 SciERC entity types 是多 token 长词（Task, Method, Material, OtherScientificTerm），token masking 影响较小；DocRED 用 2-4 字符缩写（PER, ORG, LOC），对 token 边界更敏感

### 建议修复方案

1. **Checker 修复**（不改变实验结果，只修正度量）：
   - `violation_checker_docred.py` 中所有 `.upper()` 改为 `.strip().upper()`
   - 添加 alias map `PERSON→PER`（可选，取决于严格程度）

2. **TypeConstraintProcessor 修复**（解决真实退化）：
   - 排查为什么 logit masking 影响 relation JSON 中的 entity type 字段——TypeConstraintProcessor 应只约束 relation type 的 head/tail type pair，但似乎在更广泛的范围内干扰了 token 概率
   - 可能需要让 masking 只在特定 JSON 字段位置激活，而不是全局影响

---
