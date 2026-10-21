# ops v7 completion and pipeline

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_v7_completion_and_pipeline_20260519T004355_result.json`
- **Structured JSON:** [`4b22dfced54d359e394e.json`](../../sessions/4b/4b22dfced54d359e394e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 都完成了。汇报结果：

---

## v7 训练结果

**训练**: 成功完成，3 epoch，21352s (~5.9h)
- Final avg loss: 0.897 (NTP=0.896, GAR=0.001, DIV=0.000)
- Final gate profile (step 3000): mean=0.9336, std=0.0492, min=0.7891, max=0.9883
- Gate gradients active: True
- Checkpoints: epoch_0, epoch_1, epoch_2 + gate_params.pt

**Final gate profile**:
```
L0:0.859 L1:0.988 L2:0.957 L3:0.801 L4:0.789 L5:0.895 L6:0.961 L7:0.941
L8:0.953 L9:0.945 L10:0.957 L11:0.926 L12:0.914 L13:0.898 L14:0.887 L15:0.949
L16:0.934 L17:0.934 L18:0.930 L19:0.961 L20:0.945 L21:0.973 L22:0.977 L23:0.965
L24:0.961 L25:0.977 L26:0.984 L27:0.980
```
L3(0.801), L4(0.789) 仍是最低层，与 Dongre onset layers 对齐。

---

## Eval 结果

### GAR-ours (last token per assistant turn)
| Metric | Value |
|---|---|
| Turn 1 avg GAR | 0.0502 |
| Mid-turns avg GAR | 0.0157 |
| Baseline mid-turn | 0.0122 |
| **GAR recovery** | **+0.35pp** |

Per-turn GAR: `[0.0503, 0.0295, 0.0201, 0.0172, 0.0128, 0.0143, 0.0144, 0.0153, 0.0094, 0.0268]`

### GAR-Dongre (all response tokens per turn)
| Metric | Value |
|---|---|
| Turn 1 avg GAR | 0.0587 |
| Mid-turns avg GAR | 0.0194 |
| Baseline mid-turn | 0.0122 |
| **GAR recovery** | **+0.72pp** |

Per-turn GAR: `[0.0587, 0.0301, 0.0238, 0.0212, 0.0185, 0.0198, 0.0176, 0.0155, 0.0163, 0.0141]`

---

## Pipeline 修复

**Bug**: `gar.py` 的 `compute_gar()` 在 `measure_only=True` 时逐层清除 `_attention_weights`，第二次调用时 `first_weights` 为 None 导致 `AttributeError`。已删除 lines 92-93 的清除逻辑。

**额外问题**: 首次 ours eval 因 3 个孤儿 eval 进程占满 GPU，`device_map="auto"` 把模型放到 CPU 导致 device mismatch。杀掉孤儿后重跑成功。

---

## UG Baseline 状态

tmux session `ug_train` 运行中，step 350/3000 (epoch 0)，Gate=0.81，GAR_loss=0.23。已注册 cron 监控 (`phase2_ug_s42`, interval=300s)。

Registry 已更新：v7 → DONE/success, UG → RUNNING。

---
