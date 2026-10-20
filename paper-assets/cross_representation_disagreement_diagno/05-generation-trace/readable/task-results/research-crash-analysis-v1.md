# research crash analysis v1

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_crash_analysis_v1_20260514T081827_result.json`
- **Structured JSON:** [`777a1ad486398dd02b45.json`](../../sessions/77/777a1ad486398dd02b45.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data. Let me compile the final analysis.

---

## MVP 第一轮 FOL Crash 分析报告

### 1. 总览

| 指标 | 值 |
|------|-----|
| 总样本数 | 50 |
| FOL 有效执行 | 50 |
| **FOL crashes** | **38 (76.0%)** |
| FOL 成功执行 | 12 |
| FOL 正确判断 | 7 (14%) |
| Pipeline errors | 0 |
| Code exec 正常 | 40 (80%) |

### 2. Crash 原因分类

| 类别 | 数量 | 占比 | 根因 |
|------|------|------|------|
| **z3_expression_expected** | 14 | 36.8% | ForAll/Exists 中误用 Sort 作为变量 |
| **z3_other** | 12 | 31.6% | Sort 类型混淆（见子分类） |
| **type_error** | 5 | 13.2% | 把 SortRef 当构造函数调用 |
| **name_error** | 3 | 7.9% | 未定义变量 |
| **z3_sort_mismatch** | 3 | 7.9% | 函数参数 Sort 类型不匹配 |
| **attribute_error** | 1 | 2.6% | 对象属性访问错误 |

#### z3_other 子分类（12 个）

| 子类 | 数量 | 说明 |
|------|------|------|
| Z3 sort expected | 5 | Function 定义时参数类型错误 |
| enumeration sort already declared | 3 | Datatype + EnumSort 重复声明同名 sort |
| Value cannot be converted to Bool | 2 | 自定义 Bool sort 与 BoolSort() 混淆 |
| Invalid bounded variable(s) | 1 | ForAll 绑定变量格式错误 |
| Symbolic → concrete Boolean cast | 1 | Z3 符号值用在 Python bool 上下文 |

### 3. 三大反模式（覆盖 ~90% crash）

**反模式 A：ForAll 直接用 Sort 名而非绑定变量** — ~40% crashes

```python
# 错误：People 是 Sort，不是变量
People = DeclareSort('People')
s.add(ForAll(People, Implies(f(People), g(People))))  # CRASH

# 也错误：Sort 不可调用
s.add(ForAll(People(), Implies(...)))   # TypeError: SortRef not callable
s.add(ForAll([Object('x')], ...))       # TypeError: SortRef not callable

# 正确：
x = Const('x', People)
s.add(ForAll([x], Implies(f(x), g(x))))
```

**反模式 B：自定义 Bool Sort 替代 BoolSort()** — ~20% crashes

```python
# 错误：
Bool = DeclareSort('Bool')  # 创建了新 Sort，和 Z3 BoolSort 不兼容
f = Function('f', People, Bool)  # Sort mismatch

# 正确：
f = Function('f', People, BoolSort())
```

**反模式 C：Datatype/EnumSort 误用** — ~15% crashes

```python
# 错误：先 Datatype 后 EnumSort 同名
Person = Datatype('Person')
Person, marvin = EnumSort('Person', ['Marvin'])  # 重复声明

# 错误：EnumSort 值直接在 ForAll 中当变量
Animal, (Human, Mammal, Virus) = EnumSort('Animal', [...])
s.add(ForAll(Human, ...))  # Human 是枚举值，不是变量
```

### 4. 成功 FOL 样本（few-shot 候选）

以下 5 个样本正确执行且判断正确：

**Sample 1: folio_validation_4** (verdict: Unknown ✓)
```python
from z3 import *
Employee = DeclareSort('Employee')
Bool = BoolSort()
james = Const('james', Employee)
meeting_with_customers = Function('meeting_with_customers', Employee, Bool)
appear_in_company = Function('appear_in_company', Employee, Bool)
lunch_in_company = Function('lunch_in_company', Employee, Bool)
lunch_at_home = Function('lunch_at_home', Employee, Bool)
work_remotely = Function('work_remotely', Employee, Bool)
s = Solver()
# Premises encoded with proper ForAll + bound variable pattern
# ... (uses james as ground constant, no ForAll needed for this problem)
```

**Sample 2: folio_validation_12** (verdict: True ✓)
```python
from z3 import *
Game = DeclareSort('Game')
Company = DeclareSort('Company')
Bool = BoolSort()
legend_of_zelda = Const('legend_of_zelda', Game)
japanese_game_company = Const('japanese_game_company', Company)
created_by = Function('created_by', Game, Company, Bool)
in_top_10 = Function('in_top_10', Game, Bool)
sold_more_than_1m = Function('sold_more_than_1m', Game, Bool)
s = Solver()
s.add(created_by(legend_of_zelda, japanese_game_company))
s.add(Implies(sold_more_than_1m(legend_of_zelda), in_top_10(legend_of_zelda)))
s.add(sold_more_than_1m(legend_of_zelda))
conclusion = in_top_10(legend_of_zelda)
s.push()
s.add(Not(conclusion))
if s.check() == unsat:
    print("True")
else:
    s.pop()
    s.push()
    s.add(conclusion)
    if s.check() == unsat:
        print("False")
    else:
        print("Unknown")
```

**Sample 3: folio_validation_14** (verdict: False ✓)
```python
from z3 import *
Game = DeclareSort('Game')
Company = DeclareSort('Company')
legend_of_zelda = Const('legend_of_zelda', Game)
japanese_game_company = Const('japanese_game_company', Company)
created_by = Function('created_by', Game, Company)
in_top_10 = Function('in_top_10', Game, BoolSort())
sold_more_than_one_million = Function('sold_more_than_one_million', Game, BoolSort())
s = Solver()
s.add(created_by(legend_of_zelda) == japanese_game_company)
s.add(Implies(in_top_10(legend_of_zelda), created_by(legend_of_zelda) == japanese_game_company))
s.add(Implies(sold_more_than_one_million(legend_of_zelda), in_top_10(legend_of_zelda)))
s.add(sold_more_than_one_million(legend_of_zelda))
conclusion = Not(in_top_10(legend_of_zelda))
# Standard entailment check...
```

注意：成功样本有个共同特征 —— 都**避免了 ForAll**，只用 ground constants 建模。需要 ForAll 的样本几乎全部 crash。

### 5. 修复方向建议

| 方向 | 可修的 crash 数 | 方法 |
|------|----------------|------|
| **Prompt 加 Z3 ForAll 正确用法示例** | ~22 (58%) | 在 prompt 中显式展示 `x = Const('x', Sort); ForAll([x], ...)` 模式，附反例 |
| **Prompt 禁止自定义 Bool sort** | ~5 (13%) | 明确要求 `BoolSort()` 用于谓词返回值 |
| **Prompt 禁止 Datatype/EnumSort 混用** | ~3 (8%) | 统一用 `DeclareSort` + `Const`，禁用 EnumSort |
| **执行层：自动修复 Sort→Const** | ~22 (58%) | 在 exec 前做 AST 预处理，检测 `ForAll(SortName, ...)` 并自动插入 `Const` 绑定 |
| **执行层：自动替换 DeclareSort('Bool')** | ~5 (13%) | 正则替换为 `BoolSort()` |

**优先级**：先改 prompt（加 few-shot + 禁令），预计可将 crash rate 从 76% 降到 ~30%。剩余的用执行层 AST 预处理兜底。

---
