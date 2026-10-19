# ssh cross task probe run

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cross-task-probe-run_20260516T053110_result.json`
- **Structured JSON:** [`921b22b8554df5e6f5a5.json`](../../sessions/92/921b22b8554df5e6f5a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。总结：

**Cross-task probe 在 checkpoint-10000 上成功运行**，结果与之前 checkpoint-5000 完全一致：

1. **Probe A（固定图像，交换指令）**：所有 3 对指令的 importance map **完全相同**（bit-identical，cos=1.0，L2=0.0）→ scorer 在架构上就忽略 language instruction

2. **Probe B（自然跨任务观察）**：不同任务的 importance map 高度相似（cos ∈ [0.9937, 0.9978]，全部 > 0.99）→ scorer 学到的是 **spatial position prior**，而非 task-dependent selection

3. **结论**：当前 v5_div_reg 架构的 scorer **不是** action-conditioned 的。"Action-conditioned information bottleneck" 的 framing 在实验上不成立。

**已注册的 artifacts（7 个）**：
- `cross_task_probe_results.md` — 完整分析报告（含两个 checkpoint 数据）
- `cross_task_probe_summary.json` — 结构化 JSON
- `probe_A_fixed_image_swap_instruction.png` — Probe A heatmap
- `probe_B_cross_task_heatmaps.png` — Probe B heatmap
- `seed1_token_importance_heatmap.png` — scorer token 重要性
- `seed1_avg_importance_per_camera.png` — 每相机平均重要性
- `seed1_scorer_weight_histogram.png` — scorer 权重分布

---
