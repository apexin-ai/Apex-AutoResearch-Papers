# analysis ae only data inspection

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ae_only_data_inspection_20260515T123025_result.json`
- **Structured JSON:** [`1a722ce1685c02371908.json`](../../sessions/1a/1a722ce1685c02371908.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕，汇总结果如下。

---

## ae_only fallback locals dump 分析结果

### 基本统计

| 指标 | 值 |
|------|-----|
| 总样本数 (test) | 1190 |
| Fallback 样本 | 1084/1190 (91.1%) |
| Non-fallback 样本 | 106/1190 |
| Fallback pass/fail | 815/269 |
| Non-fallback pass/fail | 36/70 |
| No-trace 样本 | 70 |

### 样本展示

**SAMPLE 1** (label=pass, FALLBACK, HumanEval/99)
```
[ASSERT] assert candidate("10") == 10, "Test 1" | actual=10, expected=10
[ASSERT] assert candidate("14.5") == 15, "Test 2" | actual=15, expected=15
[ASSERT] assert candidate("-15.5") == -16, "Test 3" | actual=-16, expected=-16
[ASSERT] assert candidate("15.3") == 15, "Test 3" | actual=15, expected=15
[ASSERT] assert candidate("0") == 0, "Test 0" | actual=0, expected=0
[ASSERT] assert candidate("0") == 0, "Test 0" | [fallback: full locals] candidate='&lt;function closest_integer at 0x7fed9954a480>'
```
Leakage: **NONE**

**SAMPLE 2** (label=pass, FALLBACK, HumanEval/72)
```
[ASSERT] assert candidate([3, 2, 3], 9) is True | [fallback: full locals] candidate='&lt;function will_it_fly at 0x7fe872b1a480>'
[ASSERT] assert candidate([1, 2], 5) is False | [fallback: full locals] candidate='&lt;function will_it_fly at 0x7fe872b1a480>'
[ASSERT] assert candidate([3], 5) is True | [fallback: full locals] candidate='&lt;function will_it_fly at 0x7fe872b1a480>'
[ASSERT] assert candidate([3, 2, 3], 1) is False | [fallback: full locals] candidate='&lt;function will_it_fly at 0x7fe872b1a480>'
...
```
Leakage: True/False 出现在 **assert 文本** 中（`is True`/`is False` 是测试代码本身的一部分），不在 locals dump 中

**SAMPLE 3** (label=pass, FALLBACK, MBPP/555) — 典型的大型 fallback dump
```
[ASSERT] assert difference(3) == 30 | actual=30, expected=30
[ASSERT] assert difference(3) == 30 | [fallback: full locals] math="&lt;module 'math' from '...'>, 
  re="&lt;module 're' from '...'>, string="&lt;module 'string' ...>", heapq=..., bisect=..., 
  copy=..., operator=..., collections=..., itertools=..., functools=..., 
  List='typing.List', Tuple='typing.Tuple', Dict='typing.Dict', Set='typing.Set', 
  Optional='typing.Optional', Any='typing.Any', Union='typing.Union', 
  defaultdict="&lt;class 'collections.defaultdict'>", Counter=..., OrderedDict=..., 
  deque=..., combinations=..., permutations=..., product=..., chain=..., 
  accumulate=..., reduce='&lt;built-in function reduce>', 
  lru_cache='&lt;function lru_cache at 0x...>', 
  difference='&lt;function difference at 0x...>'
```
Total length: ~5000 chars. Leakage: **NONE**

**SAMPLE 6** (label=fail, FALLBACK, MBPP/143)
```
[ASSERT] assert find_lists(([1,2,3,4],[5,6,7,8])) == 2 | actual=2, expected=2
[ASSERT] assert find_lists(...) == 2 | [fallback: full locals] math=..., re=..., ..., 
  find_lists='&lt;function find_lists at 0x...>'
[ASSERT] assert find_lists(...) == 2 | actual=3, expected=3
[ASSERT] assert find_lists(...) == 2 | [fallback: full locals] math=..., ..., 
  find_lists='&lt;function find_lists at 0x...>'
```
Leakage: **NONE**

**SAMPLE 7** (label=fail, FALLBACK, MBPP/259)
```
[ASSERT] assert maximize_elements(...) == ((6,7),(4,9),(2,9),(7,10)) 
  | actual=[[6,7],[4,5],[2,9],[7,3]], expected=[[6,7],[4,9],[2,9],[7,10]]
[ASSERT] assert maximize_elements(...) | [fallback: full locals] math=..., ..., 
  maximize_elements='&lt;function maximize_elements at 0x...>'
```
Leakage: **NONE**

**SAMPLE 8** (label=fail, FALLBACK, MBPP/738)
```
[ASSERT] assert is_Sum_Of_Powers_Of_Two(10) == True | actual=False, expected=True
[ASSERT] assert is_Sum_Of_Powers_Of_Two(10) == True | [fallback: full locals] math=..., ...
[ASSERT] assert is_Sum_Of_Powers_Of_Two(10) == True | actual=False, expected=False
...
```
Leakage: True/False 出现在 **assert 文本和 actual/expected 值** 中（函数返回值本身就是 bool），不在 locals dump

**SAMPLE 9** (label=fail, FALLBACK, HumanEval/162)
```
[ASSERT] assert candidate('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62' 
  | actual=None, expected='3e25960a79dbc69b674cd4ec67a72c62'
[ASSERT] assert candidate('Hello world') == '...' 
  | [fallback: full locals] candidate='&lt;function string_to_md5 at 0x...>'
```
Leakage: **NONE**

**NON-FALLBACK 对照** (HumanEval/44, label=pass)
```
[ASSERT] assert candidate(8, 3) == "22" | actual='22', expected='22'
[ASSERT] assert candidate(9, 3) == "100" | actual='100', expected='100'
[ASSERT] assert candidate(234, 2) == "11101010" | actual='11101010', expected='11101010'
```

**NON-FALLBACK 对照** (label=fail) — 70 个 `[No trace available]`

---

### SUMMARY

```
Total fallback samples:                      1084/1190 (91.1%)

Fallback containing "pass"/"fail" string:    34/1084 (3.1%)
  → ALL 34 are label=pass
  → "fail" appears in assert MESSAGE TEXT: "This prints if this assert fails"
  → "pass"/"fail" in locals dump part:       0/34 (0%)

Fallback containing "error"/"assert" string: 1084/1084 (100%)
  → ALL from "[ASSERT]" line prefix — structural, not semantic

Fallback containing "True"/"False" string:   216/1084 (19.9%)
  → Appear in assert text ("is True") or actual/expected values (bool return)
  → NOT in locals dump

"pass"/"fail" in locals dump:                0/1084 (0%)
```

### Fallback locals dump 内容本质

**fallback dump 里只有一种东西：scope 内的变量列表**，具体是：
1. **标准库 module 引用**：math, re, string, heapq, bisect, copy, operator, collections, itertools, functools
2. **typing 类型别名**：List, Tuple, Dict, Set, Optional, Any, Union
3. **collections/itertools 类引用**：defaultdict, Counter, OrderedDict, deque, combinations, permutations, product, chain, accumulate
4. **内置函数**：reduce, lru_cache
5. **被测函数指针**：`candidate='&lt;function XXX at 0x...>'`

**locals dump 中不含任何 pass/fail/error/True/False 等可能泄漏 verdict 的信息。** 所有检测到的 "可疑字符串" 都来自 `[ASSERT]` 行前缀、assert 文本本身（测试代码的一部分，pass/fail 两类样本都能看到）、以及 actual/expected 值（函数返回值本身是 bool 时）。

---
