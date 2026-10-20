# ops prep s123 gsm8k cqa1

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prep-s123-gsm8k-cqa1_20260519T223254_result.json`
- **Structured JSON:** [`92bd37d00bb44681a88e.json`](../../sessions/92/92bd37d00bb44681a88e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

### 产出报告

1. **s123 checkpoints**: cqa1 本地已有，无需 SCP
   - `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d000_s123/lora_adapter/` ✅ lora_alpha=32
   - `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d100_s123/lora_adapter/` ✅ lora_alpha=32

2. **eval 脚本**: `/root/contamcal-irt-calibration/exp001/eval_gsm8k_qwen7b_s123.sh` 已就绪
   - 语法检查通过
   - C009 md5 校验、C004 CUDA_VISIBLE_DEVICES=0、adapter 不存在则 exit 1 均已包含
   - 与 s42 脚本结构一致，仅改 seed 42→123 和对应路径

3. **可直接启动**: intermediate eval 完成后，确认 GPU 0 空闲（C001/C002: `nvidia-smi`），即可 `bash eval_gsm8k_qwen7b_s123.sh` 启动。

---
