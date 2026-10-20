# run oracle full validation

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_oracle_full_validation_20260515T140208_result.json`
- **Structured JSON:** [`7d4035642effd89edf2b.json`](../../sessions/7d/7d4035642effd89edf2b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 14 个实例 patch 都 apply 成功（`diff_apply=True`），10 个失败全是 test infra 问题。

## Oracle 全量验证结果：4/14 PASS

| Instance | test_pass | failure_reason |
|---|---|---|
| **black_1** | FAIL | 测试方法名不存在 (`BlackTestCase` 无 `test_works_in_mono_process_only_environment`) |
| **cookiecutter_1** | FAIL | pytest-cov 未装 (`--cov-report` 参数不识别) |
| **cookiecutter_2** | FAIL | pytest-cov 未装（同上） |
| **cookiecutter_3** | FAIL | conftest ImportError（cookiecutter 循环导入） |
| **fastapi_2** | FAIL | 测试方法不存在 (`test_router_ws_depends_with_override` not found) |
| **httpie_2** | **PASS** | |
| **luigi_5** | FAIL | `ModuleNotFoundError: No module named 'luigi'`（未 pip install -e .） |
| **sanic_2** | FAIL | `ModuleNotFoundError: No module named 'sanic'`（未 pip install -e .） |
| **scrapy_2** | FAIL | scrapy import 失败（`_monkeypatches.py` 依赖缺失） |
| **scrapy_7** | FAIL | scrapy import 失败（同上） |
| **tornado_2** | FAIL | 测试方法名不存在（截断的方法名） |
| **youtube-dl_1** | **PASS** | |
| **youtube-dl_5** | **PASS** | |
| **youtube-dl_20** | **PASS** | |

### 失败归类

所有 10 个失败都是 **test infra 问题**（patch 本身都正确 apply），分 3 类：

1. **测试方法名无效** (3): black_1, fastapi_2, tornado_2 — test command 引用了不存在的测试方法
2. **缺少 pytest-cov 插件** (2): cookiecutter_1, cookiecutter_2 — bugsinpy env 没装 pytest-cov
3. **项目包未安装/依赖缺失** (5): cookiecutter_3, luigi_5, sanic_2, scrapy_2, scrapy_7 — 项目自身未 `pip install -e .` 或缺关键依赖

### 可用实例

只有 **4 个实例的 test infra 可用**：httpie_2, youtube-dl_1, youtube-dl_5, youtube-dl_20。这 4 个是 v2 修复实验中唯一可以基于测试通过率评估的实例。

---
