# diagnose detach ln s4 anomaly

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_detach_ln_s4_anomaly_20260527T144548_result.json`
- **Structured JSON:** [`776d76b19cd8c7b7d851.json`](../../sessions/77/776d76b19cd8c7b7d851.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**确定根因。**

## 排查报告：detach_ln_s4_eval TSR=0.018

### 1. Action Loss 收敛情况
**无法直接确认** — 训练日志完全缺失（westd-34685、westd-10894 的 `/root/occsafe_vla/logs/`、`/root/autodl-tmp/logs/` 均无 detach_ln_s4 训练日志，bash_history 为空，WandB offline run 数据不可解析）。

但通过间接证据：
- 40k→50k checkpoint 的 LoRA 权重几乎不变（growth ratio ~1.00x），说明训练已收敛/稳定
- 权重中无 NaN/Inf
- **但收敛到了错误解**

### 2. Checkpoint 路径
**正确** — eval 加载了 `/root/autodl-tmp/checkpoints/detach_ln_s4/...--detach_ln_s4--50000_chkpt`，checkpoint 文件完整（model shards、LoRA adapter、action_head、occ_head、proprio_projector 齐全）。

### 3. 代码版本
checkpoint 中的 modeling_prismatic.py 和 configuration_prismatic.py 与 v2_s1 **完全一致**。eval 代码路径无差异。

### 4. 根因判断：**训练产生了过度偏移的 LoRA 权重**

直接推理对比（相同 dummy 输入）：

| 指标 | s4 (broken) | v2_s1 (good) |
|------|-------------|-------------|
| 首步 z-action | **-0.824** | -0.247 |
| gripper action | **1.0**（饱和）| 0.305 |
| action range | [-0.83, 1.02] | [-0.26, 0.52] |
| action mean | -0.015 | 0.034 |

**s4 的动作预测值比正常模型大 2-4 倍。** 机器人执行极端动作，无法完成任何任务但会随机碰撞物体（CAR=67.2%）。

根源是 **LLM 早期层 LoRA delta_W 异常**：

| 层 | s4 delta_W std | v2 delta_W std | 倍率 |
|----|-------------|-------------|------|
| L0.q_proj | 0.00791 | 0.00254 | **3.1x** |
| L0.v_proj | 0.00269 | 0.00055 | **4.9x** |
| L0.down_proj | 0.00411 | 0.00084 | **4.9x** |
| L15.q_proj | 0.00671 | 0.00677 | 1.0x |
| L31.q_proj | 0.00650 | 0.00522 | 1.2x |

早期层（L0-L1，处理视觉特征输入的层）LoRA 修正量过大 → hidden states 被放大 → action head 输出极端值。

### 5. 为什么训练出了问题？

无法确定确切原因（训练日志缺失），但发现以下线索：

1. **代码版本差异**：训练时 committed 代码（`bdaee75`）**没有 `occ_norm_type` 参数**。尽管实验名含 "ln"，实际 occ_head 使用的是 BatchNorm（因为 LN 支持在未提交的修改中才添加）。但 `occ_detach=True` 理论上阻止了 occ 梯度回传，BN vs LN 不应影响 action loss。

2. **另一个 v1 实验（s3）** 早期层也偏大但程度较轻（1.4-2.5x），提示 v1 训练可能系统性地存在早期层过度适应的倾向。

3. **最可能解释**：不良随机种子导致训练早期阶段 L0 层接收到异常梯度信号后"锁定"在次优解上。40k 和 50k 权重几乎相同，说明问题在训练前半段就已形成。

### 建议下一步
- 这个 checkpoint **不可挽救**，需要用 v2 代码（含 LN 支持）以不同种子重新训练
- 或者直接用已有的 3 个 v2 种子（s0/s1/s2）的结果，不再追加 v1 数据点

---
