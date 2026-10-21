# paper figure fig1 rasp pipeline

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig1-rasp-pipeline_20260515T071719_result.json`
- **Structured JSON:** [`d270cebb23b8bee7b852.json`](../../sessions/d2/d270cebb23b8bee7b852.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Figure 1 已生成并注册。

**输出文件**：
- PDF: `docs/paper/figures/fig1_rasp_pipeline.pdf` (54KB, 矢量)
- PNG: `docs/paper/figures/fig1_rasp_pipeline.png` (217KB, 300 DPI)
- 脚本: `artifacts/plot_fig1_pipeline.py`

**图表内容**：
- **Stage 1**: 模型 + CoT 数据 → 注意力头重要性 I(h) (Taylor) 和功能重叠 F(h) (CKA) 梯度条
- **Stage 2** (核心): Standard Pruning (按 I 排序) vs RASP (按 S=I×(1-F)^α 排序) 对比面板。关键交换标注：B (I=.85, F=.80) 因高 overlap 被剪枝；D (I=.55, F=.05) 因低 overlap 被保护。三色图例区分 Protected / Redundant / Unimportant
- **Stage 3**: Pruned Model → SFT Warmup (format+EOS) → GRPO RLVR (reasoning recovery) → Recovered Model

---
