# launch alpha3p0 grpo eval westd0 v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_launch_alpha3p0_grpo_eval_westd0_v2_20260522T115405_result.json`
- **Structured JSON:** [`b2eee8554fe8406ea4ea.json`](../../sessions/b2/b2eee8554fe8406ea4ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 正常运行中。

**汇总：**

- **GRPO α=3.0 训练 (PID 42003)**: 已完成，checkpoint-100/model.safetensors 12.3GB 正常
- **Eval PID**: 43755（实际 python 进程），父 shell PID 43749
- **GPU 0**: 12682MiB / 97887MiB，89% utilization
- **进度**: 8/1319 samples，~2.8s/it，预计 ~60 分钟完成
- **模型**: cuda:0，Non-uniform MLP (intermediate_size [8128, 18944])，GSM8K 离线缓存加载成功

**nvidia-smi 完整状态：**
| GPU | Memory | Util | Process |
|-----|--------|------|---------|
| 0 | 12691MiB | 89% | PID 43755 — **eval_gsm8k grpo_rasp_alpha3p0_20** (本次启动) |
| 1 | 17651MiB | 97% | PID 5241 |
| 2 | 16261MiB | 91% | PID 37026 — eval_gsm8k sft_alpha3p0_20 |
| 3 | 31358MiB | 94% | PID 40073 + 41541 — eval depth_first_20 + random_20_seed123 |

**日志前几行：**
```
Loading model from .../grpo_rasp_alpha3p0_20_v2/checkpoint-100
Non-uniform MLP detected: intermediate_size range [8128, 18944]
Model device after .cuda(): cuda:0 (CUDA_VISIBLE_DEVICES=0)
Evaluating on 1319 test samples
Evaluating:   1%|          | 8/1319 [00:22<1:01:37, 2.82s/it]
```

---
