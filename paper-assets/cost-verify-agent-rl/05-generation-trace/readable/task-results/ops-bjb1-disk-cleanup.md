# ops bjb1 disk cleanup

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb1_disk_cleanup_20260522T144205_result.json`
- **Structured JSON:** [`8aa7fa0d080159c322e7.json`](../../sessions/8a/8aa7fa0d080159c322e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 清理结果

| 指标 | 值 |
|------|-----|
| 清理前 | 250GB / 250GB (100%, 0 可用) |
| 清理后 | 208GB / 250GB (83%, **43GB 可用**) |
| 释放量 | **~42GB** |

### 已删除
| 目标 | 大小 |
|------|------|
| `scienceworld-cell-c-v5/` | 35GB |
| `qwen3_scienceworld_sft/` | 7.6GB |
| `scienceworld_sft/` | 7.6GB |（发现额外的 scienceworld SFT 目录）|
| `scienceworld-cell-c-v4/` | 0GB |
| `__pycache__` 目录 | 微量 |

### 跳过（不存在）
- 8b/v9d checkpoints — 无匹配目录
- `.cache` 目录 — 不存在
- 日志 >100MB — 无（最大 2.5MB）

### 未达 50GB 目标

差约 7GB。下一步可选候选：
- `.hf_cache/models--dunzhang--stella_en_1.5B_v5/` — **17GB**（embedding 模型，删除后可达 60GB 可用）

需要 Director 确认是否删除该 HF 缓存模型。

---
