# exp_026_t05 Prompt Format Check

## 结论

**exp_026_t05 使用了 joint NER+RE prompt（`_TRAIN_ALIGNED_TEMPLATE`），不是 NER-only prompt。**

但 exp_012_rerun_1024（T=1.0 baseline）也使用了完全相同的 joint prompt，两者 prompt 一致。

## Prompt 内容

exp_026_t05 的 `report.json` 显示 `use_train_format: true`，对应 `_TRAIN_ALIGNED_TEMPLATE`：

```
Extract all structured information (entities and relations) from the following text.
Output a JSON object.

Text: {text}
{schema_line}

Output format: {"entities": [{"text": "...", "type": "...", "start": <int>, "end": <int>}],
"relations": [{"head": "...", "tail": "...", "type": "...",
"head_start": <int>, "head_end": <int>, "tail_start": <int>, "tail_end": <int>}],
"events": []}
```

指令明确要求 "entities and relations"，输出格式包含 relations 字段。

作为对比，NER-only prompt（`_NER_TEMPLATE`，未使用）：

```
Extract named entities from the following text.
Output a JSON object with the fields: entities, relations, events.

Text: {text}
{schema_line}

Output format: {"entities": [{"text": "...", "type": "...", "start": <int>, "end": <int>}],
"relations": [], "events": []}
```

## 与 T=1.0 baseline 的一致性

| 字段 | exp_026_t05 (T=0.5) | exp_012_rerun_1024 (T=1.0) |
|------|---------------------|---------------------------|
| use_train_format | true | true |
| prompt template | `_TRAIN_ALIGNED_TEMPLATE` | `_TRAIN_ALIGNED_TEMPLATE` |
| model | qwen3-8b-scierc-merged-v2 | qwen3-8b-scierc-merged-v2 |
| n_samples | 8 | 8 |
| subtask (eval) | ner | joint |
| 输出包含 relations | YES | YES |

**两者 prompt 完全一致。** 区别仅在于：
- exp_026_t05 评估时只算了 NER F1（subtask="ner"）
- exp_012_rerun_1024 评估时算了 NER + RE（subtask="joint"）

## 实际输出验证

exp_026_t05 的 samples.jsonl 第一条记录确认模型输出了 entities + relations + events，关系类型包括 PART-OF, USED-FOR, EVALUATE-FOR 等 SciERC 标准关系类型。

## 是否需要重跑

**取决于目标：**

1. **如果目标是 T=0.5 vs T=1.0 的公平对比**：不需要重跑。两者使用相同的 joint prompt，prompt 一致性已确认。
2. **如果目标是纯 NER-only 推理（排除 RE 对 NER 的干扰）**：需要用 `_NER_TEMPLATE`（`--use_train_format false --subtask ner`）重跑。但此时 T=1.0 baseline 也应同步重跑以保持一致。

注意：当前代码中 `use_train_format` 默认值为 True，且 `use_train_format=True` 时 subtask 参数被忽略（line 310: "ignores subtask"）。
