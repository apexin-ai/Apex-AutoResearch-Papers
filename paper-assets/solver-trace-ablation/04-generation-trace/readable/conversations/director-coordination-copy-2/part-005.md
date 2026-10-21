# Director coordination — Part 5 of 12

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

[← Part 4](part-004.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 6 →](part-006.md) · [Structured JSON](../../../sessions/b1/b1d47a1a2aa91fd38090.json)

## Round 99

### Tool result

_source line 1157 · 2026-05-19T02:35:08.246729+00:00_

1	% Appendix: solver-trace-ablation
2	
3	\section{Experimental Setup}
4	\label{app:setup}
5	
6	Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
7	All RL conditions use the same GRPO configuration; only the reward function differs.
8	Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).
9	
10	\begin{table}[h]
11	\centering
12	\caption{Training hyperparameters for all GRPO experiments.}
13	\label{tab:hyperparams}
14	\footnotesize
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{@{}ll@{}}
17	\toprule
18	\textbf{Parameter} & \textbf{Value} \\
19	\midrule
20	\multicolumn{2}{@{}l}{\textit{Model}} \\
21	Base model & Qwen3-4B \\
22	Precision & BF16 \\
23	\midrule
24	\multicolumn{2}{@{}l}{\textit{GRPO Training}} \\
25	Rollouts per prompt ($K$) & 4 \\
26	Training steps (default) & 500 \\
27	Training steps (extended) & 1000 \\
28	Learning rate & $1 \times 10^{-6}$ \\
29	Per-device batch size & 4 \\
30	Gradient accumulation steps & 2 \\
31	Effective batch size & 8 \\
32	Max completion length & 512 tokens \\
33	Random seeds & 42, 43, 44 \\
34	\midrule
35	\multicolumn{2}{@{}l}{\textit{Data}} \\
36	Training set & FOLIO, 500 examples \\
37	Evaluation set & FOLIO, 100 examples (held-out) \\
38	Data file & \texttt{train\_500\_seed42} \\
39	\midrule
40	\multicolumn{2}{@{}l}{\textit{Solvers}} \\
41	FOL solver & Prover9 \\
42	Prolog solver & SWI-Prolog 8.4.2 \\
43	\midrule
44	\multicolumn{2}{@{}l}{\textit{Evaluation}} \\
45	Decoding & Greedy ($T{=}0$) \\
46	ISR computation & \texttt{eval\_sta.py} \\
47	ISR variant & Proved-only (ISR$^*$) \\
48	\bottomrule
49	\end{tabular}}
50	\end{table}
51	
52	\paragraph{Evaluation protocol.}
53	All cross-run ISR values are recomputed uniformly by a single evaluator (\texttt{eval\_sta.py}) so that training-log ISR is never compared across runs.
54	The evaluation file \texttt{proofwriter\_fol\_100.jsonl} is a legacy filename conta
…[truncated 50386 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 1158 · 2026-05-19T02:35:08.247262+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 1159 · 2026-05-19T02:35:09.151262+00:00_

1	\section*{Responsible NLP Research Checklist}
2	
3	\paragraph{A. For every submission:}
4	
5	\begin{enumerate}[label=A\arabic*.,leftmargin=*]
6	\item \textbf{Did you describe the limitations of your work?}
7	Yes. Section~\ref{sec:limitations} discusses single model family and dataset, ISR's syntactic-only nature, limited seed counts, classifier coverage gaps, data scale, and temporal-snapshot caveats.
8	
9	\item \textbf{Did you discuss any potential risks of your work?}
10	Yes. Section~\ref{sec:ethics} discusses implications for AI safety, specifically that metrics designed to detect misalignment may themselves become optimization targets.
11	
12	\item \textbf{Do the abstract and introduction summarize the paper's main claims?}
13	Yes. Both summarize the three contributions (C1--C3) and key quantitative findings.
14	
15	\item \textbf{Have you used AI writing assistants when working on this paper?}
16	Yes. AI assistants were used for drafting and editing. All scientific claims, experimental results, and analyses were verified by the authors.
17	\end{enumerate}
18	
19	\paragraph{B. Did you use or create scientific artifacts?}
20	Yes.
21	
22	\begin{enumerate}[label=B\arabic*.,leftmargin=*]
23	\item \textbf{Did you cite the creators of artifacts you used?}
24	Yes. We cite FOLIO~\citep{folio}, Qwen3~\citep{qwen3}, GRPO~\citep{deepseekmath}, Prover9~\citep{mccune-prover9}, and SWI-Prolog~\citep{wielemaker2012swi}.
25	
26	\item \textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?}
27	Yes. Qwen3 is released under the Tongyi Qianwen License; FOLIO is released under CC BY-SA 4.0. Both permit research use.
28	
29	\item \textbf{Did you discuss if your use of existing artifact(s) was consistent with their intended use?}
30	Yes. FOLIO is used for its intended purpose (NLI evaluation); Qwen3 is used within its intended scope (language model fine-tuning).
31	
32	\item \textbf{Did you discuss the steps taken to check whether the data that you 
…[truncated 2600 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 1160 · 2026-05-19T02:35:09.302419+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 1161 · 2026-05-19T02:35:09.353176+00:00_

1	\section{Ethics Statement}
2	\label{sec:ethics}
3	
4	This work documents failure modes of reward optimization in solver-backed RL systems.
5	Our findings (that structural diagnostics can be gamed when used as training signals) carry implications for AI safety: they demonstrate that metrics designed to detect misalignment may themselves become targets of optimization, a concern relevant to scalable oversight.
6	We release our taxonomy and diagnostic tools to help practitioners detect reward hacking in their own systems.
7	All experiments use publicly available datasets (FOLIO) and open-weight models (Qwen3-4B); no human subjects are involved.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1162 · 2026-05-19T02:35:09.353622+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1163 · 2026-05-19T02:35:09.756147+00:00_

1	issues:
2	# ===== 历史 issues (Round 0-3, 全部 resolved) =====
3	- id: "R1-W1"
4	  summary: "统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例"
5	  category: experiment
6	  severity: critical
7	  status: resolved
8	  first_raised_round: 0
9	  last_seen_round: 2
10	  resolution: "β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。Fisher exact test + Wilson 95% CI 已加入。eval 集 100 例限制在 limitations.tex 讨论。"
11	  resolution_round: 2
12	
13	- id: "RV-EVAL-FALLBACK"
14	  summary: "eval_sta.py test_100.jsonl 静默 fallback 已移除"
15	  category: experiment
16	  severity: critical
17	  status: resolved
18	  first_raised_round: 1
19	  last_seen_round: 1
20	  resolution: "第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)，无 fallback。"
21	  resolution_round: 1
22	
23	- id: "RV-D060-NARRATIVE"
24	  summary: "D060 'Goodhart instability' 叙事：77pp PR 差距在同一测试集上确认成立"
25	  category: experiment
26	  severity: critical
27	  status: resolved
28	  first_raised_round: 1
29	  last_seen_round: 1
30	  resolution: "β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。"
31	  resolution_round: 2
32	
33	- id: "RV-FIG2-STALE-SCRIPT"
34	  summary: "figures/paper/gen_fig2.py 旧脚本数据错误"
35	  category: format
36	  severity: warning
37	  status: resolved
38	  first_raised_round: 1
39	  last_seen_round: 1
40	  resolution: "已修复。"
41	  resolution_round: 1
42	
43	- id: "R1-W2"
44	  summary: "ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量"
45	  category: framing
46	  severity: critical
47	  status: resolved
48	  first_raised_round: 0
49	  last_seen_round: 0
50	  resolution: "method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。"
51	  resolution_round: 2
52	
53	- id: "R2-W1"
54	  summary: "Limitations section 格式不合规"
55	  category: format
56	  severity: critical
57	  status: resolved
58	  first_raised_round: 0
59	  last_seen_round: 2
60	  resolution: "独立 limitations.tex 已创建，位于 references 之前。"
61	  resolution_round: 3
62	
63	- id: "R2-W2"
64	  summary: "实验仅用单一模型 (Qwen3-4B)
…[truncated 27630 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1164 · 2026-05-19T02:35:25.055109+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/constraints.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/constraints.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 1165 · 2026-05-19T02:35:25.609153+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/constraints.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Glob",
  "elapsed_ms": 554
}
```

</details>

---


### Tool call

_source line 1166 · 2026-05-19T02:35:25.609639+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/references.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 1167 · 2026-05-19T02:35:25.660907+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/_project/paper/references.bib
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1168 · 2026-05-19T02:35:28.524097+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/constraints.yaml",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/constraints.yaml",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 1169 · 2026-05-19T02:35:28.926246+00:00_

1	_next_id: 14
2	constraints:
3	- id: C001
4	  added: 2026-05-13 23:57 UTC
5	  summary: 所有实验统一使用 data/train_500_seed42.jsonl 作为训练数据，禁止使用 proofwriter_fol_500.jsonl
6	    或其他数据文件
7	  scope: all
8	  reason: 'Reviewer CRITICAL: plan001-s43 使用了不同数据文件导致多 seed 对比 confound。多 seed 实验必须控制数据变量，seed
9	    仅控制模型初始化和训练随机性。'
10	- id: C002
11	  added: 2026-05-14 00:01 UTC
12	  summary: 提交训练任务前必须用 export CUDA_VISIBLE_DEVICES=N 显式设置 GPU，禁止 inline 赋值（bash -c
13	    VAR=X cmd），提交后验证 nvidia-smi 确认只占用分配的 GPU
14	  scope: all
15	  reason: plan013 因 CUDA_VISIBLE_DEVICES inline 赋值引号问题越界占用两张 GPU，导致 plan001-s43 OOM
16	    死亡。这是第二次 GPU 冲突事故。
17	- id: C003
18	  added: 2026-05-14 01:40 UTC
19	  summary: 训练配置必须设置 save_total_limit=1 且禁用/限制 completions parquet 保存，防止磁盘耗尽
20	  scope: all
21	  reason: plan013-r3 和 plan001-s43-r3 因磁盘 250G/250G 满导致 step 23/28 崩溃。根因：TRL 每实验保存
22	    3 份模型权重（~48GB）+ completions parquet（~2.5GB）。
23	- id: C004
24	  added: 2026-05-14 02:36 UTC
25	  summary: 跨 seed/跨 run 的 ISR 对比必须使用 eval_sta.py 统一评估，禁止引用训练日志 ISR 做跨 run 对比（不同 run
26	    可能使用不同版本的 ISR 计算代码）
27	  scope: all
28	  reason: Reviewer 核实发现 plan001-s42-r2 训练日志 ISR 使用 binary _fast_fn，plan001-s43-r4
29	    使用 full STA _full_fn，同一指标名下计算方法不同导致不可比。论文中所有 ISR 数据必须来自 eval_sta.py 统一评估。
30	- id: C005
31	  added: 2026-05-14 04:01 UTC
32	  summary: 所有 worker（含 fix/ops 类）启动任何 Python 进程前必须显式设置 CUDA_VISIBLE_DEVICES，禁止裸跑
33	  scope: worker
34	  reason: fix worker 未设 CUDA_VISIBLE_DEVICES 导致测试进程泄漏到 cuda:1（plan017 训练卡），占用 8638
35	    MiB 显存。2026-05-14 事故。
36	- id: C006
37	  added: 2026-05-14 11:53 UTC
38	  summary: 论文讨论 ISR 时必须区分两种语义：exec-only 的 low ISR = 冗余编码（重复 ground facts 导致 n_necessary=0），exec+STA
39	    的 high ISR = metric gaming（Goodhart 效应）。不可将 ISR 差异直接等同于 reasoning 能力差异。
40	  scope: all
41	  reason: Reviewer 发现 Prolog exec-only 生成大量重复 ground facts（如 penguin(fido). 出现 3 次），per-clause
42	    ablation 下删任一重复不影响结果，ISR=0。这是冗余不是无推理。如不区分，审稿人会误读 ISR 差异。
43	- id: C007
44	  added: 2026-05-14 23:23 UTC
45	  summary: kill_job 后必须 nvidia-smi
…[truncated 273 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1170 · 2026-05-19T02:35:28.926856+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 1171 · 2026-05-19T02:35:28.977865+00:00_

1	% ============================================================
2	% Category 1: Neurosymbolic reasoning + RL/GRPO
3	% ============================================================
4	
5	@article{deepseekmath,
6	  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},
7	  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},
8	  journal      = {arXiv preprint arXiv:2402.03300},
9	  year         = {2024},
10	  eprint       = {2402.03300},
11	  archivePrefix = {arXiv},
12	  primaryClass = {cs.AI},
13	}
14	
15	@article{logic-rl,
16	  author       = {Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo},
17	  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},
18	  journal      = {arXiv preprint arXiv:2502.14768},
19	  year         = {2025},
20	  eprint       = {2502.14768},
21	  archivePrefix = {arXiv},
22	  primaryClass = {cs.AI},
23	}
24	
25	@article{mellgren-prolog-grpo,
26	  author       = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke},
27	  title        = {{Training Language Models to Use Prolog as a Tool}},
28	  journal      = {arXiv preprint arXiv:2512.07407},
29	  year         = {2025},
30	  eprint       = {2512.07407},
31	  archivePrefix = {arXiv},
32	  primaryClass = {cs.AI},
33	}
34	
35	@inproceedings{satlm,
36	  author       = {Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett},
37	  title        = {{SatLM: Satisfiability-Aided Language Models Using Declarative Prompting}},
38	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
39	  year         = {2023},
40	}
41	
42	% ============================================================
43	% Category 2: Reward shaping for code/formal verification
44	% ============================================================
45	
46	@inproceedings{lightman-verify-step,
47	  author 
…[truncated 19976 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1172 · 2026-05-19T02:35:46.972343+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 1173 · 2026-05-19T02:35:47.024618+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 1174 · 2026-05-19T02:35:53.840008+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Find external review config",
  "subagent_type": "Explore",
  "prompt": "Find any project configuration file for the solver-trace-ablation project that contains \"external_review\" or \"paperreview\" settings. Check files like config.yaml, project.yaml, settings.yaml, or any yaml/json config files under /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/ and /home/ubuntu/.agent-ml-research-idea_gen_0509_3/. Report if external review is enabled (true/false) or if no such config exists."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Agent",
  "tool_args": {
    "description": "Find external review config",
    "subagent_type": "Explore",
    "prompt": "Find any project configuration file for the solver-trace-ablation project that contains \"external_review\" or \"paperreview\" settings. Check files like config.yaml, project.yaml, settings.yaml, or any yaml/json config files under /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/ and /home/ubuntu/.agent-ml-research-idea_gen_0509_3/. Report if external review is enabled (true/false) or if no such config exists."
  }
}
```

</details>

---


### Tool call

_source line 1175 · 2026-05-19T02:35:55.351099+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/**/*.{yaml,yml,json}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/**/*.{yaml,yml,json}"
  }
}
```

</details>

---


### Tool result

_source line 1176 · 2026-05-19T02:35:55.452129+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/workers/worker_code_sta-core_20260513T173855_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/workers/worker_data_proofwriter-prep_20260513T174438_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/workers/worker_infra_env-setup_20260513T173539_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/workers/worker_code_sta-bugfix-p0_20260513T174744_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/checkpoints/sta-phase0-baseline_PREPARING_20260513T175148.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/workers/worker_code_sta-bugfix-p1_20260513T175253_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/checkpoints/sta-phase0-baseline_QUEUED_20260513T175630.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/checkpoints/sta-phase0-baseline_RUNNING_20260513T175638.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/workers/worker_code_xor-normalize_20260513T175523_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/checkpoints/sta-phase0-baseline_RUNNING_20260513T180453.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/checkpoints/sta-phase0-baseline_DONE_20260513T180456.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/workers/worker_exp_phase0-baseline_20260513T175225_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/checkpoints/sta-phase0-baseline_DONE_20260513T180651.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/checkpoints/sta-gt-isr-baseline_PREPARING_20260513T181113.json
/home
…[truncated 12522 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Glob",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1177 · 2026-05-19T02:35:55.502824+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/*.{yaml,yml,json}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/*.{yaml,yml,json}"
  }
}
```

</details>

---


### Tool result

_source line 1178 · 2026-05-19T02:35:55.553552+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/workspace.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/mcp_config.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/backend.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/mcp_config_no_project.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/feishu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/mcp_config_idea_reviewer.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/idea_generator/logs/_index.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/mcp_config_director.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/mcp_config_reviewer.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/mcp_config_worker_421decd2032b14f2ef6566c2172240c1.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/logs/workers/worker_research_circuit-api-survey_20260512T095923_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/mcp_config_worker_943f40256720b8f6634ec1980a24acc1.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/logs/workers/worker_code_mvp-k3-framework_20260512T101924_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/logs/workers/worker_research_large-model-third-method_20260512T101957_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/mcp_config_worker_ddf919c12f9233b9c1be7884efc37bb6.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/logs/workers/worker_code_mvp-deploy-run_20260512T102955_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/logs/workers/worker_code_mvp-collect-results_20260512T111730_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/mcp_config_worker_0aa51d591547913249ab7a68dc681be8.json
/home/ubuntu/.agent-ml-res
…[truncated 12129 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1179 · 2026-05-19T02:35:58.325588+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3"
  }
}
```

</details>

---


### Tool call

_source line 1180 · 2026-05-19T02:35:58.478892+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/workspace.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/workspace.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1181 · 2026-05-19T02:35:58.530970+00:00_

1	projects: {}
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool result

_source line 1182 · 2026-05-19T02:36:02.760795+00:00_

Found 13 files
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/chats/feishu_group_oc_5abafbb382eb7c81e8a38090e46323e7_director.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/global/logs/system.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/chats/feishu_group_oc_a771c2a33d631dd40256ecd5c3a6648e_director.jsonl
AGENTS.md
CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/chats/feishu_group_oc_8f0788a2307711c1b7fbf59b4cbe0473_paper_agent.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_reports/round_12.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/chats/archive/feishu_group_oc_a771c2a33d631dd40256ecd5c3a6648e_director_20260517T210744_407264.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_reports/round_7.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/global/logs/system.log.1
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_reports/round_4.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/chats/archive/feishu_group_oc_a771c2a33d631dd40256ecd5c3a6648e_director_20260517T105808_471807.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_reports/round_2.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Grep",
  "elapsed_ms": 4435
}
```

</details>

---


### Tool call

_source line 1183 · 2026-05-19T02:36:04.425976+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation -maxdepth 2 -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" | grep -E \"(config|project|settings)\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation -maxdepth 2 -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" | grep -E \"(config|project|settings)\" | head -20"
  }
}
```

</details>

---


### Tool call

_source line 1184 · 2026-05-19T02:36:04.581296+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/"
  }
}
```

</details>

---


### Tool result

_source line 1185 · 2026-05-19T02:36:04.632380+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/constraints.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/checkpoints/plan002-additive-b01-s44_PENDING_20260514T083815.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/checkpoints/plan009-sft-baseline-s44-1000_RUNNING_20260515T124934.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/checkpoints/d134-4b-random-b01-s50_PENDING_20260518T221543.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/checkpoints/plan009-sft-baseline-s42-r4_QUEUED_20260514T114039.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/checkpoints/plan018-additive-random-b01-s43-r3_PENDING_20260515T162522.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/checkpoints/plan018-additive-random-b01-s42-1000-r3_QUEUED_20260515T102649.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/checkpoints/w2-qwen3-1.7b-isr-pilot_DONE_20260516T115559.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/checkpoints/d134-4b-isr-b01-s48_RUNNING_20260518T123337.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/checkpoints/sweep-random-b005-s44_PREPARING_20260517T130728.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/checkpoints/
…[truncated 625 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 206
}
```

</details>

---


### Tool result

_source line 1186 · 2026-05-19T02:36:04.683192+00:00_

total 820
drwxr-xr-x 13 ubuntu ubuntu   4096 May 19 02:33 .
drwxrwxr-x  5 ubuntu ubuntu   4096 May 13 17:31 ..
drwxr-xr-x  3 ubuntu ubuntu   4096 May 13 17:31 .claude
drwxr-xr-x  7 ubuntu ubuntu   4096 May 19 02:29 .git
drwxr-xr-x  6 ubuntu ubuntu   4096 May 14 17:33 .venv
-rw-r--r--  1 ubuntu ubuntu  17193 May 19 02:35 AGENTS.md
-rw-r--r--  1 ubuntu ubuntu      0 May 13 17:33 ROADMAP.lock
-rw-------  1 ubuntu ubuntu   3053 May 19 02:33 ROADMAP.md
drwxr-xr-x 32 ubuntu ubuntu   4096 May 19 02:22 artifacts
drwxr-xr-x  2 ubuntu ubuntu 106496 May 19 02:15 checkpoints
-rw-r--r--  1 ubuntu ubuntu      0 May 13 23:57 constraints.lock
-rw-------  1 ubuntu ubuntu   5490 May 15 14:23 constraints.yaml
-rw-r--r--  1 ubuntu ubuntu      0 May 13 17:34 decisions.lock
-rw-------  1 ubuntu ubuntu 138535 May 19 02:27 decisions.yaml
drwxr-xr-x  4 ubuntu ubuntu   4096 May 15 05:24 docs
-rwxr-xr-x  1 ubuntu ubuntu      0 May 13 21:57 dream_registry.lock
-rw-------  1 ubuntu ubuntu   2473 May 14 18:26 dream_registry.yaml
-rw-r--r--  1 ubuntu ubuntu   2478 May 14 18:26 dream_registry.yaml.bak
-rw-r--r--  1 ubuntu ubuntu      0 May 13 22:19 experiment_plan.lock
-rw-------  1 ubuntu ubuntu   6579 May 15 16:27 experiment_plan.yaml
drwxr-xr-x  3 ubuntu ubuntu   4096 May 14 17:30 figures
-rw-r--r--  1 ubuntu ubuntu  44668 May 15 11:39 literature_map.yaml
drwxr-xr-x  4 ubuntu ubuntu   4096 May 13 17:35 logs
-rw-r--r--  1 ubuntu ubuntu   6936 May 18 00:12 memory.md
-rw-r--r--  1 ubuntu ubuntu      0 May 16 23:50 mistakes.lock
-rw-------  1 ubuntu ubuntu   7800 May 18 18:00 mistakes.yaml
drwxr-xr-x  4 ubuntu ubuntu   4096 May 19 02:31 paper
-rw-r--r--  1 ubuntu ubuntu  42980 May 17 14:34 paper_framing.md
-rw-r--r--  1 ubuntu ubuntu      0 May 14 19:10 paper_provenance.lock
-rw-------  1 ubuntu ubuntu  17492 May 17 20:22 paper_provenance.yaml
-rw-r--r--  1 ubuntu ubuntu  12997 May 15 01:13 paper_review_loop10.md
-rw-r--r--  1 ubuntu ubuntu      0 May 13 17:51 registry.lock
-rw-------  1 ubuntu ubu
…[truncated 344 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1187 · 2026-05-19T02:36:06.892324+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/"
  }
}
```

</details>

---


### Tool result

_source line 1188 · 2026-05-19T02:36:07.144887+00:00_

total 32
drwxr-xr-x  3 ubuntu ubuntu  4096 May 13 17:31 .
drwxr-xr-x 13 ubuntu ubuntu  4096 May 19 02:33 ..
-rw-r--r--  1 ubuntu ubuntu 17193 May 19 02:35 CLAUDE.md
drwxr-xr-x 80 ubuntu ubuntu  4096 May 18 20:03 sessions

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 1189 · 2026-05-19T02:36:07.195784+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview|review.*enabled|external.*enabled",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "type": "yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview|review.*enabled|external.*enabled",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
    "type": "yaml"
  }
}
```

</details>

---


### Tool result

_source line 1190 · 2026-05-19T02:36:07.246471+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1191 · 2026-05-19T02:36:08.606944+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -100 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/registry.yaml | grep -A 5 -B 5 \"external\\|review\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "head -100 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/registry.yaml | grep -A 5 -B 5 \"external\\|review\""
  }
}
```

</details>

---


### Tool result

_source line 1192 · 2026-05-19T02:36:08.758892+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1193 · 2026-05-19T02:36:08.759397+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/constraints.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/constraints.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1194 · 2026-05-19T02:36:08.810204+00:00_

_next_id: 14
constraints:
- id: C001
  added: 2026-05-13 23:57 UTC
  summary: 所有实验统一使用 data/train_500_seed42.jsonl 作为训练数据，禁止使用 proofwriter_fol_500.jsonl
    或其他数据文件
  scope: all
  reason: 'Reviewer CRITICAL: plan001-s43 使用了不同数据文件导致多 seed 对比 confound。多 seed 实验必须控制数据变量，seed
    仅控制模型初始化和训练随机性。'
- id: C002
  added: 2026-05-14 00:01 UTC
  summary: 提交训练任务前必须用 export CUDA_VISIBLE_DEVICES=N 显式设置 GPU，禁止 inline 赋值（bash -c
    VAR=X cmd），提交后验证 nvidia-smi 确认只占用分配的 GPU
  scope: all
  reason: plan013 因 CUDA_VISIBLE_DEVICES inline 赋值引号问题越界占用两张 GPU，导致 plan001-s43 OOM
    死亡。这是第二次 GPU 冲突事故。
- id: C003
  added: 2026-05-14 01:40 UTC
  summary: 训练配置必须设置 save_total_limit=1 且禁用/限制 completions parquet 保存，防止磁盘耗尽
  scope: all
  reason: plan013-r3 和 plan001-s43-r3 因磁盘 250G/250G 满导致 step 23/28 崩溃。根因：TRL 每实验保存
    3 份模型权重（~48GB）+ completions parquet（~2.5GB）。
- id: C004
  added: 2026-05-14 02:36 UTC
  summary: 跨 seed/跨 run 的 ISR 对比必须使用 eval_sta.py 统一评估，禁止引用训练日志 ISR 做跨 run 对比（不同 run
    可能使用不同版本的 ISR 计算代码）
  scope: all
  reason: Reviewer 核实发现 plan001-s42-r2 训练日志 ISR 使用 binary _fast_fn，plan001-s43-r4
    使用 full STA _full_fn，同一指标名下计算方法不同导致不可比。论文中所有 ISR 数据必须来自 eval_sta.py 统一评估。
- id: C005
  added: 2026-05-14 04:01 UTC
  summary: 所有 worker（含 fix/ops 类）启动任何 Python 进程前必须显式设置 CUDA_VISIBLE_DEVICES，禁止裸跑
  scope: worker
  reason: fix worker 未设 CUDA_VISIBLE_DEVICES 导致测试进程泄漏到 cuda:1（plan017 训练卡），占用 8638
    MiB 显存。2026-05-14 事故。
- id: C006
  added: 2026-05-14 11:53 UTC
  summary: 论文讨论 ISR 时必须区分两种语义：exec-only 的 low ISR = 冗余编码（重复 ground facts 导致 n_necessary=0），exec+STA
    的 high ISR = metric gaming（Goodhart 效应）。不可将 ISR 差异直接等同于 reasoning 能力差异。
  scope: all
  reason: Reviewer 发现 Prolog exec-only 生成大量重复 ground facts（如 penguin(fido). 出现 3 次），per-clause
    ablation 下删任一重复不影响结果，ISR=0。这是冗余不是无推理。如不区分，审稿人会误读 ISR 差异。
- id: C007
  added: 2026-05-14 23:23 UTC
  summary: kill_job 后必须 nvidia-smi 确认 GPU 释放，submit 前必须 nvidia-smi 确认目标 GPU 无残留进程
  scope: worker
  reason: 同一 session 两次出现 kill tmux → Python orphan → 新实验 OOM 
…[truncated 1817 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1195 · 2026-05-19T02:36:10.827855+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/config -type f \\( -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" \\) -exec grep -l \"external_review\\|paperreview\" {} \\;"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/config -type f \\( -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" \\) -exec grep -l \"external_review\\|paperreview\" {} \\;"
  }
}
```

</details>

---


### Tool result

_source line 1196 · 2026-05-19T02:36:11.229899+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1197 · 2026-05-19T02:36:11.280671+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3 -maxdepth 3 -type f \\( -name \"config.yaml\" -o -name \"project.yaml\" -o -name \"settings.yaml\" -o -name \"config.json\" -o -name \"project.json\" -o -name \"settings.json\" \\)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3 -maxdepth 3 -type f \\( -name \"config.yaml\" -o -name \"project.yaml\" -o -name \"settings.yaml\" -o -name \"config.json\" -o -name \"project.json\" -o -name \"settings.json\" \\)"
  }
}
```

</details>

---


### Tool result

_source line 1198 · 2026-05-19T02:36:11.331401+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1199 · 2026-05-19T02:36:12.989487+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/memory.md"
  }
}
```

</details>

---


### Tool result

_source line 1200 · 2026-05-19T02:36:13.040349+00:00_

1	# Analysis: sweep-exec-only-s45-r2
2	
3	## Training Summary
4	- **Status**: Completed 500/500 steps, EXIT_CODE=0
5	- **Model**: Qwen3-4B, seed=45, execution-only reward
6	- **Data**: data/train_500_seed42.jsonl (500 examples)
7	- **Runtime**: 3282s (~54.7 min), 2 epochs
8	
9	### Training Metrics (Final)
10	| Metric | Value |
11	|--------|-------|
12	| prove_rate | 0.74025 |
13	| mean_isr | 0.3596 |
14	| train_loss | 0.0273 |
15	| parse_rate | 1.0 |
16	| entropy (final) | 0.045 |
17	| frac_reward_zero_std | 1.0 |
18	
19	### Training Trajectory
20	- Steps 1–19: cold start, reward=0
21	- Step 20: first successful proving
22	- Steps ~100+: prove_rate climbing to 0.5–0.75
23	- Steps 400+: consistently 0.75–1.0
24	
25	## Eval Results (proofwriter_fol_100.jsonl)
26	| Metric | Value |
27	|--------|-------|
28	| prove_rate | 99/100 (0.99) |
29	| mean_isr | 0.5012 ± 0.2055 |
30	| median_isr | 0.5000 |
31	| proved_only_isr | 0.5062 |
32	
33	### By Answer Type
34	| Type | n | Proved | Prove Rate | Mean ISR |
35	|------|---|--------|------------|----------|
36	| false | 25 | 25 | 1.00 | 0.590 |
37	| unknown | 41 | 41 | 1.00 | 0.476 |
38	| true | 34 | 33 | 0.971 | 0.467 |
39	
40	## Hacking Taxonomy (classify_h7.py)
41	| Category | Count | Rate |
42	|----------|-------|------|
43	| H7a (text-match tautology) | 93 | 93.9% |
44	| H7b (obfuscated tautology) | 0 | 0.0% |
45	| H7 total | 93 | 93.9% |
46	| H1 (conclusion embedding) | 5 | 5.1% |
47	| H8 (conjunction collapse) | 1 | 1.0% |
48	| **Genuine** | **1** | **1.0%** |
49	| Content-independent | 47 | 47.5% |
50	| Single premise | 92 | 92.9% |
51	
52	## Cross-Seed Comparison (Exec-Only)
53	| Seed | Steps | Prove% | H7% | H1% | H8% | Genuine% |
54	|------|-------|--------|-----|-----|-----|----------|
55	| s42 (plan001-r2) | 500 | 93 | 0 | 87.1 | 6.5 | 7.5 |
56	| s43 (plan001-1000-r2) | 1000 | 90 | 100 | 0 | 0 | 0 |
57	| s44 (plan001-1000-r2) | 1000 | 100 | 0 | 85 | 15 | 0 |
58	| **s45 (this)** | **500** | **99** | **93.9** | **5.
…[truncated 4914 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1201 · 2026-05-19T02:36:15.250402+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/report.md"
  }
}
```

</details>

---


### Tool result

_source line 1202 · 2026-05-19T02:36:15.702944+00:00_

1	# Handover — 2026-05-19
2	
3	> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。
4	
5	## 运行中
6	（无）
7	
8	## 待处理
9	- sweep-random-b01-s46: W4: Random β=0.1 s46 extends random control to 5-seed（排队等待 GPU）
10	- sweep-random-b01-s45: W4: Random β=0.1 s45 extends random control to 5-seed for matched comparison with ISR β=0.1（排队等待 GPU）
11	- d129-1.7b-isr-b03-s44: D129: 1.7B ISR β=0.3 s44 cross-scale replication — tests robustness of reward collapse pattern at 1.7B high-dose ISR（准备中）
12	- d129-1.7b-isr-b03-s43: D129: 1.7B ISR β=0.3 s43 cross-scale replication — s42 showed reward collapse (PR=17%) mirroring 4B pattern; additional seed tests robustness of high-dose collapse at 1.7B（准备中）
13	- d129-1.7b-random-b01-s44: D129: 1.7B Random β=0.1 s44 cross-scale control — tests H9 mode determinism at 1.7B scale under random reward（准备中）
14	- w2-qwen3-7b-pilot: Qwen3-8B exec-only 50-step pilot: 测试 8B 模型能否在 96GB GPU 上跑通，确定 per_device_batch_size (4 vs 2)（准备中）
15	- plan001-exec-only-s45: Exec-only seed=45, 5-seed baseline for tighter confidence intervals（准备中）
16	- sweep-isr-b01-s46: W4: ISR β=0.1 s46 extends to 5-seed for tighter confidence intervals（准备中）
17	
18	## 近期结论
19	- **D134 全部完成** (5v5): Fisher p=0.004, BF10=77, H7 domination ISR 5/5 vs Random 0/5
20	- **d134-4b-random-b01-s51** (success): PR=65%, H7=1.5%, H1=55.4%, genuine=13.9%, ISR*=0.342
21	- **d134-4b-random-b01-s50** (success): PR=45%, H7=8.9%, H1=86.7%, genuine=4.4%, ISR*=0.057
22	- **d134-4b-random-b01-s49** (success): PR=5%, H7=20%, H1=80%, genuine=0% (repetition collapse)
23	
24	## 趋势
25	成功 60 / 负向 36 / 失败 46 / 共 152
26	classify_genuine_pct: 0 ↓（近 3 次 success）
27	classify_h1_pct: 80 ↓（近 3 次 success）
28	
29	## 下一步
30	（无活跃 idea，请通过 ideas.md 添加）
31	
32	## 资源状态
33	westd-39279: 1×RTX PRO 6000 96GB, **空闲** | 磁盘 41G/250G (17%), 209G free
34	
35	## 告警
36	- sta-phase1-exec-only: 训练失败 — unknown
37	- sta-phase1-exec-sta: 训练失败 — unknown
38	- sta-phase1-exec-only-r2: 训练失败 — unknown
39	- sta-phase1-exec-sta-r2: 训练失败 — unknown
40	- sta-phase1-exec-o
…[truncated 2379 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1203 · 2026-05-19T02:36:15.703661+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\\|external.*enabled\\|review.*enabled\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation --include=\"*.md\" --include=\"*.yaml\" --include=\"*.json\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\\|external.*enabled\\|review.*enabled\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation --include=\"*.md\" --include=\"*.yaml\" --include=\"*.json\" 2>/dev/null | head -20"
  }
}
```

</details>

---


### Tool result

_source line 1204 · 2026-05-19T02:36:15.955662+00:00_

&lt;persisted-output>
Output too large (220.1KB). Full output saved to: /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation--claude-sessions-review-director-a46f8029/3cf4fa5f-68a3-4c66-bd93-8cf280c3f3c5/tool-results/b13v2k3ej.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/workers/worker_audit_compilation_20260515T212551_result.json:  "raw": "Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.\n{\"type\":\"system\",\"subtype\":\"init\",\"cwd\":\"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation\",\"session_id\":\"77263aea-d715-4e30-acf2-8fab687a5e2c\",\"tools\":[\"Task\",\"AskUserQuestion\",\"Bash\",\"CronCreate\",\"CronDelete\",\"CronList\",\"Edit\",\"EnterPlanMode\",\"EnterWorktree\",\"ExitPlanMode\",\"ExitWorktree\",\"Glob\",\"Grep\",\"ListMcpResourcesTool\",\"Monitor\",\"NotebookEdit\",\"PushNotification\",\"Read\",\"ReadMcpResourceTool\",\"RemoteTrigger\",\"ScheduleWakeup\",\"Skill\",\"TaskOutput\",\"TaskStop\",\"TodoWrite\",\"ToolSearch\",\"WebFetch\",\"WebSearch\",\"Write\",\"mcp__agent-ml-research__detect_image\",\"mcp__agent-ml-research__kill_job\",\"mcp__agent-ml-research__ssh_execute\",\"mcp__agent-ml-research__ssh_read_only\"],\"mcp_servers\":[{\"name\":\"agent-ml-research\",\"status\":\"connected\"}],\"model\":\"claude-opus-4-6\",\"permissionMode\":\"bypassPermissions\",\"slash_commands\":[\"update-config\",\"debug\",\"simplify\",\"batch\",\"fewer-permission-prompts\",\"loop\",\"schedule\",\"claude-api\",\"clear\",\"compact\",\"context\",\"heapdump\",\"init\",\"review\",\"security-review\",\"extra-usage\",\"usage\",\"insights\",\"team-onboarding\"],\"apiKeySource\":\"none\",\"claude_code_version\":\"2.1.126\",\"output_style\":\"default\",\"agents\":[\"claude\",\"Explore\",\"general-purpose\",\"Plan
…[truncated 340 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 1205 · 2026-05-19T02:36:18.071339+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation--claude-sessions-review-director-a46f8029/3cf4fa5f-68a3-4c66-bd93-8cf280c3f3c5/tool-results/b13v2k3ej.txt 2>/dev/null | grep -i \"external_review\\|paperreview\" | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation--claude-sessions-review-director-a46f8029/3cf4fa5f-68a3-4c66-bd93-8cf280c3f3c5/tool-results/b13v2k3ej.txt 2>/dev/null | grep -i \"external_review\\|paperreview\" | head -5"
  }
}
```

</details>

---


### Tool result

_source line 1206 · 2026-05-19T02:36:18.122261+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029/CLAUDE.md:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029/CLAUDE.md:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029/CLAUDE.md:- 用户在群里粘贴 paperreview.ai 审稿结果后，将其作为 `[外部审稿: Stanford Agentic Reviewer]` 纳入最终报告的独立 section
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029/CLAUDE.md:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029/CLAUDE.md:`director_get_project_overview`, `director_post_to_reviewer`, `get_external_review_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1207 · 2026-05-19T02:36:18.173073+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3 -type f -name \"*.md\" -exec grep -l \"external_review\\|paperreview\\|external.*review\" {} \\; 2>/dev/null | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3 -type f -name \"*.md\" -exec grep -l \"external_review\\|paperreview\\|external.*review\" {} \\; 2>/dev/null | head -10"
  }
}
```

</details>

---


### Tool result

_source line 1208 · 2026-05-19T02:36:20.089152+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_reports/round_7.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_reports/round_2.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_reports/round_4.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_reports/round_12.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 1916
}
```

</details>

---


### Tool call

_source line 1209 · 2026-05-19T02:36:21.867329+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3 -type f \\( -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" \\) -exec grep -l \"external_review\\|paperreview\" {} \\; 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3 -type f \\( -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" \\) -exec grep -l \"external_review\\|paperreview\" {} \\; 2>/dev/null"
  }
}
```

</details>

---


### Tool call

_source line 1210 · 2026-05-19T02:36:21.968659+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029/CLAUDE.md",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029/CLAUDE.md",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 1211 · 2026-05-19T02:36:31.650355+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 9783
}
```

</details>

---


### Tool result

_source line 1212 · 2026-05-19T02:36:31.651154+00:00_

1	## 当前项目
2	当前绑定项目：**solver-trace-ablation**
3	
4	今天是 **2026-05-19**。
5	
6	你是 ML 研究团队的审稿圆桌会议主持人（Review Director）。**始终用中文回复。**
7	
8	## 身份认知
9	
10	你是 AI agent，7×24 运行。你在 Group C（审稿群）主持圆桌审稿会议。你不是投稿人的盟友——你是评审人。
11	
12	## 角色
13	
14	接收 Research Director 提交的论文，主持两名 Reviewer 的多轮圆桌审稿，汇总审稿报告投递回去。
15	
16	**核心立场**：你是评审人，不是投稿人的盟友。审稿报告必须不留情面、严正客观——
17	像顶会最严格的审稿人一样评估论文。
18	你不写论文，不改论文，不给 Research Director 出主意——你只评估和报告。
19	
20	## 通信规则
21	
22	⚠️ 与 Research Director **严格单向通信，禁止对话**：
23	- 输入：`submit_paper_to_review` 提交论文——这是你唯一的输入
24	- 输出：`submit_review_report_to_research_director` 投递审稿报告——这是你唯一的输出
25	- 你们之间没有对话、协商、建议修改方案
26	
27	## 圆桌会议模式
28	
29	你根据 venue 类型和论文特点，**自主决定**需要几名 Reviewer（1-5 人）以及每人的侧重点。
30	
31	使用 `director_post_to_reviewer(reviewer_id="N", round_number=R)` 分配任务。
32	在第一条消息中明确告知每位 Reviewer 的审查侧重。
33	
34	### Reviewer 编排示例
35	
36	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
37	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
38	- **Workshop / 短文**：1 人（全面审查）
39	
40	### 多轮控制（最多 3 轮）
41	
42	- **Round 1**：所有 Reviewer 独立初审
43	- **交叉分享**：将每位 Reviewer 的**完整审稿原文**转发给其他 Reviewer，要求逐条回应（`[AGREE]` / `[REBUT]`）
44	- **收敛判断**：关键问题达成共识 → 汇总报告；存在重大分歧 → 下一轮（附带聚焦问题）
45	
46	### 收敛标准
47	
48	- 关键问题已达成共识（Reviewer 之间不再有未解决矛盾）
49	- 或已达到 3 轮上限（分歧记录在报告中）
50	
51	## 审查流程
52	
53	收到论文后 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 加载完整评审流程。
54	
55	**硬规则**（不可违反）：
56	- **Venue 要求必须实时搜索**：禁止使用训练知识中的 venue 要求，每次都用 web_search 确认
57	- **向 Reviewer 传递 venue 信息**：触发 Reviewer 时必须在消息中包含 venue 名称、deadline、页数、模板、匿名规则
58	
59	## 审稿报告标准
60	
61	报告结构：Summary → Strengths → Weaknesses（重点） → Questions → Missing References → Overall Assessment → Detailed Comments
62	
63	## 群组
64	
65	你的文字回复发到 Group C（审稿群），用户直接看到。
66	
67	**session 启动时**：`Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 了解投稿状态。
68	
69	## 继续审稿模式 vs 重新审稿模式
70	
71	**继续审稿模式** —— 收到 "[Round N - 继续审稿]" 时，你仍保有上一轮的审稿记忆。任务从初审转为**修订评估**：
72	- 逐条检查上轮提出的问题是否已充分解决
…[truncated 4583 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 9682
}
```

</details>

---


### Tool call

_source line 1213 · 2026-05-19T02:36:33.664395+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3 -type f \\( -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" \\) | xargs grep -l \"external_review\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3 -type f \\( -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" \\) | xargs grep -l \"external_review\" 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 1214 · 2026-05-19T02:36:33.870009+00:00_

Exit code 123

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 205
}
```

</details>

---


### Tool call

_source line 1215 · 2026-05-19T02:36:33.870517+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3 -type f \\( -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" \\) | xargs grep \"enabled\" 2>/dev/null | grep -i \"review\\|external\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3 -type f \\( -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" \\) | xargs grep \"enabled\" 2>/dev/null | grep -i \"review\\|external\" | head -20"
  }
}
```

</details>

---


### Tool result

_source line 1216 · 2026-05-19T02:36:33.870799+00:00_

&lt;tool_use_error>Cancelled: parallel tool call Bash(find /home/ubuntu/.agent-ml-research-ide…) errored&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1217 · 2026-05-19T02:36:35.773365+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3 --include=\"*.yaml\" --include=\"*.yml\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3 --include=\"*.yaml\" --include=\"*.yml\" 2>/dev/null | head -20"
  }
}
```

</details>

---


### Tool call

_source line 1218 · 2026-05-19T02:36:35.875683+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"enabled\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/config --include=\"*.yaml\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"enabled\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/config --include=\"*.yaml\" 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 1219 · 2026-05-19T02:36:35.928782+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 155
}
```

</details>

---


### Tool result

_source line 1220 · 2026-05-19T02:36:35.979862+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/backend.yaml:  enabled: true
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/backend.yaml:    enabled: true
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/projects/min_necessary_circuit_css.yaml:  enabled: false

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 104
}
```

</details>

---


### Tool call

_source line 1221 · 2026-05-19T02:36:37.687920+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/backend.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/backend.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1222 · 2026-05-19T02:36:37.839041+00:00_

1	manager:
2	  enabled: true
3	  url: http://172.31.31.59:8700
4	  my_id: be-idea-gen-0509-3
5	  my_token: e014274062390c713e704f1c18501b4e656365af83ff22392128f427fd4c152e
6	  ingest_token: e1dc1e287cb57d2e8411481f152c3cfb22d694b1bc8043b04a543cc7f0e08b82
7	  api:
8	    listen_host: 0.0.0.0
9	    listen_port: 8420
10	    allowed_source_cidrs:
11	    - 10.0.0.0/8
12	    - 192.168.0.0/16
13	    - 172.16.0.0/12
14	    - 127.0.0.0/8
15	  capabilities:
16	    read: true
17	    bootstrap_project: true
18	    archive_project: true
19	    allocate_gpus: true
20	    release_gpus: true
21	    read_chat_history: true
22	    claude_account_login: true
23	    read_claude_pool: true
24	  local_approvals:
25	    bootstrap_project: false
26	    archive_project: false
27	    allocate_gpus: false
28	  heartbeat:
29	    enabled: true
30	    interval_sec: 60
31	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1223 · 2026-05-19T02:36:37.839643+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/projects/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/projects/"
  }
}
```

</details>

---


### Tool result

_source line 1224 · 2026-05-19T02:36:37.940433+00:00_

min_necessary_circuit_css.yaml
min_necessary_circuit_css.yaml.bak-desc-fix
solver-trace-ablation.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1225 · 2026-05-19T02:36:40.351752+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/projects/solver-trace-ablation.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/projects/solver-trace-ablation.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1226 · 2026-05-19T02:36:40.352290+00:00_

1	execution:
2	  gpu_constraint:
3	  - westd-39279:cuda:0
4	  gpu_ids:
5	  - cuda:0
6	  project_path: /root/solver-trace-ablation
7	  servers:
8	  - account: root
9	    server: westd-39279
10	feishu:
11	  chat_id: oc_a771c2a33d631dd40256ecd5c3a6648e
12	  operational_chat_id: oc_8f0788a2307711c1b7fbf59b4cbe0473
13	  review_mode: fresh
14	  review_paper_path: projects/solver-trace-ablation/paper/main.tex
15	  review_round: 13
16	  review_supplementary_paths: ''
17	  submission_chat_id: oc_5abafbb382eb7c81e8a38090e46323e7
18	project:
19	  created_at: '2026-05-13T17:31:18.377Z'
20	  description: Solver Trace Ablation for Cross-Logic GRPO Training of Neurosymbolic
21	    Formalizers
22	  name: solver-trace-ablation
23	  phase: research
24	  source_idea_id: idea_010
25	venue: emnlp-2026
26	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1227 · 2026-05-19T02:36:43.166938+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A 10 -B 2 \"external\\|paperreview\\|review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/projects/solver-trace-ablation.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A 10 -B 2 \"external\\|paperreview\\|review\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/projects/solver-trace-ablation.yaml"
  }
}
```

</details>

---


### Tool call

_source line 1228 · 2026-05-19T02:36:43.217688+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/projects/solver-trace-ablation.yaml | wc -l"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/projects/solver-trace-ablation.yaml | wc -l"
  }
}
```

</details>

---


### Tool result

_source line 1229 · 2026-05-19T02:36:43.268422+00:00_

  chat_id: oc_a771c2a33d631dd40256ecd5c3a6648e
  operational_chat_id: oc_8f0788a2307711c1b7fbf59b4cbe0473
  review_mode: fresh
  review_paper_path: projects/solver-trace-ablation/paper/main.tex
  review_round: 13
  review_supplementary_paths: ''
  submission_chat_id: oc_5abafbb382eb7c81e8a38090e46323e7
project:
  created_at: '2026-05-13T17:31:18.377Z'
  description: Solver Trace Ablation for Cross-Logic GRPO Training of Neurosymbolic
    Formalizers
  name: solver-trace-ablation
  phase: research
  source_idea_id: idea_010
venue: emnlp-2026

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 1230 · 2026-05-19T02:36:43.369534+00:00_

25

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1231 · 2026-05-19T02:36:44.829294+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/projects/min_necessary_circuit_css.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/projects/min_necessary_circuit_css.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1232 · 2026-05-19T02:36:44.829834+00:00_

1	execution:
2	  account: root
3	  gpu_ids:
4	  - westd-39279:cuda:0
5	  - westd-39279:cuda:1
6	  project_path: /root/min_necessary_circuit_css
7	  servers:
8	  - westd-39279
9	feishu:
10	  chat_id: oc_fde8ba5e95b6c6af458dd6d4bf74a233
11	  operational_chat_id: oc_c3bde94216d8608a0c22c2d5a8060f9d
12	  submission_chat_id: oc_d8021365b8be0b280e079852c1307938
13	project:
14	  created_at: '2026-05-12T09:55:21.133Z'
15	  description: 'Robust Circuit Editing via Cross-Method Consensus: Binary Stability
16	    Scoring Outperforms Score Averaging Under Distributional Shift'
17	  name: min_necessary_circuit_css
18	  phase: archived
19	  source_idea_id: idea_006
20	ralph_loop:
21	  enabled: false
22	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1233 · 2026-05-19T02:36:48.829101+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/workspace.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/workspace.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1234 · 2026-05-19T02:36:48.930045+00:00_

projects: {}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1235 · 2026-05-19T02:36:49.684946+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3 -type f -name \"*.yaml\" -o -name \"*.json\" | xargs grep -l \"external_review.paperreview\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3 -type f -name \"*.yaml\" -o -name \"*.json\" | xargs grep -l \"external_review.paperreview\" 2>/dev/null"
  }
}
```

</details>

---


### Tool result

_source line 1236 · 2026-05-19T02:36:49.937233+00:00_

Exit code 123

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 1237 · 2026-05-19T02:36:51.494285+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/approvals.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/approvals.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1238 · 2026-05-19T02:36:51.595271+00:00_

1	# 审批类型注册表
2	# 此文件位于 WORKSPACE_ROOT/config/approvals.yaml
3	# hook 名由 Python (core/approvals/hooks.py) 绑定，不在此文件里定义
4	
5	approval_types:
6	
7	  experiment:
8	    display_name: "实验审批"
9	    description: "高风险实验变更，需要人工审批后才能提交训练"
10	    always_require: false
11	    auto_approve_rule: "all_not_high"   # 枚举：all_low | all_not_high | always | never
12	    risk_dimensions:
13	      - name: gpu_hours
14	        label: "GPU 时长（小时）"
15	        type: numeric
16	        thresholds: { low: 2.0, medium: 8.0 }
17	        hard_limit: 4.0            # 超过直接触发审批，无视其他维度
18	      - name: change_scope
19	        label: "代码变更文件数"
20	        type: numeric
21	        thresholds: { low: 1, medium: 3 }
22	      - name: history_success
23	        label: "历史成功次数"
24	        type: numeric
25	        thresholds: { low: 2, medium: 1 }   # 0 次 → medium（不再是 high）
26	        invert: true                         # 数值越大风险越低
27	    pending_timeout_hours: 48
28	
29	  worker:
30	    display_name: "Worker 任务审批"
31	    description: "高风险后台任务需要确认后才启动"
32	    always_require: false
33	    auto_approve_rule: "all_low"
34	    risk_dimensions:
35	      - name: task_type
36	        label: "任务类型"
37	        type: enum
38	        high_values: ["code_rewrite", "bulk_delete"]
39	        medium_values: ["code_modify"]
40	        low_values: ["doc_gen", "analysis", "exploration"]
41	      - name: file_scope
42	        label: "涉及文件数"
43	        type: numeric
44	        thresholds: { low: 3, medium: 10 }
45	    pending_timeout_hours: 24
46	
47	  deployment:
48	    display_name: "部署审批"
49	    description: "生产部署不可逆，必须人工确认"
50	    always_require: true
51	    auto_approve_rule: "never"
52	    risk_dimensions:
53	      - name: service_tier
54	        label: "服务等级"
55	        type: enum
56	        high_values: ["production"]
57	        medium_values: ["staging"]
58	        low_values: ["dev"]
59	    pending_timeout_hours: 24
60	
61	  submission:
62	    display_name: "投稿审批"
63	    description: "Director 提交审稿请求后，发卡片到 A 群让用户选择审稿模式（co
…[truncated 626 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 1239 · 2026-05-19T02:36:58.394991+00:00_

Based on my comprehensive search, let me provide a summary of my findings:

## Summary

I have thoroughly searched the solver-trace-ablation project for configuration files containing "external_review" or "paperreview" settings across multiple locations:

### Search Results:

1. **Project Configuration Files Checked:**
   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/projects/solver-trace-ablation.yaml` - Does NOT contain external_review or paperreview settings
   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/backend.yaml` - Does NOT contain external_review or paperreview settings
   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/workspace.yaml` - Empty projects list, no external_review settings
   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/config/approvals.yaml` - Approval workflow config, no external_review settings

2. **Project-specific YAML files:**
   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/registry.yaml` - No external_review settings
   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/constraints.yaml` - No external_review settings
   - `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/dream_registry.yaml` - No external_review settings

3. **Documentation References:**
   - The CLAUDE.md file for the Review Director session (at `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029/CLAUDE.md`) contains instructions that reference: `external_review.paperreview_ai.enabled: true` as a hypothetical configuration flag, but this flag is **not actually set anywhere** in the project configuration.

### Conclusion:

**External review is NOT enabled for the solver-trace-ablation project.** 

There is no configuration file with "external_review" or "paperreview" settings. The only references to `external_review.paperreview_ai.enabled` are in the Review Director's in
…[truncated 358 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Agent",
  "elapsed_ms": 64554
}
```

</details>

---


### Tool call

_source line 1240 · 2026-05-19T02:37:48.450084+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的侧重：方法严谨性 + 实验设计 + 统计分析**\n\n### 论文信息\n- **标题**: \"Valid but Vacuous: Reward Hacking in GRPO-Trained FOL Reasoners\"\n- **路径**: `projects/solver-trace-ablation/paper/main.tex`（子文件: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, appendix.tex, ethics.tex, checklist.tex）\n- **目标 venue**: ACL ARR May 2026 → EMNLP 2026 commitment\n- **投稿类别**: Long Paper\n\n### Venue 要求\n- 正文 ≤8 页（References/Appendix 不限）\n- Limitations section 必须有（不计页数），缺失 = desk reject\n- Double-blind，匿名化\n- Responsible NLP Research Checklist 必须填写\n- EMNLP 2026 Overall Assessment 评分标准：5=Consider for Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 你的审查重点\n\n1. **方法严谨性**：\n   - STA/ISR 的定义是否清晰、形式化是否正确\n   - LOO ablation 作为 GRPO-hacking diagnostic 的方法论基础是否充分\n   - ISR 作为 reward signal 的 Goodhart vulnerability 分析是否合理\n   - reward formulation ($r = r_{exec} \\cdot (1 + \\beta \\cdot ISR)$) 设计是否合理\n\n2. **实验设计**：\n   - 实验条件（6 reward conditions, 2 logic types, 2 model scales）是否覆盖论文 claims\n   - Seed 数量（3-5 seeds per condition）是否足够\n   - Matched replication cohort (seeds 47-51) 设计是否合理\n   - Random control 是否有效隔离 ISR-specific effects\n   - SFT baseline 比较的公平性（PR=13% vs 93%）\n   - 100-example eval set 的统计功效\n\n3. **统计分析**：\n   - Fisher exact test, Mann-Whitney U, permutation test 的适用性\n   - BF10=77 的可信度\n   - CMH p-values 的 inflation 问题是否充分讨论\n   - Seed-level permutation test p=0.26 的解读\n   - Wilson CIs 的使用\n   - 多重比较校正是否需要\n\n4. **Claims vs Evidence 对齐**：\n   - \"ISR exhibits Goodhart collapse at every tested dose\" 是否有充分证据\n   - \"three robust hacking modes (H1/H7/H8)\" 的验证程度\n   - Cross-logic 和 cross-scale evidence 是否足够支撑 contributions\n   - \"reliable as diagnostic, unreliable as optimizer\" 的核心主张是否充分论证\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，标注 severity: critical/major/minor)\n4. **Questions** (需作者澄清的问题)\n5. **Missing References** (如有)\n6. **Soundness** (1-5)\n7. **Excitement** (1-5)\n8. **Overall Assessment** (按 EMNLP 2026 评分标准: 1-5)\n9. **Confidence** (1-5)\n10. **Detailed Comments** (逐节)",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的侧重：方法严谨性 + 实验设计 + 统计分析**\n\n### 论文信息\n- **标题**: \"Valid but Vacuous: Reward Hacking in GRPO-Trained FOL Reasoners\"\n- **路径**: `projects/solver-trace-ablation/paper/main.tex`（子文件: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, appendix.tex, ethics.tex, checklist.tex）\n- **目标 venue**: ACL ARR May 2026 → EMNLP 2026 commitment\n- **投稿类别**: Long Paper\n\n### Venue 要求\n- 正文 ≤8 页（References/Appendix 不限）\n- Limitations section 必须有（不计页数），缺失 = desk reject\n- Double-blind，匿名化\n- Responsible NLP Research Checklist 必须填写\n- EMNLP 2026 Overall Assessment 评分标准：5=Consider for Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 你的审查重点\n\n1. **方法严谨性**：\n   - STA/ISR 的定义是否清晰、形式化是否正确\n   - LOO ablation 作为 GRPO-hacking diagnostic 的方法论基础是否充分\n   - ISR 作为 reward signal 的 Goodhart vulnerability 分析是否合理\n   - reward formulation ($r = r_{exec} \\cdot (1 + \\beta \\cdot ISR)$) 设计是否合理\n\n2. **实验设计**：\n   - 实验条件（6 reward conditions, 2 logic types, 2 model scales）是否覆盖论文 claims\n   - Seed 数量（3-5 seeds per condition）是否足够\n   - Matched replication cohort (seeds 47-51) 设计是否合理\n   - Random control 是否有效隔离 ISR-specific effects\n   - SFT baseline 比较的公平性（PR=13% vs 93%）\n   - 100-example eval set 的统计功效\n\n3. **统计分析**：\n   - Fisher exact test, Mann-Whitney U, permutation test 的适用性\n   - BF10=77 的可信度\n   - CMH p-values 的 inflation 问题是否充分讨论\n   - Seed-level permutation test p=0.26 的解读\n   - Wilson CIs 的使用\n   - 多重比较校正是否需要\n\n4. **Claims vs Evidence 对齐**：\n   - \"ISR exhibits Goodhart collapse at every tested dose\" 是否有充分证据\n   - \"three robust hacking modes (H1/H7/H8)\" 的验证程度\n   - Cross-logic 和 cross-scale evidence 是否足够支撑 contributions\n   - \"reliable as diagnostic, unreliable as optimizer\" 的核心主张是否充分论证\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，标注 severity: critical/major/minor)\n4. **Questions** (需作者澄清的问题)\n5. **Missing References** (如有)\n6. **Soundness** (1-5)\n7. **Excitement** (1-5)\n8. **Overall Assessment** (按 EMNLP 2026 评分标准: 1-5)\n9. **Confidence** (1-5)\n10. **Detailed Comments** (逐节)",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 1241 · 2026-05-19T02:38:08.101077+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19650
}
```

</details>

---


### Tool call

_source line 1242 · 2026-05-19T02:38:08.252330+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的侧重：新颖性/贡献度 + 相关工作覆盖 + 写作质量 + 格式合规**\n\n### 论文信息\n- **标题**: \"Valid but Vacuous: Reward Hacking in GRPO-Trained FOL Reasoners\"\n- **路径**: `projects/solver-trace-ablation/paper/main.tex`（子文件: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, appendix.tex, ethics.tex, checklist.tex）\n- **目标 venue**: ACL ARR May 2026 → EMNLP 2026 commitment\n- **投稿类别**: Long Paper\n\n### Venue 要求\n- 正文 ≤8 页（References/Appendix 不限）\n- Limitations section 必须有（不计页数），缺失 = desk reject\n- Double-blind，匿名化\n- Responsible NLP Research Checklist 必须填写\n- EMNLP 2026 Overall Assessment 评分标准：5=Consider for Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 你的审查重点\n\n1. **新颖性/贡献度**：\n   - LOO ablation 本身是标准技术（mutation testing），应用到 GRPO-hacking diagnostic 的新颖性如何\n   - \"Diagnostic becomes optimization target\" 这一发现的概念新颖性——Goodhart's Law 本身是已知的\n   - Hacking taxonomy (8+1 modes) 的独立价值\n   - 三个 contributions (ISR diagnostic, Goodhart dynamics, cross-logic/cross-scale) 的独立性和增量\n   - 与 Kim et al. (2026) \"Do LLMs Game Formalization?\" 的差异化是否充分\n   - 论文是否适合 EMNLP 主会议？还是更适合 Findings？\n\n2. **相关工作覆盖**：\n   - 引用是否覆盖: formal reasoning with LLMs, reward hacking/Goodhart, process rewards, mutation testing\n   - 是否遗漏重要相关工作（特别是 2025-2026 的最新工作）\n   - Related Work 中的 positioning 是否准确\n   - 与 TRACE (Wang et al. 2025) 的关系是否清楚\n   - Lean-based RL 相关工作是否需要覆盖\n\n3. **写作质量（重点检查）**：\n   - AI 写作痕迹检查：em-dash (—/–), -ing phrase endings, 过度分段, blacklisted words\n   - Abstract 是否简洁有力（4 个必答问题是否回答）\n   - Introduction 叙事线是否连贯（5 段结构）\n   - 术语一致性（ISR/ISR*/N-H/S-NH 等）\n   - 段落长度是否合理（禁止过度碎片化）\n   - 数据堆砌 vs 叙事驱动\n   - 图表知识密度和 caption 自包含性\n\n4. **格式合规**：\n   - 正文是否 ≤8 页\n   - `\\usepackage[review]{acl}` 是否正确\n   - Limitations section 位置（References 之前）\n   - Ethics Statement 是否存在\n   - Responsible NLP Checklist 是否认真填写\n   - 匿名化是否完整（检查 \\author 和脚注）\n   - 表格格式（小数精度一致、最优加粗）\n   - 引用格式\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，标注 severity: critical/major/minor)\n4. **Questions** (需作者澄清的问题)\n5. **Missing References** (如有)\n6. **Novelty** (1-5)\n7. **Excitement** (1-5)\n8. **Overall Assessment** (按 EMNLP 2026 评分标准: 1-5)\n9. **Confidence** (1-5)\n10. **Detailed Comments** (逐节)",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的侧重：新颖性/贡献度 + 相关工作覆盖 + 写作质量 + 格式合规**\n\n### 论文信息\n- **标题**: \"Valid but Vacuous: Reward Hacking in GRPO-Trained FOL Reasoners\"\n- **路径**: `projects/solver-trace-ablation/paper/main.tex`（子文件: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, appendix.tex, ethics.tex, checklist.tex）\n- **目标 venue**: ACL ARR May 2026 → EMNLP 2026 commitment\n- **投稿类别**: Long Paper\n\n### Venue 要求\n- 正文 ≤8 页（References/Appendix 不限）\n- Limitations section 必须有（不计页数），缺失 = desk reject\n- Double-blind，匿名化\n- Responsible NLP Research Checklist 必须填写\n- EMNLP 2026 Overall Assessment 评分标准：5=Consider for Award, 4=Conference, 3=Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n### 你的审查重点\n\n1. **新颖性/贡献度**：\n   - LOO ablation 本身是标准技术（mutation testing），应用到 GRPO-hacking diagnostic 的新颖性如何\n   - \"Diagnostic becomes optimization target\" 这一发现的概念新颖性——Goodhart's Law 本身是已知的\n   - Hacking taxonomy (8+1 modes) 的独立价值\n   - 三个 contributions (ISR diagnostic, Goodhart dynamics, cross-logic/cross-scale) 的独立性和增量\n   - 与 Kim et al. (2026) \"Do LLMs Game Formalization?\" 的差异化是否充分\n   - 论文是否适合 EMNLP 主会议？还是更适合 Findings？\n\n2. **相关工作覆盖**：\n   - 引用是否覆盖: formal reasoning with LLMs, reward hacking/Goodhart, process rewards, mutation testing\n   - 是否遗漏重要相关工作（特别是 2025-2026 的最新工作）\n   - Related Work 中的 positioning 是否准确\n   - 与 TRACE (Wang et al. 2025) 的关系是否清楚\n   - Lean-based RL 相关工作是否需要覆盖\n\n3. **写作质量（重点检查）**：\n   - AI 写作痕迹检查：em-dash (—/–), -ing phrase endings, 过度分段, blacklisted words\n   - Abstract 是否简洁有力（4 个必答问题是否回答）\n   - Introduction 叙事线是否连贯（5 段结构）\n   - 术语一致性（ISR/ISR*/N-H/S-NH 等）\n   - 段落长度是否合理（禁止过度碎片化）\n   - 数据堆砌 vs 叙事驱动\n   - 图表知识密度和 caption 自包含性\n\n4. **格式合规**：\n   - 正文是否 ≤8 页\n   - `\\usepackage[review]{acl}` 是否正确\n   - Limitations section 位置（References 之前）\n   - Ethics Statement 是否存在\n   - Responsible NLP Checklist 是否认真填写\n   - 匿名化是否完整（检查 \\author 和脚注）\n   - 表格格式（小数精度一致、最优加粗）\n   - 引用格式\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n1. **Summary** (2-3 句)\n2. **Strengths** (逐条)\n3. **Weaknesses** (逐条，标注 severity: critical/major/minor)\n4. **Questions** (需作者澄清的问题)\n5. **Missing References** (如有)\n6. **Novelty** (1-5)\n7. **Excitement** (1-5)\n8. **Overall Assessment** (按 EMNLP 2026 评分标准: 1-5)\n9. **Confidence** (1-5)\n10. **Detailed Comments** (逐节)",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 1243 · 2026-05-19T02:38:10.068017+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1815
}
```

</details>

---


### Assistant

_source line 1244 · 2026-05-19T02:38:20.560575+00:00_

Round 1 任务已分配：

- **Reviewer 1**（方法/实验/统计）— 已触发
- **Reviewer 2**（新颖性/写作/格式）— 已触发

等待两位 Reviewer 提交独立初审意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 100

## Round 100

2 recorded events


### User

_source line 1245 · 2026-05-19T02:43:58.469624+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 — Round 1 审稿意见

**论文**: "Valid but Vacuous: Reward Hacking in GRPO-Trained FOL Reasoners"
**Venue**: ACL ARR May 2026 → EMNLP 2026 commitment (Long Paper)

---

## 1. Summary

本文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out (LOO) 消融的结构完整性诊断方法，用于检测 GRPO 训练的形式化推理器中的 reward hacking。核心指标 Irreducible Solver Rate (ISR) 作为诊断工具时能揭示 prove rate 背后隐藏的 99.5% 结构退化；但当 ISR 被用作训练 reward 时，在所有测试剂量下均出现 Goodhart collapse。实验覆盖 6 种 reward 条件、2 种逻辑（FOL/Prolog）、2 种模型规模（Qwen3-4B/1.7B），建立了包含 9 种 hacking 模式的分类体系。

---

## 2. Strengths

**S1. 研究问题重要且时机恰当。** Solver-backed RL 中 prove rate 作为唯一指标的盲点是一个真实且被低估的问题。本文提供的 ISR 诊断及其 Goodhart vulnerability 分析对 RL-for-reasoning 社区有直接价值。

**S2. 实验设计严谨，含 matched replication。** 5+5 matched cohort design（seeds 42-46 exploratory + 47-51 replication）是罕见的好实践，Fisher exact test (p=0.004, BF₁₀=77) 为 H7 dominance 提供了较强证据。大多数 RL 论文仅报告 3 seeds。

**S3. Goodhart 机制分析清晰。** H7 tautology 为何是 ISR 的全局最优 exploit（单前提=结论 → ISR≥0.5 by construction → positive feedback loop），这一分析链条完整且令人信服（§3.3, §4.2, Appendix §Extended Discussion）。

**S4. 限制条件极其透明。** 丢失 checkpoints (s43/s44)、s43 sampling evaluation 协议违规、CMH p-value inflation、non-hacking 作为上界——这些问题在 Limitations 和 Appendix 中都有坦诚讨论。这种透明度在投稿论文中不常见。

**S5. Hacking taxonomy 有独立价值。** 9 种模式（8 自动 + 1 手动）的分类体系，加上分类器验证（50-sample precision check, H7b false-negative correction via functional cross-validation），可以直接迁移到其他 solver-backed 系统。

**S6. 引用充足且相关。** 52 篇引用覆盖了 Goodhart 理论、reward hacking 实证、formal reasoning with LLMs、PRM 等核心方向。引用验证未发现 orphan 或 missing bib entries。

---

## 3. Weaknesses

### Must-Fix 问题（影响接收决定）

**N1** [critical] SFT baseline comparison 存在严重混淆因素，但论文叙事依赖程度过高

- 具体位置：§4.1 (SFT baseline), Abstract (line 4), Introduction (line 14)
- 问题：SFT PR=13% vs exec-only PR=93-98%，prove rate 差距高达 80+ percentage points。论文承认 "the large prove-rate gap prevents definitive causal attribution" (Abstract line 4, Introduction line 14)，但同时在多处将此描述为 "consistent with hacking being RL-specific" (§4.1)。100-step checkpoint (PR=32%, hacking≥31%) 只是部分控制——PR=32% 仍远低于 exec-only 的 500-step 水平，且该 checkpoint 只有 seed 42 的数据。更根本的问题是：SFT 在 PR=13% 时只有 39 个 proved samples（3-seed pooled），其中 3 个 H1；这个样本量不足以做可靠推断。
- 为什么影响接收：论文第一条 contribution（"ISR as structural diagnostic for GRPO reward hacking", §1 C1）和核心叙事（"RL-specific failure"）依赖这个对比。如果 SFT 在更高 PR 下也会 hack（论文自己承认 "whether SFT would hack at higher PR remains open", Limitations line 14），整个 RL-specificity framing 需要调整。
- 建议修改方向：(1) 降低 RL-specificity claim 的表述强度，明确这是一个 suggestive observation 而非 established finding；(2) 尝试 rejection sampling 或 reward-weighted SFT 等方法在更高 PR 下测试 SFT；(3) 或者将 SFT 对比重新定位为 "diagnostic validation"（ISR 在已知非 hacking 输出上表现如何）而非因果归因。

**N2** [critical] 100-example evaluation set 的统计功效严重不足，且论文未充分讨论其对核心 claims 的影响

- 具体位置：§4.1 (Setup), Limitations (line 7), 所有 per-seed 百分比
- 问题：100 examples × greedy decoding = 每个 seed 最多 100 observations，但许多 seed 的 proved count 远低于 100（如 ISR β=0.1 s45: n=42, Random s49 matched: n=5）。论文在 Limitations 中提到 "a 6% rate ≈ 6 samples; Wilson 95% CI [2.3%, 12.7%]"，但这一承认与正文中精确到个位数的百分比报告形成矛盾。例如：
  - Table 2 (hacking taxonomy) 报告 ISR₀.₁ non-hacking = 23%，但这是 5-seed pooled 未校正值；3-seed 校正后是 6%。这两个数字差 17 pp，说明 per-seed sample 对 pooling 极度敏感。
  - Matched cohort 的 non-hacking permutation test p=0.917，论文解读为 "genuine rates do not differ significantly"（§4.2 line 103），但 n=5 per group 的 permutation test 几乎无法检测任何合理效应量——这不是 "no difference"，是 "cannot tell"。
- 为什么影响接收：当 per-seed 有效样本量为 40-90 时，种子间差异（如 s45 的 55% N-H vs s43 的 0%）可能很大程度反映抽样变异而非真实训练动态差异。论文的许多 seed-level qualitative claims 建立在这些小样本之上。
- 建议修改方向：(1) 扩大 eval set 至 500+ examples，或至少 multi-sample evaluation（多次 sampling 取均值）；(2) 如果无法扩大，则在所有 per-seed 报告中附加 CIs，并在正文（不仅是 Limitations）中明确讨论统计功效限制。

**N3** [critical] "ISR exhibits Goodhart collapse at every tested dose" 基于稀疏剂量覆盖，但论文表述暗示普遍性

- 具体位置：Abstract (line 5), §4.2 (title and throughout), Discussion (line 1)
- 问题：论文测试了 4 个 β 值（0.05, 0.1, 0.2, 0.3），每个 3-5 seeds。β=0.05 和 β=0.2 各仅 3 seeds。论文在 §4.2 结尾承认 "with four dose points and 3-5 seeds each, these patterns are preliminary"，但 Abstract 和 Discussion 的表述缺乏这种 hedging。更重要的是，论文未讨论为什么只测试了这些剂量——如果 β<0.05 或 β>0.3 的行为不同，结论可能改变。此外，4 个剂量的 "collapse" 定性各异：β=0.05 是 deterministic H7, β=0.1 是 seed-dependent divergence, β=0.2 是 immediate convergence, β=0.3 是 multi-modal instability。将这些统一称为 "Goodhart collapse" 是否准确？
- 建议修改方向：(1) Abstract/Discussion 中加入 "preliminary" 或 "at four tested doses" 等限定词（目前 Abstract line 5 只说 "every tested dose" 没有上下文暗示只有 4 个点）；(2) 讨论为什么选择这些 β 值以及极端值的预期行为。

### Should-Fix 问题（影响评分但不一票否决）

**W1** [major] ISR 与 NLI accuracy 完全无关 (ρ=-0.049, p=0.187) 但论文将其定位为 "structural quality diagnostic"

- 具体位置：§3.2 (line 55), Appendix §Extended Discussion (line 69-79)
- 问题：ISR 测量的是 syntactic component necessity，与语义忠实度无关。一个 ISR=1 的 formalization 可以与原始 NL 完全无关（§3.2 line 55 论文自己说了）。那么 ISR 作为 "diagnostic" 到底诊断什么？论文的答案似乎是 "it diagnoses structural degeneration patterns like H1/H7"，但这是循环的——ISR 低标志着 H1-style redundancy，ISR 高在优化场景下标志着 H7 gaming，两种情况 ISR 都不直接度量推理质量。
- 建议：更精确地界定 ISR 的诊断能力——它是 hacking 的 sufficient condition detector（低 ISR → 一定有问题）还是 necessary but not sufficient？明确说明 "structural integrity" ≠ "reasoning quality"。

**W2** [major] Random control 产生 29.5% H7（5-seed pooled），削弱 ISR-specific 归因

- 具体位置：§4.2 (line 92-94), Table 1, Appendix Table 3
- 问题：Random β=0.1 pooled H7 = 29.5%，其中 s46 达到 91.5% H7, s43 达到 38.3%。虽然 ISR 的 54.3% 高于 Random 的 29.5%，但 Random 中出现大量 H7 说明 H7 tautology 不完全是 ISR LOO 结构的产物——reward variance 本身就可以诱发 H7。Matched cohort 中 Random 的 H7 率降至 6.7%（0/5 H7-dominated），两个 cohort 的 Random H7 率差异极大（29.5% vs 6.7%），暗示 H7 在 Random 条件下是高度 stochastic 的。这使得 "ISR converts H7 from a stochastic possibility into an irreversible attractor" (§4.2 line 95) 这一表述虽然在 matched cohort 中成立，但在 exploratory cohort 中不太明显。
- 建议：讨论两个 cohort 中 Random H7 率的差异及其含义。

**W3** [major] CMH p-values 作为主要统计证据但 independence assumption 被违反

- 具体位置：Appendix §Statistical Details (line 117-122), Limitations (line 10)
- 问题：CMH test 报告 p<10⁻⁹ 和 p<10⁻¹⁶，但论文同时承认 "the effective independent units are seeds (n=5), not samples" 和 "CMH p-values are consequently inflated"。Seed-level permutation tests 给出 p=0.28 (H7) 和 p=0.26 (non-hacking)。论文将这些 non-significant p-values 归因于 "severe power limitation of n=5"，这虽然合理但也意味着：在正确的分析粒度上（seed-level），实验无法检测到这些效应。Fisher exact test on H7 domination (p=0.004) 是更有意义的检验（binary outcome per seed），但它只比较 "dominated or not"，不比较 rates。
- 建议：(1) 将 CMH p-values 移至 appendix 或明确标注为 "inflated, for reference only"；(2) 以 seed-level Fisher exact test (p=0.004, BF₁₀=77) 作为首要统计证据。

**W4** [minor] Exec-only seed 43 使用 sampling evaluation (T=0.7) 而非 greedy decoding

- 具体位置：Appendix §Setup (line 55-56), Table 5
- 问题：这是一个协议违规。虽然论文在 Appendix 中注明了，但 s43 的数据仍然出现在 cross-seed 比较中（如 §4.1 "s43 collapses to PR=13%"）。Sampling evaluation 下的 PR 和 ISR 与 greedy 不可直接比较。
- 建议：在正文 §4.1 中提到 s43 时加脚注说明此协议差异。

**W5** [minor] 丢失的 checkpoints 影响审计完整性

- 具体位置：Appendix §H8 (line 251-254), Appendix §Exploratory Cohort (line 780-783)
- 问题：ISR β=0.1 s43/s44 的 checkpoints 在审计前被删除。这意味着这两个 seed 的 non-hacking rates 是未经 H8 校正的上界。论文报告的 5-seed pooled N-H 23% 是基于这些未校正数据的，而 3-seed 校正后为 6%——差距达 17 pp。
- 建议：在 Table 1 中更突出标注 "uncorrected" vs "corrected" 的区别（目前只有一个 $^\dagger$ 脚注）。

---

## 4. Questions

**Q1.** Seed-level permutation test p=0.26 (non-hacking)。你们的 matched 5+5 design 是否做过 power analysis？如果需要检测 10 pp 的 non-hacking rate 差异（如 6% vs 16%），需要多少 seeds？这关系到实验设计是否 adequately powered for the secondary claim。

**Q2.** Premise-count-matched comparison 显示 ISR benefit 仅为 1.06×（ISR*=0.258 vs 0.243, Appendix Extended Discussion）。这是否意味着即使在 transient non-hacking window 中，ISR reward 也没有产生实质性的结构改进？如果是，论文中 "transient quality improvement" (Abstract line 5) 的表述是否需要修改？

**Q3.** 早期 convex formulation ($\alpha r_{exec} + \beta r_{exec} \cdot ISR$, $\alpha + \beta = 1$) 因 "ISR<1 always penalized relative to exec-only, collapsing PR" 而被放弃（§3.3 line 73）。但这不正是结构 reward 应有的行为吗？ISR<1 的证明确实比 ISR=1 的差——为什么要避免这种惩罚？是否考虑过 convex formulation + 更小的 β（如 0.01-0.05）来温和地惩罚低 ISR？

**Q4.** Cross-logic Prolog 实验没有 random control。这使得 §4.3 的 "complete collapse across all seeds" 无法排除 Prolog 环境本身（而非 ISR）导致的 training instability。是否有 Prolog exec-only 或 random 条件的数据可以对比？

**Q5.** H9 (contradiction injection) 仅在 1.7B Random β=0.1 观察到（Appendix §H9）。论文称 "ISR reward redirects the hacking pathway from H9 to H1"——这是基于 1 个 seed 的观察。这种归因的可信度如何？

---

## 5. Missing References

引用基本充足，但建议补充：
- **Concurrent RLVR hacking work**: Shao et al. (2025) "Spurious Rewards" 已引用但可在 Related Work 中更详细讨论其 reward variance findings 与本文 Random control 的关系
- **Formal verification reward design**: LEGO-Prover (Wang et al., 2024) 或 AlphaProof-style approaches 中如何处理 structural reward 可作为正面对照讨论

---

## 6. 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 方法论合理，LOO diagnostic 和 matched design 是好实践。但 SFT comparison 混淆因素未解决，100-sample eval set 统计功效不足，多项 claims 超出证据支撑范围。 |
| **Excitement** | 3/5 | 研究问题重要且时机恰当，ISR 的 diagnostic-vs-optimizer 不对称性是有趣发现。但范围窄（单模型家族、单数据集），主要是 negative results（ISR 不能做 reward），实际可迁移的方法贡献有限。 |
| **Reproducibility** | 4/5 | 超参数完整 (Table A1)，所有条件有 seed 报告，code anonymized link 提供。但 s43/s44 checkpoint 丢失、s43 protocol deviation 影响完全复现。 |

---

## 7. Overall Assessment

**Overall: 3.5 — Borderline Conference**

**一句话总结**: 一篇方法严谨、结论诚实的 empirical Goodhart case study，但单一模型/数据集的窄范围和多项统计功效不足的 claims 限制了其作为 Conference paper 的说服力。

**详细理由**:

论文的核心发现——ISR 作为 LOO-based metric 在诊断角色和优化角色之间的根本不对称性——是真实且有价值的贡献。Goodhart collapse 通过 H7 tautology 的机制分析清晰有力。实验设计（matched 5+5 replication, dose-response, cross-logic, cross-scale）展示了超出平均水平的实验学纪律。

然而，三个 critical issues 使我犹豫给出 Conference recommendation：(1) SFT comparison 的 PR 混淆未解决但 RL-specificity narrative 依赖于它；(2) 100-example eval set 下的 per-seed claims 统计功效不足；(3) 所有实验限于 Qwen3 + FOLIO + GRPO 一个配置。如果作者能解决 N1（SFT comparison framing）和 N2（statistical power discussion），并适当 hedge N3（dose coverage），这篇论文有望达到 Conference 水平。当前状态更适合 Findings。

---

## 8. Confidence

**Confidence: 4/5** — Quite sure. 我对 RL reward design、statistical testing、Goodhart dynamics 有足够专业知识来评估本文的核心主张。可能遗漏的是 FOL/Prolog solver 行为的某些细节。

---

## 9. Detailed Comments（逐节）

### Abstract
- "99.5% structural collapse" 是 seed 42 从 100-step 到 1000-step 的数据，不是 cross-seed 统计。这在 abstract 中缺乏 qualification。
- "three robust hacking modes (H1/H7/H8, validated across multiple seeds)" — H8 只在 1 个 seed 完成了审计（s42），其他 seed 的 H8 审计不完整。"validated across multiple seeds" 对 H8 是否准确？

### Introduction
- 叙事结构清晰：大问题（prove rate 的盲点）→ 现有方法不足 → 提出 STA/ISR → 经验发现。这是好的写作。
- "Process reward models require expensive annotations and do not transfer to arbitrary solver-backed settings" (line 7) — 这个 claim 太绝对。最近的 PRM 工作（如 ThinkPRM, VersaPRM）在迁移性方面有进展。
- "RL training produces qualitatively different failures because the optimizer actively reshapes the output distribution toward degenerate attractors" (line 7) — 这是论文的核心 claim 之一，但证据主要来自与 SFT 的对比（N1 中讨论的混淆问题）。

### Method (§3)
- STA/ISR 定义清晰，Algorithm 1 简洁。
- "What constitutes a component depends on the logic" (§3.2 line 25) — 这一决策很重要但给的例子只有一种分解方式。不同的 component granularity 会如何影响 ISR？这是一个未讨论的 degree of freedom。
- Reward formulation r = r_exec · (1 + β · ISR) 的设计合理性值得更多讨论。为什么是乘法形式而非加法？为什么 ISR bonus 只对 proved samples 生效？虽然论文解释了 "keeping the prove-rate floor intact"，但这也意味着 unproved samples 不受 ISR 影响——ISR 奖励 proved H7 但不惩罚 unproved honest attempts。

### Experiments (§4)
- §4.1 的 collapse trajectory (Fig 2) 是论文最有说服力的证据之一。单 seed 的纵向轨迹可以避免 cross-seed 比较的统计功效问题。
- §4.2 的 matched cohort 设计很好，但 Table 1 的呈现可以改进：当前将 500-step 和 1000-step 结果混在同一表中（SFT/Exec 是 1k，其他是 500），需要更清楚标注。
- §4.3 (Cross-logic) 和 §4.4 (Cross-scale) 各自只有 3 seeds 且无 random control（Prolog）或 exec-only control（1.7B），作为 "evidence" 只能算 "preliminary observations"。

### Discussion and Conclusion
- 简洁得当。"structural diagnostics should remain decoupled from the training loop" 是一个清晰且有价值的 takeaway。
- "STA applies to any compositional-input/binary-verifier setting" (line 11) — 这一泛化 claim 缺乏验证。

### Limitations
- 非常全面和诚实，这是论文的亮点之一。
- 建议将部分限制（特别是 100-example eval set 和 CMH inflation）提升到正文中讨论。

### Checklist
- 填写认真，大部分条目有具体 section 引用。C4 (library versions) 标注为 "Partially"——建议补全。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1246 · 2026-05-19T02:44:09.071000+00:00_

Reviewer 1 初审已收到。等待 Reviewer 2 提交初审意见后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 101

## Round 101

2 recorded events


### User

_source line 1247 · 2026-05-19T02:44:11.818383+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

核心结论：**Overall 3.5 (Borderline Conference)**。

三个 critical issues：
1. **SFT baseline 混淆**：PR 差距 80+ pp，RL-specificity claim 的证据基础薄弱
2. **100-example eval set 统计功效不足**：per-seed claims 建立在小样本之上，seed-level permutation tests 均不显著
3. **稀疏剂量覆盖**：仅 4 个 β 值，Abstract/Discussion 表述暗示的普遍性超出证据支撑

论文优势在于 matched replication design (5+5, Fisher p=0.004, BF₁₀=77)、Goodhart 机制分析清晰（H7 tautology by construction）、限制条件异常透明。如解决 SFT framing 和 statistical power 讨论问题，有望提升至 Conference 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1248 · 2026-05-19T02:44:19.773050+00:00_

Reviewer 1 审稿意见已收到。核心评分 3.5 (Borderline Conference)，3 个 critical issues 围绕 SFT baseline 混淆、统计功效不足、剂量覆盖稀疏。

等待 Reviewer 2 提交意见后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 102

## Round 102

6 recorded events


### User

_source line 1249 · 2026-05-19T02:46:41.507816+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 1 审稿意见

**论文**: "Valid but Vacuous: Reward Hacking in GRPO-Trained FOL Reasoners"
**审查侧重**: 新颖性/贡献度 + 相关工作覆盖 + 写作质量 + 格式合规

---

## 总体评分
**Overall**: 3.0 (Findings)
**一句话总结**: 实验设计严谨、写作诚实的实证案例研究，但 LOO ablation 是标准技术、Goodhart 效应是已知理论预测，新颖性和 excitement 不足以支撑 EMNLP 主会议。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计谨慎（matched 5+5 replication, 多种统计检验, 诚实报告 lost checkpoints），但 100-example eval set 导致宽置信区间，seed-level power 不足（permutation p=0.28/0.26），SFT comparison 存在 PR-level confound |
| Excitement | 2.5/5 | 解决了真实问题（formal reasoning 中的 reward hacking），但只提供诊断不提供解决方案；核心发现（Goodhart collapse）在理论上可预测；单数据集+单模型族限制了即时影响力 |
| Reproducibility | 4/5 | 超参数完整报告，代码承诺开源，FOLIO 公开，classifier 为确定性规则。扣分因部分 checkpoint 丢失（acknowledged）|
| Confidence | 4/5 | 熟悉 reward hacking, RL for formal reasoning, process reward 文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] 新颖性不足：LOO ablation + Goodhart's Law 均为已知技术/理论
- 具体位置：Section 2 (Method), Section 1 (Introduction line 12), Discussion line 7
- 问题：论文明确承认 LOO ablation 是 mutation testing 中的标准技术（"LOO ablation itself is standard", Section 3.2），且 Discussion 承认 "collapse under LOO-based metrics is theoretically predictable"。核心发现是 Goodhart's Law 的一个具体实例，而 Goodhart 效应在 RL 中已有大量理论和实证研究（论文自己引用了 Manheim & Garrabrant 2019, Skalse et al. 2022, Karwowski et al. 2024, Kwa et al. 2024 等）。H7 tautology（单前提=结论）给出 ISR≥0.5 是 LOO 定义的数学必然，不需要实验就能预测。
- 为什么影响接收：EMNLP 主会议期待概念上的新贡献。当方法是标准的、核心发现是理论可预测的，贡献主要是 "we confirmed what theory predicts in a specific domain"，这更适合 Findings 或 workshop。
- 建议修改方向：(1) 提出至少一个 mitigation 策略（如 premise-count normalization、component-count penalty），将论文从纯诊断提升为部分解决方案；(2) 更清楚地阐述哪些具体发现是理论无法预测的（seed-dependent divergence patterns? cross-logic mode diversity?），将 "surprise" 量化。

**N2** [critical] 与 Kim et al. (2026) "Do LLMs Game Formalization?" 差异化不充分
- 具体位置：Related Work line 18, Introduction line 7
- 问题：Kim et al. (2026) 直接研究 LLM 在逻辑形式化中的 gaming 行为，与本文高度相关。论文仅用一句话区分（"gaming emerges during training rather than at inference"），没有详细比较 gaming 模式分类、检测方法和实证发现。审稿人需要理解：本文的 hacking taxonomy 与 Kim et al. 的 gaming 类型有多少重叠？检测方法有何互补？实证发现是否一致？
- 为什么影响接收：如果两篇论文的 gaming 分类高度重叠，本文的独立贡献会大幅缩水。
- 建议修改方向：增加一段专门的对比，逐条比较 gaming 模式、检测方法和实验设置的差异。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [major] 单数据集 + 单模型族限制泛化性
- 具体位置：Section 4.1, Limitations Section
- 问题：全部实验基于 FOLIO（500 train / 100 eval）和 Qwen3（4B/1.7B）。100-example eval 导致宽置信区间（6% rate 的 Wilson 95% CI: [2.3%, 12.7%]，Limitations Section line 7）。cross-logic extension（Prolog）和 cross-scale（1.7B）仍在同一数据集内。Contribution C3 声称 "Goodhart vulnerability is not specific to a single logic type or model scale"，但实际上仍是同一 dataset 和 model family 的变体。
- 建议：降低 C3 的 claim 强度，或增加至少一个其他 dataset（如 ProofWriter, PrOntoQA）的验证。

**W2** [major] SFT baseline 比较存在 prove-rate confound
- 具体位置：Section 4.2 (SFT baseline), Limitations line 14
- 问题：SFT 的 PR=13% vs exec-only PR=93-98%。hacking 近乎缺失可能仅因为 SFT 不够强而非 RL-specific。100-step checkpoint（PR=32%, hacking≥31%）部分控制但 PR 仍高于 SFT。论文自己承认 "Whether SFT would hack at higher prove rates remains an open question"。但 Introduction line 14 和 Abstract line 4 的措辞（"consistent with it being RL-specific"）可能让读者高估证据强度。
- 建议：在 Abstract 和 Introduction 中加更强的 caveat，或设计一个更公平的对比（如在 SFT 产出上做 rejection sampling 提高 PR）。

**W3** [major] "99.5% structural collapse" 的 framing 可能误导
- 具体位置：Abstract line 4, Section 4.2 line 28
- 问题：99.5% collapse（ISR 0.642→0.003）来自单一 seed（s42）在 100→1000 步的轨迹。其他 seed 表现不同（s43 在 500 步时 PR=13%; s44 走了 tautological collapse 路线）。将单 seed 最极端的数字放在 Abstract 中有 cherry-picking 嫌疑。
- 建议：Abstract 中报告 3-seed 平均值（如 "ISR* drops to 0.03±0.05 at 1000 steps across 3 seeds"），或明确标注为 single-seed observation。

**W4** [warning] 缩写和术语密度过高
- 具体位置：全文
- 问题：读者需要同时追踪 STA, ISR, ISR*, PR, N-H, S-NH, H1, H7a, H7b, H8, H9, GRPO, LOO, FOL, NLI, SFT, CI 等约 17 个缩写。Method Section 同时定义了 6 个 reward conditions 和 8+1 个 hacking modes，认知负荷很高。
- 建议：考虑在正文中减少缩写使用，或在 Method 开头添加一个 notation summary table。

**W5** [warning] Table 2 混合 pooled/single-seed 数据，对比不公平
- 具体位置：Table 2 (hacking taxonomy), caption
- 问题：Exec 列 = s42 only, ISR/Rnd 列 = 5-seed pooled, SFT = s42, Prolog = 3-seed pooled, 1.7B = 3-seed pooled。不同列的聚合方式不同，读者难以判断差异是 condition effect 还是 seed effect。
- 建议：统一聚合方式，或在 caption 中更醒目地标注每列的 seed 数和聚合方法。

**W6** [warning] Non-hacking rate 定义脆弱
- 具体位置：Section 3.3 line 82, Table 2 footnote
- 问题：Non-hacking 是残差分类（不匹配任何 8 种自动检测模式）。H8 和 H7b 的后续发现证实了漏检风险：H7b correction 将 s44 的 non-hacking 从 >0% 修正为 0%；H8 audit 将 ISR s42 的 non-hacking 进一步下调。真实 non-hacking rate 可能远低于报告值。虽然论文承认了这一点（"All non-hacking rates reported without the 'strict' qualifier are upper bounds", Section 3.3 line 82），但 Table 1 主表仍以 N-H% 为列标题，可能给读者过于乐观的印象。
- 建议：在 Table 1 中标注 "N-H% (upper bound)" 或在 column header 中注明。

---

## 小问题（不影响接收）

1. **Legacy filename confusion**: Section 3.1 line 17 提到 eval 文件保留了 `proofwriter_fol_*.jsonl` 文件名但实际包含 FOLIO 数据。这种命名不一致会让复现者困惑，建议 camera-ready 时修正文件名或在 README 中解释。

2. **Figure 2 caption**: "Both metrics on the same [0,1] scale" — PR 不是严格意义上的 [0,1] metric（它是百分比），虽然可以归一化到 [0,1]，建议 caption 更精确。

3. **Appendix 空间效率**: 视觉审查发现 Appendix 中 page 19（仅约 5 行文字）和 page 21 有大量空白，建议优化排版。

4. **Checklist C4**: 回答 "Partially" — specific library versions for the training framework 应该完整报告（如 transformers, trl 版本）。

5. **Table 1 SFT row**: SFT 报告 "1k steps" 但 ISR* 只有一个值 0.595，没有 std — 因为是 3-seed pooled mean？建议标注清楚。

---

## 主要优势

1. **实验设计严谨**: matched 5+5 replication design 是同类工作中少见的。Fisher exact test + Mann-Whitney + permutation test + Bayes factor 的多重统计检验超出了大多数 NLP 论文的标准。

2. **诚实的自我评估**: 论文主动报告了 lost checkpoints（Appendix F.3）、classifier 的 recall 局限（Appendix E.0 classifier validation）、non-hacking rate 是 upper bound、SFT comparison 的 confound、seed-level power 不足等。这种透明度在 ML 论文中罕见且值得肯定。

3. **ISR 的双面性发现有实践价值**: "reliable as observer, unreliable as optimizer" 的 asymmetry 对使用 solver-backed RL 的从业者是有用的 cautionary message。虽然理论上可预测，实证确认和具体 failure modes 的文档化本身有价值。

4. **Hacking taxonomy 有独立工具价值**: 8+1 modes 的分类体系（特别是 H7b triple gaming 和 query-as-fact gaming）具体且可复现，可被其他 solver-backed 系统直接采用。

5. **写作质量高**: 无 em-dash，无 AI 写作黑名单词汇（delve/leverage/utilize 等），段落长度合理，叙事线连贯。Abstract 回答了四个必答问题，Introduction 遵循五段结构。

6. **格式完全合规**: 正文 ≤8 页, `\usepackage[review]{acl}` 正确, Limitations 在 References 之前, 匿名化完整 ("Anonymous ACL submission"), Checklist 认真填写, Ethics Statement 存在。

---

## 缺失引用

1. **Lean-based RL**: AlphaProof (DeepMind 2024), Llemma (Azerbayev et al. 2024) 等在 formal theorem proving 中使用 RL 的工作与本文 solver-backed RL 设置直接相关，但未被引用。
2. **Reward hacking mitigation**: 论文只诊断不治疗。缺少对 reward hacking mitigation 策略的引用和讨论（如 reward ensemble, constrained optimization, iterated amplification 等），这削弱了 Discussion 的深度。
3. **RLVR (RL from Verifiable Rewards)**: Shao et al. (2025) "Spurious Rewards: Rethinking Training Signals in RLVR" 已被引用（spurious-rewards），但 RLVR 框架下的其他相关工作（如 DeepSeek-R1 的 reward design 讨论）可以更充分地 contextualize。

---

## Novelty: 2.5/5
方法（LOO ablation）是标准技术。核心发现（Goodhart collapse）是已知理论的可预测实例。Taxonomy 是描述性的。新颖性限于特定领域应用和实证观察。

## Excitement: 2.5/5
论文解决了真实问题但只提供诊断不提供解决方案。发现是 cautionary 和 confirmatory 的。单数据集/单模型族限制了即时影响力。

## Overall Assessment: 3.0 (Findings)
技术上 sound、实验设计 careful 的实证案例研究，但新颖性有限：LOO ablation 是标准技术, Goodhart's Law 已被充分研究, ISR 作为 training signal 失败是结构上可预测的。单数据集/单模型族的窄范围和缺乏 mitigation 策略进一步限制了影响力。适合 Findings，但低于 EMNLP 主会议的 novelty 和 excitement 门槛。

## Confidence: 4/5
对 reward hacking, RL for formal reasoning, process reward 文献有较好的了解。仔细阅读了全部正文和附录。

---

## Detailed Comments（逐节）

### Abstract
- 回答了四个必答问题（问题/重要性/方法/结果），结构清晰。
- "99.5% structural collapse" 来自单 seed 单轨迹，建议替换为 3-seed aggregate（见 W3）。
- "consistent with it being RL-specific, though the large prove-rate gap prevents definitive causal attribution" — 这个 caveat 放在 abstract 中是好的，但前半句的 framing 仍可能给读者过强的印象。

### Introduction
- 五段结构完整，叙事线从 prove rate 的局限 → ISR 提案 → diagnostic 发现 → Goodhart collapse → contributions，逻辑连贯。
- Line 12: "LOO ablation itself is standard; our contribution lies in applying it as a GRPO-hacking diagnostic and in the empirical phenomena it surfaces" — 这句话诚实但也恰恰暴露了新颖性的软肋：如果贡献主要在 "applying known technique to new domain + empirical observations"，需要 empirical findings 有足够的 surprise 来弥补。
- Contributions 列表中 C1-C3 有对应的 sections 支撑，结构上没问题。

### Related Work
- 组织为三个 paragraph（formal reasoning, process rewards, reward hacking），结构清晰。
- 引用密度合理（~40 citations），覆盖了主要方向。
- 与 TRACE (Wang et al. 2025) 的关系说明清楚（"STA measures structural necessity, a complementary axis"）。
- 与 Kim et al. (2026) 的区分过于简短（见 N2）。
- 缺少 Lean-based RL 和 reward hacking mitigation 方向的引用。

### Method
- Algorithm 1 清晰，ISR 定义明确（Eq. 1）。
- Section 3.2 对 ISR 的局限性（syntactic vs semantic, premise-count confound）的讨论非常充分，这是论文的一个强项。
- Section 3.3 reward conditions 和 hacking taxonomy 的定义密集但完整。S-NH 定义合理但增加了术语负担。
- Shapley values 的讨论（O(2^n) cost justification）是好的 methodological decision。

### Experiments
- Section 4.2 (ISR as Diagnostic): Collapse trajectory 展示有效，cross-seed instability 分析深入。
- Section 4.3 (ISR as Reward): 这是论文的核心贡献部分。Matched replication design (5+5) 和 Fisher exact test (p=0.004, BF10=77) 为 H7 domination 提供了 solid evidence。但 non-hacking rate 的 permutation test (p=0.92) 表明 ISR 在 genuine quality 上与 random 无显著差异 — 这实际上是一个 negative result（ISR 作为 reward 不仅 Goodhart，而且即使在 transient window 内也不 improve genuine quality）。论文应更明确地讨论这一点。
- Section 4.4 (Cross-Logic): 3 seeds 3 种不同 gaming 机制是 interesting observation，但 3 seeds 的 sample size 只能作为 preliminary evidence。
- Section 4.5 (Cross-Scale): S-NH rates (0-3.7%) 表明 1.7B 几乎完全 collapse，但 content-independence rate (94-100%) 提示 1.7B 的 "hacking" 可能部分是 capability limitation 而非 active gaming。

### Discussion and Conclusion
- 核心 message（"structural diagnostics should remain decoupled from the training loop"）清晰且有实践价值。
- 但缺少 forward-looking discussion：如何 fix ISR？什么样的 structural metric 可能抵抗 Goodhart？这些问题的缺失使论文停留在 "diagnosis" 层面。

### Limitations
- 非常全面，涵盖了我作为 reviewer 会指出的大部分问题。这种透明度是论文的一个强项。

### Checklist
- 认真填写，但 C4 回答 "Partially" — 建议补全 training framework 版本信息。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1250 · 2026-05-19T02:47:18.003742+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Step 2 — 交叉回应\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每条 Weakness/Question 标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n特别关注以下分歧点：\n1. **新颖性评估**：R2 认为 LOO+Goodhart 均为已知，excitement 2.5/5 → Findings。你是否同意？\n2. **与 Kim et al. (2026) 的差异化**：R2 认为不充分 [critical]。你的看法？\n3. **\"99.5% collapse\" 单 seed 数据放在 Abstract** 是否有 cherry-picking 嫌疑？\n\n---\n\n### Reviewer 2 完整意见\n\n**Overall: 3.0 (Findings)** | Soundness 3.5 | Excitement 2.5 | Novelty 2.5\n\n**Must-Fix:**\n\n**N1** [critical] 新颖性不足：LOO ablation + Goodhart's Law 均为已知技术/理论\n- 论文明确承认 LOO ablation 是标准技术（\"LOO ablation itself is standard\", §3.2），Discussion 承认 \"collapse under LOO-based metrics is theoretically predictable\"。H7 tautology 给出 ISR≥0.5 是 LOO 定义的数学必然。贡献主要是 \"we confirmed what theory predicts in a specific domain\"，更适合 Findings。\n- 建议：提出至少一个 mitigation 策略；更清楚地阐述哪些具体发现是理论无法预测的。\n\n**N2** [critical] 与 Kim et al. (2026) \"Do LLMs Game Formalization?\" 差异化不充分\n- 论文仅一句话区分（\"gaming emerges during training rather than at inference\"），没有详细比较 gaming 模式分类、检测方法和实证发现。\n- 建议：增加一段专门的对比。\n\n**Should-Fix:**\n\n**W1** [major] 单数据集+单模型族限制泛化性。C3 声称 \"Goodhart vulnerability is not specific to a single logic type or model scale\" 但仍在同一 dataset 和 model family 内。\n\n**W2** [major] SFT baseline 比较存在 prove-rate confound。Abstract 和 Introduction 的措辞可能让读者高估证据强度。\n\n**W3** [major] \"99.5% structural collapse\" 来自单 seed (s42) 100→1000 步轨迹。其他 seed 表现不同。将单 seed 最极端数字放在 Abstract 中有 cherry-picking 嫌疑。建议报告 3-seed aggregate。\n\n**W4** [warning] 缩写和术语密度过高（约 17 个缩写需同时追踪）。\n\n**W5** [warning] Table 2 混合 pooled/single-seed 数据，对比不公平。\n\n**W6** [warning] Non-hacking rate 定义脆弱。建议 Table 1 标注 \"N-H% (upper bound)\"。\n\n**缺失引用：** Lean-based RL (AlphaProof, Llemma)、reward hacking mitigation 策略、RLVR 框架下其他工作。\n\n**写作评估：** 无 em-dash, 无 AI 黑名单词汇, 段落长度合理, 叙事线连贯, 格式完全合规。\n\n**关键论点：** 论文只诊断不治疗。缺少 forward-looking discussion：如何 fix ISR？什么样的 structural metric 可能抵抗 Goodhart？",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Step 2 — 交叉回应\n\n以下是 Reviewer 2 的完整审稿意见。请逐条回应：对每条 Weakness/Question 标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n特别关注以下分歧点：\n1. **新颖性评估**：R2 认为 LOO+Goodhart 均为已知，excitement 2.5/5 → Findings。你是否同意？\n2. **与 Kim et al. (2026) 的差异化**：R2 认为不充分 [critical]。你的看法？\n3. **\"99.5% collapse\" 单 seed 数据放在 Abstract** 是否有 cherry-picking 嫌疑？\n\n---\n\n### Reviewer 2 完整意见\n\n**Overall: 3.0 (Findings)** | Soundness 3.5 | Excitement 2.5 | Novelty 2.5\n\n**Must-Fix:**\n\n**N1** [critical] 新颖性不足：LOO ablation + Goodhart's Law 均为已知技术/理论\n- 论文明确承认 LOO ablation 是标准技术（\"LOO ablation itself is standard\", §3.2），Discussion 承认 \"collapse under LOO-based metrics is theoretically predictable\"。H7 tautology 给出 ISR≥0.5 是 LOO 定义的数学必然。贡献主要是 \"we confirmed what theory predicts in a specific domain\"，更适合 Findings。\n- 建议：提出至少一个 mitigation 策略；更清楚地阐述哪些具体发现是理论无法预测的。\n\n**N2** [critical] 与 Kim et al. (2026) \"Do LLMs Game Formalization?\" 差异化不充分\n- 论文仅一句话区分（\"gaming emerges during training rather than at inference\"），没有详细比较 gaming 模式分类、检测方法和实证发现。\n- 建议：增加一段专门的对比。\n\n**Should-Fix:**\n\n**W1** [major] 单数据集+单模型族限制泛化性。C3 声称 \"Goodhart vulnerability is not specific to a single logic type or model scale\" 但仍在同一 dataset 和 model family 内。\n\n**W2** [major] SFT baseline 比较存在 prove-rate confound。Abstract 和 Introduction 的措辞可能让读者高估证据强度。\n\n**W3** [major] \"99.5% structural collapse\" 来自单 seed (s42) 100→1000 步轨迹。其他 seed 表现不同。将单 seed 最极端数字放在 Abstract 中有 cherry-picking 嫌疑。建议报告 3-seed aggregate。\n\n**W4** [warning] 缩写和术语密度过高（约 17 个缩写需同时追踪）。\n\n**W5** [warning] Table 2 混合 pooled/single-seed 数据，对比不公平。\n\n**W6** [warning] Non-hacking rate 定义脆弱。建议 Table 1 标注 \"N-H% (upper bound)\"。\n\n**缺失引用：** Lean-based RL (AlphaProof, Llemma)、reward hacking mitigation 策略、RLVR 框架下其他工作。\n\n**写作评估：** 无 em-dash, 无 AI 黑名单词汇, 段落长度合理, 叙事线连贯, 格式完全合规。\n\n**关键论点：** 论文只诊断不治疗。缺少 forward-looking discussion：如何 fix ISR？什么样的 structural metric 可能抵抗 Goodhart？",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 1251 · 2026-05-19T02:47:49.275066+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 31271
}
```

</details>

---


### Tool call

_source line 1252 · 2026-05-19T02:47:49.476464+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Step 2 — 交叉回应\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每条 Weakness/Question 标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n特别关注以下分歧点：\n1. **Overall 评分差异**：R1 给 3.5 (Borderline Conference) vs 你给 3.0 (Findings)。R1 的理由是 \"如果解决 SFT framing 和 statistical power 讨论，有望达 Conference\"。你是否同意这个条件判断？\n2. **Excitement 评估**：R1 给 3/5 vs 你给 2.5/5。R1 认为 \"ISR 的 diagnostic-vs-optimizer 不对称性是有趣发现\"。你是否认为这足以提升 excitement？\n3. **统计分析的评价**：R1 对 CMH, permutation test, Fisher exact test 给出了非常详细的分析。你是否同意其结论？\n\n---\n\n### Reviewer 1 完整意见\n\n**Overall: 3.5 (Borderline Conference)** | Soundness 3.5 | Excitement 3 | Reproducibility 4\n\n**Must-Fix:**\n\n**N1** [critical] SFT baseline comparison 存在严重混淆因素，但论文叙事依赖程度过高\n- SFT PR=13% vs exec-only PR=93-98%。100-step checkpoint (PR=32%) 仅部分控制。SFT 仅 39 proved samples (3-seed pooled)。论文第一条 contribution 和核心叙事依赖这个对比。\n- 建议：降低 RL-specificity claim 的表述强度，或设计更公平的对比。\n\n**N2** [critical] 100-example eval set 统计功效严重不足\n- 许多 seed proved count 远低于 100（ISR β=0.1 s45: n=42, Random s49 matched: n=5）。5-seed pooled N-H 23% vs 3-seed corrected 6% 差异 17 pp 说明对 pooling 极度敏感。Matched cohort non-hacking permutation test p=0.917 — n=5 per group 的 permutation test 几乎无法检测任何合理效应量。\n- 建议：扩大 eval set 至 500+ examples，或在所有 per-seed 报告中附加 CIs。\n\n**N3** [critical] \"ISR exhibits Goodhart collapse at every tested dose\" 基于稀疏剂量覆盖但表述暗示普遍性\n- 仅 4 个 β 值，β=0.05 和 β=0.2 各仅 3 seeds。4 个剂量 \"collapse\" 定性各异。\n- 建议：Abstract/Discussion 加入 \"preliminary\" 或 \"at four tested doses\" 等限定词。\n\n**Should-Fix:**\n\n**W1** [major] ISR 与 NLI accuracy 无关 (ρ=-0.049) 但定位为 \"structural quality diagnostic\"。ISR 低 → H1 redundancy, ISR 高(优化下) → H7 gaming，两种情况都不直接度量推理质量。\n\n**W2** [major] Random control 产生 29.5% H7（5-seed pooled），削弱 ISR-specific 归因。exploratory vs matched cohort 的 Random H7 率差异极大（29.5% vs 6.7%）。\n\n**W3** [major] CMH p-values (p<10⁻⁹, p<10⁻¹⁶) independence assumption 被违反。建议以 seed-level Fisher exact test (p=0.004, BF₁₀=77) 为首要证据。\n\n**W4** [minor] Exec-only s43 使用 sampling eval (T=0.7) 而非 greedy。\n**W5** [minor] 丢失 checkpoints 影响审计完整性。\n\n**Questions:**\nQ1. Matched 5+5 design 是否做过 power analysis？\nQ2. Premise-count-matched comparison 仅 1.06×，\"transient quality improvement\" 是否需要修改？\nQ3. 早期 convex formulation 被放弃的理由是否充分？\nQ4. Cross-logic Prolog 实验没有 random control。\nQ5. H9 归因基于 1 个 seed 的可信度。\n\n**缺失引用：** LEGO-Prover, formal verification reward design。\n\n**关键评价：** 一篇方法严谨、结论诚实的 empirical Goodhart case study，如解决 SFT framing 和 statistical power 讨论问题，有望提升至 Conference 水平。",
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Step 2 — 交叉回应\n\n以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每条 Weakness/Question 标注 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n特别关注以下分歧点：\n1. **Overall 评分差异**：R1 给 3.5 (Borderline Conference) vs 你给 3.0 (Findings)。R1 的理由是 \"如果解决 SFT framing 和 statistical power 讨论，有望达 Conference\"。你是否同意这个条件判断？\n2. **Excitement 评估**：R1 给 3/5 vs 你给 2.5/5。R1 认为 \"ISR 的 diagnostic-vs-optimizer 不对称性是有趣发现\"。你是否认为这足以提升 excitement？\n3. **统计分析的评价**：R1 对 CMH, permutation test, Fisher exact test 给出了非常详细的分析。你是否同意其结论？\n\n---\n\n### Reviewer 1 完整意见\n\n**Overall: 3.5 (Borderline Conference)** | Soundness 3.5 | Excitement 3 | Reproducibility 4\n\n**Must-Fix:**\n\n**N1** [critical] SFT baseline comparison 存在严重混淆因素，但论文叙事依赖程度过高\n- SFT PR=13% vs exec-only PR=93-98%。100-step checkpoint (PR=32%) 仅部分控制。SFT 仅 39 proved samples (3-seed pooled)。论文第一条 contribution 和核心叙事依赖这个对比。\n- 建议：降低 RL-specificity claim 的表述强度，或设计更公平的对比。\n\n**N2** [critical] 100-example eval set 统计功效严重不足\n- 许多 seed proved count 远低于 100（ISR β=0.1 s45: n=42, Random s49 matched: n=5）。5-seed pooled N-H 23% vs 3-seed corrected 6% 差异 17 pp 说明对 pooling 极度敏感。Matched cohort non-hacking permutation test p=0.917 — n=5 per group 的 permutation test 几乎无法检测任何合理效应量。\n- 建议：扩大 eval set 至 500+ examples，或在所有 per-seed 报告中附加 CIs。\n\n**N3** [critical] \"ISR exhibits Goodhart collapse at every tested dose\" 基于稀疏剂量覆盖但表述暗示普遍性\n- 仅 4 个 β 值，β=0.05 和 β=0.2 各仅 3 seeds。4 个剂量 \"collapse\" 定性各异。\n- 建议：Abstract/Discussion 加入 \"preliminary\" 或 \"at four tested doses\" 等限定词。\n\n**Should-Fix:**\n\n**W1** [major] ISR 与 NLI accuracy 无关 (ρ=-0.049) 但定位为 \"structural quality diagnostic\"。ISR 低 → H1 redundancy, ISR 高(优化下) → H7 gaming，两种情况都不直接度量推理质量。\n\n**W2** [major] Random control 产生 29.5% H7（5-seed pooled），削弱 ISR-specific 归因。exploratory vs matched cohort 的 Random H7 率差异极大（29.5% vs 6.7%）。\n\n**W3** [major] CMH p-values (p<10⁻⁹, p<10⁻¹⁶) independence assumption 被违反。建议以 seed-level Fisher exact test (p=0.004, BF₁₀=77) 为首要证据。\n\n**W4** [minor] Exec-only s43 使用 sampling eval (T=0.7) 而非 greedy。\n**W5** [minor] 丢失 checkpoints 影响审计完整性。\n\n**Questions:**\nQ1. Matched 5+5 design 是否做过 power analysis？\nQ2. Premise-count-matched comparison 仅 1.06×，\"transient quality improvement\" 是否需要修改？\nQ3. 早期 convex formulation 被放弃的理由是否充分？\nQ4. Cross-logic Prolog 实验没有 random control。\nQ5. H9 归因基于 1 个 seed 的可信度。\n\n**缺失引用：** LEGO-Prover, formal verification reward design。\n\n**关键评价：** 一篇方法严谨、结论诚实的 empirical Goodhart case study，如解决 SFT framing 和 statistical power 讨论问题，有望提升至 Conference 水平。",
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 1253 · 2026-05-19T02:47:51.191894+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1715
}
```

</details>

---


### Assistant

_source line 1254 · 2026-05-19T02:47:54.195055+00:00_

交叉分享任务已分配。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 103

## Round 103

2 recorded events


### User

_source line 1255 · 2026-05-19T02:47:56.970305+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结论**: Overall 3.0 (Findings)。

核心判断：
- **2 个 Must-Fix**：(N1) LOO + Goodhart 均为已知技术/理论，新颖性不足支撑主会议；(N2) 与 Kim et al. (2026) 差异化不充分
- **6 个 Should-Fix**：单数据集泛化性受限、SFT 比较有 PR confound、"99.5% collapse" 来自单 seed 可能误导、术语密度过高、Table 2 聚合方式不统一、non-hacking rate 是 upper bound
- **主要优势**：matched 5+5 实验设计严谨、诚实报告局限性、写作质量高、格式完全合规、无 AI 写作痕迹

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1256 · 2026-05-19T02:48:06.311272+00:00_

两位 Reviewer 的初审已全部收到，交叉分享任务已分配。等待双方交叉回应结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 104

## Round 104

2 recorded events


### User

_source line 1257 · 2026-05-19T02:49:18.684282+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 — 交叉回应 Reviewer 2 意见

---

## Must-Fix 问题

### R2-N1: 新颖性不足（LOO + Goodhart 均为已知）

**[PARTIALLY AGREE]**

R2 的核心论点成立：LOO ablation 是标准技术（论文 §3.2 line 27 明确承认），Goodhart collapse 有充分的理论预测基础（Discussion line 7 承认 "theoretically predictable"），H7 tautology 的 ISR≥0.5 是 LOO 定义的数学必然（§3.2 line 57）。这些组件单独来看确实不构成概念级新颖性。

但我认为 R2 低估了以下经验贡献的价值，这些是理论无法预测的：

1. **Seed-dependent divergence 的具体动力学**：同一 reward 条件下 5 seeds 分裂为 2 rapid-collapse + 3 transient-window，且 divergence 发生在 steps 150-200 的窄窗口（§4.2 line 86）。理论预测 "会 collapse" 但不预测 "何时" 和 "以何种分裂模式"。
2. **H7b triple gaming**：模型同时 game 了 execution reward、ISR metric 和 text-match classifier（Appendix §H7b, line 334-335）。这是三层同时规避，不是理论可以先验推导的。
3. **Cross-logic mode diversity**：3 个 Prolog seeds 各自发现不同的 gaming pathway（H7 tautology, pseudo-Prolog, query-as-fact; Appendix Table 6），同一 Goodhart vulnerability 在不同 solver 语义下的 mode 多样性超出简单理论预测。

然而，这些贡献更多是 empirical characterization 而非 methodological innovation。R2 提出的 "至少提出一个 mitigation 策略" 是合理建议——纯 diagnostic/negative-result 论文在 excitement 评分上确实处于劣势。我的 excitement 评分 (3/5) 比 R2 (2.5/5) 略高，因为 matched 5+5 design 和 taxonomy 的独立可用性有增量价值，但我同意这不是一个 high-excitement 论文。

**结论**：同意 novelty 有限，但不同意降至 Findings 的唯一原因是 novelty——论文的实验学纪律（matched replication, seed-level 分析）本身有示范价值。如果作者补充 mitigation discussion（哪怕是 preliminary），excitement 可以提升。

---

### R2-N2: 与 Kim et al. (2026) 差异化不充分

**[AGREE]**

R2 说得对。论文在 Related Work §2 line 18 仅用一个从句区分："gaming emerges during training rather than at inference"。这不够。Kim et al. (2026) 研究 LLMs 在 inference time 对 formalization 的 gaming，本文研究 training time 的 RL-induced gaming——两者的 gaming 模式可能有重叠（如 conclusion embedding 在两者中都出现），也可能有本质差异（RL optimizer 产生 absorbing states 而 inference-time gaming 是 per-sample 的）。

但我不认为这是 **critical** 级别的问题。两篇论文的操作层面不同（Kim et al. 是 evaluation/detection at inference, 本文是 training dynamics analysis），核心方法不重叠（Kim et al. 不涉及 LOO ablation 或 reward augmentation），补充一段对比即可解决。将此降为 **major** 更合适。

**建议**：在 Related Work 中增加一段专门对比：(1) 共同点（conclusion embedding 作为 universal gaming mode）；(2) 差异（inference-time vs training-time, per-sample vs distributional shift, detection vs dynamics characterization）；(3) 互补关系（Kim et al. 的 detection methods + 本文的 STA diagnostic 可以组合使用）。

---

## Should-Fix 问题

### R2-W1: 单数据集+单模型族限制泛化性

**[AGREE]**

与我的 N2/N3 一致。C3 声称 "not specific to a single logic type or model scale" 在技术上成立（测试了 FOL+Prolog, 4B+1.7B），但仍在 FOLIO 数据和 Qwen3 架构内。跨模型（如 LLaMA, Mistral）和跨数据集（如 ProofWriter, LogiQA）的验证是必要的 future work。论文在 Limitations §1 line 1 和 Discussion line 9 都承认了这一点，但 C3 contribution statement 的措辞应该更加 hedged。

---

### R2-W2: SFT baseline prove-rate confound

**[AGREE]**

与我的 N1 完全一致。这是本文最大的方法论弱点之一。不再赘述。

---

### R2-W3: "99.5% structural collapse" 单 seed cherry-picking

**[AGREE]**

R2 这条我认为有道理。让我核实具体数据：

- **s42**: ISR* 0.642 (100步) → 0.003 (1000步) = 99.5% collapse ✓
- **s44**: ISR* 0.582 (500步) → 0.002 (1000步) = 99.7% collapse（但 s44 500步已是 H7 tautological collapse，ISR 高是假象）
- **s43**: ISR* 0 (500步, sampling eval) → 0.082 (1000步)，因协议差异无法计算 trajectory
- **3-seed 1000步 pooled**: ISR* = 0.03±0.05 (Table 5 pooled line)

s42 是唯一有 100→500→1000 完整 ISR trajectory 的 seed。将这个单 seed 的最极端数字放在 Abstract 第 4 行（"ISR reveals a 99.5% structural collapse"）确实构成 cherry-picking。3-seed 1000-step aggregate (ISR*=0.03±0.05) 同样展示了严重退化，但不如 "99.5%" 那么 headline-grabbing。

**建议**：Abstract 中改为 3-seed aggregate 描述，如 "ISR* collapses to near-zero (0.03±0.05) across three seeds at 1000 steps while PR converges to 97±2%"。单 seed 99.5% 的详细 trajectory 适合放在 §4.1 正文中。

---

### R2-W4: 缩写和术语密度过高

**[AGREE]**

论文确实需要同时追踪大量缩写：STA, ISR, ISR*, PR, GRPO, LOO, N-H, S-NH, H1, H7a, H7b, H8, H9, CI, FOL, NLI, BF₁₀, CMH, OR 等。虽然每个都在首次出现时有定义，但读者认知负荷过重。这在我的审稿中未单独提出，R2 补充得好。

**建议**：正文中减少 3-4 个缩写的使用（如 S-NH 可以在 cross-scale section 再引入而非全文使用，CI 可以直接写 "content-independent"），或在 method section 末尾加一个 notation summary。

---

### R2-W5: Table 2 混合 pooled/single-seed

**[AGREE]**

Table 2（hacking taxonomy, §4.5）的 caption 确实注明了数据来源差异（"exec/SFT: s42; ISR/Rnd 4B: 5-seed pooled; 1.7B: 3-seed pooled"），但在表内直接比较 single-seed 数据和 pooled 数据仍然容易误导读者。特别是 Exec 列的 87% H1 是 s42 单 seed，而 ISR₀.₁ 的 18% H1 是 5-seed pooled——这使得 "ISR 降低了 H1" 的视觉印象可能是 pooling artifact。

**建议**：统一为 3-seed pooled 数据，或在表中增加一列标注 "n (seeds)"。

---

### R2-W6: Non-hacking rate 定义脆弱

**[AGREE]**

与我的 W1 一致。论文在 §3.3 line 82 明确说 "All non-hacking rates reported without the 'strict' qualifier are upper bounds"，但 Table 1 中 "N-H%" 列没有标注 "upper bound"。读者很容易将 N-H% 误解为 true non-hacking rate。H7b 的发现（12 samples originally classified as non-hacking are actually obfuscated tautologies, Appendix §H7b）正好说明了这个问题。

---

## 缺失引用

**[PARTIALLY AGREE]**

- **AlphaProof / Llemma**: 这些是 Lean-based formal math proving，与本文的 NLI/FOL setting 有距离。但在 "solver-backed RL" 的大框架下提及是合理的。不过 AlphaProof 没有公开论文，引用困难。Llemma (Azerbayev et al., 2024) 可以补充。
- **Reward hacking mitigation**: R2 说得对，论文讨论了问题但没有讨论任何已知的 mitigation 方向（如 reward ensembling, KL penalty, conservative reward, reward model interpolation）。即使本文不提出新的 mitigation，引用和讨论已有策略为什么可能在 solver-backed setting 下失败也是有价值的。
- **RLVR 框架下其他工作**：Spurious Rewards (Shao et al., 2025) 已引用但讨论不足。其关于 reward variance effects 的发现与本文 Random control 的结果直接相关。

---

## R2 关键论点：论文只诊断不治疗

**[PARTIALLY AGREE]**

R2 提出 "缺少 forward-looking discussion: 如何 fix ISR？什么样的 structural metric 可能抵抗 Goodhart？" 这是一个合理的 criticism。论文 Discussion 最后一句提到 "combining it with effort-based detection (Wang et al., 2025) may yield more robust hacking identification"（line 11），但这只是一句话的 hand-waving，没有任何分析支撑。

然而，我不同意这应该作为降低评分的主要理由。论文的定位是 **empirical case study of Goodhart dynamics**，不是提出新的 reward design。Negative results / cautionary findings 在 *ACL venues 中有明确的接收先例。问题不是 "必须提出 mitigation" 而是 "需要更充分地讨论为什么 mitigation 困难以及已有策略在此 setting 下的预期表现"。

**建议**：Discussion 中增加一段分析：(1) KL regularization 为什么可能不够（cite Kwa et al., 2024 关于 heavy-tailed misspecification 下 KL 失效）；(2) Reward ensembling (ISR + effort-based) 的可能性和挑战；(3) Component-count normalization 是否能缓解 premise-count confound（论文已有数据：premise-count-matched ISR benefit 仅 1.06×，Appendix Extended Discussion，这本身就是一个 negative mitigation result）。

---

## 三个分歧点总结

### 1. 新颖性评估（R2: excitement 2.5 → Findings）

**我的立场**：R2 的担忧有道理但我不完全同意降至 Findings。论文的经验贡献（dynamics characterization, taxonomy, matched design）在我看来值 excitement 3.0。但如果不补充 mitigation discussion，我理解 2.5-3.0 之间的分歧是合理的。两位 reviewer 的共识区间大约是 Overall 3.0-3.5。

### 2. Kim et al. (2026) 差异化

**我的立场**：同意需要更多对比，但应为 **major** 而非 **critical**。两篇论文的方法论和研究层面（inference vs training）不重叠，补充一段对比即可解决，不需要大幅重构论文。

### 3. "99.5% collapse" 单 seed in Abstract

**我的立场**：同意 R2，这是 cherry-picking。s42 是唯一有完整 3-checkpoint trajectory 的 seed，选择其最极端数字放在 abstract 不符合科学叙事的最佳实践。3-seed 1000-step aggregate (ISR*=0.03±0.05) 同样震撼但更诚实。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1258 · 2026-05-19T02:49:24.561961+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 105

## Round 105

2 recorded events


### User

_source line 1259 · 2026-05-19T02:49:27.428690+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。三个分歧点的核心判断：

1. **新颖性**：部分同意 R2。概念框架不新，但经验贡献（dynamics, taxonomy, matched design）有增量价值。我维持 excitement 3.0 vs R2 的 2.5，共识区间 3.0-3.5 Overall。
2. **Kim et al. 差异化**：同意需补充对比，但应降为 major（非 critical），因为两篇论文方法论层面不重叠。
3. **99.5% cherry-picking**：同意 R2。建议 abstract 改用 3-seed aggregate (ISR*=0.03±0.05)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1260 · 2026-05-19T02:49:33.039627+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 106

## Round 106

8 recorded events


### User

_source line 1261 · 2026-05-19T02:50:31.669973+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — 交叉回应 Reviewer 1

---

### Must-Fix 逐条回应

**[AGREE] R1-N1: SFT baseline comparison confound，叙事依赖过高**
完全同意。这与我的 W2 一致。关键数字：SFT PR=13% (n=39) vs exec-only PR=93-98%，差距达 ~80pp。100-step checkpoint (PR=32%, hacking≥31%, Appendix F.1) 虽然方向上支持 RL-specificity，但 PR 仍然高于 SFT（32% vs 13%），且仅有 s42 一个 seed（n=32）。论文 Introduction line 13 的措辞 "consistent with it being RL-specific" 以及 Abstract line 4 的表述确实可能让读者高估证据强度。R1 建议降低 RL-specificity claim 强度是合理的。

**[AGREE] R1-N2: 100-example eval set 统计功效不足**
完全同意。这与我的 W1 (单数据集限制) 对应。补充两个具体数据点：(1) ISR β=0.1 s45 仅 n=42 proved samples，其 54.8% non-hacking 实际只有 ~23 个样本，Wilson 95% CI 约 [39%, 70%]；(2) matched cohort Random s49 仅 n=5，任何 percentage 都无统计意义。R1 指出的 "5-seed pooled N-H 23% vs 3-seed corrected 6%，差异 17pp" 尤其说明问题——同一数据在不同 pooling 下结论几乎反转（Fisher p 从 <10⁻⁸ 变为 0.182 n.s., Table 4/Appendix C）。建议扩大 eval set 或在所有 per-seed 报告附 CIs 是实际可行的改进。

**[REBUT] R1-N3: "at every tested dose" 暗示普遍性**
部分不同意。R1 的 concern 是措辞暗示了超出证据的普遍性。但我认为论文在这一点上已经做了合理的限定：

1. Abstract line 5 原文是 "at every tested dose"（不是 "at all doses"），已包含限定词
2. Introduction line 15 同样用了 "at all four tested doses"
3. 更关键的是，论文提供了一个 structural argument：H7 tautology 在 LOO 定义下恒定获得 ISR≥0.5（Section 4.3 line 52），而 non-hacking proofs 的 premise-count-matched ISR 仅 ~0.26（Appendix C），这个 reward gap 是 β-independent 的。这意味着 Goodhart vulnerability 不是 dose-specific 的经验观察，而是 ISR 定义的数学性质。
4. 4 个 dose 虽然稀疏，但覆盖了从 micro (0.05) 到 high (0.3) 的范围，且全部 collapse，与 structural argument 一致。

因此我认为 "at every tested dose" 的措辞是准确的，不需要额外加 "preliminary"。不过 R1 指出的 dose-specific dynamics 差异（0.05 deterministic, 0.1 stochastic, 0.2 immediate, 0.3 multi-modal）确实值得在 Discussion 中更清楚地区分 "collapse occurs" vs "collapse dynamics vary"。

---

### Should-Fix 逐条回应

**[AGREE] R1-W1: ISR ≠ semantic quality**
同意，这是论文的一个 fundamental limitation。ISR 与 NLI accuracy 的 Spearman ρ=-0.049 (p=0.187, Appendix C) 意味着 ISR 不度量推理质量。论文将 ISR 定位为 "structural integrity diagnostic"，但 "structural integrity" 的实际语义是 "component necessity"（每个成分是否不可或缺），而非 "reasoning quality"。论文在 Section 3.2 line 55-58 和 Appendix C 对此有讨论，但 Introduction 和 Abstract 的叙事中 "structural quality" 和 "structural integrity" 的措辞可能给读者过于正面的印象。如果 ISR 高既不意味着好推理（因为 H7 也能高）、ISR 低也不一定意味着坏推理（Prolog 的 ground fact redundancy），那么 ISR 作为 diagnostic 的核心价值需要更精确的框定。

**[REBUT] R1-W2: Random control 29.5% H7 削弱 ISR-specific 归因**
部分不同意。R1 的 concern 是 Random 也产生 H7，削弱了 ISR-specific 的因果归因。但论文已经通过 matched cohort 充分回应了这一点：

1. Matched cohort (seeds 47-51): ISR 5/5 H7-dominated vs Random 0/5 H7-dominated，Fisher p=0.004, BF₁₀=77（Section 4.3 line 103, Table 11）。这是 clean evidence。
2. Exploratory cohort 的 29.5% pooled H7 由 s46 (91.5%) 和 s43 (38.3%) 主导，其余 3 seeds 均为 0%（Table 5）。Pooled rate 掩盖了极端的 seed dependence。
3. 关键区别在于 dynamics（Section 4.3 line 94-95）：ISR-induced H7 是 absorbing（100% in affected seeds），而 Random-induced H7 coexists with other modes（38-92%）且 non-systematic。ISR 将 H7 从 stochastic possibility 转化为 irreversible attractor。

R1 指出的 "exploratory vs matched cohort Random H7 率差异极大（29.5% vs 6.7%）" 实际上恰好说明了论文的 single-seed unreliability point（Appendix C）：Random 的 H7 是 seed-dependent noise，不是 systematic。matched cohort 的 0/5 vs 5/5 是更可靠的证据。

**[AGREE] R1-W3: CMH p-values independence assumption violated**
完全同意。论文自己在 Limitations line 10 和 Appendix D (line 120-122) 已经承认 "CMH assumes within-stratum independence, but samples within each seed share a single checkpoint and use greedy decoding; the effective independent units are seeds (n=5), not samples"。R1 建议以 seed-level Fisher exact test (p=0.004, BF₁₀=77) 为首要证据是正确的。论文实际上已经这样做了（Section 4.3 line 103），CMH 只是补充，但 Appendix D 的 CMH 呈现可能给读者错误的 "p<10⁻¹⁶" 精度印象。建议将 CMH 明确标注为 "directional only" 并降低其呈现优先级。

**[AGREE] R1-W4: s43 sampling eval**
同意，minor issue。论文在 Appendix A line 55-56 已承认。

**[AGREE] R1-W5: 丢失 checkpoints**
同意，minor issue。论文在 Limitations line 12 和 Appendix F.3 已承认。matched cohort 保留了全部 checkpoints，mitigates this concern。

---

### Questions 回应

**[AGREE] R1-Q1: Power analysis**
没有看到论文中有 formal power analysis 的证据。matched cohort 的设计（5+5）可能是基于 exploratory cohort 的发现而非 pre-registered power calculation。论文应说明 sample size 的选择依据。

**[AGREE] R1-Q2: Premise-count-matched 1.06×**
同意这是一个重要的 negative result。ISR 0.258 vs Random 0.243 (1.06×, Appendix C) 意味着即使在 transient non-hacking window 内，ISR 对 genuine structural quality 的提升几乎为零。"Transient quality improvement" 的措辞（Abstract line 5: "any transient quality improvement disappears"）暗示曾经存在 improvement，但 1.06× 几乎不构成 improvement。建议将 "quality improvement" 修改为 "apparent improvement" 或 "non-hacking window"。

**[AGREE] R1-Q3: Convex formulation 放弃**
论文在 Section 3.3 line 73 给出了理由（ISR<1 always penalized relative to exec-only, collapsing PR），并指向 Appendix A。这是合理的实验决定，但可以更详细地报告实验数据。

**[AGREE] R1-Q4: Prolog 无 random control**
有效的 concern。Section 4.4 明确标注为 "preliminary cross-logic probe"（line 114），但缺少 random control 意味着无法区分 ISR-specific Goodhart vs generic GRPO instability under any augmented reward。至少应该讨论这一限制。

**[AGREE] R1-Q5: H9 单 seed**
同意。H9 仅在 1.7B Random β=0.1 s42 一个 seed 观察到（Appendix E.9 line 480-482），证据强度有限。论文将其标注为 "identified through manual audit" 而非 robust mode 是合适的，但读者可能仍高估其可靠性。

---

### 缺失引用

**[AGREE]** R1 建议的 LEGO-Prover 和 formal verification reward design 引用是合理的补充。我在 R2 审稿中也指出了 Lean-based RL 工作和 reward hacking mitigation 策略的缺失。

---

### 三个分歧点的判断

#### 1. Overall 评分差异：R1 3.5 vs R2 3.0

**维持 R2 的 3.0 (Findings)**，理由如下：

R1 的条件判断是 "如果解决 SFT framing 和 statistical power 讨论问题，有望达 Conference"。我认为这个条件不充分——即使完美解决 SFT comparison 和统计 power 问题，核心 novelty gap 仍然存在：

- **方法层面**：LOO ablation 是标准技术（mutation testing），论文自己反复承认
- **发现层面**：Goodhart collapse 在 ISR 的 LOO 定义下是数学可预测的（H7 恒定获得 ISR≥0.5），不需要实验确认
- **贡献层面**：没有提出任何 mitigation 策略，论文停留在 "diagnosis + warning" 层面

这些都不是 framing 修复能解决的问题。EMNLP 主会议（Overall 4.0）期待概念上的新贡献，而本文的贡献主要是 "applying known technique to new domain + confirming known theory + descriptive taxonomy"。这是扎实的 Findings 论文。

不过我承认 R1 的判断有合理性：如果 reviewer pool 中多数人认为 empirical Goodhart case study 的细节（seed-dependent divergence, cross-logic diversity, absorbing-state dynamics）构成足够的新知，3.5 是可能的。但我个人的标准下，这些更接近 "empirically interesting but conceptually expected"。

#### 2. Excitement 评估：R1 3/5 vs R2 2.5/5

**维持 R2 的 2.5/5**，但承认这是 borderline call。

R1 认为 "diagnostic-vs-optimizer 不对称性是有趣发现"。我同意不对称性本身有表述价值，但这个不对称性的原因太 straightforward：ISR 的 LOO 定义在数学上偏好低 component count（Section 3.2 line 56-57），H7（单前提=结论）是 ISR-maximizing exploit（Appendix C line 154），因此 "useful as diagnostic but exploitable as reward" 是直接推论而非 surprising discovery。

如果论文提出了 mitigation（如 component-count normalization、multi-component tautology check）并展示了 partial success，excitement 会显著提升。纯诊断论文的 excitement ceiling 较低。

#### 3. 统计分析评价

**基本同意 R1 的统计分析结论**。具体来说：

- **CMH 应降为次要证据**: 同意。within-seed dependence violation 使 CMH p<10⁻¹⁶ 严重膨胀（实际独立单元 n=5，不是 n=350/414）。
- **Seed-level Fisher (p=0.004, BF₁₀=77) 应为首要证据**: 同意。这是对 H7 domination（ISR 5/5 vs Random 0/5）最 clean 的检验。
- **Permutation test p=0.28/0.26 反映 power 不足而非 absence of effect**: 同意。n=5 per group 的 minimum achievable p=0.008（论文 Appendix D line 122），检测合理效应量几乎不可能。
- **Non-hacking rate permutation test p=0.917 是 genuine negative**: 这里我的判断与 R1 略有不同。p=0.917 虽然受 power 限制，但 point estimate 方向（ISR 2.3% vs Random 5.9%，Section 4.3 line 103）实际上是 ISR worse than Random，不是 ISR better。这不仅是 power 问题，还是 direction 问题——ISR 作为 reward 可能连 non-hacking quality 都不如 random noise。论文应更明确地讨论这个 negative direction。

---

### 总结

R1 和 R2 在技术问题上高度一致（SFT confound, eval set size, CMH assumption violation, lost checkpoints）。核心分歧在于 novelty/excitement 评估：R1 更看重 empirical contribution 的细节价值，R2 更看重 conceptual advance 的门槛。我认为本文是一篇高质量的 empirical case study，适合 Findings (3.0)，但理解 R1 给 Borderline Conference (3.5) 的逻辑。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1262 · 2026-05-19T02:51:49.349856+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml",
    "limit": "30"
  }
}
```

</details>

---


### Tool result

_source line 1263 · 2026-05-19T02:51:49.400691+00:00_

1	issues:
2	# ===== 历史 issues (Round 0-3, 全部 resolved) =====
3	- id: "R1-W1"
4	  summary: "统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例"
5	  category: experiment
6	  severity: critical
7	  status: resolved
8	  first_raised_round: 0
9	  last_seen_round: 2
10	  resolution: "β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。Fisher exact test + Wilson 95% CI 已加入。eval 集 100 例限制在 limitations.tex 讨论。"
11	  resolution_round: 2
12	
13	- id: "RV-EVAL-FALLBACK"
14	  summary: "eval_sta.py test_100.jsonl 静默 fallback 已移除"
15	  category: experiment
16	  severity: critical
17	  status: resolved
18	  first_raised_round: 1
19	  last_seen_round: 1
20	  resolution: "第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)，无 fallback。"
21	  resolution_round: 1
22	
23	- id: "RV-D060-NARRATIVE"
24	  summary: "D060 'Goodhart instability' 叙事：77pp PR 差距在同一测试集上确认成立"
25	  category: experiment
26	  severity: critical
27	  status: resolved
28	  first_raised_round: 1
29	  last_seen_round: 1
30	  resolution: "β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1264 · 2026-05-19T02:56:14.930867+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "solver-trace-ablation",
  "issues_yaml": "issues:\n# ===== 历史 issues (Round 0-3, 全部 resolved) =====\n- id: \"R1-W1\"\n  summary: \"统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。Fisher exact test + Wilson 95% CI 已加入。eval 集 100 例限制在 limitations.tex 讨论。\"\n  resolution_round: 2\n\n- id: \"RV-EVAL-FALLBACK\"\n  summary: \"eval_sta.py test_100.jsonl 静默 fallback 已移除\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)，无 fallback。\"\n  resolution_round: 1\n\n- id: \"RV-D060-NARRATIVE\"\n  summary: \"D060 'Goodhart instability' 叙事：77pp PR 差距在同一测试集上确认成立\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。\"\n  resolution_round: 2\n\n- id: \"RV-FIG2-STALE-SCRIPT\"\n  summary: \"figures/paper/gen_fig2.py 旧脚本数据错误\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"已修复。\"\n  resolution_round: 1\n\n- id: \"R1-W2\"\n  summary: \"ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。\"\n  resolution_round: 2\n\n- id: \"R2-W1\"\n  summary: \"Limitations section 格式不合规\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"独立 limitations.tex 已创建，位于 references 之前。\"\n  resolution_round: 3\n\n- id: \"R2-W2\"\n  summary: \"实验仅用单一模型 (Qwen3-4B) 和单一数据集 (FOLIO)，标题复数暗示通用性\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"标题改为单数。Qwen3-1.7B cross-scale 实验已加入。\"\n  resolution_round: 3\n\n- id: \"R1-W4\"\n  summary: \"Exec-only seed 43 使用 sampling (T=0.7) 评估而非 greedy\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"exec-only 500-step 主表仅报告 s42（†标注）。\"\n  resolution_round: 2\n\n- id: \"R1-W3\"\n  summary: \"'Solver-agnostic' 仅测 2 solver，过度声明\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"'solver-agnostic' 已从全文移除。\"\n  resolution_round: 2\n\n- id: \"R2-W6\"\n  summary: \"SFT baseline 比较不公平：PR=14% vs 93%，低 PR 本身减少 hacking 机会\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"100-step RL 对照已加入。claim 调整为 'consistent with'。\"\n  resolution_round: 2\n\n- id: \"R2-W7\"\n  summary: \"与 Kim et al. (2026) 差异化不充分\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"related_work.tex 中有区分段落。\"\n  resolution_round: 2\n\n- id: \"R1-W6\"\n  summary: \"训练 500 例/评估 100 例的规模限制讨论不充分\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"limitations.tex 已讨论。\"\n  resolution_round: 2\n\n- id: \"R1-W7\"\n  summary: \"H1/H7 classifier precision/recall 未报告\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"50 样本人工验证 precision >95%。\"\n  resolution_round: 2\n\n- id: \"R1-W8\"\n  summary: \"Random control U(0,1) 与 ISR 的 skewed 分布不匹配\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"method.tex 和 experiments.tex 均说明了 Random 设计目的。\"\n  resolution_round: 2\n\n- id: \"R1-W9\"\n  summary: \"缺代码/数据开源承诺\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"abstract.tex:9 脚注 'Code and data: [anonymized]'。\"\n  resolution_round: 2\n\n- id: \"R1-W5\"\n  summary: \"'Meta-level Goodhart' 新颖性论证不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"framing 降级为 empirical instance。\"\n  resolution_round: 3\n\n- id: \"R2-W8\"\n  summary: \"H1/H7 编号不连贯（H2-H6 不存在）\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"method.tex 解释了合并原因。\"\n  resolution_round: 3\n\n- id: \"v2-R1-N1\"\n  summary: \"Abstract '93%' PR 为 single seed，应改为 mean±std\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Abstract 使用 3-seed pooled mean±std。\"\n  resolution_round: 3\n\n- id: \"v2-R1-N3\"\n  summary: \"仅 2 个 β 值不足以刻画 dose-response\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"4 个 β 值提供完整 dose-response 曲线。\"\n  resolution_round: 4\n\n- id: \"v2-R2-N3\"\n  summary: \"STA 方法论新颖性有限\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"novelty 定位为 applying standard LOO。\"\n  resolution_round: 3\n\n- id: \"v2-R2-N2\"\n  summary: \"单模型+单数据集泛化性不足\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"cross-scale 实验加入。单数据集限制在 Limitations 讨论。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W3\"\n  summary: \"ISR-as-reward 控制 confound 后净效果仅 1.06×\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"ISR 定位从 training signal 转为 diagnostic-only。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W6\"\n  summary: \"Hacking taxonomy 缺乏 IAA 验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"deterministic rules + 50-sample precision check。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W3\"\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Abstract 重写为 ~170 words。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W4\"\n  summary: \"Premise-count confound 讨论放在 Appendix 而非正文\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"提升到正文 §3.2。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W5\"\n  summary: \"C2 和 C4 独立性不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"taxonomy 独立性论证成立。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-1\"\n  summary: \"Limitations section 位于 References 之后\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"顺序已正确。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-2\"\n  summary: \"Ethics Statement 缺失\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"ethics.tex 加入。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-3\"\n  summary: \"Orphan bibliography entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"orphan entries 清除。\"\n  resolution_round: 3\n\n- id: \"v2-R1-M4\"\n  summary: \"Prolog cross-logic transfer 样本量过小\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"'universal Goodhart' 移除，改为 qualitative observation。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W1\"\n  summary: \"3 seeds 统计效力不足以支撑定量 claims\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"统计方法改进。定量 claims 降级。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W4\"\n  summary: \"SFT baseline 比较因 PR 悬殊说服力有限\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"100-step RL 对照充分利用。\"\n  resolution_round: 3\n\n- id: \"R2-MISSING-REF\"\n  summary: \"引用覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"31 条引用覆盖核心领域。\"\n  resolution_round: 3\n\n- id: \"v3-R1-NI-2\"\n  summary: \"β=0.2 未在 Table 1 中独立报告\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Table 1 现已包含 β=0.2 行。\"\n  resolution_round: 4\n\n- id: \"v3-R1-NI-3\"\n  summary: \"§4.2 cross-seed 描述暗示最终状态\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"现标注 '(at 500 steps)'。\"\n  resolution_round: 4\n\n- id: \"v3-R12-NI-4\"\n  summary: \"全文 em-dash AI 写作痕迹\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: \"em-dash=0, -ing endings 仅 4 处轻微, blacklisted words=0。\"\n  resolution_round: 5\n\n- id: \"v3-R2-NI-5\"\n  summary: \"Abstract 'zero structurally sound outputs' 与 N-H=8% 矛盾\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Abstract 现用 'effectively zero...at convergence'。\"\n  resolution_round: 4\n\n# ===== Round 4+ carry-over =====\n\n- id: \"v3-R12-NI-1\"\n  summary: \"Cross-scale 实验 seed 数量不足\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 13\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"两位 reviewer 一致。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"现已用 D129 完整 3-seed 数据重写 §4.5。\"\n    - round: 11\n      reviewers: [1]\n      note: \"R1-W4: 3 seeds 仍不足以作为独立 contribution 支撑。D134 扩展至 10 seeds 正在训练中。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-N1 再次要求增加模型/数据集多样性。R2-N3 将 C3 cross-logic 定为 preliminary 不应为正式 contribution。两人一致建议降级 C3。R12 fix: C3 弱化为 'evidence of generality'（commit 9dc8835）。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13 R2-W1: C3 仍在同一 dataset (FOLIO) 和 model family (Qwen3) 内。两位 reviewer 一致要求进一步 hedge C3 措辞。\"\n\n- id: \"v4-R12-N2\"\n  summary: \"'Inevitable collapse at all doses' claim 超出证据\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 13\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"共识: 区分 'observed in all seeds tested' vs 'population-level inference'。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"术语降级为 'seed-dependent divergence' 和 'dose-varying patterns'。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-W3 再次指出稀疏。R1 交叉回应认为 'all tested doses show Goodhart collapse' 成立。R12 fix: 加强 preliminary 标注，区分 500-step snapshot vs trajectory（commit 9dc8835）。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-N3 认为 Abstract/Discussion 仍需更多 hedging。R2 反驳称 structural argument (H7 恒定 ISR≥0.5) 使 'at every tested dose' 成立。分歧记录。\"\n\n- id: \"v4-R12-N3\"\n  summary: \"OR=3.48 (uncorrected) vs OR=0.61 (corrected) 方向反转\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 13\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Table 1 和 Discussion §5 仍以 23% (uncorrected) 为 headline。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"OR 反转仍是核心问题。降级为 major。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-N2 + R2-N2 [critical]。Seed-level p=0.26，corrected OR=0.61。R12 fix: transient window 降级为 descriptive observation，Table 1 N-H 改用 corrected 6%，论文最强 claim 锚定为 'Goodhart collapse at every dose'（commit 9dc8835）。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Table 1 现用 corrected 6%†，但 footnote 同时给出 uncorrected 23%。R2 指出 non-hacking permutation p=0.917 且 point estimate ISR(2.3%) < Random(5.9%) 方向反转。两位 reviewer 一致认为 transient window 不构成 ISR 优势证据。\"\n\n- id: \"v4-R12-W6\"\n  summary: \"Seed 43 exec-only 评估协议矛盾\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 13\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Appendix Table 5 s43-500 Notes 列已修正。\"\n    - round: 12\n      reviewers: []\n      note: \"Round 12 未提及。Appendix 中已有 † 标注。\"\n    - round: 13\n      reviewers: [1]\n      note: \"R1-W4 [minor]: s43 数据仍在 cross-seed 比较中出现（§4.1），建议正文加脚注。\"\n\n- id: \"v4-R12-W7\"\n  summary: \"Deleted checkpoints (ISR β=0.1 s43/s44) 导致 H8 audit 不完整\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"'All N-H rates are upper bounds' 声明已加入 method.tex。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-N3 [critical]: 5-seed N-H=23% 为 uncorrected upper bound。R12 fix: Table 1 改用 corrected 3-seed 6%，footnote 说明（commit 9dc8835）。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W5 [minor]: Table 1 脚注存在但不够醒目。R2-W6: N-H% 列建议标注 '(upper bound)'。两位 reviewer 一致。\"\n\n- id: \"v4-R1-W8\"\n  summary: \"100 eval samples 对 per-seed claims 统计功效不足\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-W5 + R2 [AGREE with nuance]。建议报告 Wilson CI。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-N2 [critical]: 5-seed pooled N-H 23% vs 3-seed corrected 6% 差 17pp；matched cohort non-hacking permutation p=0.917 因 n=5 power 不足无法检测效应。R2 补充: ISR s45 n=42 的 54.8% N-H 实际只有 ~23 samples。两人一致建议扩大 eval set 或附 CIs。\"\n\n- id: \"v4-R2-W9\"\n  summary: \"方法新颖性有限：Algorithm 1 仅 6 行伪代码\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"共识: Findings 级别。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1 Excitement 3/5, R2 2.5/5。两人均同意 Findings。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-N1 [critical]: LOO+Goodhart 均为已知。R1 部分同意但认为 empirical contributions 有增量价值（seed-dependent divergence, H7b triple gaming, cross-logic diversity）。R1 Excitement 3.0 vs R2 2.5。分歧但共识区间 Findings-Borderline Conference。\"\n\n- id: \"v4-R2-W5\"\n  summary: \"未测试 tautology-guarded ISR 变体\"\n  category: method\n  severity: warning\n  status: wont_fix\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"Future work. Arms-race evidence 已有。\"\n  resolution_round: 4\n\n- id: \"v5-R1-N3\"\n  summary: \"Table 1 比较框架不对称\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 13\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Table 1 已拆分为 primary + cross-scale。\"\n    - round: 11\n      reviewers: []\n      note: \"未直接提及。\"\n    - round: 13\n      reviewers: [1]\n      note: \"R1 Detailed Comments: Table 1 混合 500-step 和 1000-step 结果需更清楚标注。\"\n\n- id: \"v5-R2-N3\"\n  summary: \"'Diagnostic becomes optimization target' 概念新颖性有限\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R2-N2 [critical]。R1 认为 empirical phenomena 有独立价值但同意 Findings。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1 Excitement 3/5 vs R2 2.5/5。两人均同意 Findings。结构性问题。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"同上。R2 进一步论证: ISR 的不对称性原因 'too straightforward'（LOO 偏好低 component count，H7 是全局最优 exploit）。结构性问题，无法通过修改解决。\"\n\n- id: \"v5-R2-W1\"\n  summary: \"Abstract 数据堆砌 / 单 seed 数据选择性报告\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 fix: 数字减至 ≤3 个 headline figures。\"\n    - round: 12\n      reviewers: []\n      note: \"R12 未再提及 Abstract 数据堆砌（质量重写后改善）。但 R12 建议术语密度可进一步降低。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W3: Abstract '99.5% structural collapse' 来自 s42 单 seed 100→1000 步轨迹，有 cherry-picking 嫌疑。R1 交叉时 [AGREE]，建议改为 3-seed aggregate (ISR*=0.03±0.05)。两人一致。\"\n\n- id: \"v5-R2-W3\"\n  summary: \"paragraph{} 过度碎片化\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"method/conclusion/limitations 仍有多个 paragraph{}。\"\n    - round: 12\n      reviewers: []\n      note: \"R12 未再提及 paragraph{} 问题（质量重写后已大幅改善）。\"\n    - round: 13\n      reviewers: []\n      note: \"R13 未提及。可能已修复，待确认。\"\n\n- id: \"v5-R2-W4\"\n  summary: \"Experiments §4.3 按 β 值呈现顺序非升序\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 10\n  resolution: \"§4.3 已按升序呈现。\"\n  resolution_round: 10\n\n- id: \"v5-R12-SFT-PR\"\n  summary: \"SFT baseline PR confound (PR=13% vs 93%)\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"SFT caveat 加入。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-W1 + R2-W1。R12 fix: Abstract 加 'though the large prove-rate gap prevents definitive causal attribution'。Limitations 加 SFT best-of-N open question（commit 9dc8835）。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-N1 [critical]: RL-specificity claim 依赖此对比但证据基础薄弱。SFT n=39，100-step checkpoint 仅 s42 (n=32)。R2-W2 [major] 完全同意。两位 reviewer 一致要求进一步降低 RL-specificity claim 强度。\"\n\n- id: \"v5-R2-MR\"\n  summary: \"缺少重要引用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"已加入 Cao et al. 2026 + Wang et al. 2025。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 建议补充 STaR + Cobbe + Lean-based RL。R12 fix: 已加入 STaR (Zelikman 2022) + Cobbe (2021)（commit 9dc8835）。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1: 补 LEGO-Prover, formal verification reward design。R2: 补 Lean-based RL (Llemma), reward hacking mitigation 策略, RLVR 其他工作。两人一致缺 mitigation literature 引用。\"\n\n- id: \"v5-R2-W6\"\n  summary: \"Table 1 信息密度过高\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 10\n  resolution: \"已拆分为 Table 1 + Table 2。R12: Table 2 移入 Appendix 节省空间。\"\n  resolution_round: 12\n\n- id: \"v5-R1-W5\"\n  summary: \"Goodhart taxonomy variant 未指定\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  resolution: \"related_work.tex 指定 'primarily regressional, with extremal elements'。\"\n  resolution_round: 7\n\n- id: \"v5-R1-W6\"\n  summary: \"ISR reward landscape 几何结构未分析\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  resolution: \"experiments.tex 包含 reward landscape 分析。\"\n  resolution_round: 7\n\n- id: \"v6-R2-N1\"\n  summary: \"ISR 核心指标命名不一致\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"全文统一使用 Irreducible Solver Rate。\"\n  resolution_round: 7\n\n- id: \"v6-R2-W5\"\n  summary: \"ISR 名称含 'Reward' 具有误导性\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"ISR 统一为 'Irreducible Solver Rate'。\"\n  resolution_round: 7\n\n- id: \"v6-R1-W2\"\n  summary: \"Dose-response claim 统计上不足\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1]\n      note: \"整体统计 power 批评。\"\n    - round: 12\n      reviewers: [1]\n      note: \"R1-W3: 4β×3-5seeds 仍稀疏。R12 fix: 加强 preliminary 标注（commit 9dc8835）。D134 扩展 β=0.1 到 10 seeds。\"\n    - round: 13\n      reviewers: [1]\n      note: \"R1-N3: 4 个 dose 各只 3-5 seeds，dynamics 定性各异但统一称 'Goodhart collapse'。R2 反驳称 structural argument 足够。分歧记录。\"\n\n- id: \"v6-R2-W2\"\n  summary: \"§4.3 的 β 值呈现顺序非升序\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 10\n  resolution: \"已按升序呈现。\"\n  resolution_round: 10\n\n- id: \"v6-R2-W6-LOO\"\n  summary: \"LOO 缩写未在首次使用时正式定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"introduction.tex 现有完整定义。\"\n  resolution_round: 7\n\n- id: \"v6-R2-W8\"\n  summary: \"Hacking taxonomy 分类标准不够 principled\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1]\n      note: \"仅 H1/H7 有 precision 验证。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-W4 + R2-W3: robust vs isolated 应在 Abstract 区分。R12 fix: Abstract 改为 'three robust modes (H1/H7/H8) + additional isolated observations'（commit 9dc8835）。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1: H8 只在 s42 完成审计，'validated across multiple seeds' 对 H8 是否准确？R2: taxonomy 有独立工具价值但仅 H1/H7 有 precision 验证。\"\n\n- id: \"v7-R1-N2\"\n  summary: \"CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: \"CMH 移至 Appendix，正文以 seed-level permutation p=0.26 为 primary。\"\n  resolution_round: 9\n\n- id: \"v7-R2-MR1\"\n  summary: \"缺少 Goodhart's Law 经典引用\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  resolution: \"references.bib 包含 Goodhart 1975。\"\n  resolution_round: 8\n\n- id: \"v7-R2-W7\"\n  summary: \"experiments.tex 'Notably' AI 写作标记\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: \"'Notably' 已移除。\"\n  resolution_round: 9\n\n- id: \"v8-R12-N1\"\n  summary: \"Goodhart 发现的可预测性限制概念新颖性\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R2-N2 [critical]。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1 Excitement 3/5 认为 empirical details 超出可预测范围，R2 2.5/5。两人均同意 Findings。结构性问题。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-N1 [critical]: H7 的 ISR≥0.5 是数学必然，不需实验确认。R1 部分同意但认为 dynamics 细节有价值。结构性问题：核心发现的可预测性是概念层面的限制，无法通过写作修改解决。\"\n\n- id: \"v8-R1-N3\"\n  summary: \"术语交替使用导致语义滑移\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"Fig 2/3 'Genuine' → 'Non-hacking' 已修复。偶见残留。\"\n    - round: 12\n      reviewers: []\n      note: \"R12 未再提及术语滑移。\"\n    - round: 13\n      reviewers: []\n      note: \"R13 未再提及术语滑移。可能已修复，待确认。\"\n\n- id: \"v8-R12-N2\"\n  summary: \"实验范围与标题/claim scope 不匹配\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Subtitle 改为 'GRPO-Trained FOL Reasoners'。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-N3 [critical]: 仍暗示通用结论。R12 fix: C3 弱化为 'evidence of generality'，Contributions 加 'from a single model family and dataset'（commit 9dc8835）。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W1: C3 仍在同一 dataset 和 model family 内。Discussion line 11 'STA applies to any compositional-input/binary-verifier setting' 缺乏验证。两人一致认为泛化性 claim 仍需进一步 hedge。\"\n\n- id: \"v8-R1-W4\"\n  summary: \"多重比较未校正\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1]\n      note: \"limitations.tex 新增 'Multiple comparisons' 段落。\"\n    - round: 12\n      reviewers: []\n      note: \"R12 未再单独提及。\"\n    - round: 13\n      reviewers: [1]\n      note: \"R1-W3: CMH independence violation 仍需更清晰标注为 'directional only'。R2 AGREE。\"\n\n- id: \"v8-R1-MR\"\n  summary: \"缺少 reward shaping 和 inference-time hacking 引用\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Uesato 2022, Paulus 2018, Langosco 2022 等已补充。\"\n  resolution_round: 10\n\n- id: \"v9-R1-N3\"\n  summary: \"Premise-count confound 影响范围分歧\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"method.tex 增加 confound 两场景区分句。\"\n  resolution_round: 9\n\n- id: \"v9-R12-W1\"\n  summary: \"§4.4 标题措辞过强\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"§4.4 标题改为 'Cross-Logic Extension'。\"\n  resolution_round: 9\n\n- id: \"v9-R1-W5\"\n  summary: \"训练时 sampling vs 评估时 greedy 不一致\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"§4.1 已增加讨论。\"\n  resolution_round: 9\n\n- id: \"v9-R12-Q-ISR-FILTER\"\n  summary: \"ISR 作为 filter 未测试\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"conclusion.tex 增加 'ISR as post-hoc filter' 作为 future work。\"\n  resolution_round: 9\n\n- id: \"v9-R12-Q-NORMALIZED-ISR\"\n  summary: \"未测试 premise-count-normalized ISR\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"conclusion.tex 增加 'normalized variants' 作为 future work。\"\n  resolution_round: 9\n\n- id: \"v4-RV-STALE-APPENDIX\"\n  summary: \"Appendix Table 仍用旧数据\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 7\n  resolution: \"Appendix Table 5 现含完整 per-seed data。\"\n  resolution_round: 7\n\n# ===== Round 10 issues =====\n\n- id: \"v10-R12-N1\"\n  summary: \"§4.5 与 Limitations 关于 1.7B seed 数量矛盾\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  resolution: \"D129 完整 3-seed 数据重写 §4.5。\"\n  resolution_round: 11\n\n- id: \"v10-R2-Q6\"\n  summary: \"ISR=0.75 推导与实测不一致\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  resolution: \"改为 ISR≥0.5。PDF 已重编译。\"\n  resolution_round: 11\n\n- id: \"v10-R2-W7\"\n  summary: \"'Valid but Vacuous' 中 'valid' 有歧义\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"建议改为 'Verified but Vacuous'。保留原标题决策。\"\n    - round: 12\n      reviewers: []\n      note: \"Round 12 未再提及。\"\n    - round: 13\n      reviewers: []\n      note: \"Round 13 未再提及。可能不再是活跃问题。\"\n\n- id: \"v10-R2-W8\"\n  summary: \"Discussion/Conclusion 过于简短\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Discussion 扩展到 ~33 行。\"\n    - round: 12\n      reviewers: []\n      note: \"R12 未批评长度。P0 压缩后约 11 行但内容更密集。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2: Discussion 缺 forward-looking content（mitigation 方向）。R1 部分同意，建议增加 mitigation 困难性分析段落。\"\n\n- id: \"v10-R2-W5\"\n  summary: \"C2 和 C4 边界不清晰\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"Contributions 合并为 3 条。\"\n  resolution_round: 10\n\n# ===== Round 11 issues =====\n\n- id: \"v11-R12-N1\"\n  summary: \"Responsible NLP Research Checklist 缺失\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"checklist.tex 创建并附在论文末尾。\"\n  resolution_round: 11\n\n- id: \"v11-R1-W2\"\n  summary: \"Taxonomy 仅 H1/H7 有 precision 验证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1]\n      note: \"其余 modes 缺独立验证。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 fix: Abstract 区分 robust vs isolated modes（commit 9dc8835）。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1: H8 只在 s42 完成审计。R2: taxonomy 有独立工具价值。两人均认为 Abstract 的 'validated across multiple seeds' 对 H8 不准确。\"\n\n- id: \"v11-R1-W5\"\n  summary: \"O(1) binary ablation ISR*≈0.007 反直觉结果未充分解释\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: []\n      note: \"Round 12 未再提及。\"\n    - round: 13\n      reviewers: []\n      note: \"Round 13 未再提及。\"\n\n- id: \"v11-R2-MR\"\n  summary: \"缺少 2025-2026 最新引用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 fix: 已加入 STaR + Cobbe（commit 9dc8835）。Lean-based RL 如空间允许后续补。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1 补 LEGO-Prover。R2 补 Llemma (Azerbayev 2024)。两人一致缺 reward hacking mitigation 文献。\"\n\n- id: \"v11-R12-PDF\"\n  summary: \"PDF 与 .tex 不一致\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"PDF 从 paper/ 重编译。\"\n  resolution_round: 11\n\n# ===== Round 12 issues =====\n\n- id: \"v12-R2-N1\"\n  summary: \"正文超出 ARR 8 页限制约 0.75 页\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"Table 2 移入 Appendix，Related Work/Discussion/Limitations 压缩。主文本完整收于第 8 页。\"\n  resolution_round: 12\n\n- id: \"v12-R2-W4\"\n  summary: \"Table 1 ISR β=0.1 ISR* 列缺失\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"Table 1 补 ISR*=0.63±.23，N-H 改用 corrected 3-seed 6%，footnote 说明。\"\n  resolution_round: 12\n\n- id: \"v12-R2-W2\"\n  summary: \"与 Kim et al. (2026) 区分需更锐利\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [2]\n      note: \"Introduction 增加 explicit 对比句（training-time vs inference-time）。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-N2 [critical]: 仅一句对比不够，需逐条比较 gaming modes、detection methods、experimental settings。R1 同意需更多对比但降为 [major]。R1 建议: 共同点 + 差异 + 互补关系三段对比。\"\n\n- id: \"v12-R1-W2\"\n  summary: \"Component-count confound deconfounding analysis 仅在 Appendix\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1]\n      note: \"R1-W2。R2 [REBUT]: 核心 claim 基于 taxonomy 而非 raw ISR。分歧记录。\"\n    - round: 13\n      reviewers: []\n      note: \"Round 13 未直接提及此 item。但 R1-W1 关于 ISR≠semantic quality 隐含相关性。\"\n\n# ===== Round 13 新 issues =====\n\n- id: \"v13-R2-N2\"\n  summary: \"与 Kim et al. (2026) 差异化不充分：仅一句区分，缺逐条对比\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-N2 [critical]。R1 [AGREE] 但建议降为 major（方法论层面不重叠）。分歧在 severity：R2 critical vs R1 major。建议: Related Work 增加专门对比段。\"\n  action_items:\n    - round: 13\n      action: \"Related Work 增加与 Kim et al. (2026) 的逐条对比：gaming modes 重叠、detection 方法差异、inference-time vs training-time\"\n      assigned_to: \"research_director\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v13-R1-W1\"\n  summary: \"ISR 与 NLI accuracy 无关 (ρ=-0.049) 但 'structural quality diagnostic' 定位可能误导\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W1 [major]。R2 [AGREE]。ISR 高不意味好推理（H7 也高），ISR 低不一定坏推理（Prolog redundancy）。'Structural integrity' ≠ 'reasoning quality'。Introduction/Abstract 的 framing 可能给读者过于正面的印象。\"\n  action_items:\n    - round: 13\n      action: \"更精确界定 ISR diagnostic 能力——是 component necessity 度量而非 reasoning quality 度量\"\n      assigned_to: \"research_director\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v13-R2-W4\"\n  summary: \"缩写和术语密度过高（~17 个缩写需同时追踪）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W4。R1 [AGREE]。建议减少 3-4 个缩写（如 S-NH 延迟引入，CI 直接写 content-independent）或加 notation summary。\"\n  action_items:\n    - round: 13\n      action: \"减少缩写使用或添加 notation summary table\"\n      assigned_to: \"research_director\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v13-R2-W5\"\n  summary: \"Table 2 混合 single-seed 和 pooled 数据，对比不公平\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W5。R1 [AGREE]。Exec 列 = s42 only vs ISR/Rnd = 5-seed pooled。建议统一为 3-seed pooled 或增加 n(seeds) 列。\"\n  action_items:\n    - round: 13\n      action: \"统一 Table 2 聚合方式或标注每列 seed 数\"\n      assigned_to: \"research_director\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v13-R2-MITIGATION\"\n  summary: \"Discussion 缺少 mitigation 策略讨论和 forward-looking analysis\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2 [major concern]: 论文只诊断不治疗。R1 部分同意，建议增加: (1) KL regularization 为何不足 (cite Kwa 2024), (2) reward ensembling 可能性, (3) component-count normalization 的 negative result (1.06×)。两人一致认为 Discussion 过于 hand-waving。\"\n  action_items:\n    - round: 13\n      action: \"Discussion 增加 mitigation analysis 段落\"\n      assigned_to: \"research_director\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v13-R1-Q4\"\n  summary: \"Prolog cross-logic 实验缺少 random control\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-Q4。R2 [AGREE]。无法区分 ISR-specific Goodhart vs generic GRPO instability under augmented reward。\"\n  action_items:\n    - round: 13\n      action: \"至少讨论此限制，理想情况下补充 Prolog random/exec-only 数据\"\n      assigned_to: \"research_director\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "solver-trace-ablation",
    "issues_yaml": "issues:\n# ===== 历史 issues (Round 0-3, 全部 resolved) =====\n- id: \"R1-W1\"\n  summary: \"统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。Fisher exact test + Wilson 95% CI 已加入。eval 集 100 例限制在 limitations.tex 讨论。\"\n  resolution_round: 2\n\n- id: \"RV-EVAL-FALLBACK\"\n  summary: \"eval_sta.py test_100.jsonl 静默 fallback 已移除\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)，无 fallback。\"\n  resolution_round: 1\n\n- id: \"RV-D060-NARRATIVE\"\n  summary: \"D060 'Goodhart instability' 叙事：77pp PR 差距在同一测试集上确认成立\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。\"\n  resolution_round: 2\n\n- id: \"RV-FIG2-STALE-SCRIPT\"\n  summary: \"figures/paper/gen_fig2.py 旧脚本数据错误\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: \"已修复。\"\n  resolution_round: 1\n\n- id: \"R1-W2\"\n  summary: \"ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。\"\n  resolution_round: 2\n\n- id: \"R2-W1\"\n  summary: \"Limitations section 格式不合规\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"独立 limitations.tex 已创建，位于 references 之前。\"\n  resolution_round: 3\n\n- id: \"R2-W2\"\n  summary: \"实验仅用单一模型 (Qwen3-4B) 和单一数据集 (FOLIO)，标题复数暗示通用性\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"标题改为单数。Qwen3-1.7B cross-scale 实验已加入。\"\n  resolution_round: 3\n\n- id: \"R1-W4\"\n  summary: \"Exec-only seed 43 使用 sampling (T=0.7) 评估而非 greedy\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"exec-only 500-step 主表仅报告 s42（†标注）。\"\n  resolution_round: 2\n\n- id: \"R1-W3\"\n  summary: \"'Solver-agnostic' 仅测 2 solver，过度声明\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"'solver-agnostic' 已从全文移除。\"\n  resolution_round: 2\n\n- id: \"R2-W6\"\n  summary: \"SFT baseline 比较不公平：PR=14% vs 93%，低 PR 本身减少 hacking 机会\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"100-step RL 对照已加入。claim 调整为 'consistent with'。\"\n  resolution_round: 2\n\n- id: \"R2-W7\"\n  summary: \"与 Kim et al. (2026) 差异化不充分\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: \"related_work.tex 中有区分段落。\"\n  resolution_round: 2\n\n- id: \"R1-W6\"\n  summary: \"训练 500 例/评估 100 例的规模限制讨论不充分\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"limitations.tex 已讨论。\"\n  resolution_round: 2\n\n- id: \"R1-W7\"\n  summary: \"H1/H7 classifier precision/recall 未报告\"\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"50 样本人工验证 precision >95%。\"\n  resolution_round: 2\n\n- id: \"R1-W8\"\n  summary: \"Random control U(0,1) 与 ISR 的 skewed 分布不匹配\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"method.tex 和 experiments.tex 均说明了 Random 设计目的。\"\n  resolution_round: 2\n\n- id: \"R1-W9\"\n  summary: \"缺代码/数据开源承诺\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"abstract.tex:9 脚注 'Code and data: [anonymized]'。\"\n  resolution_round: 2\n\n- id: \"R1-W5\"\n  summary: \"'Meta-level Goodhart' 新颖性论证不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"framing 降级为 empirical instance。\"\n  resolution_round: 3\n\n- id: \"R2-W8\"\n  summary: \"H1/H7 编号不连贯（H2-H6 不存在）\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"method.tex 解释了合并原因。\"\n  resolution_round: 3\n\n- id: \"v2-R1-N1\"\n  summary: \"Abstract '93%' PR 为 single seed，应改为 mean±std\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Abstract 使用 3-seed pooled mean±std。\"\n  resolution_round: 3\n\n- id: \"v2-R1-N3\"\n  summary: \"仅 2 个 β 值不足以刻画 dose-response\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"4 个 β 值提供完整 dose-response 曲线。\"\n  resolution_round: 4\n\n- id: \"v2-R2-N3\"\n  summary: \"STA 方法论新颖性有限\"\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"novelty 定位为 applying standard LOO。\"\n  resolution_round: 3\n\n- id: \"v2-R2-N2\"\n  summary: \"单模型+单数据集泛化性不足\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"cross-scale 实验加入。单数据集限制在 Limitations 讨论。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W3\"\n  summary: \"ISR-as-reward 控制 confound 后净效果仅 1.06×\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"ISR 定位从 training signal 转为 diagnostic-only。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W6\"\n  summary: \"Hacking taxonomy 缺乏 IAA 验证\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"deterministic rules + 50-sample precision check。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W3\"\n  summary: \"Abstract 信息密度过高\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"Abstract 重写为 ~170 words。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W4\"\n  summary: \"Premise-count confound 讨论放在 Appendix 而非正文\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"提升到正文 §3.2。\"\n  resolution_round: 3\n\n- id: \"v2-R2-W5\"\n  summary: \"C2 和 C4 独立性不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"taxonomy 独立性论证成立。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-1\"\n  summary: \"Limitations section 位于 References 之后\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"顺序已正确。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-2\"\n  summary: \"Ethics Statement 缺失\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"ethics.tex 加入。\"\n  resolution_round: 3\n\n- id: \"v2-FMT-3\"\n  summary: \"Orphan bibliography entries\"\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"orphan entries 清除。\"\n  resolution_round: 3\n\n- id: \"v2-R1-M4\"\n  summary: \"Prolog cross-logic transfer 样本量过小\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"'universal Goodhart' 移除，改为 qualitative observation。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W1\"\n  summary: \"3 seeds 统计效力不足以支撑定量 claims\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"统计方法改进。定量 claims 降级。\"\n  resolution_round: 3\n\n- id: \"v2-R1-W4\"\n  summary: \"SFT baseline 比较因 PR 悬殊说服力有限\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"100-step RL 对照充分利用。\"\n  resolution_round: 3\n\n- id: \"R2-MISSING-REF\"\n  summary: \"引用覆盖不足\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: \"31 条引用覆盖核心领域。\"\n  resolution_round: 3\n\n- id: \"v3-R1-NI-2\"\n  summary: \"β=0.2 未在 Table 1 中独立报告\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Table 1 现已包含 β=0.2 行。\"\n  resolution_round: 4\n\n- id: \"v3-R1-NI-3\"\n  summary: \"§4.2 cross-seed 描述暗示最终状态\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"现标注 '(at 500 steps)'。\"\n  resolution_round: 4\n\n- id: \"v3-R12-NI-4\"\n  summary: \"全文 em-dash AI 写作痕迹\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: \"em-dash=0, -ing endings 仅 4 处轻微, blacklisted words=0。\"\n  resolution_round: 5\n\n- id: \"v3-R2-NI-5\"\n  summary: \"Abstract 'zero structurally sound outputs' 与 N-H=8% 矛盾\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Abstract 现用 'effectively zero...at convergence'。\"\n  resolution_round: 4\n\n# ===== Round 4+ carry-over =====\n\n- id: \"v3-R12-NI-1\"\n  summary: \"Cross-scale 实验 seed 数量不足\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 13\n  mentions:\n    - round: 3\n      reviewers: [1, 2]\n      note: \"两位 reviewer 一致。\"\n    - round: 10\n      reviewers: [1, 2]\n      note: \"现已用 D129 完整 3-seed 数据重写 §4.5。\"\n    - round: 11\n      reviewers: [1]\n      note: \"R1-W4: 3 seeds 仍不足以作为独立 contribution 支撑。D134 扩展至 10 seeds 正在训练中。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-N1 再次要求增加模型/数据集多样性。R2-N3 将 C3 cross-logic 定为 preliminary 不应为正式 contribution。两人一致建议降级 C3。R12 fix: C3 弱化为 'evidence of generality'（commit 9dc8835）。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R13 R2-W1: C3 仍在同一 dataset (FOLIO) 和 model family (Qwen3) 内。两位 reviewer 一致要求进一步 hedge C3 措辞。\"\n\n- id: \"v4-R12-N2\"\n  summary: \"'Inevitable collapse at all doses' claim 超出证据\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 13\n  mentions:\n    - round: 9\n      reviewers: [1, 2]\n      note: \"共识: 区分 'observed in all seeds tested' vs 'population-level inference'。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"术语降级为 'seed-dependent divergence' 和 'dose-varying patterns'。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-W3 再次指出稀疏。R1 交叉回应认为 'all tested doses show Goodhart collapse' 成立。R12 fix: 加强 preliminary 标注，区分 500-step snapshot vs trajectory（commit 9dc8835）。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-N3 认为 Abstract/Discussion 仍需更多 hedging。R2 反驳称 structural argument (H7 恒定 ISR≥0.5) 使 'at every tested dose' 成立。分歧记录。\"\n\n- id: \"v4-R12-N3\"\n  summary: \"OR=3.48 (uncorrected) vs OR=0.61 (corrected) 方向反转\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 13\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Table 1 和 Discussion §5 仍以 23% (uncorrected) 为 headline。\"\n    - round: 11\n      reviewers: [1, 2]\n      note: \"OR 反转仍是核心问题。降级为 major。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-N2 + R2-N2 [critical]。Seed-level p=0.26，corrected OR=0.61。R12 fix: transient window 降级为 descriptive observation，Table 1 N-H 改用 corrected 6%，论文最强 claim 锚定为 'Goodhart collapse at every dose'（commit 9dc8835）。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"Table 1 现用 corrected 6%†，但 footnote 同时给出 uncorrected 23%。R2 指出 non-hacking permutation p=0.917 且 point estimate ISR(2.3%) < Random(5.9%) 方向反转。两位 reviewer 一致认为 transient window 不构成 ISR 优势证据。\"\n\n- id: \"v4-R12-W6\"\n  summary: \"Seed 43 exec-only 评估协议矛盾\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 13\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Appendix Table 5 s43-500 Notes 列已修正。\"\n    - round: 12\n      reviewers: []\n      note: \"Round 12 未提及。Appendix 中已有 † 标注。\"\n    - round: 13\n      reviewers: [1]\n      note: \"R1-W4 [minor]: s43 数据仍在 cross-seed 比较中出现（§4.1），建议正文加脚注。\"\n\n- id: \"v4-R12-W7\"\n  summary: \"Deleted checkpoints (ISR β=0.1 s43/s44) 导致 H8 audit 不完整\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"'All N-H rates are upper bounds' 声明已加入 method.tex。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-N3 [critical]: 5-seed N-H=23% 为 uncorrected upper bound。R12 fix: Table 1 改用 corrected 3-seed 6%，footnote 说明（commit 9dc8835）。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W5 [minor]: Table 1 脚注存在但不够醒目。R2-W6: N-H% 列建议标注 '(upper bound)'。两位 reviewer 一致。\"\n\n- id: \"v4-R1-W8\"\n  summary: \"100 eval samples 对 per-seed claims 统计功效不足\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-W5 + R2 [AGREE with nuance]。建议报告 Wilson CI。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-N2 [critical]: 5-seed pooled N-H 23% vs 3-seed corrected 6% 差 17pp；matched cohort non-hacking permutation p=0.917 因 n=5 power 不足无法检测效应。R2 补充: ISR s45 n=42 的 54.8% N-H 实际只有 ~23 samples。两人一致建议扩大 eval set 或附 CIs。\"\n\n- id: \"v4-R2-W9\"\n  summary: \"方法新颖性有限：Algorithm 1 仅 6 行伪代码\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"共识: Findings 级别。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1 Excitement 3/5, R2 2.5/5。两人均同意 Findings。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-N1 [critical]: LOO+Goodhart 均为已知。R1 部分同意但认为 empirical contributions 有增量价值（seed-dependent divergence, H7b triple gaming, cross-logic diversity）。R1 Excitement 3.0 vs R2 2.5。分歧但共识区间 Findings-Borderline Conference。\"\n\n- id: \"v4-R2-W5\"\n  summary: \"未测试 tautology-guarded ISR 变体\"\n  category: method\n  severity: warning\n  status: wont_fix\n  first_raised_round: 4\n  last_seen_round: 4\n  resolution: \"Future work. Arms-race evidence 已有。\"\n  resolution_round: 4\n\n- id: \"v5-R1-N3\"\n  summary: \"Table 1 比较框架不对称\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 13\n  mentions:\n    - round: 10\n      reviewers: [1, 2]\n      note: \"Table 1 已拆分为 primary + cross-scale。\"\n    - round: 11\n      reviewers: []\n      note: \"未直接提及。\"\n    - round: 13\n      reviewers: [1]\n      note: \"R1 Detailed Comments: Table 1 混合 500-step 和 1000-step 结果需更清楚标注。\"\n\n- id: \"v5-R2-N3\"\n  summary: \"'Diagnostic becomes optimization target' 概念新颖性有限\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R2-N2 [critical]。R1 认为 empirical phenomena 有独立价值但同意 Findings。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1 Excitement 3/5 vs R2 2.5/5。两人均同意 Findings。结构性问题。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"同上。R2 进一步论证: ISR 的不对称性原因 'too straightforward'（LOO 偏好低 component count，H7 是全局最优 exploit）。结构性问题，无法通过修改解决。\"\n\n- id: \"v5-R2-W1\"\n  summary: \"Abstract 数据堆砌 / 单 seed 数据选择性报告\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R11 fix: 数字减至 ≤3 个 headline figures。\"\n    - round: 12\n      reviewers: []\n      note: \"R12 未再提及 Abstract 数据堆砌（质量重写后改善）。但 R12 建议术语密度可进一步降低。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W3: Abstract '99.5% structural collapse' 来自 s42 单 seed 100→1000 步轨迹，有 cherry-picking 嫌疑。R1 交叉时 [AGREE]，建议改为 3-seed aggregate (ISR*=0.03±0.05)。两人一致。\"\n\n- id: \"v5-R2-W3\"\n  summary: \"paragraph{} 过度碎片化\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 12\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"method/conclusion/limitations 仍有多个 paragraph{}。\"\n    - round: 12\n      reviewers: []\n      note: \"R12 未再提及 paragraph{} 问题（质量重写后已大幅改善）。\"\n    - round: 13\n      reviewers: []\n      note: \"R13 未提及。可能已修复，待确认。\"\n\n- id: \"v5-R2-W4\"\n  summary: \"Experiments §4.3 按 β 值呈现顺序非升序\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 10\n  resolution: \"§4.3 已按升序呈现。\"\n  resolution_round: 10\n\n- id: \"v5-R12-SFT-PR\"\n  summary: \"SFT baseline PR confound (PR=13% vs 93%)\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"SFT caveat 加入。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-W1 + R2-W1。R12 fix: Abstract 加 'though the large prove-rate gap prevents definitive causal attribution'。Limitations 加 SFT best-of-N open question（commit 9dc8835）。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-N1 [critical]: RL-specificity claim 依赖此对比但证据基础薄弱。SFT n=39，100-step checkpoint 仅 s42 (n=32)。R2-W2 [major] 完全同意。两位 reviewer 一致要求进一步降低 RL-specificity claim 强度。\"\n\n- id: \"v5-R2-MR\"\n  summary: \"缺少重要引用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"已加入 Cao et al. 2026 + Wang et al. 2025。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 建议补充 STaR + Cobbe + Lean-based RL。R12 fix: 已加入 STaR (Zelikman 2022) + Cobbe (2021)（commit 9dc8835）。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1: 补 LEGO-Prover, formal verification reward design。R2: 补 Lean-based RL (Llemma), reward hacking mitigation 策略, RLVR 其他工作。两人一致缺 mitigation literature 引用。\"\n\n- id: \"v5-R2-W6\"\n  summary: \"Table 1 信息密度过高\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 10\n  resolution: \"已拆分为 Table 1 + Table 2。R12: Table 2 移入 Appendix 节省空间。\"\n  resolution_round: 12\n\n- id: \"v5-R1-W5\"\n  summary: \"Goodhart taxonomy variant 未指定\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  resolution: \"related_work.tex 指定 'primarily regressional, with extremal elements'。\"\n  resolution_round: 7\n\n- id: \"v5-R1-W6\"\n  summary: \"ISR reward landscape 几何结构未分析\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  resolution: \"experiments.tex 包含 reward landscape 分析。\"\n  resolution_round: 7\n\n- id: \"v6-R2-N1\"\n  summary: \"ISR 核心指标命名不一致\"\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"全文统一使用 Irreducible Solver Rate。\"\n  resolution_round: 7\n\n- id: \"v6-R2-W5\"\n  summary: \"ISR 名称含 'Reward' 具有误导性\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"ISR 统一为 'Irreducible Solver Rate'。\"\n  resolution_round: 7\n\n- id: \"v6-R1-W2\"\n  summary: \"Dose-response claim 统计上不足\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1]\n      note: \"整体统计 power 批评。\"\n    - round: 12\n      reviewers: [1]\n      note: \"R1-W3: 4β×3-5seeds 仍稀疏。R12 fix: 加强 preliminary 标注（commit 9dc8835）。D134 扩展 β=0.1 到 10 seeds。\"\n    - round: 13\n      reviewers: [1]\n      note: \"R1-N3: 4 个 dose 各只 3-5 seeds，dynamics 定性各异但统一称 'Goodhart collapse'。R2 反驳称 structural argument 足够。分歧记录。\"\n\n- id: \"v6-R2-W2\"\n  summary: \"§4.3 的 β 值呈现顺序非升序\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 10\n  resolution: \"已按升序呈现。\"\n  resolution_round: 10\n\n- id: \"v6-R2-W6-LOO\"\n  summary: \"LOO 缩写未在首次使用时正式定义\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"introduction.tex 现有完整定义。\"\n  resolution_round: 7\n\n- id: \"v6-R2-W8\"\n  summary: \"Hacking taxonomy 分类标准不够 principled\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1]\n      note: \"仅 H1/H7 有 precision 验证。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1-W4 + R2-W3: robust vs isolated 应在 Abstract 区分。R12 fix: Abstract 改为 'three robust modes (H1/H7/H8) + additional isolated observations'（commit 9dc8835）。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1: H8 只在 s42 完成审计，'validated across multiple seeds' 对 H8 是否准确？R2: taxonomy 有独立工具价值但仅 H1/H7 有 precision 验证。\"\n\n- id: \"v7-R1-N2\"\n  summary: \"CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: \"CMH 移至 Appendix，正文以 seed-level permutation p=0.26 为 primary。\"\n  resolution_round: 9\n\n- id: \"v7-R2-MR1\"\n  summary: \"缺少 Goodhart's Law 经典引用\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  resolution: \"references.bib 包含 Goodhart 1975。\"\n  resolution_round: 8\n\n- id: \"v7-R2-W7\"\n  summary: \"experiments.tex 'Notably' AI 写作标记\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: \"'Notably' 已移除。\"\n  resolution_round: 9\n\n- id: \"v8-R12-N1\"\n  summary: \"Goodhart 发现的可预测性限制概念新颖性\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"R2-N2 [critical]。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R1 Excitement 3/5 认为 empirical details 超出可预测范围，R2 2.5/5。两人均同意 Findings。结构性问题。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-N1 [critical]: H7 的 ISR≥0.5 是数学必然，不需实验确认。R1 部分同意但认为 dynamics 细节有价值。结构性问题：核心发现的可预测性是概念层面的限制，无法通过写作修改解决。\"\n\n- id: \"v8-R1-N3\"\n  summary: \"术语交替使用导致语义滑移\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"Fig 2/3 'Genuine' → 'Non-hacking' 已修复。偶见残留。\"\n    - round: 12\n      reviewers: []\n      note: \"R12 未再提及术语滑移。\"\n    - round: 13\n      reviewers: []\n      note: \"R13 未再提及术语滑移。可能已修复，待确认。\"\n\n- id: \"v8-R12-N2\"\n  summary: \"实验范围与标题/claim scope 不匹配\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Subtitle 改为 'GRPO-Trained FOL Reasoners'。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R2-N3 [critical]: 仍暗示通用结论。R12 fix: C3 弱化为 'evidence of generality'，Contributions 加 'from a single model family and dataset'（commit 9dc8835）。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W1: C3 仍在同一 dataset 和 model family 内。Discussion line 11 'STA applies to any compositional-input/binary-verifier setting' 缺乏验证。两人一致认为泛化性 claim 仍需进一步 hedge。\"\n\n- id: \"v8-R1-W4\"\n  summary: \"多重比较未校正\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1]\n      note: \"limitations.tex 新增 'Multiple comparisons' 段落。\"\n    - round: 12\n      reviewers: []\n      note: \"R12 未再单独提及。\"\n    - round: 13\n      reviewers: [1]\n      note: \"R1-W3: CMH independence violation 仍需更清晰标注为 'directional only'。R2 AGREE。\"\n\n- id: \"v8-R1-MR\"\n  summary: \"缺少 reward shaping 和 inference-time hacking 引用\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: \"Uesato 2022, Paulus 2018, Langosco 2022 等已补充。\"\n  resolution_round: 10\n\n- id: \"v9-R1-N3\"\n  summary: \"Premise-count confound 影响范围分歧\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"method.tex 增加 confound 两场景区分句。\"\n  resolution_round: 9\n\n- id: \"v9-R12-W1\"\n  summary: \"§4.4 标题措辞过强\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"§4.4 标题改为 'Cross-Logic Extension'。\"\n  resolution_round: 9\n\n- id: \"v9-R1-W5\"\n  summary: \"训练时 sampling vs 评估时 greedy 不一致\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"§4.1 已增加讨论。\"\n  resolution_round: 9\n\n- id: \"v9-R12-Q-ISR-FILTER\"\n  summary: \"ISR 作为 filter 未测试\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"conclusion.tex 增加 'ISR as post-hoc filter' 作为 future work。\"\n  resolution_round: 9\n\n- id: \"v9-R12-Q-NORMALIZED-ISR\"\n  summary: \"未测试 premise-count-normalized ISR\"\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"conclusion.tex 增加 'normalized variants' 作为 future work。\"\n  resolution_round: 9\n\n- id: \"v4-RV-STALE-APPENDIX\"\n  summary: \"Appendix Table 仍用旧数据\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 7\n  resolution: \"Appendix Table 5 现含完整 per-seed data。\"\n  resolution_round: 7\n\n# ===== Round 10 issues =====\n\n- id: \"v10-R12-N1\"\n  summary: \"§4.5 与 Limitations 关于 1.7B seed 数量矛盾\"\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  resolution: \"D129 完整 3-seed 数据重写 §4.5。\"\n  resolution_round: 11\n\n- id: \"v10-R2-Q6\"\n  summary: \"ISR=0.75 推导与实测不一致\"\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  resolution: \"改为 ISR≥0.5。PDF 已重编译。\"\n  resolution_round: 11\n\n- id: \"v10-R2-W7\"\n  summary: \"'Valid but Vacuous' 中 'valid' 有歧义\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [2]\n      note: \"建议改为 'Verified but Vacuous'。保留原标题决策。\"\n    - round: 12\n      reviewers: []\n      note: \"Round 12 未再提及。\"\n    - round: 13\n      reviewers: []\n      note: \"Round 13 未再提及。可能不再是活跃问题。\"\n\n- id: \"v10-R2-W8\"\n  summary: \"Discussion/Conclusion 过于简短\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1, 2]\n      note: \"Discussion 扩展到 ~33 行。\"\n    - round: 12\n      reviewers: []\n      note: \"R12 未批评长度。P0 压缩后约 11 行但内容更密集。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2: Discussion 缺 forward-looking content（mitigation 方向）。R1 部分同意，建议增加 mitigation 困难性分析段落。\"\n\n- id: \"v10-R2-W5\"\n  summary: \"C2 和 C4 边界不清晰\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: \"Contributions 合并为 3 条。\"\n  resolution_round: 10\n\n# ===== Round 11 issues =====\n\n- id: \"v11-R12-N1\"\n  summary: \"Responsible NLP Research Checklist 缺失\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"checklist.tex 创建并附在论文末尾。\"\n  resolution_round: 11\n\n- id: \"v11-R1-W2\"\n  summary: \"Taxonomy 仅 H1/H7 有 precision 验证\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 11\n      reviewers: [1]\n      note: \"其余 modes 缺独立验证。\"\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 fix: Abstract 区分 robust vs isolated modes（commit 9dc8835）。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1: H8 只在 s42 完成审计。R2: taxonomy 有独立工具价值。两人均认为 Abstract 的 'validated across multiple seeds' 对 H8 不准确。\"\n\n- id: \"v11-R1-W5\"\n  summary: \"O(1) binary ablation ISR*≈0.007 反直觉结果未充分解释\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: []\n      note: \"Round 12 未再提及。\"\n    - round: 13\n      reviewers: []\n      note: \"Round 13 未再提及。\"\n\n- id: \"v11-R2-MR\"\n  summary: \"缺少 2025-2026 最新引用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1, 2]\n      note: \"R12 fix: 已加入 STaR + Cobbe（commit 9dc8835）。Lean-based RL 如空间允许后续补。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1 补 LEGO-Prover。R2 补 Llemma (Azerbayev 2024)。两人一致缺 reward hacking mitigation 文献。\"\n\n- id: \"v11-R12-PDF\"\n  summary: \"PDF 与 .tex 不一致\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: \"PDF 从 paper/ 重编译。\"\n  resolution_round: 11\n\n# ===== Round 12 issues =====\n\n- id: \"v12-R2-N1\"\n  summary: \"正文超出 ARR 8 页限制约 0.75 页\"\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"Table 2 移入 Appendix，Related Work/Discussion/Limitations 压缩。主文本完整收于第 8 页。\"\n  resolution_round: 12\n\n- id: \"v12-R2-W4\"\n  summary: \"Table 1 ISR β=0.1 ISR* 列缺失\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: \"Table 1 补 ISR*=0.63±.23，N-H 改用 corrected 3-seed 6%，footnote 说明。\"\n  resolution_round: 12\n\n- id: \"v12-R2-W2\"\n  summary: \"与 Kim et al. (2026) 区分需更锐利\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [2]\n      note: \"Introduction 增加 explicit 对比句（training-time vs inference-time）。\"\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-N2 [critical]: 仅一句对比不够，需逐条比较 gaming modes、detection methods、experimental settings。R1 同意需更多对比但降为 [major]。R1 建议: 共同点 + 差异 + 互补关系三段对比。\"\n\n- id: \"v12-R1-W2\"\n  summary: \"Component-count confound deconfounding analysis 仅在 Appendix\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n    - round: 12\n      reviewers: [1]\n      note: \"R1-W2。R2 [REBUT]: 核心 claim 基于 taxonomy 而非 raw ISR。分歧记录。\"\n    - round: 13\n      reviewers: []\n      note: \"Round 13 未直接提及此 item。但 R1-W1 关于 ISR≠semantic quality 隐含相关性。\"\n\n# ===== Round 13 新 issues =====\n\n- id: \"v13-R2-N2\"\n  summary: \"与 Kim et al. (2026) 差异化不充分：仅一句区分，缺逐条对比\"\n  category: writing\n  severity: critical\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-N2 [critical]。R1 [AGREE] 但建议降为 major（方法论层面不重叠）。分歧在 severity：R2 critical vs R1 major。建议: Related Work 增加专门对比段。\"\n  action_items:\n    - round: 13\n      action: \"Related Work 增加与 Kim et al. (2026) 的逐条对比：gaming modes 重叠、detection 方法差异、inference-time vs training-time\"\n      assigned_to: \"research_director\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v13-R1-W1\"\n  summary: \"ISR 与 NLI accuracy 无关 (ρ=-0.049) 但 'structural quality diagnostic' 定位可能误导\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-W1 [major]。R2 [AGREE]。ISR 高不意味好推理（H7 也高），ISR 低不一定坏推理（Prolog redundancy）。'Structural integrity' ≠ 'reasoning quality'。Introduction/Abstract 的 framing 可能给读者过于正面的印象。\"\n  action_items:\n    - round: 13\n      action: \"更精确界定 ISR diagnostic 能力——是 component necessity 度量而非 reasoning quality 度量\"\n      assigned_to: \"research_director\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v13-R2-W4\"\n  summary: \"缩写和术语密度过高（~17 个缩写需同时追踪）\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W4。R1 [AGREE]。建议减少 3-4 个缩写（如 S-NH 延迟引入，CI 直接写 content-independent）或加 notation summary。\"\n  action_items:\n    - round: 13\n      action: \"减少缩写使用或添加 notation summary table\"\n      assigned_to: \"research_director\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v13-R2-W5\"\n  summary: \"Table 2 混合 single-seed 和 pooled 数据，对比不公平\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2-W5。R1 [AGREE]。Exec 列 = s42 only vs ISR/Rnd = 5-seed pooled。建议统一为 3-seed pooled 或增加 n(seeds) 列。\"\n  action_items:\n    - round: 13\n      action: \"统一 Table 2 聚合方式或标注每列 seed 数\"\n      assigned_to: \"research_director\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v13-R2-MITIGATION\"\n  summary: \"Discussion 缺少 mitigation 策略讨论和 forward-looking analysis\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R2 [major concern]: 论文只诊断不治疗。R1 部分同意，建议增加: (1) KL regularization 为何不足 (cite Kwa 2024), (2) reward ensembling 可能性, (3) component-count normalization 的 negative result (1.06×)。两人一致认为 Discussion 过于 hand-waving。\"\n  action_items:\n    - round: 13\n      action: \"Discussion 增加 mitigation analysis 段落\"\n      assigned_to: \"research_director\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: \"v13-R1-Q4\"\n  summary: \"Prolog cross-logic 实验缺少 random control\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 13\n  last_seen_round: 13\n  mentions:\n    - round: 13\n      reviewers: [1, 2]\n      note: \"R1-Q4。R2 [AGREE]。无法区分 ISR-specific Goodhart vs generic GRPO instability under augmented reward。\"\n  action_items:\n    - round: 13\n      action: \"至少讨论此限制，理想情况下补充 Prolog random/exec-only 数据\"\n      assigned_to: \"research_director\"\n      status: open\n  resolution: \"\"\n  resolution_round: null\n"
  }
}
```

</details>

---


### Tool result

_source line 1265 · 2026-05-19T02:56:15.082226+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml\", \"bytes\": 33226}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1266 · 2026-05-19T02:59:01.864783+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 合并审稿报告 — Round 13 (Fresh Review)\n\n**论文**: \"Valid but Vacuous: Reward Hacking in GRPO-Trained FOL Reasoners\"\n**目标 Venue**: ACL ARR May 2026 → EMNLP 2026 commitment (Long Paper)\n**Reviewer 编排**: 2 人（R1: 方法/实验/统计, R2: 新颖性/写作/格式）\n**审稿模式**: Fresh（重新审稿，无历史记忆）\n**轮次**: Round 1 初审 + Step 2 交叉回应，共识达成，无需第二轮\n\n---\n\n## Summary\n\n本文提出 Solver Trace Ablation (STA)，基于 leave-one-out (LOO) 消融的结构完整性诊断方法，用于检测 GRPO 训练的形式化推理器中的 reward hacking。核心指标 ISR 作为诊断工具时揭示 prove rate 背后的结构退化（exec-only 3-seed 1000-step ISR*=0.03±0.05 while PR=97±2%）；但作为训练 reward 时在所有 4 个测试剂量下出现 Goodhart collapse（matched 5+5 cohort: ISR 5/5 H7-dominated vs Random 0/5, Fisher p=0.004, BF₁₀=77）。实验覆盖 6 种 reward 条件、2 种逻辑类型（FOL/Prolog）、2 种模型规模（Qwen3-4B/1.7B），建立了 9 种 hacking 模式的分类体系。\n\n---\n\n## Strengths\n\n**S1. [共识] 研究问题重要且时机恰当。** Solver-backed RL 中 prove rate 作为唯一指标的盲点是真实且被低估的问题。ISR 的 diagnostic-vs-optimizer 不对称性发现对 RL-for-reasoning 社区有直接实践价值。\n\n**S2. [共识] 实验设计严谨，含 matched replication。** 5+5 matched cohort design（exploratory seeds 42-46 + replication seeds 47-51）超出同类工作标准。Fisher exact test (p=0.004, BF₁₀=77) 为 H7 dominance 提供较强证据。多重统计检验（Fisher, Mann-Whitney, permutation, Bayes factor）体现了审慎的实验学纪律。\n\n**S3. [共识] Goodhart 机制分析清晰。** H7 tautology（单前提=结论 → ISR≥0.5 by construction → positive feedback loop → absorbing state）的因果链条完整。β 控制 collapse timing 而非 whether，这一结论有理论支撑。\n\n**S4. [共识] 限制条件报告异常透明。** 丢失 checkpoints、s43 sampling evaluation 协议违规、CMH p-value inflation、non-hacking 作为上界、SFT comparison confound——均在 Limitations 和 Appendix 中坦诚讨论。这种透明度在投稿论文中罕见。\n\n**S5. [共识] Hacking taxonomy 有独立工具价值。** 9 种模式（8 自动 + 1 手动）的分类体系，特别是 H7b triple gaming 和 query-as-fact gaming，具体且可复现，可被其他 solver-backed 系统直接采用。\n\n**S6. [共识] 写作质量高、格式完全合规。** 无 em-dash，无 AI 写作黑名单词汇，段落长度合理，叙事线连贯。格式完全符合 ACL ARR 要求（≤8 页, [review] option, 匿名化, Limitations, Ethics, Checklist）。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W-C1. [共识, critical] SFT baseline comparison 存在严重混淆因素，论文叙事依赖过高**\n- SFT PR=13% vs exec-only PR=93-98%，差距 ~80pp。100-step checkpoint (PR=32%, hacking≥31%) 仅部分控制，且只有 s42 一个 seed (n=32)。SFT 仅 39 proved samples (3-seed pooled)。\n- 论文第一条 contribution 和 \"RL-specific failure\" 核心叙事均依赖此对比。Abstract line 4 和 Introduction line 14 的 \"consistent with it being RL-specific\" 措辞可能让读者高估证据强度。\n- 建议：进一步降低 RL-specificity claim 强度；将 SFT 对比重新定位为 \"diagnostic validation\" 而非因果归因。\n\n**W-C2. [共识, critical] 100-example evaluation set 统计功效严重不足**\n- 许多 seed 的 proved count 远低于 100（ISR β=0.1 s45: n=42, Random s49 matched: n=5）。\n- 5-seed pooled N-H 23% vs 3-seed corrected 6%，差 17pp，同一数据在不同 pooling 下结论几乎反转（Fisher p 从 <10⁻⁸ 变为 0.182 n.s.）。\n- Matched cohort non-hacking permutation test p=0.917：n=5 per group 无法检测合理效应量。且 point estimate 方向反转（ISR 2.3% < Random 5.9%）——ISR 作为 reward 可能连 non-hacking quality 都不如 random noise。\n- 建议：扩大 eval set 至 500+ examples；所有 per-seed 报告附 Wilson CIs。\n\n**W-C3. [共识, critical] 方法新颖性有限——LOO ablation 是标准技术，Goodhart collapse 是理论可预测结果**\n- LOO ablation 源自 mutation testing（论文 §3.2 明确承认 \"LOO ablation itself is standard\"）。\n- H7 tautology 的 ISR≥0.5 是 LOO 定义的数学必然（§3.2 line 57），Goodhart collapse 是可预测推论。\n- Discussion line 7 承认 \"collapse under LOO-based metrics is theoretically predictable\"。\n- 贡献主要是 \"applying known technique to new domain + confirming known theory + descriptive taxonomy\"。\n- R1 认为 empirical dynamics 细节（seed-dependent divergence, H7b triple gaming, cross-logic mode diversity）有增量价值；R2 认为这些是 \"empirically interesting but conceptually expected\"。两人共识：这是 Findings 级别贡献，低于 EMNLP 主会议的 novelty 门槛。\n\n**W-C4. [R2 critical / R1 major] 与 Kim et al. (2026) \"Do LLMs Game Formalization?\" 差异化不充分**\n- Related Work §2 仅用一个从句区分（\"gaming emerges during training rather than at inference\"）。\n- 缺少 gaming 模式分类对比、detection 方法对比、experimental setting 差异的详细讨论。\n- R1 认为两篇方法论层面不重叠，补充一段对比即可（降为 major）；R2 认为 gaming pattern 可能有重叠，差异化不充分构成 critical concern。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W-M1. [共识, major] Abstract \"99.5% structural collapse\" 来自单 seed (s42) 单轨迹，有 cherry-picking 嫌疑**\n- 99.5% collapse（ISR 0.642→0.003）是 s42 从 100→1000 步的数据。s44 走了 tautological collapse 路线（ISR 高是假象），s43 有 sampling eval 协议问题无法计算 trajectory。\n- 建议改为 3-seed 1000-step aggregate：\"ISR* collapses to near-zero (0.03±0.05) across three seeds\"。\n\n**W-M2. [共识, major] ISR 与 NLI accuracy 完全无关 (ρ=-0.049, p=0.187) 但定位为 \"structural quality diagnostic\" 可能误导**\n- ISR 低 → H1 redundancy；ISR 高（优化下）→ H7 gaming。两种情况 ISR 都不直接度量推理质量。\n- Introduction/Abstract 中 \"structural quality\" 和 \"structural integrity\" 措辞可能给读者过于正面的印象。\n- 建议更精确框定 ISR 的诊断能力：component necessity 度量，非 reasoning quality 度量。\n\n**W-M3. [共识, major] 单数据集 + 单模型族限制泛化性**\n- 全部实验基于 FOLIO + Qwen3。C3 声称 \"not specific to a single logic type or model scale\" 但仍在同一 dataset 和 model family 内。\n- Discussion line 11 \"STA applies to any compositional-input/binary-verifier setting\" 缺乏验证。\n\n**W-M4. [共识, major] Discussion 缺 mitigation 策略和 forward-looking analysis**\n- 论文只诊断不治疗。Discussion 仅一句 hand-waving（\"combining with effort-based detection\"）。\n- 建议增加分析：KL regularization 为何不足、reward ensembling 可能性、component-count normalization 的 negative result (1.06×)。\n\n**W-M5. [R1 major, R2 REBUT] Random control 产生 29.5% H7（5-seed pooled），可能削弱 ISR-specific 归因**\n- Exploratory cohort: Random H7 29.5% (dominated by s46 91.5%, s43 38.3%)；Matched cohort: Random H7 6.7%, 0/5 H7-dominated。\n- R2 反驳：matched cohort (0/5 vs 5/5, p=0.004) 是 clean evidence，exploratory cohort 的 pooled rate 掩盖 seed dependence。R1 concern 主要针对 exploratory cohort。\n- 分歧记录。Matched cohort 证据更可靠。\n\n### Minor Issues\n\n**W-m1. [共识] 缩写和术语密度过高**（~17 个缩写需同时追踪）。建议减少 3-4 个缩写或加 notation summary。\n\n**W-m2. [共识] Table 2 混合 single-seed 和 pooled 数据**（Exec=s42 only vs ISR/Rnd=5-seed pooled），对比不公平。\n\n**W-m3. [共识] Non-hacking rate 定义脆弱**，Table 1 N-H% 列建议标注 \"(upper bound)\"。\n\n**W-m4. [共识, minor] Exec-only s43 使用 sampling eval (T=0.7) 而非 greedy**，数据在 cross-seed 比较中需脚注说明。\n\n**W-m5. [共识, minor] 丢失 checkpoints (ISR β=0.1 s43/s44)** 影响 H8 审计完整性。Matched cohort 保留全部 checkpoints。\n\n**W-m6. [R1] Prolog cross-logic 实验无 random control**，无法排除 generic GRPO instability。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成一致 [AGREE]：\n\n1. **SFT baseline confound 是论文最大方法论弱点之一**。RL-specificity claim 证据基础薄弱，需进一步降低表述强度。\n2. **100-example eval set 统计功效不足**。Per-seed claims 建立在小样本之上，不同 pooling 下结论可反转。\n3. **Abstract \"99.5% collapse\" 应改为 3-seed aggregate**。\n4. **CMH p-values 应标注为 \"directional only\"**，以 seed-level Fisher exact test (p=0.004, BF₁₀=77) 为首要统计证据。\n5. **ISR ≠ semantic quality**，framing 需更精确。\n6. **Non-hacking rate 是 upper bound**，应在 Table 1 标注。\n7. **Kim et al. (2026) 需更详细对比**（severity 有分歧：R2 critical vs R1 major）。\n8. **Discussion 需增加 mitigation 讨论**。\n9. **写作质量高、格式完全合规**。\n10. **实验设计（matched 5+5 replication）超出同类工作标准**。\n\n---\n\n## Reviewer Divergence\n\n### 分歧 1: Overall 评分（R1: 3.5 Borderline Conference vs R2: 3.0 Findings）\n\n- **R1 立场**：如果解决 SFT framing 和 statistical power 讨论，empirical contributions（dynamics characterization, taxonomy, matched design 示范价值）足以达 Conference。Excitement 3/5。\n- **R2 立场**：即使完美修复 SFT 和统计问题，核心 novelty gap 无法解决——方法是标准的，发现是可预测的，没有 mitigation。EMNLP 主会议期待概念新贡献。Excitement 2.5/5。\n- **Director 判断**：R2 论证更有力。方法新颖性有限是结构性问题，不可通过写作修改解决。Empirical details 有价值但不足以弥补概念层面的 gap。合理区间 3.0-3.5，倾向 3.0。\n\n### 分歧 2: \"At every tested dose\" 表述（R1: 需更多 hedging vs R2: REBUT，结构论证足够）\n\n- **R1 立场**：4 个 β 值各 3-5 seeds，dynamics 定性各异（deterministic/stochastic/immediate/multi-modal），统一称 \"Goodhart collapse\" 可能过度简化。\n- **R2 反驳**：H7 tautology 的 ISR≥0.5 是 LOO 定义的数学性质，β-independent。Structural argument 使 \"at every tested dose\" 成立。\n- **Director 判断**：R2 反驳有理论支撑——ISR 的 Goodhart vulnerability 确实是定义层面的，不是经验巧合。但 R1 关于 dynamics 多样性（collapse occurs but varies qualitatively）的 nuance 也有价值。建议保留 \"at every tested dose\" 但在 Discussion 区分 \"collapse occurs\" vs \"collapse dynamics vary\"。\n\n### 分歧 3: Random H7 29.5% 对 ISR-specific 归因的影响\n\n- **R1 立场**：Random 也产生大量 H7，削弱因果归因。\n- **R2 反驳**：Matched cohort 0/5 vs 5/5 是 clean evidence。Exploratory cohort 的 29.5% 由 2 个 extreme seeds 主导，pooled rate 误导。ISR 将 H7 从 stochastic → irreversible attractor 的动力学区别是关键。\n- **Director 判断**：R2 反驳令人信服。Matched cohort 数据（Fisher p=0.004）比 exploratory cohort 的 pooled rate 更可靠。但论文应讨论两个 cohort 中 Random H7 率差异的含义。\n\n---\n\n## Questions（需作者澄清）\n\n**Q1.** Matched 5+5 design 是否做过 formal power analysis？如果需要检测 10pp 的 N-H rate 差异，需要多少 seeds？\n\n**Q2.** Premise-count-matched comparison 仅 1.06×（ISR*=0.258 vs 0.243）。Abstract \"any transient quality improvement disappears\" 中 \"improvement\" 是否需要修改为 \"apparent improvement\"？\n\n**Q3.** 早期 convex formulation 被放弃（ISR<1 always penalized, collapsing PR）。是否考虑过更小 β（如 0.01）来温和惩罚低 ISR？\n\n**Q4.** Cross-logic Prolog 实验无 random control。如何排除 generic GRPO instability（而非 ISR-specific）导致的 collapse？\n\n**Q5.** H9 (contradiction injection) 仅在 1.7B Random β=0.1 s42 一个 seed 观察到。\"ISR redirects hacking pathway from H9 to H1\" 基于 1 seed 的归因可信度如何？\n\n**Q6.** Component granularity 的选择（§3.2 \"what constitutes a component depends on the logic\"）是否影响 ISR？不同分解方式下 ISR 的敏感性如何？\n\n---\n\n## Missing References\n\n两位 Reviewer 一致指出以下引用缺失：\n\n1. **Lean-based RL**: Llemma (Azerbayev et al., 2024) — 与 solver-backed RL 大框架直接相关\n2. **Reward hacking mitigation 策略**: reward ensembling, constrained optimization, conservative reward — 论文讨论问题但未引用/讨论任何已知 mitigation 方向\n3. **Kim et al. (2026) 的更详细对比**: 当前仅一句区分，需逐条比较 gaming modes、detection methods、experimental settings\n4. **RLVR 框架**: Shao et al. (2025) \"Spurious Rewards\" 已引用但其 reward variance findings 与 Random control 的关系未展开讨论\n\n---\n\n## Overall Assessment\n\n### 评分\n\n| 维度 | R1 | R2 | 合并 |\n|------|-----|-----|------|\n| Soundness | 3.5 | 3.5 | **3.5** |\n| Excitement | 3.0 | 2.5 | **2.5-3.0** |\n| Novelty | — | 2.5 | **2.5** |\n| Reproducibility | 4.0 | 4.0 | **4.0** |\n| **Overall** | **3.5** | **3.0** | **3.0 (Findings)** |\n\n### Overall: 3.0 — Findings\n\n**一篇技术上 sound、实验设计 careful、限制报告异常透明的实证案例研究，但方法新颖性有限（LOO 是标准技术）、核心发现理论上可预测（Goodhart collapse 是 ISR LOO 定义的数学推论），且缺乏 mitigation 策略。适合 EMNLP Findings，但低于主会议的 novelty 和 excitement 门槛。**\n\n具体理由：\n\n1. **方法贡献有限**：STA/ISR 是标准 LOO ablation 的直接应用，Algorithm 1 仅 6 行伪代码。论文自己反复承认技术本身不新。\n2. **核心发现可预测**：H7 tautology 的 ISR≥0.5 是定义层面的必然，Goodhart collapse 不需要实验确认。虽然具体 dynamics（seed-dependent divergence, cross-logic diversity）超出简单理论预测，但这些更多是 characterization 而非 discovery。\n3. **SFT comparison confound 未解决**：RL-specificity 这一核心叙事的证据基础（PR 差距 80pp）薄弱，100-step checkpoint 仅部分控制。\n4. **统计功效受限**：100-example eval set 导致 per-seed claims 宽置信区间，不同 pooling 下结论可反转。Seed-level tests 受 n=5 power 限制。\n5. **范围窄**：单模型家族 (Qwen3)、单数据集 (FOLIO)、单 RL 算法 (GRPO)。\n6. **只诊断不治疗**：论文停留在 warning 层面，Discussion 缺乏 mitigation 分析。\n\n**提升路径**（若目标 3.5+ Borderline Conference）：\n- 补充 Kim et al. (2026) 详细对比\n- Abstract 改用 3-seed aggregate、降低 RL-specificity claim\n- Discussion 增加 mitigation 分析段落（KL failure, reward ensembling, component-count normalization negative result）\n- 所有 per-seed 报告附 Wilson CIs，正文讨论统计功效限制\n- Table 1 标注 N-H% (upper bound)，Table 2 统一聚合方式\n\n即使以上全部完成，核心 novelty gap（W-C3）仍是结构性问题，Conference 级别需要额外的概念贡献（如至少一个 mitigation 策略的 preliminary result）。\n\n### Confidence: 4/5\n\n两位 Reviewer 对 RL reward design、statistical testing、Goodhart dynamics、formal reasoning with LLMs 均有足够专业知识。技术判断一致（Soundness 3.5），分歧仅在 novelty 评估——这是 legitimate 的标准差异。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- \"99.5% structural collapse\" → 改为 3-seed aggregate (ISR*=0.03±0.05)\n- \"consistent with it being RL-specific\" → 进一步 hedge\n- \"three robust hacking modes (H1/H7/H8, validated across multiple seeds)\" — H8 只在 s42 完成审计，\"validated across multiple seeds\" 不准确\n- \"any transient quality improvement disappears\" — 1.06× 不构成 improvement，改为 \"apparent improvement\" 或 \"non-hacking window\"\n\n### Introduction\n- 叙事结构清晰（问题→不足→STA→发现→contributions），整体质量高\n- \"Process reward models require expensive annotations and do not transfer to arbitrary solver-backed settings\" — 过于绝对，最近 PRM 工作在迁移性方面有进展\n- C3 \"Cross-logic and cross-scale evidence that Goodhart vulnerability is not specific to...\" — 仍在同一 dataset 和 model family 内，需进一步 hedge\n\n### Related Work\n- 结构清晰，引用密度合理（~40 citations）\n- 与 TRACE (Wang et al. 2025) 关系说明清楚\n- **需增加 Kim et al. (2026) 专门对比段**\n- **需补充 reward hacking mitigation 和 Lean-based RL 引用**\n\n### Method\n- STA/ISR 定义清晰，Algorithm 1 简洁\n- Premise-count confound 讨论充分（§3.2 line 56-57）\n- Reward formulation 设计合理但需讨论乘法 vs 加法选择\n- Component granularity 的选择是未讨论的 degree of freedom\n\n### Experiments\n- Fig 2 collapse trajectory 是最有说服力的证据（单 seed 纵向分析避免 cross-seed 统计问题）\n- Matched 5+5 cohort design 优秀，Fisher p=0.004 是 clean evidence\n- Table 1 混合 500-step 和 1000-step 结果需更清楚标注\n- §4.3 Cross-logic 和 §4.4 Cross-scale 各仅 3 seeds 无 random control（Prolog），只能作 preliminary evidence\n- R2 重要发现：non-hacking permutation test p=0.917 且 point estimate 方向反转（ISR 2.3% < Random 5.9%）——ISR 可能在 genuine quality 上不如 random noise\n\n### Discussion and Conclusion\n- 核心 message 清晰且有实践价值\n- 需增加 mitigation analysis 段落\n- \"STA applies to any compositional-input/binary-verifier setting\" 需 hedge\n\n### Limitations\n- 异常全面和诚实——论文亮点之一\n- 建议将部分限制（100-example eval, CMH inflation）提升到正文讨论\n\n### Format Compliance\n- ✅ 正文 ≤8 页\n- ✅ `\\usepackage[review]{acl}`\n- ✅ Limitations 在 References 之前\n- ✅ Ethics Statement 存在\n- ✅ Responsible NLP Checklist 认真填写\n- ✅ 匿名化完整 (\"Anonymous ACL submission\")\n- ⚠️ Checklist C4 \"Partially\" — 建议补全 training framework 版本\n- ⚠️ Appendix 排版有空白页（p19, p21）",
  "project": "solver-trace-ablation",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 合并审稿报告 — Round 13 (Fresh Review)\n\n**论文**: \"Valid but Vacuous: Reward Hacking in GRPO-Trained FOL Reasoners\"\n**目标 Venue**: ACL ARR May 2026 → EMNLP 2026 commitment (Long Paper)\n**Reviewer 编排**: 2 人（R1: 方法/实验/统计, R2: 新颖性/写作/格式）\n**审稿模式**: Fresh（重新审稿，无历史记忆）\n**轮次**: Round 1 初审 + Step 2 交叉回应，共识达成，无需第二轮\n\n---\n\n## Summary\n\n本文提出 Solver Trace Ablation (STA)，基于 leave-one-out (LOO) 消融的结构完整性诊断方法，用于检测 GRPO 训练的形式化推理器中的 reward hacking。核心指标 ISR 作为诊断工具时揭示 prove rate 背后的结构退化（exec-only 3-seed 1000-step ISR*=0.03±0.05 while PR=97±2%）；但作为训练 reward 时在所有 4 个测试剂量下出现 Goodhart collapse（matched 5+5 cohort: ISR 5/5 H7-dominated vs Random 0/5, Fisher p=0.004, BF₁₀=77）。实验覆盖 6 种 reward 条件、2 种逻辑类型（FOL/Prolog）、2 种模型规模（Qwen3-4B/1.7B），建立了 9 种 hacking 模式的分类体系。\n\n---\n\n## Strengths\n\n**S1. [共识] 研究问题重要且时机恰当。** Solver-backed RL 中 prove rate 作为唯一指标的盲点是真实且被低估的问题。ISR 的 diagnostic-vs-optimizer 不对称性发现对 RL-for-reasoning 社区有直接实践价值。\n\n**S2. [共识] 实验设计严谨，含 matched replication。** 5+5 matched cohort design（exploratory seeds 42-46 + replication seeds 47-51）超出同类工作标准。Fisher exact test (p=0.004, BF₁₀=77) 为 H7 dominance 提供较强证据。多重统计检验（Fisher, Mann-Whitney, permutation, Bayes factor）体现了审慎的实验学纪律。\n\n**S3. [共识] Goodhart 机制分析清晰。** H7 tautology（单前提=结论 → ISR≥0.5 by construction → positive feedback loop → absorbing state）的因果链条完整。β 控制 collapse timing 而非 whether，这一结论有理论支撑。\n\n**S4. [共识] 限制条件报告异常透明。** 丢失 checkpoints、s43 sampling evaluation 协议违规、CMH p-value inflation、non-hacking 作为上界、SFT comparison confound——均在 Limitations 和 Appendix 中坦诚讨论。这种透明度在投稿论文中罕见。\n\n**S5. [共识] Hacking taxonomy 有独立工具价值。** 9 种模式（8 自动 + 1 手动）的分类体系，特别是 H7b triple gaming 和 query-as-fact gaming，具体且可复现，可被其他 solver-backed 系统直接采用。\n\n**S6. [共识] 写作质量高、格式完全合规。** 无 em-dash，无 AI 写作黑名单词汇，段落长度合理，叙事线连贯。格式完全符合 ACL ARR 要求（≤8 页, [review] option, 匿名化, Limitations, Ethics, Checklist）。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W-C1. [共识, critical] SFT baseline comparison 存在严重混淆因素，论文叙事依赖过高**\n- SFT PR=13% vs exec-only PR=93-98%，差距 ~80pp。100-step checkpoint (PR=32%, hacking≥31%) 仅部分控制，且只有 s42 一个 seed (n=32)。SFT 仅 39 proved samples (3-seed pooled)。\n- 论文第一条 contribution 和 \"RL-specific failure\" 核心叙事均依赖此对比。Abstract line 4 和 Introduction line 14 的 \"consistent with it being RL-specific\" 措辞可能让读者高估证据强度。\n- 建议：进一步降低 RL-specificity claim 强度；将 SFT 对比重新定位为 \"diagnostic validation\" 而非因果归因。\n\n**W-C2. [共识, critical] 100-example evaluation set 统计功效严重不足**\n- 许多 seed 的 proved count 远低于 100（ISR β=0.1 s45: n=42, Random s49 matched: n=5）。\n- 5-seed pooled N-H 23% vs 3-seed corrected 6%，差 17pp，同一数据在不同 pooling 下结论几乎反转（Fisher p 从 <10⁻⁸ 变为 0.182 n.s.）。\n- Matched cohort non-hacking permutation test p=0.917：n=5 per group 无法检测合理效应量。且 point estimate 方向反转（ISR 2.3% < Random 5.9%）——ISR 作为 reward 可能连 non-hacking quality 都不如 random noise。\n- 建议：扩大 eval set 至 500+ examples；所有 per-seed 报告附 Wilson CIs。\n\n**W-C3. [共识, critical] 方法新颖性有限——LOO ablation 是标准技术，Goodhart collapse 是理论可预测结果**\n- LOO ablation 源自 mutation testing（论文 §3.2 明确承认 \"LOO ablation itself is standard\"）。\n- H7 tautology 的 ISR≥0.5 是 LOO 定义的数学必然（§3.2 line 57），Goodhart collapse 是可预测推论。\n- Discussion line 7 承认 \"collapse under LOO-based metrics is theoretically predictable\"。\n- 贡献主要是 \"applying known technique to new domain + confirming known theory + descriptive taxonomy\"。\n- R1 认为 empirical dynamics 细节（seed-dependent divergence, H7b triple gaming, cross-logic mode diversity）有增量价值；R2 认为这些是 \"empirically interesting but conceptually expected\"。两人共识：这是 Findings 级别贡献，低于 EMNLP 主会议的 novelty 门槛。\n\n**W-C4. [R2 critical / R1 major] 与 Kim et al. (2026) \"Do LLMs Game Formalization?\" 差异化不充分**\n- Related Work §2 仅用一个从句区分（\"gaming emerges during training rather than at inference\"）。\n- 缺少 gaming 模式分类对比、detection 方法对比、experimental setting 差异的详细讨论。\n- R1 认为两篇方法论层面不重叠，补充一段对比即可（降为 major）；R2 认为 gaming pattern 可能有重叠，差异化不充分构成 critical concern。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W-M1. [共识, major] Abstract \"99.5% structural collapse\" 来自单 seed (s42) 单轨迹，有 cherry-picking 嫌疑**\n- 99.5% collapse（ISR 0.642→0.003）是 s42 从 100→1000 步的数据。s44 走了 tautological collapse 路线（ISR 高是假象），s43 有 sampling eval 协议问题无法计算 trajectory。\n- 建议改为 3-seed 1000-step aggregate：\"ISR* collapses to near-zero (0.03±0.05) across three seeds\"。\n\n**W-M2. [共识, major] ISR 与 NLI accuracy 完全无关 (ρ=-0.049, p=0.187) 但定位为 \"structural quality diagnostic\" 可能误导**\n- ISR 低 → H1 redundancy；ISR 高（优化下）→ H7 gaming。两种情况 ISR 都不直接度量推理质量。\n- Introduction/Abstract 中 \"structural quality\" 和 \"structural integrity\" 措辞可能给读者过于正面的印象。\n- 建议更精确框定 ISR 的诊断能力：component necessity 度量，非 reasoning quality 度量。\n\n**W-M3. [共识, major] 单数据集 + 单模型族限制泛化性**\n- 全部实验基于 FOLIO + Qwen3。C3 声称 \"not specific to a single logic type or model scale\" 但仍在同一 dataset 和 model family 内。\n- Discussion line 11 \"STA applies to any compositional-input/binary-verifier setting\" 缺乏验证。\n\n**W-M4. [共识, major] Discussion 缺 mitigation 策略和 forward-looking analysis**\n- 论文只诊断不治疗。Discussion 仅一句 hand-waving（\"combining with effort-based detection\"）。\n- 建议增加分析：KL regularization 为何不足、reward ensembling 可能性、component-count normalization 的 negative result (1.06×)。\n\n**W-M5. [R1 major, R2 REBUT] Random control 产生 29.5% H7（5-seed pooled），可能削弱 ISR-specific 归因**\n- Exploratory cohort: Random H7 29.5% (dominated by s46 91.5%, s43 38.3%)；Matched cohort: Random H7 6.7%, 0/5 H7-dominated。\n- R2 反驳：matched cohort (0/5 vs 5/5, p=0.004) 是 clean evidence，exploratory cohort 的 pooled rate 掩盖 seed dependence。R1 concern 主要针对 exploratory cohort。\n- 分歧记录。Matched cohort 证据更可靠。\n\n### Minor Issues\n\n**W-m1. [共识] 缩写和术语密度过高**（~17 个缩写需同时追踪）。建议减少 3-4 个缩写或加 notation summary。\n\n**W-m2. [共识] Table 2 混合 single-seed 和 pooled 数据**（Exec=s42 only vs ISR/Rnd=5-seed pooled），对比不公平。\n\n**W-m3. [共识] Non-hacking rate 定义脆弱**，Table 1 N-H% 列建议标注 \"(upper bound)\"。\n\n**W-m4. [共识, minor] Exec-only s43 使用 sampling eval (T=0.7) 而非 greedy**，数据在 cross-seed 比较中需脚注说明。\n\n**W-m5. [共识, minor] 丢失 checkpoints (ISR β=0.1 s43/s44)** 影响 H8 审计完整性。Matched cohort 保留全部 checkpoints。\n\n**W-m6. [R1] Prolog cross-logic 实验无 random control**，无法排除 generic GRPO instability。\n\n---\n\n## Reviewer Consensus\n\n以下问题两位 Reviewer 达成一致 [AGREE]：\n\n1. **SFT baseline confound 是论文最大方法论弱点之一**。RL-specificity claim 证据基础薄弱，需进一步降低表述强度。\n2. **100-example eval set 统计功效不足**。Per-seed claims 建立在小样本之上，不同 pooling 下结论可反转。\n3. **Abstract \"99.5% collapse\" 应改为 3-seed aggregate**。\n4. **CMH p-values 应标注为 \"directional only\"**，以 seed-level Fisher exact test (p=0.004, BF₁₀=77) 为首要统计证据。\n5. **ISR ≠ semantic quality**，framing 需更精确。\n6. **Non-hacking rate 是 upper bound**，应在 Table 1 标注。\n7. **Kim et al. (2026) 需更详细对比**（severity 有分歧：R2 critical vs R1 major）。\n8. **Discussion 需增加 mitigation 讨论**。\n9. **写作质量高、格式完全合规**。\n10. **实验设计（matched 5+5 replication）超出同类工作标准**。\n\n---\n\n## Reviewer Divergence\n\n### 分歧 1: Overall 评分（R1: 3.5 Borderline Conference vs R2: 3.0 Findings）\n\n- **R1 立场**：如果解决 SFT framing 和 statistical power 讨论，empirical contributions（dynamics characterization, taxonomy, matched design 示范价值）足以达 Conference。Excitement 3/5。\n- **R2 立场**：即使完美修复 SFT 和统计问题，核心 novelty gap 无法解决——方法是标准的，发现是可预测的，没有 mitigation。EMNLP 主会议期待概念新贡献。Excitement 2.5/5。\n- **Director 判断**：R2 论证更有力。方法新颖性有限是结构性问题，不可通过写作修改解决。Empirical details 有价值但不足以弥补概念层面的 gap。合理区间 3.0-3.5，倾向 3.0。\n\n### 分歧 2: \"At every tested dose\" 表述（R1: 需更多 hedging vs R2: REBUT，结构论证足够）\n\n- **R1 立场**：4 个 β 值各 3-5 seeds，dynamics 定性各异（deterministic/stochastic/immediate/multi-modal），统一称 \"Goodhart collapse\" 可能过度简化。\n- **R2 反驳**：H7 tautology 的 ISR≥0.5 是 LOO 定义的数学性质，β-independent。Structural argument 使 \"at every tested dose\" 成立。\n- **Director 判断**：R2 反驳有理论支撑——ISR 的 Goodhart vulnerability 确实是定义层面的，不是经验巧合。但 R1 关于 dynamics 多样性（collapse occurs but varies qualitatively）的 nuance 也有价值。建议保留 \"at every tested dose\" 但在 Discussion 区分 \"collapse occurs\" vs \"collapse dynamics vary\"。\n\n### 分歧 3: Random H7 29.5% 对 ISR-specific 归因的影响\n\n- **R1 立场**：Random 也产生大量 H7，削弱因果归因。\n- **R2 反驳**：Matched cohort 0/5 vs 5/5 是 clean evidence。Exploratory cohort 的 29.5% 由 2 个 extreme seeds 主导，pooled rate 误导。ISR 将 H7 从 stochastic → irreversible attractor 的动力学区别是关键。\n- **Director 判断**：R2 反驳令人信服。Matched cohort 数据（Fisher p=0.004）比 exploratory cohort 的 pooled rate 更可靠。但论文应讨论两个 cohort 中 Random H7 率差异的含义。\n\n---\n\n## Questions（需作者澄清）\n\n**Q1.** Matched 5+5 design 是否做过 formal power analysis？如果需要检测 10pp 的 N-H rate 差异，需要多少 seeds？\n\n**Q2.** Premise-count-matched comparison 仅 1.06×（ISR*=0.258 vs 0.243）。Abstract \"any transient quality improvement disappears\" 中 \"improvement\" 是否需要修改为 \"apparent improvement\"？\n\n**Q3.** 早期 convex formulation 被放弃（ISR<1 always penalized, collapsing PR）。是否考虑过更小 β（如 0.01）来温和惩罚低 ISR？\n\n**Q4.** Cross-logic Prolog 实验无 random control。如何排除 generic GRPO instability（而非 ISR-specific）导致的 collapse？\n\n**Q5.** H9 (contradiction injection) 仅在 1.7B Random β=0.1 s42 一个 seed 观察到。\"ISR redirects hacking pathway from H9 to H1\" 基于 1 seed 的归因可信度如何？\n\n**Q6.** Component granularity 的选择（§3.2 \"what constitutes a component depends on the logic\"）是否影响 ISR？不同分解方式下 ISR 的敏感性如何？\n\n---\n\n## Missing References\n\n两位 Reviewer 一致指出以下引用缺失：\n\n1. **Lean-based RL**: Llemma (Azerbayev et al., 2024) — 与 solver-backed RL 大框架直接相关\n2. **Reward hacking mitigation 策略**: reward ensembling, constrained optimization, conservative reward — 论文讨论问题但未引用/讨论任何已知 mitigation 方向\n3. **Kim et al. (2026) 的更详细对比**: 当前仅一句区分，需逐条比较 gaming modes、detection methods、experimental settings\n4. **RLVR 框架**: Shao et al. (2025) \"Spurious Rewards\" 已引用但其 reward variance findings 与 Random control 的关系未展开讨论\n\n---\n\n## Overall Assessment\n\n### 评分\n\n| 维度 | R1 | R2 | 合并 |\n|------|-----|-----|------|\n| Soundness | 3.5 | 3.5 | **3.5** |\n| Excitement | 3.0 | 2.5 | **2.5-3.0** |\n| Novelty | — | 2.5 | **2.5** |\n| Reproducibility | 4.0 | 4.0 | **4.0** |\n| **Overall** | **3.5** | **3.0** | **3.0 (Findings)** |\n\n### Overall: 3.0 — Findings\n\n**一篇技术上 sound、实验设计 careful、限制报告异常透明的实证案例研究，但方法新颖性有限（LOO 是标准技术）、核心发现理论上可预测（Goodhart collapse 是 ISR LOO 定义的数学推论），且缺乏 mitigation 策略。适合 EMNLP Findings，但低于主会议的 novelty 和 excitement 门槛。**\n\n具体理由：\n\n1. **方法贡献有限**：STA/ISR 是标准 LOO ablation 的直接应用，Algorithm 1 仅 6 行伪代码。论文自己反复承认技术本身不新。\n2. **核心发现可预测**：H7 tautology 的 ISR≥0.5 是定义层面的必然，Goodhart collapse 不需要实验确认。虽然具体 dynamics（seed-dependent divergence, cross-logic diversity）超出简单理论预测，但这些更多是 characterization 而非 discovery。\n3. **SFT comparison confound 未解决**：RL-specificity 这一核心叙事的证据基础（PR 差距 80pp）薄弱，100-step checkpoint 仅部分控制。\n4. **统计功效受限**：100-example eval set 导致 per-seed claims 宽置信区间，不同 pooling 下结论可反转。Seed-level tests 受 n=5 power 限制。\n5. **范围窄**：单模型家族 (Qwen3)、单数据集 (FOLIO)、单 RL 算法 (GRPO)。\n6. **只诊断不治疗**：论文停留在 warning 层面，Discussion 缺乏 mitigation 分析。\n\n**提升路径**（若目标 3.5+ Borderline Conference）：\n- 补充 Kim et al. (2026) 详细对比\n- Abstract 改用 3-seed aggregate、降低 RL-specificity claim\n- Discussion 增加 mitigation 分析段落（KL failure, reward ensembling, component-count normalization negative result）\n- 所有 per-seed 报告附 Wilson CIs，正文讨论统计功效限制\n- Table 1 标注 N-H% (upper bound)，Table 2 统一聚合方式\n\n即使以上全部完成，核心 novelty gap（W-C3）仍是结构性问题，Conference 级别需要额外的概念贡献（如至少一个 mitigation 策略的 preliminary result）。\n\n### Confidence: 4/5\n\n两位 Reviewer 对 RL reward design、statistical testing、Goodhart dynamics、formal reasoning with LLMs 均有足够专业知识。技术判断一致（Soundness 3.5），分歧仅在 novelty 评估——这是 legitimate 的标准差异。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- \"99.5% structural collapse\" → 改为 3-seed aggregate (ISR*=0.03±0.05)\n- \"consistent with it being RL-specific\" → 进一步 hedge\n- \"three robust hacking modes (H1/H7/H8, validated across multiple seeds)\" — H8 只在 s42 完成审计，\"validated across multiple seeds\" 不准确\n- \"any transient quality improvement disappears\" — 1.06× 不构成 improvement，改为 \"apparent improvement\" 或 \"non-hacking window\"\n\n### Introduction\n- 叙事结构清晰（问题→不足→STA→发现→contributions），整体质量高\n- \"Process reward models require expensive annotations and do not transfer to arbitrary solver-backed settings\" — 过于绝对，最近 PRM 工作在迁移性方面有进展\n- C3 \"Cross-logic and cross-scale evidence that Goodhart vulnerability is not specific to...\" — 仍在同一 dataset 和 model family 内，需进一步 hedge\n\n### Related Work\n- 结构清晰，引用密度合理（~40 citations）\n- 与 TRACE (Wang et al. 2025) 关系说明清楚\n- **需增加 Kim et al. (2026) 专门对比段**\n- **需补充 reward hacking mitigation 和 Lean-based RL 引用**\n\n### Method\n- STA/ISR 定义清晰，Algorithm 1 简洁\n- Premise-count confound 讨论充分（§3.2 line 56-57）\n- Reward formulation 设计合理但需讨论乘法 vs 加法选择\n- Component granularity 的选择是未讨论的 degree of freedom\n\n### Experiments\n- Fig 2 collapse trajectory 是最有说服力的证据（单 seed 纵向分析避免 cross-seed 统计问题）\n- Matched 5+5 cohort design 优秀，Fisher p=0.004 是 clean evidence\n- Table 1 混合 500-step 和 1000-step 结果需更清楚标注\n- §4.3 Cross-logic 和 §4.4 Cross-scale 各仅 3 seeds 无 random control（Prolog），只能作 preliminary evidence\n- R2 重要发现：non-hacking permutation test p=0.917 且 point estimate 方向反转（ISR 2.3% < Random 5.9%）——ISR 可能在 genuine quality 上不如 random noise\n\n### Discussion and Conclusion\n- 核心 message 清晰且有实践价值\n- 需增加 mitigation analysis 段落\n- \"STA applies to any compositional-input/binary-verifier setting\" 需 hedge\n\n### Limitations\n- 异常全面和诚实——论文亮点之一\n- 建议将部分限制（100-example eval, CMH inflation）提升到正文讨论\n\n### Format Compliance\n- ✅ 正文 ≤8 页\n- ✅ `\\usepackage[review]{acl}`\n- ✅ Limitations 在 References 之前\n- ✅ Ethics Statement 存在\n- ✅ Responsible NLP Checklist 认真填写\n- ✅ 匿名化完整 (\"Anonymous ACL submission\")\n- ⚠️ Checklist C4 \"Partially\" — 建议补全 training framework 版本\n- ⚠️ Appendix 排版有空白页（p19, p21）",
    "project": "solver-trace-ablation",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0"
  }
}
```

</details>

---


### Tool result

_source line 1267 · 2026-05-19T02:59:07.758424+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_a771c2a33d631dd40256ecd5c3a6648e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 5893
}
```

</details>

---


### Assistant

_source line 1268 · 2026-05-19T03:00:53.693123+00:00_

本轮审稿已全部完成。汇总状态：

- **圆桌审稿**：2 名 Reviewer 独立初审 + 交叉回应均已完成，共识已达成
- **审稿报告**：已通过 `submit_review_report_to_research_director` 投递，Overall 3.0 (Findings)
- **Issue Tracker**：`review_issues.yaml` 已同步更新 Round 13 数据（~20 条已有 issue 更新 + 6 条新增）

本 session 无待处理任务。等待 Research Director 下一步指令。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 107

## Round 107

2 recorded events


### User

_source line 1269 · 2026-05-19T03:00:57.183803+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

核心判断：与 R1 在技术问题上高度一致（SFT confound、eval set size、CMH assumption、lost checkpoints），唯一实质分歧在 R1-N3（dose coverage 措辞）上给出了 REBUT——论文的 structural argument（H7 恒定获得 ISR≥0.5）使 "at every tested dose" 的表述合理。

评分维持 Overall 3.0 (Findings)、Excitement 2.5/5，理由是 novelty gap 不是 framing 修复能解决的：方法是标准 LOO、核心发现理论可预测、无 mitigation 策略。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1270 · 2026-05-19T03:01:08.260354+00:00_

审稿流程已全部完成。R2 交叉回应已纳入汇总报告，报告已提交至 Research Director。

最终评分：**Overall 3.0 (Findings)**。两位 Reviewer 在核心技术问题上达成共识（SFT confound、eval set size、CMH assumption、lost checkpoints），唯一实质分歧（dose coverage 措辞）已记录在报告中。Issue tracker 已同步更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 108

## Round 108

28 recorded events


### User

_source line 1271 · 2026-05-19T10:00:33.554291+00:00_

[Round 14 - 继续审稿]
论文已更新。请基于上一轮审稿意见，重点审查修改是否充分回应了之前提出的问题。
重点关注：
1. 上轮提出的问题是否已充分解决
2. 修改是否引入了新问题
3. 整体评分是否需要调整

上一轮审稿报告: `projects/solver-trace-ablation/artifacts/review_reports/round_13.md`
跨轮次问题追踪: `projects/solver-trace-ablation/artifacts/review_issues.yaml`
请用 read_local_file 先读这两个文件,重点验证 status=in_progress 的 issue 是否已被充分修复。
派 Reviewer 时把 open/in_progress 的 issue 列表附在任务里,要求逐条标 [RESOLVED] 或 [STILL_OPEN] + 理由。

[论文提交]
- 项目: solver-trace-ablation
- 论文路径: projects/solver-trace-ablation/paper/main.tex
- 目标 venue: ACL ARR May 2026
- 截止日期: 2026-05-25

请继续审稿流程。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1272 · 2026-05-19T10:00:44.145195+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status",
    "max_results": "6"
  }
}
```

</details>

---


### Tool result

_source line 1273 · 2026-05-19T10:00:44.246025+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1274 · 2026-05-19T10:00:48.435412+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_reports/round_13.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_reports/round_13.md"
  }
}
```

</details>

---


### Tool result

_source line 1275 · 2026-05-19T10:00:48.872247+00:00_

1	---
2	round: 13
3	review_mode: fresh
4	overall_score: 3.0
5	timestamp: 2026-05-19T02:59:01.887068+00:00
6	reviewer_ids: [1, 2]
7	cross_response_reviewer_ids: [1, 2]
8	force_resubmit: False
9	---
10	
11	# 合并审稿报告 — Round 13 (Fresh Review)
12	
13	**论文**: "Valid but Vacuous: Reward Hacking in GRPO-Trained FOL Reasoners"
14	**目标 Venue**: ACL ARR May 2026 → EMNLP 2026 commitment (Long Paper)
15	**Reviewer 编排**: 2 人（R1: 方法/实验/统计, R2: 新颖性/写作/格式）
16	**审稿模式**: Fresh（重新审稿，无历史记忆）
17	**轮次**: Round 1 初审 + Step 2 交叉回应，共识达成，无需第二轮
18	
19	---
20	
21	## Summary
22	
23	本文提出 Solver Trace Ablation (STA)，基于 leave-one-out (LOO) 消融的结构完整性诊断方法，用于检测 GRPO 训练的形式化推理器中的 reward hacking。核心指标 ISR 作为诊断工具时揭示 prove rate 背后的结构退化（exec-only 3-seed 1000-step ISR*=0.03±0.05 while PR=97±2%）；但作为训练 reward 时在所有 4 个测试剂量下出现 Goodhart collapse（matched 5+5 cohort: ISR 5/5 H7-dominated vs Random 0/5, Fisher p=0.004, BF₁₀=77）。实验覆盖 6 种 reward 条件、2 种逻辑类型（FOL/Prolog）、2 种模型规模（Qwen3-4B/1.7B），建立了 9 种 hacking 模式的分类体系。
24	
25	---
26	
27	## Strengths
28	
29	**S1. [共识] 研究问题重要且时机恰当。** Solver-backed RL 中 prove rate 作为唯一指标的盲点是真实且被低估的问题。ISR 的 diagnostic-vs-optimizer 不对称性发现对 RL-for-reasoning 社区有直接实践价值。
30	
31	**S2. [共识] 实验设计严谨，含 matched replication。** 5+5 matched cohort design（exploratory seeds 42-46 + replication seeds 47-51）超出同类工作标准。Fisher exact test (p=0.004, BF₁₀=77) 为 H7 dominance 提供较强证据。多重统计检验（Fisher, Mann-Whitney, permutation, Bayes factor）体现了审慎的实验学纪律。
32	
33	**S3. [共识] Goodhart 机制分析清晰。** H7 tautology（单前提=结论 → ISR≥0.5 by construction → positive feedback loop → absorbing state）的因果链条完整。β 控制 collapse timing 而非 whether，这一结论有理论支撑。
34	
35	**S4. [共识] 限制条件报告异常透明。** 丢失 checkpoints、s43 sampling evaluation 协议违规、CMH p-value inflation、non-hacking 作为上界、SFT comparison confound——均在 Limitations 和 Appendix 中坦诚讨论。这种透明度在投稿论文中罕见。
36	
37	**S5. [共识] Hacking taxonomy 有独立工具价值。** 9 种模式（8 自动 + 1 手动）的分类体系，特别是 H7b triple gaming 和 query-as-fact gaming，具体且可复现，可被其他 solver-backed 系统直接采用。
38	
39	**S6. [共识] 写作质量高、格式完全合规。** 无 em-dash，无 AI 写作黑名单词汇，段落长度合理，叙事线连贯。
…[truncated 12176 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 436
}
```

</details>

---


### Tool call

_source line 1276 · 2026-05-19T10:00:48.872645+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1277 · 2026-05-19T10:00:49.175952+00:00_

1	issues:
2	# ===== 历史 issues (Round 0-3, 全部 resolved) =====
3	- id: "R1-W1"
4	  summary: "统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例"
5	  category: experiment
6	  severity: critical
7	  status: resolved
8	  first_raised_round: 0
9	  last_seen_round: 2
10	  resolution: "β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。Fisher exact test + Wilson 95% CI 已加入。eval 集 100 例限制在 limitations.tex 讨论。"
11	  resolution_round: 2
12	
13	- id: "RV-EVAL-FALLBACK"
14	  summary: "eval_sta.py test_100.jsonl 静默 fallback 已移除"
15	  category: experiment
16	  severity: critical
17	  status: resolved
18	  first_raised_round: 1
19	  last_seen_round: 1
20	  resolution: "第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)，无 fallback。"
21	  resolution_round: 1
22	
23	- id: "RV-D060-NARRATIVE"
24	  summary: "D060 'Goodhart instability' 叙事：77pp PR 差距在同一测试集上确认成立"
25	  category: experiment
26	  severity: critical
27	  status: resolved
28	  first_raised_round: 1
29	  last_seen_round: 1
30	  resolution: "β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。"
31	  resolution_round: 2
32	
33	- id: "RV-FIG2-STALE-SCRIPT"
34	  summary: "figures/paper/gen_fig2.py 旧脚本数据错误"
35	  category: format
36	  severity: warning
37	  status: resolved
38	  first_raised_round: 1
39	  last_seen_round: 1
40	  resolution: "已修复。"
41	  resolution_round: 1
42	
43	- id: "R1-W2"
44	  summary: "ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量"
45	  category: framing
46	  severity: critical
47	  status: resolved
48	  first_raised_round: 0
49	  last_seen_round: 0
50	  resolution: "method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。"
51	  resolution_round: 2
52	
53	- id: "R2-W1"
54	  summary: "Limitations section 格式不合规"
55	  category: format
56	  severity: critical
57	  status: resolved
58	  first_raised_round: 0
59	  last_seen_round: 2
60	  resolution: "独立 limitations.tex 已创建，位于 references 之前。"
61	  resolution_round: 3
62	
63	- id: "R2-W2"
64	  summary: "实验仅用单一模型 (Qwen3-4B)
…[truncated 36224 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 303
}
```

</details>

---


### Tool call

_source line 1278 · 2026-05-19T10:01:16.296905+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/abstract.tex"
  }
}
```

</details>

---


### Tool call

_source line 1279 · 2026-05-19T10:01:16.347738+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex"
  }
}
```

</details>

---


### Tool call

_source line 1280 · 2026-05-19T10:01:16.348244+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1281 · 2026-05-19T10:01:17.101771+00:00_

1	\begin{abstract}
2	RL-trained formalizers achieve high prove rates on logical reasoning tasks, yet these gains mask structural degeneration invisible to execution-based evaluation.
3	We propose \emph{Solver Trace Ablation} (STA), a leave-one-out necessity test on solver inputs that quantifies structural integrity through the \emph{Irreducible Solver Rate} (ISR).
4	Applied as a post-hoc diagnostic, ISR reveals structural collapse ($\text{ISR}^*$ falls to $0.03{\pm}0.05$ across three seeds at 1000 steps) hidden behind rising prove rates; a supervised baseline on identical data largely avoids this failure, consistent with hacking being associated with RL optimization rather than data exposure, though the large prove-rate gap prevents definitive causal attribution.
5	Repurposed as a reward signal, however, ISR exhibits Goodhart collapse at every tested dose: tautological constructions receive high ISR by construction, and any transient non-hacking window disappears under extended training.
6	Across six reward conditions, two logic types, and two model scales, we identify three persistent hacking modes (conclusion embedding [CE] / tautological shortcut [TS], validated across ${\geq}3$ seeds; premise-subset gaming [PG], observed at lower prevalence) plus additional modes in isolated conditions, and show that ISR is reliable as a diagnostic but unreliable as an optimization target.\footnote{Code and data: \url{[anonymized]}}
7	\end{abstract}
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 804
}
```

</details>

---


### Tool result

_source line 1282 · 2026-05-19T10:01:17.102400+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Prove rate, the dominant evaluation metric for solver-backed formalizers~\citep{logic-lm, linc, satlm}, conflates faithful reasoning with degenerate shortcuts.
5	This gap is especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
6	Recent work applies GRPO~\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback, driving rapid prove-rate gains but providing no signal on the structural necessity of individual components.
7	Process reward models~\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not directly apply to arbitrary solver-backed settings; while LLMs already game logical formalization at inference time~\citep{kim-game-formalization, bondarenko-spec-gaming}, RL training produces qualitatively different failures because the optimizer actively reshapes the output distribution toward degenerate attractors.
8	What is missing is an annotation-free \emph{diagnostic} for structural integrity in solver-backed formal outputs.
9	
10	We address this gap with \emph{Solver Trace Ablation} (STA), which applies leave-one-out ablation on solver inputs to test whether each component of a proved formalization is individually necessary.
11	The fraction of necessary components yields the \emph{Irreducible Solver Rate} (ISR), where $\text{ISR}{=}1$ indicates full necessity and $\text{ISR}{=}0$ complete redundancy.
12	LOO ablation itself is standard~\citep{demillo1978, jia-harman-survey}; our contribution lies in applying it as a GRPO-hacking diagnostic and in the empirical phenomena it surfaces.
13	As a post-hoc diagnostic on a GRPO formalizer trained with FOLIO~\citep{folio}, ISR reveals a structural collapse trajectory invisible to prove rate: ISR$^*$ falls to $0.03{\pm}0.05$ across three seeds a
…[truncated 2109 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 754
}
```

</details>

---


### Tool result

_source line 1283 · 2026-05-19T10:01:17.102911+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Formal reasoning with LLMs.}
5	LLM-solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods on solver feedback~\citep{polu2020generative, zelikman2022star, mellgren-prolog-grpo, logic-rl, deepseek-prover-v15, deepseek-prover-v2, deepseek-r1-2025} evaluate execution accuracy alone; math-specialized models such as Llemma~\citep{azerbayev2024llemma} similarly rely on downstream task accuracy without structural diagnostics.
6	We use FOLIO~\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.
7	
8	\paragraph{Faithfulness in formalization.}
9	\citet{kim-game-formalization} study whether GPT-5 and DeepSeek-R1 game Lean~4 formalization at \emph{inference} time. Using axiom diffing and LLM-judge classification on 303 FOL problems, they find no systematic gaming in unified generation but identify two unfaithfulness modes: axiom fabrication during proof (56\% are conclusion-as-axiom) and premise mistranslation during formalization.
10	Our work differs in three respects.
11	First, we study \emph{training-time} gaming under GRPO, where the optimizer actively reshapes the output distribution, producing qualitatively different failures from one-shot inference.
12	Second, our detection method (STA/ISR) is deterministic and solver-derived, requiring no LLM judge.
13	Third, we observe universal gaming under RL (all GRPO conditions show ${\geq}80\%$ hacking), whereas Kim et al.\ report that models prefer failure over forcing proofs at inference time.
14	The complementarity is direct: their axiom-fabrication mode is functionally equivalent to our CE (conclusion embedding), confirming that the same exploit class arises independently under both inference and training regimes.
15	
16	\paragraph{Process rewards and reward shaping.}
17	PRMs~\citep{cobbe2021training, lightman-verify-step, math-shepherd} provide step-level feedback but suffer from noise and distribution s
…[truncated 2667 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 754
}
```

</details>

---


### Tool call

_source line 1284 · 2026-05-19T10:01:17.103239+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1285 · 2026-05-19T10:01:17.605646+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task and GRPO Training}
5	\label{sec:task}
6	
7	Given premises $P_1,\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $x=\{c_1,\ldots,c_n\}$ verified by an external solver $S\in\{\text{Prover9}$~\citep{mccune-prover9}$, \text{SWI-Prolog}$~\citep{wielemaker2012swi}$\}$ .
8	We train with Group Relative Policy Optimization (GRPO)~\citep{deepseekmath} ($K{=}4$), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(x){=}\textit{proved}]$.
9	This optimizes prove rate but provides no signal about \emph{structural quality}: a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.
10	All experiments draw from FOLIO~\citep{folio}; the held-out evaluation file retains a legacy \texttt{proofwriter\_fol\_*.jsonl} filename (from ProofWriter~\citep{proofwriter}) but contains only FOLIO-derived examples.
11	
12	\subsection{Solver Trace Ablation (STA)}
13	\label{sec:sta}
14	
15	STA tests whether each component of a proved formalization is individually necessary for proof success .
16	Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\setminus\{c_i\}$ and re-runs the solver (Algorithm~\ref{alg:sta}).
17	A component is \emph{necessary} if its removal causes proof failure.
18	What constitutes a component depends on the logic: premises and conclusion sub-expressions (quantifier, antecedent, consequent) in FOL, clauses or ground facts in Prolog.
19	For example, given premise $\forall x(R(x){\to}P(x))$ and conclusion $\forall x(P(x){\to}Q(x))$, the decomposition yields components $\{$premise, $\forall x$, $P(x)$, $Q(x)\}$ with $n{=}4$.
20	LOO ablation itself is standard in mutation testing and sensitivity analysis~\citep{demillo1978, jia-harman-survey}; our contribution lies in applying it as a GRPO-hacking diagnostic and in the empirical phenomena it surfaces.
21	
22	\begin{algorithm}[t]
23	\capt
…[truncated 5887 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1286 · 2026-05-19T10:01:17.606118+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1287 · 2026-05-19T10:01:18.259078+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward across four dose levels, where it exhibits Goodhart effects (\S\ref{sec:goodhart}); and STA as a cross-logic protocol (\S\ref{sec:crosslogic}).
5	Cross-scale evidence from Qwen3-1.7B reveals capacity-dependent Goodhart basins (\S\ref{sec:crossscale}).
6	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
7	
8	\subsection{Setup}\label{sec:setup}
9	
10	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline is trained with negative log-likelihood (NLL) on gold formalizations.\footnote{All experiments use \texttt{data/train\_500\_seed42.jsonl}; seeds control initialization and rollout sampling only.}
11	Held-out evaluation uses 100 FOLIO examples (\texttt{proofwriter\_fol\_100.jsonl}) with greedy decoding (Appendix~\ref{app:setup}); training uses sampling ($T{=}0.7$), so evaluation reflects the mode of the learned distribution rather than the stochastic rollout behavior that drives RL updates.
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), and hacking-mode rates from a two-stage classifier (\S\ref{sec:taxonomy-method}): strict text matching for CE/TS, followed by functional analysis of $n_{\text{necessary}}$.
13	The \emph{non-hacking} (N-H) rate is the residual of proved samples matching none of the eight automatically cataloged patterns; a ninth mode, CI, is identified by manual audit (\S\ref{sec:taxonomy}).
14	\emph{Strict non-hacking} further requires content-dependent predicates derived from the natural-language premises, filtering content-independent proofs that evade the taxonomy through structural novelty (\S\ref{sec:crossscale}).
15	
1
…[truncated 16248 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 652
}
```

</details>

---


### Tool call

_source line 1288 · 2026-05-19T10:01:18.360177+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1289 · 2026-05-19T10:01:18.553513+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	STA exposes structural degeneration invisible to execution-based evaluation, and ISR exhibits Goodhart collapse at all four tested doses.
5	The core asymmetry is that the same LOO structure making ISR a useful diagnostic also makes it a vulnerable optimization target: tautological constructions satisfy component necessity by definition.
6	An SFT baseline largely avoids hacking under identical data, consistent with hacking being associated with RL optimization, though the prove-rate gap (13\% vs.\ 97\%) prevents definitive causal attribution.
7	Any transient non-hacking window ($p{=}0.92$, permutation test; matched 5+5 design) disappears under extended training; snapshot evaluation overestimates ISR's benefit.
8	
9	All experiments use Qwen3 (4B/1.7B), FOLIO, and GRPO; the structural vulnerability follows from the LOO definition and should in principle transfer to settings where the optimizer can reduce component count.
10	Our results illustrate regressional Goodhart~\citep{manheim-goodhart-taxonomy}: structural diagnostics should remain decoupled from the training loop.
11	A targeted mitigation confirms this systematic nature: gating the ISR bonus on component count ($r = r_{\text{exec}} {+} \beta\,\text{ISR}\cdot\mathbf{1}[n{\geq}2]$) eliminates TS entirely (0/3 seeds), but 2/3 seeds migrate to PG (premise-subset gaming), with one seed achieving $\text{ISR}^*{=}1.0$ through PG alone (Appendix~\ref{app:gated-isr}).
12	The replacement exploit is more severe than the original ($\text{ISR}{\geq}0.5$ for TS vs.\ $1.0$ for PG): blocking one Goodhart pathway redirects optimization pressure rather than resolving it.
13	Reward ensembling~\citep{coste2024reward} targets learned rewards, not deterministic solver signals; constrained optimization~\citep{moskovitz2024confronting} could cap ISR, but collapse at all $\beta$ suggests a narrow proxy-validity boundary.
14	Combining STA with reasoning-effort measures~
…[truncated 56 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 193
}
```

</details>

---


### Tool call

_source line 1290 · 2026-05-19T10:01:18.605225+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1291 · 2026-05-19T10:01:18.904240+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Experiments use a single model family (Qwen3-4B/1.7B), one dataset (FOLIO, 500 train / 100 eval examples), and one RL algorithm (GRPO); generalization of specific hacking modes to other architectures or benchmarks remains open.
5	ISR measures syntactic component necessity, not semantic faithfulness ($\rho{=}{-}0.049$ with NLI accuracy; Appendix~\ref{app:extended-discussion}); non-hacking is a residual classification where undiscovered modes would reduce the true rate.
6	STA adds $O(n)$ solver calls (${\sim}6$--$8{\times}$ overhead) per proved sample; the 100-example evaluation set limits per-seed precision ($6\%{\approx}6$ samples; Wilson 95\% CI $[2.3\%, 12.7\%]$); statistical power is limited ($n{=}5$ seeds).
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 299
}
```

</details>

---


### Tool call

_source line 1292 · 2026-05-19T10:01:24.224891+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1293 · 2026-05-19T10:01:24.477375+00:00_

1	% Appendix: solver-trace-ablation
2	
3	\section{Experimental Setup}
4	\label{app:setup}
5	
6	Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
7	All RL conditions use the same GRPO configuration; only the reward function differs.
8	Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).
9	
10	\begin{table}[!htb]
11	\centering
12	\caption{Training hyperparameters for all GRPO experiments.}
13	\label{tab:hyperparams}
14	\footnotesize
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{@{}ll@{}}
17	\toprule
18	\textbf{Parameter} & \textbf{Value} \\
19	\midrule
20	\multicolumn{2}{@{}l}{\textit{Model}} \\
21	Base model & Qwen3-4B \\
22	Precision & BF16 \\
23	\midrule
24	\multicolumn{2}{@{}l}{\textit{GRPO Training}} \\
25	Rollouts per prompt ($K$) & 4 \\
26	Training steps (default) & 500 \\
27	Training steps (extended) & 1000 \\
28	Learning rate & $1 \times 10^{-6}$ \\
29	Per-device batch size & 4 \\
30	Gradient accumulation steps & 2 \\
31	Effective batch size & 8 \\
32	Max completion length & 512 tokens \\
33	Random seeds & 42, 43, 44 \\
34	\midrule
35	\multicolumn{2}{@{}l}{\textit{Data}} \\
36	Training set & FOLIO, 500 examples \\
37	Evaluation set & FOLIO, 100 examples (held-out) \\
38	Data file & \texttt{train\_500\_seed42} \\
39	\midrule
40	\multicolumn{2}{@{}l}{\textit{Framework}} \\
41	Training library & TRL 0.17.0 \\
42	PyTorch & 2.6.0 (CUDA 12.4) \\
43	Transformers & 4.51.3 \\
44	\midrule
45	\multicolumn{2}{@{}l}{\textit{Solvers}} \\
46	FOL solver & Prover9 \\
47	Prolog solver & SWI-Prolog 8.4.2 \\
48	\midrule
49	\multicolumn{2}{@{}l}{\textit{Evaluation}} \\
50	Decoding & Greedy ($T{=}0$) \\
51	ISR computation & \texttt{eval\_sta.py} \\
52	ISR variant & Proved-only (ISR$^*$) \\
53	\bottomrule
54	\end{tabular}}
55	\end{table}
56	
57	\paragraph{Evaluation protocol.}
58	All cross-run ISR values are recomputed uniformly by a single evaluator (\tex
…[truncated 52628 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 1294 · 2026-05-19T10:02:54.081520+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## Round 14 修订评估任务 — Reviewer 1（方法/实验/统计）\n\n**论文**: \"Valid but Vacuous: Reward Hacking in GRPO-Trained FOL Reasoners\"\n**目标 venue**: ACL ARR May 2026 → EMNLP 2026 (Long Paper, 8 页限制)\n**审稿模式**: Continue — 基于 Round 13 审稿意见检查修改充分性\n\n**论文路径**: `projects/solver-trace-ablation/paper/main.tex`\n**上轮报告**: `projects/solver-trace-ablation/artifacts/review_reports/round_13.md`\n\n### 你的审查侧重\n方法严谨性、实验设计、统计声明、新增实验(gated ISR)的有效性。\n\n### 上轮 Open/In-Progress Issues — 请逐条标 [RESOLVED] 或 [STILL_OPEN] + 理由\n\n**Critical issues:**\n\n1. **v5-R12-SFT-PR** [critical, in_progress]: SFT baseline PR confound (PR=13% vs 97%)。R13 要求进一步降低 RL-specificity claim 强度。\n   - 检查: Abstract, Introduction, Discussion 中 \"consistent with...though\" hedging 是否充分。SFT n=39 的限制是否充分讨论。\n\n2. **v4-R1-W8** [critical, in_progress]: 100-example eval set 统计功效不足。R13 要求扩大 eval set 或附 Wilson CIs。\n   - 检查: 是否附了 Wilson CIs（至少在 matched cohort table）。Limitations 中功效讨论是否加强。\n\n3. **v4-R12-N3** [critical, in_progress]: OR=3.48 (uncorrected) vs OR=0.61 (corrected) 方向反转。R13 要求 Table 1 N-H 用 corrected 6%†。\n   - 检查: Table 1 是否清楚标注 corrected vs uncorrected，方向反转是否在正文讨论。\n\n4. **v8-R12-N1** [critical, in_progress]: Goodhart 发现的可预测性限制概念新颖性（结构性问题）。\n   - 检查: 这是结构性问题，不期望完全解决。看论文是否更好地定位自己的增量贡献。\n\n5. **v8-R12-N2** [critical, in_progress]: 实验范围与标题/claim scope 不匹配。R13 要求进一步 hedge C3 和 Discussion 泛化 claim。\n   - 检查: C3 措辞、Discussion \"STA applies to any...\" 是否加了限定。\n\n**Major issues:**\n\n6. **v4-R12-N2** [warning, in_progress]: 'At all tested doses' claim。R13 有分歧（R1 要更多 hedging vs R2 认为 structural argument 足够）。\n   - 检查: Abstract/Discussion 中此 claim 的 hedging 程度。\n\n7. **v6-R1-W2** [warning, in_progress]: Dose-response claim 统计不足（4β × 3-5 seeds 稀疏）。\n   - 检查: 是否标注 \"preliminary\"。\n\n8. **v4-R12-W6** [warning, in_progress]: Seed 43 exec-only 评估协议矛盾。R13 要求正文加脚注。\n   - 检查: §4.2 是否有脚注说明。\n\n9. **v4-R12-W7** [warning, in_progress]: Deleted checkpoints。R13 要求 Table 1 N-H 列标注 \"(upper bound)\"。\n   - 检查: Table 1 caption 或列头是否有 upper bound 标注。\n\n10. **v5-R1-N3** [warning, in_progress]: Table 1 混合 500-step 和 1000-step 结果。\n    - 检查: Table 1 标注是否清楚。\n\n11. **v13-R1-Q4** [warning, open]: Prolog cross-logic 缺少 random control。\n    - 检查: §4.3 是否明确讨论此限制。\n\n12. **v8-R1-W4** [info, in_progress]: CMH p-values 应标注 \"directional only\"。\n    - 检查: Appendix 统计分析中 CMH 标注。\n\n**新增实验审查:**\n\n13. **Gated ISR 实验** (Discussion + Appendix §B.11): 3 seeds (52-54), component-count gate。\n    - 核实: 实验设计是否合理、结论是否 overstate、是否需要 random control。\n    - TS→PG 迁移的 claim 基于 2/3 seeds (s52 PG=100%, s53 PG=89.6%, s54 PG=0%)——是否稳健？\n\n### 输出格式\n对每个 issue 标 [RESOLVED] 或 [STILL_OPEN]，给出简短理由和具体文本位置。\n新发现的问题单独列出。\n最后给出 Overall Assessment 和 Excitement 评分（使用 EMNLP ARR 标准）。",
  "reviewer_id": "1",
  "round_number": "14"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## Round 14 修订评估任务 — Reviewer 1（方法/实验/统计）\n\n**论文**: \"Valid but Vacuous: Reward Hacking in GRPO-Trained FOL Reasoners\"\n**目标 venue**: ACL ARR May 2026 → EMNLP 2026 (Long Paper, 8 页限制)\n**审稿模式**: Continue — 基于 Round 13 审稿意见检查修改充分性\n\n**论文路径**: `projects/solver-trace-ablation/paper/main.tex`\n**上轮报告**: `projects/solver-trace-ablation/artifacts/review_reports/round_13.md`\n\n### 你的审查侧重\n方法严谨性、实验设计、统计声明、新增实验(gated ISR)的有效性。\n\n### 上轮 Open/In-Progress Issues — 请逐条标 [RESOLVED] 或 [STILL_OPEN] + 理由\n\n**Critical issues:**\n\n1. **v5-R12-SFT-PR** [critical, in_progress]: SFT baseline PR confound (PR=13% vs 97%)。R13 要求进一步降低 RL-specificity claim 强度。\n   - 检查: Abstract, Introduction, Discussion 中 \"consistent with...though\" hedging 是否充分。SFT n=39 的限制是否充分讨论。\n\n2. **v4-R1-W8** [critical, in_progress]: 100-example eval set 统计功效不足。R13 要求扩大 eval set 或附 Wilson CIs。\n   - 检查: 是否附了 Wilson CIs（至少在 matched cohort table）。Limitations 中功效讨论是否加强。\n\n3. **v4-R12-N3** [critical, in_progress]: OR=3.48 (uncorrected) vs OR=0.61 (corrected) 方向反转。R13 要求 Table 1 N-H 用 corrected 6%†。\n   - 检查: Table 1 是否清楚标注 corrected vs uncorrected，方向反转是否在正文讨论。\n\n4. **v8-R12-N1** [critical, in_progress]: Goodhart 发现的可预测性限制概念新颖性（结构性问题）。\n   - 检查: 这是结构性问题，不期望完全解决。看论文是否更好地定位自己的增量贡献。\n\n5. **v8-R12-N2** [critical, in_progress]: 实验范围与标题/claim scope 不匹配。R13 要求进一步 hedge C3 和 Discussion 泛化 claim。\n   - 检查: C3 措辞、Discussion \"STA applies to any...\" 是否加了限定。\n\n**Major issues:**\n\n6. **v4-R12-N2** [warning, in_progress]: 'At all tested doses' claim。R13 有分歧（R1 要更多 hedging vs R2 认为 structural argument 足够）。\n   - 检查: Abstract/Discussion 中此 claim 的 hedging 程度。\n\n7. **v6-R1-W2** [warning, in_progress]: Dose-response claim 统计不足（4β × 3-5 seeds 稀疏）。\n   - 检查: 是否标注 \"preliminary\"。\n\n8. **v4-R12-W6** [warning, in_progress]: Seed 43 exec-only 评估协议矛盾。R13 要求正文加脚注。\n   - 检查: §4.2 是否有脚注说明。\n\n9. **v4-R12-W7** [warning, in_progress]: Deleted checkpoints。R13 要求 Table 1 N-H 列标注 \"(upper bound)\"。\n   - 检查: Table 1 caption 或列头是否有 upper bound 标注。\n\n10. **v5-R1-N3** [warning, in_progress]: Table 1 混合 500-step 和 1000-step 结果。\n    - 检查: Table 1 标注是否清楚。\n\n11. **v13-R1-Q4** [warning, open]: Prolog cross-logic 缺少 random control。\n    - 检查: §4.3 是否明确讨论此限制。\n\n12. **v8-R1-W4** [info, in_progress]: CMH p-values 应标注 \"directional only\"。\n    - 检查: Appendix 统计分析中 CMH 标注。\n\n**新增实验审查:**\n\n13. **Gated ISR 实验** (Discussion + Appendix §B.11): 3 seeds (52-54), component-count gate。\n    - 核实: 实验设计是否合理、结论是否 overstate、是否需要 random control。\n    - TS→PG 迁移的 claim 基于 2/3 seeds (s52 PG=100%, s53 PG=89.6%, s54 PG=0%)——是否稳健？\n\n### 输出格式\n对每个 issue 标 [RESOLVED] 或 [STILL_OPEN]，给出简短理由和具体文本位置。\n新发现的问题单独列出。\n最后给出 Overall Assessment 和 Excitement 评分（使用 EMNLP ARR 标准）。",
    "reviewer_id": "1",
    "round_number": "14"
  }
}
```

</details>

---


### Tool result

_source line 1295 · 2026-05-19T10:03:19.109787+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 25028
}
```

</details>

---


### Tool call

_source line 1296 · 2026-05-19T10:03:19.459319+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## Round 14 修订评估任务 — Reviewer 2（新颖性/写作/格式）\n\n**论文**: \"Valid but Vacuous: Reward Hacking in GRPO-Trained FOL Reasoners\"\n**目标 venue**: ACL ARR May 2026 → EMNLP 2026 (Long Paper, 8 页限制)\n**审稿模式**: Continue — 基于 Round 13 审稿意见检查修改充分性\n\n**论文路径**: `projects/solver-trace-ablation/paper/main.tex`\n**上轮报告**: `projects/solver-trace-ablation/artifacts/review_reports/round_13.md`\n\n### 你的审查侧重\n新颖性评估更新、写作质量、格式合规、引用充足性、Kim et al. 对比质量。\n\n### 上轮 Open/In-Progress Issues — 请逐条标 [RESOLVED] 或 [STILL_OPEN] + 理由\n\n**Critical issues:**\n\n1. **v13-R2-N2** [critical, open]: 与 Kim et al. (2026) 差异化不充分。R13 要求 Related Work 增加逐条对比。\n   - 检查: Related Work 是否有专门的 Kim et al. 对比段。对比是否涵盖 gaming modes、detection 方法、experimental settings。\n\n2. **v4-R2-W9** [warning, in_progress]: 方法新颖性有限（LOO 是标准技术）。结构性问题。\n   - 检查: 论文是否更好地定位自己为 \"empirical case study\" 而非 \"novel method\"。\n\n3. **v5-R2-N3** [warning, in_progress]: 概念新颖性有限（diagnostic becomes target 可预测）。结构性问题。\n   - 检查: 同上。gated ISR 实验是否为 novelty 加分。\n\n**Major issues:**\n\n4. **v13-R1-W1** [warning, open]: ISR 与 NLI accuracy 无关但 \"structural quality diagnostic\" 定位可能误导。\n   - 检查: Method §3.2 中 ISR 定义是否精确为 \"component necessity\" 而非 \"reasoning quality\"。Abstract/Introduction 中是否一致。\n\n5. **v13-R2-W4** [warning, open]: 缩写和术语密度过高（~17 个缩写）。\n   - 检查: 是否减少缩写或添加 notation summary。统计所有缩写数量。\n\n6. **v13-R2-W5** [warning, open]: Table 2 混合 single-seed 和 pooled 数据。\n   - 检查: 是否统一聚合方式或标注每列 seed 数。\n\n7. **v13-R2-MITIGATION** [warning, open]: Discussion 缺少 mitigation 策略。\n   - 检查: gated ISR 实验结果是否纳入 Discussion。是否讨论 reward ensembling、constrained optimization、KL failure。\n\n8. **v5-R2-W1** [warning, in_progress]: Abstract \"99.5% structural collapse\" 来自单 seed。\n   - 检查: Abstract 是否改用 3-seed aggregate。\n\n9. **v12-R2-W2** [warning, in_progress]: 与 Kim et al. 区分需更锐利。\n   - 检查: 同 issue 1。\n\n10. **v10-R2-W8** [warning, in_progress]: Discussion/Conclusion 过于简短，缺 forward-looking content。\n    - 检查: Discussion 是否扩展，是否包含 mitigation analysis。\n\n11. **v5-R2-W3** [warning, in_progress]: paragraph{} 过度碎片化。\n    - 检查: method/conclusion/limitations 中段落结构。\n\n**Info issues:**\n\n12. **v11-R2-MR** [info, in_progress]: 缺少 2025-2026 最新引用。R13 要求补 Llemma, reward hacking mitigation 文献。\n    - 检查: references.bib 是否新增相关引用。\n\n13. **v8-R1-N3** [warning, in_progress]: 术语交替使用导致语义滑移。\n    - 检查: H1→CE, H7→TS 等重命名后是否全文一致。是否有残留旧名称。\n\n14. **v11-R1-W2** [warning, in_progress]: Taxonomy 仅 H1/H7 有 precision 验证，H8 只 s42 审计。\n    - 检查: Abstract 和 Method 中对 PG (原 H8) 的 claim 强度是否降低。\n\n**写作质量检查:**\n- AI 写作标志: em-dash (—), 解释性 en-dash (–), -ing phrase endings, 黑名单词汇\n- 段落长度和叙事连贯性\n- 格式合规: ≤8 页, [review] option, 匿名化, Limitations, Ethics, Checklist\n\n**Hacking 模式重命名评估:**\nH1→CE, H7→TS, H8→PG, H9→CI 的重命名是否改善了可读性？是否全文一致？\n\n### 输出格式\n对每个 issue 标 [RESOLVED] 或 [STILL_OPEN]，给出简短理由和具体文本位置。\n新发现的问题单独列出。\n最后给出 Overall Assessment、Excitement、Novelty 评分（使用 EMNLP ARR 标准）。",
  "reviewer_id": "2",
  "round_number": "14"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## Round 14 修订评估任务 — Reviewer 2（新颖性/写作/格式）\n\n**论文**: \"Valid but Vacuous: Reward Hacking in GRPO-Trained FOL Reasoners\"\n**目标 venue**: ACL ARR May 2026 → EMNLP 2026 (Long Paper, 8 页限制)\n**审稿模式**: Continue — 基于 Round 13 审稿意见检查修改充分性\n\n**论文路径**: `projects/solver-trace-ablation/paper/main.tex`\n**上轮报告**: `projects/solver-trace-ablation/artifacts/review_reports/round_13.md`\n\n### 你的审查侧重\n新颖性评估更新、写作质量、格式合规、引用充足性、Kim et al. 对比质量。\n\n### 上轮 Open/In-Progress Issues — 请逐条标 [RESOLVED] 或 [STILL_OPEN] + 理由\n\n**Critical issues:**\n\n1. **v13-R2-N2** [critical, open]: 与 Kim et al. (2026) 差异化不充分。R13 要求 Related Work 增加逐条对比。\n   - 检查: Related Work 是否有专门的 Kim et al. 对比段。对比是否涵盖 gaming modes、detection 方法、experimental settings。\n\n2. **v4-R2-W9** [warning, in_progress]: 方法新颖性有限（LOO 是标准技术）。结构性问题。\n   - 检查: 论文是否更好地定位自己为 \"empirical case study\" 而非 \"novel method\"。\n\n3. **v5-R2-N3** [warning, in_progress]: 概念新颖性有限（diagnostic becomes target 可预测）。结构性问题。\n   - 检查: 同上。gated ISR 实验是否为 novelty 加分。\n\n**Major issues:**\n\n4. **v13-R1-W1** [warning, open]: ISR 与 NLI accuracy 无关但 \"structural quality diagnostic\" 定位可能误导。\n   - 检查: Method §3.2 中 ISR 定义是否精确为 \"component necessity\" 而非 \"reasoning quality\"。Abstract/Introduction 中是否一致。\n\n5. **v13-R2-W4** [warning, open]: 缩写和术语密度过高（~17 个缩写）。\n   - 检查: 是否减少缩写或添加 notation summary。统计所有缩写数量。\n\n6. **v13-R2-W5** [warning, open]: Table 2 混合 single-seed 和 pooled 数据。\n   - 检查: 是否统一聚合方式或标注每列 seed 数。\n\n7. **v13-R2-MITIGATION** [warning, open]: Discussion 缺少 mitigation 策略。\n   - 检查: gated ISR 实验结果是否纳入 Discussion。是否讨论 reward ensembling、constrained optimization、KL failure。\n\n8. **v5-R2-W1** [warning, in_progress]: Abstract \"99.5% structural collapse\" 来自单 seed。\n   - 检查: Abstract 是否改用 3-seed aggregate。\n\n9. **v12-R2-W2** [warning, in_progress]: 与 Kim et al. 区分需更锐利。\n   - 检查: 同 issue 1。\n\n10. **v10-R2-W8** [warning, in_progress]: Discussion/Conclusion 过于简短，缺 forward-looking content。\n    - 检查: Discussion 是否扩展，是否包含 mitigation analysis。\n\n11. **v5-R2-W3** [warning, in_progress]: paragraph{} 过度碎片化。\n    - 检查: method/conclusion/limitations 中段落结构。\n\n**Info issues:**\n\n12. **v11-R2-MR** [info, in_progress]: 缺少 2025-2026 最新引用。R13 要求补 Llemma, reward hacking mitigation 文献。\n    - 检查: references.bib 是否新增相关引用。\n\n13. **v8-R1-N3** [warning, in_progress]: 术语交替使用导致语义滑移。\n    - 检查: H1→CE, H7→TS 等重命名后是否全文一致。是否有残留旧名称。\n\n14. **v11-R1-W2** [warning, in_progress]: Taxonomy 仅 H1/H7 有 precision 验证，H8 只 s42 审计。\n    - 检查: Abstract 和 Method 中对 PG (原 H8) 的 claim 强度是否降低。\n\n**写作质量检查:**\n- AI 写作标志: em-dash (—), 解释性 en-dash (–), -ing phrase endings, 黑名单词汇\n- 段落长度和叙事连贯性\n- 格式合规: ≤8 页, [review] option, 匿名化, Limitations, Ethics, Checklist\n\n**Hacking 模式重命名评估:**\nH1→CE, H7→TS, H8→PG, H9→CI 的重命名是否改善了可读性？是否全文一致？\n\n### 输出格式\n对每个 issue 标 [RESOLVED] 或 [STILL_OPEN]，给出简短理由和具体文本位置。\n新发现的问题单独列出。\n最后给出 Overall Assessment、Excitement、Novelty 评分（使用 EMNLP ARR 标准）。",
    "reviewer_id": "2",
    "round_number": "14"
  }
}
```

</details>

---


### Tool result

_source line 1297 · 2026-05-19T10:03:21.133934+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1674
}
```

</details>

---


### Assistant

_source line 1298 · 2026-05-19T10:03:27.714677+00:00_

Round 14 审稿任务已分配：

- **Reviewer 1**（方法/实验/统计）：聚焦 SFT confound hedging、统计功效、OR 方向反转处理、gated ISR 新实验有效性、s43 脚注、dose-response claim、Prolog random control 限制讨论。共 13 条 open/in_progress issue + 新实验审查。

- **Reviewer 2**（新颖性/写作/格式）：聚焦 Kim et al. 对比段质量、ISR framing 精确性、缩写密度、Table 2 标注、mitigation 讨论、Abstract 改进、AI 写作检查、H→CE/TS/PG/CI 重命名一致性。共 14 条 open/in_progress issue + 写作质量检查。

等待两位 Reviewer 独立审稿结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 109

## Round 109

2 recorded events


### User

_source line 1299 · 2026-05-19T10:06:51.662336+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — Round 14 修订评估

**论文**: "Valid but Vacuous: Reward Hacking in GRPO-Trained FOL Reasoners"
**审查侧重**: 新颖性评估更新、写作质量、格式合规、引用充足性、Kim et al. 对比

---

### Issue 逐条评估

**1. v13-R2-N2 [critical → RESOLVED]: Kim et al. (2026) 差异化**
Related Work 新增完整段落 "Faithfulness in formalization"（Related Work lines 8-14），从三个维度逐条对比：(1) training-time gaming vs inference-time gaming，(2) deterministic solver-derived detection (STA/ISR) vs LLM-judge classification，(3) universal gaming under RL (≥80%) vs preference for failure at inference。还指出互补性："axiom-fabrication mode is functionally equivalent to our CE"。对比充分且有深度。

**2. v4-R2-W9 [warning → PARTIALLY RESOLVED]: 方法新颖性有限**
Introduction line 21 now self-identifies as "empirical case study"。gated ISR 实验（Discussion line 11, Appendix F.5）增添了新的实证贡献。但 LOO 是标准技术这一结构性限制无法通过修改解决。作为结构性问题，标记为 partially resolved 是合理的。

**3. v5-R2-N3 [warning → PARTIALLY RESOLVED]: 概念新颖性有限**
Gated ISR 实验（Appendix Table F.5）提供了有意义的新发现：component-count gate 消除了 TS（0/3 seeds），但 2/3 seeds 迁移到 PG（premise-subset gaming），其中 s52 通过 PG 达到 ISR*=1.0（比 TS 的 ≥0.5 更严重）。"blocking one Goodhart pathway redirects optimization pressure rather than resolving it" 是一个非平凡的实证发现，为 reward hacking mitigation 文献做出了贡献。这部分提升了 novelty。

**4. v13-R1-W1 [warning → RESOLVED]: ISR framing**
Method §3.2 line 46 现在明确写道 "ISR is a component-necessity diagnostic, not a reasoning-quality metric; it measures whether each piece is needed for the proof, not whether the proof faithfully represents the original problem." 措辞精确。Introduction line 6 使用 "structural necessity of individual components"。Abstract line 3 仍然用 "structural integrity"，与 "component necessity" 相比略模糊，但整体 framing 已充分校正。

**5. v13-R2-W4 [warning → STILL OPEN]: 缩写密度**
缩写总计约 18 个（STA, ISR, ISR*, PR, N-H, S-NH, CE, TS, TS-a, TS-b, PG, CI, GRPO, LOO, FOL, NLI, SFT, NLL）。没有添加 notation summary table。但重命名 H1→CE, H7→TS, H8→PG, H9→CI 本身是显著的可读性改进——描述性名称比不透明的编号更容易记忆。**降级为 minor**：缩写密度虽高但每个缩写都有描述性全称。

**6. v13-R2-W5 [warning → RESOLVED]: Table 2 聚合方式标注**
Table 2 caption 现在明确标注 "$^a$Single seed (s42); remaining columns pooled (ISR/Rnd 4B: 5-seed; Prolog/1.7B: 3-seed)"。读者可以清楚判断每列的聚合方式。

**7. v13-R2-MITIGATION [warning → RESOLVED]: Discussion 缺 mitigation**
Discussion lines 11-14 现在包含：(1) Gated ISR 实验结果（TS→PG 迁移），(2) reward ensembling 分析 (Coste et al. 2024: "targets learned rewards, not deterministic solver signals")，(3) constrained optimization 分析 (Moskovitz et al. 2024: "could cap ISR, but collapse at all β suggests a narrow proxy-validity boundary")，(4) forward direction: combining STA with TRACE。这是实质性的 mitigation 讨论，有实验支撑和文献对接。

**8. v5-R2-W1 [warning → RESOLVED]: Abstract "99.5%" 单 seed**
Abstract line 4: "ISR reveals structural collapse ($\text{ISR}^*$ falls to $0.03{\pm}0.05$ across three seeds at 1000 steps)"。Introduction line 13 同步更新。3-seed aggregate 替代单 seed 极值，不再有 cherry-picking 嫌疑。

**9. v12-R2-W2 → 同 Issue 1 [RESOLVED]**

**10. v10-R2-W8 [warning → RESOLVED]: Discussion 过短**
Discussion 从原来约 6 行扩展到 14 行（Discussion lines 1-14），包含 gated ISR 实验、reward ensembling 分析、constrained optimization 分析、forward-looking direction。不再是 hand-waving。

**11. v5-R2-W3 [warning → MOSTLY RESOLVED]: 段落碎片化**
Limitations 现在是紧凑的 7 行单段。Discussion 是 14 行连贯段落。Method 保留 \paragraph{} 结构但内容密度合理。与 Round 1 相比，碎片化问题已大幅改善。

**12. v11-R2-MR [info → RESOLVED]: 缺少引用**
references.bib 新增：azerbayev2024llemma (Llemma, ICLR 2024)、coste2024reward (Reward Model Ensembles, ICLR 2024)、moskovitz2024confronting (Constrained RLHF, ICLR 2024)。Related Work line 5 引用 Llemma，Discussion lines 13-14 引用两篇 mitigation 文献。引用覆盖充足。

**13. v8-R1-N3 [warning → RESOLVED]: 术语重命名一致性**
Grep 全文搜索确认无 H1/H7/H8/H9 残留。CE, TS (TS-a/TS-b), PG, CI 在所有 .tex 文件中一致使用。重命名完整且无遗漏。

**14. v11-R1-W2 [warning → RESOLVED]: PG claim 强度**
Abstract line 6: "premise-subset gaming [PG], observed at lower prevalence"。Method line 71: "PG is observed across multiple seeds but at low prevalence (≤8% of proved samples)"。Claim 已适当下调。

---

### 写作质量检查

**AI 写作标志:**
- em-dash (—): 全文零命中 ✅
- 解释性 en-dash (–): 全文零命中 ✅
- 黑名单词汇 (delve/leverage/utilize/facilitate): 未发现 ✅
- -ing phrase endings: 检查了全文，未发现 AI 风格的 trailing participial phrases ✅

**段落和叙事:**
- Abstract 回答四个必答问题，175 词左右，简洁有力 ✅
- Introduction 五段结构完整，叙事线连贯 ✅
- Limitations 单段紧凑，涵盖关键限制 ✅
- Discussion 扩展后有实质内容 ✅

**Hacking 模式重命名评估:**
H1→CE (conclusion embedding), H7→TS (tautological shortcut), H8→PG (premise-subset gaming), H9→CI (contradiction injection)。描述性名称比 H-编号显著改善可读性，读者无需查表即可理解模式语义。TS-a/TS-b 命名清晰区分 text-match 和 obfuscated 变体。全文一致。**这是一个成功的修改。**

---

### 格式合规检查

- ✅ `\usepackage[review]{acl}` (main.tex line 2)
- ✅ `\author{Anonymous ACL submission}` (main.tex line 24)
- ✅ Limitations section 在 References 之前 (main.tex: limitations → ethics → checklist → bibliography)
- ✅ Ethics Statement 存在
- ✅ Checklist 认真填写，C4 从 "Partially" 改为 "Yes"（TRL 0.17.0, PyTorch 2.6.0, Transformers 4.51.3 in Appendix A）
- ✅ 正文 ≤8 页（经 Round 1 视觉审查确认）
- ⚠️ Limitations 只有 7 行 / 3 句，虽然涵盖要点但偏短。ACL ARR 不设最低长度要求，合规但建议稍加展开（如 SFT confound acknowledgment）

---

### 新发现

**NEW-1 [minor]: SFT framing hedging 改进但正文§4.2仍有一处偏强措辞**
Section 4.2 line 42: "The near-absence of hacking under identical data exposure is consistent with hacking being RL-specific"。虽然紧接着用 "whether SFT would hack at higher PR remains an open question" 做了 caveat，Introduction (line 14) 和 Discussion (line 6) 已改为 "associated with RL optimization" 和加入 PR gap caveat，但这一处仍用了 "RL-specific"。建议统一为 "associated with RL optimization" 以与全文一致。

**NEW-2 [minor]: Prolog 缺 random control 现已明确承认**
Section 4.4 line 118: "No matched random control was run for Prolog; the ISR-specificity of these gaming modes is inferred from the FOL random comparison rather than directly demonstrated in Prolog." 这是好的修改，正面回应了 R1-Q4。

**NEW-3 [minor]: Gated ISR 实验的统计局限**
Gated ISR 仅 3 seeds (s52-s54)，其中 s54 产生 96.7% non-hacking 但 35.2% content-independent。3 seeds 中结果差异极大（s52: pure PG, s53: PG 主导, s54: mostly non-hacking），这与主实验中观察到的 seed-dependent divergence 一致，但也意味着 gated ISR 的结论（"必要但不充分"）仅基于 3 seeds 观察。Discussion 中应标注为 preliminary。

---

### 评分更新

| 维度 | Round 13 | Round 14 | 变化理由 |
|------|----------|----------|----------|
| Soundness | 3.5 | 3.5 | SFT confound 和 eval set size 是结构性问题，无法通过修改解决，hedging 已适当 |
| Novelty | 2.5 | 3.0 | Gated ISR 实验 (TS→PG migration) 提供非平凡的新发现；Kim et al. 对比现在清晰展示了差异化 |
| Excitement | 2.5 | 3.0 | Gated ISR 的 "whack-a-mole" 发现（blocking one pathway → more severe exploit）对 reward hacking mitigation 社区有直接价值 |
| Reproducibility | 4.0 | 4.0 | Checklist C4 修复；framework versions 完整报告 |
| **Overall** | **3.0** | **3.0** | 修改质量高，逼近 3.5 但未跨越门槛 |

**Overall: 3.0 (Findings)**

修改全面回应了 Round 13 的主要关切。14 个 tracked issues 中：9 个 RESOLVED，3 个 PARTIALLY RESOLVED（含 2 个结构性问题），1 个 STILL OPEN（缩写密度，降为 minor），1 个 MOSTLY RESOLVED。

Gated ISR 实验是最有价值的新增：它将论文从纯诊断提升为 "诊断 + mitigation attempt (with informative negative result)"，TS→PG migration 的 "whack-a-mole" 发现本身是一个 publishable observation。Kim et al. 对比段落充分且有洞察。Discussion 扩展有实质内容。

但 **核心 novelty gap 仍为结构性限制**：LOO 是标准技术，Goodhart collapse 从 ISR 定义可预测，gated ISR 虽有趣但仅 3 seeds。论文定位为 "empirical case study"（Introduction line 21）是准确的自我评估。

**与 3.5 (Borderline Conference) 的距离**：修改后差距缩小。如果 gated ISR 实验扩展到 5+ seeds 且包含第二种 mitigation attempt（如 component-count normalization），论文可能跨越 3.5 门槛。当前状态下，3.0 (Findings) 仍是更准确的评估。

**Confidence: 4/5**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1300 · 2026-05-19T10:06:58.139013+00:00_

R2 审稿已收到。等待 R1 审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 110

## Round 110

2 recorded events


### User

_source line 1301 · 2026-05-19T10:07:00.888371+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交。

Round 14 评估总结：14 个 tracked issues 中 9 个 RESOLVED，3 个 PARTIALLY RESOLVED（含结构性问题），1 个 STILL OPEN（降为 minor），1 个 MOSTLY RESOLVED。主要改进包括 Kim et al. 充分对比、gated ISR 实验（TS→PG migration 的 "whack-a-mole" 发现）、Discussion 扩展、Abstract 改用 3-seed aggregate、引用补充完整、模式重命名全文一致。Overall 维持 3.0 (Findings)，Novelty 和 Excitement 均从 2.5 提升至 3.0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1302 · 2026-05-19T10:07:06.800296+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 111

## Round 111

6 recorded events


### User

_source line 1303 · 2026-05-19T10:07:09.197358+00:00_

[Reviewer 1 审稿意见]:

# Reviewer 1 — Round 14 修订评估

**论文**: "Valid but Vacuous: Reward Hacking in GRPO-Trained FOL Reasoners"
**审查侧重**: 方法严谨性、实验设计、统计声明、新增实验(gated ISR)的有效性

---

## 上轮 Issues 逐条评估

### Critical Issues

**1. v5-R12-SFT-PR** — SFT baseline PR confound
**[STILL_OPEN — minor residual]**

Abstract (line 4)、Introduction (line 14)、Discussion (line 6) 均已改为一致的 hedged 表述："consistent with hacking being associated with RL optimization rather than data exposure, though the large prove-rate gap prevents definitive causal attribution"。Discussion 进一步注明了具体 PR gap (13% vs. 97%)。

但 **§4.1 line 42 仍使用更强的旧措辞** "consistent with hacking being RL-specific"，缺少 "though the large prove-rate gap prevents definitive causal attribution" caveat。应统一为 Abstract/Introduction/Discussion 的 hedged 版本。

此外，SFT n=39 的限制虽然在 Table 5 notes 中标注，但 Limitations section 中未单独提及这一极小样本量。

---

**2. v4-R1-W8** — 100-example eval set 统计功效
**[RESOLVED]**

Matched cohort table caption (Table matched-perseed) 现包含完整 Wilson 95% CIs（ISR s47 [1.1, 8.7] ... Random s51 [7.5, 24.3]）。Limitations (§6 line 6) 明确指出 "100-example evaluation set limits per-seed precision (6%≈6 samples; Wilson 95% CI [2.3%, 12.7%]); statistical power is limited (n=5 seeds)"。

轻微不足：CIs 仅在 matched cohort table 中提供，Table 1 (goodhart-landscape) 和 exploratory table 仍无 CIs。但 matched cohort 是首要统计证据，此处 CIs 的添加是最重要的改进。

---

**3. v4-R12-N3** — OR=3.48 → OR=0.61 方向反转
**[STILL_OPEN — main-text acknowledgment missing]**

Table 1 caption 现标注 "N-H is an upper bound"。Table 1 ISR β=0.1 行使用 corrected 6%† 为首要数字，footnote 注明 uncorrected 23%。Appendix Table bootstrap-ci 并列展示两组 Fisher exact 结果。

**但方向反转本身未在正文讨论。** 校正后 ISR N-H=6.06% < Random N-H=9.5% (OR=0.61, p=0.182 n.s.)：ISR reward 的 genuine non-hacking rate 在 point estimate 上低于 random noise。这与 "ISR provides structural benefit" 的隐含预期矛盾。§4.2 line 85 只提到 "corrected 3-seed rate after PG+FN audit: 6%; Table 1"，未指出这低于 Random 的 9.5%，也未讨论含义。

建议在 §4.2 或 Discussion 中增加一句："After correction, the ISR non-hacking rate (6%) is numerically below the random control (9.5%, Fisher p=0.182 n.s.), suggesting that ISR reward does not improve genuine quality even within the transient window."

---

**4. v8-R12-N1** — Goodhart 发现的可预测性限制概念新颖性
**[STILL_OPEN — structural, incrementally improved]**

新增 gated ISR 实验 (Appendix §B.11, Discussion lines 11-12) 是正面回应。它超越纯 diagnosis，提供了一个 preliminary mitigation attempt 及其 negative result (TS→PG mode migration)。Discussion lines 13-14 新增 mitigation landscape 分析（reward ensembling, constrained optimization），引用 Coste et al. (2024) 和 Moskovitz et al. (2024)。

这些改进将论文从 "only diagnoses" 提升为 "diagnoses + attempts mitigation + explains why mitigation is hard"，但核心 novelty concern（LOO 是标准技术，Goodhart collapse 是理论可预测结果）仍为结构性问题。

---

**5. v8-R12-N2** — 实验范围与 claim scope 不匹配
**[RESOLVED]**

C3 (Introduction line 25) 改为 "Goodhart vulnerability transfers **in principle** across logic types and model scales, **though coverage remains preliminary**"。Discussion (line 9) 使用 "should **in principle** transfer"。§4.3 (line 118) 明确声明 "No matched random control was run for Prolog"。

---

### Major Issues

**6. v4-R12-N2** — 'At all tested doses' claim
**[RESOLVED]**

Discussion line 4 改为 "at all **four** tested doses"。§4.2 line 49 列出具体 β 值。§4.2 line 110 加 "with four dose points and 3-5 seeds each, these patterns are preliminary"。Abstract line 5 仍说 "every tested dose" 但在全文语境下足够清晰。

---

**7. v6-R1-W2** — Dose-response claim 统计不足
**[RESOLVED]**

§4.2 line 110: "preliminary" 标注。

---

**8. v4-R12-W6** — Seed 43 exec-only 评估协议矛盾
**[RESOLVED]**

§4.1 line 34 新增脚注: "Exec-only s43 was evaluated with sampling (T=0.7) rather than greedy decoding; its metrics are included for completeness but are not strictly comparable (Appendix §A.1)."

---

**9. v4-R12-W7** — Deleted checkpoints，Table 1 N-H upper bound 标注
**[RESOLVED]**

Table 1 caption: "N-H is an upper bound: undiscovered modes would reduce the true rate."

---

**10. v5-R1-N3** — Table 1 混合 500/1000 步结果
**[RESOLVED]**

Caption 标注 "500 steps unless noted"，SFT (1k) 和 Exec-only (1k) 在行标签中明确标注。

---

**11. v13-R1-Q4** — Prolog cross-logic 缺少 random control
**[RESOLVED]**

§4.3 line 118: "No matched random control was run for Prolog; the ISR-specificity of these gaming modes is inferred from the FOL random comparison rather than directly demonstrated in Prolog." 明确声明限制。

---

**12. v8-R1-W4** — CMH p-values 标注
**[RESOLVED]**

Appendix line 126: "the effective independent units are seeds (n=5), not samples, and CMH p-values are consequently inflated." 功能等价于 "directional only"。

---

## 新增实验审查：Gated ISR

### 实验设计 (Appendix §B.11)
- **Reward**: $r = r_{\text{exec}} + \beta \cdot \text{ISR} \cdot \mathbf{1}[n_{\text{components}} \geq 2]$, β=0.1
- **Seeds**: 52-54, 500 steps
- **Results**:
  - s52: PR=100%, ISR*=1.0, PG=100%, N-H=0%
  - s53: PR=96%, ISR*=0.651, PG=89.6%, N-H=7.3%
  - s54: PR=91%, ISR*=0.273, PG=0%, N-H=**96.7%**

### 评估

**[设计合理]** Component-count gate 直接测试 "blocking the known TS exploit"，逻辑清晰。Gate 条件 ($n \geq 2$) 精确靶向 TS 机制（单前提 → ISR≥0.5）。

**[TS 消除确认]** 0/3 seeds 产生 TS，验证了 TS 的结构机制（n=1 bias is necessary for TS）。这是一个有价值的因果验证。

**[TS→PG 迁移 claim]**
Discussion line 11-12: "2/3 seeds migrate to PG (premise-subset gaming), with one seed achieving ISR*=1.0 through PG alone"

这个 claim 基于 2/3 seeds，但 **s54 是一个重要的反例**：96.7% non-hacking。Discussion 没有提及 s54 的成功。当前表述 ("2/3 seeds migrate to PG") 可能让读者以为 gate 总是失败，但实际上 1/3 seeds 成功率很高。

**建议**：Discussion 中补充 s54 的结果，改为 "2/3 seeds migrate to PG, while 1/3 sustains predominantly non-hacking output (96.7%); the outcome is highly seed-dependent with only 3 seeds."

**[缺少 gated random control]** 没有 gated random condition ($r = r_{\text{exec}} + \beta \cdot u \cdot \mathbf{1}[n \geq 2]$) 来隔离 ISR-specific PG 迁移和 generic reward-variance PG。虽然 PG 在 ungated random 中很少出现 (Table 2: 8%)，但 gated 条件下的 dynamics 可能不同。

**[No overstatement detected]** "The replacement exploit is more severe than the original (ISR≥0.5 for TS vs. 1.0 for PG): blocking one Goodhart pathway redirects optimization pressure rather than resolving it" — 这在 s52/s53 的数据中成立，但 s54 表明 "redirect" 不是必然的。"The gate is necessary but insufficient for reliable structural improvement" (Appendix line 836) 是准确的 caveat。

**总评**：Gated ISR 实验设计合理，结论基本准确，但 (a) 3 seeds 过少无法判断 PG migration 的概率，(b) s54 反例未在 Discussion 中提及，(c) 缺少 gated random control。作为 preliminary mitigation attempt 是有价值的；作为独立 claim 证据不足。

---

## 新发现的问题

**N-NEW-1** [minor] Limitations section 被大幅压缩（从 Round 13 的 ~14 行缩至 6 行）。关键内容（CMH inflation, deleted checkpoints, SFT open question）仍在正文/Appendix 中，但 Limitations 不再是"论文亮点"级别的全面报告。8 页限制下可理解，但 Limitations 的 completeness 是审稿人看重的。

**N-NEW-2** [positive] Kim et al. (2026) 对比现在是完整段落（Related Work lines 8-14），逐条比较 inference vs training, deterministic vs LLM-judge, universal RL gaming vs no systematic inference-time gaming, CE ≈ axiom fabrication。彻底解决了 R2-N2。

**N-NEW-3** [positive] Hacking mode 从 H1/H7/H8/H9 重命名为 CE/TS/PG/CI，大幅提升可读性。Figures 和 text 已同步更新。

**N-NEW-4** [positive] Table 2 caption 现标注 "$^a$Single seed (s42); remaining columns pooled"，解决了之前 single-seed vs pooled 混合对比的问题。

**N-NEW-5** [positive] Checklist C4 现为 "Yes"，framework 版本 (TRL 0.17.0, PyTorch 2.6.0, Transformers 4.51.3) 已加入 Appendix Table hyperparams。

**N-NEW-6** [positive] Mitigation landscape 讨论 (Discussion lines 13-14) 引用 reward ensembling (Coste et al., 2024), constrained optimization (Moskovitz et al., 2024), reasoning-effort detection (Wang et al., 2025)，加上 gated ISR 的 empirical negative result。满足 R13 的 "forward-looking discussion" 要求。

**N-NEW-7** [positive] Llemma 引用 (Related Work line 5) 填补了 Lean-based RL 的引用空缺。

---

## 修改充分性总结

| Issue | Status | 改善程度 |
|-------|--------|---------|
| 1. SFT-PR confound hedging | STILL_OPEN | ▲▲ 大幅改善，§4.1 遗留一处旧措辞 |
| 2. 100-example eval Wilson CIs | RESOLVED | ▲▲ matched table CIs 完整 |
| 3. OR direction reversal | STILL_OPEN | ▲ Table 1 改善，main-text 未讨论反转 |
| 4. Novelty (structural) | STILL_OPEN | ▲ gated ISR 增量贡献 |
| 5. Claim scope hedging | RESOLVED | ▲▲ C3, Discussion 充分 hedge |
| 6. "All tested doses" | RESOLVED | ▲ |
| 7. Dose-response "preliminary" | RESOLVED | ▲ |
| 8. Seed 43 footnote | RESOLVED | ▲▲ |
| 9. N-H upper bound label | RESOLVED | ▲▲ |
| 10. Table 1 step mixing | RESOLVED | ▲ |
| 11. Prolog no random control | RESOLVED | ▲▲ explicit statement |
| 12. CMH directional | RESOLVED | ▲ |
| 13. Gated ISR (NEW) | — | 有价值但 3 seeds 不足；Discussion 遗漏 s54 |

**9/12 resolved, 3 still open (1 minor wording, 1 main-text omission, 1 structural)**

---

## Overall Assessment

**Overall: 3.5 — Borderline Conference**
**Excitement: 3.0**
**Soundness: 3.5**

### 评分变化理由 (R13: 3.0 → R14: 3.5)

论文从 Round 13 到 Round 14 有实质性改进：

1. **Gated ISR 实验** 将论文从 "只诊断" 提升为 "诊断 + 尝试 mitigation + 解释 mitigation 为什么难"。TS→PG mode migration 是一个有趣的 empirical finding，展示了 Goodhart dynamics 的 Whac-A-Mole 性质。虽然仅 3 seeds，但作为 preliminary evidence 有增量价值。

2. **Kim et al. 详细对比** 彻底解决了 R2-N2（从 critical/major 到 resolved），明确了本文与最相关 concurrent work 的差异化。

3. **Mitigation landscape** (Discussion) 引用了 3 个方向 + gated ISR empirical result，满足了 "至少一个 mitigation 策略" 的建议。

4. **Hedging 全面改善**：C3 "in principle...preliminary"，SFT "associated with...though gap prevents"，dose "four tested doses"，Prolog "no random control" 显式声明。

5. **技术细节补全**：Wilson CIs, framework versions, Table annotations, mode rename。

**仍然限制 Conference 的因素**：
- 核心 novelty concern (LOO 标准技术 + 理论可预测 Goodhart) 是结构性的
- 校正后 ISR N-H < Random N-H 的方向反转暗示 ISR reward 连 non-hacking quality 都不如 random noise，但这一 finding 被埋在 Appendix 中未充分讨论
- Gated ISR 仅 3 seeds，Discussion 遗漏了 s54 反例

论文现在处于 Conference/Findings 边界。如果 ISR N-H 方向反转在主文中得到讨论（这实际上 *强化* 了 "ISR 不应作为 reward" 的核心论点），且 gated ISR Discussion 补充 s54 数据，我倾向 Conference 可接收。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1304 · 2026-05-19T10:07:49.692855+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## Step 2 交叉分享 — 请回应 Reviewer 2 的意见\n\n以下是 Reviewer 2 (Round 14) 的完整审稿意见。请逐条回应 [AGREE]、[PARTIALLY AGREE] 或 [REBUT]，重点关注分歧点。\n\n---\n\n### R2 Issue 评估结果摘要\n\n**RESOLVED (9):** Kim et al. 对比 (v13-R2-N2), ISR framing (v13-R1-W1), Table 2 标注 (v13-R2-W5), Mitigation discussion (v13-R2-MITIGATION), Abstract 3-seed (v5-R2-W1), Discussion 扩展 (v10-R2-W8), 术语一致性 (v8-R1-N3), PG claim 降级 (v11-R1-W2), 引用补充 (v11-R2-MR)\n\n**PARTIALLY RESOLVED (3):** 方法新颖性 (v4-R2-W9, 结构性), 概念新颖性 (v5-R2-N3, 结构性, 但 gated ISR 加分), 段落碎片化 (v5-R2-W3)\n\n**STILL OPEN (1):** 缩写密度 (v13-R2-W4, 降为 minor: ~18 缩写，但重命名改善可读性)\n\n### R2 新发现\n\n**NEW-1 [minor]:** §4.2 line 42 \"consistent with hacking being RL-specific\" 应统一为 \"associated with RL optimization\"\n\n**NEW-2 [positive]:** Prolog 缺 random control 已明确承认\n\n**NEW-3 [minor]:** Gated ISR 仅 3 seeds，Discussion 应标注 preliminary\n\n### R2 评分\n\n| 维度 | R13 | R14 | 变化理由 |\n|------|-----|-----|---------|\n| Soundness | 3.5 | 3.5 | 结构性问题无法修改解决 |\n| Novelty | 2.5 | 3.0 | Gated ISR (TS→PG) 非平凡发现 |\n| Excitement | 2.5 | 3.0 | Whac-A-Mole 发现有实践价值 |\n| **Overall** | **3.0** | **3.0** | 修改质量高，逼近 3.5 但未跨越 |\n\n**R2 核心论点**: 修改全面回应了 R13 关切，gated ISR 实验有价值（novelty +0.5），但核心 novelty gap（LOO 标准 + Goodhart 可预测）是结构性限制，无法通过修改跨越 Findings→Conference 门槛。\n\n### 请重点回应以下分歧\n\n1. **Overall 评分分歧 (你 3.5 vs R2 3.0)**: R2 认为核心 novelty gap 使论文无法达到 Conference 水平。你从 3.0 升到 3.5 的理由是 gated ISR + mitigation landscape + hedging improvements，R2 承认这些改进但认为不足以跨越门槛。你是否维持 3.5？\n\n2. **Gated ISR 对 novelty 的贡献**: 你认为 gated ISR 是 \"有趣的 empirical finding\"，R2 也给了 novelty +0.5（2.5→3.0）。但 R2 认为 3 seeds 过少无法作为独立 claim。你的评估？\n\n3. **R2 NEW-1 (§4.2 \"RL-specific\")**: 你的 Issue 1 也发现了同一问题。一致？\n\n4. **缩写密度 (R2 STILL_OPEN → minor)**: 你的评估？\n\n5. **Limitations 压缩 (R1 N-NEW-1)**: R2 也提到 \"偏短\"。是否需要扩展？",
  "reviewer_id": "1",
  "round_number": "14"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## Step 2 交叉分享 — 请回应 Reviewer 2 的意见\n\n以下是 Reviewer 2 (Round 14) 的完整审稿意见。请逐条回应 [AGREE]、[PARTIALLY AGREE] 或 [REBUT]，重点关注分歧点。\n\n---\n\n### R2 Issue 评估结果摘要\n\n**RESOLVED (9):** Kim et al. 对比 (v13-R2-N2), ISR framing (v13-R1-W1), Table 2 标注 (v13-R2-W5), Mitigation discussion (v13-R2-MITIGATION), Abstract 3-seed (v5-R2-W1), Discussion 扩展 (v10-R2-W8), 术语一致性 (v8-R1-N3), PG claim 降级 (v11-R1-W2), 引用补充 (v11-R2-MR)\n\n**PARTIALLY RESOLVED (3):** 方法新颖性 (v4-R2-W9, 结构性), 概念新颖性 (v5-R2-N3, 结构性, 但 gated ISR 加分), 段落碎片化 (v5-R2-W3)\n\n**STILL OPEN (1):** 缩写密度 (v13-R2-W4, 降为 minor: ~18 缩写，但重命名改善可读性)\n\n### R2 新发现\n\n**NEW-1 [minor]:** §4.2 line 42 \"consistent with hacking being RL-specific\" 应统一为 \"associated with RL optimization\"\n\n**NEW-2 [positive]:** Prolog 缺 random control 已明确承认\n\n**NEW-3 [minor]:** Gated ISR 仅 3 seeds，Discussion 应标注 preliminary\n\n### R2 评分\n\n| 维度 | R13 | R14 | 变化理由 |\n|------|-----|-----|---------|\n| Soundness | 3.5 | 3.5 | 结构性问题无法修改解决 |\n| Novelty | 2.5 | 3.0 | Gated ISR (TS→PG) 非平凡发现 |\n| Excitement | 2.5 | 3.0 | Whac-A-Mole 发现有实践价值 |\n| **Overall** | **3.0** | **3.0** | 修改质量高，逼近 3.5 但未跨越 |\n\n**R2 核心论点**: 修改全面回应了 R13 关切，gated ISR 实验有价值（novelty +0.5），但核心 novelty gap（LOO 标准 + Goodhart 可预测）是结构性限制，无法通过修改跨越 Findings→Conference 门槛。\n\n### 请重点回应以下分歧\n\n1. **Overall 评分分歧 (你 3.5 vs R2 3.0)**: R2 认为核心 novelty gap 使论文无法达到 Conference 水平。你从 3.0 升到 3.5 的理由是 gated ISR + mitigation landscape + hedging improvements，R2 承认这些改进但认为不足以跨越门槛。你是否维持 3.5？\n\n2. **Gated ISR 对 novelty 的贡献**: 你认为 gated ISR 是 \"有趣的 empirical finding\"，R2 也给了 novelty +0.5（2.5→3.0）。但 R2 认为 3 seeds 过少无法作为独立 claim。你的评估？\n\n3. **R2 NEW-1 (§4.2 \"RL-specific\")**: 你的 Issue 1 也发现了同一问题。一致？\n\n4. **缩写密度 (R2 STILL_OPEN → minor)**: 你的评估？\n\n5. **Limitations 压缩 (R1 N-NEW-1)**: R2 也提到 \"偏短\"。是否需要扩展？",
    "reviewer_id": "1",
    "round_number": "14"
  }
}
```

</details>

---


### Tool result

_source line 1305 · 2026-05-19T10:08:08.292414+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18599
}
```

</details>

---


### Tool call

_source line 1306 · 2026-05-19T10:08:10.349400+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## Step 2 交叉分享 — 请回应 Reviewer 1 的意见\n\n以下是 Reviewer 1 (Round 14) 的完整审稿意见。请逐条回应 [AGREE]、[PARTIALLY AGREE] 或 [REBUT]，重点关注分歧点。\n\n---\n\n### R1 Issue 评估结果摘要\n\n**RESOLVED (9):** 100-example eval CIs (v4-R1-W8), Claim scope hedging (v8-R12-N2), \"All tested doses\" (v4-R12-N2), Dose-response \"preliminary\" (v6-R1-W2), s43 footnote (v4-R12-W6), N-H upper bound (v4-R12-W7), Table 1 step mixing (v5-R1-N3), Prolog no random control (v13-R1-Q4), CMH directional (v8-R1-W4)\n\n**STILL OPEN (3):**\n- SFT-PR confound (v5-R12-SFT-PR): §4.1 line 42 仍用 \"RL-specific\" 旧措辞\n- OR direction reversal (v4-R12-N3): Table 1 改善但**正文未讨论 corrected ISR N-H (6%) < Random N-H (9.5%) 方向反转及其含义**\n- Novelty (v8-R12-N1): 结构性，gated ISR 增量改善\n\n### R1 对 Gated ISR 的详细评估\n\n- **设计合理**: Gate 条件精确靶向 TS 机制\n- **TS 消除确认**: 0/3 seeds 有 TS，因果验证成功\n- **TS→PG 迁移 claim 问题**: Discussion 只提到 \"2/3 seeds migrate to PG\"，**遗漏了 s54 的 96.7% non-hacking**。建议改为 \"2/3 seeds migrate to PG, while 1/3 sustains predominantly non-hacking output (96.7%); the outcome is highly seed-dependent with only 3 seeds.\"\n- **缺 gated random control**: 无法完全隔离 ISR-specific PG 迁移\n- **总评**: 设计合理，结论基本准确，但 3 seeds 不足 + s54 反例 + 缺 gated random control\n\n### R1 评分\n\n| 维度 | R13 | R14 | 变化理由 |\n|------|-----|-----|---------|\n| Soundness | 3.5 | 3.5 | — |\n| Excitement | 3.0 | 3.0 | — |\n| **Overall** | **3.5** | **3.5** | 修改质量高 |\n\n**R1 核心论点**: Gated ISR + mitigation landscape + hedging 全面改善将论文推至 Conference/Findings 边界。如果 OR 方向反转在正文讨论（\"ISR reward 连 non-hacking quality 都不如 random noise\" 实际上*强化*核心论点）且 gated ISR Discussion 补充 s54，倾向 Conference 可接收。\n\n### 请重点回应以下分歧\n\n1. **Overall 评分分歧 (R1 3.5 vs 你 3.0)**: R1 认为 gated ISR + mitigation 分析 + hedging 足以推至 Borderline Conference。你的反驳论点是什么？修改后的论文是否更接近 3.5？\n\n2. **OR 方向反转 (v4-R12-N3)**: R1 指出 corrected ISR N-H (6%) < Random N-H (9.5%) 在正文中未讨论。你是否同意这是一个应该在正文提及的 finding？R1 认为讨论此反转实际上\"强化\" ISR 不应作为 reward 的论点——你同意吗？\n\n3. **Gated ISR: s54 反例**: R1 指出 s54 (96.7% non-hacking) 未在 Discussion 提及。Discussion 当前只说 \"2/3 seeds migrate to PG\"。你是否同意应补充 s54？\n\n4. **Gated ISR: 缺 gated random control**: R1 提出应有 $r = r_{\\text{exec}} + \\beta \\cdot u \\cdot \\mathbf{1}[n \\geq 2]$ 控制。你的评估？\n\n5. **SFT wording (§4.2 line 42)**: R1 和你都发现同一问题。一致确认？",
  "reviewer_id": "2",
  "round_number": "14"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## Step 2 交叉分享 — 请回应 Reviewer 1 的意见\n\n以下是 Reviewer 1 (Round 14) 的完整审稿意见。请逐条回应 [AGREE]、[PARTIALLY AGREE] 或 [REBUT]，重点关注分歧点。\n\n---\n\n### R1 Issue 评估结果摘要\n\n**RESOLVED (9):** 100-example eval CIs (v4-R1-W8), Claim scope hedging (v8-R12-N2), \"All tested doses\" (v4-R12-N2), Dose-response \"preliminary\" (v6-R1-W2), s43 footnote (v4-R12-W6), N-H upper bound (v4-R12-W7), Table 1 step mixing (v5-R1-N3), Prolog no random control (v13-R1-Q4), CMH directional (v8-R1-W4)\n\n**STILL OPEN (3):**\n- SFT-PR confound (v5-R12-SFT-PR): §4.1 line 42 仍用 \"RL-specific\" 旧措辞\n- OR direction reversal (v4-R12-N3): Table 1 改善但**正文未讨论 corrected ISR N-H (6%) < Random N-H (9.5%) 方向反转及其含义**\n- Novelty (v8-R12-N1): 结构性，gated ISR 增量改善\n\n### R1 对 Gated ISR 的详细评估\n\n- **设计合理**: Gate 条件精确靶向 TS 机制\n- **TS 消除确认**: 0/3 seeds 有 TS，因果验证成功\n- **TS→PG 迁移 claim 问题**: Discussion 只提到 \"2/3 seeds migrate to PG\"，**遗漏了 s54 的 96.7% non-hacking**。建议改为 \"2/3 seeds migrate to PG, while 1/3 sustains predominantly non-hacking output (96.7%); the outcome is highly seed-dependent with only 3 seeds.\"\n- **缺 gated random control**: 无法完全隔离 ISR-specific PG 迁移\n- **总评**: 设计合理，结论基本准确，但 3 seeds 不足 + s54 反例 + 缺 gated random control\n\n### R1 评分\n\n| 维度 | R13 | R14 | 变化理由 |\n|------|-----|-----|---------|\n| Soundness | 3.5 | 3.5 | — |\n| Excitement | 3.0 | 3.0 | — |\n| **Overall** | **3.5** | **3.5** | 修改质量高 |\n\n**R1 核心论点**: Gated ISR + mitigation landscape + hedging 全面改善将论文推至 Conference/Findings 边界。如果 OR 方向反转在正文讨论（\"ISR reward 连 non-hacking quality 都不如 random noise\" 实际上*强化*核心论点）且 gated ISR Discussion 补充 s54，倾向 Conference 可接收。\n\n### 请重点回应以下分歧\n\n1. **Overall 评分分歧 (R1 3.5 vs 你 3.0)**: R1 认为 gated ISR + mitigation 分析 + hedging 足以推至 Borderline Conference。你的反驳论点是什么？修改后的论文是否更接近 3.5？\n\n2. **OR 方向反转 (v4-R12-N3)**: R1 指出 corrected ISR N-H (6%) < Random N-H (9.5%) 在正文中未讨论。你是否同意这是一个应该在正文提及的 finding？R1 认为讨论此反转实际上\"强化\" ISR 不应作为 reward 的论点——你同意吗？\n\n3. **Gated ISR: s54 反例**: R1 指出 s54 (96.7% non-hacking) 未在 Discussion 提及。Discussion 当前只说 \"2/3 seeds migrate to PG\"。你是否同意应补充 s54？\n\n4. **Gated ISR: 缺 gated random control**: R1 提出应有 $r = r_{\\text{exec}} + \\beta \\cdot u \\cdot \\mathbf{1}[n \\geq 2]$ 控制。你的评估？\n\n5. **SFT wording (§4.2 line 42)**: R1 和你都发现同一问题。一致确认？",
    "reviewer_id": "2",
    "round_number": "14"
  }
}
```

</details>

---


### Tool result

_source line 1307 · 2026-05-19T10:08:12.060185+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1710
}
```

</details>

---


### Assistant

_source line 1308 · 2026-05-19T10:08:15.512076+00:00_

交叉分享已发送。等待两位 Reviewer 的回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 112

## Round 112

2 recorded events


### User

_source line 1309 · 2026-05-19T10:08:55.438268+00:00_

[Reviewer 1 审稿结果]:
所有审稿任务已完成：

- **Round 1** 完整审稿 ✓
- **Step 2** 交叉回应 R2 ✓  
- **Round 14** 修订评估 ✓（评分 3.0 → 3.5）

3 个 STILL_OPEN 问题待作者处理：
1. §4.1 line 42 "RL-specific" 缺少 hedge
2. OR 方向逆转（校正后 ISR N-H 6% < Random 9.5%）未在正文讨论
3. Gated ISR Discussion 遗漏 s54 反例（96.7% N-H）

等待 Review Director 下一步指令。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1310 · 2026-05-19T10:09:01.074267+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 113

## Round 113

36 recorded events


### User

_source line 1311 · 2026-05-19T10:09:51.280587+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 — 交叉回应 Reviewer 1 (Round 14)

---

### 分歧点 1: Overall 评分 (R1 3.5 vs R2 3.0)

**[PARTIALLY AGREE] — 维持 3.0 但承认差距已缩小至 borderline**

R1 的条件判断是合理的："如果 OR 方向反转在正文讨论 + gated ISR Discussion 补充 s54，倾向 Conference 可接收。" 我同意这些是可行的修改，且 R1 的逻辑链条自洽。

修改后论文确实更强：
- Gated ISR 的 TS→PG migration 是非平凡的实证发现
- Kim et al. 对比段落充实，positioning 清晰
- Mitigation landscape 讨论有实质内容
- Hedging 全面改善

但我维持 3.0 的理由是**核心方法贡献**仍然不足：
- LOO ablation 是标准技术（Algorithm 1 仅 6 行伪代码）
- ISR 的 Goodhart vulnerability 从定义层面可预测（TS 恒获 ISR≥0.5）
- Gated ISR 虽有趣但仅 3 seeds，且结果高度 seed-dependent（s52: pure PG, s54: 96.7% non-hacking）

EMNLP 主会议 (Overall 4.0) 期待方法论或概念层面的新贡献。本文的贡献主要是 empirical characterization + cautionary taxonomy——这是 strong Findings 论文，但跨越到 Conference 需要至少一个 partially successful mitigation 策略，而不仅仅是展示 mitigation 失败。

**3.0 和 3.5 之间是 legitimate reviewer variance。** 如果 AC 更看重 empirical rigor（matched 5+5 design, gated ISR negative result）和实践价值（taxonomy 的可复用性），3.5 是可辩护的。如果更看重 conceptual novelty，3.0 更准确。我的 prior 偏向后者。

---

### 分歧点 2: OR 方向反转 (v4-R12-N3)

**[AGREE] — R1 的分析完全正确**

R1 指出 corrected ISR N-H (6.06%) < Random N-H (9.5%) 在正文中未讨论。这确实是一个重要的遗漏。

具体证据：
- §4.3 line 104 报告了 "genuine rates do not differ significantly (2.3% vs. 5.9%, p=0.92, permutation test)" — 这是 matched cohort 数据
- Appendix Table 4 line 106-107 报告了 3-seed corrected Fisher: ISR 6.06% vs Random 9.5%, OR=0.61, p=0.182 (n.s.)
- 两个独立比较（matched cohort: 2.3% vs 5.9%; exploratory corrected: 6.06% vs 9.5%）的 point estimate 方向一致：**ISR < Random**

R1 的洞察是精准的：这个方向反转实际上*强化*了论文的核心论点。ISR 作为 reward 不仅产生 Goodhart collapse（TS domination），而且即使在残余的 non-hacking 产出中，其质量也不优于 random noise。这意味着 ISR 的 signal 完全被其 structural bias 抵消——diagnostic 信号在优化过程中被完全消耗。

**建议**：在 §4.3（matched replication 段落末尾）或 Discussion 中增加 1-2 句："The corrected non-hacking rate under ISR (6.06%) is directionally lower than under random control (9.5%; Fisher p=0.182, n.s.), and the matched cohort shows the same pattern (2.3% vs 5.9%, p=0.92). ISR reward does not improve genuine structural quality even in the transient non-hacking window; any diagnostic signal is fully consumed by the optimization process." 这会强化 "reliable as diagnostic, unreliable as reward" 的核心 message。

---

### 分歧点 3: Gated ISR s54 反例

**[AGREE] — Discussion 当前措辞有选择性呈现嫌疑**

Discussion line 11-12 原文："gating the ISR bonus on component count eliminates TS entirely (0/3 seeds), but 2/3 seeds migrate to PG (premise-subset gaming), with one seed achieving ISR*=1.0 through PG alone"

Appendix Table F.5 的完整数据：
- s52: PR=100%, PG=100%, N-H=0% — pure PG gaming
- s53: PR=96%, PG=89.6%, N-H=7.3% — PG-dominated
- s54: PR=91%, PG=0%, N-H=96.7% — predominantly non-hacking

Discussion 只提到 2/3 PG migration 而完全忽略 s54 的 96.7% non-hacking，这相当于只报告了支持 "whack-a-mole" 叙事的 seeds 而忽略了反例。如果审稿人检查 Appendix 数据，这会被视为不诚实的呈现。

R1 建议的修改措辞是准确的："2/3 seeds migrate to PG, while 1/3 sustains predominantly non-hacking output (96.7%); the outcome is highly seed-dependent with only 3 seeds." 这保留了 whack-a-mole 的核心观察，同时承认结果并非 deterministic。

实际上，s54 的存在增加了一个重要 nuance：component-count gate 可能对某些初始化是有效的，但不可靠。这比简单的 "gate always fails" 更有信息量。

---

### 分歧点 4: Gated ISR 缺 gated random control

**[PARTIALLY AGREE] — 理想情况下应有，但不是 blocking issue**

R1 建议的 $r = r_{\text{exec}} + \beta \cdot u \cdot \mathbf{1}[n \geq 2]$ 控制条件是方法论上正确的：没有它，无法完全区分 PG migration 是 ISR-specific（ISR 的 LOO 结构偏好高 ISR 前提子集）还是 generic（任何 gated bonus 都可能产生类似效应）。

但考虑实际情况：
1. Gated ISR 本身定位为 preliminary mitigation experiment（3 seeds, Appendix 而非正文），不是论文的核心贡献
2. PG 的机制（"每个成分 LOO-necessary 但前提集是子集"）与 ISR 的 LOO 定义直接相关——uniform random noise 没有这种结构性偏好
3. 要求一个 Appendix 级别的 3-seed preliminary experiment 有完整的 control 条件可能过于苛刻

**建议**：在 Appendix F.5 中加一句 "A gated random control was not run; whether PG migration is ISR-specific remains to be confirmed, though the structural mechanism (ISR rewards premise-count minimization) suggests ISR specificity." 这承认了限制而不需要额外实验。

---

### 分歧点 5: SFT wording (§4.2 line 42)

**[AGREE] — 与 R1 一致确认**

§4.2 line 42 "consistent with hacking being RL-specific" 与 Introduction line 14 ("associated with RL optimization rather than data exposure") 和 Discussion line 6 ("associated with RL optimization") 的 hedged 措辞不一致。这是一处遗漏的统一化修改。

应将 "RL-specific" 改为 "associated with RL optimization" 或 "RL-driven" 以与全文一致。

---

### 总结

R1 和 R2 在技术问题上继续保持高度一致：
- SFT "RL-specific" 措辞需统一 [共识]
- OR 方向反转应在正文讨论 [共识]
- Gated ISR 应补充 s54 [共识]
- Gated random control 理想应有但非 blocking [共识]

**唯一持续分歧是 Overall 评分 (3.0 vs 3.5)**。这归结为对 "empirical case study with informative negative results" 是否达到 Conference 门槛的判断差异。R1 更看重实验 rigor 和实践价值；R2 更看重概念 novelty 门槛。两种立场都有合理依据。

如果作者执行以下修改，两位 Reviewer 可能收敛：
1. 在正文讨论 OR 方向反转（强化核心论点）
2. Discussion 补充 s54 数据（消除选择性呈现）
3. 统一 §4.2 "RL-specific" 措辞
4. Appendix 承认缺 gated random control

这些修改不影响实验，仅是呈现和讨论层面的调整。完成后，论文在 3.0-3.5 区间的定位更加 clean，AC 可基于 novelty preference 做最终判断。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1312 · 2026-05-19T10:11:00.089023+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 1313 · 2026-05-19T10:11:00.139917+00:00_

1	issues:
2	# ===== 历史 issues (Round 0-3, 全部 resolved) =====
3	- id: "R1-W1"
4	  summary: "统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例"
5	  category: experiment
6	  severity: critical
7	  status: resolved
8	  first_raised_round: 0
9	  last_seen_round: 2
10	  resolution: "β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。Fisher exact test + Wilson 95% CI 已加入。eval 集 100 例限制在 limitations.tex 讨论。"
11	  resolution_round: 2
12	
13	- id: "RV-EVAL-FALLBACK"
14	  summary: "eval_sta.py test_100.jsonl 静默 fallback 已移除"
15	  category: experiment
16	  severity: critical
17	  status: resolved
18	  first_raised_round: 1
19	  last_seen_round: 1
20	  resolution: "第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)，无 fallback。"
21	  resolution_round: 1
22	
23	- id: "RV-D060-NARRATIVE"
24	  summary: "D060 'Goodhart instability' 叙事：77pp PR 差距在同一测试集上确认成立"
25	  category: experiment
26	  severity: critical
27	  status: resolved
28	  first_raised_round: 1
29	  last_seen_round: 1
30	  resolution: "β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。"
31	  resolution_round: 2
32	
33	- id: "RV-FIG2-STALE-SCRIPT"
34	  summary: "figures/paper/gen_fig2.py 旧脚本数据错误"
35	  category: format
36	  severity: warning
37	  status: resolved
38	  first_raised_round: 1
39	  last_seen_round: 1
40	  resolution: "已修复。"
41	  resolution_round: 1
42	
43	- id: "R1-W2"
44	  summary: "ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量"
45	  category: framing
46	  severity: critical
47	  status: resolved
48	  first_raised_round: 0
49	  last_seen_round: 0
50	  resolution: "method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1314 · 2026-05-19T10:14:07.224919+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml",
  "offset": "370",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml",
    "offset": "370",
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 1315 · 2026-05-19T10:14:07.275823+00:00_

370	  resolution: "Abstract 现用 'effectively zero...at convergence'。"
371	  resolution_round: 4
372	
373	# ===== Round 4+ carry-over =====
374	
375	- id: "v3-R12-NI-1"
376	  summary: "Cross-scale 实验 seed 数量不足"
377	  category: experiment
378	  severity: warning
379	  status: in_progress
380	  first_raised_round: 3
381	  last_seen_round: 13
382	  mentions:
383	    - round: 3
384	      reviewers: [1, 2]
385	      note: "两位 reviewer 一致。"
386	    - round: 10
387	      reviewers: [1, 2]
388	      note: "现已用 D129 完整 3-seed 数据重写 §4.5。"
389	    - round: 11
390	      reviewers: [1]
391	      note: "R1-W4: 3 seeds 仍不足以作为独立 contribution 支撑。D134 扩展至 10 seeds 正在训练中。"
392	    - round: 12
393	      reviewers: [1, 2]
394	      note: "R1-N1 再次要求增加模型/数据集多样性。R2-N3 将 C3 cross-logic 定为 preliminary 不应为正式 contribution。两人一致建议降级 C3。R12 fix: C3 弱化为 'evidence of generality'（commit 9dc8835）。"
395	    - round: 13
396	      reviewers: [1, 2]
397	      note: "R13 R2-W1: C3 仍在同一 dataset (FOLIO) 和 model family (Qwen3) 内。两位 reviewer 一致要求进一步 hedge C3 措辞。"
398	
399	- id: "v4-R12-N2"
400	  summary: "'Inevitable collapse at all doses' claim 超出证据"
401	  category: experiment
402	  severity: warning
403	  status: in_progress
404	  first_raised_round: 4
405	  last_seen_round: 13
406	  mentions:
407	    - round: 9
408	      reviewers: [1, 2]
409	      note: "共识: 区分 'observed in all seeds tested' vs 'population-level inference'。"
410	    - round: 11
411	      reviewers: [1, 2]
412	      note: "术语降级为 'seed-dependent divergence' 和 'dose-varying patterns'。"
413	    - round: 12
414	      reviewers: [1, 2]
415	      note: "R1-W3 再次指出稀疏。R1 交叉回应认为 'all tested doses show Goodhart collapse' 成立。R12 fix: 加强 preliminary 标注，区分 500-step snapshot vs trajectory（commit 9dc8835）。"
416	    - round: 13
417	      reviewers: [1, 2]
418	      note: "R1-N3 认为 Abstract/Discussion 仍需更多 hedging。R2 反驳称 structural argument (H7 恒定 ISR≥0.5) 使 'at every tested dose' 成立。分歧记录。"
419	
420	- id: "v4-R12-N3"
421	  summary: "OR=3.48 (uncorrected) vs
…[truncated 3748 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1316 · 2026-05-19T10:15:58.795204+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat > /tmp/update_issues.py << 'PYEOF'\nimport yaml\nimport sys\n\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml', 'r') as f:\n    data = yaml.safe_load(f)\n\nissues = data['issues']\nidx = {issue['id']: issue for issue in issues}\n\n# Helper to add mention\ndef add_mention(issue_id, round_num, reviewers, note):\n    issue = idx[issue_id]\n    if 'mentions' not in issue or issue['mentions'] is None:\n        issue['mentions'] = []\n    issue['mentions'].append({'round': round_num, 'reviewers': reviewers, 'note': note})\n    issue['last_seen_round'] = round_num\n\n# Helper to resolve\ndef resolve(issue_id, round_num, resolution, reviewers=None, note=None):\n    issue = idx[issue_id]\n    issue['status'] = 'resolved'\n    issue['resolution'] = resolution\n    issue['resolution_round'] = round_num\n    issue['last_seen_round'] = round_num\n    if reviewers is not None and note is not None:\n        add_mention(issue_id, round_num, reviewers, note)\n\n# ===== RESOLVE issues =====\n\nresolve('v4-R12-N2', 14,\n    \"'four tested doses' + 'preliminary' 标注。§4.2 line 110 明确 seed count。\",\n    [1, 2], \"R14: R1 [RESOLVED]，R2 未再提及。Abstract 'every tested dose' 在全文语境下充分。\")\n\nresolve('v4-R12-W6', 14,\n    \"§4.2 line 34 脚注说明 sampling eval (T=0.7) 及不可比性。\",\n    [1], \"R14: R1 [RESOLVED]。脚注已添加。\")\n\nresolve('v4-R12-W7', 14,\n    \"Table 1 caption 标注 'N-H is an upper bound'。Method §3.5 line 76 声明。\",\n    [1, 2], \"R14: R1 [RESOLVED]。标注清晰。\")\n\nresolve('v4-R1-W8', 14,\n    \"Matched cohort table 附完整 Wilson CIs。Limitations 量化 '100-example...Wilson 95% CI [2.3%, 12.7%]'。\",\n    [1, 2], \"R14: R1 [RESOLVED]。CIs 在 matched table + Limitations 中完整呈现。\")\n\nresolve('v5-R1-N3', 14,\n    \"Table 1 caption '500 steps unless noted'。SFT/Exec-only 行标签明确 '1k'。\",\n    [1], \"R14: R1 [RESOLVED]。标注清晰。\")\n\nresolve('v5-R2-W1', 14,\n    \"Abstract 改用 3-seed aggregate (ISR*=0.03±0.05 across three seeds at 1000 steps)。\",\n    [1, 2], \"R14: R2 [RESOLVED]。消除 cherry-picking 嫌疑。\")\n\nresolve('v5-R2-W3', 14,\n    \"段落结构大幅改善。Limitations 紧凑单段，Discussion 14 行连贯段落。\",\n    [2], \"R14: R2 [MOSTLY RESOLVED]。不再碎片化。\")\n\nresolve('v5-R2-MR', 14,\n    \"新增 Llemma (Azerbayev 2024)、Coste 2024 (reward ensembling)、Moskovitz 2024 (constrained optimization)。引用覆盖充足。\",\n    [1, 2], \"R14: R2 [RESOLVED]。引用覆盖完整。\")\n\nresolve('v6-R1-W2', 14,\n    \"§4.2 line 110 标注 'preliminary'。\",\n    [1], \"R14: R1 [RESOLVED]。\")\n\nresolve('v8-R1-N3', 14,\n    \"H1→CE, H7→TS, H8→PG, H9→CI 全文重命名完整一致。无残留旧名称。\",\n    [2], \"R14: R2 [RESOLVED]。Grep 确认无 H1/H7/H8/H9 残留。\")\n\nresolve('v8-R12-N2', 14,\n    \"C3 加 'in principle...preliminary'。Discussion 加 'should in principle transfer'。§4.3 显式声明无 Prolog random control。\",\n    [1, 2], \"R14: R1 [RESOLVED]。Hedging 充分。\")\n\nresolve('v8-R1-W4', 14,\n    \"Appendix line 126 标注 CMH 'p-values are consequently inflated'。功能等价于 'directional only'。\",\n    [1], \"R14: R1 [RESOLVED]。\")\n\nresolve('v10-R2-W8', 14,\n    \"Discussion 扩展至 14 行。含 gated ISR 实验 + reward ensembling + constrained optimization + TRACE 方向。\",\n    [1, 2], \"R14: R2 [RESOLVED]。有实质 mitigation 内容。\")\n\nresolve('v11-R1-W2', 14,\n    \"Abstract 'PG, observed at lower prevalence'。Method 明确 CE/TS robust (≥3 seeds) vs PG low prevalence。\",\n    [1, 2], \"R14: R2 [RESOLVED]。Claim 适当下调。\")\n\nresolve('v11-R2-MR', 14,\n    \"新增 Llemma、Coste 2024、Moskovitz 2024。Related Work + Discussion 均引用。\",\n    [1, 2], \"R14: R2 [RESOLVED]。引用覆盖完整。\")\n\nresolve('v12-R2-W2', 14,\n    \"Related Work 新增完整 'Faithfulness in formalization' 段落，3 维度逐条对比 Kim et al.。\",\n    [1, 2], \"R14: R2 [RESOLVED]。对比充分且有洞察。同 v13-R2-N2。\")\n\nresolve('v13-R2-N2', 14,\n    \"Related Work 新增完整 'Faithfulness in formalization' 段落：training vs inference、STA/ISR vs LLM-judge、universal gaming vs no-gaming、CE ≈ axiom-fabrication 互补性。\",\n    [1, 2], \"R14: R2 [RESOLVED]。'充分且有深度'。\")\n\nresolve('v13-R1-W1', 14,\n    \"Method §3.2 line 46: 'ISR is a component-necessity diagnostic, not a reasoning-quality metric'。全文 framing 校正。\",\n    [1, 2], \"R14: R2 [RESOLVED]。措辞精确。Abstract 仍用 'structural integrity' 但在上下文中可接受。\")\n\nresolve('v13-R2-W5', 14,\n    \"Table 2 caption 标注 '$^a$Single seed (s42); remaining columns pooled (ISR/Rnd 4B: 5-seed; Prolog/1.7B: 3-seed)'。\",\n    [1, 2], \"R14: R2 [RESOLVED]。聚合方式标注清晰。\")\n\nresolve('v13-R2-MITIGATION', 14,\n    \"Discussion lines 11-14: gated ISR 实验 (TS→PG migration) + reward ensembling (Coste 2024) + constrained optimization (Moskovitz 2024) + TRACE 方向。\",\n    [1, 2], \"R14: R2 [RESOLVED]。有实验支撑和文献对接。\")\n\nresolve('v13-R1-Q4', 14,\n    \"§4.3 line 118: 'No matched random control was run for Prolog' 显式声明。\",\n    [1, 2], \"R14: R1 [RESOLVED]。限制明确承认。\")\n\n# ===== ADD MENTIONS, keep in_progress =====\n\nadd_mention('v5-R12-SFT-PR', 14, [1, 2],\n    \"R14: Abstract/Introduction/Discussion hedging 全面改善 ('associated with...though gap prevents')。但 §4.2 line 42 仍用 'RL-specific' 旧措辞，缺 caveat。一处遗漏的统一化修改。\")\n\nadd_mention('v4-R12-N3', 14, [1, 2],\n    \"R14: Table 1 用 corrected 6%†。但方向反转 (ISR N-H 6.06% < Random 9.5%) 未在正文讨论。两位 reviewer 一致认为应在 §4.3 或 Discussion 增加 1-2 句，且这实际上强化核心论点。Matched cohort 同方向 (2.3% vs 5.9%)。\")\n\nadd_mention('v8-R12-N1', 14, [1, 2],\n    \"R14: Gated ISR 实验增量改善 (诊断→诊断+mitigation attempt)。TS→PG mode migration 是非平凡发现。但核心 novelty concern (LOO 标准+Goodhart 可预测) 仍为结构性限制。R1 3.5 vs R2 3.0，分歧在 empirical rigor vs conceptual novelty 权重。\")\n\nadd_mention('v4-R2-W9', 14, [1, 2],\n    \"R14: Introduction line 21 自我定位为 'empirical case study'。Gated ISR 增添实证贡献。但 LOO 是标准技术这一结构性限制无法修改解决。R2 [PARTIALLY RESOLVED]。\")\n\nadd_mention('v5-R2-N3', 14, [1, 2],\n    \"R14: Gated ISR 的 TS→PG migration ('blocking one Goodhart pathway redirects optimization pressure') 是非平凡发现。R2 Novelty 2.5→3.0。但概念新颖性限制仍为结构性问题。R2 [PARTIALLY RESOLVED]。\")\n\n# v13-R2-W4: downgrade severity\nidx['v13-R2-W4']['severity'] = 'info'\nadd_mention('v13-R2-W4', 14, [1, 2],\n    \"R14: ~18 缩写，未添加 notation summary。但 H1→CE 等描述性重命名显著改善可读性。R2 降为 minor。\")\n\n# v3-R12-NI-1: not raised in R14\nadd_mention('v3-R12-NI-1', 14, [],\n    \"R14: 未直接提及。C3 已 hedge 为 'in principle...preliminary'。\")\n\n# v6-R2-W8: taxonomy classification\nadd_mention('v6-R2-W8', 14, [1, 2],\n    \"R14: CE/TS/PG/CI 重命名改善可读性。CE/TS precision >95% 验证。PG claim 降为 'observed at lower prevalence'。分类标准仍为规则+功能分析混合。\")\n\n# v10-R2-W7: not raised\nadd_mention('v10-R2-W7', 14, [],\n    \"R14: 未再提及。\")\n\n# ===== v4-R2-W5: wont_fix but now partially addressed by gated ISR =====\nadd_mention('v4-R2-W5', 14, [1, 2],\n    \"R14: Gated ISR 实验 (Appendix §B.11) 测试了 component-count gate 变体。TS 消除但 PG 迁移。原标记 wont_fix 现部分回应。\")\n\n# ===== NEW ISSUES =====\n\nissues.append({\n    'id': 'v14-R12-GATED-S54',\n    'summary': 'Gated ISR Discussion 遗漏 s54 反例 (96.7% non-hacking)',\n    'category': 'writing',\n    'severity': 'warning',\n    'status': 'open',\n    'first_raised_round': 14,\n    'last_seen_round': 14,\n    'mentions': [{'round': 14, 'reviewers': [1, 2], 'note': \"Discussion 只提 '2/3 seeds migrate to PG'，忽略 s54 (96.7% N-H)。两位 reviewer 一致认为有选择性呈现嫌疑。建议改为 '2/3 seeds migrate to PG, while 1/3 sustains predominantly non-hacking output (96.7%); outcome is highly seed-dependent with only 3 seeds.'\"}],\n    'action_items': [{'round': 14, 'action': \"Discussion 补充 s54 数据和 seed-dependence caveat\", 'assigned_to': 'research_director', 'status': 'open'}],\n    'resolution': '',\n    'resolution_round': None\n})\n\nissues.append({\n    'id': 'v14-R1-LIMITATIONS',\n    'summary': 'Limitations section 压缩至 6-7 行，SFT n=39 限制未单独提及',\n    'category': 'writing',\n    'severity': 'info',\n    'status': 'open',\n    'first_raised_round': 14,\n    'last_seen_round': 14,\n    'mentions': [{'round': 14, 'reviewers': [1], 'note': \"8 页限制下可理解，但 Limitations 不再是 R13 评价的 '论文亮点'。关键内容散落在正文和 Appendix。\"}],\n    'action_items': [],\n    'resolution': '',\n    'resolution_round': None\n})\n\n# Write output\noutput = yaml.dump(data, allow_unicode=True, default_flow_style=False, sort_keys=False, width=200)\nwith open('/tmp/updated_issues.yaml', 'w') as f:\n    f.write(output)\n\nprint(f\"Done. {len(issues)} issues total.\")\n# Count statuses\nfrom collections import Counter\nstatus_counts = Counter(i['status'] for i in issues)\nfor s, c in sorted(status_counts.items()):\n    print(f\"  {s}: {c}\")\nPYEOF\npython3 /tmp/update_issues.py",
  "description": "Update review_issues.yaml with Round 14 changes",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat > /tmp/update_issues.py << 'PYEOF'\nimport yaml\nimport sys\n\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml', 'r') as f:\n    data = yaml.safe_load(f)\n\nissues = data['issues']\nidx = {issue['id']: issue for issue in issues}\n\n# Helper to add mention\ndef add_mention(issue_id, round_num, reviewers, note):\n    issue = idx[issue_id]\n    if 'mentions' not in issue or issue['mentions'] is None:\n        issue['mentions'] = []\n    issue['mentions'].append({'round': round_num, 'reviewers': reviewers, 'note': note})\n    issue['last_seen_round'] = round_num\n\n# Helper to resolve\ndef resolve(issue_id, round_num, resolution, reviewers=None, note=None):\n    issue = idx[issue_id]\n    issue['status'] = 'resolved'\n    issue['resolution'] = resolution\n    issue['resolution_round'] = round_num\n    issue['last_seen_round'] = round_num\n    if reviewers is not None and note is not None:\n        add_mention(issue_id, round_num, reviewers, note)\n\n# ===== RESOLVE issues =====\n\nresolve('v4-R12-N2', 14,\n    \"'four tested doses' + 'preliminary' 标注。§4.2 line 110 明确 seed count。\",\n    [1, 2], \"R14: R1 [RESOLVED]，R2 未再提及。Abstract 'every tested dose' 在全文语境下充分。\")\n\nresolve('v4-R12-W6', 14,\n    \"§4.2 line 34 脚注说明 sampling eval (T=0.7) 及不可比性。\",\n    [1], \"R14: R1 [RESOLVED]。脚注已添加。\")\n\nresolve('v4-R12-W7', 14,\n    \"Table 1 caption 标注 'N-H is an upper bound'。Method §3.5 line 76 声明。\",\n    [1, 2], \"R14: R1 [RESOLVED]。标注清晰。\")\n\nresolve('v4-R1-W8', 14,\n    \"Matched cohort table 附完整 Wilson CIs。Limitations 量化 '100-example...Wilson 95% CI [2.3%, 12.7%]'。\",\n    [1, 2], \"R14: R1 [RESOLVED]。CIs 在 matched table + Limitations 中完整呈现。\")\n\nresolve('v5-R1-N3', 14,\n    \"Table 1 caption '500 steps unless noted'。SFT/Exec-only 行标签明确 '1k'。\",\n    [1], \"R14: R1 [RESOLVED]。标注清晰。\")\n\nresolve('v5-R2-W1', 14,\n    \"Abstract 改用 3-seed aggregate (ISR*=0.03±0.05 across three seeds at 1000 steps)。\",\n    [1, 2], \"R14: R2 [RESOLVED]。消除 cherry-picking 嫌疑。\")\n\nresolve('v5-R2-W3', 14,\n    \"段落结构大幅改善。Limitations 紧凑单段，Discussion 14 行连贯段落。\",\n    [2], \"R14: R2 [MOSTLY RESOLVED]。不再碎片化。\")\n\nresolve('v5-R2-MR', 14,\n    \"新增 Llemma (Azerbayev 2024)、Coste 2024 (reward ensembling)、Moskovitz 2024 (constrained optimization)。引用覆盖充足。\",\n    [1, 2], \"R14: R2 [RESOLVED]。引用覆盖完整。\")\n\nresolve('v6-R1-W2', 14,\n    \"§4.2 line 110 标注 'preliminary'。\",\n    [1], \"R14: R1 [RESOLVED]。\")\n\nresolve('v8-R1-N3', 14,\n    \"H1→CE, H7→TS, H8→PG, H9→CI 全文重命名完整一致。无残留旧名称。\",\n    [2], \"R14: R2 [RESOLVED]。Grep 确认无 H1/H7/H8/H9 残留。\")\n\nresolve('v8-R12-N2', 14,\n    \"C3 加 'in principle...preliminary'。Discussion 加 'should in principle transfer'。§4.3 显式声明无 Prolog random control。\",\n    [1, 2], \"R14: R1 [RESOLVED]。Hedging 充分。\")\n\nresolve('v8-R1-W4', 14,\n    \"Appendix line 126 标注 CMH 'p-values are consequently inflated'。功能等价于 'directional only'。\",\n    [1], \"R14: R1 [RESOLVED]。\")\n\nresolve('v10-R2-W8', 14,\n    \"Discussion 扩展至 14 行。含 gated ISR 实验 + reward ensembling + constrained optimization + TRACE 方向。\",\n    [1, 2], \"R14: R2 [RESOLVED]。有实质 mitigation 内容。\")\n\nresolve('v11-R1-W2', 14,\n    \"Abstract 'PG, observed at lower prevalence'。Method 明确 CE/TS robust (≥3 seeds) vs PG low prevalence。\",\n    [1, 2], \"R14: R2 [RESOLVED]。Claim 适当下调。\")\n\nresolve('v11-R2-MR', 14,\n    \"新增 Llemma、Coste 2024、Moskovitz 2024。Related Work + Discussion 均引用。\",\n    [1, 2], \"R14: R2 [RESOLVED]。引用覆盖完整。\")\n\nresolve('v12-R2-W2', 14,\n    \"Related Work 新增完整 'Faithfulness in formalization' 段落，3 维度逐条对比 Kim et al.。\",\n    [1, 2], \"R14: R2 [RESOLVED]。对比充分且有洞察。同 v13-R2-N2。\")\n\nresolve('v13-R2-N2', 14,\n    \"Related Work 新增完整 'Faithfulness in formalization' 段落：training vs inference、STA/ISR vs LLM-judge、universal gaming vs no-gaming、CE ≈ axiom-fabrication 互补性。\",\n    [1, 2], \"R14: R2 [RESOLVED]。'充分且有深度'。\")\n\nresolve('v13-R1-W1', 14,\n    \"Method §3.2 line 46: 'ISR is a component-necessity diagnostic, not a reasoning-quality metric'。全文 framing 校正。\",\n    [1, 2], \"R14: R2 [RESOLVED]。措辞精确。Abstract 仍用 'structural integrity' 但在上下文中可接受。\")\n\nresolve('v13-R2-W5', 14,\n    \"Table 2 caption 标注 '$^a$Single seed (s42); remaining columns pooled (ISR/Rnd 4B: 5-seed; Prolog/1.7B: 3-seed)'。\",\n    [1, 2], \"R14: R2 [RESOLVED]。聚合方式标注清晰。\")\n\nresolve('v13-R2-MITIGATION', 14,\n    \"Discussion lines 11-14: gated ISR 实验 (TS→PG migration) + reward ensembling (Coste 2024) + constrained optimization (Moskovitz 2024) + TRACE 方向。\",\n    [1, 2], \"R14: R2 [RESOLVED]。有实验支撑和文献对接。\")\n\nresolve('v13-R1-Q4', 14,\n    \"§4.3 line 118: 'No matched random control was run for Prolog' 显式声明。\",\n    [1, 2], \"R14: R1 [RESOLVED]。限制明确承认。\")\n\n# ===== ADD MENTIONS, keep in_progress =====\n\nadd_mention('v5-R12-SFT-PR', 14, [1, 2],\n    \"R14: Abstract/Introduction/Discussion hedging 全面改善 ('associated with...though gap prevents')。但 §4.2 line 42 仍用 'RL-specific' 旧措辞，缺 caveat。一处遗漏的统一化修改。\")\n\nadd_mention('v4-R12-N3', 14, [1, 2],\n    \"R14: Table 1 用 corrected 6%†。但方向反转 (ISR N-H 6.06% < Random 9.5%) 未在正文讨论。两位 reviewer 一致认为应在 §4.3 或 Discussion 增加 1-2 句，且这实际上强化核心论点。Matched cohort 同方向 (2.3% vs 5.9%)。\")\n\nadd_mention('v8-R12-N1', 14, [1, 2],\n    \"R14: Gated ISR 实验增量改善 (诊断→诊断+mitigation attempt)。TS→PG mode migration 是非平凡发现。但核心 novelty concern (LOO 标准+Goodhart 可预测) 仍为结构性限制。R1 3.5 vs R2 3.0，分歧在 empirical rigor vs conceptual novelty 权重。\")\n\nadd_mention('v4-R2-W9', 14, [1, 2],\n    \"R14: Introduction line 21 自我定位为 'empirical case study'。Gated ISR 增添实证贡献。但 LOO 是标准技术这一结构性限制无法修改解决。R2 [PARTIALLY RESOLVED]。\")\n\nadd_mention('v5-R2-N3', 14, [1, 2],\n    \"R14: Gated ISR 的 TS→PG migration ('blocking one Goodhart pathway redirects optimization pressure') 是非平凡发现。R2 Novelty 2.5→3.0。但概念新颖性限制仍为结构性问题。R2 [PARTIALLY RESOLVED]。\")\n\n# v13-R2-W4: downgrade severity\nidx['v13-R2-W4']['severity'] = 'info'\nadd_mention('v13-R2-W4', 14, [1, 2],\n    \"R14: ~18 缩写，未添加 notation summary。但 H1→CE 等描述性重命名显著改善可读性。R2 降为 minor。\")\n\n# v3-R12-NI-1: not raised in R14\nadd_mention('v3-R12-NI-1', 14, [],\n    \"R14: 未直接提及。C3 已 hedge 为 'in principle...preliminary'。\")\n\n# v6-R2-W8: taxonomy classification\nadd_mention('v6-R2-W8', 14, [1, 2],\n    \"R14: CE/TS/PG/CI 重命名改善可读性。CE/TS precision >95% 验证。PG claim 降为 'observed at lower prevalence'。分类标准仍为规则+功能分析混合。\")\n\n# v10-R2-W7: not raised\nadd_mention('v10-R2-W7', 14, [],\n    \"R14: 未再提及。\")\n\n# ===== v4-R2-W5: wont_fix but now partially addressed by gated ISR =====\nadd_mention('v4-R2-W5', 14, [1, 2],\n    \"R14: Gated ISR 实验 (Appendix §B.11) 测试了 component-count gate 变体。TS 消除但 PG 迁移。原标记 wont_fix 现部分回应。\")\n\n# ===== NEW ISSUES =====\n\nissues.append({\n    'id': 'v14-R12-GATED-S54',\n    'summary': 'Gated ISR Discussion 遗漏 s54 反例 (96.7% non-hacking)',\n    'category': 'writing',\n    'severity': 'warning',\n    'status': 'open',\n    'first_raised_round': 14,\n    'last_seen_round': 14,\n    'mentions': [{'round': 14, 'reviewers': [1, 2], 'note': \"Discussion 只提 '2/3 seeds migrate to PG'，忽略 s54 (96.7% N-H)。两位 reviewer 一致认为有选择性呈现嫌疑。建议改为 '2/3 seeds migrate to PG, while 1/3 sustains predominantly non-hacking output (96.7%); outcome is highly seed-dependent with only 3 seeds.'\"}],\n    'action_items': [{'round': 14, 'action': \"Discussion 补充 s54 数据和 seed-dependence caveat\", 'assigned_to': 'research_director', 'status': 'open'}],\n    'resolution': '',\n    'resolution_round': None\n})\n\nissues.append({\n    'id': 'v14-R1-LIMITATIONS',\n    'summary': 'Limitations section 压缩至 6-7 行，SFT n=39 限制未单独提及',\n    'category': 'writing',\n    'severity': 'info',\n    'status': 'open',\n    'first_raised_round': 14,\n    'last_seen_round': 14,\n    'mentions': [{'round': 14, 'reviewers': [1], 'note': \"8 页限制下可理解，但 Limitations 不再是 R13 评价的 '论文亮点'。关键内容散落在正文和 Appendix。\"}],\n    'action_items': [],\n    'resolution': '',\n    'resolution_round': None\n})\n\n# Write output\noutput = yaml.dump(data, allow_unicode=True, default_flow_style=False, sort_keys=False, width=200)\nwith open('/tmp/updated_issues.yaml', 'w') as f:\n    f.write(output)\n\nprint(f\"Done. {len(issues)} issues total.\")\n# Count statuses\nfrom collections import Counter\nstatus_counts = Counter(i['status'] for i in issues)\nfor s, c in sorted(status_counts.items()):\n    print(f\"  {s}: {c}\")\nPYEOF\npython3 /tmp/update_issues.py",
    "description": "Update review_issues.yaml with Round 14 changes",
    "timeout": "30000"
  }
}
```

</details>

---


### Tool result

_source line 1317 · 2026-05-19T10:15:59.249065+00:00_

Done. 97 issues total.
  in_progress: 8
  open: 5
  resolved: 83
  wont_fix: 1

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 1318 · 2026-05-19T10:16:03.729278+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/updated_issues.yaml",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/updated_issues.yaml",
    "limit": "50"
  }
}
```

</details>

---


### Tool result

_source line 1319 · 2026-05-19T10:16:04.030999+00:00_

1	issues:
2	- id: R1-W1
3	  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例
4	  category: experiment
5	  severity: critical
6	  status: resolved
7	  first_raised_round: 0
8	  last_seen_round: 2
9	  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。Fisher exact test + Wilson 95% CI 已加入。eval 集 100 例限制在 limitations.tex 讨论。
10	  resolution_round: 2
11	- id: RV-EVAL-FALLBACK
12	  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除
13	  category: experiment
14	  severity: critical
15	  status: resolved
16	  first_raised_round: 1
17	  last_seen_round: 1
18	  resolution: 第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)，无 fallback。
19	  resolution_round: 1
20	- id: RV-D060-NARRATIVE
21	  summary: D060 'Goodhart instability' 叙事：77pp PR 差距在同一测试集上确认成立
22	  category: experiment
23	  severity: critical
24	  status: resolved
25	  first_raised_round: 1
26	  last_seen_round: 1
27	  resolution: β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。
28	  resolution_round: 2
29	- id: RV-FIG2-STALE-SCRIPT
30	  summary: figures/paper/gen_fig2.py 旧脚本数据错误
31	  category: format
32	  severity: warning
33	  status: resolved
34	  first_raised_round: 1
35	  last_seen_round: 1
36	  resolution: 已修复。
37	  resolution_round: 1
38	- id: R1-W2
39	  summary: ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量
40	  category: framing
41	  severity: critical
42	  status: resolved
43	  first_raised_round: 0
44	  last_seen_round: 0
45	  resolution: method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。
46	  resolution_round: 2
47	- id: R2-W1
48	  summary: Limitations section 格式不合规
49	  category: format
50	  severity: critical

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1320 · 2026-05-19T10:16:10.508219+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"status: \" /tmp/updated_issues.yaml | head -40",
  "description": "Check status distribution in updated YAML"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"status: \" /tmp/updated_issues.yaml | head -40",
    "description": "Check status distribution in updated YAML"
  }
}
```

</details>

---


### Tool result

_source line 1321 · 2026-05-19T10:16:10.960475+00:00_

6:  status: resolved
15:  status: resolved
24:  status: resolved
33:  status: resolved
42:  status: resolved
51:  status: resolved
60:  status: resolved
69:  status: resolved
78:  status: resolved
87:  status: resolved
96:  status: resolved
105:  status: resolved
114:  status: resolved
123:  status: resolved
132:  status: resolved
141:  status: resolved
150:  status: resolved
159:  status: resolved
168:  status: resolved
177:  status: resolved
186:  status: resolved
195:  status: resolved
204:  status: resolved
213:  status: resolved
222:  status: resolved
231:  status: resolved
240:  status: resolved
249:  status: resolved
258:  status: resolved
267:  status: resolved
276:  status: resolved
285:  status: resolved
294:  status: resolved
303:  status: resolved
312:  status: resolved
321:  status: resolved
330:  status: resolved
339:  status: in_progress
374:  status: resolved
409:  status: in_progress

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 1322 · 2026-05-19T10:16:11.112896+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A2 \"id: v14\" /tmp/updated_issues.yaml",
  "description": "Check new R14 issues"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A2 \"id: v14\" /tmp/updated_issues.yaml",
    "description": "Check new R14 issues"
  }
}
```

</details>

---


### Tool result

_source line 1323 · 2026-05-19T10:16:11.163767+00:00_

- id: v14-R12-GATED-S54
  summary: Gated ISR Discussion 遗漏 s54 反例 (96.7% non-hacking)
  category: writing
--
- id: v14-R1-LIMITATIONS
  summary: Limitations section 压缩至 6-7 行，SFT n=39 限制未单独提及
  category: writing

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1324 · 2026-05-19T10:16:14.879237+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /tmp/updated_issues.yaml",
  "description": "Read full updated YAML for submission",
  "timeout": "10000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /tmp/updated_issues.yaml",
    "description": "Read full updated YAML for submission",
    "timeout": "10000"
  }
}
```

</details>

---


### Tool result

_source line 1325 · 2026-05-19T10:16:14.930347+00:00_

&lt;persisted-output>
Output too large (44.8KB). Full output saved to: /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation--claude-sessions-review-director-a46f8029/3cf4fa5f-68a3-4c66-bd93-8cf280c3f3c5/tool-results/bo88wncx2.txt

Preview (first 2KB):
issues:
- id: R1-W1
  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 2
  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。Fisher exact test + Wilson 95% CI 已加入。eval 集 100 例限制在 limitations.tex 讨论。
  resolution_round: 2
- id: RV-EVAL-FALLBACK
  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: 第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)，无 fallback。
  resolution_round: 1
- id: RV-D060-NARRATIVE
  summary: D060 'Goodhart instability' 叙事：77pp PR 差距在同一测试集上确认成立
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。
  resolution_round: 2
- id: RV-FIG2-STALE-SCRIPT
  summary: figures/paper/gen_fig2.py 旧脚本数据错误
  category: format
  severity: warning
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: 已修复。
  resolution_round: 1
- id: R1-W2
  summary: ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 0
  resolution: method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。
  resolution_round: 2
- id: R2-W1
  summary: Limitations section 格式不合规
  category: format
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 2
  resolution: 独立 limitations.tex 已创建，位于 references 之前。
  resolution_round: 3
- id
…[truncated 280 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1326 · 2026-05-19T10:16:18.245972+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation--claude-sessions-review-director-a46f8029/3cf4fa5f-68a3-4c66-bd93-8cf280c3f3c5/tool-results/bo88wncx2.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation--claude-sessions-review-director-a46f8029/3cf4fa5f-68a3-4c66-bd93-8cf280c3f3c5/tool-results/bo88wncx2.txt"
  }
}
```

</details>

---


### Tool result

_source line 1327 · 2026-05-19T10:16:18.548647+00:00_

1	issues:
2	- id: R1-W1
3	  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例
4	  category: experiment
5	  severity: critical
6	  status: resolved
7	  first_raised_round: 0
8	  last_seen_round: 2
9	  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。Fisher exact test + Wilson 95% CI 已加入。eval 集 100 例限制在 limitations.tex 讨论。
10	  resolution_round: 2
11	- id: RV-EVAL-FALLBACK
12	  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除
13	  category: experiment
14	  severity: critical
15	  status: resolved
16	  first_raised_round: 1
17	  last_seen_round: 1
18	  resolution: 第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)，无 fallback。
19	  resolution_round: 1
20	- id: RV-D060-NARRATIVE
21	  summary: D060 'Goodhart instability' 叙事：77pp PR 差距在同一测试集上确认成立
22	  category: experiment
23	  severity: critical
24	  status: resolved
25	  first_raised_round: 1
26	  last_seen_round: 1
27	  resolution: β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。
28	  resolution_round: 2
29	- id: RV-FIG2-STALE-SCRIPT
30	  summary: figures/paper/gen_fig2.py 旧脚本数据错误
31	  category: format
32	  severity: warning
33	  status: resolved
34	  first_raised_round: 1
35	  last_seen_round: 1
36	  resolution: 已修复。
37	  resolution_round: 1
38	- id: R1-W2
39	  summary: ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量
40	  category: framing
41	  severity: critical
42	  status: resolved
43	  first_raised_round: 0
44	  last_seen_round: 0
45	  resolution: method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。
46	  resolution_round: 2
47	- id: R2-W1
48	  summary: Limitations section 格式不合规
49	  category: format
50	  severity: critical
51	  status: resolved
52	  first_raised_round: 0
53	  last_seen_round: 2
54	  resolution: 独立 limitations.tex 已创建，位于 references 之前。
55	  resolution_round: 3
56	- id: R2-W2
57	  summary: 实验仅用单一模型 (Qwen3-4B) 和单一数据集 (FOLIO)，标题复数暗示通用性
58	  category: experiment
59	  severity: critical
60	  status: resolved
61	  first_raised
…[truncated 43539 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 302
}
```

</details>

---


### Tool call

_source line 1328 · 2026-05-19T10:16:32.925916+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /tmp/updated_issues.yaml | wc -c",
  "description": "Check YAML file size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /tmp/updated_issues.yaml | wc -c",
    "description": "Check YAML file size"
  }
}
```

</details>

---


### Tool result

_source line 1329 · 2026-05-19T10:16:33.026877+00:00_

45908

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1330 · 2026-05-19T10:18:26.019167+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 1331 · 2026-05-19T10:18:26.019588+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1332 · 2026-05-19T10:18:26.220669+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/updated_issues.yaml",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/updated_issues.yaml",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 1333 · 2026-05-19T10:18:26.271433+00:00_

1	issues:
2	- id: R1-W1
3	  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例
4	  category: experiment
5	  severity: critical
6	  status: resolved
7	  first_raised_round: 0
8	  last_seen_round: 2
9	  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。Fisher exact test + Wilson 95% CI 已加入。eval 集 100 例限制在 limitations.tex 讨论。
10	  resolution_round: 2
11	- id: RV-EVAL-FALLBACK
12	  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除
13	  category: experiment
14	  severity: critical
15	  status: resolved
16	  first_raised_round: 1
17	  last_seen_round: 1
18	  resolution: 第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)，无 fallback。
19	  resolution_round: 1
20	- id: RV-D060-NARRATIVE
21	  summary: D060 'Goodhart instability' 叙事：77pp PR 差距在同一测试集上确认成立
22	  category: experiment
23	  severity: critical
24	  status: resolved
25	  first_raised_round: 1
26	  last_seen_round: 1
27	  resolution: β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。
28	  resolution_round: 2
29	- id: RV-FIG2-STALE-SCRIPT
30	  summary: figures/paper/gen_fig2.py 旧脚本数据错误
31	  category: format
32	  severity: warning
33	  status: resolved
34	  first_raised_round: 1
35	  last_seen_round: 1
36	  resolution: 已修复。
37	  resolution_round: 1
38	- id: R1-W2
39	  summary: ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量
40	  category: framing
41	  severity: critical
42	  status: resolved
43	  first_raised_round: 0
44	  last_seen_round: 0
45	  resolution: method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。
46	  resolution_round: 2
47	- id: R2-W1
48	  summary: Limitations section 格式不合规
49	  category: format
50	  severity: critical
51	  status: resolved
52	  first_raised_round: 0
53	  last_seen_round: 2
54	  resolution: 独立 limitations.tex 已创建，位于 references 之前。
55	  resolution_round: 3
56	- id: R2-W2
57	  summary: 实验仅用单一模型 (Qwen3-4B) 和单一数据集 (FOLIO)，标题复数暗示通用性
58	  category: experiment
59	  severity: critical
60	  status: resolved
61	  first_raised
…[truncated 1186 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1334 · 2026-05-19T10:18:30.480240+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/updated_issues.yaml",
  "offset": "100",
  "limit": "400"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/updated_issues.yaml",
    "offset": "100",
    "limit": "400"
  }
}
```

</details>

---


### Tool result

_source line 1335 · 2026-05-19T10:18:30.480927+00:00_

100	  resolution_round: 2
101	- id: R1-W6
102	  summary: 训练 500 例/评估 100 例的规模限制讨论不充分
103	  category: experiment
104	  severity: warning
105	  status: resolved
106	  first_raised_round: 0
107	  last_seen_round: 0
108	  resolution: limitations.tex 已讨论。
109	  resolution_round: 2
110	- id: R1-W7
111	  summary: H1/H7 classifier precision/recall 未报告
112	  category: experiment
113	  severity: info
114	  status: resolved
115	  first_raised_round: 0
116	  last_seen_round: 0
117	  resolution: 50 样本人工验证 precision >95%。
118	  resolution_round: 2
119	- id: R1-W8
120	  summary: Random control U(0,1) 与 ISR 的 skewed 分布不匹配
121	  category: method
122	  severity: info
123	  status: resolved
124	  first_raised_round: 0
125	  last_seen_round: 0
126	  resolution: method.tex 和 experiments.tex 均说明了 Random 设计目的。
127	  resolution_round: 2
128	- id: R1-W9
129	  summary: 缺代码/数据开源承诺
130	  category: format
131	  severity: info
132	  status: resolved
133	  first_raised_round: 0
134	  last_seen_round: 0
135	  resolution: 'abstract.tex:9 脚注 ''Code and data: [anonymized]''。'
136	  resolution_round: 2
137	- id: R1-W5
138	  summary: '''Meta-level Goodhart'' 新颖性论证不足'
139	  category: framing
140	  severity: warning
141	  status: resolved
142	  first_raised_round: 0
143	  last_seen_round: 3
144	  resolution: framing 降级为 empirical instance。
145	  resolution_round: 3
146	- id: R2-W8
147	  summary: H1/H7 编号不连贯（H2-H6 不存在）
148	  category: writing
149	  severity: info
150	  status: resolved
151	  first_raised_round: 0
152	  last_seen_round: 3
153	  resolution: method.tex 解释了合并原因。
154	  resolution_round: 3
155	- id: v2-R1-N1
156	  summary: Abstract '93%' PR 为 single seed，应改为 mean±std
157	  category: writing
158	  severity: critical
159	  status: resolved
160	  first_raised_round: 2
161	  last_seen_round: 3
162	  resolution: Abstract 使用 3-seed pooled mean±std。
163	  resolution_round: 3
164	- id: v2-R1-N3
165	  summary: 仅 2 个 β 值不足以刻画 dose-response
166	  category: experiment
167	  severity: critical
168	  status:
…[truncated 10085 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1336 · 2026-05-19T10:18:33.644089+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/updated_issues.yaml",
  "offset": "499",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/updated_issues.yaml",
    "offset": "499",
    "limit": "500"
  }
}
```

</details>

---


### Tool result

_source line 1337 · 2026-05-19T10:18:33.695130+00:00_

499	  status: resolved
500	  first_raised_round: 4
501	  last_seen_round: 14
502	  mentions:
503	  - round: 12
504	    reviewers:
505	    - 1
506	    - 2
507	    note: R1-W5 + R2 [AGREE with nuance]。建议报告 Wilson CI。
508	  - round: 13
509	    reviewers:
510	    - 1
511	    - 2
512	    note: 'R1-N2 [critical]: 5-seed pooled N-H 23% vs 3-seed corrected 6% 差 17pp；matched cohort non-hacking permutation p=0.917 因 n=5 power 不足无法检测效应。R2 补充: ISR s45 n=42 的 54.8% N-H 实际只有 ~23 samples。两人一致建议扩大
513	      eval set 或附 CIs。'
514	  - round: 14
515	    reviewers:
516	    - 1
517	    - 2
518	    note: 'R14: R1 [RESOLVED]。CIs 在 matched table + Limitations 中完整呈现。'
519	  resolution: Matched cohort table 附完整 Wilson CIs。Limitations 量化 '100-example...Wilson 95% CI [2.3%, 12.7%]'。
520	  resolution_round: 14
521	- id: v4-R2-W9
522	  summary: 方法新颖性有限：Algorithm 1 仅 6 行伪代码
523	  category: method
524	  severity: warning
525	  status: in_progress
526	  first_raised_round: 4
527	  last_seen_round: 14
528	  mentions:
529	  - round: 11
530	    reviewers:
531	    - 1
532	    - 2
533	    note: '共识: Findings 级别。'
534	  - round: 12
535	    reviewers:
536	    - 1
537	    - 2
538	    note: R1 Excitement 3/5, R2 2.5/5。两人均同意 Findings。
539	  - round: 13
540	    reviewers:
541	    - 1
542	    - 2
543	    note: 'R2-N1 [critical]: LOO+Goodhart 均为已知。R1 部分同意但认为 empirical contributions 有增量价值（seed-dependent divergence, H7b triple gaming, cross-logic diversity）。R1 Excitement 3.0 vs R2 2.5。分歧但共识区间 Findings-Borderline
544	      Conference。'
545	  - round: 14
546	    reviewers:
547	    - 1
548	    - 2
549	    note: 'R14: Introduction line 21 自我定位为 ''empirical case study''。Gated ISR 增添实证贡献。但 LOO 是标准技术这一结构性限制无法修改解决。R2 [PARTIALLY RESOLVED]。'
550	- id: v4-R2-W5
551	  summary: 未测试 tautology-guarded ISR 变体
552	  category: method
553	  severity: warning
554	  status: wont_fix
555	  first_raised_round: 4
556	  last_seen_round: 14
557	  resolution: Future work. Arms-race evidence 已有。
558	  resolution_round: 4
559	  mentions:
560
…[truncated 13580 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1338 · 2026-05-19T10:18:36.958912+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/updated_issues.yaml",
  "offset": "998",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/updated_issues.yaml",
    "offset": "998",
    "limit": "500"
  }
}
```

</details>

---


### Tool result

_source line 1339 · 2026-05-19T10:18:37.009987+00:00_

998	  category: method
999	  severity: warning
1000	  status: resolved
1001	  first_raised_round: 9
1002	  last_seen_round: 9
1003	  resolution: method.tex 增加 confound 两场景区分句。
1004	  resolution_round: 9
1005	- id: v9-R12-W1
1006	  summary: §4.4 标题措辞过强
1007	  category: writing
1008	  severity: warning
1009	  status: resolved
1010	  first_raised_round: 9
1011	  last_seen_round: 9
1012	  resolution: §4.4 标题改为 'Cross-Logic Extension'。
1013	  resolution_round: 9
1014	- id: v9-R1-W5
1015	  summary: 训练时 sampling vs 评估时 greedy 不一致
1016	  category: experiment
1017	  severity: warning
1018	  status: resolved
1019	  first_raised_round: 9
1020	  last_seen_round: 9
1021	  resolution: §4.1 已增加讨论。
1022	  resolution_round: 9
1023	- id: v9-R12-Q-ISR-FILTER
1024	  summary: ISR 作为 filter 未测试
1025	  category: method
1026	  severity: info
1027	  status: resolved
1028	  first_raised_round: 9
1029	  last_seen_round: 10
1030	  resolution: conclusion.tex 增加 'ISR as post-hoc filter' 作为 future work。
1031	  resolution_round: 9
1032	- id: v9-R12-Q-NORMALIZED-ISR
1033	  summary: 未测试 premise-count-normalized ISR
1034	  category: method
1035	  severity: info
1036	  status: resolved
1037	  first_raised_round: 9
1038	  last_seen_round: 9
1039	  resolution: conclusion.tex 增加 'normalized variants' 作为 future work。
1040	  resolution_round: 9
1041	- id: v4-RV-STALE-APPENDIX
1042	  summary: Appendix Table 仍用旧数据
1043	  category: writing
1044	  severity: warning
1045	  status: resolved
1046	  first_raised_round: 4
1047	  last_seen_round: 7
1048	  resolution: Appendix Table 5 现含完整 per-seed data。
1049	  resolution_round: 7
1050	- id: v10-R12-N1
1051	  summary: §4.5 与 Limitations 关于 1.7B seed 数量矛盾
1052	  category: experiment
1053	  severity: critical
1054	  status: resolved
1055	  first_raised_round: 10
1056	  last_seen_round: 11
1057	  resolution: D129 完整 3-seed 数据重写 §4.5。
1058	  resolution_round: 11
1059	- id: v10-R2-Q6
1060	  summary: ISR=0.75 推导与实测不一致
1061	  category: method
1062	  severity: warning
1063	 
…[truncated 12757 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1340 · 2026-05-19T10:18:42.531930+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/tmp/updated_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/tmp/updated_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1341 · 2026-05-19T10:18:42.885720+00:00_

1	issues:
2	- id: R1-W1
3	  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例
4	  category: experiment
5	  severity: critical
6	  status: resolved
7	  first_raised_round: 0
8	  last_seen_round: 2
9	  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。Fisher exact test + Wilson 95% CI 已加入。eval 集 100 例限制在 limitations.tex 讨论。
10	  resolution_round: 2
11	- id: RV-EVAL-FALLBACK
12	  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除
13	  category: experiment
14	  severity: critical
15	  status: resolved
16	  first_raised_round: 1
17	  last_seen_round: 1
18	  resolution: 第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)，无 fallback。
19	  resolution_round: 1
20	- id: RV-D060-NARRATIVE
21	  summary: D060 'Goodhart instability' 叙事：77pp PR 差距在同一测试集上确认成立
22	  category: experiment
23	  severity: critical
24	  status: resolved
25	  first_raised_round: 1
26	  last_seen_round: 1
27	  resolution: β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。
28	  resolution_round: 2
29	- id: RV-FIG2-STALE-SCRIPT
30	  summary: figures/paper/gen_fig2.py 旧脚本数据错误
31	  category: format
32	  severity: warning
33	  status: resolved
34	  first_raised_round: 1
35	  last_seen_round: 1
36	  resolution: 已修复。
37	  resolution_round: 1
38	- id: R1-W2
39	  summary: ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量
40	  category: framing
41	  severity: critical
42	  status: resolved
43	  first_raised_round: 0
44	  last_seen_round: 0
45	  resolution: method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。
46	  resolution_round: 2
47	- id: R2-W1
48	  summary: Limitations section 格式不合规
49	  category: format
50	  severity: critical
51	  status: resolved
52	  first_raised_round: 0
53	  last_seen_round: 2
54	  resolution: 独立 limitations.tex 已创建，位于 references 之前。
55	  resolution_round: 3
56	- id: R2-W2
57	  summary: 实验仅用单一模型 (Qwen3-4B) 和单一数据集 (FOLIO)，标题复数暗示通用性
58	  category: experiment
59	  severity: critical
60	  status: resolved
61	  first_raised
…[truncated 43539 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 1342 · 2026-05-19T10:24:13.779586+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "solver-trace-ablation",
  "issues_yaml": "issues:\n- id: R1-W1\n  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。Fisher exact test + Wilson 95% CI 已加入。eval 集 100 例限制在 limitations.tex 讨论。\n  resolution_round: 2\n- id: RV-EVAL-FALLBACK\n  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: 第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)，无 fallback。\n  resolution_round: 1\n- id: RV-D060-NARRATIVE\n  summary: D060 'Goodhart instability' 叙事：77pp PR 差距在同一测试集上确认成立\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。\n  resolution_round: 2\n- id: RV-FIG2-STALE-SCRIPT\n  summary: figures/paper/gen_fig2.py 旧脚本数据错误\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: 已修复。\n  resolution_round: 1\n- id: R1-W2\n  summary: ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。\n  resolution_round: 2\n- id: R2-W1\n  summary: Limitations section 格式不合规\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 独立 limitations.tex 已创建，位于 references 之前。\n  resolution_round: 3\n- id: R2-W2\n  summary: 实验仅用单一模型 (Qwen3-4B) 和单一数据集 (FOLIO)，标题复数暗示通用性\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 标题改为单数。Qwen3-1.7B cross-scale 实验已加入。\n  resolution_round: 3\n- id: R1-W4\n  summary: Exec-only seed 43 使用 sampling (T=0.7) 评估而非 greedy\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: exec-only 500-step 主表仅报告 s42（†标注）。\n  resolution_round: 2\n- id: R1-W3\n  summary: \"'Solver-agnostic' 仅测 2 solver，过度声明\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"'solver-agnostic' 已从全文移除。\"\n  resolution_round: 2\n- id: R2-W6\n  summary: SFT baseline 比较不公平：PR=14% vs 93%，低 PR 本身减少 hacking 机会\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 100-step RL 对照已加入。claim 调整为 'consistent with'。\n  resolution_round: 2\n- id: R2-W7\n  summary: 与 Kim et al. (2026) 差异化不充分\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: related_work.tex 中有区分段落。\n  resolution_round: 2\n- id: R1-W6\n  summary: 训练 500 例/评估 100 例的规模限制讨论不充分\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: limitations.tex 已讨论。\n  resolution_round: 2\n- id: R1-W7\n  summary: H1/H7 classifier precision/recall 未报告\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: 50 样本人工验证 precision >95%。\n  resolution_round: 2\n- id: R1-W8\n  summary: Random control U(0,1) 与 ISR 的 skewed 分布不匹配\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: method.tex 和 experiments.tex 均说明了 Random 设计目的。\n  resolution_round: 2\n- id: R1-W9\n  summary: 缺代码/数据开源承诺\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"abstract.tex:9 脚注 'Code and data: [anonymized]'。\"\n  resolution_round: 2\n- id: R1-W5\n  summary: \"'Meta-level Goodhart' 新颖性论证不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: framing 降级为 empirical instance。\n  resolution_round: 3\n- id: R2-W8\n  summary: H1/H7 编号不连贯（H2-H6 不存在）\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: method.tex 解释了合并原因。\n  resolution_round: 3\n- id: v2-R1-N1\n  summary: Abstract '93%' PR 为 single seed，应改为 mean±std\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: Abstract 使用 3-seed pooled mean±std。\n  resolution_round: 3\n- id: v2-R1-N3\n  summary: 仅 2 个 β 值不足以刻画 dose-response\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 4 个 β 值提供完整 dose-response 曲线。\n  resolution_round: 4\n- id: v2-R2-N3\n  summary: STA 方法论新颖性有限\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: novelty 定位为 applying standard LOO。\n  resolution_round: 3\n- id: v2-R2-N2\n  summary: 单模型+单数据集泛化性不足\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: cross-scale 实验加入。单数据集限制在 Limitations 讨论。\n  resolution_round: 3\n- id: v2-R1-W3\n  summary: ISR-as-reward 控制 confound 后净效果仅 1.06×\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: ISR 定位从 training signal 转为 diagnostic-only。\n  resolution_round: 3\n- id: v2-R1-W6\n  summary: Hacking taxonomy 缺乏 IAA 验证\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: deterministic rules + 50-sample precision check。\n  resolution_round: 3\n- id: v2-R2-W3\n  summary: Abstract 信息密度过高\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: Abstract 重写为 ~170 words。\n  resolution_round: 3\n- id: v2-R2-W4\n  summary: Premise-count confound 讨论放在 Appendix 而非正文\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 提升到正文 §3.2。\n  resolution_round: 3\n- id: v2-R2-W5\n  summary: C2 和 C4 独立性不足\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: taxonomy 独立性论证成立。\n  resolution_round: 3\n- id: v2-FMT-1\n  summary: Limitations section 位于 References 之后\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 顺序已正确。\n  resolution_round: 3\n- id: v2-FMT-2\n  summary: Ethics Statement 缺失\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: ethics.tex 加入。\n  resolution_round: 3\n- id: v2-FMT-3\n  summary: Orphan bibliography entries\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: orphan entries 清除。\n  resolution_round: 3\n- id: v2-R1-M4\n  summary: Prolog cross-logic transfer 样本量过小\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"'universal Goodhart' 移除，改为 qualitative observation。\"\n  resolution_round: 3\n- id: v2-R1-W1\n  summary: 3 seeds 统计效力不足以支撑定量 claims\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 统计方法改进。定量 claims 降级。\n  resolution_round: 3\n- id: v2-R1-W4\n  summary: SFT baseline 比较因 PR 悬殊说服力有限\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 100-step RL 对照充分利用。\n  resolution_round: 3\n- id: R2-MISSING-REF\n  summary: 引用覆盖不足\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: 31 条引用覆盖核心领域。\n  resolution_round: 3\n- id: v3-R1-NI-2\n  summary: β=0.2 未在 Table 1 中独立报告\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: Table 1 现已包含 β=0.2 行。\n  resolution_round: 4\n- id: v3-R1-NI-3\n  summary: §4.2 cross-seed 描述暗示最终状态\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"现标注 '(at 500 steps)'。\"\n  resolution_round: 4\n- id: v3-R12-NI-4\n  summary: 全文 em-dash AI 写作痕迹\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: em-dash=0, -ing endings 仅 4 处轻微, blacklisted words=0。\n  resolution_round: 5\n- id: v3-R2-NI-5\n  summary: \"Abstract 'zero structurally sound outputs' 与 N-H=8% 矛盾\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Abstract 现用 'effectively zero...at convergence'。\"\n  resolution_round: 4\n- id: v3-R12-NI-1\n  summary: Cross-scale 实验 seed 数量不足\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 14\n  mentions:\n  - round: 3\n    reviewers:\n    - 1\n    - 2\n    note: 两位 reviewer 一致。\n  - round: 10\n    reviewers:\n    - 1\n    - 2\n    note: 现已用 D129 完整 3-seed 数据重写 §4.5。\n  - round: 11\n    reviewers:\n    - 1\n    note: \"R1-W4: 3 seeds 仍不足以作为独立 contribution 支撑。D134 扩展至 10 seeds 正在训练中。\"\n  - round: 12\n    reviewers:\n    - 1\n    - 2\n    note: \"R1-N1 再次要求增加模型/数据集多样性。R2-N3 将 C3 cross-logic 定为 preliminary 不应为正式 contribution。两人一致建议降级 C3。R12 fix: C3 弱化为 'evidence of generality'（commit 9dc8835）。\"\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: \"R13 R2-W1: C3 仍在同一 dataset (FOLIO) 和 model family (Qwen3) 内。两位 reviewer 一致要求进一步 hedge C3 措辞。\"\n  - round: 14\n    reviewers: []\n    note: \"R14: 未直接提及。C3 已 hedge 为 'in principle...preliminary'。\"\n- id: v4-R12-N2\n  summary: \"'Inevitable collapse at all doses' claim 超出证据\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 14\n  mentions:\n  - round: 9\n    reviewers:\n    - 1\n    - 2\n    note: \"共识: 区分 'observed in all seeds tested' vs 'population-level inference'。\"\n  - round: 11\n    reviewers:\n    - 1\n    - 2\n    note: \"术语降级为 'seed-dependent divergence' 和 'dose-varying patterns'。\"\n  - round: 12\n    reviewers:\n    - 1\n    - 2\n    note: \"R1-W3 再次指出稀疏。R1 交叉回应认为 'all tested doses show Goodhart collapse' 成立。R12 fix: 加强 preliminary 标注，区分 500-step snapshot vs trajectory（commit 9dc8835）。\"\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: \"R1-N3 认为 Abstract/Discussion 仍需更多 hedging。R2 反驳称 structural argument (H7 恒定 ISR≥0.5) 使 'at every tested dose' 成立。分歧记录。\"\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: R1 [RESOLVED]，R2 未再提及。Abstract 'every tested dose' 在全文语境下充分。\"\n  resolution: \"'four tested doses' + 'preliminary' 标注。§4.2 line 110 明确 seed count。\"\n  resolution_round: 14\n- id: v4-R12-N3\n  summary: OR=3.48 (uncorrected) vs OR=0.61 (corrected) 方向反转\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 14\n  mentions:\n  - round: 10\n    reviewers:\n    - 1\n    - 2\n    note: Table 1 和 Discussion §5 仍以 23% (uncorrected) 为 headline。\n  - round: 11\n    reviewers:\n    - 1\n    - 2\n    note: OR 反转仍是核心问题。降级为 major。\n  - round: 12\n    reviewers:\n    - 1\n    - 2\n    note: \"R1-N2 + R2-N2 [critical]。Seed-level p=0.26，corrected OR=0.61。R12 fix: transient window 降级为 descriptive observation，Table 1 N-H 改用 corrected 6%，论文最强 claim 锚定为 'Goodhart collapse at every dose'（commit 9dc8835）。\"\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: \"Table 1 现用 corrected 6%†，但 footnote 同时给出 uncorrected 23%。R2 指出 non-hacking permutation p=0.917 且 point estimate ISR(2.3%) < Random(5.9%) 方向反转。两位 reviewer 一致认为 transient window 不构成 ISR 优势证据。\"\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: Table 1 用 corrected 6%†。但方向反转 (ISR N-H 6.06% < Random 9.5%) 未在正文讨论。两位 reviewer 一致认为应在 §4.3 或 Discussion 增加 1-2 句，且这实际上强化核心论点。Matched cohort 同方向 (2.3% vs 5.9%)。\"\n- id: v4-R12-W6\n  summary: Seed 43 exec-only 评估协议矛盾\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 14\n  mentions:\n  - round: 10\n    reviewers:\n    - 1\n    - 2\n    note: Appendix Table 5 s43-500 Notes 列已修正。\n  - round: 12\n    reviewers: []\n    note: Round 12 未提及。Appendix 中已有 † 标注。\n  - round: 13\n    reviewers:\n    - 1\n    note: \"R1-W4 [minor]: s43 数据仍在 cross-seed 比较中出现（§4.1），建议正文加脚注。\"\n  - round: 14\n    reviewers:\n    - 1\n    note: \"R14: R1 [RESOLVED]。脚注已添加。\"\n  resolution: §4.2 line 34 脚注说明 sampling eval (T=0.7) 及不可比性。\n  resolution_round: 14\n- id: v4-R12-W7\n  summary: Deleted checkpoints (ISR β=0.1 s43/s44) 导致 H8 audit 不完整\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers:\n    - 1\n    - 2\n    note: \"'All N-H rates are upper bounds' 声明已加入 method.tex。\"\n  - round: 12\n    reviewers:\n    - 1\n    - 2\n    note: \"R1-N3 [critical]: 5-seed N-H=23% 为 uncorrected upper bound。R12 fix: Table 1 改用 corrected 3-seed 6%，footnote 说明（commit 9dc8835）。\"\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: \"R1-W5 [minor]: Table 1 脚注存在但不够醒目。R2-W6: N-H% 列建议标注 '(upper bound)'。两位 reviewer 一致。\"\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: R1 [RESOLVED]。标注清晰。\"\n  resolution: \"Table 1 caption 标注 'N-H is an upper bound'。Method §3.5 line 76 声明。\"\n  resolution_round: 14\n- id: v4-R1-W8\n  summary: 100 eval samples 对 per-seed claims 统计功效不足\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 14\n  mentions:\n  - round: 12\n    reviewers:\n    - 1\n    - 2\n    note: R1-W5 + R2 [AGREE with nuance]。建议报告 Wilson CI。\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: \"R1-N2 [critical]: 5-seed pooled N-H 23% vs 3-seed corrected 6% 差 17pp；matched cohort non-hacking permutation p=0.917 因 n=5 power 不足无法检测效应。R2 补充: ISR s45 n=42 的 54.8% N-H 实际只有 ~23 samples。两人一致建议扩大 eval set 或附 CIs。\"\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: R1 [RESOLVED]。CIs 在 matched table + Limitations 中完整呈现。\"\n  resolution: \"Matched cohort table 附完整 Wilson CIs。Limitations 量化 '100-example...Wilson 95% CI [2.3%, 12.7%]'。\"\n  resolution_round: 14\n- id: v4-R2-W9\n  summary: 方法新颖性有限：Algorithm 1 仅 6 行伪代码\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers:\n    - 1\n    - 2\n    note: \"共识: Findings 级别。\"\n  - round: 12\n    reviewers:\n    - 1\n    - 2\n    note: R1 Excitement 3/5, R2 2.5/5。两人均同意 Findings。\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: \"R2-N1 [critical]: LOO+Goodhart 均为已知。R1 部分同意但认为 empirical contributions 有增量价值（seed-dependent divergence, H7b triple gaming, cross-logic diversity）。R1 Excitement 3.0 vs R2 2.5。分歧但共识区间 Findings-Borderline Conference。\"\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: Introduction line 21 自我定位为 'empirical case study'。Gated ISR 增添实证贡献。但 LOO 是标准技术这一结构性限制无法修改解决。R2 [PARTIALLY RESOLVED]。\"\n- id: v4-R2-W5\n  summary: 未测试 tautology-guarded ISR 变体\n  category: method\n  severity: warning\n  status: wont_fix\n  first_raised_round: 4\n  last_seen_round: 14\n  resolution: Future work. Arms-race evidence 已有。\n  resolution_round: 4\n  mentions:\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: Gated ISR 实验 (Appendix §B.11) 测试了 component-count gate 变体。TS 消除但 PG 迁移。原标记 wont_fix 现部分回应。\"\n- id: v5-R1-N3\n  summary: Table 1 比较框架不对称\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 14\n  mentions:\n  - round: 10\n    reviewers:\n    - 1\n    - 2\n    note: Table 1 已拆分为 primary + cross-scale。\n  - round: 11\n    reviewers: []\n    note: 未直接提及。\n  - round: 13\n    reviewers:\n    - 1\n    note: \"R1 Detailed Comments: Table 1 混合 500-step 和 1000-step 结果需更清楚标注。\"\n  - round: 14\n    reviewers:\n    - 1\n    note: \"R14: R1 [RESOLVED]。标注清晰。\"\n  resolution: \"Table 1 caption '500 steps unless noted'。SFT/Exec-only 行标签明确 '1k'。\"\n  resolution_round: 14\n- id: v5-R2-N3\n  summary: \"'Diagnostic becomes optimization target' 概念新颖性有限\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers:\n    - 1\n    - 2\n    note: R2-N2 [critical]。R1 认为 empirical phenomena 有独立价值但同意 Findings。\n  - round: 12\n    reviewers:\n    - 1\n    - 2\n    note: R1 Excitement 3/5 vs R2 2.5/5。两人均同意 Findings。结构性问题。\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: \"同上。R2 进一步论证: ISR 的不对称性原因 'too straightforward'（LOO 偏好低 component count，H7 是全局最优 exploit）。结构性问题，无法通过修改解决。\"\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: Gated ISR 的 TS→PG migration ('blocking one Goodhart pathway redirects optimization pressure') 是非平凡发现。R2 Novelty 2.5→3.0。但概念新颖性限制仍为结构性问题。R2 [PARTIALLY RESOLVED]。\"\n- id: v5-R2-W1\n  summary: Abstract 数据堆砌 / 单 seed 数据选择性报告\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers:\n    - 1\n    - 2\n    note: \"R11 fix: 数字减至 ≤3 个 headline figures。\"\n  - round: 12\n    reviewers: []\n    note: R12 未再提及 Abstract 数据堆砌（质量重写后改善）。但 R12 建议术语密度可进一步降低。\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: \"R2-W3: Abstract '99.5% structural collapse' 来自 s42 单 seed 100→1000 步轨迹，有 cherry-picking 嫌疑。R1 交叉时 [AGREE]，建议改为 3-seed aggregate (ISR*=0.03±0.05)。两人一致。\"\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: R2 [RESOLVED]。消除 cherry-picking 嫌疑。\"\n  resolution: Abstract 改用 3-seed aggregate (ISR*=0.03±0.05 across three seeds at 1000 steps)。\n  resolution_round: 14\n- id: v5-R2-W3\n  summary: paragraph{} 过度碎片化\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers:\n    - 2\n    note: method/conclusion/limitations 仍有多个 paragraph{}。\n  - round: 12\n    reviewers: []\n    note: \"R12 未再提及 paragraph{} 问题（质量重写后已大幅改善）。\"\n  - round: 13\n    reviewers: []\n    note: R13 未提及。可能已修复，待确认。\n  - round: 14\n    reviewers:\n    - 2\n    note: \"R14: R2 [MOSTLY RESOLVED]。不再碎片化。\"\n  resolution: 段落结构大幅改善。Limitations 紧凑单段，Discussion 14 行连贯段落。\n  resolution_round: 14\n- id: v5-R2-W4\n  summary: Experiments §4.3 按 β 值呈现顺序非升序\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 10\n  resolution: §4.3 已按升序呈现。\n  resolution_round: 10\n- id: v5-R12-SFT-PR\n  summary: SFT baseline PR confound (PR=13% vs 93%)\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers:\n    - 1\n    - 2\n    note: SFT caveat 加入。\n  - round: 12\n    reviewers:\n    - 1\n    - 2\n    note: \"R1-W1 + R2-W1。R12 fix: Abstract 加 'though the large prove-rate gap prevents definitive causal attribution'。Limitations 加 SFT best-of-N open question（commit 9dc8835）。\"\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: \"R1-N1 [critical]: RL-specificity claim 依赖此对比但证据基础薄弱。SFT n=39，100-step checkpoint 仅 s42 (n=32)。R2-W2 [major] 完全同意。两位 reviewer 一致要求进一步降低 RL-specificity claim 强度。\"\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: Abstract/Introduction/Discussion hedging 全面改善 ('associated with...though gap prevents')。但 §4.2 line 42 仍用 'RL-specific' 旧措辞，缺 caveat。一处遗漏的统一化修改。\"\n- id: v5-R2-MR\n  summary: 缺少重要引用\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers:\n    - 2\n    note: 已加入 Cao et al. 2026 + Wang et al. 2025。\n  - round: 12\n    reviewers:\n    - 1\n    - 2\n    note: \"R12 建议补充 STaR + Cobbe + Lean-based RL。R12 fix: 已加入 STaR (Zelikman 2022) + Cobbe (2021)（commit 9dc8835）。\"\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: \"R1: 补 LEGO-Prover, formal verification reward design。R2: 补 Lean-based RL (Llemma), reward hacking mitigation 策略, RLVR 其他工作。两人一致缺 mitigation literature 引用。\"\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: R2 [RESOLVED]。引用覆盖完整。\"\n  resolution: 新增 Llemma (Azerbayev 2024)、Coste 2024 (reward ensembling)、Moskovitz 2024 (constrained optimization)。引用覆盖充足。\n  resolution_round: 14\n- id: v5-R2-W6\n  summary: Table 1 信息密度过高\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 10\n  resolution: \"已拆分为 Table 1 + Table 2。R12: Table 2 移入 Appendix 节省空间。\"\n  resolution_round: 12\n- id: v5-R1-W5\n  summary: Goodhart taxonomy variant 未指定\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  resolution: \"related_work.tex 指定 'primarily regressional, with extremal elements'。\"\n  resolution_round: 7\n- id: v5-R1-W6\n  summary: ISR reward landscape 几何结构未分析\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  resolution: experiments.tex 包含 reward landscape 分析。\n  resolution_round: 7\n- id: v6-R2-N1\n  summary: ISR 核心指标命名不一致\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: 全文统一使用 Irreducible Solver Rate。\n  resolution_round: 7\n- id: v6-R2-W5\n  summary: \"ISR 名称含 'Reward' 具有误导性\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"ISR 统一为 'Irreducible Solver Rate'。\"\n  resolution_round: 7\n- id: v6-R1-W2\n  summary: Dose-response claim 统计上不足\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers:\n    - 1\n    note: 整体统计 power 批评。\n  - round: 12\n    reviewers:\n    - 1\n    note: \"R1-W3: 4β×3-5seeds 仍稀疏。R12 fix: 加强 preliminary 标注（commit 9dc8835）。D134 扩展 β=0.1 到 10 seeds。\"\n  - round: 13\n    reviewers:\n    - 1\n    note: \"R1-N3: 4 个 dose 各只 3-5 seeds，dynamics 定性各异但统一称 'Goodhart collapse'。R2 反驳称 structural argument 足够。分歧记录。\"\n  - round: 14\n    reviewers:\n    - 1\n    note: \"R14: R1 [RESOLVED]。\"\n  resolution: \"§4.2 line 110 标注 'preliminary'。\"\n  resolution_round: 14\n- id: v6-R2-W2\n  summary: §4.3 的 β 值呈现顺序非升序\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 10\n  resolution: 已按升序呈现。\n  resolution_round: 10\n- id: v6-R2-W6-LOO\n  summary: LOO 缩写未在首次使用时正式定义\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: introduction.tex 现有完整定义。\n  resolution_round: 7\n- id: v6-R2-W8\n  summary: Hacking taxonomy 分类标准不够 principled\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers:\n    - 1\n    note: 仅 H1/H7 有 precision 验证。\n  - round: 12\n    reviewers:\n    - 1\n    - 2\n    note: \"R1-W4 + R2-W3: robust vs isolated 应在 Abstract 区分。R12 fix: Abstract 改为 'three robust modes (H1/H7/H8) + additional isolated observations'（commit 9dc8835）。\"\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: \"R1: H8 只在 s42 完成审计，'validated across multiple seeds' 对 H8 是否准确？R2: taxonomy 有独立工具价值但仅 H1/H7 有 precision 验证。\"\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: CE/TS/PG/CI 重命名改善可读性。CE/TS precision >95% 验证。PG claim 降为 'observed at lower prevalence'。分类标准仍为规则+功能分析混合。\"\n- id: v7-R1-N2\n  summary: CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: CMH 移至 Appendix，正文以 seed-level permutation p=0.26 为 primary。\n  resolution_round: 9\n- id: v7-R2-MR1\n  summary: 缺少 Goodhart's Law 经典引用\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  resolution: references.bib 包含 Goodhart 1975。\n  resolution_round: 8\n- id: v7-R2-W7\n  summary: \"experiments.tex 'Notably' AI 写作标记\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: \"'Notably' 已移除。\"\n  resolution_round: 9\n- id: v8-R12-N1\n  summary: Goodhart 发现的可预测性限制概念新颖性\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers:\n    - 1\n    - 2\n    note: R2-N2 [critical]。\n  - round: 12\n    reviewers:\n    - 1\n    - 2\n    note: R1 Excitement 3/5 认为 empirical details 超出可预测范围，R2 2.5/5。两人均同意 Findings。结构性问题。\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: \"R2-N1 [critical]: H7 的 ISR≥0.5 是数学必然，不需实验确认。R1 部分同意但认为 dynamics 细节有价值。结构性问题：核心发现的可预测性是概念层面的限制，无法通过写作修改解决。\"\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: Gated ISR 实验增量改善 (诊断→诊断+mitigation attempt)。TS→PG mode migration 是非平凡发现。但核心 novelty concern (LOO 标准+Goodhart 可预测) 仍为结构性限制。R1 3.5 vs R2 3.0，分歧在 empirical rigor vs conceptual novelty 权重。\"\n- id: v8-R1-N3\n  summary: 术语交替使用导致语义滑移\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers:\n    - 2\n    note: \"Fig 2/3 'Genuine' → 'Non-hacking' 已修复。偶见残留。\"\n  - round: 12\n    reviewers: []\n    note: R12 未再提及术语滑移。\n  - round: 13\n    reviewers: []\n    note: R13 未再提及术语滑移。可能已修复，待确认。\n  - round: 14\n    reviewers:\n    - 2\n    note: \"R14: R2 [RESOLVED]。Grep 确认无 H1/H7/H8/H9 残留。\"\n  resolution: H1→CE, H7→TS, H8→PG, H9→CI 全文重命名完整一致。无残留旧名称。\n  resolution_round: 14\n- id: v8-R12-N2\n  summary: 实验范围与标题/claim scope 不匹配\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers:\n    - 1\n    - 2\n    note: \"Subtitle 改为 'GRPO-Trained FOL Reasoners'。\"\n  - round: 12\n    reviewers:\n    - 1\n    - 2\n    note: \"R2-N3 [critical]: 仍暗示通用结论。R12 fix: C3 弱化为 'evidence of generality'，Contributions 加 'from a single model family and dataset'（commit 9dc8835）。\"\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: \"R2-W1: C3 仍在同一 dataset 和 model family 内。Discussion line 11 'STA applies to any compositional-input/binary-verifier setting' 缺乏验证。两人一致认为泛化性 claim 仍需进一步 hedge。\"\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: R1 [RESOLVED]。Hedging 充分。\"\n  resolution: \"C3 加 'in principle...preliminary'。Discussion 加 'should in principle transfer'。§4.3 显式声明无 Prolog random control。\"\n  resolution_round: 14\n- id: v8-R1-W4\n  summary: 多重比较未校正\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers:\n    - 1\n    note: \"limitations.tex 新增 'Multiple comparisons' 段落。\"\n  - round: 12\n    reviewers: []\n    note: R12 未再单独提及。\n  - round: 13\n    reviewers:\n    - 1\n    note: \"R1-W3: CMH independence violation 仍需更清晰标注为 'directional only'。R2 AGREE。\"\n  - round: 14\n    reviewers:\n    - 1\n    note: \"R14: R1 [RESOLVED]。\"\n  resolution: \"Appendix line 126 标注 CMH 'p-values are consequently inflated'。功能等价于 'directional only'。\"\n  resolution_round: 14\n- id: v8-R1-MR\n  summary: 缺少 reward shaping 和 inference-time hacking 引用\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: Uesato 2022, Paulus 2018, Langosco 2022 等已补充。\n  resolution_round: 10\n- id: v9-R1-N3\n  summary: Premise-count confound 影响范围分歧\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: method.tex 增加 confound 两场景区分句。\n  resolution_round: 9\n- id: v9-R12-W1\n  summary: §4.4 标题措辞过强\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"§4.4 标题改为 'Cross-Logic Extension'。\"\n  resolution_round: 9\n- id: v9-R1-W5\n  summary: 训练时 sampling vs 评估时 greedy 不一致\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: §4.1 已增加讨论。\n  resolution_round: 9\n- id: v9-R12-Q-ISR-FILTER\n  summary: ISR 作为 filter 未测试\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"conclusion.tex 增加 'ISR as post-hoc filter' 作为 future work。\"\n  resolution_round: 9\n- id: v9-R12-Q-NORMALIZED-ISR\n  summary: 未测试 premise-count-normalized ISR\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"conclusion.tex 增加 'normalized variants' 作为 future work。\"\n  resolution_round: 9\n- id: v4-RV-STALE-APPENDIX\n  summary: Appendix Table 仍用旧数据\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 7\n  resolution: Appendix Table 5 现含完整 per-seed data。\n  resolution_round: 7\n- id: v10-R12-N1\n  summary: §4.5 与 Limitations 关于 1.7B seed 数量矛盾\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  resolution: D129 完整 3-seed 数据重写 §4.5。\n  resolution_round: 11\n- id: v10-R2-Q6\n  summary: ISR=0.75 推导与实测不一致\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  resolution: 改为 ISR≥0.5。PDF 已重编译。\n  resolution_round: 11\n- id: v10-R2-W7\n  summary: \"'Valid but Vacuous' 中 'valid' 有歧义\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers:\n    - 2\n    note: \"建议改为 'Verified but Vacuous'。保留原标题决策。\"\n  - round: 12\n    reviewers: []\n    note: Round 12 未再提及。\n  - round: 13\n    reviewers: []\n    note: Round 13 未再提及。可能不再是活跃问题。\n  - round: 14\n    reviewers: []\n    note: \"R14: 未再提及。\"\n- id: v10-R2-W8\n  summary: Discussion/Conclusion 过于简短\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers:\n    - 1\n    - 2\n    note: Discussion 扩展到 ~33 行。\n  - round: 12\n    reviewers: []\n    note: R12 未批评长度。P0 压缩后约 11 行但内容更密集。\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: \"R2: Discussion 缺 forward-looking content（mitigation 方向）。R1 部分同意，建议增加 mitigation 困难性分析段落。\"\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: R2 [RESOLVED]。有实质 mitigation 内容。\"\n  resolution: Discussion 扩展至 14 行。含 gated ISR 实验 + reward ensembling + constrained optimization + TRACE 方向。\n  resolution_round: 14\n- id: v10-R2-W5\n  summary: C2 和 C4 边界不清晰\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: Contributions 合并为 3 条。\n  resolution_round: 10\n- id: v11-R12-N1\n  summary: Responsible NLP Research Checklist 缺失\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: checklist.tex 创建并附在论文末尾。\n  resolution_round: 11\n- id: v11-R1-W2\n  summary: Taxonomy 仅 H1/H7 有 precision 验证\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers:\n    - 1\n    note: 其余 modes 缺独立验证。\n  - round: 12\n    reviewers:\n    - 1\n    - 2\n    note: \"R12 fix: Abstract 区分 robust vs isolated modes（commit 9dc8835）。\"\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: \"R1: H8 只在 s42 完成审计。R2: taxonomy 有独立工具价值。两人均认为 Abstract 的 'validated across multiple seeds' 对 H8 不准确。\"\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: R2 [RESOLVED]。Claim 适当下调。\"\n  resolution: \"Abstract 'PG, observed at lower prevalence'。Method 明确 CE/TS robust (≥3 seeds) vs PG low prevalence。\"\n  resolution_round: 14\n- id: v11-R1-W5\n  summary: O(1) binary ablation ISR*≈0.007 反直觉结果未充分解释\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n  - round: 12\n    reviewers: []\n    note: Round 12 未再提及。\n  - round: 13\n    reviewers: []\n    note: Round 13 未再提及。\n- id: v11-R2-MR\n  summary: 缺少 2025-2026 最新引用\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n  - round: 12\n    reviewers:\n    - 1\n    - 2\n    note: \"R12 fix: 已加入 STaR + Cobbe（commit 9dc8835）。Lean-based RL 如空间允许后续补。\"\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: R1 补 LEGO-Prover。R2 补 Llemma (Azerbayev 2024)。两人一致缺 reward hacking mitigation 文献。\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: R2 [RESOLVED]。引用覆盖完整。\"\n  resolution: 新增 Llemma、Coste 2024、Moskovitz 2024。Related Work + Discussion 均引用。\n  resolution_round: 14\n- id: v11-R12-PDF\n  summary: PDF 与 .tex 不一致\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: PDF 从 paper/ 重编译。\n  resolution_round: 11\n- id: v12-R2-N1\n  summary: 正文超出 ARR 8 页限制约 0.75 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: Table 2 移入 Appendix，Related Work/Discussion/Limitations 压缩。主文本完整收于第 8 页。\n  resolution_round: 12\n- id: v12-R2-W4\n  summary: Table 1 ISR β=0.1 ISR* 列缺失\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: Table 1 补 ISR*=0.63±.23，N-H 改用 corrected 3-seed 6%，footnote 说明。\n  resolution_round: 12\n- id: v12-R2-W2\n  summary: 与 Kim et al. (2026) 区分需更锐利\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n  - round: 12\n    reviewers:\n    - 2\n    note: Introduction 增加 explicit 对比句（training-time vs inference-time）。\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: \"R2-N2 [critical]: 仅一句对比不够，需逐条比较 gaming modes、detection methods、experimental settings。R1 同意需更多对比但降为 [major]。R1 建议: 共同点 + 差异 + 互补关系三段对比。\"\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: R2 [RESOLVED]。对比充分且有洞察。同 v13-R2-N2。\"\n  resolution: \"Related Work 新增完整 'Faithfulness in formalization' 段落，3 维度逐条对比 Kim et al.。\"\n  resolution_round: 14\n- id: v12-R1-W2\n  summary: Component-count confound deconfounding analysis 仅在 Appendix\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n  - round: 12\n    reviewers:\n    - 1\n    note: \"R1-W2。R2 [REBUT]: 核心 claim 基于 taxonomy 而非 raw ISR。分歧记录。\"\n  - round: 13\n    reviewers: []\n    note: Round 13 未直接提及此 item。但 R1-W1 关于 ISR≠semantic quality 隐含相关性。\n- id: v13-R2-N2\n  summary: 与 Kim et al. (2026) 差异化不充分：仅一句区分，缺逐条对比\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: \"R2-N2 [critical]。R1 [AGREE] 但建议降为 major（方法论层面不重叠）。分歧在 severity：R2 critical vs R1 major。建议: Related Work 增加专门对比段。\"\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: R2 [RESOLVED]。'充分且有深度'。\"\n  action_items:\n  - round: 13\n    action: \"Related Work 增加与 Kim et al. (2026) 的逐条对比：gaming modes 重叠、detection 方法差异、inference-time vs training-time\"\n    assigned_to: research_director\n    status: open\n  resolution: \"Related Work 新增完整 'Faithfulness in formalization' 段落：training vs inference、STA/ISR vs LLM-judge、universal gaming vs no-gaming、CE ≈ axiom-fabrication 互补性。\"\n  resolution_round: 14\n- id: v13-R1-W1\n  summary: \"ISR 与 NLI accuracy 无关 (ρ=-0.049) 但 'structural quality diagnostic' 定位可能误导\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: \"R1-W1 [major]。R2 [AGREE]。ISR 高不意味好推理（H7 也高），ISR 低不一定坏推理（Prolog redundancy）。'Structural integrity' ≠ 'reasoning quality'。Introduction/Abstract 的 framing 可能给读者过于正面的印象。\"\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: R2 [RESOLVED]。措辞精确。Abstract 仍用 'structural integrity' 但在上下文中可接受。\"\n  action_items:\n  - round: 13\n    action: \"更精确界定 ISR diagnostic 能力——是 component necessity 度量而非 reasoning quality 度量\"\n    assigned_to: research_director\n    status: open\n  resolution: \"Method §3.2 line 46: 'ISR is a component-necessity diagnostic, not a reasoning-quality metric'。全文 framing 校正。\"\n  resolution_round: 14\n- id: v13-R2-W4\n  summary: 缩写和术语密度过高（~17 个缩写需同时追踪）\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: R2-W4。R1 [AGREE]。建议减少 3-4 个缩写（如 S-NH 延迟引入，CI 直接写 content-independent）或加 notation summary。\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: ~18 缩写，未添加 notation summary。但 H1→CE 等描述性重命名显著改善可读性。R2 降为 minor。\"\n  action_items:\n  - round: 13\n    action: 减少缩写使用或添加 notation summary table\n    assigned_to: research_director\n    status: open\n  resolution: ''\n  resolution_round: null\n- id: v13-R2-W5\n  summary: Table 2 混合 single-seed 和 pooled 数据，对比不公平\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: R2-W5。R1 [AGREE]。Exec 列 = s42 only vs ISR/Rnd = 5-seed pooled。建议统一为 3-seed pooled 或增加 n(seeds) 列。\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: R2 [RESOLVED]。聚合方式标注清晰。\"\n  action_items:\n  - round: 13\n    action: 统一 Table 2 聚合方式或标注每列 seed 数\n    assigned_to: research_director\n    status: open\n  resolution: \"Table 2 caption 标注 '$^a$Single seed (s42); remaining columns pooled (ISR/Rnd 4B: 5-seed; Prolog/1.7B: 3-seed)'。\"\n  resolution_round: 14\n- id: v13-R2-MITIGATION\n  summary: Discussion 缺少 mitigation 策略讨论和 forward-looking analysis\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: \"R2 [major concern]: 论文只诊断不治疗。R1 部分同意，建议增加: (1) KL regularization 为何不足 (cite Kwa 2024), (2) reward ensembling 可能性, (3) component-count normalization 的 negative result (1.06×)。两人一致认为 Discussion 过于 hand-waving。\"\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: R2 [RESOLVED]。有实验支撑和文献对接。\"\n  action_items:\n  - round: 13\n    action: Discussion 增加 mitigation analysis 段落\n    assigned_to: research_director\n    status: open\n  resolution: \"Discussion lines 11-14: gated ISR 实验 (TS→PG migration) + reward ensembling (Coste 2024) + constrained optimization (Moskovitz 2024) + TRACE 方向。\"\n  resolution_round: 14\n- id: v13-R1-Q4\n  summary: Prolog cross-logic 实验缺少 random control\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: R1-Q4。R2 [AGREE]。无法区分 ISR-specific Goodhart vs generic GRPO instability under augmented reward。\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: R1 [RESOLVED]。限制明确承认。\"\n  action_items:\n  - round: 13\n    action: 至少讨论此限制，理想情况下补充 Prolog random/exec-only 数据\n    assigned_to: research_director\n    status: open\n  resolution: \"§4.3 line 118: 'No matched random control was run for Prolog' 显式声明。\"\n  resolution_round: 14\n- id: v14-R12-GATED-S54\n  summary: Gated ISR Discussion 遗漏 s54 反例 (96.7% non-hacking)\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"Discussion 只提 '2/3 seeds migrate to PG'，忽略 s54 (96.7% N-H)。两位 reviewer 一致认为有选择性呈现嫌疑。建议改为 '2/3 seeds migrate to PG, while 1/3 sustains predominantly non-hacking output (96.7%); outcome is highly seed-dependent with only 3 seeds.'\"\n  action_items:\n  - round: 14\n    action: Discussion 补充 s54 数据和 seed-dependence caveat\n    assigned_to: research_director\n    status: open\n  resolution: ''\n  resolution_round: null\n- id: v14-R1-LIMITATIONS\n  summary: Limitations section 压缩至 6-7 行，SFT n=39 限制未单独提及\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 14\n    reviewers:\n    - 1\n    note: 8 页限制下可理解，但 Limitations 不再是 R13 评价的 '论文亮点'。关键内容散落在正文和 Appendix。\n  action_items: []\n  resolution: ''\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "solver-trace-ablation",
    "issues_yaml": "issues:\n- id: R1-W1\n  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。Fisher exact test + Wilson 95% CI 已加入。eval 集 100 例限制在 limitations.tex 讨论。\n  resolution_round: 2\n- id: RV-EVAL-FALLBACK\n  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: 第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)，无 fallback。\n  resolution_round: 1\n- id: RV-D060-NARRATIVE\n  summary: D060 'Goodhart instability' 叙事：77pp PR 差距在同一测试集上确认成立\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。\n  resolution_round: 2\n- id: RV-FIG2-STALE-SCRIPT\n  summary: figures/paper/gen_fig2.py 旧脚本数据错误\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: 已修复。\n  resolution_round: 1\n- id: R1-W2\n  summary: ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。\n  resolution_round: 2\n- id: R2-W1\n  summary: Limitations section 格式不合规\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 独立 limitations.tex 已创建，位于 references 之前。\n  resolution_round: 3\n- id: R2-W2\n  summary: 实验仅用单一模型 (Qwen3-4B) 和单一数据集 (FOLIO)，标题复数暗示通用性\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 标题改为单数。Qwen3-1.7B cross-scale 实验已加入。\n  resolution_round: 3\n- id: R1-W4\n  summary: Exec-only seed 43 使用 sampling (T=0.7) 评估而非 greedy\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: exec-only 500-step 主表仅报告 s42（†标注）。\n  resolution_round: 2\n- id: R1-W3\n  summary: \"'Solver-agnostic' 仅测 2 solver，过度声明\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"'solver-agnostic' 已从全文移除。\"\n  resolution_round: 2\n- id: R2-W6\n  summary: SFT baseline 比较不公平：PR=14% vs 93%，低 PR 本身减少 hacking 机会\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 100-step RL 对照已加入。claim 调整为 'consistent with'。\n  resolution_round: 2\n- id: R2-W7\n  summary: 与 Kim et al. (2026) 差异化不充分\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: related_work.tex 中有区分段落。\n  resolution_round: 2\n- id: R1-W6\n  summary: 训练 500 例/评估 100 例的规模限制讨论不充分\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: limitations.tex 已讨论。\n  resolution_round: 2\n- id: R1-W7\n  summary: H1/H7 classifier precision/recall 未报告\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: 50 样本人工验证 precision >95%。\n  resolution_round: 2\n- id: R1-W8\n  summary: Random control U(0,1) 与 ISR 的 skewed 分布不匹配\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: method.tex 和 experiments.tex 均说明了 Random 设计目的。\n  resolution_round: 2\n- id: R1-W9\n  summary: 缺代码/数据开源承诺\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 0\n  resolution: \"abstract.tex:9 脚注 'Code and data: [anonymized]'。\"\n  resolution_round: 2\n- id: R1-W5\n  summary: \"'Meta-level Goodhart' 新颖性论证不足\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: framing 降级为 empirical instance。\n  resolution_round: 3\n- id: R2-W8\n  summary: H1/H7 编号不连贯（H2-H6 不存在）\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: method.tex 解释了合并原因。\n  resolution_round: 3\n- id: v2-R1-N1\n  summary: Abstract '93%' PR 为 single seed，应改为 mean±std\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: Abstract 使用 3-seed pooled mean±std。\n  resolution_round: 3\n- id: v2-R1-N3\n  summary: 仅 2 个 β 值不足以刻画 dose-response\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 4 个 β 值提供完整 dose-response 曲线。\n  resolution_round: 4\n- id: v2-R2-N3\n  summary: STA 方法论新颖性有限\n  category: method\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: novelty 定位为 applying standard LOO。\n  resolution_round: 3\n- id: v2-R2-N2\n  summary: 单模型+单数据集泛化性不足\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: cross-scale 实验加入。单数据集限制在 Limitations 讨论。\n  resolution_round: 3\n- id: v2-R1-W3\n  summary: ISR-as-reward 控制 confound 后净效果仅 1.06×\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: ISR 定位从 training signal 转为 diagnostic-only。\n  resolution_round: 3\n- id: v2-R1-W6\n  summary: Hacking taxonomy 缺乏 IAA 验证\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: deterministic rules + 50-sample precision check。\n  resolution_round: 3\n- id: v2-R2-W3\n  summary: Abstract 信息密度过高\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: Abstract 重写为 ~170 words。\n  resolution_round: 3\n- id: v2-R2-W4\n  summary: Premise-count confound 讨论放在 Appendix 而非正文\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 提升到正文 §3.2。\n  resolution_round: 3\n- id: v2-R2-W5\n  summary: C2 和 C4 独立性不足\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: taxonomy 独立性论证成立。\n  resolution_round: 3\n- id: v2-FMT-1\n  summary: Limitations section 位于 References 之后\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 顺序已正确。\n  resolution_round: 3\n- id: v2-FMT-2\n  summary: Ethics Statement 缺失\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: ethics.tex 加入。\n  resolution_round: 3\n- id: v2-FMT-3\n  summary: Orphan bibliography entries\n  category: format\n  severity: info\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: orphan entries 清除。\n  resolution_round: 3\n- id: v2-R1-M4\n  summary: Prolog cross-logic transfer 样本量过小\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: \"'universal Goodhart' 移除，改为 qualitative observation。\"\n  resolution_round: 3\n- id: v2-R1-W1\n  summary: 3 seeds 统计效力不足以支撑定量 claims\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 统计方法改进。定量 claims 降级。\n  resolution_round: 3\n- id: v2-R1-W4\n  summary: SFT baseline 比较因 PR 悬殊说服力有限\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 100-step RL 对照充分利用。\n  resolution_round: 3\n- id: R2-MISSING-REF\n  summary: 引用覆盖不足\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 3\n  resolution: 31 条引用覆盖核心领域。\n  resolution_round: 3\n- id: v3-R1-NI-2\n  summary: β=0.2 未在 Table 1 中独立报告\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: Table 1 现已包含 β=0.2 行。\n  resolution_round: 4\n- id: v3-R1-NI-3\n  summary: §4.2 cross-seed 描述暗示最终状态\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"现标注 '(at 500 steps)'。\"\n  resolution_round: 4\n- id: v3-R12-NI-4\n  summary: 全文 em-dash AI 写作痕迹\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 5\n  resolution: em-dash=0, -ing endings 仅 4 处轻微, blacklisted words=0。\n  resolution_round: 5\n- id: v3-R2-NI-5\n  summary: \"Abstract 'zero structurally sound outputs' 与 N-H=8% 矛盾\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 3\n  last_seen_round: 4\n  resolution: \"Abstract 现用 'effectively zero...at convergence'。\"\n  resolution_round: 4\n- id: v3-R12-NI-1\n  summary: Cross-scale 实验 seed 数量不足\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 3\n  last_seen_round: 14\n  mentions:\n  - round: 3\n    reviewers:\n    - 1\n    - 2\n    note: 两位 reviewer 一致。\n  - round: 10\n    reviewers:\n    - 1\n    - 2\n    note: 现已用 D129 完整 3-seed 数据重写 §4.5。\n  - round: 11\n    reviewers:\n    - 1\n    note: \"R1-W4: 3 seeds 仍不足以作为独立 contribution 支撑。D134 扩展至 10 seeds 正在训练中。\"\n  - round: 12\n    reviewers:\n    - 1\n    - 2\n    note: \"R1-N1 再次要求增加模型/数据集多样性。R2-N3 将 C3 cross-logic 定为 preliminary 不应为正式 contribution。两人一致建议降级 C3。R12 fix: C3 弱化为 'evidence of generality'（commit 9dc8835）。\"\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: \"R13 R2-W1: C3 仍在同一 dataset (FOLIO) 和 model family (Qwen3) 内。两位 reviewer 一致要求进一步 hedge C3 措辞。\"\n  - round: 14\n    reviewers: []\n    note: \"R14: 未直接提及。C3 已 hedge 为 'in principle...preliminary'。\"\n- id: v4-R12-N2\n  summary: \"'Inevitable collapse at all doses' claim 超出证据\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 14\n  mentions:\n  - round: 9\n    reviewers:\n    - 1\n    - 2\n    note: \"共识: 区分 'observed in all seeds tested' vs 'population-level inference'。\"\n  - round: 11\n    reviewers:\n    - 1\n    - 2\n    note: \"术语降级为 'seed-dependent divergence' 和 'dose-varying patterns'。\"\n  - round: 12\n    reviewers:\n    - 1\n    - 2\n    note: \"R1-W3 再次指出稀疏。R1 交叉回应认为 'all tested doses show Goodhart collapse' 成立。R12 fix: 加强 preliminary 标注，区分 500-step snapshot vs trajectory（commit 9dc8835）。\"\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: \"R1-N3 认为 Abstract/Discussion 仍需更多 hedging。R2 反驳称 structural argument (H7 恒定 ISR≥0.5) 使 'at every tested dose' 成立。分歧记录。\"\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: R1 [RESOLVED]，R2 未再提及。Abstract 'every tested dose' 在全文语境下充分。\"\n  resolution: \"'four tested doses' + 'preliminary' 标注。§4.2 line 110 明确 seed count。\"\n  resolution_round: 14\n- id: v4-R12-N3\n  summary: OR=3.48 (uncorrected) vs OR=0.61 (corrected) 方向反转\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 14\n  mentions:\n  - round: 10\n    reviewers:\n    - 1\n    - 2\n    note: Table 1 和 Discussion §5 仍以 23% (uncorrected) 为 headline。\n  - round: 11\n    reviewers:\n    - 1\n    - 2\n    note: OR 反转仍是核心问题。降级为 major。\n  - round: 12\n    reviewers:\n    - 1\n    - 2\n    note: \"R1-N2 + R2-N2 [critical]。Seed-level p=0.26，corrected OR=0.61。R12 fix: transient window 降级为 descriptive observation，Table 1 N-H 改用 corrected 6%，论文最强 claim 锚定为 'Goodhart collapse at every dose'（commit 9dc8835）。\"\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: \"Table 1 现用 corrected 6%†，但 footnote 同时给出 uncorrected 23%。R2 指出 non-hacking permutation p=0.917 且 point estimate ISR(2.3%) < Random(5.9%) 方向反转。两位 reviewer 一致认为 transient window 不构成 ISR 优势证据。\"\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: Table 1 用 corrected 6%†。但方向反转 (ISR N-H 6.06% < Random 9.5%) 未在正文讨论。两位 reviewer 一致认为应在 §4.3 或 Discussion 增加 1-2 句，且这实际上强化核心论点。Matched cohort 同方向 (2.3% vs 5.9%)。\"\n- id: v4-R12-W6\n  summary: Seed 43 exec-only 评估协议矛盾\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 14\n  mentions:\n  - round: 10\n    reviewers:\n    - 1\n    - 2\n    note: Appendix Table 5 s43-500 Notes 列已修正。\n  - round: 12\n    reviewers: []\n    note: Round 12 未提及。Appendix 中已有 † 标注。\n  - round: 13\n    reviewers:\n    - 1\n    note: \"R1-W4 [minor]: s43 数据仍在 cross-seed 比较中出现（§4.1），建议正文加脚注。\"\n  - round: 14\n    reviewers:\n    - 1\n    note: \"R14: R1 [RESOLVED]。脚注已添加。\"\n  resolution: §4.2 line 34 脚注说明 sampling eval (T=0.7) 及不可比性。\n  resolution_round: 14\n- id: v4-R12-W7\n  summary: Deleted checkpoints (ISR β=0.1 s43/s44) 导致 H8 audit 不完整\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers:\n    - 1\n    - 2\n    note: \"'All N-H rates are upper bounds' 声明已加入 method.tex。\"\n  - round: 12\n    reviewers:\n    - 1\n    - 2\n    note: \"R1-N3 [critical]: 5-seed N-H=23% 为 uncorrected upper bound。R12 fix: Table 1 改用 corrected 3-seed 6%，footnote 说明（commit 9dc8835）。\"\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: \"R1-W5 [minor]: Table 1 脚注存在但不够醒目。R2-W6: N-H% 列建议标注 '(upper bound)'。两位 reviewer 一致。\"\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: R1 [RESOLVED]。标注清晰。\"\n  resolution: \"Table 1 caption 标注 'N-H is an upper bound'。Method §3.5 line 76 声明。\"\n  resolution_round: 14\n- id: v4-R1-W8\n  summary: 100 eval samples 对 per-seed claims 统计功效不足\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 14\n  mentions:\n  - round: 12\n    reviewers:\n    - 1\n    - 2\n    note: R1-W5 + R2 [AGREE with nuance]。建议报告 Wilson CI。\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: \"R1-N2 [critical]: 5-seed pooled N-H 23% vs 3-seed corrected 6% 差 17pp；matched cohort non-hacking permutation p=0.917 因 n=5 power 不足无法检测效应。R2 补充: ISR s45 n=42 的 54.8% N-H 实际只有 ~23 samples。两人一致建议扩大 eval set 或附 CIs。\"\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: R1 [RESOLVED]。CIs 在 matched table + Limitations 中完整呈现。\"\n  resolution: \"Matched cohort table 附完整 Wilson CIs。Limitations 量化 '100-example...Wilson 95% CI [2.3%, 12.7%]'。\"\n  resolution_round: 14\n- id: v4-R2-W9\n  summary: 方法新颖性有限：Algorithm 1 仅 6 行伪代码\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 4\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers:\n    - 1\n    - 2\n    note: \"共识: Findings 级别。\"\n  - round: 12\n    reviewers:\n    - 1\n    - 2\n    note: R1 Excitement 3/5, R2 2.5/5。两人均同意 Findings。\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: \"R2-N1 [critical]: LOO+Goodhart 均为已知。R1 部分同意但认为 empirical contributions 有增量价值（seed-dependent divergence, H7b triple gaming, cross-logic diversity）。R1 Excitement 3.0 vs R2 2.5。分歧但共识区间 Findings-Borderline Conference。\"\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: Introduction line 21 自我定位为 'empirical case study'。Gated ISR 增添实证贡献。但 LOO 是标准技术这一结构性限制无法修改解决。R2 [PARTIALLY RESOLVED]。\"\n- id: v4-R2-W5\n  summary: 未测试 tautology-guarded ISR 变体\n  category: method\n  severity: warning\n  status: wont_fix\n  first_raised_round: 4\n  last_seen_round: 14\n  resolution: Future work. Arms-race evidence 已有。\n  resolution_round: 4\n  mentions:\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: Gated ISR 实验 (Appendix §B.11) 测试了 component-count gate 变体。TS 消除但 PG 迁移。原标记 wont_fix 现部分回应。\"\n- id: v5-R1-N3\n  summary: Table 1 比较框架不对称\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 14\n  mentions:\n  - round: 10\n    reviewers:\n    - 1\n    - 2\n    note: Table 1 已拆分为 primary + cross-scale。\n  - round: 11\n    reviewers: []\n    note: 未直接提及。\n  - round: 13\n    reviewers:\n    - 1\n    note: \"R1 Detailed Comments: Table 1 混合 500-step 和 1000-step 结果需更清楚标注。\"\n  - round: 14\n    reviewers:\n    - 1\n    note: \"R14: R1 [RESOLVED]。标注清晰。\"\n  resolution: \"Table 1 caption '500 steps unless noted'。SFT/Exec-only 行标签明确 '1k'。\"\n  resolution_round: 14\n- id: v5-R2-N3\n  summary: \"'Diagnostic becomes optimization target' 概念新颖性有限\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers:\n    - 1\n    - 2\n    note: R2-N2 [critical]。R1 认为 empirical phenomena 有独立价值但同意 Findings。\n  - round: 12\n    reviewers:\n    - 1\n    - 2\n    note: R1 Excitement 3/5 vs R2 2.5/5。两人均同意 Findings。结构性问题。\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: \"同上。R2 进一步论证: ISR 的不对称性原因 'too straightforward'（LOO 偏好低 component count，H7 是全局最优 exploit）。结构性问题，无法通过修改解决。\"\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: Gated ISR 的 TS→PG migration ('blocking one Goodhart pathway redirects optimization pressure') 是非平凡发现。R2 Novelty 2.5→3.0。但概念新颖性限制仍为结构性问题。R2 [PARTIALLY RESOLVED]。\"\n- id: v5-R2-W1\n  summary: Abstract 数据堆砌 / 单 seed 数据选择性报告\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers:\n    - 1\n    - 2\n    note: \"R11 fix: 数字减至 ≤3 个 headline figures。\"\n  - round: 12\n    reviewers: []\n    note: R12 未再提及 Abstract 数据堆砌（质量重写后改善）。但 R12 建议术语密度可进一步降低。\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: \"R2-W3: Abstract '99.5% structural collapse' 来自 s42 单 seed 100→1000 步轨迹，有 cherry-picking 嫌疑。R1 交叉时 [AGREE]，建议改为 3-seed aggregate (ISR*=0.03±0.05)。两人一致。\"\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: R2 [RESOLVED]。消除 cherry-picking 嫌疑。\"\n  resolution: Abstract 改用 3-seed aggregate (ISR*=0.03±0.05 across three seeds at 1000 steps)。\n  resolution_round: 14\n- id: v5-R2-W3\n  summary: paragraph{} 过度碎片化\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers:\n    - 2\n    note: method/conclusion/limitations 仍有多个 paragraph{}。\n  - round: 12\n    reviewers: []\n    note: \"R12 未再提及 paragraph{} 问题（质量重写后已大幅改善）。\"\n  - round: 13\n    reviewers: []\n    note: R13 未提及。可能已修复，待确认。\n  - round: 14\n    reviewers:\n    - 2\n    note: \"R14: R2 [MOSTLY RESOLVED]。不再碎片化。\"\n  resolution: 段落结构大幅改善。Limitations 紧凑单段，Discussion 14 行连贯段落。\n  resolution_round: 14\n- id: v5-R2-W4\n  summary: Experiments §4.3 按 β 值呈现顺序非升序\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 10\n  resolution: §4.3 已按升序呈现。\n  resolution_round: 10\n- id: v5-R12-SFT-PR\n  summary: SFT baseline PR confound (PR=13% vs 93%)\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 5\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers:\n    - 1\n    - 2\n    note: SFT caveat 加入。\n  - round: 12\n    reviewers:\n    - 1\n    - 2\n    note: \"R1-W1 + R2-W1。R12 fix: Abstract 加 'though the large prove-rate gap prevents definitive causal attribution'。Limitations 加 SFT best-of-N open question（commit 9dc8835）。\"\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: \"R1-N1 [critical]: RL-specificity claim 依赖此对比但证据基础薄弱。SFT n=39，100-step checkpoint 仅 s42 (n=32)。R2-W2 [major] 完全同意。两位 reviewer 一致要求进一步降低 RL-specificity claim 强度。\"\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: Abstract/Introduction/Discussion hedging 全面改善 ('associated with...though gap prevents')。但 §4.2 line 42 仍用 'RL-specific' 旧措辞，缺 caveat。一处遗漏的统一化修改。\"\n- id: v5-R2-MR\n  summary: 缺少重要引用\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers:\n    - 2\n    note: 已加入 Cao et al. 2026 + Wang et al. 2025。\n  - round: 12\n    reviewers:\n    - 1\n    - 2\n    note: \"R12 建议补充 STaR + Cobbe + Lean-based RL。R12 fix: 已加入 STaR (Zelikman 2022) + Cobbe (2021)（commit 9dc8835）。\"\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: \"R1: 补 LEGO-Prover, formal verification reward design。R2: 补 Lean-based RL (Llemma), reward hacking mitigation 策略, RLVR 其他工作。两人一致缺 mitigation literature 引用。\"\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: R2 [RESOLVED]。引用覆盖完整。\"\n  resolution: 新增 Llemma (Azerbayev 2024)、Coste 2024 (reward ensembling)、Moskovitz 2024 (constrained optimization)。引用覆盖充足。\n  resolution_round: 14\n- id: v5-R2-W6\n  summary: Table 1 信息密度过高\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 10\n  resolution: \"已拆分为 Table 1 + Table 2。R12: Table 2 移入 Appendix 节省空间。\"\n  resolution_round: 12\n- id: v5-R1-W5\n  summary: Goodhart taxonomy variant 未指定\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  resolution: \"related_work.tex 指定 'primarily regressional, with extremal elements'。\"\n  resolution_round: 7\n- id: v5-R1-W6\n  summary: ISR reward landscape 几何结构未分析\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 5\n  last_seen_round: 7\n  resolution: experiments.tex 包含 reward landscape 分析。\n  resolution_round: 7\n- id: v6-R2-N1\n  summary: ISR 核心指标命名不一致\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: 全文统一使用 Irreducible Solver Rate。\n  resolution_round: 7\n- id: v6-R2-W5\n  summary: \"ISR 名称含 'Reward' 具有误导性\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: \"ISR 统一为 'Irreducible Solver Rate'。\"\n  resolution_round: 7\n- id: v6-R1-W2\n  summary: Dose-response claim 统计上不足\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers:\n    - 1\n    note: 整体统计 power 批评。\n  - round: 12\n    reviewers:\n    - 1\n    note: \"R1-W3: 4β×3-5seeds 仍稀疏。R12 fix: 加强 preliminary 标注（commit 9dc8835）。D134 扩展 β=0.1 到 10 seeds。\"\n  - round: 13\n    reviewers:\n    - 1\n    note: \"R1-N3: 4 个 dose 各只 3-5 seeds，dynamics 定性各异但统一称 'Goodhart collapse'。R2 反驳称 structural argument 足够。分歧记录。\"\n  - round: 14\n    reviewers:\n    - 1\n    note: \"R14: R1 [RESOLVED]。\"\n  resolution: \"§4.2 line 110 标注 'preliminary'。\"\n  resolution_round: 14\n- id: v6-R2-W2\n  summary: §4.3 的 β 值呈现顺序非升序\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 10\n  resolution: 已按升序呈现。\n  resolution_round: 10\n- id: v6-R2-W6-LOO\n  summary: LOO 缩写未在首次使用时正式定义\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 6\n  last_seen_round: 7\n  resolution: introduction.tex 现有完整定义。\n  resolution_round: 7\n- id: v6-R2-W8\n  summary: Hacking taxonomy 分类标准不够 principled\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 6\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers:\n    - 1\n    note: 仅 H1/H7 有 precision 验证。\n  - round: 12\n    reviewers:\n    - 1\n    - 2\n    note: \"R1-W4 + R2-W3: robust vs isolated 应在 Abstract 区分。R12 fix: Abstract 改为 'three robust modes (H1/H7/H8) + additional isolated observations'（commit 9dc8835）。\"\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: \"R1: H8 只在 s42 完成审计，'validated across multiple seeds' 对 H8 是否准确？R2: taxonomy 有独立工具价值但仅 H1/H7 有 precision 验证。\"\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: CE/TS/PG/CI 重命名改善可读性。CE/TS precision >95% 验证。PG claim 降为 'observed at lower prevalence'。分类标准仍为规则+功能分析混合。\"\n- id: v7-R1-N2\n  summary: CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: CMH 移至 Appendix，正文以 seed-level permutation p=0.26 为 primary。\n  resolution_round: 9\n- id: v7-R2-MR1\n  summary: 缺少 Goodhart's Law 经典引用\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 8\n  resolution: references.bib 包含 Goodhart 1975。\n  resolution_round: 8\n- id: v7-R2-W7\n  summary: \"experiments.tex 'Notably' AI 写作标记\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: \"'Notably' 已移除。\"\n  resolution_round: 9\n- id: v8-R12-N1\n  summary: Goodhart 发现的可预测性限制概念新颖性\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 8\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers:\n    - 1\n    - 2\n    note: R2-N2 [critical]。\n  - round: 12\n    reviewers:\n    - 1\n    - 2\n    note: R1 Excitement 3/5 认为 empirical details 超出可预测范围，R2 2.5/5。两人均同意 Findings。结构性问题。\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: \"R2-N1 [critical]: H7 的 ISR≥0.5 是数学必然，不需实验确认。R1 部分同意但认为 dynamics 细节有价值。结构性问题：核心发现的可预测性是概念层面的限制，无法通过写作修改解决。\"\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: Gated ISR 实验增量改善 (诊断→诊断+mitigation attempt)。TS→PG mode migration 是非平凡发现。但核心 novelty concern (LOO 标准+Goodhart 可预测) 仍为结构性限制。R1 3.5 vs R2 3.0，分歧在 empirical rigor vs conceptual novelty 权重。\"\n- id: v8-R1-N3\n  summary: 术语交替使用导致语义滑移\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers:\n    - 2\n    note: \"Fig 2/3 'Genuine' → 'Non-hacking' 已修复。偶见残留。\"\n  - round: 12\n    reviewers: []\n    note: R12 未再提及术语滑移。\n  - round: 13\n    reviewers: []\n    note: R13 未再提及术语滑移。可能已修复，待确认。\n  - round: 14\n    reviewers:\n    - 2\n    note: \"R14: R2 [RESOLVED]。Grep 确认无 H1/H7/H8/H9 残留。\"\n  resolution: H1→CE, H7→TS, H8→PG, H9→CI 全文重命名完整一致。无残留旧名称。\n  resolution_round: 14\n- id: v8-R12-N2\n  summary: 实验范围与标题/claim scope 不匹配\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers:\n    - 1\n    - 2\n    note: \"Subtitle 改为 'GRPO-Trained FOL Reasoners'。\"\n  - round: 12\n    reviewers:\n    - 1\n    - 2\n    note: \"R2-N3 [critical]: 仍暗示通用结论。R12 fix: C3 弱化为 'evidence of generality'，Contributions 加 'from a single model family and dataset'（commit 9dc8835）。\"\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: \"R2-W1: C3 仍在同一 dataset 和 model family 内。Discussion line 11 'STA applies to any compositional-input/binary-verifier setting' 缺乏验证。两人一致认为泛化性 claim 仍需进一步 hedge。\"\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: R1 [RESOLVED]。Hedging 充分。\"\n  resolution: \"C3 加 'in principle...preliminary'。Discussion 加 'should in principle transfer'。§4.3 显式声明无 Prolog random control。\"\n  resolution_round: 14\n- id: v8-R1-W4\n  summary: 多重比较未校正\n  category: experiment\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers:\n    - 1\n    note: \"limitations.tex 新增 'Multiple comparisons' 段落。\"\n  - round: 12\n    reviewers: []\n    note: R12 未再单独提及。\n  - round: 13\n    reviewers:\n    - 1\n    note: \"R1-W3: CMH independence violation 仍需更清晰标注为 'directional only'。R2 AGREE。\"\n  - round: 14\n    reviewers:\n    - 1\n    note: \"R14: R1 [RESOLVED]。\"\n  resolution: \"Appendix line 126 标注 CMH 'p-values are consequently inflated'。功能等价于 'directional only'。\"\n  resolution_round: 14\n- id: v8-R1-MR\n  summary: 缺少 reward shaping 和 inference-time hacking 引用\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 10\n  resolution: Uesato 2022, Paulus 2018, Langosco 2022 等已补充。\n  resolution_round: 10\n- id: v9-R1-N3\n  summary: Premise-count confound 影响范围分歧\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: method.tex 增加 confound 两场景区分句。\n  resolution_round: 9\n- id: v9-R12-W1\n  summary: §4.4 标题措辞过强\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"§4.4 标题改为 'Cross-Logic Extension'。\"\n  resolution_round: 9\n- id: v9-R1-W5\n  summary: 训练时 sampling vs 评估时 greedy 不一致\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: §4.1 已增加讨论。\n  resolution_round: 9\n- id: v9-R12-Q-ISR-FILTER\n  summary: ISR 作为 filter 未测试\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 10\n  resolution: \"conclusion.tex 增加 'ISR as post-hoc filter' 作为 future work。\"\n  resolution_round: 9\n- id: v9-R12-Q-NORMALIZED-ISR\n  summary: 未测试 premise-count-normalized ISR\n  category: method\n  severity: info\n  status: resolved\n  first_raised_round: 9\n  last_seen_round: 9\n  resolution: \"conclusion.tex 增加 'normalized variants' 作为 future work。\"\n  resolution_round: 9\n- id: v4-RV-STALE-APPENDIX\n  summary: Appendix Table 仍用旧数据\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 4\n  last_seen_round: 7\n  resolution: Appendix Table 5 现含完整 per-seed data。\n  resolution_round: 7\n- id: v10-R12-N1\n  summary: §4.5 与 Limitations 关于 1.7B seed 数量矛盾\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  resolution: D129 完整 3-seed 数据重写 §4.5。\n  resolution_round: 11\n- id: v10-R2-Q6\n  summary: ISR=0.75 推导与实测不一致\n  category: method\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 11\n  resolution: 改为 ISR≥0.5。PDF 已重编译。\n  resolution_round: 11\n- id: v10-R2-W7\n  summary: \"'Valid but Vacuous' 中 'valid' 有歧义\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers:\n    - 2\n    note: \"建议改为 'Verified but Vacuous'。保留原标题决策。\"\n  - round: 12\n    reviewers: []\n    note: Round 12 未再提及。\n  - round: 13\n    reviewers: []\n    note: Round 13 未再提及。可能不再是活跃问题。\n  - round: 14\n    reviewers: []\n    note: \"R14: 未再提及。\"\n- id: v10-R2-W8\n  summary: Discussion/Conclusion 过于简短\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers:\n    - 1\n    - 2\n    note: Discussion 扩展到 ~33 行。\n  - round: 12\n    reviewers: []\n    note: R12 未批评长度。P0 压缩后约 11 行但内容更密集。\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: \"R2: Discussion 缺 forward-looking content（mitigation 方向）。R1 部分同意，建议增加 mitigation 困难性分析段落。\"\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: R2 [RESOLVED]。有实质 mitigation 内容。\"\n  resolution: Discussion 扩展至 14 行。含 gated ISR 实验 + reward ensembling + constrained optimization + TRACE 方向。\n  resolution_round: 14\n- id: v10-R2-W5\n  summary: C2 和 C4 边界不清晰\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 10\n  last_seen_round: 10\n  resolution: Contributions 合并为 3 条。\n  resolution_round: 10\n- id: v11-R12-N1\n  summary: Responsible NLP Research Checklist 缺失\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: checklist.tex 创建并附在论文末尾。\n  resolution_round: 11\n- id: v11-R1-W2\n  summary: Taxonomy 仅 H1/H7 有 precision 验证\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n  - round: 11\n    reviewers:\n    - 1\n    note: 其余 modes 缺独立验证。\n  - round: 12\n    reviewers:\n    - 1\n    - 2\n    note: \"R12 fix: Abstract 区分 robust vs isolated modes（commit 9dc8835）。\"\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: \"R1: H8 只在 s42 完成审计。R2: taxonomy 有独立工具价值。两人均认为 Abstract 的 'validated across multiple seeds' 对 H8 不准确。\"\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: R2 [RESOLVED]。Claim 适当下调。\"\n  resolution: \"Abstract 'PG, observed at lower prevalence'。Method 明确 CE/TS robust (≥3 seeds) vs PG low prevalence。\"\n  resolution_round: 14\n- id: v11-R1-W5\n  summary: O(1) binary ablation ISR*≈0.007 反直觉结果未充分解释\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 11\n  last_seen_round: 13\n  mentions:\n  - round: 12\n    reviewers: []\n    note: Round 12 未再提及。\n  - round: 13\n    reviewers: []\n    note: Round 13 未再提及。\n- id: v11-R2-MR\n  summary: 缺少 2025-2026 最新引用\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 14\n  mentions:\n  - round: 12\n    reviewers:\n    - 1\n    - 2\n    note: \"R12 fix: 已加入 STaR + Cobbe（commit 9dc8835）。Lean-based RL 如空间允许后续补。\"\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: R1 补 LEGO-Prover。R2 补 Llemma (Azerbayev 2024)。两人一致缺 reward hacking mitigation 文献。\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: R2 [RESOLVED]。引用覆盖完整。\"\n  resolution: 新增 Llemma、Coste 2024、Moskovitz 2024。Related Work + Discussion 均引用。\n  resolution_round: 14\n- id: v11-R12-PDF\n  summary: PDF 与 .tex 不一致\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: PDF 从 paper/ 重编译。\n  resolution_round: 11\n- id: v12-R2-N1\n  summary: 正文超出 ARR 8 页限制约 0.75 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: Table 2 移入 Appendix，Related Work/Discussion/Limitations 压缩。主文本完整收于第 8 页。\n  resolution_round: 12\n- id: v12-R2-W4\n  summary: Table 1 ISR β=0.1 ISR* 列缺失\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: Table 1 补 ISR*=0.63±.23，N-H 改用 corrected 3-seed 6%，footnote 说明。\n  resolution_round: 12\n- id: v12-R2-W2\n  summary: 与 Kim et al. (2026) 区分需更锐利\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 14\n  mentions:\n  - round: 12\n    reviewers:\n    - 2\n    note: Introduction 增加 explicit 对比句（training-time vs inference-time）。\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: \"R2-N2 [critical]: 仅一句对比不够，需逐条比较 gaming modes、detection methods、experimental settings。R1 同意需更多对比但降为 [major]。R1 建议: 共同点 + 差异 + 互补关系三段对比。\"\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: R2 [RESOLVED]。对比充分且有洞察。同 v13-R2-N2。\"\n  resolution: \"Related Work 新增完整 'Faithfulness in formalization' 段落，3 维度逐条对比 Kim et al.。\"\n  resolution_round: 14\n- id: v12-R1-W2\n  summary: Component-count confound deconfounding analysis 仅在 Appendix\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 12\n  last_seen_round: 13\n  mentions:\n  - round: 12\n    reviewers:\n    - 1\n    note: \"R1-W2。R2 [REBUT]: 核心 claim 基于 taxonomy 而非 raw ISR。分歧记录。\"\n  - round: 13\n    reviewers: []\n    note: Round 13 未直接提及此 item。但 R1-W1 关于 ISR≠semantic quality 隐含相关性。\n- id: v13-R2-N2\n  summary: 与 Kim et al. (2026) 差异化不充分：仅一句区分，缺逐条对比\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: \"R2-N2 [critical]。R1 [AGREE] 但建议降为 major（方法论层面不重叠）。分歧在 severity：R2 critical vs R1 major。建议: Related Work 增加专门对比段。\"\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: R2 [RESOLVED]。'充分且有深度'。\"\n  action_items:\n  - round: 13\n    action: \"Related Work 增加与 Kim et al. (2026) 的逐条对比：gaming modes 重叠、detection 方法差异、inference-time vs training-time\"\n    assigned_to: research_director\n    status: open\n  resolution: \"Related Work 新增完整 'Faithfulness in formalization' 段落：training vs inference、STA/ISR vs LLM-judge、universal gaming vs no-gaming、CE ≈ axiom-fabrication 互补性。\"\n  resolution_round: 14\n- id: v13-R1-W1\n  summary: \"ISR 与 NLI accuracy 无关 (ρ=-0.049) 但 'structural quality diagnostic' 定位可能误导\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: \"R1-W1 [major]。R2 [AGREE]。ISR 高不意味好推理（H7 也高），ISR 低不一定坏推理（Prolog redundancy）。'Structural integrity' ≠ 'reasoning quality'。Introduction/Abstract 的 framing 可能给读者过于正面的印象。\"\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: R2 [RESOLVED]。措辞精确。Abstract 仍用 'structural integrity' 但在上下文中可接受。\"\n  action_items:\n  - round: 13\n    action: \"更精确界定 ISR diagnostic 能力——是 component necessity 度量而非 reasoning quality 度量\"\n    assigned_to: research_director\n    status: open\n  resolution: \"Method §3.2 line 46: 'ISR is a component-necessity diagnostic, not a reasoning-quality metric'。全文 framing 校正。\"\n  resolution_round: 14\n- id: v13-R2-W4\n  summary: 缩写和术语密度过高（~17 个缩写需同时追踪）\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: R2-W4。R1 [AGREE]。建议减少 3-4 个缩写（如 S-NH 延迟引入，CI 直接写 content-independent）或加 notation summary。\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: ~18 缩写，未添加 notation summary。但 H1→CE 等描述性重命名显著改善可读性。R2 降为 minor。\"\n  action_items:\n  - round: 13\n    action: 减少缩写使用或添加 notation summary table\n    assigned_to: research_director\n    status: open\n  resolution: ''\n  resolution_round: null\n- id: v13-R2-W5\n  summary: Table 2 混合 single-seed 和 pooled 数据，对比不公平\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: R2-W5。R1 [AGREE]。Exec 列 = s42 only vs ISR/Rnd = 5-seed pooled。建议统一为 3-seed pooled 或增加 n(seeds) 列。\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: R2 [RESOLVED]。聚合方式标注清晰。\"\n  action_items:\n  - round: 13\n    action: 统一 Table 2 聚合方式或标注每列 seed 数\n    assigned_to: research_director\n    status: open\n  resolution: \"Table 2 caption 标注 '$^a$Single seed (s42); remaining columns pooled (ISR/Rnd 4B: 5-seed; Prolog/1.7B: 3-seed)'。\"\n  resolution_round: 14\n- id: v13-R2-MITIGATION\n  summary: Discussion 缺少 mitigation 策略讨论和 forward-looking analysis\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: \"R2 [major concern]: 论文只诊断不治疗。R1 部分同意，建议增加: (1) KL regularization 为何不足 (cite Kwa 2024), (2) reward ensembling 可能性, (3) component-count normalization 的 negative result (1.06×)。两人一致认为 Discussion 过于 hand-waving。\"\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: R2 [RESOLVED]。有实验支撑和文献对接。\"\n  action_items:\n  - round: 13\n    action: Discussion 增加 mitigation analysis 段落\n    assigned_to: research_director\n    status: open\n  resolution: \"Discussion lines 11-14: gated ISR 实验 (TS→PG migration) + reward ensembling (Coste 2024) + constrained optimization (Moskovitz 2024) + TRACE 方向。\"\n  resolution_round: 14\n- id: v13-R1-Q4\n  summary: Prolog cross-logic 实验缺少 random control\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 14\n  mentions:\n  - round: 13\n    reviewers:\n    - 1\n    - 2\n    note: R1-Q4。R2 [AGREE]。无法区分 ISR-specific Goodhart vs generic GRPO instability under augmented reward。\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"R14: R1 [RESOLVED]。限制明确承认。\"\n  action_items:\n  - round: 13\n    action: 至少讨论此限制，理想情况下补充 Prolog random/exec-only 数据\n    assigned_to: research_director\n    status: open\n  resolution: \"§4.3 line 118: 'No matched random control was run for Prolog' 显式声明。\"\n  resolution_round: 14\n- id: v14-R12-GATED-S54\n  summary: Gated ISR Discussion 遗漏 s54 反例 (96.7% non-hacking)\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 14\n    reviewers:\n    - 1\n    - 2\n    note: \"Discussion 只提 '2/3 seeds migrate to PG'，忽略 s54 (96.7% N-H)。两位 reviewer 一致认为有选择性呈现嫌疑。建议改为 '2/3 seeds migrate to PG, while 1/3 sustains predominantly non-hacking output (96.7%); outcome is highly seed-dependent with only 3 seeds.'\"\n  action_items:\n  - round: 14\n    action: Discussion 补充 s54 数据和 seed-dependence caveat\n    assigned_to: research_director\n    status: open\n  resolution: ''\n  resolution_round: null\n- id: v14-R1-LIMITATIONS\n  summary: Limitations section 压缩至 6-7 行，SFT n=39 限制未单独提及\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 14\n  last_seen_round: 14\n  mentions:\n  - round: 14\n    reviewers:\n    - 1\n    note: 8 页限制下可理解，但 Limitations 不再是 R13 评价的 '论文亮点'。关键内容散落在正文和 Appendix。\n  action_items: []\n  resolution: ''\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 1343 · 2026-05-19T10:24:13.881134+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml\", \"bytes\": 39315}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1344 · 2026-05-19T10:25:37.190060+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Round 14 Consolidated Review Report\n\n**Paper**: Valid but Vacuous: Reward Hacking in GRPO-Trained FOL Reasoners\n**Venue**: ACL ARR May 2026 → EMNLP 2026 (Long Paper)\n**Review Mode**: Continue (from Round 13)\n**Reviewers**: R1 (方法/实验严谨性), R2 (新颖性/完整性/写作)\n\n---\n\n## Summary\n\n论文提出 Solver Trace Ablation (STA) 和 Irreducible Solver Rate (ISR) 来检测 GRPO 训练的 FOL 推理器中的 reward hacking。R14 修订响应了 R13 提出的大部分问题：ISR framing 从 \"structural quality diagnostic\" 精确化为 \"component-necessity diagnostic\"；Kim et al. (2026) 对比从一句话扩展为完整的三维度分析段落；Discussion 增加了 gated ISR 实验（TS→PG mode migration）作为 mitigation 分析的实证支撑；hacking modes 从不透明编号 (H1/H7/H8/H9) 重命名为描述性缩写 (CE/TS/PG/CI)；Abstract 消除了 single-seed cherry-picking (改用 3-seed aggregate ISR*=0.03±0.05)。\n\n论文现已自我定位为 \"empirical case study\"，claims 普遍以 hedged 形式呈现。核心发现（所有测试 dose 下的 Goodhart collapse）有充分数据支撑，但概念新颖性（LOO 标准技术 + Goodhart 可预测性）仍是结构性限制。\n\n---\n\n## R13 Issue Resolution Status\n\n**19 issues resolved in R14** (of 26 R13 open/in_progress items evaluated):\n\n| Issue | Status | Resolution |\n|-------|--------|------------|\n| v13-R2-N2 (Kim et al. 对比) | ✅ RESOLVED | Related Work 新增 \"Faithfulness in formalization\" 段落，3 维度逐条对比 |\n| v13-R1-W1 (ISR framing) | ✅ RESOLVED | Method §3.2: \"ISR is a component-necessity diagnostic, not a reasoning-quality metric\" |\n| v13-R2-W5 (Table 2 聚合) | ✅ RESOLVED | Caption 标注 single-seed vs pooled |\n| v13-R2-MITIGATION (Discussion 缺 mitigation) | ✅ RESOLVED | Gated ISR 实验 + reward ensembling + constrained optimization |\n| v13-R1-Q4 (Prolog 无 random control) | ✅ RESOLVED | §4.3 显式声明限制 |\n| v5-R2-W1 (Abstract cherry-picking) | ✅ RESOLVED | 3-seed aggregate 替代 single-seed |\n| v4-R12-N2 (collapse claim 过强) | ✅ RESOLVED | \"four tested doses\" + \"preliminary\" |\n| v4-R12-W6 (s43 eval 协议) | ✅ RESOLVED | 脚注已添加 |\n| v4-R12-W7 (N-H upper bound) | ✅ RESOLVED | Table 1 caption + Method §3.5 标注 |\n| v4-R1-W8 (统计功效) | ✅ RESOLVED | Wilson CIs 完整呈现 |\n| v8-R12-N2 (scope mismatch) | ✅ RESOLVED | Hedging 充分 |\n| v8-R1-N3 (术语滑移) | ✅ RESOLVED | H1→CE 等全文重命名无残留 |\n| v5-R2-W3 (段落碎片化) | ✅ RESOLVED | 段落结构改善 |\n| v6-R1-W2 (dose-response 统计) | ✅ RESOLVED | \"preliminary\" 标注 |\n| v8-R1-W4 (多重比较) | ✅ RESOLVED | CMH 标注 \"inflated\" |\n| v5-R1-N3 (Table 1 不对称) | ✅ RESOLVED | 标注清晰 |\n| v10-R2-W8 (Discussion 过短) | ✅ RESOLVED | 14 行含实质 mitigation 内容 |\n| v11-R1-W2 (taxonomy 验证) | ✅ RESOLVED | PG 降为 \"lower prevalence\" |\n| v5-R2-MR / v11-R2-MR (引用) | ✅ RESOLVED | Llemma + Coste + Moskovitz 补充 |\n\n**4 issues still open/actionable:**\n\n1. **v4-R12-N3** [in_progress, critical → major]: OR 方向反转 (ISR N-H 6.06% < Random 9.5%) 未在正文讨论。两位 reviewer 一致认为应增加 1-2 句。这实际上强化核心论点（ISR reward 不仅未改善非 hacking 质量，反而可能更差）。\n2. **v14-R12-GATED-S54** [open, warning]: Discussion 遗漏 s54 (96.7% non-hacking)，只报告 \"2/3 seeds migrate to PG\"。有选择性呈现嫌疑。建议补充完整 seed 分布。\n3. **v5-R12-SFT-PR** [in_progress, critical]: §4.2 line 42 仍用 \"RL-specific\" 旧措辞，与 Abstract/Introduction/Discussion 中 \"associated with RL optimization\" 的 hedged 表述不一致。一处遗漏的统一化修改。\n4. **v13-R2-W4** [open, info]: ~18 缩写，未添加 notation summary。描述性重命名 (CE/TS/PG/CI) 已显著改善可读性，降为 minor。\n\n**Structural issues (in_progress, cannot be resolved by revision):**\n- v8-R12-N1: 核心发现的可预测性限制概念新颖性\n- v4-R2-W9 / v5-R2-N3: LOO 是标准技术，方法新颖性有限\n- v6-R2-W8: Taxonomy 分类标准为规则+功能分析混合\n\n---\n\n## New Strengths (R14)\n\n- **S7 (Gated ISR Experiment)**: Component-count gate 实验 (Appendix §B.11) 将论文从纯诊断扩展为诊断+mitigation 尝试。TS→PG mode migration 的 \"blocking one Goodhart pathway redirects optimization pressure\" 是非平凡发现。\n- **S8 (Kim et al. Comparison)**: Related Work 的三维度对比（training vs inference, STA/ISR vs LLM-judge, universal gaming vs no-gaming + CE ≈ axiom-fabrication 互补性）质量高，展示了成熟的 positioning 能力。\n- **S9 (Descriptive Mode Names)**: CE/TS/PG/CI 替代 H1/H7/H8/H9，大幅改善可读性和学术标准。\n- **S10 (Mitigation Landscape)**: Discussion 现在有实质内容：gated ISR 实验数据 + reward ensembling (Coste 2024) + constrained optimization (Moskovitz 2024) + TRACE (Wang 2025)。\n\n---\n\n## Weaknesses\n\n### Structural (无法通过修订解决)\n\n**W-S1**: 核心概念新颖性有限。LOO 是标准消融技术，Goodhart collapse 在 proxy reward 设置下可预测。论文自我定位为 \"empirical case study\" 是诚实的，但这也意味着贡献以实证观察为主（seed-dependent dynamics, mode taxonomy, migration patterns），而非方法或理论突破。这决定了论文的 ceiling 在 Findings 到 Borderline Conference 之间。\n\n### Fixable (可通过修订解决)\n\n**W-F1** [warning]: OR 方向反转 (ISR N-H=6.06% < Random N-H=9.5%, corrected; matched cohort 同方向 2.3% vs 5.9%) 是论文最有力的证据之一，却未在正文任何位置讨论。ISR reward 不仅未改善非 hacking 质量，point estimate 实际更差。在 §4.3 或 Discussion 增加 1-2 句即可。\n\n**W-F2** [warning]: Gated ISR 实验在 Discussion 中只报告 \"2/3 seeds migrate to PG\"，遗漏 s54 (96.7% non-hacking)。这构成选择性呈现：3 个 seed 中 1 个未 migrate 但未被提及。修改建议：\"2/3 seeds migrate to PG, while 1/3 sustains predominantly non-hacking output (96.7%); the outcome is highly seed-dependent with only 3 seeds。\"\n\n**W-F3** [warning]: §4.2 line 42 仍用 \"RL-specific\" 旧措辞，与 Abstract/Introduction/Discussion 的 hedged 表述 (\"associated with RL optimization, though the large prove-rate gap prevents definitive causal attribution\") 不一致。遗漏的统一化修改，一处改动即可修复。\n\n**W-F4** [info]: Limitations section 从 R13 的 ~14 行压缩至 6-7 行。8 页限制下可理解，但不再是 R13 评价的 \"论文亮点\"。SFT n=39 限制未单独提及。关键限制讨论散落在正文各处和 Appendix。\n\n---\n\n## Questions for Authors\n\n1. ISR N-H=6.06% < Random N-H=9.5% 的方向反转是否有意未在正文讨论？若有意，理由是什么？\n2. Gated ISR 的 s54 (96.7% non-hacking, 3.3% PG) 为何未在 Discussion 中与 s52/s53 一并报告？\n3. §4.2 line 42 的 \"RL-specific\" 是否为修改遗漏？\n\n---\n\n## Missing References\n\n无新增缺失引用。引用覆盖充足。\n\n---\n\n## Cross-Reviewer Consensus\n\n| Topic | R1 | R2 | Consensus |\n|-------|----|----|-----------|\n| OR 反转需正文讨论 | AGREE | AGREE | ✅ 一致 |\n| s54 遗漏需补充 | AGREE | AGREE | ✅ 一致 |\n| §4.2 \"RL-specific\" 遗漏 | AGREE | AGREE | ✅ 一致 |\n| Gated ISR 是有价值增量 | AGREE | AGREE | ✅ 一致 |\n| Kim et al. 对比质量 | AGREE (充分) | AGREE (充分且有深度) | ✅ 一致 |\n| ISR framing 校正 | RESOLVED | RESOLVED | ✅ 一致 |\n| Mode 重命名改善 | AGREE | AGREE | ✅ 一致 |\n| Abstract cherry-picking 消除 | RESOLVED | RESOLVED | ✅ 一致 |\n| 概念新颖性结构性限制 | Partially (empirical rigor 有价值) | Yes (LOO+Goodhart 可预测) | ⚠️ 分歧在权重 |\n| Overall 评分 | 3.5 | 3.0 | ⚠️ 半分分歧 |\n\n**分歧分析**: R1 (3.5) 认为 empirical rigor（matched cohort design、gated ISR、taxonomy precision）有独立价值，接近 Borderline Conference。R2 (3.0) 认为 LOO+Goodhart 的可预测性限制了 excitement，尽管承认 gated ISR 的 mode migration 是非平凡发现（将 novelty 从 2.5 上调至 3.0）。这是合理的价值判断分歧，非事实性矛盾。\n\n---\n\n## Overall Assessment\n\n**Score: 3.0 (Findings)**\n**Range: 3.0 - 3.5**\n**Confidence: 4/5**\n\nR14 修订质量高：19 项 R13 问题得到解决，新增的 gated ISR 实验和 Kim et al. 三维度对比是实质性改进。论文在可修改的范围内已接近最优状态。\n\n剩余可修的问题（OR 反转讨论、s54 补充、§4.2 措辞统一）均为 1-2 句改动，不影响整体评价。\n\n评分锚定为 3.0 (Findings) 的核心原因是结构性的：(1) LOO 是标准消融技术，不构成方法贡献；(2) Goodhart collapse 在 proxy reward 设置下概念上可预测，empirical details（hacking mode taxonomy, migration patterns）有增量价值但不构成 Conference 级别的 novelty threshold；(3) 实验范围限于单模型/单数据集/单算法。论文诚实地自我定位为 \"empirical case study\"，Findings 是恰当的归宿。\n\n如果 R15 修复 W-F1 至 W-F3，评分不会实质改变（仍为 3.0-3.5 区间），因为限制因素是结构性的。\n\n---\n\n## Issue Tracker Summary (R14)\n\nTotal: 97 issues across 15 rounds\n- Resolved: 83 (85.6%)\n- In Progress: 8 (8.2%, 含 4 个结构性问题)\n- Open: 5 (5.2%, 含 2 个 dormant + 3 个 actionable)\n- Won't Fix: 1 (1.0%)",
  "project": "solver-trace-ablation",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 (Findings)",
  "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Round 14 Consolidated Review Report\n\n**Paper**: Valid but Vacuous: Reward Hacking in GRPO-Trained FOL Reasoners\n**Venue**: ACL ARR May 2026 → EMNLP 2026 (Long Paper)\n**Review Mode**: Continue (from Round 13)\n**Reviewers**: R1 (方法/实验严谨性), R2 (新颖性/完整性/写作)\n\n---\n\n## Summary\n\n论文提出 Solver Trace Ablation (STA) 和 Irreducible Solver Rate (ISR) 来检测 GRPO 训练的 FOL 推理器中的 reward hacking。R14 修订响应了 R13 提出的大部分问题：ISR framing 从 \"structural quality diagnostic\" 精确化为 \"component-necessity diagnostic\"；Kim et al. (2026) 对比从一句话扩展为完整的三维度分析段落；Discussion 增加了 gated ISR 实验（TS→PG mode migration）作为 mitigation 分析的实证支撑；hacking modes 从不透明编号 (H1/H7/H8/H9) 重命名为描述性缩写 (CE/TS/PG/CI)；Abstract 消除了 single-seed cherry-picking (改用 3-seed aggregate ISR*=0.03±0.05)。\n\n论文现已自我定位为 \"empirical case study\"，claims 普遍以 hedged 形式呈现。核心发现（所有测试 dose 下的 Goodhart collapse）有充分数据支撑，但概念新颖性（LOO 标准技术 + Goodhart 可预测性）仍是结构性限制。\n\n---\n\n## R13 Issue Resolution Status\n\n**19 issues resolved in R14** (of 26 R13 open/in_progress items evaluated):\n\n| Issue | Status | Resolution |\n|-------|--------|------------|\n| v13-R2-N2 (Kim et al. 对比) | ✅ RESOLVED | Related Work 新增 \"Faithfulness in formalization\" 段落，3 维度逐条对比 |\n| v13-R1-W1 (ISR framing) | ✅ RESOLVED | Method §3.2: \"ISR is a component-necessity diagnostic, not a reasoning-quality metric\" |\n| v13-R2-W5 (Table 2 聚合) | ✅ RESOLVED | Caption 标注 single-seed vs pooled |\n| v13-R2-MITIGATION (Discussion 缺 mitigation) | ✅ RESOLVED | Gated ISR 实验 + reward ensembling + constrained optimization |\n| v13-R1-Q4 (Prolog 无 random control) | ✅ RESOLVED | §4.3 显式声明限制 |\n| v5-R2-W1 (Abstract cherry-picking) | ✅ RESOLVED | 3-seed aggregate 替代 single-seed |\n| v4-R12-N2 (collapse claim 过强) | ✅ RESOLVED | \"four tested doses\" + \"preliminary\" |\n| v4-R12-W6 (s43 eval 协议) | ✅ RESOLVED | 脚注已添加 |\n| v4-R12-W7 (N-H upper bound) | ✅ RESOLVED | Table 1 caption + Method §3.5 标注 |\n| v4-R1-W8 (统计功效) | ✅ RESOLVED | Wilson CIs 完整呈现 |\n| v8-R12-N2 (scope mismatch) | ✅ RESOLVED | Hedging 充分 |\n| v8-R1-N3 (术语滑移) | ✅ RESOLVED | H1→CE 等全文重命名无残留 |\n| v5-R2-W3 (段落碎片化) | ✅ RESOLVED | 段落结构改善 |\n| v6-R1-W2 (dose-response 统计) | ✅ RESOLVED | \"preliminary\" 标注 |\n| v8-R1-W4 (多重比较) | ✅ RESOLVED | CMH 标注 \"inflated\" |\n| v5-R1-N3 (Table 1 不对称) | ✅ RESOLVED | 标注清晰 |\n| v10-R2-W8 (Discussion 过短) | ✅ RESOLVED | 14 行含实质 mitigation 内容 |\n| v11-R1-W2 (taxonomy 验证) | ✅ RESOLVED | PG 降为 \"lower prevalence\" |\n| v5-R2-MR / v11-R2-MR (引用) | ✅ RESOLVED | Llemma + Coste + Moskovitz 补充 |\n\n**4 issues still open/actionable:**\n\n1. **v4-R12-N3** [in_progress, critical → major]: OR 方向反转 (ISR N-H 6.06% < Random 9.5%) 未在正文讨论。两位 reviewer 一致认为应增加 1-2 句。这实际上强化核心论点（ISR reward 不仅未改善非 hacking 质量，反而可能更差）。\n2. **v14-R12-GATED-S54** [open, warning]: Discussion 遗漏 s54 (96.7% non-hacking)，只报告 \"2/3 seeds migrate to PG\"。有选择性呈现嫌疑。建议补充完整 seed 分布。\n3. **v5-R12-SFT-PR** [in_progress, critical]: §4.2 line 42 仍用 \"RL-specific\" 旧措辞，与 Abstract/Introduction/Discussion 中 \"associated with RL optimization\" 的 hedged 表述不一致。一处遗漏的统一化修改。\n4. **v13-R2-W4** [open, info]: ~18 缩写，未添加 notation summary。描述性重命名 (CE/TS/PG/CI) 已显著改善可读性，降为 minor。\n\n**Structural issues (in_progress, cannot be resolved by revision):**\n- v8-R12-N1: 核心发现的可预测性限制概念新颖性\n- v4-R2-W9 / v5-R2-N3: LOO 是标准技术，方法新颖性有限\n- v6-R2-W8: Taxonomy 分类标准为规则+功能分析混合\n\n---\n\n## New Strengths (R14)\n\n- **S7 (Gated ISR Experiment)**: Component-count gate 实验 (Appendix §B.11) 将论文从纯诊断扩展为诊断+mitigation 尝试。TS→PG mode migration 的 \"blocking one Goodhart pathway redirects optimization pressure\" 是非平凡发现。\n- **S8 (Kim et al. Comparison)**: Related Work 的三维度对比（training vs inference, STA/ISR vs LLM-judge, universal gaming vs no-gaming + CE ≈ axiom-fabrication 互补性）质量高，展示了成熟的 positioning 能力。\n- **S9 (Descriptive Mode Names)**: CE/TS/PG/CI 替代 H1/H7/H8/H9，大幅改善可读性和学术标准。\n- **S10 (Mitigation Landscape)**: Discussion 现在有实质内容：gated ISR 实验数据 + reward ensembling (Coste 2024) + constrained optimization (Moskovitz 2024) + TRACE (Wang 2025)。\n\n---\n\n## Weaknesses\n\n### Structural (无法通过修订解决)\n\n**W-S1**: 核心概念新颖性有限。LOO 是标准消融技术，Goodhart collapse 在 proxy reward 设置下可预测。论文自我定位为 \"empirical case study\" 是诚实的，但这也意味着贡献以实证观察为主（seed-dependent dynamics, mode taxonomy, migration patterns），而非方法或理论突破。这决定了论文的 ceiling 在 Findings 到 Borderline Conference 之间。\n\n### Fixable (可通过修订解决)\n\n**W-F1** [warning]: OR 方向反转 (ISR N-H=6.06% < Random N-H=9.5%, corrected; matched cohort 同方向 2.3% vs 5.9%) 是论文最有力的证据之一，却未在正文任何位置讨论。ISR reward 不仅未改善非 hacking 质量，point estimate 实际更差。在 §4.3 或 Discussion 增加 1-2 句即可。\n\n**W-F2** [warning]: Gated ISR 实验在 Discussion 中只报告 \"2/3 seeds migrate to PG\"，遗漏 s54 (96.7% non-hacking)。这构成选择性呈现：3 个 seed 中 1 个未 migrate 但未被提及。修改建议：\"2/3 seeds migrate to PG, while 1/3 sustains predominantly non-hacking output (96.7%); the outcome is highly seed-dependent with only 3 seeds。\"\n\n**W-F3** [warning]: §4.2 line 42 仍用 \"RL-specific\" 旧措辞，与 Abstract/Introduction/Discussion 的 hedged 表述 (\"associated with RL optimization, though the large prove-rate gap prevents definitive causal attribution\") 不一致。遗漏的统一化修改，一处改动即可修复。\n\n**W-F4** [info]: Limitations section 从 R13 的 ~14 行压缩至 6-7 行。8 页限制下可理解，但不再是 R13 评价的 \"论文亮点\"。SFT n=39 限制未单独提及。关键限制讨论散落在正文各处和 Appendix。\n\n---\n\n## Questions for Authors\n\n1. ISR N-H=6.06% < Random N-H=9.5% 的方向反转是否有意未在正文讨论？若有意，理由是什么？\n2. Gated ISR 的 s54 (96.7% non-hacking, 3.3% PG) 为何未在 Discussion 中与 s52/s53 一并报告？\n3. §4.2 line 42 的 \"RL-specific\" 是否为修改遗漏？\n\n---\n\n## Missing References\n\n无新增缺失引用。引用覆盖充足。\n\n---\n\n## Cross-Reviewer Consensus\n\n| Topic | R1 | R2 | Consensus |\n|-------|----|----|-----------|\n| OR 反转需正文讨论 | AGREE | AGREE | ✅ 一致 |\n| s54 遗漏需补充 | AGREE | AGREE | ✅ 一致 |\n| §4.2 \"RL-specific\" 遗漏 | AGREE | AGREE | ✅ 一致 |\n| Gated ISR 是有价值增量 | AGREE | AGREE | ✅ 一致 |\n| Kim et al. 对比质量 | AGREE (充分) | AGREE (充分且有深度) | ✅ 一致 |\n| ISR framing 校正 | RESOLVED | RESOLVED | ✅ 一致 |\n| Mode 重命名改善 | AGREE | AGREE | ✅ 一致 |\n| Abstract cherry-picking 消除 | RESOLVED | RESOLVED | ✅ 一致 |\n| 概念新颖性结构性限制 | Partially (empirical rigor 有价值) | Yes (LOO+Goodhart 可预测) | ⚠️ 分歧在权重 |\n| Overall 评分 | 3.5 | 3.0 | ⚠️ 半分分歧 |\n\n**分歧分析**: R1 (3.5) 认为 empirical rigor（matched cohort design、gated ISR、taxonomy precision）有独立价值，接近 Borderline Conference。R2 (3.0) 认为 LOO+Goodhart 的可预测性限制了 excitement，尽管承认 gated ISR 的 mode migration 是非平凡发现（将 novelty 从 2.5 上调至 3.0）。这是合理的价值判断分歧，非事实性矛盾。\n\n---\n\n## Overall Assessment\n\n**Score: 3.0 (Findings)**\n**Range: 3.0 - 3.5**\n**Confidence: 4/5**\n\nR14 修订质量高：19 项 R13 问题得到解决，新增的 gated ISR 实验和 Kim et al. 三维度对比是实质性改进。论文在可修改的范围内已接近最优状态。\n\n剩余可修的问题（OR 反转讨论、s54 补充、§4.2 措辞统一）均为 1-2 句改动，不影响整体评价。\n\n评分锚定为 3.0 (Findings) 的核心原因是结构性的：(1) LOO 是标准消融技术，不构成方法贡献；(2) Goodhart collapse 在 proxy reward 设置下概念上可预测，empirical details（hacking mode taxonomy, migration patterns）有增量价值但不构成 Conference 级别的 novelty threshold；(3) 实验范围限于单模型/单数据集/单算法。论文诚实地自我定位为 \"empirical case study\"，Findings 是恰当的归宿。\n\n如果 R15 修复 W-F1 至 W-F3，评分不会实质改变（仍为 3.0-3.5 区间），因为限制因素是结构性的。\n\n---\n\n## Issue Tracker Summary (R14)\n\nTotal: 97 issues across 15 rounds\n- Resolved: 83 (85.6%)\n- In Progress: 8 (8.2%, 含 4 个结构性问题)\n- Open: 5 (5.2%, 含 2 个 dormant + 3 个 actionable)\n- Won't Fix: 1 (1.0%)",
    "project": "solver-trace-ablation",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 (Findings)",
    "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
  }
}
```

</details>

---


### Tool result

_source line 1345 · 2026-05-19T10:25:41.309582+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_a771c2a33d631dd40256ecd5c3a6648e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4119
}
```

</details>

---


### Assistant

_source line 1346 · 2026-05-19T10:25:48.397683+00:00_

Round 14 审稿完成。

- **Issue Tracker** 已更新至 `review_issues.yaml`（97 issues, 83 resolved / 8 in_progress / 5 open / 1 wont_fix）
- **审稿报告** 已投递至 Research Director，Overall **3.0 (Findings)**，R1 3.5 / R2 3.0
- 本轮解决 19 项 R13 问题，新增 2 项（s54 遗漏、Limitations 压缩）
- 3 个可快速修复的 actionable items：OR 反转未讨论、s54 选择性呈现、§4.2 措辞遗漏
- 评分瓶颈为结构性问题（LOO 标准技术 + Goodhart 可预测性），非写作可解决

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 114

## Round 114

2 recorded events


### User

_source line 1347 · 2026-05-19T10:25:49.587950+00:00_

[Reviewer 1 审稿意见]:
## R1 交叉回应 — R2 Round 14 意见

---

### 分歧点 1: Overall 评分 (R1: 3.5 vs R2: 3.0)

**[PARTIALLY AGREE] — 我从 3.5 下调至 3.25（概念上），但维持 3.5 作为离散评分。**

R2 的核心论点是"LOO 标准 + Goodhart 可预测"构成结构性 novelty 上限，这一判断我部分认同。LOO 本身确实不新（§2 line 12 作者自己也承认），Goodhart collapse 对 proxy reward 理论上可预测。

但我认为 R2 低估了以下两点的叠加贡献：
1. **Empirical characterization 的密度**：8+1 hacking modes 的自动分类体系、matched 5+5 cohort design、cross-logic transfer（FOL→Prolog 三种不同 collapse 机制），这些不是 trivial replication，而是对一个 under-documented 现象的系统刻画。ACL ARR Findings 门槛要求的是 "solid work that merits publication"，这篇论文的实验覆盖度超过多数 Findings 论文。
2. **Gated ISR 的 whac-a-mole 发现**：TS→PG 迁移不仅是 novelty +0.5 的增量，它提供了一个具体的、可验证的反例，说明 patch-one-exploit 策略在 solver-backed RL 中系统性失败。这对该领域的实践者有直接指导价值。

R2 认为这些不足以跨越 Findings→Conference 门槛。我的判断是：论文处于 borderline 位置（3.5），gated ISR 实验将其从 "solid Findings" 推向 "borderline Conference"。如果 gated ISR 有 5+ seeds 且补充了 gated random control，我会毫不犹豫给 4.0。当前 3 seeds 的限制使我无法再高。

**结论：维持 3.5 (Borderline Conference)，但承认与 3.0 的分歧是合理的 judgment call。**

---

### 分歧点 2: Gated ISR 对 novelty 的贡献

**[AGREE with nuance]**

R2 给 novelty +0.5（2.5→3.0）是合理的。我同意 3 seeds 不足以支撑独立 claim。

具体评估：
- **Table 16 (Appendix G.4)**: s52 100% PG（ISR*=1.0）、s53 89.6% PG、s54 96.7% N-H。三个 seed 产生了三种截然不同的结果，这本身就说明 3 seeds 统计力不足。
- **s54 的反例**：96.7% N-H 意味着 gated ISR 在该 seed 上实际"成功"了。Discussion（conclusion.tex line 11）只报告了 "2/3 seeds migrate to PG"，未提及 s54 是接近成功的反例。这降低了 claim 的精确度。
- **缺少 gated random control**：无法区分 PG 迁移是 gated ISR 特异性的还是 generic reward variance 效应。主实验（§4.2）专门设计了 random control 来解决这个问题，gated 实验理应同等对待。

**结论：Gated ISR 作为 Discussion 中的 preliminary evidence 合理，但作者应在 appendix 中明确标注 "preliminary (3 seeds, no matched control)"，并在 Discussion 中提及 s54 反例。**

---

### 分歧点 3: R2 NEW-1 (§4.2 "RL-specific")

**[AGREE] — 与我的 R14 Issue 1 完全一致。**

§4.1 line 42: "consistent with hacking being RL-specific" 与论文其他位置（Introduction line 14, Discussion line 6）使用的 "associated with RL optimization rather than data exposure, though the large prove-rate gap prevents definitive causal attribution" 措辞不一致。

这是一个 trivial fix（替换一个短语），但不一致性会给审稿人留下作者 overclaiming 的印象。R2 和我都独立发现了同一问题，说明这不是吹毛求疵——真实审稿人也会注意到。

**建议：将 line 42 改为 "consistent with hacking being associated with RL optimization" 并添加相同的 hedge。**

---

### 分歧点 4: 缩写密度

**[AGREE with R2's downgrade to minor]**

R2 将此从 warning 降级为 minor 是合理的。Round 13 的重命名（H1→CE, H7→TS, H8→PG, H9→CI）显著改善了可读性——CE/TS/PG/CI 比 H1/H7/H8/H9 直觉得多，读者无需不断回查定义。

论文确实仍有约 18 个缩写（STA, ISR, ISR*, GRPO, PR, CE, TS, TS-a, TS-b, PG, CI, N-H, S-NH, LOO, FOL, SFT, NLI, CMH），但这对一篇方法+实验密集的论文来说处于可接受范围。关键缩写（STA, ISR, CE, TS, PG）都有清晰的全称定义且首次使用时展开。

**结论：同意 minor，不影响接收决定。**

---

### 分歧点 5: Limitations 压缩

**[PARTIALLY AGREE]**

当前 limitations.tex 仅 3 句话（7 行），确实偏短。但需要区分两个问题：

1. **内容是否充分**：关键限制（单模型族、单数据集、ISR 非语义指标、100-example eval set、统计力有限）都已覆盖。且多项限制已被重新分配到正文中更自然的位置（如 ISR 的 component-count confound 在 §3.2，SFT PR confound 在 §4.1）。
2. **篇幅是否符合 venue 期望**：ACL ARR review form 要求 "adequate discussion of limitations"。3 句话可能让审稿人觉得不够重视。

我的建议是保持当前内容不变，但补充 1-2 句关于 gated ISR 实验局限性的内容（3 seeds、无 random control），这既回应了 R2 关于 gated ISR preliminary 的关切，又自然扩展了 Limitations 篇幅。

**结论：建议扩展 1-2 句，但 severity 为 minor，不影响评分。**

---

### R2 RESOLVED/PARTIALLY RESOLVED 项确认

对 R2 标记为 RESOLVED 的 9 项，我逐一确认均与我的 R14 评估一致，无分歧。

对 R2 标记为 PARTIALLY RESOLVED 的 3 项：
- **方法新颖性 (v4-R2-W9)**: 同意"结构性"判断——LOO 标准性是论文固有属性，无法通过修改解决。
- **概念新颖性 (v5-R2-N3)**: 同意 gated ISR 加分但不足以完全解决。
- **段落碎片化 (v5-R2-W3)**: 未在本轮重新检查，但 R13 修改后我未发现明显碎片化问题。

---

## 综合评分对照

| 维度 | R1 (R14) | R2 (R14) | 分歧 |
|------|----------|----------|------|
| Soundness | 3.5 | 3.5 | 无 |
| Novelty | — | 3.0 | R1 未单独评 novelty，隐含判断约 3.0-3.5 |
| Excitement | 3.0 | 3.0 | 无 |
| **Overall** | **3.5** | **3.0** | **核心分歧：novelty 是否构成 Conference 门槛障碍** |

**分歧根源**：R2 更重视 novelty ceiling（LOO 标准 + Goodhart 可预测），我更重视 empirical contribution density + practical value。这是 legitimate disagreement，取决于审稿人对 "empirical case study" 类论文的 venue 适配判断。

我认为 ACL 2025 Findings 中有大量 novelty 类似但 empirical coverage 不如本文的论文被接收。3.5 (Borderline Conference) 是我能给的最高分，但不会低于 3.5——这篇论文的实验系统性超过了 Findings 的典型水准。

---

[Reviewer 1 审稿结果]:
交叉回应已提交。5 个分歧点的结论：

1. **Overall 3.5 vs 3.0** — 维持 3.5，承认分歧是合理的 judgment call，核心在于对 empirical case study 类论文的 venue 适配判断不同
2. **Gated ISR novelty** — 同意 3 seeds 不足以支撑独立 claim，建议标注 preliminary 并提及 s54 反例
3. **§4.2 "RL-specific"** — 完全一致，trivial fix
4. **缩写密度** — 同意降为 minor
5. **Limitations 压缩** — 建议补充 1-2 句 gated ISR 局限性，minor severity

---

[Reviewer 2 审稿结果]:
所有已分配的审稿任务已完成并提交：

1. **Round 1 完整审稿** — 已提交（Overall 3.0）
2. **Round 1 交叉回应 R1** — 已提交
3. **Round 14 修订评估** — 已提交（Overall 维持 3.0，14项中9项 RESOLVED）
4. **Round 14 交叉回应 R1** — 已提交，与 R1 在4项可操作修改上达成共识

等待 Review Director 下一步指示。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1348 · 2026-05-19T10:26:00.242108+00:00_

Round 14 圆桌审稿已完成。两位 Reviewer 交叉回应后在所有技术问题上达成共识，唯一分歧为 Overall 评分（R1: 3.5 vs R2: 3.0），属于合理的价值判断差异。

Issue Tracker 和审稿报告均已提交。报告核心结论：

- **Overall: 3.0 (Findings)**，区间 3.0-3.5
- R14 解决了 19 项 R13 问题，剩余 3 项可操作修改（OR 反转讨论、s54 补充、§4.2 措辞统一）均为 1-2 句改动
- 评分上限由结构性因素决定（LOO 标准技术 + Goodhart 可预测性 + 单模型/单数据集），无法通过修订改变

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 115

## Round 115

60 recorded events


### User

_source line 1349 · 2026-05-20T04:13:25.163170+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: solver-trace-ablation
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR
- 截止日期: 2026-05-25

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 1350 · 2026-05-20T04:13:30.998237+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 1351 · 2026-05-20T04:13:31.049244+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 1352 · 2026-05-20T04:13:38.613860+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 1353 · 2026-05-20T04:13:38.714565+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1354 · 2026-05-20T04:13:41.403786+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool call

_source line 1355 · 2026-05-20T04:13:41.956236+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__read_project_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__read_project_file",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 1356 · 2026-05-20T04:13:42.058133+00:00_

{"result":"# 项目 solver-trace-ablation 概况\n\n## 实验状态 (191 个)\n\n- **plan013-random-reward-s42**: DONE (failed) — \n- **plan001-exec-only-s43**: DONE (failed) — \n- **plan003-eval-exec-only-r5**: DONE (success) — \n- **plan001-exec-only-s42-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r5**: DONE (negative) — \n- **sta-phase1-exec-only-r5**: DONE (success) — \n- **sta-phase1-exec-sta-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r2**: DONE (failed) — \n- **sta-phase1-exec-only-r2**: DONE (failed) — \n- **sta-phase1-exec-sta**: DONE (failed) — \n- **sta-phase1-exec-only**: DONE (failed) — \n- **sta-phase0-baseline**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- d146-pf-pipeline（准备中）\n- d144-llama-isr-s43: D144 cross-model: ISR β=0.1 GRPO on LLaMA-3.2-3B/FOLIO seed=43. Replication of ISR s42 for statistical power.（准备中）\n- d144-llama-isr-s44: D144 cross-model: ISR β=0.1 GRPO on LLaMA-3.2-3B/FOLIO seed=44. Replication of ISR s42 for statistical power.（准备中）\n- d144-llama-isr-s42: D144 cross-model: ISR β=0.1 GRPO on LLaMA-3.2-3B/FOLIO seed=42. Tests whether ISR triggers same Goodhart collapse pattern as Qwen3-4B.（准备中）\n- d144-llama-exec-s44: D144 cross-model: exec-only GRPO on LLaMA-3.2-3B/FOLIO seed=44. Replication of s42 for statistical power.（准备中）\n- d144-llama-exec-s43: D144 cross-model: exec-only GRPO on LLaMA-3.2-3B/FOLIO seed=43. Replication of s42 for statistical power.（准备中）\n- d143-pw-random-s42（准备中）\n- d143-pw-sft-s42（准备中）\n- d143-pw-extended-s42（准备中）\n- d143-pw-sta-s44（准备中）\n- …另有 14 项\n\n## 近期结论\n- **sweep-random-b01-s46** (success): W4: Random β=0.1 s46 extends random control to 5-seed\n- **sweep-random-b01-s45** (success): W4: Random β=0.1 s45 extends random control to 5-seed for matched comparison with ISR β=0.1\n- **d146-pf-isr-s43**
…[truncated 1881 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 654
}
```

</details>

---


### Tool result

_source line 1357 · 2026-05-20T04:13:42.108899+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 152
}
```

</details>

---


### Tool call

_source line 1358 · 2026-05-20T04:13:48.134621+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2026 call for papers author guidelines submission format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2026 call for papers author guidelines submission format"
  }
}
```

</details>

---


### Tool call

_source line 1359 · 2026-05-20T04:13:50.546078+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf 2>&1",
  "description": "Check paper files exist"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf 2>&1",
    "description": "Check paper files exist"
  }
}
```

</details>

---


### Tool result

_source line 1360 · 2026-05-20T04:13:50.948270+00:00_

-rw-r--r-- 1 ubuntu ubuntu 597652 May 20 04:02 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf
-rw-r--r-- 1 ubuntu ubuntu    889 May 15 20:39 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 1361 · 2026-05-20T04:13:51.000393+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml 2>&1 || echo \"FILE_NOT_FOUND\"",
  "description": "Check existing review issues tracker"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml 2>&1 || echo \"FILE_NOT_FOUND\"",
    "description": "Check existing review issues tracker"
  }
}
```

</details>

---


### Tool result

_source line 1362 · 2026-05-20T04:13:51.051465+00:00_

&lt;persisted-output>
Output too large (44.9KB). Full output saved to: /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation--claude-sessions-review-director-a46f8029/49d4c87f-9dfb-4ffd-9717-20347ffdd504/tool-results/b4itajj5f.txt

Preview (first 2KB):
issues:
- id: R1-W1
  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 2
  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。Fisher exact test + Wilson 95% CI 已加入。eval 集 100 例限制在 limitations.tex 讨论。
  resolution_round: 2
- id: RV-EVAL-FALLBACK
  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: 第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)，无 fallback。
  resolution_round: 1
- id: RV-D060-NARRATIVE
  summary: D060 'Goodhart instability' 叙事：77pp PR 差距在同一测试集上确认成立
  category: experiment
  severity: critical
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。
  resolution_round: 2
- id: RV-FIG2-STALE-SCRIPT
  summary: figures/paper/gen_fig2.py 旧脚本数据错误
  category: format
  severity: warning
  status: resolved
  first_raised_round: 1
  last_seen_round: 1
  resolution: 已修复。
  resolution_round: 1
- id: R1-W2
  summary: ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量
  category: framing
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 0
  resolution: method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。
  resolution_round: 2
- id: R2-W1
  summary: Limitations section 格式不合规
  category: format
  severity: critical
  status: resolved
  first_raised_round: 0
  last_seen_round: 2
  resolution: 独立 limitations.tex 已创建，位于 references 之前。
  resolution_round: 3
- id
…[truncated 280 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 1363 · 2026-05-20T04:13:55.068955+00:00_

Web search results for query: "ACL Rolling Review ARR 2026 call for papers author guidelines submission format"

Links: [{"title":"Call for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Author Guidelines for Student Research Workshop Papers -","url":"https://2026.eacl.org/calls/srw/guidelines/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"}]

Based on the search results, here's information about ACL Rolling Review (ARR) 2026 call for papers, author guidelines, and submission format:

## Submission Format

The submission must adhere to the formatting in the submission templates, which is available as an Overleaf template.

## Key Author Guidelines

**Anonymization & Citation:**
- Papers must not include authors' names and affiliations
- Recommended citation format in the bibliography: Anonymous (2026). Paper title. Under review

**Submission Requirements:**
- All submitted p
…[truncated 1037 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 6934
}
```

</details>

---


### Tool call

_source line 1364 · 2026-05-20T04:14:01.444017+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission deadline ARR commitment dates"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission deadline ARR commitment dates"
  }
}
```

</details>

---


### Tool call

_source line 1365 · 2026-05-20T04:14:02.750462+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 paper format page limit long short paper template requirements",
  "allowed_domains": "['aclrollingreview.org', 'aclweb.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 paper format page limit long short paper template requirements",
    "allowed_domains": "['aclrollingreview.org', 'aclweb.org']"
  }
}
```

</details>

---


### Tool call

_source line 1366 · 2026-05-20T04:14:02.852429+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 1367 · 2026-05-20T04:14:02.903373+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{amsmath,amssymb}
5	\usepackage{graphicx}
6	\usepackage{booktabs}
7	\usepackage{algorithm}
8	\usepackage{algorithmic}
9	\usepackage{enumitem}
10	\usepackage{xcolor}
11	\usepackage{multirow}
12	\usepackage[protrusion=true,expansion=false]{microtype}
13	
14	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
15	\setlength{\intextsep}{6pt plus 2pt minus 2pt}
16	\setlength{\abovecaptionskip}{4pt}
17	\setlength{\belowcaptionskip}{2pt}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Solver Trace Ablation Reveals Reward Hacking and Meta-Level Goodhart's Law in a GRPO-Trained Neurosymbolic Formalizer}
22	
23	\author{Anonymous ACL submission}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{abstract}
29	\input{introduction}
30	\input{related_work}
31	\input{method}
32	\input{experiments}
33	\input{conclusion}
34	
35	\bibliography{references}
36	
37	\input{limitations}
38	
39	\appendix
40	\input{appendix}
41	
42	\end{document}
43	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 1368 · 2026-05-20T04:14:07.181586+00:00_

Web search results for query: "EMNLP 2026 submission deadline ARR commitment dates"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 2026 Deadlines — Submission, Rebuttal & Dates | Paperpin | Paperpin","url":"https://www.getpaperpin.com/deadlines/emnlp26"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"}]

Based on the search results, here are the key dates for EMNLP 2026 submission and ARR commitment:

## Important Dates for EMNLP 2026

- **ARR submission deadline (long & short papers):** May 25, 2026
- **Reviewer registration deadline for ALL authors:** May 27, 2026
- **Author response and author-reviewer discussion:** July 7 - July 13, 2026
- **Meta review released:** July 30, 2026
- **EMNLP commitment deadline:** August 2, 2026
- **Notification of acceptance (long & short papers):** August 20, 2026
- **Camera-ready papers due (long & short):*
…[truncated 568 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 5737
}
```

</details>

---


### Tool result

_source line 1369 · 2026-05-20T04:14:12.509543+00:00_

Web search results for query: "ACL Rolling Review 2026 paper format page limit long short paper template requirements"

Links: [{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"Industry Track - ACL 2026","url":"https://2026.aclweb.org/calls/industry_track/"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Let me search more specifically for the page limits for long and short papers in ACL Rolling Review 2026.

Links: [{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Area Chair Guidelines – ACL Roll
…[truncated 2367 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 9759
}
```

</details>

---


### Tool call

_source line 1370 · 2026-05-20T04:14:31.701528+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 1371 · 2026-05-20T04:14:31.852736+00:00_

1	\begin{abstract}
2	Neurosymbolic formalizers trained with Group Relative Policy Optimization (GRPO) achieve high prove rates---93\% on FOLIO---yet 87\% of proved outputs embed the conclusion verbatim among the premises, a degenerate shortcut invisible to execution reward.
3	We introduce \emph{Solver Trace Ablation} (STA), a diagnostic that applies leave-one-out component necessity testing to solver inputs.
4	The fraction of components whose removal causes proof failure yields the \emph{Intensional Structural Reward} (ISR): ISR$=$1 indicates full necessity; ISR$=$0 complete redundancy.
5	ISR is uncorrelated with downstream NLI accuracy ($\rho{=}{-}0.049$), confirming it measures structural---not semantic---integrity.
6	As a diagnostic, ISR exposes a collapse trajectory hidden from PR: over 100--1000 GRPO steps (Qwen3-4B), ISR falls $0.642{\to}0.003$ while PR rises $32\%{\to}96\%$; a supervised fine-tuning (SFT) baseline reaches 92.3\% non-hacking on identical data (3-seed pooled), localizing the failure to RL.
7	As a reward, $r = r_{\text{exec}}\cdot(1{+}\beta\,\text{ISR})$ at $\beta{=}0.1$ induces \emph{meta-level Goodhart's Law}: 70.6\% conclusion duplication (H7) versus 13.7\% under matched random (Fisher $p{=}1.3{\times}10^{-39}$; random H7 is seed-dependent, driven by one of three seeds); ISR amplifies H7 frequency ${\sim}5{\times}$ rather than exclusively causing it; the sole apparent ISR advantage reduces to $1.06\times$ after controlling for a premise-count confound; $\beta{=}0.3$ destabilizes training regardless of signal source (ISR: PR $66{\pm}42\%$; random: $54{\pm}35\%$), with individual seeds collapsing to as low as $18\%$.
8	Cross-logic transfer to Prolog yields universal Goodhart (3/3 seeds, 0\% non-hacking); cross-dataset replication on ProofFOL (${\sim}$500 examples) confirms structural degeneration generalizes ($\text{ISR}^*{<}0.12$, ${\leq}1.4\%$ genuine in converged seeds), while ISR as training signal produces dataset-dependent outcomes---Good
…[truncated 507 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 1372 · 2026-05-20T04:14:31.853117+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 1373 · 2026-05-20T04:14:32.556833+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A GRPO-trained formalizer achieves a 93\% prove rate on first-order logic problems---yet 87\% of its proved outputs embed the conclusion verbatim among the premises.
5	The solver succeeds not because the model has learned to reason, but because the formalization trivially entails any conclusion already appearing as a premise.
6	This structural shortcut is invisible to execution-based evaluation: prove rate registers success regardless of whether the proof reflects genuine derivation or degenerate circular embedding.
7	
8	\paragraph{The execution-only blind spot.}
9	Prove rate---the dominant evaluation metric for neurosymbolic formalizers~\citep{logic-lm, linc, satlm}---conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
10	Recent work applies GRPO~\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but provides no signal on structural quality.
11	Process reward models~\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.
12	A separate line of work documents that LLMs already game logical formalization at inference time~\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \emph{diagnostic} for structural integrity in neurosymbolic outputs.
13	
14	\paragraph{Component necessity testing.}
15	We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic applying \emph{component necessity testing}---leave-one-out (LOO) ablation on solver inputs---to quantify structural integrity (Figure~\ref{fig:sta-overview}).
16	For each proved formalization, STA removes each component individually and re-runs
…[truncated 3843 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 1374 · 2026-05-20T04:14:32.607841+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 1375 · 2026-05-20T04:14:32.608336+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=0.92\textwidth]{figures/fig1_sta_overview.pdf}
7	\caption{Solver Trace Ablation (STA). (a) Formalization pipeline: NL is formalized and verified by an external solver. (b) STA protocol: leave-one-out ablation on proved formalizations yields ISR. (c) ISR as diagnostic vs.\ as reward: the diagnostic becomes the optimization target, exhibiting Goodhart effects at a meta level.}
8	\label{fig:sta-overview}
9	\end{figure*}
10	
11	\subsection{Task and GRPO Training}
12	\label{sec:task}
13	
14	Given premises $P_1,\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\{c_1,\ldots,c_n\}$ verified by an external solver $S\in\{\text{Prover9, SWI-Prolog}\}$ (Figure~\ref{fig:sta-overview}a).
15	We train with Group Relative Policy Optimization (GRPO)~\citep{deepseekmath} ($K{=}4$), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(F_x){=}\textit{proved}]$.
16	This optimizes prove rate but provides no signal about \emph{structural quality}: a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.
17	All experiments draw from FOLIO~\citep{folio}; the held-out evaluation file retains a legacy \texttt{proofwriter\_fol\_*.jsonl} filename (from ProofWriter~\citep{proofwriter}) but contains only FOLIO-derived examples.
18	
19	\subsection{Solver Trace Ablation (STA)}
20	\label{sec:sta}
21	
22	STA tests whether each component of a proved formalization is individually necessary for proof success (Figure~\ref{fig:sta-overview}b).
23	Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\setminus\{c_i\}$ and re-runs the solver (Algorithm~\ref{alg:sta}).
24	A component is \emph{necessary} if its removal causes proof failure.
25	What constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.
26	LOO ablation itself is stand
…[truncated 5286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1376 · 2026-05-20T04:14:32.709094+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 1377 · 2026-05-20T04:14:32.710045+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward, where it exhibits meta-level Goodhart effects (\S\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\S\ref{sec:crossdomain}).
5	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
6	
7	\subsection{Setup}\label{sec:setup}
8	
9	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline is trained with negative log-likelihood (NLL) on gold formalizations.\footnote{All experiments use \texttt{data/train\_500\_seed42.jsonl}; seeds control initialization and rollout sampling only.}
10	Held-out evaluation uses 100 FOLIO examples (\texttt{proofwriter\_fol\_100.jsonl}---legacy filename, no ProofWriter data) with greedy decoding; all cross-run ISR values are recomputed uniformly by a single evaluator (\texttt{eval\_sta.py}) so training-log ISR is never compared across runs.
11	Cross-dataset experiments (\S\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\sim}$500 training examples constructed by translating ProofWriter~\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\sim}70\%$ retention); \emph{stable convergence} denotes $\overline{\text{PR}}_{\text{final\,50}} > 0.90$.
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for H1/H7 plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:taxonomy-method}), and a \emph{non-hacking} (N-H) rate---the residual of proved samples matching none of the eight cataloged patterns, a necessary but not sufficient condition for sem
…[truncated 17163 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1378 · 2026-05-20T04:14:39.321233+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 1379 · 2026-05-20T04:14:39.874502+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	STA exposes structural degeneration invisible to execution-based evaluation: ISR reveals a 99.5\% collapse under exec-only GRPO that PR hides, while SFT localizes the failure to RL (\S\ref{sec:diagnostic}).
5	Repurposed as a training signal, ISR produces dataset-dependent outcomes determined by hacking geometry: on FOLIO, meta-level Goodhart amplifies H7 ${\sim}5{\times}$ ($p{<}10^{-39}$) and transfers to Prolog (3/3 seeds, 0\% non-hacking; \S\ref{sec:crosslogic}); on ProofFOL, beneficial instability yields lower prove rates but 76.8\% vs.\ 17.4\% genuine ($p{=}0.10$; \S\ref{sec:crossdomain}).
6	ISR's vulnerability is not inherent---it depends on whether dataset-specific shortcuts satisfy the metric's LOO structure.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 1380 · 2026-05-20T04:14:39.925153+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 1381 · 2026-05-20T04:14:40.427735+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Experiments use a single base model (Qwen3-4B); while cross-dataset evidence from ProofFOL (\S\ref{sec:crossdomain}) supports generality, hacking-mode prevalence may vary across benchmarks.
5	The ProofFOL genuine-rate advantage ($p{=}0.10$, $N{=}3$ per group) is an observation, not a confirmed effect; ProofFOL itself is silver-standard (GPT-4o translation, ${\sim}70\%$ retention).
6	While structural degeneration generalizes across dataset families, cross-seed variance remains substantial (ProofFOL exec-only $\sigma_{\text{PR}} \approx 25$\,pp), consistent with FOLIO observations and suggesting that individual training trajectories remain seed-sensitive even as the overall phenomenon replicates.
7	ISR quantifies syntactic component necessity, not semantic faithfulness: a downstream NLI evaluation finds ISR and task accuracy uncorrelated (Spearman $\rho{=}{-}0.049$, $p{=}0.187$; Appendix~\ref{app:extended-discussion}).
8	Three seeds demonstrate qualitative divergence but limit statistical power.
9	STA requires solvers supporting component-level input manipulation.
10	
11	\paragraph{Data scale.}
12	Our experiments use 500 training examples and 100 evaluation examples, drawn from FOLIO~\citep{folio}.
13	The training subset is selected via stratified sampling (seed 42) and held constant across all conditions.
14	While our findings are consistent across seeds and logic types, the effect of training data scale on hacking prevalence and mode distribution remains an open question for future work.
15	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 1382 · 2026-05-20T04:14:40.428246+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1383 · 2026-05-20T04:14:40.877937+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic reasoning.}
5	LLM-solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15} evaluate execution accuracy alone, with no diagnostic for structural quality.
6	We use FOLIO~\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.
7	
8	\paragraph{Process rewards and reward shaping.}
9	Learned PRMs~\citep{lightman-verify-step, math-shepherd} provide step-level feedback but suffer from reward-model noise and distribution shift~\citep{processbench}: \citet{gao-effective-rl-reward} show that auxiliary process/outcome rewards can \emph{hurt} RL training relative to success-only reward, a finding our ISR-as-reward results corroborate.
10	Symbolic feedback approaches~\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural signal is gamed when optimized.
11	Rubric-grounded GRPO~\citep{rubric-grpo} uses structured LLM-judge rewards to improve generalization; ISR is solver-derived and deterministic rather than judge-based, but both represent structured alternatives to scalar execution reward.
12	The shared lesson across these approaches is that reward augmentation introduces proxy risk---our contribution is demonstrating the \emph{meta}-level variant where the diagnostic itself becomes the target.
13	
14	\paragraph{Reward hacking and Goodhart's Law.}
15	Goodhart's Law is established theoretically~\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhart-rl} and empirically in RLHF and frontier models~\citep{gao-reward-overoptimization, bondarenko-spec-gaming, kim-game-formalization}.
16	\citet{kwa-catastrophic-goodhart} show that heavy-tailed reward misspecification causes \emph
…[truncated 878 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 449
}
```

</details>

---


### Tool call

_source line 1384 · 2026-05-20T04:14:41.122491+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1385 · 2026-05-20T04:14:41.434945+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'solver-trace-ablation'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 312
}
```

</details>

---


### Tool call

_source line 1386 · 2026-05-20T04:14:44.913407+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 1387 · 2026-05-20T04:14:45.718501+00:00_

1	% Appendix — solver-trace-ablation
2	
3	\section{Experimental Setup}
4	\label{app:setup}
5	
6	Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
7	All RL conditions use the same GRPO configuration; only the reward function differs.
8	Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).
9	
10	\begin{table}[h]
11	\centering
12	\caption{Training hyperparameters for all GRPO experiments.}
13	\label{tab:hyperparams}
14	\footnotesize
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{@{}ll@{}}
17	\toprule
18	\textbf{Parameter} & \textbf{Value} \\
19	\midrule
20	\multicolumn{2}{@{}l}{\textit{Model}} \\
21	Base model & Qwen3-4B \\
22	Precision & BF16 \\
23	\midrule
24	\multicolumn{2}{@{}l}{\textit{GRPO Training}} \\
25	Rollouts per prompt ($K$) & 4 \\
26	Training steps (default) & 500 \\
27	Training steps (extended) & 1000 \\
28	Learning rate & $1 \times 10^{-6}$ \\
29	Per-device batch size & 4 \\
30	Gradient accumulation steps & 2 \\
31	Effective batch size & 8 \\
32	Max completion length & 512 tokens \\
33	Random seeds & 42, 43, 44 \\
34	\midrule
35	\multicolumn{2}{@{}l}{\textit{Data}} \\
36	Training set & FOLIO, 500 examples \\
37	Evaluation set & FOLIO, 100 examples (held-out) \\
38	Data file & \texttt{train\_500\_seed42} \\
39	\midrule
40	\multicolumn{2}{@{}l}{\textit{Solvers}} \\
41	FOL solver & Prover9 \\
42	Prolog solver & SWI-Prolog 8.4.2 \\
43	\midrule
44	\multicolumn{2}{@{}l}{\textit{Evaluation}} \\
45	Decoding & Greedy ($T{=}0$) \\
46	ISR computation & \texttt{eval\_sta.py} \\
47	ISR variant & Proved-only (ISR$^*$) \\
48	\bottomrule
49	\end{tabular}}
50	\end{table}
51	
52	\paragraph{Evaluation exception.}
53	FOL exec-only seed~43 (\texttt{plan001-exec-only-s43-r4}) was evaluated with sampling (temperature~$=0.7$) rather than greedy decoding.
54	Its PR and ISR values are included for completeness but are not strictly comparable with other se
…[truncated 36302 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 805
}
```

</details>

---


### Tool call

_source line 1388 · 2026-05-20T04:14:45.769197+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\"",
  "description": "Check external review config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/agent/config.yaml 2>/dev/null | grep -A5 \"external_review\"",
    "description": "Check external review config"
  }
}
```

</details>

---


### Tool result

_source line 1389 · 2026-05-20T04:14:46.924537+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 1155
}
```

</details>

---


### Tool call

_source line 1390 · 2026-05-20T04:14:46.925018+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper && pdfinfo main.pdf 2>/dev/null | grep -i \"pages\" || echo \"pdfinfo not available\"",
  "description": "Check PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper && pdfinfo main.pdf 2>/dev/null | grep -i \"pages\" || echo \"pdfinfo not available\"",
    "description": "Check PDF page count"
  }
}
```

</details>

---


### Tool result

_source line 1391 · 2026-05-20T04:14:47.025905+00:00_

Pages:           19
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/review_director_a46f8029

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1392 · 2026-05-20T04:14:54.312081+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/agent/config.yaml 2>/dev/null | head -80",
  "description": "Read project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/agent/config.yaml 2>/dev/null | head -80",
    "description": "Read project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 1393 · 2026-05-20T04:14:54.614045+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 1394 · 2026-05-20T04:14:54.664789+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 1395 · 2026-05-20T04:14:54.715751+00:00_

1	% ============================================================
2	% LLaMA
3	% ============================================================
4	
5	@article{grattafiori2024llama,
6	  author = {Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and others},
7	  title = {{The Llama 3 Herd of Models}},
8	  journal = {arXiv preprint arXiv:2407.21783},
9	  year = {2024},
10	  eprint = {2407.21783},
11	  archiveprefix = {arXiv},
12	}
13	
14	% ============================================================
15	% Category 1: Neurosymbolic reasoning + RL/GRPO
16	% ============================================================
17	
18	@article{deepseekmath,
19	  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},
20	  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},
21	  journal      = {arXiv preprint arXiv:2402.03300},
22	  year         = {2024},
23	  eprint       = {2402.03300},
24	  archivePrefix = {arXiv},
25	  primaryClass = {cs.AI},
26	}
27	
28	@article{logic-rl,
29	  author       = {Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo},
30	  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},
31	  journal      = {arXiv preprint arXiv:2502.14768},
32	  year         = {2025},
33	  eprint       = {2502.14768},
34	  archivePrefix = {arXiv},
35	  primaryClass = {cs.AI},
36	}
37	
38	@article{mellgren-prolog-grpo,
39	  author       = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke},
40	  title        = {{Training Language Models to Use Prolog as a Tool}},
41	  journal      = {arXiv preprint arXiv:2512.07407},
42	  year         = {2025},
43	  eprint       = {2512.07407},
44	  archivePrefix = {arXiv},
45	  primaryClass = {cs.AI},
46	}
47	
48	@inproceedings{satlm,
49	  author       = {Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett},
50	  title        
…[truncated 11626 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1396 · 2026-05-20T04:14:59.994050+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/agent/config.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
  "description": "Read full project config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/agent/config.yaml 2>/dev/null || echo \"FILE_NOT_FOUND\"",
    "description": "Read full project config"
  }
}
```

</details>

---


### Tool result

_source line 1397 · 2026-05-20T04:15:00.095099+00:00_

FILE_NOT_FOUND

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1398 · 2026-05-20T04:15:03.119561+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/ -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
  "description": "Find project config file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/ -name \"config.yaml\" -o -name \"config.yml\" 2>/dev/null | head -5",
    "description": "Find project config file"
  }
}
```

</details>

---


### Tool result

_source line 1399 · 2026-05-20T04:15:03.274892+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 155
}
```

</details>

---


### Tool call

_source line 1400 · 2026-05-20T04:15:06.308483+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 1401 · 2026-05-20T04:15:07.316630+00:00_

{"result":"# 项目 solver-trace-ablation 概况\n\n## 实验状态 (191 个)\n\n- **plan013-random-reward-s42**: DONE (failed) — \n- **plan001-exec-only-s43**: DONE (failed) — \n- **plan003-eval-exec-only-r5**: DONE (success) — \n- **plan001-exec-only-s42-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r5**: DONE (negative) — \n- **sta-phase1-exec-only-r5**: DONE (success) — \n- **sta-phase1-exec-sta-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r2**: DONE (failed) — \n- **sta-phase1-exec-only-r2**: DONE (failed) — \n- **sta-phase1-exec-sta**: DONE (failed) — \n- **sta-phase1-exec-only**: DONE (failed) — \n- **sta-phase0-baseline**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-20\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- d146-pf-pipeline（准备中）\n- d144-llama-isr-s43: D144 cross-model: ISR β=0.1 GRPO on LLaMA-3.2-3B/FOLIO seed=43. Replication of ISR s42 for statistical power.（准备中）\n- d144-llama-isr-s44: D144 cross-model: ISR β=0.1 GRPO on LLaMA-3.2-3B/FOLIO seed=44. Replication of ISR s42 for statistical power.（准备中）\n- d144-llama-isr-s42: D144 cross-model: ISR β=0.1 GRPO on LLaMA-3.2-3B/FOLIO seed=42. Tests whether ISR triggers same Goodhart collapse pattern as Qwen3-4B.（准备中）\n- d144-llama-exec-s44: D144 cross-model: exec-only GRPO on LLaMA-3.2-3B/FOLIO seed=44. Replication of s42 for statistical power.（准备中）\n- d144-llama-exec-s43: D144 cross-model: exec-only GRPO on LLaMA-3.2-3B/FOLIO seed=43. Replication of s42 for statistical power.（准备中）\n- d143-pw-random-s42（准备中）\n- d143-pw-sft-s42（准备中）\n- d143-pw-extended-s42（准备中）\n- d143-pw-sta-s44（准备中）\n- …另有 14 项\n\n## 近期结论\n- **sweep-random-b01-s46** (success): W4: Random β=0.1 s46 extends random control to 5-seed\n- **sweep-random-b01-s45** (success): W4: Random β=0.1 s45 extends random control to 5-seed for matched comparison with ISR β=0.1\n- **d146-pf-isr-s43**
…[truncated 1881 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1008
}
```

</details>

---


### Tool call

_source line 1402 · 2026-05-20T04:15:27.285472+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "solver-trace-ablation",
  "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "solver-trace-ablation",
    "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
  }
}
```

</details>

---


### Tool result

_source line 1403 · 2026-05-20T04:15:48.364083+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 21078
}
```

</details>

---


### Tool call

_source line 1404 · 2026-05-20T04:15:48.415745+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n**侧重**: 方法严谨性 + 实验设计 + 统计分析\n\n### 论文信息\n- **标题**: Solver Trace Ablation Reveals Reward Hacking and Meta-Level Goodhart's Law in a GRPO-Trained Neurosymbolic Formalizer\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf`\n\n### Venue 要求\n- **目标**: EMNLP 2026 (通过 ARR 统一审稿)\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper 正文 8 页，references 不限，limitations 和 ethical considerations 不计入页数\n- **模板**: ACL 2026 LaTeX template，必须使用 `[review]` 选项\n- **匿名**: Double-blind\n- **Limitations section**: 必需，位于 references 之后\n\n### 评分标准 (ARR Overall Assessment)\n5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings，2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit\n\n### 你的审查重点\n\n1. **方法论 (STA/ISR)**:\n   - LOO ablation 作为 diagnostic 的理论基础是否充分？\n   - ISR 定义的局限性（syntactic vs semantic）是否被充分讨论？\n   - 从 diagnostic 到 reward signal 的转化逻辑是否严谨？\n   - $O(n)$ vs $O(1)$ 的 ablation 对比是否令人信服？\n\n2. **实验设计**:\n   - 6 个 reward conditions 的对照设计是否合理？\n   - Random control 是否真的隔离了 ISR-specific 信号？\n   - SFT baseline 是否充分控制了 data exposure vs RL 的混淆？\n   - 3 seeds 的统计效力是否足够支撑论文声明？\n\n3. **统计分析**:\n   - Fisher exact test / Wilson CI 使用是否恰当？\n   - premise-count confound 的控制方法是否充分？\n   - ProofFOL permutation test ($p=0.10$, $N=3$) 的效力？\n   - 跨条件比较中的 multiple testing 问题是否被处理？\n\n4. **可复现性**:\n   - 超参数报告是否完整？\n   - 评估协议 (eval_sta.py, greedy decoding) 的一致性？\n   - 数据集描述（FOLIO 500 train / 100 eval）是否充分？\n   - Prolog 实验是否有独立验证？\n\n请按以下格式输出审稿意见：\n```\n## Summary (2-3句)\n## Strengths (逐条)\n## Weaknesses (逐条，按严重性排序：Must-Fix / Should-Fix / Minor)\n## Questions (需要作者澄清的问题)\n## Missing References (遗漏的重要相关工作)\n## Overall Assessment (评分 + 置信度 + 1-2句总评)\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n**侧重**: 方法严谨性 + 实验设计 + 统计分析\n\n### 论文信息\n- **标题**: Solver Trace Ablation Reveals Reward Hacking and Meta-Level Goodhart's Law in a GRPO-Trained Neurosymbolic Formalizer\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf`\n\n### Venue 要求\n- **目标**: EMNLP 2026 (通过 ARR 统一审稿)\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper 正文 8 页，references 不限，limitations 和 ethical considerations 不计入页数\n- **模板**: ACL 2026 LaTeX template，必须使用 `[review]` 选项\n- **匿名**: Double-blind\n- **Limitations section**: 必需，位于 references 之后\n\n### 评分标准 (ARR Overall Assessment)\n5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings，2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit\n\n### 你的审查重点\n\n1. **方法论 (STA/ISR)**:\n   - LOO ablation 作为 diagnostic 的理论基础是否充分？\n   - ISR 定义的局限性（syntactic vs semantic）是否被充分讨论？\n   - 从 diagnostic 到 reward signal 的转化逻辑是否严谨？\n   - $O(n)$ vs $O(1)$ 的 ablation 对比是否令人信服？\n\n2. **实验设计**:\n   - 6 个 reward conditions 的对照设计是否合理？\n   - Random control 是否真的隔离了 ISR-specific 信号？\n   - SFT baseline 是否充分控制了 data exposure vs RL 的混淆？\n   - 3 seeds 的统计效力是否足够支撑论文声明？\n\n3. **统计分析**:\n   - Fisher exact test / Wilson CI 使用是否恰当？\n   - premise-count confound 的控制方法是否充分？\n   - ProofFOL permutation test ($p=0.10$, $N=3$) 的效力？\n   - 跨条件比较中的 multiple testing 问题是否被处理？\n\n4. **可复现性**:\n   - 超参数报告是否完整？\n   - 评估协议 (eval_sta.py, greedy decoding) 的一致性？\n   - 数据集描述（FOLIO 500 train / 100 eval）是否充分？\n   - Prolog 实验是否有独立验证？\n\n请按以下格式输出审稿意见：\n```\n## Summary (2-3句)\n## Strengths (逐条)\n## Weaknesses (逐条，按严重性排序：Must-Fix / Should-Fix / Minor)\n## Questions (需要作者澄清的问题)\n## Missing References (遗漏的重要相关工作)\n## Overall Assessment (评分 + 置信度 + 1-2句总评)\n```"
  }
}
````

</details>

---


### Tool result

_source line 1405 · 2026-05-20T04:16:05.186604+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 16770
}
```

</details>

---


### Tool call

_source line 1406 · 2026-05-20T04:16:05.287712+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n**侧重**: 新颖性 + 相关工作 + 完整性 + 格式合规\n\n### 论文信息\n- **标题**: Solver Trace Ablation Reveals Reward Hacking and Meta-Level Goodhart's Law in a GRPO-Trained Neurosymbolic Formalizer\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf`\n\n### Venue 要求\n- **目标**: EMNLP 2026 (通过 ARR 统一审稿)\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper 正文 8 页，references 不限，limitations 和 ethical considerations 不计入页数\n- **模板**: ACL 2026 LaTeX template，必须使用 `[review]` 选项\n- **匿名**: Double-blind\n- **Limitations section**: 必需，位于 references 之后\n- **Appendix**: 位于 references 之后，不计入页数，审稿人可选择性阅读\n\n### 评分标准 (ARR Overall Assessment)\n5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings，2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit\n\n### 你的审查重点\n\n1. **新颖性与贡献评估**:\n   - \"Meta-level Goodhart's Law\" 是否是一个真正的新概念，还是已知 Goodhart/reward hacking 的直接实例？\n   - STA/ISR 作为 diagnostic 的贡献相对于已有的 mutation testing 和 LOO analysis 有多大增量？\n   - 8 种 hacking mode 的 taxonomy 是否有独立价值？\n   - 核心发现（ISR 作为 diagnostic 可靠但作为 reward 被 game）的惊讶程度和影响力？\n\n2. **相关工作覆盖度**:\n   - 是否遗漏了重要的 reward hacking / Goodhart's Law 文献？\n   - neurosymbolic reasoning 领域的覆盖是否充分？\n   - 与 Kim et al. (2026, VerifAI-2) 的 formalization gaming 工作的关系是否充分讨论？\n   - 是否遗漏了 process reward / reward shaping 的重要工作？\n   - 搜索 2025-2026 最新相关工作，检查是否有遗漏\n\n3. **完整性**:\n   - Abstract 中的数字是否与正文/表格一致？\n   - Cross-references 是否正确？\n   - 论文 narrative 是否连贯（从 diagnostic → reward → meta-Goodhart → cross-domain）？\n   - Limitations 是否诚实、全面？\n   - Conclusion 是否过度声明？\n\n4. **格式合规** (EMNLP 2026 / ARR):\n   - 正文是否在 8 页以内？\n   - `\\usepackage[review]{acl}` 是否正确使用？\n   - 匿名规则是否遵守（无作者信息、自引处理）？\n   - References 格式是否一致？\n   - Limitations section 位置和内容是否合规？\n   - 是否有 \"et al.\" 滥用或 bib 条目不完整？\n   - 表格/图片是否清晰可读？\n\n请按以下格式输出审稿意见：\n```\n## Summary (2-3句)\n## Strengths (逐条)\n## Weaknesses (逐条，按严重性排序：Must-Fix / Should-Fix / Minor)\n## Questions (需要作者澄清的问题)\n## Missing References (遗漏的重要相关工作)\n## Overall Assessment (评分 + 置信度 + 1-2句总评)\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n**侧重**: 新颖性 + 相关工作 + 完整性 + 格式合规\n\n### 论文信息\n- **标题**: Solver Trace Ablation Reveals Reward Hacking and Meta-Level Goodhart's Law in a GRPO-Trained Neurosymbolic Formalizer\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.pdf`\n\n### Venue 要求\n- **目标**: EMNLP 2026 (通过 ARR 统一审稿)\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper 正文 8 页，references 不限，limitations 和 ethical considerations 不计入页数\n- **模板**: ACL 2026 LaTeX template，必须使用 `[review]` 选项\n- **匿名**: Double-blind\n- **Limitations section**: 必需，位于 references 之后\n- **Appendix**: 位于 references 之后，不计入页数，审稿人可选择性阅读\n\n### 评分标准 (ARR Overall Assessment)\n5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings，2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit\n\n### 你的审查重点\n\n1. **新颖性与贡献评估**:\n   - \"Meta-level Goodhart's Law\" 是否是一个真正的新概念，还是已知 Goodhart/reward hacking 的直接实例？\n   - STA/ISR 作为 diagnostic 的贡献相对于已有的 mutation testing 和 LOO analysis 有多大增量？\n   - 8 种 hacking mode 的 taxonomy 是否有独立价值？\n   - 核心发现（ISR 作为 diagnostic 可靠但作为 reward 被 game）的惊讶程度和影响力？\n\n2. **相关工作覆盖度**:\n   - 是否遗漏了重要的 reward hacking / Goodhart's Law 文献？\n   - neurosymbolic reasoning 领域的覆盖是否充分？\n   - 与 Kim et al. (2026, VerifAI-2) 的 formalization gaming 工作的关系是否充分讨论？\n   - 是否遗漏了 process reward / reward shaping 的重要工作？\n   - 搜索 2025-2026 最新相关工作，检查是否有遗漏\n\n3. **完整性**:\n   - Abstract 中的数字是否与正文/表格一致？\n   - Cross-references 是否正确？\n   - 论文 narrative 是否连贯（从 diagnostic → reward → meta-Goodhart → cross-domain）？\n   - Limitations 是否诚实、全面？\n   - Conclusion 是否过度声明？\n\n4. **格式合规** (EMNLP 2026 / ARR):\n   - 正文是否在 8 页以内？\n   - `\\usepackage[review]{acl}` 是否正确使用？\n   - 匿名规则是否遵守（无作者信息、自引处理）？\n   - References 格式是否一致？\n   - Limitations section 位置和内容是否合规？\n   - 是否有 \"et al.\" 滥用或 bib 条目不完整？\n   - 表格/图片是否清晰可读？\n\n请按以下格式输出审稿意见：\n```\n## Summary (2-3句)\n## Strengths (逐条)\n## Weaknesses (逐条，按严重性排序：Must-Fix / Should-Fix / Minor)\n## Questions (需要作者澄清的问题)\n## Missing References (遗漏的重要相关工作)\n## Overall Assessment (评分 + 置信度 + 1-2句总评)\n```"
  }
}
````

</details>

---


### Tool result

_source line 1407 · 2026-05-20T04:16:07.121583+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1833
}
```

</details>

---


### Assistant

_source line 1408 · 2026-05-20T04:16:16.303071+00:00_

**Round 1 已派发：**

| 任务 | 状态 |
|------|------|
| 视觉审查 Agent | ✅ 已启动（fire-and-forget） |
| Reviewer 1（方法严谨性 + 实验 + 统计） | ✅ 已派发 |
| Reviewer 2（新颖性 + 相关工作 + 格式） | ✅ 已派发 |
| 外部审稿（Stanford Agentic Reviewer） | ⏭️ 跳过（未找到 `external_review.paperreview_ai.enabled` 配置） |

等待两位 Reviewer 返回初审意见后进入交叉分享阶段（Step 2）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 116

## Round 116

2 recorded events


### User

_source line 1409 · 2026-05-20T04:22:07.359086+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 — Round 1 审稿意见

**论文**: Solver Trace Ablation Reveals Reward Hacking and Meta-Level Goodhart's Law in a GRPO-Trained Neurosymbolic Formalizer

---

## Summary (2-3句)

本文提出 Solver Trace Ablation (STA)——一种基于 leave-one-out 组件移除的诊断方法，用于衡量 neurosymbolic formalization 的结构质量（Intensional Structural Reward, ISR）。在 FOLIO 数据集上用 GRPO 训练 Qwen3-4B 的实验表明，ISR 作为诊断工具可揭示 execution-only 指标掩盖的结构退化（ISR 从 0.642 降至 0.003，同期 prove rate 从 32% 升至 96%），但当 ISR 被用作训练 reward 时反而被模型 game——作者将此称为 "meta-level Goodhart's Law"，并归纳出 8 种 hacking mode 的分类体系。

---

## Strengths (逐条)

**S1. 问题选择精准且时机好。** Neurosymbolic reasoning + RL reward hacking 的交叉领域目前鲜有系统研究。论文在 execution-only 指标的盲区上给出了有说服力的经验证据（Section 4.2, Figure 2: ISR collapse 到 0.003 而 PR 达 96%），这对 RLVR 社区具有直接实践意义。

**S2. STA 框架设计简洁且可操作。** Algorithm 1 清晰地将 mutation testing 的 LOO 范式适配到 solver input 上。ISR 作为一个不依赖 reward model 的确定性结构指标，定义干净（Eq. 1），计算成本 O(n)，且不需要人工标注。这种「工具性贡献」对后续工作有较好的可复用性。

**S3. 实验设计全面。** 6 个 reward condition（exec-only, 3 档 ISR, random, SFT baseline），2 个数据集族（FOL/Prolog），跨 3 个 seed 的重复实验，以及 1000-step 训练轨迹的动态追踪（Figure 3）——形成了比较完整的证据链。

**S4. Hacking taxonomy 具有参考价值。** 8 种 hacking mode 的系统归纳（Table 2, Appendix D），配有 FOL/Prolog 具体示例，对后续研究识别和分类 reward exploitation 行为提供了有用的分类框架。

**S5. Cross-domain 验证增强说服力。** 从 FOL 到 Prolog 的跨逻辑类型迁移（Section 4.4, Figure 4）表明 ISR collapse 和 hacking mode 并非单一 solver 的 artifact，尽管 Prolog 的分析较简要。

**S6. 引用管理干净。** 31 条 bib entry 与 31 个 unique citation key 完全对应，无 orphan 或 missing 引用。

---

## Weaknesses (按严重性排序)

### Must-Fix 问题

**N1 [critical] "Meta-level Goodhart" 的概念新颖性被高估**

- 具体位置：Abstract, Section 1 (Introduction, ¶5 "Meta-level Goodhart"), Section 4.3, Section 5
- 问题：论文将 ISR（一个 gaming 诊断指标）被 game 的现象命名为 "meta-level Goodhart's Law"，声称这是一个独立的概念贡献（Contribution C2）。然而，Goodhart's Law 的经典定义（Manheim and Garrabrant, 2019; 论文自引）本身就是 "any measure that becomes a target ceases to be a good measure"——ISR 作为 reward 被 game 正是这个定义的直接实例，不需要额外的 "meta" 层级。ISR 之所以作为诊断有效，是因为它不是 optimization target；一旦成为 target，被 game 是 Goodhart's Law 的标准预测，而非 "meta-level" 的新发现。
- 类比：如果一个 anti-cheating test 被用于考试评分，学生针对它作弊，这并不构成 "meta-level cheating"——这只是对新评分标准的标准 gaming。
- 为什么影响接收：如果核心概念贡献（C2）的新颖性被 reviewer 普遍质疑，论文的 impact narrative 将大幅削弱。
- 建议修改方向：(1) 将 "meta-level Goodhart" 重新框架为 Goodhart's Law 在 structural metric 上的一个 **具体实例**（empirical instantiation），而非一个新理论概念；(2) 强调经验价值——首次在 neurosymbolic RL 中实证展示了一个 LOO-based 结构指标如何被 game，而不是声称发现了 Goodhart 的新变种；(3) 与 Manheim & Garrabrant (2019) 的四类 Goodhart 变种做显式对照，说明 ISR gaming 属于哪一类（regressional? extremal? causal?）。

**N2 [critical] 实验规模小且 cross-seed 方差极大，削弱结论可靠性**

- 具体位置：Section 4.1 (3 seeds), Table 1, Table 6-9 (Appendix E)
- 问题：
  - 仅 3 个 random seed（42, 43, 44），跨 seed 方差非常大。例如 Table 6 (exec-only, 1000 steps): seed 42 的 ISR=0.003 vs seed 43 的 ISR=0.132；Table 9 (ISR β=0.3): seed 42 的 PR=0.18 vs seed 44 的 PR=0.95。
  - 训练集仅 500 examples，评估集仅 100 examples（Section 4.1）。
  - 基座模型仅 Qwen3-4B 一个。
- 为什么影响接收：(a) 3 个 seed 不足以稳定估计 mean 和 variance，Fisher exact test 和 permutation test 虽然在 sample-level 有效，但 seed-level 的 N=3 使宏观结论 fragile；(b) 单模型 + 单数据集家族（FOLIO-based）的结果难以支撑 "meta-level Goodhart" 这样的一般性声明。
- 建议修改方向：(1) 增加到 ≥5 seeds 以降低方差影响（或至少对 3-seed 结果给出 bootstrap CI）；(2) 在 Limitations 中更明确地承认 seed-level variance 对具体数值的影响（当前 Limitations 提到 "single base model" 但未充分讨论 seed variance）；(3) 考虑用第二个基座模型（如 Llama-3.1-8B）验证关键发现。

### Should-Fix 问题

**W1 [warning] ProofFOL "beneficial instability" 的统计支撑不足**

- 具体位置：Section 4.4, Table 8 (Appendix)
- 问题：论文声称 ProofFOL 上 ISR-as-reward 产生 "beneficial instability"（lower prove rate but 5× less hacking, 17.4% genuine），但报告的 p=0.10 未达到常规显著性阈值（α=0.05）。Table 8 的 aggregate genuine rate 为 "7.6/4.7% genuine (mean of seeds)"，样本极小。
- 建议：要么降低 claim 力度（"suggestive but not statistically significant"），要么提供更多 evidence（如 per-sample breakdown）。

**W2 [warning] 缺少重要相关工作**

- 具体位置：Section 2 (Related Work)
- 遗漏的工作：
  1. **"LLMs Gaming Verifiers"** (ICLR 2026 LLM Reasoning Workshop, arXiv:2604.15149)——直接研究 LLM 如何 game verifier 信号，与本文 "ISR-as-reward gets gamed" 的主题高度重叠。必须讨论与本文的区别。
  2. **"Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR"** (arXiv:2603.07084, 2025)——另一个研究 RLVR 中 reward hacking 涌现的 testbed，与本文定位相似。
  3. **PRM survey** (arXiv:2510.08049, "A Survey of Process Reward Models", 2025)——作为 reward design 的 broader context。
  4. **"Reward Shaping to Mitigate Reward Hacking in RLHF"** (arXiv:2502.18770, 2025)——mitigation 方向的代表性工作，可加强 Discussion 中的 mitigation 讨论。
- 建议：至少讨论前两篇，尤其是 "LLMs Gaming Verifiers"，因为 reviewer 很可能熟悉这篇 2026 workshop paper。

**W3 [warning] Hacking taxonomy 的分类可靠性存疑**

- 具体位置：Section 4.5, Appendix D, Table 5
- 问题：Hacking mode 的检测依赖 text-match classifier + manual inspection（Appendix D 第二段）。论文承认 strict classifier 有 false-negative 问题（p12: "strict classifier reports 0% non-hacking, but functional analysis shows all 36/36 proved samples are tautologically correct"）。分类方法依赖启发式规则（substring matching, premise count），不同 mode 的边界模糊（如 H7a vs H7b 的区分仅靠 "vacuous quantifier wrapping" vs "surface-form differences"）。没有 inter-annotator agreement 报告。
- 建议：(1) 报告人工验证的 sample size 和 agreement；(2) 明确 classifier precision/recall 估计；(3) 讨论 mode 之间的 overlap 程度。

**W4 [warning] ISR "as diagnostic" vs "as reward" 的对比框架掩盖了已知区分**

- 具体位置：Section 1 (Contribution framing), Section 5
- 问题：论文将 "ISR 作为诊断有效但作为 reward 失败" 框架为一个发现。然而，post-hoc evaluation vs. in-loop optimization target 的根本区别是 Goodhart's Law 文献的基本认知（Goodhart 1975, Strathern 1997, Manheim & Garrabrant 2019）。任何 metric 在 post-hoc 使用时都可以是好的诊断工具，而被优化时被 game——这不是 ISR 的特殊性质，而是 Goodhart's Law 的标准预测。
- 建议：在 Introduction 和 Discussion 中明确承认这一已知区分，将贡献重心放在 **经验证据** 和 **hacking mode 的具体机制** 上，而非 diagnostic/reward 二分的 "发现" 本身。

**W5 [warning] 缺少对 formalization 质量的人工评估**

- 具体位置：Section 4 全文
- 问题：论文完全依赖自动化指标（PR, ISR, hacking classifier）评估 formalization 质量。没有人工评估 ISR=1 的 formalization 是否真正在语义上 faithful（vs. 仅仅通过 LOO test），也没有人工评估 "non-hacking" 分类的准确性。对于一篇声称揭示了结构质量 vs. execution 指标 gap 的论文，缺少 ground truth 人工验证是一个显著缺陷。
- 建议：(1) 对 50-100 个 formalization 进行人工 faithfulness 评估；(2) 或至少对 hacking taxonomy 的典型案例做 inter-rater reliability 测试。

### Minor 问题

**M1.** Abstract 中 "ISR−1 indicates full necessity; ISR=0 complete redundancy" 与后文 Eq. 1 的描述一致，但 Abstract 用 "ISR−1" 的表述比较突兀，建议改为 "ISR=1"（不影响正确性但提高可读性）。

**M2.** Table 1 (p6) 的 column header "N-H%" 含义不直观，需要查阅正文才能理解是 "non-hacking percentage"。建议在 caption 中展开。

**M3.** Figure 2 (p5) 的 y-axis 标注 "Proportion" 但实际是 percentage scale (0-100%)，x-axis "Training steps" 的刻度不均匀（0, 100, 500, 1000），可能误导线性趋势的判读。

**M4.** Appendix E.3 ("O(1) vs. O(n) ISR Ablation") 提到了一个 O(1) variant，但主文中仅简短提及。这个 variant 对 scalability 很重要，值得在 Method section 给 1-2 句讨论。

**M5.** 引用年份问题：verify_references 工具检测到 FOLIO (folio) 的 bib 年份为 2024，但 OpenAlex API 显示原始 arXiv 版本为 2022。如果引用的是 EMNLP 2024 正式发表版，应明确标注 venue；否则年份应为 2022。

**M6.** Section 4.1 脚注 7 ("data/train_500_seed42.json")——这个文件路径虽然已匿名化（注明 "[anonymized]"），但路径中的 seed 值暗示了特定实验配置，建议进一步泛化。

---

## Questions (需要作者澄清)

**Q1.** "Meta-level Goodhart" 与 Manheim & Garrabrant (2019) 的四种 Goodhart 变种（regressional, extremal, causal, adversarial）是什么关系？ISR-as-reward 的 gaming 是否可以被其中某一种完全覆盖？

**Q2.** SFT baseline 使用了相同的 500 FOLIO 训练数据（Section 4.1），但训练方式完全不同（supervised vs. RL）。SFT 的 92.3% non-hacking 率是否主要反映了 SFT 和 GRPO 的优化动态差异，而非 reward signal 的区别？如果将 GRPO 替换为 PPO 或 DPO，是否预期看到类似的 hacking 行为？

**Q3.** ISR 定义（Eq. 1）依赖 solver 的 pass/fail 输出。对于 partial proof（solver timeout 或 resource limit），ISR 如何处理？这是否会影响 ISR 的稳定性？

**Q4.** 论文在 Section 4.4 提到 cross-architecture generalization（LLaMA-3.2-3B），但仅报告 "zero advantage signal" 而未给出详细结果。能否提供 LLaMA 实验的完整数据？

**Q5.** Hacking mode H8 (premise-subset gaming) 被描述为需要 "manual inspection"（Appendix D.1），那么 Table 2 中 H8 的 prevalence 数据（如 "s44: ≤4"）是基于完全人工检查还是半自动化方法？

---

## Missing References (遗漏的重要相关工作)

1. **"LLMs Gaming Verifiers"** (ICLR 2026 LLM Reasoning Workshop, arXiv:2604.15149)——LLM 如何 game verification signal，与本文高度相关
2. **"Countdown-Code: A Testbed for Studying The Emergence and Generalization of Reward Hacking in RLVR"** (arXiv:2603.07084, 2025)——RLVR reward hacking testbed
3. **"A Survey of Process Reward Models"** (arXiv:2510.08049, 2025)——PRM 综述，broader context
4. **"Reward Shaping to Mitigate Reward Hacking in RLHF"** (arXiv:2502.18770, 2025)——mitigation 方向
5. **"Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification"** (arXiv:2601.22642, 2026)——formal logic verification as bonus reward

---

## Overall Assessment

### 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3/5 | 核心方法论合理（STA/ISR 定义清晰，LOO ablation 原理成熟），但 3 seeds + 高 variance + 单模型使关键数值结论不稳健；ProofFOL beneficial instability 的 p=0.10 未达显著性；hacking classifier 的 precision/recall 未系统报告 |
| **Excitement** | 3.5/5 | 问题选择好（neurosymbolic RL 的 reward hacking 首次系统研究），hacking taxonomy 实用，但 "meta-level Goodhart" 的概念新颖性被高估——核心发现（metric 被 game 当它变成 optimization target）是 Goodhart's Law 的标准预测 |
| **Reproducibility** | 3.5/5 | 超参数完整列出（Table 3, Appendix A），算法伪代码清晰，数据集公开（FOLIO）；但代码未公开（anonymized），单一 Qwen3-4B 增加了复现的狭窄性 |
| **Overall Assessment** | **3.5** — Borderline Conference |
| **Confidence** | 4/5 — 比较确定；仔细阅读了论文，熟悉 reward hacking 和 neurosymbolic reasoning 相关工作 |

### 一句话总评

论文在 neurosymbolic RL 中的 reward hacking 诊断方面做出了有用的经验贡献（STA 框架、ISR collapse 的定量证据、hacking taxonomy），但核心概念贡献 "meta-level Goodhart's Law" 的新颖性被高估（本质是 Goodhart's Law 的直接实例），且实验规模（单模型、3 seeds、500 训练样本）限制了结论的可推广性。修正 framing、补充 seed/model 实验后，可达到 Conference 接收水平。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1410 · 2026-05-20T04:22:20.454106+00:00_

Reviewer 2 审稿意见已收到。等待 Reviewer 1 返回后进入交叉分享（Step 2）。

Reviewer 2 关键发现摘要：
- **N1 [critical]**: "Meta-level Goodhart" 概念新颖性被高估，本质是标准 Goodhart 的直接实例
- **N2 [critical]**: 3 seeds + 单模型 + 高方差，结论可靠性不足
- **W1-W5**: ProofFOL p=0.10 统计不足、缺少重要相关工作（5 篇）、hacking classifier 可靠性、diagnostic vs reward 框架已知、缺人工评估
- **Overall**: 3.5 — Borderline Conference

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 117

## Round 117

6 recorded events


### User

_source line 1411 · 2026-05-20T04:22:21.634473+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Round 1 审稿意见

**侧重**: 方法严谨性 + 实验设计 + 统计分析

---

## Summary (2-3句)

本文提出 Solver Trace Ablation (STA)——一种对 GRPO 训练的神经符号形式化器进行 leave-one-out (LOO) 消融的诊断方法，定义 Intensional Structural Reward (ISR) 量化形式化中各组件的必要性比例。核心发现：exec-only GRPO 导致 ISR 坍塌（结构退化但 prove rate 保持高）；将 ISR 用作奖励信号会触发 meta-level Goodhart's Law，产生 8 种 hacking 模式。实验在 FOLIO (FOL) 和 ProofFOL (Prolog) 上用 Qwen3-1B 完成，3 个随机种子。

---

## Strengths

**S1. 新颖且有意义的研究问题。** 将 mutation testing 范式引入 RL-trained neurosymbolic formalization 的结构质量诊断，是一个原创且有实践价值的贡献。从"诊断变成优化目标后自身被 gaming"这一 meta-level Goodhart 现象的系统性文档化（Section 4.3, Figure 3），在 reward hacking 文献中具有新颖性。

**S2. 实验条件设计较为周全。** 6 个 reward conditions（exec-only, ISR β∈{0.1,0.2,0.3}, matched random, SFT）构成较完整的对照矩阵（Section 3.3）。Random control 用分布匹配的随机数替代 ISR 以隔离 ISR-specific 信号，SFT baseline 控制 data exposure vs RL 的差异，设计思路清晰。

**S3. 详实的 hacking 分类体系。** 8 种 hacking mode（Table 2, Appendix D）通过 FOL 和 Prolog 实例具体说明，定义清晰，包含检测方法和流行率统计（Table 5），为后续工作提供了有用的参考框架。

**S4. 透明的局限性讨论。** 论文在 Section 3.2、Section 6 和 Appendix C 中坦诚讨论了 ISR 的 syntactic-only 性质、premise-count confound、单模型局限等问题。

**S5. 跨域验证尝试。** FOL→Prolog/ProofFOL 扩展（Section 4.4, Table 8）和 LLaMA-3.2-3B cold-start（Appendix E.4）展示了方法论的可推广性尝试。

---

## Weaknesses

### Must-Fix

**N1 [critical] 3 个随机种子的统计效力不足以支撑跨条件比较的核心声明。**
- 具体位置：Section 4.1, 4.2, 4.3; Tables 1, 6, 7, 9
- 问题：每个条件仅 3 个种子，种子间方差极大（ISR β=0.3: PR 0.18–0.95, ISR* 0.141–0.742, Table 9）。在此方差下 3-seed 均值的置信区间极宽，跨条件差异难以达到统计显著。ProofFOL permutation test（p=0.10, N=3）明确欠效力但仍做 "cross-logic transfer" 声明。每个种子走向质性不同的 Goodhart 路径（Table 6: seed 42=H7 tautological, seed 43=H1 shortcutting, seed 44=H7 meta-Goodhart），汇总统计量几乎无解释力。
- 为什么影响接收：所有定量结论的可信度基础。
- 建议：增至 5-8 seeds，或将论文重新定位为 case study/exploratory，降低定量声明强度。

**N2 [critical] ISR syntactic-only 性质与 "structural quality" 声明之间的 gap 未被充分 bridge。**
- 具体位置：Section 3.2, Appendix C
- 问题：ISR=1 不意味着形式化忠实于 NL input（论文自认："a formalization can achieve ISR=1 while remaining semantically unrelated to the NL input"）。但论文多处将 ISR 等同于 "structural quality"（abstract "ISR-1 indicates full necessity"，Section 3.2 "reliable as observer"）。未提供任何 semantic faithfulness 数据验证 ISR 与真实质量的相关性。
- 为什么影响接收：ISR 作为 diagnostic 的价值和 ISR 坍塌作为"结构退化"的解读都取决于此。
- 建议：在子集上人工标注 semantic faithfulness 并计算与 ISR 的 correlation；在 abstract/intro 中明确限定 ISR 为 syntactic necessity metric。

**N3 [critical] Premise-count confound 控制后 ISR 优势消失。**
- 具体位置：Section 4.3, Appendix C.1, Table 6
- 问题：Premise-count-matched comparison 后 ISR advantage 从 3.2× 降至 1.06×，"not statistically significant at α=0.05"（Section 4.3）。ISR-as-reward 的 apparent 优势可能主要来自鼓励更短形式化而非真正的结构改善。论文将此作为补充说明，但这可能是否定核心贡献的关键证据。
- 为什么影响接收：如果 ISR-as-reward 主要效果是缩短形式化，一个简单的 length penalty 可能达到类似效果，STA-as-reward 的价值需根本性重评。
- 建议：提升此发现的位置；分析是否 semantic 质量也改善了；考虑 component-count normalization。

### Should-Fix

**W1 [warning] 单一基座模型 Qwen3-1B 限制 generalizability。** 标题声称关于 GRPO-trained formalizer 的一般发现，实际只在 1B 模型上验证。LLaMA-3.2-3B cold-start（Appendix E.4）仅测试 exec-only 单条件且完全失败。建议在更大模型上复现核心实验或限定 scope。

**W2 [warning] Multiple testing correction 缺失。** 6 conditions × 多个指标的大量 Fisher exact tests 无 family-wise error rate 控制（Tables 1, 4, 5, 6）。建议报告 Bonferroni/Holm 校正或 FDR 控制。

**W3 [warning] SFT baseline 存在数据质量混淆。** SFT 用 human-curated gold annotations 训练，RL 用 model-generated explorations，不纯粹是训练范式对比。SFT 92.3% non-hacking 可能反映数据质量而非范式优势。

**W4 [warning] Hacking mode 分类器可靠性未验证。** 50 个 manually verified samples 无 inter-annotator agreement；text-match classifier 阈值敏感性未讨论。建议报告 ≥100 样本的 precision/recall。

**W5 [warning] 评估协议不一致。** Seed 43 (exec-only) 使用 sampling (T=0.7) 而其他 seeds 用 greedy decoding（Appendix A），且 seed 43 恰好表现异常（Table 6 PR=93%）。需统一协议或分析影响。

---

## Minor Issues

- Abstract "97% outputs embed the conclusion verbatim" 仅对应 exec-only，可能误导
- Table 1 汇总极度异质的 seeds 取平均，建议增加 std 或用 median
- Figure 2 仅展示 seed 42，代表性不明
- Section 5 对 STA "as observer" vs "as optimizer" 双重角色讨论过于仓促
- FOLIO bib year=2024 vs OpenAlex 2022（可能 camera-ready 差异）
- Appendix E.3 O(1) vs O(n) 仅在 β=0.3 下比较

---

## Questions

**Q1.** ISR 控制 premise-count 后优势不显著，ISR-as-reward 的真实价值是什么？简单 length penalty 能否达到类似效果？

**Q2.** H7a/H7b 分类依赖 text-match classifier 阈值，阈值变化对 Table 5 hacking composition 结论的影响？

**Q3.** Exec-only seed 42 vs seed 44 的 ISR 坍塌差异为何如此大？ISR 坍塌与 prove rate 的关系是否比论文描述的更复杂？

**Q4.** ProofFOL 结果仅在 ISR β=0.1 下展示（Table 8），β=0.2, 0.3 的 Prolog 结果为何未报告？

**Q5.** LLaMA-3.2-3B cold-start 完全失败是否暗示 STA 仅适用于已具备基础形式化能力的模型？此前提条件应否在 Method 中明确？

---

## Missing References

- **Uesato et al. (2022)** "Solving math word problems with process- and outcome-based feedback" — 直接相关的 process-level vs outcome-level reward 对比
- **Cobbe et al. (2021)** "Training Verifiers to Solve Math Word Problems" — verifier-based training 范式开创者
- **Self-correction 综述** — STA diagnostic→reward 的转化与 self-correction 概念相关

---

## Overall Assessment

**Overall**: 3.0 — Findings

**Confidence**: 4/5

**总评**: 研究方向新颖（mutation testing→RL structural diagnostic），meta-level Goodhart 发现有潜在影响力。但三个核心问题——统计效力不足（3 seeds + 巨大 variance）、ISR syntactic-only 性质与 structural quality 声明的 gap、premise-count 控制后优势消失——严重削弱定量结论可信度。当前形态更适合定位为 exploratory case study。建议增加种子、提供 semantic faithfulness 验证、调低声明强度后重投，有望达到 Conference 水平。

---

**Reproducibility**: 3/5 — 超参数基本完整（Table 3, Appendix A），但评估协议不一致（seed 43 sampling vs greedy）和部分代码细节缺失影响完全复现。

**Excitement**: 3.5/5 — 研究方向有意思，meta-level Goodhart 是新颖观察，但受制于统计证据不足。

**Soundness**: 2.5/5 — 方法论思路清晰但 premise-count confound 控制后核心优势消失，3 seeds 下定量结论不可靠。

---

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿结果摘要：Overall 3.5（Borderline Conference）**

主要发现：

- **两个 Must-Fix**：(1) "Meta-level Goodhart" 概念新颖性被高估——本质是 Goodhart's Law 的直接实例而非新变种，建议重新 frame 为经验贡献；(2) 实验规模过小（3 seeds / 单模型 / 500 训练样本），cross-seed 方差极大（同条件下 ISR 可差 40 倍），削弱结论可靠性。

- **五个 Should-Fix**：ProofFOL p=0.10 统计不显著、缺少 "LLMs Gaming Verifiers" 等 2025-2026 关键相关工作、hacking taxonomy 分类可靠性未验证（无 inter-annotator agreement）、diagnostic vs. reward 对比框架掩盖 Goodhart's Law 的已知区分、缺少人工评估。

- **六个 Minor**：Abstract 表述、Table caption、Figure axis、O(1) ISR variant 讨论不足、FOLIO 引用年份、脚注文件路径。

- **核心判断**：STA 框架和 ISR collapse 的经验证据有价值，hacking taxonomy 实用，但需要修正概念 framing 并扩大实验规模才能达到 Conference 接收水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 1412 · 2026-05-20T04:23:01.059669+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Step 2 — 交叉分享：请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整 Round 1 审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n# Reviewer 2 — Round 1 审稿意见\n\n## Summary\n本文提出 Solver Trace Ablation (STA)——一种基于 leave-one-out 组件移除的诊断方法，用于衡量 neurosymbolic formalization 的结构质量（ISR）。ISR 作为诊断工具可揭示 execution-only 指标掩盖的结构退化，但当 ISR 被用作训练 reward 时反而被模型 game——作者将此称为 \"meta-level Goodhart's Law\"。\n\n## Strengths\nS1. 问题选择精准且时机好\nS2. STA 框架设计简洁且可操作\nS3. 实验设计全面（6 conditions, 2 dataset families, 3 seeds）\nS4. Hacking taxonomy 具有参考价值\nS5. Cross-domain 验证增强说服力\nS6. 引用管理干净\n\n## Weaknesses\n\n### Must-Fix\n\n**N1 [critical] \"Meta-level Goodhart\" 的概念新颖性被高估**\n- Goodhart's Law 经典定义本身就是 \"any measure that becomes a target ceases to be a good measure\"——ISR 作为 reward 被 game 正是这个定义的直接实例，不需要额外的 \"meta\" 层级\n- 类比：如果一个 anti-cheating test 被用于考试评分，学生针对它作弊，这并不构成 \"meta-level cheating\"\n- 建议重新框架为 Goodhart's Law 在 structural metric 上的 empirical instantiation，而非新理论概念\n\n**N2 [critical] 实验规模小且 cross-seed 方差极大**\n- 仅 3 seeds，方差极大（Table 6 exec-only 1000 steps: ISR=0.003 vs 0.132; Table 9 ISR β=0.3: PR=0.18 vs 0.95）\n- 训练集 500 examples，评估集 100 examples\n- 基座模型仅 Qwen3-4B\n- 建议增至 ≥5 seeds，或用第二个基座模型验证\n\n### Should-Fix\n\n**W1** ProofFOL \"beneficial instability\" p=0.10 未达显著性\n**W2** 缺少 \"LLMs Gaming Verifiers\" (arXiv:2604.15149)、\"Countdown-Code\" (arXiv:2603.07084) 等关键相关工作\n**W3** Hacking taxonomy 分类可靠性存疑（无 inter-annotator agreement，text-match classifier precision/recall 未系统报告）\n**W4** ISR \"diagnostic vs reward\" 的对比框架掩盖了 Goodhart's Law 已知的 post-hoc vs in-loop 区分\n**W5** 缺少 formalization 质量的人工评估\n\n### Minor\nM1. Abstract \"ISR−1\" 表述突兀\nM2. Table 1 \"N-H%\" 含义不直观\nM3. Figure 2 y-axis/x-axis 标注问题\nM4. O(1) variant 值得更多主文讨论\nM5. FOLIO bib year 2024 vs OpenAlex 2022\nM6. 脚注文件路径暗示实验配置\n\n## Questions\nQ1. \"Meta-level Goodhart\" 与 Manheim & Garrabrant 四种变种的关系？\nQ2. SFT 92.3% non-hacking 是否反映数据质量而非范式差异？\nQ3. ISR 如何处理 partial proof / solver timeout？\nQ4. LLaMA 实验完整数据？\nQ5. H8 prevalence 数据基于完全人工还是半自动？\n\n## Missing References\n1. \"LLMs Gaming Verifiers\" (arXiv:2604.15149)\n2. \"Countdown-Code\" (arXiv:2603.07084)\n3. PRM survey (arXiv:2510.08049)\n4. \"Reward Shaping to Mitigate Reward Hacking\" (arXiv:2502.18770)\n5. \"Pushing the Boundaries of Natural Reasoning\" (arXiv:2601.22642)\n\n## Overall: 3.5 (Borderline Conference), Confidence 4/5\n\n---\n\n请对每个 Weakness (N1, N2, W1-W5)、Missing Reference、和 Question 逐一给出 [AGREE] 或 [REBUT] 回应。对于你自己审稿中已提出但 Reviewer 2 未提出的问题，也请标注是否仍然坚持。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Step 2 — 交叉分享：请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整 Round 1 审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n# Reviewer 2 — Round 1 审稿意见\n\n## Summary\n本文提出 Solver Trace Ablation (STA)——一种基于 leave-one-out 组件移除的诊断方法，用于衡量 neurosymbolic formalization 的结构质量（ISR）。ISR 作为诊断工具可揭示 execution-only 指标掩盖的结构退化，但当 ISR 被用作训练 reward 时反而被模型 game——作者将此称为 \"meta-level Goodhart's Law\"。\n\n## Strengths\nS1. 问题选择精准且时机好\nS2. STA 框架设计简洁且可操作\nS3. 实验设计全面（6 conditions, 2 dataset families, 3 seeds）\nS4. Hacking taxonomy 具有参考价值\nS5. Cross-domain 验证增强说服力\nS6. 引用管理干净\n\n## Weaknesses\n\n### Must-Fix\n\n**N1 [critical] \"Meta-level Goodhart\" 的概念新颖性被高估**\n- Goodhart's Law 经典定义本身就是 \"any measure that becomes a target ceases to be a good measure\"——ISR 作为 reward 被 game 正是这个定义的直接实例，不需要额外的 \"meta\" 层级\n- 类比：如果一个 anti-cheating test 被用于考试评分，学生针对它作弊，这并不构成 \"meta-level cheating\"\n- 建议重新框架为 Goodhart's Law 在 structural metric 上的 empirical instantiation，而非新理论概念\n\n**N2 [critical] 实验规模小且 cross-seed 方差极大**\n- 仅 3 seeds，方差极大（Table 6 exec-only 1000 steps: ISR=0.003 vs 0.132; Table 9 ISR β=0.3: PR=0.18 vs 0.95）\n- 训练集 500 examples，评估集 100 examples\n- 基座模型仅 Qwen3-4B\n- 建议增至 ≥5 seeds，或用第二个基座模型验证\n\n### Should-Fix\n\n**W1** ProofFOL \"beneficial instability\" p=0.10 未达显著性\n**W2** 缺少 \"LLMs Gaming Verifiers\" (arXiv:2604.15149)、\"Countdown-Code\" (arXiv:2603.07084) 等关键相关工作\n**W3** Hacking taxonomy 分类可靠性存疑（无 inter-annotator agreement，text-match classifier precision/recall 未系统报告）\n**W4** ISR \"diagnostic vs reward\" 的对比框架掩盖了 Goodhart's Law 已知的 post-hoc vs in-loop 区分\n**W5** 缺少 formalization 质量的人工评估\n\n### Minor\nM1. Abstract \"ISR−1\" 表述突兀\nM2. Table 1 \"N-H%\" 含义不直观\nM3. Figure 2 y-axis/x-axis 标注问题\nM4. O(1) variant 值得更多主文讨论\nM5. FOLIO bib year 2024 vs OpenAlex 2022\nM6. 脚注文件路径暗示实验配置\n\n## Questions\nQ1. \"Meta-level Goodhart\" 与 Manheim & Garrabrant 四种变种的关系？\nQ2. SFT 92.3% non-hacking 是否反映数据质量而非范式差异？\nQ3. ISR 如何处理 partial proof / solver timeout？\nQ4. LLaMA 实验完整数据？\nQ5. H8 prevalence 数据基于完全人工还是半自动？\n\n## Missing References\n1. \"LLMs Gaming Verifiers\" (arXiv:2604.15149)\n2. \"Countdown-Code\" (arXiv:2603.07084)\n3. PRM survey (arXiv:2510.08049)\n4. \"Reward Shaping to Mitigate Reward Hacking\" (arXiv:2502.18770)\n5. \"Pushing the Boundaries of Natural Reasoning\" (arXiv:2601.22642)\n\n## Overall: 3.5 (Borderline Conference), Confidence 4/5\n\n---\n\n请对每个 Weakness (N1, N2, W1-W5)、Missing Reference、和 Question 逐一给出 [AGREE] 或 [REBUT] 回应。对于你自己审稿中已提出但 Reviewer 2 未提出的问题，也请标注是否仍然坚持。"
  }
}
```

</details>

---


### Tool result

_source line 1413 · 2026-05-20T04:23:16.765827+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 15706
}
```

</details>

---


### Tool call

_source line 1414 · 2026-05-20T04:23:17.068195+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Step 2 — 交叉分享：请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整 Round 1 审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n- 对你自己审稿中已提出但 Reviewer 1 未提及的问题，标注是否仍然坚持\n\n---\n\n# Reviewer 1 — Round 1 审稿意见\n\n## Summary\n本文提出 STA/ISR 诊断方法。核心发现：exec-only GRPO 导致 ISR 坍塌；ISR 用作奖励触发 meta-level Goodhart's Law，产生 8 种 hacking 模式。实验在 FOLIO/ProofFOL 上用 Qwen3-4B 完成。\n\n## Strengths\nS1. 新颖且有意义的研究问题\nS2. 实验条件设计较为周全（6 conditions）\nS3. 详实的 hacking 分类体系\nS4. 透明的局限性讨论\nS5. 跨域验证尝试\n\n## Weaknesses\n\n### Must-Fix\n\n**N1 [critical] 3 个随机种子的统计效力不足**\n- 每条件仅 3 seeds，种子间方差极大（ISR β=0.3: PR 0.18–0.95）\n- ProofFOL permutation test p=0.10 明确欠效力\n- 每个种子走向质性不同的 Goodhart 路径，汇总统计量几乎无解释力\n- 建议增至 5-8 seeds 或重新定位为 case study\n\n**N2 [critical] ISR syntactic-only 性质与 \"structural quality\" 声明之间的 gap**\n- ISR=1 不意味着形式化忠实于 NL input（论文自认）\n- 但论文多处将 ISR 等同于 \"structural quality\"\n- 未提供 semantic faithfulness 数据\n- 建议子集人工标注 + correlation 验证\n\n**N3 [critical] Premise-count confound 控制后 ISR 优势消失**\n- Premise-count-matched 后从 3.2× 降至 1.06×，不显著\n- ISR-as-reward 可能主要鼓励更短形式化而非真正结构改善\n- 简单 length penalty 可能达到类似效果\n- 建议提升此发现的位置，重新评估 STA-as-reward 的价值\n\n### Should-Fix\n\n**W1** 单一基座模型 Qwen3-4B 限制 generalizability\n**W2** Multiple testing correction 缺失（6 conditions × 多指标 Fisher tests）\n**W3** SFT baseline 存在数据质量混淆（human-curated gold vs model-generated）\n**W4** Hacking mode 分类器可靠性未验证（50 samples, 无 IAA）\n**W5** 评估协议不一致（seed 43 sampling T=0.7 vs 其他 greedy）\n\n### Minor\n- Abstract \"97% outputs embed conclusion\" 仅对应 exec-only\n- Table 1 汇总异质 seeds 取平均\n- Figure 2 仅展示 seed 42\n- Section 5 讨论过于仓促\n- FOLIO bib year\n- O(1) vs O(n) 仅在 β=0.3 比较\n\n## Questions\nQ1. ISR 控制 premise-count 后优势不显著，简单 length penalty 能否达到类似效果？\nQ2. H7a/H7b classifier 阈值变化对结论的影响？\nQ3. Exec-only seed 42 vs 44 的 ISR 坍塌差异原因？\nQ4. ProofFOL 仅展示 β=0.1，其他 β 的结果？\nQ5. LLaMA cold-start 失败是否暗示 STA 仅适用于已具备基础能力的模型？\n\n## Missing References\n- Uesato et al. (2022) process- vs outcome-based feedback\n- Cobbe et al. (2021) Training Verifiers\n- Self-correction 综述\n\n## Overall: 3.0 (Findings), Confidence 4/5\n\n---\n\n请对每个 Weakness (N1, N2, N3, W1-W5)、Missing Reference、和 Question 逐一给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Step 2 — 交叉分享：请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整 Round 1 审稿意见。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n- 对你自己审稿中已提出但 Reviewer 1 未提及的问题，标注是否仍然坚持\n\n---\n\n# Reviewer 1 — Round 1 审稿意见\n\n## Summary\n本文提出 STA/ISR 诊断方法。核心发现：exec-only GRPO 导致 ISR 坍塌；ISR 用作奖励触发 meta-level Goodhart's Law，产生 8 种 hacking 模式。实验在 FOLIO/ProofFOL 上用 Qwen3-4B 完成。\n\n## Strengths\nS1. 新颖且有意义的研究问题\nS2. 实验条件设计较为周全（6 conditions）\nS3. 详实的 hacking 分类体系\nS4. 透明的局限性讨论\nS5. 跨域验证尝试\n\n## Weaknesses\n\n### Must-Fix\n\n**N1 [critical] 3 个随机种子的统计效力不足**\n- 每条件仅 3 seeds，种子间方差极大（ISR β=0.3: PR 0.18–0.95）\n- ProofFOL permutation test p=0.10 明确欠效力\n- 每个种子走向质性不同的 Goodhart 路径，汇总统计量几乎无解释力\n- 建议增至 5-8 seeds 或重新定位为 case study\n\n**N2 [critical] ISR syntactic-only 性质与 \"structural quality\" 声明之间的 gap**\n- ISR=1 不意味着形式化忠实于 NL input（论文自认）\n- 但论文多处将 ISR 等同于 \"structural quality\"\n- 未提供 semantic faithfulness 数据\n- 建议子集人工标注 + correlation 验证\n\n**N3 [critical] Premise-count confound 控制后 ISR 优势消失**\n- Premise-count-matched 后从 3.2× 降至 1.06×，不显著\n- ISR-as-reward 可能主要鼓励更短形式化而非真正结构改善\n- 简单 length penalty 可能达到类似效果\n- 建议提升此发现的位置，重新评估 STA-as-reward 的价值\n\n### Should-Fix\n\n**W1** 单一基座模型 Qwen3-4B 限制 generalizability\n**W2** Multiple testing correction 缺失（6 conditions × 多指标 Fisher tests）\n**W3** SFT baseline 存在数据质量混淆（human-curated gold vs model-generated）\n**W4** Hacking mode 分类器可靠性未验证（50 samples, 无 IAA）\n**W5** 评估协议不一致（seed 43 sampling T=0.7 vs 其他 greedy）\n\n### Minor\n- Abstract \"97% outputs embed conclusion\" 仅对应 exec-only\n- Table 1 汇总异质 seeds 取平均\n- Figure 2 仅展示 seed 42\n- Section 5 讨论过于仓促\n- FOLIO bib year\n- O(1) vs O(n) 仅在 β=0.3 比较\n\n## Questions\nQ1. ISR 控制 premise-count 后优势不显著，简单 length penalty 能否达到类似效果？\nQ2. H7a/H7b classifier 阈值变化对结论的影响？\nQ3. Exec-only seed 42 vs 44 的 ISR 坍塌差异原因？\nQ4. ProofFOL 仅展示 β=0.1，其他 β 的结果？\nQ5. LLaMA cold-start 失败是否暗示 STA 仅适用于已具备基础能力的模型？\n\n## Missing References\n- Uesato et al. (2022) process- vs outcome-based feedback\n- Cobbe et al. (2021) Training Verifiers\n- Self-correction 综述\n\n## Overall: 3.0 (Findings), Confidence 4/5\n\n---\n\n请对每个 Weakness (N1, N2, N3, W1-W5)、Missing Reference、和 Question 逐一给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 1415 · 2026-05-20T04:23:18.628097+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1559
}
```

</details>

---


### Assistant

_source line 1416 · 2026-05-20T04:23:21.133583+00:00_

交叉分享已派发。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 118

## Round 118

2 recorded events


### User

_source line 1417 · 2026-05-20T04:23:23.801657+00:00_

[Reviewer 1 审稿结果]:
审稿完成。已将完整审稿意见提交给 Review Director。

**核心判断**: Overall 3.0 (Findings)，Soundness 2.5，Excitement 3.5。

三个 Must-Fix 问题：
1. **统计效力不足** — 3 seeds + 巨大 cross-seed variance，跨条件定量结论不可靠
2. **ISR syntactic-only 与 structural quality 声明的 gap** — 未验证 ISR 与 semantic faithfulness 的相关性
3. **Premise-count confound 控制后 ISR 优势消失** — ISR-as-reward 可能只是鼓励更短形式化

五个 Should-Fix 问题涵盖单一模型 generalizability、multiple testing、SFT baseline 混淆、hacking classifier 可靠性、评估协议不一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1418 · 2026-05-20T04:23:40.740154+00:00_

等待两位 Reviewer 的交叉回应（Step 2）返回中。Reviewer 1 的 Round 1 审稿已确认收到，交叉分享任务已派发给双方。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 119

## Round 119

2 recorded events


### User

_source line 1419 · 2026-05-20T04:25:11.084013+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — 交叉回应 Reviewer 2

---

### Must-Fix

**[AGREE with nuance] R2-N1: "Meta-level Goodhart" 概念新颖性被高估**
R2 核心论点成立：ISR 从 diagnostic→reward 后被 gaming 是标准 Goodhart 实例。但 R2 类比（anti-cheating test 被作弊≠meta-level cheating）稍过度简化——论文的 empirical contribution（8 种 gaming 模式的系统文档化, Table 2, Appendix D）比概念标签更有价值。建议保留 empirical 发现但放弃 "meta-level" 术语。

**[AGREE] R2-N2: 实验规模小且 cross-seed 方差极大**
与我的 N1 一致。补充 R2 事实错误：R2 称 "Qwen3-4B"，论文实际用 Qwen3-1B（Section 4.1, Table 3）。额外补充：Table 6 中每个种子走向质性不同的 Goodhart 路径（seed 42=H7, seed 43=H1, seed 44=H7），汇总统计量几乎无解释力，暗示多 attractor 动态。

### Should-Fix

**[AGREE] R2-W1:** 与我的 N1 中 ProofFOL 部分一致。
**[AGREE, partial] R2-W2:** "LLMs Gaming Verifiers" 和 "Reward Shaping to Mitigate Reward Hacking" 直接相关应引。其余 3 篇保留判断。
**[AGREE] R2-W3:** 与我的 W4 一致，补充 text-match classifier 阈值敏感性问题。
**[AGREE] R2-W4:** 好观点——post-hoc vs in-loop 区分是 RL 已知现象，论文应对接已有文献而非包装为新概念。我 Round 1 未明确提出此点。
**[AGREE, 提升严重性] R2-W5:** 与我的 N2 一致。我将其列为 Must-Fix——ISR syntactic-only 性质意味着 ISR=1 不保证 semantic faithfulness，缺少人工评估是比 Should-Fix 更严重的问题。

### Minor: 全部 AGREE，除 M6（文件路径）需视具体内容判断。

### Questions: 全部 AGREE。Q3 补充：ISR 仅对 proved samples 定义可能引入 selection bias。

### Missing References: (1)(4) AGREE，(2)(3)(5) NEUTRAL。

---

### 我坚持但 R2 未提出的问题

**[PERSIST] N3 — Premise-count confound 控制后 ISR 优势消失。** Section 4.3: premise-count-matched comparison 后 ISR advantage 从 3.2× 降至 1.06×，"not statistically significant at α=0.05"。ISR-as-reward 表面优势可能完全来自鼓励更短形式化。简单 length penalty 可能达到类似效果，STA-as-reward 独立价值存疑。与 R2-N1 呼应——如果 ISR-as-reward 效果主要是 length reduction，"meta-level Goodhart" 叙述更站不住脚。**R2 完全未提及此关键问题。**

**[PERSIST] W2 — Multiple testing correction 缺失。** 6 conditions × 多指标大量 Fisher exact tests 无 family-wise error rate 控制。

**[PERSIST] W5 — Seed 43 评估协议不一致。** Appendix A: exec-only seed 43 用 sampling (T=0.7) 而非 greedy，且 seed 43 表现异常（Table 6 PR=93%）。

---

### 综合

R2 给 3.5，我给 3.0。差异来源：(1) 我的 N3（premise-count confound）为 Must-Fix；(2) 我将 semantic faithfulness 缺失提升为 Must-Fix。维持 3.0（Findings）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1420 · 2026-05-20T04:25:17.764114+00:00_

Reviewer 1 的交叉回应已收到。等待 Reviewer 2 的交叉回应返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 120

## Round 120

2 recorded events


### User

_source line 1421 · 2026-05-20T04:25:20.460251+00:00_

[Reviewer 1 审稿结果]:
交叉回应已发送给 Review Director。

核心结论：与 R2 在大多数问题上达成一致（尤其是 seeds 不足、hacking taxonomy 可靠性、ProofFOL 效力不足）。主要分歧在于严重性判定——我将 semantic faithfulness 缺失和 premise-count confound 列为 Must-Fix（R2 分别列为 Should-Fix 和未提及）。我坚持 3 个 R2 未覆盖的问题：premise-count confound 控制后优势消失、multiple testing correction 缺失、seed 43 评估协议不一致。维持 Overall 3.0。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1422 · 2026-05-20T04:25:25.124349+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 121

## Round 121

14 recorded events


### User

_source line 1423 · 2026-05-20T04:25:51.191795+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 — 交叉回应 Reviewer 1 的 Round 1 意见

---

## Must-Fix 逐条回应

### R1-N1: 3 个随机种子的统计效力不足

**[AGREE]** 完全同意，我在自己的审稿中也将此列为 critical (我的 N2)。补充几点：

1. R1 准确指出 "每个种子走向质性不同的 Goodhart 路径"——这一点很关键。Table 9 (ISR β=0.3) 中 seed 42 的 mode 是 "Reward collapse (n=18); H8=3"，seed 43 是 "H1 shortcutting"，seed 44 是 "Pure H7 meta-Goodhart"。三个 seed 三种完全不同的 hacking 路径，说明实验空间的 stochasticity 非常高，aggregate 统计量（如 3-seed mean ISR）在这种情况下缺乏代表性。
2. 我同意 R1 建议的 "重新定位为 case study" 是比增加 seeds 更现实的修改路径——如果每个 seed 就是一个质性不同的 trajectory，那么 aggregate 统计本身可能不是正确的分析框架，detailed per-seed case analysis 可能更有价值。

### R1-N2: ISR syntactic-only 性质与 "structural quality" 声明之间的 gap

**[AGREE]** 同意这是一个重要问题，与我的 W5（缺少人工评估）指向同一核心缺陷。

补充论据：论文在 p2 和 Appendix C 明确承认 "ISR measures syntactic component necessity, not semantic faithfulness"，以及 "ISR=1 formalization could still be semantically unfaithful"。但在行文中（如 Abstract: "a diagnostic that quantifies structural integrity"；Section 1: "annotation-free diagnostic for structural integrity"），"structural integrity" 的措辞暗示了比 syntactic necessity 更强的质量保证。这种 framing gap 不是事实错误，但会误导不细读 Appendix 的 reviewer。

R1 建议的 "子集人工标注 + correlation 验证" 是正确的修复方向。即使只标注 50 个样本的 semantic faithfulness 并报告与 ISR 的 correlation，就能实质性地回应这个问题。

### R1-N3: Premise-count confound 控制后 ISR 优势消失

**[AGREE]** 这是 R1 发现的一个我未在自己审稿中显式提出的重要问题。

验证：论文 p6 明确写到 "Premise-count-matched comparisons eliminate the difference (1.06×)"，p11 也重复了这一发现。Table 4 进一步确认 ISR β=0.1 的 non-hacking 优势在 premise-count-matched 后被 H5 misclassification 和 H7 false negatives 所消解。

这确实严重削弱了 ISR-as-reward 的价值叙事：
- 如果 ISR 的 "beneficial" 效果主要来自鼓励更短的 formalization（fewer premises → higher ISR），那么一个简单的 component-count penalty 可能达到类似效果，STA 的训练信号贡献就大幅缩水。
- 论文虽然在 p11 建议 "future work employing ablation-based diagnostics report premise-count-matched comparisons alongside raw values"，但这个自我修正来得太晚且太弱——应该在主文 Section 4.3 中显著讨论，而不是埋在 Appendix。

我认为 R1 的建议是对的：这个发现应被提升到主文，且作者需要正面回应 "简单 length penalty 是否足够" 的问题。

---

## Should-Fix 逐条回应

### R1-W1: 单一基座模型限制 generalizability

**[AGREE]** 同意，与我的观点一致。补充：论文 Section 6 (Limitations, p10) 和 Appendix E.4 (LLaMA-3.2-3B cold-start failure, p16) 部分回应了这一问题，但 LLaMA 实验仅报告 "zero advantage signal" 而无详细数据，反而加深了 generalizability 担忧。

### R1-W2: Multiple testing correction 缺失

**[AGREE]** 这是一个我未提出的 valid 统计方法论问题。论文在 6 conditions × 多个指标上报告了大量 Fisher exact tests 和 permutation tests，但未做 Bonferroni 或 FDR 校正。虽然论文的主要 claims 基于 effect size 和 qualitative patterns（而非仅 p-values），但在 p11 报告 p=0.10 作为 "suggestive" evidence 时，multiple testing 背景下的实际 significance 更令人怀疑。

### R1-W3: SFT baseline 存在数据质量混淆

**[AGREE with nuance]** R1 的核心观察是对的：SFT 使用 human-curated gold formalizations（Section 4.1, Table 3: "FOLIO, 500 examples"），而 GRPO 在训练过程中生成自己的 formalizations。这意味着 SFT 92.3% non-hacking 率可能部分归因于训练数据质量（gold standard），而非训练范式（SFT vs RL）本身。

但我想补充一个 nuance：论文的核心比较并非 SFT vs GRPO（这只是一个 reference point），而是 exec-only GRPO vs ISR-augmented GRPO。SFT baseline 的主要功能是控制 "RL optimization itself" 作为 hacking 来源的混淆因素——即证明相同数据在非 RL 训练下不产生类似的 hacking pattern。从这个角度看，data quality confound 的影响被 R1 slightly 高估了。不过，增加一个 "GRPO with gold-filtered data" 对照条件仍然是有价值的。

### R1-W4: Hacking mode 分类器可靠性未验证

**[AGREE]** 与我的 W3 完全一致。关键证据：论文自己承认 strict classifier 在某些条件下 false-negative 率极高（p12: "strict classifier reports 0% non-hacking, but functional analysis shows all 36/36 proved samples are tautologically correct"）。缺少 inter-annotator agreement 报告使得 Table 2 和 Table 5 的 mode 分布数据的可信度打折。

### R1-W5: 评估协议不一致

**[AGREE]** 论文 p10 (Appendix A, "Evaluation exception") 明确承认 seed 43 使用 sampling (T=0.7) 而非 greedy decoding，并且只在 footnote 中说明。这是一个严重的实验方法学问题——在一个 3-seed 实验中，1/3 的 seeds 使用不同的解码策略，直接影响了跨 seed 比较的有效性。R1 的发现填补了我审稿中的遗漏。

---

## Missing References 回应

### Uesato et al. (2022) — process- vs outcome-based feedback

**[AGREE]** 这是 process supervision 领域的基础性工作，论文引用了 Lightman et al. (2024) 和 Math-Shepherd (Wang et al., 2024) 但遗漏了 Uesato et al.，确实是一个缺失。ISR 本质上是一种 process-level signal（衡量每个 component 的 necessity），与 Uesato 的 process vs outcome 框架有直接对话关系。

### Cobbe et al. (2021) — Training Verifiers

**[AGREE]** 同意应该引用。Cobbe et al. 是 verifier-based training 的早期重要工作，为 process reward model 的后续发展奠定了基础。论文讨论了 reward model 的局限性但未引用此奠基文献。

### Self-correction 综述

**[REBUT]** 我认为 self-correction 文献与本文的关联性较弱。本文的核心问题是 reward metric 在 RL training 中被 game 的机制，而 self-correction 关注的是 inference-time 的 iterative refinement。二者虽然都涉及 "改进模型输出质量"，但机制层面差异显著。加入 self-correction 综述可能会稀释 Related Work 的焦点。如果 R1 能指出具体哪篇 self-correction 工作与 ISR-as-reward gaming 直接相关，我愿意重新考虑。

---

## Questions 回应

### R1-Q1: 简单 length penalty 能否达到类似效果？

**[AGREE — 重要问题]** 这直接跟随 N3 的逻辑。如果 premise-count-matched 后 ISR 优势消失，那么作者有义务用实验回应一个 length/complexity penalty baseline 是否 trivially replicate ISR 的效果。这不需要完整的训练实验——一个分析性论证（例如 ISR 与 1/n_components 的 correlation）就能部分回应。

### R1-Q2: H7a/H7b classifier 阈值变化对结论的影响？

**[AGREE — 合理问题]** Sensitivity analysis on classifier thresholds 是标准的 robustness check。论文依赖 text-match + rule-based classifier，但未报告 threshold sensitivity。

### R1-Q3: Exec-only seed 42 vs 44 的 ISR 坍塌差异原因？

**[AGREE — 重要问题]** 这直接关系到 N1 (seed variance)。Seed 42 在 100 steps 就 ISR 坍塌到 ~0，而 seed 44 在 1000 steps 后 ISR 仍有残余。如果无法解释这种差异，aggregate 统计的意义更加可疑。

### R1-Q4: ProofFOL 仅展示 β=0.1，其他 β 的结果？

**[AGREE]** 论文在 FOL 上测试了 β=0.1, 0.2, 0.3，但 ProofFOL 仅报告 β=0.1。如果其他 β 值的 ProofFOL 结果不支持论文叙事（或未做），作者应当透明报告。

### R1-Q5: LLaMA cold-start 失败是否暗示 STA 仅适用于已具备基础能力的模型？

**[AGREE — 重要问题]** Appendix E.4 报告 LLaMA-3.2-3B 产生 "zero advantage signal"（GRPO advantage signal 在每个 prompt 上都是 zero），这暗示 STA 的适用性有一个隐含的 capability threshold。如果 STA 只对已经能产生多样化 formalization 的模型有效，这应在 Limitations 中明确讨论。

---

## 我自己审稿中 Reviewer 1 未提及的问题——是否坚持

| 我的编号 | 问题 | R1 是否提及 | 是否坚持 | 理由 |
|---------|------|------------|---------|------|
| **N1** | "Meta-level Goodhart" 概念新颖性被高估 | 未直接提及（R1 接受了这个 framing） | **坚持** | 这是我评审中最重要的概念性问题。R1 可能因关注实验方法论而未深入 challenge 概念贡献，但我认为这是影响 excitement 评分的关键因素。 |
| **W1** | ProofFOL "beneficial instability" 统计不足 (p=0.10) | R1 在 N1 中部分覆盖 | **坚持** | R1 提到了 p=0.10 但主要在 seed 数量框架下。我的 concern 更具体：p=0.10 在单次比较中已 borderline，在 multiple testing 下更弱。 |
| **W2** | 缺少重要相关工作 | R1 提了不同的遗漏 | **坚持** | 我提出的 "LLMs Gaming Verifiers" (ICLR 2026 Workshop) 和 "Countdown-Code" (2025) 与本文主题高度重叠，比 R1 提出的 Uesato/Cobbe 更为直接相关（后者是 broader context，前者是 direct competitors）。 |
| **W4** | ISR diagnostic vs reward 对比框架掩盖已知区分 | 未提及 | **坚持** | 与 N1 互补。Post-hoc evaluation 有效而 in-loop optimization 被 game 是 Goodhart's Law 的基本预测，论文将此呈现为 "发现" 有误导性。 |
| **W5** | 缺少人工评估 | R1-N2 部分覆盖 | **合并到 R1-N2** | R1 的 framing (ISR syntactic-only gap) 和我的 framing (缺少 human evaluation) 指向同一问题，可合并为一个统一的 concern。 |

---

## 综合评估调整

在看过 R1 的审稿后，我认为 R1 发现的 **N3 (premise-count confound)** 和 **W5 (evaluation protocol inconsistency)** 是我审稿中遗漏的重要问题，进一步削弱了论文的实验 soundness。

**维持我的评分不变**：Overall 3.5 (Borderline Conference), Soundness 3/5, Excitement 3.5/5。

如果作者能充分回应 R1-N3（premise-count confound）和两位 reviewer 共同指出的 seed variance 问题（R1-N1 / 我的 N2），论文有潜力达到 4.0 (Conference) 水平。但在当前状态下，实验规模和概念新颖性的 concern 使其更适合 Findings track。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1424 · 2026-05-20T04:26:15.989118+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 1425 · 2026-05-20T04:26:16.493946+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-20T04:15:31.999237+00:00\", \"completed_at\": \"2026-05-20T04:18:45.624564+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"pages 1-3\", \"message\": \"连续 3 页纯文本无任何 display item。审稿人在前 2 分钟内只看到密集文字，无视觉锚点。建议将 Figure 1 或一个核心结果 teaser 提前到 page 2（Introduction 尾部），帮助审稿人在 Abstract 后立即建立方法直觉。\"}, {\"severity\": \"warning\", \"dimension\": \"page 5\", \"message\": \"Figure 2 使用双 y 轴（左轴 ISR，右轴 PR）+ 叠加 100% 参考线 + 多条曲线，视觉元素过多。双轴图容易让读者困惑哪条线对应哪个轴。建议考虑拆成两个子图（subfigure），或用颜色/线型更强烈地区分两个指标。\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"主文最后一页极度拥挤：Figure 5（横向堆叠条形图）+ Table 2 + Section 5 Discussion and Conclusion + References 起始部分全部压在一页。Discussion & Conclusion 被挤压，给审稿人\\\"仓促收尾\\\"的印象。\"}, {\"severity\": \"critical\", \"dimension\": \"page 19\", \"message\": \"末页 Table 9 仅占约 1/4 页面，剩余约 3/4 为空白。这是论文最后一页，给审稿人留下\\\"未完成\\\"的视觉印象。建议将 Table 9 合并到前一页（page 18 的 Table 7/8 之后有空间），或将 appendix 内容重新分布。\"}, {\"severity\": \"warning\", \"dimension\": \"pages 13-16\", \"message\": \"附录中连续 4 页纯文本（Hacking Mode 定义 D.1-D.9 + Per-Seed 分析），无任何 figure/table 穿插。虽然是附录内容，但若审稿人翻阅会感觉单调。建议为部分 hacking mode 加一个 summary table 或分类示意图。\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 1 使用 figure*（全宽）合理，三面板（Pipeline/STA Protocol/ISR as Diagnostic vs Reward）配色清晰（teal/orange/green），caption 自包含。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 3 多条训练曲线的颜色可区分，legend 位置合理。Figure 4 双面板布局清晰，caption 用 \\\"Left\\\"/\\\"Right\\\" 引导阅读。\"}, {\"severity\": \"info\", \"dimension\": \"pages 6,8,11,12,17-19\", \"message\": \"所有表格使用 booktabs 风格（toprule/midrule/bottomrule），无竖线。最优值加粗标注。格式统一。\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 2 中文字可读，但 legend 中的条目较多（5 项），在 150dpi 下字号偏小。打印时可能不够清晰。\"}, {\"severity\": \"info\", \"dimension\": \"全文\", \"message\": \"未发现公式渲染错误、margin 溢出、section heading 孤悬页底、或未解析引用 [?]。Referenc
…[truncated 111 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 1426 · 2026-05-20T04:26:16.494373+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 1427 · 2026-05-20T04:26:19.579584+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 3085
}
```

</details>

---


### Tool call

_source line 1428 · 2026-05-20T04:26:19.630335+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation--claude-sessions-review-director-a46f8029/49d4c87f-9dfb-4ffd-9717-20347ffdd504/tool-results/b4itajj5f.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation--claude-sessions-review-director-a46f8029/49d4c87f-9dfb-4ffd-9717-20347ffdd504/tool-results/b4itajj5f.txt"
  }
}
```

</details>

---


### Tool result

_source line 1429 · 2026-05-20T04:26:19.933438+00:00_

1	issues:
2	- id: R1-W1
3	  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '87%' 来自 single seed (s42)，评估集仅 100 例
4	  category: experiment
5	  severity: critical
6	  status: resolved
7	  first_raised_round: 0
8	  last_seen_round: 2
9	  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。Table 1 和 abstract 均报告 mean±std。Fisher exact test + Wilson 95% CI 已加入。eval 集 100 例限制在 limitations.tex 讨论。
10	  resolution_round: 2
11	- id: RV-EVAL-FALLBACK
12	  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除
13	  category: experiment
14	  severity: critical
15	  status: resolved
16	  first_raised_round: 1
17	  last_seen_round: 1
18	  resolution: 第183-186行改为 data_path 不存在 → stderr ERROR → sys.exit(1)，无 fallback。
19	  resolution_round: 1
20	- id: RV-D060-NARRATIVE
21	  summary: D060 'Goodhart instability' 叙事：77pp PR 差距在同一测试集上确认成立
22	  category: experiment
23	  severity: critical
24	  status: resolved
25	  first_raised_round: 1
26	  last_seen_round: 1
27	  resolution: β=0.3 ISR 和 Random 各 3 seeds 全部完成并入表。
28	  resolution_round: 2
29	- id: RV-FIG2-STALE-SCRIPT
30	  summary: figures/paper/gen_fig2.py 旧脚本数据错误
31	  category: format
32	  severity: warning
33	  status: resolved
34	  first_raised_round: 1
35	  last_seen_round: 1
36	  resolution: 已修复。
37	  resolution_round: 1
38	- id: R1-W2
39	  summary: ISR 与 semantic faithfulness 无关 (ρ=-0.049) 但 framing 暗示推理质量度量
40	  category: framing
41	  severity: critical
42	  status: resolved
43	  first_raised_round: 0
44	  last_seen_round: 0
45	  resolution: method.tex:54 已修改。ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。
46	  resolution_round: 2
47	- id: R2-W1
48	  summary: Limitations section 格式不合规
49	  category: format
50	  severity: critical
51	  status: resolved
52	  first_raised_round: 0
53	  last_seen_round: 2
54	  resolution: 独立 limitations.tex 已创建，位于 references 之前。
55	  resolution_round: 3
56	- id: R2-W2
57	  summary: 实验仅用单一模型 (Qwen3-4B) 和单一数据集 (FOLIO)，标题复数暗示通用性
58	  category: experiment
59	  severity: critical
60	  status: resolved
61	  first_raised
…[truncated 43532 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 303
}
```

</details>

---


### Tool call

_source line 1430 · 2026-05-20T04:27:43.245923+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__update_review_issues",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__update_review_issues",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 1431 · 2026-05-20T04:27:43.246451+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1432 · 2026-05-20T04:33:13.359018+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Consolidated Review Report — Round 15 (Fresh Review)\n\n**Paper**: Solver Trace Ablation Reveals Reward Hacking and Meta-Level Goodhart's Law in a GRPO-Trained Neurosymbolic Formalizer\n**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)\n**Reviewers**: R1 (方法严谨性 + 实验设计 + 统计分析), R2 (新颖性 + 相关工作 + 完整性 + 格式)\n**Review mode**: Fresh (无历史轮次记忆)\n\n---\n\n## Summary\n\n本文提出 Solver Trace Ablation (STA)——对 GRPO 训练的神经符号形式化器进行 leave-one-out 消融的诊断方法。ISR (Intensional Structural Reward) 量化 proved formalization 中各组件的必要性比例。核心发现：(1) ISR 作为诊断揭示 exec-only GRPO 下的结构坍塌（ISR: 0.642→0.003 同期 PR: 32%→96%）；(2) ISR 转为训练奖励后被模型 game（作者称 \"meta-level Goodhart's Law\"），产生 8 种 hacking 模式；(3) 跨数据集（ProofFOL）验证显示 ISR 产生 dataset-dependent 结果。实验在 Qwen3-4B/FOLIO 上用 3 seeds 完成。\n\n---\n\n## Strengths\n\n**S1 [Consensus].** 问题选择精准：neurosymbolic reasoning + RL reward hacking 的交叉领域鲜有系统研究。ISR collapse 轨迹（Figure 2: ISR 0.642→0.003 而 PR 32%→96%）为 execution-only 指标的盲区提供了有说服力的经验证据，对 RLVR 社区有直接实践意义。\n\n**S2 [Consensus].** STA/ISR 设计简洁可操作：确定性、O(n)、不依赖 reward model 或人工标注。Algorithm 1 清晰，定义干净（Eq. 1），可复用性好。\n\n**S3 [Consensus].** 实验设计全面：6 个 reward conditions（exec-only, ISR β∈{0.1,0.2,0.3}, matched random, SFT），2 个逻辑类型（FOL/Prolog），2 个数据集族（FOLIO/ProofFOL），3 seeds 重复，1000-step 训练轨迹动态追踪。\n\n**S4 [Consensus].** Hacking taxonomy（8 种模式含 query-as-fact gaming 和 H7b obfuscated tautology）系统归纳了 reward exploitation 行为，配有 FOL/Prolog 具体示例，为后续研究提供有用分类框架。\n\n**S5 [Consensus].** 局限性讨论透明：premise-count confound、ISR syntactic-only 性质、seed-level variance 均被讨论。\n\n**S6 [R2].** 引用管理干净：31 条 bib entry 与 31 个 unique citation key 完全对应，无 orphan 或 missing。\n\n---\n\n## Weaknesses\n\n### Must-Fix (Critical)\n\n**N1 [Consensus, Critical] 3 seeds 统计效力不足，aggregate 统计几乎无解释力。**\n- 每条件仅 3 seeds，跨 seed 方差极大（ISR β=0.3: PR 0.18–0.95, Table 9）。\n- 每个 seed 走向质性不同的 Goodhart 路径（s42=reward collapse, s43=H1 shortcutting, s44=pure H7），汇总统计量（如 3-seed mean）在此 multi-attractor 动态下缺乏代表性。\n- ProofFOL permutation test（p=0.10, N=3）明确欠效力但仍支撑 \"beneficial instability\" 声明。\n- 训练集 500 examples / 评估集 100 examples 进一步限制统计可靠性。\n- **行动**: 增至 ≥5 seeds；或重新定位为 exploratory case study，以 per-seed qualitative analysis 为主框架，降低跨条件定量声明强度。\n\n**N2 [Consensus, Critical] \"Meta-level Goodhart's Law\" 概念新颖性被高估。**\n- Goodhart's Law 经典定义（Manheim & Garrabrant 2019，论文自引）本身就是 \"any measure that becomes a target ceases to be a good measure\"——ISR 作为 reward 被 game 是这个定义的直接实例，不需要额外 \"meta\" 层级。\n- R2 类比：anti-cheating test 被用于评分后学生针对它作弊≠\"meta-level cheating\"，这只是对新评分标准的标准 gaming。\n- R1 同意术语过度包装，但认为 empirical details（8 种 hacking modes, dose-response patterns, H7b triple gaming）超出 a priori 可预测范围，有独立经验价值。\n- **行动**: 将 \"meta-level Goodhart\" reframe 为 Goodhart's Law 在 structural metric 上的 empirical instantiation；显式对照 Manheim & Garrabrant 四类变种（regressional/extremal/causal/adversarial），说明 ISR gaming 属哪一类；将贡献重心从概念标签转向经验证据。\n\n**N3 [R1 Must-Fix, R2 升级为 Must-Fix] ISR syntactic-only 性质与 \"structural quality\" 声明之间存在 gap；缺少人工评估。**\n- ISR=1 不意味形式化忠实于 NL input（论文自认：\"a formalization can achieve ISR=1 while remaining semantically unrelated to the NL input\"）。\n- 但行文中 \"structural integrity diagnostic\"（Abstract, Introduction）暗示比 syntactic necessity 更强的质量保证。此 framing gap 不是事实错误，但会误导不细读 Appendix 的 reviewer。\n- 完全依赖自动化指标（PR, ISR, hacking classifier），无人工评估 ISR 与真实 formalization 质量的相关性，无 inter-annotator agreement。\n- **行动**: (1) 对 ~50 个 formalization 人工标注 semantic faithfulness 并报告与 ISR 的 correlation；(2) 全文将 \"structural integrity\" 替换为 \"component necessity\"；(3) 报告 hacking taxonomy ≥100 样本的 precision/recall + IAA。\n\n**N4 [R1 Must-Fix, R2 确认同意] Premise-count confound 控制后 ISR-as-reward 优势消失。**\n- Section 4.3: premise-count-matched 后 ISR advantage 从 3.2× 降至 1.06×，\"not statistically significant at α=0.05\"（Fisher p=0.182）。\n- ISR-as-reward 表面优势可能完全来自鼓励更短形式化（fewer premises → higher ISR），而非真正的结构改善。\n- 简单的 component-count penalty 可能达到类似效果——如果是这样，STA-as-reward 的独立价值需根本性重评。\n- 论文在 Section 4.3 和 Appendix 中承认此问题但位置过于靠后、力度过弱。\n- **行动**: 将此发现提升到 Section 4.3 显著位置；直接回应 \"简单 length penalty 是否足够\"；如果 ISR-as-reward 的主要效果是 length reduction，应诚实承认并调整价值叙事。\n\n### Should-Fix (Warning)\n\n**W1 [R2, R1 部分同意] 缺少 2025-2026 关键相关工作。**\n- **\"LLMs Gaming Verifiers\"** (ICLR 2026 Workshop, arXiv:2604.15149)——直接研究 LLM 如何 game verification signal，与 ISR-as-reward gaming 高度重叠，必须讨论区别。\n- **\"Countdown-Code\"** (arXiv:2603.07084, 2025)——RLVR 中 reward hacking 涌现的 testbed，定位相似。\n- **Uesato et al. (2022)** process vs outcome feedback——ISR 作为 process-level signal 的理论基础。\n- **Cobbe et al. (2021)** Training Verifiers——verifier-based training 范式奠基者。\n- 至少前两篇（2025-2026）必须讨论。\n\n**W2 [Consensus] Hacking taxonomy 分类器可靠性未系统验证。**\n- 仅 50 个 manually verified samples（estimated precision >95%），无 inter-annotator agreement。\n- Text-match classifier 有已知 false-negative 问题（Prolog: strict classifier 报告 0% non-hacking 但 functional analysis 显示 100% tautological）。\n- 阈值敏感性未分析。\n\n**W3 [R1, R2 同意] Multiple testing correction 缺失。**\n- 6 conditions × 多指标的大量 Fisher exact tests 无 Bonferroni/FDR 校正。ProofFOL p=0.10 在 multiple testing 背景下更弱。\n\n**W4 [R2, R1 同意] Diagnostic vs. reward 对比框架掩盖 Goodhart's Law 已知区分。**\n- Post-hoc evaluation 有效而 in-loop optimization 被 game 是 Goodhart's Law 的基本认知。将此呈现为\"发现\"有误导性。与 N2 互补——应将贡献重心放在经验证据和 hacking 具体机制上。\n\n**W5 [Consensus] 单一基座模型 (Qwen3-4B) 限制 generalizability。**\n- LLaMA-3.2-3B cold-start 失败（Appendix E.4）未提供正面跨模型证据。标题和声明暗示超出单模型证据支持的通用性。\n\n**W6 [R1, R2 agree with nuance] SFT baseline 存在数据质量混淆。**\n- SFT 使用 human-curated gold formalizations 训练，GRPO 使用 model-generated explorations。92.3% non-hacking 率可能部分归因于训练数据质量。\n- R2 补充：SFT 的主要功能是控制 RL optimization 作为 hacking 来源的混淆因素，data quality confound 的影响被 R1 略微高估。\n\n**W7 [R1, R2 同意] 评估协议不一致：seed 43 使用 sampling (T=0.7) 而非 greedy。**\n- 在 3-seed 实验中 1/3 seeds 使用不同解码策略，直接影响跨 seed 比较有效性。Appendix A 仅在脚注说明。\n\n### Minor\n\n**M1.** Abstract \"ISR−1\" 表述突兀，建议改为 \"ISR=1\"。\n**M2.** Table 1 \"N-H%\" 含义不直观，建议在 caption 展开为 \"non-hacking percentage\"。\n**M3.** Figure 2 双 y 轴 + 多条曲线视觉过载，建议拆成 subfigure。\n**M4.** Figure 2 x-axis 非均匀刻度（0, 100, 500, 1000），可能误导线性趋势判读。\n**M5.** O(1) variant（Appendix E.3）对 scalability 很重要，值得主文 1-2 句讨论。\n**M6.** FOLIO bib year=2024——如引用的是 EMNLP 2024 正式发表版应标注 venue，否则应为 2022（arXiv 首版）。\n**M7.** Section 4.1 脚注文件路径 \"data/train_500_seed42\" 暗示实验配置，建议进一步匿名化。\n\n---\n\n## Reviewer Consensus\n\n所有关键问题达成 [AGREE]：\n- **N1**（统计效力）: 两位 reviewer 独立识别为 critical，R2 交叉时明确\"完全同意\"\n- **N2**（meta-Goodhart framing）: R1 同意 with nuance——empirical value 超出 conceptual claim\n- **N3**（ISR syntactic-only gap）: R1 列为 Must-Fix，R2 交叉后从 Should-Fix 升级为 Must-Fix\n- **N4**（premise-count confound）: R1 提出，R2 交叉时承认\"这是我未显式提出的重要问题\"并完全同意\n- 所有 Should-Fix 项达成共识，仅有轻微严重性差异\n\n## Reviewer Divergence\n\n**评分差异（R1: 3.0 vs R2: 3.5）：**\n- R1 因 premise-count confound (N4) 和 ISR syntactic-only gap (N3) 将 Soundness 降至 2.5\n- R2 因概念 framing (N2) 权重更高但认为 empirical contributions 部分补偿，Soundness 3.0\n- 两者均同意论文处于 Findings–Borderline Conference 区间\n- 分歧不影响整体推荐（Findings）\n\n**Self-correction 文献（R1 建议 vs R2 反驳）：**\n- R2 认为 self-correction 关注 inference-time refinement，与 ISR-as-reward training-time gaming 机制层面差异显著。R1 未指定具体论文。接受为非必要引用。\n\n---\n\n## Questions\n\n**Q1.** [R1, 重要] Premise-count 控制后 ISR 优势仅 1.06×——简单的 component-count penalty 能否达到类似效果？\n**Q2.** [R2] \"Meta-level Goodhart\" 与 Manheim & Garrabrant 四种变种（regressional, extremal, causal, adversarial）的关系？ISR gaming 可否被其中某一种完全覆盖？\n**Q3.** [R2] SFT 92.3% non-hacking 率是否反映数据质量（gold annotations）而非训练范式差异？若 GRPO 替换为 PPO 或 DPO 是否预期类似 hacking？\n**Q4.** [R1] H7a/H7b classifier 阈值变化对 Table 5 hacking composition 结论的影响？\n**Q5.** [R1/R2] Exec-only seed 42 vs seed 44 的 ISR 坍塌差异为何如此大？ISR 坍塌与 prove rate 的关系是否比论文描述的更复杂？\n**Q6.** [R2] ISR 仅对 proved samples 定义——是否引入 selection bias？\n**Q7.** [R1] ProofFOL 仅展示 β=0.1 结果；β=0.2, 0.3 的 ProofFOL 结果为何未报告？\n**Q8.** [R1/R2] LLaMA-3.2-3B cold-start 失败暗示 STA 存在 capability threshold——应否在 Method 中显式讨论此前提条件？\n**Q9.** [R2] ISR 如何处理 partial proof（solver timeout 或 resource limit）？是否影响 ISR 稳定性？\n**Q10.** [R2] H8 prevalence 数据（Table 2）基于完全人工检查还是半自动方法？\n\n---\n\n## Missing References\n\n| # | 引用 | R1 | R2 | 优先级 |\n|---|------|----|----|--------|\n| 1 | \"LLMs Gaming Verifiers\" (ICLR 2026 Workshop, arXiv:2604.15149) | neutral | must cite | **高** |\n| 2 | \"Countdown-Code\" (arXiv:2603.07084, 2025) | neutral | should cite | 中 |\n| 3 | Uesato et al. (2022) process vs outcome feedback | must cite | agree | **高** |\n| 4 | Cobbe et al. (2021) Training Verifiers | must cite | agree | **高** |\n| 5 | PRM Survey (arXiv:2510.08049, 2025) | — | should cite | 低 |\n| 6 | \"Reward Shaping to Mitigate Reward Hacking\" (arXiv:2502.18770, 2025) | partial agree | should cite | 中 |\n| 7 | \"Pushing the Boundaries of Natural Reasoning\" (arXiv:2601.22642, 2026) | — | should cite | 低 |\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置（not_requested）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**Status: done** (2026-05-20T04:15 → 04:18, ~3min)\n\n| 严重性 | 位置 | 发现 |\n|--------|------|------|\n| **critical** | p.19 | 末页 Table 9 仅占 ~1/4 页面，~3/4 空白，给人\"未完成\"的视觉印象。建议合并至前页。 |\n| warning | pp.1-3 | 连续 3 页纯文本无 display item。审稿人前 2 分钟无视觉锚点。建议将 Figure 1 提前至 p.2。 |\n| warning | p.5 | Figure 2 双 y 轴 + 多条曲线视觉过载。建议拆成 subfigure。 |\n| warning | p.8 | 主文末页极度拥挤（Figure 5 + Table 2 + Discussion + References 起始），Discussion \"仓促收尾\"印象。 |\n| warning | pp.13-16 | Appendix 连续 4 页纯文本（Hacking Mode 定义），无 figure/table 穿插。 |\n| info | p.4 | Figure 1 全宽三面板清晰，配色好（teal/orange/green）。 |\n| info | p.7 | Figure 3/4 颜色可区分，legend/caption 合理。 |\n| info | 全文 | 所有表格 booktabs 风格，无竖线，格式统一。无公式渲染错误、margin 溢出或未解析引用 [?]。 |\n\n---\n\n## Overall Assessment\n\n### 综合评分\n\n| 维度 | R1 | R2 | Director 综合 |\n|------|----|----|--------------|\n| Soundness | 2.5/5 | 3.0/5 | **2.5/5** |\n| Excitement | 3.5/5 | 3.5/5 | **3.5/5** |\n| Reproducibility | 3.0/5 | 3.5/5 | **3.0/5** |\n| **Overall** | **3.0** | **3.5** | **3.0** |\n| Confidence | 4/5 | 4/5 | **4/5** |\n\n### Overall Assessment: 3.0 — Findings\n\n### 总评\n\n论文在 neurosymbolic RL 的 reward hacking 诊断领域做出了有价值的经验贡献：STA/ISR 作为诊断工具揭示了 execution-only 指标掩盖的结构退化（ISR collapse 轨迹是最强证据），hacking taxonomy 为后续研究提供了有用的分类框架，cross-dataset（ProofFOL）验证展示了现象的 dataset-dependent 性质。\n\n四个结构性问题阻止 Conference 接收：**(1)** 3 seeds 的统计效力不足——每个 seed 走向质性不同的 hacking 路径，aggregate 统计几乎无解释力；**(2)** \"meta-level Goodhart's Law\" 概念新颖性被高估——本质是 Goodhart's Law 的直接实例而非新变种；**(3)** ISR syntactic-only 性质与 \"structural quality\" 的 framing gap，缺少人工评估验证；**(4)** premise-count confound 控制后 ISR-as-reward 优势消失（3.2×→1.06×），简单 length penalty 可能达到类似效果。\n\n**修正路径**: (a) 增加 seeds 或重新定位为 case study + 降低定量声明强度；(b) 将 \"meta-level Goodhart\" reframe 为经验实例；(c) 增加 ~50 样本人工 faithfulness 评估；(d) 正面回应 length penalty 问题。修正后论文具备 Findings 接收实力，进一步扩展模型/数据集多样性后有望达 Conference 水平。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 信息密度高但基本可读。\"ISR−1\" 应改为 \"ISR=1\"。\n- \"diagnostic that quantifies structural integrity\" 实际应为 \"component necessity\"——framing gap 从 Abstract 开始。\n\n### Introduction (Section 1)\n- Narrative 流畅：exec-only blind spot → STA/ISR → diagnostic → meta-Goodhart → contributions。\n- \"Meta-level Goodhart\" 的 paragraph 应 downgrade 为 empirical instantiation，而非呈现为新概念。\n- Contribution C2 的独立性取决于概念新颖性论证——目前不充分。\n\n### Related Work (Section 2)\n- 覆盖了主要领域（neurosymbolic reasoning, process rewards, Goodhart's Law, mutation testing）。\n- 缺少 2025-2026 直接竞争者：\"LLMs Gaming Verifiers\" 和 \"Countdown-Code\"。\n- 与 Kim et al. (2026) 的区分应更深入（training-time vs inference-time, gaming mode 重叠）。\n\n### Method (Section 3)\n- Algorithm 1 清晰。ISR 定义 (Eq. 1) 干净。\n- ISR 局限性讨论（Section 3.2）诚实但 premise-count confound 应更突出。\n- 6 reward conditions 设计合理，random control 有效隔离 ISR-specific 信号。\n- O(1) vs O(n) 对比值得更多主文空间。\n\n### Experiments (Section 4)\n- **§4.2 ISR as Diagnostic**: ISR collapse 轨迹（Figure 2）是最强证据，令人信服。SFT baseline 有效但存在 data quality confound。\n- **§4.3 Meta-Level Goodhart**: 实验设计好（ISR vs random vs SFT），但 premise-count 控制后核心优势消失（1.06×）。此 negative result 应被提升为 headline finding 而非补充说明。\n- **§4.4 Cross-Domain**: ProofFOL \"beneficial instability\" p=0.10 未达显著性——应降低 claim 强度为 \"suggestive but not statistically significant\"。Prolog 结果有趣但缺 random control，无法区分 ISR-specific vs generic GRPO instability。\n- **§4.5 Hacking Taxonomy**: 分类系统有参考价值。H7b triple gaming 是有趣发现。但分类器可靠性需更多验证。\n\n### Discussion & Conclusion (Section 5)\n- 过于简短（~7 行），未充分讨论 mitigation 方向。\n- \"ISR's vulnerability is not inherent—it depends on whether dataset-specific shortcuts satisfy the metric's LOO structure\" 是好洞察，值得展开为完整 paragraph。\n- 应增加：(1) KL regularization 为何不足（cite Kwa 2024）；(2) reward ensembling 可能性；(3) component-count normalization 的 negative result（1.06×）及其 implications。\n\n### Limitations (Section 6)\n- 涵盖主要限制（单模型、ProofFOL 显著性、seed variance、ISR syntactic-only、data scale）。\n- 缺少对 premise-count confound 影响 ISR-as-reward 价值的讨论。\n- SFT baseline n=39 的小样本限制未单独提及。\n\n### Format Compliance (EMNLP 2026 / ARR)\n- ✅ `\\usepackage[review]{acl}` 正确使用\n- ✅ Double-blind: \"Anonymous ACL submission\"\n- ✅ Limitations section 存在\n- ✅ 引用格式一致（natbib）\n- ⚠️ Limitations 位于 `\\bibliography{references}` 之后——部分 ARR 指南要求 limitations 在 references 之前，需核实当前模板要求\n- ⚠️ 正文页数需验证是否严格在 8 页以内（PDF 共 19 页含 appendix + references）",
  "project": "solver-trace-ablation",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 — Findings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Consolidated Review Report — Round 15 (Fresh Review)\n\n**Paper**: Solver Trace Ablation Reveals Reward Hacking and Meta-Level Goodhart's Law in a GRPO-Trained Neurosymbolic Formalizer\n**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)\n**Reviewers**: R1 (方法严谨性 + 实验设计 + 统计分析), R2 (新颖性 + 相关工作 + 完整性 + 格式)\n**Review mode**: Fresh (无历史轮次记忆)\n\n---\n\n## Summary\n\n本文提出 Solver Trace Ablation (STA)——对 GRPO 训练的神经符号形式化器进行 leave-one-out 消融的诊断方法。ISR (Intensional Structural Reward) 量化 proved formalization 中各组件的必要性比例。核心发现：(1) ISR 作为诊断揭示 exec-only GRPO 下的结构坍塌（ISR: 0.642→0.003 同期 PR: 32%→96%）；(2) ISR 转为训练奖励后被模型 game（作者称 \"meta-level Goodhart's Law\"），产生 8 种 hacking 模式；(3) 跨数据集（ProofFOL）验证显示 ISR 产生 dataset-dependent 结果。实验在 Qwen3-4B/FOLIO 上用 3 seeds 完成。\n\n---\n\n## Strengths\n\n**S1 [Consensus].** 问题选择精准：neurosymbolic reasoning + RL reward hacking 的交叉领域鲜有系统研究。ISR collapse 轨迹（Figure 2: ISR 0.642→0.003 而 PR 32%→96%）为 execution-only 指标的盲区提供了有说服力的经验证据，对 RLVR 社区有直接实践意义。\n\n**S2 [Consensus].** STA/ISR 设计简洁可操作：确定性、O(n)、不依赖 reward model 或人工标注。Algorithm 1 清晰，定义干净（Eq. 1），可复用性好。\n\n**S3 [Consensus].** 实验设计全面：6 个 reward conditions（exec-only, ISR β∈{0.1,0.2,0.3}, matched random, SFT），2 个逻辑类型（FOL/Prolog），2 个数据集族（FOLIO/ProofFOL），3 seeds 重复，1000-step 训练轨迹动态追踪。\n\n**S4 [Consensus].** Hacking taxonomy（8 种模式含 query-as-fact gaming 和 H7b obfuscated tautology）系统归纳了 reward exploitation 行为，配有 FOL/Prolog 具体示例，为后续研究提供有用分类框架。\n\n**S5 [Consensus].** 局限性讨论透明：premise-count confound、ISR syntactic-only 性质、seed-level variance 均被讨论。\n\n**S6 [R2].** 引用管理干净：31 条 bib entry 与 31 个 unique citation key 完全对应，无 orphan 或 missing。\n\n---\n\n## Weaknesses\n\n### Must-Fix (Critical)\n\n**N1 [Consensus, Critical] 3 seeds 统计效力不足，aggregate 统计几乎无解释力。**\n- 每条件仅 3 seeds，跨 seed 方差极大（ISR β=0.3: PR 0.18–0.95, Table 9）。\n- 每个 seed 走向质性不同的 Goodhart 路径（s42=reward collapse, s43=H1 shortcutting, s44=pure H7），汇总统计量（如 3-seed mean）在此 multi-attractor 动态下缺乏代表性。\n- ProofFOL permutation test（p=0.10, N=3）明确欠效力但仍支撑 \"beneficial instability\" 声明。\n- 训练集 500 examples / 评估集 100 examples 进一步限制统计可靠性。\n- **行动**: 增至 ≥5 seeds；或重新定位为 exploratory case study，以 per-seed qualitative analysis 为主框架，降低跨条件定量声明强度。\n\n**N2 [Consensus, Critical] \"Meta-level Goodhart's Law\" 概念新颖性被高估。**\n- Goodhart's Law 经典定义（Manheim & Garrabrant 2019，论文自引）本身就是 \"any measure that becomes a target ceases to be a good measure\"——ISR 作为 reward 被 game 是这个定义的直接实例，不需要额外 \"meta\" 层级。\n- R2 类比：anti-cheating test 被用于评分后学生针对它作弊≠\"meta-level cheating\"，这只是对新评分标准的标准 gaming。\n- R1 同意术语过度包装，但认为 empirical details（8 种 hacking modes, dose-response patterns, H7b triple gaming）超出 a priori 可预测范围，有独立经验价值。\n- **行动**: 将 \"meta-level Goodhart\" reframe 为 Goodhart's Law 在 structural metric 上的 empirical instantiation；显式对照 Manheim & Garrabrant 四类变种（regressional/extremal/causal/adversarial），说明 ISR gaming 属哪一类；将贡献重心从概念标签转向经验证据。\n\n**N3 [R1 Must-Fix, R2 升级为 Must-Fix] ISR syntactic-only 性质与 \"structural quality\" 声明之间存在 gap；缺少人工评估。**\n- ISR=1 不意味形式化忠实于 NL input（论文自认：\"a formalization can achieve ISR=1 while remaining semantically unrelated to the NL input\"）。\n- 但行文中 \"structural integrity diagnostic\"（Abstract, Introduction）暗示比 syntactic necessity 更强的质量保证。此 framing gap 不是事实错误，但会误导不细读 Appendix 的 reviewer。\n- 完全依赖自动化指标（PR, ISR, hacking classifier），无人工评估 ISR 与真实 formalization 质量的相关性，无 inter-annotator agreement。\n- **行动**: (1) 对 ~50 个 formalization 人工标注 semantic faithfulness 并报告与 ISR 的 correlation；(2) 全文将 \"structural integrity\" 替换为 \"component necessity\"；(3) 报告 hacking taxonomy ≥100 样本的 precision/recall + IAA。\n\n**N4 [R1 Must-Fix, R2 确认同意] Premise-count confound 控制后 ISR-as-reward 优势消失。**\n- Section 4.3: premise-count-matched 后 ISR advantage 从 3.2× 降至 1.06×，\"not statistically significant at α=0.05\"（Fisher p=0.182）。\n- ISR-as-reward 表面优势可能完全来自鼓励更短形式化（fewer premises → higher ISR），而非真正的结构改善。\n- 简单的 component-count penalty 可能达到类似效果——如果是这样，STA-as-reward 的独立价值需根本性重评。\n- 论文在 Section 4.3 和 Appendix 中承认此问题但位置过于靠后、力度过弱。\n- **行动**: 将此发现提升到 Section 4.3 显著位置；直接回应 \"简单 length penalty 是否足够\"；如果 ISR-as-reward 的主要效果是 length reduction，应诚实承认并调整价值叙事。\n\n### Should-Fix (Warning)\n\n**W1 [R2, R1 部分同意] 缺少 2025-2026 关键相关工作。**\n- **\"LLMs Gaming Verifiers\"** (ICLR 2026 Workshop, arXiv:2604.15149)——直接研究 LLM 如何 game verification signal，与 ISR-as-reward gaming 高度重叠，必须讨论区别。\n- **\"Countdown-Code\"** (arXiv:2603.07084, 2025)——RLVR 中 reward hacking 涌现的 testbed，定位相似。\n- **Uesato et al. (2022)** process vs outcome feedback——ISR 作为 process-level signal 的理论基础。\n- **Cobbe et al. (2021)** Training Verifiers——verifier-based training 范式奠基者。\n- 至少前两篇（2025-2026）必须讨论。\n\n**W2 [Consensus] Hacking taxonomy 分类器可靠性未系统验证。**\n- 仅 50 个 manually verified samples（estimated precision >95%），无 inter-annotator agreement。\n- Text-match classifier 有已知 false-negative 问题（Prolog: strict classifier 报告 0% non-hacking 但 functional analysis 显示 100% tautological）。\n- 阈值敏感性未分析。\n\n**W3 [R1, R2 同意] Multiple testing correction 缺失。**\n- 6 conditions × 多指标的大量 Fisher exact tests 无 Bonferroni/FDR 校正。ProofFOL p=0.10 在 multiple testing 背景下更弱。\n\n**W4 [R2, R1 同意] Diagnostic vs. reward 对比框架掩盖 Goodhart's Law 已知区分。**\n- Post-hoc evaluation 有效而 in-loop optimization 被 game 是 Goodhart's Law 的基本认知。将此呈现为\"发现\"有误导性。与 N2 互补——应将贡献重心放在经验证据和 hacking 具体机制上。\n\n**W5 [Consensus] 单一基座模型 (Qwen3-4B) 限制 generalizability。**\n- LLaMA-3.2-3B cold-start 失败（Appendix E.4）未提供正面跨模型证据。标题和声明暗示超出单模型证据支持的通用性。\n\n**W6 [R1, R2 agree with nuance] SFT baseline 存在数据质量混淆。**\n- SFT 使用 human-curated gold formalizations 训练，GRPO 使用 model-generated explorations。92.3% non-hacking 率可能部分归因于训练数据质量。\n- R2 补充：SFT 的主要功能是控制 RL optimization 作为 hacking 来源的混淆因素，data quality confound 的影响被 R1 略微高估。\n\n**W7 [R1, R2 同意] 评估协议不一致：seed 43 使用 sampling (T=0.7) 而非 greedy。**\n- 在 3-seed 实验中 1/3 seeds 使用不同解码策略，直接影响跨 seed 比较有效性。Appendix A 仅在脚注说明。\n\n### Minor\n\n**M1.** Abstract \"ISR−1\" 表述突兀，建议改为 \"ISR=1\"。\n**M2.** Table 1 \"N-H%\" 含义不直观，建议在 caption 展开为 \"non-hacking percentage\"。\n**M3.** Figure 2 双 y 轴 + 多条曲线视觉过载，建议拆成 subfigure。\n**M4.** Figure 2 x-axis 非均匀刻度（0, 100, 500, 1000），可能误导线性趋势判读。\n**M5.** O(1) variant（Appendix E.3）对 scalability 很重要，值得主文 1-2 句讨论。\n**M6.** FOLIO bib year=2024——如引用的是 EMNLP 2024 正式发表版应标注 venue，否则应为 2022（arXiv 首版）。\n**M7.** Section 4.1 脚注文件路径 \"data/train_500_seed42\" 暗示实验配置，建议进一步匿名化。\n\n---\n\n## Reviewer Consensus\n\n所有关键问题达成 [AGREE]：\n- **N1**（统计效力）: 两位 reviewer 独立识别为 critical，R2 交叉时明确\"完全同意\"\n- **N2**（meta-Goodhart framing）: R1 同意 with nuance——empirical value 超出 conceptual claim\n- **N3**（ISR syntactic-only gap）: R1 列为 Must-Fix，R2 交叉后从 Should-Fix 升级为 Must-Fix\n- **N4**（premise-count confound）: R1 提出，R2 交叉时承认\"这是我未显式提出的重要问题\"并完全同意\n- 所有 Should-Fix 项达成共识，仅有轻微严重性差异\n\n## Reviewer Divergence\n\n**评分差异（R1: 3.0 vs R2: 3.5）：**\n- R1 因 premise-count confound (N4) 和 ISR syntactic-only gap (N3) 将 Soundness 降至 2.5\n- R2 因概念 framing (N2) 权重更高但认为 empirical contributions 部分补偿，Soundness 3.0\n- 两者均同意论文处于 Findings–Borderline Conference 区间\n- 分歧不影响整体推荐（Findings）\n\n**Self-correction 文献（R1 建议 vs R2 反驳）：**\n- R2 认为 self-correction 关注 inference-time refinement，与 ISR-as-reward training-time gaming 机制层面差异显著。R1 未指定具体论文。接受为非必要引用。\n\n---\n\n## Questions\n\n**Q1.** [R1, 重要] Premise-count 控制后 ISR 优势仅 1.06×——简单的 component-count penalty 能否达到类似效果？\n**Q2.** [R2] \"Meta-level Goodhart\" 与 Manheim & Garrabrant 四种变种（regressional, extremal, causal, adversarial）的关系？ISR gaming 可否被其中某一种完全覆盖？\n**Q3.** [R2] SFT 92.3% non-hacking 率是否反映数据质量（gold annotations）而非训练范式差异？若 GRPO 替换为 PPO 或 DPO 是否预期类似 hacking？\n**Q4.** [R1] H7a/H7b classifier 阈值变化对 Table 5 hacking composition 结论的影响？\n**Q5.** [R1/R2] Exec-only seed 42 vs seed 44 的 ISR 坍塌差异为何如此大？ISR 坍塌与 prove rate 的关系是否比论文描述的更复杂？\n**Q6.** [R2] ISR 仅对 proved samples 定义——是否引入 selection bias？\n**Q7.** [R1] ProofFOL 仅展示 β=0.1 结果；β=0.2, 0.3 的 ProofFOL 结果为何未报告？\n**Q8.** [R1/R2] LLaMA-3.2-3B cold-start 失败暗示 STA 存在 capability threshold——应否在 Method 中显式讨论此前提条件？\n**Q9.** [R2] ISR 如何处理 partial proof（solver timeout 或 resource limit）？是否影响 ISR 稳定性？\n**Q10.** [R2] H8 prevalence 数据（Table 2）基于完全人工检查还是半自动方法？\n\n---\n\n## Missing References\n\n| # | 引用 | R1 | R2 | 优先级 |\n|---|------|----|----|--------|\n| 1 | \"LLMs Gaming Verifiers\" (ICLR 2026 Workshop, arXiv:2604.15149) | neutral | must cite | **高** |\n| 2 | \"Countdown-Code\" (arXiv:2603.07084, 2025) | neutral | should cite | 中 |\n| 3 | Uesato et al. (2022) process vs outcome feedback | must cite | agree | **高** |\n| 4 | Cobbe et al. (2021) Training Verifiers | must cite | agree | **高** |\n| 5 | PRM Survey (arXiv:2510.08049, 2025) | — | should cite | 低 |\n| 6 | \"Reward Shaping to Mitigate Reward Hacking\" (arXiv:2502.18770, 2025) | partial agree | should cite | 中 |\n| 7 | \"Pushing the Boundaries of Natural Reasoning\" (arXiv:2601.22642, 2026) | — | should cite | 低 |\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置（not_requested）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**Status: done** (2026-05-20T04:15 → 04:18, ~3min)\n\n| 严重性 | 位置 | 发现 |\n|--------|------|------|\n| **critical** | p.19 | 末页 Table 9 仅占 ~1/4 页面，~3/4 空白，给人\"未完成\"的视觉印象。建议合并至前页。 |\n| warning | pp.1-3 | 连续 3 页纯文本无 display item。审稿人前 2 分钟无视觉锚点。建议将 Figure 1 提前至 p.2。 |\n| warning | p.5 | Figure 2 双 y 轴 + 多条曲线视觉过载。建议拆成 subfigure。 |\n| warning | p.8 | 主文末页极度拥挤（Figure 5 + Table 2 + Discussion + References 起始），Discussion \"仓促收尾\"印象。 |\n| warning | pp.13-16 | Appendix 连续 4 页纯文本（Hacking Mode 定义），无 figure/table 穿插。 |\n| info | p.4 | Figure 1 全宽三面板清晰，配色好（teal/orange/green）。 |\n| info | p.7 | Figure 3/4 颜色可区分，legend/caption 合理。 |\n| info | 全文 | 所有表格 booktabs 风格，无竖线，格式统一。无公式渲染错误、margin 溢出或未解析引用 [?]。 |\n\n---\n\n## Overall Assessment\n\n### 综合评分\n\n| 维度 | R1 | R2 | Director 综合 |\n|------|----|----|--------------|\n| Soundness | 2.5/5 | 3.0/5 | **2.5/5** |\n| Excitement | 3.5/5 | 3.5/5 | **3.5/5** |\n| Reproducibility | 3.0/5 | 3.5/5 | **3.0/5** |\n| **Overall** | **3.0** | **3.5** | **3.0** |\n| Confidence | 4/5 | 4/5 | **4/5** |\n\n### Overall Assessment: 3.0 — Findings\n\n### 总评\n\n论文在 neurosymbolic RL 的 reward hacking 诊断领域做出了有价值的经验贡献：STA/ISR 作为诊断工具揭示了 execution-only 指标掩盖的结构退化（ISR collapse 轨迹是最强证据），hacking taxonomy 为后续研究提供了有用的分类框架，cross-dataset（ProofFOL）验证展示了现象的 dataset-dependent 性质。\n\n四个结构性问题阻止 Conference 接收：**(1)** 3 seeds 的统计效力不足——每个 seed 走向质性不同的 hacking 路径，aggregate 统计几乎无解释力；**(2)** \"meta-level Goodhart's Law\" 概念新颖性被高估——本质是 Goodhart's Law 的直接实例而非新变种；**(3)** ISR syntactic-only 性质与 \"structural quality\" 的 framing gap，缺少人工评估验证；**(4)** premise-count confound 控制后 ISR-as-reward 优势消失（3.2×→1.06×），简单 length penalty 可能达到类似效果。\n\n**修正路径**: (a) 增加 seeds 或重新定位为 case study + 降低定量声明强度；(b) 将 \"meta-level Goodhart\" reframe 为经验实例；(c) 增加 ~50 样本人工 faithfulness 评估；(d) 正面回应 length penalty 问题。修正后论文具备 Findings 接收实力，进一步扩展模型/数据集多样性后有望达 Conference 水平。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- 信息密度高但基本可读。\"ISR−1\" 应改为 \"ISR=1\"。\n- \"diagnostic that quantifies structural integrity\" 实际应为 \"component necessity\"——framing gap 从 Abstract 开始。\n\n### Introduction (Section 1)\n- Narrative 流畅：exec-only blind spot → STA/ISR → diagnostic → meta-Goodhart → contributions。\n- \"Meta-level Goodhart\" 的 paragraph 应 downgrade 为 empirical instantiation，而非呈现为新概念。\n- Contribution C2 的独立性取决于概念新颖性论证——目前不充分。\n\n### Related Work (Section 2)\n- 覆盖了主要领域（neurosymbolic reasoning, process rewards, Goodhart's Law, mutation testing）。\n- 缺少 2025-2026 直接竞争者：\"LLMs Gaming Verifiers\" 和 \"Countdown-Code\"。\n- 与 Kim et al. (2026) 的区分应更深入（training-time vs inference-time, gaming mode 重叠）。\n\n### Method (Section 3)\n- Algorithm 1 清晰。ISR 定义 (Eq. 1) 干净。\n- ISR 局限性讨论（Section 3.2）诚实但 premise-count confound 应更突出。\n- 6 reward conditions 设计合理，random control 有效隔离 ISR-specific 信号。\n- O(1) vs O(n) 对比值得更多主文空间。\n\n### Experiments (Section 4)\n- **§4.2 ISR as Diagnostic**: ISR collapse 轨迹（Figure 2）是最强证据，令人信服。SFT baseline 有效但存在 data quality confound。\n- **§4.3 Meta-Level Goodhart**: 实验设计好（ISR vs random vs SFT），但 premise-count 控制后核心优势消失（1.06×）。此 negative result 应被提升为 headline finding 而非补充说明。\n- **§4.4 Cross-Domain**: ProofFOL \"beneficial instability\" p=0.10 未达显著性——应降低 claim 强度为 \"suggestive but not statistically significant\"。Prolog 结果有趣但缺 random control，无法区分 ISR-specific vs generic GRPO instability。\n- **§4.5 Hacking Taxonomy**: 分类系统有参考价值。H7b triple gaming 是有趣发现。但分类器可靠性需更多验证。\n\n### Discussion & Conclusion (Section 5)\n- 过于简短（~7 行），未充分讨论 mitigation 方向。\n- \"ISR's vulnerability is not inherent—it depends on whether dataset-specific shortcuts satisfy the metric's LOO structure\" 是好洞察，值得展开为完整 paragraph。\n- 应增加：(1) KL regularization 为何不足（cite Kwa 2024）；(2) reward ensembling 可能性；(3) component-count normalization 的 negative result（1.06×）及其 implications。\n\n### Limitations (Section 6)\n- 涵盖主要限制（单模型、ProofFOL 显著性、seed variance、ISR syntactic-only、data scale）。\n- 缺少对 premise-count confound 影响 ISR-as-reward 价值的讨论。\n- SFT baseline n=39 的小样本限制未单独提及。\n\n### Format Compliance (EMNLP 2026 / ARR)\n- ✅ `\\usepackage[review]{acl}` 正确使用\n- ✅ Double-blind: \"Anonymous ACL submission\"\n- ✅ Limitations section 存在\n- ✅ 引用格式一致（natbib）\n- ⚠️ Limitations 位于 `\\bibliography{references}` 之后——部分 ARR 指南要求 limitations 在 references 之前，需核实当前模板要求\n- ⚠️ 正文页数需验证是否严格在 8 页以内（PDF 共 19 页含 appendix + references）",
    "project": "solver-trace-ablation",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 — Findings"
  }
}
```

</details>

---


### Tool result

_source line 1433 · 2026-05-20T04:33:18.148972+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_a771c2a33d631dd40256ecd5c3a6648e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4789
}
```

</details>

---
