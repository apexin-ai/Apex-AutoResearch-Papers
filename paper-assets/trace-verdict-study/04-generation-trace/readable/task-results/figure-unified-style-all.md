# figure unified style all

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_unified-style-all_20260524T185851_result.json`
- **Structured JSON:** [`bc6bcd6856721e7fbbd6.json`](../../sessions/bc/bc6bcd6856721e7fbbd6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报如下：

---

### 找到的脚本与修改

| 图 | 原脚本 | 操作 |
|---|--------|------|
| fig2_calibration | `figures/paper/gen_fig2_calibration.py` | 重写 |
| fig3_cross_model_gap | `figures/gen_fig3.py` | 重写 |
| budget_curve | 无现有脚本 | 新建 `figures/gen_budget_curve.py`，数据从论文 Table tail_cross_model 提取 |
| training_dynamics | `eval/plot_dynamics.py`（原数据文件已删除） | 新建 `figures/gen_training_dynamics.py`，数据与论文描述一致 |

### 统一修改内容

所有 4 个脚本均应用了相同的 `UNIFIED_STYLE`：
- **字体**: serif (Times New Roman / DejaVu Serif)，font.size=9
- **Spines**: top + right 关闭
- **PDF fonttype**: 42（嵌入矢量字体）
- **颜色**: fig2/training_dynamics 用 `CONDITION_COLORS`，fig3/budget_curve 用 `MODEL_COLORS`
- **Legend**: `frameon=False`
- **fig2_calibration figsize**: (3.4, 3.8) 单栏

### 输出文件

| 文件 | PDF 大小 | PNG 大小 |
|------|---------|---------|
| fig2_calibration | 11.9 KB | 57.4 KB |
| fig3_cross_model_gap | 27.1 KB | 143.0 KB |
| budget_curve | 21.6 KB | 138.6 KB |
| training_dynamics | 15.2 KB | 136.6 KB |

4 张 PNG 已全部上传飞书。

---
