# ops full gpu state audit

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full_gpu_state_audit_20260519T090108_result.json`
- **Structured JSON:** [`e9e249e1ae08c2b30dc4.json`](../../sessions/e9/e9e249e1ae08c2b30dc4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已收集完毕。以下是完整报告：

---

## westd-29022 — 4 × RTX PRO 6000 Blackwell

| GPU | 实验 | Session | 状态 | 进度 | 当前指标 |
|-----|------|---------|------|------|----------|
| cuda:0 | GSM8K Standard fair v2 | `eval_gsm8k_std_fair_v2` | **ALIVE, 运行中** | 4/1319 (~0.3%) | 刚启动 (16:58)，~4s/it |
| cuda:1 | HumanEval SFT CKA-only v2 | `eval_humaneval_sft_cka_only_20_2048_v2` | **ALIVE, 运行中** | 79/164 (48%) | Pass@1 中间值波动中，最近 checkpoint: 60→0.3167, 80未到 |
| cuda:2 | HumanEval GRPO Standard fair v3 | `eval_humaneval_grpo_standard_20_fair_2048_v3` | **ALIVE, 运行中** | 84/164 (51%) | Pass@1=0.1125 (@ 80) |
| cuda:3 | HumanEval GRPO RASP fair | `eval_humaneval_rasp_fair` (PID 74303) | **ALIVE, 运行中** | 134/164 (82%) | Pass@1=0.1250 (@ 120) |

### 详细进度快照

**cuda:0 — GSM8K Standard fair v2**
- 刚启动 3 分钟 (16:58)，4/1319 samples，ETA ~1.5h
- 网络不通但成功使用 HF cache

**cuda:1 — HumanEval SFT CKA-only v2** (最高优先级)
- 48% 完成 (79/164)，已运行 ~1h20m
- 中间 Pass@1 snapshot: 20→0.3000, 40→0.2750, 60→0.3167
- 速度 ~24-70s/it，ETA ~1-2h
- **尚未完成，无最终结果文件**

**cuda:2 — HumanEval GRPO Standard fair v3**
- 51% 完成 (84/164)，已运行 ~1h56m
- 中间 Pass@1 snapshot: 20→0.0500, 40→0.0750, 60→0.1333, 80→0.1125
- 速度 ~75-105s/it，ETA ~2h+

**cuda:3 — HumanEval GRPO RASP fair**
- 82% 完成 (134/164)，已运行 ~2h20m
- 中间 Pass@1 snapshot: 20→0.1500, 40→0.1500, 60→0.1333, 80→0.1375, 100→0.1300, 120→0.1250
- **最接近完成**，ETA ~45min

---

## westb-23072 — 2 × RTX PRO 6000 Blackwell

| GPU | 实验 | 状态 | 进度 |
|-----|------|------|------|
| cuda:0 | **空闲** | 0% util, 0 MiB | 无进程 |
| cuda:1 | GRPO CKA-only seed123 训练 | **ALIVE** | **45/100 steps (45%)** |

**cuda:1 — GRPO CKA-only seed123 训练**
- PID 857962, 已运行 ~5h16m
- 45/100 steps, ~417s/step
- ETA: ~55 steps × 418s ≈ **6.4h 剩余**
- WandB 已连接记录中
- tmux session `grpo_cka_only_20_seed123` 活跃

---

## 任务 3：结果收割

**所有实验均未完成，暂无最终结果文件可收割。** 预计完成顺序：

1. **cuda:3 RASP HumanEval** — ~45min 后完成（134/164）
2. **cuda:1 SFT CKA-only HumanEval v2** — ~1-2h 后完成（79/164）
3. **cuda:2 Standard HumanEval v3** — ~2h+ 后完成（84/164）
4. **cuda:0 GSM8K Standard fair v2** — ~1.5h 后完成（刚启动）
5. **westb seed123 训练** — ~6.4h 后完成（45/100 steps）

**关键观察：** SFT CKA-only 的中间 Pass@1 (~0.28-0.32) 明显优于 GRPO Standard (~0.11) 和 GRPO RASP (~0.13)。

---
