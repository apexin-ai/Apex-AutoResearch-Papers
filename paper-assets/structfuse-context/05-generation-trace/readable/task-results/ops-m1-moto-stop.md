# ops m1 moto stop

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_m1_moto_stop_20260516T025914_result.json`
- **Structured JSON:** [`ec9f235772150dad7aec.json`](../../sessions/ec/ec9f235772150dad7aec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

- **moto 重试循环已终止** — 杀掉了 batch_extract 主进程及其所有子进程（含 CodeQL java 进程），tmux session `m1_reextract_v2` 自动关闭
- **最终数据量**: `all.jsonl` = **44,173 行**，71/72 repos 完成，跳过 getmoto/moto（536 instances, ~1.2%）
- **Registry 已更新**: `m1_reextract_v2` → status=DONE, conclusion=success，metrics 记录了跳过 moto 的决策

注：registry notes 中提到 combine script 已就绪（`/root/structfuse/scripts/combine_m1_reextract.py`），如需合并数据可后续执行。

---
