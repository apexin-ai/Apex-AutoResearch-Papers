# code classify dryrun compare

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_classify-dryrun-compare_20260512T224442_result.json`
- **Structured JSON:** [`2dbb6e9bf94f498eb141.json`](../../sessions/2d/2dbb6e9bf94f498eb141.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两版均完成。对比分析结果：

## 对比摘要

20 条输入样本中有 8 条匹配到失败轨迹并被分类。

### 分类分布

| error_type | 版本 A (有 span hint) | 版本 B (无 span hint) |
|---|---|---|
| planning | 6 | 6 |
| verification | 2 | 2 |
| action | 0 | 0 |

### 逐条对比

| task_id | task_type | A: error_type | B: error_type | A: llm_original | B: llm_original | 一致？ |
|---|---|---|---|---|---|---|
| 0 | pick_clean_then_place | planning | planning | planning | planning | ✓ |
| 3 | pick_heat_then_place | verification | verification | planning | planning | ✓ |
| 4 | pick_and_place | planning | planning | planning | planning | ✓ |
| 5 | pick_heat_then_place | planning | planning | planning | planning | ✓ |
| 9 | pick_heat_then_place | planning | planning | planning | planning | ✓ |
| 13 | pick_clean_then_place | verification | verification | planning | planning | ✓ |
| 14 | pick_heat_then_place | planning | planning | planning | planning | ✓ |
| 16 | pick_heat_then_place | planning | planning | planning | planning | ✓ |

### 关键发现

**分类完全一致，0 条不同。**

- LLM 在两版中均将全部 8 条归类为 `planning`（`llm_original_type` 全部是 planning）
- task_id 3 和 13 被后处理 CSF 检测覆盖为 `verification`（`premature_completion_belief`），这是代码逻辑覆盖而非 LLM 判断，两版行为一致
- reasoning 文本有细微措辞差异，但分类标签无变化

### 结论

移除 span hint 对这 8 条样本的分类结果**无影响**。LLM 无论是否看到 span 长度描述（SHORT/MEDIUM/LONG），都将所有样本归类为 planning。span hint 并非 planning 比例过高的原因——LLM 本身就倾向于将所有错误归类为 planning。

输出文件：
- `outputs/classify_compare_with_hint_20.jsonl`
- `outputs/classify_compare_no_hint_20.jsonl`

---
