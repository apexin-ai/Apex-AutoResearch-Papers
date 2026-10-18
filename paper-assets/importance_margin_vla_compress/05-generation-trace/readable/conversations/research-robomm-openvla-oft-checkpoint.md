# research robomm openvla oft checkpoint

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_research_robomm-openvla-oft-checkpoint_20260520T053545.jsonl`
- **Structured JSON:** [`ff7eaab60cd51f50d6aa.json`](../../sessions/ff/ff7eaab60cd51f50d6aa.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-20T05:40:30.512466+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "RoboMM LIBERO checkpoint research",
  "subagent_type": "general-purpose",
  "prompt": "Research the RoboMM VLA model for LIBERO benchmark availability. Do the following searches and report findings:\n\n1. WebSearch \"RoboMM LIBERO checkpoint download\"\n2. WebSearch \"RoboMM github robot manipulation multimodal\"\n3. WebSearch \"RoboMM paper arxiv cross-attention VLA\"\n4. Check HuggingFace for any RoboMM models\n\nKey questions to answer:\n- What is RoboMM's vision connector architecture exactly? (reported as cross-attention / decoder-side fusion)\n- Does the paper report LIBERO results? Which LIBERO suites?\n- Are there pretrained/fine-tuned LIBERO checkpoints publicly available?\n- If no checkpoint, what's the training cost estimate (GPU hours, hardware requirements)?\n- GitHub repo URL and whether it includes training code for LIBERO\n- How many vision tokens does it use?\n\nReport all findings concisely with URLs.",
  "run_in_background": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_robomm-openvla-oft-checkpoint_20260520T053545",
  "tool": "Agent",
  "tool_args": {
    "description": "RoboMM LIBERO checkpoint research",
    "subagent_type": "general-purpose",
    "prompt": "Research the RoboMM VLA model for LIBERO benchmark availability. Do the following searches and report findings:\n\n1. WebSearch \"RoboMM LIBERO checkpoint download\"\n2. WebSearch \"RoboMM github robot manipulation multimodal\"\n3. WebSearch \"RoboMM paper arxiv cross-attention VLA\"\n4. Check HuggingFace for any RoboMM models\n\nKey questions to answer:\n- What is RoboMM's vision connector architecture exactly? (reported as cross-attention / decoder-side fusion)\n- Does the paper report LIBERO results? Which LIBERO suites?\n- Are there pretrained/fine-tuned LIBERO checkpoints publicly available?\n- If no checkpoint, what's the training cost estimate (GPU hours, hardware requirements)?\n- GitHub repo URL and whether it includes training code for LIBERO\n- How many vision tokens does it use?\n\nReport all findings concisely with URLs.",
    "run_in_background": "True"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T05:40:30.512841+00:00_

Async agent launched successfully.
agentId: a92c8053bda6b8f41 (internal ID - do not mention to user. Use SendMessage with to: 'a92c8053bda6b8f41' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/e5fd1477-16f4-46f0-88e4-4469422a31cc/tasks/a92c8053bda6b8f41.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_robomm-openvla-oft-checkpoint_20260520T053545",
  "tool": "Agent",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T05:40:30.513045+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "OpenVLA-OFT checkpoint research",
  "subagent_type": "general-purpose",
  "prompt": "Research the OpenVLA-OFT model for LIBERO benchmark availability. Do the following searches and report findings:\n\n1. WebSearch \"OpenVLA-OFT checkpoint download\"\n2. WebSearch \"OpenVLA-OFT github flow matching action\"\n3. WebSearch \"OpenVLA-OFT paper arxiv\"\n4. Check HuggingFace for any OpenVLA-OFT models (search \"openvla-oft\")\n\nKey questions to answer:\n- Confirm: does OpenVLA-OFT use the same 2-layer MLP vision connector as the original OpenVLA?\n- What's different about OpenVLA-OFT? (flow matching action head?)\n- Does the paper report LIBERO results? Which LIBERO suites?\n- Are there pretrained/fine-tuned LIBERO checkpoints publicly available?\n- If the connector is identical to OpenVLA, the pruning behavior of vision tokens should theoretically be the same. The main value would be isolating the action head's effect on compression. Confirm or refute this reasoning.\n- GitHub repo URL\n- How many vision tokens does it use?\n\nReport all findings concisely with URLs.",
  "run_in_background": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_robomm-openvla-oft-checkpoint_20260520T053545",
  "tool": "Agent",
  "tool_args": {
    "description": "OpenVLA-OFT checkpoint research",
    "subagent_type": "general-purpose",
    "prompt": "Research the OpenVLA-OFT model for LIBERO benchmark availability. Do the following searches and report findings:\n\n1. WebSearch \"OpenVLA-OFT checkpoint download\"\n2. WebSearch \"OpenVLA-OFT github flow matching action\"\n3. WebSearch \"OpenVLA-OFT paper arxiv\"\n4. Check HuggingFace for any OpenVLA-OFT models (search \"openvla-oft\")\n\nKey questions to answer:\n- Confirm: does OpenVLA-OFT use the same 2-layer MLP vision connector as the original OpenVLA?\n- What's different about OpenVLA-OFT? (flow matching action head?)\n- Does the paper report LIBERO results? Which LIBERO suites?\n- Are there pretrained/fine-tuned LIBERO checkpoints publicly available?\n- If the connector is identical to OpenVLA, the pruning behavior of vision tokens should theoretically be the same. The main value would be isolating the action head's effect on compression. Confirm or refute this reasoning.\n- GitHub repo URL\n- How many vision tokens does it use?\n\nReport all findings concisely with URLs.",
    "run_in_background": "True"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T05:40:30.513290+00:00_

Async agent launched successfully.
agentId: abf2bbc209fbf884b (internal ID - do not mention to user. Use SendMessage with to: 'abf2bbc209fbf884b' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/e5fd1477-16f4-46f0-88e4-4469422a31cc/tasks/abf2bbc209fbf884b.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_robomm-openvla-oft-checkpoint_20260520T053545",
  "tool": "Agent",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T05:40:30.513473+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "DeeR-VLA checkpoint research",
  "subagent_type": "general-purpose",
  "prompt": "Research the DeeR-VLA model for LIBERO benchmark availability. Do the following searches and report findings:\n\n1. WebSearch \"DeeR-VLA LIBERO checkpoint\"\n2. WebSearch \"DeeR-VLA github Perceiver Resampler\"\n3. WebSearch \"DeeR-VLA paper arxiv\"\n4. Check HuggingFace for any DeeR-VLA models\n\nKey questions to answer:\n- What is DeeR-VLA's vision connector? (reported as Perceiver Resampler)\n- Does the paper report LIBERO results? Which LIBERO suites?\n- Are there pretrained/fine-tuned LIBERO checkpoints publicly available?\n- GitHub repo URL and whether it includes training code\n- How many vision tokens does it output (after resampling)?\n- Training cost if we need to train from scratch\n\nReport all findings concisely with URLs.",
  "run_in_background": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_robomm-openvla-oft-checkpoint_20260520T053545",
  "tool": "Agent",
  "tool_args": {
    "description": "DeeR-VLA checkpoint research",
    "subagent_type": "general-purpose",
    "prompt": "Research the DeeR-VLA model for LIBERO benchmark availability. Do the following searches and report findings:\n\n1. WebSearch \"DeeR-VLA LIBERO checkpoint\"\n2. WebSearch \"DeeR-VLA github Perceiver Resampler\"\n3. WebSearch \"DeeR-VLA paper arxiv\"\n4. Check HuggingFace for any DeeR-VLA models\n\nKey questions to answer:\n- What is DeeR-VLA's vision connector? (reported as Perceiver Resampler)\n- Does the paper report LIBERO results? Which LIBERO suites?\n- Are there pretrained/fine-tuned LIBERO checkpoints publicly available?\n- GitHub repo URL and whether it includes training code\n- How many vision tokens does it output (after resampling)?\n- Training cost if we need to train from scratch\n\nReport all findings concisely with URLs.",
    "run_in_background": "True"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T05:40:30.513633+00:00_

Async agent launched successfully.
agentId: af5fc4b32e1a808ab (internal ID - do not mention to user. Use SendMessage with to: 'af5fc4b32e1a808ab' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/e5fd1477-16f4-46f0-88e4-4469422a31cc/tasks/af5fc4b32e1a808ab.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_robomm-openvla-oft-checkpoint_20260520T053545",
  "tool": "Agent",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T05:40:30.513842+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "π0 checkpoint research",
  "subagent_type": "general-purpose",
  "prompt": "Research the π0 (pi-zero, pi0) VLA model for LIBERO benchmark availability. Do the following searches and report findings:\n\n1. WebSearch \"pi0 VLA model LIBERO checkpoint\"\n2. WebSearch \"pi0 robot policy 3.3B SigLIP open weights\"\n3. WebSearch \"pi0 github physical intelligence\"\n4. WebSearch \"pi0 huggingface model download\"\n5. Check HuggingFace for pi0 models\n\nKey questions to answer:\n- Does π0 use SigLIP as vision encoder? How many vision tokens does SigLIP output?\n- What is π0's vision connector type? (reported as linear projection)\n- Does the paper report LIBERO results?\n- Are there open-source weights available? Where to download?\n- Are there LIBERO fine-tuned checkpoints specifically?\n- Model size (reported as 3.3B) — confirm\n- Training cost if we need to fine-tune on LIBERO from scratch\n\nAlso search for \"π0 open source release\" or \"Physical Intelligence pi0 weights\" to check the latest status of weight availability.\n\nReport all findings concisely with URLs.",
  "run_in_background": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_robomm-openvla-oft-checkpoint_20260520T053545",
  "tool": "Agent",
  "tool_args": {
    "description": "π0 checkpoint research",
    "subagent_type": "general-purpose",
    "prompt": "Research the π0 (pi-zero, pi0) VLA model for LIBERO benchmark availability. Do the following searches and report findings:\n\n1. WebSearch \"pi0 VLA model LIBERO checkpoint\"\n2. WebSearch \"pi0 robot policy 3.3B SigLIP open weights\"\n3. WebSearch \"pi0 github physical intelligence\"\n4. WebSearch \"pi0 huggingface model download\"\n5. Check HuggingFace for pi0 models\n\nKey questions to answer:\n- Does π0 use SigLIP as vision encoder? How many vision tokens does SigLIP output?\n- What is π0's vision connector type? (reported as linear projection)\n- Does the paper report LIBERO results?\n- Are there open-source weights available? Where to download?\n- Are there LIBERO fine-tuned checkpoints specifically?\n- Model size (reported as 3.3B) — confirm\n- Training cost if we need to fine-tune on LIBERO from scratch\n\nAlso search for \"π0 open source release\" or \"Physical Intelligence pi0 weights\" to check the latest status of weight availability.\n\nReport all findings concisely with URLs.",
    "run_in_background": "True"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T05:40:30.514016+00:00_

Async agent launched successfully.
agentId: a4263a7173cf3b2e5 (internal ID - do not mention to user. Use SendMessage with to: 'a4263a7173cf3b2e5' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/e5fd1477-16f4-46f0-88e4-4469422a31cc/tasks/a4263a7173cf3b2e5.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_robomm-openvla-oft-checkpoint_20260520T053545",
  "tool": "Agent",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T05:40:30.514289+00:00_

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
  "session": "worker_research_robomm-openvla-oft-checkpoint_20260520T053545",
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

_source line 10 · 2026-05-20T05:40:30.514444+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_robomm-openvla-oft-checkpoint_20260520T053545",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T05:40:30.514618+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "file": "ROADMAP.md",
  "max_chars": "6000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_robomm-openvla-oft-checkpoint_20260520T053545",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "importance_margin_vla_compress",
    "file": "ROADMAP.md",
    "max_chars": "6000"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T05:40:30.514822+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/ROADMAP.md\", \"content\": \"# importance_margin_vla_compress — Research Dashboard\\n\\n> 最后更新: 2026-05-19 23:23 UTC | 更新原因: C4-ext 10K gate MARGINAL (D094), M-sweep deferred to 20K, cqa1 evals submitted\\n\\n## 核心方向\\n**Analysis + Method paper** (D091): Vision connector 架构决定 VLA token 可压缩性。提出 VTR (Vision Token Re-encoding)。详见 paper_framing.md。\\n\\n## 当前阶段\\n🔬 Research + 📝 审稿进行中 | 目标: **CoRL 2026** (abstract May 26, paper May 29)\\n- Paper identity: Round 3 — analysis + method\\n- **C4-ext 10K gate: MARGINAL (D094)** — loss avg 3.01, 趋势下降无 plateau, 继续到 50K\\n- **20K checkpoint**: ~May 20 13:00 UTC → loss < 2.5 则启动 M-sweep\\n- **50K eval gate**: ~May 20 18:00 UTC → SR > 37.4% 则 method paper 确认\\n\\n## Claims 完成度\\n| Claim | 状态 | 关键数据 |\\n|-------|------|---------|\\n| C1: Architecture-Dependent Compressibility | ✅ | SmolVLA 0% vs OpenVLA 37.4% @ k=0.5 |\\n| C2: Pixel Shuffle Entanglement | ✅ | 22 experiments, ALL 0%, k=0.95→0% |\\n| C3: MLP Projector Graceful Degradation | ✅ | 6-point curve 74→20.6%, 全部已注册 |\\n| C4: Learned Re-encoding (SmolVLA) | ✅* | VTC 60.1±1.3%, MLP 63.4±2.6%, cross-suite confirmed |\\n| **C4-ext: Method Universality (OpenVLA)** | 🟡 | 10K gate marginal, 继续到 50K eval |\\n| **C5: 3rd Connector (RoboFlamingo)** | 🟡 | Bug 修复 (M029), v2 重训中, grip_loss 已开始下降 |\\n\\n*C4 pending: m128_seed43 eval running, m16_seed43 eval running, m16_seed44_v3 training ~85K\\n\\n## ⚠️ 活跃问题\\n1. **C4-ext marginal**: 10K avg loss 3.01, 需 20K 确认收敛\\n2. **3 台 96GB GPU 待命**: westd-41074:2-3 + westd-27271:1 等 20K gate (~14h)\\n3. **M029 blast radius**: ✅ 已确认仅影响 C5，SmolVLA/OpenVLA 安全\\n\\n## 论文写作\\n- ✅ Introduction reframe, §3.3/§3.4 patches\\n- 🔄 Architecture figure 制作中 (Paper Agent)\\n- ⏳ §4.3 命名升级 + OpenVLA 结果 → 待 C4-ext 50K eval\\n\\n## 运行中\\n| exp_id | 服务器:GPU | 进度 | 备注 |\\n|--------|-----------|------|------|\\n| train_openvla_
…[truncated 2691 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_robomm-openvla-oft-checkpoint_20260520T053545",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T05:40:30.515044+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "artifacts/vla_model_survey*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_robomm-openvla-oft-checkpoint_20260520T053545",
  "tool": "Glob",
  "tool_args": {
    "pattern": "artifacts/vla_model_survey*",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T05:40:30.515210+00:00_

artifacts/vla_model_survey.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_robomm-openvla-oft-checkpoint_20260520T053545",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T05:40:30.515384+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/vla_model_survey.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_robomm-openvla-oft-checkpoint_20260520T053545",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/vla_model_survey.md"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T05:40:30.515663+00:00_

1	# VLA 模型全面调研报告
2	
3	> 调研日期：2026-05-20（更新版）
4	> 目标：为论文 "Vision Connectors and VLA Token Compressibility" 寻找更多不同 connector 架构的 VLA 模型
5	
6	## 已有实验数据
7	
8	| 模型 | Connector 类型 | 压缩行为 |
9	|------|---------------|----------|
10	| SmolVLA | Pixel-shuffle + MLP | Cliff-edge collapse (k=0.95 → 0% SR) |
11	| OpenVLA | 2-layer MLP projector (Prismatic) | Graded degradation (线性下降) |
12	| RoboFlamingo | Perceiver Resampler + Cross-attention | 训练失败（gripper loss 无法收敛） |
13	
14	---
15	
16	## 完整模型调研表
17	
18	### 1. Octo (UC Berkeley, 2024)
19	
20	| 字段 | 信息 |
21	|------|------|
22	| 参数量 | 27M (Small) / 93M (Base) |
23	| Vision encoder | Shallow CNN（从头训练，非预训练 ViT） |
24	| **Connector** | **CNN patch encoder → 直接拼接** — 无独立 connector，image patches (16×16) 直接拼入 transformer 序列 |
25	| LLM backbone | 纯 transformer（非预训练 LLM），语言用 T5 encoder |
26	| 开源 | ✅ GitHub: [octo-models/octo](https://github.com/octo-models/octo), HF: rail-berkeley/octo-base |
27	| LIBERO | ✅ fine-tune 后 ~72% SR |
28	| 改造成本 | 低 |
29	| 备注 | 非标准 VLM→LLM 架构，是 transformer-based diffusion policy。Action head 是 diffusion policy。 |
30	
31	### 2. CogACT (Microsoft/Tsinghua, 2024)
32	
33	| 字段 | 信息 |
34	|------|------|
35	| 参数量 | ~7.1B (7B Prismatic + 89-300M DiT action module) |
36	| Vision encoder | DINOv2 + SigLIP (双 encoder，channel concat) |
37	| **Connector** | **2-layer MLP projector** — 与 OpenVLA 相同（Prismatic 架构） |
38	| LLM backbone | Llama-2 7B (via Prismatic-7B) |
39	| 开源 | ✅ GitHub: [microsoft/CogACT](https://github.com/microsoft/CogACT), HF: CogACT/CogACT-Base |
40	| LIBERO | 需改造（paper 用 SimplerEnv + 真机） |
41	| 改造成本 | 中 |
42	| 备注 | 创新在 DiT action module。Connector 与 OpenVLA 相同。 |
43	
44	### 3. HPT (MIT, NeurIPS 2024)
45	
46	| 字段 | 信息 |
47	|------|------|
48	| 参数量 | 3.1M–1.1B (5 个 size) |
49	| Vision encoder | 预训练冻结 ResNet18 |
50	| **Connector** | **Cross-attention tokenizer** — learnable tokens 通过 cross-attention (8 heads) 聚合 vision features → 固定 16 tokens，每 camera view 独立 MLP projector |
51	| LLM backbone | 无（decoder-only
…[truncated 10820 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_robomm-openvla-oft-checkpoint_20260520T053545",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-20T05:40:30.516371+00:00_

4 个 agent 全部完成。汇总结果：

---

## 调研结果汇总

| 模型 | Connector 类型 | LIBERO checkpoint | 下载链接 | Vision tokens | 备注 |
|------|---------------|-------------------|----------|--------------|------|
| **RoboMM** | Cross-attention (OpenFlamingo) + UVFormer | **❌ 无** | GitHub有代码无权重 | ~64 (Perceiver 标准) | 权重标记为 TODO 未发布。训练成本 32×A100 130h（全数据集），LIBERO-only 未知 |
| **OpenVLA-OFT** | **3-layer MLP** (与 OpenVLA 相同) | **✅ 4个suite全有** | [HF: moojink/openvla-7b-oft-finetuned-libero-*](https://huggingface.co/moojink) | 256 | Action head 是 L1 regression + parallel decoding（非 flow matching）。97.1% avg SR |
| **DeeR-VLA** | Perceiver Resampler + Cross-attention | **❌ 无** (只有 CALVIN) | [HF: Yang130/DeeR-VLA](https://huggingface.co/Yang130/DeeR-VLA) (CALVIN only) | 64 | 需从零训练 LIBERO，8×V100 ~14-25h |
| **π0** | Linear projection | **✅ 有** | [HF: lerobot/pi0_libero_base](https://huggingface.co/lerobot/pi0_libero_base) | 256 (@224×224) | avg ~65% SR，社区复现有困难 |

---

## 综合建议

**立即可用（有 LIBERO checkpoint，零训练成本）：**

1. **OpenVLA-OFT** — 最容易集成。Connector 与 OpenVLA 完全相同（3-layer MLP），价值在于隔离 action head 对压缩行为的影响。如果 pruning 曲线与 OpenVLA 一致 → 证明压缩性由 connector 决定，与 action head 无关。如果不同 → 有趣的发现。**推荐优先跑。**

2. **π0** — Linear projection connector，与 MLP projector 形成直接对比。已有 LIBERO checkpoint，但性能较低（65%）且社区复现不稳定。256 vision tokens 与 OpenVLA 相同，便于直接比较。**推荐第二个跑。**

**需从零训练（成本较高）：**

3. **DeeR-VLA** — Perceiver Resampler，64 tokens。给 RoboFlamingo 失败的 connector 类型第二次机会。但需自行适配 LIBERO pipeline，8×V100 ~14-25h。**中等优先。**

4. **RoboMM** — Cross-attention，最独特的 connector 类型。但权重未发布、训练成本高（32×A100 全数据集）、LIBERO-only 训练流程未文档化。**暂不推荐，等权重发布。**

---

**修正一个信息**：之前调研报告中 OpenVLA 的 projector 标记为 "2-layer MLP"，OpenVLA-OFT 调研确认实际是 **3-layer MLP with GELU**。需在后续引用中统一。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_robomm-openvla-oft-checkpoint_20260520T053545"
}
```

</details>

---
