# infra diagnose exit0 and resume

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_diagnose_exit0_and_resume_20260514T214455_result.json`
- **Structured JSON:** [`56fc559b894e398042b2.json`](../../sessions/56/56fc559b894e398042b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 排查报告

### 1. 根因

**`executor.py:59` 的 `exec()` 调用不捕获 `SystemExit`。**

LLM 生成的代码通过 `exec(code, {"__builtins__": __builtins__})` 在主进程内执行。`__builtins__` 包含 `exit()` 和 `quit()`。如果 LLM 生成的代码含 `exit()`/`quit()`/`sys.exit(0)`，会抛出 `SystemExit`——这是 `BaseException` 的子类，**不是 `Exception` 的子类**，因此穿透 executor.py → pipeline.py 的所有 `except Exception` 块，导致进程以 EXIT_CODE=0 静默退出。

无 bare `except:`，无其他 `sys.exit`（仅 `evaluate_mvp.py` 有一个不相关的）。`disagree.py`/`repair.py` 无退出路径。

### 2. 修复内容

`executor.py` L76 新增 `except SystemExit as e:` 捕获块（在 `except Exception` 之前），将 `SystemExit` 转为 `ExecResult(verdict="Error")`，pipeline 继续处理下一个样本而非退出。

备份：`src/executor.py.bak_exit_fix`

### 3. JSONL 当前行数

**154 行**（原始 147 + PID 56393 新增 7 行）。folio_validation_148 已被成功处理。

### 4. PID 56393 状态

**还活着**（运行 26 分钟，状态 S）。已过 folio_validation_148，正在继续处理后续样本。但它运行的是**未修复的代码**，仍可能在其他样本上遇到同样的 bug 而静默退出。

建议：kill 56393 后用修复后的代码重启（resume 从 154 行继续），由你决定。

---
