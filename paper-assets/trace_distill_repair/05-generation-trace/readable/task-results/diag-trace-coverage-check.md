# diag trace coverage check

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_trace_coverage_check_20260515T043002_result.json`
- **Structured JSON:** [`9f63a5978ab8c8b1d372.json`](../../sessions/9f/9f63a5978ab8c8b1d372.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完毕。所有数据已收集齐全。

---

## 结果汇总

### 1. keep=0 实例列表 (27个)

| 实例 | 总 segments | trace 事件数 | 目标 test 到达 |
|------|------------|-------------|---------------|
| black_1 | 11 | 51 | NOT_REACHED |
| black_14 | 9 | 41 | NOT_REACHED |
| black_2 | 10 | 46 | NOT_REACHED |
| black_5 | 9 | 44 | NOT_REACHED |
| httpie_1 | 1 | 5 | NOT_REACHED |
| luigi_1 | 200 | 3329 | NOT_REACHED |
| luigi_10 | 200 | 1954 | NOT_REACHED |
| luigi_14 | 200 | 1948 | NOT_REACHED |
| luigi_2 | 200 | 3317 | NOT_REACHED |
| luigi_5 | 200 | 1952 | NOT_REACHED |
| sanic_1 | 16 | 78 | NOT_REACHED |
| sanic_2 | 140 | 700 | NOT_REACHED |
| scrapy_1 | 41 | 202 | NOT_REACHED |
| scrapy_3 | 32 | 158 | NOT_REACHED |
| scrapy_4 | 2 | 7 | NOT_REACHED |
| thefuck_1 | 7 | 31 | NOT_REACHED |
| thefuck_4 | 6 | 30 | NOT_REACHED |
| tornado_1 | 200 | 7059 | NOT_REACHED |
| tornado_4 | 200 | 6415 | NOT_REACHED |
| tornado_5 | 200 | 1362 | NOT_REACHED |
| tqdm_1 | 94 | 466 | NOT_REACHED |
| tqdm_2 | 2 | 8 | NOT_REACHED |
| youtube-dl_1 | 200 | 67244 | **REACHED** |
| youtube-dl_10 | 200 | 30365 | **REACHED** |
| youtube-dl_2 | 200 | 59653 | **REACHED** |
| youtube-dl_20 | 200 | 63820 | **REACHED** |
| youtube-dl_5 | 200 | 52172 | **REACHED** |

### 2. Exception 覆盖（Fisher exact test）

| 指标 | keep=0 (27) | keep>0 (11) | Fisher p |
|------|------------|------------|----------|
| 有 exception 事件 | 27 (100%) | 9 (82%) | 0.078 |
| 有非 import exception | 19 (70%) | 6 (55%) | 0.457 |
| 覆盖源码文件 | 24 (89%) | 10 (91%) | 1.000 |

**结论：exception 覆盖与 keep=0 无显著关联。**

### 3. Phase 1 用的测试类型

**不是 passing vs failing test 的问题。** BugsInPy 的 `run_test.sh` 里确实是特定的 failing test function（如 `test_get_future_imports`），但 **pipeline 根本没读 run_test.sh**。

`bugsinpy_setup._read_bug_info()` 读的是 `bug.info`，该文件没有 `test_command` 字段，所以 `setup_instance()` 回退到 `"python -m pytest"`——**所有 38 个实例都在跑完整 test suite 而非特定 failing test**。

### 4. 真正的根因

**38/38 实例的 specific failing test function 均未被 trace 覆盖**（youtube-dl 5 个虽 REACHED，但因 trace 30K-67K 事件被稀释，teacher 仍判 drop）。

两个叠加的根因：

1. **错误的 test command**：Pipeline 用 `python -m pytest`（全量 test suite），而非 `run_test.sh` 里的特定 failing test（如 `pytest tests/test_black.py::BlackTestCase::test_get_future_imports`）。Trace 要么停在 import 阶段，要么被海量无关 test 事件稀释。

2. **Python 版本不匹配**：BugsInPy 要求 Python 3.6-3.8，服务器跑 Python 3.12。很多模块 import 阶段就崩了（black_* 只有 41-51 个 module-level 事件）。

### 5. 为什么有些 keep>0

11 个 keep>0 实例也没到达 failing test，但 teacher 在 import/初始化阶段碰巧发现了有诊断价值的异常（如 cookiecutter 的 `InvalidModeException`、`CookiecutterException` 返回 `None`）。这是 **巧合而非系统性覆盖**。

### 6. 结论

**低 keep rate 是 trace 覆盖问题，不是 teacher 过严问题。** Teacher 对 import-only segments 判 drop 是正确的——这些 segments 确实没有 buggy path 的诊断信息。

**修复建议**：在 `bugsinpy_setup._read_bug_info()` 中读取 `run_test.sh` 作为 `test_command`，替代 `"python -m pytest"` 回退值。

---
