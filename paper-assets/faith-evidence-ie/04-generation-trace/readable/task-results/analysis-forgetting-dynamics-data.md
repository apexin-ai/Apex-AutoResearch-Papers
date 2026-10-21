# analysis forgetting dynamics data

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_forgetting-dynamics-data_20260515T162933_result.json`
- **Structured JSON:** [`31e3fd6b99fde493a1d9.json`](../../sessions/31/31e3fd6b99fde493a1d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 已保存到 `/root/autodl-tmp/artifacts/forgetting_dynamics_data.json`。

## 结果汇总

### 已有 eval 数据

| Experiment | Step | rel_f1 | evi_f1 | edcr |
|---|---|---|---|---|
| **QLoRA GRPO (kl001)** | 10 | 0.0030 | 0.7200 | 0.998 |
| | 20 | 0.0088 | 0.4230 | 0.995 |
| | 30 | 0.0338 | 0.5889 | 0.980 |
| | 50 | 0.1563 | 0.5643 | 0.886 |
| | 60 | 0.1467 | 0.5763 | 0.906 |
| | 90 | 0.2108 | 0.5666 | 0.858 |
| | 100 | **0.2167** | 0.5746 | 0.854 |
| **bf16 GRPO G=8** | 80 | 0.4456 | 0.8034 | 0.641 |
| | 100 | **0.4549** | 0.8086 | 0.632 |
| **SFT baseline** | — | **0.4057** | 0.7979 | — |

额外发现：还有一个 `qlora_grpo_lr5e6` 实验，forgetting 更严重（rel_f1 始终 < 0.014），也一并收录。

### 缺失的 eval（需安排后续 eval）

**高优先级（forgetting dynamics figure 必需）**：
- `bf16_grpo_g8` steps **10, 20, 30, 40, 50, 60, 70** — 目前只有 80/100 两个点，画不出完整曲线
- `bf16_grpo_g8` step **90** — 正在跑（63%）

**中优先级**：
- `qlora_grpo` steps **40, 70, 80** — 补全曲线上的 gap

### 无 W&B reward 数据
服务器上未发现 wandb 目录，training log 的 reward 是 per-batch 值（噪声大）。如需平滑 reward 曲线，需要从 W&B project 拉取或重新从 log 按 step 提取。

---
