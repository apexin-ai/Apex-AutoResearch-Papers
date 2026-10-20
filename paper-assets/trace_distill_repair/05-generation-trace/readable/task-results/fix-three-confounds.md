# fix three confounds

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_three_confounds_20260515T122721_result.json`
- **Structured JSON:** [`8a400fbf44823b2eaa56.json`](../../sessions/8a/8a400fbf44823b2eaa56.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。以下是变更总结：

### Confound A — max_tokens 截断
| 文件 | 行 | 旧值 | 新值 |
|------|-----|------|------|
| `run_phase3_repair.py` | 288 | `max_tokens=4096` | `max_tokens=16384` |
| `mvp_pipeline.py` | 267 | `max_tokens=4096` | `max_tokens=16384` |

### Confound B — 输出格式改为 diff/patch
- **`mvp_pipeline.py`**: `REPAIR_PROMPT_TEMPLATE` 改为要求 unified diff 格式输出，新增 `{buggy_file}` 占位符
- **`mvp_pipeline.py`**: `_build_repair_prompt` 新增 `buggy_file` 参数
- **`mvp_pipeline.py`** + **`run_phase3_repair.py`**: LLM 输出解析从 `` ```python `` → `` ```diff `` 块提取
- **`run_phase3_repair.py`**: 新增 `apply_diff_to_code()` 函数（调用 `patch -p1` 应用 diff，自动修正路径前缀）
- **`run_phase3_repair.py`**: `run_instance` 中 LLM 返回 diff → 应用到 buggy code → 传给 evaluate/judge。diff 应用失败时回退到原始输出。

### Confound C — get_buggy_code 健壮性
- **`run_phase2_scoring.py`**: 新增 `get_buggy_file_relpath()` 函数，从 `bug_info["buggy_file"]` 或 `bug_patch.txt` 的 diff header 提取目标文件路径
- **`run_phase2_scoring.py`**: `get_buggy_code()` 改为先用 `get_buggy_file_relpath()` 定位文件，最后才 fallback 到 `_find_main_python_file`

### 验证结果
```
cookiecutter_1: relpath=cookiecutter/generate.py, 381 lines
fastapi_2:     relpath=fastapi/routing.py, 992 lines
youtube-dl_5:  relpath=youtube_dl/utils.py, 2972 lines
```
三个实例全部返回正确的 buggy 文件。`apply_diff_to_code` 测试通过。所有文件无语法错误。

---
