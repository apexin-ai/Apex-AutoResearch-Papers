# code fix prolog prompt mismatch

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-prolog-prompt-mismatch_20260514T062901_result.json`
- **Structured JSON:** [`5d1a3ce3f0282eafaeee.json`](../../sessions/5d/5d1a3ce3f0282eafaeee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部通过。

**修复结果：**

| 项目 | 修改前 (eval_sta.py) | 修改后 (= train_grpo.py) |
|------|---------------------|------------------------|
| PROLOG_SYSTEM_PROMPT 角色 | "Prolog expert" | "Prolog logic programming expert" |
| PROLOG_SYSTEM_PROMPT 任务描述 | "formalize them as a Prolog program with a query" | "formalize them into Prolog" |
| 输出格式示例 | `fact1.` / `rule1 :- body1.` / `?- query.` | `&lt;fact_or_rule>.` / `Query: &lt;goal>` |
| 语法说明 | "atoms start lowercase, variables start uppercase. End each clause with a period." | "facts (predicate(args).), rules (head :- body.), variables start with uppercase, atoms/predicates start with lowercase." |
| PROLOG_USER_TEMPLATE | "Formalize the following as a Prolog program with a query" | "Formalize the following in Prolog" |

**验证：**
- `sta_prolog.py --test`: 5/5 PASS
- `eval_sta.py --help`: `--logic_type {fol,prolog}` 参数正常

---
