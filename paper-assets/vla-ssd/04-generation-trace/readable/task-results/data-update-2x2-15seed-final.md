# data update 2x2 15seed final

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_update_2x2_15seed_final_20260520T115230_result.json`
- **Structured JSON:** [`674d099b34b06aa0dbbb.json`](../../sessions/67/674d099b34b06aa0dbbb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 6 个文件已更新。以下是完整 2×2 summary 报告：

| | OpenVLA Untrained | OpenVLA Trained | Phi3V Untrained | Phi3V Trained |
|---|---|---|---|---|
| **Peak Layer** | L0 | L9 | **L6** | L11 |
| **Peak R²** | 0.629 ± 0.016 | 0.637 ± 0.008 | **0.578 ± 0.018** | 0.634 ± 0.009 |
| **L0 R²** | 0.629 ± 0.016 | 0.629 ± 0.016 | -0.330 ± 0.003 | -0.330 ± 0.002 |
| **L32 R²** | 0.584 ± 0.011 | 0.535 ± 0.015 | **0.410 ± 0.185** | 0.550 ± 0.007 |
| **Late-layer mean (L25-L32)** | 0.193 | 0.531 | **0.392** | 0.586 |
| **Late-layer avg std** | 0.244 | 0.037 | **0.172** | 0.011 |
| **Seeds** | 15 | 15 | **15** | 15 |

Phi3V Untrained 从 5→15 seeds 后的主要变化：
- Peak 从 L4 移到 **L6**，R² 从 0.583 降至 **0.578**（5-seed 的 L4 高值被摊平）
- 晚层 std 从 0.047 升至 **0.172**（新 seeds 中部分晚层 probe 出现负 R²，暴露不稳定性）
- Δ_train (peak) 从 +0.051 升至 **+0.056**；L15-L25 avg gap 从 +0.103 升至 **+0.137**
- 所有 4 条件现在统一 15 seeds，表格脚注已简化

---
