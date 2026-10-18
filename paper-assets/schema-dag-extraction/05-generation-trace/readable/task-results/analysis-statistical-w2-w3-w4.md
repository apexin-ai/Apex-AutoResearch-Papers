# analysis statistical w2 w3 w4

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_statistical_w2_w3_w4_20260516T031959_result.json`
- **Structured JSON:** [`50abfdce60a116e017b8.json`](../../sessions/50/50abfdce60a116e017b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三项分析全部完成，产出已保存至 `artifacts/d037_statistical_analyses/`：

| 文件 | 内容 |
|------|------|
| `w3_cluster_bootstrap_results.json` | Type-level cluster bootstrap CI |
| `w4_count_recall_ci_results.json` | Count=22 vs 44 recall CI |
| `w2_practical_effect_results.json` | Typical BCS range practical effect |
| `paper_text.md` | 三段论文可用文字 |

服务器上的脚本在 `/root/schema-dag-extraction/scripts/d037/`。

**核心结论**：
- **W3**：Cluster-robust CI 仍显著（Few-NERD [0.057, 0.190]，MAVEN [0.070, 0.139]，均不含 0），CI 比 pair-level 更宽但结论一致
- **W4**：count_22 和 count_44 的 CI 大幅重叠，置换检验 p=0.31，非单调性在采样变异内
- **W2**：Typical gap 仅 2.2pp [0.4, 4.0]pp，是 extreme 31.2pp 的约 7%

---
