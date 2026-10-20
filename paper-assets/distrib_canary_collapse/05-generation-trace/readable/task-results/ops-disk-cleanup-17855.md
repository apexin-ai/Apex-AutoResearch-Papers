# ops disk cleanup 17855

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-cleanup-17855_20260522T201944_result.json`
- **Structured JSON:** [`5041664fbb66c6b5e7aa.json`](../../sessions/50/5041664fbb66c6b5e7aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 清理前
- 17855 磁盘: 93% (27GB 剩余)

## 清理详情

| 目录 | 清理前 | 清理后 | 释放 |
|------|-------|-------|------|
| scale/14b_c4_s42_fp32 gen_9 | 5.3G | 9.6M | ~5.3G |
| phase_diagram/t10_a060_s42_fp32_14b gen_9 | 5.3G | 11M | ~5.3G |
| phase_diagram/t10_a075_s42_fp32_14b gen_9 | 5.3G | 11M | ~5.3G |
| phase_diagram_14b/ | 不存在 | — | 0 |
| **合计** | | | **~15.9G** |

gen_1-gen_8 已经是小文件（~7M，之前已清理过），只有 gen_9 有模型残留。

## 清理后
- 17855 磁盘: 88% (43GB 剩余)
- 目标 ≥80GB: **✗**（差 ~37GB）

## 19828 磁盘
- 54% (116GB 剩余)

---

**未达标原因分析**：4 个 14b 实验正在运行（t10_a045, t15_a045/a050/a060），各占 ~11G，每个保留了 2 个 gen 的 5.3G 模型文件。可安全清理每个实验中较旧的 gen checkpoint，预计再释放 ~21G（→64GB）。仍不够 80G。

大空间占用：

| 目录 | 大小 | 说明 |
|------|------|------|
| .hf_cache | 41G | 模型缓存 |
| scale_check/pythia69b | 26G | 6.9B 实验 |
| generalize/smollm3_3b | 24G | 3B 实验 |
| intervention/predictive_te_14b | 11G | 14b 干预实验 |

需要 Director 决定是否额外清理这些目录或运行中实验的旧 checkpoint。

---
