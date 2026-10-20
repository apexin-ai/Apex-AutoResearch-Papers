# monitor llama ss progress

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_llama_ss_progress_20260524T120502_result.json`
- **Structured JSON:** [`d39ff7b8d3f5c0be3474.json`](../../sessions/d3/d39ff7b8d3f5c0be3474.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Llama SS 训练状态 — westd-20861**

| 项目 | 值 |
|------|-----|
| **PID** | 158507 ✅ 存活，已运行 4h48m |
| **当前进度** | Epoch 1, Step 3000 / 21600 (**13.9%**) |
| **GPU** | 99% 利用率，84.4 / 97.9 GB 显存 |
| **速率** | ~10.4 steps/min |
| **预计剩余** | ~29.7 小时 |
| **预计完成** | ~5月25日 18:00 UTC |

**最近指标 (Step 3000):**
- `L_NTP` = 0.78, `Loss` = 0.78, `Gate` = 0.92
- `SS_L_GAR` = 0.020 (从 0.023 下降中), `TF_L_GAR` = 0.016 (从 0.018 下降)
- SS ratio 固定在 0.300

**Gate Profile (step 1350):**
- 浅层 (L0-L16): 0.95-0.99 — 几乎全通
- 深层 (L22-L28): 0.72-0.85 — 明显降低，符合预期的"深层压缩"模式
- L24-L25 最低 (0.742, 0.715)

训练正常推进，gate 分布和 loss 趋势均符合预期。

---
