# diagnose phase2 lora only s42

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_phase2_lora_only_s42_20260519T130521_result.json`
- **Structured JSON:** [`5538cdad3563970992d8.json`](../../sessions/55/5538cdad3563970992d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告：phase2_lora_only_s42

### 根本原因

**`--gate-type lora_only` 不是合法的 argparse 选项。**

`train_phase2.py` 第 102 行：
```python
parser.add_argument("--gate-type", type=str, default="threadgate", choices=["threadgate", "uniform", "none"])
```
choices 只有 `threadgate`、`uniform`、`none`，不包含 `lora_only`。传入 `--gate-type lora_only` 会被 argparse 直接拒绝并退出（exit code 2，dispatcher 可能映射为 1）。

### 训练进度

**训练实际已完成。** 日志 `/root/runs/turn_residual_gating/phase2_lora_only_s42.log` 显示一次用 `--gate-type none` 的运行已成功完成：

- 3 个 epoch 全部完成（epoch 0/1/2）
- 3000 total steps
- 耗时 20588.6s（~5.7 小时）
- Gate 全程固定 1.0000（符合 lora_only 预期）
- 无 error/traceback

### 可用 Checkpoint

| 路径 | 内容 |
|------|------|
| `runs/phase2_lora_only_s42/epoch_0/lora/` | epoch 0 LoRA adapter |
| `runs/phase2_lora_only_s42/epoch_1/lora/` | epoch 1 LoRA adapter |
| `runs/phase2_lora_only_s42/epoch_2/lora/` | epoch 2 LoRA adapter |
| `runs/phase2_lora_only_s42/lora/` | 最终 LoRA adapter（20MB） |
| `runs/phase2_lora_only_s42/train_config.json` | 训练配置（记录 gate_type="none"） |

无 `gate_params.pt`（`gate_type=none` 时 `model.gates is None`，不保存 gate 参数，这是正确行为）。

### GPU / 磁盘状态

- **GPU**: NVIDIA RTX PRO 6000 Blackwell (98GB), 空闲（0MB used, 0% utilization）
- **根分区**: 30GB, 已用 16GB (52%), 剩余 15GB
- **数据盘**: 250GB, 基本空闲

### 修复方案

**方案 A（推荐）**: 在 `train_phase2.py` 第 102 行添加 `lora_only` 到 choices，并在解析后映射为 `none`：

```python
# 第 102 行
parser.add_argument("--gate-type", type=str, default="threadgate", 
                    choices=["threadgate", "uniform", "none", "lora_only"])

# 在 args = parser.parse_args() 之后添加：
if args.gate_type == "lora_only":
    args.gate_type = "none"
```

**方案 B**: 直接把 dispatch 命令中的 `--gate-type lora_only` 改为 `--gate-type none`。

### 结论

**训练结果可用，无需重跑。** EXIT_CODE=1 是因为 argparse 不认识 `lora_only`。现有 checkpoint 来自之前一次用 `--gate-type none` 的成功运行，语义上等价于 "lora_only"（纯 LoRA，无 gating）。只需修复 choices 或 dispatch 命令即可避免后续同样的错误。

---
