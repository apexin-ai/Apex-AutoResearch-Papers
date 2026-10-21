# status westd check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_westd-check_20260517T101225_result.json`
- **Structured JSON:** [`5c80e0ca6aa5900fbd85.json`](../../sessions/5c/5c80e0ca6aa5900fbd85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-11672 实验状态汇总

### GPU 使用情况 (全部 4 张在用)

| GPU | 显存占用 | 利用率 | 温度 | 进程 |
|-----|---------|--------|------|------|
| 0 | 17.7/97.9 GB | 91% | 55°C | PID 3331 - eval_math500_unpruned |
| 1 | 30.1/97.9 GB | 98% | 81°C | PID 14556 - eval_math500_grpo_standard_20 |
| 2 | 13.0/97.9 GB | 92% | 70°C | PID 16488 - eval_humaneval_grpo_standard_20 |
| 3 | 30.1/97.9 GB | 98% | 79°C | PID 11896 - eval_math500_grpo_rasp_20_v2 |

### tmux sessions (3个)
- `eval_math500_unpruned` (14:20 启动)
- `eval_math500_grpo_rasp_20_v2` (16:34 启动)
- `eval_humaneval_grpo_standard_20` (18:00 启动)

---

### 各实验状态

#### 1. eval_sft_rasp_rlvr_20_qwen_math — **已完成**
- **GSM8K Accuracy: 73.0% ± 3.14% (146/200)**
- EOS rate: 100%, avg response length: 127 tokens
- 完成时间: 2026-05-17 02:08

#### 2. eval_postprune_25 — **已完成**
- **RASP 25% pruned (GSM8K): 16.0% ± 3.67% (16/100)**
  - EOS rate: 23%, avg length: 3241 (严重截断)
- **Standard 25% pruned (GSM8K): 16.0% ± 3.67% (16/100)**
  - EOS rate: 23%, avg length: 3241 (严重截断)
- 完成时间: 2026-05-16 16:07

#### 3. eval_math500_unpruned — **运行中** (GPU 0)
- 模型: DeepSeek-R1-Distill-Qwen-7B (unpruned baseline)
- 进度: **400/500** (80%), 当前 Acc: **73.75%**
- 已运行 ~3h51m, 预计还需 ~36 分钟
- 结果文件尚未生成

#### 4. eval_math500_grpo_standard_20 (PID 14556) — **运行中** (GPU 1)
- 模型: grpo_stage2_standard_20_v8/checkpoint-50
- 进度: **18/500** (~4%), 当前速度极慢 (~5-6min/sample)
- 已运行 ~44 min, 预计还需很长时间 (可能 20h+)
- 结果文件尚未生成

#### 5. eval_math500_grpo_rasp_20_v2 — **运行中** (GPU 3)
- 模型: grpo_stage2_rasp_20_v9
- 进度: **64/500** (~13%), Acc@50: **34.0%**
- 已运行 ~1h36m, 速度也很慢 (部分 sample 耗时 3-5min)
- 结果文件尚未生成

#### 6. eval_humaneval_grpo_standard_20 — **运行中** (GPU 2, 刚启动)
- 模型: grpo_stage2_standard_20_v8/checkpoint-50
- 进度: **55/164** (~34%), Pass@1@40: 2.5%
- 已运行 ~12 min, 预计还需 ~20 min
- 结果文件尚未生成

---

### 磁盘
`/root/autodl-tmp`: 718G/750G used (**96%**, 仅剩 33G)

### 空闲 GPU
**无** — 4 张全部占满。eval_math500_unpruned (GPU 0) 和 eval_humaneval_grpo_standard_20 (GPU 2) 预计较快完成 (30-40 min 内)，之后可释放。

### 注意事项
- eval_math500_grpo_standard_20 和 eval_math500_grpo_rasp_20_v2 速度极慢（GRPO 模型生成 token 多），可能需要 10-20h 才能完成
- 磁盘 96% 使用率，需注意新结果文件不会因空间不足失败

---
