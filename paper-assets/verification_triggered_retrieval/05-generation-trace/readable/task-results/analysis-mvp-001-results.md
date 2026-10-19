# analysis mvp 001 results

**verification triggered retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mvp_001_results_20260517T091755_result.json`
- **Structured JSON:** [`cddde8efcb998b46f0fc.json`](../../sessions/cd/cddde8efcb998b46f0fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完整运行无错误。以下是完整结果汇报。

---

## MVP 实验结果汇报

### 实验概况
- **6 个 step 全部完成**，无 error/exception/traceback
- 总耗时：5645.3s (~94 min)
- 进程"异常退出"应为 SSH session 超时断开，非实验代码错误

### 实验配置
| 项目 | 值 |
|---|---|
| 数据源 | HotpotQA dev set, 200 条 |
| Corpus | HotpotQA distractor set, **1987 passages**（非 full Wikipedia） |
| CoT + Claim 模型 | Qwen3-8B |
| 检索 | Hybrid (BM25 + BGE-base-en-v1.5 FAISS), RRF fusion, top-5 |
| NLI 模型 | nli-deberta-v3-large |

### 各 Step 产出
| Step | 文件 | 条数 |
|---|---|---|
| 1. Claim Extraction | step1_claims.json | 200 条 (每条含多个 claims) |
| 2. Query Generation | step2_queries.json | 200 条 (每条含 query_pairs) |
| 3. Build Index | index/ (BM25 + FAISS) | 1987 passages |
| 4. Retrieval | step4_retrieval.json | **1598 paired retrievals** |
| 5. NLI Evaluation | step5_nli_scores.json | 200 条 |
| 6. Analysis | step6_report.json | 统计报告 |

200 条 × 每条多个 claims = 1598 claim-level paired comparisons。

### 核心结果

**假设不成立（NOT SUPPORTED）。**

#### Entailment Rate (top-5 中 entailing 的比例)
| Query Type | Mean | Std |
|---|---|---|
| Answer-seeking | 0.5046 | 0.3319 |
| Verification | 0.4972 | 0.3304 |
| **差值** | **-0.74 pp** | |

- Paired t-test: t = -1.617, **p = 0.1061**（不显著，α=0.05）
- **Cohen's d = -0.040**（negligible effect）
- 方向甚至相反（verification 略低于 answer-seeking）

#### Mean Entailment Score (连续分数)
| Query Type | Mean | Std |
|---|---|---|
| Answer-seeking | 0.5039 | 0.3259 |
| Verification | 0.4983 | 0.3239 |

- p = 0.1965, Cohen's d = -0.032

### Query 示例
- **Claim**: "Scott Derrickson is an American filmmaker, screenwriter, and producer."
- **Verification query**: "Evidence supporting or contradicting that Scott Derrickson is an American filmmaker, screenwriter, and producer."
- **Answer-seeking query**: "What is Scott Derrickson's profession and nationality?"

### 诊断

两种 query 类型的 NLI 分数几乎无差异（差值 <1pp, effect size negligible）。可能原因：

1. **Corpus 太小**（~2000 passages）：大部分 claim 的相关 passage 都在 top-5 中，query formulation 的差异被 corpus 的高覆盖率掩盖
2. **Query 生成质量**：verification query 模式过于模板化（"Evidence supporting or contradicting that..."），可能没有真正激发不同的检索行为
3. **Hybrid retrieval + RRF** 可能对 query 表述不够敏感——BM25 和 dense retrieval 的组合在小 corpus 上可能返回几乎相同的 top-5

---
