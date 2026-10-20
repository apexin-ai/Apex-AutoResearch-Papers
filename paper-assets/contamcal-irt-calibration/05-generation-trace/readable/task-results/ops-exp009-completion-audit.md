# ops exp009 completion audit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp009_completion_audit_20260517T080525_result.json`
- **Structured JSON:** [`8999f9fd630b166f72fb.json`](../../sessions/89/8999f9fd630b166f72fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-009 审计结果

### GPU 状态
| GPU | 状态 | 进程 |
|-----|------|------|
| 0-3 | 空闲 | - |
| 4 | 占用 1.6G | PID 946440: 0.5B-Instruct MMLU s4 signal |
| 5 | 占用 3.7G | PID 947036: 1.5B-Instruct MMLU s4 signal |

另有 PID 951036 在 CPU 上跑 `run_mmlu_domain_gamma_no05b.py`（exp006 IRT fitting）。

### tmux sessions
`exp009_3b_instruct`, `exp009_deepseek`, `sig_05b`, `sig_15b`, `irt_no05b`

---

### 完成的

| 模型 | Eval (MMLU/ARC/GSM8K) | Signals ARC (s2+s4) | Signals GSM8K (s2+s4) | Signals MMLU (s2+s4) |
|------|----------------------|---------------------|----------------------|---------------------|
| **Qwen2.5-3B-Instruct** | 全部完成 | 全部完成 + merged | 全部完成 + merged | 全部完成 + merged |
| **DeepSeek-R1-Distill-Qwen-1.5B** | 全部完成 | 全部完成 + merged | 全部完成 + merged | 全部完成 + merged |
| **Qwen2.5-0.5B-Instruct** | 全部完成 | s2 完成, s4 完成 | s2 完成, s4 完成 | s2 完成 |
| **Qwen2.5-1.5B-Instruct** | 全部完成 | s2 完成, s4 完成 | s2 完成 | s2 完成 |

### 正在跑

- **0.5B-Instruct MMLU s4** (GPU 4): 有 13 chunks 已完成，正在继续生成剩余 chunks
- **1.5B-Instruct MMLU s4** (GPU 5): 有 12 chunks 已完成，正在继续生成剩余 chunks

### 未完成

- **1.5B-Instruct GSM8K s4**: 缺失（只有 s2）
- **0.5B / 1.5B MMLU signals_merged**: 等 s4 完成后才能 merge
- **0.5B / 1.5B ARC / GSM8K signals_merged**: 缺失（单独 s2/s4 文件存在但未 merge）
- DeepSeek GSM8K 相关文件：无额外文件（eval 已在 exp009 完成）

---
