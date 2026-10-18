# code w2 unconstrained baselines

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_w2_unconstrained_baselines_20260515T050316_result.json`
- **Structured JSON:** [`d1ad6fd0650611dc49e6.json`](../../sessions/d1/d1ad6fd0650611dc49e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态：实验已完成，无需重跑

服务器上 `/root/ratekv/run_w2_unconstrained_baselines.py`（11993 字节，2026-05-15 12:46）和结果 JSON、log 均存在；log 末尾 "ALL DONE. Total 3.5min"。已同步到本地：
- `run_w2_unconstrained_baselines.py`
- `artifacts/w2_unconstrained_baselines_results.json`

### 结果（budget=0.25, 64 seq × 2048 tok）

| Model | conc | baseline PPL | unconstrained PPL | 倍数 | 行为 |
|---|---|---|---|---|---|
| Yi-1.5-9B | 0.71 (Spike) | 5.89 | **672.2** | 114× | catastrophic |
| Llama-3.1-8B | 0.57 (Spike) | 6.51 | **1219.7** | 187× | catastrophic |
| Mistral-7B-v0.3 | 0.24 (Flat) | 5.87 | **47.8** | 8.2× | severe 但非 catastrophic |
| Gemma-2-9B | 0.23 (Flat) | 7.32 | **277.4** | 37.9× | catastrophic |

### 关键观察

1. **MCKP 与 Greedy 在所有 4 个模型上 PPL 完全相同**：bf16_2bitonly profile 的每头动作集是 {16, 2}，只有 2 个选项，MCKP 退化为 greedy。bit distribution 也一致（Yi 165/27, Llama 220/36, Mistral 220/36, Gemma2 288/48）。

2. **Backfire 部分发生但混合**：
   - 强支持假设：Mistral (Flat) 仅 8.2× 退化，远轻于 Yi/Llama (Spike)
   - 不支持：Gemma-2 (Flat, conc=0.23) 也 catastrophic (37.9×)
   - reframe 思路："concentration alone 不充分预测 catastrophic"——可能需要叠加 calibration heavy-tail 或 layer-wise variance。或者 Gemma-2 的 softcap/post-LN 架构使其对量化更敏感。

3. **结论与 paper 一致**：unconstrained allocation 对高 concentration 模型必然 catastrophic，cardinality constraint 是必要的；Flat 模型的失败程度依赖架构而非仅 concentration。

---
