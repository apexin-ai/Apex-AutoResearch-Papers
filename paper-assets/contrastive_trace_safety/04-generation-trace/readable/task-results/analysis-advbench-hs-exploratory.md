# analysis advbench hs exploratory

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_advbench_hs_exploratory_20260520T013808_result.json`
- **Structured JSON:** [`a30b93b8d51a7a757eb3.json`](../../sessions/a3/a30b93b8d51a7a757eb3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。关键发现：

### 结果摘要

**Volatility 分布（核心发现）**：
- AdvBench 和 HarmThoughts 的 volatility 曲线形状高度一致：**浅层 < 深层**
- AdvBench shallow (L0-4): **0.265**, deep (L12-24): **0.442**, ratio = **0.60**
- HarmThoughts shallow (L0-4): **0.226**, deep (L12-24): **0.386**, ratio = **0.59**
- 两者 shallow/deep ratio 几乎相同（0.60 vs 0.59）

**Volatility 曲线特征**（Fig 1）：
- 峰值在 L8-L10 附近（AdvBench ~0.54, HarmThoughts ~0.48）
- L12 之后逐渐下降并稳定在 ~0.42 (AdvBench) / ~0.37 (HarmThoughts)
- AdvBench 整体 volatility 略高于 HarmThoughts（+0.04~0.06），说明 AdvBench traces 的 hidden states 在 step 间变化更大

**Norm 趋势**（Fig 2）：
- 两个数据集 norm 分布相似：深层 norm 远大于浅层（L24 ~28 vs L0 ~0.4）
- Norm 在 step 位置上相对平稳，无明显趋势

**预测：deep_CR_likely**

浅层 volatility 低意味着 consecutive steps 间的 cosine similarity 高（变化小）→ crossing rate 方法在浅层检测到的"变化"更少。这预测 AdvBench 上 CR 方法会倾向于选择 **中深层**（L8-L12 附近 volatility 峰值区域），而非浅层。

所有输出已保存到 `artifacts/advbench_preliminary/`（3 张图 + JSON）。

---
