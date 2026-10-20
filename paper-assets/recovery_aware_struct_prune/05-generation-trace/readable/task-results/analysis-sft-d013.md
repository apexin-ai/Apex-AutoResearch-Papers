# analysis sft d013

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sft_d013_20260515T003006_result.json`
- **Structured JSON:** [`2e8de4bebe8c9aa7d1a3.json`](../../sessions/2e/2e8de4bebe8c9aa7d1a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both evals complete. Here are the full results:

---

## D013 SFT Warmup 实验结果

### 对比表格

| 模型 | Post-Prune Acc | Post-SFT Acc | Δ Acc | Train Loss | EOS Rate (Greedy) | EOS Rate (Sampling) | Avg Resp Len |
|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| RASP 20% | 29% | **57%** | +28pp | 0.7736 | 99% | **100%** | 180 |
| Standard 20% | 1% | **64%** | +63pp | 0.7593 | 99% | **100%** | 176 |

### 训练详情
- 两个实验都正常完成（EXIT_CODE=0），无 crash/error
- 训练时间：~37 分钟（1870 steps, 2 epochs, 7473 samples）
- 无 W&B（服务器网络不可达）

### Checkpoint 路径和大小
- RASP: `/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20/` — model.safetensors 11.5 GB
- Standard: `/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20/` — model.safetensors 11.5 GB
- 两者各有 checkpoint-935 和 checkpoint-1870

### Sampling 生成样本（temperature=0.7, 5/5 全部产出 EOS）

**RASP 20% SFT:**
| # | 长度 | EOS | 内容摘要 |
|---|---:|:---:|---|
| 1 | 119 | ✓ | `First, I will find Jared's typing speed after one lesson by adding his increase of 5 words per minute...` |
| 2 | 151 | ✓ | `First, I will calculate the total number of diapers...2 * 5 = <<2*5=10>>10...` |
| 3 | 82 | ✓ | `The maximum weight the truck can take is 5000 - 3755 = <<5000-3755=1245>>1245 pounds...#### 86` |
| 4 | 217 | ✓ | `First find the total number of blue shoe boxes...` |
| 5 | 91 | ✓ | `Half as many robots as helmets means 20/2 = <<20/2=10>>10 robots...#### 60` |

**Standard 20% SFT:**
| # | 长度 | EOS | 内容摘要 |
|---|---:|:---:|---|
| 1 | 147 | ✓ | `The first measurement is 47 WPM. The second measurement is 52 WPM...` |
| 2 | 65 | ✓ | `The 2 children require 2 x 5 = <<2*5=10>>10 diaper changes per day...#### 5` |
| 3 | 128 | ✓ | `The total weight that can pass over the bridge is 5000 pounds...5000 - 3755 = <<5000-3755=...` |
| 4 | 207 | ✓ | `First, we need to determine the number of blue shoe boxes Tim used...7 - 3 = <<7-3=4>>4...` |
| 5 | 176 | ✓ | `There are twice as many footballs as robots...20 x 2 = <<20*2=40>>40 footballs` |

### 关键发现

1. **SFT 成功修复了 EOS 生成** — 两个模型 sampling 模式 EOS rate 均为 100%，greedy 99%（仅 1/100 样本命中 4096 上限）
2. **Standard 模型恢复幅度更大** — 1% → 64%（+63pp），超过 RASP 的 29% → 57%（+28pp）。说明 standard pruning 虽然严重破坏输出格式，但保留了更多可恢复的模型容量
3. **两个模型都具备进入 GRPO Stage 2 的条件** — 能正常生成 EOS，输出格式合理（reasoning + #### answer），响应长度可控（~176-180 tokens 均值）

---
