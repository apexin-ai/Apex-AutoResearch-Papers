# paper figure fig 1 response pattern

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure_fig_1_response_pattern_20260520T195802_result.json`
- **Structured JSON:** [`951a72e49b8513194475.json`](../../sessions/95/951a72e49b8513194475.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Figure 1 生成完成。

**输出文件**：
- PDF: `figures/paper/fig_1_response_pattern.pdf` (39 KB)
- PNG: `figures/paper/fig_1_response_pattern.png` (199 KB, 300 DPI)
- 尺寸: 6.2 × 3.7 inches（ACL 双栏全宽）

**验证结果**：
- lz* clean = **+0.5**（正常范围）
- lz* contam = **-4.7**（显著异常）
- 数据来源: PSN-IRT MMLU 4PL 参数，100 items subsample，θ = 0.5
- 污染模拟: 14 个困难 items 翻转为正确（记忆），7 个简单 items 翻转为错误

**设计**: 双面板对比——(a) Clean Model 响应服从 ICC 曲线，(b) Contaminated Model 在困难端出现红色菱形标记（记忆 items）+ 简单端出现橙色方块（异常错误），虚线连接异常点到期望概率曲线。生成脚本: `figures/paper/gen_fig1.py`。

---
