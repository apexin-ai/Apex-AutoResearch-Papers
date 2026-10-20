# paper redesign framework figure

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_redesign-framework-figure_20260517T154447_result.json`
- **Structured JSON:** [`9ac933df60696cf3daf3.json`](../../sessions/9a/9ac933df60696cf3daf3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已全部同步。

**输出文件** (4 份，PDF/PNG 一致):

| 位置 | PDF | PNG |
|------|-----|-----|
| `artifacts/_project/chart/` | 46K | 180K |
| `artifacts/_project/paper/figures/` | 46K | 180K |

**服务器脚本**: `/root/gen-depth-fingerprint/scripts/plot_fig2_framework_v2.py`

**设计要点**:
- 三栏布局 (6.75×3.0 inches, `figure*` 双栏)
- **左栏**: Seed text (gen-0) → Generator G (含 ×4 回环箭头) → 5 级深度渐变条 → 参数标注框
- **中栏**: Pythia-410M → Token NLL 分布曲线 → 7 features 三组分色 (Drifting 蓝 / Stationary 橙 / Intermediate 灰)
- **右栏**: XGBoost (LOGO-CV) → 3-class 输出 → DDR 趋势子图 (三条趋势线带端点标签)
- 配色: 深度渐变 #F7FBFF→#08519C，跨栏粗箭头，虚线分隔符

---
