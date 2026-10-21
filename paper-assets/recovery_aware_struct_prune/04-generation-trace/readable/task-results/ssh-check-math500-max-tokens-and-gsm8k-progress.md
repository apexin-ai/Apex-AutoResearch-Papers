# ssh check math500 max tokens and gsm8k progress

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_math500_max_tokens_and_gsm8k_progress_20260521T132439_result.json`
- **Structured JSON:** [`873dd55c9e6e1d41b3b1.json`](../../sessions/87/873dd55c9e6e1d41b3b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. MATH-500 max_new_tokens

**脚本默认值: 4096**（`eval_math500.py:110` — `parser.add_argument("--max_new_tokens", type=int, default=4096)`）

三个进程的 cmdline 均未传 `--max_new_tokens` 参数：
| PID | 任务 | max_new_tokens |
|---|---|---|
| 336961 | eval_math500_grpo_cka_only_25 | **4096**（默认值） |
| 338876 | eval_math500_sft_cka_only_25 | **4096**（默认值） |
| 359173 | eval_math500_grpo_random_20 | **4096**（默认值） |

**与 20% 不一致** — 20% 统一用 @2048，25% 这批用的是 4096。grpo_random_20 也是 4096。

---

### 2. eval_gsm8k_sft_standard_25 进度

- **PID 335301**: ALIVE，已运行 5h17m
- **进度**: 1106/1319 (~**84%**)，已跑 ~5h10m
- **最近指标**（@1100 samples）: acc=**0.5082**, eos_rate=**95.64%**, avg_len=320
- **预计剩余**: 213 samples，正常速度 ~2-3s/it，但有间歇性长停顿（100s+/it），估计还需 **1-2h**

---
