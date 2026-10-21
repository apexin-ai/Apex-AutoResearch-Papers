# analysis eval pipeline 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_pipeline_34685_20260525T082642_result.json`
- **Structured JSON:** [`1e2988d98beb5bbdbcde.json`](../../sessions/1e/1e2988d98beb5bbdbcde.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### Eval Pipeline 准备状态

| 检查项 | 状态 |
|--------|------|
| eval 脚本 (`evaluate_safelibero.py`) | ✓ 可用 |
| MUJOCO 3.8.1 + EGL | ✓ 正常 |
| conda 环境 `occsafe` | ✓ 正常 |
| eval 脚本已创建 (`/root/occsafe_vla/eval_after_training.sh`) | ✓ |
| Checkpoint 路径格式确认 | ✓ |
| 日志目录 `/root/runs/occsafe_vla/` | ✓ 存在 |

### Checkpoint 路径格式

训练完成后 50K checkpoint 路径为：
```
/root/autodl-tmp/checkpoints/{exp}/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--{exp}--50000_chkpt
```
脚本已包含 fallback 逻辑：若 `--50000_chkpt` 不存在则使用 latest 目录。

### 训练进度（与预期严重偏差）

| GPU | 实验 | 进度 | 已运行 |
|-----|------|------|--------|
| 0 | cutoff_25k_s2_v3 | 12,777/50,005 (25%) | ~3h47m |
| 1 | reverse_cutoff_s2_v3 | 12,891/50,005 (26%) | ~3h51m |
| 2 | cutoff_45k_s1_v3 | 13,220/50,005 (26%) | ~3h57m |
| 3 | cutoff_15k_s2_v2 | 13,213/50,005 (26%) | ~3h57m |

速率约 0.92 it/s，剩余 ~37,000 步，**预计还需 ~11 小时**，完成时间约 **May 26 03:30 UTC**，远晚于预期的 16:30-17:00 UTC。

### 预估 eval 时长
~50-60 min/个（基于历史记录 cutoff_15k_s0_eval 52 min），4 个并行 eval 总耗时 ~1h。

### 使用方式
训练完成后在 34685 上执行：
```bash
bash /root/occsafe_vla/eval_after_training.sh
```

---
