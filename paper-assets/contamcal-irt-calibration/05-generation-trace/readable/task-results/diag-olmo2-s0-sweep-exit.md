# diag olmo2 s0 sweep exit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_olmo2-s0-sweep-exit_20260520T102455_result.json`
- **Structured JSON:** [`3aa129d007a5303c6008.json`](../../sessions/3a/3aa129d007a5303c6008.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

**5 个 dosage 全部正常完成。** 证据：
- 5 个 checkpoint 都有 `adapter_model.safetensors` (~160MB) 和 `train_config.json`
- checkpoint step 数与样本数吻合：d000=3125, d005=3177, d025=3384, d050=3642, d100=4159
- `lora_alpha=32` 确认正确

**MMLU eval 结果：无。** sweep 脚本 (`sft_qwen7b_olmo2_s0_sweep.sh`) 只包含训练，不包含 eval 步骤。`results/` 目录下也没有 OLMo eval 文件。

**cuda:2 已释放。** 0MiB / 0% utilization。

当前 GPU 占用：cuda:0 (59GB), cuda:1 (95GB), cuda:3 (66GB) 有其他进程在跑。

---
