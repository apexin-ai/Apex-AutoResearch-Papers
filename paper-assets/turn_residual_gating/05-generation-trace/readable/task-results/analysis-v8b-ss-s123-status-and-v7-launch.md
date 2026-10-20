# analysis v8b ss s123 status and v7 launch

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_v8b_ss_s123_status_and_v7_launch_20260521T094357_result.json`
- **Structured JSON:** [`d6b183284f6d5beb8a01.json`](../../sessions/d6/d6b183284f6d5beb8a01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### v8b SS s123 — 运行中 (55%)

| 指标 | 值 |
|------|-----|
| 进度 | **Step 1650/3000** (55%), Epoch 1 进行中 |
| L_NTP | ~0.64–0.90 (收敛正常) |
| L_GAR | ~0.000 (已坍塌，与 s42 一致) |
| Gate mean | 0.9581 (std=0.053, min=0.734) |
| SS ratio | **0.500** (已达上限) |
| SS_L_GAR | 0.016 / TF_L_GAR: 0.021 |
| GPU | 82% utilization, 30.2 GB VRAM |
| Checkpoint | epoch_0 已保存 (gate_params.pt + lora/) |

**ETA**: 参考 s42 全程 8.1h，剩余 45% ≈ **~3.6 小时**（预计 ~20:30-21:00 服务器时间完成）。

### v7 TG s123 — 暂不启动

GPU 被 v8b SS s123 占用（v8b 峰值 53GB + v7 峰值 53GB > 102GB，共享会 OOM，s42 有前车之鉴）。v8b 完成后立即启动。

**已准备好的 v7 TG s123 启动命令**（seed 42→123，output dir 对应修改）：
```bash
PYTHONUNBUFFERED=1 python src/train_phase2.py \
  --gate-type threadgate --gar-loss-mode mse_target --gar-target 0.5 \
  --lambda-gar 1.0 --lambda-gate-div 1.0 --min-gate-std 0.05 \
  --init-bias 1.5 --gate-lr-multiplier 10 --max-seq-len 2048 \
  --seed 123 --output-dir runs/phase2_tg_s123_v7 \
  --data-dir data/ultrachat_8k --epochs 3
```

训练健康，gate dynamics 与 s42 一致。等 v8b 完成后可直接提交 v7 TG s123。

---
