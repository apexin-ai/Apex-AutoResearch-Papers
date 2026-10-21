# ops westd disk cleanup urgent

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-disk-cleanup-urgent_20260522T135337_result.json`
- **Structured JSON:** [`2077915cec8cd5f3c550.json`](../../sessions/20/2077915cec8cd5f3c550.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

## 结果

| 项目 | 详情 |
|------|------|
| **清理前** | 2.4GB 可用 (100%) |
| **清理后** | **17GB 可用 (94%)** |
| **释放空间** | ~14.6GB |
| **目标 10GB** | **已达成** |

**删除内容：**
- `/root/autodl-tmp/.hf_cache/Falcon3-7B-Base/` — 14GB（Falcon3 eval 全部完成，基模型缓存不再需要）
- pip cache — 14 个缓存文件

**Yi-1.5-9B 训练状态：**
- PID 636899，GPU 0，46GB VRAM
- Step 662/3125（21%），~4s/it，预计剩余约 2.7 小时
- 运行正常，checkpoint 保存空间充足

---
