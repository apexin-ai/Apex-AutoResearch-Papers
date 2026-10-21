# research real data n expansion

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_real_data_n_expansion_20260523T123150_result.json`
- **Structured JSON:** [`480cc0b65d34d6ef95f1.json`](../../sessions/48/480cc0b65d34d6ef95f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存至 `artifacts/n17_feasibility_report.md`。

## 结论：可行，预计 1.5-2 天，~$1,200

### 核心发现

**技术层面**：
- 代码完全数据驱动，无 N=8 硬编码。exp-018 已在 N=20 synthetic 上跑通。
- MCMC 参数量仅增加 18 个（9×θ + 9×c），被 I=316 项 item 参数主导，runtime 约 2x。

**数据层面**：
- Arena-Hard v0.1 HuggingFace 数据集有 **76 个模型**的预生成 responses 可直接下载
- 其中 **30+ 个**同时有 Chatbot Arena ELO，可直接用作 target models
- 推荐选 9 个（claude-3.5-sonnet, gpt-4-turbo, llama-3.1-70b, gemma-2-27b, claude-3-opus, llama-3-70b, mixtral-8x22b, claude-3-haiku, llama-3-8b），ELO 分布 ~1165-1299
- 不推荐用已有本地 responses 的 4 个模型（claude-opus-4.7/sonnet-4.6, gpt-5.5, mistral-large-2），因为它们全是 judges，会把 judge-target overlap 推到 50%

**成本层面**：
- Response 生成：$0（用 HF 预生成数据）
- Judge 评测：~$1,184（6 个 API judges × 9 个新模型 × 1000 calls/model）
- 瓶颈：claude-opus/sonnet 50 RPM → ~3h wall time
- 去掉 gpt-5.5 judge 可降至 $765

**主要风险**：即使 N=17，real-data Δτ 仍可能不显著（exp-015 已证明是 model-data mismatch 而非 power 问题）。但 N=17 的 τ 分辨率从 1/28≈0.036 提高到 1/136≈0.0074，reviewer 攻击面显著缩小。

---
