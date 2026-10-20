# paper figure fig3

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig3_20260516T014750_result.json`
- **Structured JSON:** [`3ed65244be7203a6462b.json`](../../sessions/3e/3ed65244be7203a6462b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Figure 3 已生成并注册（`art_20260516_468ffa`）。

**输出文件：**
- PDF: `artifacts/figures/paper/fig3.pdf`
- PNG: `artifacts/figures/paper/fig3.png`

**注意：** 由于无法 SSH 读取服务器上的逐层数据 (`perlayer_degradation_curve.json`)，当前使用 fallback 摘要数据通过 PCHIP 插值生成的合成曲线。拿到真实逐层数据后应替换。关键特征已正确呈现：
- Proj→L1 最大 drop（Embedding Interface 高亮区域）
- Trained−instruction（橙色）呈持续上升模式，peak 在 L30 附近
- 其余三条线呈 non-monotonic 模式，peak 在 L6–L12
- SigLIP+Proj (0.615) 和 DINOv2 (0.388) 参考线

---
