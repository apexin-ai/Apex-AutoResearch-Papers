# diag exp044b 028b progress

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp044b-028b-progress_20260518T222746_result.json`
- **Structured JSON:** [`75bd09948de272b8b8e9.json`](../../sessions/75/75bd09948de272b8b8e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总 (截至 2026-05-19 06:28 UTC)

| 实验 | 进度 | 已用时间 | 预估剩余 | 预计完成 | 状态 |
|------|------|----------|----------|----------|------|
| **exp-044b** (ICL Oracle, cuda:0) | 161/199 | ~2h 8min | **~31 min** | ~07:00 UTC | 正常 |
| **exp-028b** (Qwen3-14B thinking, cuda:3) | 43/204 | ~1h 47min | **~412 min (~6.9h)** | ~13:20 UTC | 正常 |
| **exp-046** (Mistral pw600, cuda:2) | 266/600 | ~2h 11min | **~162 min (~2.7h)** | ~09:10 UTC | 正常 |

### 关键细节

- **exp-044b**: avg 48.0s/prob，即将完成（还剩 39 题）
- **exp-028b**: avg 152.7s/prob（thinking mode 导致每题耗时长，单题 trace+extract ~221s），进度较慢，预计还需近 7 小时
- **exp-046**: avg 29.0s/prob，稳定运行，600 题规模较大

### GPU 状态
4x NVIDIA RTX PRO 6000 Blackwell (96GB)，全部 96-97% 利用率，内存占用 ~88/97GB。满负荷运行，无空闲。

---
