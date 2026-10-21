# code plan 010 figures

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_010_figures_20260516T073019_result.json`
- **Structured JSON:** [`aa1200ad3d689b5c7e2b.json`](../../sessions/aa/aa1200ad3d689b5c7e2b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

6 个文件全部生成：

| 文件 | 大小 |
|------|------|
| `libero_spatial_rsa_perlayer.pdf` / `.png` | 25K / 282K |
| `libero_spatial_r2_perlayer.pdf` / `.png` | 23K / 261K |
| `cross_benchmark_comparison.pdf` / `.png` | 28K / 776K |

路径：`/root/autodl-tmp/vla-ssd/results/figures/`

脚本：`/root/vla-ssd/scripts/plot_spatial_results.py`

图表说明：
- **Figure A**: Spatial 4 条 RSA 曲线 + 95% CI shading + peak 标注
- **Figure B**: Spatial 4 条 R² 曲线 + peak 标注
- **Figure C**: 1×2 cross-benchmark 对比，Goal（细线/半透明）vs Spatial（粗线），左=RSA 右=R²，颜色区分 trained/untrained，线型区分 image_mean/last_preaction

---
