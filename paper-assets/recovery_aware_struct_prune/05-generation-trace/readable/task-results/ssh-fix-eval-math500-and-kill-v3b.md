# ssh fix eval math500 and kill v3b

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix_eval_math500_and_kill_v3b_20260523T142237_result.json`
- **Structured JSON:** [`68972d6ef9947f56cb1c.json`](../../sessions/68/68972d6ef9947f56cb1c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Westb-23072 file verified:
- Line 67: trig function normalization (`\sin`, `\cos`, etc.)
- Lines 99-101: full-text fallback (`boxed_full` extraction)
- File size: 8568 bytes (matches westd-32935)

---

## 最终报告

### 1. Kill 结果
- PID 139697 (tmux `eval_math500_grpo_standard_20_fair_2048_v3b`) + 子进程 PID 139706 已在 westd-32935 上终止
- GPU 2 已释放

### 2. Bug 修复详情

**Bug A — 答案提取失败 (11 samples)**
- 根因：`&lt;think>` 标签被移除后，`\boxed{}` 答案也被丢弃；模式匹配不够灵活
- 修复：`extract_model_answer()` 添加全文回退逻辑（lines 97-104），在 clean text 提取失败时搜索完整文本中的 `\boxed{}` 和 pattern matches
- 模式调整：`(?:final )?` → `(?:\w+ )?`（更灵活）；`[Aa]nswer[:\s]*` → `\b[Aa]nswer\s*(?:is|:)\s*`（更精确）

**Bug B — 答案匹配失败 (5 samples)**
- 根因：`normalize_answer()` 未处理空格差异（逗号后空格、括号内空格、运算符周围空格）和 LaTeX 函数反斜杠（`\cot` vs `cot`）
- 修复：添加 6 条归一化规则（lines 67-72）:
  - LaTeX 函数名反斜杠剥离 (`\sin` → `sin`)
  - 逗号后空格压缩 (`1, 2` → `1,2`)
  - 括号内空格压缩 (`( x )` → `(x)`)
  - 运算符周围空格压缩 (`x + y` → `x+y`)
  - 单字符括号剥离 (`(a)` → `a`)

### 3. 验证结果
| 类别 | 结果 |
|------|------|
| Bug B (normalization) | **5/5 fixed** |
| Bug A (extraction + normalization) | **11/11 fixed** |
| v3+ regressions | **0/4** |
| **Projected accuracy** | **(117 + 16) / 500 = 26.60%** (vs v3 buggy 23.40%) |

### 4. 同步结果
- westd-32935: `eval_math500.py` 已修复 + `eval_math500_buggy.py` 已备份
- westb-23072: `eval_math500.py` 已通过 base64 同步写入，8568 bytes，内容已验证

### 5. 文件清单
| 服务器 | 文件 | 说明 |
|--------|------|------|
| westd-32935 | `src/eval_math500.py` | Fixed version |
| westd-32935 | `src/eval_math500_buggy.py` | Backup of buggy version |
| westd-32935 | `validate_fix.py` | Validation script |
| westb-23072 | `src/eval_math500.py` | Fixed version (synced) |

---
