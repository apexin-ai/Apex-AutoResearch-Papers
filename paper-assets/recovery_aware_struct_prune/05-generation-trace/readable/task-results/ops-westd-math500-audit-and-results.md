# ops westd math500 audit and results

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_math500_audit_and_results_20260519T020750_result.json`
- **Structured JSON:** [`ab801437c51e8c9541bf.json`](../../sessions/ab/ab801437c51e8c9541bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是完整报告。

---

## 任务 A: MATH-500 @2048 Config 一致性审计

**脚本版本**: `src/eval_math500.py` 最后修改 May 17 14:20:40，早于所有 @2048 eval 启动时间，版本一致。

**验证方法**: JSON 中无 `max_new_tokens` 字段。通过 (1) examples 的 `response_length` 上限确认截断阈值 (2) ps 命令行确认运行中 eval 的参数 (3) tmux 历史确认 grpo_standard_fair_v2。

| eval_id | max_new_tokens | model_path | script | 一致 |
|---------|---------------|------------|--------|------|
| dense_2048 | 2048 (max_resp_len=2048, truncated=266) | `/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B` | eval_math500.py | ✅ |
| sft_cka_only_20_2048 | 2048 (max_resp_len=2048, truncated=116) | `.../sft_cka_only_20` | eval_math500.py | ✅ |
| grpo_standard_20_fair_v2 | 2048 (max_resp_len=2048 + tmux cmd确认) | `.../grpo_stage2_standard_20_fair` | eval_math500.py | ✅ |
| sft_rasp_20_2048 | 2048 (max_resp_len=2048, truncated=186) | `.../sft_rasp_20_westd` | eval_math500.py | ✅ |
| grpo_rasp_20_fair | 2048 (max_resp_len=2048, truncated=180) | `.../grpo_stage2_rasp_20_fair` | eval_math500.py | ✅ |
| grpo_cka_only_20_2048 🔄 | 2048 (ps 命令行确认 `--max_new_tokens 2048`) | `.../grpo_cka_only_20` | eval_math500.py | ✅ |
| sft_standard_20_2048_v2 🔄 | 2048 (ps 命令行确认 `--max_new_tokens 2048`) | `.../sft_standard_20` | eval_math500.py | ✅ |

**全部 7 个 eval 一致 ✅**

**⚠️ 发现**: `math500_sft_standard_20_2048.log`（v1）加载了错误模型 `sft_qwen_math_standard_20`，无输出 JSON。当前运行的 v2 已修正为 `sft_standard_20`。

**补充**: `grpo_rasp_20_fair` 在 westd-29022 上运行（log 起始 05/19 02:15），不在旧 westd-11672 上。

---

## 任务 B: GPU 状态

| GPU | Util | Memory | 进程 |
|-----|------|--------|------|
| cuda:0 | 96% | 16.8/97.9 GiB | eval_math500_sft_standard_20_2048_v2 (PID 56151) |
| cuda:1 | 99% | 28.7/97.9 GiB | eval_gsm8k_grpo_cka_only_20_extended_300 (PID 56977) |
| cuda:2 | 98% | 17.0/97.9 GiB | eval_math500_grpo_cka_only_20_2048 (PID 36703) |
| cuda:3 | **0%** | **0/97.9 GiB** | **空闲** |

- **PID 56977 (cuda:1)**: 存活，eval_gsm8k_grpo_cka_only_20_extended_300，进度 **311/1319 (23.6%)**, acc=**67.7%**, eos_rate=99.3%
- **cuda:3**: 确认空闲，无遗留进程

---

## 任务 C: 已完成实验结果

| Eval | Accuracy | n_correct/n_total | eos_stats |
|------|----------|-------------------|-----------|
| math500_dense_2048 | **53.0%** | 265/500 | natural_eos=234, truncated=266, avg_len=1724.5 |
| math500_grpo_standard_20_fair_v2 | **26.4%** | 132/500 | natural_eos=278, truncated=222, avg_len=1127.8 |
| math500_sft_rasp_20_2048 | **22.6%** | 113/500 | natural_eos=314, truncated=186, avg_len=930.6 |
| eval_gsm8k_grpo_cka_only_20_extended_300 | 🔄 **~67.7%** at 311/1319 | 运行中 | eos_rate=99.3%, avg_len=184 |

运行中 eval 进度:
- grpo_cka_only_20 MATH-500: **310+/500**, Acc ~29.7%
- sft_standard_20 MATH-500: 刚启动约 30 分钟

---

## 任务 D: cuda:3 空闲分析

MATH-500 @2048 全部 7 cell 已覆盖:
- ✅ 完成 5 个: Dense (53.0%), SFT CKA-only (29.0%), GRPO Standard (26.4%), SFT RASP (22.6%), GRPO RASP (24.0%)
- 🔄 运行中 2 个: GRPO CKA-only (cuda:2), SFT Standard (cuda:0)

**cuda:3 当前无 MATH-500 任务需求**。可用于其他 pending eval（如 HumanEval @2048 缺失 cell、GSM8K 系列、或其他 benchmark）。

---
