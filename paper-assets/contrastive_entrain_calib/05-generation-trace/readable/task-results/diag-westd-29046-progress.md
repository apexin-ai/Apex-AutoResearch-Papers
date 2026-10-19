# diag westd 29046 progress

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_westd-29046-progress_20260518T231441_result.json`
- **Structured JSON:** [`4ba42a80cf1d32762936.json`](../../sessions/4b/4ba42a80cf1d32762936.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完成总结

### Task 1: 实验进度

**exp-002** (PID 69020, GPU 0)
- 当前 step: ~932 (最新日志 07:39:56)
- R1_mean: -0.15 ~ -0.64 (波动正常，R1 + R2 + R3 全部激活)
- R3_mean: 0.62 ~ 0.93
- combined_mean: 0.43 ~ 0.67
- R2 = 0.0 (cross-step EMA 尚未配对，符合预期)

**exp-003** (PID 70649, GPU 1)
- 当前 step: 882/8000 (11%, ETA ~52h)
- `d_syc not loaded` — R3-only 模式运行
- R3_mean: 0.20 ~ 0.61
- combined_mean = R3_mean (w3=1.0 因为无 d_syc)
- 速度 ~26s/step

**GPU 利用率**
| GPU | Util | VRAM |
|-----|------|------|
| 0 | 95% | 63.6/97.9 GB |
| 1 | 98% | 38.2/97.9 GB |

### Task 2: dcgrpo_trainer.py 同步

- 远程备份: `/root/mvp_v2_1_expanded/training/dcgrpo_trainer.py.bak.*`
- MD5 验证: `4a1a94bb1412033d4861feb3558e6d07` **匹配**
- 文件行数: 1020 行 (与本地一致)
- `recalibrate_direction` 方法: 已存在 (line 348)
- `DCGRPOConfig.recalibration_interval`: 已存在 (line 129)
- `DCGRPOConfig.calibration_data_path`: 已存在 (line 130)
- 触发逻辑 `_DCRewardCallable.__call__`: 已存在 (lines 193-196)

---
