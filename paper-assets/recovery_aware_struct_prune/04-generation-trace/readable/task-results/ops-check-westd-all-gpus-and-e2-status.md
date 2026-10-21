# ops check westd all gpus and e2 status

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_westd_all_gpus_and_e2_status_20260519T014846_result.json`
- **Structured JSON:** [`508dbf9220c499fbe691.json`](../../sessions/50/508dbf9220c499fbe691.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-29022 状态汇总

### GPU 总览（4 卡全部活跃）

| GPU | 利用率 | 显存 | 任务 | PID | 状态 |
|-----|--------|------|------|-----|------|
| cuda:0 | 97% | 16.5/97.9 GB | eval_math500_sft_standard_20_2048_v2 | 56146 | 运行中 (14/500, ~3%) |
| cuda:1 | 94% | 12.8/97.9 GB | eval_gsm8k_grpo_cka_only_20_extended_300 | 56977 | 运行中 (~12min CPU time) |
| cuda:2 | 91% | 17.0/97.9 GB | math500_grpo_cka_only_20_2048 | 36703 | 运行中 (已跑 150min) |
| cuda:3 | 92% | 12.7/97.9 GB | inference_bench_clean_v2 | 56892 | 运行中 (第2/3个模型) |

### 任务 1: cuda:1 E2 extended eval (PID 56977)
- **仍在运行**，09:42 UTC 启动，无结果文件
- 正在跑 GSM8K 1319 samples，预计还需较长时间

### 任务 3: Inference bench (PID 56892)
- 已完成第 1 个模型 (original)：**72.0 tok/s, TTFT 20.1ms**
- 正在 benchmark 第 2 个模型 (pruned_cka_only_20)
- 还剩第 3 个模型 (pruned_standard_20)，无 JSON 结果文件

### 任务 4: 已完成的 MATH-500 结果

| 模型 | Accuracy |
|------|----------|
| Dense unpruned (default tokens) | **73.6%** |
| Dense (2048 tokens) | **53.0%** |
| SFT CKA-only 20% (v4) | **29.0%** |
| GRPO standard 20% (fair v2) | **26.4%** |
| GRPO RASP 20% (fair) | **24.0%** |
| SFT RASP 20% (2048) | **22.6%** |

### 备注
- cuda:0 的 sft_standard_20_2048_v2 刚开始（14/500），按当前速度预计 ~8-10h
- cuda:2 的 grpo_cka_only_20_2048 已跑 2.5h，进度未知（log 被重定向）
- 4 张卡全部满负荷运行，无空闲 GPU

---
