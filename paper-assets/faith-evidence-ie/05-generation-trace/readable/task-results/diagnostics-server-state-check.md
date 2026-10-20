# diagnostics server state check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnostics_server-state-check_20260522T013735_result.json`
- **Structured JSON:** [`78e73c9da57842844661.json`](../../sessions/78/78e73c9da57842844661.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/server_state_20260522.md`。

**关键发现：**

| GPU | 状态 | 实验 |
|-----|------|------|
| 0 | 占用 6GB | test_eval_1_7b_sft_s42 (PID 140534, 运行2h47m) |
| 1 | 占用 6GB | test_eval_1_7b_sft_s42_no_evi (PID 147596, 185/500=37%) |
| 2 | **空闲** | — |
| 3 | 占用 32GB | test_eval_14b_sft_s42_no_evi (PID 143166, 221/500=44%) |

**已完成 9 个 test_eval**，F1 排序：14B SFT (0.389) > 14B RSFT (0.385) > Llama RSFT (0.360) > Llama SFT (0.342) > 8B RSFT (0.335) > 8B SFT (0.311) > 1.7B RSFT (0.293) > 4B RSFT (0.250) > 4B SFT (0.223)

**需要处理：**
- 7 个旧 PID 已死，6 个正常完成可清理 registry
- PID 151217 (test_eval_4b_rsft_s42_v3) 失败，输出目录为空，需重跑
- GPU 2 空闲可用

---
