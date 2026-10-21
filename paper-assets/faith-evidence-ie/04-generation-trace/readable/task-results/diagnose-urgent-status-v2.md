# diagnose urgent status v2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_urgent-status-v2_20260520T111916_result.json`
- **Structured JSON:** [`44d3c11d5293806a006b.json`](../../sessions/44/44d3c11d5293806a006b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 迁移状态汇总

| 项目 | 状态 |
|------|------|
| **磁盘** | 86G / 350G 已用（25%），剩余 265G，充裕 |
| **Llama-3.1-8B** | 4 shards 全齐 — shard3 = **4.6G** ✅ ≥4G |
| **Llama-3.1-8B-Instruct** | 不存在 |
| **Qwen3-14B** | 8/8 shards，28G，完整 ✅ |
| **14B adapter** | ❌ 缺失 |
| **14B generations** | ❌ 缺失 |
| **8B SFT adapter** | ❌ 缺失 |
| **Milestone A** | `MILESTONE_A_READY` ✅ |
| **传输进程** | 无活跃 rsync/scp（ps 命令格式报错，但 milestone 已 ready 且无新文件写入） |
| **GPU** | 0,1 空闲（0 MiB）；2,3 利用率 100% 但显存 0 MiB（可能刚释放或驱动状态延迟） |

**结论**：基座模型（8B + 14B）就绪，可以开始 8B 实验。14B 的 adapter 和 generations 未迁移，8B SFT adapter 也缺失——如果实验依赖这些产物需要先补传。GPU 0/1 可用。

---
