# ops s2v2 exit diag and len512

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_s2v2-exit-diag-and-len512_20260523T020618_result.json`
- **Structured JSON:** [`f9e230cdb334e4b3ec3e.json`](../../sessions/f9/f9e230cdb334e4b3ec3e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报如下：

---

## 诊断结果

### 1. 训练状态：**SUCCESS**
- 最终 step: **8000/8000**，lr=0.0（cosine schedule 走完）
- 最终 loss: sft_loss=2e-06, l2_loss=0.00078, total_loss=8e-05
- Checkpoints: ckpt-2000 到 ckpt-8000（每 500 步），共 13 个
- 总训练耗时: ~54831s (~15.2h)

### 2. Registry & Cron
- Registry: status=DONE, conclusion=success, checkpoint_path 和 log_path 已更新
- Cron: exp-004-s2-v2 已删除

### 3. SCP 状态
- **ckpt-8000**: 已 SCP 到 28034，验证通过（698MB adapter_model.safetensors）
- **ckpt-7500**: 28034 上缺失，已补 SCP，验证通过

### 4. len512 启动
- **cuda:1 不空闲** — `run_exp003_len512_r3only.py` (PID 552217) **已经在 cuda:1 上运行**
- 无需重新启动，已有人提交了 len512 任务

### 5. 异常/注意事项
- 日志文件实际路径是 `train_exp004s2v2.log`，非 `exp-004-s2-resume.log`（registry spec 中的旧路径）
- 29046 上没有 SSH config，SCP 到 28034 需要用 `connect.westd.seetacloud.com -P 28034` 全路径
- cuda:0 上还跑着 `run_exp003_gs8_r3only.py` (PID 516696)

---
