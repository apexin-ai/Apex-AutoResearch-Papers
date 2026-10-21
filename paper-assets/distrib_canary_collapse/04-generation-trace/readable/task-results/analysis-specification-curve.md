# analysis specification curve

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_specification_curve_20260521T085823_result.json`
- **Structured JSON:** [`7f6a827efcd5995368ac.json`](../../sessions/7f/7f6a827efcd5995368ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。以下是 Specification Curve Analysis 的关键发现：

## 覆盖范围
- **16 个实验**（α=0.00 到 0.75）× **18 个 specifications**
- 5 methods × 2 directions × FDR correction（where applicable）+ 4 consensus specs

## 关键发现

### 1. 最 robust 的 specifications（高 α 下始终检测到信号）
- **NaiveXCorr**（Fwd/Rev）：几乎所有 α 下都 ≥0.875——但这说明它**不分区高/低 α**，是 false positive 过高的迹象
- **DiffXCorr**（Fwd/Rev，含 FDR）：高 α 下稳定 0.75，是**真正可靠的 discriminative method**
- **PermG_Fwd**：高 α 下 0.25-0.75，有区分力
- **K≥3_Fwd**：高 α 下 0.25-0.75，共识投票有效

### 2. 始终无信号的 specifications（低 α ≤0.30 全 =0）
- PermG_Fwd_FDR, PermG_Rev, PermG_Rev_FDR, K≥4_Fwd, K≥4_Rev

### 3. Transition region（α=0.50）
- median 检测率突然跳到 **0.6875**（其他 α 多为 0.0-0.3125）
- 是唯一一个 ThreshOnset_Fwd >0（0.5）的实验
- K≥4_Fwd 达到 0.625——所有 α 中最高

### 4. 重要发现：NaiveXCorr 的 false positive 问题
NaiveXCorr 在 α=0.00（zero contamination）时检测率就是 1.0，说明它检测到的是 **训练动态中固有的相关性**而非 contamination 信号。这在论文中需要讨论。

### 输出文件
- JSON: `artifacts/spec_curve_analysis/spec_curve_results.json`, `spec_curve_stats.json`
- 图表（服务器 westd-17855）: `spec_curve_heatmap.{pdf,png}`, `spec_curve_a075.{pdf,png}`, `spec_curve_a050.{pdf,png}`, `spec_curve_comparison.{pdf,png}`
- 分析脚本: `specification_curve_analysis.py`（本地 + 服务器）
- 所有 artifacts 已注册

---
