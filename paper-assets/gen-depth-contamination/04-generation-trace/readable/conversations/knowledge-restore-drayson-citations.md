# knowledge restore drayson citations

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 0
- **Tool calls:** 16
- **Original source:** `logs/chats/worker_knowledge_restore_drayson_citations_20260513T012807.jsonl`
- **Structured JSON:** [`620e2bb91c1f61684951.json`](../../sessions/62/620e2bb91c1f61684951.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

33 recorded events

### Tool call

_source line 1 · 2026-05-13T01:30:59.047283+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/related_work_structure.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_restore_drayson_citations_20260513T012807",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/related_work_structure.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-13T01:30:59.047645+00:00_

1	# Related Work 结构笔记
2	
3	> 四个 thread 的核心论文梳理，每个 thread 说明与本工作的定位关系。
4	
5	---
6	
7	## Thread 1: Binary Synthetic Text Detection → 我们扩展到 Ordinal Depth
8	
9	**核心问题**：现有检测方法将合成文本视为 binary label（human vs. machine），忽略了代际深度这一关键维度。
10	
11	**核心论文**：
12	
13	1. **Min-K%++ (Zhang et al., ICLR 2025)**
14	   - 通过 token probability 分析检测 pre-training membership，改进了 Min-K% 基线
15	   - 局限：membership inference ≠ ordinal depth estimation；仅判断"是否在训练集中"，无法回答"经过了几代生成"
16	   - 与我们的关系：Min-K% 的 low-probability token fraction 是我们 token-level 特征的子集；我们证明这些特征可以做更细粒度的 ordinal prediction
17	
18	2. **DivEye (Basani & Chen, TMLR 2026)**
19	   - 9 个 surprisal-based 统计特征（分布矩 + 一阶/二阶差分）用于可解释的 binary 检测，超过 zero-shot baseline 33.2%
20	   - 局限：纯 binary 分类，未利用特征随 depth 变化的系统性趋势
21	   - 与我们的关系：DivEye 的 9 维 surprisal 特征是我们特征集的核心子集；我们扩展为 ordinal regression 输入，证明同一特征集可支撑 depth 分辨
22	
23	3. **DetectGPT (Mitchell et al., ICML 2023)**
24	   - 利用 log probability curvature（perturbation-based）检测 machine-generated text
25	   - 后续改进：DNA-GPT、Fast-DetectGPT 等
26	   - 与我们的关系：zero-shot detection 方法的 confidence score 理论上可作为 depth proxy（confidence ↑ with depth），但我们在 baseline 对比中验证其与 true depth 的 Spearman 相关性，预期弱于专用 ordinal classifier
27	
28	4. **Binoculars (Hans et al., ICML 2024)**
29	   - 使用两个 LM 的 perplexity 比值检测合成文本
30	   - 与我们的关系：另一种 binary detection confidence → depth proxy 的 baseline
31	
32	**我们的定位**：从 binary classification 升级为 ordinal regression。不是提出新的检测特征，而是证明已有特征（DivEye-style + 扩展）在 ordinal depth 维度上有系统性可分辨结构，且 ordinal signal 对下游 data curation 有实用价值。
33	
34	---
35	
36	## Thread 2: Model Collapse / Iterative Retraining → 我们量化代际退化边界
37	
38	**核心问题**：递归训练导致的模型坍缩已被广泛研究，但缺少从 forensic 视角量化单个文档"经历了几代"的工具。
39	
40	**核心论文**：
41	
42	1. **Shumailov et al. (Nature 2024)**
43	   - 首次系统证明递归训练导致 tail disappearance → diversity loss → mode conflation 的三阶段坍缩
44	   - 早期坍缩（tail loss）比晚期坍缩（mode conflation）发生得更早、更剧烈
45	   - 与我们的关系：他们刻画了 macro 现象（population-level collapse dynamics），我们构建 micro 工具（单文档 depth forensics）。他们的"早期退化最剧烈"观察是我们 K* 假
…[truncated 4804 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_restore_drayson_citations_20260513T012807",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-13T01:30:59.047863+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/methodology_draft.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_restore_drayson_citations_20260513T012807",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/methodology_draft.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-13T01:30:59.048106+00:00_

1	# 3. Methodology
2	
3	## 3.1 Multi-generation Corpus Construction
4	
5	### 问题形式化
6	
7	设 $X_0$ 为人类撰写的文本（seed text），建模为概率空间上的随机变量。LLM 的生成过程定义为随机信道 $\mathcal{T}: \mathcal{X} \to \mathcal{X}$，将输入文本映射到输出文本。递归生成形成 Markov chain：
8	
9	$$X_0 \xrightarrow{\mathcal{T}} X_1 \xrightarrow{\mathcal{T}} X_2 \xrightarrow{\mathcal{T}} \cdots \xrightarrow{\mathcal{T}} X_K$$
10	
11	其中 depth-0 文本 $X_0$ 为人类原始文本，depth-$k$ 文本 $X_k = \mathcal{T}(X_{k-1})$ 由 depth-$(k-1)$ 文本经过一次 LLM 信道产生。该形式化依赖两个关键假设：**(A1) 时不变信道**——同一 LLM 与 decoding strategy 在每次迭代中定义相同的信道 $\mathcal{T}$；**(A2) Markov 性**——$X_{k+1}$ 仅依赖 $X_k$，不依赖更早的 $X_0, \ldots, X_{k-1}$。这两个假设在 prompt-chain 设定下成立（每次生成仅以上一轮输出为输入），retrain-chain 场景需将 $\mathcal{T}$ 放宽为 $\mathcal{T}_k$。
12	
13	### Prompt-chain 实现
14	
15	我们采用 prompt-chain 方式构造 depth chain：每一轮将前一深度的文本嵌入固定的 rewrite prompt 模板，由模型生成同主题、同风格的新文本。具体 prompt 模板如下：
16	
17	> Below is a passage. Write a new passage of similar length on the same topic and in the same style.
18	>
19	> Original passage:
20	> {prev\_text}
21	>
22	> New passage:
23	
24	该模板要求模型保持主题与风格一致性，同时生成全新文本而非简单复述。这一设计的意图是模拟现实场景中合成文本被反复改写的过程——例如 AI 生成的内容被爬取后再次作为 LLM 的输入进行改写或续写。
25	
26	Prompt-chain 与 retrain-chain（在合成数据上重新训练模型再生成）的区别值得说明。Retrain-chain 更接近 Shumailov et al. [2024] 描述的 model collapse 真实路径，但 prompt-chain 提供了一个 **upper bound estimate**：如果在 prompt-chain（模型权重不变、仅输入文本退化）下特征已饱和，retrain-chain（模型本身也退化）下只会更快饱和。我们选择 prompt-chain 作为 MVP 方案以控制变量，retrain-chain 验证留作后续研究。
27	
28	### 模型选择
29	
30	我们选用 **Qwen2.5-1.5B-Instruct** [Qwen Team, 2024] 作为生成模型。选择理由如下：
31	
32	**Instruct 而非 base 模型**。现实世界中绝大多数合成文本（ChatGPT 输出、AI 写作工具、自动摘要等）均来自经过 instruction tuning 的模型。使用 Instruct 版本可确保生成文本的分布特征更接近实际污染数据。此外，Instruct 模型能更好地遵循 rewrite prompt 中的改写指令，生成主题一致但非直接复制的文本，而 base 模型可能简单延续原文或产生不相关内容。
33	
34	**1.5B 参数规模**。选择小规模模型基于以下考量：(1) 计算效率——在单块 RTX 4090D (24GB) 上可高效完成 5000 文档 × 5 个深度的生成任务；(2) model collapse 文献 [Shumailov et al., 2024; Drayson et al., 2025] 表明退化现象在小模型上更为显著，有利于在 pilot study 中观察清晰的深度信号；(3) Qwen2.5 系列在 1.5B 规模上已展现出 competitive 的语言能力 [需验
…[truncated 11648 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_restore_drayson_citations_20260513T012807",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-13T01:30:59.048275+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/full_study_plan.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_restore_drayson_citations_20260513T012807",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/full_study_plan.md"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-13T01:30:59.048481+00:00_

1	# Full Study 实验矩阵预案
2	
3	> 基于 MVP (Qwen2.5-1.5B-Instruct, C4 5K, depth 0→5, nucleus p=0.95 T=1.0) 的经验推算
4	> 目标: EMNLP ARR 2026-05-25 提交（剩余 13 天）
5	> 硬件: 1×RTX 4090D 24GB @ autodl-4090d
6	
7	---
8	
9	## 1. 实验矩阵
10	
11	### 维度 1：模型族
12	
13	| 模型 | 参数量 | 类型 | HuggingFace 路径 | ModelScope 路径 | VRAM (bf16) | 4090D 可行性 | 推荐 batch_size | 目的 |
14	|------|--------|------|-------------------|-----------------|-------------|-------------|----------------|------|
15	| Qwen2.5-1.5B-Instruct | 1.5B | Instruct | `Qwen/Qwen2.5-1.5B-Instruct` | `Qwen/Qwen2.5-1.5B-Instruct` | ~3GB | ✅ 余量 21GB | gen=64, feat=24 | MVP baseline，Instruct 代表真实污染源 |
16	| Pythia-1.4B | 1.4B | Base | `EleutherAI/pythia-1.4b` | N/A（用 HF_ENDPOINT mirror） | ~2.8GB | ✅ 余量 21GB | gen=64, feat=24 | Base vs Instruct 对比；GPT-NeoX 架构代表 |
17	| OLMo-1B | 1B | Base | `allenai/OLMo-1B-0724-hf` | N/A（用 HF_ENDPOINT mirror） | ~2GB | ✅ 余量 22GB | gen=64, feat=32 | 不同训练方法/数据的 base model family |
18	| Qwen2.5-7B-Instruct | 7B | Instruct | `Qwen/Qwen2.5-7B-Instruct` | `Qwen/Qwen2.5-7B-Instruct` | ~14GB | ✅ 余量 10GB | gen=8, feat=4 | Cross-scale: K* 是否随模型规模变化 |
19	
20	**注**: Pythia/OLMo 在 ModelScope 无官方仓库，AutoDL 下载需设 `HF_ENDPOINT=https://hf-mirror.com`。Qwen 系列优先走 ModelScope CDN。
21	
22	### 维度 2：解码策略消融
23	
24	| ID | 策略 | 参数 | 目的 | 与 MVP 关系 |
25	|----|------|------|------|-------------|
26	| D-greedy | Greedy | T→0 (do_sample=False) | 确定性下界：最大 mode collapse，预测 K* 最小 | 新增 |
27	| D-p90 | Nucleus p=0.9 | top_p=0.9, T=1.0 | p 值敏感性 | 新增 |
28	| D-p95 | Nucleus p=0.95 | top_p=0.95, T=1.0 | MVP 默认 | 已有 |
29	| D-lowT | Low temperature | top_p=0.95, T=0.7 | 温度降低 → 多样性下降速度加快? | 新增 |
30	| D-highT | High temperature | top_p=0.95, T=1.2 | 温度升高 → 延缓饱和? 支撑 MI 衰减假设检验 | 新增 |
31	
32	**核心假设检验**: greedy → 近指数 MI 衰减（快速饱和），high-T → 较慢多项式衰减（随机性延缓同质化）。用 AIC/BIC 对比拟合优度。
33	
34	### 维度 3：生成方式
35	
36	| 方式 | 配置 | 预估耗时 | 目的 |
37	|------|------|----------|------|
38	| Prompt-chain | 直接喂上一代输出给 LLM，用 rewrite prompt | ~2-2.5h/config (1.5B) | Upper bound，MVP 已验证 |
39	| 
…[truncated 11656 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_restore_drayson_citations_20260513T012807",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-13T01:30:59.048641+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/ROADMAP.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_restore_drayson_citations_20260513T012807",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/ROADMAP.md"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-13T01:30:59.048804+00:00_

1	# gen-depth-contamination — Research Dashboard
2	
3	> 最后更新: 2026-05-13 01:08 UTC | 更新原因: Reviewer 建议: exp-013 加 exp-017 依赖 (4×4 matrix), 文献整合任务合并 Drayson positioning
4	
5	## 核心方向
6	递归合成文本的代际深度估计：测量 K*_empirical（给定特征族下的 practical discrimination boundary），为 depth-aware data curation 提供 actionable guidance。Route B framing（K* 作为首次系统测量的 operational quantity）。Drayson et al. (EMNLP 2025) = closest prior work (binary filtering 防 collapse)，我们是 ordinal 推广。详见 paper_framing.md。
7	
8	## 当前进展
9	- **阶段**: Research（P0 实验推进中）+ 审稿通道已开
10	- **MVP**: K*=2 confirmed (Qwen2.5-1.5B, mvp-001 success)
11	- **exp-001 (Pythia-1.4B)**: DONE — K*=2, 跨模型验证完成
12	- **exp-002 (OLMo-1B)**: RUNNING (depth 3 进行中, ~1.5h 完成)
13	- **Dream**: D005 整合 8 项行动项; D006 回滚 Drayson 引用清理
14	- **覆盖率**: 2/10 P0 完成 (mvp-001, exp-001)
15	
16	## 近期任务
17	- [ ] exp-002 OLMo-1B depth chain（RUNNING, ~1.5h）
18	- [ ] exp-017 Qwen continuation mode control（exp-002 后立即启动）
19	- [ ] exp-013 cross-model transfer — 4×4 matrix（依赖 exp-001 + exp-002 + exp-017）
20	- [ ] exp-003 decoding strategy ablation（依赖 GPU）
21	- [ ] exp-005 degradation ordering analysis（依赖 exp-001 + exp-002）
22	- [ ] exp-007 K* sensitivity + bootstrap CI（依赖 exp-001/002/003）
23	- [ ] 文献整合：Drayson positioning (binary→ordinal generalization) + Schaeffer ICML'25 (K* 定义族) + Kazdan ICML'25 (accumulate vs replace) + He NeurIPS'25 (gen→mem)
24	- [ ] [Dream 观察] exp-013 结果出来后评估 cross-model transfer framing 是否 misleading
25	- [ ] [Dream 观察] exp-006 设计时确认 DSIR baseline 实现可行性
26	
27	## GPU 预算
28	- 分配：1×RTX 4090D (cuda:0) on autodl-4090d
29	- P0 总预算：~123h（含 Dream 调整后的 exp-006=72h, exp-007=2h）
30	- 已消耗：~18h (mvp-001 + exp-001)
31	- 剩余可用：~240h
32	
33	## 实验序列规划
34	exp-002 (6h) → exp-017 (6h) → exp-013 (2h, 纯分析, 4×4 transfer matrix) → exp-003 (20h) → exp-005 (2h, 纯分析) → exp-007 (2h, 纯分析) → exp-004 (8h) → exp-006 (72h, 最重 C3 证据)
35	
36	## 关键决策日志
37	
38	| ID | 日期 | 摘要 | 关联实验 |
39	|----|------|------|----------|
40	| D006 | 2026-05-13 | 回滚 Drayson et al. 引用清理——Reviewer 确认为真实论文 (EMN
…[truncated 485 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_restore_drayson_citations_20260513T012807",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-13T01:30:59.049043+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "幻觉|Drayson",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_restore_drayson_citations_20260513T012807",
  "tool": "Grep",
  "tool_args": {
    "pattern": "幻觉|Drayson",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-13T01:30:59.049256+00:00_

&lt;persisted-output>
Output too large (29.3KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/2d5c486d-f470-4b1c-9c9c-4d70b10a5d55/tool-results/toolu_0131adT3gQcqkvWoy6AXZsEg.txt

Preview (first 2KB):
decisions.yaml:53:    CI + permutation-test; (5) exp-015 从 P2 升 P1; (6) 3-class accuracy 显式报告。6 项观察项待真实实验验证：Drayson
decisions.yaml:70:  summary: '回滚 Drayson et al. 引用清理——Reviewer 确认为真实论文 (EMNLP 2025 #1506)'
decisions.yaml:71:  rationale: D005 中基于 web search 无结果将 Drayson et al. (2025) 判定为 Dream 幻觉引用并指示 Agent
decisions.yaml:74:    web search 不足以判定引用为幻觉，应交叉验证（arXiv ID + 作者机构 + 会议 proceedings）。
ROADMAP.md:3:> 最后更新: 2026-05-13 01:08 UTC | 更新原因: Reviewer 建议: exp-013 加 exp-017 依赖 (4×4 matrix), 文献整合任务合并 Drayson positioning
ROADMAP.md:6:递归合成文本的代际深度估计：测量 K*_empirical（给定特征族下的 practical discrimination boundary），为 depth-aware data curation 提供 actionable guidance。Route B framing（K* 作为首次系统测量的 operational quantity）。Drayson et al. (EMNLP 2025) = closest prior work (binary filtering 防 collapse)，我们是 ordinal 推广。详见 paper_framing.md。
ROADMAP.md:13:- **Dream**: D005 整合 8 项行动项; D006 回滚 Drayson 引用清理
ROADMAP.md:23:- [ ] 文献整合：Drayson positioning (binary→ordinal generalization) + Schaeffer ICML'25 (K* 定义族) + Kazdan ICML'25 (accumulate vs replace) + He NeurIPS'25 (gen→mem)
ROADMAP.md:40:| D006 | 2026-05-13 | 回滚 Drayson et al. 引用清理——Reviewer 确认为真实论文 (EMNLP 20 | — |
docs/IDEA_BRIEF.md:34:[Omitted long matching line]
docs/IDEA_BRIEF.md:44:[Omitted long matching line]
docs/IDEA_BRIEF.md:46:[Omitted long matching line]
docs/IDEA_BRIEF.md:56:[Omitted long matching line]
docs/IDEA_BRIEF.md:82:- Machine-generated text detection prevents language model collapse (Drayson et al., EMNLP 2025)
docs/IDEA_BRIEF.md:105:  - novelty: **{'rationale': 'Verified novel across 14+ targeted searches: no existing work frames generational depth estimation as a prediction task. Drayson et al. (EMNLP 2025) and Guo et al. (NAACL 202
…[truncated 292 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_restore_drayson_citations_20260513T012807",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-13T01:30:59.049445+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/2d5c486d-f470-4b1c-9c9c-4d70b10a5d55/tool-results/toolu_0131adT3gQcqkvWoy6AXZsEg.txt",
  "offset": "0",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_restore_drayson_citations_20260513T012807",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/2d5c486d-f470-4b1c-9c9c-4d70b10a5d55/tool-results/toolu_0131adT3gQcqkvWoy6AXZsEg.txt",
    "offset": "0",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-13T01:30:59.049662+00:00_

0	decisions.yaml:53:    CI + permutation-test; (5) exp-015 从 P2 升 P1; (6) 3-class accuracy 显式报告。6 项观察项待真实实验验证：Drayson
1	decisions.yaml:70:  summary: '回滚 Drayson et al. 引用清理——Reviewer 确认为真实论文 (EMNLP 2025 #1506)'
2	decisions.yaml:71:  rationale: D005 中基于 web search 无结果将 Drayson et al. (2025) 判定为 Dream 幻觉引用并指示 Agent
3	decisions.yaml:74:    web search 不足以判定引用为幻觉，应交叉验证（arXiv ID + 作者机构 + 会议 proceedings）。
4	ROADMAP.md:3:> 最后更新: 2026-05-13 01:08 UTC | 更新原因: Reviewer 建议: exp-013 加 exp-017 依赖 (4×4 matrix), 文献整合任务合并 Drayson positioning
5	ROADMAP.md:6:递归合成文本的代际深度估计：测量 K*_empirical（给定特征族下的 practical discrimination boundary），为 depth-aware data curation 提供 actionable guidance。Route B framing（K* 作为首次系统测量的 operational quantity）。Drayson et al. (EMNLP 2025) = closest prior work (binary filtering 防 collapse)，我们是 ordinal 推广。详见 paper_framing.md。
6	ROADMAP.md:13:- **Dream**: D005 整合 8 项行动项; D006 回滚 Drayson 引用清理
7	ROADMAP.md:23:- [ ] 文献整合：Drayson positioning (binary→ordinal generalization) + Schaeffer ICML'25 (K* 定义族) + Kazdan ICML'25 (accumulate vs replace) + He NeurIPS'25 (gen→mem)
8	ROADMAP.md:40:| D006 | 2026-05-13 | 回滚 Drayson et al. 引用清理——Reviewer 确认为真实论文 (EMNLP 20 | — |
9	docs/IDEA_BRIEF.md:34:[Omitted long matching line]
10	docs/IDEA_BRIEF.md:44:[Omitted long matching line]
11	docs/IDEA_BRIEF.md:46:[Omitted long matching line]
12	docs/IDEA_BRIEF.md:56:[Omitted long matching line]
13	docs/IDEA_BRIEF.md:82:- Machine-generated text detection prevents language model collapse (Drayson et al., EMNLP 2025)
14	docs/IDEA_BRIEF.md:105:  - novelty: **{'rationale': 'Verified novel across 14+ targeted searches: no existing work frames generational depth estimation as a prediction task. Drayson et al. (EMNLP 2025) and Guo et al. (NAACL 2024) characterize feature evolution across generations descriptively, but neither builds a depth classifier or proposes depth-aware filtering. The ordinal depth estimation formulation and graduated filtering application are genuinely new contributions.', 'score':
…[truncated 13270 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_restore_drayson_citations_20260513T012807",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-13T01:30:59.049876+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/related_work_structure.md",
  "old_string": "4. **Alemohammad et al. (ICLR 2024) — \"Self-Consuming Generative Models Go MAD\"**\n   - 理论与实验分析自消费训练循环（model autophagy disorder），证明迭代训练导致分布退化\n   - 关键贡献：形式化了 fully synthetic / synthetic augmentation / fresh data 三种数据混合策略的退化速率差异\n   - 局限：关注宏观训练退化现象，未提供逐代检测或 depth estimation 工具\n   - 与我们的关系：为递归退化提供了互补的理论视角（自消费 vs 我们的 iterated channel），其 depth-wise 退化曲线与我们的 JSD 衰减一致\n\n**我们的定位**：从 binary quality gate → graduated quality signal。",
  "new_string": "4. **Alemohammad et al. (ICLR 2024) — \"Self-Consuming Generative Models Go MAD\"**\n   - 理论与实验分析自消费训练循环（model autophagy disorder），证明迭代训练导致分布退化\n   - 关键贡献：形式化了 fully synthetic / synthetic augmentation / fresh data 三种数据混合策略的退化速率差异\n   - 局限：关注宏观训练退化现象，未提供逐代检测或 depth estimation 工具\n   - 与我们的关系：为递归退化提供了互补的理论视角（自消费 vs 我们的 iterated channel），其 depth-wise 退化曲线与我们的 JSD 衰减一致\n\n5. **Drayson et al. (EMNLP 2025)**\n   - 训练 MGT 检测器并用 importance resampling 提升训练数据中人类文本的权重，不仅防止 collapse 还提升了性能\n   - 局限：仍是 binary detection（human vs. machine），不估计深度\n   - 与我们的关系：最直接的上游工作——他们用 binary detection 做 collapse prevention，我们用 ordinal depth estimation 做 graduated curation，是 binary → ordinal 的自然推广\n\n**我们的定位**：从 binary quality gate → graduated quality signal。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_restore_drayson_citations_20260513T012807",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/related_work_structure.md",
    "old_string": "4. **Alemohammad et al. (ICLR 2024) — \"Self-Consuming Generative Models Go MAD\"**\n   - 理论与实验分析自消费训练循环（model autophagy disorder），证明迭代训练导致分布退化\n   - 关键贡献：形式化了 fully synthetic / synthetic augmentation / fresh data 三种数据混合策略的退化速率差异\n   - 局限：关注宏观训练退化现象，未提供逐代检测或 depth estimation 工具\n   - 与我们的关系：为递归退化提供了互补的理论视角（自消费 vs 我们的 iterated channel），其 depth-wise 退化曲线与我们的 JSD 衰减一致\n\n**我们的定位**：从 binary quality gate → graduated quality signal。",
    "new_string": "4. **Alemohammad et al. (ICLR 2024) — \"Self-Consuming Generative Models Go MAD\"**\n   - 理论与实验分析自消费训练循环（model autophagy disorder），证明迭代训练导致分布退化\n   - 关键贡献：形式化了 fully synthetic / synthetic augmentation / fresh data 三种数据混合策略的退化速率差异\n   - 局限：关注宏观训练退化现象，未提供逐代检测或 depth estimation 工具\n   - 与我们的关系：为递归退化提供了互补的理论视角（自消费 vs 我们的 iterated channel），其 depth-wise 退化曲线与我们的 JSD 衰减一致\n\n5. **Drayson et al. (EMNLP 2025)**\n   - 训练 MGT 检测器并用 importance resampling 提升训练数据中人类文本的权重，不仅防止 collapse 还提升了性能\n   - 局限：仍是 binary detection（human vs. machine），不估计深度\n   - 与我们的关系：最直接的上游工作——他们用 binary detection 做 collapse prevention，我们用 ordinal depth estimation 做 graduated curation，是 binary → ordinal 的自然推广\n\n**我们的定位**：从 binary quality gate → graduated quality signal。"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-13T01:30:59.050028+00:00_

&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_restore_drayson_citations_20260513T012807",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-13T01:30:59.050155+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/methodology_draft.md",
  "old_string": "- **对数据 curation 从业者**：$K^*$ 告诉你在当前模型和生成配置下，depth-aware filtering 能有效区分多少层深度——depth $\\leq K^*$ 的文本可进行 graduated weighting，depth $> K^*$ 的文本可统一处理。",
  "new_string": "- **对数据 curation 从业者**：$K^*$ 告诉你在当前模型和生成配置下，depth-aware filtering 能有效区分多少层深度——depth $\\leq K^*$ 的文本可进行 graduated weighting，depth $> K^*$ 的文本可统一处理。Drayson et al. (2025) 已证明即使 binary MGT detection 也能通过 importance resampling 防止 model collapse；我们的 depth estimator 将此推广为 graduated、ordinal-aware 的 curation，在可区分范围内提供比 binary 更细粒度的质量信号。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_restore_drayson_citations_20260513T012807",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/methodology_draft.md",
    "old_string": "- **对数据 curation 从业者**：$K^*$ 告诉你在当前模型和生成配置下，depth-aware filtering 能有效区分多少层深度——depth $\\leq K^*$ 的文本可进行 graduated weighting，depth $> K^*$ 的文本可统一处理。",
    "new_string": "- **对数据 curation 从业者**：$K^*$ 告诉你在当前模型和生成配置下，depth-aware filtering 能有效区分多少层深度——depth $\\leq K^*$ 的文本可进行 graduated weighting，depth $> K^*$ 的文本可统一处理。Drayson et al. (2025) 已证明即使 binary MGT detection 也能通过 importance resampling 防止 model collapse；我们的 depth estimator 将此推广为 graduated、ordinal-aware 的 curation，在可区分范围内提供比 binary 更细粒度的质量信号。"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-13T01:30:59.050280+00:00_

&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_restore_drayson_citations_20260513T012807",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-13T01:30:59.050401+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/full_study_plan.md",
  "old_string": "| Binary filter | DivEye 特征二分类移除所有检测为合成的文本 |",
  "new_string": "| Binary filter | DivEye 特征二分类移除所有检测为合成的文本；另设 Drayson et al. (2025) importance resampling 变体作为 binary curation baseline |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_restore_drayson_citations_20260513T012807",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/full_study_plan.md",
    "old_string": "| Binary filter | DivEye 特征二分类移除所有检测为合成的文本 |",
    "new_string": "| Binary filter | DivEye 特征二分类移除所有检测为合成的文本；另设 Drayson et al. (2025) importance resampling 变体作为 binary curation baseline |"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-13T01:30:59.050553+00:00_

&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_restore_drayson_citations_20260513T012807",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-13T01:30:59.050731+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/ROADMAP.md",
  "old_string": "| D006 | 2026-05-13 | 回滚 Drayson et al. 引用清理——Reviewer 确认为真实论文 (EMNLP 20 | — |",
  "new_string": "| D006 | 2026-05-13 | [Dream 观察] Drayson et al. (2025) 经二次验证确认为真实论文（arXiv:2502.15654, EMNLP 2025），已恢复引用（2026-05-13） | — |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_restore_drayson_citations_20260513T012807",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/ROADMAP.md",
    "old_string": "| D006 | 2026-05-13 | 回滚 Drayson et al. 引用清理——Reviewer 确认为真实论文 (EMNLP 20 | — |",
    "new_string": "| D006 | 2026-05-13 | [Dream 观察] Drayson et al. (2025) 经二次验证确认为真实论文（arXiv:2502.15654, EMNLP 2025），已恢复引用（2026-05-13） | — |"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-13T01:30:59.050913+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/ROADMAP.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_restore_drayson_citations_20260513T012807",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-13T01:30:59.051077+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/related_work_structure.md",
  "offset": "85",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_restore_drayson_citations_20260513T012807",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/related_work_structure.md",
    "offset": "85",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-13T01:30:59.051210+00:00_

85	   - "Learning by Surprise"——按 surprise 值过滤训练数据缓解 collapse
86	   - 不区分 human vs. AI text，完全基于 perplexity 信号
87	   - 与我们的关系：Surplexity 是我们 downstream curation 实验的 baseline 之一；depth-aware filtering 预期优于 surprise-only filtering，因为 depth 编码了更多 provenance 信息
88	
89	4. **Alemohammad et al. (ICLR 2024) — "Self-Consuming Generative Models Go MAD"**
90	   - 理论与实验分析自消费训练循环（model autophagy disorder），证明迭代训练导致分布退化
91	   - 关键贡献：形式化了 fully synthetic / synthetic augmentation / fresh data 三种数据混合策略的退化速率差异
92	   - 局限：关注宏观训练退化现象，未提供逐代检测或 depth estimation 工具
93	   - 与我们的关系：为递归退化提供了互补的理论视角（自消费 vs 我们的 iterated channel），其 depth-wise 退化曲线与我们的 JSD 衰减一致
94	
95	5. **Drayson et al. (EMNLP 2025) — "On the Role of Synthetic Text Detection in Model Collapse Prevention"**
96	   - 训练 MGT 检测器做 importance resampling 防止 model collapse，在 GPT-2 和 SmolLM2 (124M–1.7B) 上实验
97	   - 关键贡献：首次将 binary MGT detection 作为 data curation 手段应用于 model collapse prevention
98	   - 局限：仍是 binary detection（synthetic vs human），不估计生成深度（depth）
99	   - 与我们的关系：**最接近的先行工作 (closest prior work)**。他们用 binary MGT detection 做 data curation 防 collapse，我们扩展为 ordinal depth estimation 做 graduated curation——从 binary filtering → graduated weighting 的自然推广。我们的工作回答了 Drayson 未触及的问题：不仅区分 human/synthetic，还估计文本经历了几代递归生成

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_restore_drayson_citations_20260513T012807",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-13T01:30:59.051342+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/methodology_draft.md",
  "offset": "245",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_restore_drayson_citations_20260513T012807",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/methodology_draft.md",
    "offset": "245",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-13T01:30:59.051467+00:00_

245	需要承认的局限：unigram-level JSD 忽略了序列结构（n-gram patterns、句法依赖等），不等价于真正的互信息 $I(X_0; X_k)$。但 DPI 的定性结论——单调衰减——在 JSD 框架下同样成立，因此作为 tracking metric 仍然有效。
246	
247	### $K^*$ 的科学意义
248	
249	$K^*$ 是本工作提出的首次被系统测量的科学量。此前关于递归生成退化的研究 [Shumailov et al., 2024; Alemohammad et al., 2024; Drayson et al., 2025] 主要提供定性描述（"early generations show most change"）或仅做 binary 过滤（synthetic vs human），但从未给出精确的判别边界。Drayson et al. (EMNLP 2025) 是最接近的先行工作——他们训练 MGT 检测器做 importance resampling 防止 model collapse，但仍限于 binary detection，不估计生成深度。我们的 ordinal depth estimation 是其自然推广：从 binary filtering 到 graduated weighting。$K^*$ 的测量具有直接的实践指导价值：
250	
251	- **对数据 curation 从业者**：$K^*$ 告诉你在当前模型和生成配置下，depth-aware filtering 能有效区分多少层深度——depth $\leq K^*$ 的文本可进行 graduated weighting，depth $> K^*$ 的文本可统一处理。
252	- **对 model collapse 研究**：$K^*$ 量化了 Shumailov et al. 描述的 "early collapse" 与 "late collapse" 之间的精确过渡边界。
253	- **对 AI 生成文本检测**：$K^*$ 揭示了 depth estimation 作为检测范式的 fundamental resolution limit——无论特征工程或分类器如何改进，信息论约束决定了 $K^*$ 之外不可能做得更好。
254	
255	[TODO: 补充 MVP 实验中测得的 $K^*$ 实际值及其置信区间]
256	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_restore_drayson_citations_20260513T012807",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-13T01:30:59.051600+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/full_study_plan.md",
  "offset": "50",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_restore_drayson_citations_20260513T012807",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/full_study_plan.md",
    "offset": "50",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-13T01:30:59.051723+00:00_

50	
51	**过滤策略对比**:
52	| 策略 | 说明 |
53	|------|------|
54	| No filter | 全部混入（baseline） |
55	| Binary filter | DivEye 特征二分类移除所有检测为合成的文本 |
56	| Depth-graduated | weight = quality(k)/quality(0)，按深度衰减曲线经验推导权重 |
57	| Surplexity filter | 按 surprisal 高低过滤 |
58	
59	**污染比例**: 10% / 30% / 50% 合成文本注入

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_restore_drayson_citations_20260513T012807",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-13T01:30:59.051897+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/full_study_plan.md",
  "old_string": "| Binary filter | DivEye 特征二分类移除所有检测为合成的文本 |",
  "new_string": "| Binary filter | DivEye 特征二分类移除所有检测为合成的文本；另设 Drayson et al. (2025) importance resampling 变体作为 binary curation baseline |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_restore_drayson_citations_20260513T012807",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/full_study_plan.md",
    "old_string": "| Binary filter | DivEye 特征二分类移除所有检测为合成的文本 |",
    "new_string": "| Binary filter | DivEye 特征二分类移除所有检测为合成的文本；另设 Drayson et al. (2025) importance resampling 变体作为 binary curation baseline |"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-13T01:30:59.052063+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/full_study_plan.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_restore_drayson_citations_20260513T012807",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-13T01:30:59.052198+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Drayson",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_restore_drayson_citations_20260513T012807",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Drayson",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-13T01:30:59.052327+00:00_

docs/IDEA_BRIEF.md:34:[Omitted long matching line]
docs/IDEA_BRIEF.md:44:[Omitted long matching line]
docs/IDEA_BRIEF.md:46:[Omitted long matching line]
docs/IDEA_BRIEF.md:56:[Omitted long matching line]
docs/IDEA_BRIEF.md:82:- Machine-generated text detection prevents language model collapse (Drayson et al., EMNLP 2025)
docs/IDEA_BRIEF.md:105:  - novelty: **{'rationale': 'Verified novel across 14+ targeted searches: no existing work frames generational depth estimation as a prediction task. Drayson et al. (EMNLP 2025) and Guo et al. (NAACL 2024) characterize feature evolution across generations descriptively, but neither builds a depth classifier or proposes depth-aware filtering. The ordinal depth estimation formulation and graduated filtering application are genuinely new contributions.', 'score': 4}**/5
docs/related_work_structure.md:95:5. **Drayson et al. (EMNLP 2025) — "On the Role of Synthetic Text Detection in Model Collapse Prevention"**
docs/related_work_structure.md:99:   - 与我们的关系：**最接近的先行工作 (closest prior work)**。他们用 binary MGT detection 做 data curation 防 collapse，我们扩展为 ordinal depth estimation 做 graduated curation——从 binary filtering → graduated weighting 的自然推广。我们的工作回答了 Drayson 未触及的问题：不仅区分 human/synthetic，还估计文本经历了几代递归生成
docs/methodology_draft.md:34:[Omitted long matching line]
docs/methodology_draft.md:249:[Omitted long matching line]
docs/full_study_plan.md:16:| Pythia-1.4B | 1.4B | Base | `EleutherAI/pythia-1.4b` | N/A（用 HF_ENDPOINT mirror） | ~2.8GB | ✅ 余量 21GB | gen=64, feat=24 | Base vs Instruct 对比；GPT-NeoX 架构代表；与 Drayson et al. (2025) GPT-2 实验规模对齐 |
docs/full_study_plan.md:55:| Binary filter | DivEye 特征二分类移除所有检测为合成的文本；另设 Drayson et al. (2025) importance resampling 变体作为 binary curation baseline |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_restore_drayson_citations_20260513T012807",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-13T01:30:59.052469+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Drayson",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/ROADMAP.md",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_restore_drayson_citations_20260513T012807",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Drayson",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/ROADMAP.md",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-13T01:30:59.052594+00:00_

3:> 最后更新: 2026-05-13 01:08 UTC | 更新原因: Reviewer 建议: exp-013 加 exp-017 依赖 (4×4 matrix), 文献整合任务合并 Drayson positioning
6:递归合成文本的代际深度估计：测量 K*_empirical（给定特征族下的 practical discrimination boundary），为 depth-aware data curation 提供 actionable guidance。Route B framing（K* 作为首次系统测量的 operational quantity）。Drayson et al. (EMNLP 2025) = closest prior work (binary filtering 防 collapse)，我们是 ordinal 推广。详见 paper_framing.md。
13:- **Dream**: D005 整合 8 项行动项; D006 回滚 Drayson 引用清理
23:- [ ] 文献整合：Drayson positioning (binary→ordinal generalization) + Schaeffer ICML'25 (K* 定义族) + Kazdan ICML'25 (accumulate vs replace) + He NeurIPS'25 (gen→mem)
25:- [x] [Dream 观察] Drayson et al. (EMNLP 2025) 确认为真实论文 (arXiv:2502.15654)，已恢复所有引用
41:| D006 | 2026-05-13 | [Dream 观察] Drayson et al. (2025) 经二次验证确认为真实论文（arXiv:2502.15654, EMNLP 2025），已恢复引用（2026-05-13） | — |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_restore_drayson_citations_20260513T012807",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-13T01:30:59.052770+00:00_

修改完成。Drayson et al. 引用已在所有相关文件中确认到位：

- **`docs/related_work_structure.md:95`** — Thread 3 第 5 项，标注为 closest prior work（已在之前 session 恢复）
- **`docs/methodology_draft.md:34,249`** — 模型选择理由 + K* 科学意义段落（已在之前 session 恢复）
- **`docs/full_study_plan.md:55`** — Binary filter 策略行新增 Drayson importance resampling baseline（本次修改）
- **`ROADMAP.md:41`** — D006 更新为"经二次验证确认为真实论文（arXiv:2502.15654, EMNLP 2025），已恢复引用"（本次修改）
- **`ROADMAP.md:25`** — 已有完成态任务项 `[x] Drayson et al. 确认为真实论文，已恢复所有引用`（系统已自动添加）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_knowledge_restore_drayson_citations_20260513T012807"
}
```

</details>

---
