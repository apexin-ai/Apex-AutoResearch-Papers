# analysis v3 lora visual r16

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v3_lora_visual_r16_20260516T201401_result.json`
- **Structured JSON:** [`d45b83a06004a80448db.json`](../../sessions/d4/d45b83a06004a80448db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完成。`v3_lora_visual_r16` 分析结果：

| 指标 | 值 |
|------|-----|
| final_train_loss | **0.5899** |
| initial_train_loss | 1.9794 |
| loss_reduction | 3.36x |
| total_steps | 10,000 |
| training_time | 182 min (3.41 GPU-hours) |
| exit_code | 0 |
| errors/tracebacks | 0 |

**v3 系列对比**：

| 实验 | Final Loss |
|------|-----------|
| v3_lora_physical_r16 | 0.5876 |
| v3_lora_visual_r16 | **0.5899** |
| v3_lora_universal_r16 | 0.6030 |
| v3_lora_spatial_r16 | 0.6126 |

Visual expert 的 final loss 排第二，与 physical 非常接近，表现符合预期。状态已标记为 `DONE / success`。

---
