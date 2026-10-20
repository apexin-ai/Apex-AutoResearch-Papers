# infra restart lconsist training

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_restart-lconsist-training_20260519T231922_result.json`
- **Structured JSON:** [`fea74d6fe377df091e0d.json`](../../sessions/fe/fea74d6fe377df091e0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功恢复，汇总：

1. **Resume 机制**：脚本原本只有 `--resume` / `--resume_step` 调整 log_step 计数器，不加载权重。已 patch 添加了 checkpoint 加载逻辑：LoRA adapter 用 `PeftModel.from_pretrained`，action_head/afford_decoder 用 `load_state_dict`。optimizer state 未保存，从头初始化。
2. **新 PID**：116255（torchrun 主进程）
3. **从 step 1000 开始**：日志显示 `[Step 1000]` 起步，当前已到 1039
4. **无错误**：日志正常，loss 合理（L_act ≈ 0.27-0.53, L_consist ≈ 0.0003-0.0006, para_hit=100%）
5. **GPU 0 显存**：24917 MiB 已占用
6. **预计时长**：~2h40m 完成剩余 19000 步（~2.1 it/s）

---
