# verify cf cohens d all conditions

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_cf_cohens_d_all_conditions_20260523T175248_result.json`
- **Structured JSON:** [`39575e2508637ecc5a85.json`](../../sessions/39/39575e2508637ecc5a85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已全部收集完毕。以下是完整分析报告。

---

## 数据不一致根因

三个来源使用了**不同的数据文件**：

| 来源 | 引用值 (empty / wrong) | 实际文件 | 问题 |
|---|---|---|---|
| 画图 Worker | 1.17 / 1.18 | `libero_goal/counterfactual_combined.json` (May 22, **finetuned**) | **正确** ✓ |
| Paper Agent Table 4 | 0.98 / 0.92 | `counterfactual_10tasks/` (May 21, **base openvla-7b**) | **用错文件** ✗ |
| paper_framing.md | 1.09 (empty) | 不明 — 最接近 libero_goal **shuffled**=1.096 | **搞混了 condition** ✗ |

**权威数据**来自 `libero_goal/counterfactual_combined.json`（最新版，finetuned 模型，May 22）。

`counterfactual_10tasks/` 是旧版实验，用的是 **base openvla-7b + bridge_orig**（非 finetuned），config 中 model="openvla-7b", unnorm_key="bridge_orig"。Paper Agent 把这个当成了 trained 结果。

---

## 完整 Cohen's d 表格（所有 trained 条件）

### OpenVLA (finetuned) — 基于 action MSE 的 global Cohen's d

| Arch-Suite | empty | wrong | shuffled | paraphrased | 数据文件 | 修改时间 |
|---|---|---|---|---|---|---|
| OpenVLA-Object | **1.212** | 1.188 | 1.1218 | 0.8955 | `libero_object/counterfactual_combined.json` | May 21 16:50 |
| OpenVLA-Goal | **1.1696** | 1.1821 | 1.096 | 0.9956 | `libero_goal/counterfactual_combined.json` | May 22 10:22 |
| OpenVLA-Spatial | **1.1734** | 0.8849 | 0.9787 | 0.807 | `libero_spatial/counterfactual_combined.json` | May 22 18:40 |
| OpenVLA-Long | 0.5048 | 0.5453 | **0.5646** | 0.4486 | `libero_long/counterfactual_combined.json` | May 22 06:39 |

### TracVLA (finetuned)

| Arch-Suite | empty | wrong | shuffled | paraphrased | 数据文件 |
|---|---|---|---|---|---|
| TracVLA-Object | **1.2117** | 1.0595 | 1.1643 | 0.9711 | `tracvla_object/trained/` |
| TracVLA-Goal | **1.5241** | 1.4046 | 1.3358 | 1.2128 | `tracvla_goal/trained/` |
| TracVLA-Spatial | **1.3268** | 1.1724 | 1.2947 | 1.1825 | `tracvla_spatial/trained/` |
| TracVLA-Long | **1.4726** | 1.4176 | 1.3909 | 1.1614 | `tracvla_long/trained/` |

### NORA (trained) — 使用不同指标

| Arch-Suite | 指标类型 | empty | wrong | shuffled | paraphrased | 说明 |
|---|---|---|---|---|---|---|
| NORA-Goal | cosine_dist | 1.0 | 1.0 | 1.0 | 1.0 | Cohen's d 全部 = 0.0（FAST+ 离散 token，MSE 无差异） |
| NORA-Spatial | cosine_dist | 0.238 | 0.275 | 0.114 | 0.023 | 有 Cohen's d（per-task 级，非全局） |

NORA config 明确说明："NORA uses FAST+ action tokens; MSE-based counterfactual not applicable. Using readout cosine distance instead."

---

## d 值含义

这些 Cohen's d 是 **global_metrics 级别**：5000 个 paired samples（10 tasks × 10 demos × 50 timesteps）的 action output MSE 计算的效应量。**不涉及任何 layer 信息**——纯粹度量 correct vs counterfactual instruction 下 action 输出的差异。

---

## 旧版文件清单（应避免引用）

| 文件 | 模型 | 日期 | 备注 |
|---|---|---|---|
| `counterfactual_combined.json` (根目录) | openvla-7b (base), 3 tasks | May 19 | 最早版本 |
| `counterfactual_10tasks/` | openvla-7b (base), 10 goal tasks | May 21 | Paper Agent 误用 |
| `counterfactual_spatial/` | openvla-7b (base), 10 spatial tasks | May 21 | 旧版 |

---
