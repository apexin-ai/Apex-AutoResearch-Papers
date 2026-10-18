# analysis pi0 38929 gpu2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pi0-38929-gpu2_20260520T063634_result.json`
- **Structured JSON:** [`aa3c429ca5a4fd22c810.json`](../../sessions/aa/aa3c429ca5a4fd22c810.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已存在，分析完成。

## π0 Token Importance Analysis — 结果汇总

数据已在 `artifacts/` 中（`pi0_pruning_curve.json` + `pi0_attention_entropy_perlayer.json`），无需重新运行。

### π0 vs OpenVLA 核心对比

| 指标 | π0 (linear proj, 256 tokens) | OpenVLA (3-layer MLP, 256 tokens) |
|------|------|------|
| **Keep 10% → normalized loss** | 0.976 (仅损失2.4%) | 1.608 (损失增加61%) |
| **Keep 50% → normalized loss** | 0.983 (仅损失1.7%) | 1.167 (损失增加17%) |
| **Keep 90% → normalized loss** | 0.993 | 1.023 |
| **Importance CV** | 0.038 | ~0.215 (5.7× higher) |
| **Importance Gini** | 0.009 | — |
| **Entropy ratio** | 0.9999 | 0.661 |
| **Suffix→vis entropy (mean)** | 0.959 | 0.661 (declining 0.97→0.49 across layers) |

### 关键发现

**π0 的 vision tokens 几乎完全均匀**:
- Gini=0.009, entropy_ratio=0.9999 — 接近完美均匀分布
- 丢弃 90% tokens，loss 仅下降 2.4%（甚至略微改善）
- 所有 18 层的 suffix→vis entropy 都维持在 0.93-0.98

**OpenVLA 的 vision tokens 高度分化**:
- CV 是 π0 的 5.7 倍
- 丢弃 90% tokens，loss 增加 61%
- Entropy 从浅层 0.97 持续衰减到深层 0.49

### 对论文 thesis 的支撑

两者都是 **256 vision tokens + SigLIP-family encoder**，关键差异是 connector:
- **Linear projection (π0)** → tokens 保持均匀 → 极度可压缩
- **3-layer MLP (OpenVLA)** → tokens 产生 importance 分化 → 难压缩

**结论**: Connector type 是 compressibility 的主要决定因素，不是 token count。这直接支撑核心 thesis。

### 缺失数据

X-VLA (64 tokens, linear) 的离线分析数据尚未生成，artifacts 中未找到。如需完成三方对比，需要单独运行 X-VLA 的 token importance analysis。

---
