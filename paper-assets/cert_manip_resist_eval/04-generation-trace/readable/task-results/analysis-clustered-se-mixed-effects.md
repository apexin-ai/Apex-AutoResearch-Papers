# analysis clustered se mixed effects

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_clustered-se-mixed-effects_20260522T185951_result.json`
- **Structured JSON:** [`e516c2ee633de42bce96.json`](../../sessions/e5/e516c2ee633de42bce96.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件较大（~34KB），通过分段下载。直接用完整日志中的 summary 数据即可。

分析完成。结果汇总：

## 汇总表格

| Method | η_max FDR sig (/12) | K_eff FDR sig (/12) | K_eff sig+ | K_eff sig− |
|---|---|---|---|---|
| Canonical OLS | 11/12 | 8/12 | 7 | 1 |
| **Clustered SE (max)** | **8/12** | **0/12** | 0 | 0 |
| **Mixed Effects (max)** | **7/12** | **3/12** | 3 | 0 |

## SE Inflation

- K_eff SE inflation: mean=**2.54x**, range=[1.50x, 4.64x]
- η_max SE inflation: mean=**2.62x**, range=[1.78x, 3.82x]

## 关键发现

1. **η_max 是 robust 的**：从 11/12 降到 8/12 (clustered) / 7/12 (mixed)，仍然多数显著。审稿人的 p-value 膨胀担忧对 η_max 影响有限。

2. **K_eff 确实受非独立性影响严重**：clustered SE 下从 8/12 直接降到 0/12。Mixed effects 保留了 3/12（全部正方向，prompt_injection 和 position_bias 在 arc_challenge 上），但远弱于 OLS 结论。

3. **SE 膨胀约 2.5x**：符合预期——每个 judge 出现在 91/455 panels，有效样本量约为名义值的 1/2.5。

## 对论文的影响

K_eff 4+/12 的门槛未达到（clustered: 0/12, mixed: 3/12）。Story 需要调整：
- η_max（个体脆弱性）是 panel ASR 的主导因素——**robust**
- K_eff（面板冗余度）的独立预测力在控制 judge 非独立性后大幅减弱——需要降级为 secondary/suggestive evidence

JSON 已保存到服务器 `/root/cert_manip_resist_eval/artifacts/results/plan001/clustered_se_analysis.json`。

---
