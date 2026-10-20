# figure fig1 framework paperbanana v3

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_fig1-framework-paperbanana-v3_20260524T172758_result.json`
- **Structured JSON:** [`a7074969cb45016e2312.json`](../../sessions/a7/a7074969cb45016e2312.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

register_artifact 工具不可用，跳过注册步骤。

**完成汇报：**

- **方法**：PaperBanana 直接生成（gemini-2.5-pro + gemini-3-pro-image-preview），1 次迭代 critic 即通过
- **公式正确性**：✓ Stage 3 G-MFRM 公式为 `θ_n − b_i − d_j − τ_k + c_n·e_i`（正号），`c_n·e_i` 橙色高亮
- **输出标签**：✓ `ĉ_n`（Contamination），`θ̃_n`（Fair scores，带 tilde）
- **视觉质量**：顶会级别——圆角面板、彩色 Stage 标签、阴影、Warm-start 弧形箭头、ê_i fixed 箭头、OVB 双向红色虚线箭头全部到位
- **分辨率**：300 DPI，2752×1536 px

**产出文件**：
- PNG: `/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/fig1_framework_v2.png` (4.1MB)
- PDF: `/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/figures/paper/fig1_framework_v2.pdf` (4.0MB)

---
