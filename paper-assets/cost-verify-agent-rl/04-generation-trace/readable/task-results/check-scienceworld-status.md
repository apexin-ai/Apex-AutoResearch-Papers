# check scienceworld status

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_scienceworld_status_20260519T141628_result.json`
- **Structured JSON:** [`adc20b68e13e3bb92089.json`](../../sessions/ad/adc20b68e13e3bb92089.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/scienceworld_extraction_status_20260519.md`。

**核心结论：**

| 项目 | 状态 |
|------|------|
| PID 19201 / 51279 | 仍在跑，但**可以 kill** |
| 完整数据 | `scienceworld_sft_train.jsonl` (3592条) + `scienceworld_sft_val.jsonl` (1796条) — **30个任务全覆盖，0错误** |
| 成功轨迹 | train 2994 + val 1544 = **4538 条 score=100 轨迹** |
| SFT 可用性 | **直接可用**，过滤 `metadata.success == true` 即可 |

两个在跑的进程是冗余的（只覆盖前25个任务的子集），且因同时写同一文件导致输出有损坏。建议 kill 掉并删除 `*_partial.jsonl`。

---
