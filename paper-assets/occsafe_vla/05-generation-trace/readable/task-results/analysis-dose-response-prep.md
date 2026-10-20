# analysis dose response prep

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_dose_response_prep_20260524T185531_result.json`
- **Structured JSON:** [`d99519d438d94f0df539.json`](../../sessions/d9/d99519d438d94f0df539.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。产出总结：

## 产出文件

| 文件 | 说明 |
|------|------|
| `dose_response_data.json` | 7 个 cutoff 条件 × 多 seed 的 CAR/TSR 原始数据 |
| `plot_dose_response.py` | 绘制 gradient flow duration → CAR 曲线（含误差带、reverse_cutoff 标注、vanilla baseline） |
| `factorial_2x2_config.json` | 2×2 设计（Flow×Norm）的 4 个 cell 配置与已有 metrics |
| `plot_factorial_2x2.py` | 绘制热力图 + 交互效应图 |

## 数据完整性

| 条件 | 已完成 seed | 缺失/正在跑 |
|------|------------|-------------|
| Detach (0 steps) | s0, s1, s2 ✓ | — |
| cutoff_15k | s0 ✓ | **s1 RUNNING** |
| cutoff_25k | s0, s1 ✓ | **s2 RUNNING** |
| cutoff_35k | s0, s1, s2 ✓ | — |
| cutoff_45k | s0 ✓ | **s1 RUNNING** |
| Full OCC (50K) | s0, s1, s2 ✓ | — |
| reverse_cutoff | s0, s1 ✓ | **s2 RUNNING** |
| Full OCC + LN (factorial) | — | **s0, s1, s2 全部 RUNNING** |

**关键发现预览**：dose-response 曲线呈现非单调模式——cutoff_15k (CAR=0.804) 高于 Full OCC 均值 (0.797)，而 cutoff_25k 出现严重"withdrawal effect"（均值 0.724，方差极大）。Early gradient flow (cutoff_15k=0.804) 远优于同等时长的 late gradient flow (reverse_cutoff=0.718)。待 RUNNING 实验完成后，直接运行脚本即可出图。

---
