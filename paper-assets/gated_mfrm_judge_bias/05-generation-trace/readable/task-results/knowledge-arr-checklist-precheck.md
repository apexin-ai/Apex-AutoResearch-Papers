# knowledge arr checklist precheck

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_arr_checklist_precheck_20260524T071755_result.json`
- **Structured JSON:** [`1d4413718e6af88542c4.json`](../../sessions/1d/1d4413718e6af88542c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## ARR Responsible NLP Checklist 预检报告

### Limitations ✅ 已覆盖

位置：`main.tex:40` 的 `\section*{Limitations}` → 输入 `limitations.tex`。放在正文、bibliography 之前，符合 EMNLP 规则。

覆盖 3 个点：
1. **单一 benchmark + 稀疏性**：仅用 Arena-Hard，fill rate 有占位符未填；Stage 2 依赖 gpt-4-0314 anchor 需定期重评
2. **CI 覆盖率 / 后验过度自信**：c_n 95% CI 实际覆盖仅 71%（N=50）/68%（N=8），源于乘法耦合和 HalfNormal 边界约束；rank-1 假设限制
3. **统计功效不足**：N=8 仅 ~50% power，需 N≈17 达 80% power；未做完整的 self-evaluation 排除分析

末尾有代码/数据发布声明。内容偏长但实质到位。

---

### Ethical Considerations ⚠️ 部分覆盖

- **有**：Appendix `\section{Use of AI Assistants}`（`appendix.tex:459`）披露了 Claude 的使用
- **缺**：没有独立的 `\section*{Ethical Considerations}` 或 `\section*{Ethics Statement}` 讨论 LLM evaluation bias 对模型排名、下游部署决策的潜在影响

**建议**：在 `main.tex` 的 `\section*{Limitations}` 之后、`\bibliography` 之前加一个 `\section*{Ethical Considerations}`，简短写 2-3 句：(1) G-MFRM 排名校正可能影响模型选择决策；(2) contamination susceptibility 分数不应作为训练数据合规性的唯一依据；(3) judge bias 参数反映评分倾向而非模型质量判断。

---

### Compute Budget ❌ 缺失

`experiments.tex` 仅报告了 MCMC 配置（4,000 warmup + 4,000 sampling, 4 chains），**未提及**：
- GPU 类型
- 单次 MCMC 拟合的 wall-clock 时间
- LLM judge API 调用成本（9 judges × 17 models × 176 items × position swap）
- 总实验计算量

**建议**：在 `experiments.tex` 的 Setup 段末尾加一个 `\paragraph{Compute budget.}`，报告 GPU 型号、单次拟合时间、API 调用总数和估计成本。

---

### Reproducibility ⚠️ 部分覆盖

- `limitations.tex:7`："Code and data will be released upon acceptance at [anonymized URL]." — 仅一句
- `experiments.tex` 报告了 MCMC 超参（warmup/sampling/chains/acceptance）、prior 规格、Stage 2 权重配置
- **缺**：未明确说明随机种子策略、软件版本（NumPyro/JAX 版本）、exact judge prompt template 是否在附录或代码包中

**建议**：将代码/数据声明从 limitations.tex 移到 experiments.tex 末尾或 conclusion，补充说明代码包含完整 prompt templates、配置文件和预处理脚本。

---

### Human Subjects ✅ N/A

无人类实验，checklist 中选 N/A 即可，论文无需额外说明。

---

### 额外发现：占位符未填

`experiments.tex:7` 有未填占位符：
- `XX{,}XXX of XX{,}XXX potential cells`
- `XX.X\% fill rate`

提交前必须填入实际数值。

---
