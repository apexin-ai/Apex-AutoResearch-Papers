# DebugBench Exception Extraction Bug Analysis

## Bug Summary
`debugbench_format_data.py` 的 `compress_exception_only()` 丢失 62.7% fail 样本的异常信号。

## Root Cause
`compress_exception_only()` (L96) 仅调用 `compressor._extract_exceptions(trace_events)`，该方法只检查 `trace_raw` 中 `event=="exception"` 的事件。

两个问题：
1. **625/1006 fail 样本 trace_raw 为空列表**（syntax error 等在代码解析阶段就失败，无法产生 trace 事件）
2. **5/1006 fail 样本 trace 达 2000 事件上限**，异常发生在上限之后（如 RecursionError, IndexError）
3. `format_sample()` L124 的 `if trace_raw` 短路：空 trace 直接返回 "[No exception data in trace]"，不检查其他字段

但所有 1006 个 fail 样本都有 `test_results.error` 字段记录了实际异常信息。所有 1042 个 pass 样本的 `test_results.error` 为 None。

## Empty trace 分布（按 bug_category）
| Category | Total fail | Empty trace | Has exc event | Has trace no exc |
|----------|-----------|-------------|---------------|-----------------|
| syntax error | 200 | 173 (86.5%) | 27 | 0 |
| logic error | 136 | 12 (8.8%) | 121 | 3 |
| reference error | 154 | 10 (6.5%) | 143 | 1 |
| multiple error | 516 | 430 (83.3%) | 85 | 1 |

## Fix (2 changes)
### 1. compress_exception_only() — L96-104
```python
# Before:
def compress_exception_only(compressor, trace_events):
    parts = compressor._extract_exceptions(trace_events)
    if not parts:
        return EMPTY_MESSAGES["exception_only"]
    return "\n".join(parts)

# After:
def compress_exception_only(compressor, trace_events, test_results=None):
    parts = compressor._extract_exceptions(trace_events)
    if not parts and test_results and test_results.get("error"):
        parts = [f'[ERROR] {test_results["error"]}']
    if not parts:
        return EMPTY_MESSAGES["exception_only"]
    return "\n".join(parts)
```

### 2. format_sample() — L127-129
```python
# Before:
if condition == "exception_only":
    trace_text = compress_exception_only(compressor, trace_raw) if trace_raw else EMPTY_MESSAGES["exception_only"]

# After:
if condition == "exception_only":
    test_results = item.get("test_results", {})
    trace_text = compress_exception_only(compressor, trace_raw, test_results)
```

## Verification
| Metric | Before fix | After fix |
|--------|-----------|-----------|
| Fail with exception signal | 376/1006 (37.4%) | 1006/1006 (100%) |
| Pass with exception signal | 0/1042 (0%) | 0/1042 (0%) |
| Empty trace (exception_only) | 1668/2048 (81.4%) | 1042/2048 (50.9%) |
| Theoretical upper bound | 69.2% | 100.0% |

## Sample outputs (after fix)
- SyntaxError: `[ERROR] SyntaxError: expected an indented block after class definition on line 2 (<solution>, line 3)`
- AttributeError: `[ERROR] AttributeError at line 4: 'Solution' object has no attribute 'concat' | locals: self=..., word1=['ab', 'c'], word2=['a', 'bc']`
- RecursionError (edge case, 2000 events): `[ERROR] RecursionError: maximum recursion depth exceeded`
