# eval restart all evals v2

**schema conform ie training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_restart_all_evals_v2_20260513T154355_result.json`
- **Structured JSON:** [`4e45704647d08efc118a.json`](../../sessions/4e/4e45704647d08efc118a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 进程均已正常启动并在推理中。

**汇报：**

| 项目 | 状态 |
|------|------|
| **GPU** | 2× RTX PRO 6000 96GB，启动前空闲，现已各加载一个模型 |
| **代码修复** | evaluate.py: `{%- set enable_thinking = false -%}` 前缀注入 ✓ / rewards.py: `_normalize_relation` + `_arg_similarity` ✓ |
| **旧 eval 结果** | `eval_D2_ckpt400/`, `eval_D2_final/`, `eval_D1_v4/` 均有完整 `eval_results.json`（修复前的旧结果） |
| **resume 支持** | evaluate.py 无 resume 逻辑，需全量重跑 |

**启动的 tmux sessions：**

| Session | GPU | 内容 | PID |
|---------|-----|------|-----|
| `eval_d2_v2` | cuda:0 | D2 ckpt400 → D2 final（串行） | 98615 |
| `eval_d1v4_v2` | cuda:1 | D1 v4 | 98692 |

**日志确认：** 两个进程均已完成模型加载（427 weights），正在 scierc_test 上推理（~5s/sample）。

**预估完成时间：**
- 每个数据集：scierc 551 samples × ~5s ≈ 46min, crossner_politics 651 × ~5s ≈ 54min, crossner_science 543 × ~5s ≈ 45min
- **D1 v4 (cuda:1)**: 3 个数据集串行 ≈ **2.5 小时**
- **D2 ckpt400 + D2 final (cuda:0)**: 6 个数据集串行 ≈ **5 小时**
- 输出目录：`eval_D2_ckpt400_v2/`, `eval_D2_final_v2/`, `eval_D1_v4_v2/`

---
