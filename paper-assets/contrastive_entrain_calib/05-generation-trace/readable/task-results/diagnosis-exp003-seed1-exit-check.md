# diagnosis exp003 seed1 exit check

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_exp003-seed1-exit-check_20260521T102010_result.json`
- **Structured JSON:** [`a3937d7af4ed7b070290.json`](../../sessions/a3/a3937d7af4ed7b070290.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：**SUCCESS**

**checkpoint-8000 完整存在，训练正常完成 8000 steps。**

证据：
- `trainer_state.json` 确认 `global_step: 8000`，epoch=177.78
- `adapter_model.safetensors` 245MB，时间戳 May 21 18:12
- checkpoint-8000 目录包含全部 15 个文件（adapter_config, optimizer, scheduler, tokenizer 等）
- 所有中间 checkpoint（500-8000，每 500 步）均存在

**日志说明**：`exp003_v2.log` 在 step 3760 处停止写入（May 20 05:55），但训练实际继续运行到完成。这是日志 buffer/handler 问题，不影响训练。另有 `exp003_restart.log`（May 18，17KB）是更早的文件。

**GPU 状态**：进程 70649 已退出，但 GPU 0 上仍有进程 PID 237437 占用 38GB（92% util）。这可能是其他实验，不是 exp-003。

**ckpt-8000 可以立即 SCP + eval。**

---
