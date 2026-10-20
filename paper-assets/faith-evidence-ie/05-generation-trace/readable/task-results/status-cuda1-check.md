# status cuda1 check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_cuda1_check_20260516T145501_result.json`
- **Structured JSON:** [`f2aa179dd3efa9371e94.json`](../../sessions/f2/f2aa179dd3efa9371e94.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

That's a single JSON array file. The progress shows 64 completed doc_ids and 512 generation lines (likely 8 candidates per doc: 64×8=512).

## 汇报

| 实验 | PID | 状态 | 详情 |
|------|-----|------|------|
| **plan_016_llama_rsft_candidates_r2** | 353179 | **DEAD** | 进程已退出。已生成 512 行 (64 docs × 8 candidates/doc)。progress.json 记录 64 个 completed_doc_ids。DocRED dev 约 998 docs → 进度约 **6.4%**，提前终止。 |
| **plan_014_no_evidence_eval_d076** | 353322 | **ALIVE** | 运行中 30min，GPU 1 占用 10,288 MiB。输出目录尚无结果文件（推理还未完成写出）。 |

**需要关注：**
- plan_016 (PID 353179) 已死但只完成 6.4%，需要排查退出原因（可能 OOM 或代码错误）并决定是否重启。
- plan_014 正常运行中，等待完成后检查结果。

---
