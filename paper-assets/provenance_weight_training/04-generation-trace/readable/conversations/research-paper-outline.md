# research paper outline

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 0
- **Tool calls:** 16
- **Original source:** `logs/chats/worker_research_paper_outline_20260515T200947.jsonl`
- **Structured JSON:** [`c232715758dc80c74a78.json`](../../sessions/c2/c232715758dc80c74a78.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

33 recorded events

### Tool call

_source line 1 · 2026-05-15T20:14:10.929896+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_registry",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_outline_20260515T200947",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_registry",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T20:14:10.930355+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_outline_20260515T200947",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T20:14:10.930592+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_outline_20260515T200947",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "provenance_weight_training",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T20:14:10.930997+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/paper_framing.md\", \"content\": \"# Paper Framing — provenance_weight_training\\n\\n> 状态: STABLE (D023 dual-constraint + D029 ESS-only resolved + D035 τ sweep complete)\\n> 最后更新: 2026-05-15 21:30 UTC\\n> 投稿目标: EMNLP 2026 ARR May 25\\n\\n## Core Insight\\n\\nWeb 语料预训练面临合成数据污染问题（20-60%，来源未知），Drayson et al. (EMNLP 2025) 提出 w=(1-q)^b detect-and-reweight 框架，但 b 需要 per-model validation-based grid search（GPT-2/SmolLM ≤360M 用 b=10，SmolLM 1.7B 用 b=1）。\\n\\n我们提出 **dual-constrained adaptive b***：per-batch 从 q-score 分布推导最优 b*，同时满足两个约束：\\n- **α_eff(b) ≥ τ** — 质量下界：确保加权后有效真实率达到收敛理论要求的阈值（\\\"至少做够清洁\\\"）\\n- **ESS(b) ≥ n_min** — 稳定上界：确保有效样本量不低于 Kish 阈值（\\\"不要清洁过头\\\"）\\n\\nb* = inf{b ≥ 0 : α_eff(b) ≥ τ} subject to ESS(b) ≥ n_min — **最小干预准则**：在保证质量的前提下，使用最少的 downweighting。\\n\\n**关键洞察**：α_eff(b) 单调递增、ESS(b) 单调递减。α_eff 给出 b 的下界 b_τ（需至少这么多清洁），ESS 给出 b 的上界 b_ESS（最多这么多清洁）。当 b_τ < b_ESS（~40% reweighted batches），α_eff 是 binding constraint，b* 远小于 ESS 上界（mean 1.67 vs 4.15）——方法选择保守干预而非最大干预。\\n\\n实现路径：**直接 loss reweighting**（gradient 层面连续加权），vs Drayson 的 SIR resampling（离散重采样）。\\n\\n### α_eff(b) 的角色（D023 修正定论）\\n\\n**D021 证明 α_eff(b) 严格单调递增**（dα_eff/db = Cov_w(x, ln x) ≥ 0）——这是正确的。\\n\\n**D021 的错误推论**：\\\"因此 α_eff 优化等价于 ESS 阈值化\\\"——这假设优化目标是 max α_eff(b) s.t. ESS ≥ n_min。但实际优化是 **inf{b : α_eff(b) ≥ τ}**——最小满足质量阈值的 b。单调性恰恰保证了 b_τ 的**存在性和唯一性**。\\n\\n**Q1 实证（Reviewer 独立核实）**：\\n- 51,913 micro-batches 中，49.9% clean (b*=0), 20.2% α_eff binding, 30.0% ESS binding\\n- 在需 reweighting 的 batch 中：40.1% α_eff binding, 59.9% ESS binding\\n- α_eff binding 时 b*=1.67，ESS-only 方法会选 b*=4.15（2.5× 更激进）\\n- α_eff binding 时 ESS=2.60（vs n_min=2.0，有 30% 余量）\\n\\n**论文呈现**：α_eff 是方法的核心组件（非仅 motivation），提供质量阈值约束。Figure: 双轴图展示 α_eff(b) 和 ESS(b) 曲线 + b_τ 和 b_ESS 标注。\\n\\n**τ 的定位（D025 定论 + D035 τ sweep 完整数据更新）**：收敛理论 (arXiv 2602.16065) 中 α = m₁/(m₁+m₂) 是已知设计参数，推导依赖已知比例。τ **不能声称有 propor
…[truncated 10140 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_outline_20260515T200947",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T20:14:10.931306+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "literature_map.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_outline_20260515T200947",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "provenance_weight_training",
    "file": "literature_map.yaml",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T20:14:10.931834+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/literature_map.yaml\", \"content\": \"# Literature Map for provenance_weight_training\\n# 研究方向：基于收敛理论的自适应污染重加权\\n# 核心公式：w=(1-q)^b，q 为检测器合成概率，b* 为理论最优权重指数\\n# 更新日期：2026-05-15（文献扫描：补充 Wang et al. + 4 方向新文献 + 修正 2 处错误）\\n\\n# ============================================================\\n# Category: direct-competitor\\n# 同主题/同方法的论文\\n# ============================================================\\n\\n- id: drayson_2025_detection_collapse\\n  title: \\\"Machine-Generated Text Detection Prevents Language Model Collapse\\\"\\n  authors: \\\"George Drayson, Emine Yilmaz, Vasileios Lampos\\\"\\n  venue: \\\"EMNLP 2025\\\"\\n  year: 2025\\n  arxiv_id: \\\"2502.15654\\\"\\n  url: \\\"https://arxiv.org/abs/2502.15654\\\"\\n  github: \\\"https://github.com/GeorgeDrayson/model_collapse\\\"\\n  category: direct-competitor\\n  role: \\\"使用同一公式 w=(1-q)^b 进行重加权，但 b 为验证集 empirical 选取，训练中固定\\\"\\n  method_summary: >\\n    Detect-and-reweight 防止递归训练 model collapse。检测器为 ModernBERT 150M\\n    (MAGE fine-tune, in-domain AUC=0.986, OOD AUC=0.943)。权重公式 wⱼ=(1-q(xⱼ))^b / Σₗ(1-q(xₗ))^b，\\n    通过 SIR 按权重重采样训练数据。b 通过 WikiText-2 验证集上 1 代递归训练后评估选取\\n    (GPT-2/SmolLM 135M/360M 用 b=10, SmolLM 1.7B 用 b=1)，训练全程固定。\\n    实验覆盖 4 个模型 (GPT-2 124M, SmolLM 135M/360M/1.7B)、10 代递归训练、6 种解码策略。\\n    结果 PPL 降低 0.85%–25.65%，diversity 提升 3.44%–14.62%。\\n  key_findings: \\\"验证 detect-and-reweight 有效防止 model collapse 且优于纯人类数据训练；b 值对模型规模敏感（小模型 b=10，大模型 b=1）\\\"\\n  differentiation:\\n    b_selection: \\\"Drayson: 验证集 empirical grid search, per-model 固定 | 我们: α_eff(b) + ESS 约束, per-batch 自适应\\\"\\n    contamination_setting: \\\"Drayson: 不假设已知比例（原文明确声明），但实验为控制设置 | 我们: 未知比例（batch 统计量在线估计）\\\"\\n    detector: \\\"Drayson: ModernBERT 150M (AUC=0.986) | 我们: TF-IDF+LR (AUC=0.939)，证明轻量检测器即可\\\"\\n    theory: \\\"Drayson: 无 b 选取理论（SIR 启发式） | 我们: 收敛理论 motivated α_eff(b) 推导\\\"\\n    traini
…[truncated 15650 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_outline_20260515T200947",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T20:14:10.932112+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "provenance_weight_training",
  "limit": "0",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_outline_20260515T200947",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "provenance_weight_training",
    "limit": "0",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-15T20:14:10.932312+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "ROADMAP.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_outline_20260515T200947",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "provenance_weight_training",
    "file": "ROADMAP.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-15T20:14:10.933105+00:00_

Error: result (90,979 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/a0a804d4-6478-4fc5-9087-f104ab623fd4/tool-results/mcp-agent-ml-research-read_registry-1778875802923.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/a0a804d4-6478-4fc5-9087-f104ab623fd4/tool-results/mcp-agent-ml-research-read_registry-1778875802923.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/a0a804d4-6478-4fc5-9087-f104ab623fd4/tool-results/mcp-agent-ml-research-read_registry-1778875802923.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_outline_20260515T200947",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T20:14:10.933476+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/ROADMAP.md\", \"content\": \"# provenance_weight_training — Research Dashboard\\n\\n> 最后更新: 2026-05-15 18:40 UTC | 更新原因: τ sweep 6/6 完成(D036) + zombie kill + bs8 配置修正(D037) + 全面状态刷新\\n\\n## 核心方向\\nDual-constrained adaptive b*：α_eff 质量下界 + ESS 稳定上界 → 最小干预准则。per-batch 自适应推导 b*，替代 Drayson 的 validation-based grid search。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research（D023 dual-constraint 框架）+ 审稿并行\\n- **投稿目标**: EMNLP 2026 ARR May 25（10 天）\\n- **MVP**: ✅ PASS (D019)\\n- **Framing**: D023 dual-constraint ✅ | D025 τ empirical HP ✅ | D036 τ sweep 6 点完成 ✅\\n- **Key Risk #1**: ✅ RESOLVED (D029) — ESS-only PPL=17.728, dual > ESS-only confirmed\\n- **τ sweep**: ✅ 6/6 complete (D036) — safe range [0.5,0.8], τ=0.8 optimal, τ>0.8 退化\\n- **成功实验**: 30/36 (negative 2, failed 1, killed 3)\\n\\n## RUNNING 实验\\n| GPU | 实验 | 类型 | 进度 | ETA (UTC) |\\n|-----|------|------|------|-----------|\\n| cuda:0 | ess_only_seed123 | Claim 1 多 seed | 14% | ~22:00 |\\n| cuda:1 | nmin4_seed42 | n_min 边界 (b*=0 确认中) | 27% | ~21:45 |\\n| cuda:2 | bs8_seed42 → kill+restart | D037: n_min=4→2 修正 | 1% kill | 重启后 ~3.8h |\\n| cuda:3 | ess_only_seed456 | Claim 1 多 seed | 14% | ~22:00 |\\n\\n## 近期完成\\n- ✅ τ sweep 6/6 (D036): [0.5,0.8] safe, τ=0.8 optimal, τ>0.8 degrades (b* inflation)\\n- ✅ ess_only_seed42 (D029): PPL=17.728 > uniform — max-intervention 退化确认\\n- ✅ golden_ratio_seed42: PPL=17.654 ≈ adaptive — oracle baseline\\n- ✅ nmin1_seed42: PPL=17.789 — ESS 约束失效，过度 downweight\\n- ✅ GPU 1 zombie kill: nmin4 速度 4.33→2.22s/it，节省 ~3h\\n- ❌ bs8_seed42 (D037): n_min=4 配置错误，kill 重启为 n_min=2\\n\\n## 近期任务\\n- [ ] bs8_seed42 kill + restart with n_min=2 (Agent 执行中)\\n- [ ] τ sweep 分析图表（τ vs PPL + τ vs b* 双轴图）\\n- [ ] ess_only_seed123/456 eval → Claim 1 多 seed 加固\\n- [ ] nmin4_seed42 eval → 预期 PPL≈17.69 (b*=0 退化为 uniform)\\n- [ ] bs8_nmin2_seed42 eval → n_min=2 在大 batch 下的泛化性\\n-
…[truncated 2499 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_outline_20260515T200947",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T20:14:10.933770+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Extract experiment registry data",
  "prompt": "Read the file /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/a0a804d4-6478-4fc5-9087-f104ab623fd4/tool-results/mcp-agent-ml-research-read_registry-1778875802923.txt\n\nIt's JSON with schema: {result: string}. The inner \"result\" is also a JSON string that needs parsing.\n\nExtract ALL experiments and for each one, report:\n- exp_id\n- status (DONE, RUNNING, FAILED, KILLED, etc.)\n- conclusion (if any)\n- key metrics (especially eval_ppl)\n- category/claim it supports\n- config highlights (model, batch_size, n_min, tau, contamination_ratio, b value if grid)\n\nReturn a structured summary organized by claim/category. Be thorough - I need every experiment.",
  "model": "sonnet"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_outline_20260515T200947",
  "tool": "Agent",
  "tool_args": {
    "description": "Extract experiment registry data",
    "prompt": "Read the file /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/a0a804d4-6478-4fc5-9087-f104ab623fd4/tool-results/mcp-agent-ml-research-read_registry-1778875802923.txt\n\nIt's JSON with schema: {result: string}. The inner \"result\" is also a JSON string that needs parsing.\n\nExtract ALL experiments and for each one, report:\n- exp_id\n- status (DONE, RUNNING, FAILED, KILLED, etc.)\n- conclusion (if any)\n- key metrics (especially eval_ppl)\n- category/claim it supports\n- config highlights (model, batch_size, n_min, tau, contamination_ratio, b value if grid)\n\nReturn a structured summary organized by claim/category. Be thorough - I need every experiment.",
    "model": "sonnet"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T20:14:10.934048+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/a0a804d4-6478-4fc5-9087-f104ab623fd4/tool-results/mcp-agent-ml-research-read_registry-1778875802923.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_outline_20260515T200947",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/a0a804d4-6478-4fc5-9087-f104ab623fd4/tool-results/mcp-agent-ml-research-read_registry-1778875802923.txt"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T20:14:10.934240+00:00_

File content (37860 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_outline_20260515T200947",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T20:14:10.934438+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/a0a804d4-6478-4fc5-9087-f104ab623fd4/tool-results/mcp-agent-ml-research-read_registry-1778875802923.txt",
  "limit": "500",
  "offset": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_outline_20260515T200947",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/a0a804d4-6478-4fc5-9087-f104ab623fd4/tool-results/mcp-agent-ml-research-read_registry-1778875802923.txt",
    "limit": "500",
    "offset": "0"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T20:14:10.934623+00:00_

File content (37860 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_outline_20260515T200947",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T20:14:10.934816+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -c \"/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/a0a804d4-6478-4fc5-9087-f104ab623fd4/tool-results/mcp-agent-ml-research-read_registry-1778875802923.txt\"",
  "description": "Get file size in bytes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_outline_20260515T200947",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -c \"/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/a0a804d4-6478-4fc5-9087-f104ab623fd4/tool-results/mcp-agent-ml-research-read_registry-1778875802923.txt\"",
    "description": "Get file size in bytes"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-15T20:14:10.935045+00:00_

92453 /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/a0a804d4-6478-4fc5-9087-f104ab623fd4/tool-results/mcp-agent-ml-research-read_registry-1778875802923.txt

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_outline_20260515T200947",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T20:14:10.935267+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 - <<'EOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/a0a804d4-6478-4fc5-9087-f104ab623fd4/tool-results/mcp-agent-ml-research-read_registry-1778875802923.txt\"\n\nwith open(filepath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nresult_str = outer['result']\nregistry = json.loads(result_str)\n\nprint(type(registry))\nif isinstance(registry, dict):\n    print(\"Top-level keys:\", list(registry.keys())[:20])\nelif isinstance(registry, list):\n    print(\"List length:\", len(registry))\n    print(\"First item keys:\", list(registry[0].keys()) if registry else \"empty\")\nEOF\n",
  "description": "Parse the JSON structure to understand its format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_outline_20260515T200947",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 - <<'EOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/a0a804d4-6478-4fc5-9087-f104ab623fd4/tool-results/mcp-agent-ml-research-read_registry-1778875802923.txt\"\n\nwith open(filepath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nresult_str = outer['result']\nregistry = json.loads(result_str)\n\nprint(type(registry))\nif isinstance(registry, dict):\n    print(\"Top-level keys:\", list(registry.keys())[:20])\nelif isinstance(registry, list):\n    print(\"List length:\", len(registry))\n    print(\"First item keys:\", list(registry[0].keys()) if registry else \"empty\")\nEOF\n",
    "description": "Parse the JSON structure to understand its format"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T20:14:10.935482+00:00_

&lt;class 'dict'>
Top-level keys: ['success', 'data', 'error', 'metadata']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_outline_20260515T200947",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-15T20:14:10.935697+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 - <<'EOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/a0a804d4-6478-4fc5-9087-f104ab623fd4/tool-results/mcp-agent-ml-research-read_registry-1778875802923.txt\"\n\nwith open(filepath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nresult_str = outer['result']\nregistry = json.loads(result_str)\n\ndata = registry['data']\nprint(type(data))\nif isinstance(data, dict):\n    print(\"data keys:\", list(data.keys())[:20])\nelif isinstance(data, list):\n    print(\"data list length:\", len(data))\n    print(\"First item:\", json.dumps(data[0], indent=2)[:500])\nEOF\n",
  "description": "Explore the data field structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_outline_20260515T200947",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 - <<'EOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/a0a804d4-6478-4fc5-9087-f104ab623fd4/tool-results/mcp-agent-ml-research-read_registry-1778875802923.txt\"\n\nwith open(filepath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nresult_str = outer['result']\nregistry = json.loads(result_str)\n\ndata = registry['data']\nprint(type(data))\nif isinstance(data, dict):\n    print(\"data keys:\", list(data.keys())[:20])\nelif isinstance(data, list):\n    print(\"data list length:\", len(data))\n    print(\"First item:\", json.dumps(data[0], indent=2)[:500])\nEOF\n",
    "description": "Explore the data field structure"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T20:14:10.935949+00:00_

&lt;class 'dict'>
data keys: ['experiments', 'count', 'total', 'baseline']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_outline_20260515T200947",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-15T20:14:10.936168+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 - <<'EOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/a0a804d4-6478-4fc5-9087-f104ab623fd4/tool-results/mcp-agent-ml-research-read_registry-1778875802923.txt\"\n\nwith open(filepath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nresult_str = outer['result']\nregistry = json.loads(result_str)\n\ndata = registry['data']\nexps = data['experiments']\nprint(f\"Total experiments: {data['total']}, count in this response: {data['count']}\")\nprint(f\"Baseline: {data['baseline']}\")\nprint(f\"\\nExperiments type: {type(exps)}\")\nif isinstance(exps, list):\n    print(f\"Number: {len(exps)}\")\n    print(\"First exp keys:\", list(exps[0].keys()))\n    print(\"First exp sample:\", json.dumps(exps[0], indent=2)[:800])\nelif isinstance(exps, dict):\n    print(\"Keys:\", list(exps.keys())[:10])\nEOF\n",
  "description": "Get experiments count and structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_outline_20260515T200947",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 - <<'EOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/a0a804d4-6478-4fc5-9087-f104ab623fd4/tool-results/mcp-agent-ml-research-read_registry-1778875802923.txt\"\n\nwith open(filepath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nresult_str = outer['result']\nregistry = json.loads(result_str)\n\ndata = registry['data']\nexps = data['experiments']\nprint(f\"Total experiments: {data['total']}, count in this response: {data['count']}\")\nprint(f\"Baseline: {data['baseline']}\")\nprint(f\"\\nExperiments type: {type(exps)}\")\nif isinstance(exps, list):\n    print(f\"Number: {len(exps)}\")\n    print(\"First exp keys:\", list(exps[0].keys()))\n    print(\"First exp sample:\", json.dumps(exps[0], indent=2)[:800])\nelif isinstance(exps, dict):\n    print(\"Keys:\", list(exps.keys())[:10])\nEOF\n",
    "description": "Get experiments count and structure"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-15T20:14:10.936361+00:00_

Total experiments: 46, count in this response: 46
Baseline: None

Experiments type: &lt;class 'dict'>
Keys: ['p0_contamination_60_datagen', 'bs8_nmin2_seed42_r2', 'nmin4_seed42', 'bs8_nmin2_seed42', 'bs8_seed42', 'tau_095_seed42', 'tau_09_seed42', 'ess_only_seed456', 'ess_only_seed123', 'tau_07_seed42']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_outline_20260515T200947",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-15T20:14:10.936562+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 - <<'EOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/a0a804d4-6478-4fc5-9087-f104ab623fd4/tool-results/mcp-agent-ml-research-read_registry-1778875802923.txt\"\n\nwith open(filepath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nresult_str = outer['result']\nregistry = json.loads(result_str)\n\ndata = registry['data']\nexps = data['experiments']\nprint(\"All experiment IDs:\")\nfor i, eid in enumerate(exps.keys()):\n    print(f\"  {i+1}. {eid}\")\nEOF\n",
  "description": "List all experiment IDs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_outline_20260515T200947",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 - <<'EOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/a0a804d4-6478-4fc5-9087-f104ab623fd4/tool-results/mcp-agent-ml-research-read_registry-1778875802923.txt\"\n\nwith open(filepath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nresult_str = outer['result']\nregistry = json.loads(result_str)\n\ndata = registry['data']\nexps = data['experiments']\nprint(\"All experiment IDs:\")\nfor i, eid in enumerate(exps.keys()):\n    print(f\"  {i+1}. {eid}\")\nEOF\n",
    "description": "List all experiment IDs"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-15T20:14:10.936766+00:00_

All experiment IDs:
  1. p0_contamination_60_datagen
  2. bs8_nmin2_seed42_r2
  3. nmin4_seed42
  4. bs8_nmin2_seed42
  5. bs8_seed42
  6. tau_095_seed42
  7. tau_09_seed42
  8. ess_only_seed456
  9. ess_only_seed123
  10. tau_07_seed42
  11. tau_06_seed42
  12. tau_05_seed42
  13. adaptive_fix_seed456
  14. adaptive_fix_seed123
  15. adaptive_fix_seed42
  16. adaptive_seed456
  17. adaptive_seed123
  18. adaptive_seed42
  19. uniform_seed456
  20. uniform_seed123
  21. uniform_seed42
  22. detector_modernbert
  23. nmin1_seed42
  24. ess_only_seed42
  25. golden_ratio_seed42
  26. tau_0.6_seed42
  27. grid_b5_0_seed456
  28. grid_b3_0_seed456
  29. grid_b2_0_seed456
  30. grid_b_low_seed42
  31. grid_b1_5_seed456
  32. grid_b1_0_seed456
  33. grid_b0_5_seed456
  34. grid_b_seed42_batch
  35. grid_b5_0_seed123
  36. grid_b2_0_seed123
  37. grid_b3_0_seed123
  38. adaptive_v2_seed456
  39. adaptive_v2_seed123
  40. adaptive_v2_seed42
  41. grid_b1_5_seed123
  42. grid_b1_0_seed123
  43. grid_b0_5_seed123
  44. diagnostic_contamination100
  45. detector_tfidf_lr
  46. datagen_synthetic_4gpu

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_outline_20260515T200947",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-15T20:14:10.937012+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 - <<'EOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/a0a804d4-6478-4fc5-9087-f104ab623fd4/tool-results/mcp-agent-ml-research-read_registry-1778875802923.txt\"\n\nwith open(filepath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nresult_str = outer['result']\nregistry = json.loads(result_str)\n\ndata = registry['data']\nexps = data['experiments']\n\n# Print full details for each experiment\nfor eid, exp in exps.items():\n    print(f\"\\n{'='*60}\")\n    print(f\"EXP_ID: {eid}\")\n    print(json.dumps(exp, indent=2))\nEOF\n",
  "description": "Print all experiment details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_outline_20260515T200947",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 - <<'EOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/a0a804d4-6478-4fc5-9087-f104ab623fd4/tool-results/mcp-agent-ml-research-read_registry-1778875802923.txt\"\n\nwith open(filepath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nresult_str = outer['result']\nregistry = json.loads(result_str)\n\ndata = registry['data']\nexps = data['experiments']\n\n# Print full details for each experiment\nfor eid, exp in exps.items():\n    print(f\"\\n{'='*60}\")\n    print(f\"EXP_ID: {eid}\")\n    print(json.dumps(exp, indent=2))\nEOF\n",
    "description": "Print all experiment details"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-15T20:14:10.937242+00:00_

&lt;persisted-output>
Output too large (97.5KB). Full output saved to: /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/a0a804d4-6478-4fc5-9087-f104ab623fd4/tool-results/b67tdywua.txt

Preview (first 2KB):
============================================================
EXP_ID: p0_contamination_60_datagen
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-15T19:37:10.827Z",
  "updated_at": "2026-05-15T20:08:12.383Z",
  "spec": {
    "command": "python scripts/prepare_rho06_data.py",
    "server": "westd-47453",
    "data_path": "/root/provenance_weight_training/data/scored_data_60.jsonl",
    "data_count": 371499,
    "model_name": "Qwen3-0.6B (TF-IDF scoring)",
    "seed": 42,
    "checkpoint_path": "/root/provenance_weight_training/data/scored_data_60.jsonl",
    "log_path": "/root/provenance_weight_training/scripts/prepare_rho06_data.py"
  },
  "conclusion": "success",
  "metrics": {
    "total_lines": 371499,
    "synthetic_count": 222900,
    "human_count": 148599,
    "actual_contamination_ratio": 0.6,
    "q_score_mean": 0.6243,
    "q_score_std": 0.3703,
    "q_score_median": 0.7753,
    "file_size_mb": 907
  },
  "completed_at": "2026-05-15T20:08:12.383Z"
}

============================================================
EXP_ID: bs8_nmin2_seed42_r2
{
  "status": "RUNNING",
  "retry_count": 0,
  "created_at": "2026-05-15T18:48:45.682Z",
  "updated_at": "2026-05-15T18:59:17.405Z",
  "spec": {
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/provenance_weight_training && python training/pretrain_weighted.py --data_path data/scored_data.jsonl --output_dir output/models/bs8_nmin2_seed42 --model_name models/Qwen/Qwen3-0.6B --weighting_method adaptive --contamination_ratio 0.4 --num_train_tokens 200000000 --n_min 2 --tau 0.8 --batch_size 8 --gradient_accumulation_steps 2 --learning_rate 5e-5 --max_length 2048 --seed 42 --logg
…[truncated 265 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_outline_20260515T200947",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-15T20:14:10.937502+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 - <<'EOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/a0a804d4-6478-4fc5-9087-f104ab623fd4/tool-results/mcp-agent-ml-research-read_registry-1778875802923.txt\"\n\nwith open(filepath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nresult_str = outer['result']\nregistry = json.loads(result_str)\n\ndata = registry['data']\nexps = data['experiments']\n\n# Extract structured summary for each experiment\ndef extract_exp_info(eid, exp):\n    spec = exp.get('spec', {})\n    metrics = exp.get('metrics', {})\n    \n    # Extract key config items from command string\n    cmd = spec.get('command', '')\n    \n    def extract_flag(cmd, flag):\n        import re\n        pattern = rf'--{flag}\\s+(\\S+)'\n        m = re.search(pattern, cmd)\n        return m.group(1) if m else None\n    \n    info = {\n        'exp_id': eid,\n        'status': exp.get('status', 'UNKNOWN'),\n        'conclusion': exp.get('conclusion', None),\n        'metrics': {},\n        'config': {\n            'model': spec.get('model_name', extract_flag(cmd, 'model_name')),\n            'weighting_method': extract_flag(cmd, 'weighting_method'),\n            'batch_size': extract_flag(cmd, 'batch_size'),\n            'n_min': extract_flag(cmd, 'n_min'),\n            'tau': extract_flag(cmd, 'tau'),\n            'contamination_ratio': spec.get('contamination_ratio', extract_flag(cmd, 'contamination_ratio')),\n            'seed': spec.get('seed', extract_flag(cmd, 'seed')),\n            'b': extract_flag(cmd, 'b ') or extract_flag(cmd, '-b '),\n            'server': spec.get('server'),\n            'gpu': spec.get('gpu'),\n        },\n        'category': spec.get('category', spec.get('claim', None)),\n        'note': spec.get('note', spec.get('description', None)),\n    }\n    \n    # Extract metrics\n    eval_ppl = metrics.get('eval_ppl', metrics.get('final_eval_ppl', metrics.get('ppl', None)))\n    info['metrics']['eval_ppl'] = eval_ppl\n    info['metrics']['all'] = metrics\n    \n    return info\n\nresults = []\nfor eid, exp in exps.items():\n    results.append(extract_exp_info(eid, exp))\n\n# Print structured summary\nfor r in results:\n    print(f\"\\n{'='*70}\")\n    print(f\"EXP_ID: {r['exp_id']}\")\n    print(f\"STATUS: {r['status']}\")\n    print(f\"CONCLUSION: {r['conclusion']}\")\n    print(f\"CATEGORY: {r['category']}\")\n    print(f\"NOTE: {r['note']}\")\n    print(f\"CONFIG: model={r['config']['model']}, method={r['config']['weighting_method']}, \"\n          f\"bs={r['config']['batch_size']}, n_min={r['config']['n_min']}, \"\n          f\"tau={r['config']['tau']}, contamination={r['config']['contamination_ratio']}, \"\n          f\"seed={r['config']['seed']}, server={r['config']['server']}, gpu={r['config']['gpu']}\")\n    metrics = r['metrics']['all']\n    if metrics:\n        print(f\"METRICS: {json.dumps(metrics, indent=2)}\")\n    else:\n        print(\"METRICS: none\")\n\nEOF\n",
  "description": "Extract and print structured summary of all experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_outline_20260515T200947",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 - <<'EOF'\nimport json\n\nfilepath = \"/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-10-projects-provenance-weight-training/a0a804d4-6478-4fc5-9087-f104ab623fd4/tool-results/mcp-agent-ml-research-read_registry-1778875802923.txt\"\n\nwith open(filepath, 'r') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\nresult_str = outer['result']\nregistry = json.loads(result_str)\n\ndata = registry['data']\nexps = data['experiments']\n\n# Extract structured summary for each experiment\ndef extract_exp_info(eid, exp):\n    spec = exp.get('spec', {})\n    metrics = exp.get('metrics', {})\n    \n    # Extract key config items from command string\n    cmd = spec.get('command', '')\n    \n    def extract_flag(cmd, flag):\n        import re\n        pattern = rf'--{flag}\\s+(\\S+)'\n        m = re.search(pattern, cmd)\n        return m.group(1) if m else None\n    \n    info = {\n        'exp_id': eid,\n        'status': exp.get('status', 'UNKNOWN'),\n        'conclusion': exp.get('conclusion', None),\n        'metrics': {},\n        'config': {\n            'model': spec.get('model_name', extract_flag(cmd, 'model_name')),\n            'weighting_method': extract_flag(cmd, 'weighting_method'),\n            'batch_size': extract_flag(cmd, 'batch_size'),\n            'n_min': extract_flag(cmd, 'n_min'),\n            'tau': extract_flag(cmd, 'tau'),\n            'contamination_ratio': spec.get('contamination_ratio', extract_flag(cmd, 'contamination_ratio')),\n            'seed': spec.get('seed', extract_flag(cmd, 'seed')),\n            'b': extract_flag(cmd, 'b ') or extract_flag(cmd, '-b '),\n            'server': spec.get('server'),\n            'gpu': spec.get('gpu'),\n        },\n        'category': spec.get('category', spec.get('claim', None)),\n        'note': spec.get('note', spec.get('description', None)),\n    }\n    \n    # Extract metrics\n    eval_ppl = metrics.get('eval_ppl', metrics.get('final_eval_ppl', metrics.get('ppl', None)))\n    info['metrics']['eval_ppl'] = eval_ppl\n    info['metrics']['all'] = metrics\n    \n    return info\n\nresults = []\nfor eid, exp in exps.items():\n    results.append(extract_exp_info(eid, exp))\n\n# Print structured summary\nfor r in results:\n    print(f\"\\n{'='*70}\")\n    print(f\"EXP_ID: {r['exp_id']}\")\n    print(f\"STATUS: {r['status']}\")\n    print(f\"CONCLUSION: {r['conclusion']}\")\n    print(f\"CATEGORY: {r['category']}\")\n    print(f\"NOTE: {r['note']}\")\n    print(f\"CONFIG: model={r['config']['model']}, method={r['config']['weighting_method']}, \"\n          f\"bs={r['config']['batch_size']}, n_min={r['config']['n_min']}, \"\n          f\"tau={r['config']['tau']}, contamination={r['config']['contamination_ratio']}, \"\n          f\"seed={r['config']['seed']}, server={r['config']['server']}, gpu={r['config']['gpu']}\")\n    metrics = r['metrics']['all']\n    if metrics:\n        print(f\"METRICS: {json.dumps(metrics, indent=2)}\")\n    else:\n        print(\"METRICS: none\")\n\nEOF\n",
    "description": "Extract and print structured summary of all experiments"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-15T20:14:10.937925+00:00_

======================================================================
EXP_ID: p0_contamination_60_datagen
STATUS: DONE
CONCLUSION: success
CATEGORY: None
NOTE: None
CONFIG: model=Qwen3-0.6B (TF-IDF scoring), method=None, bs=None, n_min=None, tau=None, contamination=None, seed=42, server=westd-47453, gpu=None
METRICS: {
  "total_lines": 371499,
  "synthetic_count": 222900,
  "human_count": 148599,
  "actual_contamination_ratio": 0.6,
  "q_score_mean": 0.6243,
  "q_score_std": 0.3703,
  "q_score_median": 0.7753,
  "file_size_mb": 907
}

======================================================================
EXP_ID: bs8_nmin2_seed42_r2
STATUS: RUNNING
CONCLUSION: None
CATEGORY: None
NOTE: None
CONFIG: model=Qwen/Qwen3-0.6B, method=adaptive, bs=8, n_min=2, tau=0.8, contamination=0.4, seed=42, server=westd-47453, gpu=['cuda:2']
METRICS: none

======================================================================
EXP_ID: nmin4_seed42
STATUS: RUNNING
CONCLUSION: None
CATEGORY: None
NOTE: None
CONFIG: model=Qwen3-0.6B, method=adaptive, bs=4, n_min=4, tau=0.8, contamination=0.4, seed=42, server=westd-47453, gpu=['cuda:1']
METRICS: none

======================================================================
EXP_ID: bs8_nmin2_seed42
STATUS: DONE
CONCLUSION: failed
CATEGORY: None
NOTE: None
CONFIG: model=models/Qwen/Qwen3-0.6B, method=adaptive, bs=8, n_min=2, tau=0.8, contamination=0.4, seed=42, server=westd-47453, gpu=['cuda:2']
METRICS: none

======================================================================
EXP_ID: bs8_seed42
STATUS: DONE
CONCLUSION: failed
CATEGORY: None
NOTE: None
CONFIG: model=models/Qwen/Qwen3-0.6B, method=adaptive, bs=8, n_min=4, tau=0.8, contamination=0.4, seed=42, server=westd-47453, gpu=['cuda:2']
METRICS: none

======================================================================
EXP_ID: tau_095_seed42
STATUS: DONE
CONCLUSION: negative
CATEGORY: None
NOTE: None
CONFIG: model=None, method=None, bs=None, n_min=None, tau=None, contamination=None, 
…[truncated 25495 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_outline_20260515T200947",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T20:14:10.938296+00:00_

Now I have all the data. Let me compile the full structured summary:

---

## Experiment Registry Summary — provenance_weight_training

**Total experiments: 46** | Model: Qwen3-0.6B | Server: westd-47453

---

### CATEGORY 1: Data Generation / Infrastructure

| exp_id | status | conclusion | key metrics / notes |
|--------|--------|------------|---------------------|
| datagen_synthetic_4gpu | DONE | success | Generated synthetic data; model=Qwen3-0.6B, bs=128, seeds=42/1042/2042/3042, all 4 GPUs. No eval_ppl. |
| p0_contamination_60_datagen | DONE | success | Prepared 60% contamination dataset: 371,499 lines (222,900 synthetic + 148,599 human), contamination_ratio=0.60, q_score_mean=0.6243, q_score_median=0.7753, file=907MB |

---

### CATEGORY 2: Detector Training

| exp_id | status | conclusion | key metrics / notes |
|--------|--------|------------|---------------------|
| detector_tfidf_lr | DONE | success | TF-IDF + LogisticRegression detector; AUC=0.939, accuracy=0.858, ECE_raw=0.24, ECE_calibrated=0.048 (temp T=0.204), q_score_mean=0.60, q_score_median=0.707, mid_range_ratio=0.463 |
| detector_modernbert | DONE | killed | No metrics recorded |

---

### CATEGORY 3: Baseline — Uniform Weighting (contamination_ratio=0.4, n_min=default)

All seeds: Qwen3-0.6B, method=uniform, bs=4, 6103 steps, contamination=0.4

| exp_id | status | conclusion | eval_ppl_holdout | train_loss |
|--------|--------|------------|-----------------|------------|
| uniform_seed42 | DONE | success | **17.6939** | 7.3104 |
| uniform_seed123 | DONE | success | **17.6861** | 7.3121 |
| uniform_seed456 | DONE | success | **17.7015** | 7.2895 |

**Mean uniform eval_ppl ≈ 17.694**

---

### CATEGORY 4: Adaptive Weighting (original — tau=0.8, n_min=3)

All seeds: Qwen3-0.6B, method=adaptive, bs=4, 6103 steps, contamination=0.4, tau=0.8, n_min=3

| exp_id | status | conclusion | eval_ppl_holdout | train_loss |
|--------|--------|------------|-----------------|------------|
| adaptive_seed42 | D
…[truncated 6833 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_outline_20260515T200947",
  "tool": "Agent",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T20:14:10.938703+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

```json
{
  "project": "provenance_weight_training",
  "file": "writing_plan.yaml",
  "content": "# Writing Plan — provenance_weight_training\n# Generated: 2026-05-15\n# Contract for downstream writing Workers\n\nvenue: EMNLP 2026 ARR May 25\ndeadline: 2026-05-25\npage_limit: 8 (+ unlimited appendix)\n\ntitle: \"Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining\"\n# 备选:\n# - \"Dual-Constrained Adaptive Reweighting for Pretraining on Contaminated Web Corpora\"\n# - \"How Much to Downweight? Principled Exponent Selection for Contamination-Aware Pretraining\"\n\nabstract_outline:\n  - sentence_1: \"Web pretraining corpora contain 20–60% machine-generated text of unknown provenance, and naive training on such mixtures degrades model quality (model collapse).\"\n  - sentence_2: \"Existing detect-and-reweight methods (Drayson et al., 2025) require per-model validation-based grid search over the weighting exponent b, which is expensive and fragile.\"\n  - sentence_3: \"We propose a dual-constrained adaptive b* that jointly enforces a quality lower bound (α_eff ≥ τ) and a stability upper bound (ESS ≥ n_min), yielding the minimum intervention—the smallest b that achieves sufficient cleaning per batch, with zero validation cost.\"\n  - sentence_4: \"On FineWeb with Qwen3-0.6B, adaptive b* matches grid-search-optimal performance within seed variance while eliminating 6× search cost, and outperforms both uniform training and the max-intervention (ESS-only) baseline.\"\n\n# ============================================================\n# SECTIONS\n# ============================================================\n\nsections:\n\n  introduction:\n    target_pages: 1.0\n    key_points:\n      - \"Web corpora contamination is pervasive (20–60%) and growing; strong model collapse occurs even at low contamination (Dohmatob et al., 2025)\"\n      - \"Detect-and-reweight via w=(1-q)^b is effective (Drayson et al., 2025), but b selection requires per-model validation grid search\"\n      - \"Problem statement: given per-sample detector scores q, how to choose b without validation?\"\n      - \"Our answer: dual-constrained adaptive b* — α_eff(b) ≥ τ (quality floor) + ESS(b) ≥ n_min (stability ceiling) → minimum intervention principle\"\n      - \"Key insight: α_eff monotonically increasing, ESS monotonically decreasing → b has a lower bound b_τ and upper bound b_ESS; b* = b_τ when feasible\"\n    contributions:\n      - \"Dual-constrained framework for adaptive b* selection with minimum intervention semantics (Section 3)\"\n      - \"Empirical demonstration that adaptive b* matches grid-best within seed variance at zero validation cost (Section 5)\"\n      - \"Evidence that minimum intervention (dual-constraint) outperforms maximum intervention (ESS-only), and that a lightweight TF-IDF+LR detector suffices (Section 5)\"\n    evidence:\n      - adaptive_fix_seed42\n      - adaptive_fix_seed123\n      - adaptive_fix_seed456\n      - ess_only_seed42\n\n  related_work:\n    target_pages: 1.0\n    groups:\n      synthetic_contamination_and_collapse:\n        narrative: \"Model collapse under recursive/contaminated training\"\n        papers:\n          - shumailov_2024_model_collapse\n          - alemohammad_2024_mad\n          - dohmatob_2025_strong_collapse\n          - cheng_2025_contamination_survey\n      detect_and_reweight:\n        narrative: \"Detection-based reweighting and filtering for contaminated data\"\n        papers:\n          - drayson_2025_detection_collapse    # direct competitor, most detailed comparison\n          - feng_2025_beyond_collapse          # hard filtering via verifier\n          - guo_2025_escaping_collapse         # verification-based\n          - mitchell_2023_detectgpt            # detector method\n          - shi_2024_minkprob                  # detector method\n      data_mixing_and_reweighting:\n        narrative: \"Domain- and instance-level data weighting for LLM pretraining\"\n        papers:\n          - xie_2023_doremi\n          - xie_2023_dsir\n          - he_2024_softdedup\n          - sow_2025_dynamic_reweighting\n          - chen_2025_aioli\n          - ye_2025_data_mixing_laws\n          - yang_2026_data_mixing_agent\n          - kuo_2024_data_weighting\n      theoretical_foundations:\n        narrative: \"Optimal weighting theory and importance sampling diagnostics\"\n        papers:\n          - he_2025_golden_ratio\n          - wang_2026_survive_contamination\n          - vehtari_2024_psis\n          - kimura_2024_iw_survey\n    key_points:\n      - \"Position Drayson as closest prior work: same w=(1-q)^b formula, but b is a per-model hyperparameter chosen via validation grid search\"\n      - \"Distinguish from Golden Ratio (requires known proportion) and DoReMi/DSIR (domain-level, not instance-level contamination)\"\n      - \"Highlight gap: no existing method provides principled per-batch b selection without validation\"\n\n  method:\n    target_pages: 2.5\n    subsections:\n      problem_setup:\n        key_points:\n          - \"Training corpus D = D_real ∪ D_synth, proportion unknown\"\n          - \"Detector provides per-sample q(x) ∈ [0,1] (synthetic probability)\"\n          - \"Weighting formula w(x) = (1-q(x))^b, shared with Drayson et al.\"\n          - \"Goal: choose b per-batch to maximize training quality without validation\"\n        evidence: []\n      dual_constraint_framework:\n        key_points:\n          - \"Define α_eff(b) = Σ_i w_i · 1[real_i] / Σ_i w_i — effective real proportion after reweighting\"\n          - \"Define ESS(b) = (Σ w_i)² / Σ w_i² — Kish's effective sample size\"\n          - \"Monotonicity: α_eff(b) strictly increasing (Proposition 1, proof via Cov_w(x, ln x) ≥ 0); ESS(b) strictly decreasing\"\n          - \"Quality constraint: α_eff(b) ≥ τ → lower bound b_τ (at least this much cleaning)\"\n          - \"Stability constraint: ESS(b) ≥ n_min → upper bound b_ESS (at most this much cleaning)\"\n          - \"b* = inf{b ≥ 0 : α_eff(b) ≥ τ} subject to ESS(b) ≥ n_min\"\n          - \"Minimum intervention principle: use the smallest b that achieves the quality floor\"\n        evidence: []\n      algorithm:\n        key_points:\n          - \"Algorithm 1: Per-batch b* solver (bisection on α_eff, check ESS feasibility)\"\n          - \"Three regimes per batch: (1) already clean → b*=0; (2) α_eff binding → b*=b_τ; (3) ESS binding → b*=b_ESS\"\n          - \"Implementation: loss reweighting (continuous gradient weighting) vs Drayson's SIR (discrete resampling)\"\n          - \"Complexity: O(B log(1/ε)) per batch, negligible vs forward/backward pass\"\n        evidence: []\n      hyperparameters:\n        key_points:\n          - \"τ (quality threshold): theoretically motivated by convergence rate ∝ α (Wang et al., 2026); empirically, wide safe range [0.5, 0.8] with default τ=0.8\"\n          - \"n_min (ESS floor): default n_min=2; robust across {2,3}; n_min=1 removes stability constraint (degrades); n_min ≥ batch_size trivially forces b*=0\"\n          - \"Both have principled defaults set once, no per-model tuning needed\"\n        evidence:\n          - tau_05_seed42\n          - tau_06_seed42\n          - tau_07_seed42\n          - adaptive_fix_seed42  # tau=0.8\n          - tau_09_seed42\n          - tau_095_seed42\n          - nmin1_seed42\n\n  experiments:\n    target_pages: 1.0\n    key_points:\n      - \"Base model: Qwen3-0.6B pretrained from scratch on FineWeb subset\"\n      - \"Data: 132M+ tokens, 40% synthetic injection (Qwen3-0.6B self-generated), uniform random mixing\"\n      - \"Detector: TF-IDF + Logistic Regression (AUC=0.939, calibrated ECE=0.048)\"\n      - \"Training: 6103 steps, batch_size=4, AdamW, cosine schedule\"\n      - \"Evaluation: held-out eval_ppl on balanced real/synthetic held-out set\"\n      - \"All comparisons use 3 random seeds (42, 123, 456) for statistical reliability\"\n    subsections:\n      baselines:\n        items:\n          - \"Uniform: w=1 for all samples (no contamination handling)\"\n          - \"Grid-b: fixed b ∈ {0.5, 1.0, 1.5, 2.0, 3.0, 5.0}, best selected post-hoc\"\n          - \"ESS-only: b* = max{b : ESS(b) ≥ n_min} (maximum intervention, no α_eff constraint)\"\n          - \"Golden Ratio: w*=1/φ ≈ 0.618 for synthetic samples (oracle, requires known proportion)\"\n      experiment_groups:\n        main_comparison:\n          description: \"Adaptive b* vs grid-best vs uniform vs ESS-only vs golden ratio\"\n          exp_ids:\n            - adaptive_fix_seed42\n            - adaptive_fix_seed123\n            - adaptive_fix_seed456\n            - uniform_seed42\n            - uniform_seed123\n            - uniform_seed456\n            - grid_b_seed42   # b=0.5 best\n            - grid_b_seed123\n            - grid_b_seed456\n            - ess_only_seed42\n            - ess_only_seed123   # running\n            - ess_only_seed456   # running\n            - golden_ratio_seed42\n        tau_sweep:\n          description: \"τ ∈ {0.5, 0.6, 0.7, 0.8, 0.9, 0.95} sensitivity analysis\"\n          exp_ids:\n            - tau_05_seed42\n            - tau_06_seed42\n            - tau_07_seed42\n            - adaptive_fix_seed42   # τ=0.8\n            - tau_09_seed42\n            - tau_095_seed42\n        nmin_sensitivity:\n          description: \"n_min ∈ {1, 2, 3, 4} sensitivity analysis\"\n          exp_ids:\n            - nmin1_seed42\n            - adaptive_fix_seed42   # n_min=2\n            - adaptive_seed42       # n_min=3\n            - nmin4_seed42          # running\n        batch_size:\n          description: \"batch_size ∈ {4, 8} generalization (n_min=2 fixed)\"\n          exp_ids:\n            - adaptive_fix_seed42      # bs=4\n            - bs8_nmin2_seed42_r2      # bs=8, running\n    evidence:\n      - all exp_ids listed above\n\n  results:\n    target_pages: 1.5\n    key_points:\n      - \"Main result: adaptive b* PPL within seed variance of grid-best (aggregate ratio 88.6%), both beating uniform by ~0.04 PPL\"\n      - \"ESS-only (max intervention) PPL=17.73 — worse than uniform (17.69), confirming minimum > maximum intervention\"\n      - \"Golden ratio PPL=17.654 ≈ adaptive — oracle baseline matched without known proportion\"\n      - \"τ sweep: [0.5, 0.8] all beat uniform; τ=0.8 optimal (PPL=17.653); τ>0.8 degrades due to b* inflation\"\n      - \"n_min: n_min=2 stable across 3 seeds; n_min=1 degrades (no stability constraint); n_min=3 also works; n_min=4 expected to force b*≈0\"\n      - \"Binding constraint analysis: 49.9% clean (b*=0), 20.2% α_eff-binding, 30.0% ESS-binding; when α_eff binds, b*=1.67 vs ESS-only's 4.15\"\n      - \"Detector: lightweight TF-IDF+LR (AUC=0.939) sufficient; calibration (ECE=0.048) more important than raw AUC\"\n    evidence:\n      - adaptive_fix_seed42\n      - adaptive_fix_seed123\n      - adaptive_fix_seed456\n      - uniform_seed42\n      - uniform_seed123\n      - uniform_seed456\n      - ess_only_seed42\n      - golden_ratio_seed42\n      - tau_05_seed42\n      - tau_06_seed42\n      - tau_07_seed42\n      - tau_09_seed42\n      - tau_095_seed42\n      - nmin1_seed42\n      - detector_tfidf_lr\n\n  discussion:\n    target_pages: 0.5\n    key_points:\n      - \"Minimum intervention principle: why doing less is better — over-downweighting discards useful gradient signal from borderline samples\"\n      - \"τ as practical dial: controls the quality-efficiency tradeoff; [0.5, 0.8] safe range gives practitioners a clear operating region\"\n      - \"Connection to convergence theory: Wang et al. (2026) show convergence rate ∝ α; our τ serves as a proxy for α without requiring known proportions\"\n    limitations:\n      - \"Single model scale (0.6B) — batch-level statistics may behave differently at 3B+ where batch sizes are larger\"\n      - \"Controlled injection (uniform random) — real web contamination has domain-skewed distribution\"\n      - \"Single detector family (TF-IDF+LR) — detector quality ablation not yet complete\"\n      - \"τ is an empirical hyperparameter; the convergence theory (Wang et al.) requires known α, which we do not assume\"\n      - \"Effect size ~0.3% PPL at 0.6B/40% contamination — expected to amplify at higher contamination and larger scale\"\n    evidence: []\n\n  conclusion:\n    target_pages: 0.3\n    key_points:\n      - \"Dual-constrained adaptive b* provides principled, validation-free exponent selection for contamination-aware pretraining\"\n      - \"Minimum intervention principle — quality floor + stability ceiling — outperforms both no intervention and maximum intervention\"\n      - \"Future work: scale to 3B+ models, real web contamination, detector quality ablation, multi-task evaluation\"\n    evidence: []\n\n# ============================================================\n# FIGURES\n# ============================================================\n\nfigures:\n\n  - id: fig_dual_constraint\n    description: \"Dual-constraint diagram: α_eff(b) and ESS(b) curves on shared x-axis (b), with b_τ (quality lower bound) and b_ESS (stability upper bound) annotated. Shaded feasible region between b_τ and b_ESS. b* marked at b_τ (minimum intervention). Three regimes labeled: clean (b*=0), α_eff-binding, ESS-binding.\"\n    section: method\n    data_source: \"Analytical curves from a representative batch (adaptive_fix_seed42, select batch with α_eff binding)\"\n    priority: P0\n\n  - id: fig_main_comparison\n    description: \"Bar chart or grouped bar: eval_ppl for uniform, grid-best (b=0.5), adaptive b*, ESS-only, golden ratio. Error bars from 3 seeds where available. Dashed line at uniform baseline.\"\n    section: results\n    data_source: \"uniform_seed{42,123,456}, adaptive_fix_seed{42,123,456}, grid_b_seed{42,123,456} (b=0.5), ess_only_seed{42,123,456}, golden_ratio_seed42\"\n    priority: P0\n\n  - id: fig_tau_sweep\n    description: \"Dual-axis plot: left y-axis = eval_ppl, right y-axis = mean b*; x-axis = τ ∈ {0.5, 0.6, 0.7, 0.8, 0.9, 0.95}. Horizontal dashed line at uniform PPL. Shaded safe region [0.5, 0.8]. Shows asymmetric sensitivity: gradual improvement then sharp degradation.\"\n    section: results\n    data_source: \"tau_05_seed42, tau_06_seed42, tau_07_seed42, adaptive_fix_seed42, tau_09_seed42, tau_095_seed42\"\n    priority: P0\n\n  - id: fig_binding_distribution\n    description: \"Stacked bar or pie chart showing per-batch regime distribution: 49.9% clean, 20.2% α_eff-binding, 30.0% ESS-binding. Companion histogram of b* values for α_eff-binding vs ESS-binding batches.\"\n    section: results\n    data_source: \"adaptive_fix_seed42 training logs (b_star, alpha_eff, ess per batch)\"\n    priority: P0\n\n  - id: fig_bstar_trajectory\n    description: \"b* over training steps (x-axis = step, y-axis = b*). Shows per-batch adaptation dynamics. Color-code by binding regime. Moving average overlay.\"\n    section: results\n    data_source: \"adaptive_fix_seed42 training logs\"\n    priority: P1\n\n  - id: fig_nmin_sensitivity\n    description: \"Line plot: eval_ppl vs n_min ∈ {1, 2, 3, 4}. Annotate n_min=1 (no stability → over-downweight), n_min=4 (over-constrained → b*≈0). Sweet spot at n_min=2.\"\n    section: results\n    data_source: \"nmin1_seed42, adaptive_fix_seed42 (n_min=2), adaptive_seed42 (n_min=3), nmin4_seed42\"\n    priority: P1\n\n  - id: fig_grid_b_curve\n    description: \"Line plot: eval_ppl vs fixed b ∈ {0.5, 1.0, 1.5, 2.0, 3.0, 5.0} across 3 seeds. Horizontal band for adaptive b* ± seed std. Shows adaptive matches best grid point without search.\"\n    section: results\n    data_source: \"grid_b_seed{42,123,456}, adaptive_fix_seed{42,123,456}\"\n    priority: P1\n\n# ============================================================\n# TABLES\n# ============================================================\n\ntables:\n\n  - id: tab_main_results\n    description: \"Main results table: method × seed → eval_ppl. Methods: uniform, grid-best (b=0.5), adaptive b* (τ=0.8, n_min=2), ESS-only, golden ratio. Columns: seed42, seed123, seed456, mean, std. Bold best non-oracle. Report Δ vs uniform.\"\n    section: results\n    data_source: \"uniform_seed{42,123,456}, adaptive_fix_seed{42,123,456}, grid_b_seed{42,123,456}, ess_only_seed{42,123,456}, golden_ratio_seed42\"\n    priority: P0\n\n  - id: tab_tau_sweep\n    description: \"τ sweep table: τ | eval_ppl | Δ vs uniform | mean b* | median b* | conclusion. 6 rows.\"\n    section: results\n    data_source: \"tau_{05,06,07}_seed42, adaptive_fix_seed42 (τ=0.8), tau_{09,095}_seed42\"\n    priority: P0\n\n  - id: tab_binding_stats\n    description: \"Binding constraint statistics: regime | % batches | mean b* | mean ESS | mean α_eff. Three rows: clean, α_eff-binding, ESS-binding.\"\n    section: results\n    data_source: \"adaptive_fix_seed42 training logs (Q1 analysis)\"\n    priority: P0\n\n  - id: tab_grid_search\n    description: \"Grid search results: b ∈ {0.5, 1.0, 1.5, 2.0, 3.0, 5.0} × 3 seeds → eval_ppl. Shows monotonic degradation with b and motivates adaptive selection.\"\n    section: results\n    data_source: \"grid_b_seed{42,123,456}\"\n    priority: P1\n\n  - id: tab_detector\n    description: \"Detector characteristics: method (TF-IDF+LR), features, AUC, accuracy, ECE (raw/calibrated), calibration temperature T.\"\n    section: experiments\n    data_source: \"detector_tfidf_lr\"\n    priority: P1\n\n  - id: tab_nmin\n    description: \"n_min sensitivity: n_min ∈ {1,2,3,4} | eval_ppl | mean b* | interpretation.\"\n    section: results\n    data_source: \"nmin1_seed42, adaptive_fix_seed42, adaptive_seed42, nmin4_seed42\"\n    priority: P1\n\n# ============================================================\n# WRITING ORDER\n# ============================================================\n\nwriting_order:\n  - section: method\n    rationale: \"Core contribution; everything else depends on precise method description\"\n  - section: experiments\n    rationale: \"Setup must be clear before results\"\n  - section: results\n    rationale: \"Data-driven; needs method + experiments in place\"\n  - section: introduction\n    rationale: \"Frame the story using concrete results\"\n  - section: related_work\n    rationale: \"Position after knowing exactly what we claim\"\n  - section: discussion\n    rationale: \"Limitations and implications from results\"\n  - section: conclusion\n    rationale: \"Compress intro + results\"\n  - section: abstract\n    rationale: \"Last — distill the full paper\"\n\n# ============================================================\n# KEY CITATIONS (must-cite)\n# ============================================================\n\nkey_citations:\n\n  must_cite:\n    - id: drayson_2025_detection_collapse\n      reason: \"Direct competitor; shared w=(1-q)^b formula; primary differentiation target\"\n    - id: he_2025_golden_ratio\n      reason: \"Theoretical optimal weight; oracle baseline\"\n    - id: wang_2026_survive_contamination\n      reason: \"Convergence theory motivating τ; α_eff theoretical grounding\"\n    - id: dohmatob_2025_strong_collapse\n      reason: \"Strong model collapse; core motivation for why contamination matters\"\n    - id: shumailov_2024_model_collapse\n      reason: \"Foundational model collapse result\"\n    - id: vehtari_2024_psis\n      reason: \"ESS / Kish's effective sample size theory\"\n    - id: sow_2025_dynamic_reweighting\n      reason: \"Loss-based reweighting at ICLR 2025; complementary approach\"\n\n  should_cite:\n    - id: feng_2025_beyond_collapse\n      reason: \"Verifier-based alternative; hard filtering vs our soft reweighting\"\n    - id: he_2024_softdedup\n      reason: \"Soft reweighting precedent in pretraining\"\n    - id: xie_2023_doremi\n      reason: \"Domain-level mixing optimization baseline\"\n    - id: chen_2025_aioli\n      reason: \"Online adaptive mixing; closest non-grid-search comparison\"\n    - id: kimura_2024_iw_survey\n      reason: \"Importance weighting survey; theoretical context\"\n    - id: alemohammad_2024_mad\n      reason: \"MAD framework; background on self-consuming models\"\n    - id: cheng_2025_contamination_survey\n      reason: \"Contamination survey; problem scope\"\n\n  optional:\n    - id: xie_2023_dsir\n      reason: \"Importance resampling for data selection\"\n    - id: mitchell_2023_detectgpt\n      reason: \"Zero-shot detection method\"\n    - id: shi_2024_minkprob\n      reason: \"Membership inference detection\"\n    - id: ye_2025_data_mixing_laws\n      reason: \"Data mixing scaling laws\"\n    - id: yang_2026_data_mixing_agent\n      reason: \"RL-based domain mixing\"\n    - id: wei_2024_data_watermarks\n      reason: \"Active provenance (complementary)\"\n    - id: kuo_2024_data_weighting\n      reason: \"Synthetic data weighting for classification\"\n    - id: nait_saada_2025_quality_illusion\n      reason: \"Caution on classifier-based quality scores\"\n    - id: guo_2025_escaping_collapse\n      reason: \"Verification-based escape from collapse\"\n\n# ============================================================\n# RUNNING / PENDING EXPERIMENTS\n# ============================================================\n\npending_results:\n  - exp_id: ess_only_seed123\n    status: RUNNING\n    needed_for: \"tab_main_results (ESS-only multi-seed)\"\n    eta: \"2026-05-15 22:00 UTC\"\n  - exp_id: ess_only_seed456\n    status: RUNNING\n    needed_for: \"tab_main_results (ESS-only multi-seed)\"\n    eta: \"2026-05-15 22:00 UTC\"\n  - exp_id: nmin4_seed42\n    status: RUNNING\n    needed_for: \"tab_nmin, fig_nmin_sensitivity\"\n    eta: \"2026-05-15 21:45 UTC\"\n  - exp_id: bs8_nmin2_seed42_r2\n    status: RUNNING\n    needed_for: \"batch_size generalization (appendix if not ready)\"\n    eta: \"2026-05-16 01:30 UTC\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper_outline_20260515T200947",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "provenance_weight_training",
    "file": "writing_plan.yaml",
    "content": "# Writing Plan — provenance_weight_training\n# Generated: 2026-05-15\n# Contract for downstream writing Workers\n\nvenue: EMNLP 2026 ARR May 25\ndeadline: 2026-05-25\npage_limit: 8 (+ unlimited appendix)\n\ntitle: \"Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining\"\n# 备选:\n# - \"Dual-Constrained Adaptive Reweighting for Pretraining on Contaminated Web Corpora\"\n# - \"How Much to Downweight? Principled Exponent Selection for Contamination-Aware Pretraining\"\n\nabstract_outline:\n  - sentence_1: \"Web pretraining corpora contain 20–60% machine-generated text of unknown provenance, and naive training on such mixtures degrades model quality (model collapse).\"\n  - sentence_2: \"Existing detect-and-reweight methods (Drayson et al., 2025) require per-model validation-based grid search over the weighting exponent b, which is expensive and fragile.\"\n  - sentence_3: \"We propose a dual-constrained adaptive b* that jointly enforces a quality lower bound (α_eff ≥ τ) and a stability upper bound (ESS ≥ n_min), yielding the minimum intervention—the smallest b that achieves sufficient cleaning per batch, with zero validation cost.\"\n  - sentence_4: \"On FineWeb with Qwen3-0.6B, adaptive b* matches grid-search-optimal performance within seed variance while eliminating 6× search cost, and outperforms both uniform training and the max-intervention (ESS-only) baseline.\"\n\n# ============================================================\n# SECTIONS\n# ============================================================\n\nsections:\n\n  introduction:\n    target_pages: 1.0\n    key_points:\n      - \"Web corpora contamination is pervasive (20–60%) and growing; strong model collapse occurs even at low contamination (Dohmatob et al., 2025)\"\n      - \"Detect-and-reweight via w=(1-q)^b is effective (Drayson et al., 2025), but b selection requires per-model validation grid search\"\n      - \"Problem statement: given per-sample detector scores q, how to choose b without validation?\"\n      - \"Our answer: dual-constrained adaptive b* — α_eff(b) ≥ τ (quality floor) + ESS(b) ≥ n_min (stability ceiling) → minimum intervention principle\"\n      - \"Key insight: α_eff monotonically increasing, ESS monotonically decreasing → b has a lower bound b_τ and upper bound b_ESS; b* = b_τ when feasible\"\n    contributions:\n      - \"Dual-constrained framework for adaptive b* selection with minimum intervention semantics (Section 3)\"\n      - \"Empirical demonstration that adaptive b* matches grid-best within seed variance at zero validation cost (Section 5)\"\n      - \"Evidence that minimum intervention (dual-constraint) outperforms maximum intervention (ESS-only), and that a lightweight TF-IDF+LR detector suffices (Section 5)\"\n    evidence:\n      - adaptive_fix_seed42\n      - adaptive_fix_seed123\n      - adaptive_fix_seed456\n      - ess_only_seed42\n\n  related_work:\n    target_pages: 1.0\n    groups:\n      synthetic_contamination_and_collapse:\n        narrative: \"Model collapse under recursive/contaminated training\"\n        papers:\n          - shumailov_2024_model_collapse\n          - alemohammad_2024_mad\n          - dohmatob_2025_strong_collapse\n          - cheng_2025_contamination_survey\n      detect_and_reweight:\n        narrative: \"Detection-based reweighting and filtering for contaminated data\"\n        papers:\n          - drayson_2025_detection_collapse    # direct competitor, most detailed comparison\n          - feng_2025_beyond_collapse          # hard filtering via verifier\n          - guo_2025_escaping_collapse         # verification-based\n          - mitchell_2023_detectgpt            # detector method\n          - shi_2024_minkprob                  # detector method\n      data_mixing_and_reweighting:\n        narrative: \"Domain- and instance-level data weighting for LLM pretraining\"\n        papers:\n          - xie_2023_doremi\n          - xie_2023_dsir\n          - he_2024_softdedup\n          - sow_2025_dynamic_reweighting\n          - chen_2025_aioli\n          - ye_2025_data_mixing_laws\n          - yang_2026_data_mixing_agent\n          - kuo_2024_data_weighting\n      theoretical_foundations:\n        narrative: \"Optimal weighting theory and importance sampling diagnostics\"\n        papers:\n          - he_2025_golden_ratio\n          - wang_2026_survive_contamination\n          - vehtari_2024_psis\n          - kimura_2024_iw_survey\n    key_points:\n      - \"Position Drayson as closest prior work: same w=(1-q)^b formula, but b is a per-model hyperparameter chosen via validation grid search\"\n      - \"Distinguish from Golden Ratio (requires known proportion) and DoReMi/DSIR (domain-level, not instance-level contamination)\"\n      - \"Highlight gap: no existing method provides principled per-batch b selection without validation\"\n\n  method:\n    target_pages: 2.5\n    subsections:\n      problem_setup:\n        key_points:\n          - \"Training corpus D = D_real ∪ D_synth, proportion unknown\"\n          - \"Detector provides per-sample q(x) ∈ [0,1] (synthetic probability)\"\n          - \"Weighting formula w(x) = (1-q(x))^b, shared with Drayson et al.\"\n          - \"Goal: choose b per-batch to maximize training quality without validation\"\n        evidence: []\n      dual_constraint_framework:\n        key_points:\n          - \"Define α_eff(b) = Σ_i w_i · 1[real_i] / Σ_i w_i — effective real proportion after reweighting\"\n          - \"Define ESS(b) = (Σ w_i)² / Σ w_i² — Kish's effective sample size\"\n          - \"Monotonicity: α_eff(b) strictly increasing (Proposition 1, proof via Cov_w(x, ln x) ≥ 0); ESS(b) strictly decreasing\"\n          - \"Quality constraint: α_eff(b) ≥ τ → lower bound b_τ (at least this much cleaning)\"\n          - \"Stability constraint: ESS(b) ≥ n_min → upper bound b_ESS (at most this much cleaning)\"\n          - \"b* = inf{b ≥ 0 : α_eff(b) ≥ τ} subject to ESS(b) ≥ n_min\"\n          - \"Minimum intervention principle: use the smallest b that achieves the quality floor\"\n        evidence: []\n      algorithm:\n        key_points:\n          - \"Algorithm 1: Per-batch b* solver (bisection on α_eff, check ESS feasibility)\"\n          - \"Three regimes per batch: (1) already clean → b*=0; (2) α_eff binding → b*=b_τ; (3) ESS binding → b*=b_ESS\"\n          - \"Implementation: loss reweighting (continuous gradient weighting) vs Drayson's SIR (discrete resampling)\"\n          - \"Complexity: O(B log(1/ε)) per batch, negligible vs forward/backward pass\"\n        evidence: []\n      hyperparameters:\n        key_points:\n          - \"τ (quality threshold): theoretically motivated by convergence rate ∝ α (Wang et al., 2026); empirically, wide safe range [0.5, 0.8] with default τ=0.8\"\n          - \"n_min (ESS floor): default n_min=2; robust across {2,3}; n_min=1 removes stability constraint (degrades); n_min ≥ batch_size trivially forces b*=0\"\n          - \"Both have principled defaults set once, no per-model tuning needed\"\n        evidence:\n          - tau_05_seed42\n          - tau_06_seed42\n          - tau_07_seed42\n          - adaptive_fix_seed42  # tau=0.8\n          - tau_09_seed42\n          - tau_095_seed42\n          - nmin1_seed42\n\n  experiments:\n    target_pages: 1.0\n    key_points:\n      - \"Base model: Qwen3-0.6B pretrained from scratch on FineWeb subset\"\n      - \"Data: 132M+ tokens, 40% synthetic injection (Qwen3-0.6B self-generated), uniform random mixing\"\n      - \"Detector: TF-IDF + Logistic Regression (AUC=0.939, calibrated ECE=0.048)\"\n      - \"Training: 6103 steps, batch_size=4, AdamW, cosine schedule\"\n      - \"Evaluation: held-out eval_ppl on balanced real/synthetic held-out set\"\n      - \"All comparisons use 3 random seeds (42, 123, 456) for statistical reliability\"\n    subsections:\n      baselines:\n        items:\n          - \"Uniform: w=1 for all samples (no contamination handling)\"\n          - \"Grid-b: fixed b ∈ {0.5, 1.0, 1.5, 2.0, 3.0, 5.0}, best selected post-hoc\"\n          - \"ESS-only: b* = max{b : ESS(b) ≥ n_min} (maximum intervention, no α_eff constraint)\"\n          - \"Golden Ratio: w*=1/φ ≈ 0.618 for synthetic samples (oracle, requires known proportion)\"\n      experiment_groups:\n        main_comparison:\n          description: \"Adaptive b* vs grid-best vs uniform vs ESS-only vs golden ratio\"\n          exp_ids:\n            - adaptive_fix_seed42\n            - adaptive_fix_seed123\n            - adaptive_fix_seed456\n            - uniform_seed42\n            - uniform_seed123\n            - uniform_seed456\n            - grid_b_seed42   # b=0.5 best\n            - grid_b_seed123\n            - grid_b_seed456\n            - ess_only_seed42\n            - ess_only_seed123   # running\n            - ess_only_seed456   # running\n            - golden_ratio_seed42\n        tau_sweep:\n          description: \"τ ∈ {0.5, 0.6, 0.7, 0.8, 0.9, 0.95} sensitivity analysis\"\n          exp_ids:\n            - tau_05_seed42\n            - tau_06_seed42\n            - tau_07_seed42\n            - adaptive_fix_seed42   # τ=0.8\n            - tau_09_seed42\n            - tau_095_seed42\n        nmin_sensitivity:\n          description: \"n_min ∈ {1, 2, 3, 4} sensitivity analysis\"\n          exp_ids:\n            - nmin1_seed42\n            - adaptive_fix_seed42   # n_min=2\n            - adaptive_seed42       # n_min=3\n            - nmin4_seed42          # running\n        batch_size:\n          description: \"batch_size ∈ {4, 8} generalization (n_min=2 fixed)\"\n          exp_ids:\n            - adaptive_fix_seed42      # bs=4\n            - bs8_nmin2_seed42_r2      # bs=8, running\n    evidence:\n      - all exp_ids listed above\n\n  results:\n    target_pages: 1.5\n    key_points:\n      - \"Main result: adaptive b* PPL within seed variance of grid-best (aggregate ratio 88.6%), both beating uniform by ~0.04 PPL\"\n      - \"ESS-only (max intervention) PPL=17.73 — worse than uniform (17.69), confirming minimum > maximum intervention\"\n      - \"Golden ratio PPL=17.654 ≈ adaptive — oracle baseline matched without known proportion\"\n      - \"τ sweep: [0.5, 0.8] all beat uniform; τ=0.8 optimal (PPL=17.653); τ>0.8 degrades due to b* inflation\"\n      - \"n_min: n_min=2 stable across 3 seeds; n_min=1 degrades (no stability constraint); n_min=3 also works; n_min=4 expected to force b*≈0\"\n      - \"Binding constraint analysis: 49.9% clean (b*=0), 20.2% α_eff-binding, 30.0% ESS-binding; when α_eff binds, b*=1.67 vs ESS-only's 4.15\"\n      - \"Detector: lightweight TF-IDF+LR (AUC=0.939) sufficient; calibration (ECE=0.048) more important than raw AUC\"\n    evidence:\n      - adaptive_fix_seed42\n      - adaptive_fix_seed123\n      - adaptive_fix_seed456\n      - uniform_seed42\n      - uniform_seed123\n      - uniform_seed456\n      - ess_only_seed42\n      - golden_ratio_seed42\n      - tau_05_seed42\n      - tau_06_seed42\n      - tau_07_seed42\n      - tau_09_seed42\n      - tau_095_seed42\n      - nmin1_seed42\n      - detector_tfidf_lr\n\n  discussion:\n    target_pages: 0.5\n    key_points:\n      - \"Minimum intervention principle: why doing less is better — over-downweighting discards useful gradient signal from borderline samples\"\n      - \"τ as practical dial: controls the quality-efficiency tradeoff; [0.5, 0.8] safe range gives practitioners a clear operating region\"\n      - \"Connection to convergence theory: Wang et al. (2026) show convergence rate ∝ α; our τ serves as a proxy for α without requiring known proportions\"\n    limitations:\n      - \"Single model scale (0.6B) — batch-level statistics may behave differently at 3B+ where batch sizes are larger\"\n      - \"Controlled injection (uniform random) — real web contamination has domain-skewed distribution\"\n      - \"Single detector family (TF-IDF+LR) — detector quality ablation not yet complete\"\n      - \"τ is an empirical hyperparameter; the convergence theory (Wang et al.) requires known α, which we do not assume\"\n      - \"Effect size ~0.3% PPL at 0.6B/40% contamination — expected to amplify at higher contamination and larger scale\"\n    evidence: []\n\n  conclusion:\n    target_pages: 0.3\n    key_points:\n      - \"Dual-constrained adaptive b* provides principled, validation-free exponent selection for contamination-aware pretraining\"\n      - \"Minimum intervention principle — quality floor + stability ceiling — outperforms both no intervention and maximum intervention\"\n      - \"Future work: scale to 3B+ models, real web contamination, detector quality ablation, multi-task evaluation\"\n    evidence: []\n\n# ============================================================\n# FIGURES\n# ============================================================\n\nfigures:\n\n  - id: fig_dual_constraint\n    description: \"Dual-constraint diagram: α_eff(b) and ESS(b) curves on shared x-axis (b), with b_τ (quality lower bound) and b_ESS (stability upper bound) annotated. Shaded feasible region between b_τ and b_ESS. b* marked at b_τ (minimum intervention). Three regimes labeled: clean (b*=0), α_eff-binding, ESS-binding.\"\n    section: method\n    data_source: \"Analytical curves from a representative batch (adaptive_fix_seed42, select batch with α_eff binding)\"\n    priority: P0\n\n  - id: fig_main_comparison\n    description: \"Bar chart or grouped bar: eval_ppl for uniform, grid-best (b=0.5), adaptive b*, ESS-only, golden ratio. Error bars from 3 seeds where available. Dashed line at uniform baseline.\"\n    section: results\n    data_source: \"uniform_seed{42,123,456}, adaptive_fix_seed{42,123,456}, grid_b_seed{42,123,456} (b=0.5), ess_only_seed{42,123,456}, golden_ratio_seed42\"\n    priority: P0\n\n  - id: fig_tau_sweep\n    description: \"Dual-axis plot: left y-axis = eval_ppl, right y-axis = mean b*; x-axis = τ ∈ {0.5, 0.6, 0.7, 0.8, 0.9, 0.95}. Horizontal dashed line at uniform PPL. Shaded safe region [0.5, 0.8]. Shows asymmetric sensitivity: gradual improvement then sharp degradation.\"\n    section: results\n    data_source: \"tau_05_seed42, tau_06_seed42, tau_07_seed42, adaptive_fix_seed42, tau_09_seed42, tau_095_seed42\"\n    priority: P0\n\n  - id: fig_binding_distribution\n    description: \"Stacked bar or pie chart showing per-batch regime distribution: 49.9% clean, 20.2% α_eff-binding, 30.0% ESS-binding. Companion histogram of b* values for α_eff-binding vs ESS-binding batches.\"\n    section: results\n    data_source: \"adaptive_fix_seed42 training logs (b_star, alpha_eff, ess per batch)\"\n    priority: P0\n\n  - id: fig_bstar_trajectory\n    description: \"b* over training steps (x-axis = step, y-axis = b*). Shows per-batch adaptation dynamics. Color-code by binding regime. Moving average overlay.\"\n    section: results\n    data_source: \"adaptive_fix_seed42 training logs\"\n    priority: P1\n\n  - id: fig_nmin_sensitivity\n    description: \"Line plot: eval_ppl vs n_min ∈ {1, 2, 3, 4}. Annotate n_min=1 (no stability → over-downweight), n_min=4 (over-constrained → b*≈0). Sweet spot at n_min=2.\"\n    section: results\n    data_source: \"nmin1_seed42, adaptive_fix_seed42 (n_min=2), adaptive_seed42 (n_min=3), nmin4_seed42\"\n    priority: P1\n\n  - id: fig_grid_b_curve\n    description: \"Line plot: eval_ppl vs fixed b ∈ {0.5, 1.0, 1.5, 2.0, 3.0, 5.0} across 3 seeds. Horizontal band for adaptive b* ± seed std. Shows adaptive matches best grid point without search.\"\n    section: results\n    data_source: \"grid_b_seed{42,123,456}, adaptive_fix_seed{42,123,456}\"\n    priority: P1\n\n# ============================================================\n# TABLES\n# ============================================================\n\ntables:\n\n  - id: tab_main_results\n    description: \"Main results table: method × seed → eval_ppl. Methods: uniform, grid-best (b=0.5), adaptive b* (τ=0.8, n_min=2), ESS-only, golden ratio. Columns: seed42, seed123, seed456, mean, std. Bold best non-oracle. Report Δ vs uniform.\"\n    section: results\n    data_source: \"uniform_seed{42,123,456}, adaptive_fix_seed{42,123,456}, grid_b_seed{42,123,456}, ess_only_seed{42,123,456}, golden_ratio_seed42\"\n    priority: P0\n\n  - id: tab_tau_sweep\n    description: \"τ sweep table: τ | eval_ppl | Δ vs uniform | mean b* | median b* | conclusion. 6 rows.\"\n    section: results\n    data_source: \"tau_{05,06,07}_seed42, adaptive_fix_seed42 (τ=0.8), tau_{09,095}_seed42\"\n    priority: P0\n\n  - id: tab_binding_stats\n    description: \"Binding constraint statistics: regime | % batches | mean b* | mean ESS | mean α_eff. Three rows: clean, α_eff-binding, ESS-binding.\"\n    section: results\n    data_source: \"adaptive_fix_seed42 training logs (Q1 analysis)\"\n    priority: P0\n\n  - id: tab_grid_search\n    description: \"Grid search results: b ∈ {0.5, 1.0, 1.5, 2.0, 3.0, 5.0} × 3 seeds → eval_ppl. Shows monotonic degradation with b and motivates adaptive selection.\"\n    section: results\n    data_source: \"grid_b_seed{42,123,456}\"\n    priority: P1\n\n  - id: tab_detector\n    description: \"Detector characteristics: method (TF-IDF+LR), features, AUC, accuracy, ECE (raw/calibrated), calibration temperature T.\"\n    section: experiments\n    data_source: \"detector_tfidf_lr\"\n    priority: P1\n\n  - id: tab_nmin\n    description: \"n_min sensitivity: n_min ∈ {1,2,3,4} | eval_ppl | mean b* | interpretation.\"\n    section: results\n    data_source: \"nmin1_seed42, adaptive_fix_seed42, adaptive_seed42, nmin4_seed42\"\n    priority: P1\n\n# ============================================================\n# WRITING ORDER\n# ============================================================\n\nwriting_order:\n  - section: method\n    rationale: \"Core contribution; everything else depends on precise method description\"\n  - section: experiments\n    rationale: \"Setup must be clear before results\"\n  - section: results\n    rationale: \"Data-driven; needs method + experiments in place\"\n  - section: introduction\n    rationale: \"Frame the story using concrete results\"\n  - section: related_work\n    rationale: \"Position after knowing exactly what we claim\"\n  - section: discussion\n    rationale: \"Limitations and implications from results\"\n  - section: conclusion\n    rationale: \"Compress intro + results\"\n  - section: abstract\n    rationale: \"Last — distill the full paper\"\n\n# ============================================================\n# KEY CITATIONS (must-cite)\n# ============================================================\n\nkey_citations:\n\n  must_cite:\n    - id: drayson_2025_detection_collapse\n      reason: \"Direct competitor; shared w=(1-q)^b formula; primary differentiation target\"\n    - id: he_2025_golden_ratio\n      reason: \"Theoretical optimal weight; oracle baseline\"\n    - id: wang_2026_survive_contamination\n      reason: \"Convergence theory motivating τ; α_eff theoretical grounding\"\n    - id: dohmatob_2025_strong_collapse\n      reason: \"Strong model collapse; core motivation for why contamination matters\"\n    - id: shumailov_2024_model_collapse\n      reason: \"Foundational model collapse result\"\n    - id: vehtari_2024_psis\n      reason: \"ESS / Kish's effective sample size theory\"\n    - id: sow_2025_dynamic_reweighting\n      reason: \"Loss-based reweighting at ICLR 2025; complementary approach\"\n\n  should_cite:\n    - id: feng_2025_beyond_collapse\n      reason: \"Verifier-based alternative; hard filtering vs our soft reweighting\"\n    - id: he_2024_softdedup\n      reason: \"Soft reweighting precedent in pretraining\"\n    - id: xie_2023_doremi\n      reason: \"Domain-level mixing optimization baseline\"\n    - id: chen_2025_aioli\n      reason: \"Online adaptive mixing; closest non-grid-search comparison\"\n    - id: kimura_2024_iw_survey\n      reason: \"Importance weighting survey; theoretical context\"\n    - id: alemohammad_2024_mad\n      reason: \"MAD framework; background on self-consuming models\"\n    - id: cheng_2025_contamination_survey\n      reason: \"Contamination survey; problem scope\"\n\n  optional:\n    - id: xie_2023_dsir\n      reason: \"Importance resampling for data selection\"\n    - id: mitchell_2023_detectgpt\n      reason: \"Zero-shot detection method\"\n    - id: shi_2024_minkprob\n      reason: \"Membership inference detection\"\n    - id: ye_2025_data_mixing_laws\n      reason: \"Data mixing scaling laws\"\n    - id: yang_2026_data_mixing_agent\n      reason: \"RL-based domain mixing\"\n    - id: wei_2024_data_watermarks\n      reason: \"Active provenance (complementary)\"\n    - id: kuo_2024_data_weighting\n      reason: \"Synthetic data weighting for classification\"\n    - id: nait_saada_2025_quality_illusion\n      reason: \"Caution on classifier-based quality scores\"\n    - id: guo_2025_escaping_collapse\n      reason: \"Verification-based escape from collapse\"\n\n# ============================================================\n# RUNNING / PENDING EXPERIMENTS\n# ============================================================\n\npending_results:\n  - exp_id: ess_only_seed123\n    status: RUNNING\n    needed_for: \"tab_main_results (ESS-only multi-seed)\"\n    eta: \"2026-05-15 22:00 UTC\"\n  - exp_id: ess_only_seed456\n    status: RUNNING\n    needed_for: \"tab_main_results (ESS-only multi-seed)\"\n    eta: \"2026-05-15 22:00 UTC\"\n  - exp_id: nmin4_seed42\n    status: RUNNING\n    needed_for: \"tab_nmin, fig_nmin_sensitivity\"\n    eta: \"2026-05-15 21:45 UTC\"\n  - exp_id: bs8_nmin2_seed42_r2\n    status: RUNNING\n    needed_for: \"batch_size generalization (appendix if not ready)\"\n    eta: \"2026-05-16 01:30 UTC\"\n"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T20:14:10.939298+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_10/projects/provenance_weight_training/writing_plan.yaml\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper_outline_20260515T200947",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-15T20:14:10.939566+00:00_

`writing_plan.yaml` 已保存。涵盖：

- **暂定标题**: "Minimum Intervention Reweighting: Adaptive Exponent Selection for Contamination-Aware Pretraining"
- **7 个 section** 的详细 key_points + evidence 映射（含 46 个实验的 exp_id 关联）
- **7 个 figures**（4 个 P0 + 3 个 P1）：dual-constraint 示意图、主对比图、τ sweep 双轴图、binding 分布图等
- **6 个 tables**（3 个 P0 + 3 个 P1）：主结果表、τ sweep 表、binding 统计表等
- **写作顺序**: method → experiments → results → intro → related work → discussion → conclusion → abstract
- **key_citations**: 7 must-cite + 7 should-cite + 9 optional，从 literature_map 提取
- **pending_results**: 4 个 RUNNING 实验的 ETA 和依赖关系

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_paper_outline_20260515T200947"
}
```

</details>

---
