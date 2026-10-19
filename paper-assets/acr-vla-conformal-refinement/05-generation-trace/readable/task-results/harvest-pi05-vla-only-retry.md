# harvest pi05 vla only retry

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_pi05-vla-only-retry_20260525T004709_result.json`
- **Structured JSON:** [`08c14ef59597fbdd1940.json`](../../sessions/08/08c14ef59597fbdd1940.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Harvest 状态已确认完整。所有 π0.5 VLA-only JSON 文件均已正确 harvest 到 registry，无新结果需要添加。

## π0.5 VLA-only 结果汇总

### 已 harvest 进 registry 的实验（8 个 DONE/success）

| exp_id | Suite | Seed | SR | JSON 源 |
|--------|-------|------|------|---------|
| eval-pi05-vla-only-spatial-s42 | spatial | 42 | **0.980** | bjb1-32546 (5/25) |
| eval-pi05-vla-only-spatial-s43 | spatial | 43 | **0.960** | bjb1-32546 (5/25) |
| eval-pi05-vla-only-spatial-s45 | spatial | 45 | **0.850** | bjb1-32546 (5/21) |
| eval-pi05-vla-only-object-s42 | object | 42 | **0.965** | bjb1-32546 (5/25) |
| eval-pi05-vla-only-object-s43 | object | 43 | **0.815** | bjb1-32546 (5/21) |
| eval-pi05-vla-only-object-s44 | object | 44 | **0.810** | bjb1-32546 (5/21) |
| eval-pi05-vla-only-goal-s42 | goal | 42 | **0.955** | bjb1-32546 (5/25) |
| eval-pi05-vla-only-goal-s43 | goal | 43 | **0.970** | bjb1-32546 (5/25) |

### 仍 QUEUED 但无独立结果的 v2 stub 条目（6 个）

object-s42-v2, object-s43-v2, goal-s42-v2, goal-s43-v2, spatial-s42-v2, spatial-s43-v2

- 创建于 2026-05-24T18:20Z（比对应非-v2 条目晚 3 分钟），从未进入 RUNNING 状态
- bjb1-32546 上的 May 25 JSON 已被非-v2 条目消费，v2 条目并无独立 JSON
- object-s43-v2 之前注解为 "INVALID OOM"

### bjb1-18228 上的 JSON（已映射到 -r4 系列）

bjb1-18228 的 6 个 JSON（5/22）映射到已 harvest 的 `eval-pi05-vla-only-{object,spatial}-seed{42,43,44}-r4` 条目（SR 完全匹配 1.0/0.985/0.995/0.98/0.975/0.985）。spatial-seed44 在 r4 系列被标 killed/无 metrics，但 r3/r4 系列已是历史归档，未列入当前需 harvest 范围。

### 结论

无需调用 update_registry——所有可 harvest 的 π0.5 VLA-only 结果已经在 registry 中。"上次 harvest 失败" 的实际状态：harvest 已成功完成，遗留的 6 个 v2 QUEUED 条目是重复 stub 而非未 harvest 结果。如需清理，可单独标记这 6 个 v2 条目为 superseded。

---
