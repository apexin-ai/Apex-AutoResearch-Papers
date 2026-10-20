# Research conversation: 任务：论文写作 polish 审查（只读，不修改） 读以下文件，完成 4 项审查任务，输出详细建议。 文件路径（全部在 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a760df4be266cc066.jsonl`
- **Structured JSON:** [`80a236415d96b7e3483f.json`](../../sessions/80/80a236415d96b7e3483f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

16 recorded events

### User

_source line 1 · 2026-05-23T22:23:19.032Z_

## 任务：论文写作 polish 审查（只读，不修改）

读以下文件，完成 4 项审查任务，输出详细建议。

文件路径（全部在 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/` 下）：
- introduction.tex
- related_work.tex
- method.tex
- results.tex
- discussion.tex
- limitations.tex

### 任务 1: Introduction hook
读 introduction.tex 开头（前 15 行左右）。评估：
- 是否立即抓住读者注意力？
- 有没有更好的 opening 方式？（比如用一个具体的 contamination case / 数据点开场，而不是泛泛的 background）
- 如果有建议修改，给出具体的替代文本（2-3 句）

### 任务 2: Transition 检查
检查以下 section 衔接处：
- Introduction 结尾 → Related Work 开头
- Related Work 结尾 → Method 开头（或 Introduction → Method，看结构）
- Method 结尾 → Results 开头
- Results 各 subsection 之间的过渡句
- Results 结尾 → Discussion 开头

对每个衔接点：读最后 2-3 句 + 下一节前 2-3 句，评估逻辑是否连贯。如果有断裂，指出并给出修改建议。

### 任务 3: Prose tightening
通读所有 section，找出可以更精练的表述。关注：
- 冗余短语（"it is important to note that", "in order to" 等）
- 可以合并的相邻句子
- 过度 hedging（"may potentially", "could possibly"）
- 重复表达同一个 point 的地方

对每处给出：原文 → 建议修改，并估计节省的字数。

### 任务 4: Table/Figure caption 自包含性
读所有 \caption{...} 和 figure/table 环境。检查：
- 读者是否仅凭 caption 就能理解图表内容？
- 是否有关键术语在 caption 中未解释？
- 是否缺少单位、模型名、数据集名等关键信息？

列出每个图表的 caption，标注"自包含/需补充"。

### 输出格式
按 4 个任务分别输出，每个任务标题清晰。建议要具体，给出原文引用和行号。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "db957384-5e7f-4db3-aba3-2ab2a6e43bac",
  "agentId": "a760df4be266cc066",
  "type": "user",
  "uuid": "2fcdc812-8cbc-49ae-bb04-20fff1bd3efc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_51ea7db2",
  "sessionId": "16ee981e-ef12-42ca-ad7f-0e04fded96ed",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "concurrent-knitting-hare"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-23T22:23:19.036Z_

```json
{
  "parentUuid": "2fcdc812-8cbc-49ae-bb04-20fff1bd3efc",
  "isSidechain": true,
  "agentId": "a760df4be266cc066",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__allocate_and_submit",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__approve_worker",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__backup_project_to_s3",
      "mcp__agent-ml-research__cancel_worker",
      "mcp__agent-ml-research__check_job_status",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__distill_papers",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_alert",
      "mcp__agent-ml-research__feishu_send_approval_card",
      "mcp__agent-ml-research__feishu_send_result_card",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_baseline_metrics",
      "mcp__agent-ml-research__get_distill_status",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_matrix_value",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__get_tum_config",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__impact_analysis",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_available_gpus",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__list_s3_backups",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__main_agent_post_to_director",
      "mcp__agent-ml-research__matrix_gap_analysis",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__poll_cron",
      "mcp__agent-ml-research__poll_secret_request",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_mistakes",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reconcile_crons",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__register_cron",
      "mcp__agent-ml-research__request_secret",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__submit_on_allocated",
      "mcp__agent-ml-research__submit_training_job",
      "mcp__agent-ml-research__sync_matrix_status",
      "mcp__agent-ml-research__tail_training_logs",
      "mcp__agent-ml-research__update_baseline",
      "mcp__agent-ml-research__update_matrix",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__allocate_and_submit",
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__approve_worker",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__backup_project_to_s3",
      "mcp__agent-ml-research__cancel_worker",
      "mcp__agent-ml-research__check_job_status",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__distill_papers",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__feishu_read_tum_pending_key",
      "mcp__agent-ml-research__feishu_send_alert",
      "mcp__agent-ml-research__feishu_send_approval_card",
      "mcp__agent-ml-research__feishu_send_result_card",
      "mcp__agent-ml-research__feishu_send_tum_key_request_card",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_baseline_metrics",
      "mcp__agent-ml-research__get_distill_status",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_matrix_value",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__get_tum_config",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__impact_analysis",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_available_gpus",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__list_s3_backups",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__main_agent_post_to_director",
      "mcp__agent-ml-research__matrix_gap_analysis",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__poll_cron",
      "mcp__agent-ml-research__poll_secret_request",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_mistakes",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reconcile_crons",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__register_cron",
      "mcp__agent-ml-research__request_secret",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__submit_on_allocated",
      "mcp__agent-ml-research__submit_training_job",
      "mcp__agent-ml-research__sync_matrix_status",
      "mcp__agent-ml-research__tail_training_logs",
      "mcp__agent-ml-research__update_baseline",
      "mcp__agent-ml-research__update_matrix",
      "mcp__agent-ml-research__update_registry",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "3347fd2a-e748-4fdd-b1b3-bf7cf0c720c9",
  "timestamp": "2026-05-23T22:23:19.036Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_51ea7db2",
  "sessionId": "16ee981e-ef12-42ca-ad7f-0e04fded96ed",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "concurrent-knitting-hare"
}
```

---

### Assistant

_source line 3 · 2026-05-23T22:23:24.713Z_



我先读取所有论文章节文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3347fd2a-e748-4fdd-b1b3-bf7cf0c720c9",
  "isSidechain": true,
  "agentId": "a760df4be266cc066",
  "requestId": "req_011CbLHMUu22LeBUYEURaG39",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "77fa4045-4361-4076-89fc-71a5775877f8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_51ea7db2",
  "sessionId": "16ee981e-ef12-42ca-ad7f-0e04fded96ed",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "concurrent-knitting-hare",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NnrDoPTR58kwbL8NeB8PvY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 29750,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 29750,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-23T22:23:25.173Z_

<details open><summary>🔧 Tool call — Read · `toolu_01L2UNNjc6cvzLBanSCtsN4y`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77fa4045-4361-4076-89fc-71a5775877f8",
  "isSidechain": true,
  "agentId": "a760df4be266cc066",
  "requestId": "req_011CbLHMUu22LeBUYEURaG39",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b553081-5ad4-4bfb-8d99-d1cc513428ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_51ea7db2",
  "sessionId": "16ee981e-ef12-42ca-ad7f-0e04fded96ed",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "concurrent-knitting-hare",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NnrDoPTR58kwbL8NeB8PvY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 29750,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 29750,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-23T22:23:25.185Z_

<details><summary>↩ Tool result · `toolu_01L2UNNjc6cvzLBanSCtsN4y`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Benchmark contamination, the unintended inclusion of evaluation data in training corpora, poses a growing threat to the integrity of large language model (LLM) evaluation \citep{dodge2021, magar2022, sainz2023}.
4	As training corpora and public benchmarks both expand, the probability of overlap increases structurally \citep{jacovi2023, chang2024survey}.
5	When contamination occurs, benchmark scores no longer reflect genuine capability, undermining the primary mechanism by which the community compares and selects models.
6	
7	A range of detection methods have been proposed, but all require some form of privileged access beyond the binary response record.
8	N-gram overlap methods need the training corpus \citep{dodge2021, magar2022}.
9	Membership inference approaches require token-level probabilities \citep{minkprob2024, deng2024}.
10	Probing methods rely on crafted prompts \citep{golchin2024, oren2024}.
11	Performance-based methods require multiple test variants or output logits \citep{constat2024, codec2026}.
12	These methods form a detection frontier ordered by information access.
13	No existing method operates using only binary response patterns, without model weights, gradients, logits, or training data---though, as we show, effective detection additionally requires externally calibrated item parameters.
14	
15	In this work, we focus on SFT-stage contamination---where benchmark answers are explicitly included in fine-tuning data---for three reasons.
16	First, controlled experiments require known ground-truth contamination sets, achievable through fine-tuning with specific benchmark items.
17	Second, SFT-stage contamination is increasingly relevant as fine-tuning-as-a-service platforms proliferate, creating new pathways for benchmark data to enter training mixtures.
18	Third, SFT provides a methodologically clean setting to characterize detection boundaries before extending to noisier pretraining scenarios.
19	
20	The need for detection from binary response patterns grows more pressing as models evolve.
21	\citet{wang2025fragility} show that all ten log-probability-based methods they evaluate perform at chance level on models trained with reinforcement learning (RL), because RL reshapes internal token distributions while preserving binary correctness patterns.
22	This motivates a fundamental question: \emph{what can binary response patterns reveal about contamination, and under what conditions?}
23	
24	We observe that a contaminated LLM is functionally analogous to a test-taker with item preknowledge: both produce response patterns in which difficult items are answered correctly through memorization rather than genuine ability.
25	This connection points to person-fit statistics, developed over four decades for cheating detection in educational testing \citep{drasgow1985, meijer2001, karabatsos2003, sinharay2017}.
26	The standardized statistic $\ell_z^*$ \citep{snijders2001} measures how well a response pattern conforms to Item Response Theory (IRT) model predictions.
27	Figure~\ref{fig:motivation} illustrates this analogy.
28	Despite the natural correspondence, no prior work has applied person-fit statistics to LLM benchmark contamination.
29	
30	\begin{figure}[t]
31	  \centering
32	  \includegraphics[width=\columnwidth]{fig_1_response_pattern.pdf}
33	  \caption{A clean model's responses track the IRT-predicted probability curve (left); a contaminated model shows anomalous successes on hard items (right, red diamonds), producing a large $|\Delta\ell_z^*|$ signal.}
34	  \label{fig:motivation}
35	\end{figure}
36	
37	Rather than proposing $\ell_z^*$ as a ready-to-deploy detection tool, we characterize the behavior boundaries of IRT person-fit statistics for LLM contamination detection.
38	Our framework operates at three layers: (i) pre-calibrated 4PL item parameters from the PSN-IRT item bank \citep{psnirt2026}, an external resource derived from 13,000+ models; (ii) binary response patterns obtained from the target model without access to weights or logits; and (iii) retrospective statistical inference requiring no model modification.
39	Using controlled contamination experiments across three 7--8B model families (Qwen2.5-7B, Llama-3.1-8B, Mistral-7B; $n{=}10$ clean seeds each) with pre-calibrated 4PL item parameters from PSN-IRT \citep{psnirt2026}, we identify three IRT-specific findings on MMLU \citep{hendrycks2021mmlu} and ARC-Challenge:
40	
41	\begin{enumerate}[leftmargin=*,nosep]
42	\item \textbf{Model-specific $\theta$-shift dynamics.} Contamination inflates ability estimates ($\hat{\theta}$), absorbing the person-fit signal; $\theta$-anchoring amplifies Qwen's multi-seed $|d|$ by 2.4$\times$ at 50\% contamination while reducing inter-seed CV from 60\% to 19\%, establishing $\theta$-anchoring as a necessary condition for reliable detection of high-ability models at high contamination. ARC-C reverses through a ceiling effect.
43	
44	\item \textbf{Detection-diagnosis tradeoff.} Simpler statistics yield stronger detection: accuracy $z$-scores produce $|d|$ values several-fold to over an order of magnitude larger than person-fit statistics, and HT generally exceeds $\ell_z^*$. Yet the diagnostic power reverses: only $\ell_z^*$ supports seen/unseen decomposition, mechanistic $\theta$-shift analysis, and sensitivity to response-pattern structure (57/60 vs.\ 4/60 flagged cells on real-world data).
45	
46	\item \textbf{Non-monotonic dose-response under free-$\theta$ (exploratory).} Multi-seed Qwen trajectory ($|d|$: $4.15 \to 5.36 \to 7.44 \to 5.08$ at 5\%/15\%/25\%/50\%) shows attenuated non-monotonicity; $\theta$-anchoring eliminates the pattern and reveals strong positive dose-response ($|d|{=}12.32$ at 50\%). The non-monotonicity is a $\theta$-estimation artifact, not a detection boundary.
47	\end{enumerate}
48	
49	Our contributions are threefold:
50	(1) We provide the first empirical characterization of IRT person-fit behavior for LLM contamination, quantifying theoretically predicted phenomena ($\theta$-shift absorption, detection-diagnosis tradeoff) whose magnitudes and boundary conditions are not derivable from IRT theory alone.
51	(2) We establish that $\Delta\ell_z^*$ reliably detects SFT-stage contamination across three model families (all bootstrap 95\% CIs exclude zero, $n{=}10$).
52	(3) We document the detection-diagnosis tradeoff, clarifying what binary response patterns can and cannot reveal.
53	Findings~1--2 are confirmatory (pre-planned 15\%/50\% $\times$ 3 families); Finding~3 is exploratory (5\%/25\% added post-hoc).
54	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b553081-5ad4-4bfb-8d99-d1cc513428ce",
  "isSidechain": true,
  "promptId": "db957384-5e7f-4db3-aba3-2ab2a6e43bac",
  "agentId": "a760df4be266cc066",
  "type": "user",
  "uuid": "de5399d6-a6e6-4a4d-9385-2061ad3f4cfb",
  "sourceToolAssistantUUID": "7b553081-5ad4-4bfb-8d99-d1cc513428ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_51ea7db2",
  "sessionId": "16ee981e-ef12-42ca-ad7f-0e04fded96ed",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "concurrent-knitting-hare"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-23T22:23:25.613Z_

<details open><summary>🔧 Tool call — Read · `toolu_018rfaveTtf86CHFkPACNV1W`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de5399d6-a6e6-4a4d-9385-2061ad3f4cfb",
  "isSidechain": true,
  "agentId": "a760df4be266cc066",
  "requestId": "req_011CbLHMUu22LeBUYEURaG39",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "feace329-29b7-44c1-8b87-9adf2ddd7167",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_51ea7db2",
  "sessionId": "16ee981e-ef12-42ca-ad7f-0e04fded96ed",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "concurrent-knitting-hare",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NnrDoPTR58kwbL8NeB8PvY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 29750,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 29750,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-23T22:23:25.620Z_

<details><summary>↩ Tool result · `toolu_018rfaveTtf86CHFkPACNV1W`</summary>

```text
1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Benchmark contamination detection.}
4	Contamination detection methods span a wide range of information requirements.
5	Corpus-search methods match benchmark items directly against pretraining data \citep{dodge2021, magar2022}, but require full corpus access unavailable for closed models.
6	Membership inference attacks (MIA) use token-level log-probabilities to distinguish training from unseen examples \citep{minkprob2024, deng2024}.
7	Generation-based probes elicit benchmark content via prompting \citep{golchin2024, golchin2024quiz, oren2024}.
8	Performance-based methods compare accuracy on target and reference sets \citep{constat2024, pacost2024, codec2026}, requiring multiple evaluations or in-context learning passes.
9	\citet{zhou2023benchmark} and \citet{sainz2023} argue for systematic contamination measurement, \citet{jacovi2023} propose mitigation strategies, and \citet{bordt2025forget} show that contamination can be ``forgotten'' under sufficient continued training.
10	\citet{han2026quantifying} quantify contamination in psychometric evaluations of LLMs, demonstrating that memorization effects extend beyond standard benchmarks.
11	\citet{kattamuri2025radar} take a mechanistic interpretability approach, using activation patterns to distinguish recall-based from reasoning-based responses; our work instead operates purely on behavioral response patterns without access to model internals.
12	\citet{fu2025contamination} systematically evaluate detection method assumptions, finding that most methods degrade under realistic conditions; our work contributes a psychometric perspective to this ongoing evaluation.
13	
14	A critical limitation unites all token-level methods: \citet{wang2025fragility} show that RL post-training renders MIA-based detectors no better than random across 10 methods and 4 benchmarks, because RL reshapes token distributions while largely preserving binary correctness patterns.
15	\citet{selfcritique2026} and \citet{zhang2026rlvr} propose RL-specific solutions but require generation-level access.
16	Our approach requires no access to model weights, logits, or training data---only binary response patterns and externally calibrated item parameters from PSN-IRT \citep{psnirt2026}.
17	
18	\paragraph{IRT for LLM evaluation.}
19	Item Response Theory has seen growing adoption in NLP and ML evaluation.
20	\citet{martinezplumed2019} applied IRT to analyze machine learning classifiers at the instance level, establishing that item difficulty and discrimination parameters capture meaningful variation across models.
21	\citet{lalor2019} proposed estimating IRT parameters from DNN-generated response patterns, removing the need for human annotators.
22	\citet{rodriguez2021} demonstrated that IRT-informed item weighting improves leaderboard rankings over raw accuracy.
23	\citet{polo2024tinybenchmarks} used IRT-based item selection to reduce benchmark sizes by 100$\times$ while preserving model rankings, and \citet{atlas2025} developed adaptive testing procedures for efficient LLM evaluation.
24	Most directly relevant, \citet{psnirt2026} calibrated 4PL item parameters for over 13,000 models across 11 benchmarks, providing the item bank our framework builds on.
25	All of these works use IRT for ability estimation or benchmark efficiency; none apply \emph{person-fit} statistics for contamination detection.
26	
27	\paragraph{Person-fit statistics in psychometrics.}
28	Person-fit analysis has a long history in educational measurement for detecting aberrant test-taking behavior \citep[see][for a textbook treatment]{embretson2000}.
29	\citet{levine1988} formalized optimal appropriateness measurement; \citet{drasgow1985} introduced $\ell_z$, a standardized log-likelihood residual; \citet{snijders2001} derived the corrected $\ell_z^*$ that accounts for ability estimation uncertainty.
30	\citet{karabatsos2003} compared 36 person-fit statistics and found $\ell_z$ among the most powerful for detecting cheating; \citet{sinharay2017personfit} revisited these simulations and confirmed comparable power between parametric and nonparametric statistics.
31	We select $\ell_z^*$ for its theoretical grounding and HT \citep{vanderflier1982} as a nonparametric complement, following their top-ranked performance in that comparison.
32	\citet{reise1990} and \citet{meijer2001} provide systematic evaluations of person-fit methodology.
33	\citet{sinharay2017} showed that $\ell_z^*$ is particularly effective when the set of compromised items is known, a setting analogous to benchmark contamination where memorized items constitute the compromised set.
34	Our work transfers this psychometric toolkit to LLM evaluation, treating each model as an examinee whose item-level response pattern may reveal memorization.
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "feace329-29b7-44c1-8b87-9adf2ddd7167",
  "isSidechain": true,
  "promptId": "db957384-5e7f-4db3-aba3-2ab2a6e43bac",
  "agentId": "a760df4be266cc066",
  "type": "user",
  "uuid": "5c9bf444-ab74-4934-b474-d9952365bc6c",
  "sourceToolAssistantUUID": "feace329-29b7-44c1-8b87-9adf2ddd7167",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_51ea7db2",
  "sessionId": "16ee981e-ef12-42ca-ad7f-0e04fded96ed",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "concurrent-knitting-hare"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-23T22:23:26.585Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GURazmZCnk3pebKR1ikGAi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c9bf444-ab74-4934-b474-d9952365bc6c",
  "isSidechain": true,
  "agentId": "a760df4be266cc066",
  "requestId": "req_011CbLHMUu22LeBUYEURaG39",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "aff62691-1dbc-4100-a647-eb8e8326c6f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_51ea7db2",
  "sessionId": "16ee981e-ef12-42ca-ad7f-0e04fded96ed",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "concurrent-knitting-hare",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NnrDoPTR58kwbL8NeB8PvY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 29750,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 29750,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-23T22:23:26.596Z_

<details><summary>↩ Tool result · `toolu_01GURazmZCnk3pebKR1ikGAi`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{IRT Person-Fit Framework}
5	\label{sec:framework}
6	
7	We adopt the four-parameter logistic (4PL) IRT model to characterize contamination-induced aberrance in LLM response patterns.
8	The 4PL model defines the probability that a model with ability $\theta$ answers item $i$ correctly:
9	\begin{equation}
10	  P_i(\theta) = c_i + (d_i - c_i)\,\frac{1}{1 + e^{-a_i(\theta - b_i)}}
11	  \label{eq:4pl}
12	\end{equation}
13	where $a_i$ is discrimination, $b_i$ difficulty, $c_i$ the lower asymptote (guessing), and $d_i$ the upper asymptote (slip).
14	Item parameters are pre-calibrated by PSN-IRT \citep{psnirt2026} from a large-scale leaderboard dataset; we use these external parameters rather than re-estimating from potentially contaminated data, since our MML-EM refit shows discrimination recovery degrades to $r_a{=}0.127$ on contaminated leaderboard data.
15	
16	Given item parameters and a binary response vector $\mathbf{x} = (x_1, \ldots, x_n)$, we compute the person-fit statistic $\ell_z^*$ \citep{snijders2001}, a standardized log-likelihood residual quantifying deviation between observed and expected response patterns.
17	The Snijders correction accounts for estimation uncertainty in $\hat{\theta}_{\text{MLE}}$, so that $\ell_z^* \sim \mathcal{N}(0,1)$ under the null \citep{drasgow1985, snijders2001}; \citet{magis2012} provide a detailed treatment of how response model selection and ability estimation affect $\ell_z^*$.
18	Large negative $\ell_z^*$ indicates aberrant responding (unexpected failures on easy items or unexpected successes on hard items); large positive values indicate over-consistent patterns.
19	
20	\subsection{$\Delta\ell_z^*$ Matched-Difference Design}
21	\label{sec:did}
22	
23	LLM response patterns systematically violate IRT assumptions of local independence and unidimensionality.
24	In our empirical data, 57 of 60 model-benchmark cells yield $|\ell_z^*| > 1.96$ even absent contamination, rendering absolute thresholds uninformative.
25	We address this through a matched-difference design.
26	
27	For controlled experiments with clean baselines, we compute:
28	\begin{equation}
29	  \Delta\ell_z^* = \ell_{z,\text{contam}}^{*} - \bar{\ell}_{z,\text{clean}}^{*}
30	  \label{eq:delta_lz}
31	\end{equation}
32	where $\bar{\ell}_{z,\text{clean}}^{*}$ averages over $n{=}10$ clean seeds.
33	The shared model misfit cancels, isolating contamination-specific aberrance.
34	We quantify effect sizes as $d = (\ell_{z,\text{contam}}^{*} - \bar{\ell}_{z,\text{clean}}^{*})\,/\,s_{\text{clean}}$, where $s_{\text{clean}}$ is the SD of the $n{=}10$ clean-seed $\ell_z^*$ values; with a single contaminated observation per condition, $d$ is a standardized departure rather than a two-sample effect size (Hedges' $g = J \cdot d$, $J \approx 0.914$ for $n{=}10$; \citealp{hedges1981}).
35	We report percentile bootstrap 95\% CIs (10,000 resamples) reflecting clean-seed variability only; BCa correction (Appendix~\ref{app:bca}) generally confirms conservative coverage; multi-seed contamination-run variance appears in Appendix~\ref{app:reproducibility}.
36	
37	For deployment without clean baselines, cross-benchmark comparison provides the reference: the target benchmark's $\ell_z^*$ is compared against benchmarks presumed clean from the same model.
38	Significance thresholds derive from a nonparametric bootstrap null rather than the asymptotic $\mathcal{N}(0,1)$ reference, accommodating residual model misspecification.
39	Simulation analysis (Appendix~\ref{app:local_dep}) confirms that the matched-difference design is robust to local dependence at realistic levels ($d_{\text{ratio}} \geq 0.93$ for $\sigma_\tau \leq 0.5$) and maintains ${\geq}98.5\%$ power even under contamination-specific asymmetric dependence.
40	
41	\subsection{Experimental Setup}
42	\label{sec:setup}
43	
44	\paragraph{Models and contamination.}
45	We validate on three 7--8B model families: Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct, and Mistral-7B-Instruct-v0.3.
46	Each is fine-tuned with QLoRA (rank\,$=$\,16, $\alpha$\,$=$\,32) under clean and contaminated conditions at varying levels: at $X\%$ contamination, $X\%$ of SFT training examples are benchmark items (questions paired with gold answers in the standard evaluation format), with the remainder drawn from a general instruction-following dataset.
47	All three families are tested at 15\% and 50\% contamination.
48	Following initial observation of non-monotonic dose-response for Qwen, we added 5\% and 25\% conditions for Qwen to trace the full dose-response curve.
49	The 25\% condition was subsequently extended to Llama to test whether the pattern generalizes; Mistral was not tested at 5\% or 25\% due to computational constraints.
50	We train $n{=}10$ independent clean seeds per model to establish baseline variability and construct bootstrap confidence intervals.
51	Reported CIs reflect variability across $n$ clean baseline seeds; for Qwen, each contamination level (15\%/25\%/50\%) was additionally replicated with $n{=}3$ independent QLoRA seeds to assess training-run variance (Appendix~\ref{app:reproducibility}).
52	
53	\paragraph{Benchmarks.}
54	We evaluate on MMLU \citep{hendrycks2021mmlu} (14,042 items) and ARC-Challenge \citep{clark2018arc} (295 items), spanning two orders of magnitude in benchmark size.
55	All 4PL item parameters are from \citet{psnirt2026}.
56	ARC-Challenge experiments were conducted on Qwen only, as the primary evaluation of cross-benchmark generalizability; extending to additional families was constrained by computational budget.
57	
58	\paragraph{Post-RL extension.}
59	To probe behavior boundaries beyond SFT, we apply Group Relative Policy Optimization (GRPO; \citealp{shao2024}) to one contaminated Qwen model (15\% MMLU) for 1,500 steps, evaluating at three checkpoints.
60	This extension is $N{=}1$ (single model family, single contamination level).
61	
62	\paragraph{Contamination model.}
63	QLoRA SFT on benchmark items serves as a controlled proxy for SFT-stage contamination, where benchmark data is explicitly included in fine-tuning mixtures---analogous to a test-taker with item preknowledge.
64	Our findings are scoped to SFT-based contamination and may not generalize to pretraining contamination, which operates through different learning dynamics.
65	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aff62691-1dbc-4100-a647-eb8e8326c6f4",
  "isSidechain": true,
  "promptId": "db957384-5e7f-4db3-aba3-2ab2a6e43bac",
  "agentId": "a760df4be266cc066",
  "type": "user",
  "uuid": "8e9ee3a5-c43a-412a-a78d-8b7a715ef9a0",
  "sourceToolAssistantUUID": "aff62691-1dbc-4100-a647-eb8e8326c6f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_51ea7db2",
  "sessionId": "16ee981e-ef12-42ca-ad7f-0e04fded96ed",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "concurrent-knitting-hare"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-23T22:23:27.079Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XPXLUNWbgCqwv7fSx7KDc7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e9ee3a5-c43a-412a-a78d-8b7a715ef9a0",
  "isSidechain": true,
  "agentId": "a760df4be266cc066",
  "requestId": "req_011CbLHMUu22LeBUYEURaG39",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b2dcdd2f-38ee-4d0f-8d6f-b981d14f7df3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_51ea7db2",
  "sessionId": "16ee981e-ef12-42ca-ad7f-0e04fded96ed",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "concurrent-knitting-hare",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NnrDoPTR58kwbL8NeB8PvY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 29750,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 29750,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-23T22:23:27.123Z_

<details><summary>↩ Tool result · `toolu_01XPXLUNWbgCqwv7fSx7KDc7`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Detection Signal Across Model Families}
5	\label{sec:detection}
6	
7	Table~\ref{tab:cohens_d} presents Cohen's $d$ effect sizes for $\ell_z^*$ across three model families and two benchmarks.
8	All confidence intervals exclude zero, confirming that $\Delta\ell_z^*$ reliably separates contaminated from clean models at both contamination levels.
9	
10	On MMLU, effect sizes range from $|d|{=}1.99$ (Llama at 25\%) to $|d|{=}7.44$ (Qwen at 25\%), with Qwen at 5\% ($|d|{=}4.15$) confirming detection at the lowest contamination level tested. Llama ($|d|{=}2.11$/$1.99$/$2.33$) and Mistral ($|d|{=}3.01$/$3.50$) show comparable magnitudes.
11	On ARC-C (295 items), Qwen yields $|d|{=}3.16$ at 15\% and $|d|{=}5.30$ at 50\%, demonstrating that detection remains feasible even on small benchmarks when contamination is sufficiently concentrated.
12	
13	Clean-model $\ell_z^*$ baselines diverge substantially across families: Qwen ${+}8.68$ ($\text{SD}{=}0.74$), Mistral ${+}4.02$ ($\text{SD}{=}2.05$), Llama ${+}0.26$ ($\text{SD}{=}1.54$), and ARC-C Qwen ${-}5.42$ ($\text{SD}{=}0.16$).
14	Absolute $\ell_z^*$ thresholds would produce contradictory results: Qwen's contaminated $\ell_z^*$ at 15\% (${+}3.8$) is still positive.
15	The $\Delta\ell_z^*$ design normalizes these divergent baselines: Cohen's $d$ yields comparable effect sizes ($|d|{=}1.99$--$7.44$) despite order-of-magnitude differences.
16	Figure~\ref{fig:heatmap} provides a visual summary.
17	
18	\begin{table}[t]
19	\centering
20	\caption{Cohen's $d$ for $\Delta\ell_z^*$ across model families ($n{=}10$ clean seeds). Single-seed conditions: percentile bootstrap 95\% CI (10,000 resamples) reflecting clean-seed variability. Qwen MMLU 15\%/25\%/50\%: multi-seed mean $\pm$ SD ($n{=}3$ independent contamination runs). All exclude zero.}
21	\label{tab:cohens_d}
22	\footnotesize
23	\resizebox{\columnwidth}{!}{%
24	\begin{tabular}{@{}llrrrr@{}}
25	\toprule
26	Model & Bench. & $d$ (5\%) [CI] & $d$ (15\%) [CI] & $d$ (25\%) [CI] & $d$ (50\%) [CI] \\
27	\midrule
28	Qwen$^{\dagger}$ & MMLU & $-4.15$ [$-9.9$, $-2.7$] & $-5.36$ ($\pm$1.10) & $-7.44$ ($\pm$1.86) & $-5.08$ ($\pm$3.02) \\
29	Llama & MMLU & --- & $-2.11$ [$-4.8$, $-1.4$] & $-1.99$ [$-4.4$, $-1.3$] & $-2.33$ [$-5.1$, $-1.6$] \\
30	Mistral & MMLU & --- & $-3.01$ [$-8.2$, $-1.8$] & --- & $-3.50$ [$-9.4$, $-2.1$] \\
31	Qwen$^{\dagger}$ & ARC-C & --- & $+3.16$ [$2.0$, $9.5$] & --- & $+5.30$ [$3.6$, $15.2$] \\
32	\bottomrule
33	\multicolumn{6}{@{}l}{\scriptsize $^{\dagger}$15\%/25\%/50\%: multi-seed means ($n{=}3$ QLoRA runs); 5\%: single seed. Per-seed values in Appendix~\ref{app:reproducibility}.}
34	\end{tabular}}
35	\end{table}
36	
37	\begin{figure*}[t]
38	  \centering
39	  \includegraphics[width=\textwidth]{fig_heatmap.pdf}
40	  \caption{Cohen's $|d|$ heatmap (single-seed values; multi-seed means in Table~\ref{tab:cohens_d}). Blue intensity reflects effect-size magnitude. Grey cells: conditions not tested.}
41	  \label{fig:heatmap}
42	\end{figure*}
43	
44	\subsection{Model-Specific $\theta$-Shift Dynamics}
45	\label{sec:theta_dynamics}
46	
47	Contamination raises overall accuracy, which inflates $\hat{\theta}_{\text{MLE}}$; a higher $\hat{\theta}$ ``explains away'' anomalous successes on hard items, absorbing the contamination signal into the ability estimate.
48	We term this \emph{$\theta$-shift absorption}.
49	The magnitude of $\theta$-shift is comparable across families---Qwen ($\Delta\theta{=}0.47$ at 50\%) and Llama ($\Delta\theta{=}0.52$)---yet their fixed-$\theta$ amplification diverges markedly (Table~\ref{tab:theta_fixed}), indicating that $\theta$-shift magnitude alone does not predict fixed-$\theta$ benefit.
50	Figure~\ref{fig:theta_scatter} plots baseline accuracy against Cohen's $|d|$ for all model-benchmark combinations.
51	
52	$\theta$-shift absorption is the dominant source of detection variability for high-ability models at high contamination:
53	(i) fixed-$\theta$ estimation amplifies Qwen's multi-seed $|d|$ by 2.4$\times$ at 50\% ($5.08 \to 12.32$; Table~\ref{tab:theta_fixed}), while Llama shows no amplification ($0.4\times$);
54	(ii) $\theta$-anchoring reduces Qwen's inter-seed CV from 60\% to 19\%, confirming that training-run variance is driven by $\theta$-shift stochasticity rather than true signal variance;
55	(iii) the cross-model ranking under free-$\theta$ is seed-dependent at 50\%, making $\theta$-anchoring a necessary condition for reliable detection of high-ability models at high contamination.
56	
57	ARC-C reverses this pattern.
58	Despite Qwen's high baseline accuracy on ARC-C (89.7\%), contamination produces larger, not smaller, effect sizes ($|d|{=}3.16$ at 15\%, $|d|{=}5.30$ at 50\%).
59	This reversal reflects a ceiling effect: with only 295 items and 89.7\% baseline accuracy, the already-correct items offer minimal room for further $\theta$ inflation, so contamination manifests primarily as anomalous successes on the few remaining hard items.
60	The small item count amplifies this concentration, producing a disproportionately large $\ell_z^*$ shift per contaminated item.
61	
62	The baseline $\ell_z^*$ for ARC-C is negative ($-5.42$), reflecting the 4PL model's expectation of near-perfect performance; contamination pushes $\ell_z^*$ toward zero, producing the positive Cohen's $d$ values in Table~\ref{tab:cohens_d}.
63	
64	These findings indicate that detection sensitivity is not a fixed property of $\ell_z^*$ but depends on the interaction between model ability and benchmark characteristics, a consideration absent from standard person-fit applications.
65	
66	\paragraph{Fixed-$\theta$ estimation.}
67	Table~\ref{tab:theta_fixed} compares free-$\theta$ and fixed-$\theta$ Cohen's $d$ across all three families.
68	The benefit of fixed-$\theta$ is modulated by baseline $\ell_z^*$ level rather than $\theta$-shift magnitude.
69	Qwen (67.8\% accuracy, $\Delta\theta{=}0.47$, baseline $\ell_z^*{=}{+}8.68$) shows 2.4$\times$ amplification at 50\%: its large baseline departure from the IRT null provides substantial signal that free-$\theta$ absorption erodes, which $\theta$-anchoring recovers (multi-seed mean ${\ell_z^*}_{\text{fixed}} {=} 14.5$ vs.\ clean $7.35$).
70	Mistral (52.4\%, baseline $\ell_z^*{=}{+}4.02$) shows 1.7$\times$ at 50\%.
71	Llama (59.4\%, $\Delta\theta{=}0.39$ at 15\%, $0.52$ at 50\%) shows 0.4$\times$ at 50\% despite comparable $\theta$-shift: its near-zero baseline $\ell_z^*$ ($+0.26$) indicates that the clean response pattern conforms to IRT expectations, leaving no absorbed signal for $\theta$-anchoring to recover.
72	The amplification ratio tracks baseline $|\ell_z^*|$ monotonically ($8.68 {\to} 2.4{\times}$; $4.02 {\to} 1.7{\times}$; $0.26 {\to} 0.4{\times}$ at 50\%), making fixed-$\theta$ a targeted remedy for models with substantial baseline misfit, not a universal one.
73	
74	\begin{table}[t]
75	\centering
76	\caption{Free-$\theta$ vs.\ fixed-$\theta$ Cohen's $|d|$ on MMLU (bootstrap 95\% CI). Fixed-$\theta$ anchors $\hat{\theta}$ at the clean-model mean, eliminating $\theta$-shift absorption.}
77	\label{tab:theta_fixed}
78	\footnotesize
79	\resizebox{\columnwidth}{!}{%
80	\begin{tabular}{@{}lcccc@{}}
81	\toprule
82	Model & $|d_{\text{free}}|$ & $|d_{\text{fixed}}|$ & Ratio & Fixed CI \\
83	\midrule
84	\multicolumn{5}{@{}l}{\textit{5\% contamination}} \\
85	Qwen & 4.15 & 3.52 & 0.8$\times$ & [2.9, 5.7] \\
86	\addlinespace
87	\multicolumn{5}{@{}l}{\textit{15\% contamination}} \\
88	Qwen$^{\S}$ & 5.36 & 6.85 & 1.3$\times$ & ($\pm$1.80) \\
89	Llama & 2.11 & 0.58 & 0.3$\times$ & [0, 2.37]$^{\dagger}$ \\
90	Mistral$^{\ddagger}$ & 3.01 & 2.69 & 0.9$\times$ & [1.53, 9.06] \\
91	\addlinespace
92	\multicolumn{5}{@{}l}{\textit{50\% contamination}} \\
93	Qwen$^{\S}$ & 5.08 & 12.32 & 2.4$\times$ & ($\pm$2.38) \\
94	Llama & 2.33 & 0.84 & 0.4$\times$ & [0.17, 2.97] \\
95	Mistral$^{\ddagger}$ & 3.50 & 5.80 & 1.7$\times$ & [3.87, 18.45] \\
96	\bottomrule
97	\multicolumn{5}{@{}l}{\scriptsize $^{\dagger}$CI includes zero.} \\
98	\multicolumn{5}{@{}l}{\scriptsize $^{\S}$Multi-seed mean ($n{=}3$); CI column shows $\pm$SD of fixed-$\theta$ $|d|$.} \\
99	\multicolumn{5}{@{}l}{\scriptsize $^{\ddagger}$Fixed-$\theta$: 6 seeds (4--7 response vectors not retained in pipeline); free-$\theta$ uses all 10.}
100	\end{tabular}}
101	\end{table}
102	
103	\begin{figure}[t]
104	  \centering
105	  \includegraphics[width=\columnwidth]{fig_theta_scatter.pdf}
106	  \caption{Baseline accuracy vs.\ Cohen's $|d|$ for all model-benchmark combinations (single-seed values; multi-seed means in Table~\ref{tab:cohens_d}). Diamonds: 5\%; triangles: 15\%; squares: 25\%; circles: 50\%. ARC-C reversal reflects a ceiling effect.}
107	  \label{fig:theta_scatter}
108	\end{figure}
109	
110	\subsection{Detection-Diagnosis Tradeoff}
111	\label{sec:degradation}
112	
113	A natural question is whether the full 4PL IRT framework is necessary for contamination detection, or whether simpler statistics suffice.
114	Table~\ref{tab:degradation} compares three statistics at decreasing levels of information access: $\ell_z^*$ (requires 4PL parameters $a, b, c, d$), the HT statistic (requires only difficulty $b$), and an accuracy $z$-score (requires no item parameters).
115	
116	The comparison reveals a detection-diagnosis tradeoff.
117	For pure detection, simpler statistics are more powerful: accuracy $z$-scores yield $|d|$ values several-fold to over an order of magnitude larger than person-fit statistics (Table~\ref{tab:degradation}), because cross-seed accuracy variance is near-zero in controlled settings.
118	HT generally exceeds $\ell_z^*$ in detection strength, since HT is not attenuated by the Snijders correction for $\theta$ estimation uncertainty.
119	Both person-fit statistics exhibit seed-dependent non-monotonicity under free-$\theta$ estimation (Table~\ref{tab:degradation}), confirming that $\theta$-shift absorption affects all statistics conditioned on ability, not $\ell_z^*$ specifically.
120	
121	Yet the diagnostic power reverses.
122	Full IRT parameterization is unnecessary for mere detection, but the value of $\ell_z^*$ lies in three capabilities that HT and $z$-scores lack:
123	(a) \emph{seen/unseen decomposition}: $\ell_z^*$ can be computed separately on seen and unseen item subsets, though item-level detection is near-random (AUROC $\approx 0.53$; Appendix~\ref{app:item_auroc}), confirming that the contamination signal is diffuse and requires model-level aggregation;
124	(b) \emph{$\theta$-shift mechanism}: the ability parameter exposes why detection sensitivity depends on model ability (\S\ref{sec:theta_dynamics}), a mechanistic insight inaccessible to non-parametric statistics;
125	(c) \emph{structural sensitivity}: on real leaderboard data, $\ell_z^*$ flags 57/60 model-benchmark cells as aberrant---evidence of systematic IRT assumption violations that motivates the $\Delta\ell_z^*$ matched-difference design (\S\ref{sec:did}; Appendix~\ref{app:leaderboard_aberrance}).
126	Accuracy $z$-scores flag only 4/60 cells, making them insensitive to the response-pattern structure that $\ell_z^*$ exploits for within-model diagnosis.
127	While such patterns have theoretical antecedents in person-fit literature \citep{stonge2011}, the specific magnitude and model-dependence we observe are new empirical findings in the LLM domain; nonparametric alternatives \citep{tendeiro2014} may complement $\ell_z^*$ where 4PL calibration is unavailable.
128	
129	In practice, a two-stage workflow follows: screen using accuracy $z$-scores (Table~\ref{tab:degradation}), then apply $\ell_z^*$ to characterize whether the signal reflects $\theta$-shift absorption (indicating fixed-$\theta$ anchoring is needed) or uniform aberrance (suggesting direct memorization).
130	
131	Within the IRT family, the 4PL specification matters: simulation ablations show a mean $+$27.3pp power gain over 3PL on MMLU, because 46\% of MMLU items have upper asymptote $d < 0.95$, and the 3PL model (which assumes $d{=}1$) misattributes slip-related response patterns as aberrance (Appendix~\ref{app:4pl_ablation}).
132	
133	\begin{table}[t]
134	\centering
135	\caption{Detection-diagnosis tradeoff on MMLU: Cohen's $|d|$ across three statistics. Simpler statistics detect more powerfully; $\ell_z^*$ provides unique diagnostic capabilities (\S\ref{sec:degradation}).}
136	\label{tab:degradation}
137	\footnotesize
138	\begin{tabular}{@{}llrr@{}}
139	\toprule
140	Model & Statistic & $|d|$ (15\%) & $|d|$ (50\%) \\
141	\midrule
142	Qwen$^\dagger$ & $\ell_z^*$ & $5.36$ ($\pm$1.10) & $5.08$ ($\pm$3.02) \\
143	     & HT & $5.83$ ($\pm$1.30) & $5.29$ ($\pm$3.41) \\
144	     & Acc.\ $z$ & $45.0$ ($\pm$2.5) & $70.0$ ($\pm$1.1) \\
145	\addlinespace
146	Llama & $\ell_z^*$ & $2.11$ [$1.4$, $4.8$] & $2.33$ [$1.6$, $5.1$] \\
147	      & HT & $2.45$ [$1.5$, $4.3$] & $3.07$ [$1.9$, $5.3$] \\
148	      & Acc.\ $z$ & $22.5$ [$13.6$, $47.0$] & $32.8$ [$19.8$, $68.6$] \\
149	\addlinespace
150	Mistral & $\ell_z^*$ & $3.01$ [$1.8$, $8.2$] & $3.50$ [$2.1$, $9.4$] \\
151	      & HT & $4.36$ [$1.2$, $7.0$] & $5.89$ [$1.9$, $9.4$] \\
152	      & Acc.\ $z$ & $7.81$ [$4.4$, $14.4$] & $16.6$ [$9.7$, $34.6$] \\
153	\bottomrule
154	\multicolumn{4}{@{}p{0.9\columnwidth}}{\scriptsize $^\dagger$Qwen values are means across $n{=}3$ independent seeds (42, 123, 456); per-seed values in Appendix~\ref{app:reproducibility}. Llama and Mistral are single-seed with bootstrap CIs.}
155	\end{tabular}
156	\end{table}
157	
158	\subsection{Ability-Dependent Non-Monotonic Dose-Response}
159	\label{sec:inverted_u}
160	
161	As an exploratory observation, the free-$\theta$ dose-response is non-monotonic for Qwen.
162	The multi-seed mean trajectory ($|d|$: $4.15 \to 5.36 \to 7.44 \to 5.08$ at 5\%/15\%/25\%/50\%; Appendix~\ref{app:reproducibility}) shows signal peaking at 25\% before declining at 50\%, but the decline is attenuated relative to single-seed estimates and the inter-seed variance at 50\% is high (CV${=}$60\%, range $[1.90, 7.91]$).
163	This non-monotonicity is a $\theta$-estimation artifact: fixed-$\theta$ analysis eliminates the inverted-U and reveals a strong positive dose-response (mean $|d|$: $5.89$ at 25\% vs.\ $12.32$ at 50\%, no seed-level overlap), while reducing the 50\% CV to 19\%.
164	Llama shows an approximately flat dose-response ($|d|{=}2.11 \to 1.99 \to 2.33$), consistent with its near-zero $\ell_z^*$ baseline ($+0.26$ vs.\ ${+}8.68$ for Qwen) despite comparable $\theta$-shift ($\Delta\theta{=}0.52$ vs.\ $0.47$).
165	The mechanism is predictable from simulation (Appendix~\ref{app:simulation}): at moderate contamination, aberrant responses dominate; at high contamination, inflated $\hat{\theta}$ absorbs the anomaly---but the magnitude is highly seed-dependent.
166	
167	A simulated power analysis corroborates these findings: two-sided testing (flagging both large negative and large positive $\ell_z^*$) achieves ${>}$93\% power on MMLU at all contamination levels, with the theoretical power function yielding $R^2 {=} 0.957$ against simulated values (Appendix~\ref{app:simulation}).
168	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b2dcdd2f-38ee-4d0f-8d6f-b981d14f7df3",
  "isSidechain": true,
  "promptId": "db957384-5e7f-4db3-aba3-2ab2a6e43bac",
  "agentId": "a760df4be266cc066",
  "type": "user",
  "uuid": "e8f741dd-ebf8-4d51-87aa-6b89fa7afead",
  "sourceToolAssistantUUID": "b2dcdd2f-38ee-4d0f-8d6f-b981d14f7df3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_51ea7db2",
  "sessionId": "16ee981e-ef12-42ca-ad7f-0e04fded96ed",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "concurrent-knitting-hare"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-23T22:23:27.538Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RhxWKwVbfZM3dwDrYJCgZ6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8f741dd-ebf8-4d51-87aa-6b89fa7afead",
  "isSidechain": true,
  "agentId": "a760df4be266cc066",
  "requestId": "req_011CbLHMUu22LeBUYEURaG39",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4751fafc-983f-4e44-b56d-9013444600a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_51ea7db2",
  "sessionId": "16ee981e-ef12-42ca-ad7f-0e04fded96ed",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "concurrent-knitting-hare",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NnrDoPTR58kwbL8NeB8PvY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 29750,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 29750,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-23T22:23:27.552Z_

<details><summary>↩ Tool result · `toolu_01RhxWKwVbfZM3dwDrYJCgZ6`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	Our findings reveal both the strengths and boundaries of IRT person-fit for contamination detection: $\ell_z^*$ reliably detects SFT-stage contamination across model families, but three boundary conditions constrain its practical utility.
4	
5	\paragraph{Characterization over tool.}
6	The detection-diagnosis tradeoff (\S\ref{sec:degradation}) shows that simpler statistics detect contamination more powerfully than $\ell_z^*$: accuracy $z$-scores yield $|d|$ values several-fold to over an order of magnitude larger, and HT generally exceeds $\ell_z^*$.
7	The value of the IRT framework lies not in detection power but in mechanistic understanding: the $\theta$-shift analysis reveals \emph{why} detection sensitivity varies across models and contamination levels, the seen/unseen decomposition identifies \emph{what fraction} of items are memorized, and the 4PL parameterization captures item-level ceiling effects that 3PL misattributes as aberrance.
8	These diagnostic capabilities are invisible to accuracy $z$-scores or HT.
9	Findings~1--2 are theoretically predictable from IRT principles; our contribution lies in quantifying these effects in the LLM setting, where the magnitude and boundary conditions are not derivable from theory alone.
10	
11	\paragraph{Practical implications.}
12	Two results have immediate consequences.
13	Free-$\theta$ estimation produces seed-dependent dose-response curves (CV up to 60\%); anchoring $\theta$ to a pre-contamination baseline stabilizes detection and amplifies the signal for models whose clean $\ell_z^*$ departs substantially from zero.
14	The benchmark size boundary means $\ell_z^*$ is most informative for large benchmarks ($n \approx 8{,}000$ items for 80\% power at 15\% contamination); on small benchmarks like ARC-C (295 items), detection relies on concentrated contamination effects.
15	
16	\paragraph{Scope and calibration.}
17	Universal baseline misfit (57/60 cells flagged) confirms systematic IRT violations; the $\Delta\ell_z^*$ design turns this into a feature through within-model differencing.
18	PSN-IRT provides pre-calibrated 4PL parameters \citep{psnirt2026}, but classical calibration fails on contaminated data ($r_a{=}0.127$; Appendix~\ref{app:mml_em}); the calibration sample (13,000+ models) may itself include contaminated ones, though individual contamination effects are diluted across models.
19	The robustness analysis (Appendix~\ref{app:param_perturb}) provides partial reassurance (${\pm}10\%$ noise tolerance).
20	\paragraph{Information requirements and method positioning.}
21	$\ell_z^*$ sits below MIA \citep[logits;][]{minkprob2024} and ConStat \citep[multi-benchmark scores;][]{constat2024} in an information-requirements hierarchy, needing only single-benchmark binary patterns and an external item bank---suited to retrospective audits where logits are unavailable. Our GRPO pilot directly confirms this advantage: Min-K\% AUC degrades from $0.611$ (SFT) to $0.493$ (post-RL), indistinguishable from chance, while $\ell_z^*$ signal persists (${\sim}3.3$; Figure~\ref{fig:grpo}), demonstrating that response-pattern anomalies survive RL alignment that eliminates memorization-based features \citep{wang2025fragility}.
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4751fafc-983f-4e44-b56d-9013444600a6",
  "isSidechain": true,
  "promptId": "db957384-5e7f-4db3-aba3-2ab2a6e43bac",
  "agentId": "a760df4be266cc066",
  "type": "user",
  "uuid": "c2f77da7-6976-4220-88e3-b0112bd583ee",
  "sourceToolAssistantUUID": "4751fafc-983f-4e44-b56d-9013444600a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_51ea7db2",
  "sessionId": "16ee981e-ef12-42ca-ad7f-0e04fded96ed",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "concurrent-knitting-hare"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-23T22:23:27.831Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NdrQ6PmCrg7uZizmS7sYsy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2f77da7-6976-4220-88e3-b0112bd583ee",
  "isSidechain": true,
  "agentId": "a760df4be266cc066",
  "requestId": "req_011CbLHMUu22LeBUYEURaG39",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "98225eff-0b41-4088-a0ff-ee9eb4547784",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_51ea7db2",
  "sessionId": "16ee981e-ef12-42ca-ad7f-0e04fded96ed",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "concurrent-knitting-hare",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NnrDoPTR58kwbL8NeB8PvY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 29750,
      "cache_read_input_tokens": 0,
      "output_tokens": 484,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 29750
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 484,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 29750,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 29750,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-23T22:23:27.839Z_

<details><summary>↩ Tool result · `toolu_01NdrQ6PmCrg7uZizmS7sYsy`</summary>

```text
1	\section*{Limitations}
2	
3	Our controlled experiments cover three 7--8B model families with QLoRA fine-tuning; generalization to larger scales, mixture-of-experts architectures, full-parameter fine-tuning, and pretraining-stage contamination remains untested.
4	Most contamination conditions use a single training run, and multi-seed replication (available for Qwen) reveals high seed dependence at 50\% contamination (CV${=}$60\%), partially resolved by $\theta$-anchoring; the post-RL characterization is $N{=}1$.
5	The framework depends on pre-calibrated 4PL item parameters from PSN-IRT, whose calibration sample may include contaminated models, and we do not provide head-to-head comparison with logit-based methods (MIA, ConStat) that operate at a different information level.
6	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98225eff-0b41-4088-a0ff-ee9eb4547784",
  "isSidechain": true,
  "promptId": "db957384-5e7f-4db3-aba3-2ab2a6e43bac",
  "agentId": "a760df4be266cc066",
  "type": "user",
  "uuid": "db2aa140-eb25-46ec-adc9-8a8dac51304b",
  "sourceToolAssistantUUID": "98225eff-0b41-4088-a0ff-ee9eb4547784",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_51ea7db2",
  "sessionId": "16ee981e-ef12-42ca-ad7f-0e04fded96ed",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "concurrent-knitting-hare"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-23T22:25:57.247Z_

---

## 任务 1: Introduction Hook

**当前开头（L1-5）：**

> Benchmark contamination, the unintended inclusion of evaluation data in training corpora, poses a growing threat to the integrity of large language model (LLM) evaluation. As training corpora and public benchmarks both expand, the probability of overlap increases structurally. When contamination occurs, benchmark scores no longer reflect genuine capability, undermining the primary mechanism by which the community compares and selects models.

**评估：** 这是典型的"定义问题 → 指出问题在扩大 → 说明后果"三段式开场。功能上完整，但读感平淡——reviewer 在审 50 篇论文时不会被这种 generic statement 抓住。三句话没有一个具体数字或案例，读者还没产生"这件事很紧迫"的直觉。

**建议替代文本（两种方案）：**

**方案 A：用 RL 失效的反直觉事实开场（与本文核心动机对齐）**

> Ten log-probability-based contamination detectors, evaluated across four benchmarks, all perform at chance level on models trained with reinforcement learning \citep{wang2025fragility}. The reason is simple: RL reshapes internal token distributions while preserving the binary correctness patterns that benchmarks actually record. This gap---methods that require privileged access failing precisely when models become more opaque---motivates a fundamental question: what can binary response patterns alone reveal about contamination?

优势：第一句就给出具体数字（10 methods, 4 benchmarks, chance level），制造认知冲击；直接引出本文的核心定位（binary-only detection）。当前文本把 Wang et al. 的发现放在 L20-22（第四段），太迟了。

**方案 B：用 57/60 的经验数据开场（更大胆）**

> Fifty-seven of sixty model-benchmark combinations we examine produce statistically aberrant response patterns under Item Response Theory---even without contamination. This universal misfit means no absolute threshold can distinguish contaminated from clean models. Yet when we difference against a clean baseline, the contamination signal emerges reliably across three model families, revealing a detection pathway that requires no model weights, no logits, and no training data.

优势：用本文自己的发现开场，立即展示贡献的独特性。风险是 reviewer 可能认为 opening 太 results-heavy。

**推荐方案 A**。它同时完成了三件事：(1) 具体数据点制造紧迫感，(2) 精确定位本文动机，(3) 让当前第四段的内容提前发挥作用，避免前三段"铺背景"的冗余感。当前第一段可压缩为一句放在方案 A 之后作为补充。

---

## 任务 2: Transition 检查

### 2.1 Introduction 结尾 → Related Work 开头

**Introduction 结尾（L49-53）：**
> Our contributions are threefold: (1) ... (2) ... (3) ... Findings 1--2 are confirmatory; Finding 3 is exploratory.

**Related Work 开头（L1-4）：**
> Benchmark contamination detection methods span a wide range of information requirements. Corpus-search methods match benchmark items directly against pretraining data...

**评估：断裂较小但缺乏逻辑桥。** Introduction 以贡献列表结束，Related Work 直接跳到方法分类，没有"我们的方法在这个生态中处于什么位置"的衔接。读者需要自行推断两段的关系。

**建议：** 在 Related Work 开头加一句定位句：

> Our framework positions at the minimal end of information requirements: only binary response patterns and externally calibrated item parameters. We next situate this positioning within three lines of related work.

或者更简洁地，将 Related Work 第一句改为：

> Contamination detection methods can be organized by their information requirements---from full corpus access to binary response patterns---and our approach occupies the minimal end of this spectrum.

### 2.2 Related Work 结尾 → Method 开头

**Related Work 结尾（L33-34）：**
> Our work transfers this psychometric toolkit to LLM evaluation, treating each model as an examinee whose item-level response pattern may reveal memorization.

**Method 开头（L1-8）：**
> We adopt the four-parameter logistic (4PL) IRT model to characterize contamination-induced aberrance in LLM response patterns.

**评估：衔接良好。** Related Work 结尾明确说"我们把这个工具迁移到 LLM"，Method 开头紧接着说"我们采用 4PL 模型"。逻辑连贯，无需修改。

### 2.3 Method 结尾 → Results 开头

**Method 结尾（L63-64）：**
> Our findings are scoped to SFT-based contamination and may not generalize to pretraining contamination, which operates through different learning dynamics.

**Results 开头（L4-8）：**
> Table~\ref{tab:cohens_d} presents Cohen's $d$ effect sizes for $\ell_z^*$ across three model families and two benchmarks. All confidence intervals exclude zero...

**评估：轻微断裂。** Method 以 scope caveat 结束（防御性语气），Results 直接跳到报数字，中间缺少"我们按上述设计跑了什么、现在报告结果"的过渡。不严重但可改进。

**建议：** Results 开头加一句过渡：

> We first examine whether $\Delta\ell_z^*$ reliably separates contaminated from clean models across families and benchmarks, then analyze the mechanisms driving detection sensitivity.

### 2.4 Results 各 subsection 之间的过渡

**4.1 → 4.2（L16 → L44-47）：**
> Figure~\ref{fig:heatmap} provides a visual summary.
→ Contamination raises overall accuracy, which inflates $\hat{\theta}_{\text{MLE}}$...

**评估：断裂明显。** 4.1 以"看图"结束，4.2 直接跳到 θ-shift 机制解释，没有说明"为什么跨 family 效果差异大"这个 4.1 遗留的问题是 4.2 要回答的。

**建议：** 在 4.2 开头加一句：

> The cross-family variation in Table~\ref{tab:cohens_d}---Qwen's $|d|$ declining from 25\% to 50\% while Llama's increases---suggests that detection sensitivity depends on more than contamination dose. The mechanism is $\theta$-shift absorption.

**4.2 → 4.3（L72 → L110-113）：**
> ...making fixed-$\theta$ a targeted remedy for models with substantial baseline misfit, not a universal one.
→ A natural question is whether the full 4PL IRT framework is necessary for contamination detection, or whether simpler statistics suffice.

**评估：衔接可以。** "A natural question" 是一种常见但有效的过渡手法。可以更具体一点。

**建议（微调即可）：**
> Having established that $\theta$-anchoring matters for high-ability models, a natural question follows: is the full 4PL framework itself necessary, or do simpler statistics suffice?

**4.3 → 4.4（L156 → L158-161）：**
> ...per-seed values in Appendix~\ref{app:reproducibility}. [table ends]
→ As an exploratory observation, the free-$\theta$ dose-response is non-monotonic for Qwen.

**评估：衔接弱。** Table 脚注之后直接跳到新现象，没有过渡。

**建议：**
> The preceding analysis treats each contamination level independently. We next examine how detection sensitivity varies \emph{across} doses, revealing an unexpected non-monotonicity.

### 2.5 Results 结尾 → Discussion 开头

**Results 结尾（L167-168）：**
> ...with the theoretical power function yielding $R^2{=}0.957$ against simulated values (Appendix~\ref{app:simulation}).

**Discussion 开头（L1-3）：**
> Our findings reveal both the strengths and boundaries of IRT person-fit for contamination detection: $\ell_z^*$ reliably detects SFT-stage contamination across model families, but three boundary conditions constrain its practical utility.

**评估：衔接可以。** Discussion 开头做了一个 high-level summary，功能上合理。但"three boundary conditions"的预告和后面的 paragraph 标题不完全对应（实际有四个 paragraph），建议要么改数字要么调整 paragraph 结构。

---

## 任务 3: Prose Tightening

### Introduction

**1. L7: "A range of detection methods have been proposed, but all require some form of privileged access beyond the binary response record."**

"some form of privileged access beyond the binary response record" → "privileged access beyond binary responses"

原文 18 词 → 建议 12 词。省 6 词。

**2. L12: "These methods form a detection frontier ordered by information access."**

"detection frontier ordered by information access" 这个隐喻在后面没有展开，且和 Related Work 里的 "information requirements" 术语不一致。建议删除整句或改为更直接的表述：

→ "Each requires access unavailable for closed-source models."

**3. L13: "No existing method operates using only binary response patterns, without model weights, gradients, logits, or training data---though, as we show, effective detection additionally requires externally calibrated item parameters."**

过长（30 词）。"operates using" → "operates on"；破折号后的 caveat 可以移到 framework 介绍处。

→ "No existing method operates on binary response patterns alone." 后面的 caveat 在 L38 已经说了（"pre-calibrated 4PL item parameters"）。省 ~20 词。

**4. L15-18: SFT focus 的三个 reasons**

"we focus on SFT-stage contamination---where benchmark answers are explicitly included in fine-tuning data---for three reasons" 中破折号里的解释和 L63 重复。删除 L15 的破折号插入语。省 ~10 词。

**5. L20: "The need for detection from binary response patterns grows more pressing as models evolve."**

"grows more pressing" 是 hedging + 空泛。可以删掉整句，直接用 Wang et al. 的结果开场：

→ "\citet{wang2025fragility} show that..." 省 15 词。

**6. L37: "Rather than proposing $\ell_z^*$ as a ready-to-deploy detection tool, we characterize the behavior boundaries of IRT person-fit statistics for LLM contamination detection."**

"Rather than proposing ... as a ready-to-deploy detection tool" 是防御性 framing，建议简化：

→ "We characterize the behavior boundaries of IRT person-fit statistics for LLM contamination detection, rather than proposing a deployment-ready tool." 重心前移。

### Related Work

**7. L9: "\citet{zhou2023benchmark} and \citet{sainz2023} argue for systematic contamination measurement, \citet{jacovi2023} propose mitigation strategies, and \citet{bordt2025forget} show that contamination can be 'forgotten' under sufficient continued training."**

一句话塞了四篇 citation，信息密度低但句子长。如果这些 citation 对本文论点不核心，考虑删减或移入 parenthetical：

→ "Several works address contamination measurement and mitigation more broadly \citep{zhou2023benchmark, sainz2023, jacovi2023, bordt2025forget}." 省 ~25 词。

**8. L19-24（IRT for LLM evaluation 段落）：**

前四句（L19-23）每句都是 "Author did X" 的平行结构，读感单调。建议把前两句合并：

> "IRT has been applied to ML classifiers \citep{martinezplumed2019} and DNN-generated response patterns \citep{lalor2019}, establishing that item parameters capture meaningful variation across models."

省 ~15 词，减少机械罗列感。

### Method

**9. L23: "LLM response patterns systematically violate IRT assumptions of local independence and unidimensionality."**

好句子，但 "systematically" 可以删——"violate" 已经够强了，后面 57/60 的数据支撑强度。省 1 词。

**10. L46: "Each is fine-tuned with QLoRA (rank=16, α=32) under clean and contaminated conditions at varying levels: at X% contamination, X% of SFT training examples are benchmark items (questions paired with gold answers in the standard evaluation format), with the remainder drawn from a general instruction-following dataset."**

一句话 50+ 词。拆分：

→ "Each is fine-tuned with QLoRA (rank=16, α=32). At $X$\% contamination, $X$\% of SFT training examples are benchmark items (questions paired with gold answers); the remainder are from a general instruction-following dataset."

省 ~10 词，可读性提升。

### Results

**11. L47-48 (4.2): "Contamination raises overall accuracy, which inflates $\hat{\theta}_{\text{MLE}}$; a higher $\hat{\theta}$ 'explains away' anomalous successes on hard items, absorbing the contamination signal into the ability estimate."**

第二个分句重复第一个分句的逻辑。可以合并：

→ "Contamination inflates $\hat{\theta}_{\text{MLE}}$, which absorbs anomalous successes on hard items into the ability estimate---a phenomenon we term \emph{$\theta$-shift absorption}."

省 ~15 词。

**12. L113-114: "A natural question is whether the full 4PL IRT framework is necessary for contamination detection, or whether simpler statistics suffice."**

"A natural question is whether...or whether..." → 可以更直接：

→ "Is the full 4PL framework necessary, or do simpler statistics suffice?" 省 10 词。

**13. L117-118: "accuracy $z$-scores yield $|d|$ values several-fold to over an order of magnitude larger than person-fit statistics"**

"several-fold to over an order of magnitude" 措辞冗长但信息量高（保留具体数字很好），可微调：

→ "accuracy $z$-scores yield $|d|$ values 4--14$\times$ larger than person-fit statistics" （用实际数据区间替代模糊描述）。

### Discussion

**14. L6-8: "The value of the IRT framework lies not in detection power but in mechanistic understanding: the $\theta$-shift analysis reveals \emph{why} detection sensitivity varies across models and contamination levels, the seen/unseen decomposition identifies \emph{what fraction} of items are memorized, and the 4PL parameterization captures item-level ceiling effects that 3PL misattributes as aberrance."**

一句话 55 词。建议拆：

→ "The value of the IRT framework lies in mechanistic understanding, not detection power. $\theta$-shift analysis reveals \emph{why} sensitivity varies across models; seen/unseen decomposition identifies \emph{what fraction} of items are memorized; and 4PL parameterization captures ceiling effects that 3PL misattributes as aberrance."

**15. L9: "Findings 1--2 are theoretically predictable from IRT principles; our contribution lies in quantifying these effects in the LLM setting, where the magnitude and boundary conditions are not derivable from theory alone."**

和 Introduction L49-50 高度重复。Discussion 应该深化而非重述。建议删除或替换为更具体的讨论（比如具体哪个 magnitude 是 surprising）。

### Limitations

**16. 整段只有两句话（L3-5），第二句 85 词，密度过高。** 拆成 3 句：

→ "Most contamination conditions use a single training run. Multi-seed replication for Qwen reveals high seed dependence at 50\% contamination (CV=60\%), partially resolved by $\theta$-anchoring. The post-RL characterization is $N{=}1$."

**估计总节省：~150-180 词。** 对 8 页限制有实质帮助。

---

## 任务 4: Table/Figure Caption 自包含性

### Figure 1 (fig:motivation, Introduction L33)
> "A clean model's responses track the IRT-predicted probability curve (left); a contaminated model shows anomalous successes on hard items (right, red diamonds), producing a large $|\Delta\ell_z^*|$ signal."

**评估：基本自包含。** 读者能理解图在说什么。**需补充：**
- X 轴和 Y 轴的含义未说明（推测 X=item difficulty, Y=P(correct)）
- 未说明用的是什么模型/benchmark（即使是示意图也应注明 "Illustrative example" 或标注具体模型）

→ 建议修改：
> "A clean model's response pattern (left) tracks the IRT-predicted probability curve ($x$-axis: item difficulty $b_i$; $y$-axis: observed accuracy). A contaminated model (right) shows anomalous successes on hard items (red diamonds), producing a large $|\Delta\ell_z^*|$ signal. Illustrative; see \S\ref{sec:detection} for empirical results."

### Table 1 (tab:cohens_d, Results L20-21)
> "Cohen's $d$ for $\Delta\ell_z^*$ across model families ($n{=}10$ clean seeds). Single-seed conditions: percentile bootstrap 95\% CI (10,000 resamples) reflecting clean-seed variability. Qwen MMLU 15\%/25\%/50\%: multi-seed mean $\pm$ SD ($n{=}3$ independent contamination runs). All exclude zero."

**评估：自包含。** 解释了 CI 的来源、multi-seed 标记、核心结论。唯一问题是 "All exclude zero" 对 CI 的指代略模糊（是所有 CI 都 exclude zero，还是所有 $d$ 值？）。建议改为 "All 95\% CIs exclude zero."

### Figure 2 (fig:heatmap, Results L40)
> "Cohen's $|d|$ heatmap (single-seed values; multi-seed means in Table~\ref{tab:cohens_d}). Blue intensity reflects effect-size magnitude. Grey cells: conditions not tested."

**评估：需补充。**
- 未说明 heatmap 的行列分别是什么（模型 × 污染比例？模型 × benchmark？）
- 未说明数值范围

→ 建议修改：
> "Cohen's $|d|$ heatmap across model families (rows) and contamination levels (columns) on MMLU and ARC-C. Blue intensity reflects effect-size magnitude; values shown in cells. Grey: conditions not tested. Single-seed values; multi-seed means in Table~\ref{tab:cohens_d}."

### Table 2 (tab:theta_fixed, Results L76-77)
> "Free-$\theta$ vs.\ fixed-$\theta$ Cohen's $|d|$ on MMLU (bootstrap 95\% CI). Fixed-$\theta$ anchors $\hat{\theta}$ at the clean-model mean, eliminating $\theta$-shift absorption."

**评估：自包含。** 解释了 fixed-θ 的含义。脚注补充了 multi-seed 和缺失数据的说明。无需修改。

### Figure 3 (fig:theta_scatter, Results L106)
> "Baseline accuracy vs.\ Cohen's $|d|$ for all model-benchmark combinations (single-seed values; multi-seed means in Table~\ref{tab:cohens_d}). Diamonds: 5\%; triangles: 15\%; squares: 25\%; circles: 50\%. ARC-C reversal reflects a ceiling effect."

**评估：基本自包含。** marker 形状的图例写在 caption 中是好做法。**需补充：**
- 未标注颜色编码（是否不同模型用不同颜色？）
- "ARC-C reversal" 对只看图的读者可能不够明确——正值 vs 负值的含义

→ 建议追加：
> "Colors distinguish model families (see legend). ARC-C points (positive $d$) reverse the MMLU pattern due to ceiling effects (\S\ref{sec:theta_dynamics})."

### Table 3 (tab:degradation, Results L135-136)
> "Detection-diagnosis tradeoff on MMLU: Cohen's $|d|$ across three statistics. Simpler statistics detect more powerfully; $\ell_z^*$ provides unique diagnostic capabilities (\S\ref{sec:degradation})."

**评估：自包含。** 三个统计量名称在表头出现，caption 解释了核心 message。建议微调：在 caption 末尾加一句说明三个统计量的 information requirement 差异（这是 tradeoff 的核心维度）。

→ 追加：
> "$\ell_z^*$ requires full 4PL parameters; HT requires only difficulty; accuracy $z$-score requires no item parameters."

### 汇总

| 图表 | 状态 | 主要问题 |
|------|------|---------|
| Figure 1 | 需补充 | 缺轴标签说明，缺模型/数据标注 |
| Table 1 | 自包含 | "All exclude zero" 指代略模糊 |
| Figure 2 | 需补充 | 缺行列语义说明 |
| Table 2 | 自包含 | -- |
| Figure 3 | 需补充 | 缺颜色编码说明 |
| Table 3 | 需补充 | 缺三个统计量的信息需求差异说明 |
| Discussion Figure (fig:grpo) | 未在已读文件中看到 caption | 在正文 L21 引用但未看到 figure 环境——可能在其他文件中，需确认 caption 是否自包含 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db2aa140-eb25-46ec-adc9-8a8dac51304b",
  "isSidechain": true,
  "agentId": "a760df4be266cc066",
  "requestId": "req_011CbLHN8n5bKFADeWqas2V2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6c115fda-7726-4151-878e-a7cfec7476fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/agent_51ea7db2",
  "sessionId": "16ee981e-ef12-42ca-ad7f-0e04fded96ed",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "concurrent-knitting-hare",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019vhoH19f4Bx1cAn4F2V1em",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13489,
      "cache_read_input_tokens": 29750,
      "output_tokens": 5980,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13489
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5980,
          "cache_read_input_tokens": 29750,
          "cache_creation_input_tokens": 13489,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13489,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---
