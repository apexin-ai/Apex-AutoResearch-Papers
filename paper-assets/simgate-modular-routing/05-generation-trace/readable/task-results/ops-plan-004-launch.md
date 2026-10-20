# ops plan 004 launch

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_plan-004-launch_20260514T053757_result.json`
- **Structured JSON:** [`5516a5e90e58fff0b58e.json`](../../sessions/55/5516a5e90e58fff0b58e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动并正常运行。汇报：

**数据格式化**
- 2040 条记录转换完成，0 条跳过
- 分布：deterministic 1830 (89.7%) / internal 210 (10.3%)

**训练配置**
- Train: 1735, Val: 305
- Route 分布 (train): deterministic 1555, internal 180
- Upsampling 已启用: WeightedRandomSampler with 1735 draws/epoch
- LoRA trainable params: 6,422,528 / 1.73B total (0.37%)
- Gradient accumulation: 8 steps (batch_size=4, effective=32)
- WANDB offline 模式已生效
- GPU1 上运行，~1.0 it/s，165 steps/epoch，预计 ~3×165s ≈ 8 分钟/epoch

**进程状态**
- tmux session: `plan-004-ablation-b` 运行中
- PID: 223455
- GPU1 显存: 3897 MiB
- 当前进度: epoch 1, 22/165 steps (~13%)

---
