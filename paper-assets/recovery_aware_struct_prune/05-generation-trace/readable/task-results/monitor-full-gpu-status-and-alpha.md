# monitor full gpu status and alpha

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_full_gpu_status_and_alpha_20260516T200622_result.json`
- **Structured JSON:** [`918e9f927f406c2050b2.json`](../../sessions/91/918e9f927f406c2050b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. GPU 状态

**westd-11672 (4× RTX PRO 6000, 98GB each)**

| GPU | Util | VRAM | 任务 |
|-----|------|------|------|
| 0 | 95% | 25.5/98 GB | `eval_grpo_rasp_rlvr_20_qwen_math` (n=200, PID 42301) |
| 1 | 97% | 42.5/98 GB | `eval_grpo_standard_25` (n=200, PID 42096) + `eval_grpo_standard_25_n1319` (tmux, PID 42590) |
| 2 | 94% | 60.9/98 GB | `eval_pass_k8_standard_20_grpo_qwen_math` (pass@8, PID 33921) + `eval_grpo_rasp_25` (n=1319, PID 34234) |
| 3 | 92% | 14.0/98 GB | Alpha ablation Phase B — 当前正在 SFT alpha=0.3 |

**westb-23072 (2× RTX PRO 6000, 98GB each)**

| GPU | Util | VRAM | 任务 |
|-----|------|------|------|
| 0 | 99% | 28.9/98 GB | `eval_grpo_rasp_25` (n=1319, tmux session) |
| 1 | 100% | 71.7/98 GB | `train_grpo_v5.py` — GRPO training on `sft_rasp_rlvr_20/checkpoint-1870` (已跑 ~2h) |

所有 6 张 GPU 均满载。

---

### 2. Alpha Ablation 进度

| α | SFT | Eval | Accuracy |
|---|-----|------|----------|
| 0.0 | ✅ | ✅ | **0.70** (140/200) |
| 0.3 | 🔄 进行中 (started 04:07) | ❌ | — |
| 0.5 | ❌ | ❌ | — |
| 0.7 | ❌ | ❌ | — |
| 1.0 | ❌ | ❌ | — |
| 2.0 | ❌ | ❌ | — |

已完成 1/6。Phase B 脚本仍在跑（GPU 3），正在顺序处理 alpha=0.3 的 SFT 阶段。

---

### 3. eval_grpo_rasp_rlvr_20_qwen_math

原始 PID 40541 已死。**已重新启动**为 PID 42301（04:00 启动，CUDA:0，运行约 7 分钟），结果文件尚未生成，eval 仍在进行中。

---
