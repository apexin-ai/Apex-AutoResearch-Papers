# ops check cuda3 status

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-cuda3-status_20260515T225716_result.json`
- **Structured JSON:** [`4daa85fa1bf4c6af80b2.json`](../../sessions/4d/4daa85fa1bf4c6af80b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

| Eval | PID | 状态 | 进度 |
|------|-----|------|------|
| **mvp2_eval_rsft_s44** | 261617 | **已死** | 停在 52% (32/62)，无错误输出、无结果文件 |
| **eval_dpo_1ep_fixed_r2** | 262080 | **运行中** | 50% (31/62)，已跑 ~59min，预计还需 ~58min |

**GPU 3**: 29764 MiB / 94% util — 只剩 DPO eval 一个进程在跑。

**mvp2_eval_rsft_s44 问题**: 进程在推理到 52% 时静默退出，日志无 Error/OOM/Traceback，也没有生成结果文件。两个 eval 同时跑在同一张卡上（各声明 90% 显存），大概率 OOM 被 kernel 杀掉。需要等 DPO eval 跑完后重新提交 rsft_s44。

---
