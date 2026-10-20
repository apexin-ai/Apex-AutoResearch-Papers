# ops ckpt60 manual launch

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_ckpt60_manual_launch_20260514T222840_result.json`
- **Structured JSON:** [`80b01965f452687803da.json`](../../sessions/80/80b01965f452687803da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

- **PID**: 108025
- **GPU**: cuda:1，已确认占用 4450 MiB（模型加载中）
- **日志**: `/tmp/eval_lr5e6_ckpt60.log`
- **Registry**: `mvp2_eval_lr5e6_r1_ckpt60` 已更新为 RUNNING
- **Cron 监控**: 每 5 分钟自动检查进程状态

**脚本内容摘要**: `freige.eval.batch_eval`，评估 `/root/autodl-tmp/grpo_ced_lr5e6` 的 checkpoint-60，使用 SFT adapter，输出到 `/root/autodl-tmp/eval_results/lr5e6_r1_ckpt60`，启用 quantize。

---
