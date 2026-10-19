# data globalmmlu 20lang check

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_globalmmlu_20lang_check_20260520T214558_result.json`
- **Structured JSON:** [`744d8cc25de039df6e40.json`](../../sessions/74/744d8cc25de039df6e40.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整结果已获取。以下是报告：

---

## GlobalMMLU 数据可用性报告

### 1. 20 语言 test/dev 样本数

| 语言 | test | dev | dev split | 状态 |
|------|------|-----|-----------|------|
| en   | 14,042 | 285 | dev | OK |
| zh   | 14,042 | 285 | dev | OK |
| ar   | 14,042 | 285 | dev | OK |
| hi   | 14,042 | 285 | dev | OK |
| sw   | 14,042 | 285 | dev | OK |
| ko   | 14,042 | 285 | dev | OK |
| es   | 14,042 | 285 | dev | OK |
| fr   | 14,042 | 285 | dev | OK |
| de   | 14,042 | 285 | dev | OK |
| ru   | 14,042 | 285 | dev | OK |
| tr   | 14,042 | 285 | dev | OK |
| bn   | 14,042 | 285 | dev | OK |
| ja   | 14,042 | 285 | dev | OK |
| pt   | 14,042 | 285 | dev | OK |
| vi   | 14,042 | 285 | dev | OK |
| **th** | — | — | — | **不可用** |
| id   | 14,042 | 285 | dev | OK |
| pl   | 14,042 | 285 | dev | OK |
| nl   | 14,042 | 285 | dev | OK |
| uk   | 14,042 | 285 | dev | OK |

**19/20 语言可用。** Thai (th) 不在 GlobalMMLU 中。所有可用语言样本数完全一致（test=14042, dev=285）。

### 2. 字段格式差异

| | cais/mmlu (en) | CohereForAI/Global-MMLU (其他) |
|---|---|---|
| 选项格式 | `choices` (list) | `option_a/b/c/d` (4个独立字段) |
| answer 类型 | **int** (0-3) | **str** ("A"/"B"/"C"/"D") |
| 额外字段 | 无 | `sample_id`, `subject_category`, `required_knowledge`, `time_sensitive`, `reference`, `culture`, `region`, `country`, `cultural_sensitivity_label`, `is_annotated` |

**需要统一处理逻辑：** en 用 int index，其他语言用字母 A/B/C/D；en 用 choices list，其他语言用 option_a/b/c/d。

### 3. Train split 可用性

GlobalMMLU **没有 train split**（zh/ar/hi/sw 均无）。只有 test 和 dev 两个 split。CaCLR consistency loss 需要用 test split 本身或 dev split 来构建 parallel pairs。

### 4. Parallel alignment 验证

| idx | en subject | zh subject | en answer | zh answer | 对齐 |
|-----|-----------|-----------|-----------|-----------|------|
| 0 | abstract_algebra | abstract_algebra | 1 | B | subject 对齐 |
| 1 | abstract_algebra | abstract_algebra | 2 | C | subject 对齐 |
| 2 | abstract_algebra | abstract_algebra | 3 | D | subject 对齐 |
| 3 | abstract_algebra | abstract_algebra | 1 | B | subject 对齐 |
| 4 | abstract_algebra | abstract_algebra | 1 | B | subject 对齐 |

**Subject 完全对齐，answer 语义一致**（en 的 int 1→B, 2→C, 3→D 与 zh 的字母完全匹配：0→A, 1→B, 2→C, 3→D）。test[i] 在各语言中是同一道题的翻译，可直接用 index 构建 parallel pairs。

### 5. 问题与建议

1. **th 不可用**：需替换为 GlobalMMLU 中的其他语言（可选：`te`泰卢固语, `fil`菲律宾语, `fa`波斯语, `el`希腊语, `he`希伯来语, `cs`捷克语 等）
2. **answer 格式统一**：en 需要 int→letter 映射（`{0:'A', 1:'B', 2:'C', 3:'D'}`）
3. **选项格式统一**：en 的 `choices[i]` 对应其他语言的 `option_a/b/c/d`，数据加载时需统一
4. **无 train split**：CaCLR 可直接用 test split 按 index 构建跨语言 parallel pairs

---
