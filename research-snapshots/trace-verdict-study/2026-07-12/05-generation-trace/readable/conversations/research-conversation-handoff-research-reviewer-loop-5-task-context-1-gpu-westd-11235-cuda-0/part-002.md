# Research conversation: [HANDOFF] 你是 Research Reviewer，这是 Loop #5。 ## 上一轮交接 (task_context) ### 1. 🔴 硬约束 / 红线 - GPU 白名单：westd-11235 上仅 `cuda:0` 和 — Part 2 of 2

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../research-conversation-handoff-research-reviewer-loop-5-task-context-1-gpu-westd-11235-cuda-0.md) · [Structured JSON](../../../sessions/4c/4cd27a530898df531c15.json)

## Round 7

### Tool call

_source line 168 · 2026-05-15T19:23:22.553Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__reviewer_post_to_director · `toolu_01DRjFTH6tKr7JBAiLuHZm46`</summary>

```json
{
  "text": "[写作评审] 轮次 3/5\n\n维度评分（1-4，4 为最好）：\n- Originality: 3     ← 首个 verdict prediction 组件消融 + 信息密度分解框架，有新意\n- Clarity: 3         ← 结构清晰，表格设计好，统计报告规范\n- Soundness: 3       ← 所有定量 claim 均与 registry 数据一致，统计检验完备\n- Significance: 2    ← 实用 takeaway 窄（单数据集），\"exception 预测 failure\" 可能被质疑近乎循环\n- Presentation: 3    ← 排版干净，25 篇引用（从 7 篇大幅改善），附录完整\n\nOverall（1-10，10 为最好）: 6\n\n## Round 2 修复验证\n\n6/6 claimed fixes 全部确认：\n- ✅ #1: McNemar → paired bootstrap (B=10,000) — experiments.tex 正确\n- ✅ #2: Table 1 CI [99.58, 100.00] 确认\n- ✅ #3: fig2 caption \"The Tier~1 condition (exception_only)\" 匹配 4-panel 设计\n- ✅ #4: Brier \"indicates substantial miscalibration\" 替换了 \"approaches theoretical maximum\"\n- ✅ #5: no_trace ECE 0.172→0.171（表 + 正文统一）\n- ✅ #6: gradient_accumulation=8, effective batch=32，与代码 line 151 一致\n\n## 数据一致性全面核验\n\n逐表对照 registry，**所有数字均正确**：\n- Table 1 (cross_model): 8 个准确率 + 6 组 CI 全部匹配 ✓\n- Table 2 (ablation): 7 个条件 × (accuracy + CI) 全部匹配 ✓\n- Table 3 (density): 分解比例 26%/74% 计算正确 (4.46/17.65=25.27%≈26%) ✓\n- Table 4 (calibration): ECE + Brier 10 个值全部与 calibration_analysis_seed42 一致 ✓\n- Appendix Table 5 (per-class): 抽查 3 行（Qwen exception_only, DeepSeek VOTA, DeepSeek exception_only）手工计算均正确 ✓\n- Seed robustness: σ=0, 3 seeds 99.83%，error IDs 901/905 ✓\n- p-values: ae vs exc p=0.80, exc vs VOTA p=0.01, label_only vs full_trace p<0.0001 ✓\n\n## 具体问题\n\n### Warnings（3 个）\n\n- [severity: warning] **Table 1 脚注 ‡ 根因描述不准确**（experiments.tex）。脚注写 \"invalidated due to an evaluate.py truncation mismatch between training and evaluation\"，但 registry 记录的根因是**训练时 label 被截断**（DeepSeek tokenizer 生成 >2048 tokens → SFTTrainer 右截断 → 分类 label 丢失 → LoRA 未学到分类行为）。eval 不匹配只是发现过程中的中间步骤。建议修改为：\"invalidated because the DeepSeek tokenizer produced sequences exceeding 2,048 tokens, causing the verdict label to be truncated during training; the model consequently failed to learn the classification task.\"\n\n- [severity: warning] **\"Model-Agnostic\" 标题 claim 过强**。标题 \"Model-Agnostic Fault Detection\" 基于 n=2 模型（均为 ~7B decoder-only instruction-tuned code LLM）。虽然 Limitations §4.5 承认了 \"only two models at the 7B parameter scale\"，但标题和摘要未加限定。EMNLP 审稿人极可能攻击这一点。建议：(a) 标题改为 \"Cross-Model\" 而非 \"Model-Agnostic\"；或 (b) 在摘要中加 \"across two model families\" 等限定语，降低 claim 强度。\n\n- [severity: warning] **Exception signal 近循环性未讨论**。对于失败测试，exception event 本质上直接编码了\"执行出错\"这一事实；对于通过测试，无 exception → 模型只需检测\"有无 exception\"。这使得 exception_only 接近一个 trivially solvable task。论文未讨论这一点。审稿人可能质疑：\"exception 预测 failure 本身几乎是同义反复，Tier 1 的 99.8%+ 并不令人意外。\" Discussion §4.1 解释了 \"why exception events dominate\"，但没有承认任务本身对 exception 信号近乎 trivial。建议在 Discussion 或 Limitations 中加一段：承认 exception_only 本质上是 fault indicator presence detection，真正的贡献在于 (a) 量化了为什么添加更多信息反而 hurt，(b) 跨模型对比表明即使是 trivial signal 在 VOTA 混合后也会退化。\n\n### Info（2 个）\n\n- [severity: info] **800 functions → 5910 samples 未解释**。Method §2.2 说 \"a benchmark of 800 Python functions\"，但数据集为 4720 train + 1190 test = 5910 samples。CRUXEval 原始为 800 input-output pairs。如何扩展到 5910 samples 的过程应简要说明（多测试输入/TracePile 扩展？），否则审稿人会追问。\n\n- [severity: info] **ae_only Brier vs exception_only Brier 显示精度**。两者在表中均显示为 0.001，但实际值为 0.000847 vs 0.001311（差 55%）。不影响结论，但如果审稿人试图复现精确值可能困惑。可考虑多保留一位小数（0.0008 vs 0.0013）。\n\n## Round 1 三个 Critical 状态\n\n1. ~~gradient_accumulation=4~~ → 已修正为 8 ✅\n2. ~~truncation 策略描述错误~~ → method.tex 正确描述 label-preserving truncation ✅\n3. ~~wang2025dcsh 占位符引用~~ → bib 条目完整（title/authors/venue/url）✅\n\n**全部 Critical 已清零。**\n\n## 整体评估\n\n论文从 Round 1 (Overall=4, 3 criticals) 显著改善至当前 (Overall=6, 0 criticals, 3 warnings)。数据完整性无硬伤，统计方法规范，25 篇引用覆盖合理。主要弱点是：(1) 单数据集限制，(2) exception signal 近循环性未讨论，(3) 标题 claim 过强。这些是 presentation/framing 问题，非数据/方法硬伤，可在下一轮快速修复。\n\n论文距 ARR May 25 提交基本就绪。建议 Round 4 聚焦修复上述 3 个 warning（特别是 Table 1 脚注和 Discussion circularity 段落），之后可收敛。",
  "project": "trace-verdict-study"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "37afc49e-e8e9-4c85-aa76-bfcb18ecb40a",
  "isSidechain": false,
  "requestId": "req_011Cb4u6VTDtFXwUoBEBykTc",
  "type": "assistant",
  "uuid": "931bf68e-6094-4929-b39c-902c785d02de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/reviewer_4eb9adda",
  "sessionId": "f3ca64e3-2194-4cc3-ae32-366bb9225676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EY34ZVgADUcWcWe2NunXr7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11388,
      "cache_read_input_tokens": 127333,
      "output_tokens": 2190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11388,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2190,
          "cache_read_input_tokens": 127333,
          "cache_creation_input_tokens": 11388,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11388
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

_source line 169 · 2026-05-15T19:23:26.173Z_

<details><summary>↩ Tool result · `toolu_01DRjFTH6tKr7JBAiLuHZm46`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_32bf96185a4c2e36ec51db573ff4edaa:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "931bf68e-6094-4929-b39c-902c785d02de",
  "isSidechain": false,
  "promptId": "15f84573-d748-42a3-bb84-7f9d95774f92",
  "type": "user",
  "uuid": "1a2d44ca-8762-475d-9d6f-6a7d59bcf98d",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"director_session\\\": \\\"feishu:group:oc_32bf96185a4c2e36ec51db573ff4edaa:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_32bf96185a4c2e36ec51db573ff4edaa:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "931bf68e-6094-4929-b39c-902c785d02de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/reviewer_4eb9adda",
  "sessionId": "f3ca64e3-2194-4cc3-ae32-366bb9225676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 170_

```json
{
  "type": "ai-title",
  "aiTitle": "Review loop 5 training status and paper critical fixes",
  "sessionId": "f3ca64e3-2194-4cc3-ae32-366bb9225676"
}
```

---


### Runtime record

_source line 171 · 2026-05-15T19:23:37.300Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T19:23:37.300Z",
  "sessionId": "f3ca64e3-2194-4cc3-ae32-366bb9225676",
  "content": "[Paper Agent 触发审查]:\n## Step 5 Round 3 Review Request\n\n**Project**: trace-verdict-study\n**Venue**: EMNLP 2026 Main (ARR May 2026)\n**writing_plan.yaml**: projects/trace-verdict-study/writing_plan.yaml\n\n### Changes since Round 2 (5/10)\n\nRound 2 issues all addressed:\n1. **McNemar→bootstrap**: All statistical test references corrected to \"paired bootstrap resampling (B=10,000, seed=42)\" with p-values and bootstrap CIs\n2. **CI confirmed**: exception_only CI [99.58, 100.00] consistent across tables and captions\n3. **fig2 caption**: Changed from \"Tier~1 conditions (ae_only, exception_only)\" to \"The Tier~1 condition (exception_only)\" — fig2 only shows exception_only\n4. **Brier claim**: \"approaches the theoretical maximum\" → \"indicates substantial miscalibration\"\n5. **ECE rounding**: 0.172 → 0.171 (registry value 0.171476 rounds to 0.171 at 3dp)\n6. **gradient_accumulation**: Confirmed 8 (effective batch 32) matches method.tex\n\n### Prior Round 1 fixes (also in this version)\n- method.tex hyperparameters verified against training code\n- wang2025dcsh citation verified (ACL 2025 Findings, arXiv 2509.11686)\n- Citations expanded 7→25 with specific paper descriptions\n- Related Work rewritten with 19 specific citations across 3 paragraphs\n- DeepSeek checkpoint degradation analysis (§4.3)\n- Per-class P/R/F1 appendix table\n- Bootstrap CIs and p-values for all pairwise comparisons\n\n### Full Paper LaTeX\n\n#### introduction.tex\n\\section{Introduction}\n\nExecution traces---line-by-line records of a program's runtime behavior---have emerged as a promising input modality for code language models.\nRecent work has explored trace-augmented training for code generation \\citep{chen2025tracepile}, execution-aware pretraining \\citep{ding2024traced}, trace-based code understanding \\citep{wang2025dcsh}, and self-training on trace chain-of-thought \\citep{ni2024next}.\nYet a fundamental question remains open: \\emph{which components of an execution trace actually matter?}\n\n\\citet{wang2025dcsh} found that no single trace representation consistently outperforms others on generation-oriented tasks, concluding that the utility of execution traces is task- and format-dependent.\nHowever, their study focused on code generation and repair---tasks that require the model to simulate or reconstruct execution semantics.\n\\emph{Verdict prediction}---classifying whether a test passes or fails---is a fundamentally different task type: it is a fault detection problem, not a generation problem.\nWhether the same trace components matter for fault detection as for generation is unknown.\n\nWe present the first systematic study of what trace components drive verdict prediction performance.\nUsing CRUXEval-derived data \\citep{gu2024cruxeval} with execution traces from TracePile \\citep{chen2025tracepile}, we decompose a multi-component trace representation (VOTA: exception events + assertion-point comparisons + loop compression) into individual components and evaluate each in isolation across two models: Qwen-2.5-Coder-7B-Instruct and DeepSeek-Coder-6.7B-Instruct.\n\nOur results reveal a striking finding: \\textbf{exception events alone are sufficient for near-perfect verdict prediction, and this signal is model-agnostic.}\nWith only exception events as trace input, both models achieve ${\\geq}$99.3\\% accuracy (cross-model gap = 0.50 percentage points).\nIn contrast, the full VOTA representation---which combines exception events with assertion-point and loop information---degrades by 14.96pp on the weaker model, indicating that processing mixed trace components demands model capability that exception-only prediction does not.\n\nThese results reframe verdict prediction as fault detection: the minimal sufficient signal is the exception event, a compact structured diagnostic moment that both models can interpret without deep trace reasoning.\nWe further decompose the gap between full trace and VOTA into two mechanisms---\\emph{gradient dilution} (26\\% of the gap) and \\emph{information overload} (74\\%)---showing that the primary bottleneck is not training signal quality but the presence of irrelevant trace content.\n\nOur contributions are:\n\\begin{enumerate}\n\\item \\textbf{Exception signal universality}: We show that exception events alone achieve 99.83\\%/99.33\\% accuracy across two models (gap = 0.50pp), while VOTA degrades 14.96pp on the weaker model (\\S\\ref{sec:cross_model}).\n\\item \\textbf{Information density decomposition}: We decompose the full-trace-to-VOTA gap into gradient dilution (26\\%) and information overload (74\\%), identifying the primary bottleneck for trace-based prediction (\\S\\ref{sec:density}).\n\\item \\textbf{Two-tier diagnostic hierarchy}: Component ablation reveals that Tier~1 signals (exception events, assertion points) individually achieve ${\\geq}$99.8\\% accuracy while Tier~2 signals (loop compression) reach only 85.6\\% (\\S\\ref{sec:ablation}).\n\\end{enumerate}\n\n#### method.tex\n\\section{Method}\n\n\\subsection{Task Definition}\nWe study \\emph{verdict prediction}: given a Python function, a test input, and an optional execution trace, predict whether the test passes or fails.\nThe model produces a single token---\\texttt{pass} or \\texttt{fail}---making this a binary classification task.\nUnlike code generation \\citep{chen2025tracepile} or output prediction \\citep{gu2024cruxeval}, verdict prediction isolates the model's ability to detect faults from its ability to simulate execution, providing a cleaner lens on what trace information actually contributes.\n\n\\subsection{Dataset}\nWe derive our dataset from CRUXEval \\citep{gu2024cruxeval}, a benchmark of 800 Python functions with associated test inputs.\nExecution traces are generated via line-level instrumentation following the TracePile methodology \\citep{chen2025tracepile}.\nEach function--test pair is executed to produce a full execution trace along with the ground-truth verdict (pass/fail).\nThe resulting dataset contains 4,720 training and 1,190 test samples with a class distribution of 71.5\\% pass / 28.5\\% fail, yielding a majority-class baseline of 71.51\\%.\n\n\\subsection{Trace Representations}\nSeven input conditions systematically vary trace information (Figure~\\ref{fig:trace_overview}):\nno_trace, full_trace, VOTA (exception+ae+loop), exception_only, ae_only, loop_only, VOTA_no_ae.\n\n\\subsection{Models}\nQwen-2.5-Coder-7B-Instruct (5.5T tokens) and DeepSeek-Coder-6.7B-Instruct (2T tokens).\n\n\\subsection{Training Setup}\nLoRA (rank=16, α=32) to all linear layers, 3 epochs, batch 4, gradient accumulation 8 (effective batch 32), lr 2e-4 with linear warmup and linear decay, warmup ratio 0.1, weight decay 0.01. Max seq 2048 tokens, truncated from input content preserving verdict label. Primary seed 42; robustness seeds 123, 456.\n\n\\subsection{Loss Ablation}\nfull_trace_label_only: full trace input but loss only on verdict token, masking trace tokens.\n\n#### experiments.tex\n[Full content as read above — Tables 1-4, cross-model comparison, component ablation, information density decomposition, calibration analysis. All statistical tests use paired bootstrap (B=10,000, seed=42). Wilson 95% CIs. Per-class analysis in Appendix.]\n\n#### discussion.tex\n[Full content as read above — §4.1 Why Exception Events Dominate, §4.2 Simplicity as Robustness, §4.3 Checkpoint Selection and Signal Stability, §4.4 Error Analysis, §4.5 Limitations]\n\n#### related_work.tex\n[Full content as read above — 3 paragraphs, 19 specific citations: Execution Traces for Code LLMs (8), Code Verdict and Patch Classification (6), Trace Compression and Selection (5)]\n\n#### conclusion.tex\n[Full content as read above — 3 findings + future work]\n\n#### appendix.tex\n[Per-class P/R/F1 table — 11 conditions × 2 models, highlighting DeepSeek VOTA 45.43% fail recall]\n\n### Paper stats\n- 25 citations in references.bib\n- ~7 pages content + 2 pages references + 1 page appendix\n- 3 figures (fig1_trace_overview, fig2_calibration, fig3_cross_model_gap)\n- 4 tables in main text + 1 in appendix\n\n### Review focus\nPlease evaluate all dimensions. This is Round 3 — all Round 1 (4/10) and Round 2 (5/10) issues have been addressed."
}
```

---


### Runtime record

_source line 172 · 2026-05-15T19:23:37.300Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T19:23:37.300Z",
  "sessionId": "f3ca64e3-2194-4cc3-ae32-366bb9225676"
}
```

---


## Round 8

## Round 8

2 recorded events


### User

_source line 173 · 2026-05-15T19:23:37.292Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1a2d44ca-8762-475d-9d6f-6a7d59bcf98d",
  "isSidechain": false,
  "promptId": "f4049486-b013-427c-a864-a8552d7f34c2",
  "type": "user",
  "isMeta": true,
  "uuid": "f75744b5-90d9-4fa1-b888-6c0f77e9b0b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/reviewer_4eb9adda",
  "sessionId": "f3ca64e3-2194-4cc3-ae32-366bb9225676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 174 · 2026-05-15T19:23:37.292Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f75744b5-90d9-4fa1-b888-6c0f77e9b0b7",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "dd85dd44-6cd7-4a2c-9e68-8a03993a99c9",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/reviewer_4eb9adda",
  "sessionId": "f3ca64e3-2194-4cc3-ae32-366bb9225676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "id": "522f01f7-b787-44c6-b454-29f4b2eddfb6",
    "container": null,
    "model": "&lt;synthetic>",
    "stop_reason": "stop_sequence",
    "stop_sequence": "",
    "type": "message",
    "usage": {
      "input_tokens": 0,
      "output_tokens": 0,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 0,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": null,
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": null,
      "iterations": null,
      "speed": null
    },
    "context_management": null
  }
}
```

</details>

---


## Round 9

## Round 9

5 recorded events


### User

_source line 175 · 2026-05-15T19:23:37.392Z_

[Paper Agent 触发审查]:
## Step 5 Round 3 Review Request

**Project**: trace-verdict-study
**Venue**: EMNLP 2026 Main (ARR May 2026)
**writing_plan.yaml**: projects/trace-verdict-study/writing_plan.yaml

### Changes since Round 2 (5/10)

Round 2 issues all addressed:
1. **McNemar→bootstrap**: All statistical test references corrected to "paired bootstrap resampling (B=10,000, seed=42)" with p-values and bootstrap CIs
2. **CI confirmed**: exception_only CI [99.58, 100.00] consistent across tables and captions
3. **fig2 caption**: Changed from "Tier~1 conditions (ae_only, exception_only)" to "The Tier~1 condition (exception_only)" — fig2 only shows exception_only
4. **Brier claim**: "approaches the theoretical maximum" → "indicates substantial miscalibration"
5. **ECE rounding**: 0.172 → 0.171 (registry value 0.171476 rounds to 0.171 at 3dp)
6. **gradient_accumulation**: Confirmed 8 (effective batch 32) matches method.tex

### Prior Round 1 fixes (also in this version)
- method.tex hyperparameters verified against training code
- wang2025dcsh citation verified (ACL 2025 Findings, arXiv 2509.11686)
- Citations expanded 7→25 with specific paper descriptions
- Related Work rewritten with 19 specific citations across 3 paragraphs
- DeepSeek checkpoint degradation analysis (§4.3)
- Per-class P/R/F1 appendix table
- Bootstrap CIs and p-values for all pairwise comparisons

### Full Paper LaTeX

#### introduction.tex
\section{Introduction}

Execution traces---line-by-line records of a program's runtime behavior---have emerged as a promising input modality for code language models.
Recent work has explored trace-augmented training for code generation \citep{chen2025tracepile}, execution-aware pretraining \citep{ding2024traced}, trace-based code understanding \citep{wang2025dcsh}, and self-training on trace chain-of-thought \citep{ni2024next}.
Yet a fundamental question remains open: \emph{which components of an execution trace actually matter?}

\citet{wang2025dcsh} found that no single trace representation consistently outperforms others on generation-oriented tasks, concluding that the utility of execution traces is task- and format-dependent.
However, their study focused on code generation and repair---tasks that require the model to simulate or reconstruct execution semantics.
\emph{Verdict prediction}---classifying whether a test passes or fails---is a fundamentally different task type: it is a fault detection problem, not a generation problem.
Whether the same trace components matter for fault detection as for generation is unknown.

We present the first systematic study of what trace components drive verdict prediction performance.
Using CRUXEval-derived data \citep{gu2024cruxeval} with execution traces from TracePile \citep{chen2025tracepile}, we decompose a multi-component trace representation (VOTA: exception events + assertion-point comparisons + loop compression) into individual components and evaluate each in isolation across two models: Qwen-2.5-Coder-7B-Instruct and DeepSeek-Coder-6.7B-Instruct.

Our results reveal a striking finding: \textbf{exception events alone are sufficient for near-perfect verdict prediction, and this signal is model-agnostic.}
With only exception events as trace input, both models achieve ${\geq}$99.3\% accuracy (cross-model gap = 0.50 percentage points).
In contrast, the full VOTA representation---which combines exception events with assertion-point and loop information---degrades by 14.96pp on the weaker model, indicating that processing mixed trace components demands model capability that exception-only prediction does not.

These results reframe verdict prediction as fault detection: the minimal sufficient signal is the exception event, a compact structured diagnostic moment that both models can interpret without deep trace reasoning.
We further decompose the gap between full trace and VOTA into two mechanisms---\emph{gradient dilution} (26\% of the gap) and \emph{information overload} (74\%)---showing that the primary bottleneck is not training signal quality but the presence of irrelevant trace content.

Our contributions are:
\begin{enumerate}
\item \textbf{Exception signal universality}: We show that exception events alone achieve 99.83\%/99.33\% accuracy across two models (gap = 0.50pp), while VOTA degrades 14.96pp on the weaker model (\S\ref{sec:cross_model}).
\item \textbf{Information density decomposition}: We decompose the full-trace-to-VOTA gap into gradient dilution (26\%) and information overload (74\%), identifying the primary bottleneck for trace-based prediction (\S\ref{sec:density}).
\item \textbf{Two-tier diagnostic hierarchy}: Component ablation reveals that Tier~1 signals (exception events, assertion points) individually achieve ${\geq}$99.8\% accuracy while Tier~2 signals (loop compression) reach only 85.6\% (\S\ref{sec:ablation}).
\end{enumerate}

#### method.tex
\section{Method}

\subsection{Task Definition}
We study \emph{verdict prediction}: given a Python function, a test input, and an optional execution trace, predict whether the test passes or fails.
The model produces a single token---\texttt{pass} or \texttt{fail}---making this a binary classification task.
Unlike code generation \citep{chen2025tracepile} or output prediction \citep{gu2024cruxeval}, verdict prediction isolates the model's ability to detect faults from its ability to simulate execution, providing a cleaner lens on what trace information actually contributes.

\subsection{Dataset}
We derive our dataset from CRUXEval \citep{gu2024cruxeval}, a benchmark of 800 Python functions with associated test inputs.
Execution traces are generated via line-level instrumentation following the TracePile methodology \citep{chen2025tracepile}.
Each function--test pair is executed to produce a full execution trace along with the ground-truth verdict (pass/fail).
The resulting dataset contains 4,720 training and 1,190 test samples with a class distribution of 71.5\% pass / 28.5\% fail, yielding a majority-class baseline of 71.51\%.

\subsection{Trace Representations}
Seven input conditions systematically vary trace information (Figure~\ref{fig:trace_overview}):
no_trace, full_trace, VOTA (exception+ae+loop), exception_only, ae_only, loop_only, VOTA_no_ae.

\subsection{Models}
Qwen-2.5-Coder-7B-Instruct (5.5T tokens) and DeepSeek-Coder-6.7B-Instruct (2T tokens).

\subsection{Training Setup}
LoRA (rank=16, α=32) to all linear layers, 3 epochs, batch 4, gradient accumulation 8 (effective batch 32), lr 2e-4 with linear warmup and linear decay, warmup ratio 0.1, weight decay 0.01. Max seq 2048 tokens, truncated from input content preserving verdict label. Primary seed 42; robustness seeds 123, 456.

\subsection{Loss Ablation}
full_trace_label_only: full trace input but loss only on verdict token, masking trace tokens.

#### experiments.tex
[Full content as read above — Tables 1-4, cross-model comparison, component ablation, information density decomposition, calibration analysis. All statistical tests use paired bootstrap (B=10,000, seed=42). Wilson 95% CIs. Per-class analysis in Appendix.]

#### discussion.tex
[Full content as read above — §4.1 Why Exception Events Dominate, §4.2 Simplicity as Robustness, §4.3 Checkpoint Selection and Signal Stability, §4.4 Error Analysis, §4.5 Limitations]

#### related_work.tex
[Full content as read above — 3 paragraphs, 19 specific citations: Execution Traces for Code LLMs (8), Code Verdict and Patch Classification (6), Trace Compression and Selection (5)]

#### conclusion.tex
[Full content as read above — 3 findings + future work]

#### appendix.tex
[Per-class P/R/F1 table — 11 conditions × 2 models, highlighting DeepSeek VOTA 45.43% fail recall]

### Paper stats
- 25 citations in references.bib
- ~7 pages content + 2 pages references + 1 page appendix
- 3 figures (fig1_trace_overview, fig2_calibration, fig3_cross_model_gap)
- 4 tables in main text + 1 in appendix

### Review focus
Please evaluate all dimensions. This is Round 3 — all Round 1 (4/10) and Round 2 (5/10) issues have been addressed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd85dd44-6cd7-4a2c-9e68-8a03993a99c9",
  "isSidechain": false,
  "promptId": "f4049486-b013-427c-a864-a8552d7f34c2",
  "type": "user",
  "uuid": "30b1336e-ed83-4649-9ceb-ad2414eb5c09",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/reviewer_4eb9adda",
  "sessionId": "f3ca64e3-2194-4cc3-ae32-366bb9225676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 176_

```json
{
  "type": "ai-title",
  "aiTitle": "Review loop 5 training status and paper critical fixes",
  "sessionId": "f3ca64e3-2194-4cc3-ae32-366bb9225676"
}
```

---


### Runtime record

_source line 177 · 2026-05-15T19:27:03.169Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T19:27:03.169Z",
  "sessionId": "f3ca64e3-2194-4cc3-ae32-366bb9225676",
  "content": "[Paper Agent 触发审查]:\n## Step 5 Round 4 Review Request\n\n**Project**: trace-verdict-study\n**Venue**: EMNLP 2026 Main (ARR May 2026)\n**writing_plan.yaml**: projects/trace-verdict-study/writing_plan.yaml\n\n### Changes since Round 3 (6/10)\n\nAll 3 Warnings + 2 Info items addressed:\n\n**W1 — Table 1 footnote ‡ root cause**: Changed from \"evaluate.py truncation mismatch\" to \"DeepSeek tokenizer produced sequences exceeding 2,048 tokens, causing verdict label truncation during training; model failed to learn classification task.\" Also updated matching description in Limitations (discussion.tex §4.5).\n\n**W2 — Title \"Model-Agnostic\" → \"Cross-Model\"**: \n- main.tex title: \"Model-Agnostic\" → \"Cross-Model\"\n- introduction.tex: \"this signal is model-agnostic\" → \"this signal transfers across model families\"\n- experiments.tex §3.1: \"model-agnostic\" → \"transfers across model families\"\n- experiments.tex fig3 caption: \"model-agnostic\" → \"transfer across models\"\n\n**W3 — Exception signal near-circularity discussion**: New paragraph added to §4.1 (Why Exception Events Dominate). Acknowledges that exception-based verdict prediction is essentially fault indicator presence detection, close to trivially solvable. States that the real contribution is: (a) quantifying that adding more trace info hurts (information density dilution), and (b) cross-model comparison showing dilution is model-dependent (DeepSeek VOTA fail recall 45.43%).\n\n**Info — Brier precision**: ae_only 0.001→0.0008, exception_only 0.001→0.0013 (from registry: 0.000847 and 0.001311). Updated in both Table 5 and inline text.\n\n**Note**: Info item \"800 functions → 5910 samples expansion mechanism\" flagged to Director — I need the experiment code to confirm exact expansion mechanism (multiple test inputs per function vs TracePile augmentation).\n\n### Compilation & Consistency\n- Compiled: PASS (10 pages, 0 critical warnings)\n- Consistency check: 0 critical, 0 warning\n\n### Cumulative fixes across all rounds\n- Round 1 (4/10): method hyperparams, wang2025dcsh verified, 7→25 citations, Related Work rewrite, DeepSeek degradation §4.3, per-class appendix, bootstrap CIs/p-values\n- Round 2 (5/10): McNemar→bootstrap, fig2 caption, Brier claim, ECE rounding\n- Round 3 (6/10): full_trace footnote root cause, Model-Agnostic→Cross-Model, near-circularity discussion, Brier precision\n\n### Full LaTeX sections attached\n[All sections as previously submitted with the Round 3 changes applied. Key diffs:\n- main.tex: title \"Cross-Model\"\n- introduction.tex: \"transfers across model families\"\n- experiments.tex: 4 edits (model-agnostic×2, footnote ‡, Brier precision)\n- discussion.tex: new near-circularity paragraph in §4.1, updated Limitations §4.5]"
}
```

---


### Runtime record

_source line 178 · 2026-05-15T19:27:03.170Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T19:27:03.170Z",
  "sessionId": "f3ca64e3-2194-4cc3-ae32-366bb9225676"
}
```

---


### Assistant

_source line 179 · 2026-05-15T19:27:03.162Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30b1336e-ed83-4649-9ceb-ad2414eb5c09",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "f0995663-6a3d-421f-83a9-64a1fe11de7c",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/reviewer_4eb9adda",
  "sessionId": "f3ca64e3-2194-4cc3-ae32-366bb9225676",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "id": "ff093e4c-f40f-4f8a-86f9-b95a438aafb2",
    "container": null,
    "model": "&lt;synthetic>",
    "stop_reason": "stop_sequence",
    "stop_sequence": "",
    "type": "message",
    "usage": {
      "input_tokens": 0,
      "output_tokens": 0,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 0,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": null,
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": null,
      "iterations": null,
      "speed": null
    },
    "context_management": null
  }
}
```

</details>

---


## Round 10

## Round 10

1 recorded events


### User

_source line 180 · 2026-05-15T19:27:03.270Z_

[Paper Agent 触发审查]:
## Step 5 Round 4 Review Request

**Project**: trace-verdict-study
**Venue**: EMNLP 2026 Main (ARR May 2026)
**writing_plan.yaml**: projects/trace-verdict-study/writing_plan.yaml

### Changes since Round 3 (6/10)

All 3 Warnings + 2 Info items addressed:

**W1 — Table 1 footnote ‡ root cause**: Changed from "evaluate.py truncation mismatch" to "DeepSeek tokenizer produced sequences exceeding 2,048 tokens, causing verdict label truncation during training; model failed to learn classification task." Also updated matching description in Limitations (discussion.tex §4.5).

**W2 — Title "Model-Agnostic" → "Cross-Model"**: 
- main.tex title: "Model-Agnostic" → "Cross-Model"
- introduction.tex: "this signal is model-agnostic" → "this signal transfers across model families"
- experiments.tex §3.1: "model-agnostic" → "transfers across model families"
- experiments.tex fig3 caption: "model-agnostic" → "transfer across models"

**W3 — Exception signal near-circularity discussion**: New paragraph added to §4.1 (Why Exception Events Dominate). Acknowledges that exception-based verdict prediction is essentially fault indicator presence detection, close to trivially solvable. States that the real contribution is: (a) quantifying that adding more trace info hurts (information density dilution), and (b) cross-model comparison showing dilution is model-dependent (DeepSeek VOTA fail recall 45.43%).

**Info — Brier precision**: ae_only 0.001→0.0008, exception_only 0.001→0.0013 (from registry: 0.000847 and 0.001311). Updated in both Table 5 and inline text.

**Note**: Info item "800 functions → 5910 samples expansion mechanism" flagged to Director — I need the experiment code to confirm exact expansion mechanism (multiple test inputs per function vs TracePile augmentation).

### Compilation & Consistency
- Compiled: PASS (10 pages, 0 critical warnings)
- Consistency check: 0 critical, 0 warning

### Cumulative fixes across all rounds
- Round 1 (4/10): method hyperparams, wang2025dcsh verified, 7→25 citations, Related Work rewrite, DeepSeek degradation §4.3, per-class appendix, bootstrap CIs/p-values
- Round 2 (5/10): McNemar→bootstrap, fig2 caption, Brier claim, ECE rounding
- Round 3 (6/10): full_trace footnote root cause, Model-Agnostic→Cross-Model, near-circularity discussion, Brier precision

### Full LaTeX sections attached
[All sections as previously submitted with the Round 3 changes applied. Key diffs:
- main.tex: title "Cross-Model"
- introduction.tex: "transfers across model families"
- experiments.tex: 4 edits (model-agnostic×2, footnote ‡, Brier precision)
- discussion.tex: new near-circularity paragraph in §4.1, updated Limitations §4.5]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0995663-6a3d-421f-83a9-64a1fe11de7c",
  "isSidechain": false,
  "promptId": "06bf6684-a2ac-416b-8ef0-074625387b36",
  "type": "user",
  "uuid": "87ad929e-5c95-4156-8f61-f14cbea46ee0",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/.claude/sessions/reviewer_4eb9adda",
  "sessionId": "f3ca64e3-2194-4cc3-ae32-366bb9225676",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---
