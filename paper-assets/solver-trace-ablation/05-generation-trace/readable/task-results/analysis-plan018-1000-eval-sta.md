# analysis plan018 1000 eval sta

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan018-1000-eval-sta_20260515T153631_result.json`
- **Structured JSON:** [`405a8f2baf42f325396e.json`](../../sessions/40/405a8f2baf42f325396e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

## eval_sta 指标（已在 eval_results.json 中）

| 指标 | 值 |
|------|-----|
| prove_rate | 0.97 (97/100) |
| mean_isr | 0.6892 |
| proved_only_mean_isr | 0.7105 |
| median_isr | 0.75 |

## classify_h7 Taxonomy

| 类别 | 数量 | 占比 |
|------|------|------|
| H7a (text-match tautology) | 97 | 100% |
| H7b (obfuscated tautology) | 0 | 0% |
| H1 (conclusion embedding) | 0 | 0% |
| H8 (conjunction collapse) | 0 | 0% |
| **Genuine** | **0** | **0%** |

100% single-premise, 100% H7a。所有 97 个 proved 样本都是 premise = conclusion 的 tautological collapse。

## 500步 vs 1000步 对比（Random β=0.1 s42）

| 指标 | 500步 | 1000步 | 变化 |
|------|-------|--------|------|
| prove_rate | 0.80 | 0.97 | +17pp |
| H7 | 0 | 97 | 0→100% |
| H1 | 58 | 0 | 58→0 |
| H8 | 4 | 0 | 4→0 |
| Genuine | 18 | 0 | 18→0 |
| proved_only_ISR | — | 0.71 | — |

**关键发现确认**：Random β=0.1 在 1000 步完全坍塌到 H7 tautological mode。500 步时还有多样的 hacking 模式（H1=58, H8=4, genuine=18），到 1000 步全部收敛为 single-premise tautology。H7 不是 ISR 特异的——Random reward 同样会诱发。

注：eval_results.json 实际已含完整 STA 数据（per-sample ISR ablation），无需重跑 eval_sta。模型权重已被清理，无法重跑。classify_h7_results.json 已保存。

---
