# diagnose exp 002 exit

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_002_exit_20260516T130202_result.json`
- **Structured JSON:** [`809779b1c373aabd344b.json`](../../sessions/80/809779b1c373aabd344b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**状态：崩溃（Generation 0 评估完成后，保存 checkpoint 时磁盘满）**

**错误信息：**
```
safetensors_rust.SafetensorError: Error while serializing: I/O error: No space left on device (os error 28)
```

**崩溃位置：** `src/pipeline.py:79` — `model.save_pretrained(gen0_ckpt_path)` 保存 Gen 0 checkpoint 时失败。

**已完成的工作：**
- Gen 0 (pretrained baseline) 评估成功：**eff_rank=516.14, ppl=8.07, distinct4=0.7510**
- Gen 0 checkpoint 实际已写入 2.04 GB（`checkpoints_1b/gen_0/model.safetensors`），但后续操作时磁盘耗尽

**根因：** 根分区 30GB 已 100% 占满（仅剩 996K）。Pythia 1B 模型单个 checkpoint 约 2GB，多代训练 + 模型权重无法放在 30GB 根分区。

**需要的修复：**
1. 清理磁盘空间，或将 checkpoints 路径改到数据盘（如 `/root/autodl-tmp/`）
2. 确认是否有数据盘可用，如果有则修改 `run_phase0_1b.py` 中的 checkpoint 输出路径

---
