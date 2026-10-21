# analysis cls multiseed summary

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cls-multiseed-summary_20260520T004621_result.json`
- **Structured JSON:** [`2a31f3c412ecd45d7a43.json`](../../sessions/2a/2a31f3c412ecd45d7a43.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总完成。两个文件已写入 `artifacts/` 并注册：

**Table 3 聚合数据 (mean ± std)**:

| Model | Form | n | Accuracy | F1_macro | F1_fail | F1_pass |
|-------|------|---|----------|----------|---------|---------|
| Qwen3-8B | CLS | 3 | 84.83±0.67 | 77.58±1.21 | 64.84±2.30 | 90.32±0.50 |
| DeepSeek-6.7B | CLS | 2 | 84.38±2.50 | 77.75±3.79 | 65.59±6.00 | 89.90±1.58 |
| Qwen3-8B | TRAJ | 3 | 73.61±3.18 | 73.37±3.01 | — | — |
| Majority | — | — | 72.96 | — | — | — |

**95% CI (Qwen3-8B CLS, n=3, t=4.303)**: Accuracy [83.16, 86.50], F1_macro [74.58, 80.58]

**CLS vs TRAJ gap**: +11.22 pp accuracy, +4.21 pp F1_macro

注意事项：
- DeepSeek n=2 的 CI 极宽（t=12.706），基本无统计意义，建议论文中只报 mean±std
- TRAJ s42 的 per-class F1 registry 中缺失，TRAJ F1_fail/F1_pass 按 2-seed 计算
- Qwen CLS s42 用的是 val-selected ckpt-3600（84.48%），与 ablation 实验一致
- LaTeX 行已在 `cls_multiseed_table.md` 底部，可直接复制

---
