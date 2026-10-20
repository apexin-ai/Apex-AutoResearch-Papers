# ops westd cqa1 status check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-cqa1-status-check_20260520T033012_result.json`
- **Structured JSON:** [`f302311da2ba3efc09d5.json`](../../sessions/f3/f302311da2ba3efc09d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐全了。汇总结果：

## 实验状态汇总

### westd-29999 (4× RTX PRO 6000 Blackwell 96GB)

| GPU | 实验 | PID | 状态 | 进度 | ETA |
|-----|------|-----|------|------|-----|
| cuda:0 (75%, 58/98GB) | Phi-4 s0 sweep | 265121 | **still_running** | d000 训练中, 451/3125 (14%), ~2.4s/it | ~1h45m |
| cuda:1 (81%, 62/98GB) | Qwen-14B d100_s123 retrain | 246779 | **still_running** | 1905/4159 (46%), ~2.9s/it | ~1h50m |
| cuda:2 (95%, 67/98GB) | OLMo-2 s0 sweep | 261133 | **still_running** | d000 已完成(checkpoint-3125), d005 训练中 ~40-45% | ~1h |
| cuda:3 (90%, 95/98GB) | Gemma-2 d100_s123 retrain | 246861 | **still_running** | 1956/4159 (47%), ~3.0s/it | ~1h50m |
| CPU | IRT fitting MMLU v3 | 265452 | **crashed** | fitting 完成但保存失败 | — |

### cqa1-21977 (1× RTX 4090D 24GB)

| GPU | 实验 | PID | 状态 | 进度 | ETA |
|-----|------|-----|------|------|-----|
| cuda:0 (33%, 21/25GB) | Qwen-7B s0 sweep | 313418 | **still_running** | d000 训练中, ~24% (761/3125), ~4.3s/it | ~2h45m |

### IRT fitting 详情

两次运行（原始 + rerun）的 2PL+γ fitting 均在 25 respondents × 14042 items 上**成功完成**，但都在保存 trace 时崩溃：
- 第一次: `AttributeError: module 'arviz' has no attribute 'to_netcdf'`
- 第二次（rerun）: `ValueError: cannot write NetCDF files ... none of the suitable backend libraries (netCDF4, h5netcdf) are installed`

Fitting 控制台输出的关键结果：
- **mean(γ) = 0.0256 ± 0.3587, median(γ) = 0.0778**
- **57.8% items with γ > 0**
- `/root/contamcal-irt-calibration/analysis/irt_results/mmlu_v3/` 目录为空，无文件落盘

**修复方案**: westd 上 `pip install h5netcdf` 后重跑即可。

### 磁盘

| 服务器 | 根分区 | 数据盘 |
|--------|--------|--------|
| westd | 1.4/30G (5%) | 192/250G (77%) |
| cqa1 | 19/30G (64%) | 121/169G (72%) |

### 结论
- 4 个 GPU 训练全部 **still_running**，registry 误标 failed 确认是假阳性
- IRT fitting 需要装 h5netcdf 后重跑保存步骤（fitting 已完成，只差落盘）
- cqa1 根分区 64% 偏高，需关注

---
