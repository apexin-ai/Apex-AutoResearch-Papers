# code stage2 recovery prep

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_stage2_recovery_prep_20260517T094336_result.json`
- **Structured JSON:** [`0bec4f293f5956837fdc.json`](../../sessions/0b/0bec4f293f5956837fdc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. Config 文件
`configs/libero_stage2_recovery.yaml` - 基于 `libero_baseline.yaml`，核心设置：
- 从 `checkpoints/libero_acis_stage1only_k07/stage1_done/checkpoint.pt` 加载
- `lambda_margin: 0.0` (仅 action_loss 驱动训练，ACIS 只负责 token selection)
- `lr: 2e-6`，`total_steps: 20000`，`save_every: 2000`
- piecewise k_ratio schedule: `[0, 0.9] → [5000, 0.7] → [10000, 0.5]`

### 2. 代码修改 (train.py, 808→853 lines)

| 位置 | 修改 |
|------|------|
| L53 | `parse_args()` 添加 `--max_steps` 参数 |
| L325-340 | `compute_k_ratio()` 新增 `piecewise` schedule 类型，提前于 `start/end` 解析避免 KeyError |
| L411-432 | 新增 `setup_stage2_recovery()` 函数：加载 stage1 checkpoint → `model.load_state_dict()` → 冻结 ACIS、解冻 expert |
| L638-648 | `main()` 中新增 `is_stage2_recovery` 路径和 `--max_steps` override 逻辑 |

关键设计：`stage2_recovery` 不触发 `is_twostage`，因此训练循环走 full `model()` forward（action_loss + token selection），而非 `forward_acis_only()`。

### 3. Dry-run 结果

```
Loaded stage1 checkpoint from .../stage1_done/checkpoint.pt
Stage2 recovery: frozen(ACIS)=3,460,801, trainable(expert)=450,046,176
Stage2 recovery mode: lr=2.00e-06, total_steps=20000
Overriding total_steps to 5 (dry-run)

step=0/5  loss=0.1235  action=0.1235  margin_loss=0.0000  lr=4.00e-09  grad=21.47
step=1/5  loss=0.0718  action=0.0718  margin_loss=0.0601  lr=8.00e-09  grad=21.72
step=2/5  loss=0.1061  action=0.1061  margin_loss=0.0000  lr=1.20e-08  grad=39.06
step=3/5  loss=0.1117  action=0.1117  margin_loss=0.0723  lr=1.60e-08  grad=23.70
step=4/5  loss=0.0690  action=0.0690  margin_loss=0.0100  lr=2.00e-08  grad=5.33
Training complete.
```

- **checkpoint 加载成功**
- **ACIS 冻结、expert 解冻** (3.5M frozen / 450M trainable)
- **loss == action_loss**（确认 lambda_margin=0 生效，margin_loss 仅 log 不参与训练）
- **无 shape mismatch**
- **1.5 steps/s** 训练速度

### 4. 注意事项
- 正式训练需设置 `HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1`（服务器无法访问 HuggingFace Hub）
- stage1_done checkpoint 的 step 字段为 -1（不影响训练，仅日志显示）
- k_ratio 在 5 步 dry-run 中始终为 0.9（正确，< 5000 步），完整运行时会在 step 5000/10000 处跳变

---
