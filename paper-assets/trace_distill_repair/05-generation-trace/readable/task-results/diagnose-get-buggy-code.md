# diagnose get buggy code

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_get_buggy_code_20260515T120839_result.json`
- **Structured JSON:** [`e4efbe89ba55580718b5.json`](../../sessions/e4/e4efbe89ba55580718b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 1. 根因分析

`get_buggy_code()` 在 `run_phase2_scoring.py:88-100` 中有一个致命 bug：

```python
def get_buggy_code(instance_key: str) -> str:
    ...
    buggy_file = bug_info.get("buggy_file", "")   # ← 永远为空
    if buggy_file:
        ...
    return setup._find_main_python_file(buggy_dir)  # ← 每次都走这个 fallback
```

- **BugsInPy 的 `bug.info` 根本没有 `buggy_file` 字段**。它只有 `python_version`, `buggy_commit_id`, `fixed_commit_id`, `test_file`。
- 因此 `buggy_file` 永远是 `""`，**全部 33 个实例**都 fallback 到 `_find_main_python_file()`
- `_find_main_python_file()` 用 `os.walk()` 返回第一个按字母序排列的 `.py` 文件 —— 总是拿到无关文件：
  - youtube-dl → `devscripts/bash-completion.py`（869 chars）
  - tornado → `demos/blog/blog.py`
  - luigi → `doc/conf.py`
  - scrapy → `conftest.py`
  - thefuck → `fastentrypoints.py`
  - 等等

**不是 ~14 个出错，是全部 33 个都错了。** 之前某些实例看起来"正常"只是因为 fallback 碰巧选到的文件够大，LLM 基于 issue description 猜出了修复。

### 2. 修复方案

修改 `get_buggy_code()` —— 从 `bug_patch.txt` 提取正确的目标文件：

```python
def get_buggy_code(instance_key: str) -> str:
    buggy_dir = os.path.join(WORKSPACE, "instances", instance_key, "buggy")
    if not os.path.isdir(buggy_dir):
        return ""
    setup = BugsInPySetup(WORKSPACE)
    parts = instance_key.rsplit("_", 1)
    project, bug_id = parts[0], int(parts[1])
    bug_dir = os.path.join(WORKSPACE, "BugsInPy", "projects", project, "bugs", str(bug_id))
    bug_info = setup._read_bug_info(bug_dir)

    # 1) Try buggy_file from bug.info (BugsInPy doesn't have this, but keep for safety)
    buggy_file = bug_info.get("buggy_file", "")
    if buggy_file:
        path = os.path.join(buggy_dir, buggy_file)
        if os.path.isfile(path):
            with open(path) as f:
                return f.read()

    # 2) Extract target file from bug_patch.txt
    import re
    patch_path = os.path.join(bug_dir, "bug_patch.txt")
    if os.path.isfile(patch_path):
        with open(patch_path) as f:
            patch_content = f.read()
        changed_files = re.findall(r'diff --git a/(.*?) b/', patch_content)
        # Pick first non-test source file
        for cf in changed_files:
            basename = os.path.basename(cf)
            if not basename.startswith("test_") and "/tests/" not in cf:
                path = os.path.join(buggy_dir, cf)
                if os.path.isfile(path):
                    with open(path) as fh:
                        return fh.read()
        # If all are test files, use the first one
        if changed_files:
            path = os.path.join(buggy_dir, changed_files[0])
            if os.path.isfile(path):
                with open(path) as fh:
                    return fh.read()

    # 3) Last resort fallback
    return setup._find_main_python_file(buggy_dir)
```

### 3. 33 实例完整状态表（修复后）

| instance_id | fixed_valid | fixed_chars | struct_keep | line_keep | n_changed | tier | patch_file |
|---|---|---|---|---|---|---|---|
| black_1 | True | 221272 | 2/10 | 1/30 | 1 | Tier1 | black.py |
| cookiecutter_1 | True | 14412 | 6/20 | 11/35 | 1 | Tier1 | cookiecutter/generate.py |
| cookiecutter_2 | True | 4126 | 6/20 | 8/35 | 1 | Tier1 | cookiecutter/hooks.py |
| cookiecutter_3 | True | 7592 | 2/6 | 2/8 | 1 | Tier1 | cookiecutter/prompt.py |
| fastapi_1 | True | 27421 | 5/20 | 15/200 | 5 | **Exclude** | fastapi/applications.py + 4 more |
| fastapi_2 | True | 40170 | 3/20 | 19/200 | 1 | Tier1 | fastapi/routing.py |
| httpie_1 | True | 13468 | 0/1 | 0/1 | 1 | Tier2 | httpie/downloads.py |
| httpie_2 | True | 4338 | 0/12 | 0/27 | 2 | **Exclude** | httpie/client.py + httpie/core.py |
| luigi_1 | True | 13376 | 0/20 | 9/200 | 1 | Tier2 | luigi/server.py |
| luigi_2 | True | 16164 | 0/20 | 3/200 | 1 | Tier2 | luigi/contrib/beam_dataflow.py |
| luigi_5 | True | 14216 | 1/20 | 6/200 | 1 | Tier1 | luigi/util.py |
| luigi_10 | True | 52029 | 0/20 | 0/200 | 1 | Tier2 | luigi/scheduler.py |
| luigi_14 | True | 44813 | 0/20 | 0/200 | 1 | Tier2 | luigi/scheduler.py |
| sanic_1 | True | 51301 | 0/7 | 1/14 | 1 | Tier2 | sanic/app.py |
| sanic_2 | True | 34350 | 2/6 | 2/14 | 1 | Tier1 | sanic/server.py |
| scrapy_1 | True | 2563 | 0/20 | 0/32 | 1 | Tier2 | scrapy/spidermiddlewares/offsite.py |
| scrapy_2 | True | 9823 | 2/20 | 2/36 | 1 | Tier1 | scrapy/utils/datatypes.py |
| scrapy_3 | True | 4436 | 0/20 | 0/33 | 1 | Tier2 | scrapy/downloadermiddlewares/redirect.py |
| scrapy_4 | True | 5416 | 0/4 | 1/6 | 1 | Tier2 | scrapy/contracts/__init__.py |
| scrapy_7 | True | 7337 | 2/20 | 3/37 | 1 | Tier1 | scrapy/http/request/form.py |
| thefuck_1 | True | 608 | 0/20 | 1/153 | 1 | Tier2 | thefuck/rules/pip_unknown_command.py |
| thefuck_2 | True | 9180 | 0/20 | 0/110 | 1 | Tier2 | thefuck/utils.py |
| thefuck_4 | True | 4239 | 0/20 | 0/120 | 1 | Tier2 | thefuck/shells/fish.py |
| tornado_1 | True | 60926 | 0/20 | 0/200 | 1 | Tier2 | tornado/websocket.py |
| tornado_2 | True | 35556 | 1/20 | 2/200 | 1 | Tier1 | tornado/http1connection.py |
| tornado_4 | True | 137803 | 0/20 | 0/200 | 1 | Tier2 | tornado/web.py |
| tornado_5 | True | 47635 | 0/20 | 0/200 | 1 | Tier2 | tornado/ioloop.py |
| tornado_7 | True | 43706 | 0/20 | 5/200 | 1 | Tier2 | tornado/ioloop.py |
| youtube-dl_1 | True | 120524 | 3/20 | 22/200 | 1 | Tier1 | youtube_dl/utils.py |
| youtube-dl_2 | True | 122963 | 1/20 | 20/200 | 1 | Tier1 | youtube_dl/extractor/common.py |
| youtube-dl_5 | True | 90377 | 4/20 | 72/200 | 1 | Tier1 | youtube_dl/utils.py |
| youtube-dl_10 | True | 54513 | 0/20 | 11/200 | 1 | Tier2 | youtube_dl/utils.py |
| youtube-dl_20 | True | 118720 | 1/20 | 10/200 | 1 | Tier1 | youtube_dl/utils.py |

### 4. Tier 统计

| Tier | 数量 | 实例 |
|---|---|---|
| **Tier 1（必跑）** | 14 | black_1, cookiecutter_1/2/3, fastapi_2, luigi_5, sanic_2, scrapy_2/7, tornado_2, youtube-dl_1/2/20/5 |
| **Tier 2（后跑）** | 17 | httpie_1, luigi_1/2/10/14, sanic_1, scrapy_1/3/4, thefuck_1/2/4, tornado_1/4/5/7, youtube-dl_10 |
| **Exclude** | 2 | fastapi_1, httpie_2 |

### 5. Exclude 实例说明

- **fastapi_1**: multi-file patch（5 个文件：applications.py, encoders.py, openapi/utils.py, routing.py, tests/test_skip_defaults.py）
- **httpie_2**: multi-file patch（2 个文件：client.py, core.py）

---
