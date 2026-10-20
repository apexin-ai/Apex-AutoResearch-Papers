# ops westd full progress check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_full_progress_check_20260519T030823_result.json`
- **Structured JSON:** [`ba576a3aac23ad0110c5.json`](../../sessions/ba/ba576a3aac23ad0110c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-29022 实验状态汇总

| GPU | 实验 | 状态 | 进度 | 关键指标 |
|-----|------|------|------|----------|
| **cuda:0** | eval_math500_sft_standard_20_2048_v2 | 运行中 | **104/500 (20.8%)** | Acc=0.3500 |
| **cuda:1** | eval_gsm8k_grpo_cka_only_20_extended_300 | 运行中 | **900/1319 (68.2%)** | Acc=64.22%, eos_rate=99.22%, avg_len=191 |
| **cuda:2** | eval_math500_grpo_cka_only_20_2048 | **已完成** | 500/500 | **Acc=29.2%**, natural_eos=78%, avg_len=654.7 |
| **cuda:3** | eval_gsm8k_grpo_standard_20_extended_300 | 运行中 | **264/1319 (20.0%)** | Acc=62.4%, eos_rate=98%, avg_len=231 |

### cuda:2 完成结果详情 (math500_grpo_cka_only_20_2048)
- **Accuracy: 29.2%** (146/500), stderr=0.0203
- **EOS stats**: natural_eos=390 (78%), truncated=110 (22%)
- 平均响应长度 654.7 tokens, 中位数 250.5
- 22% 的样本被截断到 2048 tokens，说明模型在 MATH-500 上生成偏长

### cuda:2 现在空闲，可用于新实验。

---
