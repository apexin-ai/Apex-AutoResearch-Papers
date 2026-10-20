# analysis trace length ablation fig

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_trace_length_ablation_fig_20260516T040942_result.json`
- **Structured JSON:** [`0de133747b648123cc89.json`](../../sessions/0d/0de133747b648123cc89.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有任务完成。总结：

**已完成：**

1. **生成缺失的 predictions.jsonl** — 在 GPU 1 上成功运行了 256tok 和 512tok 的评估，predictions 已保存到各自的 checkpoint 目录。

2. **Paired Bootstrap 显著性检验** (N=10,000, seed=42) — 12 对比较全部完成。关键发现：
   - 256→512: +1.60pp, **不显著** (p=0.117)
   - 512→1024: **-3.19pp** (p=0.002), 1024tok 显著更差
   - 1024→no_limit: **+4.54pp** (p<0.001), no_limit 显著更好
   - 所有 full_trace vs exception_only: **-18~23pp** (全部 p<0.001)
   - 1024tok vs no_trace: +2.10pp, **不显著** (p=0.078)

3. **论文级图表** — `fig_trace_ablation.pdf` 和 `.png` 已生成在服务器 `/root/trace-verdict-study/artifacts/`。使用 DejaVu Serif 字体，线性 x 轴，带 95% CI error bars，含 exception_only 和 no_trace 参考线。

4. **分析报告** — 写入本地 `artifacts/trace_ablation_analysis.md`。

5. **Bootstrap JSON** — 已复制到本地 `artifacts/trace_ablation_bootstrap.json`。

**图表文件位于服务器：** `/root/trace-verdict-study/artifacts/fig_trace_ablation.{pdf,png}`（SCP 不可用，无法直接传输到本地）。

---
