# paper writing related work expansion

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_related_work_expansion_20260522T232439_result.json`
- **Structured JSON:** [`cd0100a5c1da6405d578.json`](../../sessions/cd/cd0100a5c1da6405d578.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

636 词（含 LaTeX 命令），目标范围内。各段扩展完成：

1. **LLM-as-Judge**: 加入 Dawid & Skene（多标注者聚合渊源）、AlpacaEval（win-rate 自动化）、FLASK（fine-grained 评估），并加了一句过渡将这些 benign 框架与我们的 adversarial 测试连接。
2. **Condorcet**: 加了一句关于 voter independence 条件被 LLM 相关性违反的说明。
3. **Ensemble Diversity**: 展开了 Brown et al. 的 bias-variance-covariance 分解（弱模型 bias 抵消多样性收益），展开了 Kuncheva & Whitaker 的十种度量测试结果与我们 $K_{\mathrm{eff}}$ 的对应关系。
4. **Adversarial Robustness**: 展开了 Tramer et al. 的结果（提升但未消除跨模型漏洞），明确了 Kariyappa/Pang 依赖训练时协调而 LLM 面板缺乏这种控制。

---
