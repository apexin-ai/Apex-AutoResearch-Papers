# viz dose response final figure

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_dose_response_final_figure_20260518T163318_result.json`
- **Structured JSON:** [`81220a2160a88b2c4bdb.json`](../../sessions/81/81220a2160a88b2c4bdb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**总结：**

1. **数据读取** — 8 个条件（top-4 到 top-32）的完整结果已全部提取

2. **Figure 生成** — PDF + PNG 已保存到：
   - 服务器：`/root/autodl-tmp/vla-ssd/results/fig_dose_response_curve.{pdf,png}`
   - 本地：`/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/figures/fig_dose_response_curve.{pdf,png}`

3. **合并 JSON** — `/root/autodl-tmp/vla-ssd/results/dose_response_curve_combined.json` 包含所有 8 个条件的完整数据（paired_mse, per_dim_shift, token_divergence_rate, kl_divergence, per_task breakdown, heads_ablated 等）

4. **绘图脚本更新** — 服务器 `/root/vla-ssd/scripts/plot_dose_response.py` 和本地副本均已更新为实际数据

**Dose-response curve 关键发现：**
- 4→12 heads: steep rise (d: 0.48 → 0.56), 前 12 个最高选择性 head 贡献了大部分效应
- 16→20 heads: plateau (d: 0.59 → 0.59), 新增 head 几乎无额外影响
- 20→32 heads: slow rise (d: 0.59 → 0.64), 边际递减
- 所有条件的 d 均显著高于 control (8 random heads, d=0.41)

---
