# ssh status check loop4

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_status-check-loop4_20260514T230444_result.json`
- **Structured JSON:** [`157ecc8e1d462ba8576e.json`](../../sessions/15/157ecc8e1d462ba8576e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

状态报告已写入 `artifacts/status_check_loop4.md`。

**总结**：4 个进程全部存活。

| 任务 | 进度 | ETA |
|------|------|-----|
| GRPO 训练 lr5e6_r1 | **113/200 (56.5%)** | ~2h40m |
| ckpt-40 eval r2 | **60/62 (97%)** | **~3min** |
| ckpt-60 eval r2 | 23/62 (37%) | ~60min |
| SFT baseline eval | ~65% (估) | ~36min |

**关键发现**：
- ckpt-40 eval 即将完成 (60/62)，结果将写入 `/root/autodl-tmp/eval_results/lr5e6_r1_ckpt40/checkpoint-40/`
- 已完成的 ckpt-20 eval 结果很差：**F1=0.008**，关系抽取能力崩溃，但 EDCR=0.99 证据质量高
- GRPO 训练 KL divergence 多次爆炸至 7e13（monitoring-only）
- SFT baseline eval 无日志可追踪（脚本启动未重定向）

---
