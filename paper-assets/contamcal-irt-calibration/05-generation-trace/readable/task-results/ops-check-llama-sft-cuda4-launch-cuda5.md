# ops check llama sft cuda4 launch cuda5

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_llama_sft_cuda4_launch_cuda5_20260516T125411_result.json`
- **Structured JSON:** [`2993a66fb6df115645c2.json`](../../sessions/29/2993a66fb6df115645c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务全部完成。

---

## 产出汇总

### Part A: cuda:4 Llama SFT 状态
- **状态**: 训练已正常完成，进程自然退出（非崩溃）
- **PID 752961**: 已退出
- **最终指标**: train_loss=1.5165, mean_token_accuracy=0.6685, epoch=1.0, runtime=8170s
- **Checkpoint**: `/root/autodl-tmp/exp001/checkpoints/Llama-3.2-3B_d000_s42/` (含 `lora_adapter/`, `merged/`, `train_config.json`)
- **Registry**: `exp_001_sft_llama32_3B_d000_s42` → DONE(success)
- cuda:4 现在空闲

### Part B: cuda:5 新任务
- **任务**: Qwen2.5-1.5B-Instruct eval (aligned + para_aligned, 4 benchmarks: mmlu/gsm8k/arc_challenge/humaneval)
- **脚本**: `scripts/run_instruct_15b_eval_cuda5.sh` (CUDA_VISIBLE_DEVICES=5)
- **PID**: 782625
- **Log**: `/tmp/instruct_15b_eval_cuda5.log`
- **当前状态**: 正在下载模型 (2.88GB, ~6MB/s, 预计 ~8min)，下载完成后自动开始 eval
- **Registry**: `exp_001_eval_15B_instruct` → RUNNING

### GPU 全局状态
| GPU | 占用 | 任务 |
|-----|------|------|
| cuda:0 | 7.3G, 56% | python (PID 780943) |
| cuda:1 | 1.9G, 22% | 0.5B signals (PID 780591) |
| cuda:2 | 空闲 | — |
| cuda:3 | 6.6G, 62% | 3B-Instruct eval v2 (PID 764460) |
| cuda:4 | 空闲 | Llama SFT 已完成 |
| cuda:5 | 启动中 | 1.5B-Instruct eval (PID 782625) |

---
