# code lora only baseline

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_lora_only_baseline_20260518T201649_result.json`
- **Structured JSON:** [`80aa0466b8dc660862e2.json`](../../sessions/80/80aa0466b8dc660862e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件修改完毕，语法检查通过。

### 修改汇总

**threadgate.py** (5 处修改):
- L86: 新增 `self.num_layers = num_layers`
- L88-89: `gate_type="none"` 分支，`self.gates = None`
- L102: gates 设备迁移加 `if self.gates is not None` 守卫
- L114-117: hooks 注册加 `if self.gate_type != "none"` 守卫
- L163-164: `get_gate_values()` 对 `gate_type="none"` 返回全 1.0 字典

**train_phase2.py** (5 处修改):
- L101: choices 加入 `"none"`
- L181-187: gate_params 为空时 param_groups 只含 LoRA
- L263: diversity loss 条件加 `args.gate_type != "none"`
- L279: gate grad 检查加 `model.gates is not None`
- L326, L340: checkpoint 保存 gate_params.pt 加 `model.gates is not None` 守卫

### LoRA-only 训练命令

```bash
python3 /root/turn_residual_gating/src/train_phase2.py \
    --gate-type none \
    --output-dir /root/turn_residual_gating/checkpoints/v8_lora_only \
    --data-dir /root/turn_residual_gating/data/ultrachat_8k \
    --epochs 3 \
    --lr 2e-4 \
    --grad-accum 4 \
    --max-seq-len 2048 \
    --lambda-gar 0.1 \
    --gar-loss-mode mse_target \
    --gar-target 0.5 \
    --lambda-gate-div 0.0 \
    --seed 42
```

`--lambda-gate-div 0.0` 因为无 gate 可分化；`--init-bias` 和 `--gate-lr-multiplier` 会被忽略。L_GAR 仍通过 LoRA 改变 attention pattern 正常反传。

---
