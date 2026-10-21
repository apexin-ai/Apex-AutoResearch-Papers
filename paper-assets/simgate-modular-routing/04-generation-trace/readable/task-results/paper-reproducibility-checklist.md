# paper reproducibility checklist

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_reproducibility-checklist_20260521T093338_result.json`
- **Structured JSON:** [`e802ea52e36d8b3443b1.json`](../../sessions/e8/e802ea52e36d8b3443b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## ARR Responsible NLP Research Checklist 自查报告

---

### 1. 实验超参数

**✅ 已覆盖：**
- Router 训练全部超参数：lr, batch size, epochs, gradient accumulation, warmup, weight decay, max_seq_len=512, optimizer=AdamW, LoRA r/α=16/32, seeds — `main.tex` Appendix I (Table 4, L338-354)
- 数据收集 backbone：Qwen2.5-7B-Instruct + vLLM — `method.tex` L29, checklist C4
- Episode 上限：T_max=30 steps — `method.tex` L21
- 跨模型验证：Llama-3.1-8B-Instruct, Gemma-2-9B-it, Qwen2.5-72B-Instruct — `experiments.tex` §5.2, §5.3
- Router 模型：Qwen3-0.6B/1.7B/4B — Appendix I, P
- Reflexion 试验次数：N=3,4,5 — `experiments.tex` §5.3

**❌ 缺失：**
1. **Agent 推理时的 temperature / sampling 参数**（top-p, top-k, temperature）：全文未提及 Qwen2.5-7B 等模型做 agent 推理时的生成参数。**建议补在 Appendix I 或 Method §3.2**。
2. **ReAct prompt template**：仅引用了 ReAct 论文，但实际使用的 system prompt / few-shot template 未展示。**建议补在 Appendix（新增 prompt 模板 appendix 或放在 Appendix I）**。
3. **Reflexion 的 self-reflection prompt**：未给出具体 prompt。**建议补在 Appendix**。
4. **vLLM 版本号**：未指定。**建议补在 Appendix I 脚注**。
5. **HuggingFace Model ID**：写的是 "Qwen2.5-7B-Instruct" 而非精确 HF ID（如 `Qwen/Qwen2.5-7B-Instruct`）。名称基本无歧义但 reviewer 可能要求精确 ID。**建议在首次出现时用脚注补上精确 HF model ID**。
6. **MATH code interpreter 的具体配置**：用了什么 code interpreter（Python sandbox? 具体实现?）。**建议补在 §5.4 或 Appendix L**。

**⚠️ 部分覆盖：**
- Router 训练的 `enable_thinking=False` 已提及（Appendix J），但 agent 推理阶段是否也关闭 thinking 未说明。

---

### 2. 计算资源描述

**✅ 已覆盖：**
- GPU 型号：2× NVIDIA RTX 5090 (32GB) + 4× NVIDIA RTX 6000 PRO (96GB) — Ethics Statement (`main.tex` L49)
- 总 GPU-hours：约 200 GPU-hours — Ethics Statement
- 碳排放：约 25 kg CO₂eq — checklist C1 (`responsibleNLPchecklist.tex` L48)

**❌ 缺失：**
1. **每个实验的 GPU-hours 分解**：200 GPU-hours 是总数，但未分解为 data collection (ScienceWorld/MATH/ALFWorld)、router training、evaluation 各多少。**建议在 Ethics Statement 或 Appendix 中补一个 breakdown table**。
2. **推理 vs 训练的资源区分**：未说明哪些 GPU-hours 花在推理（episode collection）、哪些花在训练（router LoRA fine-tuning）。**建议至少给粗略比例**。
3. **72B 模型的推理资源**：72B 模型 255 episodes 的推理成本（需要多少 GPU/多长时间）未单独说明。**建议补在 §5.3 或 Appendix**。

---

### 3. 数据集版本/来源

**✅ 已覆盖：**
- ScienceWorld：引用 \cite{scienceworld-2022}，30 task types，11 selected，per-task episode counts in Table 2 (`main.tex` L124-150)，排除原因详细说明 (Appendix C)
- MATH：Level 4-5，N=795，引用 \cite{math-2021} — `experiments.tex` L80
- ALFWorld：6 task types（per-task breakdown in Table 7），135 games，引用 \cite{alfworld-2021} — `experiments.tex` L82, Appendix L
- 数据划分方式：episode-level cross-validation，8 seeds — Appendix J
- 开源许可：Apache 2.0 / MIT — Ethics Statement

**❌ 缺失：**
1. **ScienceWorld 版本号**：未指定具体版本（如 v1.0, v1.1, 或 commit hash）。**建议在 Method §3.2 首次提及时补上版本号或 pip 包版本**。
2. **MATH 具体 subset 类型**：仅写 "Level 4-5"，但 MATH 有 7 个类型（Algebra, Counting & Probability, Geometry, Intermediate Algebra, Number Theory, Prealgebra, Precalculus）。795 题是全部 Level 4-5 还是某些类型？**建议在 §5.4 或 Appendix L 补上 subset 分布**。
3. **ALFWorld 版本号**：未指定。**建议在首次提及时补上**。
4. **MATH 数据来源**：是用 HuggingFace datasets 上的版本还是原始 GitHub？**建议脚注说明**。

**⚠️ 部分覆盖：**
- ScienceWorld task type 列表完整（included + excluded 全部 30 个），但 episode 具体如何抽样的细节（random seed 如何选 task variation）描述较简略。

---

### 4. 统计检验方法

**✅ 已覆盖：**
- Bootstrap B=10,000 — `method.tex` L70, `experiments.tex` §5.1
- 95% CI for DAF: [81.1%, 99.0%] — `experiments.tex` §5.1
- Pearson r = 0.97, Spearman ρ = 0.986 — `experiments.tex` §5.1, Appendix D
- Bootstrap CI for correlation: [0.952, 0.995] — Appendix D
- p-values: 多处报告（p < 10⁻⁶, p = 0.81 for MATH, p = 0.002 for permutation, p < 0.001 for cluster）
- Cohen's d = 3.02 — Appendix E (Table 3)
- Wild cluster bootstrap (K=11, B=9,999) — Appendix E
- Exact permutation test (2,048 perms) — Appendix E
- Sign test — Appendix E
- McNemar test for MATH — `experiments.tex` L80
- Wilson CIs for dose-response — `experiments.tex` Fig. 3
- Bonferroni correction (8 comparisons for router) — `experiments.tex` L114
- Minimum detectable effect (8pp, α=0.05, 80% power) — `experiments.tex` L65
- Mann-Whitney for reasoning depth ablation — Appendix P
- ICC discussion — Appendix E

**⚠️ 部分覆盖：**
1. **多重比较校正**：Bonferroni 仅在 router 的 8 comparisons 提到一次。全文有多处 hypothesis test（correlation, cluster, MATH, dose-response 等），但未系统讨论是否需要对所有比较做校正。不过大部分 p 值极小（< 0.001），校正后仍显著。**建议在 Limitations 或 Method 中加一句说明多重比较策略**。
2. **部分 claim 缺 CI**：如 Reflexion 死亡率从 42.9% 降到 31.4% 的差异没有 CI（仅在 dose-response 图中有 Wilson CI）。72B 的 DAF=92.4% 没有 CI（Table 8 中标 "---"）。**建议补上 72B 和 Gemma 的 DAF CI**。

---

### 5. 代码/数据可用性声明

**⚠️ 部分覆盖：**
- Ethics Statement: "Code and data will be released upon acceptance" — `main.tex` L49

**❌ 缺失：**
1. **匿名 repo 链接**：ARR 审稿阶段通常期望提供 anonymous GitHub/GitLab 链接（如 `https://anonymous.4open.science/r/...`），当前论文没有。**强烈建议在 Ethics Statement 或 Abstract 末尾补上匿名 repo 链接**。
2. **数据可获取性的独立声明**：虽然说 "code and data will be released"，但未说明数据格式、大小、是否包含 raw episodes 等。**建议补一句说明发布内容（counterfactual episode pairs, router training data, evaluation scripts 等）**。
3. **Environment reproducibility**：ScienceWorld/ALFWorld/MATH 的安装和复现指引未提及。**可选：在 repo 中提供 environment setup 说明即可**。

---

## 总结

| 维度 | 完成度 | 评级 |
|------|--------|------|
| 1. 实验超参数 | ~70% | ⚠️ Router 部分完整，agent 推理参数和 prompt 缺失 |
| 2. 计算资源 | ~60% | ⚠️ 有总数和 GPU 型号，缺分解 |
| 3. 数据集版本 | ~70% | ⚠️ 有引用和 task 列表，缺版本号和 MATH subset |
| 4. 统计检验 | ~90% | ✅ 非常详尽，少量 CI 缺失 |
| 5. 代码/数据可用性 | ~30% | ❌ 仅有承诺，无匿名链接 |

### Critical Items（必须补充）

1. **匿名 repo 链接** — reviewer 高频扣分点，优先级最高
2. **Agent 推理的 temperature/sampling 参数** — reproducibility 基本要求
3. **ReAct / Reflexion prompt template** — 至少放一个示例在 Appendix
4. **ScienceWorld 版本号** — 一行即可
5. **MATH 具体 subset 分布** — reviewer 可能质疑选择偏差
6. **GPU-hours 分解**（推理 vs 训练）— checklist C1 的细化要求
7. **72B DAF 的 CI** — Table 8 中标 "---" 会引起注意

### Nice-to-have（建议补充但非 critical）

- vLLM 版本号
- 精确 HuggingFace Model ID
- ALFWorld 版本号
- MATH code interpreter 实现细节
- 多重比较策略的整体说明

---
