# viz fig5 lambda curve multiseed fix

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_fig5_lambda_curve_multiseed_fix_20260526T142903_result.json`
- **Structured JSON:** [`b425a2e25772ffee6a56.json`](../../sessions/b4/b425a2e25772ffee6a56.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图表生成完成。验证结果：

- **误差条可见**: λ=0 CAR (±2.83) 和 λ=0.005 CAR (±2.29) 的误差条清晰显示
- **λ=0.01 空心 marker**: CAR (圆圈) 和 TSR (方块) 均为空心，n=1 标注可见
- **λ=0.1 Pending**: 虚线矩形 + "?" 占位符
- **Baseline 虚线清晰**: LoRA-only (54.5%/51.5%) 和 π₀.₅ (28.5%/71.5%) 均标注
- **无虚假上升趋势**: CAR 在 λ=0 → 0.005 均为 54.5%，完全 flat

**注**: TSR λ=0.005 显示 mean=54.0 (Director 确认的 3-seed 均值) 但无误差条，因为 registry 中 `reeval_sdf_s1_l005_30k` 和 `reeval_sdf_s2_l005_30k` 的 metrics 为空，无法计算 std。

输出文件:
- `artifacts/figures/fig5_lambda_curve.pdf`
- `artifacts/figures/fig5_lambda_curve.png`
- `artifacts/figures/plot_fig5.py` (已覆盖)

---
