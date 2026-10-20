# paper writing experimental setup

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 9
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/chats/worker_paper_writing_experimental_setup_20260517T042638.jsonl`
- **Structured JSON:** [`9bdf393555e87d24f483.json`](../../sessions/9b/9bdf393555e87d24f483.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

9 recorded events

### Tool call

_source line 1 · 2026-05-17T04:27:57.705508+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experimental_setup_20260517T042638",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T04:27:57.706069+00:00_

1	---
2	name: paper-writing-norms
3	description: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。
4	allowed-tools: [Read, Write, Edit, Glob, Grep]
5	scope: global
6	version: 2
7	priority: 9
8	tags:
9	  - writing
10	  - paper
11	  - style
12	  - norms
13	roles:
14	  - agent
15	  - worker
16	  - paper_agent
17	---
18	
19	# 论文写作风格规范
20	
21	> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。
22	
23	---
24	
25	## 一、总体写作哲学
26	
27	### 1.1 故事驱动，不是数据堆砌
28	
29	- 论文必须以"故事线"为核心展开：问题 → 洞察 → 方法 → 验证
30	- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进
31	- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌
32	- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing
33	
34	### 1.2 主线统一性
35	
36	- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**
37	- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C
38	- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机
39	- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线
40	
41	### 1.3 专有名词必须有定义
42	
43	- 首次出现的专有名词/缩写必须给出完整定义和解释
44	- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）
45	- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用
46	- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug
47	
48	### 1.4 写作前必读同类优秀论文
49	
50	- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可
51	- 重点学：
52	  - Abstract 怎么用最少篇幅讲完故事
53	  - Introduction 怎么从大问题切入到具体贡献
54	  - Related Work 怎么 positioning 自己（不是 survey）
55	  - Table/Figure 怎么压缩信息密度
56	- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大
57	- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文
58	
59	---
60	
61	## 二、Abstract 写作规范
62	
63	### 2.1 四个必答问题（150-250 words）
64	
65	Abstract 必须在很短的篇幅内清楚回答：
66	1. **研究什么问题** — 1-2 句话交代背景和痛点
67	2. **为什么重要** — 现有方法的不足（不用写太多）
68	3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）
69	4. **结果说明什么** — 用具体实验结论支撑贡献
70	
71	### 2.2 禁忌
72	
73	- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim
74	- **
…[truncated 4866 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_20260517T042638",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T04:27:57.706270+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/collapse_aware_reward_rebalancing/docs/paper/sections/",
  "description": "Check existing paper sections directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experimental_setup_20260517T042638",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/collapse_aware_reward_rebalancing/docs/paper/sections/",
    "description": "Check existing paper sections directory"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T04:27:57.706426+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_20260517T042638",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T04:27:57.706601+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/collapse_aware_reward_rebalancing/docs/paper/sections/experimental_setup.tex",
  "content": "% Section 3: Experimental Setup\n% Note: \\section{} header is in main.tex\n\n\\subsection{Iterative Self-Training Pipeline}\n\\label{sec:pipeline}\n\nWe study diversity dynamics through an iterative self-training loop where each generation produces training data for the next. The base model is Qwen3-0.6B (596M parameters), chosen as the smallest model capable of coherent instruction-following while permitting complete multi-generation experiments in tractable compute budgets. We use UltraFeedback \\cite{placeholder_ultrafeedback} as the prompt source, sampling 2{,}200 general instruction-following prompts (2{,}000 for training, 200 held out for evaluation). Each generation proceeds in four steps: (1) generate $K$ candidate responses per prompt from the current model; (2) score all candidates with ArmoRM-Llama3-8B-v0.1 \\cite{placeholder_armorm}, a reward model that does not participate in training; (3) select the top-1 candidate per prompt according to ArmoRM scores; (4) fine-tune the base model on the selected subset to produce the next-generation model. We run three generations (Gen~0 $\\rightarrow$ Gen~1 $\\rightarrow$ Gen~2), where Gen~0 denotes the original base model before any self-training. All generation uses the default sampling temperature to maintain output diversity within each candidate set.\n\n\\subsection{Experimental Conditions}\n\\label{sec:conditions}\n\nTable~\\ref{tab:conditions} summarizes the seven configurations. Our design isolates four factors through controlled comparisons. First, adaptation method (LoRA vs.\\ Full Fine-Tuning) isolates the effect of parameter capacity: LoRA \\cite{placeholder_lora} updates only 1.67\\% of parameters (rank 16), while Full-FT (Full Fine-Tuning) updates all parameters. Second, candidate pool size ($K{=}4$ vs.\\ $K{=}8$) isolates selection pressure, corresponding to 25\\% and 12.5\\% retention rates respectively. Third, learning rate (5e-6 vs.\\ 2e-5 for Full-FT) isolates learning intensity, spanning a conservative to aggressive optimization range. Fourth, curation strategy (ArmoRM top-1 vs.\\ random selection) isolates the causal effect of reward-based filtering: configurations C5, C6, and C7 serve as matched baselines for C1, C3, and C4 respectively, differing only in whether selection is reward-guided or random.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Experimental configurations. Each curated condition (C1--C4) has a matched random baseline (C5--C7) that differs only in selection strategy. Trainable \\% refers to the fraction of model parameters updated during fine-tuning.}\n\\label{tab:conditions}\n\\begin{tabular}{@{}lllcll@{}}\n\\toprule\nID & Adaptation & $K$ & LR & Curation & Trainable \\\\\n\\midrule\nC1 & LoRA ($r{=}16$) & 4 & 2e-4 & ArmoRM top-1 & 1.67\\% \\\\\nC2 & LoRA ($r{=}16$) & 8 & 2e-4 & ArmoRM top-1 & 1.67\\% \\\\\nC3 & Full-FT & 4 & 5e-6 & ArmoRM top-1 & 100\\% \\\\\nC4 & Full-FT & 4 & 2e-5 & ArmoRM top-1 & 100\\% \\\\\n\\midrule\nC5 & LoRA ($r{=}16$) & 4 & 2e-4 & Random 1-of-$K$ & 1.67\\% \\\\\nC6 & Full-FT & 4 & 5e-6 & Random 1-of-$K$ & 100\\% \\\\\nC7 & Full-FT & 4 & 2e-5 & Random 1-of-$K$ & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis factorial structure enables direct attribution. If reward curation causes diversity collapse, curated conditions (C1--C4) should show steeper diversity decline than their random counterparts (C5--C7) across generations. If parameter capacity mediates collapse, LoRA and Full-FT conditions should diverge even under identical curation. If selection pressure drives collapse, C2 ($K{=}8$, 12.5\\% retention) should collapse faster than C1 ($K{=}4$, 25\\% retention).\n\n\\subsection{Evaluation Metrics}\n\\label{sec:metrics}\n\nWe evaluate diversity at two levels: semantic content and surface format.\n\n\\paragraph{Semantic diversity.} Our primary metric is the Vendi Score \\cite{placeholder_vendi}, a kernel-based diversity measure computed over sentence embeddings from all-MiniLM-L6-v2 \\cite{placeholder_minilm}. The Vendi Score equals the exponential of the Shannon entropy of the eigenvalues of the kernel matrix, with higher values indicating greater diversity. We complement this with Self-BLEU \\cite{placeholder_selfbleu}, defined as the average pairwise BLEU score among all responses in the evaluation set (lower indicates more diversity), and Nearest-Neighbor Distance (NND), the average cosine distance to the nearest neighbor in embedding space (higher indicates more diversity). All semantic metrics are computed over the 200 evaluation prompts with one response per prompt per generation.\n\n\\paragraph{Format diversity.} Standard embedding-based metrics can miss surface-level homogenization because semantically distinct responses may share identical templates. We introduce two format-level indicators. Opening Entropy measures the Shannon entropy of first-10-token sequences across responses; lower values indicate convergence toward fixed opening patterns. Near-Duplicate Start Rate measures the fraction of response pairs sharing a 50-character prefix; higher values indicate template repetition. These metrics capture a distinct failure mode: models that produce varied content but wrap it in repetitive formatting.\n\n\\paragraph{Quality and training dynamics.} We track mean ArmoRM score per generation to verify that quality does not degrade, and per-generation training loss to monitor learning dynamics and detect underfitting or overfitting.\n\n\\subsection{Training Details}\n\\label{sec:training_details}\n\nFor LoRA configurations, we set rank to 16, scaling factor $\\alpha{=}32$, and apply adapters to all linear layers. For Full-FT configurations, all parameters are updated without freezing. Both use AdamW \\cite{placeholder_adamw} with cosine learning rate scheduling and train for 2 epochs per generation (3 epochs for the aggressive Full-FT setting C4 when loss has not converged). The effective batch size is 16 across all conditions. All experiments run on 2$\\times$ NVIDIA RTX 5090 GPUs (32GB each). The complete pipeline (7 configurations $\\times$ 3 generations) requires approximately 48 GPU-hours.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experimental_setup_20260517T042638",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/collapse_aware_reward_rebalancing/docs/paper/sections/experimental_setup.tex",
    "content": "% Section 3: Experimental Setup\n% Note: \\section{} header is in main.tex\n\n\\subsection{Iterative Self-Training Pipeline}\n\\label{sec:pipeline}\n\nWe study diversity dynamics through an iterative self-training loop where each generation produces training data for the next. The base model is Qwen3-0.6B (596M parameters), chosen as the smallest model capable of coherent instruction-following while permitting complete multi-generation experiments in tractable compute budgets. We use UltraFeedback \\cite{placeholder_ultrafeedback} as the prompt source, sampling 2{,}200 general instruction-following prompts (2{,}000 for training, 200 held out for evaluation). Each generation proceeds in four steps: (1) generate $K$ candidate responses per prompt from the current model; (2) score all candidates with ArmoRM-Llama3-8B-v0.1 \\cite{placeholder_armorm}, a reward model that does not participate in training; (3) select the top-1 candidate per prompt according to ArmoRM scores; (4) fine-tune the base model on the selected subset to produce the next-generation model. We run three generations (Gen~0 $\\rightarrow$ Gen~1 $\\rightarrow$ Gen~2), where Gen~0 denotes the original base model before any self-training. All generation uses the default sampling temperature to maintain output diversity within each candidate set.\n\n\\subsection{Experimental Conditions}\n\\label{sec:conditions}\n\nTable~\\ref{tab:conditions} summarizes the seven configurations. Our design isolates four factors through controlled comparisons. First, adaptation method (LoRA vs.\\ Full Fine-Tuning) isolates the effect of parameter capacity: LoRA \\cite{placeholder_lora} updates only 1.67\\% of parameters (rank 16), while Full-FT (Full Fine-Tuning) updates all parameters. Second, candidate pool size ($K{=}4$ vs.\\ $K{=}8$) isolates selection pressure, corresponding to 25\\% and 12.5\\% retention rates respectively. Third, learning rate (5e-6 vs.\\ 2e-5 for Full-FT) isolates learning intensity, spanning a conservative to aggressive optimization range. Fourth, curation strategy (ArmoRM top-1 vs.\\ random selection) isolates the causal effect of reward-based filtering: configurations C5, C6, and C7 serve as matched baselines for C1, C3, and C4 respectively, differing only in whether selection is reward-guided or random.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Experimental configurations. Each curated condition (C1--C4) has a matched random baseline (C5--C7) that differs only in selection strategy. Trainable \\% refers to the fraction of model parameters updated during fine-tuning.}\n\\label{tab:conditions}\n\\begin{tabular}{@{}lllcll@{}}\n\\toprule\nID & Adaptation & $K$ & LR & Curation & Trainable \\\\\n\\midrule\nC1 & LoRA ($r{=}16$) & 4 & 2e-4 & ArmoRM top-1 & 1.67\\% \\\\\nC2 & LoRA ($r{=}16$) & 8 & 2e-4 & ArmoRM top-1 & 1.67\\% \\\\\nC3 & Full-FT & 4 & 5e-6 & ArmoRM top-1 & 100\\% \\\\\nC4 & Full-FT & 4 & 2e-5 & ArmoRM top-1 & 100\\% \\\\\n\\midrule\nC5 & LoRA ($r{=}16$) & 4 & 2e-4 & Random 1-of-$K$ & 1.67\\% \\\\\nC6 & Full-FT & 4 & 5e-6 & Random 1-of-$K$ & 100\\% \\\\\nC7 & Full-FT & 4 & 2e-5 & Random 1-of-$K$ & 100\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis factorial structure enables direct attribution. If reward curation causes diversity collapse, curated conditions (C1--C4) should show steeper diversity decline than their random counterparts (C5--C7) across generations. If parameter capacity mediates collapse, LoRA and Full-FT conditions should diverge even under identical curation. If selection pressure drives collapse, C2 ($K{=}8$, 12.5\\% retention) should collapse faster than C1 ($K{=}4$, 25\\% retention).\n\n\\subsection{Evaluation Metrics}\n\\label{sec:metrics}\n\nWe evaluate diversity at two levels: semantic content and surface format.\n\n\\paragraph{Semantic diversity.} Our primary metric is the Vendi Score \\cite{placeholder_vendi}, a kernel-based diversity measure computed over sentence embeddings from all-MiniLM-L6-v2 \\cite{placeholder_minilm}. The Vendi Score equals the exponential of the Shannon entropy of the eigenvalues of the kernel matrix, with higher values indicating greater diversity. We complement this with Self-BLEU \\cite{placeholder_selfbleu}, defined as the average pairwise BLEU score among all responses in the evaluation set (lower indicates more diversity), and Nearest-Neighbor Distance (NND), the average cosine distance to the nearest neighbor in embedding space (higher indicates more diversity). All semantic metrics are computed over the 200 evaluation prompts with one response per prompt per generation.\n\n\\paragraph{Format diversity.} Standard embedding-based metrics can miss surface-level homogenization because semantically distinct responses may share identical templates. We introduce two format-level indicators. Opening Entropy measures the Shannon entropy of first-10-token sequences across responses; lower values indicate convergence toward fixed opening patterns. Near-Duplicate Start Rate measures the fraction of response pairs sharing a 50-character prefix; higher values indicate template repetition. These metrics capture a distinct failure mode: models that produce varied content but wrap it in repetitive formatting.\n\n\\paragraph{Quality and training dynamics.} We track mean ArmoRM score per generation to verify that quality does not degrade, and per-generation training loss to monitor learning dynamics and detect underfitting or overfitting.\n\n\\subsection{Training Details}\n\\label{sec:training_details}\n\nFor LoRA configurations, we set rank to 16, scaling factor $\\alpha{=}32$, and apply adapters to all linear layers. For Full-FT configurations, all parameters are updated without freezing. Both use AdamW \\cite{placeholder_adamw} with cosine learning rate scheduling and train for 2 epochs per generation (3 epochs for the aggressive Full-FT setting C4 when loss has not converged). The effective batch size is 16 across all conditions. All experiments run on 2$\\times$ NVIDIA RTX 5090 GPUs (32GB each). The complete pipeline (7 configurations $\\times$ 3 generations) requires approximately 48 GPU-hours.\n"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T04:27:57.706830+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/collapse_aware_reward_rebalancing/docs/paper/sections/experimental_setup.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_20260517T042638",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T04:27:57.707016+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"—\" /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/collapse_aware_reward_rebalancing/docs/paper/sections/experimental_setup.tex; grep -n \" – \" /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/collapse_aware_reward_rebalancing/docs/paper/sections/experimental_setup.tex; grep -n \"ing\\.\" /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/collapse_aware_reward_rebalancing/docs/paper/sections/experimental_setup.tex | grep -v \"\\\\\\\\cite\\|train\\|following\\|opening\\|setting\\|scaling\\|freez\"",
  "description": "Check for em-dash, en-dash, and -ing phrase endings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_experimental_setup_20260517T042638",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"—\" /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/collapse_aware_reward_rebalancing/docs/paper/sections/experimental_setup.tex; grep -n \" – \" /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/collapse_aware_reward_rebalancing/docs/paper/sections/experimental_setup.tex; grep -n \"ing\\.\" /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/collapse_aware_reward_rebalancing/docs/paper/sections/experimental_setup.tex | grep -v \"\\\\\\\\cite\\|train\\|following\\|opening\\|setting\\|scaling\\|freez\"",
    "description": "Check for em-dash, en-dash, and -ing phrase endings"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T04:27:57.707173+00:00_

17:\caption{Experimental configurations. Each curated condition (C1--C4) has a matched random baseline (C5--C7) that differs only in selection strategy. Trainable \% refers to the fraction of model parameters updated during fine-tuning.}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_experimental_setup_20260517T042638",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-17T04:27:57.707360+00:00_

无 em-dash、无解释性 en-dash、无 -ing 短语结尾问题。`--` 仅用于 LaTeX 数字范围（C1--C4 等），符合规范。

文件已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/collapse_aware_reward_rebalancing/docs/paper/sections/experimental_setup.tex`。

内容包含：
- **3.1 Pipeline**: 完整 4-step 循环描述，模型/数据/reward model 选择理由
- **3.2 Conditions**: Table 1（7 configs, booktabs 格式）+ 变量隔离逻辑的预测性表述
- **3.3 Metrics**: 语义层（Vendi Score, Self-BLEU, NND）+ 格式层（Opening Entropy, Near-Duplicate Start Rate）+ 质量/训练动态
- **3.4 Training Details**: LoRA/Full-FT 超参、硬件、总计算量

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_experimental_setup_20260517T042638"
}
```

</details>

---
