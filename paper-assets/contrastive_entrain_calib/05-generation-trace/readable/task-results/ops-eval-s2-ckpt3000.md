# ops eval s2 ckpt3000

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-s2-ckpt3000_20260525T145244_result.json`
- **Structured JSON:** [`d099e476b06daa99895a.json`](../../sessions/d0/d099e476b06daa99895a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

状态汇报：

**ckpt-3000 eval 已在运行中**（PID 38838, cuda:0），无需重新提交。

- 命令：`python eval/eval_unified_preset.py --model_path .../Qwen3-8B --lora_path .../checkpoint-3000 --output_dir .../exp003s2_d027_eval/ --exp_id exp003s2-ckpt3000`
- 已运行 ~19 分钟，参考 ckpt-2500 耗时 4896s (~82min)，预计还需 ~63 分钟
- Registry 已更新为 RUNNING（exp-003-s2-eval-ckpt3000）

**诊断**：上次 chained eval 的 ckpt-3000 并非未执行——结果目录只有 ckpt-2500 的输出文件，但 cuda:0 上正在跑的正是 ckpt-3000 eval，说明它在 ckpt-2500 完成后确实启动了 ckpt-3000（可能是手动或脚本自动触发的）。

cuda:1 上 exp-003-s3 训练正常运行，未受影响。

预计 ~23:55（UTC+8）完成。完成后我需要：
1. 从 `exp003s2-ckpt3000_preset_summary.txt` 提取 SYCONScore/ToF/NoF
2. update_registry 更新 metrics、conclusion、checkpoint_path、log_path

需要我稍后回来检查结果吗？

---
