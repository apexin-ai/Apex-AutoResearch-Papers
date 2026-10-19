# code d023 correction span check

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d023_correction_span_check_20260512T193517_result.json`
- **Structured JSON:** [`451ca60b0132d1080c2b.json`](../../sessions/45/451ca60b0132d1080c2b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。下面是端到端分析报告。

---

## Correction Span 端到端就绪报告

### 1. 代码就绪状态：基本就绪，有一处字段不兼容

存在**两条 correction span 计算路径**：

| | Path A: `classify_errors.py` | Path B: `measure_correction_span.py` |
|---|---|---|
| **作用** | 完整 pipeline：匹配 → divergence → LLM 分类 → Kruskal-Wallis | 独立验证：取分类结果 → 重算 correction_span → Kruskal-Wallis |
| **correction_span 计算** | `len(expert_actions) - div_step`（action 级精确对齐） | `expert_steps - failure_step + 1`（步数差值） |
| **输出字段** | `divergence_step` | 期望输入 `failure_step` |
| **KW 检验** | 内置 `run_dual_analysis()` | 独立 `run_analysis()` |

**Path A 自身端到端完整**——从 post_processed JSONL 到 Kruskal-Wallis 一条龙，不需要 Path B。

### 2. Expert 数据格式：兼容

`alfworld_sft.json` 格式：
```json
{"id": "alfworld_0", "game_file": "data/json_2.1.1/train/&lt;task>/&lt;trial>",
 "conversations": [{"from": "human/gpt", "value": "..."}]}
```

`classify_errors.py` 已正确处理：
- `extract_actions_expert()` 处理 `from/value` 格式
- `extract_actions_model()` 处理 `role/content` 格式
- `normalize_game_file()` 统一抽取 `json_2.1.1/...` 作为匹配 key，兼容 expert 的 `data/json_2.1.1/...` 和 model 的 `/root/.../json_2.1.1/.../game.tw-pddl`

### 3. 字段不兼容问题

如果要用 `measure_correction_span.py` 做独立验证：

- `classify_errors.py` 输出 `divergence_step`
- `measure_correction_span.py` 读取 `failure_step`

**但这不是阻塞问题**——`classify_errors.py` 自身已经包含完整的 Kruskal-Wallis 分析（`run_dual_analysis()`），可以不经过 `measure_correction_span.py`。

### 4. 现有数据状态

`classified_errors.jsonl` 是**旧版 pipeline 产物**（含 `conversations`、`reward`、`correction_horizon` 等旧字段），不是当前 `classify_errors.py` 的输出格式。v5 需要重新运行。

`correction_span_results.jsonl` 已有旧数据（82 条，p=0.00022），但这是基于旧分类结果的。

### 5. v5 端到端执行流程

```
post_process_trajectories.py (v5 raw → true_failure.jsonl)
    ↓
classify_errors.py --failure_dir data/post_processed/ \
                   --expert_file data/alfworld_sft.json \
                   --output_file data/classified/v5_classified.jsonl \
                   [--dry_run]
    ↓
输出包含: error_type, divergence_step, correction_span + Kruskal-Wallis 结果
```

### 6. 建议修复

如果希望 `measure_correction_span.py` 也能作为独立验证工具使用，需要让它兼容 `divergence_step` 字段。改动很小：

```python
# measure_correction_span.py, compute_correction_spans() 中
failure_step = max(1, rec.get("failure_step", rec.get("divergence_step", 1)))
```

要现在做这个修改吗？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "id": "alfworld_0",
    "game_file": "data/json_2.1.1/train/&lt;task>/&lt;trial>",
    "conversations": [
      {
        "from": "human/gpt",
        "value": "..."
      }
    ]
  }
}
```

</details>

---
