# paper add bertrand bib

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 14
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/workers/worker_paper_add-bertrand-bib_20260519T032111.log`
- **Structured JSON:** [`ac28a054cadf4686eaff.json`](../../sessions/ac/ac28a054cadf4686eaff.json)

## Before a recorded user message

14 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "session_id": "231f8c0f-eec9-474b-a616-122ee19a9223",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "4989060d-6120-4426-91df-5e7aabd33048",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Assistant

_source line 3_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the literature notes and the references.bib file in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "231f8c0f-eec9-474b-a616-122ee19a9223",
  "uuid": "ae43b773-f650-45cf-a08a-a6ac9a6d674a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LzV76mayAEyTj3YfyKJ5jY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12724,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12724
      },
      "output_tokens": 26,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 4_

<details open><summary>🔧 Tool call — Read · `toolu_01TBtoQ6evUh7TS7NwyygSfB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/model_collapse_literature_notes.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "231f8c0f-eec9-474b-a616-122ee19a9223",
  "uuid": "a1dd5725-a904-4cff-adc4-272c2bfe9350",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LzV76mayAEyTj3YfyKJ5jY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12724,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12724
      },
      "output_tokens": 26,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-19T03:21:27.458Z_

<details><summary>↩ Tool result · `toolu_01TBtoQ6evUh7TS7NwyygSfB`</summary>

````text
1	# Model Collapse Literature Notes for Retrain-Chain Positioning
2	
3	> 为论文 Discussion 中 retrain-chain (K*≥7 vs. prompt-chain K*=2) 的发现提供引用支撑。
4	
5	---
6	
7	## 1. Shumailov et al. (2024) — 奠基性工作
8	
9	- **引用**: Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, Yarin Gal. "AI Models Collapse When Trained on Recursively Generated Data." *Nature*, 631, 755–759, 2024.
10	- **核心发现**: 在 VAE、GMM、LLM 上系统验证了 model collapse 现象：递归训练导致分布尾部消失，模型输出逐代收敛到低方差的点估计。早期代次丢失低频模式（tail trimming），后期代次丢失高频模式（tail narrowing）。
11	- **与我们的关系**: 直接相关。他们关注的是质量退化（分布收敛），我们关注的是这种退化是否可被检测器区分。我们的 retrain-chain 实验本质上复现了他们的递归训练设定（LoRA fine-tune on own output），但测量的是代际可区分性而非输出质量。K*≥7 说明每代的分布漂移足够大，使检测器在 7 代内仍能区分相邻代次。
12	- **Bib key**: `shumailov2024collapse` ✅ 已在 references.bib
13	
14	---
15	
16	## 2. Alemohammad et al. (2024) — MAD 概念
17	
18	- **引用**: Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard G. Baraniuk. "Self-Consuming Generative Models Go MAD." *Proceedings of ICLR*, 2024.
19	- **核心发现**: 提出 Model Autophagy Disorder (MAD) 概念。在图像生成模型上证明：纯合成数据递归训练导致质量和多样性持续下降；混入真实数据可减缓但不能完全阻止退化。区分了 fully synthetic loop 和 synthetic augmentation 两种场景。
20	- **与我们的关系**: MAD 框架适用于理解 retrain-chain：每代 LoRA fine-tune 构成 fully synthetic loop。他们的"质量/多样性退化随代数单调递增"与我们的"代际可区分性随代数保持"是同一现象的两面：distributional drift 既导致退化，也产生可检测的代际签名。
21	- **Bib key**: `alemohammad2024selfconsuming` ✅ 已在 references.bib
22	
23	---
24	
25	## 3. Dohmatob et al. (2024) — 理论 scaling law 视角
26	
27	- **引用**: Elvis Dohmatob, Yunzhen Feng, Pin-Yu Yang, Francois Charton, Julia Kempe. "A Tale of Tails: Model Collapse as a Change of Scaling Laws." *Proceedings of ICML*, 2024.
28	- **核心发现**: 将 model collapse 形式化为 scaling law 的变化：递归训练使尾部概率以特定速率衰减，collapse 速率取决于数据维度和模型族。提供了 collapse 不可避免性的理论下界。
29	- **与我们的关系**: 他们的理论预测了每代分布漂移的量级。这解释了为什么 retrain-chain 的 K* 远高于 prompt-chain：retrain-chain 每代引入权重更新（LoRA），产生的分布漂移远大于仅改变输入（prompt-chain）所引起的漂移，因此代际签名更强、可区分的代数更多。
30	- **Bib key**: `dohmatob2024model` ✅ 已在 references.bib
31	
32	---
33	
34	## 4. Gerstgrasser et al. (2024) — Collapse 可避免性
35	
36	- **引用**: Matthias Gerstgrasser, Rylan Schaeffer, Apratim Dey, Rafael Rafailov, Henry Sleight, John Hughes, Tomasz Korbak, Rajashree Agrawal, Dhruv Pai, Andrey Gromov, Daniel A. Roberts, Diyi Yang, David L. Donoho, Sanmi Koyejo. "Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data." *Proceedings of COLM*, 2024.
37	- **核心发现**: 证明如果每代训练都累积保留之前所有真实数据（而非仅用上一代合成数据），model collapse 可以完全避免。关键条件：真实数据占比不能低于某阈值。
38	- **与我们的关系**: 我们的 retrain-chain 设定是 pure synthetic loop（每代仅用上一代输出），属于他们证明的"必然 collapse"情形。这恰好是我们需要的：持续的分布漂移保证了代际可区分性。如果混入真实数据（如他们建议的），collapse 减缓，代际签名也会减弱，K* 可能降低。
39	- **Bib key**: `gerstgrasser2024model` ✅ 已在 references.bib
40	
41	---
42	
43	## 5. Bertrand et al. (2024) — 迭代再训练的稳定性理论
44	
45	- **引用**: Quentin Bertrand, Avishek (Joey) Bose, Alexandre Duplessis, Marco Jiralerspong, Gauthier Gidel. "On the Stability of Iterative Retraining of Generative Models on their Own Data." *Proceedings of ICLR* (Spotlight), 2024.
46	- **核心发现**: 为 likelihood-based 生成模型的迭代再训练提供稳定性理论框架。证明在初始模型足够接近真实分布、且每轮真实数据比例足够高的条件下，迭代再训练是稳定的（不会 collapse）。反之，纯合成循环不满足稳定性条件。
47	- **与我们的关系**: 提供了 retrain-chain 行为的理论解释。我们的纯合成 LoRA 循环不满足其稳定性条件，因此每代产生不可逆的分布漂移。这种理论预测的不稳定性正是代际可区分性的来源。
48	- **Bib key**: ❌ **不在 references.bib，需添加**
49	
50	---
51	
52	## 6. Briesch et al. (2023) — LLM 自消费训练实证
53	
54	- **引用**: Martin Briesch, Dominik Sobania, Franz Rothlauf. "Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop." arXiv:2311.16822, 2023.
55	- **核心发现**: 专门在 LLM 上实证研究自消费训练循环。发现递归训练导致词汇多样性下降、重复率上升、困惑度先降后升。退化速度与模型规模和采样温度相关。
56	- **与我们的关系**: 最直接的实证对照。他们测量的是质量指标（困惑度、多样性），我们测量的是可区分性（AUC）。两者互补：他们的质量退化曲线对应我们的可区分性保持曲线。可在 Discussion 中对照引用。
57	- **Bib key**: `briesch2023selfconsuming` ✅ 已在 references.bib
58	
59	---
60	
61	## 推荐 Positioning 文字（可直接用于 Discussion）
62	
63	> The distributional drift underlying model collapse \citep{shumailov2024collapse, alemohammad2024selfconsuming} is typically framed as a failure mode: recursive training on synthetic outputs erodes tail coverage and reduces diversity \citep{dohmatob2024model, briesch2023selfconsuming}. Our retrain-chain results reveal a complementary perspective: the same per-generation drift that degrades output quality also produces generation-specific distributional signatures that remain detectable across at least seven iterations ($K^*\!\geq\!7$). Because each LoRA fine-tuning step modifies model weights, the distributional shift per generation far exceeds that of prompt-chain inference (where weights are frozen), explaining why retrain-chain sustains discriminability well beyond the $K^*\!=\!2$ ceiling observed for prompt-chain. This connects our work to theoretical analyses showing that pure synthetic loops are inherently unstable \citep{bertrand2024stability, gerstgrasser2024model}: the instability that drives collapse simultaneously enables depth-aware contamination detection.
64	
65	---
66	
67	## 需添加的 BibTeX 条目
68	
69	```bibtex
70	@inproceedings{bertrand2024stability,
71	  title={On the Stability of Iterative Retraining of Generative Models on their Own Data},
72	  author={Bertrand, Quentin and Bose, Avishek Joey and Duplessis, Alexandre and Jiralerspong, Marco and Gidel, Gauthier},
73	  booktitle={Proceedings of ICLR},
74	  year={2024},
75	  url={https://arxiv.org/abs/2310.00429}
76	}
77	```
78	
79	---
80	
81	## 已在 bib 中的相关条目汇总
82	
83	| Bib key | 论文 | 核心角度 |
84	|---------|------|---------|
85	| `shumailov2024collapse` | Nature 2024 | 奠基性实证：尾部消失、分布收敛 |
86	| `alemohammad2024selfconsuming` | ICLR 2024 | MAD 概念：质量+多样性退化 |
87	| `dohmatob2024model` | ICML 2024 | 理论 scaling law：collapse 速率 |
88	| `dohmatob2025strong` | ICLR 2025 | Strong collapse 条件 |
89	| `gerstgrasser2024model` | COLM 2024 | 累积真实数据可避免 collapse |
90	| `kazdan2025collapse` | ICML 2025 | Collapse vs. thrive 条件分析 |
91	| `schaeffer2025position` | ICML 2025 | 澄清 collapse 定义误区 |
92	| `briesch2023selfconsuming` | arXiv 2023 | LLM 自消费循环实证 |
93	| `guo2024curious` | NAACL Findings 2024 | 语言多样性下降 |
94	| `shi2025collapse` | NeurIPS 2025 | 泛化→记忆视角 |
95	| `amin2025escaping` | NeurIPS 2025 | Weak data 逃逸 collapse |
96	| `drayson2025` | EMNLP 2025 | 检测防止 collapse（与我们最近） |
97	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "231f8c0f-eec9-474b-a616-122ee19a9223",
  "uuid": "f40026e1-1658-4352-8b31-dccbd770196d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/model_collapse_literature_notes.md",
      "content": "# Model Collapse Literature Notes for Retrain-Chain Positioning\n\n> 为论文 Discussion 中 retrain-chain (K*≥7 vs. prompt-chain K*=2) 的发现提供引用支撑。\n\n---\n\n## 1. Shumailov et al. (2024) — 奠基性工作\n\n- **引用**: Ilia Shumailov, Zakhar Shumaylov, Yiren Zhao, Nicolas Papernot, Ross Anderson, Yarin Gal. \"AI Models Collapse When Trained on Recursively Generated Data.\" *Nature*, 631, 755–759, 2024.\n- **核心发现**: 在 VAE、GMM、LLM 上系统验证了 model collapse 现象：递归训练导致分布尾部消失，模型输出逐代收敛到低方差的点估计。早期代次丢失低频模式（tail trimming），后期代次丢失高频模式（tail narrowing）。\n- **与我们的关系**: 直接相关。他们关注的是质量退化（分布收敛），我们关注的是这种退化是否可被检测器区分。我们的 retrain-chain 实验本质上复现了他们的递归训练设定（LoRA fine-tune on own output），但测量的是代际可区分性而非输出质量。K*≥7 说明每代的分布漂移足够大，使检测器在 7 代内仍能区分相邻代次。\n- **Bib key**: `shumailov2024collapse` ✅ 已在 references.bib\n\n---\n\n## 2. Alemohammad et al. (2024) — MAD 概念\n\n- **引用**: Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, Richard G. Baraniuk. \"Self-Consuming Generative Models Go MAD.\" *Proceedings of ICLR*, 2024.\n- **核心发现**: 提出 Model Autophagy Disorder (MAD) 概念。在图像生成模型上证明：纯合成数据递归训练导致质量和多样性持续下降；混入真实数据可减缓但不能完全阻止退化。区分了 fully synthetic loop 和 synthetic augmentation 两种场景。\n- **与我们的关系**: MAD 框架适用于理解 retrain-chain：每代 LoRA fine-tune 构成 fully synthetic loop。他们的\"质量/多样性退化随代数单调递增\"与我们的\"代际可区分性随代数保持\"是同一现象的两面：distributional drift 既导致退化，也产生可检测的代际签名。\n- **Bib key**: `alemohammad2024selfconsuming` ✅ 已在 references.bib\n\n---\n\n## 3. Dohmatob et al. (2024) — 理论 scaling law 视角\n\n- **引用**: Elvis Dohmatob, Yunzhen Feng, Pin-Yu Yang, Francois Charton, Julia Kempe. \"A Tale of Tails: Model Collapse as a Change of Scaling Laws.\" *Proceedings of ICML*, 2024.\n- **核心发现**: 将 model collapse 形式化为 scaling law 的变化：递归训练使尾部概率以特定速率衰减，collapse 速率取决于数据维度和模型族。提供了 collapse 不可避免性的理论下界。\n- **与我们的关系**: 他们的理论预测了每代分布漂移的量级。这解释了为什么 retrain-chain 的 K* 远高于 prompt-chain：retrain-chain 每代引入权重更新（LoRA），产生的分布漂移远大于仅改变输入（prompt-chain）所引起的漂移，因此代际签名更强、可区分的代数更多。\n- **Bib key**: `dohmatob2024model` ✅ 已在 references.bib\n\n---\n\n## 4. Gerstgrasser et al. (2024) — Collapse 可避免性\n\n- **引用**: Matthias Gerstgrasser, Rylan Schaeffer, Apratim Dey, Rafael Rafailov, Henry Sleight, John Hughes, Tomasz Korbak, Rajashree Agrawal, Dhruv Pai, Andrey Gromov, Daniel A. Roberts, Diyi Yang, David L. Donoho, Sanmi Koyejo. \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data.\" *Proceedings of COLM*, 2024.\n- **核心发现**: 证明如果每代训练都累积保留之前所有真实数据（而非仅用上一代合成数据），model collapse 可以完全避免。关键条件：真实数据占比不能低于某阈值。\n- **与我们的关系**: 我们的 retrain-chain 设定是 pure synthetic loop（每代仅用上一代输出），属于他们证明的\"必然 collapse\"情形。这恰好是我们需要的：持续的分布漂移保证了代际可区分性。如果混入真实数据（如他们建议的），collapse 减缓，代际签名也会减弱，K* 可能降低。\n- **Bib key**: `gerstgrasser2024model` ✅ 已在 references.bib\n\n---\n\n## 5. Bertrand et al. (2024) — 迭代再训练的稳定性理论\n\n- **引用**: Quentin Bertrand, Avishek (Joey) Bose, Alexandre Duplessis, Marco Jiralerspong, Gauthier Gidel. \"On the Stability of Iterative Retraining of Generative Models on their Own Data.\" *Proceedings of ICLR* (Spotlight), 2024.\n- **核心发现**: 为 likelihood-based 生成模型的迭代再训练提供稳定性理论框架。证明在初始模型足够接近真实分布、且每轮真实数据比例足够高的条件下，迭代再训练是稳定的（不会 collapse）。反之，纯合成循环不满足稳定性条件。\n- **与我们的关系**: 提供了 retrain-chain 行为的理论解释。我们的纯合成 LoRA 循环不满足其稳定性条件，因此每代产生不可逆的分布漂移。这种理论预测的不稳定性正是代际可区分性的来源。\n- **Bib key**: ❌ **不在 references.bib，需添加**\n\n---\n\n## 6. Briesch et al. (2023) — LLM 自消费训练实证\n\n- **引用**: Martin Briesch, Dominik Sobania, Franz Rothlauf. \"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop.\" arXiv:2311.16822, 2023.\n- **核心发现**: 专门在 LLM 上实证研究自消费训练循环。发现递归训练导致词汇多样性下降、重复率上升、困惑度先降后升。退化速度与模型规模和采样温度相关。\n- **与我们的关系**: 最直接的实证对照。他们测量的是质量指标（困惑度、多样性），我们测量的是可区分性（AUC）。两者互补：他们的质量退化曲线对应我们的可区分性保持曲线。可在 Discussion 中对照引用。\n- **Bib key**: `briesch2023selfconsuming` ✅ 已在 references.bib\n\n---\n\n## 推荐 Positioning 文字（可直接用于 Discussion）\n\n> The distributional drift underlying model collapse \\citep{shumailov2024collapse, alemohammad2024selfconsuming} is typically framed as a failure mode: recursive training on synthetic outputs erodes tail coverage and reduces diversity \\citep{dohmatob2024model, briesch2023selfconsuming}. Our retrain-chain results reveal a complementary perspective: the same per-generation drift that degrades output quality also produces generation-specific distributional signatures that remain detectable across at least seven iterations ($K^*\\!\\geq\\!7$). Because each LoRA fine-tuning step modifies model weights, the distributional shift per generation far exceeds that of prompt-chain inference (where weights are frozen), explaining why retrain-chain sustains discriminability well beyond the $K^*\\!=\\!2$ ceiling observed for prompt-chain. This connects our work to theoretical analyses showing that pure synthetic loops are inherently unstable \\citep{bertrand2024stability, gerstgrasser2024model}: the instability that drives collapse simultaneously enables depth-aware contamination detection.\n\n---\n\n## 需添加的 BibTeX 条目\n\n```bibtex\n@inproceedings{bertrand2024stability,\n  title={On the Stability of Iterative Retraining of Generative Models on their Own Data},\n  author={Bertrand, Quentin and Bose, Avishek Joey and Duplessis, Alexandre and Jiralerspong, Marco and Gidel, Gauthier},\n  booktitle={Proceedings of ICLR},\n  year={2024},\n  url={https://arxiv.org/abs/2310.00429}\n}\n```\n\n---\n\n## 已在 bib 中的相关条目汇总\n\n| Bib key | 论文 | 核心角度 |\n|---------|------|---------|\n| `shumailov2024collapse` | Nature 2024 | 奠基性实证：尾部消失、分布收敛 |\n| `alemohammad2024selfconsuming` | ICLR 2024 | MAD 概念：质量+多样性退化 |\n| `dohmatob2024model` | ICML 2024 | 理论 scaling law：collapse 速率 |\n| `dohmatob2025strong` | ICLR 2025 | Strong collapse 条件 |\n| `gerstgrasser2024model` | COLM 2024 | 累积真实数据可避免 collapse |\n| `kazdan2025collapse` | ICML 2025 | Collapse vs. thrive 条件分析 |\n| `schaeffer2025position` | ICML 2025 | 澄清 collapse 定义误区 |\n| `briesch2023selfconsuming` | arXiv 2023 | LLM 自消费循环实证 |\n| `guo2024curious` | NAACL Findings 2024 | 语言多样性下降 |\n| `shi2025collapse` | NeurIPS 2025 | 泛化→记忆视角 |\n| `amin2025escaping` | NeurIPS 2025 | Weak data 逃逸 collapse |\n| `drayson2025` | EMNLP 2025 | 检测防止 collapse（与我们最近） |\n",
      "numLines": 97,
      "startLine": 1,
      "totalLines": 97
    }
  }
}
````

</details>

---

### Tool call

_source line 6_

<details open><summary>🔧 Tool call — Read · `toolu_015DvooXHdwNLymuSaqe8uLB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "231f8c0f-eec9-474b-a616-122ee19a9223",
  "uuid": "e9562370-61a0-4f17-a727-1978c0126440",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LzV76mayAEyTj3YfyKJ5jY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12724,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12724
      },
      "output_tokens": 26,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-19T03:21:28.000Z_

<details><summary>↩ Tool result · `toolu_015DvooXHdwNLymuSaqe8uLB`</summary>

```text
1	% === References for gen-depth-contamination ===
2	% Source: literature_map.yaml — verified 2026-05-15
3	
4	% === Must-Cite ===
5	
6	@inproceedings{drayson2025,
7	  title={Machine-Generated Text Detection Prevents Language Model Collapse},
8	  author={Drayson, George and Yilmaz, Emine and Lampos, Vasileios},
9	  booktitle={Proceedings of EMNLP},
10	  year={2025},
11	  url={https://arxiv.org/abs/2502.15654}
12	}
13	
14	@inproceedings{schaeffer2025position,
15	  title={Position: Model Collapse Does Not Mean What You Think},
16	  author={Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Anirudh and Koyejo, Sanmi},
17	  booktitle={Proceedings of ICML},
18	  year={2025},
19	  url={https://arxiv.org/abs/2503.03150}
20	}
21	
22	@inproceedings{kazdan2025collapse,
23	  title={Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World},
24	  author={Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David and Koyejo, Sanmi},
25	  booktitle={Proceedings of ICML},
26	  year={2025},
27	  url={https://arxiv.org/abs/2410.16713}
28	}
29	
30	@inproceedings{mitchell2023detectgpt,
31	  title={{DetectGPT}: Zero-Shot Machine-Generated Text Detection using Probability Curvature},
32	  author={Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},
33	  booktitle={Proceedings of ICML},
34	  year={2023}
35	}
36	
37	% === Should-Cite ===
38	
39	@article{basani2026diveye,
40	  title={{DivEye}: Diversity Boosts {AI}-Generated Text Detection},
41	  author={Basani, Advik Raj and Chen, Pin-Yu},
42	  journal={Transactions on Machine Learning Research},
43	  issn={2835-8856},
44	  year={2026},
45	  url={https://arxiv.org/abs/2509.18880}
46	}
47	
48	@inproceedings{zawalski2026codec,
49	  title={{CoDeC}: Detecting Data Contamination in {LLM}s via In-Context Learning},
50	  author={Zawalski, Micha{\l} and Boubdir, Meriem and Ba{\l}azy, Klaudia and Nushi, Besmira and Ribalta, Pablo},
51	  booktitle={Proceedings of ICLR},
52	  year={2026},
53	  url={https://arxiv.org/abs/2510.27055}
54	}
55	
56	@inproceedings{zhang2024minkpp,
57	  title={Min-{K}\%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models},
58	  author={Zhang, Jingyang and Zheng, Jingwei and Gao, Jing and Miao, Chunyan},
59	  booktitle={Proceedings of EMNLP},
60	  year={2024}
61	}
62	
63	@article{shumailov2024collapse,
64	  title={{AI} Models Collapse When Trained on Recursively Generated Data},
65	  author={Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
66	  journal={Nature},
67	  volume={631},
68	  pages={755--759},
69	  year={2024}
70	}
71	
72	@inproceedings{alemohammad2024selfconsuming,
73	  title={Self-Consuming Generative Models Go {MAD}},
74	  author={Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},
75	  booktitle={Proceedings of ICLR},
76	  year={2024}
77	}
78	
79	@inproceedings{dohmatob2024model,
80	  title={A Tale of Tails: Model Collapse as a Change of Scaling Laws},
81	  author={Dohmatob, Elvis and Feng, Yunzhen and Yang, Pin-Yu and Charton, Francois and Kempe, Julia},
82	  booktitle={Proceedings of ICML},
83	  year={2024}
84	}
85	
86	@inproceedings{xie2023dsir,
87	  title={Data Selection for Language Models via Importance Resampling},
88	  author={Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},
89	  booktitle={Advances in Neural Information Processing Systems},
90	  year={2023}
91	}
92	
93	@inproceedings{tirumala2023d4,
94	  title={{D4}: Improving {LLM} Pretraining via Document De-Duplication and Diversification},
95	  author={Tirumala, Kushal and Markosyan, Aram and Zettlemoyer, Luke and Aghajanyan, Armen},
96	  booktitle={Advances in Neural Information Processing Systems},
97	  year={2023}
98	}
99	
100	@inproceedings{xie2023doremi,
101	  title={{DoReMi}: Optimizing Data Mixtures Speeds Up Language Model Pretraining},
102	  author={Xie, Sang Michael and Pham, Hieu and Dong, Xuanyi and Du, Nan and Liu, Hanxiao and Lu, Yifeng and Liang, Percy and Le, Quoc V. and Ma, Tengyu and Yu, Adams Wei},
103	  booktitle={Advances in Neural Information Processing Systems},
104	  year={2023}
105	}
106	
107	@inproceedings{hans2024binoculars,
108	  title={Spotting {LLMs} With Binoculars},
109	  author={Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},
110	  booktitle={Proceedings of ICML},
111	  year={2024}
112	}
113	
114	% === Probing Classifiers ===
115	
116	@inproceedings{alain2017understanding,
117	  title={Understanding Intermediate Layers Using Linear Classifier Probes},
118	  author={Alain, Guillaume and Bengio, Yoshua},
119	  booktitle={ICLR Workshop},
120	  year={2017}
121	}
122	
123	@article{belinkov2022probing,
124	  title={Probing Classifiers: Promises, Shortcomings, and Advances},
125	  author={Belinkov, Yonatan},
126	  journal={Computational Linguistics},
127	  volume={48},
128	  number={1},
129	  pages={207--219},
130	  year={2022}
131	}
132	
133	% === Model Collapse Avoidability ===
134	
135	@inproceedings{bao2024fast,
136	  title={{Fast-DetectGPT}: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature},
137	  author={Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},
138	  booktitle={Proceedings of ICLR},
139	  year={2024},
140	  url={https://arxiv.org/abs/2310.05130}
141	}
142	
143	@inproceedings{frank2001ordinal,
144	  title={A Simple Approach to Ordinal Classification},
145	  author={Frank, Eibe and Hall, Mark},
146	  booktitle={Proceedings of ECML},
147	  pages={145--156},
148	  year={2001}
149	}
150	
151	% === Beyond-Binary Detection ===
152	
153	@inproceedings{cheng2025beyond,
154	  title={Beyond Binary: Towards Fine-Grained {LLM}-Generated Text Detection via Role Recognition and Involvement Measurement},
155	  author={Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou},
156	  booktitle={Proceedings of the ACM Web Conference (WWW)},
157	  year={2025},
158	  url={https://arxiv.org/abs/2410.14259}
159	}
160	
161	@article{mehta2025beyond,
162	  title={Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models},
163	  author={Mehta, Sushant},
164	  journal={arXiv preprint arXiv:2511.17602},
165	  year={2025},
166	  url={https://arxiv.org/abs/2511.17602}
167	}
168	
169	% === AI-Generated Content Prevalence ===
170	
171	@inproceedings{sun2025aigt,
172	  title={Are We in the {AI}-Generated Text World Already? Quantifying and Monitoring {AIGT} on Social Media},
173	  author={Sun, Zhen and Zhang, Zongmin and Shen, Xinyue and Zhang, Ziyi and Liu, Yule and Backes, Michael and Zhang, Yang and He, Xinlei},
174	  booktitle={Proceedings of ACL},
175	  year={2025},
176	  url={https://arxiv.org/abs/2412.18148}
177	}
178	
179	@article{spennemann2025quantifying,
180	  title={Delving into: the Quantification of {AI}-Generated Content on the Internet (Synthetic Data)},
181	  author={Spennemann, Dirk H. R.},
182	  journal={arXiv preprint arXiv:2504.08755},
183	  year={2025},
184	  url={https://arxiv.org/abs/2504.08755}
185	}
186	
187	% === New entries (added 2026-05-16, Round 4 reviewer) ===
188	
189	@inproceedings{dohmatob2025strong,
190	  title={Strong Model Collapse},
191	  author={Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
192	  booktitle={Proceedings of ICLR},
193	  year={2025},
194	  url={https://arxiv.org/abs/2410.04840}
195	}
196	
197	@inproceedings{wang2024semeval,
198	  title={{SemEval}-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection},
199	  author={Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas},
200	  booktitle={Proceedings of SemEval},
201	  year={2024},
202	  url={https://arxiv.org/abs/2404.14183}
203	}
204	
205	@inproceedings{gerstgrasser2024model,
206	  title={Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data},
207	  author={Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},
208	  booktitle={Proceedings of COLM},
209	  year={2024},
210	  url={https://arxiv.org/abs/2404.01413}
211	}
212	
213	@inproceedings{guo2024curious,
214	  title={The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text},
215	  author={Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chloe},
216	  booktitle={Findings of NAACL},
217	  year={2024},
218	  url={https://arxiv.org/abs/2311.09807}
219	}
220	
221	@article{briesch2023selfconsuming,
222	  title={Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop},
223	  author={Briesch, Martin and Sobania, Dominik and Rothlauf, Franz},
224	  journal={arXiv preprint arXiv:2311.16822},
225	  year={2023},
226	  url={https://arxiv.org/abs/2311.16822}
227	}
228	
229	@inproceedings{padmakumar2024writing,
230	  title={Does Writing with Language Models Reduce Content Diversity?},
231	  author={Padmakumar, Vishakh and He, He},
232	  booktitle={Proceedings of ICLR},
233	  year={2024},
234	  url={https://arxiv.org/abs/2309.05196}
235	}
236	
237	% === New entries (added 2026-05-15, FR-10) ===
238	
239	@inproceedings{krishna2023paraphrasing,
240	  title={Paraphrasing Evades Detectors of {AI}-Generated Text, but Retrieval is an Effective Defense},
241	  author={Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and Iyyer, Mohit},
242	  booktitle={Advances in Neural Information Processing Systems},
243	  year={2023}
244	}
245	
246	@article{sadasivan2023detect,
247	  title={Can {AI}-Generated Text be Reliably Detected?},
248	  author={Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},
249	  journal={arXiv preprint arXiv:2303.11156},
250	  year={2023},
251	  url={https://arxiv.org/abs/2303.11156}
252	}
253	
254	@inproceedings{hao2025rewrite,
255	  title={Learning to Rewrite: Generalized {LLM}-Generated Text Detection},
256	  author={Hao, Wei and Guan, Ran and Lu, Kangjie and Zhang, Shuai},
257	  booktitle={Findings of ACL},
258	  year={2025}
259	}
260	
261	@inproceedings{shi2025collapse,
262	  title={A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective},
263	  author={Shi, Lianghe and Wu, Meng and Zhang, Huijie and Zhang, Zekai and Tao, Molei and Qu, Qing},
264	  booktitle={Advances in Neural Information Processing Systems},
265	  year={2025}
266	}
267	
268	@article{gambetta2024surplexity,
269	  title={Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative {AI}},
270	  author={Gambetta, Daniele and Gezici, Gizem and Giannotti, Fosca and Pedreschi, Dino and Knott, Alistair and Pappalardo, Luca},
271	  journal={arXiv preprint arXiv:2410.12341},
272	  year={2024}
273	}
274	
275	@inproceedings{amin2025escaping,
276	  title={Escaping Collapse: The Strength of Weak Data for Large Language Model Training},
277	  author={Amin, Kareem and Babakniya, Sara and Bie, Alex and Kong, Weiwei and Syed, Umar and Vassilvitskii, Sergei},
278	  booktitle={Advances in Neural Information Processing Systems},
279	  year={2025}
280	}
281	
282	@inproceedings{kirchenbauer2023watermark,
283	  title     = {A Watermark for Large Language Models},
284	  author    = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},
285	  booktitle = {Proceedings of the 40th International Conference on Machine Learning},
286	  pages     = {17061--17084},
287	  year      = {2023},
288	  volume    = {202},
289	  series    = {Proceedings of Machine Learning Research},
290	  publisher = {PMLR}
291	}
292	
293	@inproceedings{penedo2024fineweb,
294	  title     = {The {FineWeb} Datasets: Decanting the Web for the Finest Text Data at Scale},
295	  author    = {Penedo, Guilherme and Kydl{\'{\i}}{\v{c}}ek, Hynek and Ben Allal, Loubna and Lozhkov, Anton and Mitchell, Margaret and Raffel, Colin and Von Werra, Leandro and Wolf, Thomas},
296	  booktitle = {Advances in Neural Information Processing Systems},
297	  volume    = {37},
298	  pages     = {30811--30849},
299	  year      = {2024}
300	}
301	
302	@inproceedings{gehrmann2019gltr,
303	  title     = {{GLTR}: Statistical Detection and Visualization of Generated Text},
304	  author    = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander},
305	  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics: System Demonstrations},
306	  pages     = {111--116},
307	  year      = {2019},
308	  address   = {Florence, Italy},
309	  publisher = {Association for Computational Linguistics},
310	  doi       = {10.18653/v1/P19-3019}
311	}
312	
313	@inproceedings{ke2017lightgbm,
314	  title     = {{LightGBM}: A Highly Efficient Gradient Boosting Decision Tree},
315	  author    = {Ke, Guolin and Meng, Qi and Finley, Thomas and Wang, Taifeng and Chen, Wei and Ma, Weidong and Ye, Qiwei and Liu, Tie-Yan},
316	  booktitle = {Advances in Neural Information Processing Systems},
317	  volume    = {30},
318	  year      = {2017}
319	}
320	
321	@article{wu2023survey,
322	  title     = {A Survey on {LLM}-generated Text Detection: Necessity, Methods, and Future Directions},
323	  author    = {Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Wong, Derek F. and Chao, Lidia S.},
324	  journal   = {arXiv preprint arXiv:2310.14724},
325	  year      = {2023}
326	}
327	
328	@article{tang2024science,
329	  title     = {The Science of Detecting {LLM}-Generated Text},
330	  author    = {Tang, Ruixiang and Chuang, Yu-Neng and Hu, Xia},
331	  journal   = {Communications of the ACM},
332	  volume    = {67},
333	  number    = {4},
334	  pages     = {50--59},
335	  year      = {2024},
336	  doi       = {10.1145/3624725}
337	}
338	
339	@inproceedings{oren2024proving,
340	  title     = {Proving Test Set Contamination in Black Box Language Models},
341	  author    = {Oren, Yonatan and Meister, Nicole and Chatterji, Niladri S. and Ladhak, Faisal and Hashimoto, Tatsunori B.},
342	  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations},
343	  year      = {2024}
344	}
345	
346	@article{cao2020coral,
347	  title     = {Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation},
348	  author    = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},
349	  journal   = {Pattern Recognition Letters},
350	  volume    = {140},
351	  pages     = {325--331},
352	  year      = {2020},
353	  doi       = {10.1016/j.patrec.2020.11.008}
354	}
355	
356	@article{husain2019codesearchnet,
357	  title     = {{CodeSearchNet} Challenge: Evaluating the State of Semantic Code Search},
358	  author    = {Husain, Hamel and Wu, Ho-Hsiang and Gazit, Tiferet and Allamanis, Miltiadis and Brockschmidt, Marc},
359	  journal   = {arXiv preprint arXiv:1909.09436},
360	  year      = {2019},
361	  url       = {https://arxiv.org/abs/1909.09436}
362	}
363	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "231f8c0f-eec9-474b-a616-122ee19a9223",
  "uuid": "6c872bd7-8bed-4fb0-a060-7831a1914b93",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib",
      "content": "% === References for gen-depth-contamination ===\n% Source: literature_map.yaml — verified 2026-05-15\n\n% === Must-Cite ===\n\n@inproceedings{drayson2025,\n  title={Machine-Generated Text Detection Prevents Language Model Collapse},\n  author={Drayson, George and Yilmaz, Emine and Lampos, Vasileios},\n  booktitle={Proceedings of EMNLP},\n  year={2025},\n  url={https://arxiv.org/abs/2502.15654}\n}\n\n@inproceedings{schaeffer2025position,\n  title={Position: Model Collapse Does Not Mean What You Think},\n  author={Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Anirudh and Koyejo, Sanmi},\n  booktitle={Proceedings of ICML},\n  year={2025},\n  url={https://arxiv.org/abs/2503.03150}\n}\n\n@inproceedings{kazdan2025collapse,\n  title={Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World},\n  author={Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David and Koyejo, Sanmi},\n  booktitle={Proceedings of ICML},\n  year={2025},\n  url={https://arxiv.org/abs/2410.16713}\n}\n\n@inproceedings{mitchell2023detectgpt,\n  title={{DetectGPT}: Zero-Shot Machine-Generated Text Detection using Probability Curvature},\n  author={Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},\n  booktitle={Proceedings of ICML},\n  year={2023}\n}\n\n% === Should-Cite ===\n\n@article{basani2026diveye,\n  title={{DivEye}: Diversity Boosts {AI}-Generated Text Detection},\n  author={Basani, Advik Raj and Chen, Pin-Yu},\n  journal={Transactions on Machine Learning Research},\n  issn={2835-8856},\n  year={2026},\n  url={https://arxiv.org/abs/2509.18880}\n}\n\n@inproceedings{zawalski2026codec,\n  title={{CoDeC}: Detecting Data Contamination in {LLM}s via In-Context Learning},\n  author={Zawalski, Micha{\\l} and Boubdir, Meriem and Ba{\\l}azy, Klaudia and Nushi, Besmira and Ribalta, Pablo},\n  booktitle={Proceedings of ICLR},\n  year={2026},\n  url={https://arxiv.org/abs/2510.27055}\n}\n\n@inproceedings{zhang2024minkpp,\n  title={Min-{K}\\%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models},\n  author={Zhang, Jingyang and Zheng, Jingwei and Gao, Jing and Miao, Chunyan},\n  booktitle={Proceedings of EMNLP},\n  year={2024}\n}\n\n@article{shumailov2024collapse,\n  title={{AI} Models Collapse When Trained on Recursively Generated Data},\n  author={Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},\n  journal={Nature},\n  volume={631},\n  pages={755--759},\n  year={2024}\n}\n\n@inproceedings{alemohammad2024selfconsuming,\n  title={Self-Consuming Generative Models Go {MAD}},\n  author={Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},\n  booktitle={Proceedings of ICLR},\n  year={2024}\n}\n\n@inproceedings{dohmatob2024model,\n  title={A Tale of Tails: Model Collapse as a Change of Scaling Laws},\n  author={Dohmatob, Elvis and Feng, Yunzhen and Yang, Pin-Yu and Charton, Francois and Kempe, Julia},\n  booktitle={Proceedings of ICML},\n  year={2024}\n}\n\n@inproceedings{xie2023dsir,\n  title={Data Selection for Language Models via Importance Resampling},\n  author={Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},\n  booktitle={Advances in Neural Information Processing Systems},\n  year={2023}\n}\n\n@inproceedings{tirumala2023d4,\n  title={{D4}: Improving {LLM} Pretraining via Document De-Duplication and Diversification},\n  author={Tirumala, Kushal and Markosyan, Aram and Zettlemoyer, Luke and Aghajanyan, Armen},\n  booktitle={Advances in Neural Information Processing Systems},\n  year={2023}\n}\n\n@inproceedings{xie2023doremi,\n  title={{DoReMi}: Optimizing Data Mixtures Speeds Up Language Model Pretraining},\n  author={Xie, Sang Michael and Pham, Hieu and Dong, Xuanyi and Du, Nan and Liu, Hanxiao and Lu, Yifeng and Liang, Percy and Le, Quoc V. and Ma, Tengyu and Yu, Adams Wei},\n  booktitle={Advances in Neural Information Processing Systems},\n  year={2023}\n}\n\n@inproceedings{hans2024binoculars,\n  title={Spotting {LLMs} With Binoculars},\n  author={Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},\n  booktitle={Proceedings of ICML},\n  year={2024}\n}\n\n% === Probing Classifiers ===\n\n@inproceedings{alain2017understanding,\n  title={Understanding Intermediate Layers Using Linear Classifier Probes},\n  author={Alain, Guillaume and Bengio, Yoshua},\n  booktitle={ICLR Workshop},\n  year={2017}\n}\n\n@article{belinkov2022probing,\n  title={Probing Classifiers: Promises, Shortcomings, and Advances},\n  author={Belinkov, Yonatan},\n  journal={Computational Linguistics},\n  volume={48},\n  number={1},\n  pages={207--219},\n  year={2022}\n}\n\n% === Model Collapse Avoidability ===\n\n@inproceedings{bao2024fast,\n  title={{Fast-DetectGPT}: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature},\n  author={Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},\n  booktitle={Proceedings of ICLR},\n  year={2024},\n  url={https://arxiv.org/abs/2310.05130}\n}\n\n@inproceedings{frank2001ordinal,\n  title={A Simple Approach to Ordinal Classification},\n  author={Frank, Eibe and Hall, Mark},\n  booktitle={Proceedings of ECML},\n  pages={145--156},\n  year={2001}\n}\n\n% === Beyond-Binary Detection ===\n\n@inproceedings{cheng2025beyond,\n  title={Beyond Binary: Towards Fine-Grained {LLM}-Generated Text Detection via Role Recognition and Involvement Measurement},\n  author={Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou},\n  booktitle={Proceedings of the ACM Web Conference (WWW)},\n  year={2025},\n  url={https://arxiv.org/abs/2410.14259}\n}\n\n@article{mehta2025beyond,\n  title={Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models},\n  author={Mehta, Sushant},\n  journal={arXiv preprint arXiv:2511.17602},\n  year={2025},\n  url={https://arxiv.org/abs/2511.17602}\n}\n\n% === AI-Generated Content Prevalence ===\n\n@inproceedings{sun2025aigt,\n  title={Are We in the {AI}-Generated Text World Already? Quantifying and Monitoring {AIGT} on Social Media},\n  author={Sun, Zhen and Zhang, Zongmin and Shen, Xinyue and Zhang, Ziyi and Liu, Yule and Backes, Michael and Zhang, Yang and He, Xinlei},\n  booktitle={Proceedings of ACL},\n  year={2025},\n  url={https://arxiv.org/abs/2412.18148}\n}\n\n@article{spennemann2025quantifying,\n  title={Delving into: the Quantification of {AI}-Generated Content on the Internet (Synthetic Data)},\n  author={Spennemann, Dirk H. R.},\n  journal={arXiv preprint arXiv:2504.08755},\n  year={2025},\n  url={https://arxiv.org/abs/2504.08755}\n}\n\n% === New entries (added 2026-05-16, Round 4 reviewer) ===\n\n@inproceedings{dohmatob2025strong,\n  title={Strong Model Collapse},\n  author={Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},\n  booktitle={Proceedings of ICLR},\n  year={2025},\n  url={https://arxiv.org/abs/2410.04840}\n}\n\n@inproceedings{wang2024semeval,\n  title={{SemEval}-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection},\n  author={Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas},\n  booktitle={Proceedings of SemEval},\n  year={2024},\n  url={https://arxiv.org/abs/2404.14183}\n}\n\n@inproceedings{gerstgrasser2024model,\n  title={Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data},\n  author={Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},\n  booktitle={Proceedings of COLM},\n  year={2024},\n  url={https://arxiv.org/abs/2404.01413}\n}\n\n@inproceedings{guo2024curious,\n  title={The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text},\n  author={Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chloe},\n  booktitle={Findings of NAACL},\n  year={2024},\n  url={https://arxiv.org/abs/2311.09807}\n}\n\n@article{briesch2023selfconsuming,\n  title={Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop},\n  author={Briesch, Martin and Sobania, Dominik and Rothlauf, Franz},\n  journal={arXiv preprint arXiv:2311.16822},\n  year={2023},\n  url={https://arxiv.org/abs/2311.16822}\n}\n\n@inproceedings{padmakumar2024writing,\n  title={Does Writing with Language Models Reduce Content Diversity?},\n  author={Padmakumar, Vishakh and He, He},\n  booktitle={Proceedings of ICLR},\n  year={2024},\n  url={https://arxiv.org/abs/2309.05196}\n}\n\n% === New entries (added 2026-05-15, FR-10) ===\n\n@inproceedings{krishna2023paraphrasing,\n  title={Paraphrasing Evades Detectors of {AI}-Generated Text, but Retrieval is an Effective Defense},\n  author={Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and Iyyer, Mohit},\n  booktitle={Advances in Neural Information Processing Systems},\n  year={2023}\n}\n\n@article{sadasivan2023detect,\n  title={Can {AI}-Generated Text be Reliably Detected?},\n  author={Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},\n  journal={arXiv preprint arXiv:2303.11156},\n  year={2023},\n  url={https://arxiv.org/abs/2303.11156}\n}\n\n@inproceedings{hao2025rewrite,\n  title={Learning to Rewrite: Generalized {LLM}-Generated Text Detection},\n  author={Hao, Wei and Guan, Ran and Lu, Kangjie and Zhang, Shuai},\n  booktitle={Findings of ACL},\n  year={2025}\n}\n\n@inproceedings{shi2025collapse,\n  title={A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective},\n  author={Shi, Lianghe and Wu, Meng and Zhang, Huijie and Zhang, Zekai and Tao, Molei and Qu, Qing},\n  booktitle={Advances in Neural Information Processing Systems},\n  year={2025}\n}\n\n@article{gambetta2024surplexity,\n  title={Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative {AI}},\n  author={Gambetta, Daniele and Gezici, Gizem and Giannotti, Fosca and Pedreschi, Dino and Knott, Alistair and Pappalardo, Luca},\n  journal={arXiv preprint arXiv:2410.12341},\n  year={2024}\n}\n\n@inproceedings{amin2025escaping,\n  title={Escaping Collapse: The Strength of Weak Data for Large Language Model Training},\n  author={Amin, Kareem and Babakniya, Sara and Bie, Alex and Kong, Weiwei and Syed, Umar and Vassilvitskii, Sergei},\n  booktitle={Advances in Neural Information Processing Systems},\n  year={2025}\n}\n\n@inproceedings{kirchenbauer2023watermark,\n  title     = {A Watermark for Large Language Models},\n  author    = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},\n  booktitle = {Proceedings of the 40th International Conference on Machine Learning},\n  pages     = {17061--17084},\n  year      = {2023},\n  volume    = {202},\n  series    = {Proceedings of Machine Learning Research},\n  publisher = {PMLR}\n}\n\n@inproceedings{penedo2024fineweb,\n  title     = {The {FineWeb} Datasets: Decanting the Web for the Finest Text Data at Scale},\n  author    = {Penedo, Guilherme and Kydl{\\'{\\i}}{\\v{c}}ek, Hynek and Ben Allal, Loubna and Lozhkov, Anton and Mitchell, Margaret and Raffel, Colin and Von Werra, Leandro and Wolf, Thomas},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {37},\n  pages     = {30811--30849},\n  year      = {2024}\n}\n\n@inproceedings{gehrmann2019gltr,\n  title     = {{GLTR}: Statistical Detection and Visualization of Generated Text},\n  author    = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander},\n  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics: System Demonstrations},\n  pages     = {111--116},\n  year      = {2019},\n  address   = {Florence, Italy},\n  publisher = {Association for Computational Linguistics},\n  doi       = {10.18653/v1/P19-3019}\n}\n\n@inproceedings{ke2017lightgbm,\n  title     = {{LightGBM}: A Highly Efficient Gradient Boosting Decision Tree},\n  author    = {Ke, Guolin and Meng, Qi and Finley, Thomas and Wang, Taifeng and Chen, Wei and Ma, Weidong and Ye, Qiwei and Liu, Tie-Yan},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {30},\n  year      = {2017}\n}\n\n@article{wu2023survey,\n  title     = {A Survey on {LLM}-generated Text Detection: Necessity, Methods, and Future Directions},\n  author    = {Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Wong, Derek F. and Chao, Lidia S.},\n  journal   = {arXiv preprint arXiv:2310.14724},\n  year      = {2023}\n}\n\n@article{tang2024science,\n  title     = {The Science of Detecting {LLM}-Generated Text},\n  author    = {Tang, Ruixiang and Chuang, Yu-Neng and Hu, Xia},\n  journal   = {Communications of the ACM},\n  volume    = {67},\n  number    = {4},\n  pages     = {50--59},\n  year      = {2024},\n  doi       = {10.1145/3624725}\n}\n\n@inproceedings{oren2024proving,\n  title     = {Proving Test Set Contamination in Black Box Language Models},\n  author    = {Oren, Yonatan and Meister, Nicole and Chatterji, Niladri S. and Ladhak, Faisal and Hashimoto, Tatsunori B.},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations},\n  year      = {2024}\n}\n\n@article{cao2020coral,\n  title     = {Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation},\n  author    = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},\n  journal   = {Pattern Recognition Letters},\n  volume    = {140},\n  pages     = {325--331},\n  year      = {2020},\n  doi       = {10.1016/j.patrec.2020.11.008}\n}\n\n@article{husain2019codesearchnet,\n  title     = {{CodeSearchNet} Challenge: Evaluating the State of Semantic Code Search},\n  author    = {Husain, Hamel and Wu, Ho-Hsiang and Gazit, Tiferet and Allamanis, Miltiadis and Brockschmidt, Marc},\n  journal   = {arXiv preprint arXiv:1909.09436},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1909.09436}\n}\n",
      "numLines": 363,
      "startLine": 1,
      "totalLines": 363
    }
  }
}
```

</details>

---

### Runtime record

_source line 8_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1779172800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "359b37d1-d30f-47ce-94dc-458af53eef7f",
  "session_id": "231f8c0f-eec9-474b-a616-122ee19a9223"
}
```

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
I found the BibTeX entry in the literature notes. Let me confirm "Bertrand" is not in the references.bib (I can see it's not from reading the file). Now I need to add it in the appropriate alphabetical position.

Looking at the bib file structure, entries are organized by sections (Must-Cite, Should-Cite, Probing Classifiers, Model Collapse Avoidability, Beyond-Binary Detection, etc.). The entry should go in the "Model Collapse Avoidability" section or near other model collapse papers.

Actually, looking more carefully, the sections are:


- Must-Cite
- Should-Cite  
- Probing Classifiers
- Model Collapse Avoidability (has bao2024fast and frank2001ordinal - these don't seem to match the section name well)
- Beyond-Binary Detection
- AI-Generated Content Prevalence
- New entries (added 2026-05-16, Round 4 reviewer)
- New entries (added 2026-05-15, FR-10)

The Bertrand et al. paper is about model collapse stability theory. It would fit well near other model collapse papers. Looking at the bib file, the model collapse papers are scattered: shumailov2024collapse (line 63), alemohammad

2024selfconsuming (line 72), dohmatob2024model (line 79), gerstgrasser2024model (line 205), and briesch2023selfconsuming (line 221). The naming convention follows patterns like `shumailov2024collapse`, `alemohammad2024selfconsuming`, and `dohmatob2024model`, so `bertrand2024stability` fits naturally. Alphabetically by first author, Bertrand would slot between Belinkov (line 127) and Briesch (line 221), and the best placement seems to be in the Model Collapse Avoidability section.

Looking at the section structure more closely, I notice the Model Collapse Avoidability section contains entries like `bao2024fast` and `frank2001ordinal` that don't quite match the section name, so the organization is more topic-based than strictly alphabetical. I'll place `bertrand2024stability` near the other model collapse papers, either between `belinkov2022probing` and the section comment at line 133, or right after `alemohammad2024selfconsuming` at line 77.

Actually, the cleanest approach is to put it in the Should-Cite section after `alemohammad2024selfconsuming` since both are ICLR 2024 papers on model collapse. Alphabetically, "Bertrand" fits between "Alemohammad" and "Dohmatob", so that placement makes sense.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "231f8c0f-eec9-474b-a616-122ee19a9223",
  "uuid": "9f4bd511-a22a-48e9-950a-a1f1217f31ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UpLEY5YJMJAPnDeXm4TNjB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9547,
      "cache_read_input_tokens": 24565,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9547
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 10_

确认 `Bertrand` 不在 bib 中，literature notes 已有完整 BibTeX。按首字母顺序插入到 `alemohammad2024selfconsuming` 和 `dohmatob2024model` 之间。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "231f8c0f-eec9-474b-a616-122ee19a9223",
  "uuid": "19320021-123b-46ea-b5dc-816b7224c254",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UpLEY5YJMJAPnDeXm4TNjB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9547,
      "cache_read_input_tokens": 24565,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9547
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Edit · `toolu_01LF1tgNk8tapHk3ueFdFpLq`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib",
  "old_string": "@inproceedings{dohmatob2024model,\n  title={A Tale of Tails: Model Collapse as a Change of Scaling Laws},",
  "new_string": "@inproceedings{bertrand2024stability,\n  title={On the Stability of Iterative Retraining of Generative Models on their Own Data},\n  author={Bertrand, Quentin and Bose, Avishek Joey and Duplessis, Alexandre and Jiralerspong, Marco and Gidel, Gauthier},\n  booktitle={Proceedings of ICLR},\n  year={2024},\n  url={https://arxiv.org/abs/2310.00429}\n}\n\n@inproceedings{dohmatob2024model,\n  title={A Tale of Tails: Model Collapse as a Change of Scaling Laws},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "231f8c0f-eec9-474b-a616-122ee19a9223",
  "uuid": "50a4bdfb-feee-4f7b-8d82-33fad6ed9f8a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UpLEY5YJMJAPnDeXm4TNjB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9547,
      "cache_read_input_tokens": 24565,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9547
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T03:21:57.733Z_

<details><summary>↩ Tool result · `toolu_01LF1tgNk8tapHk3ueFdFpLq`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "231f8c0f-eec9-474b-a616-122ee19a9223",
  "uuid": "1f8f4c8b-57da-4a20-9fab-b10e326c3bd5",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/docs/paper/references.bib",
    "oldString": "@inproceedings{dohmatob2024model,\n  title={A Tale of Tails: Model Collapse as a Change of Scaling Laws},",
    "newString": "@inproceedings{bertrand2024stability,\n  title={On the Stability of Iterative Retraining of Generative Models on their Own Data},\n  author={Bertrand, Quentin and Bose, Avishek Joey and Duplessis, Alexandre and Jiralerspong, Marco and Gidel, Gauthier},\n  booktitle={Proceedings of ICLR},\n  year={2024},\n  url={https://arxiv.org/abs/2310.00429}\n}\n\n@inproceedings{dohmatob2024model,\n  title={A Tale of Tails: Model Collapse as a Change of Scaling Laws},",
    "originalFile": "% === References for gen-depth-contamination ===\n% Source: literature_map.yaml — verified 2026-05-15\n\n% === Must-Cite ===\n\n@inproceedings{drayson2025,\n  title={Machine-Generated Text Detection Prevents Language Model Collapse},\n  author={Drayson, George and Yilmaz, Emine and Lampos, Vasileios},\n  booktitle={Proceedings of EMNLP},\n  year={2025},\n  url={https://arxiv.org/abs/2502.15654}\n}\n\n@inproceedings{schaeffer2025position,\n  title={Position: Model Collapse Does Not Mean What You Think},\n  author={Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Anirudh and Koyejo, Sanmi},\n  booktitle={Proceedings of ICML},\n  year={2025},\n  url={https://arxiv.org/abs/2503.03150}\n}\n\n@inproceedings{kazdan2025collapse,\n  title={Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World},\n  author={Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David and Koyejo, Sanmi},\n  booktitle={Proceedings of ICML},\n  year={2025},\n  url={https://arxiv.org/abs/2410.16713}\n}\n\n@inproceedings{mitchell2023detectgpt,\n  title={{DetectGPT}: Zero-Shot Machine-Generated Text Detection using Probability Curvature},\n  author={Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},\n  booktitle={Proceedings of ICML},\n  year={2023}\n}\n\n% === Should-Cite ===\n\n@article{basani2026diveye,\n  title={{DivEye}: Diversity Boosts {AI}-Generated Text Detection},\n  author={Basani, Advik Raj and Chen, Pin-Yu},\n  journal={Transactions on Machine Learning Research},\n  issn={2835-8856},\n  year={2026},\n  url={https://arxiv.org/abs/2509.18880}\n}\n\n@inproceedings{zawalski2026codec,\n  title={{CoDeC}: Detecting Data Contamination in {LLM}s via In-Context Learning},\n  author={Zawalski, Micha{\\l} and Boubdir, Meriem and Ba{\\l}azy, Klaudia and Nushi, Besmira and Ribalta, Pablo},\n  booktitle={Proceedings of ICLR},\n  year={2026},\n  url={https://arxiv.org/abs/2510.27055}\n}\n\n@inproceedings{zhang2024minkpp,\n  title={Min-{K}\\%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models},\n  author={Zhang, Jingyang and Zheng, Jingwei and Gao, Jing and Miao, Chunyan},\n  booktitle={Proceedings of EMNLP},\n  year={2024}\n}\n\n@article{shumailov2024collapse,\n  title={{AI} Models Collapse When Trained on Recursively Generated Data},\n  author={Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},\n  journal={Nature},\n  volume={631},\n  pages={755--759},\n  year={2024}\n}\n\n@inproceedings{alemohammad2024selfconsuming,\n  title={Self-Consuming Generative Models Go {MAD}},\n  author={Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},\n  booktitle={Proceedings of ICLR},\n  year={2024}\n}\n\n@inproceedings{dohmatob2024model,\n  title={A Tale of Tails: Model Collapse as a Change of Scaling Laws},\n  author={Dohmatob, Elvis and Feng, Yunzhen and Yang, Pin-Yu and Charton, Francois and Kempe, Julia},\n  booktitle={Proceedings of ICML},\n  year={2024}\n}\n\n@inproceedings{xie2023dsir,\n  title={Data Selection for Language Models via Importance Resampling},\n  author={Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},\n  booktitle={Advances in Neural Information Processing Systems},\n  year={2023}\n}\n\n@inproceedings{tirumala2023d4,\n  title={{D4}: Improving {LLM} Pretraining via Document De-Duplication and Diversification},\n  author={Tirumala, Kushal and Markosyan, Aram and Zettlemoyer, Luke and Aghajanyan, Armen},\n  booktitle={Advances in Neural Information Processing Systems},\n  year={2023}\n}\n\n@inproceedings{xie2023doremi,\n  title={{DoReMi}: Optimizing Data Mixtures Speeds Up Language Model Pretraining},\n  author={Xie, Sang Michael and Pham, Hieu and Dong, Xuanyi and Du, Nan and Liu, Hanxiao and Lu, Yifeng and Liang, Percy and Le, Quoc V. and Ma, Tengyu and Yu, Adams Wei},\n  booktitle={Advances in Neural Information Processing Systems},\n  year={2023}\n}\n\n@inproceedings{hans2024binoculars,\n  title={Spotting {LLMs} With Binoculars},\n  author={Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},\n  booktitle={Proceedings of ICML},\n  year={2024}\n}\n\n% === Probing Classifiers ===\n\n@inproceedings{alain2017understanding,\n  title={Understanding Intermediate Layers Using Linear Classifier Probes},\n  author={Alain, Guillaume and Bengio, Yoshua},\n  booktitle={ICLR Workshop},\n  year={2017}\n}\n\n@article{belinkov2022probing,\n  title={Probing Classifiers: Promises, Shortcomings, and Advances},\n  author={Belinkov, Yonatan},\n  journal={Computational Linguistics},\n  volume={48},\n  number={1},\n  pages={207--219},\n  year={2022}\n}\n\n% === Model Collapse Avoidability ===\n\n@inproceedings{bao2024fast,\n  title={{Fast-DetectGPT}: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature},\n  author={Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},\n  booktitle={Proceedings of ICLR},\n  year={2024},\n  url={https://arxiv.org/abs/2310.05130}\n}\n\n@inproceedings{frank2001ordinal,\n  title={A Simple Approach to Ordinal Classification},\n  author={Frank, Eibe and Hall, Mark},\n  booktitle={Proceedings of ECML},\n  pages={145--156},\n  year={2001}\n}\n\n% === Beyond-Binary Detection ===\n\n@inproceedings{cheng2025beyond,\n  title={Beyond Binary: Towards Fine-Grained {LLM}-Generated Text Detection via Role Recognition and Involvement Measurement},\n  author={Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou},\n  booktitle={Proceedings of the ACM Web Conference (WWW)},\n  year={2025},\n  url={https://arxiv.org/abs/2410.14259}\n}\n\n@article{mehta2025beyond,\n  title={Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models},\n  author={Mehta, Sushant},\n  journal={arXiv preprint arXiv:2511.17602},\n  year={2025},\n  url={https://arxiv.org/abs/2511.17602}\n}\n\n% === AI-Generated Content Prevalence ===\n\n@inproceedings{sun2025aigt,\n  title={Are We in the {AI}-Generated Text World Already? Quantifying and Monitoring {AIGT} on Social Media},\n  author={Sun, Zhen and Zhang, Zongmin and Shen, Xinyue and Zhang, Ziyi and Liu, Yule and Backes, Michael and Zhang, Yang and He, Xinlei},\n  booktitle={Proceedings of ACL},\n  year={2025},\n  url={https://arxiv.org/abs/2412.18148}\n}\n\n@article{spennemann2025quantifying,\n  title={Delving into: the Quantification of {AI}-Generated Content on the Internet (Synthetic Data)},\n  author={Spennemann, Dirk H. R.},\n  journal={arXiv preprint arXiv:2504.08755},\n  year={2025},\n  url={https://arxiv.org/abs/2504.08755}\n}\n\n% === New entries (added 2026-05-16, Round 4 reviewer) ===\n\n@inproceedings{dohmatob2025strong,\n  title={Strong Model Collapse},\n  author={Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},\n  booktitle={Proceedings of ICLR},\n  year={2025},\n  url={https://arxiv.org/abs/2410.04840}\n}\n\n@inproceedings{wang2024semeval,\n  title={{SemEval}-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection},\n  author={Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas},\n  booktitle={Proceedings of SemEval},\n  year={2024},\n  url={https://arxiv.org/abs/2404.14183}\n}\n\n@inproceedings{gerstgrasser2024model,\n  title={Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data},\n  author={Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},\n  booktitle={Proceedings of COLM},\n  year={2024},\n  url={https://arxiv.org/abs/2404.01413}\n}\n\n@inproceedings{guo2024curious,\n  title={The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text},\n  author={Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chloe},\n  booktitle={Findings of NAACL},\n  year={2024},\n  url={https://arxiv.org/abs/2311.09807}\n}\n\n@article{briesch2023selfconsuming,\n  title={Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop},\n  author={Briesch, Martin and Sobania, Dominik and Rothlauf, Franz},\n  journal={arXiv preprint arXiv:2311.16822},\n  year={2023},\n  url={https://arxiv.org/abs/2311.16822}\n}\n\n@inproceedings{padmakumar2024writing,\n  title={Does Writing with Language Models Reduce Content Diversity?},\n  author={Padmakumar, Vishakh and He, He},\n  booktitle={Proceedings of ICLR},\n  year={2024},\n  url={https://arxiv.org/abs/2309.05196}\n}\n\n% === New entries (added 2026-05-15, FR-10) ===\n\n@inproceedings{krishna2023paraphrasing,\n  title={Paraphrasing Evades Detectors of {AI}-Generated Text, but Retrieval is an Effective Defense},\n  author={Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and Iyyer, Mohit},\n  booktitle={Advances in Neural Information Processing Systems},\n  year={2023}\n}\n\n@article{sadasivan2023detect,\n  title={Can {AI}-Generated Text be Reliably Detected?},\n  author={Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},\n  journal={arXiv preprint arXiv:2303.11156},\n  year={2023},\n  url={https://arxiv.org/abs/2303.11156}\n}\n\n@inproceedings{hao2025rewrite,\n  title={Learning to Rewrite: Generalized {LLM}-Generated Text Detection},\n  author={Hao, Wei and Guan, Ran and Lu, Kangjie and Zhang, Shuai},\n  booktitle={Findings of ACL},\n  year={2025}\n}\n\n@inproceedings{shi2025collapse,\n  title={A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective},\n  author={Shi, Lianghe and Wu, Meng and Zhang, Huijie and Zhang, Zekai and Tao, Molei and Qu, Qing},\n  booktitle={Advances in Neural Information Processing Systems},\n  year={2025}\n}\n\n@article{gambetta2024surplexity,\n  title={Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative {AI}},\n  author={Gambetta, Daniele and Gezici, Gizem and Giannotti, Fosca and Pedreschi, Dino and Knott, Alistair and Pappalardo, Luca},\n  journal={arXiv preprint arXiv:2410.12341},\n  year={2024}\n}\n\n@inproceedings{amin2025escaping,\n  title={Escaping Collapse: The Strength of Weak Data for Large Language Model Training},\n  author={Amin, Kareem and Babakniya, Sara and Bie, Alex and Kong, Weiwei and Syed, Umar and Vassilvitskii, Sergei},\n  booktitle={Advances in Neural Information Processing Systems},\n  year={2025}\n}\n\n@inproceedings{kirchenbauer2023watermark,\n  title     = {A Watermark for Large Language Models},\n  author    = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},\n  booktitle = {Proceedings of the 40th International Conference on Machine Learning},\n  pages     = {17061--17084},\n  year      = {2023},\n  volume    = {202},\n  series    = {Proceedings of Machine Learning Research},\n  publisher = {PMLR}\n}\n\n@inproceedings{penedo2024fineweb,\n  title     = {The {FineWeb} Datasets: Decanting the Web for the Finest Text Data at Scale},\n  author    = {Penedo, Guilherme and Kydl{\\'{\\i}}{\\v{c}}ek, Hynek and Ben Allal, Loubna and Lozhkov, Anton and Mitchell, Margaret and Raffel, Colin and Von Werra, Leandro and Wolf, Thomas},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {37},\n  pages     = {30811--30849},\n  year      = {2024}\n}\n\n@inproceedings{gehrmann2019gltr,\n  title     = {{GLTR}: Statistical Detection and Visualization of Generated Text},\n  author    = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander},\n  booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics: System Demonstrations},\n  pages     = {111--116},\n  year      = {2019},\n  address   = {Florence, Italy},\n  publisher = {Association for Computational Linguistics},\n  doi       = {10.18653/v1/P19-3019}\n}\n\n@inproceedings{ke2017lightgbm,\n  title     = {{LightGBM}: A Highly Efficient Gradient Boosting Decision Tree},\n  author    = {Ke, Guolin and Meng, Qi and Finley, Thomas and Wang, Taifeng and Chen, Wei and Ma, Weidong and Ye, Qiwei and Liu, Tie-Yan},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {30},\n  year      = {2017}\n}\n\n@article{wu2023survey,\n  title     = {A Survey on {LLM}-generated Text Detection: Necessity, Methods, and Future Directions},\n  author    = {Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Wong, Derek F. and Chao, Lidia S.},\n  journal   = {arXiv preprint arXiv:2310.14724},\n  year      = {2023}\n}\n\n@article{tang2024science,\n  title     = {The Science of Detecting {LLM}-Generated Text},\n  author    = {Tang, Ruixiang and Chuang, Yu-Neng and Hu, Xia},\n  journal   = {Communications of the ACM},\n  volume    = {67},\n  number    = {4},\n  pages     = {50--59},\n  year      = {2024},\n  doi       = {10.1145/3624725}\n}\n\n@inproceedings{oren2024proving,\n  title     = {Proving Test Set Contamination in Black Box Language Models},\n  author    = {Oren, Yonatan and Meister, Nicole and Chatterji, Niladri S. and Ladhak, Faisal and Hashimoto, Tatsunori B.},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations},\n  year      = {2024}\n}\n\n@article{cao2020coral,\n  title     = {Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation},\n  author    = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},\n  journal   = {Pattern Recognition Letters},\n  volume    = {140},\n  pages     = {325--331},\n  year      = {2020},\n  doi       = {10.1016/j.patrec.2020.11.008}\n}\n\n@article{husain2019codesearchnet,\n  title     = {{CodeSearchNet} Challenge: Evaluating the State of Semantic Code Search},\n  author    = {Husain, Hamel and Wu, Ho-Hsiang and Gazit, Tiferet and Allamanis, Miltiadis and Brockschmidt, Marc},\n  journal   = {arXiv preprint arXiv:1909.09436},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1909.09436}\n}\n",
    "structuredPatch": [
      {
        "oldStart": 76,
        "oldLines": 6,
        "newStart": 76,
        "newLines": 14,
        "lines": [
          "   year={2024}",
          " }",
          " ",
          "+@inproceedings{bertrand2024stability,",
          "+  title={On the Stability of Iterative Retraining of Generative Models on their Own Data},",
          "+  author={Bertrand, Quentin and Bose, Avishek Joey and Duplessis, Alexandre and Jiralerspong, Marco and Gidel, Gauthier},",
          "+  booktitle={Proceedings of ICLR},",
          "+  year={2024},",
          "+  url={https://arxiv.org/abs/2310.00429}",
          "+}",
          "+",
          " @inproceedings{dohmatob2024model,",
          "   title={A Tale of Tails: Model Collapse as a Change of Scaling Laws},",
          "   author={Dohmatob, Elvis and Feng, Yunzhen and Yang, Pin-Yu and Charton, Francois and Kempe, Julia},"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 13_

已添加 `bertrand2024stability` 条目，位于 `alemohammad2024selfconsuming` 和 `dohmatob2024model` 之间。Bib key 格式与现有条目一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "231f8c0f-eec9-474b-a616-122ee19a9223",
  "uuid": "afdcb556-2823-4c95-9ebb-0368ff7ee5fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FbrdsVNxPwtrwHAjFsE4wR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1303,
      "cache_read_input_tokens": 34112,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1303
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 14_

已添加 `bertrand2024stability` 条目，位于 `alemohammad2024selfconsuming` 和 `dohmatob2024model` 之间。Bib key 格式与现有条目一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 38409,
  "duration_api_ms": 47500,
  "num_turns": 4,
  "stop_reason": "end_turn",
  "session_id": "231f8c0f-eec9-474b-a616-122ee19a9223",
  "total_cost_usd": 0.22100550000000002,
  "usage": {
    "input_tokens": 5,
    "cache_creation_input_tokens": 23574,
    "cache_read_input_tokens": 70518,
    "output_tokens": 1491,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 23574,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 63,
        "cache_read_input_tokens": 34112,
        "cache_creation_input_tokens": 1303,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1303
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-opus-4-6": {
      "inputTokens": 5,
      "outputTokens": 1491,
      "cacheReadInputTokens": 70518,
      "cacheCreationInputTokens": 23574,
      "webSearchRequests": 0,
      "costUSD": 0.2198965,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    },
    "claude-haiku-4-5-20251001": {
      "inputTokens": 984,
      "outputTokens": 25,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0011090000000000002,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "b65bb0f8-e2ac-4eef-bd17-6314f820a1d2"
}
```

</details>

---
