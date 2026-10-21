# analysis bayesian posterior entropy

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bayesian-posterior-entropy_20260524T192252_result.json`
- **Structured JSON:** [`bd8aa3a90d44170323f5.json`](../../sessions/bd/bd8aa3a90d44170323f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果已写入 `/root/cert_manip_resist_eval/artifacts/results/plan001/bayesian_posterior_entropy.json`。

关键发现：

| 指标 | K=3 | K=5 | K=7 |
|------|-----|-----|-----|
| Posterior entropy | 0.975 | 1.470 | 1.800 |
| Effective judges | 2.67/3 | 4.37/5 | 6.07/7 |
| Concentration ratio | 0.890 | 0.874 | 0.867 |
| K_eff CV | 0.157 | 0.148 | 0.131 |
| Max weight (mean) | 0.500 | 0.342 | 0.266 |

非单调行为的双重机制解释：
1. **Posterior concentration**: concentration ratio 单调下降 (0.890→0.874→0.867)，所有 pairwise Mann-Whitney 检验均显著 (p < 1e-20)
2. **K_eff variance compression**: K_eff 的 CV 从 0.157 降至 0.131，predictor range 被压缩，regression 检测力下降

K=5 时 raw panel size 增益尚可补偿 concentration loss；K=7 时双重压缩叠加导致 K_eff 效应完全不显著。

---
