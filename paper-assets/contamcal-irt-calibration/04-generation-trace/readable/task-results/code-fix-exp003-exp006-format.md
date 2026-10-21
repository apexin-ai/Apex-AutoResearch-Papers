# code fix exp003 exp006 format

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_exp003_exp006_format_20260514T133501_result.json`
- **Structured JSON:** [`fc747627d387a470af89.json`](../../sessions/fc/fc747627d387a470af89.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部通过。

## 结果

**改了什么：** `exp006/run_irt_calibration.py` 和 `exp006/run_irt_stan.py` 的 `load_exposure_scores` 函数，各加 ~10 行格式自适应逻辑。在 `json.load(f)` 后、使用 `raw` 前，自动检测并转换 3 种嵌套格式：
- `{bench: {exposure_scores: [...], ...}}` → 提取 list
- `{model_id: {bench: {exposure_scores: [...], ...}}}` → 解包 model 层 + 提取 list
- `{model_id: {bench: [floats]}}` → 解包 model 层

**dry-run 验证：**
| 测试 | 结果 |
|------|------|
| exp-003 嵌套格式 → run_irt_calibration | PASSED (3 benchmarks, item counts 正确) |
| exp-003 嵌套格式 → run_irt_stan | PASSED |
| 旧的扁平格式 `{bench: [floats]}` | PASSED (向后兼容) |

**向后兼容：** exp-003 侧零改动，已有的 `exposure_scores.json` 文件无需重新生成。exp-006 同时接受新旧两种格式。

---
