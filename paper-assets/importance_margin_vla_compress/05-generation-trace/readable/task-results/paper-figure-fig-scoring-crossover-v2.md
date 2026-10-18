# paper figure fig scoring crossover v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig_scoring_crossover_v2_20260525T184906_result.json`
- **Structured JSON:** [`9b242be699bd8142880d.json`](../../sessions/9b/9b242be699bd8142880d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图表已完成，4 轮迭代后输出：

**输出文件**:
- PDF: `docs/paper/figures/paper/fig_scoring_crossover.pdf`
- PNG: `docs/paper/figures/paper/fig_scoring_crossover.png`
- 脚本: `docs/paper/figures/paper/gen_fig_scoring_crossover.py`

**数据修正**（全部从 registry 验证）:
1. OpenVLA Long 不再是 "No data" — 显示 L2=43.6%, R=46.8%, A=44.0%（method-indifferent）
2. X-VLA Object L2 = 99.2%（registry 确认是实际 k=0.9 值）
3. π₀.₅ Object Random = 9.0%（registry seed42）
4. π₀.₅ Long L2 = 81.0%（registry: 405/500）
5. X-VLA Goal: L2=70.2%, R=70.6%（registry 确认）
6. X-VLA Long: L2=27.5%, R=29.6%（registry 确认）

**新设计**: 3 模型×4 suite + SmolVLA 汇总行，3 列 scoring 方法，颜色编码 SR/baseline 保留率，蓝色竖条标注 winner，虚线边框标注 method-indifferent（gap < 3.5pp），代码内含 9 条 assertion 校验。

---
