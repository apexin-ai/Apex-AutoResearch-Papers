# diagnose test execution failure

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_test_execution_failure_20260515T110020_result.json`
- **Structured JSON:** [`26fe0181e7d8a0d66362.json`](../../sessions/26/26fe0181e7d8a0d66362.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

---

## 根因分析

### 根本原因：缺少项目级依赖环境

`_run_test_evaluation` (`mvp_pipeline.py:302-336`) 直接在当前 conda base 环境中用 `subprocess.run(shlex.split(test_command), cwd=buggy_dir)` 跑测试。但 **每个 BugsInPy 项目都有自己的依赖**，conda base 里一个都没装。

`BugsInPySetup.setup_instance()` (bugsinpy_setup.py:88) 只做了 git checkout 源码，**没有安装任何项目依赖**。

### 三类失败模式

| 类型 | 示例 | 错误 |
|------|------|------|
| **缺项目依赖** | black_1 | `NameError: name 'AioHTTPTestCase' is not defined`（缺 aiohttp） |
| **缺测试工具** | cookiecutter_1 | `tox: command not found` |
| **版本不兼容** | fastapi_1 | pydantic v2 与旧 fastapi 代码不兼容 |

所有 33 实例 × 4 条件 = 132 次测试全部因环境问题失败，不是修复质量问题。

### `_evaluate_repair` 关键逻辑 (mvp_pipeline.py:266-300)

```python
if test_command and buggy_dir and buggy_file_relpath:
    test_result = self._run_test_evaluation(...)  # 永远走这条路（因为三个值都有）
    result.update(test_result)                      # returncode != 0 → pass=False
else:
    result["method"] = "line_overlap_fallback"       # 从没走到这里
    if result["line_overlap"] > 0.9:
        result["pass"] = True
```

test_command / buggy_dir / buggy_file_relpath 三个值对所有实例都存在，所以**永远不会 fallback 到 line_overlap**。测试跑了但因环境缺失全挂了。

### 修复方案

**方案 A（推荐，快速修复）**：在 `_evaluate_repair` 中，将 `line_overlap` + LLM judge 作为主评估方式，跳过 test execution。Phase 3 的目的是对比 4 种 trace condition 的修复效果差异，line_overlap + judge score 已经足够。

**方案 B（完整方案）**：为每个 BugsInPy 项目创建独立 venv，安装项目依赖，`_run_test_evaluation` 在对应 venv 中执行测试。工作量大，需要处理 10+ 个项目的依赖安装。

**方案 C（折中）**：加 `--skip-test-execution` flag，重跑 Phase 3 时 fallback 到 line_overlap。

需要我实施哪个方案？

---
