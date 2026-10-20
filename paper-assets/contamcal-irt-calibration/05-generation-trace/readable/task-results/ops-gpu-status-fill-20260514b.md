# ops gpu status fill 20260514b

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-fill-20260514b_20260514T073952_result.json`
- **Structured JSON:** [`06a72b56ee01f9af7522.json`](../../sessions/06/06a72b56ee01f9af7522.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## GPU 状态报告 (cqa1-21977)

```
GPU 状态:
cuda:0 - 运行中  PID 325310  eval Qwen2.5-1.5B_d100_s42 (lora adapter)  85%  5857/24564 MiB  运行 1h22m
cuda:1 - 运行中  PID 318424  eval Qwen2.5-0.5B raw (mmlu,gsm8k,arc,humaneval)  36%  3593/24564 MiB  运行 48m
cuda:2 - 运行中  PID 324158  train_sft Qwen2.5-0.5B_d025_s42  98%  21423/24564 MiB  运行 9m
cuda:3 - 运行中  PID 319555  train_sft Qwen2.5-3B_d100_s42 (step 575/4159, 14%)  24%  13329/24564 MiB  运行 45m
cuda:4 - 运行中  PID 271921  train_sft Qwen2.5-1.5B_d005_s42  21%  18549/24564 MiB  运行 4h28m
cuda:5 - 运行中  PID 318748  eval Qwen2.5-3B raw (gsm8k,humaneval)  59%  6623/24564 MiB  运行 47m
```

**6 张卡全满，无空闲 GPU。**

PID 251924 (exp_001_sft_d100_15B_v2): **已死亡**，GPU 0 已被 1.5B d100 eval 占用。

---

### Raw eval 状态
- **0.5B raw** (cuda:1): 仍在运行，当前在评 MMLU（~20it/s on 14042 items），尚未写出 eval_results.json
- **3B raw** (cuda:5): 仍在运行，评 gsm8k+humaneval，尚未写出结果

---

### 3B d100 SFT
**Registry 显示 failed 但进程实际存活。** PID 319555 在 cuda:3 正常训练中，step 575/4159 (14%)，loss ~1.1-1.3，token accuracy ~0.72。Registry 状态有误。

---

### 已完成 eval 结果

| Benchmark | 0.5B d000 (clean) | 0.5B d100 (contaminated) | Delta |
|-----------|-------------------|--------------------------|-------|
| MMLU | 40.5% | 23.2% | -17.3% |
| GSM8K | 36.5% | 35.7% | -0.8% |
| ARC-Challenge | 37.8% | 22.7% | -15.1% |
| HumanEval pass@1 | 11.0% | 8.5% | -2.5% |

d100 在所有 benchmark 上均**低于** d000，MMLU 和 ARC 下降尤其严重。100% 污染数据训练后模型通用能力大幅下降而非膨胀分数。

---
