# urgent westd38929 deep disk cleanup

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_urgent_westd38929_deep_disk_cleanup_20260525T141628_result.json`
- **Structured JSON:** [`fe8b8c154143d268734c.json`](../../sessions/fe/fe8b8c154143d268734c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

76G 已远超 40G 目标。清理完成。

**结果：**
- 删除了 `datasets/parquet/` (66G 的 HF datasets arrow 缓存，含两份 LIBERO 副本)
- 删除了 4 个 stale `.lock` 文件
- 可用空间：11G → **76G** (释放 65G)

**未触碰的内容：**
- `eval_results/` — 无
- `models/` — 完整保留 (51G)
- `lerobot/hub/` — 保留 LIBERO 原始数据集 (33G，训练需要)
- 所有 openvla/openvla-oft baseline 模型目录 — 保留
- 项目代码 — 保留

---
