# fix overflow and resume

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_overflow-and-resume_20260514T075121_result.json`
- **Structured JSON:** [`6a463fe3c1a87d90298c.json`](../../sessions/6a/6a463fe3c1a87d90298c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

**修复：**
- `src/eval_gsm8k.py:62` — `except ValueError:` → `except (ValueError, OverflowError):`
- `src/train_grpo.py:72` — `except ValueError:` → `except (ValueError, OverflowError):`

**验证通过：** `normalize_answer("1e999")` 不再 crash（float("1e999")=inf → int(inf) 触发 OverflowError，现已捕获）。

**产物检查：**
- `models/pruned_standard_35/config.json` ✓
- `models/pruned_rasp_35/config.json` ✓
- `results/cka_scores.pt` ✓ (122KB)
- `results/importance_scores.pt` ✓ (17KB)
- `src/run_mvp_resume.sh` ✓ (可执行)
- `src/run_mvp_resume_from_3_5.sh` ✓ (可执行)

**Pipeline 状态：** 无 tmux session，无残留进程。

**READY** — 两个 resume 脚本均可用，等 Main Agent 通过 submit_training_job 启动。

---
