# viz fig5 lambda curve template

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_fig5_lambda_curve_template_20260526T134613_result.json`
- **Structured JSON:** [`7d75e92621672668a6cf.json`](../../sessions/7d/7d75e92621672668a6cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图表第二轮迭代完成，质量达标。

**输出文件**：
- PDF: `artifacts/figures/fig5_lambda_curve.pdf`
- PNG: `artifacts/figures/fig5_lambda_curve.png`
- 脚本: `artifacts/figures/plot_fig5.py`

**图表要素**：
- 双 Y 轴（蓝=CAR, 红=TSR），spine 颜色对应
- X 轴为等距伪 log 布局，λ=0 标注 "(LoRA-only)"
- Pi0.5 baseline 两条虚线分别标注在左上(TSR=71.5%)和左下(CAR=28.5%)
- λ=0.1 灰色空心圆 + "Pending" 标注
- n=1 标注在每个数据点下方
- `plot_lambda_curve(data_dict, output_path)` 函数可直接复用，append 新 seed 数据即自动计算 mean±std

---
