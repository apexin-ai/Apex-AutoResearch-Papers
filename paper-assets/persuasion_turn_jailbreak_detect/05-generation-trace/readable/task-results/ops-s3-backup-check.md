# ops s3 backup check

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_s3-backup-check_20260523T093820_result.json`
- **Structured JSON:** [`51bc2fc15f92348c8ffe.json`](../../sessions/51/51bc2fc15f92348c8ffe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 磁盘占用清单

**总大小：5.5G**

### 各目录大小（降序）

| 目录 | 大小 | 备注 |
|------|------|------|
| `checkpoints/` | **5.0G** | 占总量 91% |
| `data/` | **538M** | 占总量 9.5% |
| `results/` | 13M | |
| `figures/` | 1.1M | |
| `paper/` | 1.3M | |
| `logs/` | 1.2M | |
| `scripts/` | 2.1M | |
| `src/` | 876K | |
| `docs/` | 24K | |
| `artifacts/` | 12K | |

无 `.git/` 目录。根目录无大型模型文件。

### checkpoints 细分

| 子目录 | 大小 |
|--------|------|
| `exp27_mean_pooling/` | **2.1G** |
| `exp59_seed42/` | 721M |
| `exp59_seed123/` | 721M |
| `exp59_seed456/` | 721M |
| `plan_016v2_topic/` | 710M |
| `exp26_frozen_seed*` (×3) | 各 12M |
| `exp36_frozen_mlm_seed*` (×3) | 各 12M |

### data 细分（较大的）

| 子目录 | 大小 |
|--------|------|
| `plan_002_splits/` | 85M |
| `generated/` | 44M |
| `exp59_resample/` | 41M |
| `expanded_*/` (×2) | 各 21M |
| `mhj/` | 21M |
| `exp61_partition_seed*` (×10) | 各 9M |

### 备份瘦身建议

- **排除 `checkpoints/`** 可省 5.0G（91%），备份体积降到 ~500M
- 如只保留最终模型，可只留 `exp59_seed*`（3×721M）和 `plan_016v2_topic`（710M），删掉 `exp27_mean_pooling`（2.1G）
- `data/` 中 `exp61_partition_seed*` 有 10 个 seed 共 90M，如果可以重新生成也可排除

---
