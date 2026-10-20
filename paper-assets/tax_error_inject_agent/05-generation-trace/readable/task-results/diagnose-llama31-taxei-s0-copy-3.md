# diagnose llama31 taxei s0

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_llama31-taxei-s0_20260516T115604_result.json`
- **Structured JSON:** [`eea90160e4c794ed3d8d.json`](../../sessions/ee/eea90160e4c794ed3d8d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 不支持将 conclusion 清回 null。当前状态矛盾无法通过 API 修复（status=RUNNING + conclusion=failed）。

## 诊断结论：**RUNNING** ✓

| 指标 | 值 |
|------|-----|
| 进度 | step 2548/3387 (75%), epoch ~2.25/3 |
| 运行时间 | 1h38m |
| loss | ~0.32 |
| token_acc | ~0.88 |
| GPU 利用率 | cuda:1, 26GB/32GB, 99% util |
| checkpoint | 2个已保存 (v0, v1) |
| 预计完成 | ~32 分钟后 |

**失败标记原因**：`reproduce.finished_at` 在 10:20:07 被设置，触发了 on_failed hook。但进程实际从未中断——可能是监控脚本误判（提交时间 09:15，10:20 时训练约 1h 处于正常状态）。

**Registry 问题**：conclusion 字段不支持 null 值，无法清除误报的 `failed` 标记。训练完成后会自然更新为 `success`/需要手动更新。建议训练结束后直接 `update_registry conclusion=success`。

---
