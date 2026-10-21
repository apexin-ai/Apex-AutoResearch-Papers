# code r14 exp4 gsm1k cooks

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r14_exp4_gsm1k_cooks_20260522T121542_result.json`
- **Structured JSON:** [`be9d8794e0ff6c287ac8.json`](../../sessions/be/be9d8794e0ff6c287ac8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果摘要：

**Cook's D 分布**：3/33 models 超过 4/N 阈值 (0.121)：
- **Deepseek-math-7b-rl** (D=0.300) — 唯一 gap 为负且 dif_advantage 为正的 model，属于反方向异常点
- **GPT-2-xl** (D=0.161) — 近零 gap 和近零 dif_advantage，floor effect
- **Smaug-2-72B** (D=0.129) — 高 gap 但 dif_advantage 偏小

**Leave-one-out**：所有 33 次 LOO 的 p 值均 < 0.05（range: 0.0015–0.0352）。移除最有影响力的 Deepseek-math-7b-rl 后 r 从 -0.478 降到 -0.373，p=0.035 仍显著。

**移除全部 3 个 outlier 后**：r = -0.384, p = 0.036, N=30 — 仍显著。

**结论**：r = -0.478 对 outlier removal 是 **robust** 的。相关性减弱但不消失。

输出文件：
- `artifacts/r14_sf9_gsm1k_cooks/cooks_d_report.md`
- `artifacts/r14_sf9_gsm1k_cooks/cooks_d_results.csv`

---
