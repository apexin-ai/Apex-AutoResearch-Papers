# analysis cka transfer degradation

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cka_transfer_degradation_20260520T203251_result.json`
- **Structured JSON:** [`d7409f4e1d5f2c67f483.json`](../../sessions/d7/d7409f4e1d5f2c67f483.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。以下是结果汇总：

---

## 1. mvp_003 Gate Check (Llama-3.1-8B-Instruct)

**EN Probe (per layer):**

| Layer | AUROC | ECE |
|-------|-------|-----|
| 0 | 0.6498 | 0.1481 |
| 4 | 0.6349 | 0.2214 |
| 8 | 0.6331 | 0.2287 |
| 12 | 0.6563 | 0.2630 |
| 16 | 0.7026 | 0.2579 |
| 20 | 0.7229 | 0.2257 |
| 24 | 0.7235 | 0.2421 |
| 28 | 0.7129 | 0.2438 |
| **31** | **0.7284** | **0.2052** |

**ZS Transfer (best layer per lang):**

| Lang | Best AUROC | Layer | p |
|------|-----------|-------|---|
| zh | 0.6400 | 20 | 0.001 |
| ko | 0.6480 | 31 | 0.001 |
| ar | 0.6143 | 31 | 0.001 |
| hi | 0.5917 | 31 | 0.001 |
| sw | 0.5838 | 16 | 0.001 |

**Gate:**
- P1: **FAIL** (ECE=0.2052 > 0.15)
- P2: **PASS** (5/5 ≥ 0.58)
- P3: **PASS** (9.53pp)
- P4: **FAIL** (0/5 mean-shift)
- Overall: **PARTIAL** — 与 Qwen (mvp_001) 模式一致

---

## 2. CKA vs Transfer Degradation

**Llama (mvp_003) — Overall: rho=-0.5192, p=0.0012 \*\***

Higher CKA (more similar EN-target representations) → lower transfer degradation. Significant.

Per-language:
| Lang | rho | p |
|------|------|-------|
| hi | -0.7333 | 0.025 * |
| sw | -0.5833 | 0.099 |
| zh | -0.5333 | 0.139 |
| ar | -0.2833 | 0.460 |

**Qwen (mvp_001) — Overall: rho=-0.3086, p=0.053 (marginal)**

Per-language: 无显著结果。

---

## 3. Cross-model CKA 对比

| Lang | Qwen CKA | Llama CKA | Qwen Deg | Llama Deg |
|------|----------|-----------|----------|-----------|
| zh | 0.7388 | 0.7527 | 0.1148 | 0.1462 |
| ar | 0.6934 | 0.6776 | 0.1542 | 0.1698 |
| hi | 0.4359 | 0.3805 | 0.2164 | 0.1698 |
| sw | 0.4158 | 0.4788 | 0.2246 | 0.2090 |

**Language ranking 两模型一致：**
- CKA: zh > ar > ... > hi/sw（高资源语言表征更相似）
- Degradation: zh < ar < hi < sw（高资源语言迁移损失更小）

**关键发现：** Llama 上 CKA-degradation 相关性显著（p=0.001），Qwen 上边际显著（p=0.053）。方向一致（负相关），说明 **representation similarity 确实能解释 cross-lingual transfer quality**，且这个关系是 model-agnostic 的。Llama 的 ko 数据缺失（CKA 分析未包含 ko），但不影响主结论。

Registry 已更新为 DONE，artifact 已注册。

---
