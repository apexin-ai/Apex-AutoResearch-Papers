# diag failed instances v2

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_failed_instances_v2_20260515T053617_result.json`
- **Structured JSON:** [`3748bec890efbe4bbf3e.json`](../../sessions/37/3748bec890efbe4bbf3e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。以下是完整报告。

---

## Part A: 5 个 0 events 实例的根因

### black_2, black_5, black_14
**根因**：这些 git checkout 的 `tests/` 目录缺少 `__init__.py`。

```
# 验证 black_2:
ls tests/__init__.py  → No such file or directory
python -m unittest -q tests.test_black.BlackTestCase.test_fmtonoff4
  → ModuleNotFoundError: No module named 'tests.test_black'
```

unittest loader 的错误发生在 stdlib 代码中（`unittest/loader.py`），不在 PROJECT_ROOT 下，trace callback 过滤掉了所有事件 → 0 events。

对比 black_1 成功（147 events）：black_1 的 checkout 版本有 `tests/__init__.py`，import 能进入 `tests/test_black.py` → `import black` → 进入项目代码 → 有 events（虽然最终 black.py 导入 mypy_extensions 失败，test 也没真正执行）。

### tqdm_1, tqdm_2
**根因**：run_test.sh 用 `python3 -m pytest`，但 trace_collector 的命令解析器只匹配 `python`，不匹配 `python3`。

`trace_collector.py` 中的解析逻辑：
```python
if _test_parts[0] == 'python' and ...:    # 'python3' != 'python' → False
elif _test_parts[0] in ('pytest', 'py.test'):  # 'python3' 不匹配
else:
    _test_runner = 'exec'  # fallback: exec(open('python3').read()) → FileNotFoundError
```

即使修了这个 bug，tqdm 测试还需要 `nose` 模块（未安装），也无法运行。

---

## Part B: pytest exit code 4 问题

### 实际 exit code 分布（40 个实例）

用户说的"所有 33 个成功实例都是 exit code 4"不准确。实际分布：

| exit_code | 数量 | 含义 |
|-----------|------|------|
| 0 | 1 | thefuck_1 — **唯一真正成功的 pytest 实例** |
| 1 | 1 | thefuck_4 — 测试运行但断言失败 |
| 4 | 15 | pytest 收集失败，测试从未执行 |
| None | 16 | unittest runner（不产生 pytest exit code） |
| 0 events | 7 | 完全失败 |

### 根因：共享 bugsinpy 环境缺少项目特有依赖

所有项目共用一个 `bugsinpy` conda env，但各项目需要不同的依赖：

| 项目 | 缺失依赖 | 影响 |
|------|----------|------|
| scrapy | twisted | import 失败 |
| thefuck_2 | mock | import 失败 |
| black | mypy_extensions | import 失败 |
| tqdm | nose | import 失败 |
| cookiecutter | pytest-cov（setup.cfg 配置） | pytest 参数解析失败 |
| luigi | 某些 server deps | import 失败 |
| sanic, httpie, fastapi | 各自框架依赖 | import 失败 |

手动验证结果：

```
youtube-dl_1:  Ran 1 test in 0.000s → OK  ✅ 测试真正执行
tornado_1:     Ran 1 test in 0.005s → OK  ✅ 测试真正执行
scrapy_1:      ModuleNotFoundError: twisted → FAILED (errors=1) ❌ 仅 import
luigi_1:       ERROR collecting → exit code 4 ❌ 仅 import
cookiecutter_1: unrecognized arguments: --cov-report ❌ pytest 启动就失败
```

### 真正执行了测试的实例（12/33）

| 项目 | 实例数 | 说明 |
|------|--------|------|
| thefuck | 2 | thefuck_1(pass), thefuck_4(fail) |
| youtube-dl | 5 | 纯 Python，无外部依赖，全部运行成功 |
| tornado | 5 | 自包含，全部运行成功 |

其余 21 个实例的 traces 只包含 **import/setup 阶段**的事件，不包含实际测试执行。

---

## 修复方案

### 1. trace_collector.py 命令解析 bug（简单）
```python
# 当前: if _test_parts[0] == 'python'
# 修复: if _test_parts[0] in ('python', 'python3', 'python3.8', ...)
```
或更通用：`if _test_parts[0].startswith('python')`

### 2. 依赖问题（核心，两种策略）

**策略 A（快速）**：在 bugsinpy env 中批量安装缺失依赖
```bash
pip install twisted mock nose mypy_extensions pytest-cov
pip install sanic httpie cookiecutter fastapi pydantic
```
风险：版本冲突（不同项目需要不同版本的同一依赖）。

**策略 B（稳健）**：每个项目创建独立 conda/venv 环境，使用 BugsInPy 自带的 setup 脚本。工作量大但结果可靠。

### 3. black `__init__.py` 问题
改用 `python -m pytest` 替代 `python -m unittest`（pytest 不需要 `__init__.py`），或者在 checkout 后创建 `tests/__init__.py`。

---

## 研究影响评估

**12 个真正执行测试的实例可用于 structural vs line 对比实验。** 涵盖 thefuck（规则匹配）、youtube-dl（数据处理管道）、tornado（异步网络），有一定多样性。

**21 个 import-only traces 不可用**，原因：
- 不触发 buggy code path
- import trace 结构单一（顺序模块加载，无循环/分支）
- buggy/fixed 版本在 import 阶段几乎无差异

**建议**：先用 12 个 working 实例做 proof-of-concept，同时修复依赖问题以获得完整的 40 实例 trace 数据。如果信号足够强，12 个就够写 paper；否则必须修。

---
