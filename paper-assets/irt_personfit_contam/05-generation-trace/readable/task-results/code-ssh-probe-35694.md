# code ssh probe 35694

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ssh-probe-35694_20260521T130840_result.json`
- **Structured JSON:** [`79eb32b52688dbbd0a0f.json`](../../sessions/79/79eb32b52688dbbd0a0f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-35694 全面状态报告

### 1. GPU 状态

| GPU | 显存占用 | 利用率 | PID | 进程 |
|-----|---------|--------|-----|------|
| 0 | 20,871 / 97,887 MiB (21%) | 97% | 143378 | Llama train.py (clean_s8/s9/s10 之一) |
| 1 | 28,807 / 97,887 MiB (29%) | 96% | 143458 | Llama train.py |
| 2 | 10,913 / 97,887 MiB (11%) | 83% | 141866 | GRPO v3 (train_grpo.py --gpu 2) |
| 3 | 25,977 / 97,887 MiB (27%) | 82% | 143599 | Llama train.py |

4 卡全部在用，无空闲 GPU。

### 2. GRPO v3

- **状态**: RUNNING, step **428/3000** (14.3%)
- **速度**: ~3.0-3.5 s/step
- **预计剩余**: ~2 小时
- **tmux session**: `exp-post-rl-v3`
- **SFT checkpoint**: 存在于 `checkpoints/sft/`
- **GRPO checkpoint**: `checkpoints/grpo/` **为空**，尚无中间 checkpoint
- **最近 reward**: 在 -0.025 ~ 0.775 间波动，entropy ~1.6-1.7

### 3. Llama 训练 (`ctrl_contam_llama`)

| 条件 | 训练状态 | 完整 Checkpoint | Eval 结果 |
|------|---------|----------------|----------|
| clean (s1) | DONE | adapter_config + safetensors | clean_results.json |
| clean_s2 | DONE | adapter_config + safetensors | clean_s2_results.json |
| clean_s3 | DONE | adapter_config + safetensors | clean_s3_results.json |
| clean_s4 | DONE | adapter_config + safetensors | clean_s4_results.json |
| clean_s5 | DONE | adapter_config + safetensors | clean_s5_results.json |
| clean_s6 | DONE | adapter_config + safetensors | clean_s6_results.json |
| clean_s7 | DONE | adapter_config + safetensors | clean_s7_results.json |
| **clean_s8** | **RUNNING ~30%** (289/939) | checkpoint-313 only | 无 |
| **clean_s9** | **RUNNING ~31%** (290/939) | checkpoint-313 only | 无 |
| **clean_s10** | **RUNNING ~31%** (290/939) | checkpoint-313 only | 无 |
| contam_15 | DONE | adapter_config + safetensors | contam_15_results.json |
| contam_50 | DONE | adapter_config + safetensors | contam_50_results.json |

s8/s9/s10 速度 ~1.1 s/step，剩余 ~650 steps，预计 **~12 分钟**完成。

### 4. Mistral 训练 (`ctrl_contam_mistral`)

| 条件 | 训练状态 | 完整 Checkpoint | Eval 结果 |
|------|---------|----------------|----------|
| clean (s1) | DONE | adapter_config + safetensors | clean_results.json |
| clean_s2 | DONE | adapter_config + safetensors | clean_s2_results.json |
| clean_s3 | DONE | adapter_config + safetensors | clean_s3_results.json |
| contam_15 | DONE | adapter_config + safetensors | contam_15_results.json |
| contam_50 | DONE | adapter_config + safetensors | contam_50_results.json |

Mistral 全部完成且已 eval。

### 5. Pilot / Qwen (`ctrl_contam_pilot`)

全部完成：clean_s1~s10、contam_15、contam_50，均已 eval（含 cohens_d_n10.json 汇总）。

### 6. 活跃/Zombie 进程

**活跃进程**（4 个训练）:
- PID 141866: GRPO v3 (GPU 2)
- PID 143378: Llama training (GPU 0)
- PID 143458: Llama training (GPU 1)
- PID 143599: Llama training (GPU 3)
- PID 144524/144525: train.py --condition clean_s8
- PID 144729/144730: train.py --condition clean_s9
- PID 144828/144830: train.py --condition clean_s10

**旧 PID 全部 DEAD**: 97791, 99214, 99807, 96745, 98622 — 无 zombie。

### 7. 已完成未 eval 模型清单

**当前所有已完成训练的模型均已 eval**，无遗漏。

待 eval（训练完成后需要跑 eval）：
- Llama **clean_s8**, **clean_s9**, **clean_s10** — 约 12 分钟后训练完成
- GRPO v3 — 约 2 小时后训练完成

---
