# analysis d112 rsft no evidence eval r3

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d112_rsft_no_evidence_eval_r3_20260519T182405_result.json`
- **Structured JSON:** [`788117272370a3950b32.json`](../../sessions/78/788117272370a3950b32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果摘要：**

| 指标 | 值 |
|------|-----|
| ign_f1 | **0.5246** |
| f1 | 0.5341 |
| evidence tax | **+0.94pp**（移除 evidence 后 RE 提升） |
| format_ok | 983/985 (99.8%) |
| truncated | 144/985 (14.6%) |

**核心发现**：4B RSFT 存在近 1pp 的 evidence tax — 生成 evidence 会拖累 RE 性能。与 8B（evidence 有微弱 bonus，-0.78pp）形成对比，呈现 scale-dependent 趋势：

| Scale | With-evi | No-evi | Tax |
|-------|----------|--------|-----|
| 4B | 0.5152 | 0.5246 | +0.94pp |
| 8B | 0.5414 | 0.5336 | -0.78pp |

报告已注册：`art_20260519_6ccf9c`

---
