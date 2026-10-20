# code student training scaffold

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_student_training_scaffold_20260515T080759_result.json`
- **Structured JSON:** [`1c6c9a6f48261d26d534.json`](../../sessions/1c/1c6c9a6f48261d26d534.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两项验证通过。

### 产出

**脚本路径**: `/root/trace_distill_repair/convert_scoring_to_training.py`

**支持的参数**:

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--mode` | `both` | `structural` / `line` / `both` |
| `--train-ratio` | `0.8` | train/val 按 instance 划分比例 |
| `--with-context` | off | 加入 bug 描述、buggy code、邻近 segment 摘要 |
| `--scoring-dir` | `pipeline_output/` | scoring JSON 所在目录 |
| `--output-dir` | `pipeline_output/training_data/` | 输出目录 |
| `--seed` | `42` | 随机种子 |
| `--structural-scores-file` | auto | 覆盖 structural scores 文件名 |
| `--line-scores-file` | auto | 覆盖 line scores 文件名 |

**输出文件**: `train.jsonl` + `val.jsonl`，每行格式：

```json
{
  "input": "## Trace Segment (call_subtree)\n[call     ] func:10 depth=2 locals={...}\n...",
  "output": "keep",
  "metadata": {
    "instance_id": "thefuck_1",
    "segment_id": "call_subtree_0_15",
    "segment_type": "structural",
    "teacher_confidence": 0.85,
    "teacher_reasoning": "Shows the root cause..."
  }
}
```

关键设计点：
- train/val 按 instance_id 整体划分（同一 bug 的 segments 不会跨 split）
- label 字段名容错（label/decision/score/verdict/classification）
- error/parse_failure segments 自动过滤并计数
- `--with-context` 模式加入 buggy code + 邻近 segment 摘要，用于 rich input 实验

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "input": "## Trace Segment (call_subtree)\n[call     ] func:10 depth=2 locals={...}\n...",
    "output": "keep",
    "metadata": {
      "instance_id": "thefuck_1",
      "segment_id": "call_subtree_0_15",
      "segment_type": "structural",
      "teacher_confidence": 0.85,
      "teacher_reasoning": "Shows the root cause..."
    }
  }
}
```

</details>

---
