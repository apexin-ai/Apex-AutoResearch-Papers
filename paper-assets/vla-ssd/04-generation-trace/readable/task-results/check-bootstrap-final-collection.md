# check bootstrap final collection

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bootstrap_final_collection_20260522T225437_result.json`
- **Structured JSON:** [`6024ac7046d253616fc4.json`](../../sessions/60/6024ac7046d253616fc4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### 进度：10/16 完成，2 正在跑

| # | 条件 | 状态 |
|---|------|------|
| 1 | openvla_goal/trained | ✅ 完成 |
| 2 | openvla_goal/untrained | ✅ 完成 |
| 3 | openvla_spatial/trained | ✅ 完成 |
| 4 | openvla_spatial/untrained | ✅ 完成 |
| 5 | openvla_object/trained | ✅ 完成 |
| 6 | openvla_object/untrained | ✅ 完成 |
| 7 | openvla_long/trained | ✅ 完成 |
| 8 | tracvla_goal/trained | ✅ 完成 |
| 9 | tracvla_goal/untrained | ✅ 完成 |
| 10 | tracvla_spatial/trained | ✅ 完成 |
| 11 | **openvla_long/untrained** | 🔄 cuda0: bootstrap 阶段 (1000 iter, 100 workers)，06:51 开始 |
| 12 | **tracvla_spatial/untrained** | 🔄 cuda1: fitting RidgeCV，06:53 开始 |
| 13 | tracvla_object/trained | ⏳ 排队 |
| 14 | tracvla_object/untrained | ⏳ 排队 |
| 15 | tracvla_long/trained | ⏳ 排队 |
| 16 | tracvla_long/untrained | ⏳ 排队 |

GPU 当前空闲（0% util），因为 bootstrap 和 RidgeCV 都在 CPU 上跑。

---

### 已完成结果汇总

| 条件 | peak_r2 | peak_layer | exit_r2 | **delta** | **delta_ci_95** | bootstrap mean±std |
|------|---------|------------|---------|-----------|-----------------|-------------------|
| **openvla_goal/trained** | 0.4164 | L1 | 0.2826 | 0.1339 | [0.0, 0.074] | 0.017±0.022 |
| **openvla_goal/untrained** | 0.4026 | L10 | 0.3039 | 0.0988 | [0.0, 0.048] | 0.012±0.015 |
| **openvla_spatial/trained** | 0.5452 | L24 | 0.4963 | 0.0489 | [0.0, 0.044] | 0.008±0.012 |
| **openvla_spatial/untrained** | 0.5339 | L4 | 0.5180 | 0.0160 | [0.0, 0.036] | 0.012±0.010 |
| **openvla_object/trained** | 0.5752 | L21 | 0.5509 | 0.0242 | [0.0, 0.027] | 0.006±0.008 |
| **openvla_object/untrained** | 0.5932 | L14 | 0.5407 | 0.0525 | [0.0, 0.058] | 0.014±0.017 |
| **openvla_long/trained** | 0.5121 | L25 | 0.4691 | 0.0430 | [0.0, 0.059] | 0.014±0.018 |
| **tracvla_goal/trained** | 0.5399 | L13 | 0.2065 | **0.3334** | **[0.092, 0.355]** | 0.191±0.070 |
| **tracvla_goal/untrained** | 0.5048 | L11 | 0.4403 | 0.0645 | [0.0, 0.078] | 0.023±0.023 |
| **tracvla_spatial/trained** | 0.6871 | L13 | 0.5315 | **0.1557** | **[0.049, 0.162]** | 0.099±0.030 |

### 关键观察

**TracVLA 有显著 SSD（CI 下界 > 0）**：
- `tracvla_goal/trained`: delta=0.333, CI=[0.092, 0.355] — 显著
- `tracvla_spatial/trained`: delta=0.156, CI=[0.049, 0.162] — 显著

**OpenVLA 所有条件 CI 下界均为 0**，delta 不显著。

**TracVLA trained 的后层 R² 严重衰减**（goal: L13=0.54→L31=0.21, spatial: L13=0.69→L31=0.53），而 untrained 没有这种模式。这支持 SSD 是训练导致的。

**等待中**：tracvla_spatial/untrained 的结果将与 trained 配对，形成完整对照。openvla_long/untrained 也快完成。还剩 4 个 tracvla 条件（object × 2, long × 2）排队。

---
