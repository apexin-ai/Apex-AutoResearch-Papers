# paper figure fig2 nve complete

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig2_nve_complete_20260515T105046_result.json`
- **Structured JSON:** [`5b7d56afcfbfc36d20ad.json`](../../sessions/5b/5b7d56afcfbfc36d20ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

渲染完成。修改摘要：

**修复了 3 个问题：**
1. 数据路径：`actor_loss_data.json` 在 `data/` 目录，脚本原来错误地在 `paper/` 目录查找
2. 数据格式：JSON 是 `[{"step":..., "actor_loss":...}, ...]` 列表格式，脚本原来期望 `{"steps":[], "actor_loss":[]}` 字典格式
3. 缺少 baseline：原脚本只映射了 3 个实验，现在加入 `exp_001_baseline`（颜色 `#2C3E50`）

**产出：**
- `fig2_nve_trajectory.png` (2171×1556, 349KB) — 双面板完整版
- `fig2_nve_trajectory.pdf` (32KB) — 矢量版
- 上面板：7 条 NVE 轨迹，x 轴 25K-105K
- 下面板：4 条 actor_loss 轨迹（baseline/008d/009b/009e），x 轴自适应至 505K，含 y=0 虚线和 009e sign flip 标注
- 两个面板 x 轴独立（因 baseline 数据延伸至 505K，共享会压缩上面板）

---
