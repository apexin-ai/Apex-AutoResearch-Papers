# code action delta implementation

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_action-delta-implementation_20260515T142441_result.json`
- **Structured JSON:** [`c88d0270d3eb333e1417.json`](../../sessions/c8/c88d0270d3eb333e1417.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总结果：

---

## Action Delta Dry-Run (Trained, Layer 4)

| 指标 | 值 |
|---|---|
| overall_r2 | 0.0345 |
| per_task_mean_r2 | 0.0329 |
| gripper_accuracy | 0.697 |
| gripper_delta_accuracy | 0.987 |
| raw_mse | 0.0077 |

per_dim_r2: dx=0.140, dy=0.200, dz=0.318, drx=0.041, dry=0.040, drz=0.109, gripper=0.013

符合预期：去除自相关后 R² 从 ~0.54 降到 ~0.035（copy baseline = 0），说明 layer 4 对 action delta 有微弱但正的预测能力。gripper delta accuracy 高达 98.7%（因为大部分时间 gripper 不变，delta=0 占绝对多数）。

---

## DINO Action Prediction (Layer 0)

目录 **存在**，结果：

| 指标 | 值 |
|---|---|
| overall_r2 | 0.669 |
| per_task_mean_r2 | 0.676 |
| gripper_accuracy | 0.900 |

DINO 只有 1 层（layer 0），已跑完。

---

## 全 33 层 Sweep 启动命令

**Trained:**
```bash
cd /root/vla-ssd && nohup python scripts/train_probes.py \
  --features_dir /root/autodl-tmp/vla-ssd/features/trained/ \
  --output_dir /root/autodl-tmp/vla-ssd/results/trained/ \
  --probe_type action_delta \
  --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_10/ \
  --gpu 0 \
  > /tmp/action_delta_trained.log 2>&1 &
```

**Untrained:**
```bash
cd /root/vla-ssd && nohup python scripts/train_probes.py \
  --features_dir /root/autodl-tmp/vla-ssd/features/untrained/ \
  --output_dir /root/autodl-tmp/vla-ssd/results/untrained/ \
  --probe_type action_delta \
  --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_10/ \
  --gpu 0 \
  > /tmp/action_delta_untrained.log 2>&1 &
```

**代码改动摘要**: `train_probes.py` 新增 `action_delta` probe type，复用 `run_action_prediction` 函数，通过 `predict_delta` flag 切换 target 为 `a[t+1]-a[t]`。额外报告 `gripper_delta_accuracy`（3-class）。结果输出到 `action_delta/` 子目录。

---
