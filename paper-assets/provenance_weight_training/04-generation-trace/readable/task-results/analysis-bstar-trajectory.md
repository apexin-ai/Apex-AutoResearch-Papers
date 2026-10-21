# analysis bstar trajectory

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bstar-trajectory_20260516T142250_result.json`
- **Structured JSON:** [`20ac9283a9dec943912f.json`](../../sessions/20/20ac9283a9dec943912f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 artifact 已注册。任务完成。

## 分析结论

**Figure 1: b* 轨迹**
- b* 均值 ≈ 1.40，标准差 ≈ 0.98
- 训练前 1/4 均值 = 1.409，后 1/4 均值 = 1.367
- **趋势：稳定** — 方法从训练一开始就完成了校准，b* 不随训练步数系统性递减或递增

**Figure 2: α_eff binding rate**
- 训练早期（step 0–2000）：α_eff binding rate 仅 ~10–12%，ESS 约束主导
- step 2000 之后：α_eff binding rate 跳升至 ~37% 并稳定
- 整体：α_eff binding 19.1%，ESS binding 29.5%，无约束激活 51.4%
- **解读**：step 2000 左右模型学会了识别污��模式，更多 batch 触碰 α_eff 上界（0.8），但 ESS 约束仍是更常见的活跃约束

**PDF 文件位置**（服务器 westd-47453）：
- `/root/autodl-tmp/provenance_weight_training/output/models/adaptive_fix_seed42/bstar_trajectory.pdf`
- `/root/autodl-tmp/provenance_weight_training/output/models/adaptive_fix_seed42/alpha_eff_binding_rate.pdf`

---
