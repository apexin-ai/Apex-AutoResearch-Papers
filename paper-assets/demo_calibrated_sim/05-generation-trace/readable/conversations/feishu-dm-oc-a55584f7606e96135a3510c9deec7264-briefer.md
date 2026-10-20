# feishu dm oc a55584f7606e96135a3510c9deec7264 briefer

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 8
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/feishu_dm_oc_a55584f7606e96135a3510c9deec7264_briefer.jsonl`
- **Structured JSON:** [`cbd7aee53cccf5635357.json`](../../sessions/cb/cbd7aee53cccf5635357.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

8 recorded events

### User

_source line 1 · 2026-05-13T11:31:58.755197+00:00_

[飞书用户 曹晓玉 (ou_ed2f4ceeab862a8049a88352dc56181e)]: 这项目名和内容以及idea是对应的吗

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:dm:oc_a55584f7606e96135a3510c9deec7264:briefer",
  "source": "feishu:oc_a55584f7606e96135a3510c9deec7264"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-13T11:32:06.606944+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:dm:oc_a55584f7606e96135a3510c9deec7264:briefer",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-13T11:32:07.260385+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:dm:oc_a55584f7606e96135a3510c9deec7264:briefer",
  "tool": "ToolSearch",
  "elapsed_ms": 653
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-13T11:32:09.769692+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "file": "memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:dm:oc_a55584f7606e96135a3510c9deec7264:briefer",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "cost-verify-agent-rl",
    "file": "memory.md"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-13T11:32:10.370795+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/memory.md\", \"content\": \"# Memory — cost-verify-agent-rl\\n\\n## 教训\\n\\n### [2026-05-12] 禁止 cherry-picking eval 结果\\ndpo-001 eval 跑了 ≥5 次，completion 分别为 25%/20%/10%/30%/未完成。Reviewer 发现后要求全部记录。\\n**规则：所有 eval run 结果必须完整记录到 registry，报告 mean ± 所有单次值。不能只选最好的一次。**\\n\\n### [2026-05-12] tokenizer mismatch 导致 DPO 训练无效\\ndpo-001 使用 v1 数据（raw text 格式），48% 的 DPO pairs 存在 tokenizer mismatch。训练 loss 仅比随机低 0.012，accuracy=0.5（随机水平）。\\n**教训：DPO 数据必须用 chat template 格式构造（v2 脚本），否则 tokenizer 对齐问题会让训练完全无效。**\\n\\n### [2026-05-12] TRL 1.4.0 + Qwen2.5 根因：add_generation_prompt 硬编码\\nTRL DPOTrainer 对 conversational 数据硬编码 `add_generation_prompt=True`，追加 `<|im_start|>assistant\\\\n` 到 prompt_ids。当 chosen/rejected 是 user 角色时导致 100% mismatch。已知 issue TRL #5213，无修复版本。\\n**修复**：数据预处理用 `apply_chat_template()` 转纯文本 → DPOTrainer 走文本路径 → 0 mismatch。同时设 `padding_side=\\\"right\\\"`。脚本：`train_dpo_v3.py`。\\n\\n### [2026-05-12] BCP prompt 三个失败机制\\nmvp-004 (n=19/20) 验证 BCP 路线失败：(1) 全局行为抑制——completion 崩溃至 10-26%；(2) 跨维度干扰——校准一个维度破坏其他维度；(3) 过校正反弹——overcorrected variant politeness 反升至 60.5%。\\n\\n### [2026-05-13] vLLM LoRA 动态加载严重低估 completion\\ndiag-lora-merge 实验证明 vLLM LoRA serving 存在 bug：同一个 DPO-003 adapter，LoRA 动态加载 completion=15%，merge_and_unload 后 completion=60%（4 倍差距）。Base model 无 DPO 为 40%。\\n**规则：H-gate eval 必须用 merged 模型（PEFT merge_and_unload），不要用 vLLM LoRA 动态加载。**\\n\\n### [2026-05-13] Mistral-7B 无法在 16-tool 场景做 function calling\\nmistral-bcp-001 实验发现 Mistral-7B-Instruct-v0.3 通过 vLLM 无法在 tau-bench retail 环境（16 tools）下生成 structured tool_calls。\\n- 1 tool 时正常，16 tools 时 tool_calls 返回空列表\\n**教训：跨模型对比实验前必须先验证基础能力（tool calling、instruction following）。**\\n\\n### [2026-05-13] AWQ 量化破坏 Qwen2.5 的 tool-call special token\\nQwen2.5-14B-Instruct-AWQ（4-bit 量化）通过 vLLM 部署时，`&lt;tool_call>` special token (ID 151657) 被映射到泰语字符 \\\"คณะกรรม\\\" (token 139738)。导致 tool calling 完全失效。\\n**
…[truncated 932 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:dm:oc_a55584f7606e96135a3510c9deec7264:briefer",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 601
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-13T11:32:10.371141+00:00_

called mcp__agent-ml-research__read_roadmap

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap</summary>

```json
{
  "project": "cost-verify-agent-rl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:dm:oc_a55584f7606e96135a3510c9deec7264:briefer",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "cost-verify-agent-rl"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-13T11:32:10.998531+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/ROADMAP.md\", \"content\": \"# cost-verify-agent-rl — Research Dashboard\\n\\n> 最后更新: 2026-05-13 08:17 UTC | 更新原因: D012 Option C 执行中：Qwen14B 下载 + 论文骨架 + framing 修正完成\\n\\n## 核心方向\\nDemoCalib: BCP/DPO 行为校准失败机制 taxonomy + alignment non-compositionality 发现。\\n\\n## 当前进展\\n- 阶段：**MVP 验证** — D012 Option C（Qwen14B 跨 scale 验证）执行中\\n- 目标投稿：EMNLP 2026 Findings（ARR deadline 2026-05-25，剩余 12 天）\\n- **Plan A（DPO 方法论文）：FAIL（D011）** — H2+H3 双 FAIL，DPO+BCP 反转效应\\n- **Plan B multi-model：FAIL（D012）** — Mistral 0%, Llama 5%，7B 模型 tool-calling 能力不足\\n- **Option C：进行中** — Qwen2.5-14B-AWQ 下载中，验证 BCP 失败机制是否 scale-dependent\\n- 核心发现：\\\"alignment non-compositionality\\\" — DPO 和 BCP 各自有效但组合反转\\n\\n## 论文 Framing（已定稿，Reviewer PASS）\\n- **C1**：BCP 失败机制 taxonomy（FM1 全局抑制, FM2 跨维度干扰, FM3 过校正反弹）— evidence: Moderate\\n- **C2**：FM4 DPO+BCP 反转效应（\\\"alignment non-compositionality\\\"）— evidence: Strong (4 runs, 10/12 checks)\\n- **C3**：跨 scale 验证 — PENDING（14B 结果）\\n- **C4**：implications for compositional alignment\\n\\n## 决策树（D012 分支）\\n```\\nQwen14B BCP eval\\n├── completion >20% + BCP 效应可测\\n│   ├── FM1+FM2+FM3 全复现 → 8 页全文（est. 45-55% 接受率）\\n│   ├── 部分复现 → 8 页（hedge 未复现 FM）\\n│   └── 模式不同 → \\\"scale-dependent failure boundary\\\"（同样可发表）\\n└── completion ≤20%\\n    └── 降级 Narrative 1：Qwen-only 4 页短论文（est. 30-40%）\\n```\\n\\n## 并行执行线\\n| 线路 | GPU | 状态 | 预计完成 |\\n|------|-----|------|----------|\\n| Qwen14B-AWQ 下载 | CPU | 下载中 | ~30min |\\n| Qwen14B tool-calling 验证 | cuda:2 | 待下载完成 | +30min |\\n| Qwen14B BCP eval (如验证通过) | cuda:2+3 | 待验证 | +3-4h |\\n| Method+Experiments 骨架 | CPU | 写作中 | ~1h |\\n| paper_framing.md | — | ✅ 5 点修正完成，Reviewer PASS | — |\\n\\n## GPU 预算\\n- 当前：2× RTX 4090D（cuda:2, cuda:3），MVP 后迁移独享服务器\\n- 14B eval ~4h → 今天内出 Plan B 最终判定\\n- 剩余 12 天：eval 1 天 + framing 1 天 + 写作 5-7 天 + revision 2-3 天 = 勉强可行\\n\\n## 近期任务\\n- [x] hgate-dpo003-merged 4 runs → H2+
…[truncated 1453 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:dm:oc_a55584f7606e96135a3510c9deec7264:briefer",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 627
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-13T11:32:29.598324+00:00_

**不太对应。** 项目名 `cost-verify-agent-rl` 暗示的是"成本验证 + Agent + RL"，但实际研究内容是：

**DemoCalib** — 研究 LLM Agent 行为校准方法（BCP prompting 和 DPO）的**失败机制**，核心发现是 "alignment non-compositionality"（DPO 和 BCP 各自有效但组合后效果反转）。

拆开看：
- **agent** ✅ — 确实是做 agent（tau-bench retail 环境，tool calling 场景）
- **rl** 勉强沾边 — DPO 算 RLHF 的变体，但项目重心不在 RL 训练本身，而是在分析校准失败
- **verify** 勉强沾边 — 有验证/评估环节，但不是项目核心主题
- **cost** ❌ — 当前内容跟"成本"没什么关系

推测项目名是立项时定的，后来研究方向演化了，名字没跟着改。目前论文 framing 叫 **DemoCalib**，目标投稿 EMNLP 2026 Findings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:dm:oc_a55584f7606e96135a3510c9deec7264:briefer"
}
```

</details>

---
