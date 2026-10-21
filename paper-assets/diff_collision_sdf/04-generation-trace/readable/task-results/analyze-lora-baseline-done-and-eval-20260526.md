# analyze lora baseline done and eval 20260526

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_lora_baseline_done_and_eval_20260526_20260526T013527_result.json`
- **Structured JSON:** [`4a8024300ef97689e694.json`](../../sessions/4a/4a8024300ef97689e694.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 训练结果
| Exp | Final Loss | Checkpoint | Status |
|-----|-----------|------------|--------|
| train_pi05_lora_baseline_s0 | 0.01343 | 30000/ ✓ (+ best/) | DONE |
| train_pi05_lora_baseline_s1 | 0.01408 | 30000/ ✓ (+ best/) | DONE |

两个 seed 的 loss 都正常收敛（lr=0 at final step），30K checkpoint 完整（~7.5GB model.safetensors）。

### Eval 启动状态
| Exp ID | GPU | PID | Log | 状态 |
|--------|-----|-----|-----|------|
| eval_lora_baseline_30k_s0 | cuda:0 | 28196 | /tmp/eval_lora_baseline_30k_s0.log | 模型加载中 |
| eval_lora_baseline_30k_s1 | cuda:1 | 28961 | /tmp/eval_lora_baseline_30k_s1.log | 模型加载中 |

两个 eval 进程都已正确启动，日志确认 checkpoint 加载正确（model_type=lora_baseline, config=pi05_libero, suite=safelibero_object, --pi05）。GPU 内存尚未占用（模型权重加载阶段），无异常。

---
