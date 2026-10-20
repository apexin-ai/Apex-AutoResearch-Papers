# diag classify exit none

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_classify_exit_none_20260515T054057_result.json`
- **Structured JSON:** [`345ff1cdb8e85319d958.json`](../../sessions/34/345ff1cdb8e85319d958.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

深入检查完成。black_1 和 cookiecutter_3 虽然触及了 buggy 文件但仅有 `&lt;module>` 事件（import 级别），buggy 函数未被调用。需要重新分类为 IMPORT_ONLY。

现在生成最终分类表。实际有 19 个 exit=None 实例（非 pytest runner），而非 21 个。

## 分类结果

### exit=None 的 19 个实例（非 pytest runner）

| instance_id | runner | events | test_funcs_found | buggy_func_found | buggy_file_hit | classification |
|-------------|--------|--------|------------------|------------------|----------------|----------------|
| tornado_1 | unittest | 5286 | TestWebSocketHandler | WebSocketHandler, WebSocketProtocol, WebSocketProtocol13 | websocket.py | **CONFIRMED_GOOD** |
| tornado_2 | unittest | 3755 | — | HTTP1Connection | http1connection.py | **CONFIRMED_GOOD** |
| tornado_4 | unittest | 4575 | — | StaticFileHandler | web.py | **CONFIRMED_GOOD** |
| tornado_5 | unittest | 2741 | TestIOLoop, TestIOLoopAddCallback, TestIOLoopAddCallbackFromSignal | PeriodicCallback | ioloop.py | **CONFIRMED_GOOD** |
| tornado_7 | unittest | 3287 | TestIOLoop, TestIOLoopAddCallback, TestIOLoopAddCallbackFromSignal | IOLoop | ioloop.py | **CONFIRMED_GOOD** |
| youtube-dl_1 | unittest | 45807 | TestURLIE, TestUtil, test_match_str | _match_one | utils.py | **CONFIRMED_GOOD** |
| youtube-dl_2 | unittest | 49974 | TestIE, TestInfoExtra | InfoExtractor | common.py | **CONFIRMED_GOOD** |
| youtube-dl_5 | unittest | 35459 | TestURLIE, TestUtil, test_unified_timestamps | unified_timestamp | utils.py | **CONFIRMED_GOOD** |
| youtube-dl_10 | unittest | 19481 | TestURLIE, TestUtil, test_js_to_json_realworld | js_to_json | utils.py | **CONFIRMED_GOOD** |
| youtube-dl_20 | unittest | 41275 | TestURLIE, TestUtil, test_get_element_by_attribute | get_elements_by_attribute | utils.py | **CONFIRMED_GOOD** |
| black_1 | unittest | 147 | — | — | black.py (module-level only) | **IMPORT_ONLY** |
| cookiecutter_1 | other (tox) | 173 | — | — | — | **IMPORT_ONLY** |
| cookiecutter_2 | other (tox) | 173 | — | — | — | **IMPORT_ONLY** |
| cookiecutter_3 | other (tox) | 37 | — | — | prompt.py (module-level only) | **IMPORT_ONLY** |
| scrapy_1 | unittest | 160 | — | — | offsite.py (module-level only) | **IMPORT_ONLY** |
| scrapy_2 | unittest | 176 | — | — | datatypes.py (module-level only) | **IMPORT_ONLY** |
| scrapy_3 | unittest | 164 | — | — | redirect.py (module-level only) | **IMPORT_ONLY** |
| scrapy_4 | unittest | 30 | — | — | — | **IMPORT_ONLY** |
| scrapy_7 | unittest | 181 | — | — | — | **IMPORT_ONLY** |

### pytest runner 实例（14 个，供参考）

| instance_id | test_funcs | 推测 exit_code |
|-------------|-----------|---------------|
| thefuck_1 | test_get_new_command | 0 或 1 |
| thefuck_4 | TestFish | 0 或 1 |
| luigi_1, 2, 5, 10, 14 | TestNotificationsTask | 0 或 1 |
| thefuck_2 | — | 4 (no tests collected) |
| fastapi_1, 2 | — | 4 |
| httpie_1, 2 | — | 4 |
| sanic_1, 2 | — | 4 |

### 汇总

| 分类 | 数量 | 实例 |
|------|------|------|
| **CONFIRMED_GOOD** (exit=None) | 10 | tornado_1/2/4/5/7, youtube-dl_1/2/5/10/20 |
| **IMPORT_ONLY** (exit=None) | 9 | black_1, cookiecutter_1/2/3, scrapy_1/2/3/4/7 |
| pytest 有测试运行 (exit=0/1) | 7 | thefuck_1/4, luigi_1/2/5/10/14 |
| pytest 无测试收集 (exit=4) | 7 | thefuck_2, fastapi_1/2, httpie_1/2, sanic_1/2 |

### 可用于 scoring 的实例

pytest 测试实际运行的 7 个 + exit=None CONFIRMED_GOOD 的 10 个 = **17 个实例可用于 scoring**。

IMPORT_ONLY 的 9 个和 exit=4 的 7 个 trace 仅含 import/setup 事件，测试函数未执行，不可用于评估。

---
