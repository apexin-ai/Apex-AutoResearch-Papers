# ops eval pipeline edgecase

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-pipeline-edgecase_20260526T174910_result.json`
- **Structured JSON:** [`9c1de6970846ef197841.json`](../../sessions/9c/9c1de6970846ef197841.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/eval_pipeline_check_report.md`。

核心结论：**没有必须修复的问题，8 个 eval 命令可以一次跑通。**

3 个需注意的点：
1. 命令未指定 `--output_path`，结果按时间戳命名，需通过 JSON 内 `config.checkpoint` 字段反查对应实验。可考虑给每条命令加 `--output_path /root/occsafe_vla/artifacts/{exp_id}_eval.json`。
2. 输出 JSON 用 `tsr`/`car` 字段名，不是 `success_rate`/`collision_rate`，下游读取代码需匹配。
3. 训练仍在进行中，启动 eval 前必须确认 `--50000_chkpt` 目录已生成。

---
