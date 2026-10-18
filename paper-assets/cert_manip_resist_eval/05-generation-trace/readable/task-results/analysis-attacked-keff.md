# analysis attacked keff

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_attacked-keff_20260523T070444_result.json`
- **Structured JSON:** [`401fb686b56da6fe2ad6.json`](../../sessions/40/401fb686b56da6fe2ad6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果保存在 `/root/cert_manip_resist_eval/artifacts/results/plan001/attacked_keff.json`。

**核心发现**：

| Attack | Spearman r (mmlu / arc) | Mean \|ΔK_eff\| | 稳定性 |
|---|---|---|---|
| score_manipulation | 0.98 / 0.99 | 0.08–0.11 | 稳定 |
| authority_bias | 0.95 / 0.97 | 0.08–0.09 | 稳定 |
| sycophancy | 0.91 / 0.92 | 0.09 | 稳定 |
| verbosity_bias | 0.91 / 0.92 | 0.09–0.12 | 稳定 |
| prompt_injection | 0.63 / 0.60 | 0.24–0.25 | 中等扰动 |
| position_bias | 0.60 / **0.08** | 0.53–**0.84** | 严重破坏 |

**结论**：Clean K_eff 对 4/6 攻击是可靠的 proxy（r > 0.91）。Position bias 严重改变 judges 间的 MI 结构（位置交换使原本相关的 judges 变得 decorrelated），prompt injection 中等程度扰动。对 SF-4 reviewer 的回应：可以指出 K_eff 对多数攻击稳定，但需 acknowledge position bias 这一例外。

---
