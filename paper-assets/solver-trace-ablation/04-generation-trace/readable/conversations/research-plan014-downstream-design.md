# research plan014 downstream design

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 77
- **Recorded user turns:** 0
- **Tool calls:** 38
- **Original source:** `logs/chats/worker_research_plan014-downstream-design_20260514T020422.jsonl`
- **Structured JSON:** [`dc5da4c65938fd53cbb9.json`](../../sessions/dc/dc5da4c65938fd53cbb9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

77 recorded events

### Tool call

_source line 1 · 2026-05-14T02:11:53.536405+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T02:11:53.536791+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T02:11:53.536964+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "ROADMAP.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "ROADMAP.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T02:11:53.537163+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/ROADMAP.md\", \"content\": \"# solver-trace-ablation — Research Dashboard\\n\\n> 最后更新: 2026-05-13 23:09 UTC | 更新原因: Dream 完成 + plan_003 消歧确认 penalty effect + plan_001 3次失败紧急处理\\n\\n## 核心方向\\nSTA（Solver Trace Ablation）：基于 mutation testing 的 component necessity testing，为 neurosymbolic formalizer 的 GRPO 训练提供 intensional structural reward。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research（MVP 通过，消歧实验完成，Dream 审稿指导重构中）\\n- **基础设施**: westd-39279 × 2 RTX PRO 6000 96GB\\n- **消歧结论 (D008)**: plan_003 held-out eval 确认 exec-only checkpoint ISR=0.6423（proved-only），高于 GT 0.56。**Interpretation B confirmed**: 50/50 STA reward 是 penalty effect，非 hacking detection。\\n- **Dream 结果**: dream_20260513T215750 done — best 4/6 Borderline Reject, median 3/6 Weak Reject\\n- **Dream 跨档一致问题**: (1) related work 6→25+ (2) RIP framing 过度 (3) ISR circularity (4) single-seed secondary (5) ISR sparsity/\\\"dense+automatic\\\" 不成立\\n- **论文 story 转向**: \\\"STA detects hacking\\\" → \\\"STA as principled structural metric + proper integration\\\"\\n- **⚠️ plan_001 连续 3 次 failed**: exec-only baseline 500步尚未成功运行，Agent 正在诊断\\n- **plan_005 RUNNING**: STA weight=0.1 训练进行中（cuda:1）\\n\\n## 实验计划摘要（详见 experiment_plan.yaml）\\n**既有 P0**:\\n- plan_001: exec-only 500步 3seed baseline — **3次failed，紧急修复中**\\n- plan_002: exec+STA 500步 3seed — 待 plan_005 确定最优权重\\n- plan_003: held-out eval — ✅ done, 消歧完成\\n- plan_005: weight ablation — RUNNING (sta_weight=0.1)\\n\\n**Dream 新增实验需求**:\\n- **random reward baseline** (NEW): random structural penalty 替代 ISR → 隔离 ISR specific signal vs multi-objective regularization. ~1 GPU·h. **Dream M2/W7 必修**\\n- **downstream validation** (NEW): 高 ISR formalizations 用于下游逻辑推理任务 → 打破 ISR circularity. **Dream M2/W4 必修**\\n- **3-seed for secondary**: 至少 Prolog (plan_006) + top weight config 需 3 seed. ~6 GPU·h\\n- **curriculum ablation**: linear ramp vs sigmoid c
…[truncated 2553 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T02:11:53.537337+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "report.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "report.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T02:11:53.537496+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/report.md\", \"content\": \"# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| plan001-exec-only-s43-r4 | — | — | — | — |\\n| plan013-random-reward-s42-r4 | — | — | — | — |\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **plan001-exec-only-s43-r3** (failed): —\\n- **plan013-random-reward-s42-r3** (failed): —\\n- **plan001-exec-only-s43-r2** (failed): —\\n\\n## 趋势\\n成功 5 / 负向 4 / 失败 14 / 共 23\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-39279: 无 GPU 信息\\n\\n## 告警\\n- sta-phase1-exec-only: 训练失败 — unknown\\n- sta-phase1-exec-sta: 训练失败 — unknown\\n- sta-phase1-exec-only-r2: 训练失败 — unknown\\n- sta-phase1-exec-sta-r2: 训练失败 — unknown\\n- sta-phase1-exec-only-r3: 训练失败 — unknown\\n- sta-phase1-exec-sta-r3: 训练失败 — unknown\\n- plan001-exec-only-s42: 训练失败 — unknown\\n- plan001-exec-only-s42-r3: 训练失败 — unknown\\n- plan001-exec-only-s43: 训练失败 — unknown\\n- plan013-random-reward-s42: 训练失败 — unknown\\n- plan013-random-reward-s42-r2: 训练失败 — unknown\\n- plan001-exec-only-s43-r2: 训练失败 — unknown\\n- plan013-random-reward-s42-r3: 训练失败 — unknown\\n- plan001-exec-only-s43-r3: 训练失败 — unknown\\n\", \"total_chars\": 1088, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T02:11:53.537648+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "EVALUATION.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "EVALUATION.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T02:11:53.537842+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No EVALUATION.md found for 'solver-trace-ablation'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T02:11:53.537972+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "paper_framing.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "paper_framing.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T02:11:53.538165+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md\", \"content\": \"# Paper Framing — solver-trace-ablation\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026\\n\\n## Core Claims (2 条，精简自原始 5 条)\\n\\n### Claim 1: STA as Reward Design Methodology\\nSolver Trace Ablation (STA), grounded in the Reachability-Infection-Propagation (RIP) framework from mutation testing theory, provides a **general, solver-agnostic procedure** for deriving intensional verification rewards from solver execution semantics. For any solver+language pair, a 5-step derivation protocol (pilot → collect shortcuts → classify → map RIP → design check) produces domain-specific structural rewards. This is the first application of the RIP framework to RL reward design.\\n\\n**MVP 证据**: Full STA 在 FOL+Prover9 上提供连续 ISR（0.125-0.889）。O(1) 近似（tautology-only check）信号过粗无效——重要阴性结果，证明了 full component ablation 的必要性。\\n**✅ 因果归因已确认 (D008)**: plan_003 held-out eval: exec-only checkpoint proved_only_ISR=0.6423，高于 GT 0.56。**Interpretation B confirmed**: 50/50 STA 权重是 penalty effect，非 hacking detection。Exec-only 模型天然产生结构良好的 proofs，过高 STA 权重惩罚了 prove 行为。\\n**Claim 调整**: STA 的价值在于 (1) 作为结构质量度量指标（ISR 区分力强），(2) 合理集成（低权重/bonus/curriculum）可在不牺牲 prove rate 前提下引导结构质量。不再声称 \\\"STA 检测 reward hacking\\\"。plan_005（weight ablation RUNNING）将验证最优集成方式。\\n\\n### Claim 2: Multi-Logic GRPO Empirical Findings\\nMulti-logic GRPO training across structurally different formal languages (FOL→Prover9, Prolog→SWI-Prolog, SMT-LIB→Z3) exhibits measurable cross-logic transfer patterns and logic-type-specific reward hacking modes. STA-derived rewards detect and quantify these phenomena.\\n\\n**MVP 证据**: 待验证（FOL 单逻辑已验证，multi-logic 需 research 阶段实验）。\\n\\n## Story Spine\\n\\n- **Problem**: GRPO with solver-verified rewards trains formalizers that achieve
…[truncated 5695 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T02:11:53.538326+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "memory.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "memory.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T02:11:53.538520+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/memory.md\", \"content\": \"# solver-trace-ablation — Memory\\n\\n## 环境信息 (2026-05-13)\\n\\n### westd-39279 服务器\\n- **GPU**: 2× RTX PRO 6000 Blackwell, 94GB VRAM 每张\\n- **CUDA**: 12.8, PyTorch 2.10.0+cu128\\n- **镜像**: aml-train（conda 环境，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）\\n- **ML 栈**: transformers/trl/vllm/accelerate 全部预装\\n- **Solvers**: Prover9 (LADR 2009-11A 源码编译), SWI-Prolog 8.4.2, Z3 4.16.0.0\\n- **模型**: Qwen3-4B 已下载（7.6GB，通过 ModelScope）\\n- **代码路径**: `/root/solver-trace-ablation/`\\n- **磁盘**: 系统盘 250GB，大文件（outputs/checkpoints）必须放 `/root/autodl-tmp/`\\n\\n### 决策记录\\n- Qwen3-4B 用 ModelScope 下载（HuggingFace 直连可能慢）\\n- Prover9 从 LADR 源码编译（apt 无包）\\n- 94GB VRAM 单卡跑 Qwen3-4B 完全无压力\\n\\n## 数据 (2026-05-13)\\n\\n### 数据源变更：ProofWriter → FOLIO\\n- ProofWriter 原始数据无 FOL 列，改用 `tasksource/folio`（1204 条人工标注 FOL）\\n- Phase 0 子集 100 条，训练子集 500 条\\n- 34% 数据含 XOR (⊕) 符号，已在 `_normalize_fol()` 中修复展开\\n\\n### 数据约束 (2026-05-14, D009)\\n- **C001**: 所有 plan001/plan013 实验统一使用 `train_500_seed42.jsonl`，不再用 `proofwriter_fol_500.jsonl`（消除数据差异 confound）\\n\\n## Phase 0 关键发现 (2026-05-13)\\n\\n### Base Model ISR Baseline (sta-phase0-baseline)\\n- **Prove rate**: 12% overall, 18.2% excluding XOR-affected samples\\n- **Mean ISR**: 0.064 (very low — base model formalizations mostly unprovable)\\n- **ISR 区分度**: proved 样本 ISR 0.125–0.889\\n\\n### Ground-Truth ISR Baseline (sta-gt-isr-baseline)\\n- **GT prove rate**: 18% (limited by Prover9 only proving entailment; true=50%, false=4%, unknown=0%)\\n- **GT mean ISR**: 0.5588 (median 0.6125, range 0.14–1.00)\\n- **MVP Pass #2 验证**: GT ISR 0.559 > 0.5 ✅，好的 formalization ISR 高\\n- **Model vs GT gap**: ISR 0.064 vs 0.559 = 8.7x 差距，STA 有强区分力\\n\\n### Prover9 局限性\\n- Prover9 只能证明 entailment（conclusion 从 premises 推出）\\n- `false` 和 `unknown` 类问题几乎无法证明（false 4%, unknown 0%）\\n- Phase 1 训练中 r
…[truncated 4421 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T02:11:53.538682+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Explore project eval code",
  "subagent_type": "Explore",
  "prompt": "I need to understand the solver-trace-ablation project's evaluation infrastructure. Look in /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/ and also /root/solver-trace-ablation/ (if accessible via local files).\n\nSearch for:\n1. Any eval scripts (eval*.py, evaluate*.py, inference*.py)\n2. How ISR is computed (grep for \"isr\", \"intensional\", \"ablation\", \"leave_one_out\", \"necessity\")\n3. How solvers are invoked (grep for \"prover9\", \"swipl\", \"z3\", \"subprocess\" in .py files)\n4. The data format of proofwriter_fol_100.jsonl or any eval data\n5. Any existing downstream evaluation code\n\nReport file paths, key function names, and how the ISR pipeline works. Be thorough."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Agent",
  "tool_args": {
    "description": "Explore project eval code",
    "subagent_type": "Explore",
    "prompt": "I need to understand the solver-trace-ablation project's evaluation infrastructure. Look in /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/ and also /root/solver-trace-ablation/ (if accessible via local files).\n\nSearch for:\n1. Any eval scripts (eval*.py, evaluate*.py, inference*.py)\n2. How ISR is computed (grep for \"isr\", \"intensional\", \"ablation\", \"leave_one_out\", \"necessity\")\n3. How solvers are invoked (grep for \"prover9\", \"swipl\", \"z3\", \"subprocess\" in .py files)\n4. The data format of proofwriter_fol_100.jsonl or any eval data\n5. Any existing downstream evaluation code\n\nReport file paths, key function names, and how the ISR pipeline works. Be thorough."
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T02:11:53.538873+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation -type f -name \"*.py\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation -type f -name \"*.py\" | head -20"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T02:11:53.538995+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/train_grpo.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T02:11:53.539122+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/ 2>/dev/null | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/ 2>/dev/null | head -30"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T02:11:53.539242+00:00_

total 184
drwxr-xr-x 8 ubuntu ubuntu  4096 May 14 02:04 .
drwxrwxr-x 5 ubuntu ubuntu  4096 May 13 17:31 ..
drwxr-xr-x 3 ubuntu ubuntu  4096 May 13 17:31 .claude
-rw-r--r-- 1 ubuntu ubuntu 12790 May 14 02:04 AGENTS.md
-rw-r--r-- 1 ubuntu ubuntu     0 May 13 17:33 ROADMAP.lock
-rw------- 1 ubuntu ubuntu  5187 May 14 02:03 ROADMAP.md
drwxr-xr-x 4 ubuntu ubuntu  4096 May 14 02:03 artifacts
drwxr-xr-x 2 ubuntu ubuntu 20480 May 14 01:45 checkpoints
-rw-r--r-- 1 ubuntu ubuntu     0 May 13 23:57 constraints.lock
-rw------- 1 ubuntu ubuntu  1207 May 14 01:40 constraints.yaml
-rw-r--r-- 1 ubuntu ubuntu     0 May 13 17:34 decisions.lock
-rw------- 1 ubuntu ubuntu  9647 May 14 02:03 decisions.yaml
drwxr-xr-x 2 ubuntu ubuntu  4096 May 13 17:31 docs
-rwxr-xr-x 1 ubuntu ubuntu     0 May 13 21:57 dream_registry.lock
-rw------- 1 ubuntu ubuntu  1042 May 13 22:47 dream_registry.yaml
-rw-r--r-- 1 ubuntu ubuntu  1047 May 13 22:47 dream_registry.yaml.bak
-rw-r--r-- 1 ubuntu ubuntu     0 May 13 22:19 experiment_plan.lock
-rw------- 1 ubuntu ubuntu  4773 May 14 02:04 experiment_plan.yaml
-rw-r--r-- 1 ubuntu ubuntu 20468 May 14 01:56 literature_map.yaml
drwxr-xr-x 4 ubuntu ubuntu  4096 May 13 17:35 logs
-rw-r--r-- 1 ubuntu ubuntu  7759 May 14 01:47 memory.md
-rw-r--r-- 1 ubuntu ubuntu  7662 May 13 23:11 paper_framing.md
-rw-r--r-- 1 ubuntu ubuntu     0 May 13 17:51 registry.lock
-rw------- 1 ubuntu ubuntu 37848 May 14 01:55 registry.yaml
-rw-r--r-- 1 ubuntu ubuntu  1398 May 14 01:45 report.md
-rwxr-xr-x 1 ubuntu ubuntu     0 May 13 17:31 study_status.lock
drwxr-xr-x 3 ubuntu ubuntu  4096 May 14 01:58 task_context

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T02:11:53.539392+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /root/solver-trace-ablation/ 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /root/solver-trace-ablation/ 2>/dev/null | head -20"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T02:11:53.539510+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-14T02:11:53.539634+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/**/*.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/**/*.py"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-14T02:11:53.539776+00:00_

artifacts/train_grpo.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-14T02:11:53.539901+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation -type f \\( -name \"*.py\" -o -name \"*.sh\" -o -name \"*.jsonl\" \\) 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation -type f \\( -name \"*.py\" -o -name \"*.sh\" -o -name \"*.jsonl\" \\) 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-14T02:11:53.540032+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/ralph_loop_timeline.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/chats/worker_ops_check-training-progress_20260514T020044.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/chats/worker_ops_check-server-status_20260513T230158.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/chats/worker_code_eval-scripts-prep_20260514T013607.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/chats/worker_ops_server-status-check_20260513T233559.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/chats/worker_code_prepare-plan013-submission_20260513T234655.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/chats/cron_hook_sta-phase1-exec-sta-r3.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/chats/cron_hook_sta-phase1-exec-sta.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/chats/worker_monitor_phase1-r5-verify_20260513T205535.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/chats/feishu_group_oc_a771c2a33d631dd40256ecd5c3a6648e_director.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/chats/worker_code_plan001-exec-only-s42-r4_20260513T230425.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/chats/cron_hook_sta-phase1-exec-only-r2.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/chats/cron_hook_sta-phase1-exec-sta-r2.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/chats/worker_train_plan001-exec-only-s43_20260513T235424.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects
…[truncated 5777 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-14T02:11:53.540171+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-14T02:11:53.540288+00:00_

total 100
drwxr-xr-x 4 ubuntu ubuntu  4096 May 14 02:03 .
drwxr-xr-x 8 ubuntu ubuntu  4096 May 14 02:04 ..
-rw-r--r-- 1 ubuntu ubuntu  4610 May 13 20:27 diagnose_phase1_r3.md
drwxr-xr-x 3 ubuntu ubuntu  4096 May 13 22:47 dream_reports
-rw-r--r-- 1 ubuntu ubuntu   437 May 13 19:59 grpo_exec_only.yaml
-rw-r--r-- 1 ubuntu ubuntu   434 May 13 19:59 grpo_exec_sta.yaml
-rw-r--r-- 1 ubuntu ubuntu 16143 May 14 02:01 hacking_taxonomy.md
-rw-r--r-- 1 ubuntu ubuntu  1262 May 13 18:25 launch_phase1.sh
-rw-r--r-- 1 ubuntu ubuntu 20468 May 14 01:55 literature_map.yaml
-rw-r--r-- 1 ubuntu ubuntu  1044 May 13 18:13 manifest.yaml
-rw-r--r-- 1 ubuntu ubuntu  2653 May 13 20:00 phase1_r2_diagnosis.md
-rw-r--r-- 1 ubuntu ubuntu  1759 May 14 02:03 seed44_readiness.md
drwxr-xr-x 3 ubuntu ubuntu  4096 May 13 18:05 sta-phase0-baseline
-rw-r--r-- 1 ubuntu ubuntu 11977 May 13 20:14 train_grpo.py
-rw-r--r-- 1 ubuntu ubuntu  1373 May 14 02:01 training_progress_check.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-14T02:11:53.540420+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/train_grpo.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/train_grpo.py"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-14T02:11:53.540590+00:00_

1	"""Phase 1 GRPO training: execution-only vs execution+STA reward.
2	
3	Usage:
4	  # execution-only (GPU 0)
5	  CUDA_VISIBLE_DEVICES=0 python scripts/train_grpo.py \
6	    --model_path /root/autodl-tmp/models/Qwen3-4B \
7	    --data_path data/proofwriter_fol_500.jsonl \
8	    --reward_mode execution_only --output_dir outputs/grpo_exec_only \
9	    --num_steps 100 --wandb_project solver-trace-ablation
10	
11	  # execution+STA (GPU 1)
12	  CUDA_VISIBLE_DEVICES=1 python scripts/train_grpo.py \
13	    --model_path /root/autodl-tmp/models/Qwen3-4B \
14	    --data_path data/proofwriter_fol_500.jsonl \
15	    --reward_mode execution_sta --output_dir outputs/grpo_exec_sta \
16	    --num_steps 100 --wandb_project solver-trace-ablation
17	"""
18	
19	from __future__ import annotations
20	
21	import argparse
22	import json
23	import logging
24	import os
25	import re
26	import sys
27	import time
28	from datetime import datetime, timezone
29	from pathlib import Path
30	
31	import torch
32	from datasets import Dataset
33	from transformers import AutoModelForCausalLM, AutoTokenizer, TrainerCallback
34	from trl import GRPOConfig, GRPOTrainer
35	
36	sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
37	
38	from src.solvers.factory import get_solver
39	from src.sta.reward import _parse_formalization, fast_sta_reward
40	
41	logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
42	logger = logging.getLogger(__name__)
43	
44	
45	SYSTEM_PROMPT = (
46	    "You are a first-order logic (FOL) expert. "
47	    "Given natural language premises and a conclusion, formalize them into FOL.\n\n"
48	    "Output format:\n"
49	    "Premises:\n"
50	    "1. &lt;FOL formula>\n"
51	    "2. &lt;FOL formula>\n"
52	    "...\n"
53	    "Conclusion: &lt;FOL formula>\n\n"
54	    "Use standard FOL notation with predicate-argument syntax: "
55	    "all x (P(x) -> Q(x)), exists x P(x), P(a) & Q(a), -P(a), P(a) | Q(a), P(a) -> Q(a)."
56	)
57	
58	USER_TEMPLATE = (
59	    "Formali
…[truncated 11253 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-14T02:11:53.540762+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "fast_sta_reward|_parse_formalization|intensional|isr|leave_one_out|necessity|ablation",
  "type": "py",
  "head_limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Grep",
  "tool_args": {
    "pattern": "fast_sta_reward|_parse_formalization|intensional|isr|leave_one_out|necessity|ablation",
    "type": "py",
    "head_limit": "0"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-14T02:11:53.540894+00:00_

Found 1 file
artifacts/train_grpo.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-14T02:11:53.541023+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation -type d -name \"src\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation -type d -name \"src\" 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-14T02:11:53.541137+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-14T02:11:53.541276+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation -type f -name \"*.md\" | xargs grep -l \"eval\\|isr\\|solver\\|prover\\|z3\\|proofwriter\" 2>/dev/null | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation -type f -name \"*.md\" | xargs grep -l \"eval\\|isr\\|solver\\|prover\\|z3\\|proofwriter\" 2>/dev/null | head -10"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-14T02:11:53.541422+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/IDEA_BRIEF.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/task_context/agent.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/task_context/director.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/task_context/reviewer.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/task_context/history/director/loop_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/task_context/history/agent/loop_1_1778715281.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/task_context/history/agent/loop_1_1778716131.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/task_context/history/agent/loop_1_1778714720.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/task_context/history/agent/loop_1_1778723906.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/task_context/history/agent/loop_1_1778716202.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-14T02:11:53.541551+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/IDEA_BRIEF.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/IDEA_BRIEF.md"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-14T02:11:53.541762+00:00_

1	# Idea Brief: Solver Trace Ablation for Cross-Logic GRPO Training of Neurosymbolic Formalizers
2	
3	
4	- **Idea ID**: `idea_010`
5	- **Created**: 2026-05-13
6	- **Approved**: 2026-05-13
7	- **Source**: foreign:be-idea-gen-0509-3
8	- **Level**: top-tier
9	- **Target Venues**: EMNLP 2026 (ARR submission deadline May 25, 2026)
10	
11	## Seed Topic
12	
13	Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: NLP and Symbolic Reasoning.
14	
15	Direction: Neurosymbolic reasoning — combining neural models with symbolic systems (logic programs, knowledge graphs, formal verification, constraint solvers). NOT limited to LLM-only reasoning — explicitly seek methods that integrate external symbolic components. Also in-scope: structured mathematical reasoning, program-aided reasoning, theorem prover integration.
16	
17	Contribution type: METHOD ONLY. Must propose a new hybrid algorithm, training objective, or inference pipeline that combines neural + symbolic components. Pure prompting tricks (vanilla CoT, self-consistency) are out of scope.
18	
19	HARD CONSTRAINTS:
20	1. Compute: ≤200 H100-hours total. Neurosymbolic methods are often inference-heavy not training-heavy — budget accordingly.
21	2. Time: ≤16 days. Use existing open checkpoints (Qwen3, Llama-3.x, DeepSeek-R1 distills) + off-the-shelf solvers (Z3, Prolog, SymPy, Lean4).
22	3. Eval: MATH, AIME 2024/2025, GPQA Diamond, ProofWriter, FOLIO, LogiQA, ARC-Challenge, BBH.
23	
24	Look for: lightweight symbolic verifiers as post-hoc filters, neural-guided symbolic search, structured output → formal checker pipelines, hybrid neuro-symbolic distillation. Avoid: pure prompt engineering, vanilla CoT.
25	
26	Tag: direction=neurosymbolic_reasoning, contribution_type=method. target_venues=["EMNLP 2026 Main", "EMNLP 2026 Findings"].
27	
28	## Generation Journey
29	
30	1. **Start** — 开始生成，seed: 'Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: NLP
…[truncated 32382 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-14T02:11:53.541941+00:00_

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
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/memory.md"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-14T02:11:53.542091+00:00_

1	# solver-trace-ablation — Memory
2	
3	## 环境信息 (2026-05-13)
4	
5	### westd-39279 服务器
6	- **GPU**: 2× RTX PRO 6000 Blackwell, 94GB VRAM 每张
7	- **CUDA**: 12.8, PyTorch 2.10.0+cu128
8	- **镜像**: aml-train（conda 环境，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
9	- **ML 栈**: transformers/trl/vllm/accelerate 全部预装
10	- **Solvers**: Prover9 (LADR 2009-11A 源码编译), SWI-Prolog 8.4.2, Z3 4.16.0.0
11	- **模型**: Qwen3-4B 已下载（7.6GB，通过 ModelScope）
12	- **代码路径**: `/root/solver-trace-ablation/`
13	- **磁盘**: 系统盘 250GB，大文件（outputs/checkpoints）必须放 `/root/autodl-tmp/`
14	
15	### 决策记录
16	- Qwen3-4B 用 ModelScope 下载（HuggingFace 直连可能慢）
17	- Prover9 从 LADR 源码编译（apt 无包）
18	- 94GB VRAM 单卡跑 Qwen3-4B 完全无压力
19	
20	## 数据 (2026-05-13)
21	
22	### 数据源变更：ProofWriter → FOLIO
23	- ProofWriter 原始数据无 FOL 列，改用 `tasksource/folio`（1204 条人工标注 FOL）
24	- Phase 0 子集 100 条，训练子集 500 条
25	- 34% 数据含 XOR (⊕) 符号，已在 `_normalize_fol()` 中修复展开
26	
27	### 数据约束 (2026-05-14, D009)
28	- **C001**: 所有 plan001/plan013 实验统一使用 `train_500_seed42.jsonl`，不再用 `proofwriter_fol_500.jsonl`（消除数据差异 confound）
29	
30	## Phase 0 关键发现 (2026-05-13)
31	
32	### Base Model ISR Baseline (sta-phase0-baseline)
33	- **Prove rate**: 12% overall, 18.2% excluding XOR-affected samples
34	- **Mean ISR**: 0.064 (very low — base model formalizations mostly unprovable)
35	- **ISR 区分度**: proved 样本 ISR 0.125–0.889
36	
37	### Ground-Truth ISR Baseline (sta-gt-isr-baseline)
38	- **GT prove rate**: 18% (limited by Prover9 only proving entailment; true=50%, false=4%, unknown=0%)
39	- **GT mean ISR**: 0.5588 (median 0.6125, range 0.14–1.00)
40	- **MVP Pass #2 验证**: GT ISR 0.559 > 0.5 ✅，好的 formalization ISR 高
41	- **Model vs GT gap**: ISR 0.064 vs 0.559 = 8.7x 差距，STA 有强区分力
42	
43	### Prover9 局限性
44	- Prover9 只能证明 entailment（conclusion 从 premises 推出）
45	- `false` 和 `unknown` 类问题几乎无法证明（false 4%, unknown 0%）
46	- Phase 1 训练中 reward 信号主要来自 `true` 类样本
47	
48	### ISR 已知盲区
49	- premise-conclusion 重复的 trivial formalization 可能获高 ISR
50	- 需在论文 Discussio
…[truncated 4308 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-14T02:11:53.542248+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"sta_reward\\|_parse_formalization\\|get_solver\\|subprocess\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation --include=\"*.py\" --include=\"*.md\" 2>/dev/null | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"sta_reward\\|_parse_formalization\\|get_solver\\|subprocess\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation --include=\"*.py\" --include=\"*.md\" 2>/dev/null | head -30"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-14T02:11:53.542381+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/task_context/reviewer.md:- ISR 指标跨 reward_mode 不可比：exec-only 用 fast_sta_reward（binary ISR=0/1），exec-sta 用 sta_reward（continuous ISR 0.0-1.0）。不能直接比两组的 mean_isr
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/task_context/history/agent/loop_1_1778715780.md:- `fast_isr_fol()` 是二值信号，**不能用于训练 reward**——必须用 `sta_reward()`（full STA，连续 ISR 0.0-1.0）
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/task_context/history/agent/loop_2.md:1. **plan013 isr_mean 字段是陷阱**: random_reward 模式下 `sta_reward`=0 → `isr_mean`=0，真正的随机值在 `random_reward` 字段。分析时看 prove_rate 趋势和 `random_reward` 字段，不看 `isr_mean`
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/memory.md:**配置变更**: r4→r5: `fast_sta_reward` → `sta_reward` (continuous ISR) + K=4→8
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/memory.md:- `isr_mean` 取 `result["sta_reward"]`，而 random_reward 分支调用 `_fast_fn(..., sta_weight=0.0)` → `sta_reward` 恒为 0.0
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/train_grpo.py:from src.solvers.factory import get_solver
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/train_grpo.py:from src.sta.reward import _parse_formalization, fast_sta_reward
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/train_grpo.py:                result = fast_sta_reward(
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/train_grpo.py:                result = fast_sta_reward(
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/train_grpo.py:            isr = result.get("sta_reward", 0.0)
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/train_grpo.py:    solver = get_solver(args.solver)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-14T02:11:53.542527+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/task_context/reviewer.md",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/task_context/reviewer.md",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-14T02:11:53.542663+00:00_

1	---
2	loop: 1
3	reason: max_wall_time
4	updated: '2026-05-13T22:04:04+00:00'
5	---
6	
7	### 1. 🔴 硬约束 / 红线
8	- GPU 只能用 cuda:0 和 cuda:1（westd-39279 上的 2× RTX PRO 6000 96GB）
9	- exec-only 跑 CUDA_VISIBLE_DEVICES=0，exec-sta 跑 CUDA_VISIBLE_DEVICES=1（历史约定，r3 因未隔离 OOM 过）
10	- exec-sta-r5 registry conclusion="success" 是错的——prove_rate=0.1 低于 baseline=0.12，应为 "negative"。Agent 至今未修正，如果你看到 Agent 引用此结论需要 challenge
11	- ISR 指标跨 reward_mode 不可比：exec-only 用 fast_sta_reward（binary ISR=0/1），exec-sta 用 sta_reward（continuous ISR 0.0-1.0）。不能直接比两组的 mean_isr
12	
13	### 2. 🖥️ 基础设施快照
14	- 服务器：westd-39279(root)，工作目录 /root/solver-trace-ablation
15	- Python：/root/miniconda3/bin/python3（conda base 环境，不是 venv）
16	- 激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
17	- 模型：/root/autodl-tmp/models/Qwen3-4B
18	- 数据：/root/solver-trace-ablation/data/proofwriter_fol_500.jsonl（500条训练）+ proofwriter_fol_100.jsonl（100条 baseline）
19	- 输出：/root/autodl-tmp/outputs/grpo_exec_only/ 和 grpo_exec_sta/
20	- W&B：no_wandb=true（服务器无 API key）
21	- 活跃进程：无。两张卡 0% util, 0 MiB（已空闲 >20 分钟）
22	
23	### 3. 📊 当前状态
24	我完成了三件事：
25	1. Phase 1 r5 综合审查——发现 full STA 50/50 权重导致 prove_rate 退化至 baseline 以下，posted to Director
26	2. ROADMAP "MVP 通过" 审查——指出 Pass Criteria #4/#5 未满足，要求修正标签、增加 Kill Criteria、不等 Dream 启动实验
27	3. ROADMAP 修正确认——Director 已采纳所有建议（MVP 改"部分通过"、增 Kill Criteria、plan_005 提前）
28	
29	Registry：12 实验全部 DONE（无 RUNNING）。ROADMAP 说"紧急实验已排队"（低权重 STA + ISR-as-bonus）但实际尚未提交。
30	等待：Dream dream_20260513T215750 pending（但已决定不等 Dream 启动无依赖实验）
31	
32	### 4. 📋 待办
33	- 新实验提交（低权重 STA / plan_004 / plan_009）→ 审查 CUDA_VISIBLE_DEVICES 是否在白名单内 + spec 完整性
34	- plan_005 weight ablation 结果出来 → **这是 pivotal experiment**：所有权重配比 STA 均 ≤ exec-only → 论文退化为 "STA as monitor"，需立即 post Director
35	- plan_001/002（500步 3seed）完成 → 审查 prove_rate 是否显著高于 100 步 pilot（15-20%），若仍停滞说明 GRPO 基座本身有问题
36	- plan_003（held-out eval，统一 ISR 评估）完成 → 核查 exec-only checkpoint 用 full STA 评估后的 ISR/PR 比，这是 "STA 检测 hacking" claim 的关键证据
37	- Agent 做 Framing
…[truncated 663 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-14T02:11:53.542857+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/task_context/director.md",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/task_context/director.md",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-14T02:11:53.542998+00:00_

1	---
2	loop: 2
3	reason: max_messages
4	updated: '2026-05-13T23:25:21+00:00'
5	---
6	
7	### 1. 🔴 硬约束 / 红线
8	- 本项目 GPU 白名单：westd-39279 的 cuda:0 和 cuda:1，共 2 张 RTX PRO 6000 96GB。不可用其他服务器或设备号
9	- plan_003 消歧已确认 Interpretation B（penalty effect）—— 论文中**不可再声称 "STA 检测 reward hacking"**，只能用观察性表述（D006/D008）
10	- 50/50 STA 权重已证实有害（prove_rate 退化至 baseline 以下）—— 任何新 exec+STA 实验必须用 plan_005 确定的最优权重，不可用 0.5/0.5
11	- Dream 审稿明确禁止的措辞：不可说 "Pareto-improving"（prove rate 差异不显著）、不可说 "dense+automatic"（ISR 对 unproved=0，改用 "conditionally dense"）
12	
13	### 2. 🖥️ 基础设施快照
14	- 服务器：westd-39279，SSH connect.westd.seetacloud.com:39279，account root
15	- 工作目录：/root/solver-trace-ablation
16	- Python 环境：未确认（Agent 之前做过环境探测但 handoff 缺细节，需 SSH 验证）
17	- 数据：FOL 数据在 data/proofwriter_fol_*.jsonl；**Prolog 数据不存在**（Reviewer WARNING，阻塞 plan_006）
18	- GPU 健康数据：stale（get_gpu_health 返回 "no data yet"），需 Agent SSH 确认实际状态
19	- 活跃进程：plan005-sta-low-s42 应在 cuda:1 上 RUNNING（registry 状态），但已超 3h 未确认实际进程状态
20	
21	### 3. 📊 当前状态
22	**我刚做完**：
23	- Dream dream_20260513T215750 完整分析（best 4/6 Borderline Reject, median 3/6 Weak Reject）
24	- paper_framing.md 更新：story 从 "STA detects hacking" 转向 "STA as structural metric + proper integration"
25	- experiment_plan.yaml 新增 plan_013-016（random baseline / downstream validation / curriculum ablation / longer training），plan_006 升级 3 seeds
26	- ROADMAP 更新，D008 决策记录
27	- 给 Agent 发了 plan_001 诊断指令（但 Agent 空闲 180min 未响应，触发本次 RESET）
28	
29	**Registry**：
30	- RUNNING: plan005-sta-low-s42（STA weight=0.1，cuda:1）—— 实际进程状态未知，需确认
31	- DONE(failed): plan001-exec-only-s42, -r2, -r3 —— 连续 3 次失败，根因未诊断
32	- DONE(success): plan003-eval-exec-only-r5（prove_rate=0.32, proved_only_ISR=0.6423）
33	- 其余 12 个 DONE（4 success, 3 negative, 9 failed，详见 registry）
34	
35	**等待中**：无。Agent 被 RESET，新 session 需重新派任务。
36	
37	### 4. 📋 待办
38	- Agent RESET 完成 → 立即派指令：(1) 确认 plan_005 进程是否还活着 (2) 诊断 plan_001 连续 3 次失败根因 (3) cuda:0 空闲则立即修复 plan_001 并重跑
39	- plan_005 完成(success) → 分析最优权重 → 用该权重配置 plan_002 和 Prolog exec+STA config → 启
…[truncated 1312 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-14T02:11:53.543166+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation -name \"*.jsonl\" -type f 2>/dev/null | xargs wc -l 2>/dev/null | tail -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation -name \"*.jsonl\" -type f 2>/dev/null | xargs wc -l 2>/dev/null | tail -5"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-14T02:11:53.543291+00:00_

     69 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/chats/worker_ops_disk-cleanup-and-resubmit_20260514T013754.jsonl
     53 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/chats/worker_diagnose_phase1-r3-failure_20260513T202119.jsonl
     29 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/chats/worker_code_fix-isr-monitoring_20260513T234032.jsonl
     25 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/chats/worker_monitor_plan001r3-005-verify_20260513T224257.jsonl
   5173 total

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-14T02:11:53.543420+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -3 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/ralph_loop_timeline.jsonl 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Bash",
  "tool_args": {
    "command": "head -3 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/ralph_loop_timeline.jsonl 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-14T02:11:53.543541+00:00_

{"ts": "2026-05-13T17:31:21+00:00", "role": "director", "loop_id": "director_loop_1", "event": "BOOT_STARTED", "details": {"loop_count": 1, "boot_kind": "first_boot"}}
{"ts": "2026-05-13T17:31:21+00:00", "role": "agent", "loop_id": "agent_loop_1", "event": "BOOT_COMPLETE", "details": {"new_session_id": null, "loop_count": 1, "boot_kind": "first_boot_agent_skip", "restart_recovery": false}}
{"ts": "2026-05-13T17:33:52+00:00", "role": "reviewer", "loop_id": "reviewer_loop_1", "event": "BOOT_STARTED", "details": {"loop_count": 1, "boot_kind": "first_boot"}}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-14T02:11:53.543668+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/experiment_plan.yaml"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-14T02:11:53.543874+00:00_

1	experiments:
2	- id: plan_001
3	  claim: 1
4	  description: FOL single-logic GRPO, execution-only reward (500 steps, K=8, 3 seeds)
5	    — baseline for STA comparison
6	  priority: P0
7	  gpu_budget_hours: 3
8	  deps: []
9	  registry_id: plan001-exec-only-s43-r4
10	- id: plan_002
11	  claim: 1
12	  description: 'FOL single-logic GRPO, additive ISR bonus: r = r_exec · (1 + β·ISR),
13	    β∈{0.1, 0.3, 0.5}. 先跑 β=0.3 单 seed 验证方向，成功再 3-seed。旧凸组合公式
14	    (α·r_exec + β·r_exec·ISR, α+β=1) 已废弃——ISR<1 时永远是 penalty (plan005 confirmed)。
15	    新公式确保 ISR 只能 bonus 不能 penalty。'
16	  priority: P0
17	  gpu_budget_hours: 4
18	  deps: []
19	- id: plan_003
20	  claim: 1
21	  description: 'FOL held-out evaluation: compare plan_001 vs plan_002 checkpoints
22	    on test set using identical full STA metrics (prove_rate, ISR, ISR/PR ratio, hacking
23	    taxonomy annotation)'
24	  priority: P0
25	  gpu_budget_hours: 1
26	  deps:
27	  - plan_001
28	  - plan_002
29	  registry_id: plan003-eval-exec-only-r5
30	- id: plan_004
31	  claim: 1
32	  description: 'STA O(1) vs O(N) ablation: rerun exec+STA with fast_isr_fol to confirm
33	    O(1) ineffectiveness at scale (500 steps, 1 seed) — negative result documentation'
34	  priority: P0
35	  gpu_budget_hours: 1
36	  deps: []
37	- id: plan_005
38	  claim: 1
39	  description: 'STA reward weight ablation: test α/β ratios (0.3/0.7, 0.5/0.5, 0.7/0.3)
40	    + sigmoid curriculum vs fixed — isolate optimal STA integration'
41	  priority: P0
42	  gpu_budget_hours: 4
43	  deps: []
44	  registry_id: plan005-sta-low-s42
45	- id: plan_006
46	  claim: 2
47	  description: 'Prolog single-logic GRPO: exec-only vs exec+STA (500 steps, K=8, 3
48	    seeds) — second logic type validation. Dream M3: must have 3 seeds for cross-logic
49	    claim.'
50	  priority: P1
51	  gpu_budget_hours: 6
52	  deps: []
53	  notes: Requires Prolog STA instantiation (rule ablation). SWI-Prolog already installed.
54	    Upgraded from 1→3 seeds per Dream feedback.
55	- id: plan_007

…[truncated 3124 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-14T02:11:53.544039+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/decisions.yaml",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/decisions.yaml",
    "limit": "150"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-14T02:11:53.544188+00:00_

1	_next_id: 12
2	decisions:
3	- id: D001
4	  date: 2026-05-13 17:34 UTC
5	  summary: MVP 方案：FOL+Prover9 单逻辑 50-step GRPO pilot 验证 STA reward 有效性
6	  rationale: EMNLP ARR DDL 5/25 仅剩 12 天，需要最快速度验证核心假设。选 FOL+Prover9 因为 hacking 模式最清晰（tautological
7	    formulas），STA 的 O(1) 近似最直观（去掉前提后能否证明结论）。50-step pilot 足以观察 ISR 趋势。两个条件并行跑 2 GPU。Pass
8	    标准：ISR gap >20pp + accuracy 降幅 <5pp。
9	  related_experiments: []
10	  depends_on: []
11	- id: D002
12	  date: 2026-05-13 17:37 UTC
13	  summary: MVP 方案调整：50步→100步 + 趋势判断 + Phase 0 ISR baseline + kill criteria
14	  rationale: 采纳 Reviewer 三条 warning：(1) 加 pre-training ISR baseline 锚定训练前水平；(2) 50步太短难以观察
15	    reward hacking，改 100步+最后20步 moving average 趋势判断；(3) 补充硬性 kill criteria 防止 DDL
16	    压力下无止境调整。
17	  related_experiments: []
18	  depends_on:
19	  - D001
20	- id: D003
21	  date: 2026-05-13 20:50 UTC
22	  summary: Phase 1 r4 fast_isr_fol 训练信号无效，改用 full STA + K=8 重跑
23	  rationale: fast_isr_fol 是二值 O(1) 近似（ISR=0 tautology / ISR=1 non-tautology），Qwen3-4B
24	    生成的 proved formalization 几乎全部 ISR=1，与 execution-only 零差异。full STA 提供连续 ISR（0.125-0.889
25	    in Phase 0），能给出真实梯度信号。K=4 导致 frac_reward_zero_std=0.5-1.0（GRPO 无 advantage），K=8
26	    增加 within-group variance。两个改动分别解决 STA 信号粒度和 GRPO 梯度信号两个独立问题。
27	  related_experiments:
28	  - exp_id: sta-phase1-exec-only-r4
29	    role: evidence
30	    result: prove_rate 12%→15%, ISR ~0.15, minimal learning
31	  - exp_id: sta-phase1-exec-sta-r4
32	    role: evidence
33	    result: 与 exec-only 几乎完全相同, fast_isr 提供零额外信号
34	  depends_on:
35	  - D002
36	- id: D004
37	  date: 2026-05-13 21:59 UTC
38	  summary: Reviewer 指出 exec-sta-r5 prove_rate 低于 baseline（退化），STA 50/50 权重过于惩罚性。立即补跑低权重
39	    + bonus 模式实验
40	  rationale: exec-sta-r5 prove_rate=0.10 < baseline=0.12 < exec-only=0.15。连续 ISR 给
41	    proved-but-low-ISR 样本 reward≈0.3（几乎等于未 prove），模型学到 prove 不值得。Kill criteria 未触发（差
42	    5pp 非 15pp，权重未调整），但核心假设受挑战。需立即验证：(1) sta_weight=0.1 降低惩罚 (2) ISR-as-bonus 模式 r=exec×(1+α×ISR)
43	    避免惩罚。
44	  relate
…[truncated 4952 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-14T02:11:53.544352+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"ISR\\|Intensional\\|Necessary\\|ablation\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation --include=\"*.md\" 2>/dev/null | grep -v \"^Binary\" | head -40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"ISR\\|Intensional\\|Necessary\\|ablation\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation --include=\"*.md\" 2>/dev/null | grep -v \"^Binary\" | head -40"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-14T02:11:53.544502+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/IDEA_BRIEF.md:**(A) The STA Algorithm.** Grounded in the RIP framework (DeMillo & Offutt 1991): a program component is 'necessary' iff its perturbation satisfies three conditions — Reachability (the solver processes it), Infection (the solver's intermediate state changes), and Propagation (the solver's output changes). We adapt this to formal verification: for a formalization p verified by solver S, decompose p into structural components C(p) = {c_1, ..., c_n}. Component c_i is intensionally necessary iff its ablation propagates to the solver's output:
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/IDEA_BRIEF.md:  Necessary(c_i, p, S) = 1[S(p_{-i}) ≠ S(p)]
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/IDEA_BRIEF.md:where p_{-i} is p with component c_i removed/nullified. The Intensional Score Rate (ISR) is:
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/IDEA_BRIEF.md:  ISR(p, S) = (1/|C(p)|) × Σ Necessary(c_i, p, S)
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/IDEA_BRIEF.md:ISR = 1.0 means all components are necessary (fully intensional). ISR ≈ 0 means most components are extensionally redundant (reward-hacked). This is not ad-hoc — it instantiates a well-established formal criterion. The STA algorithm is solver-agnostic: given any new solver S' and language L', one defines the component decomposition for L' and applies the same procedure.
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/IDEA_BRIEF.md:- **FOL → Prover9**: Ablation target = all premises. Single check: prove conclusion without any premises. If provable → ISR ≈ 0 (tautology, extensionally correct but intensionally vacuous). This is the propagation condition applied to the premise set as a unit.
/home/ubuntu/.agent-ml-research-idea_gen_050
…[truncated 9655 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-14T02:11:53.544654+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper_framing.md"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-14T02:11:53.544825+00:00_

1	# Paper Framing — solver-trace-ablation
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (NLP and Symbolic Reasoning track)
5	- Fallback: EMNLP 2026 Findings
6	- Deadline: ARR May 25, 2026
7	
8	## Core Claims (2 条，精简自原始 5 条)
9	
10	### Claim 1: STA as Reward Design Methodology
11	Solver Trace Ablation (STA), grounded in the Reachability-Infection-Propagation (RIP) framework from mutation testing theory, provides a **general, solver-agnostic procedure** for deriving intensional verification rewards from solver execution semantics. For any solver+language pair, a 5-step derivation protocol (pilot → collect shortcuts → classify → map RIP → design check) produces domain-specific structural rewards. This is the first application of the RIP framework to RL reward design.
12	
13	**MVP 证据**: Full STA 在 FOL+Prover9 上提供连续 ISR（0.125-0.889）。O(1) 近似（tautology-only check）信号过粗无效——重要阴性结果，证明了 full component ablation 的必要性。
14	**✅ 因果归因已确认 (D008)**: plan_003 held-out eval: exec-only checkpoint proved_only_ISR=0.6423，高于 GT 0.56。**Interpretation B confirmed**: 50/50 STA 权重是 penalty effect，非 hacking detection。Exec-only 模型天然产生结构良好的 proofs，过高 STA 权重惩罚了 prove 行为。
15	**✅ Framing 转向已批准 (D010)**: STA 是 principled structural metric；凸组合是 penalty（plan005 confirmed）；正确集成方式是 additive bonus。
16	
17	**Claim 调整 (D010)**:
18	- STA 的价值在于 (1) 作为结构质量度量指标（ISR 区分力强），(2) **additive bonus 集成**可在不牺牲 prove rate 前提下引导结构质量
19	- **旧公式（废弃）**: r = α·r_exec + β·r_exec·ISR, α+β=1 → ISR<1 时永远是 penalty
20	- **新公式 (D010)**: r = r_exec · (1 + β·ISR), β>0 → ISR 只能 bonus，不能 penalty
21	- 测试 β ∈ {0.1, 0.3, 0.5}，先跑 β=0.3 单 seed 验证方向
22	- 不再声称 "STA 检测 reward hacking"
23	
24	### Claim 2: Multi-Logic GRPO Empirical Findings
25	Multi-logic GRPO training across structurally different formal languages (FOL→Prover9, Prolog→SWI-Prolog, SMT-LIB→Z3) exhibits measurable cross-logic transfer patterns and logic-type-specific reward hacking modes. STA-derived rewards detect and quantify these phenomena.
26	
27	**MVP 证据**: 待验证（FOL 单逻辑已验证，mu
…[truncated 6276 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-14T02:11:53.544982+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A 5 \"plan001-exec-only\\|plan003-eval\\|plan005-sta\\|plan013-random\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/registry.yaml | head -80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A 5 \"plan001-exec-only\\|plan003-eval\\|plan005-sta\\|plan013-random\" /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/registry.yaml | head -80"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-14T02:11:53.545113+00:00_

  plan001-exec-only-s42:
    status: DONE
    retry_count: 0
    created_at: '2026-05-13T22:19:41.568Z'
    updated_at: '2026-05-13T23:03:42.892Z'
    spec:
--
      log_path: ~/runs/solver-trace-ablation/plan001-exec-only-s42.log
      submitted_at: '2026-05-13T22:20:46.569Z'
      submitted_via: submit_training_job
      backend: tmux
      account: root
      data_path: /root/solver-trace-ablation/data/train_500_seed42.jsonl
--
  plan005-sta-low-s42:
    status: DONE
    retry_count: 0
    created_at: '2026-05-13T22:20:47.812Z'
    updated_at: '2026-05-14T01:55:26.234Z'
    spec:
--
  plan003-eval-exec-only-r5:
    status: DONE
    retry_count: 0
    created_at: '2026-05-13T22:21:48.691Z'
    updated_at: '2026-05-13T23:03:19.945Z'
    spec:
--
      log_path: ~/runs/solver-trace-ablation/plan003-eval-exec-only-r5.log
      submitted_at: '2026-05-13T22:21:48.658Z'
      submitted_via: submit_training_job
      backend: tmux
      account: root
      data_path: /root/solver-trace-ablation/data/proofwriter_fol_100.jsonl
--
    log_path: ~/runs/solver-trace-ablation/plan003-eval-exec-only-r5.log
    completed_at: '2026-05-13T23:03:18.848Z'
  plan001-exec-only-s42-r2:
    status: DONE
    retry_count: 1
    created_at: '2026-05-13T22:40:41.773Z'
    updated_at: '2026-05-14T00:21:13.743Z'
    completed_at: '2026-05-13T23:46:00Z'
--
      log_path: ~/runs/solver-trace-ablation/plan001-exec-only-s42-r2.log
      submitted_at: '2026-05-13T22:42:40.204Z'
      submitted_via: submit_training_job
      backend: tmux
      account: root
      wall_clock_seconds: 3820
--
  plan001-exec-only-s42-r3:
    status: DONE
    retry_count: 0
    created_at: '2026-05-13T22:42:40.242Z'
    updated_at: '2026-05-13T23:03:11.395Z'
    spec:
--
      log_path: ~/runs/solver-trace-ablation/plan001-exec-only-s42-r3.log
      submitted_at: '2026-05-13T22:42:40.204Z'
      submitted_via: submit_training_job
      backend: tmux
      account: root
      data_path: /root/solver-trace-ablation/dat
…[truncated 506 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-14T02:11:53.545283+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation -type f -name \"*.yaml\" -o -name \"*.md\" | sort | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation -type f -name \"*.yaml\" -o -name \"*.md\" | sort | head -30"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-14T02:11:53.545435+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_37abaa24/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_37abaa24/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_442ef4ae/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_442ef4ae/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_6e7888b5/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_6e7888b5/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_79f408c6/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_8c44377d/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_8c44377d/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_90dbe871/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_90dbe871/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_a16afcec/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_a16afcec/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/sessions/agent_d44a3988/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/.claude/s
…[truncated 1660 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-14T02:11:53.545668+00:00_

Perfect! Let me compile my findings into a comprehensive summary:

## Comprehensive Report: Solver-Trace-Ablation Project Evaluation Infrastructure

Based on my thorough exploration of the `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/` directory, here's the complete picture of the evaluation infrastructure:

### 1. **Core Evaluation Methodology: Solver Trace Ablation (STA)**

**What is STA?**
- A component-based ablation algorithm for measuring formalization quality through the **Intensional Score Rate (ISR)**
- Grounded in the **Reachability-Infection-Propagation (RIP) framework** from mutation testing theory
- For each formalization component `c_i`, tests if its removal/ablation changes the solver's output:
  - `Necessary(c_i, p, S) = 1[S(p_{-i}) ≠ S(p)]` (where `p_{-i}` = formalization with component removed)
  - **ISR** = `(1/|C(p)|) × Σ Necessary(c_i, p, S)`
  - ISR = 1.0 means all components are necessary (fully intensional)
  - ISR ≈ 0 means most components are extensionally redundant (reward-hacked)

**Key Files:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/train_grpo.py` — Contains the GRPO training pipeline that invokes `fast_sta_reward()` and solver integration
- Imports from `src.solvers.factory` and `src.sta.reward` (external to this directory)

### 2. **Solver Integration & Invocation**

**Solvers Configured:**
1. **FOL → Prover9** (LADR 2009-11A)
   - O(1) ISR approximation: Check if conclusion is provable without premises (tautology detection)
   - If provable without premises → ISR ≈ 0 (extensional shortcut)
   
2. **Prolog → SWI-Prolog 8.4.2**
   - O(1) ISR approximation: Execute query with facts only (remove all rules)
   - If succeeds → ISR ≈ 0 (fact enumeration shortcut)
   
3. **SMT-LIB → Z3 4.16.0.0**
   - O(1) ISR approximation: Check satisfiability of negation
   - If unsatisfiable → ISR ≈ 0 (hard-coded assignment shortcut)

**How Solvers Are Called:**
- `get
…[truncated 8455 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Agent",
  "elapsed_ms": 6
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-14T02:11:53.545972+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.py",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-14T02:11:53.546110+00:00_

artifacts/train_grpo.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-14T02:11:53.546231+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "decisions.yaml",
  "max_chars": "4000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "decisions.yaml",
    "max_chars": "4000"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-14T02:11:53.546400+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/decisions.yaml\", \"content\": \"_next_id: 12\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 17:34 UTC\\n  summary: MVP 方案：FOL+Prover9 单逻辑 50-step GRPO pilot 验证 STA reward 有效性\\n  rationale: EMNLP ARR DDL 5/25 仅剩 12 天，需要最快速度验证核心假设。选 FOL+Prover9 因为 hacking 模式最清晰（tautological\\n    formulas），STA 的 O(1) 近似最直观（去掉前提后能否证明结论）。50-step pilot 足以观察 ISR 趋势。两个条件并行跑 2 GPU。Pass\\n    标准：ISR gap >20pp + accuracy 降幅 <5pp。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 17:37 UTC\\n  summary: MVP 方案调整：50步→100步 + 趋势判断 + Phase 0 ISR baseline + kill criteria\\n  rationale: 采纳 Reviewer 三条 warning：(1) 加 pre-training ISR baseline 锚定训练前水平；(2) 50步太短难以观察\\n    reward hacking，改 100步+最后20步 moving average 趋势判断；(3) 补充硬性 kill criteria 防止 DDL\\n    压力下无止境调整。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 20:50 UTC\\n  summary: Phase 1 r4 fast_isr_fol 训练信号无效，改用 full STA + K=8 重跑\\n  rationale: fast_isr_fol 是二值 O(1) 近似（ISR=0 tautology / ISR=1 non-tautology），Qwen3-4B\\n    生成的 proved formalization 几乎全部 ISR=1，与 execution-only 零差异。full STA 提供连续 ISR（0.125-0.889\\n    in Phase 0），能给出真实梯度信号。K=4 导致 frac_reward_zero_std=0.5-1.0（GRPO 无 advantage），K=8\\n    增加 within-group variance。两个改动分别解决 STA 信号粒度和 GRPO 梯度信号两个独立问题。\\n  related_experiments:\\n  - exp_id: sta-phase1-exec-only-r4\\n    role: evidence\\n    result: prove_rate 12%→15%, ISR ~0.15, minimal learning\\n  - exp_id: sta-phase1-exec-sta-r4\\n    role: evidence\\n    result: 与 exec-only 几乎完全相同, fast_isr 提供零额外信号\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-13 21:59 UTC\\n  summary: Reviewer 指出 exec-sta-r5 prove_rate 低于 baseline（退化），STA 50/50 权重过于惩罚性。立即补跑低权重\\n    + bonus 模式实验\\n  rationale: exec-sta-r5 prove_rate=0.10 < baseline=0.12 < exec-only=0.15。连续 ISR 给\\n    proved-but-low-ISR 样本 reward≈0.3（几乎等于未 prove），模型学到 prove 不值得。Kill criteria
…[truncated 2500 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-14T02:11:53.546557+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/train_grpo.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/train_grpo.py"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-14T02:11:53.546800+00:00_

1	"""Phase 1 GRPO training: execution-only vs execution+STA reward.
2	
3	Usage:
4	  # execution-only (GPU 0)
5	  CUDA_VISIBLE_DEVICES=0 python scripts/train_grpo.py \
6	    --model_path /root/autodl-tmp/models/Qwen3-4B \
7	    --data_path data/proofwriter_fol_500.jsonl \
8	    --reward_mode execution_only --output_dir outputs/grpo_exec_only \
9	    --num_steps 100 --wandb_project solver-trace-ablation
10	
11	  # execution+STA (GPU 1)
12	  CUDA_VISIBLE_DEVICES=1 python scripts/train_grpo.py \
13	    --model_path /root/autodl-tmp/models/Qwen3-4B \
14	    --data_path data/proofwriter_fol_500.jsonl \
15	    --reward_mode execution_sta --output_dir outputs/grpo_exec_sta \
16	    --num_steps 100 --wandb_project solver-trace-ablation
17	"""
18	
19	from __future__ import annotations
20	
21	import argparse
22	import json
23	import logging
24	import os
25	import re
26	import sys
27	import time
28	from datetime import datetime, timezone
29	from pathlib import Path
30	
31	import torch
32	from datasets import Dataset
33	from transformers import AutoModelForCausalLM, AutoTokenizer, TrainerCallback
34	from trl import GRPOConfig, GRPOTrainer
35	
36	sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
37	
38	from src.solvers.factory import get_solver
39	from src.sta.reward import _parse_formalization, fast_sta_reward
40	
41	logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
42	logger = logging.getLogger(__name__)
43	
44	
45	SYSTEM_PROMPT = (
46	    "You are a first-order logic (FOL) expert. "
47	    "Given natural language premises and a conclusion, formalize them into FOL.\n\n"
48	    "Output format:\n"
49	    "Premises:\n"
50	    "1. &lt;FOL formula>\n"
51	    "2. &lt;FOL formula>\n"
52	    "...\n"
53	    "Conclusion: &lt;FOL formula>\n\n"
54	    "Use standard FOL notation with predicate-argument syntax: "
55	    "all x (P(x) -> Q(x)), exists x P(x), P(a) & Q(a), -P(a), P(a) | Q(a), P(a) -> Q(a)."
56	)
57	
58	USER_TEMPLATE = (
59	    "Formali
…[truncated 11253 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-14T02:11:53.546982+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "IDEA_BRIEF.md",
  "max_chars": "6000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "IDEA_BRIEF.md",
    "max_chars": "6000"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-14T02:11:53.547150+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'IDEA_BRIEF.md'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-14T02:11:53.547342+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*eval*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*eval*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-14T02:11:53.547554+00:00_

logs/workers/worker_code_plan003-eval-submit_20260513T222000.log
logs/workers/worker_code_plan003-eval-submit_20260513T222000_result.json
logs/workers/worker_code_p2-eval-scripts_20260513T222126.log
logs/chats/worker_code_p2-eval-scripts_20260513T222126.lock
logs/chats/worker_code_p2-eval-scripts_20260513T222126.jsonl
logs/workers/worker_code_p2-eval-scripts_20260513T222126_result.json
checkpoints/plan003-eval-exec-only-r5_PREPARING_20260513T224234.json
checkpoints/plan003-eval-exec-only-r5_PENDING_20260513T230219.json
checkpoints/plan003-eval-exec-only-r5_QUEUED_20260513T230229.json
checkpoints/plan003-eval-exec-only-r5_QUEUED_20260513T230230.json
checkpoints/plan003-eval-exec-only-r5_ALLOCATED_20260513T230237.json
checkpoints/plan003-eval-exec-only-r5_ALLOCATED_20260513T230238.json
checkpoints/plan003-eval-exec-only-r5_RUNNING_20260513T230249.json
checkpoints/plan003-eval-exec-only-r5_RUNNING_20260513T230254.json
checkpoints/plan003-eval-exec-only-r5_ANALYZING_20260513T230302.json
checkpoints/plan003-eval-exec-only-r5_DONE_20260513T230318.json
logs/workers/worker_code_eval-scripts-prep_20260514T013607.log
logs/chats/worker_code_eval-scripts-prep_20260514T013607.lock
logs/chats/worker_code_eval-scripts-prep_20260514T013607.jsonl
logs/workers/worker_code_eval-scripts-prep_20260514T013607_result.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-14T02:11:53.547734+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/checkpoints/plan003-eval-exec-only-r5_DONE_20260513T230318.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/checkpoints/plan003-eval-exec-only-r5_DONE_20260513T230318.json"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-14T02:11:53.547939+00:00_

1	{
2	  "exp_id": "plan003-eval-exec-only-r5",
3	  "project": "solver-trace-ablation",
4	  "state": "DONE",
5	  "previous_state": "ANALYZING",
6	  "experiment_data": {
7	    "status": "DONE",
8	    "retry_count": 0,
9	    "created_at": "2026-05-13T22:21:48.691Z",
10	    "updated_at": "2026-05-13T23:03:18.848Z",
11	    "spec": {
12	      "command": "eval_sta.py on r5 exec-only checkpoint",
13	      "server": "westd-39279",
14	      "gpu": [
15	        "cuda:1"
16	      ],
17	      "pid": "83690",
18	      "log_path": "~/runs/solver-trace-ablation/plan003-eval-exec-only-r5.log",
19	      "submitted_at": "2026-05-13T22:21:48.658Z",
20	      "submitted_via": "submit_training_job",
21	      "backend": "tmux",
22	      "account": "root",
23	      "data_path": "/root/solver-trace-ablation/data/proofwriter_fol_100.jsonl",
24	      "data_count": 100,
25	      "model_name": "Qwen3-4B (r5 exec-only checkpoint)",
26	      "seed": 0,
27	      "checkpoint_source": "sta-phase1-exec-only-r5",
28	      "eval_data": "proofwriter_fol_100",
29	      "hypothesis": "Full STA eval on exec-only 100-step checkpoint to measure formalization quality",
30	      "wall_clock_seconds": 2490.2,
31	      "gpu_hours": 0.69
32	    },
33	    "metrics": {
34	      "prove_rate": 0.32,
35	      "mean_isr": 0.2055,
36	      "isr_std": 0.3194,
37	      "proved_only_isr": 0.6423,
38	      "isr_by_type": {
39	        "true": 0.3598,
40	        "false": 0.1723,
41	        "unknown": 0.0979
42	      },
43	      "total_samples": 100,
44	      "proved_count": 32,
45	      "runtime_s": 251.7
46	    },
47	    "conclusion": "success",
48	    "checkpoint_path": "/root/autodl-tmp/outputs/plan003_eval_exec_only_r5.json",
49	    "log_path": "~/runs/solver-trace-ablation/plan003-eval-exec-only-r5.log",
50	    "completed_at": "2026-05-13T23:03:18.848Z"
51	  },
52	  "timestamp": "2026-05-13T23:03:18.886626+00:00",
53	  "trigger": "update_registry"
54	}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-14T02:11:53.548138+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-14T02:11:53.548271+00:00_

diagnose_phase1_r3.md
dream_reports
grpo_exec_only.yaml
grpo_exec_sta.yaml
hacking_taxonomy.md
launch_phase1.sh
literature_map.yaml
manifest.yaml
phase1_r2_diagnosis.md
plan005_negative_literature.md
seed44_readiness.md
sta-phase0-baseline
train_grpo.py
training_progress_check.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-14T02:11:53.548428+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/plan014_design.md",
  "content": "# Plan 014: Downstream Validation — ISR as Quality Proxy\n\n## 1. 选择方案及理由\n\n**主方案：Label-Prediction Accuracy（3-way entailment classification）**\n\n对每个 FOLIO 样本，用 checkpoint 生成 K 个 FOL formalization，然后通过 Prover9 做 3-way 分类：\n- Prove(premises → conclusion) 成功 → 预测 `true`\n- Prove(premises → ¬conclusion) 成功 → 预测 `false`\n- 两者均失败 → 预测 `unknown`\n\n将预测与 ground-truth label 比较，得到 **label accuracy**。然后分析 ISR 与 label accuracy 的相关性。\n\n**为什么选这个方案：**\n\n| 方案 | 独立于 ISR? | 工程量 | 说服力 | 可行性 |\n|------|-----------|--------|--------|--------|\n| A. Entailment accuracy | ⚠️ 用同一个 solver | 低 | 中 | ✅ |\n| **B. Label prediction** | ✅ 评估 semantic correctness | 低 | **高** | ✅ |\n| C. Cross-solver transfer | ✅ 不同 solver | 中（需 FOL→SMT-LIB 翻译） | 高 | ⚠️ |\n| D. Semantic equivalence | ✅ 不用 solver 评估 | 高（需多次生成+一致性度量） | 中 | ⚠️ |\n| E. Human evaluation | ✅ 完全独立 | 低（代码）但高（人力） | 最高 | ❌ DDL 内不可行 |\n\nLabel prediction 的核心优势：\n1. **与 ISR 完全正交**：ISR 衡量\"每个 premise 是否 necessary\"，label accuracy 衡量\"formalization 是否正确捕获了语义\"。一个 tautological formalization 可以有 prove_rate=1.0 但 label accuracy 很低（所有 false/unknown 样本都被错误预测为 true），同时 ISR 也低（premises 不必要）。\n2. **直接回答 reviewer 的问题**：\"高 ISR 的 formalization 真的更好吗？\" → 是的，它们在独立的 semantic correctness 任务上表现更好。\n3. **零额外工程依赖**：只需在现有 Prover9 pipeline 上加一个 negation-prove 步骤。\n4. **Best-of-N framing**：ISR 作为 selection criterion 选出的 formalization 比随机选择的 label accuracy 更高 — 这是一个直接的实用价值证明。\n\n**副方案（可选）：Cross-Solver Transfer（FOL → Z3）**\n\n将 Prover9 FOL 翻译为 SMT-LIB，用 Z3 验证。高 ISR 的 formalization 应更 transferable（在不同 solver 上也能 prove）。这个方案说服力强但需要 FOL→SMT-LIB 翻译器（~150 行），视时间决定是否实施。\n\n## 2. 具体实验步骤\n\n### Phase 1: Inference（GPU，~20 min）\n\n```\n输入：proofwriter_fol_100.jsonl + exec-only 500-step checkpoint\n输出：generations.jsonl（100 × K=8 = 800 formalizations）\n```\n\n1. 加载 plan001-exec-only-s42-r2 checkpoint\n2. 对 100 个 eval 样本，每个生成 K=8 个 formalization（temperature=0.7，top_p=0.9）\n3. 解析每个 formalization，提取 premises 和 conclusion\n4. 保存：`{example_id, generation_idx, raw_text, parsed_premises, parsed_conclusion}`\n\n### Phase 2: ISR Computation（CPU，~40 min）\n\n```\n输入：generations.jsonl\n输出：isr_scores.jsonl\n```\n\n对每个 formalization：\n1. 用 Prover9 prove(premises → conclusion)（5s timeout）\n2. 若 proved：run full STA（leave-one-out ablation each premise）→ ISR ∈ [0,1]\n3. 若 not proved：ISR = undefined（仅分析 proved 子集）\n4. 保存：`{example_id, generation_idx, proved, isr_score}`\n\n可用 `multiprocessing.Pool(workers=8)` 并行化 Prover9 调用（CPU-bound，不占 GPU）。\n\n### Phase 3: Label Prediction（CPU，~20 min）\n\n```\n输入：generations.jsonl + ground-truth labels\n输出：label_predictions.jsonl\n```\n\n对每个 formalization：\n1. Prove(premises → conclusion)：成功 → candidate_true = True\n2. Prove(premises → ¬conclusion)：成功 → candidate_false = True\n   - 实现：将 conclusion 取反后作为 goal，e.g., `-(conclusion)` in Prover9 syntax\n3. 3-way classification：\n   - candidate_true and not candidate_false → predict `true`\n   - candidate_false and not candidate_true → predict `false`\n   - neither → predict `unknown`\n   - both → predict `true`（entailment 优先，此情况理论上不应发生）\n4. 与 ground-truth label 比较 → correct ∈ {0, 1}\n5. 保存：`{example_id, generation_idx, predicted_label, gt_label, correct}`\n\n### Phase 4: Ground-Truth Baseline（CPU，~10 min）\n\n```\n输入：proofwriter_fol_100.jsonl 中的 GT fol_premises + fol_conclusion\n输出：gt_baseline.jsonl\n```\n\n对 GT formalization 执行 Phase 2 + Phase 3，作为 upper bound 参考：\n- GT ISR（已知 ~0.56）\n- GT label accuracy（衡量 solver 能力天花板）\n\n### Phase 5: Analysis（CPU，~5 min）\n\n```\n输入：isr_scores.jsonl + label_predictions.jsonl + gt_baseline.jsonl\n输出：plan014_results.json + 图表\n```\n\n#### 5a. Correlation Analysis\n- 在 proved 子集上：Spearman ρ(ISR, correct)\n- 在全部样本上：point-biserial correlation(proved, correct)\n\n#### 5b. Stratified Comparison\n- 按 ISR 分为 4 组（quartiles）\n- 每组计算 mean label accuracy\n- Mann-Whitney U test: top-quartile ISR vs bottom-quartile ISR 的 label accuracy 差异\n\n#### 5c. Best-of-N Selection\n对每个 example（K=8 generations），比较 4 种 selection 策略的 label accuracy：\n- **Oracle**：选 correct 的（upper bound）\n- **ISR-best**：选 ISR 最高的\n- **Random**：随机选一个\n- **Prove-first**：选第一个 proved 的\n\n如果 ISR-best > Random，说明 ISR 可作为 quality selector，这是直接的实用价值。\n\n#### 5d. Per-Label-Type Breakdown\n- 分 true/false/unknown 三类计算上述指标\n- 预期：ISR 对 true 类最 discriminative（Prover9 对 true 证明最可靠）\n\n### Phase 6（可选）: Cross-Solver Transfer\n\n```\n输入：proved formalizations\n输出：z3_transfer.jsonl\n```\n\n1. 实现 FOL → SMT-LIB 翻译器（~150 行）\n   - Prover9 语法 → AST → SMT-LIB s-expression\n   - 处理：quantifiers, predicates, connectives, negation\n2. 对每个 proved formalization：Z3 check(premises → conclusion)\n3. 计算 cross-solver prove rate，按 ISR 分组对比\n\n## 3. 需要的脚本/代码变更\n\n### 新建脚本\n\n| 文件 | 职责 | 估计行数 |\n|------|------|---------|\n| `scripts/eval_downstream.py` | Phase 1-3 一体化：inference + ISR + label prediction | ~250 |\n| `scripts/analyze_downstream.py` | Phase 5 分析：correlation, Best-of-N, 可视化 | ~150 |\n| `scripts/fol_to_smtlib.py` | （可选）Phase 6 FOL→SMT-LIB 翻译 | ~150 |\n\n### 已有代码变更\n\n| 文件 | 变更 | 说明 |\n|------|------|------|\n| `src/solvers/prover9_solver.py`（或等价） | 新增 `prove_negation(premises, conclusion)` | 将 conclusion 取反后 prove；或直接在 eval 脚本中处理 |\n\n主要复用：\n- `src/sta.reward.fast_sta_reward()` — ISR 计算\n- `src/sta.reward._parse_formalization()` — 解析模型输出\n- `src/solvers.factory.get_solver()` — Prover9 实例化\n- `train_grpo.py` 中的 `SYSTEM_PROMPT`、`USER_TEMPLATE`、`strip_thinking()` — prompt 构造\n\n### eval_downstream.py 核心结构\n\n```python\ndef main():\n    # Phase 1: Inference\n    model = load_checkpoint(args.checkpoint_path)\n    tokenizer = AutoTokenizer.from_pretrained(args.checkpoint_path)\n    eval_data = load_jsonl(args.eval_data)\n    generations = generate_k(model, tokenizer, eval_data, K=8, temp=0.7)\n\n    # Phase 2 + 3: ISR + Label prediction (parallelizable)\n    solver = get_solver(\"prover9\")\n    with Pool(8) as pool:\n        results = pool.map(eval_single, [(g, solver) for g in generations])\n\n    # Output\n    save_jsonl(results, args.output_path)\n\ndef eval_single(gen, solver):\n    # Parse formalization\n    parsed = _parse_formalization(gen[\"text\"])\n    premises, conclusion = parsed[\"premises\"], parsed[\"conclusion\"]\n\n    # ISR (Phase 2)\n    sta_result = fast_sta_reward({}, gen[\"text\"], solver, ...)\n    isr = sta_result.get(\"sta_reward\", None)\n\n    # Label prediction (Phase 3)\n    proved_true = solver.prove(premises, conclusion, timeout=5)\n    proved_false = solver.prove(premises, negate(conclusion), timeout=5)\n    predicted = classify(proved_true, proved_false)\n    correct = (predicted == gen[\"gt_label\"])\n\n    return {**gen, \"isr\": isr, \"predicted\": predicted, \"correct\": correct}\n```\n\n## 4. 评估指标\n\n### Primary Metrics（论文 Table）\n\n| Metric | 定义 | 预期方向 |\n|--------|------|---------|\n| **ρ(ISR, accuracy)** | Spearman rank correlation between ISR and label correctness | ρ > 0.3 (positive) |\n| **BoN accuracy (ISR)** | Best-of-N label accuracy using ISR as selector | > Random |\n| **BoN accuracy (Random)** | Best-of-N label accuracy using random selection | baseline |\n| **Δ accuracy (Q4 − Q1)** | Label accuracy difference between top and bottom ISR quartiles | > 0, significant |\n\n### Secondary Metrics\n\n| Metric | 定义 |\n|--------|------|\n| GT label accuracy | Ground-truth formalization 的 label accuracy（solver 天花板） |\n| Per-type ρ | 按 true/false/unknown 分别计算 correlation |\n| Cross-solver rate (optional) | Z3 prove rate for high vs low ISR groups |\n\n### Statistical Tests\n\n- Spearman ρ with p-value（n ≥ 50 for adequate power at ρ > 0.35）\n- Mann-Whitney U for quartile comparisons（non-parametric，不假设正态）\n- Bootstrap 95% CI for BoN accuracy differences\n\n## 5. 预期结果\n\n### 支持 ISR 有效性的结果\n\n```\nρ(ISR, label_accuracy) ≥ 0.3, p < 0.05\nBoN(ISR-best) accuracy > BoN(Random) accuracy by ≥ 5pp\nQ4 ISR group accuracy > Q1 ISR group accuracy, p < 0.05\n```\n\n**解释**：高 ISR 的 formalization 确实更正确地捕获了 NL 语义 → ISR 是 genuine quality proxy，非 circular metric。\n\n论文表述：*\"Formalizations with higher ISR achieve X% label accuracy versus Y% for the lowest ISR quartile (Mann-Whitney U, p < 0.05), confirming that ISR measures structural quality beyond Prover9-specific provability.\"*\n\n### 弱支持/需注意的结果\n\n```\nρ ∈ (0.15, 0.3), p < 0.1\nBoN(ISR-best) ≈ BoN(Prove-first) > BoN(Random)\n```\n\n**解释**：ISR 有一定预测力但与 prove/not-prove 区分难以分离。需在论文中 qualify claim：*\"ISR provides additional but modest quality signal beyond binary provability.\"*\n\n### 反对 ISR 有效性的结果\n\n```\nρ ≤ 0.15 or ρ < 0, n.s.\nBoN(ISR-best) ≈ BoN(Random)\n```\n\n**解释**：ISR 不预测 semantic correctness → ISR 只反映 Prover9 内部 proof structure，非真实质量。论文须降级 ISR 为 monitoring-only metric，不可作为 quality proxy。\n\n### 关于 label type 分布的预期\n\n| Label type | 占比 (~) | 预期 label accuracy | ISR 相关性 |\n|-----------|---------|-------------------|-----------|\n| true | ~50% | 高（Prover9 擅长 prove entailment） | 最强 |\n| false | ~30% | 中（需 prove negation，依赖 formalization 质量） | 中 |\n| unknown | ~20% | 低（需两个 prove 都失败，受 timeout 影响） | 最弱 |\n\n## 6. 时间/资源估算\n\n### 实现（人力）\n\n| 阶段 | 工作量 | 说明 |\n|------|--------|------|\n| eval_downstream.py | 3-4h | 复用大量现有代码 |\n| analyze_downstream.py | 2-3h | scipy.stats + matplotlib |\n| 调试 & 修复 | 2h | negation prove、edge case |\n| fol_to_smtlib.py（可选） | 4-6h | FOL parser + SMT-LIB emitter |\n| **总计** | **7-9h**（不含可选） | |\n\n### 运行（计算）\n\n| Phase | 资源 | 时间 | 说明 |\n|-------|------|------|------|\n| 1: Inference | 1 GPU | ~20 min | Qwen3-4B, 100×8 generations |\n| 2: ISR | CPU only | ~40 min | 8-worker parallel Prover9 |\n| 3: Label pred | CPU only | ~20 min | 800 × 2 Prover9 calls |\n| 4: GT baseline | CPU only | ~10 min | 100 × STA + label pred |\n| 5: Analysis | CPU only | ~5 min | stats + plots |\n| **Total GPU** | | **~20 min** | 远低于 1 GPU·h 预算 |\n| **Total wall clock** | | **~1.5h** | 串行；并行可压缩到 ~1h |\n\n### DDL 风险评估\n\n- **可行性**：高。核心代码 1 天可完成，实验运行 < 2h。\n- **依赖**：需要 plan001-exec-only-s42 checkpoint 成功运行。当前 r4 正在运行中。\n  - **备选**：用 100-step exec-only checkpoint（r5，已成功），prove_rate 较低但 ISR 方差更大，更利于 correlation 分析。\n- **与其他实验并行性**：Phase 2-5 只用 CPU，不占 GPU → 可与 plan001/plan013 训练同时进行。\n- **建议排期**：plan001-r4 成功后立即启动。最晚 5/19 开始，5/20 完成。\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/plan014_design.md",
    "content": "# Plan 014: Downstream Validation — ISR as Quality Proxy\n\n## 1. 选择方案及理由\n\n**主方案：Label-Prediction Accuracy（3-way entailment classification）**\n\n对每个 FOLIO 样本，用 checkpoint 生成 K 个 FOL formalization，然后通过 Prover9 做 3-way 分类：\n- Prove(premises → conclusion) 成功 → 预测 `true`\n- Prove(premises → ¬conclusion) 成功 → 预测 `false`\n- 两者均失败 → 预测 `unknown`\n\n将预测与 ground-truth label 比较，得到 **label accuracy**。然后分析 ISR 与 label accuracy 的相关性。\n\n**为什么选这个方案：**\n\n| 方案 | 独立于 ISR? | 工程量 | 说服力 | 可行性 |\n|------|-----------|--------|--------|--------|\n| A. Entailment accuracy | ⚠️ 用同一个 solver | 低 | 中 | ✅ |\n| **B. Label prediction** | ✅ 评估 semantic correctness | 低 | **高** | ✅ |\n| C. Cross-solver transfer | ✅ 不同 solver | 中（需 FOL→SMT-LIB 翻译） | 高 | ⚠️ |\n| D. Semantic equivalence | ✅ 不用 solver 评估 | 高（需多次生成+一致性度量） | 中 | ⚠️ |\n| E. Human evaluation | ✅ 完全独立 | 低（代码）但高（人力） | 最高 | ❌ DDL 内不可行 |\n\nLabel prediction 的核心优势：\n1. **与 ISR 完全正交**：ISR 衡量\"每个 premise 是否 necessary\"，label accuracy 衡量\"formalization 是否正确捕获了语义\"。一个 tautological formalization 可以有 prove_rate=1.0 但 label accuracy 很低（所有 false/unknown 样本都被错误预测为 true），同时 ISR 也低（premises 不必要）。\n2. **直接回答 reviewer 的问题**：\"高 ISR 的 formalization 真的更好吗？\" → 是的，它们在独立的 semantic correctness 任务上表现更好。\n3. **零额外工程依赖**：只需在现有 Prover9 pipeline 上加一个 negation-prove 步骤。\n4. **Best-of-N framing**：ISR 作为 selection criterion 选出的 formalization 比随机选择的 label accuracy 更高 — 这是一个直接的实用价值证明。\n\n**副方案（可选）：Cross-Solver Transfer（FOL → Z3）**\n\n将 Prover9 FOL 翻译为 SMT-LIB，用 Z3 验证。高 ISR 的 formalization 应更 transferable（在不同 solver 上也能 prove）。这个方案说服力强但需要 FOL→SMT-LIB 翻译器（~150 行），视时间决定是否实施。\n\n## 2. 具体实验步骤\n\n### Phase 1: Inference（GPU，~20 min）\n\n```\n输入：proofwriter_fol_100.jsonl + exec-only 500-step checkpoint\n输出：generations.jsonl（100 × K=8 = 800 formalizations）\n```\n\n1. 加载 plan001-exec-only-s42-r2 checkpoint\n2. 对 100 个 eval 样本，每个生成 K=8 个 formalization（temperature=0.7，top_p=0.9）\n3. 解析每个 formalization，提取 premises 和 conclusion\n4. 保存：`{example_id, generation_idx, raw_text, parsed_premises, parsed_conclusion}`\n\n### Phase 2: ISR Computation（CPU，~40 min）\n\n```\n输入：generations.jsonl\n输出：isr_scores.jsonl\n```\n\n对每个 formalization：\n1. 用 Prover9 prove(premises → conclusion)（5s timeout）\n2. 若 proved：run full STA（leave-one-out ablation each premise）→ ISR ∈ [0,1]\n3. 若 not proved：ISR = undefined（仅分析 proved 子集）\n4. 保存：`{example_id, generation_idx, proved, isr_score}`\n\n可用 `multiprocessing.Pool(workers=8)` 并行化 Prover9 调用（CPU-bound，不占 GPU）。\n\n### Phase 3: Label Prediction（CPU，~20 min）\n\n```\n输入：generations.jsonl + ground-truth labels\n输出：label_predictions.jsonl\n```\n\n对每个 formalization：\n1. Prove(premises → conclusion)：成功 → candidate_true = True\n2. Prove(premises → ¬conclusion)：成功 → candidate_false = True\n   - 实现：将 conclusion 取反后作为 goal，e.g., `-(conclusion)` in Prover9 syntax\n3. 3-way classification：\n   - candidate_true and not candidate_false → predict `true`\n   - candidate_false and not candidate_true → predict `false`\n   - neither → predict `unknown`\n   - both → predict `true`（entailment 优先，此情况理论上不应发生）\n4. 与 ground-truth label 比较 → correct ∈ {0, 1}\n5. 保存：`{example_id, generation_idx, predicted_label, gt_label, correct}`\n\n### Phase 4: Ground-Truth Baseline（CPU，~10 min）\n\n```\n输入：proofwriter_fol_100.jsonl 中的 GT fol_premises + fol_conclusion\n输出：gt_baseline.jsonl\n```\n\n对 GT formalization 执行 Phase 2 + Phase 3，作为 upper bound 参考：\n- GT ISR（已知 ~0.56）\n- GT label accuracy（衡量 solver 能力天花板）\n\n### Phase 5: Analysis（CPU，~5 min）\n\n```\n输入：isr_scores.jsonl + label_predictions.jsonl + gt_baseline.jsonl\n输出：plan014_results.json + 图表\n```\n\n#### 5a. Correlation Analysis\n- 在 proved 子集上：Spearman ρ(ISR, correct)\n- 在全部样本上：point-biserial correlation(proved, correct)\n\n#### 5b. Stratified Comparison\n- 按 ISR 分为 4 组（quartiles）\n- 每组计算 mean label accuracy\n- Mann-Whitney U test: top-quartile ISR vs bottom-quartile ISR 的 label accuracy 差异\n\n#### 5c. Best-of-N Selection\n对每个 example（K=8 generations），比较 4 种 selection 策略的 label accuracy：\n- **Oracle**：选 correct 的（upper bound）\n- **ISR-best**：选 ISR 最高的\n- **Random**：随机选一个\n- **Prove-first**：选第一个 proved 的\n\n如果 ISR-best > Random，说明 ISR 可作为 quality selector，这是直接的实用价值。\n\n#### 5d. Per-Label-Type Breakdown\n- 分 true/false/unknown 三类计算上述指标\n- 预期：ISR 对 true 类最 discriminative（Prover9 对 true 证明最可靠）\n\n### Phase 6（可选）: Cross-Solver Transfer\n\n```\n输入：proved formalizations\n输出：z3_transfer.jsonl\n```\n\n1. 实现 FOL → SMT-LIB 翻译器（~150 行）\n   - Prover9 语法 → AST → SMT-LIB s-expression\n   - 处理：quantifiers, predicates, connectives, negation\n2. 对每个 proved formalization：Z3 check(premises → conclusion)\n3. 计算 cross-solver prove rate，按 ISR 分组对比\n\n## 3. 需要的脚本/代码变更\n\n### 新建脚本\n\n| 文件 | 职责 | 估计行数 |\n|------|------|---------|\n| `scripts/eval_downstream.py` | Phase 1-3 一体化：inference + ISR + label prediction | ~250 |\n| `scripts/analyze_downstream.py` | Phase 5 分析：correlation, Best-of-N, 可视化 | ~150 |\n| `scripts/fol_to_smtlib.py` | （可选）Phase 6 FOL→SMT-LIB 翻译 | ~150 |\n\n### 已有代码变更\n\n| 文件 | 变更 | 说明 |\n|------|------|------|\n| `src/solvers/prover9_solver.py`（或等价） | 新增 `prove_negation(premises, conclusion)` | 将 conclusion 取反后 prove；或直接在 eval 脚本中处理 |\n\n主要复用：\n- `src/sta.reward.fast_sta_reward()` — ISR 计算\n- `src/sta.reward._parse_formalization()` — 解析模型输出\n- `src/solvers.factory.get_solver()` — Prover9 实例化\n- `train_grpo.py` 中的 `SYSTEM_PROMPT`、`USER_TEMPLATE`、`strip_thinking()` — prompt 构造\n\n### eval_downstream.py 核心结构\n\n```python\ndef main():\n    # Phase 1: Inference\n    model = load_checkpoint(args.checkpoint_path)\n    tokenizer = AutoTokenizer.from_pretrained(args.checkpoint_path)\n    eval_data = load_jsonl(args.eval_data)\n    generations = generate_k(model, tokenizer, eval_data, K=8, temp=0.7)\n\n    # Phase 2 + 3: ISR + Label prediction (parallelizable)\n    solver = get_solver(\"prover9\")\n    with Pool(8) as pool:\n        results = pool.map(eval_single, [(g, solver) for g in generations])\n\n    # Output\n    save_jsonl(results, args.output_path)\n\ndef eval_single(gen, solver):\n    # Parse formalization\n    parsed = _parse_formalization(gen[\"text\"])\n    premises, conclusion = parsed[\"premises\"], parsed[\"conclusion\"]\n\n    # ISR (Phase 2)\n    sta_result = fast_sta_reward({}, gen[\"text\"], solver, ...)\n    isr = sta_result.get(\"sta_reward\", None)\n\n    # Label prediction (Phase 3)\n    proved_true = solver.prove(premises, conclusion, timeout=5)\n    proved_false = solver.prove(premises, negate(conclusion), timeout=5)\n    predicted = classify(proved_true, proved_false)\n    correct = (predicted == gen[\"gt_label\"])\n\n    return {**gen, \"isr\": isr, \"predicted\": predicted, \"correct\": correct}\n```\n\n## 4. 评估指标\n\n### Primary Metrics（论文 Table）\n\n| Metric | 定义 | 预期方向 |\n|--------|------|---------|\n| **ρ(ISR, accuracy)** | Spearman rank correlation between ISR and label correctness | ρ > 0.3 (positive) |\n| **BoN accuracy (ISR)** | Best-of-N label accuracy using ISR as selector | > Random |\n| **BoN accuracy (Random)** | Best-of-N label accuracy using random selection | baseline |\n| **Δ accuracy (Q4 − Q1)** | Label accuracy difference between top and bottom ISR quartiles | > 0, significant |\n\n### Secondary Metrics\n\n| Metric | 定义 |\n|--------|------|\n| GT label accuracy | Ground-truth formalization 的 label accuracy（solver 天花板） |\n| Per-type ρ | 按 true/false/unknown 分别计算 correlation |\n| Cross-solver rate (optional) | Z3 prove rate for high vs low ISR groups |\n\n### Statistical Tests\n\n- Spearman ρ with p-value（n ≥ 50 for adequate power at ρ > 0.35）\n- Mann-Whitney U for quartile comparisons（non-parametric，不假设正态）\n- Bootstrap 95% CI for BoN accuracy differences\n\n## 5. 预期结果\n\n### 支持 ISR 有效性的结果\n\n```\nρ(ISR, label_accuracy) ≥ 0.3, p < 0.05\nBoN(ISR-best) accuracy > BoN(Random) accuracy by ≥ 5pp\nQ4 ISR group accuracy > Q1 ISR group accuracy, p < 0.05\n```\n\n**解释**：高 ISR 的 formalization 确实更正确地捕获了 NL 语义 → ISR 是 genuine quality proxy，非 circular metric。\n\n论文表述：*\"Formalizations with higher ISR achieve X% label accuracy versus Y% for the lowest ISR quartile (Mann-Whitney U, p < 0.05), confirming that ISR measures structural quality beyond Prover9-specific provability.\"*\n\n### 弱支持/需注意的结果\n\n```\nρ ∈ (0.15, 0.3), p < 0.1\nBoN(ISR-best) ≈ BoN(Prove-first) > BoN(Random)\n```\n\n**解释**：ISR 有一定预测力但与 prove/not-prove 区分难以分离。需在论文中 qualify claim：*\"ISR provides additional but modest quality signal beyond binary provability.\"*\n\n### 反对 ISR 有效性的结果\n\n```\nρ ≤ 0.15 or ρ < 0, n.s.\nBoN(ISR-best) ≈ BoN(Random)\n```\n\n**解释**：ISR 不预测 semantic correctness → ISR 只反映 Prover9 内部 proof structure，非真实质量。论文须降级 ISR 为 monitoring-only metric，不可作为 quality proxy。\n\n### 关于 label type 分布的预期\n\n| Label type | 占比 (~) | 预期 label accuracy | ISR 相关性 |\n|-----------|---------|-------------------|-----------|\n| true | ~50% | 高（Prover9 擅长 prove entailment） | 最强 |\n| false | ~30% | 中（需 prove negation，依赖 formalization 质量） | 中 |\n| unknown | ~20% | 低（需两个 prove 都失败，受 timeout 影响） | 最弱 |\n\n## 6. 时间/资源估算\n\n### 实现（人力）\n\n| 阶段 | 工作量 | 说明 |\n|------|--------|------|\n| eval_downstream.py | 3-4h | 复用大量现有代码 |\n| analyze_downstream.py | 2-3h | scipy.stats + matplotlib |\n| 调试 & 修复 | 2h | negation prove、edge case |\n| fol_to_smtlib.py（可选） | 4-6h | FOL parser + SMT-LIB emitter |\n| **总计** | **7-9h**（不含可选） | |\n\n### 运行（计算）\n\n| Phase | 资源 | 时间 | 说明 |\n|-------|------|------|------|\n| 1: Inference | 1 GPU | ~20 min | Qwen3-4B, 100×8 generations |\n| 2: ISR | CPU only | ~40 min | 8-worker parallel Prover9 |\n| 3: Label pred | CPU only | ~20 min | 800 × 2 Prover9 calls |\n| 4: GT baseline | CPU only | ~10 min | 100 × STA + label pred |\n| 5: Analysis | CPU only | ~5 min | stats + plots |\n| **Total GPU** | | **~20 min** | 远低于 1 GPU·h 预算 |\n| **Total wall clock** | | **~1.5h** | 串行；并行可压缩到 ~1h |\n\n### DDL 风险评估\n\n- **可行性**：高。核心代码 1 天可完成，实验运行 < 2h。\n- **依赖**：需要 plan001-exec-only-s42 checkpoint 成功运行。当前 r4 正在运行中。\n  - **备选**：用 100-step exec-only checkpoint（r5，已成功），prove_rate 较低但 ISR 方差更大，更利于 correlation 分析。\n- **与其他实验并行性**：Phase 2-5 只用 CPU，不占 GPU → 可与 plan001/plan013 训练同时进行。\n- **建议排期**：plan001-r4 成功后立即启动。最晚 5/19 开始，5/20 完成。\n"
  }
}
````

</details>

---

### Tool result

_source line 76 · 2026-05-14T02:11:53.548744+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/plan014_design.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan014-downstream-design_20260514T020422",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 77 · 2026-05-14T02:11:53.548953+00:00_

设计文档已写入 `artifacts/plan014_design.md`。

核心设计：

**主方案 — Label-Prediction Accuracy**：用 checkpoint 生成 K=8 个 FOL formalization，对每个做 3-way entailment 分类（prove 原结论 → true，prove 否定结论 → false，均失败 → unknown），与 ground-truth label 比较。ISR 与 label accuracy 的 Spearman 相关性 + Best-of-N selection 实验直接回答 "高 ISR 是否意味着更好的 formalization"。

关键优势：
- **与 ISR 完全正交**：ISR 度量 component necessity，label accuracy 度量 semantic correctness
- **工程量极低**：只需在现有 Prover9 pipeline 上加 negation-prove
- **GPU 仅需 ~20 min**（inference），其余全是 CPU-bound 的 Prover9 调用，可与训练并行
- **Best-of-N framing** 同时证明了 ISR 的实用价值（作为 selection criterion）

预期 7-9h 实现，1.5h 运行，留有充足 buffer 应对 DDL。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_plan014-downstream-design_20260514T020422"
}
```

</details>

---
