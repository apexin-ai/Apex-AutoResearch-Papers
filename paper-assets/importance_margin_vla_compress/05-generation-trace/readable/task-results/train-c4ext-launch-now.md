# train c4ext launch now

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_c4ext_launch_now_20260519T182622_result.json`
- **Structured JSON:** [`9a037c0dcfa0ccef66a4.json`](../../sessions/9a/9a037c0dcfa0ccef66a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**训练已成功启动并在跑！**

## 汇报

- **服务器**: westd-41074, GPU 0 (NVIDIA RTX PRO 6000 Black, 98GB)
- **PID**: 26118 (tmux session: `train_openvla_sc_m128_seed42`)
- **实验 ID**: `train_openvla_sc_m128_seed42`
- **日志**: `~/runs/importance_margin_vla_compress/train_openvla_sc_m128_seed42.log`

### 日志前 20 行关键信息：
```
OpenVLA loaded: 7541237184 params
Freeze config: trainable=403308544 / total=7944545728 (5.08%)
  Compressor params: 403308544
Dataset: 273465 samples, 34183 batches/epoch
Starting training: 0 -> 100000 steps
step=0/100000   loss=19.9729  lr=1.10e-06  grad=932.19  sps=0.3
step=50/100000  loss=4.6484   lr=6.05e-06  grad=47.32   sps=0.6
```

Loss 从 19.97 快速降到 4.65（50 步内），训练正常进行，速度 ~0.6 steps/sec。

---
