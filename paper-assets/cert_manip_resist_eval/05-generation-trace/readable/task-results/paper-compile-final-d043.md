# paper compile final d043

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_compile-final-d043_20260524T085718_result.json`
- **Structured JSON:** [`641390f9ad5b7b4f7767.json`](../../sessions/64/641390f9ad5b7b4f7767.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 最终编译验证 + 审计报告

### 编译状态
- **错误**: NO_ERRORS
- **页数**: 20

### 0/12 审计 (11处匹配)

| 位置 | 上下文 | 判定 |
|------|--------|------|
| results.tex:37 | K=3 clustered SE K_eff 0/12 | 正确保留 |
| results.tex:47 | K=3 clustered SE K_eff 0/12 (表格) | 正确保留 |
| results.tex:53 | K=3 clustered SE K_eff 0/12 (caption) | 正确保留 |
| results.tex:69 | K=3 clustered SE K_eff 0/12 | 正确保留 |
| analysis.tex:14 | K=7 Bayesian K_eff 0/12 | 正确保留 |
| appendix.tex:69 | K=7 Bayesian K_eff 0/12 | 正确保留 |
| appendix.tex:91 | K=7 Bayesian K_eff 0/12 | 正确保留 |
| appendix.tex:103 | K=7 Bayesian η_max 1/12, K_eff 0/12 (表格) | 正确保留 |
| appendix.tex:106 | K=7 Bayesian K_eff 0/12 (caption) | 正确保留 |
| appendix.tex:115 | K=3 partial info K_eff 0/12 | 正确保留 |
| appendix.tex:132 | K=3 clustered SE K_eff 0/12 | 正确保留 |

**无错误残留。** 所有 0/12 均属于 K=7 Bayesian K_eff、K=3 clustered SE K_eff、或 K=3 partial info K_eff，全部合法。无 K=5 η_max 0/12 错误。

### 9/12 审计 (多处匹配)

全部合法，分布在：
- **Fractional logit K=3**: abstract, analysis.tex:11, conclusion, introduction, results.tex:50/69/118
- **K=3 Bayesian OLS η_max**: analysis.tex:14, appendix.tex:57, introduction:22, results.tex:106-107/115
- **Pool A K=5**: appendix.tex:148/157/278
- **K=5 Cinelli sensitivity**: appendix.tex:249
- **Q-statistic**: appendix.tex:353/364

**无 K=7 bootstrap 残留。**

### 10/12 审计 (12处匹配)

全部合法，分布在：
- **K=3 OLS η_max**: results.tex:35/46/105
- **K=7 Threshold K_eff**: analysis.tex:14, appendix.tex:69/91/102/106
- **Pool A K=5 Cinelli**: analysis.tex:11, appendix.tex:278/281/285

**无 K=5 bootstrap 残留。**

### "sole" 审计 (2处匹配)

| 位置 | 上下文 | 判定 |
|------|--------|------|
| appendix.tex:115 | "η_max remains the sole significant predictor" — K=3 partial info (K_eff=0/12) | 合法 |
| appendix.tex:190 | "sole non-significant η_max condition" — 指 position bias 单个条件 | 合法 |

**无 K≥5 "sole significant predictor" 残留。**

### 结论

编译无错误，20页，所有四项审计全部通过，无需修改。

---
