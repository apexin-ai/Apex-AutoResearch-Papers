# paper round5 edits

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_round5-edits_20260516T064949_result.json`
- **Structured JSON:** [`d4a52e69d60053249111.json`](../../sessions/d4/d4a52e69d60053249111.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits are complete. Let me produce the final summary of changes per file.

---

## 变更摘要

### **main.tex**
- 标题改为 "Component Ablation for Trace-Based Verdict Prediction"
- Abstract: 14.96pp 处加括号说明 truncation confound (91.7%)
- Abstract: 26%/74% 加 "approximately" 和 "suggesting" 替代 "establishing"
- Abstract: 新增 scope 限定句 "Evaluated on two 7B-scale code-specialized models across two Python benchmarks."
- Limitations: seed123 归因改为 "we hypothesize reflects LoRA initialization sensitivity...though direct evidence is lacking"
- Limitations: 新增第六/七条（self-familiarity bias, error distribution bias），共 3 句

### **introduction.tex**
- 14.96pp 两处加括号 confound 说明
- 26%/74% 三处改为 "approximately"/"suggesting"
- "decompose why" 改为 "approximately decompose"

### **experiments.tex**
- Table 1 caption: "LoRA outlier" → "hypothesized LoRA sensitivity"
- Table 2: ae_only 改为 3-seed 均值 99.64%†，exception_only 加粗
- Table 2 caption: 新增多 seed 注释说明 σ=0 vs σ=0.49
- 正文：ae_only/exception_only 描述更新为多 seed 结果
- seed 123: "LoRA initialization outlier" → "hypothesized LoRA initialization sensitivity"
- 14.96pp: 加入 "(91.7% of DeepSeek training samples were affected)"
- Table 3 caption: "Information density decomposition" → "Approximate information density decomposition"
- 正文: "accounts for" → "corresponds to approximately...this is an approximate decomposition as the two factors may interact"

### **discussion.tex**
- 新增 §"Why exception_only outperforms ae_only"（ae_only ⊃ exception_only，σ=0.49 vs 0）
- 新增 §"SFT vs. regex incremental analysis"（B5 vs SFT 边缘样本分析，精确措辞已使用）
- 新增 §"Format marker sensitivity"（从 Appendix 提到正文）
- 新增 §"Tier hierarchy: practical implications"（工程意义）

### **related_work.tex**
- 新增 §"Fault Localization"（~150 words），引用 Ochiai, Tarantula, DStar, AutoFL, AgentFL, LLM4FL, Mukherjee et al.
- 26%/74% 加 "approximate"

### **conclusion.tex**
- 14.96pp 加括号 confound 说明
- 26%/74% 加 "approximately"

### **references.bib**
- 删除 4 个 orphan 条目：`jung2025execution`, `yang2025apsg`, `yadavally2024ndslicer`, `wu2026runtime`
- 新增 7 个 FL ���目：`abreu2007accuracy`, `jones2002visualization`, `wong2014dstar`, `kang2024autofl`, `qin2024agentfl`, `widyasari2024llm4fl`, `mukherjee2025llmfl`

### **appendix.tex**
- ae_only 表格：[TODO] 填入 99.08 / 99.92，mean 99.64±0.49
- 表格 caption 更新
- 14.96pp confound 说明
- seed123 归因改为推测性

### 无需修改
- Task 1: McNemar p=0.041 已正确归属 B5
- Task 2: Conclusion 未将 DebugBench 列为 future work
- Task 3: Figure 编号连续（自动编号，无跳跃）

---
