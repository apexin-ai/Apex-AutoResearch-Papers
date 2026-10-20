# infra westd gpu status

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd-gpu-status_20260517T094813_result.json`
- **Structured JSON:** [`6268e7284ffc66265c17.json`](../../sessions/62/6268e7284ffc66265c17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/westd_gpu_report.md`。

## 总结

**westd-11672 全部 4 GPU 满载运行：**

| GPU | 任务 | 进度 | 预计完成 |
|-----|------|------|----------|
| 0 | eval_math500_unpruned | 357/500 (71%), acc=0.734 | ~19:00 今天 |
| 1 | eval_math500_grpo_standard_20 | 9/500 (2%) | ~07:00 明天 |
| 2 | eval_math500_sft_standard_20 | 484/500 (97%), acc=0.251 | ~18:00 今天（10-15分钟内） |
| 3 | eval_math500_grpo_rasp_20_v2 | 55/500 (11%), acc=0.340 | ~03:30 明天 |

**已完成结果**: eval_math500_sft_rasp_20 → accuracy **0.242**

**空闲 GPU**: 无。GPU 2 约 10-15 分钟后释放，GPU 0 约 70 分钟后释放。GRPO eval（GPU 1/3）因生成长度极大，需过夜运行。

**磁盘**: 根分区 18%，数据盘 3%，状态健康。

---
