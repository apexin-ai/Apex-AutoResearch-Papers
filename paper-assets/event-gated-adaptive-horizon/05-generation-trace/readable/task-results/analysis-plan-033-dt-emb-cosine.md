# analysis plan 033 dt emb cosine

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_033_dt_emb_cosine_20260525T102254_result.json`
- **Structured JSON:** [`177640d9f137cff9e520.json`](../../sessions/17/177640d9f137cff9e520.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结论：

**1. exp_065 结论完全复现并扩展**：11 个实验、47 个 checkpoint 交叉验证。Trained cos(dt1,dt2) 范围从 [-0.94, -0.70] 扩展为 **[-0.947, -0.639]**。

**2. 高分辨率演化曲线 (exp_066b, 5k resolution)**：
- 10k step 时已达 -0.947（极早期即强反相关）
- 25k-45k step 放松最快（+0.024/10k steps）
- 65k step 后放松减速，300k step 趋近 **-0.65 平衡点**

**3. Cosine 放松领先 CIVO alert ~40k steps**：
- Cosine 放松从 15k step 开始（VE ratio 仅 0.03）
- CIVO alert 在 55k step 才触发
- dt_embedding 分化是训练自发行为，不是 CIVO 触发的结果；分化是 value estimation divergence 的**结构性前提**

**4. Walker vs Cheetah 差异**：Walker 的 norm 显著增长（dt1 从 0.23→0.76），Cheetah 的 norm 几乎恒定但方向仍在变化。

**5. Frozen embedding** 维持恒定 cos ∈ [-0.15, +0.17]（随机初始化状态），从结构上消除了分化 channel。

报告和图表已保存至 `artifacts/plan_033_dt_emb_cosine/` 并注册。

---
