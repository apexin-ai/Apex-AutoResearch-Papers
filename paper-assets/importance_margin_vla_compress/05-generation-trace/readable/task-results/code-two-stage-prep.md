# code two stage prep

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_two_stage_prep_20260516T041247_result.json`
- **Structured JSON:** [`dd0db163758b16f39d9f.json`](../../sessions/dd/dd0db163758b16f39d9f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。总结：

### 产出清单

**新文件：**
- `configs/imm_two_stage.yaml` — Two-stage v9 配置，基于 `imm_anchor.yaml`，lambda=1.0, stage1_steps=30000, stage2_steps=0, lr=5e-4

**修改文件：**
- `train_twostage.py` — 4 处补丁：
  1. **L324**: `max_steps` 不覆盖 stage2_steps=0 的配置
  2. **L339**: 加载 baseline_v5 checkpoint 到 `model.policy`
  3. **L376**: 打印参数统计（total/trainable/frozen）
  4. **L414**: stage2_steps=0 时跳过 Stage 2 并输出 dry-run 结果

**Dry-Run 结果（5 steps on GPU 1）：**
- 冻结参数 451.5M，可训参数 3.46M (ACIS, 0.76%)
- LoRA 梯度为 0，ACIS 梯度正常（7/10 params）
- margin_loss 初始值 0.2969，grad_norm=15.07
- Stage 2 正确跳过，DRY RUN PASSED

**注意事项：**
- 运行正式训练需要 `source /etc/network_turbo`（AutoDL 网络限制）
- 有另一个 v8b_twostage 训练进程 (PID 133669) 在 GPU 1 上运行，正式训练前需确认其状态
- 实验已注册为 `imm_two_stage_v9`，状态 PREPARING

---
