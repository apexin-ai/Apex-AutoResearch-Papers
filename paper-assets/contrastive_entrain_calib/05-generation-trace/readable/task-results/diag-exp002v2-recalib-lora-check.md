# diag exp002v2 recalib lora check

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp002v2-recalib-lora-check_20260519T064536_result.json`
- **Structured JSON:** [`a08acea33ff830212405.json`](../../sessions/a0/a08acea33ff830212405.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成，汇总如下。

---

## 诊断结果

### LoRA 加载状态：**LOADED** ✓

**证据：**

1. **脚本明确调用 resume**（第 ~155 行）：
   ```python
   trainer.train(resume_from_checkpoint="/root/contrastive_entrain_calib/checkpoints/exp002v2_dcgrpo_cosine/checkpoint-500")
   ```

2. **checkpoint-500 目录完整**，包含 `adapter_model.safetensors`（LoRA 权重）、`optimizer.pt`、`scheduler.pt`、`trainer_state.json` 等全部恢复文件。

3. **进度条从 0 跳到 501**：`0/8000 [00:00]` → `501/8000 [00:33]`，33 秒跳过 500 步。这是 HF Trainer 处理 `resume_from_checkpoint` 后 fast-forward dataloader 的标志行为，只有成功加载 checkpoint 才会触发。

4. **step counter 重置是正常的**：日志里的 `[step 1]`、`[step 2]` 来自 `Exp002v2Trainer._log_step`，在 `__init__` 中初始化为 0，是自定义计数器，不是 global step。实际 global step 是 501、502...（与进度条一致）。

5. **日志中没有 "Continuing training" 或 "Loading adapter" 消息**：这是因为 TRL GRPOTrainer 有自己的 `train()` 实现，不输出标准 HF Trainer 的 resume 日志。不影响实际加载。

### recalibration_interval 设置

- **已设置，值 = 500**
- 脚本第 10 行注释：`recalibration_interval=500 (no recalibration)`
- 第 42 行：使用预计算的 `directions_recalib_step500.pt` 作为起始方向
- 第 144 行：`recalibration_interval=500`
- 含义：下一次 recalibration 将在 global step 1000 触发

### 采取的行动

无需 kill。训练正常进行，当前在 global step ~513，LoRA 权重已从 checkpoint-500 恢复。

---
