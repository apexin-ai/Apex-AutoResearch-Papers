# infra disk cleanup and deberta check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_disk-cleanup-and-deberta-check_20260522T171957_result.json`
- **Structured JSON:** [`c3fd0f2cc477a18bc4c9.json`](../../sessions/c3/c3fd0f2cc477a18bc4c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

| 项目 | 状态 |
|------|------|
| **DeBERTa 训练** | 原进程 643576 已死（磁盘满时保存 checkpoint 崩溃）。已重启为 PID 650581，正常训练中（61/21820 步，~3.5 it/s，预计 ~1h45m 完成）。output-dir 已改到数据盘 `/root/autodl-tmp/` |
| **根分区清理** | 清理前 20G/30G (67%) → 清理后 11G/30G (34%)，释放 ~9G。删除了：dry-run 产物 6.1G、损坏 checkpoint 2.2G、HF cache 1.6G |
| **LLaMA FOLIO seed=789** | 189/204 intermediates 已保存在根分区，差 15 个。结果可恢复（需补跑剩余 15 条） |
| **崩溃实验恢复** | LLaMA PW 只有 seed42，缺 seed456/seed789。FOLIO seed=789 差 15 条。这些需要在 DeBERTa 训练完成后、有 GPU 空闲时补跑 |

---
