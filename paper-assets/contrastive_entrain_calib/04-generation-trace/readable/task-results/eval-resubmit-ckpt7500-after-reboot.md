# eval resubmit ckpt7500 after reboot

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_resubmit-ckpt7500-after-reboot_20260522T122129_result.json`
- **Structured JSON:** [`ffce049a3de550398611.json`](../../sessions/ff/ffce049a3de550398611.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 都已正常运行：

**28034 GPU0** — `exp-003-eval-s2-ckpt7500`：已加载 LoRA adapter，正在对 362 pairs 执行 eval。

**28034 GPU1** — `exp-002v3-eval-ckpt2000`：模型加载中（checkpoint shards loading）。

总结：
- exp-002v3 的 checkpoints 在 29046 上不存在，但 **28034 上已有副本** (`/root/autodl-tmp/checkpoints/exp002v3_dcgrpo_scaled_cosine/`)，包含 checkpoint-500 到 checkpoint-2500，无需 SCP。
- 原始命令参数有误（`--checkpoint-dir` / `--n-valid` / `--n-invalid` 不是脚本参数），已修正为 `--model_path` + `--lora_path`。
- 两个 eval 分别在 GPU0 和 GPU1 并行运行。

---
