# ops r6 data audit

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_r6-data-audit_20260525T064840_result.json`
- **Structured JSON:** [`7ad593a286d28906db17.json`](../../sessions/7a/7ad593a286d28906db17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告已保存至 `artifacts/r6_data_audit.md`。

**发现 8 处不一致：**

**Fractional logit（6处 🔴）：**
- `results.tex:24` 表格 K=3 行：η_max 6/12→**7/12**, K_eff 9/12→**4/12**（都错）
- `results.tex:43` "fractional logit giving 9/12"→**4/12**（K=3）
- `results.tex:99` 声称 "9/12 across all K"→实际 **4/12, 9/12, 10/12**
- `introduction.tex:20` 同上 "9/12 across all K"
- `analysis.tex:15` 同上 "9/12 at all K"
- `appendix.tex:159` 表格 K=5 行 η_max 4/12→**5/12**

**Adaptive R²（2处 🔴）：**
- `introduction.tex:16` R²=0.275→**0.256**
- `results.tex:66` R²=0.275→**0.256**

**全部正确的：** WCB bootstrap 数字（9处）、OLS 计数、dominance 分布、Bayesian 方向/neutralization。

**需额外核实：** 98.6% directional concordance (71/72) 在 fractional logit 数字修正后是否仍成立。

---
