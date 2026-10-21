# viz fig counterfactual bar v3

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_fig_counterfactual_bar_v3_20260524T050506_result.json`
- **Structured JSON:** [`823e0bf226362728a581.json`](../../sessions/82/823e0bf226362728a581.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图表生成完毕。验证结果：

1. **数据正确** — Panel A 的 8 组 Cohen's d 值与服务器数据一致，Panel B 的 NORA cosine distance 同样正确
2. **颜色清晰** — 四种条件颜色区分度好
3. **NORA Goal 饱和值** — 截断到 0.34 高度，内部标注 "1.0 (sat.)"
4. **数值标注不重叠** — 各 bar 顶部标注清晰可读
5. **OpenVLA/TracVLA 分组** — 有虚线分隔和间距
6. **d=0.8 参考线** + "large effect" 标注 ✓
7. **星号** 标记每组最大值 ✓

输出文件：
- `docs/paper/figures/fig_counterfactual_bar.pdf` + `.png`
- `artifacts/figures/paper/fig_counterfactual_bar.pdf` + `.png`（硬链接，同文件）
- 脚本：`scripts/plot_counterfactual_bar.py`

---
