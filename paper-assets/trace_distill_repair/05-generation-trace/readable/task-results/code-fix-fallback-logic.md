# code fix fallback logic

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_fallback_logic_20260514T202821_result.json`
- **Structured JSON:** [`f69e4148b92f72d999fa.json`](../../sessions/f6/f69e4148b92f72d999fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成，汇总如下：

---

## Diff

### teacher_scorer.py (2 处)

```diff
@@ -125,9 +125,10 @@
                         max_retries, segment.start_idx, segment.end_idx, e,
                     )
+                    # Use 'error' not 'drop' so API failures don't bias keep/drop statistics
                     return ScoredSegment(
                         segment=segment,
-                        label="drop",
+                        label="error",
                         confidence=0.0,
                         reasoning="API_FAILURE_FALLBACK",
                     )
@@ -176,7 +177,7 @@
                     results[idx] = ScoredSegment(
                         segment=segments[idx],
-                        label="drop",
+                        label="error",
                         confidence=0.0,
                         reasoning=f"Scoring error: {e}",
                     )
```

### run_phase2_scoring.py (1 处)

```diff
@@ -169,7 +169,7 @@
             for scored in batch_results:
                 seg = scored.segment
-                if scored.confidence == 0.0 and scored.reasoning.startswith("API error:"):
+                if scored.label == "error":
                     inst_result["scores"].append({
```

## 下游兼容性

| 文件 | 状态 | 说明 |
|------|------|------|
| `run_phase2_scoring.py` | **已修复** | 旧条件 `reasoning.startswith("API error:")` 从不匹配实际 reasoning（"API_FAILURE_FALLBACK" / "Scoring error: ..."），是死代码。改为 `scored.label == "error"` 直接检测 |
| `run_phase3_repair.py` | **无需改动** | `build_keep_segments` (L111) 只选 `label == "keep"`，"error" 自动排除；统计处 (L494-495) 也只计 `label == "keep"` |
| `filter_segments` | **无需改动** | 只选 `label == "keep" and confidence >= threshold` |

## Rerun 进度

- 38 个实例已完成 8 个（~21%），运行 ~8 分钟
- 当前进程使用旧代码（内存中），不受本次修改影响
- 如果希望新代码生效，需要重启 rerun，约损失已完成的 8 个实例的工作量

---
