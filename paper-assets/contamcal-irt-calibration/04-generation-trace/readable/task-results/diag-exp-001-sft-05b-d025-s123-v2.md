# diag exp 001 sft 05B d025 s123 v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp_001_sft_05B_d025_s123_v2_20260515T054927_result.json`
- **Structured JSON:** [`36344f04b4180bdd4a11.json`](../../sessions/36/36344f04b4180bdd4a11.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

- **根因**: **误报 — 训练实际已成功完成。** 进程正常退出（epoch 1.0, train_runtime=5929.6s），但脚本未写 sentinel 文件且未配置 W&B，监控系统检测到 PID 498153 不存在后判定为 "process dead"，连续 5 次检查均无 sentinel/W&B 信号，自动标记为 failed。
- **日志关键信息**: 最后一条日志 `{'train_loss': 1.5481, 'epoch': 1.0, 'train_runtime': 5929.61s}` — 训练正常跑完 1 个 epoch，无任何错误。
- **checkpoint 状态**: **完整。** `lora_adapter/` 目录包含 `adapter_model.safetensors` (33.6MB)、`adapter_config.json`、tokenizer 文件、`training_args.bin`，以及中间 checkpoint `checkpoint-3384`。可直接用于推理/评估。
- **GPU 当前状态**: GPU 3 当前被 PID 503791 占用（8976MiB），非本实验进程（本实验 PID 498153 已正常退出）。GPU 0/4 空闲。
- **建议修复方案**: 将此实验状态从 failed 改为 completed。训练脚本 `train_sft.py` 需要在训练结束后写一个 sentinel 文件（如 `touch &lt;output_dir>/DONE`），否则监控系统无法区分"正常完成退出"和"异常崩溃退出"。
- **是否可重试**: **不需要重试** — 训练已成功完成，checkpoint 完整可用。
- **重试时建议修改**: N/A（无需重试）。后续实验应在 `train_sft.py` 末尾添加 sentinel 写入逻辑。

---
