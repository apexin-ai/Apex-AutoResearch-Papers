# viz appendix gate profiles

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_appendix_gate_profiles_20260522T144350_result.json`
- **Structured JSON:** [`e96394c1c54271914d42.json`](../../sessions/e9/e96394c1c54271914d42.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 3 个图表已成功生成并保存到服务器 `/root/turn_residual_gating/artifacts/`。

**生成的文件：**

| 文件 | PDF 大小 | PNG 大小 |
|------|---------|---------|
| `fig_gate_profile_heatmap` | 43 KB | 126 KB |
| `fig_training_loss_curves` | 72 KB | 651 KB |
| `fig_gate_distribution` | 32 KB | 180 KB |

**图表 1: Per-layer Gate Profile Heatmap**
- Panel (a): Qwen 28 层 × 5 条件（Init, LO, UG, TG, TG+PCGrad）
- Panel (b): Llama 32 层 × 1 条件（TG）
- 使用 RdBu_r diverging colormap，范围 0.7–1.0
- 低 gate 值（<0.82）的格子标注了数值
- **注意**: PCGrad 数据来自 step 2500（非最终 step 3000），因为完整训练日志不在服务器上，只在本地 JSONL 聊天记录中找到部分数据

**图表 2: Training Loss Curves**
- 3 个子图：NTP Loss / GAR Loss / Total Loss
- 3 条线：TG (Qwen, 蓝)、UG (Qwen, 红)、TG (Llama, 绿)
- 带 rolling average 平滑
- **缺失**: PCGrad 和 LO 的训练日志不可用（PCGrad 仅有 24 条部分记录，LO 无日志）

**图表 3: Gate Value Distribution**
- Violin + strip plot，3 个条件：TG, UG, TG+PCGrad
- 标注了 μ 和 σ 统计量
- 可见 TG 的 gate 值方差最大（std=0.052），与 UG（std=0.055）和 PCGrad（std=0.063）对比

**如需补全缺失数据：**
- PCGrad 完整训练日志：需要重跑 `train_phase2_v9_pcgrad.py` 并重定向输出到 `.log` 文件，或从 W&B 拉取
- LO 训练日志：需要重跑 lora-only 训练并保存日志
- PCGrad 最终 gate profile：需要跑一次 `eval_phase2_gar.py --gate-profile` on PCGrad checkpoint

---
