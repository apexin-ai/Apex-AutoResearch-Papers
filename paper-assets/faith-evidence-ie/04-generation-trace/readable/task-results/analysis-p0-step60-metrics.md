# analysis p0 step60 metrics

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_p0-step60-metrics_20260514T213842_result.json`
- **Structured JSON:** [`2b0fc5e7f68974dae2ec.json`](../../sessions/2b/2b0fc5e7f68974dae2ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## P0 step 40-60+ 指标

| Step | f1_reward | ced_reward | format | reward_mean | frac_zero_std | KL | grad_norm | loss |
|------|-----------|------------|--------|-------------|---------------|-----|-----------|------|
| 35 | 0.0101 | 0.0154 | 0.168 | 0.193 | 0.1 | 0.157 | 0.19 | 0.053 |
| 40 | **0.0381** | 0.0786 | 0.201 | 0.318 | 0.3 | 0.006 | 0.14 | 0.023 |
| 45 | **0.0** | 0.0 | 0.138 | 0.138 | 0.3 | 0.011 | 0.26 | 0.041 |
| 50 | 0.0087 | 0.0113 | 0.225 | 0.245 | 0.2 | 0.008 | 0.97 | 0.086 |
| 55 | **0.0378** | 0.0278 | 0.198 | 0.264 | 0.2 | 0.095 | **67.0** | 0.045 |
| 60 | 0.0094 | 0.0059 | 0.208 | 0.223 | 0.1 | 0.145 | 10.88 | 0.041 |

当前 step: **62/200**（进度条确认，仍在运行，~119s/it）
Checkpoint-60: **EXISTS**

## 趋势评估

- **f1_reward 趋势: 剧烈振荡，无持续上升。** Step 40 达到 0.038 的峰值后，step 45 直接归零，step 55 又回到 0.038，step 60 再跌回 0.009。模型未学到稳定的 IE 能力，每5步一轮"撞大运"。
- **KL 稳定性: 稳定，无新 mega-spike。** Step 30 的 7e13 spike 后完全恢复，step 35-60 KL 在 0.006-0.157 区间，但 step 55→60 有轻微上升趋势（0.095→0.145）。
- **grad_norm 异常: step 55 出现 67.0 的 spike**（正常值 0.1-1.0），step 60 仍偏高 10.88。这与 KL 上升同步，提示模型参数在局部震荡。
- **整体: ⚠️ 警告**
  - f1/ced reward 极不稳定，step 45 完全归零说明模型在"遗忘-重学"循环
  - grad_norm spike 暗示优化不稳定
  - format reward 相对稳定（0.13-0.23），说明格式学习没崩
  - 核心问题：lr=5e-6 可能仍偏高，或 GRPO 的 group 采样方差太大导致信号噪声比低

---
