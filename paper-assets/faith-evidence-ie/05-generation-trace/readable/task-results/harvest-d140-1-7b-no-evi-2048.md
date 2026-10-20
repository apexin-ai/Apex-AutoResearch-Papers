# harvest d140 1 7b no evi 2048

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_d140-1_7b-no-evi-2048_20260521T055943_result.json`
- **Structured JSON:** [`93b920c501a6a40c55fd.json`](../../sessions/93/93b920c501a6a40c55fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 不存在（可能已被清理）。收割完成。

## 结果：d140_1_7b_sft_s42_no_evi_2048 — **negative**

| 指标 | @1024 | @2048 | delta |
|------|-------|-------|-------|
| **ign_f1** | 0.3982 | **0.3925** | **-0.57pp** |
| truncated | 501 (50.9%) | 498 (50.6%) | -0.3pp |
| format_ok | 100% | 100% | — |
| predictions | — | 47,069 | — |
| inference_time | — | 7394s | — |

**关键发现：** 预期落空。@2048 不仅没提升，ign_f1 反而微降 0.57pp。截断率几乎不变（501→498），说明 1.7B no-evi 模型的截断输出绝大多数超过 2048 tokens，翻倍 budget 无法解决。模型本身生成控制能力不足，不是单纯的 budget 瓶颈。

Registry 已更新为 DONE/negative。

---
