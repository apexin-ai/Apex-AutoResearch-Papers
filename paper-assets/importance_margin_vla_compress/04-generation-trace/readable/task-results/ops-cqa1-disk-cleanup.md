# ops cqa1 disk cleanup

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1_disk_cleanup_20260517T091712_result.json`
- **Structured JSON:** [`7fbaee3c802ad7b209c1.json`](../../sessions/7f/7fbaee3c802ad7b209c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 清理报告

| 指标 | 清理前 | 清理后 |
|------|--------|--------|
| 已用 | 217G | 184G |
| 可用 | 34G | **67G** |
| 使用率 | 87% | 74% |

**已删除：**
- `libero_imm_twostage_fullft/` — 17G
- `libero_imm_twostage_fullft_k07/` — 17G
- 共释放 **~33G**

**剩余 checkpoint 目录：**
| 目录 | 大小 | 备注 |
|------|------|------|
| libero_acis_stage1only_k03 | 1.8G | 保留 |
| libero_acis_stage1only_k07 | 1.8G | 保留 |
| libero_baseline | 8.7G | 保留 |
| libero_baseline_seed0 | 8.7G | 保留 |
| libero_full_ft | 13G | baseline，保留 |
| libero_full_ft_seed0 | 13G | 保留 |
| libero_full_ft_seed1 | 13G | 保留 |
| libero_fullft_batch64 | 0 | 空目录 |
| libero_imm_twostage_fullft_seed0 | 17G | **未删，待确认** |

---

**待确认：** `libero_imm_twostage_fullft_seed0/` (17G) 是同一失败 twostage 实验的 seed0 run。如果也确认无用，删除后可用空间将达 ~84G。是否删除？

---
