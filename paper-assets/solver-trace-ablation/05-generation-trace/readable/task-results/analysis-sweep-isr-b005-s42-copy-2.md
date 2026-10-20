# analysis sweep isr b005 s42

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sweep-isr-b005-s42_20260516T040311_result.json`
- **Structured JSON:** [`d4a3502be3cc61eadc4f.json`](../../sessions/d4/d4a3502be3cc61eadc4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。报告已写入 `artifacts/sweep-isr-b005-s42/report/analysis_report.md` 并注册。

## 核心发现

**β=0.05 是 Goodhart 阈值以下的关键数据点。**

| 指标 | β=0.05 | β=0.1 (s43) | β=0.3 (s43) |
|------|--------|-------------|-------------|
| Eval prove_rate | 55.1% | 61.0% | 91.0% |
| Proved-only ISR | **0.759** | — | 0.283 |
| H7 hacking | **排除**（ISR=0.75 → 多前提） | **100%** | ~70% |
| Genuine est. | **≥75%** | **0%** | ~2.8% |

三个关键结论：

1. **ISR 没有崩塌**：训练过程中 ISR 从 0.10 稳步上升到 0.74，与 β≥0.1 的 ISR→0 形成鲜明对比
2. **Goodhart 阈值在 β=0.05 和 β=0.1 之间**：β=0.05 保留了推理结构，β=0.1 则 100% 坍缩为 H7 tautology
3. **ISR=0.750 的极端均匀性**（96.3% proved 样本精确为 0.75）说明模型收敛到 4 前提 / 3 必要的固定模板

**待完成**：两个 GPU 被 sweep-isr-b02 训练占用，classify_h7.py 无法运行。需要等 GPU 空闲后重跑 eval_sta.py 生成 JSON，再做完整 hacking taxonomy 分类。

---
