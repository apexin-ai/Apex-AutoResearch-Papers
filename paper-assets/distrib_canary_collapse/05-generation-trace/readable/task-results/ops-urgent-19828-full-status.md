# ops urgent 19828 full status

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-19828-full-status_20260523T123733_result.json`
- **Structured JSON:** [`73014c26394bb5f605d6.json`](../../sessions/73/73014c26394bb5f605d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### GPU 状态
| GPU | 显存占用 | 利用率 | PID | 实验 |
|-----|---------|--------|-----|------|
| 0 | 27727/97887 MiB | 98% | 857058 | t15_a075_s43_fp32_14b |
| 1 | 27727/97887 MiB | 96% | 865472 | t10_a075_s44_fp32_14b |

两张 GPU 满载运行中。

### 运行中实验进度
| 实验 | 已完成 gen | 当前 gen | 总 gen 数 | 进度 |
|------|-----------|---------|----------|------|
| t15_a075_s43_fp32_14b (cuda:0) | gen_0~4 | gen_5 训练中 | 16 (gen_0~15) | **5/16 ≈ 31%** |
| t10_a075_s44_fp32_14b (cuda:1) | gen_0~2 | gen_3 训练中 | 11 (gen_0~10) | **3/11 ≈ 27%** |

（gen_5 和 gen_3 目录已有 synthetic_data + trainer 但无 metrics.json，说明正在训练阶段）

### 已完成实验（EXIT_CODE=0）
| 实验 | gen 数 | all_metrics.json | 需 D102？ |
|------|--------|-----------------|----------|
| t15_a075_s42_fp32_14b | 16 (gen_0~15) | ✅ 有 | **需检查是否已 D102** |
| t10_a050_s42_fp32_14b | 11 (gen_0~10) | ❌ 只有 .bak | **需检查是否已 D102** |
| t15_a045_s42_fp32 | 有 top-level all_metrics | ✅ 有 | 需检查 |
| t25_a075_s42_fp32 | 有 top-level all_metrics | ✅ 有 | 需检查 |
| t20_a045_s43_fp32 | 有 top-level all_metrics | ✅ 有 | 需检查 |
| t25_a075_s43_fp32 | 有 top-level all_metrics | ✅ 有 | 需检查 |
| t10_a050_s43_fp32 | 有 top-level all_metrics | ✅ 有 | 需检查 |

### 17855 迁移检查
- t15_a050_s43、t15_a045_s43、t15_a060_s43 目录均**不存在**于 19828 上，未迁移。

### 磁盘
- **/root/autodl-tmp/**: 250G 总量，已用 167G，**剩余 84G (33%)**

---
