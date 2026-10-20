# infra download check and fix

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_download-check-and-fix_20260519T184720_result.json`
- **Structured JSON:** [`1180b37dacbc75e1dac5.json`](../../sessions/11/1180b37dacbc75e1dac5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载稳定在 19% (12:30 elapsed)，预计还需约 50 分钟。下载进程 (PID 25295) 健康运行中，无需继续紧密监控。

---

## 最终报告

### 1. Qwen3 状态: **已切换 4B，下载进行中**
- **Qwen3-8B**: 5 个 shard 文件全部存在但文件内容不完整（safetensors 反序列化报错 `incomplete metadata`）。已清理 temp 目录释放 7.5G。损坏的 8B 主目录文件仍保留在 `/root/autodl-tmp/models/Qwen/Qwen3-8B/`
- **Qwen3-4B**: 下载中 (PID 25295)
  - `model-00003-of-00003.safetensors` (95M) ✅ 已完成
  - `model-00001-of-00003.safetensors`: 19%/3.69G (~1 MB/s)
  - `model-00002-of-00003.safetensors`: 18%/3.71G (~1 MB/s)
  - **预计完成时间**: ~50 分钟后
  - 路径: `/root/autodl-tmp/models/Qwen/Qwen3-4B`
  - 日志: `/tmp/download_qwen3_4b.log`
- **下载完成后需要运行验证** (手动或下一轮 Worker 执行)

### 2. RLDS 状态: ✅ **全部完成**
| Suite | 文件数 | 大小 |
|-------|--------|------|
| libero_spatial_no_noops | 16 | 1.8G |
| libero_object_no_noops | 32 | 2.7G |
| libero_goal_no_noops | 16 | 1.8G |
| libero_10_no_noops | 32 | 3.4G |
| **总计** | **96** | **9.6G** |

### 3. Embedding 修复状态: ✅ **APPLIED**
`diversity_metrics.py` 已包含双 embedding 体系：
- Primary: `compute_openvla_embedding_metrics()` — SigLIP text encoder (`/root/autodl-tmp/siglip-base-local`)
- Reference: `compute_minilm_embedding_metrics()` — MiniLM `all-MiniLM-L6-v2`

### 4. 磁盘
```
/root/autodl-tmp: 70G used / 350G total (20%), 281G free
├── LIBERO-datasets:       28G
├── openvla-7b:            15G
├── models (Qwen 8B+4B):  12G  (4B 完成后 ~20G)
├── modified_libero_rlds:  9.6G
└── siglip-base:           1.6G
```

---
