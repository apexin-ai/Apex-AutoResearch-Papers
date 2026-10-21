# analyze exp 001 sft 3B d000 s123

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_exp_001_sft_3B_d000_s123_20260515T002900_result.json`
- **Structured JSON:** [`a127c28fe2e6a9359953.json`](../../sessions/a1/a127c28fe2e6a9359953.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完成。

**分析结论：exp_001_sft_3B_d000_s123 训练成功。**

- train_loss=1.1361（与 seed=42 的 1.1357 仅差 0.04%），两 seed 一致性好
- 1 epoch / 3125 steps，耗时 3.65h
- Checkpoint 完整：`/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s123/lora_adapter/adapter_model.safetensors`（119.8MB）
- 无 W&B 记录
- 状态保持 ANALYZING，可进入 eval 阶段

---
