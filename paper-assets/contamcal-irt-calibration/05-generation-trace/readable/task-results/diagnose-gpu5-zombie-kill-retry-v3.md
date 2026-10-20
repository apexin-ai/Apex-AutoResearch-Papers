# diagnose gpu5 zombie kill retry v3

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gpu5_zombie_kill_retry_v3_20260513T235308_result.json`
- **Structured JSON:** [`11cd75f785bc7dac30f9.json`](../../sessions/11/11cd75f785bc7dac30f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

v3 训练成功启动并稳定运行。

**报告：**

| 项目 | 结果 |
|------|------|
| **PID 235248** | `train_sft.py` (d100 训练)，在 **GPU 0** 上运行（CUDA_VISIBLE_DEVICES=0），运行 ~14 分钟，占 21986 MiB。**不在 GPU 5 上**。 |
| **GPU 5 实际残留** | PID 237875（`evaluate.py`，占 8948 MiB），已 kill 清理 |
| **v3 首次提交** | OOM（第一次提交和 kill 之间可能有竞态条件，GPU 内存未完全释放） |
| **v3 第二次提交** | 成功启动。PID 239734，GPU 5 占 21986 MiB，25/3177 步，~1.2s/it，预计约 1 小时完成 |

---
