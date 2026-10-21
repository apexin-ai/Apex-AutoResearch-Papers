# check bootstrap v2 status

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bootstrap_v2_status_20260523T012502_result.json`
- **Structured JSON:** [`aff50d10d6a2caf3a4b0.json`](../../sessions/af/aff50d10d6a2caf3a4b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Bootstrap v2 进度

**完成：2/20 结果文件**（仅 `bootstrap_r2/` 下 2 个子目录：`openvla_goal/`, `tracvla_goal/`）

**GPU 状态：**
| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 0% | 2135/97887 MiB |
| 1 | 55% | 12621/97887 MiB |

**当前进度：**
- **cuda0**：第3个模型，提取完成（5000/5000），正在 RidgeCV 拟合（GPU 空闲因为是 CPU 计算）
- **cuda1**：第3个模型，提取中 900/5000（~18%），每50样本约17秒

**已完成 JSON 内容：**

### 1. OpenVLA goal (trained)
| 指标 | 值 |
|------|-----|
| peak_r2 | **0.4556** (L1) |
| exit_r2 | 0.3395 (L31) |
| delta (peak−exit) | 0.116 |
| delta 95% CI | **[−0.2528, −0.0117]** |
| bootstrap mean delta | −0.1417 ± 0.0647 |

R² 曲线：L1 峰值后缓降，L27 低谷(0.2776)，L28-30 小幅回弹。

### 2. TracVLA goal (trained)
| 指标 | 值 |
|------|-----|
| peak_r2 | **0.5399** (L13) |
| exit_r2 | 0.2065 (L31) |
| delta (peak−exit) | 0.3334 |
| delta 95% CI | **[0.0546, 0.3416]** |
| bootstrap mean delta | 0.1671 ± 0.0733 |

R² 曲线：中层（L2-L14）高原，后层急剧下降（L28 转负至 −0.46），L31 微回弹。

**预估剩余时间：** 每个配置约10-12分钟（提取~10min + RidgeCV~2min）。2 GPU 并行，剩余18个配置需约9轮 → **约1.5-2小时**完成全部20个。

---
