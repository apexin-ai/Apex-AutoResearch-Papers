# data attention steering v7 extract

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_attention_steering_v7_extract_20260520T111756_result.json`
- **Structured JSON:** [`905ba4039c0808387c64.json`](../../sessions/90/905ba4039c0808387c64.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已保存。

**结果总结：**
- **4/6 betas 有完整 per-conversation 数据**（0.0, 2.0, 5.0, 10.0）
- **2 betas 只有聚合均值**（0.5, 1.0）— 因为 SSH 工具输出被截断在 ~8KB，这两个 beta 的 per-conv 数据丢失在截断区域

Per-conv GAR 用 gar_curves 的中间 turns (2-8) 平均值计算。beta_0.0 和 10.0 保留了完整精度，beta_2.0 和 5.0 的 gar 来自实验日志（4位小数），beta_5.0 的 PPL 保留了完整精度。

如果需要 beta_0.5 和 1.0 的 per-conv 数据，需要等 SSH 工具可用后重新从服务器分 beta 读取。

---
