# analysis maven residualized bcs

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_maven_residualized_bcs_20260516T012720_result.json`
- **Structured JSON:** [`246bea0be04d5b48a924.json`](../../sessions/24/246bea0be04d5b48a924.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结果：

**MAVEN 正相关 BCS-F1 是 centrality artifact，对两种 embedding 都成立：**

| | Raw ρ(BCS,F1) | Confound | BCS↔Confound r | Partial r (controlled) |
|---|---|---|---|---|
| **MiniLM** | +0.208 (p=.011) | log_freq | +0.201 (p=.014) | +0.133 (p=.107, n.s.) |
| **Qwen3** | +0.184 (p=.025) | degree_0.7 | +0.854 (p<.001) | +0.063 (p=.442, n.s.) |

关键发现：
1. MiniLM 的 confound 是 **type frequency**（频繁类型 → 高 BCS → 高 F1）
2. Qwen3 的 confound 不是 frequency（r=-0.043, n.s.），而是 **degree centrality**（语义邻居数量，r=0.854）
3. 联合控制 log_freq + degree 后，两种 embedding 的 BCS-F1 相关都消失（Qwen3 p=0.439, MiniLM p=0.226）
4. 与 Few-NERD 对比：Few-NERD 无 centrality confound（BCS↔freq r=0.042），所以 BCS 保持预期负方向

产出文件在服务器 `artifacts/maven_residualized_bcs/`：`analysis_report.txt`（完整报告含 appendix 建议文本）和 `residualized_analysis.py`（可复现脚本）。

---
