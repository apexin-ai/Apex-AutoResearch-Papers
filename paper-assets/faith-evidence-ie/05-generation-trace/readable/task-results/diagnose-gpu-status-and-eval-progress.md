# diagnose gpu status and eval progress

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gpu-status-and-eval-progress_20260523T014341_result.json`
- **Structured JSON:** [`5cb8046f29ceb06c18dc.json`](../../sessions/5c/5cb8046f29ceb06c18dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态

| GPU | 利用率 | 显存占用 | PID | 任务 |
|-----|--------|---------|-----|------|
| 0 | 95% | 26.8 / 95.6 GB | 212762 | 8B s43 with-evi eval |
| 1 | 80% | 32.5 / 95.6 GB | 194682 | 14B s43 generation |
| 2 | 94% | 21.3 / 95.6 GB | 213753 | 4B s43 with-evi eval |
| 3 | 43% | 6.1 / 95.6 GB | 214028 | 1.7B s43 with-evi eval |

## Eval 进度

| Eval | PID | 运行时间 | 进度 | 预估剩余 |
|------|-----|---------|------|---------|
| **8B s43 with-evi** | 212762 | 53min | 31/32 batches (97%) | ~1min |
| **4B s43 with-evi** | 213753 | 36min | 16/32 batches (50%) | ~35min |
| **1.7B s43 with-evi** | 214028 | 35min | 47/500 docs (9.4%) | ~5.5h |
| **14B s43 generation** | 194682 | 7h27m | 1280/3027 (42%) | ~10h |

**备注**：
- 8B eval 即将完成（剩最后 1 个 batch）
- 4B eval 进度一半，batch 粒度推理（32 batches），约 35 min 完成
- 1.7B eval 用 doc 粒度推理（500 docs），速度 ~45s/doc，预估还需 ~5.5h
- 14B generation 40% 完成，~20s/sample，预估还需 ~10h
- 三个 eval 输出目录（`test_eval_*_rsft_s43_with_evi/`）暂无 predictions jsonl，结果可能在最后一次性写入

---
