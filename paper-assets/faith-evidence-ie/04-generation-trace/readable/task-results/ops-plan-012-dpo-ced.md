# ops plan 012 dpo ced

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_plan_012_dpo_ced_20260515T155054_result.json`
- **Structured JSON:** [`a14dd2391c2908ef3894.json`](../../sessions/a1/a14dd2391c2908ef3894.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

plan_012 DPO+CED 实验已成功启动。

**总结：**
- **DPO pairs**: 2,666 pairs 构建完成（从 21,952 scored generations，按 CED reward top-1 vs bottom-1）
  - Chosen CED mean: 0.721, Rejected CED mean: 0.286, margin mean: 0.435
- **训练配置**: Qwen3-4B + SFT adapter merge → 新 LoRA (r=64, α=128), β=0.1, lr=2e-5, bs=1×16, 3 epochs, sigmoid loss
- **运行状态**: GPU 2 (RTX 5090), 29.1/32.6 GB, ~12.5s/step, 501 steps total
- **预计完成时间**: ~1.7h
- **修复**: TRL 1.1.0 不支持 `max_prompt_length` 参数，已从 DPOConfig 中移除
- **日志**: `~/runs/faith-evidence-ie/plan_012_dpo_ced.log`

---
