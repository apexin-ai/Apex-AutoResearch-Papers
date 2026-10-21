# ops ug completion check

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_ug_completion_check_20260519T065227_result.json`
- **Structured JSON:** [`7691da3fa428a0f2fb6a.json`](../../sessions/76/7691da3fa428a0f2fb6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。Cron 列表为空（不在本 session 创建的，无需删除）。

---

## 报告

### 1. 训练状态：正常完成
"Training complete in 21994.5s" + "Final model saved" + gate gradients confirmed。无任何 error/traceback。

### 2. 训练量
- **3 个 epoch 全部完成**，最终 global step = 7950（每 epoch ~2650 steps × 3 = 7950）
- 总耗时 **21994.5 秒（~6.1 小时）**

### 3. 关键 Metrics

| Epoch | Avg Loss | Avg NTP | Avg GAR | Avg DIV |
|-------|----------|---------|---------|---------|
| 0 | 1.0019 | 0.9755 | 0.0259 | 0.0005 |
| 1 | 0.9447 | 0.9435 | 0.0013 | 0.0000 |
| 2 | 0.9319 | 0.9309 | 0.0010 | 0.0000 |

Final gate stats: **mean=0.9598, std=0.0518, min=0.7773, max=1.0000**

### 4. Final Gate Profile (step 3000, 28 layers)

```
L0:0.875  L1:0.996  L2:0.996  L3:0.777  L4:0.980  L5:0.812  L6:0.977
L7:0.957  L8:0.977  L9:0.973  L10:0.980 L11:0.961 L12:0.969 L13:0.973
L14:0.934 L15:0.980 L16:0.965 L17:0.953 L18:0.980 L19:0.969 L20:0.961
L21:0.992 L22:0.980 L23:0.984 L24:0.984 L25:0.992 L26:0.996 L27:1.000
```

注意：uniform gate 模式下各层值仍有差异（L3=0.777 最低，L27=1.000 最高），这说明 uniform gate 实际上也学到了 per-layer 不同的 gate 值。

### 5. Checkpoint 路径
- Final model: `/root/turn_residual_gating/runs/phase2_ug_s42/`
- LoRA adapter: `lora/adapter_model.safetensors` (19.3MB)
- Gate params: `gate_params.pt` (3.2MB)
- Per-epoch checkpoints: `epoch_0/`, `epoch_1/`, `epoch_2/`

### 6. GPU 状态
**已完全释放**：0 MiB / 97887 MiB used, 0% utilization。GPU 可用。

---
