# ssh harvest all evals westd westb

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_harvest_all_evals_westd_westb_20260521T074256_result.json`
- **Structured JSON:** [`3c35de946e795c1f797a.json`](../../sessions/3c/3c35de946e795c1f797a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集，汇总如下：

---

## westd-29022 Eval 状态

### 1. GRPO CKA-only 25% GSM8K (最关键)
- **状态**: 进行中
- **进度**: 1177/1319 (89%)
- **Interim accuracy**: **59.65%** (at 1150/1319), eos_rate=98.26%, avg_len=235
- **PID**: 322443, cuda:0
- **预计剩余**: ~7 min

### 2. SFT CKA-only 25% GSM8K
- **状态**: 进行中
- **进度**: 294/1319 (22%)
- **Interim accuracy**: **58.80%** (at 250/1319), eos_rate=98.40%, avg_len=234
- **PID**: 329698, cuda:1
- **预计剩余**: ~50 min

### 3. SFT Random 20% GSM8K
- **状态**: 进行中
- **进度**: 524/1319 (40%)
- **Interim accuracy**: **51.40%** (at 500/1319), eos_rate=99.00%, avg_len=192
- **PID**: 329770, cuda:2

---

## westb-23072 Eval 状态

### 5. GRPO Standard 25% GSM8K
- **状态**: 进行中
- **进度**: 207/1319 (16%)
- **Interim accuracy**: **52.50%** (at 200/1319), eos_rate=96.00%, avg_len=301
- **PID**: 75282, cuda:1
- 注：进度较慢，有多次长停顿（可能是 max_new_tokens=2048 的长生成）

### 6. MATH-500 SFT Standard 25%
- **状态**: 进行中
- **进度**: 293/500 (59%)
- **日志路径**: `/tmp/eval_math500_sft_standard_25.log`（不在预期路径）
- **无 interim accuracy**（MATH-500 eval 没有周期性精度日志）
- **PID**: 62714, cuda:0
- 注：每题耗时 ~1 min（max_new_tokens=2048），预计还需 ~3.5 hr

---

## GPU 占用汇总

| 服务器 | GPU | 显存占用 | 利用率 | 任务 |
|--------|-----|---------|--------|------|
| westd-29022 | cuda:0 | 28.9/97.9 GB | 94% | GRPO CKA-only 25% GSM8K eval |
| westd-29022 | cuda:1 | 28.9/97.9 GB | 99% | SFT CKA-only 25% GSM8K eval |
| westd-29022 | cuda:2 | 26.2/97.9 GB | 89% | SFT Random 20% GSM8K eval |
| westd-29022 | cuda:3 | 0/97.9 GB | 0% | **空闲** |
| westb-23072 | cuda:0 | 18.6/97.9 GB | 99% | MATH-500 SFT Standard 25% eval |
| westb-23072 | cuda:1 | 28.9/97.9 GB | 99% | GRPO Standard 25% GSM8K eval |

---
