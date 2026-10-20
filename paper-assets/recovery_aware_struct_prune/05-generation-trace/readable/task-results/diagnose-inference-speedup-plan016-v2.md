# diagnose inference speedup plan016 v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_inference_speedup_plan016_v2_20260516T222412_result.json`
- **Structured JSON:** [`a4ab3d12f7b962a09e66.json`](../../sessions/a4/a4ab3d12f7b962a09e66.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**结论：实验 v2 没有失败，是 cron 监控误判。**

- 脚本 `benchmark_inference.py` 已正确使用 `load_pruned_model()` 加载非均匀剪枝模型，三个模型全部跑完
- 结果已写入 `inference_benchmark.json`（rasp_20: 52.07 tok/s, 28.5% 内存节省）
- 但脚本没有任何 W&B 集成，cron 检测不到 metrics 就判定 failed

报告已写入两处：
- 服务器：`/root/autodl-tmp/recovery_aware_struct_prune/artifacts/diagnosis_inference_v2.md`
- 本地：`artifacts/diagnosis_inference_v2.md`

---
