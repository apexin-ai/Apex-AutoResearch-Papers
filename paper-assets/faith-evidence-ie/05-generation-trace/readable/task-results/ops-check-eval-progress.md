# ops check eval progress

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-eval-progress_20260515T113109_result.json`
- **Structured JSON:** [`2646261636e1fd6a3338.json`](../../sessions/26/2646261636e1fd6a3338.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/eval_progress_check_0515.md`。

**摘要：**

| 实验 | 进度 | ETA |
|------|------|-----|
| rsft_r1 | ✅ 完成 | F1=0.4449 (比 s44 低 2pp) |
| rsft_r2a | 88% (109/124) | ~12 min |
| rsft_r2b | 89% (110/124) | ~11 min |
| ced_reranker_poc | 60% (591/985) | ~2.5h |

**s43 eval 命令已准备好**，参数基于 s44 成功 config 确认（`--model_path` / `--sft_adapter` / `--data_path` / `--no-quantize`）。建议用 GPU 2（rsft_r1 已完成），但需先检查是否有残留进程占显存。

**异常：** GPU 2 显示 11.9GB 显存占用但 rsft_r1 PID 已死，提交 s43 前需 `nvidia-smi --query-compute-apps=pid` 检查并 kill 残留。

---
