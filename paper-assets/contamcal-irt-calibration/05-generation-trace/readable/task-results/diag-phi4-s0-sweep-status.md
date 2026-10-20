# diag phi4 s0 sweep status

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_phi4-s0-sweep-status_20260520T151635_result.json`
- **Structured JSON:** [`aacae80895a653769a95.json`](../../sessions/aa/aacae80895a653769a95.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Phi-4 s0 sweep 状态

- **训练：5/5 dosage 全部完成** (d000, d005, d025, d050, d100)，每个 checkpoint 目录含 `lora_adapter/` + `train_config.json`
- **最后一个 dosage (d100)** 于 `2026-05-20 22:44:54 CST` 完成，exit code=0，log 末尾打印 `ALL_DONE_PHI4_S0`
- **cuda:0 当前空闲**，无进程
- **无内置 eval**：`eval_results_v2/` 目录不存在，训练脚本仅产出 checkpoint，eval 需单独跑
- 最终 dosage 训练指标：loss=1.192, mean_token_accuracy=0.7206, epoch=1.0, 总训练时长 ~9234s (~2.5h)

---
