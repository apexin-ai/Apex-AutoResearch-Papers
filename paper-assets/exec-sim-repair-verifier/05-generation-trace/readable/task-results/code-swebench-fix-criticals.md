# code swebench fix criticals

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_swebench-fix-criticals_20260512T031825_result.json`
- **Structured JSON:** [`59761d361e044e94f6b2.json`](../../sessions/59/59761d361e044e94f6b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 修复结果

### 4 个 Fix 的实现方式

| Fix | 方案 | 结果 |
|-----|------|------|
| **P0-1 test=代码** | 对每个 instance，从 SWE-bench Docker image 启动容器，apply test_patch 后用 AST 提取测试函数体 | 1949/1953 (99.8%) 是代码 |
| **P0-2 code+上下文** | 从容器读取被修改文件的 base 版本，解析 patch hunk header 的行号，截取 ±50 行拼接到 patch 后面 | 1953/1953 (100%) 有上下文 |
| **P0-3 exec_output 噪声** | 用 SWE-bench eval 脚本自带的 `>>>>> Start/End Test Output` marker 截取，fallback 到 test framework marker 或尾部 2000 chars | 不再有 conda 噪声 |
| **P0-4 F2P 平衡** | 新增 `balance_data()` + `--balance_strategy` 参数，默认 `upsample_f2p` 复制 F2P 到 20% | 2.4% → 20.0% |

### 验证数据样本

**Record 1** (django, gold, f2p, label=1):
- `test`: `def test_validate_custom_error(self): ...` (629 chars 实际代码)
- `code`: patch + `--- Modified File: django/contrib/postgres/constraints.py (lines 1-81) ---` 上下文
- `execution_output`: `+ ./tests/runtests.py --verbosity 2 ...` (无 conda 噪声)

**Record 2** (sympy, mutation_off_by_one, p2p, label=1):
- `test`: `def test_issue_13651(): expr = c + Mul(-1, a + b, ...) ...` (121 chars 实际代码)
- `code`: patch + `--- Modified File: sympy/printing/latex.py (lines 1427-1526) ---` 上下文
- `execution_output`: `+ PYTHONWARNINGS=ignore ...` (无 conda 噪声)

### 未提取到代码的 4 条记录

4/1953 (0.2%) 是 django P2P 的一个特殊 test name `"Partial unique constraints are not ignored by"` — 它不是标准 `def test_xxx` 格式，AST 无法匹配。影响可忽略。

### 新增 CLI 参数

- `--mode dry_run|pilot|full` (替代原 `--dry_run`)
- `--balance_strategy none|upsample_f2p|downsample_p2p|weighted` (默认 `upsample_f2p`)

---
