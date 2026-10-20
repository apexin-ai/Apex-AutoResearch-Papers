# code prolog sta prep

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prolog-sta-prep_20260514T015723_result.json`
- **Structured JSON:** [`bfaf8715372390a6d822.json`](../../sessions/bf/bfaf8715372390a6d822.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Prolog STA 代码框架已完整实现且测试通过。** 无需新建 `prolog_sta.py`——代码已存在：

| 文件 | 用途 |
|------|------|
| `src/solvers/prolog.py` | PrologSolver — 调 `swipl` 执行证明 |
| `src/sta/prolog_reward.py` | `prolog_sta_reward` / `fast_prolog_sta_reward` / `parse_prolog_formalization` — 完整 STA ablation + ISR |
| `scripts/sta_prolog.py` | CLI 测试入口 |
| `scripts/train_grpo.py` | 已集成 `--logic_type prolog` 支持 |

Dry-run 结果（full O(n) 模式 + fast O(1) 模式均 5/5 通过）：
- **grandparent (all necessary)**: ISR=1.000，3 条 clause 均必要
- **grandparent + redundant fact**: ISR=0.750，`parent(alice, charlie)` 被正确识别为冗余
- **missing fact**: 证明失败，ISR=0.000
- **simple fact query**: ISR=0.500，`likes(mary, wine)` 冗余
- **chain reasoning**: ISR=1.000，3 条规则链全必要

---
