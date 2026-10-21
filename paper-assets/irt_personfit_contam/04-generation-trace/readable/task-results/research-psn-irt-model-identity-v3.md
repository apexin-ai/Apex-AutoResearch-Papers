# research psn irt model identity v3

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_psn_irt_model_identity_v3_20260520T081327_result.json`
- **Structured JSON:** [`bfad12059064c53ba227.json`](../../sessions/bf/bfad12059064c53ba227.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

12 个模型身份全部确认，置信度 ✅ 确定。

**识别方法**：论文 Section 4.1 列出全部模型名，`combine.csv` 行序为字母序。通过计算每行正确率 + 论文中 DeepSeek-V3 θ>3.0 的确认进行交叉验证。

**关键结果**：

| id | θ | 正确率 | 模型 |
|---|---|---|---|
| 1 | 3.77 | 85.7% | DeepSeek-V3 |
| 5 | 1.73 | 82.1% | Hunyuan-Turbo |
| 0 | 1.46 | 80.6% | 360GPT2-Pro |
| 2 | 1.14 | 78.9% | Doubao-pro |
| 8 | 0.96 | 76.3% | Qwen-Plus |
| 7 | 0.93 | 77.0% | Moonshot-v1 |
| 3 | 0.78 | 84.5% | **Gemini-1.5** ⚠️ |
| 11 | 0.77 | 75.2% | Yi-Lightning |
| 9 | -0.13 | 60.4% | Qwen2.5-3B-Instruct |
| 6 | -1.37 | 40.0% | Mistral-7B-Instruct-v0.1 |
| 10 | -1.89 | 31.6% | Vicuna-7B-v1.3 |
| 4 | -3.38 | 23.1% | Gemma-2B-it |

**对 Phase B 最重要的发现**：Gemini-1.5 正确率排 #2 (84.5%) 但 IRT ability 仅排 #7 (θ=0.78)，是 raw accuracy 与 IRT ability 偏差最大的模型。这正是 person-fit 统计量要捕捉的异常 response pattern。

---
