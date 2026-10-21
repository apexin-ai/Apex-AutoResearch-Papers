# verify lora pertask tsr from json

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_lora_pertask_tsr_from_json_20260528T010627_result.json`
- **Structured JSON:** [`0d719a2fc0fb592f4da6.json`](../../sessions/0d/0d719a2fc0fb592f4da6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

## LoRA Per-task TSR from Reeval JSONs (eval_seed=7, 30k checkpoint)

| Seed | OJ | CP | Milk | BBQ | Mean |
|------|-----|-----|------|-----|------|
| s0 | 32.0% | 74.0% | 42.0% | 58.0% | 51.5% |
| s1 | 34.0% | 62.0% | 50.0% | 60.0% | 51.5% |
| s2 | 24.0% | 76.0% | 42.0% | 64.0% | 51.5% |
| **Mean** | **30.0%** | **70.7%** | **44.7%** | **60.7%** | **51.5%** |

CAR: 全部 100.0%（LoRA 无碰撞惩罚，符合预期）。

## 对比 Appendix 当前值

| | OJ | CP | Milk | BBQ | Mean |
|--|-----|-----|------|-----|------|
| Appendix 现值 (s0) | 18.0% | 72.0% | 32.0% | 62.0% | 46.0% |
| Reeval s0 (seed7) | 32.0% | 74.0% | 42.0% | 58.0% | 51.5% |

## 结论

**Appendix per-task TSR 数据需要更新。** 现有 appendix 的 LoRA s0 数据 (mean=46.0%) 与主表 (51.5%) 不一致，且不匹配任何现存 JSON 文件——可能来自早期被废弃的 eval run。

正确数据来源是 westd-45947 上的 3 个 reeval JSON（eval_seed=7），三个 seed 均为 51.5%，与主表完全一致。建议用上表 Mean 行更新 appendix。

---
