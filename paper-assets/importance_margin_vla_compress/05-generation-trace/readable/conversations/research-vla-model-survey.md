# research vla model survey

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_research_vla_model_survey_20260523T062811.jsonl`
- **Structured JSON:** [`f36d654dd5908f21ec6a.json`](../../sessions/f3/f36d654dd5908f21ec6a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-23T06:32:59.110077+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_model_survey_20260523T062811",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T06:32:59.110462+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_model_survey_20260523T062811",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T06:32:59.110671+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Research Octo VLA model",
  "prompt": "Research the \"Octo\" VLA (Vision-Language-Action) model for robotics. I need to know:\n\n1. GitHub repo URL\n2. Whether it has LIBERO benchmark checkpoints (pre-trained checkpoints fine-tuned on LIBERO tasks)\n3. Vision connector type (how it processes visual tokens — linear projection, MLP, attention, cross-attention, pixel-shuffle, etc.)\n4. Parameter count\n5. Number of vision tokens fed to the backbone\n6. Architecture: does it have a clear separation between vision encoder → connector → language/action backbone? Or is it end-to-end diffusion without explicit token representations?\n7. Whether post-connector token pruning would be feasible (i.e., can you intervene between the vision connector output and the action prediction backbone?)\n\nUse WebSearch with queries like:\n- \"Octo robot model GitHub LIBERO\"\n- \"Octo VLA architecture vision connector\"\n- \"Octo model checkpoint LIBERO benchmark\"\n- \"Octo diffusion policy architecture\"\n\nReport all findings concisely. Include URLs.",
  "subagent_type": "general-purpose",
  "run_in_background": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_model_survey_20260523T062811",
  "tool": "Agent",
  "tool_args": {
    "description": "Research Octo VLA model",
    "prompt": "Research the \"Octo\" VLA (Vision-Language-Action) model for robotics. I need to know:\n\n1. GitHub repo URL\n2. Whether it has LIBERO benchmark checkpoints (pre-trained checkpoints fine-tuned on LIBERO tasks)\n3. Vision connector type (how it processes visual tokens — linear projection, MLP, attention, cross-attention, pixel-shuffle, etc.)\n4. Parameter count\n5. Number of vision tokens fed to the backbone\n6. Architecture: does it have a clear separation between vision encoder → connector → language/action backbone? Or is it end-to-end diffusion without explicit token representations?\n7. Whether post-connector token pruning would be feasible (i.e., can you intervene between the vision connector output and the action prediction backbone?)\n\nUse WebSearch with queries like:\n- \"Octo robot model GitHub LIBERO\"\n- \"Octo VLA architecture vision connector\"\n- \"Octo model checkpoint LIBERO benchmark\"\n- \"Octo diffusion policy architecture\"\n\nReport all findings concisely. Include URLs.",
    "subagent_type": "general-purpose",
    "run_in_background": "True"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T06:32:59.110865+00:00_

Async agent launched successfully.
agentId: ac217f79d5c12c3ab (internal ID - do not mention to user. Use SendMessage with to: 'ac217f79d5c12c3ab' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/0b478ffa-1a46-4507-8db6-147a1db4f3af/tasks/ac217f79d5c12c3ab.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_model_survey_20260523T062811",
  "tool": "Agent",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T06:32:59.111023+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Research CogACT VLA model",
  "prompt": "Research the \"CogACT\" VLA (Vision-Language-Action) model for robotics. I need to know:\n\n1. GitHub repo URL\n2. Whether it has LIBERO benchmark checkpoints or evaluation results on LIBERO\n3. Vision connector type (how it processes visual tokens — linear projection, MLP, attention, cross-attention, pixel-shuffle, etc.)\n4. Parameter count\n5. Number of vision tokens\n6. Architecture: does it have a clear separation between vision encoder → connector → LLM backbone? Can you intervene between connector output and backbone input for token pruning?\n7. Whether it has publicly available checkpoints\n\nUse WebSearch with queries like:\n- \"CogACT VLA model GitHub\"\n- \"CogACT robot model LIBERO checkpoint\"\n- \"CogACT vision language action architecture\"\n\nReport all findings concisely. Include URLs.",
  "subagent_type": "general-purpose",
  "run_in_background": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_model_survey_20260523T062811",
  "tool": "Agent",
  "tool_args": {
    "description": "Research CogACT VLA model",
    "prompt": "Research the \"CogACT\" VLA (Vision-Language-Action) model for robotics. I need to know:\n\n1. GitHub repo URL\n2. Whether it has LIBERO benchmark checkpoints or evaluation results on LIBERO\n3. Vision connector type (how it processes visual tokens — linear projection, MLP, attention, cross-attention, pixel-shuffle, etc.)\n4. Parameter count\n5. Number of vision tokens\n6. Architecture: does it have a clear separation between vision encoder → connector → LLM backbone? Can you intervene between connector output and backbone input for token pruning?\n7. Whether it has publicly available checkpoints\n\nUse WebSearch with queries like:\n- \"CogACT VLA model GitHub\"\n- \"CogACT robot model LIBERO checkpoint\"\n- \"CogACT vision language action architecture\"\n\nReport all findings concisely. Include URLs.",
    "subagent_type": "general-purpose",
    "run_in_background": "True"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T06:32:59.111214+00:00_

Async agent launched successfully.
agentId: aab6194641a7af522 (internal ID - do not mention to user. Use SendMessage with to: 'aab6194641a7af522' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/0b478ffa-1a46-4507-8db6-147a1db4f3af/tasks/aab6194641a7af522.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_model_survey_20260523T062811",
  "tool": "Agent",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T06:32:59.111384+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Research RoboFlamingo VLA model",
  "prompt": "Research the \"RoboFlamingo\" VLA (Vision-Language-Action) model for robotics. I need to know:\n\n1. GitHub repo URL\n2. Whether it has LIBERO benchmark checkpoints (pre-trained, fine-tuned on LIBERO)\n3. Vision connector type (Flamingo uses cross-attention / perceiver resampler — confirm the specific type)\n4. Parameter count\n5. Number of vision tokens (perceiver resampler output tokens)\n6. Architecture: does it have a clear separation where you can intervene between vision token output and LLM backbone input for token pruning?\n7. Whether it has publicly available checkpoints\n\nUse WebSearch with queries like:\n- \"RoboFlamingo GitHub LIBERO\"\n- \"RoboFlamingo checkpoint model\"\n- \"RoboFlamingo architecture vision connector\"\n- \"RoboFlamingo LIBERO benchmark results\"\n\nReport all findings concisely. Include URLs.",
  "subagent_type": "general-purpose",
  "run_in_background": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_model_survey_20260523T062811",
  "tool": "Agent",
  "tool_args": {
    "description": "Research RoboFlamingo VLA model",
    "prompt": "Research the \"RoboFlamingo\" VLA (Vision-Language-Action) model for robotics. I need to know:\n\n1. GitHub repo URL\n2. Whether it has LIBERO benchmark checkpoints (pre-trained, fine-tuned on LIBERO)\n3. Vision connector type (Flamingo uses cross-attention / perceiver resampler — confirm the specific type)\n4. Parameter count\n5. Number of vision tokens (perceiver resampler output tokens)\n6. Architecture: does it have a clear separation where you can intervene between vision token output and LLM backbone input for token pruning?\n7. Whether it has publicly available checkpoints\n\nUse WebSearch with queries like:\n- \"RoboFlamingo GitHub LIBERO\"\n- \"RoboFlamingo checkpoint model\"\n- \"RoboFlamingo architecture vision connector\"\n- \"RoboFlamingo LIBERO benchmark results\"\n\nReport all findings concisely. Include URLs.",
    "subagent_type": "general-purpose",
    "run_in_background": "True"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T06:32:59.111543+00:00_

Async agent launched successfully.
agentId: a885f30b0c2ca4f6f (internal ID - do not mention to user. Use SendMessage with to: 'a885f30b0c2ca4f6f' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/0b478ffa-1a46-4507-8db6-147a1db4f3af/tasks/a885f30b0c2ca4f6f.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_model_survey_20260523T062811",
  "tool": "Agent",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T06:32:59.111682+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Research HPT model",
  "prompt": "Research \"HPT\" (Heterogeneous Pretrained Transformers) for robotics. I need to know:\n\n1. GitHub repo URL\n2. Whether it supports LIBERO benchmark or has LIBERO checkpoints\n3. Vision connector type (how it processes visual inputs)\n4. Parameter count\n5. Number of vision tokens\n6. Architecture: does it have a clear vision encoder → connector → backbone separation? Can you do post-connector token pruning?\n7. Whether it has publicly available checkpoints\n\nUse WebSearch with queries like:\n- \"HPT Heterogeneous Pretrained Transformers GitHub\"\n- \"HPT robot model LIBERO\"\n- \"HPT architecture vision tokens\"\n- \"Heterogeneous Pretrained Transformers checkpoint\"\n\nReport all findings concisely. Include URLs.",
  "subagent_type": "general-purpose",
  "run_in_background": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_model_survey_20260523T062811",
  "tool": "Agent",
  "tool_args": {
    "description": "Research HPT model",
    "prompt": "Research \"HPT\" (Heterogeneous Pretrained Transformers) for robotics. I need to know:\n\n1. GitHub repo URL\n2. Whether it supports LIBERO benchmark or has LIBERO checkpoints\n3. Vision connector type (how it processes visual inputs)\n4. Parameter count\n5. Number of vision tokens\n6. Architecture: does it have a clear vision encoder → connector → backbone separation? Can you do post-connector token pruning?\n7. Whether it has publicly available checkpoints\n\nUse WebSearch with queries like:\n- \"HPT Heterogeneous Pretrained Transformers GitHub\"\n- \"HPT robot model LIBERO\"\n- \"HPT architecture vision tokens\"\n- \"Heterogeneous Pretrained Transformers checkpoint\"\n\nReport all findings concisely. Include URLs.",
    "subagent_type": "general-purpose",
    "run_in_background": "True"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T06:32:59.111837+00:00_

Async agent launched successfully.
agentId: a321e4a9aef33453a (internal ID - do not mention to user. Use SendMessage with to: 'a321e4a9aef33453a' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/0b478ffa-1a46-4507-8db6-147a1db4f3af/tasks/a321e4a9aef33453a.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_model_survey_20260523T062811",
  "tool": "Agent",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T06:32:59.111976+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Research Diffusion Policy model",
  "prompt": "Research \"Diffusion Policy\" for robotics manipulation. I need to know:\n\n1. GitHub repo URL\n2. Whether it has LIBERO benchmark results or LIBERO checkpoints\n3. Vision encoder/connector type — how it processes visual inputs. Is there a vision token representation?\n4. Parameter count\n5. Architecture: Diffusion Policy is typically NOT a VLA (no language model backbone). Confirm whether it has explicit vision tokens that could be pruned, or if it's an end-to-end CNN/ViT → diffusion architecture without token-level intervention points.\n6. Whether it has publicly available checkpoints for LIBERO\n\nUse WebSearch with queries like:\n- \"Diffusion Policy LIBERO benchmark\"\n- \"Diffusion Policy GitHub checkpoint\"\n- \"Diffusion Policy architecture vision encoder\"\n- \"chi mahi diffusion policy LIBERO\"\n\nReport all findings concisely. Include URLs.",
  "subagent_type": "general-purpose",
  "run_in_background": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_model_survey_20260523T062811",
  "tool": "Agent",
  "tool_args": {
    "description": "Research Diffusion Policy model",
    "prompt": "Research \"Diffusion Policy\" for robotics manipulation. I need to know:\n\n1. GitHub repo URL\n2. Whether it has LIBERO benchmark results or LIBERO checkpoints\n3. Vision encoder/connector type — how it processes visual inputs. Is there a vision token representation?\n4. Parameter count\n5. Architecture: Diffusion Policy is typically NOT a VLA (no language model backbone). Confirm whether it has explicit vision tokens that could be pruned, or if it's an end-to-end CNN/ViT → diffusion architecture without token-level intervention points.\n6. Whether it has publicly available checkpoints for LIBERO\n\nUse WebSearch with queries like:\n- \"Diffusion Policy LIBERO benchmark\"\n- \"Diffusion Policy GitHub checkpoint\"\n- \"Diffusion Policy architecture vision encoder\"\n- \"chi mahi diffusion policy LIBERO\"\n\nReport all findings concisely. Include URLs.",
    "subagent_type": "general-purpose",
    "run_in_background": "True"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T06:32:59.112124+00:00_

Async agent launched successfully.
agentId: abe5894e8b1513170 (internal ID - do not mention to user. Use SendMessage with to: 'abe5894e8b1513170' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/0b478ffa-1a46-4507-8db6-147a1db4f3af/tasks/abe5894e8b1513170.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_model_survey_20260523T062811",
  "tool": "Agent",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T06:32:59.112348+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Search VLA LIBERO benchmark broadly",
  "prompt": "Do a broad search for VLA models that have been evaluated on the LIBERO benchmark. I'm looking for models beyond the well-known ones (OpenVLA, SmolVLA, Octo, CogACT, RoboFlamingo, HPT, Diffusion Policy). \n\nI need to find OTHER VLA models that:\n1. Have public LIBERO checkpoints or evaluation results\n2. Have a vision encoder → connector → LLM backbone architecture (important for token pruning research)\n\nUse WebSearch with these queries:\n- \"VLA LIBERO benchmark leaderboard 2024 2025\"\n- \"vision language action LIBERO evaluation results\"\n- \"LIBERO benchmark comparison VLA models\"\n- \"Papers with Code LIBERO benchmark\"\n- \"HuggingFace LIBERO VLA checkpoint\"\n- \"robot manipulation LIBERO pretrained model\"\n- \"VLA model LIBERO fine-tuned checkpoint 2025\"\n- \"LIBERO long horizon benchmark VLA\"\n\nFor each model found, report:\n- Model name\n- GitHub repo URL\n- Whether LIBERO checkpoints are available\n- Vision connector type if known\n- Parameter count if known\n- Whether it's a true VLA (with LLM backbone) or a non-LLM policy\n\nReport all findings concisely with URLs.",
  "subagent_type": "general-purpose",
  "run_in_background": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_vla_model_survey_20260523T062811",
  "tool": "Agent",
  "tool_args": {
    "description": "Search VLA LIBERO benchmark broadly",
    "prompt": "Do a broad search for VLA models that have been evaluated on the LIBERO benchmark. I'm looking for models beyond the well-known ones (OpenVLA, SmolVLA, Octo, CogACT, RoboFlamingo, HPT, Diffusion Policy). \n\nI need to find OTHER VLA models that:\n1. Have public LIBERO checkpoints or evaluation results\n2. Have a vision encoder → connector → LLM backbone architecture (important for token pruning research)\n\nUse WebSearch with these queries:\n- \"VLA LIBERO benchmark leaderboard 2024 2025\"\n- \"vision language action LIBERO evaluation results\"\n- \"LIBERO benchmark comparison VLA models\"\n- \"Papers with Code LIBERO benchmark\"\n- \"HuggingFace LIBERO VLA checkpoint\"\n- \"robot manipulation LIBERO pretrained model\"\n- \"VLA model LIBERO fine-tuned checkpoint 2025\"\n- \"LIBERO long horizon benchmark VLA\"\n\nFor each model found, report:\n- Model name\n- GitHub repo URL\n- Whether LIBERO checkpoints are available\n- Vision connector type if known\n- Parameter count if known\n- Whether it's a true VLA (with LLM backbone) or a non-LLM policy\n\nReport all findings concisely with URLs.",
    "subagent_type": "general-purpose",
    "run_in_background": "True"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T06:32:59.112543+00:00_

Async agent launched successfully.
agentId: a214b68a47983d670 (internal ID - do not mention to user. Use SendMessage with to: 'a214b68a47983d670' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/0b478ffa-1a46-4507-8db6-147a1db4f3af/tasks/a214b68a47983d670.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_vla_model_survey_20260523T062811",
  "tool": "Agent",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-23T06:32:59.113679+00:00_

全部 6 个调研 agent 已返回。以下是汇总结果。

## 调研结果

### 一、候选模型总表

| 模型 | LIBERO Checkpoint | Connector 类型 | 参数量 | Vision Token 数 | Setup 时间 | 兼容 Pruning 框架 | 推荐度 |
|------|-------------------|---------------|--------|-----------------|-----------|------------------|--------|
| **Octo** | ❌ 无，需自行 finetune | Shallow CNN (SmallStem16) | 93M | 256/cam | 高（JAX 环境 + finetune） | ⚠️ 可行但 token 是低级特征，科学价值低 | ★☆☆☆☆ |
| **CogACT** | ❌ 无官方（第三方有评估） | Fused GELU MLP | ~7B | 256 | 中（需 finetune） | ✅ 清晰的 projector→LLM 边界 | ★★★☆☆ |
| **RoboFlamingo** | ❌ 无（仅 CALVIN） | Perceiver Resampler + Gated Cross-Attn | 3B/9B | 64 | 高（需 finetune） | ⚠️ Cross-attn K/V pruning，非 prefix token | ★★☆☆☆ |
| **HPT** | ❌ 无（仅 MetaWorld） | Cross-Attention (16 queries) | 最大 1B | 16 | 高（需 finetune + 适配） | ⚠️ 仅 16 token，pruning 空间极小 | ★☆☆☆☆ |
| **Diffusion Policy** | ❌ 无官方 | ResNet-18 → 全局特征向量 | 20-40M | 0（无 token） | — | ❌ **不兼容**，无 token 表示 | ☆☆☆☆☆ |

### 二、广泛搜索发现的高价值候选

| 模型 | LIBERO Checkpoint | Connector 类型 | 参数量 | Vision Token 数 | 兼容 Pruning | 推荐度 |
|------|-------------------|---------------|--------|-----------------|-------------|--------|
| **VQ-VLA** | ✅ `VQ-VLA/openvla-7b-finetuned-libero-90` | DINOv2+SigLIP → MLP | ~7B | 256 | ✅ 与 OpenVLA 同架构 | ★★★★★ |
| **MiniVLA** | ✅ `Stanford-ILIAD/minivla-libero90-prismatic` | Fused ViT → MLP | ~1B | 256 | ✅ 标准 VLA 架构 | ★★★★★ |
| **VLA-Adapter** | ✅ `VLA-Adapter/LIBERO-Long` 等 4 suite | Prismatic → Bridge Attention | ~0.5B | 256 | ✅ 有显式 vision token | ★★★★☆ |
| **pi0/pi0.5** | ✅ `lerobot/pi05_libero_finetuned` | SigLIP → Gemma-2B | ~3.3B | ~256 | ⚠️ 非标准（Action Expert 独立解码器） | ★★★☆☆ |
| **X-VLA** | ✅ `lerobot/xvla-libero` | Soft-prompted Transformer | 未明确 | 未明确 | ⚠️ 架构非标准 | ★★★☆☆ |
| **Spatial-Forcing** | ✅ GitHub 有 checkpoint | OpenVLA + 3D alignment | ~7B | 256 | ✅ OpenVLA 基础 | ★★★★☆ |

### 三、直接竞品（token compression 方向）

| 竞品 | 方法 | 状态 |
|------|------|------|
| **LightVLA** (ICRA 2026) | Gumbel-softmax differentiable token pruning，cross-attn between visual/text tokens | GitHub: `LiAutoAD/LightVLA`，有 LIBERO checkpoint，FLOPs↓59.1%，latency↓38.2% |
| **VLA-IAP** | Training-free visual token pruning via interaction alignment | arXiv:2603.22991 |
| **Compressor-VLA** | Instruction-guided visual token compression | arXiv:2511.18950 |

### 四、详细分析

**Octo** — JAX/Flax 实现，浅层 CNN 而非 ViT，93M 小模型。Token 是低级 patch 特征，不是语义丰富的 ViT token。需要从头 finetune LIBERO。科学价值和实用价值都低，**不推荐**。

**CogACT** — 基于 Prismatic-7B（DINOv2+SigLIP+LLaMA2-7B），架构与 OpenVLA 高度相似，256 visual tokens，代码中有显式 `num_patch` 追踪。第三方已在 LIBERO 上评估（90-98%）。需自行 finetune 但架构完全兼容 pruning 框架。如果愿意花时间 finetune，是好候选。

**RoboFlamingo** — Perceiver Resampler 输出 64 token 作为 cross-attention K/V（非 prefix token）。Pruning 需要修改 cross-attn K/V 而非删除序列 token，与我们现有框架不同。无 LIBERO checkpoint。**不推荐**。

**HPT** — 仅 16 vision token，pruning 空间极小。无 LIBERO 支持。backbone 是 policy transformer 而非 LLM。**不推荐**。

**Diffusion Policy** — 根本没有 vision token，ResNet-18 输出全局特征向量做 FiLM conditioning。架构层面**完全不兼容**。

**VQ-VLA** ⭐ — 基于 OpenVLA（DINOv2+SigLIP → MLP → LLaMA2-7B），改进了 action tokenizer（Residual VQ-VAE）。HF 上有 LIBERO-90 checkpoint。与 OpenVLA 同架构，pruning 框架可直接复用。ICCV 2025。**强烈推荐**。

**MiniVLA** ⭐ — Prismatic VLM 缩小到 ~1B 参数，HF 上有 LIBERO-90 checkpoint（多个变体）。标准 vision encoder → connector → LLM 架构。参数量小意味着可以快速验证 pruning 在不同模型规模上的效果。**强烈推荐**。

**VLA-Adapter** — Qwen2.5-0.5B 做 backbone，非常轻量。有全部 4 个 LIBERO suite 的 checkpoint。Bridge Attention 模块是非标准 connector，需要确认 pruning 干预点。**推荐**。

**pi0.5** — SigLIP → Gemma-2B → 独立 Action Expert 解码器。架构非标准（action 不是 LLM 自回归输出），但 visual token 确实经过 LLM，可以在 LLM 输入前 pruning。有 LIBERO checkpoint。**值得考虑**。

### 五、最终推荐（按优先级）

增加样本量最高效的路径：

1. **VQ-VLA** — 与 OpenVLA 同架构，有 LIBERO checkpoint，pruning 框架可直接复用，setup 时间最短（~2h）
2. **MiniVLA** — 1B 参数，有 LIBERO checkpoint，提供不同模型规模的数据点
3. **VLA-Adapter** — 0.5B，有全部 4 suite checkpoint，进一步丰富规模多样性
4. **CogACT** — 7B，架构兼容，但需自行 finetune LIBERO（~1-2 天）
5. **pi0.5** — 3.3B，有 LIBERO checkpoint，但架构非标准需验证兼容性

前 3 个模型都有现成 LIBERO checkpoint 且架构兼容，加上已有的 OpenVLA 和 SmolVLA，可以把样本量从 N=4 提升到 **N=7+**。

### 六、竞品警示

**LightVLA** 是直接竞品（ICRA 2026），已经做了 differentiable token pruning 并有 LIBERO 结果。需要仔细阅读并在 related work 中讨论差异化。VLA-IAP 和 Compressor-VLA 也是同方向工作，建议尽快拉取论文确认技术路线的区分度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_vla_model_survey_20260523T062811"
}
```

</details>

---
