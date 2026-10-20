# analyze exp 001 sft 3B d000 s42 a32

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_exp_001_sft_3B_d000_s42_a32_20260516T000718_result.json`
- **Structured JSON:** [`c43b709c5a8062f7d4ab.json`](../../sessions/c4/c43b709c5a8062f7d4ab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 实验结果摘要

| 项目 | 值 |
|------|-----|
| **状态** | 训练成功完成 (EXIT_CODE=0) |
| **Final loss** | 1.1324 |
| **总步数** | 3,125 steps |
| **训练时间** | 12,647s (~3h 31min) |
| **Mean token accuracy** | 0.7333 |
| **Checkpoint 路径** | `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter/` |

**Checkpoint 文件**:
- `adapter_model.safetensors` (114MB)
- `adapter_config.json` — 确认 **lora_alpha=32**, r=16, target_modules=[q/k/v/o/gate/up/down_proj]
- tokenizer 文件完整

**adapter_config 关键参数**: lora_alpha=32, r=16, dropout=0.05, bias=none, task=CAUSAL_LM, base_model=Qwen2.5-3B

---
