# submit d022 comprehensive check

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_d022-comprehensive-check_20260515T100720_result.json`
- **Structured JSON:** [`f0f485896eea42581e0a.json`](../../sessions/f0/f0f485896eea42581e0a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态总览

| GPU | 当前任务 | 状态 | 进度 | 预计剩余 |
|-----|---------|------|------|---------|
| 0 | v4-random-fixed-inject25-s0 | **运行中** | 1045/1635 (64%) | ~20 min |
| 1 | v4-random-fixed-inject25-s123 | **运行中** | 1068/1635 (65%) | ~20 min |
| 2 | v4-random-fixed-inject50-s0 | **运行中** | 1431/1635 (88%) | ~7 min |
| 3 | v4-random-fixed-inject50-s123 | **运行中** | 1410/1635 (86%) | ~8 min |

**已完成的 eval 结果：**
- v4_taxei_fixed_inject25_s0_eval: success_rate=**0.468**
- v4_taxei_fixed_inject25_s123_eval: success_rate=**0.468**

**已就绪待 eval（checkpoint-1635 存在）：**
- `v4_taxei_fixed_inject50_s0/v0-20260515-153735/checkpoint-1635`
- `v4_taxei_fixed_inject50_s123/v0-20260515-153737/checkpoint-1635`

**当前阻塞：** 所有 4 个 GPU 都在跑训练，无法提交 eval。
- GPU 2,3 约 7-8 分钟后空闲 → 提交 TaxEI inject50 eval
- GPU 0,1 约 20 分钟后空闲 → 提交 Random inject25 eval

需要等训练完成后再提交 eval 任务。是否需要我过一会儿再检查并自动提交？

---
