# writing related work draft

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 84
- **Recorded user turns:** 1
- **Tool calls:** 26
- **Original source:** `logs/workers/worker_writing_related-work-draft_20260516T003933.log`
- **Structured JSON:** [`1f6ef5f6abe5cacdef5a.json`](../../sessions/1f/1f6ef5f6abe5cacdef5a.json)

## Before a recorded user message

15 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
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
  "uuid": "62a3d86d-50ff-460d-968c-53b0445c1ece",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778903400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "aaa18c66-300c-4ee8-a257-e4afba522759",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794"
}
```

---

### Assistant

_source line 4_

I'll start by reading the literature map and paper framing to gather the necessary context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "a7a16282-b2df-42cc-b357-53074d93f729",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F2PY8uHuYDT7EFC8Y7RfNw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12150,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12150
      },
      "output_tokens": 4,
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

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01L5b13uXaeBcDjBjQxgbSBR`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "da8a44fd-50d6-4057-9bab-e63fb37bcd3b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F2PY8uHuYDT7EFC8Y7RfNw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12150,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12150
      },
      "output_tokens": 4,
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

_source line 6 · 2026-05-16T00:39:43.853Z_

<details><summary>↩ Tool result · `toolu_01L5b13uXaeBcDjBjQxgbSBR`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "c9d72b33-a3d1-48b4-a3c3-9b3ce81908c8",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Now let me read both files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "2a33dcd3-31a0-4646-9f5e-f32a26fc427e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UL8c4mr7hW1KSWVDEzVqfg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 454,
      "cache_read_input_tokens": 23597,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 454
      },
      "output_tokens": 33,
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

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01REjBsVJvjV6w5xN8r3Gm1e`</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "26b4c25c-5f08-4fb4-9d14-0dc8f001c000",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UL8c4mr7hW1KSWVDEzVqfg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 454,
      "cache_read_input_tokens": 23597,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 454
      },
      "output_tokens": 33,
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

_source line 9 · 2026-05-16T00:39:47.689Z_

<details><summary>↩ Tool result · `toolu_01REjBsVJvjV6w5xN8r3Gm1e`</summary>

```text
Error: result (80,201 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7341df47-ab61-4a7f-ab4b-fc80cccd2794/tool-results/mcp-agent-ml-research-read_project_file-1778891987655.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7341df47-ab61-4a7f-ab4b-fc80cccd2794/tool-results/mcp-agent-ml-research-read_project_file-1778891987655.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7341df47-ab61-4a7f-ab4b-fc80cccd2794/tool-results/mcp-agent-ml-research-read_project_file-1778891987655.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "c537d14d-8881-4543-9d32-4de29b74ddcb",
  "tool_use_result": {
    "content": "Error: result (80,201 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7341df47-ab61-4a7f-ab4b-fc80cccd2794/tool-results/mcp-agent-ml-research-read_project_file-1778891987655.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7341df47-ab61-4a7f-ab4b-fc80cccd2794/tool-results/mcp-agent-ml-research-read_project_file-1778891987655.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7341df47-ab61-4a7f-ab4b-fc80cccd2794/tool-results/mcp-agent-ml-research-read_project_file-1778891987655.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml\", \"content\": \"# Literature Map for faith-evidence-ie (FREIGE)\\n# Focus: CED-as-training-stabilizer (D024) + RSFT for DocRE\\n# Updated: 2026-05-16 (W4 expanded: +11 papers from literature scan; +15 papers from Related Work survey; +17 papers from Related Work expansion; +16 papers from Related Work extension scan)\\n\\npapers:\\n\\n  # === Category 1: Reward Diversity / Reward Shaping for RL Stability ===\\n\\n  - title: \\\"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization\\\"\\n    authors: NVIDIA Labs\\n    year: 2025\\n    venue: ICML 2026\\n    url: https://arxiv.org/abs/2601.05242\\n    category: reward_diversity\\n    role: closest_prior_work\\n    key_finding: >\\n      直接将 GRPO 应用于多 reward 组合时，不同 rollout 的 reward 组合在归一化后 collapse 为相同 advantage 值，\\n      降低训练信号分辨率导致收敛失败。GDPO 对每个 reward 独立做 group-wise normalization 再聚合，\\n      保留多 reward 的相对差异，显著提升训练稳定性。\\n    relevance_to_ced_stabilizer: >\\n      最直接相关。CED reward 本质上引入了独立于 extraction F1 的 reward 维度（evidence quality），\\n      GDPO 的理论分析解释了为什么多维 reward 比单一 reward 更稳定——独立 reward 维度防止 advantage collapse。\\n      但 GDPO 是方法论贡献，CED 是 task-specific reward 设计自然具备了这一特性。\\n\\n  - title: \\\"DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of LLMs\\\"\\n    authors: Xiwen Chen et al.\\n    year: 2025\\n    venue: arXiv 2505.09655\\n    url: https://arxiv.org/abs/2505.09655\\n    category: reward_diversity\\n    role: related_method\\n    key_finding: >\\n      GRPO 的标量 reward 无法区分语义多样但得分相同的输出（diversity-quality inconsistency）。\\n      DRA 用子模互信息（SMI）对 reward 加权，给多样性高的 completion 更大权重，\\n      等价于 Inverse Propensity Scoring 去偏，防止 policy 坍缩到先验模式。\\n    relevance_to_ced_stabilizer: >\\n      DRA 通过后处理 reward 注入多样性信号；CED 的 reward 本身就内含对比结构自然提供 diversity 信号。\\n      机制互补但来源不同——CED 是 reward design 层面，DRA 是 optimization 层面。\\n\\n  - title: \\\"Shrinking the Variance: Shrinkage Baselines for RL with Verifiable Rewards\\\"\\n    authors: Guanning Zeng et al.\\n    year: 2025\\n    venue: arXiv 2511.03710\\n    url: https://arxiv.org/abs/2511.03710\\n    category: reward_diversity\\n    role: theoretical_support\\n    key_finding: >\\n      RLVR 中 per-prompt 均值 baseline 在低 generation 数下估计不准导致高 variance 梯度。\\n      用 James-Stein shrinkage 混合 per-prompt 和 cross-prompt 均值，\\n      构造可证明更低 variance 的 policy gradient estimator。\\n    relevance_to_ced_stabilizer: >\\n      理论支持：reward variance 对 gradient estimation 质量至关重要。\\n      CED 的额外 reward 维度提供更丰富的 per-group variance，间接起到 variance 维持效果。\\n\\n  - title: \\\"Reward Shaping to Mitigate Reward Hacking in RLHF\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2502.18770\\n    url: https://arxiv.org/abs/2502.18770\\n    category: reward_diversity\\n    role: background\\n    key_finding: >\\n      RL reward 应有界且先快速增长后缓慢收敛。系统研究 reward shaping 原则，\\n      好的 reward 形状能抑制 reward hacking 并提升训练稳定性。\\n    relevance_to_ced_stabilizer: >\\n      CED reward 的 0-1 对比判别结构天然满足有界性，\\n      且 evidence quality 的渐进提升符合\\\"先快后慢\\\"的 reward shaping 原则。\\n\\n  # === Category 2: Mode Collapse Prevention in GRPO/RLHF ===\\n\\n  - title: \\\"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\\\"\\n    authors: ByteDance Seed, Tsinghua AIR\\n    year: 2025\\n    venue: NeurIPS 2025\\n    url: https://arxiv.org/abs/2503.14476\\n    category: mode_collapse_prevention\\n    role: key_baseline\\n    key_finding: >\\n      Naive GRPO 存在 entropy collapse（policy 熵快速下降→输出同质化）。\\n      根因：clipping 不对称性——概率 0.01 的 token 最多增到 0.012，而概率 0.9 的 token 可达 1.08，\\n      低概率 token 难以增长，抑制探索。DAPO 提出 Clip-Higher（εhigh=0.28 > εlow=0.2）\\n      为低概率 token 留更大增长空间，加 Dynamic Sampling 过滤 accuracy=0 或 1 的 prompt\\n      （这些 prompt 产生零梯度，降低有效 batch size）。在 AIME 2024 达 50 分超越 DeepSeek-R1-Zero。\\n    relevance_to_ced_stabilizer: >\\n      DAPO 从 optimization 技巧角度解决 entropy collapse。CED reward 从 reward design 层面\\n      防止 mode collapse——evidence quality 维度确保 reward 组内有足够 variance，\\n      不会出现 all-same-reward 的零梯度 prompt。DAPO 的 Dynamic Sampling 过滤 accuracy=0/1 prompt\\n      与我们观察到的 frac_zero_std→0.8 现象本质相同：extraction-only reward 下大量 prompt\\n      产生零 advantage，CED 从源头（reward 设计）而非后处理（过滤）解决这个问题。\\n\\n  - title: \\\"Dr. GRPO: Removing Optimization Bias in GRPO\\\"\\n    authors: Liu et al.\\n    year: 2025\\n    venue: COLM 2025\\n    url: https://arxiv.org/abs/2503.20783\\n    category: mode_collapse_prevention\\n    role: related_analysis\\n    key_finding: >\\n      GRPO 的 std 归一化引入两个 bias：(1) difficulty bias——std(r) 归一化对低 variance 组\\n      （全对/全错）给予过高 advantage 权重，trivial question 主导训练信号；\\n      (2) length bias——per-token loss 的 1/|o_i| 项使长的错误回答被 under-penalize。\\n      当 std(r)→0 时 advantage 爆炸或未定义，梯度数值不稳定。\\n      Dr. GRPO 移除 std 归一化，用无偏 Monte Carlo advantage：Ã = R(q,o_i) - mean(R)。\\n    relevance_to_ced_stabilizer: >\\n      与我们的实验发现高度一致：extraction-only reward 下 frac_zero_std→0.8 正是\\n      Dr. GRPO 分析的 difficulty bias 极端情况——大量 prompt 的所有 rollout 得到相同 F1，\\n      std→0 导致 advantage 异常。CED 通过增加 reward 维度天然维持 reward_std>0，\\n      从 reward 设计而非算法修改角度避免了 Dr. GRPO 发现的 bias。\\n\\n  - title: \\\"GVPO: Group Variance Policy Optimization for LLM Post-Training\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: NeurIPS 2025\\n    url: https://arxiv.org/abs/2504.19599\\n    category: mode_collapse_prevention\\n    role: alternative_framework\\n    key_finding: >\\n      将 KL 约束 reward 最大化的解析解直接嵌入梯度权重，\\n      variance 项自然平衡 exploration 与 exploitation，维持适度 entropy。\\n    relevance_to_ced_stabilizer: >\\n      GVPO 的 variance 项机制与 CED 维持 reward variance 的效果功能类似，\\n      但 GVPO 是算法层面 implicit regularization，CED 是 reward 层面 explicit structure。\\n\\n  - title: \\\"REINFORCE++: Stabilizing Critic-Free Policy Optimization with Global Advantage Normalization\\\"\\n    authors: Jian Hu et al.\\n    year: 2025\\n    venue: arXiv 2501.03262\\n    url: https://arxiv.org/abs/2501.03262\\n    category: mode_collapse_prevention\\n    role: related_method\\n    key_finding: >\\n      Prompt-level (local) advantage normalization 导致不准确估计和过拟合。\\n      Global batch normalization 提供更稳定、理论无偏的 gradient estimator。\\n    relevance_to_ced_stabilizer: >\\n      解决 local normalization 的 variance 问题；CED 从 reward 端增加 variance 来源。\\n      两者在不同层面解决同一问题：防止 gradient signal 消失。\\n\\n  - title: \\\"DiverseGRPO: Mitigating Mode Collapse in Image Generation via Diversity-Aware GRPO\\\"\\n    authors: Henglin Liu et al.\\n    year: 2025\\n    venue: arXiv 2512.21514\\n    url: https://arxiv.org/abs/2512.21514\\n    category: mode_collapse_prevention\\n    role: parallel_work\\n    key_finding: >\\n      图像生成中 GRPO 后期输出同质化。distributional reward modeling（谱聚类+exploratory reward）\\n      和 structure-aware regularization 实现 13-18% 语义多样性提升。\\n    relevance_to_ced_stabilizer: >\\n      跨域验证了 GRPO mode collapse 的普遍性，distributional reward 思路与 CED 精神相近——\\n      都是通过 reward 层面结构化信号维持输出多样性。\\n\\n  - title: \\\"Why GRPO Needs Normalization: A Local-Curvature Perspective on Adaptive Gradients\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2601.23135\\n    url: https://arxiv.org/abs/2601.23135\\n    category: mode_collapse_prevention\\n    role: theoretical_support\\n    key_finding: >\\n      GRPO 的 reward_std 归一化在温和条件下提供严格优于未归一化 REINFORCE 的收敛速率，\\n      收益由 prompt 间平均 reward std 刻画。\\n    relevance_to_ced_stabilizer: >\\n      直接理论支撑：reward_std 越大收敛越好。CED 通过 evidence quality 维度维持高 reward_std，\\n      从该理论看 CED 的稳定性优势是 reward_std 维持带来的收敛速率优势。\\n\\n  # === Category 3: Contrastive Rewards in RL ===\\n\\n  - title: \\\"Improving Reinforcement Learning from Human Feedback Using Contrastive Rewards\\\"\\n    authors: Shen, Zhang et al.\\n    year: 2024\\n    venue: arXiv 2403.07708\\n    url: https://arxiv.org/abs/2403.07708\\n    category: contrastive_reward\\n    role: closest_contrastive_precedent\\n    key_finding: >\\n      两步机制：(1) 离线采样 baseline response；(2) 用 baseline 计算 contrastive reward\\n      作为 PPO 的 penalty 项。效果：惩罚 reward uncertainty、根据任务难度自适应校准、\\n      减少 PPO 中的 variance。在 TL;DR 和 HH-RLHF 上持续优于标准 RLHF。\\n    relevance_to_ced_stabilizer: >\\n      最接近的对比 reward 先例。关键差异：(1) 它是对 learned RM 输出的后处理对比，\\n      CED 是 reward function 本身就是对比判别（evidence vs. corrupted evidence）；\\n      (2) 它在 PPO 中验证，CED 在 GRPO 中验证；\\n      (3) 它是 domain-agnostic penalty，CED 是 task-specific faithfulness signal。\\n      stabilizing 机制相通但实现路径根本不同。\\n\\n  - title: \\\"Improving Discriminative Capability of Reward Models in RLHF Using Contrastive Learning\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: EMNLP 2024\\n    url: https://aclanthology.org/2024.emnlp-main.852/\\n    category: contrastive_reward\\n    role: related_method\\n    key_finding: >\\n      无监督对比损失训练 reward model 充分捕捉对比数据区分度，\\n      带来更稳定的 PPO 训练 return 和 reward。\\n    relevance_to_ced_stabilizer: >\\n      验证对比训练 reward model → 更稳定 RL 训练链条。CED 不是对比训练 reward model，\\n      而是 reward function 本身就是对比判别，但 stabilizing 机制相通。\\n\\n  - title: \\\"Contrastive Preference Learning: Learning from Human Feedback without RL\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: ICLR 2025\\n    url: https://openreview.net/forum?id=iX1RjVQODj\\n    category: contrastive_reward\\n    role: background\\n    key_finding: >\\n      将 preference learning 重新表述为对比学习问题，无需显式 RL 即可从人类反馈中学习。\\n    relevance_to_ced_stabilizer: >\\n      对比框架在 preference alignment 中的通用性。CED 可被视为 task-specific contrastive preference signal。\\n\\n  # === Category 4: Evidence-Based Rewards in IE/NLP ===\\n\\n  - title: \\\"Drift: Enhancing LLM Faithfulness in Rationale Generation\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: ACL 2025\\n    url: https://aclanthology.org/2025.acl-long.340.pdf\\n    category: evidence_reward\\n    role: related_method\\n    key_finding: >\\n      用 faithfulness reward 引导 LLM 生成更可靠的 rationale，提升 CoT 推理事实一致性。\\n    relevance_to_ced_stabilizer: >\\n      Faithfulness reward 用于生成质量的先例。CED 中 evidence discrimination\\n      本质上也是 faithfulness 信号——判断证据是否忠实支持抽取结果。\\n\\n  - title: \\\"Fine-Grained NLI-Based Faithfulness Evaluation for Diverse Summarisation Tasks (INFUSE)\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: EACL 2024\\n    url: https://aclanthology.org/2024.eacl-long.102/\\n    category: evidence_reward\\n    role: background\\n    key_finding: >\\n      变长前提+简化假设的细粒度 NLI faithfulness 评估，超越传统 NLI 在多任务摘要上的表现。\\n    relevance_to_ced_stabilizer: >\\n      NLI 作为 faithfulness 评估工具的进展。CED 中 NLI 组件用于判断 evidence 对 triple 的支持度。\\n\\n  - title: \\\"Enhancing Cross-Evidence Reasoning Graph for Document-Level Relation Extraction\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: PMC/Bioinformatics 2024\\n    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11232587/\\n    category: evidence_reward\\n    role: background\\n    key_finding: >\\n      文档级关系抽取中用 cross-evidence reasoning graph 增强跨证据推理。\\n    relevance_to_ced_stabilizer: >\\n      DocRE 中 evidence 的重要性。但用 evidence 作为模型输入特征，\\n      我们用 evidence quality 作为 RL reward 信号——定位根本不同。\\n\\n  # === Category 5: Multi-Objective RL for Text Generation ===\\n\\n  - title: \\\"Confronting Reward Model Overoptimization with Constrained RLHF\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: OpenReview\\n    url: https://openreview.net/forum?id=gkfUvn0fLU\\n    category: multi_objective_rl\\n    role: related_analysis\\n    key_finding: >\\n      多组件 RM 的 overoptimization 研究。component RM 间的相关性显著影响 overoptimization 临界点，\\n      用 constrained MDP 防止超出适当边界。\\n    relevance_to_ced_stabilizer: >\\n      CED 引入了与 extraction F1 低相关的 reward component（evidence quality），\\n      根据该论文分析低相关多组件 reward 更不易 overoptimize，\\n      可能是 CED 稳定性的另一个理论解释角度。\\n\\n  - title: \\\"On-Policy RL with Optimal Reward Baseline\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2505.23585\\n    url: https://arxiv.org/abs/2505.23585\\n    category: multi_objective_rl\\n    role: theoretical_support\\n    key_finding: >\\n      Optimal baseline 一致性地实现更高训练 reward 和更高 entropy，\\n      有效稳定训练并促进更多样的 policy exploration。\\n    relevance_to_ced_stabilizer: >\\n      CED reward 的多维特性可能起到类似 optimal baseline 效果——\\n      evidence quality 维度为 advantage estimation 提供更丰富的参照信号。\\n\\n  # === Category 6: RSFT Methodology & Theory ===\\n\\n  - title: \\\"A Minimalist Approach to LLM Reasoning: from Rejection Sampling to Reinforce\\\"\\n    authors: Xiao et al.\\n    year: 2025\\n    venue: arXiv 2504.11343\\n    url: https://arxiv.org/abs/2504.11343\\n    category: rsft_methodology\\n    role: key_theoretical_support\\n    key_finding: >\\n      RAFT（简单 rejection sampling baseline）在数学推理上与 GRPO/PPO 表现相当。\\n      消融实验表明 GRPO 的主要优势来自丢弃全错 prompt 而非 reward normalization。\\n      提出 Reinforce-Rej，在 RAFT 基础上过滤全对和全错 sample。\\n      关键洞察：GRPO 和 RAFT 的核心区别在于负样本处理——GRPO 混合正负样本训练，\\n      RAFT 只用正样本，但 RAFT 仍能达到相当性能，说明 rejection sampling 的简单性被低估了。\\n    relevance_to_rsft_docre: >\\n      直接支持我们的设计选择：(1) RSFT 在 DocRE 上成功而 GRPO 失败，\\n      与该论文发现一致——rejection sampling 的 offline 特性天然避免了 catastrophic forgetting；\\n      (2) GRPO 主要优势来自过滤全错 prompt，这与我们 RSFT 的 reward-based filtering 机制相同；\\n      (3) DocRE structured output 比 math reasoning 更难用 online RL 优化，\\n      强化了 offline RSFT 的合理性。\\n\\n  - title: \\\"Beyond Rejection Sampling: Trajectory Fusion for Scaling Mathematical Reasoning (TrajFusion)\\\"\\n    authors: Jie Deng et al.\\n    year: 2026\\n    venue: arXiv 2602.04391\\n    url: https://arxiv.org/abs/2602.04391\\n    category: rsft_methodology\\n    role: method_component\\n    key_finding: >\\n      传统 RSFT 只用正确轨迹，丢弃错误轨迹。TrajFusion 将错误和正确轨迹交替拼接，\\n      显式建模试错推理过程，在困难数学问题上显著超越标准 RFT。\\n    relevance_to_rsft_docre: >\\n      Future work 方向：可考虑在 DocRE RSFT 中融合失败样本的信息。\\n      但 DocRE 的结构化输出（JSON triple）不同于 math 的 chain-of-thought，\\n      融合方式需要重新设计。\\n\\n  - title: \\\"Rejection Sampling Based Fine Tuning Secretly Performs PPO\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: ICML 2025\\n    url: https://openreview.net/forum?id=yQ2UivKlir\\n    category: rsft_methodology\\n    role: theoretical_support\\n    key_finding: >\\n      建立 RSFT 与 PPO 之间的理论联系：rejection sampling fine-tuning\\n      在特定条件下隐式执行 PPO with marginal KL constraints。\\n    relevance_to_rsft_docre: >\\n      为 RSFT 的有效性提供理论解释。我们的 RSFT 成功可被视为\\n      隐式执行了 constrained policy optimization，\\n      避免了显式 GRPO 在 structured output 上的不稳定性。\\n\\n  # === Category 7: RL for Information Extraction ===\\n\\n  - title: \\\"R1-RE: Cross-Domain Relation Extraction with RLVR\\\"\\n    authors: Runpeng Dai, Tong Zheng et al.\\n    year: 2025\\n    venue: arXiv 2507.04642\\n    url: https://arxiv.org/abs/2507.04642\\n    category: rl_for_ie\\n    role: direct_competitor\\n    key_finding: >\\n      首个将 RLVR（GRPO + verifiable reward）用于关系抽取的框架。\\n      将 RE 重构为推理任务，R1-RE-7B 在跨域 OOD 准确率约 70%，媲美 GPT-4o。\\n      Reward 设计：format reward (+1/-3) + metric reward (+2/-1.5)，先验证格式再加准确度。\\n      triplet extraction 用 F1-based reward（entity weight=1, triplet weight=3）。\\n      未报告 catastrophic forgetting——GRPO 训练后在 MATH-500/IFEval/GPQA 上性能不降反升，\\n      说明句子级 RE 的简单 reward 结构足以稳定 GRPO 训练。\\n    results:\\n      sem2010_in_domain: 91.8\\n      sem2010_ood: 66.5\\n      mdkg_in_domain: 88.1\\n      mdkg_ood: 65.8\\n    evidence_generation: false\\n    relevance_to_rsft_docre: >\\n      最直接竞争者。关键差异与讨论：\\n      (1) R1-RE 是句子级 RE，GRPO 成功；我们是文档级 RE，GRPO 失败→RSFT 成功。\\n      句子级 RE 每个 sample 只有 1 个 triple（binary classification），reward variance 天然充足；\\n      文档级 RE 每个 sample 有数十个 triple，F1 score 作为 reward 在 group 内趋于同质化（frac_zero_std→0.8）。\\n      (2) R1-RE 未报告 catastrophic forgetting，进一步支持\\\"句子级简单 reward 可行，文档级需要 CED\\\"的论点。\\n      (3) R1-RE 关注 OOD 泛化，无 evidence 组件；我们关注 evidence-grounded extraction quality。\\n      互补而非直接冲突——R1-RE 证明 RLVR for RE 可行，我们揭示文档级需要额外设计。\\n\\n  - title: \\\"MORE-R1: Guiding LVLM for Multimodal Object-Entity Relation Extraction via Stepwise Reasoning with RL\\\"\\n    authors: Anonymous\\n    year: 2026\\n    venue: arXiv 2603.09478\\n    url: https://arxiv.org/abs/2603.09478\\n    category: rl_for_ie\\n    role: related_method\\n    key_finding: >\\n      多模态 RE 中用 GRPO + Progressive Sample-Mixing Strategy 优化 LVLM 推理能力。\\n      两阶段训练：SFT cold-start + GRPO RL。\\n    relevance_to_rsft_docre: >\\n      跨模态验证 RL for RE 趋势。其 Progressive Sample-Mixing 与我们\\n      RSFT 的 difficulty-aware sampling 思想相通，但在不同模态。\\n\\n  - title: \\\"REAR: Reinforced Reasoning Optimization for Event Argument Extraction with Relation-Aware Support\\\"\\n    authors: Jianwen Luo et al.\\n    year: 2025\\n    venue: EMNLP 2025 Findings\\n    url: https://2025.emnlp.org/program/find_papers/\\n    category: rl_for_ie\\n    role: related_method\\n    key_finding: >\\n      将强化学习推理优化用于事件论元抽取，结合关系感知支持。\\n      不同于 DocRE 但同属 IE 领域的 RL 应用。\\n    relevance_to_rsft_docre: >\\n      验证 RL 在 IE 任务上的有效性趋势。我们的工作扩展到 DocRE + evidence，\\n      且使用 offline RSFT 而非 online RL。\\n\\n  - title: \\\"Adaptive Reinforcement Learning Planning: Harnessing LLMs for Complex Information Extraction\\\"\\n    authors: Zepeng Ding et al.\\n    year: 2024\\n    venue: arXiv 2406.11455\\n    url: https://arxiv.org/abs/2406.11455\\n    category: rl_for_ie\\n    role: background\\n    key_finding: >\\n      将 LLM 顺序抽取建模为 MDP，用 DDQN 训练 decision module\\n      自适应选择实体抽取顺序，提升复杂 IE 性能。\\n    relevance_to_rsft_docre: >\\n      RL for IE 的早期工作。用 RL 优化抽取策略而非模型本身，\\n      与我们 RSFT 直接微调 LLM 的方法路径不同。\\n\\n  - title: \\\"Graph-R1: Towards Agentic GraphRAG Framework via End-to-end Reinforcement Learning\\\"\\n    authors: Haoran Luo et al.\\n    year: 2025\\n    venue: ICML 2026\\n    url: https://arxiv.org/abs/2507.21892\\n    category: rl_for_ie\\n    role: background\\n    key_finding: >\\n      用端到端 RL 优化 GraphRAG agent 的多轮检索-推理循环，\\n      包含 knowledge hypergraph construction（n-ary relation extraction）。\\n    relevance_to_rsft_docre: >\\n      RL + knowledge extraction 的交叉点。Graph-R1 关注 QA 场景下的知识图谱构建，\\n      我们关注 DocRE 的训练优化，应用场景不同。\\n\\n  # === Category 8: Recent LLM-based DocRE Methods ===\\n\\n  - title: \\\"RelPrior: Relation as a Prior - A Novel Paradigm for LLM-based Document-level Relation Extraction\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2511.08143\\n    url: https://arxiv.org/abs/2511.08143\\n    category: llm_docre\\n    role: key_baseline\\n    key_finding: >\\n      用 binary relation 作为先验过滤无关实体对，再用 predefined relation 匹配实体，\\n      避免 LLM 在 DocRE 中被无关实体对分散注意力。\\n      在 DocRED/Re-DocRED 上超越现有纯 LLM-based DocRE 方法。\\n    results:\\n      docred_dev_f1: 47.82\\n      docred_test_f1: 48.34\\n      re_docred_dev_f1: 55.94\\n      re_docred_test_f1: 54.80\\n      backbone: LLaMA3-8B\\n    evidence_generation: false\\n    relevance_to_rsft_docre: >\\n      我们的直接 baseline 之一。RelPrior_LLaMA3-8B 在 DocRED test F1=48.34,\\n      Re-DocRED test F1=54.80。我们的 RSFT 提升显著更优。\\n      RelPrior 是 inference paradigm 创新（两阶段筛选），我们是 training paradigm 创新（RSFT+CED），正交互补。\\n\\n  - title: \\\"LMRC: LLM with Relation Classifier for Document-Level Relation Extraction\\\"\\n    authors: Xingzuo Li, Kehai Chen, Yunfei Long, Min Zhang\\n    year: 2024\\n    venue: arXiv 2408.13889\\n    url: https://arxiv.org/abs/2408.13889\\n    category: llm_docre\\n    role: related_method\\n    key_finding: >\\n      两阶段方法：先用 attention-based classifier 过滤 NA 实体对（RCP），\\n      再用 LLM 在精简候选空间中做多分类（RC）。\\n      注意：LMRC 依赖 BERT-based classifier 作为预筛选，非纯 LLM 方法。\\n    results:\\n      docred_dev_ign_f1: 58.16\\n      docred_dev_f1: 59.97\\n      docred_test_ign_f1: 58.49\\n      docred_test_f1: 60.52\\n      re_docred_test_ign_f1: 74.08\\n      re_docred_test_f1: 74.63\\n      backbone: BERT classifier + LLM\\n    evidence_generation: false\\n    relevance_to_rsft_docre: >\\n      LMRC 在 DocRED test F1=60.52, Re-DocRED test F1=74.63，性能显著高于纯 LLM 方法。\\n      但它依赖 BERT classifier 预筛选，本质上是 hybrid 方法而非纯 LLM generative。\\n      与我们端到端 LLM 生成方式不同——我们通过 RSFT 的 reward-based filtering 隐式解决 class imbalance。\\n\\n  - title: \\\"Ru-LLM: Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: NLPCC 2025\\n    url: https://link.springer.com/chapter/10.1007/978-981-95-3343-5_11\\n    category: llm_docre\\n    role: related_method\\n    key_finding: >\\n      用频繁模式挖掘 + MCTS 搜索逻辑规则，转化为 prompt 约束 LLM 输出，\\n      再用 CoT 验证过滤不满足规则的 triple。\\n      在 DWIE、DocRED、Re-DocRED 上声称超越现有 LLM 方法和规则框架。\\n      具体 F1 未公开获取（Springer 付费墙），但声称超越 AutoRE 等 LLM baseline。\\n    results:\\n      note: \\\"behind Springer paywall; claims SOTA over LLM baselines on DocRED/Re-DocRED/DWIE\\\"\\n    evidence_generation: false\\n    relevance_to_rsft_docre: >\\n      规则约束方式与我们的 CED reward 在 motivation 上相似（都是引入外部知识约束），\\n      但 Ru-LLM 用 inference-time 规则验证（MCTS+CoT），我们用 training-time reward shaping（CED）。\\n      Ru-LLM 的规则是数据集级别的频繁模式，CED 是 instance-level 的 evidence faithfulness。\\n\\n  - title: \\\"GLiDRE: Generalist Lightweight model for Document-level Relation Extraction\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2508.00757\\n    url: https://arxiv.org/abs/2508.00757\\n    category: llm_docre\\n    role: background\\n    key_finding: >\\n      基于 dual-encoder 的轻量级零/少样本 DocRE 模型，\\n      预训练于 136K 文档的大规模 RE 数据。\\n      fully supervised Re-DocRED test F1=77.83，但这是 encoder-based 非 LLM generative。\\n      zero-shot Re-DocRED test F1=17.32（超越 LLaMA 3.3 70B 和 Mistral-Small 24B）。\\n    results:\\n      re_docred_dev_f1: 77.76\\n      re_docred_test_f1: 77.83\\n      re_docred_zero_shot_test_f1: 17.32\\n      fredo_in_domain_1doc_f1: 13.00\\n      fredo_in_domain_3doc_f1: 15.71\\n      backbone: \\\"dual-encoder (few hundred M params)\\\"\\n    evidence_generation: false\\n    relevance_to_rsft_docre: >\\n      不同范式（encoder-based vs LLM generative）。GLiDRE 的 fully supervised F1=77.83\\n      远超 LLM-based 方法（RelPrior 54.80），但依赖大规模预训练数据和 encoder 架构。\\n      与我们不直接可比——我们关注 LLM generative 范式下的训练优化。\\n\\n  - title: \\\"AutoRE: Document-Level Relation Extraction with Large Language Models\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: arXiv 2403.14888\\n    url: https://arxiv.org/abs/2403.14888\\n    category: llm_docre\\n    role: background\\n    key_finding: >\\n      RHF（Relation-Head-Facts）范式用 Mistral-7B + QLoRA 做端到端 DocRE。\\n      关键设计：先抽 relation，再抽 head entity，最后抽 fact triple。\\n    results:\\n      re_docred_dev_f1_mistral: 53.01\\n      re_docred_test_f1_mistral: 51.91\\n      re_docred_dev_f1_vicuna: 54.29\\n      re_docred_test_f1_vicuna: 53.84\\n      docred_dev_f1_llama3: 45.76\\n      docred_test_f1_llama3: 45.96\\n      re_docred_dev_f1_llama3: 52.28\\n      re_docred_test_f1_llama3: 51.97\\n      backbone: \\\"Mistral-7B / Vicuna-7B / LLaMA3-8B (QLoRA)\\\"\\n    evidence_generation: false\\n    relevance_to_rsft_docre: >\\n      QLoRA fine-tuning for DocRE 的先例。AutoRE_LLaMA3-8B 在 Re-DocRED test F1=51.97,\\n      DocRED test F1=45.96。我们的 SFT baseline 与之类似，\\n      RSFT 在此基础上引入 reward-guided sample selection 进一步提升。\\n\\n  # === Category 9: Evidence Generation & Task Performance Trade-off ===\\n  # (NEW - 2026-05-15 evidence generation survey)\\n\\n  - title: \\\"Mind Your Step (by Step): Chain-of-Thought can Reduce Performance on Tasks where Thinking Makes Humans Worse\\\"\\n    authors: Sprague et al.\\n    year: 2024\\n    venue: NeurIPS 2024\\n    url: https://arxiv.org/abs/2410.21333\\n    category: evidence_generation_tradeoff\\n    role: key_evidence\\n    key_finding: >\\n      CoT 在某些任务上降低性能高达 36.3%（o1-preview vs GPT-4o）。\\n      显式推理步骤引入 error accumulation，且模型可能 overfit 到解释格式而非任务结构。\\n      隐式推理（hidden activations）在分布偏移下优于显式 token-level 推理。\\n    relevance_to_evidence_tradeoff: >\\n      直接支持我们的核心发现：要求模型同时生成 evidence sentences 是一种\\\"显式推理\\\"，\\n      会对主任务（RE）产生性能代价（~8pp F1 下降）。\\n      Related Work 引用点：evidence generation 作为 structured explanation，\\n      与 CoT 共享\\\"显式推理降低主任务性能\\\"的普遍模式。\\n\\n  - title: \\\"Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion\\\"\\n    authors: Xie et al. (Google Research)\\n    year: 2022\\n    venue: ACL Findings 2022\\n    url: https://arxiv.org/abs/2106.08657\\n    category: evidence_generation_tradeoff\\n    role: closest_docre_precedent\\n    key_finding: >\\n      Joint 训练 RE + evidence extraction，关键创新在 inference-stage fusion：\\n      分别在 extracted evidence 和 full document 上做 RE 预测再通过 blending layer 融合。\\n      DocRED 上提升 1.37 Ign F1。Silver evidence labels（启发式规则构建）即可提升 RE 性能。\\n    relevance_to_evidence_tradeoff: >\\n      最直接的 DocRE + evidence 先例。EIDER 的核心洞察是 evidence 需要 inference-stage 融合\\n      而非 joint generation——暗示 joint generation 会引入 noise。\\n      我们的 CED reranker 是 LLM-era 版本的 inference-stage fusion：\\n      先生成多个候选（含 evidence），再用 NLI 在推理阶段选最佳。\\n      Related Work 引用点：encoder-based DocRE 中 evidence 的使用方式，与我们 generative 范式的关键差异。\\n\\n  - title: \\\"Exploring the Trade-off Between Model Performance and Explanation Plausibility of Text Classifiers Using Human Rationales\\\"\\n    authors: Resck, Raimundo, Poco\\n    year: 2024\\n    venue: NAACL Findings 2024\\n    url: https://arxiv.org/abs/2404.03098\\n    category: evidence_generation_tradeoff\\n    role: formal_framework\\n    key_finding: >\\n      用 multi-objective optimization 探索 performance vs explanation plausibility 的 Pareto frontier。\\n      引入 rationale 约束创建 contrastive loss，证实加入 rationale supervision 会降低主任务性能，\\n      但存在 Pareto optimal 解平衡两者。\\n    relevance_to_evidence_tradeoff: >\\n      提供了 performance-explainability trade-off 的形式化框架。\\n      我们的 evidence-grounded RE 降 8pp 正是 Pareto frontier 上的一个点。\\n      CED reranker 的效果可解读为：将系统从 evidence-constrained 点推向 Pareto frontier，\\n      在几乎不牺牲 evidence quality（evi_f1=0.8188）的前提下恢复 RE 性能。\\n      Related Work 引用点：evidence generation 的 performance cost 有理论依据。\\n\\n  - title: \\\"The Decreasing Value of Chain of Thought in Prompting\\\"\\n    authors: Meincke, Mollick, Mollick, Shapiro\\n    year: 2025\\n    venue: Wharton Generative AI Labs Technical Report (SSRN)\\n    url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5285532\\n    category: evidence_generation_tradeoff\\n    role: empirical_support\\n    key_finding: >\\n      现代 reasoning models 上 CoT 收益微弱（4-13%），但 latency 增加 35-600%。\\n      更强的模型从显式推理中受益越少。CoT 可能在 easy questions 上引入 errors\\n      （variability 增加导致原本正确的被改错）。\\n    relevance_to_evidence_tradeoff: >\\n      支持\\\"更强的 SFT 模型不需要在生成时显式输出 evidence\\\"的论点。\\n      我们的 evidence-only SFT 的性能下降符合\\\"显式推理的边际收益递减\\\"模式。\\n      Related Work 引用点：evidence generation 的 accuracy cost 不是 DocRE-specific，而是 LLM 的普遍趋势。\\n\\n  # === Category 10: Negative Transfer in Multi-task / Auxiliary-task Learning ===\\n\\n  - title: \\\"ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning\\\"\\n    authors: Jiang, Chen et al.\\n    year: 2023\\n    venue: NeurIPS 2023\\n    url: https://arxiv.org/abs/2301.12618\\n    category: negative_transfer\\n    role: theoretical_framework\\n    key_finding: >\\n      辅助任务常导致 negative transfer，根因不仅是 gradient conflict 还有 auxiliary-target\\n      generalization gap。ForkMerge 周期性 fork 模型为多分支，搜索最优 task weights，\\n      动态 merge 过滤有害 task-parameter updates。在多个 benchmark 上减少 negative transfer。\\n    relevance_to_evidence_tradeoff: >\\n      Evidence generation 作为 auxiliary task 对 RE 的 negative transfer 可用此框架解释：\\n      evidence 和 RE 的 gradient 方向不完全对齐，joint training 时 evidence 任务\\\"拖累\\\"RE。\\n      CED reranker 本质上是将 evidence quality 从 training-time joint objective 解耦到\\n      inference-time verification，避免了 training-time 的 negative transfer。\\n      Related Work 引用点：auxiliary task 导致主任务性能下降的一般性理论。\\n\\n  # === Category 11: Faithfulness vs Accuracy / Correctness Trade-off ===\\n\\n  - title: \\\"Correctness is not Faithfulness in RAG Attributions\\\"\\n    authors: Wallat, Heuss, de Rijke, Anand\\n    year: 2024\\n    venue: SIGIR 2025\\n    url: https://arxiv.org/abs/2412.18004\\n    category: faithfulness_accuracy_tradeoff\\n    role: key_conceptual_framework\\n    key_finding: >\\n      Correctness 和 faithfulness 是独立维度，可能冲突。高达 57% 的 citations 是\\n      post-rationalized（事后编造而非真实依据）。Unfaithful attributions 可能 factually correct，\\n      但 foster misguided trust。必须同时检查 correctness 和 faithfulness。\\n    relevance_to_evidence_tradeoff: >\\n      直接相关。我们的 evidence-grounded RE 试图让模型输出 faithful evidence，\\n      但这与 relation correctness 产生张力（rel_f1 降 8pp）。\\n      CED reranker 通过 NLI verification 确保 evidence 是 faithful 的（非 post-rationalized），\\n      同时不牺牲 RE accuracy。\\n      Related Work 引用点：correctness-faithfulness 分离的概念框架。\\n\\n  - title: \\\"Evaluating Correctness and Faithfulness of Instruction-Following Models for Question Answering\\\"\\n    authors: Adlakha, BehnamGhader, Lu, Meade, Reddy\\n    year: 2024\\n    venue: TACL 2024\\n    url: https://arxiv.org/abs/2307.16877\\n    category: faithfulness_accuracy_tradeoff\\n    role: evaluation_framework\\n    key_finding: >\\n      Instruction-following LLMs 在 correctness 上表现可比 fine-tuned models，\\n      但 faithfulness 普遍较差——模型会 hallucinate 而非忠实于提供的 evidence。\\n      传统 metrics 对 correctness 和 faithfulness 的评估均有缺陷。\\n    relevance_to_evidence_tradeoff: >\\n      解释了为什么 joint evidence+RE 生成性能差——模型在同时优化 correctness\\n      和 faithfulness 时，两个目标存在张力。单纯要求模型\\\"同时输出正确 triples 和\\n      faithful evidence\\\"是 multi-objective optimization 问题。\\n      Related Work 引用点：correctness vs faithfulness 评估方法论。\\n\\n  - title: \\\"Towards Faithful Model Explanation in NLP: A Survey\\\"\\n    authors: Lyu, Havaldar, Stein et al.\\n    year: 2024\\n    venue: Computational Linguistics (MIT Press)\\n    url: https://aclanthology.org/2024.cl-2.6/\\n    category: faithfulness_accuracy_tradeoff\\n    role: comprehensive_survey\\n    key_finding: >\\n      系统综述 NLP 中 faithful explanation 的定义、评估和生成方法。\\n      识别了 faithfulness-performance trade-off 作为核心挑战：\\n      更 faithful 的解释不一定更有用，更有用的解释不一定 faithful。\\n      提出未来方向包括 multi-objective optimization 和 post-hoc verification。\\n    relevance_to_evidence_tradeoff: >\\n      权威综述为我们的 evidence generation trade-off 提供广泛文献背景。\\n      我们的 CED reranker 正是该综述建议的\\\"post-hoc verification\\\"方向的具体实例。\\n      Related Work 引用点：faithfulness 研究的全景综述，定位我们的工作。\\n\\n  # === Category 12: Reranking / Verification as Bridge ===\\n\\n  - title: \\\"Genie: Achieving Human Parity in Content-Grounded Datasets Generation\\\"\\n    authors: Yehudai, Carmeli, Mass et al.\\n    year: 2024\\n    venue: ICLR 2024\\n    url: https://arxiv.org/abs/2401.14367\\n    category: reranking_verification_bridge\\n    role: methodological_precedent\\n    key_finding: >\\n      三阶段流程：Content Preparation → Generation → NLI-based Filtering。\\n      用 fine-tuned T5-11B NLI 模型判断生成内容是否 entailed by source（faithfulness 检验），\\n      过滤不 faithful 的生成。在 LFQA、摘要、IE 上达到 human parity。\\n    relevance_to_evidence_tradeoff: >\\n      方法论上最接近我们的 CED reranker——都是用 NLI verification 作为 post-hoc filter/reranker，\\n      在不牺牲主任务质量的前提下确保 grounding quality。\\n      GENIE 验证了 NLI-based filtering 在内容生成中的有效性。\\n      关键差异：GENIE 是 data generation pipeline 的过滤，我们是 inference-time reranking。\\n      Related Work 引用点：NLI-based verification 作为 bridge 的成功先例。\\n\\n  # === Category 13: Evidence-Grounded RL (NEW - 2026-05-15 scan) ===\\n\\n  - title: \\\"EvidenceRL: Reinforcing Evidence Consistency for Trustworthy Language Models\\\"\\n    authors: Ben Tamo, Lu, Marteau, Nnamdi, Wang\\n    year: 2026\\n    venue: arXiv 2603.19532\\n    url: https://arxiv.org/abs/2603.19532\\n    category: evidence_grounded_rl\\n    role: closest_competitor\\n    key_finding: >\\n      用 GRPO 同时优化 grounding（evidence entailment）和 correctness（答案准确性）。\\n      在 cardiac diagnosis（Llama-3.2-3B）上 F1@3 从 37.0→54.5，grounding 从 47.6→78.2，\\n      hallucination 降 5 倍。在 legal reasoning（Llama-3.1-8B）上 faithfulness 从 32.8%→67.6%。\\n      核心：证据一致性 reward 不牺牲 task accuracy 的前提下大幅提升 faithfulness。\\n    relevance_to_freige: >\\n      **最直接的 novelty 威胁。** EvidenceRL 与 FREIGE 共享核心 idea：用 GRPO + evidence faithfulness reward\\n      训练更可靠的模型。关键差异：(1) EvidenceRL 在 QA 域（cardiac/legal），不涉及 DocRE 的 structured output；\\n      (2) EvidenceRL 未报告 evidence generation 的 performance cost（evidence tax）——它的 grounding 和\\n      correctness 同时提升，而我们发现 DocRE 中两者存在 ~8pp 张力；\\n      (3) EvidenceRL 不涉及 task decoupling 现象（QLoRA-specific）；\\n      (4) EvidenceRL 无 inference-time reranking（CED reranker）。\\n      定位策略：EvidenceRL 证明 evidence-grounded RL 在 QA 域有效，\\n      我们揭示 DocRE structured output 带来的独特挑战（evidence tax、task decoupling）和解法（CED reranker）。\\n\\n  # === Category 14: Multi-Objective GRPO (NEW - 2026-05-15 scan) ===\\n\\n  - title: \\\"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems\\\"\\n    authors: Ichihara, Jinnai, Morimura, Sakamoto, Mitsuhashi, Uchibe\\n    year: 2025\\n    venue: arXiv 2509.22047\\n    url: https://arxiv.org/abs/2509.22047\\n    category: multi_objective_grpo\\n    role: related_method\\n    key_finding: >\\n      GRPO 在多目标设置下易发生 reward hacking——只优化一个目标而牺牲其他目标。\\n      MO-GRPO 用 variance-based normalization 自动平衡多个 reward function 的权重，\\n      在多臂赌博机、控制、机器翻译、指令遵从四个域上实现稳定学习。\\n    relevance_to_freige: >\\n      CED reward 本质是多目标（extraction F1 + evidence quality）。MO-GRPO 的分析\\n      解释了为什么单一 extraction F1 reward 下模型可能 hack 到 \\\"忽略 evidence 只抽 triple\\\" 的策略。\\n      CED 从 reward 设计端解决，MO-GRPO 从算法端解决，互补视角。\\n\\n  - title: \\\"Multi-Objective and Mixed-Reward Reinforcement Learning via Reward-Decorrelated Policy Optimization\\\"\\n    authors: Bai, Liu, Zhuang, Zhou, Weng, Chen, Wang, Cai\\n    year: 2026\\n    venue: arXiv 2605.13641\\n    url: https://arxiv.org/abs/2605.13641\\n    category: multi_objective_grpo\\n    role: related_method\\n    key_finding: >\\n      GRPO 聚合 mixed-reward 时直接求和再归一化会淹没弱信号 reward 维度。\\n      RDPO 用 Magnitude-Aware Quantile normalization + Mahalanobis whitening\\n      去相关 reward 子空间，改善 LLM post-training 的多目标平衡。\\n    relevance_to_freige: >\\n      CED reward 的 evidence quality 维度与 extraction F1 天然低相关（r<0.3），\\n      RDPO 的理论预测这种低相关多维 reward 更易优化。\\n      为 CED 的 training-stabilizing 效果提供另一个理论解释角度。\\n\\n  # === Category 15: GRPO Theory (NEW - 2026-05-15 scan) ===\\n\\n  - title: \\\"GRPO is Secretly a Process Reward Model\\\"\\n    authors: Sullivan, Koller\\n    year: 2025\\n    venue: under review at ICML 2026\\n    url: https://arxiv.org/abs/2509.21154\\n    category: grpo_theory\\n    role: theoretical_insight\\n    key_finding: >\\n      证明 GRPO + ORM 在特定条件下等价于 PRM-aware RL objective。\\n      提出 λ-GRPO 修正 GRPO 在不均匀 process step 上的 deficiency，\\n      在 downstream reasoning 上超越标准 GRPO 且训练更快收敛。\\n    relevance_to_freige: >\\n      DocRE structured output（multi-triple generation）可视为多步 process。\\n      GRPO 隐式的 PRM 性质可能解释了为什么 extraction-only reward\\n      在文档级 multi-triple 场景下训练信号不足——单一 outcome reward\\n      无法为每个 triple 的生成步骤提供有效 process-level credit assignment。\\n      CED 通过 evidence quality 为每个 triple 提供了更细粒度的信号，\\n      等效于增强了 process-level reward 的分辨率。\\n\\n  - title: \\\"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges\\\"\\n    authors: Wang et al. (23 authors)\\n    year: 2026\\n    venue: arXiv 2604.13602\\n    url: https://arxiv.org/abs/2604.13602\\n    category: grpo_theory\\n    role: theoretical_framework\\n    key_finding: >\\n      提出 Proxy Compression Hypothesis (PCH)：reward hacking 源于 objective compression、\\n      optimization amplification、evaluator-policy co-adaptation 三者交互。\\n      识别了 perception-reasoning decoupling 作为多模态中 reward hacking 的表现之一。\\n    relevance_to_freige: >\\n      PCH 框架可解释我们观察到的 extraction-evidence decoupling：\\n      QLoRA 的 compressed representation space 下，模型可能将 extraction 和 evidence\\n      两个子目标压缩到部分重叠的 proxy 空间，导致 optimization amplification\\n      使模型专注于更容易优化的 extraction 而忽略 evidence。\\n      bf16 下不复现可能因为 full-rank update 的 representation space 更充裕。\\n\\n  # === Category 16: Training Precision & RL Stability (NEW - 2026-05-15 scan) ===\\n\\n  - title: \\\"Defeating the Training-Inference Mismatch via FP16\\\"\\n    authors: Qi, Liu, Zhou, Pang, Du, Lee, Lin\\n    year: 2025\\n    venue: arXiv 2510.26788\\n    url: https://arxiv.org/abs/2510.26788\\n    category: training_precision_rl\\n    role: key_evidence\\n    key_finding: >\\n      BF16 在 RL fine-tuning 中引入大的 rounding error 导致 training-inference 不一致，\\n      BF16 训练常在 150-600 步崩溃。仅切换到 FP16 即可消除不一致，\\n      提供更稳定训练、更快收敛和更优性能，只需改几行代码。\\n    relevance_to_freige: >\\n      直接相关我们的 QLoRA GRPO 不稳定性发现。QLoRA 在 4-bit 量化基础上\\n      使用 bf16/fp16 adapter，量化+低精度的 compounding error 可能是\\n      task decoupling 现象的底层原因之一。该论文提供了 precision-instability\\n      的机制解释，支持我们 \\\"QLoRA-specific decoupling\\\" 的发现——\\n      低精度 representation 放大了多目标 RL 中子任务间的 gradient 干扰。\\n\\n  # === Category 17: RL for Scientific IE (NEW - 2026-05-15 scan) ===\\n\\n  - title: \\\"R²GRPO: Better LLMs for Scientific Information Extraction with MimicSFT and Relevance and Rule-induced GRPO\\\"\\n    authors: Li, Di, Liu, Jing, Qiu, Chen\\n    year: 2025\\n    venue: arXiv 2505.22068\\n    url: https://arxiv.org/abs/2505.22068\\n    category: rl_for_ie\\n    role: related_method\\n    key_finding: >\\n      两阶段方法：MimicSFT（structured reasoning template，无需高质量 CoT 数据）\\n      + R²GRPO（relevance reward + rule-mining reward），\\n      在科学信息抽取 RE benchmark 上超越 baseline LLM 和 specialized supervised model。\\n    relevance_to_freige: >\\n      R²GRPO 的 rule-based reward 设计与我们的 CED reward 有相似动机——\\n      都是引入 task-specific 结构化 reward 替代单纯 F1 metric reward。\\n      差异：R²GRPO 的 rule 是 dataset-level 频繁模式（类似 Ru-LLM），\\n      CED 是 instance-level evidence faithfulness 判别。\\n      R²GRPO 未涉及 evidence generation 或 DocRE。\\n\\n  # === Category 18: LLM Alignment for IE (NEW - 2026-05-15 scan) ===\\n\\n  - title: \\\"ADELIE: Aligning Large Language Models on Information Extraction\\\"\\n    authors: Qi, Peng, Wang, Xu, Hou, Li\\n    year: 2024\\n    venue: EMNLP 2024\\n    url: https://arxiv.org/abs/2405.05008\\n    category: llm_ie_alignment\\n    role: key_baseline\\n    key_finding: >\\n      构建 IEInstruct 高质量 IE alignment 语料库，用 SFT + DPO 训练 ADELIE。\\n      支持 closed/open/on-demand IE 三种模式。\\n      基于 LLaMA-2-7B/LLaMA-3.2-3B/Qwen2.5-1.5B，在多个 held-out IE dataset 上达 SOTA。\\n    relevance_to_freige: >\\n      ADELIE 是 IE alignment 的代表性工作，用 SFT+DPO 替代 RSFT+GRPO。\\n      我们的工作与 ADELIE 在 training paradigm 上有可比性——\\n      ADELIE 用 DPO（offline preference optimization），我们用 RSFT（offline rejection sampling）。\\n      关键差异：ADELIE 覆盖通用 IE，不涉及 evidence generation 或 DocRE-specific challenges；\\n      我们专注于 DocRE + evidence grounding 的 trade-off。\\n\\n  # === Category 19: Unfaithful Reasoning / Post-Rationalization (NEW - 2026-05-15 scan) ===\\n\\n  - title: \\\"Chain-of-Thought Is Not Explainability\\\"\\n    authors: Barez et al.\\n    year: 2025\\n    venue: Oxford WhiteBox Technical Report\\n    url: https://aigi.ox.ac.uk/wp-content/uploads/2025/07/Cot_Is_Not_Explainability.pdf\\n    category: unfaithful_reasoning\\n    role: conceptual_support\\n    key_finding: >\\n      CoT 仅仅 rationalize（事后合理化）而非 report（忠实报告）模型的真实决策过程。\\n      小的操纵即可改变 CoT 的推理链但不改变模型实际决策。\\n      模型会 silently correct 错误而不在 CoT 中体现。\\n    relevance_to_freige: >\\n      支持我们 evidence generation 分析的一个维度：模型生成的 evidence sentences\\n      可能是 post-rationalization 而非真正驱动 RE 决策的信号。\\n      CED reranker 用 NLI verification 检查 evidence 的实际 entailment\\n      而非信任模型自报告的 evidence，本质上是对 post-rationalization 的防御。\\n\\n  - title: \\\"Characterizing Large Language Models as Rationalizers of Knowledge-Grounded Dialogue\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: ACL Findings 2024\\n    url: https://aclanthology.org/2024.findings-acl.484.pdf\\n    category: unfaithful_reasoning\\n    role: empirical_evidence\\n    key_finding: >\\n      LLM 在 knowledge-grounded dialogue 中普遍表现为 rationalizer 而非 faithful reasoner，\\n      模型的 explanation 与其实际使用的 knowledge evidence 不一致。\\n    relevance_to_freige: >\\n      与我们的发现呼应：DocRE 中模型可能输出看似合理的 evidence sentences\\n      但实际 RE 决策并不依赖这些 evidence。这解释了为什么 joint evidence+RE 生成\\n      对 RE 性能有负面影响——模型在学习生成 \\\"合理化解释\\\" 而非 \\\"可靠推理\\\"。\\n\\n  # === Category 20: Latent vs Explicit Reasoning Trade-off (NEW - 2026-05-15 scan) ===\\n\\n  - title: \\\"Reasoning Beyond Language: A Comprehensive Survey on Latent Chain-of-Thought Reasoning\\\"\\n    authors: Chen, Zhao, Xia, Lu, Wang, Chen, Zhang, Wang, Li, Shen\\n    year: 2025\\n    venue: arXiv 2505.16782\\n    url: https://arxiv.org/abs/2505.16782\\n    category: latent_vs_explicit_reasoning\\n    role: survey\\n    key_finding: >\\n      Latent CoT 将推理从显式 token generation 解耦到 hidden state computation，\\n      在多项任务上达到与显式 CoT 相当或更优的性能，同时推理速度提升 20 倍以上。\\n      显式 CoT 的 sequential token-level 推理是 applicability 的瓶颈。\\n    relevance_to_freige: >\\n      为 evidence generation trade-off 提供更广泛的理论视角：\\n      evidence sentences 作为显式推理步骤（类似 CoT tokens）可能不是最优的推理形式。\\n      我们的 CED reranker 可被视为将 evidence reasoning 从 generation-time 显式推理\\n      转移到 inference-time 的 NLI-based 验证——类似 latent-to-explicit 的范式转换，\\n      但方向相反：不是让推理隐式化，而是让验证外部化。\\n\\n  # =========================================================================\\n  # Related Work Survey (2026-05-15): 5 directions for FREIGE paper\\n  # =========================================================================\\n\\n  # === Category 21: Evidence-Based / Faithful DocRE (Direction 1) ===\\n\\n  - title: \\\"DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction\\\"\\n    authors: Youmi Ma, An Wang, Naoaki Okazaki\\n    year: 2023\\n    venue: EACL 2023\\n    url: https://arxiv.org/abs/2302.08675\\n    category: evidence_based_docre\\n    role: direct-competitor\\n    key_finding: >\\n      用 evidence 信息作为监督信号引导 DocRE 系统的 attention module 关注 evidence sentences。\\n      提出 evidence retrieval (ER) self-training 策略，在无 evidence 标注的大规模数据上自动生成\\n      silver evidence 训练 ER。DocRED 上 RE 和 ER 均达 SOTA。\\n      解决了 evidence retrieval 的两大问题：高内存消耗和标注有限。\\n    relevance_to_freige: >\\n      最重要的 evidence-based DocRE 先驱工作。DREEAM 用 evidence 引导 attention（encoder-based），\\n      我们用 evidence 引导 RL reward（generative LLM）。关键代际差异：\\n      (1) DREEAM 是 encoder-based（BERT/RoBERTa），我们是 LLM generative；\\n      (2) DREEAM 的 evidence 用于注意力监督，我们的 evidence 用于 reward 设计和 CED reranking；\\n      (3) DREEAM 未量化 evidence 对 RE 的 performance cost。\\n      Related Work 必引：evidence-based DocRE 的代表性工作。\\n\\n  - title: \\\"DocGNRE: Semi-automatic Data Enhancement for Document-Level Relation Extraction with Distant Supervision from Large Language Models\\\"\\n    authors: Junpeng Li, Zixia Jia, Zilong Zheng\\n    year: 2023\\n    venue: EMNLP 2023\\n    url: https://arxiv.org/abs/2311.07314\\n    category: evidence_based_docre\\n    role: method-component\\n    key_finding: >\\n      用 LLM（ChatGPT）+ NLI 模块半自动生成 relation triples，增强 DocRE 数据集。\\n      特别擅长 re-annotating long-tail relation types。提供四个增强训练数据集。\\n      解决了 vanilla in-context learning 无法处理 DocRE 大量细粒度 relation types 的问题。\\n    relevance_to_freige: >\\n      DocGNRE 的 NLI 验证模块与我们 CED reranker 的 NLI scoring 思路类似——\\n      都用 NLI 检查生成内容是否被文档支持。差异：DocGNRE 用 NLI 过滤数据增强，\\n      我们用 NLI 做 inference-time reranking。DocGNRE 关注数据质量，我们关注训练范式。\\n\\n  - title: \\\"CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction\\\"\\n    authors: Khai Phan Tran, Xue Li\\n    year: 2025\\n    venue: arXiv 2504.06529\\n    url: https://arxiv.org/abs/2504.06529\\n    category: evidence_based_docre\\n    role: direct-competitor\\n    key_finding: >\\n      用 attentional graph-based 架构捕捉同文档内语义相似实体对间的协作模式。\\n      文档转化为 bipartite graph（entity pair nodes + sentence nodes），\\n      三子图：Entity Pair 子图建模协作、Entity Pair-Sentence 子图捕捉语义关系、\\n      Sentence 子图辅助共指推理。在 DocRED 上 evidence retrieval 和 RE 均有提升。\\n    relevance_to_freige: >\\n      CDER 是最新的 encoder-based evidence retrieval 方法，验证了 evidence 对 DocRE 的价值。\\n      与我们的关键差异：(1) CDER 是 encoder-based pipeline，我们是 LLM generative；\\n      (2) CDER 用 evidence 作为输入特征，我们用 evidence quality 作为 reward/reranking 信号；\\n      (3) CDER 未探索 evidence generation 的 performance cost。\\n\\n  - title: \\\"Evidence-aware Document-level Relation Extraction\\\"\\n    authors: Xu T, Hua W, Qu J, Li Z, Xu J, Liu A et al.\\n    year: 2022\\n    venue: CIKM 2022\\n    url: https://dl.acm.org/doi/10.1145/3511808.3557313\\n    category: evidence_based_docre\\n    role: background\\n    key_finding: >\\n      将 evidence sentence selection 建模为序列决策问题，\\n      用 RL 机制选择支撑关系的 evidence sentences。\\n      在 DocRED 上验证 evidence-aware 方法的有效性。\\n    relevance_to_freige: >\\n      早期将 RL 用于 DocRE evidence 的工作。其 RL 用于 evidence selection 策略，\\n      我们的 RL 用于整体模型微调（GRPO/RSFT）。证实 RL+evidence+DocRE 的组合有研究价值。\\n\\n  # === Category 22: Faithfulness Cost in NLP (Direction 2) ===\\n\\n  - title: \\\"Does Faithfulness Conflict with Plausibility? An Empirical Study in Explainable AI across NLP Tasks\\\"\\n    authors: Xiaolei Lu, Jianghong Ma\\n    year: 2024\\n    venue: arXiv 2404.00140\\n    url: https://arxiv.org/abs/2404.00140\\n    category: faithfulness_cost\\n    role: evaluation\\n    key_finding: >\\n      在 sentiment analysis、intent detection、topic labeling 三个 NLP 任务上\\n      系统比较 faithfulness 和 plausibility 的关系。传统 perturbation-based 方法\\n      （Shapley value、LIME）可同时达到较高 faithfulness 和 plausibility。\\n      关键发现：faithfulness 和 plausibility 并非必然冲突，\\n      可通过双目标优化同时提升。\\n    relevance_to_freige: >\\n      提供了 faithfulness-plausibility 关系的实证基础。我们的 evidence generation\\n      可视为 plausibility（evidence 看起来合理）vs faithfulness（evidence 真正驱动 RE）的张力。\\n      CED reranker 的 NLI verification 本质上是在检查 faithfulness 而非仅 plausibility。\\n\\n  - title: \\\"Faithfulness vs. Plausibility: On the (Un)Reliability of Explanations from Large Language Models\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: arXiv 2402.04614\\n    url: https://arxiv.org/abs/2402.04614\\n    category: faithfulness_cost\\n    role: key_evidence\\n    key_finding: >\\n      LLM 擅长生成 plausible 的解释，但这些解释不一定 faithful——\\n      不与 LLM 的实际推理过程对齐。Self-explanations 的 reliability 存疑。\\n      LLM 的解释行为更像 post-hoc rationalization 而非真实推理报告。\\n    relevance_to_freige: >\\n      直接支持我们的核心论点：要求 LLM 在 DocRE 中同时生成 evidence 可能\\n      只是让模型学会 post-hoc rationalize，而非真正基于 evidence 做 RE。\\n      CED reranker 的外部 NLI verification 正是为了对抗这种 unreliable self-explanation。\\n\\n  - title: \\\"Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: EMNLP 2025\\n    url: https://aclanthology.org/2025.emnlp-main.504.pdf\\n    category: faithfulness_cost\\n    role: evaluation\\n    key_finding: >\\n      通过 unlearning 推理步骤来衡量 CoT 的 faithfulness。\\n      如果 unlearn 某个推理步骤后模型行为不变，说明该步骤不 faithful。\\n      揭示了 CoT 推理步骤的 faithfulness 在不同任务和模型间差异巨大。\\n    relevance_to_freige: >\\n      提供了量化 faithfulness 的方法论。可用类似思路评估我们模型生成的 evidence\\n      是否真正影响 RE 决策。CED reranker 的 evidence corruption test\\n      本质上是这种 faithfulness 检验的 inference-time 版本。\\n\\n  # === Category 23: LoRA/QLoRA Training Artifacts (Direction 3) ===\\n\\n  - title: \\\"LoRA vs Full Fine-tuning: An Illusion of Equivalence\\\"\\n    authors: Reece Shuttleworth, Jacob Andreas, Antonio Torralba, Pratyusha Sharma\\n    year: 2024\\n    venue: arXiv 2410.21228\\n    url: https://arxiv.org/abs/2410.21228\\n    category: lora_qlora_artifacts\\n    role: key_evidence\\n    key_finding: >\\n      LoRA 和 full fine-tuning 产生结构上根本不同的权重矩阵。LoRA 引入 intruder dimensions——\\n      奇异值分解中出现新的高秩奇异向量（与预训练权重高度不相似）。Full fine-tuning 不会。\\n      LoRA 的 forgetting 几乎全部集中在 intruder dimensions。\\n      缩小 intruder dimensions 的奇异值可显著恢复预训练分布建模能力，\\n      同时仅微小影响下游任务性能。\\n    relevance_to_freige: >\\n      直接解释我们的 QLoRA GRPO decoupling 现象。LoRA/QLoRA 的 intruder dimensions\\n      可能是 extraction-evidence decoupling 的结构性原因：\\n      4-bit 量化 + LoRA 低秩约束导致 extraction 和 evidence 任务被迫共享\\n      有限的 intruder dimensions，当 RL 优化 amplify 这些维度时，\\n      两个任务的 gradient 在 intruder space 中产生干扰导致 decoupling。\\n      bf16 full fine-tuning 无 intruder dimensions 问题，因此不复现。\\n\\n  - title: \\\"The Impact of LoRA on the Emergence of Clusters in Transformers\\\"\\n    authors: Hugo Koubbi, Louis Hernandez, Matthieu Boussard\\n    year: 2024\\n    venue: arXiv 2402.15415\\n    url: https://arxiv.org/abs/2402.15415\\n    category: lora_qlora_artifacts\\n    role: theoretical_support\\n    key_finding: >\\n      用 mean-field self-attention toy model 研究 LoRA fine-tuning 的 forgetting 机制。\\n      LoRA 作为低秩扰动作用于交互粒子系统（tokens）。\\n      发现关于扰动范数和 Transformer 深度的 phase transition：\\n      超过某个阈值后从 non-forgetting 转变为 forgetting behavior。\\n      理论上界 time-to-deviation 与扰动大小和谱特性相关。\\n    relevance_to_freige: >\\n      提供了 LoRA forgetting 的理论框架。我们的 QLoRA GRPO decoupling 可能\\n      对应 phase transition 的临界区域——4-bit 量化使扰动有效范数增大，\\n      加上 GRPO 的 online 更新持续增大扰动，更容易触发 forgetting/decoupling phase transition。\\n      bf16 下扰动范数更可控，因此保持在 non-forgetting phase。\\n\\n  - title: \\\"QeRL: Beyond Efficiency -- Quantization-enhanced Reinforcement Learning for LLMs\\\"\\n    authors: NVIDIA, MIT, HKU, THU\\n    year: 2025\\n    venue: arXiv 2510.11696\\n    url: https://arxiv.org/abs/2510.11696\\n    category: lora_qlora_artifacts\\n    role: direct-competitor\\n    key_finding: >\\n      标准量化引入静态确定性噪声，对 RL 后期训练不利。但精确控制的量化噪声\\n      可通过增加 policy entropy 促进探索。Adaptive Quantization Noise (AQN) 机制\\n      动态调整噪声。结合 NVFP4 + LoRA 实现 1.5x rollout 加速。\\n      首次在单张 H100 上实现 32B LLM 的 RL 训练。\\n    relevance_to_freige: >\\n      QeRL 证明量化噪声可以被利用而非消除。与我们的发现互补：\\n      我们发现 QLoRA 的量化在多目标 RL 中导致 task decoupling（负面影响），\\n      QeRL 发现适当控制的量化噪声可促进单目标 exploration（正面利用）。\\n      差异在于：单目标场景下噪声促进探索有益，\\n      多目标场景下噪声加剧不同子任务间的 gradient 干扰。\\n\\n  - title: \\\"The Impact of Quantization on Large Reasoning Model Reinforcement Learning\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: NeurIPS 2025 Workshop (Efficient Reasoning)\\n    url: https://arxiv.org/abs/2511.15694\\n    category: lora_qlora_artifacts\\n    role: key_evidence\\n    key_finding: >\\n      系统评估量化对 LRM RL 训练的影响。发现 quantization-aware RL training\\n      反而损害学习过程，PTQ 和 QLoRA 表现更好。\\n      post-RL 量化模型和 quantization-aware RL 模型在推理性能上存在显著差距。\\n    relevance_to_freige: >\\n      直接支持我们的观察：QLoRA GRPO 训练不稳定可能源于\\n      quantization 和 RL 优化的复杂交互。该论文在数学推理任务上的发现\\n      与我们在 DocRE 上的 task decoupling 观察一致——\\n      量化在 RL 训练过程中引入系统性干扰。\\n\\n  # === Category 24: GRPO / Online RL for NLP Beyond RLHF (Direction 4) ===\\n\\n  - title: \\\"ReasoningNER: A Reasoning Paradigm for Named Entity Recognition\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2511.11978\\n    url: https://arxiv.org/abs/2511.11978\\n    category: grpo_nlp_applications\\n    role: direct-competitor\\n    key_finding: >\\n      三阶段 NER 框架：CoT Generation → CoT Tuning → GRPO Reasoning Enhancement。\\n      用 composite reward（entity F1 + format compliance）训练 GRPO policy。\\n      ReasoningNER-8B 零样本超 GPT-4 12.3 F1、超 DeepSeek-R1-32B 8.4 F1，\\n      1.7B 版本超 DeepSeek-R1-8B 10.5 F1。\\n    relevance_to_freige: >\\n      GRPO 成功应用于 IE（NER）的案例。NER reward 结构相对简单（entity-level F1），\\n      reward variance 天然较高（不同 span 组合产生多样 F1 分数）。\\n      再次支持：结构简单的 IE 任务 GRPO 成功，\\n      文档级多 triple + evidence 的复杂任务需要额外设计（CED/RSFT）。\\n\\n  - title: \\\"Posterior-GRPO: Rewarding Reasoning Processes in Code Generation\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2508.05170\\n    url: https://arxiv.org/abs/2508.05170\\n    category: grpo_nlp_applications\\n    role: method-component\\n    key_finding: >\\n      在代码生成中仅对成功输出的推理过程施加 process-based reward（条件 reward），\\n      有效抑制 reward hacking——模型不能通过错误推理碰巧生成正确代码来获得高 reward。\\n      通过将 reward 条件化于最终正确性，对齐内部推理与代码正确性。\\n    relevance_to_freige: >\\n      P-GRPO 的\\\"仅对成功输出奖励推理过程\\\"与我们 RSFT 的 rejection sampling 理念一致——\\n      都是只从高质量输出中学习。P-GRPO 的 conditional reward 思路可启发 CED 改进：\\n      只在 RE 正确时奖励 evidence quality，避免\\\"evidence 好但 RE 错\\\"的情况。\\n\\n  # === Category 25: Rejection Sampling Fine-Tuning / Offline RL (Direction 5) ===\\n\\n  - title: \\\"OREO: Offline Reinforcement Learning for LLM Multi-Step Reasoning\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: arXiv 2412.16145\\n    url: https://arxiv.org/abs/2412.16145\\n    category: rsft_offline_rl\\n    role: direct-competitor\\n    key_finding: >\\n      基于 maximum entropy RL 的 offline 方法，联合学习 policy model 和 value function，\\n      优化 soft Bellman Equation。无需 paired preference data，\\n      实现更好的 credit assignment。学到的 value function 可免费引导 test-time tree search。\\n      在 GSM8K、MATH、ALFWorld 上超越现有 offline 方法。\\n    relevance_to_freige: >\\n      OREO 提供了比简单 RSFT 更理论化的 offline RL 框架。\\n      我们的 RSFT 可视为 OREO 的特例（无 value function，简单 threshold filtering）。\\n      Future work 方向：用 OREO 替代简单 RSFT 可能进一步提升 DocRE 性能。\\n\\n  - title: \\\"PCL-Reasoner-V1.5: Advancing Math Reasoning with Offline Reinforcement Learning\\\"\\n    authors: Yao Lu, Dengdong Fan, Jianzheng Nie, Fan Xu, Jie Chen, Bin Zhou, Yonghong Tian\\n    year: 2026\\n    venue: arXiv 2601.14716\\n    url: https://arxiv.org/abs/2601.14716\\n    category: rsft_offline_rl\\n    role: key_evidence\\n    key_finding: >\\n      基于 Qwen2.5-32B 的数学推理模型。核心创新是 offline RL 方法，\\n      在训练稳定性和效率上优于 GRPO 等 online RL。\\n      AIME 2024 平均 90.9%，AIME 2025 平均 85.6%，\\n      在 Qwen2.5-32B post-training 中达 SOTA。\\n    relevance_to_freige: >\\n      强有力证据支持 offline RL > online RL 的论点。\\n      PCL-Reasoner 在数学推理上用 offline RL 超越 GRPO，\\n      与我们在 DocRE 上 RSFT 超越 GRPO 的发现一致。\\n      两个独立领域的 converging evidence 增强了\\n      \\\"structured output 任务中 offline 方法优于 online GRPO\\\"的普遍性论述。\\n\\n  - title: \\\"RS-DPO: A Hybrid Rejection Sampling and Direct Preference Optimization Method for Alignment of Large Language Models\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: NAACL 2024 Findings\\n    url: https://arxiv.org/abs/2402.10038\\n    category: rsft_offline_rl\\n    role: method-component\\n    key_finding: >\\n      系统性结合 rejection sampling 和 DPO。从 SFT 模型采样 k 个 response per prompt，\\n      根据 reward 分布识别 contrastive pairs，用 DPO 对齐。\\n      在有限资源环境下有效微调 LLM，超越独立的 RS、PPO 和 DPO。\\n    relevance_to_freige: >\\n      RS-DPO 提供了 rejection sampling 和 preference optimization 的桥梁方法。\\n      我们的 RSFT 只用正样本训练（SFT loss），RS-DPO 进一步利用负样本构造 preference pair。\\n      Future work 方向：可考虑用 RS-DPO 方式利用 RSFT rejected 样本做 DPO。\\n\\n  - title: \\\"RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: TMLR 2024\\n    url: https://arxiv.org/abs/2304.06767\\n    category: rsft_offline_rl\\n    role: background\\n    key_finding: >\\n      RAFT 是 rejection sampling fine-tuning 的标准化框架：迭代式 generate → rank → filter → SFT。\\n      每轮生成 n 个 response，用 reward model 排序，取 top-k 做 SFT。\\n      在文本生成和对话上验证有效性，提供了 RSFT 的 canonical 实现。\\n    relevance_to_freige: >\\n      我们的 RSFT pipeline 直接基于 RAFT 框架。差异在于：\\n      (1) 我们用 verifiable reward（F1 score）替代 learned reward model；\\n      (2) 我们的 filtering 基于 extraction F1 threshold 而非 top-k ranking；\\n      (3) 我们额外引入 CED reward 维度用于 inference-time reranking。\\n\\n  # === Category 7: Evidence-based DocRE (Expanded) ===\\n\\n  - title: \\\"EAAGRE: Evidence and Axial Attention Guided Document-level Relation Extraction\\\"\\n    authors: Unknown (Computer Speech and Language)\\n    year: 2024\\n    venue: Computer Speech and Language 2024\\n    url: https://www.sciencedirect.com/science/article/abs/pii/S0885230824001116\\n    category: evidence_docre\\n    role: related_method\\n    key_finding: >\\n      联合考虑 evidence information 和 relation triple 的全局交互。\\n      直接引导 PLM encoder 最后一层的 top-k token attention 到 evidence sentences，\\n      不引入额外可训练参数。Axial attention 建模 relation triple 之间的全局相互依赖。\\n    relevance_to_freige: >\\n      与 DREEAM 属于同一 evidence-guided attention 范式。\\n      EAAGRE 的无参数 evidence attention 与我们 CED reranker 的 post-hoc 方式形成对比——\\n      前者在 encoder 内部注入 evidence signal，后者在 generation 后验证。\\n      证明 evidence 信号无论注入位置都能提升 DocRE 性能。\\n\\n  - title: \\\"GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction\\\"\\n    authors: Yanxu Mao et al.\\n    year: 2024\\n    venue: arXiv 2407.21384\\n    url: https://arxiv.org/abs/2407.21384\\n    category: evidence_docre\\n    role: related_method\\n    key_finding: >\\n      用 GCN 构建多权重矩阵引导 attention 到 evidence sentences。\\n      采用 Teacher-Student 框架：Teacher 在全监督数据上推断 evidence 并分配 token 权重，\\n      Student 用这些权重作为监督信号训练。\\n    relevance_to_freige: >\\n      GEGA 的 Teacher-Student evidence distillation 与我们的 CED reranker 在动机上一致——\\n      都试图把 evidence quality 信号从外部注入 RE 系统。\\n      差异在于 GEGA 在 training-time 蒸馏，我们在 inference-time rerank。\\n\\n  - title: \\\"KnowRA: Knowledge Retrieval Augmented Method for Document-level Relation Extraction with Comprehensive Reasoning Abilities\\\"\\n    authors: Chengcheng Mai et al.\\n    year: 2025\\n    venue: IJCAI 2025\\n    url: https://arxiv.org/abs/2501.00571\\n    category: evidence_docre\\n    role: related_method\\n    key_finding: >\\n      通过外部知识库检索增强 DocRE 推理。构建 document graph 并用共指消解增强，\\n      检索外部知识扩展为 document knowledge graph，并用知识过滤去除无关知识。\\n      Axial attention 建立跨句逻辑推理。\\n    relevance_to_freige: >\\n      KnowRA 代表 DocRE 中\\\"更多外部信号\\\"路线，与我们\\\"让模型自己生成 evidence\\\"路线形成对比。\\n      我们的工作表明 evidence generation 有固有代价（faithfulness tax），\\n      KnowRA 绕过这个问题通过检索而非生成。\\n\\n  # === Category 8: Faithfulness in Structured Output / Evidence Quality ===\\n\\n  - title: \\\"G&O: A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction\\\"\\n    authors: Yinghao Li et al.\\n    year: 2024\\n    venue: arXiv 2402.13364\\n    url: https://arxiv.org/abs/2402.13364\\n    category: faithfulness_structured\\n    role: related_method\\n    key_finding: >\\n      将 structured IE 拆为两步：先用自然语言生成内容，再组织为目标结构。\\n      G&O 有效分离内容生成和结构化过程，减轻同时完成两个正交任务的压力。\\n      在 zero-shot NER 和 RE 上显著提升 LLM 性能。\\n    relevance_to_freige: >\\n      直接支持我们的核心发现：要求模型同时做 relation extraction 和 evidence generation\\n      相当于同时做内容生成+结构化，两个任务存在固有冲突。\\n      G&O 的 decouple 策略与我们观察到的 task decoupling 现象相呼应，\\n      但 G&O 是 prompting 层面的解耦，我们发现 RL training 中的自发解耦。\\n\\n  - title: \\\"Improved Evidence Extraction and Metrics for Document Inconsistency Detection with LLMs\\\"\\n    authors: Nelvin Tan et al.\\n    year: 2026\\n    venue: arXiv 2601.02627\\n    url: https://arxiv.org/abs/2601.02627\\n    category: faithfulness_structured\\n    role: related_method\\n    key_finding: >\\n      引入新的 evidence extraction 评估指标和 redact-and-retry 框架。\\n      提出 constrained filtering 方法，显著优于直接 prompting 的 evidence extraction。\\n      发布新的 semi-synthetic 数据集用于评估 evidence extraction。\\n    relevance_to_freige: >\\n      为 evidence extraction 质量评估提供新指标框架。\\n      我们的 EDCR 指标从 DocRE 角度评估 evidence quality，\\n      该工作从 document inconsistency 角度评估——两者互补。\\n      其 redact-and-retry 框架可启发 CED reranker 的迭代改进策略。\\n\\n  - title: \\\"Diagnosing Structural Failures in LLM-Based Evidence Extraction for Meta-Analysis\\\"\\n    authors: Unknown\\n    year: 2026\\n    venue: arXiv 2602.10881\\n    url: https://arxiv.org/abs/2602.10881\\n    category: faithfulness_structured\\n    role: supporting_evidence\\n    key_finding: >\\n      LLM 在结构化 evidence extraction 中存在系统性 structural breakdown：\\n      role reversal、cross-analysis binding drift、instance compression、numeric misattribution。\\n      当任务需要稳定绑定 variables/roles/methods/effect-sizes 时性能急剧下降。\\n    relevance_to_freige: >\\n      强化我们的核心论点：LLM 生成结构化 evidence 存在系统性困难。\\n      我们发现的 faithfulness tax 可视为这类 structural failure 在 DocRE 场景的具体表现——\\n      模型在维持 relation extraction 准确性的同时难以忠实绑定 evidence sentences。\\n\\n  - title: \\\"Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion (APIE)\\\"\\n    authors: Unknown\\n    year: 2025\\n    venue: AAAI 2026\\n    url: https://arxiv.org/abs/2508.10036\\n    category: faithfulness_structured\\n    role: related_method\\n    key_finding: >\\n      提出 dual-component uncertainty metric 量化 LLM 在 IE 中的 Format Uncertainty\\n      （结构语法困难）和 Content Uncertainty（语义不一致）。\\n      利用 introspective confusion 主动选择 few-shot examples 提升 IE 性能。\\n    relevance_to_freige: >\\n      APIE 的 format vs content uncertainty 分解与我们观察到的 RE vs evidence 冲突类似——\\n      format uncertainty 对应 structured output 的结构要求，\\n      content uncertainty 对应 evidence faithfulness。\\n      为理解 faithfulness tax 的来源提供额外理论视角。\\n\\n  # === Category 9: RLHF/GRPO for Structured Tasks (Expanded) ===\\n\\n  - title: \\\"GRPO-LEAD: A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models\\\"\\n    authors: Jixiao Zhang, Chunsheng Zuo\\n    year: 2025\\n    venue: EMNLP 2025\\n    url: https://arxiv.org/abs/2504.09696\\n    category: grpo_structured\\n    role: related_method\\n    key_finding: >\\n      增强 GRPO：(1) length-regularized rewards 鼓励简洁性；\\n      (2) 对错误解的显式惩罚提升精度；\\n      (3) difficulty-aware advantage reweighting 增强泛化。\\n      解决 GRPO 的 reward sparsity、verbosity 和难度忽视问题。\\n    relevance_to_freige: >\\n      GRPO-LEAD 的 length penalty 与我们观察到的 evidence generation 增加输出长度导致性能下降相关。\\n      其 difficulty-aware reweighting 可启发 CED reward 对不同难度 relation triple 的差异化处理。\\n      但 GRPO-LEAD 针对数学推理的单一任务，我们面对 multi-objective（RE + evidence）。\\n\\n  - title: \\\"E-GRPO: Entity-Aware Reward for Group Relative Policy Optimization\\\"\\n    authors: Unknown\\n    year: 2025\\n    venue: ICLR 2026\\n    url: https://arxiv.org/pdf/2510.24694\\n    category: grpo_structured\\n    role: closest_prior_work\\n    key_finding: >\\n      提出 entity-aware reward function，对 negative samples 基于 entity match rate 给 partial credit。\\n      利用 ground-truth entities 作为 factual correctness 的 proxy，\\n      区分 \\\"near-miss\\\"（中间推理正确但最终答案错误）和完全失败。\\n    relevance_to_freige: >\\n      E-GRPO 的 entity-aware partial credit 与我们 CED reward 的设计理念高度一致——\\n      都是引入 task-specific fine-grained reward signal 替代 binary reward。\\n      差异在于 E-GRPO 用 entity match 作为 reward，我们用 evidence quality (NLI-based)。\\n      E-GRPO 是 training-time reward，CED 是 inference-time reranking。\\n\\n  - title: \\\"RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs\\\"\\n    authors: Hangzhan Jin et al.\\n    year: 2025\\n    venue: arXiv 2508.16546\\n    url: https://arxiv.org/abs/2508.16546\\n    category: grpo_structured\\n    role: supporting_evidence\\n    key_finding: >\\n      RL-FT 可恢复 SFT 导致的大部分 OOD 性能损失，但当 SFT 造成严重 overfitting 时 RL 无法完全恢复。\\n      OOD 性能退化和恢复主要与 singular vector 方向旋转相关，而非 singular value 变化。\\n      恢复 top 20% singular values 对应方向可恢复 70-80% OOD 性能。\\n    relevance_to_freige: >\\n      解释我们的 RSFT→GRPO pipeline 设计合理性。\\n      RSFT（SFT 变体）可能引入 distribution shift，后续 GRPO 可部分修复。\\n      但如果 RSFT 过度拟合单一任务（如只优化 F1），GRPO 的修复能力有限——\\n      这与我们观察到的 QLoRA GRPO 中 task decoupling 一致。\\n\\n  - title: \\\"Aligning Instruction-Tuned LLMs for Event Extraction with Multi-objective Reinforcement Learning\\\"\\n    authors: Unknown\\n    year: 2025\\n    venue: Springer 2025\\n    url: https://link.springer.com/chapter/10.1007/978-3-032-21300-6_50\\n    category: grpo_structured\\n    role: related_method\\n    key_finding: >\\n      将多目标强化学习应用于事件抽取，在 instruction-tuned LLM 基础上用 RL 优化抽取性能。\\n      证明 RL 在 IE 任务中可以有效提升 LLM 的结构化输出质量。\\n    relevance_to_freige: >\\n      与我们的 GRPO for DocRE 属于同一 paradigm——用 RL 优化 IE 任务的 LLM。\\n      事件抽取的多目标（trigger identification + argument extraction）\\n      与 DocRE 的多目标（relation extraction + evidence generation）有结构相似性。\\n\\n  # === Category 10: QLoRA vs Full Fine-tuning (Expanded) ===\\n\\n  - title: \\\"How Much is Too Much? Exploring LoRA Rank Trade-offs for Retaining Knowledge and Domain Robustness\\\"\\n    authors: Darshita Rathore et al.\\n    year: 2025\\n    venue: IJCNLP-AACL 2025\\n    url: https://arxiv.org/abs/2512.15634\\n    category: qlora_fft_gap\\n    role: supporting_evidence\\n    key_finding: >\\n      中等 rank (r=32-64) 在表征能力和稳定性之间达到最佳平衡。\\n      LoRA 在某些推理任务上可与 full fine-tuning 媲美甚至超越。\\n      跨域评估时 LoRA-tuned 模型展现出 robust generalization，\\n      表明 LoRA 学习的是可迁移的抽象技能而非记忆领域特定事实。\\n    relevance_to_freige: >\\n      为我们的 QLoRA rank 选择提供实证指导。\\n      我们使用的 QLoRA (r=16) 可能处于 rank 不足区间，\\n      解释为何 QLoRA GRPO 出现 task decoupling——rank 太低无法同时编码两个任务的更新。\\n      建议未来实验尝试 r=32-64 观察是否缓解 decoupling。\\n\\n  - title: \\\"RandLoRA: Full-rank Parameter-Efficient Fine-tuning of Large Models\\\"\\n    authors: Paul Albert et al.\\n    year: 2025\\n    venue: ICLR 2025\\n    url: https://arxiv.org/abs/2502.00987\\n    category: qlora_fft_gap\\n    role: related_method\\n    key_finding: >\\n      通过学习 fixed random matrices 的 diagonal scaling 实现 full-rank 更新，\\n      保持参数效率同时突破 low-rank 限制。\\n      在 vision-language 任务上显著缩小甚至消除 standard fine-tuning 与 LoRA 的性能差距。\\n    relevance_to_freige: >\\n      直接回应我们的 QLoRA 限制问题。\\n      如果 QLoRA 的 low-rank 约束导致 multi-objective GRPO 中 task decoupling，\\n      RandLoRA 的 full-rank PEFT 可能是解决方案——\\n      在保持内存效率的同时提供足够的表征能力同时编码 RE 和 evidence generation。\\n\\n  # === Category 11: Multi-task Learning Trade-offs in IE (Expanded) ===\\n\\n  - title: \\\"C-LoRAE: Collaborative Multi-LoRA Experts with Achievement-based Multi-Tasks Loss for Unified Multimodal Information Extraction\\\"\\n    authors: Unknown\\n    year: 2025\\n    venue: arXiv 2505.06303\\n    url: https://arxiv.org/abs/2505.06303\\n    category: mtl_ie_tradeoff\\n    role: closest_prior_work\\n    key_finding: >\\n      扩展 LoRA 引入 universal expert（跨任务共享知识）和 task-specific experts。\\n      用 mutual information maximization 促进 expert 间信息交换。\\n      Achievement-based multi-task loss 根据当前各任务性能动态平衡训练进度。\\n    relevance_to_freige: >\\n      C-LoRAE 的 universal + task-specific expert 架构直接对应我们的 RE + evidence 多任务设定。\\n      其 achievement-based loss 可启发 CED reward 中 RE 和 evidence 维度的动态权重调整。\\n      C-LoRAE 从架构层面解决 gradient conflict，我们从 reward design 层面解决。\\n\\n  - title: \\\"Ortho-LoRA: Disentangling Task Conflicts in Multi-Task LoRA via Orthogonal Gradient Projection\\\"\\n    authors: Ziyu Yang et al.\\n    year: 2026\\n    venue: arXiv 2601.09684\\n    url: https://arxiv.org/abs/2601.09684\\n    category: mtl_ie_tradeoff\\n    role: related_method\\n    key_finding: >\\n      针对 LoRA 的 bipartite 结构设计 gradient projection 方法。\\n      动态将冲突任务梯度投影到彼此的正交补空间，在 LoRA 固有子空间内解决冲突。\\n      解决 multi-task LoRA 中的 negative transfer 问题。\\n    relevance_to_freige: >\\n      直接解释我们的 QLoRA GRPO task decoupling：\\n      RE 和 evidence generation 的 gradient 在 low-rank 空间中冲突，\\n      QLoRA 的有限容量加剧这种冲突导致 task 自发解耦。\\n      Ortho-LoRA 的正交投影方法可作为 QLoRA GRPO 的改进方向。\\n\\n  - title: \\\"Proactive Gradient Conflict Mitigation in Multi-Task Learning: A Sparse Training Perspective\\\"\\n    authors: Zhi Zhang et al.\\n    year: 2024\\n    venue: arXiv 2411.18615\\n    url: https://arxiv.org/abs/2411.18615\\n    category: mtl_ie_tradeoff\\n    role: supporting_evidence\\n    key_finding: >\\n      从 Sparse Training 角度缓解 gradient conflict：\\n      选择原始模型参数子集同时学习多任务，冻结其余参数。\\n      将高维空间优化问题转为低维问题，限制每个任务的 gradient update 影响范围。\\n      可与 gradient manipulation 技术结合进一步提升效果。\\n    relevance_to_freige: >\\n      QLoRA 本质上就是一种 sparse training（只更新 low-rank adapter），\\n      但 sparse training 的 proactive conflict mitigation 需要 task-aware 的参数选择，\\n      而 QLoRA 的参数选择是 task-agnostic 的。\\n      这解释了为什么 QLoRA 在 multi-objective GRPO 中表现不如预期——\\n      它的 sparsity 模式不是为多任务优化设计的。\\n\\n  # === Category 12: Generative IE Surveys ===\\n\\n  - title: \\\"Large Language Models for Generative Information Extraction: A Survey\\\"\\n    authors: Unknown\\n    year: 2024\\n    venue: Frontiers of Computer Science 2024\\n    url: https://arxiv.org/abs/2312.17617\\n    category: survey\\n    role: survey\\n    key_finding: >\\n      全面综述 LLM 在 IE 各子任务（NER、RE、EE 等）中的应用。\\n      按 IE 子任务和技术分类，实证分析最先进方法和新兴趋势。\\n      指出 LLM-based IE 面临 structured output 质量和效率挑战。\\n    relevance_to_freige: >\\n      为我们的工作提供 broader context。FREIGE 属于 generative IE 范式——\\n      用 LLM 生成结构化 RE 输出。该 survey 的分类框架帮助定位 FREIGE 在 generative IE 生态中的位置：\\n      我们是首个系统研究 generative DocRE 中 evidence generation 代价的工作。\\n\\n  # === Category 13: Inference-Time Reranking / Best-of-N (New from 2025-05-16 scan) ===\\n\\n  - title: \\\"Is Best-of-N the Best of Them? Coverage, Scaling, and Optimality in Inference-Time Alignment\\\"\\n    authors: Audrey Huang et al.\\n    year: 2025\\n    venue: ICML 2025\\n    url: https://arxiv.org/abs/2503.21878\\n    category: inference_time_reranking\\n    role: key_baseline\\n    key_finding: >\\n      Best-of-N sampling provably suffers from reward hacking when N is large.\\n      提出 InferenceTimePessimism 算法，通过 pessimism in the face of uncertainty\\n      实现 scaling-monotonic 性能（性能不随 N 增大而退化）。\\n      强调 pre-trained policy 对高质量 response 的 coverage 是 BoN 成功的关键。\\n    relevance_to_freige: >\\n      直接对应 CED reranker 的理论基础。CED 作为 inference-time reward model 选择最佳候选，\\n      该论文的 pessimism 原则可指导 CED reranker 的 threshold 设计——\\n      避免过度信任 CED score 导致 reward hacking。\\n\\n  - title: \\\"Inference-Time Reward Hacking in Large Language Models\\\"\\n    authors: Yiwei Chen et al.\\n    year: 2025\\n    venue: NeurIPS 2025 Spotlight\\n    url: https://arxiv.org/abs/2506.19248\\n    category: inference_time_reranking\\n    role: related_analysis\\n    key_finding: >\\n      证明 BoN 中 true reward 先升后降的 hacking pattern 是所有 inference-time 机制的固有属性。\\n      提出 Best-of-Poisson (BoP) 高效近似最优 reward-KL tradeoff policy，\\n      以及 HedgeTune 自动寻找最优 inference-time 参数。\\n    relevance_to_freige: >\\n      CED reranker 本质上是 inference-time 对齐。此论文警示：\\n      即使 CED score 是高质量 reward，过度优化（选 N 过大）仍可能退化。\\n      HedgeTune 的思路可用于自动选择 CED reranker 的最优 N。\\n\\n  - title: \\\"Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models\\\"\\n    authors: Yinlam Chow et al.\\n    year: 2024\\n    venue: ICLR 2025\\n    url: https://arxiv.org/abs/2412.15287\\n    category: inference_time_reranking\\n    role: method_component\\n    key_finding: >\\n      提出 inference-aware fine-tuning 范式：训练时直接优化 BoN inference 策略的性能。\\n      设计 imitation learning 和 RL 方法克服 BoN 中不可微的 argmax 操作。\\n      BoN-aware 模型隐式学习 exploration-exploitation meta-strategy，\\n      交替生成最优 response 和多样性 response。\\n    relevance_to_freige: >\\n      FREIGE 的 RSFT+CED reranker 是 train-then-rerank 两阶段。\\n      此论文暗示更优方案：将 CED reranker 信号直接融入训练目标，\\n      使模型生成 BoN-aware 的多样输出而非事后选择。\\n\\n  - title: \\\"Evaluation of Best-of-N Sampling Strategies for Language Model Alignment\\\"\\n    authors: Yuki Ichihara et al.\\n    year: 2025\\n    venue: TMLR 2025\\n    url: https://arxiv.org/abs/2502.12668\\n    category: inference_time_reranking\\n    role: evaluation\\n    key_finding: >\\n      系统评估 BoN 采样的 reward hacking 问题。\\n      提出 Stochastic Regularized BoN (SRBoN) 有理论保证的方法。\\n      发现简单的 Sentence Length Regularized BoN 也能获得 comparable 性能。\\n    relevance_to_freige: >\\n      CED reranker 的 regularization 策略参考。\\n      FREIGE 中 CED score 作为 evidence quality proxy，\\n      可借鉴 SRBoN 的正则化思路防止 CED reranker over-optimize evidence 而牺牲 extraction quality。\\n\\n  - title: \\\"Regularized Best-of-N Sampling with Minimum Bayes Risk Objective for Language Model Alignment\\\"\\n    authors: Yuu Jinnai et al.\\n    year: 2024\\n    venue: NAACL 2025\\n    url: https://arxiv.org/abs/2404.01054\\n    category: inference_time_reranking\\n    role: related_method\\n    key_finding: >\\n      MBR-BoN：用 Minimum Bayes Risk 目标作为 proximity regularizer 缓解 reward hacking。\\n      MBR 目标量化 response 与 reference policy 的接近程度。\\n      在 AlpacaFarm 和 hh-rlhf 上优于 vanilla BoN 和 MBR decoding。\\n    relevance_to_freige: >\\n      CED reranker 可借鉴 MBR 正则化——在选择最高 CED score 候选时，\\n      同时考虑候选与 base policy 的接近程度，防止选择过度偏离 extraction pattern 的输出。\\n\\n  # === Category 14: RSFT Methodology Advances (New from 2025-05-16 scan) ===\\n\\n  - title: \\\"AdaSTaR: Adaptive Data Sampling for Training Self-Taught Reasoners\\\"\\n    authors: Hyung Won Chung et al.\\n    year: 2025\\n    venue: NeurIPS 2025\\n    url: https://arxiv.org/abs/2505.16322\\n    category: rsft_methodology\\n    role: related_method\\n    key_finding: >\\n      RFT/RSFT 的随机数据采样导致训练不均衡——已解决的样本被过度训练，困难样本训练不足。\\n      AdaSTaR 引入两个自适应采样原则：(1) diversity sampling 促进均衡，\\n      (2) curriculum sampling 根据模型能力动态调整数据难度。\\n      在 6 个 benchmark 全部取得最优，训练 FLOPs 平均减少 58.6%。\\n    relevance_to_freige: >\\n      直接适用于 FREIGE 的 RSFT 阶段。当前 RSFT 随机采样 CED-filtered 数据，\\n      AdaSTaR 的 curriculum 策略可优化采样——先训简单 relation pair，再逐步引入困难的多跳关系。\\n      其 diversity sampling 也可缓解 RSFT 数据中 relation type 分布不均的问题。\\n\\n  - title: \\\"RIFT: Repurposing Negative Samples via Reward-Informed Fine-Tuning\\\"\\n    authors: Unknown\\n    year: 2026\\n    venue: arXiv 2601.09253\\n    url: https://arxiv.org/abs/2601.09253\\n    category: rsft_methodology\\n    role: direct_competitor\\n    key_finding: >\\n      RSFT 的 hard rejection 丢弃大量计算昂贵的负样本。\\n      RIFT 保留所有轨迹，用标量 reward 重新加权 loss，\\n      正 reward 样本鼓励正确行为，负 reward 样本提供反向梯度。\\n      引入 stabilized loss 解决 naive reward integration 的训练坍塌问题。\\n    relevance_to_freige: >\\n      FREIGE 的 RSFT 同样面临 hard rejection 的效率问题——大量生成但 CED 不达标的样本被丢弃。\\n      RIFT 的 soft reweighting 可替代 binary CED 筛选：\\n      用 CED score 作为连续 reward 加权 SFT loss，充分利用所有生成样本。\\n\\n  # === Category 15: NLI for Evidence Scoring / Faithfulness (New from 2025-05-16 scan) ===\\n\\n  - title: \\\"FaithLens: Detecting and Explaining Faithfulness Hallucination\\\"\\n    authors: Unknown\\n    year: 2025\\n    venue: arXiv 2512.20182\\n    url: https://arxiv.org/abs/2512.20182\\n    category: faithfulness_nli\\n    role: method_component\\n    key_finding: >\\n      8B 参数模型通过合成训练数据 + rule-based RL 优化，\\n      在 12 个 faithfulness 检测任务上超越 GPT-4.1 和 o3。\\n      联合预测 binary label 和生成解释，提升可信度。\\n    relevance_to_freige: >\\n      FaithLens 的方法验证了 CED 的核心假设：小模型可以做高质量 faithfulness 判断。\\n      其 rule-based RL 训练策略可启发 CED reward model 的进一步优化——\\n      除 NLI entailment score 外，加入 explanation quality reward。\\n\\n  - title: \\\"PrefixNLI: Detecting Factual Inconsistencies as Soon as They Arise\\\"\\n    authors: Sapir Harary et al.\\n    year: 2025\\n    venue: arXiv 2511.01359\\n    url: https://arxiv.org/abs/2511.01359\\n    category: faithfulness_nli\\n    role: method_component\\n    key_finding: >\\n      将 NLI 从完整句子推广到任意文本前缀，训练 MiniTruePrefixes 模型。\\n      在 prefix-level entailment 上超越 baseline NLI 模型 5-14 F1。\\n      集成到 controlled decoding 框架后，LLaMA-3.2-3B 匹配 8B 模型的 faithfulness。\\n    relevance_to_freige: >\\n      PrefixNLI 可强化 CED 的实时性：不必等生成完成再评估 evidence faithfulness，\\n      在 autoregressive 生成过程中即时检测 unfaithful evidence。\\n      可作为 GRPO training 中的 token-level reward signal。\\n\\n  - title: \\\"Revisiting NLI: Towards Cost-Effective and Human-Aligned Metrics for Evaluating LLMs in Question Answering\\\"\\n    authors: Unknown\\n    year: 2025\\n    venue: arXiv 2511.07659\\n    url: https://arxiv.org/abs/2511.07659\\n    category: faithfulness_nli\\n    role: evaluation\\n    key_finding: >\\n      轻量 NLI scoring + 简单 lexical-match flag 在 long-form QA 上匹配 GPT-4o 准确率 (89.9%)，\\n      参数量少几个数量级。引入 DIVER-QA benchmark（3000 样本，人工标注）。\\n    relevance_to_freige: >\\n      直接支持 CED 的设计选择：用轻量 NLI 模型（而非昂贵 LLM）评估 evidence quality。\\n      DIVER-QA 的评估方法可迁移到 DocRE evidence evaluation，\\n      验证 CED score 与人类判断的一致性。\\n\\n  - title: \\\"Benchmarking LLM Faithfulness in RAG with Evolving Leaderboards\\\"\\n    authors: Manveer Singh Tamber et al.\\n    year: 2025\\n    venue: EMNLP Industry 2025\\n    url: https://arxiv.org/abs/2505.04847\\n    category: faithfulness_nli\\n    role: evaluation\\n    key_finding: >\\n      FaithJudge 框架：利用多样化人工标注 hallucination 样本池改进 LLM-as-judge 评估。\\n      建立 evolving leaderboard 跟踪 LLM 在 RAG faithfulness 上的表现。\\n      覆盖 summarization、QA、data-to-text 三类任务。\\n    relevance_to_freige: >\\n      提供 faithfulness evaluation 的 benchmark 框架。\\n      FREIGE 的 EDCR 指标衡量 evidence-extraction decoupling，\\n      FaithJudge 的人工标注方法可用于验证 EDCR 指标的有效性。\\n\\n  # === Category 16: Evidence-Grounded DocRE Recent Work (New from 2025-05-16 scan) ===\\n\\n  - title: \\\"DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning\\\"\\n    authors: Xu et al.\\n    year: 2025\\n    venue: ICML 2025\\n    url: https://proceedings.mlr.press/v267/xu25am.html\\n    category: llm_docre\\n    role: direct_competitor\\n    key_finding: >\\n      构建 Document-level Knowledge Graph 捕获实体间结构信息，\\n      结合 Sentence-level Semantic RAG 检索相关上下文语义信息。\\n      设计 hybrid-prompt tuning 方法在 LLM 上集成结构和语义理解。\\n    relevance_to_freige: >\\n      ICML 2025 的 LLM-based DocRE 方法。与 FREIGE 的区别：\\n      DocKS-RAG 用 retrieval 增强输入，FREIGE 用 evidence generation 增强输出。\\n      DocKS-RAG 不显式生成 evidence，而 FREIGE 将 evidence 作为显式输出。\\n\\n  - title: \\\"COREX: Document-level Relation Extraction Framework with Consistent Two-Hop Reasoning and Evidence Sentence Prediction\\\"\\n    authors: Unknown\\n    year: 2024\\n    venue: IEEE IJCNN 2024\\n    url: https://ieeexplore.ieee.org/document/10650330/\\n    category: evidence_based_docre\\n    role: direct_competitor\\n    key_finding: >\\n      提出高效 two-hop reasoning 表示，由 evidence prediction 和 RE 联合监督。\\n      修正 Adaptive Focal Loss 解决类别不均衡。\\n      Weighted Fusion Layer 优化 evidence 利用。\\n    relevance_to_freige: >\\n      与 FREIGE 同属 evidence-enhanced DocRE，但方法路线不同：\\n      COREX 是 discriminative 模型用 evidence 注意力引导，\\n      FREIGE 是 generative 模型显式生成 evidence text。\\n      COREX 的 evidence-RE 联合训练与 FREIGE 的多任务 GRPO 思路类似。\\n\\n  - title: \\\"Grounded Knowledge Graph Extraction via LLMs: An Anchor-Constrained Framework with Provenance Tracking\\\"\\n    authors: Unknown\\n    year: 2025\\n    venue: Computers 2025\\n    url: https://www.mdpi.com/2073-431X/15/3/178\\n    category: evidence_based_docre\\n    role: related_method\\n    key_finding: >\\n      AEVS 框架：anchor discovery → grounded extraction → verification → supplement。\\n      为每个三元组提供 character-level provenance，使 faithfulness 可验证。\\n      Hallucination rate 0.23-20.23%，每样本 2.83-4.28 次 LLM 调用。\\n    relevance_to_freige: >\\n      AEVS 的 provenance tracking 理念与 FREIGE 的 evidence generation 一致——\\n      都试图让 extraction 结果可溯源。区别：AEVS 用 anchor 约束生成，\\n      FREIGE 用 CED reward 训练模型自主生成 faithful evidence。\\n      AEVS 的 verification 步骤类似 CED 的 entailment 检验。\\n\\n  # === Category 17: QLoRA/Quantization Fine-tuning Artifacts (New from 2025-05-16 scan) ===\\n\\n  - title: \\\"Accurate and Efficient Fine-Tuning of Quantized Large Language Models Through Optimal Balance in Adaptation\\\"\\n    authors: Shinhyuk Seo et al.\\n    year: 2024\\n    venue: TACL 2025\\n    url: https://arxiv.org/abs/2407.17029\\n    category: lora_qlora_artifacts\\n    role: related_analysis\\n    key_finding: >\\n      识别量化 LLM + LoRA 的不平衡问题：adapter 输入输出过于复杂而有效可训练性不足，导致欠拟合。\\n      Q-BLoRA 简化 adapter 输入输出同时增大 rank 缓解欠拟合。\\n      QA-BLoRA 进一步支持低精度部署。\\n    relevance_to_freige: >\\n      直接解释 FREIGE 中 QLoRA GRPO 导致 evidence-extraction decoupling 的机制：\\n      量化权重的有限表征精度 + LoRA 的 rank 限制 = 双重欠拟合，\\n      多任务（RE + evidence）在此瓶颈下竞争导致任务自发解耦。\\n      Q-BLoRA 的 balanced adaptation 可能缓解此问题。\\n\\n  - title: \\\"CLoQ: Enhancing Fine-Tuning of Quantized LLMs via Calibrated LoRA Initialization\\\"\\n    authors: Unknown\\n    year: 2025\\n    venue: arXiv 2501.18475\\n    url: https://arxiv.org/abs/2501.18475\\n    category: lora_qlora_artifacts\\n    role: related_method\\n    key_finding: >\\n      QLoRA 中量化误差影响 LoRA 训练。CLoQ 用校准数据集最小化原始 LLM 与量化+LoRA 版本的\\n      逐层差异，闭式构造最优 LoRA 初始化，无需反向传播。\\n      在 ultra low-bit 宽度下显著优于现有方法。\\n    relevance_to_freige: >\\n      CLoQ 的初始化策略可缓解 FREIGE 中 QLoRA GRPO 的起点问题——\\n      更好的 LoRA 初始化 → 更小的量化-原始模型差距 → \\n      GRPO 训练起步时 RE 和 evidence 任务的表征空间更均衡，可能减轻 decoupling。\\n\", \"total_chars\": 75613, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01W8sgxtBWXuy3wVWFNER4ws`</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "0a5a2ca0-76f2-4949-b5de-d308623b19c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UL8c4mr7hW1KSWVDEzVqfg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 454,
      "cache_read_input_tokens": 23597,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 454
      },
      "output_tokens": 33,
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

_source line 11 · 2026-05-16T00:39:47.881Z_

<details><summary>↩ Tool result · `toolu_01W8sgxtBWXuy3wVWFNER4ws`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/paper_framing.md\", \"content\": \"# Paper Framing — FREIGE\\n\\n> **状态**: POST-MVP + DREAM v2 完成（D047 分析）\\n> **最后更新**: 2026-05-16\\n> **Dream v1**: best=2.5, median=3.0, worst=2.5 → reframe 完成\\n> **Dream v2**: best=3.0, median=2.5, worst=2.5 → best 提升但 median 下降，未达标。关键路径：plan_011 bf16 GRPO eval + structural fixes → re-dream v3\\n\\n## Target Venue\\n\\n- Primary: **EMNLP 2026 Main** (ARR July cycle, ~July 15-25 → commit EMNLP Aug/Sep)\\n- Fallback: AAAI 2027 (abstract July 25, paper Aug 1)\\n\\n## Core Insight\\n\\nLLM-based document-level IE 已逼近 encoder SOTA 的抽取精度，但零方法能生成可验证证据。本文提出 **evidence-grounded DocRE** 作为新任务范式：LLM 同时输出关系三元组和支撑证据句。\\n\\n我们系统性地探索了 online RL (GRPO) 、offline preference optimization (DPO) 和 offline RL (RSFT) 三条技术路线。关键发现：**RL optimization pressure 与 evidence-extraction decoupling severity 正相关**——优化强度越大，evidence 质量提升的同时抽取能力退化越严重。QLoRA 放大至 catastrophic（rel_f1<0.02），bf16 GRPO 从 0.4549 退化至 ~0.434（mild, -2pp），DPO 呈 gradual 退化（1ep→3ep rel_f1 从 0.4034→0.3429），RSFT 无 decoupling。\\n\\nCED (Contrastive Evidence Discrimination) 是一种 NLI-based 候选筛选函数，通过文档内 hard negative 对比评估 evidence 质量。CED 作为 RSFT 的 scoring function 之一进行测试，其相对于 flat-NLI 的优势需要通过充分的统计检验验证。\\n\\n## Story Arc\\n\\n1. **Problem**: LLM DocRE 无证据 → 部署障碍\\n2. **New task**: evidence-grounded DocRE — 同时生成关系和证据\\n3. **Cost of faithfulness**: evidence generation 代价 ~7pp Ign-F1（no-evidence 47.36 vs evidence-SFT 40.36）——这是 faithfulness 的真实成本\\n4. **Exploration**: 系统性比较 online RL (GRPO) vs offline preference (DPO) vs offline RL (RSFT)\\n5. **Key finding**: evidence-extraction decoupling — RL optimization pressure 与 decoupling severity 正相关，形成连续谱系（GRPO-QLoRA catastrophic > GRPO-bf16 mild > DPO gradual > RSFT none）\\n6. **QLoRA amplification**: QLoRA 量化将 mild decoupling 放大至 catastrophic forgetting——decoupling 是 RL-for-IE 的通用梯度，QLoRA 是 catastrophic amplifier\\n7. **What works**: RSFT with NLI-based scoring 是唯一有效路线——提升 evidence 质量而不牺牲抽取\\n8. **Best practical solution**: CED reranker 恢复 97% 的 evidence 代价，同时保留高质量 evidence（evi_f1=0.8188）\\n9. **Diagnostic tool**: EDCR 双层诊断——方法级量化 decoupling（与 Claim 2 呼应），per-relation 级揭示 evi_f1 不捕捉的 relation-type 难度差异（D070 ✅）\\n\\n## Core Claims (reframed after Dream v1, updated D068/D069/D070/D071/D072)\\n\\n### Claim 1 (Main): Evidence-grounded DocRE 是可行的新能力\\n- FREIGE 是首个在 DocRED 上同时输出 (head, relation, tail, [evidence]) 的 LLM 方法\\n- **Evidence generation tax**: no-evidence SFT Ign-F1=47.36 vs evidence-SFT 40.36，代价 ~7pp（plan_014 ✅）\\n- RSFT 在 4/4 配置下均超过 SFT baseline（Ign-F1 +3.3~5.5pp）\\n- **CED reranker 是最优实用方案**: rel_f1=0.4864（仅低于 no-evidence 0.29pp），evi_f1=0.8188（plan_005 ✅）\\n- 需要 DREEAM-protocol 对齐的 Evi-F1 对比（D041 在处理中）\\n\\n### Claim 2 (Core finding): RL optimization pressure 与 evidence-extraction decoupling severity 正相关（D068/D069 修正）\\n- **Decoupling spectrum**: 优化强度越大，decoupling 越严重\\n  - GRPO QLoRA: catastrophic（rel_f1=0.0138, evi_f1=0.850, EDCR=0.99）— QLoRA 放大 decoupling\\n  - GRPO bf16: mild（rel_f1 从 0.4549→~0.434, -2pp; step_30=0.434, step_50=0.4276, step_70=0.4341）— 退化可控但持续（D065/D066）\\n  - DPO bf16 1ep→3ep: gradual（Ign-F1 38.88→TBD, rel_f1 0.4034→0.3429）— 随训练渐进退化（D067/D068）\\n  - RSFT: none — 无 decoupling，唯一有效路线\\n- **QLoRA 是 catastrophic amplifier，不是 root cause**: bf16 GRPO 仅 mild decoupling（-2pp），QLoRA 放大至 catastrophic（-39pp）（D054/D065/D066）\\n- **Decoupling 是 RL-for-IE 的通用梯度**: 跨方法（GRPO/DPO）、跨量化策略（QLoRA/bf16）一致出现，严重程度与优化压力正相关\\n- 三档 Dream 审稿均认为此发现\\\\\\\"genuinely novel and striking\\\\\\\"\\n- **已完成**: GRPO G=8 bf16 确认 mild decoupling（plan_011 ✅）; DPO 1ep/3ep 确认 gradual decoupling（plan_012 ✅）\\n\\n### Claim 3 (Ablation): NLI-based scoring 提升 RSFT 质量\\n- CED 和 flat-NLI 都优于 random/no scoring\\n- CED vs flat-NLI 的差异需统计验证（Dream 报告 p=0.08/0.38/0.12 不显著）\\n- **Critical**: 如果 CED 不显著优于 flat-NLI → CED 降级为\\\"one possible scoring function\\\"\\n- **行动**: 5+ seeds for significance testing\\n- **top_k selection ablation (k=1 vs k=3)**:\\n  - k=1 (best-of-8) 优于 k=3 (top3-of-8)，CED scoring precision 随 k 增大下降\\n  - k=1 均值 (3 seeds s42/s43/s44): Ign-F1=45.00, rel_f1=0.4596, evi_f1=81.43, EDCR=0.6434\\n  - k=3 (1 seed, reeval_rsft_topk3): Ign-F1=43.64, rel_f1=0.4454, evi_f1=80.88, EDCR=0.6635\\n  - Δ (k=3 vs k=1 mean): Ign-F1 **-1.36pp**, rel_f1 **-1.42pp**, evi_f1 **-0.55pp**, EDCR +0.02\\n  - 训练数据质量下降: k=1 mean_f1=0.6157, mean_ced=0.6683 → k=3 mean_f1=0.5761, mean_ced=0.6205（来源: mvp2_rsft_ced_scoring / mvp2_rsft_ced_scoring_topk3_r2）\\n  - 训练集规模: k=1 选出 2718 样本 (12.4%), k=3 选出 8037 样本 (37%), 数据量 ×2.96 但质量下降抵消数量优势\\n  - **叙事**: 低排名 response 引入噪声——rank 2-3 样本的 F1 和 CED 分数均显著低于 rank 1，扩大训练集规模无法补偿数据质量的稀释。这表明 RSFT 的关键不在数据量而在 scoring precision\\n  - **注**: k=3 仅 1 seed，差异方向一致但尚不具备统计显著性；作为 ablation table 中的辅助行呈现，不作为独立 claim\\n\\n### Claim 4 (Diagnostic): EDCR 双层诊断价值（D070/D072）\\n- **Layer 1 — 方法级**: EDCR 量化 evidence-extraction decoupling，与 Claim 2 spectrum 呼应\\n  - 方法级 EDCR 与 rel_f1 Spearman ρ=-0.965（plan_003 ✅）——本质是 decoupling 的度量\\n  - EDCR 识别病理模型（GRPO QLoRA: EDCR≈1.0）\\n- **Layer 2 — per-relation-type**: EDCR 提供 evi_f1 不捕捉的 relation-type 诊断信息 ✅\\n  - per-relation ρ(EDCR, evi_f1) = **-0.064** (p=0.58) → **完全独立于 evi_f1**\\n  - per-relation ρ(EDCR, rel_f1) = -0.793 (p<0.001) → 与 rel_f1 强相关但非完美\\n  - per-relation ρ(evi_f1, rel_f1) = -0.013 (p=0.91) → evidence 质量与抽取能力在 relation type 间完全解耦\\n  - 典型案例：date_of_birth (EDCR=0.118, 高 faithful) vs head_of_government (EDCR=0.956, 高 decoupled)\\n  - 93 relation types 分析（≥5 样本），76 个有非零数据\\n- **论文叙事**: EDCR 在方法级是 decoupling 度量工具（横向对比方法），在 relation 级是难度诊断工具（纵向定位薄弱 relation）——两层叙事互补\\n- **仍需**: 100 例人工标注验证（RC6）\\n\\n## MVP Evidence Summary (D071: 主表报 Ign-F1，附录报 F1)\\n\\n| Config | Ign-F1 | F1 | Δ vs SFT (Ign-F1) | Evi-F1 (cond) | Evi-F1 (joint) | EDCR |\\n|--------|--------|------|-------------------|---------------|---------------|------|\\n| **SFT no-evidence** | **47.36** | 48.93 | **+7.00pp** | **—** | **—** | **—** |\\n| SFT baseline (noquant) | 40.36 | 41.06 | — | 80.13 | 31.17 | 0.7118 |\\n| **CED reranker** | **TBD** | 48.64 | **TBD** | **81.88** | — | **0.6156** |\\n| RSFT CED s43 (best) | **45.85** | 46.83 | **+5.49pp** | 81.56 | 37.11 | 0.6388 |\\n| RSFT CED s44 | 45.51 | 46.55 | +5.15pp | 80.87 | 37.13 | 0.6350 |\\n| RSFT CED s42 | 43.63 | 44.49 | +3.27pp | 81.87 | 34.68 | 0.6565 |\\n| RSFT CED k=3 | 43.64 | 44.54 | +3.28pp | 80.88 | — | 0.6635 |\\n| RSFT r2a (1ep) | 44.01 | 44.94 | +3.65pp | 81.08 | 35.09 | 0.6641 |\\n| RSFT r2b (1ep) | 44.10 | 44.93 | +3.74pp | 81.28 | 34.90 | 0.6609 |\\n| flat-NLI s42 | 44.49 | 45.39 | +4.13pp | 80.43 | — | 0.6431 |\\n| flat-NLI s43 (reeval) | TBD | 45.23 | TBD | 81.58 | — | 0.6505 |\\n| DPO bf16 1ep | 38.88 | 40.34 | -1.48pp | 80.88 | — | 0.7139 |\\n| DPO bf16 3ep | TBD | 34.29 | TBD | — | — | — |\\n| GRPO bf16 G=8 (best step) | 45.59 | ~43.4 | +5.23pp | 80.86 | — | — |\\n| GRPO QLoRA (lr=5e-6) | TBD | 1.38 | TBD | 85.00 | — | 0.9900 |\\n\\n注：Evi-F1 以百分比显示（×100）。Ign-F1 修正后排名无实质变化（仅 r2a/r2b 互换，差 0.09pp）。TBD 项等待 metrics_v2.json 补算。GRPO bf16 Ign-F1=45.59 > F1=43.4 因 train triples 过滤效应。RSFT CED k=3 数据来源: reeval_rsft_topk3 (ign_f1_corrected=true)。\\n\\n## Anticipated Reviewer Concerns (updated from Dream, D068/D069)\\n\\n### RC1: \\\"Online RL\\\" 标题过度声称（Dream 三档一致 Critical）\\n- ~~标题和 claim 收窄到 \\\"GRPO fails for DocRE\\\"~~\\n- **D068/D069 修正**: 重新定位为 \\\"RL optimization pressure correlates with decoupling severity\\\"——不是 GRPO 特有问题，而是 RL-for-IE 的通用梯度\\n- DPO 数据支撑 decoupling spectrum（gradual decay confirms the pattern）\\n\\n### RC2: GRPO G=4 太小 + LoRA confound（Dream 三档一致 Major）\\n- GRPO G=8 bf16 实验 ✅ — 确认 mild decoupling（-2pp），QLoRA 是 catastrophic amplifier（D065/D066）\\n- LoRA confound 已解决：bf16 LoRA vs QLoRA 直接对比\\n\\n### RC3: CED 不显著优于 flat-NLI（Dream 三档一致 Major）\\n- 5+ seeds 统计检验；如不显著 → CED 降级\\n\\n### RC4: RSFT 不新颖\\n- 不声称 RSFT 是贡献；贡献在于任务定义 + decoupling 发现 + EDCR\\n\\n### RC5: 评测可比性（D041）\\n- DREEAM-protocol Evi-F1；conditional Evi-F1 作为辅助指标\\n\\n### RC6: EDCR 缺人工验证\\n- 100 例小规模标注\\n\\n### RC7: Missing DPO/PPO（Dream 两档 Major）\\n- DPO experiment ✅ — 结果确认 decoupling spectrum（D067/D068）\\n\\n### RC8: Dev-test degradation\\n- 观察项，等 test set 数据\\n\\n### RC9: 连接 reward overoptimization 文献\\n- 显式引用 Gao et al. 2023\\n\\n### RC10: Post-hoc evidence retrieval baseline\\n- SFT + BM25 evidence retrieval\\n\\n## Key Baselines (12+)\\n\\n1. **SFT-only**: Qwen3-4B + LoRA SFT（with evidence）\\n1b. **SFT no-evidence**: Qwen3-4B + LoRA SFT（无 evidence，upper bound ablation）\\n2. **RSFT flat-NLI**: flat-NLI scored RSFT（核心 ablation）\\n3. **RSFT CED**: CED scored RSFT（主方法）\\n4. **CED-as-reranker**: 推理时 CED 重排（无训练）\\n5. **DPO+CED**: offline preference learning — gradual decoupling（D067/D068）\\n6. **GRPO+CED (QLoRA, G=4)**: catastrophic decoupling baseline\\n7. **GRPO+CED (bf16, G=8)**: mild decoupling — QLoRA confound 排除（D065/D066）\\n8. **Post-hoc retrieval**: SFT + BM25 evidence（NEW）\\n9. **DREEAM**: encoder evidence SOTA\\n10. **SAIS**: encoder evidence baseline\\n11. **DocKS-RAG**: extraction SOTA（无 evidence）\\n12. **LMRC**: generative LLM SOTA（无 evidence）\\n\\n## Publishability Threshold (revised after Dream, D068/D069)\\n\\n- **必要条件**: (1) RSFT 在 test set 上 Ign-F1 显著 > SFT (2) DREEAM-protocol Evi-F1 可报告 (3) Decoupling spectrum 有完整数据支撑（GRPO QLoRA/bf16 + DPO + RSFT）\\n- **充分条件**: 上述 + CED 显著 > flat-NLI + EDCR 人工验证\\n- **Failure pivot**: decoupling spectrum 不成立（bf16 GRPO 也 catastrophic）→ scope 大幅缩减。**已排除**: bf16 GRPO 确认 mild（D065/D066）\\n\\n## Research Phase Priorities (revised after Dream v1)\\n\\n| Priority | 实验 | Claim | GPU-h |\\n|----------|------|-------|-------|\\n| P0 | flat-NLI RSFT ablation (5 seeds) | C3 | ~25h |\\n| P0 | CED RSFT additional seeds (→5 total) | C3 | ~10h |\\n| P0 | DREEAM-protocol Evi-F1 对齐 | C1 | CPU |\\n| P0 | Test set evaluation | C1 | ~4h |\\n| P0 | DREEAM baseline reproduction | C1 | ~8h |\\n| ~~P0~~ | ~~GRPO G=8 experiment~~ ✅ | C2 | ~16h |\\n| ~~P0~~ | ~~DPO+CED experiment~~ ✅ | C2 | ~12h |\\n| ~~P0~~ | ~~EDCR per-relation analysis (D070)~~ ✅ | C4 | CPU |\\n| ~~P0~~ | ~~Ign-F1 bugfix + data sync (D071)~~ ✅ | ALL | CPU |\\n| P1 | EDCR human validation | C4 | API |\\n| P1 | Post-hoc evidence retrieval baseline | C1 | ~4h |\\n| P1 | CED-as-reranker (running) | C1 | ~6h |\\n| P1 | Model size ablation | RC | ~24h |\\n| P1 | Re-DocRED extension | RC | ~12h |\\n| ~~P0~~ | ~~GRPO forgetting dynamics figure (plan_009)~~ ✅ | C2 | ~2h |\\n| ~~P0~~ | ~~SFT-without-evidence ablation (plan_014)~~ ✅ | C1 | ~8h |\\n| P2 | Advantage variance measurement | C2 | CPU |\\n\", \"total_chars\": 9998, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "6ddc88b0-ee56-4c6f-8d0d-ae2ff939f0df",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — FREIGE\\\\n\\\\n> **状态**: POST-MVP + DREAM v2 完成（D047 分析）\\\\n> **最后更新**: 2026-05-16\\\\n> **Dream v1**: best=2.5, median=3.0, worst=2.5 → reframe 完成\\\\n> **Dream v2**: best=3.0, median=2.5, worst=2.5 → best 提升但 median 下降，未达标。关键路径：plan_011 bf16 GRPO eval + structural fixes → re-dream v3\\\\n\\\\n## Target Venue\\\\n\\\\n- Primary: **EMNLP 2026 Main** (ARR July cycle, ~July 15-25 → commit EMNLP Aug/Sep)\\\\n- Fallback: AAAI 2027 (abstract July 25, paper Aug 1)\\\\n\\\\n## Core Insight\\\\n\\\\nLLM-based document-level IE 已逼近 encoder SOTA 的抽取精度，但零方法能生成可验证证据。本文提出 **evidence-grounded DocRE** 作为新任务范式：LLM 同时输出关系三元组和支撑证据句。\\\\n\\\\n我们系统性地探索了 online RL (GRPO) 、offline preference optimization (DPO) 和 offline RL (RSFT) 三条技术路线。关键发现：**RL optimization pressure 与 evidence-extraction decoupling severity 正相关**——优化强度越大，evidence 质量提升的同时抽取能力退化越严重。QLoRA 放大至 catastrophic（rel_f1<0.02），bf16 GRPO 从 0.4549 退化至 ~0.434（mild, -2pp），DPO 呈 gradual 退化（1ep→3ep rel_f1 从 0.4034→0.3429），RSFT 无 decoupling。\\\\n\\\\nCED (Contrastive Evidence Discrimination) 是一种 NLI-based 候选筛选函数，通过文档内 hard negative 对比评估 evidence 质量。CED 作为 RSFT 的 scoring function 之一进行测试，其相对于 flat-NLI 的优势需要通过充分的统计检验验证。\\\\n\\\\n## Story Arc\\\\n\\\\n1. **Problem**: LLM DocRE 无证据 → 部署障碍\\\\n2. **New task**: evidence-grounded DocRE — 同时生成关系和证据\\\\n3. **Cost of faithfulness**: evidence generation 代价 ~7pp Ign-F1（no-evidence 47.36 vs evidence-SFT 40.36）——这是 faithfulness 的真实成本\\\\n4. **Exploration**: 系统性比较 online RL (GRPO) vs offline preference (DPO) vs offline RL (RSFT)\\\\n5. **Key finding**: evidence-extraction decoupling — RL optimization pressure 与 decoupling severity 正相关，形成连续谱系（GRPO-QLoRA catastrophic > GRPO-bf16 mild > DPO gradual > RSFT none）\\\\n6. **QLoRA amplification**: QLoRA 量化将 mild decoupling 放大至 catastrophic forgetting——decoupling 是 RL-for-IE 的通用梯度，QLoRA 是 catastrophic amplifier\\\\n7. **What works**: RSFT with NLI-based scoring 是唯一有效路线——提升 evidence 质量而不牺牲抽取\\\\n8. **Best practical solution**: CED reranker 恢复 97% 的 evidence 代价，同时保留高质量 evidence（evi_f1=0.8188）\\\\n9. **Diagnostic tool**: EDCR 双层诊断——方法级量化 decoupling（与 Claim 2 呼应），per-relation 级揭示 evi_f1 不捕捉的 relation-type 难度差异（D070 ✅）\\\\n\\\\n## Core Claims (reframed after Dream v1, updated D068/D069/D070/D071/D072)\\\\n\\\\n### Claim 1 (Main): Evidence-grounded DocRE 是可行的新能力\\\\n- FREIGE 是首个在 DocRED 上同时输出 (head, relation, tail, [evidence]) 的 LLM 方法\\\\n- **Evidence generation tax**: no-evidence SFT Ign-F1=47.36 vs evidence-SFT 40.36，代价 ~7pp（plan_014 ✅）\\\\n- RSFT 在 4/4 配置下均超过 SFT baseline（Ign-F1 +3.3~5.5pp）\\\\n- **CED reranker 是最优实用方案**: rel_f1=0.4864（仅低于 no-evidence 0.29pp），evi_f1=0.8188（plan_005 ✅）\\\\n- 需要 DREEAM-protocol 对齐的 Evi-F1 对比（D041 在处理中）\\\\n\\\\n### Claim 2 (Core finding): RL optimization pressure 与 evidence-extraction decoupling severity 正相关（D068/D069 修正）\\\\n- **Decoupling spectrum**: 优化强度越大，decoupling 越严重\\\\n  - GRPO QLoRA: catastrophic（rel_f1=0.0138, evi_f1=0.850, EDCR=0.99）— QLoRA 放大 decoupling\\\\n  - GRPO bf16: mild（rel_f1 从 0.4549→~0.434, -2pp; step_30=0.434, step_50=0.4276, step_70=0.4341）— 退化可控但持续（D065/D066）\\\\n  - DPO bf16 1ep→3ep: gradual（Ign-F1 38.88→TBD, rel_f1 0.4034→0.3429）— 随训练渐进退化（D067/D068）\\\\n  - RSFT: none — 无 decoupling，唯一有效路线\\\\n- **QLoRA 是 catastrophic amplifier，不是 root cause**: bf16 GRPO 仅 mild decoupling（-2pp），QLoRA 放大至 catastrophic（-39pp）（D054/D065/D066）\\\\n- **Decoupling 是 RL-for-IE 的通用梯度**: 跨方法（GRPO/DPO）、跨量化策略（QLoRA/bf16）一致出现，严重程度与优化压力正相关\\\\n- 三档 Dream 审稿均认为此发现\\\\\\\\\\\\\\\"genuinely novel and striking\\\\\\\\\\\\\\\"\\\\n- **已完成**: GRPO G=8 bf16 确认 mild decoupling（plan_011 ✅）; DPO 1ep/3ep 确认 gradual decoupling（plan_012 ✅）\\\\n\\\\n### Claim 3 (Ablation): NLI-based scoring 提升 RSFT 质量\\\\n- CED 和 flat-NLI 都优于 random/no scoring\\\\n- CED vs flat-NLI 的差异需统计验证（Dream 报告 p=0.08/0.38/0.12 不显著）\\\\n- **Critical**: 如果 CED 不显著优于 flat-NLI → CED 降级为\\\\\\\"one possible scoring function\\\\\\\"\\\\n- **行动**: 5+ seeds for significance testing\\\\n- **top_k selection ablation (k=1 vs k=3)**:\\\\n  - k=1 (best-of-8) 优于 k=3 (top3-of-8)，CED scoring precision 随 k 增大下降\\\\n  - k=1 均值 (3 seeds s42/s43/s44): Ign-F1=45.00, rel_f1=0.4596, evi_f1=81.43, EDCR=0.6434\\\\n  - k=3 (1 seed, reeval_rsft_topk3): Ign-F1=43.64, rel_f1=0.4454, evi_f1=80.88, EDCR=0.6635\\\\n  - Δ (k=3 vs k=1 mean): Ign-F1 **-1.36pp**, rel_f1 **-1.42pp**, evi_f1 **-0.55pp**, EDCR +0.02\\\\n  - 训练数据质量下降: k=1 mean_f1=0.6157, mean_ced=0.6683 → k=3 mean_f1=0.5761, mean_ced=0.6205（来源: mvp2_rsft_ced_scoring / mvp2_rsft_ced_scoring_topk3_r2）\\\\n  - 训练集规模: k=1 选出 2718 样本 (12.4%), k=3 选出 8037 样本 (37%), 数据量 ×2.96 但质量下降抵消数量优势\\\\n  - **叙事**: 低排名 response 引入噪声——rank 2-3 样本的 F1 和 CED 分数均显著低于 rank 1，扩大训练集规模无法补偿数据质量的稀释。这表明 RSFT 的关键不在数据量而在 scoring precision\\\\n  - **注**: k=3 仅 1 seed，差异方向一致但尚不具备统计显著性；作为 ablation table 中的辅助行呈现，不作为独立 claim\\\\n\\\\n### Claim 4 (Diagnostic): EDCR 双层诊断价值（D070/D072）\\\\n- **Layer 1 — 方法级**: EDCR 量化 evidence-extraction decoupling，与 Claim 2 spectrum 呼应\\\\n  - 方法级 EDCR 与 rel_f1 Spearman ρ=-0.965（plan_003 ✅）——本质是 decoupling 的度量\\\\n  - EDCR 识别病理模型（GRPO QLoRA: EDCR≈1.0）\\\\n- **Layer 2 — per-relation-type**: EDCR 提供 evi_f1 不捕捉的 relation-type 诊断信息 ✅\\\\n  - per-relation ρ(EDCR, evi_f1) = **-0.064** (p=0.58) → **完全独立于 evi_f1**\\\\n  - per-relation ρ(EDCR, rel_f1) = -0.793 (p<0.001) → 与 rel_f1 强相关但非完美\\\\n  - per-relation ρ(evi_f1, rel_f1) = -0.013 (p=0.91) → evidence 质量与抽取能力在 relation type 间完全解耦\\\\n  - 典型案例：date_of_birth (EDCR=0.118, 高 faithful) vs head_of_government (EDCR=0.956, 高 decoupled)\\\\n  - 93 relation types 分析（≥5 样本），76 个有非零数据\\\\n- **论文叙事**: EDCR 在方法级是 decoupling 度量工具（横向对比方法），在 relation 级是难度诊断工具（纵向定位薄弱 relation）——两层叙事互补\\\\n- **仍需**: 100 例人工标注验证（RC6）\\\\n\\\\n## MVP Evidence Summary (D071: 主表报 Ign-F1，附录报 F1)\\\\n\\\\n| Config | Ign-F1 | F1 | Δ vs SFT (Ign-F1) | Evi-F1 (cond) | Evi-F1 (joint) | EDCR |\\\\n|--------|--------|------|-------------------|---------------|---------------|------|\\\\n| **SFT no-evidence** | **47.36** | 48.93 | **+7.00pp** | **—** | **—** | **—** |\\\\n| SFT baseline (noquant) | 40.36 | 41.06 | — | 80.13 | 31.17 | 0.7118 |\\\\n| **CED reranker** | **TBD** | 48.64 | **TBD** | **81.88** | — | **0.6156** |\\\\n| RSFT CED s43 (best) | **45.85** | 46.83 | **+5.49pp** | 81.56 | 37.11 | 0.6388 |\\\\n| RSFT CED s44 | 45.51 | 46.55 | +5.15pp | 80.87 | 37.13 | 0.6350 |\\\\n| RSFT CED s42 | 43.63 | 44.49 | +3.27pp | 81.87 | 34.68 | 0.6565 |\\\\n| RSFT CED k=3 | 43.64 | 44.54 | +3.28pp | 80.88 | — | 0.6635 |\\\\n| RSFT r2a (1ep) | 44.01 | 44.94 | +3.65pp | 81.08 | 35.09 | 0.6641 |\\\\n| RSFT r2b (1ep) | 44.10 | 44.93 | +3.74pp | 81.28 | 34.90 | 0.6609 |\\\\n| flat-NLI s42 | 44.49 | 45.39 | +4.13pp | 80.43 | — | 0.6431 |\\\\n| flat-NLI s43 (reeval) | TBD | 45.23 | TBD | 81.58 | — | 0.6505 |\\\\n| DPO bf16 1ep | 38.88 | 40.34 | -1.48pp | 80.88 | — | 0.7139 |\\\\n| DPO bf16 3ep | TBD | 34.29 | TBD | — | — | — |\\\\n| GRPO bf16 G=8 (best step) | 45.59 | ~43.4 | +5.23pp | 80.86 | — | — |\\\\n| GRPO QLoRA (lr=5e-6) | TBD | 1.38 | TBD | 85.00 | — | 0.9900 |\\\\n\\\\n注：Evi-F1 以百分比显示（×100）。Ign-F1 修正后排名无实质变化（仅 r2a/r2b 互换，差 0.09pp）。TBD 项等待 metrics_v2.json 补算。GRPO bf16 Ign-F1=45.59 > F1=43.4 因 train triples 过滤效应。RSFT CED k=3 数据来源: reeval_rsft_topk3 (ign_f1_corrected=true)。\\\\n\\\\n## Anticipated Reviewer Concerns (updated from Dream, D068/D069)\\\\n\\\\n### RC1: \\\\\\\"Online RL\\\\\\\" 标题过度声称（Dream 三档一致 Critical）\\\\n- ~~标题和 claim 收窄到 \\\\\\\"GRPO fails for DocRE\\\\\\\"~~\\\\n- **D068/D069 修正**: 重新定位为 \\\\\\\"RL optimization pressure correlates with decoupling severity\\\\\\\"——不是 GRPO 特有问题，而是 RL-for-IE 的通用梯度\\\\n- DPO 数据支撑 decoupling spectrum（gradual decay confirms the pattern）\\\\n\\\\n### RC2: GRPO G=4 太小 + LoRA confound（Dream 三档一致 Major）\\\\n- GRPO G=8 bf16 实验 ✅ — 确认 mild decoupling（-2pp），QLoRA 是 catastrophic amplifier（D065/D066）\\\\n- LoRA confound 已解决：bf16 LoRA vs QLoRA 直接对比\\\\n\\\\n### RC3: CED 不显著优于 flat-NLI（Dream 三档一致 Major）\\\\n- 5+ seeds 统计检验；如不显著 → CED 降级\\\\n\\\\n### RC4: RSFT 不新颖\\\\n- 不声称 RSFT 是贡献；贡献在于任务定义 + decoupling 发现 + EDCR\\\\n\\\\n### RC5: 评测可比性（D041）\\\\n- DREEAM-protocol Evi-F1；conditional Evi-F1 作为辅助指标\\\\n\\\\n### RC6: EDCR 缺人工验证\\\\n- 100 例小规模标注\\\\n\\\\n### RC7: Missing DPO/PPO（Dream 两档 Major）\\\\n- DPO experiment ✅ — 结果确认 decoupling spectrum（D067/D068）\\\\n\\\\n### RC8: Dev-test degradation\\\\n- 观察项，等 test set 数据\\\\n\\\\n### RC9: 连接 reward overoptimization 文献\\\\n- 显式引用 Gao et al. 2023\\\\n\\\\n### RC10: Post-hoc evidence retrieval baseline\\\\n- SFT + BM25 evidence retrieval\\\\n\\\\n## Key Baselines (12+)\\\\n\\\\n1. **SFT-only**: Qwen3-4B + LoRA SFT（with evidence）\\\\n1b. **SFT no-evidence**: Qwen3-4B + LoRA SFT（无 evidence，upper bound ablation）\\\\n2. **RSFT flat-NLI**: flat-NLI scored RSFT（核心 ablation）\\\\n3. **RSFT CED**: CED scored RSFT（主方法）\\\\n4. **CED-as-reranker**: 推理时 CED 重排（无训练）\\\\n5. **DPO+CED**: offline preference learning — gradual decoupling（D067/D068）\\\\n6. **GRPO+CED (QLoRA, G=4)**: catastrophic decoupling baseline\\\\n7. **GRPO+CED (bf16, G=8)**: mild decoupling — QLoRA confound 排除（D065/D066）\\\\n8. **Post-hoc retrieval**: SFT + BM25 evidence（NEW）\\\\n9. **DREEAM**: encoder evidence SOTA\\\\n10. **SAIS**: encoder evidence baseline\\\\n11. **DocKS-RAG**: extraction SOTA（无 evidence）\\\\n12. **LMRC**: generative LLM SOTA（无 evidence）\\\\n\\\\n## Publishability Threshold (revised after Dream, D068/D069)\\\\n\\\\n- **必要条件**: (1) RSFT 在 test set 上 Ign-F1 显著 > SFT (2) DREEAM-protocol Evi-F1 可报告 (3) Decoupling spectrum 有完整数据支撑（GRPO QLoRA/bf16 + DPO + RSFT）\\\\n- **充分条件**: 上述 + CED 显著 > flat-NLI + EDCR 人工验证\\\\n- **Failure pivot**: decoupling spectrum 不成立（bf16 GRPO 也 catastrophic）→ scope 大幅缩减。**已排除**: bf16 GRPO 确认 mild（D065/D066）\\\\n\\\\n## Research Phase Priorities (revised after Dream v1)\\\\n\\\\n| Priority | 实验 | Claim | GPU-h |\\\\n|----------|------|-------|-------|\\\\n| P0 | flat-NLI RSFT ablation (5 seeds) | C3 | ~25h |\\\\n| P0 | CED RSFT additional seeds (→5 total) | C3 | ~10h |\\\\n| P0 | DREEAM-protocol Evi-F1 对齐 | C1 | CPU |\\\\n| P0 | Test set evaluation | C1 | ~4h |\\\\n| P0 | DREEAM baseline reproduction | C1 | ~8h |\\\\n| ~~P0~~ | ~~GRPO G=8 experiment~~ ✅ | C2 | ~16h |\\\\n| ~~P0~~ | ~~DPO+CED experiment~~ ✅ | C2 | ~12h |\\\\n| ~~P0~~ | ~~EDCR per-relation analysis (D070)~~ ✅ | C4 | CPU |\\\\n| ~~P0~~ | ~~Ign-F1 bugfix + data sync (D071)~~ ✅ | ALL | CPU |\\\\n| P1 | EDCR human validation | C4 | API |\\\\n| P1 | Post-hoc evidence retrieval baseline | C1 | ~4h |\\\\n| P1 | CED-as-reranker (running) | C1 | ~6h |\\\\n| P1 | Model size ablation | RC | ~24h |\\\\n| P1 | Re-DocRED extension | RC | ~12h |\\\\n| ~~P0~~ | ~~GRPO forgetting dynamics figure (plan_009)~~ ✅ | C2 | ~2h |\\\\n| ~~P0~~ | ~~SFT-without-evidence ablation (plan_014)~~ ✅ | C1 | ~8h |\\\\n| P2 | Advantage variance measurement | C2 | CPU |\\\\n\\\", \\\"total_chars\\\": 9998, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/paper_framing.md\", \"content\": \"# Paper Framing — FREIGE\\n\\n> **状态**: POST-MVP + DREAM v2 完成（D047 分析）\\n> **最后更新**: 2026-05-16\\n> **Dream v1**: best=2.5, median=3.0, worst=2.5 → reframe 完成\\n> **Dream v2**: best=3.0, median=2.5, worst=2.5 → best 提升但 median 下降，未达标。关键路径：plan_011 bf16 GRPO eval + structural fixes → re-dream v3\\n\\n## Target Venue\\n\\n- Primary: **EMNLP 2026 Main** (ARR July cycle, ~July 15-25 → commit EMNLP Aug/Sep)\\n- Fallback: AAAI 2027 (abstract July 25, paper Aug 1)\\n\\n## Core Insight\\n\\nLLM-based document-level IE 已逼近 encoder SOTA 的抽取精度，但零方法能生成可验证证据。本文提出 **evidence-grounded DocRE** 作为新任务范式：LLM 同时输出关系三元组和支撑证据句。\\n\\n我们系统性地探索了 online RL (GRPO) 、offline preference optimization (DPO) 和 offline RL (RSFT) 三条技术路线。关键发现：**RL optimization pressure 与 evidence-extraction decoupling severity 正相关**——优化强度越大，evidence 质量提升的同时抽取能力退化越严重。QLoRA 放大至 catastrophic（rel_f1<0.02），bf16 GRPO 从 0.4549 退化至 ~0.434（mild, -2pp），DPO 呈 gradual 退化（1ep→3ep rel_f1 从 0.4034→0.3429），RSFT 无 decoupling。\\n\\nCED (Contrastive Evidence Discrimination) 是一种 NLI-based 候选筛选函数，通过文档内 hard negative 对比评估 evidence 质量。CED 作为 RSFT 的 scoring function 之一进行测试，其相对于 flat-NLI 的优势需要通过充分的统计检验验证。\\n\\n## Story Arc\\n\\n1. **Problem**: LLM DocRE 无证据 → 部署障碍\\n2. **New task**: evidence-grounded DocRE — 同时生成关系和证据\\n3. **Cost of faithfulness**: evidence generation 代价 ~7pp Ign-F1（no-evidence 47.36 vs evidence-SFT 40.36）——这是 faithfulness 的真实成本\\n4. **Exploration**: 系统性比较 online RL (GRPO) vs offline preference (DPO) vs offline RL (RSFT)\\n5. **Key finding**: evidence-extraction decoupling — RL optimization pressure 与 decoupling severity 正相关，形成连续谱系（GRPO-QLoRA catastrophic > GRPO-bf16 mild > DPO gradual > RSFT none）\\n6. **QLoRA amplification**: QLoRA 量化将 mild decoupling 放大至 catastrophic forgetting——decoupling 是 RL-for-IE 的通用梯度，QLoRA 是 catastrophic amplifier\\n7. **What works**: RSFT with NLI-based scoring 是唯一有效路线——提升 evidence 质量而不牺牲抽取\\n8. **Best practical solution**: CED reranker 恢复 97% 的 evidence 代价，同时保留高质量 evidence（evi_f1=0.8188）\\n9. **Diagnostic tool**: EDCR 双层诊断——方法级量化 decoupling（与 Claim 2 呼应），per-relation 级揭示 evi_f1 不捕捉的 relation-type 难度差异（D070 ✅）\\n\\n## Core Claims (reframed after Dream v1, updated D068/D069/D070/D071/D072)\\n\\n### Claim 1 (Main): Evidence-grounded DocRE 是可行的新能力\\n- FREIGE 是首个在 DocRED 上同时输出 (head, relation, tail, [evidence]) 的 LLM 方法\\n- **Evidence generation tax**: no-evidence SFT Ign-F1=47.36 vs evidence-SFT 40.36，代价 ~7pp（plan_014 ✅）\\n- RSFT 在 4/4 配置下均超过 SFT baseline（Ign-F1 +3.3~5.5pp）\\n- **CED reranker 是最优实用方案**: rel_f1=0.4864（仅低于 no-evidence 0.29pp），evi_f1=0.8188（plan_005 ✅）\\n- 需要 DREEAM-protocol 对齐的 Evi-F1 对比（D041 在处理中）\\n\\n### Claim 2 (Core finding): RL optimization pressure 与 evidence-extraction decoupling severity 正相关（D068/D069 修正）\\n- **Decoupling spectrum**: 优化强度越大，decoupling 越严重\\n  - GRPO QLoRA: catastrophic（rel_f1=0.0138, evi_f1=0.850, EDCR=0.99）— QLoRA 放大 decoupling\\n  - GRPO bf16: mild（rel_f1 从 0.4549→~0.434, -2pp; step_30=0.434, step_50=0.4276, step_70=0.4341）— 退化可控但持续（D065/D066）\\n  - DPO bf16 1ep→3ep: gradual（Ign-F1 38.88→TBD, rel_f1 0.4034→0.3429）— 随训练渐进退化（D067/D068）\\n  - RSFT: none — 无 decoupling，唯一有效路线\\n- **QLoRA 是 catastrophic amplifier，不是 root cause**: bf16 GRPO 仅 mild decoupling（-2pp），QLoRA 放大至 catastrophic（-39pp）（D054/D065/D066）\\n- **Decoupling 是 RL-for-IE 的通用梯度**: 跨方法（GRPO/DPO）、跨量化策略（QLoRA/bf16）一致出现，严重程度与优化压力正相关\\n- 三档 Dream 审稿均认为此发现\\\\\\\"genuinely novel and striking\\\\\\\"\\n- **已完成**: GRPO G=8 bf16 确认 mild decoupling（plan_011 ✅）; DPO 1ep/3ep 确认 gradual decoupling（plan_012 ✅）\\n\\n### Claim 3 (Ablation): NLI-based scoring 提升 RSFT 质量\\n- CED 和 flat-NLI 都优于 random/no scoring\\n- CED vs flat-NLI 的差异需统计验证（Dream 报告 p=0.08/0.38/0.12 不显著）\\n- **Critical**: 如果 CED 不显著优于 flat-NLI → CED 降级为\\\"one possible scoring function\\\"\\n- **行动**: 5+ seeds for significance testing\\n- **top_k selection ablation (k=1 vs k=3)**:\\n  - k=1 (best-of-8) 优于 k=3 (top3-of-8)，CED scoring precision 随 k 增大下降\\n  - k=1 均值 (3 seeds s42/s43/s44): Ign-F1=45.00, rel_f1=0.4596, evi_f1=81.43, EDCR=0.6434\\n  - k=3 (1 seed, reeval_rsft_topk3): Ign-F1=43.64, rel_f1=0.4454, evi_f1=80.88, EDCR=0.6635\\n  - Δ (k=3 vs k=1 mean): Ign-F1 **-1.36pp**, rel_f1 **-1.42pp**, evi_f1 **-0.55pp**, EDCR +0.02\\n  - 训练数据质量下降: k=1 mean_f1=0.6157, mean_ced=0.6683 → k=3 mean_f1=0.5761, mean_ced=0.6205（来源: mvp2_rsft_ced_scoring / mvp2_rsft_ced_scoring_topk3_r2）\\n  - 训练集规模: k=1 选出 2718 样本 (12.4%), k=3 选出 8037 样本 (37%), 数据量 ×2.96 但质量下降抵消数量优势\\n  - **叙事**: 低排名 response 引入噪声——rank 2-3 样本的 F1 和 CED 分数均显著低于 rank 1，扩大训练集规模无法补偿数据质量的稀释。这表明 RSFT 的关键不在数据量而在 scoring precision\\n  - **注**: k=3 仅 1 seed，差异方向一致但尚不具备统计显著性；作为 ablation table 中的辅助行呈现，不作为独立 claim\\n\\n### Claim 4 (Diagnostic): EDCR 双层诊断价值（D070/D072）\\n- **Layer 1 — 方法级**: EDCR 量化 evidence-extraction decoupling，与 Claim 2 spectrum 呼应\\n  - 方法级 EDCR 与 rel_f1 Spearman ρ=-0.965（plan_003 ✅）——本质是 decoupling 的度量\\n  - EDCR 识别病理模型（GRPO QLoRA: EDCR≈1.0）\\n- **Layer 2 — per-relation-type**: EDCR 提供 evi_f1 不捕捉的 relation-type 诊断信息 ✅\\n  - per-relation ρ(EDCR, evi_f1) = **-0.064** (p=0.58) → **完全独立于 evi_f1**\\n  - per-relation ρ(EDCR, rel_f1) = -0.793 (p<0.001) → 与 rel_f1 强相关但非完美\\n  - per-relation ρ(evi_f1, rel_f1) = -0.013 (p=0.91) → evidence 质量与抽取能力在 relation type 间完全解耦\\n  - 典型案例：date_of_birth (EDCR=0.118, 高 faithful) vs head_of_government (EDCR=0.956, 高 decoupled)\\n  - 93 relation types 分析（≥5 样本），76 个有非零数据\\n- **论文叙事**: EDCR 在方法级是 decoupling 度量工具（横向对比方法），在 relation 级是难度诊断工具（纵向定位薄弱 relation）——两层叙事互补\\n- **仍需**: 100 例人工标注验证（RC6）\\n\\n## MVP Evidence Summary (D071: 主表报 Ign-F1，附录报 F1)\\n\\n| Config | Ign-F1 | F1 | Δ vs SFT (Ign-F1) | Evi-F1 (cond) | Evi-F1 (joint) | EDCR |\\n|--------|--------|------|-------------------|---------------|---------------|------|\\n| **SFT no-evidence** | **47.36** | 48.93 | **+7.00pp** | **—** | **—** | **—** |\\n| SFT baseline (noquant) | 40.36 | 41.06 | — | 80.13 | 31.17 | 0.7118 |\\n| **CED reranker** | **TBD** | 48.64 | **TBD** | **81.88** | — | **0.6156** |\\n| RSFT CED s43 (best) | **45.85** | 46.83 | **+5.49pp** | 81.56 | 37.11 | 0.6388 |\\n| RSFT CED s44 | 45.51 | 46.55 | +5.15pp | 80.87 | 37.13 | 0.6350 |\\n| RSFT CED s42 | 43.63 | 44.49 | +3.27pp | 81.87 | 34.68 | 0.6565 |\\n| RSFT CED k=3 | 43.64 | 44.54 | +3.28pp | 80.88 | — | 0.6635 |\\n| RSFT r2a (1ep) | 44.01 | 44.94 | +3.65pp | 81.08 | 35.09 | 0.6641 |\\n| RSFT r2b (1ep) | 44.10 | 44.93 | +3.74pp | 81.28 | 34.90 | 0.6609 |\\n| flat-NLI s42 | 44.49 | 45.39 | +4.13pp | 80.43 | — | 0.6431 |\\n| flat-NLI s43 (reeval) | TBD | 45.23 | TBD | 81.58 | — | 0.6505 |\\n| DPO bf16 1ep | 38.88 | 40.34 | -1.48pp | 80.88 | — | 0.7139 |\\n| DPO bf16 3ep | TBD | 34.29 | TBD | — | — | — |\\n| GRPO bf16 G=8 (best step) | 45.59 | ~43.4 | +5.23pp | 80.86 | — | — |\\n| GRPO QLoRA (lr=5e-6) | TBD | 1.38 | TBD | 85.00 | — | 0.9900 |\\n\\n注：Evi-F1 以百分比显示（×100）。Ign-F1 修正后排名无实质变化（仅 r2a/r2b 互换，差 0.09pp）。TBD 项等待 metrics_v2.json 补算。GRPO bf16 Ign-F1=45.59 > F1=43.4 因 train triples 过滤效应。RSFT CED k=3 数据来源: reeval_rsft_topk3 (ign_f1_corrected=true)。\\n\\n## Anticipated Reviewer Concerns (updated from Dream, D068/D069)\\n\\n### RC1: \\\"Online RL\\\" 标题过度声称（Dream 三档一致 Critical）\\n- ~~标题和 claim 收窄到 \\\"GRPO fails for DocRE\\\"~~\\n- **D068/D069 修正**: 重新定位为 \\\"RL optimization pressure correlates with decoupling severity\\\"——不是 GRPO 特有问题，而是 RL-for-IE 的通用梯度\\n- DPO 数据支撑 decoupling spectrum（gradual decay confirms the pattern）\\n\\n### RC2: GRPO G=4 太小 + LoRA confound（Dream 三档一致 Major）\\n- GRPO G=8 bf16 实验 ✅ — 确认 mild decoupling（-2pp），QLoRA 是 catastrophic amplifier（D065/D066）\\n- LoRA confound 已解决：bf16 LoRA vs QLoRA 直接对比\\n\\n### RC3: CED 不显著优于 flat-NLI（Dream 三档一致 Major）\\n- 5+ seeds 统计检验；如不显著 → CED 降级\\n\\n### RC4: RSFT 不新颖\\n- 不声称 RSFT 是贡献；贡献在于任务定义 + decoupling 发现 + EDCR\\n\\n### RC5: 评测可比性（D041）\\n- DREEAM-protocol Evi-F1；conditional Evi-F1 作为辅助指标\\n\\n### RC6: EDCR 缺人工验证\\n- 100 例小规模标注\\n\\n### RC7: Missing DPO/PPO（Dream 两档 Major）\\n- DPO experiment ✅ — 结果确认 decoupling spectrum（D067/D068）\\n\\n### RC8: Dev-test degradation\\n- 观察项，等 test set 数据\\n\\n### RC9: 连接 reward overoptimization 文献\\n- 显式引用 Gao et al. 2023\\n\\n### RC10: Post-hoc evidence retrieval baseline\\n- SFT + BM25 evidence retrieval\\n\\n## Key Baselines (12+)\\n\\n1. **SFT-only**: Qwen3-4B + LoRA SFT（with evidence）\\n1b. **SFT no-evidence**: Qwen3-4B + LoRA SFT（无 evidence，upper bound ablation）\\n2. **RSFT flat-NLI**: flat-NLI scored RSFT（核心 ablation）\\n3. **RSFT CED**: CED scored RSFT（主方法）\\n4. **CED-as-reranker**: 推理时 CED 重排（无训练）\\n5. **DPO+CED**: offline preference learning — gradual decoupling（D067/D068）\\n6. **GRPO+CED (QLoRA, G=4)**: catastrophic decoupling baseline\\n7. **GRPO+CED (bf16, G=8)**: mild decoupling — QLoRA confound 排除（D065/D066）\\n8. **Post-hoc retrieval**: SFT + BM25 evidence（NEW）\\n9. **DREEAM**: encoder evidence SOTA\\n10. **SAIS**: encoder evidence baseline\\n11. **DocKS-RAG**: extraction SOTA（无 evidence）\\n12. **LMRC**: generative LLM SOTA（无 evidence）\\n\\n## Publishability Threshold (revised after Dream, D068/D069)\\n\\n- **必要条件**: (1) RSFT 在 test set 上 Ign-F1 显著 > SFT (2) DREEAM-protocol Evi-F1 可报告 (3) Decoupling spectrum 有完整数据支撑（GRPO QLoRA/bf16 + DPO + RSFT）\\n- **充分条件**: 上述 + CED 显著 > flat-NLI + EDCR 人工验证\\n- **Failure pivot**: decoupling spectrum 不成立（bf16 GRPO 也 catastrophic）→ scope 大幅缩减。**已排除**: bf16 GRPO 确认 mild（D065/D066）\\n\\n## Research Phase Priorities (revised after Dream v1)\\n\\n| Priority | 实验 | Claim | GPU-h |\\n|----------|------|-------|-------|\\n| P0 | flat-NLI RSFT ablation (5 seeds) | C3 | ~25h |\\n| P0 | CED RSFT additional seeds (→5 total) | C3 | ~10h |\\n| P0 | DREEAM-protocol Evi-F1 对齐 | C1 | CPU |\\n| P0 | Test set evaluation | C1 | ~4h |\\n| P0 | DREEAM baseline reproduction | C1 | ~8h |\\n| ~~P0~~ | ~~GRPO G=8 experiment~~ ✅ | C2 | ~16h |\\n| ~~P0~~ | ~~DPO+CED experiment~~ ✅ | C2 | ~12h |\\n| ~~P0~~ | ~~EDCR per-relation analysis (D070)~~ ✅ | C4 | CPU |\\n| ~~P0~~ | ~~Ign-F1 bugfix + data sync (D071)~~ ✅ | ALL | CPU |\\n| P1 | EDCR human validation | C4 | API |\\n| P1 | Post-hoc evidence retrieval baseline | C1 | ~4h |\\n| P1 | CED-as-reranker (running) | C1 | ~6h |\\n| P1 | Model size ablation | RC | ~24h |\\n| P1 | Re-DocRED extension | RC | ~12h |\\n| ~~P0~~ | ~~GRPO forgetting dynamics figure (plan_009)~~ ✅ | C2 | ~2h |\\n| ~~P0~~ | ~~SFT-without-evidence ablation (plan_014)~~ ✅ | C1 | ~8h |\\n| P2 | Advantage variance measurement | C2 | CPU |\\n\", \"total_chars\": 9998, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
Good, I have the paper framing. Now I need to read the literature map. It was too large for the tool result, so let me use a subagent to extract the relevant information from it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "e20827df-071d-4946-9f4f-4dd08ed52db4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BJFJFFCm2dgBWSN2ndSXBB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6746,
      "cache_read_input_tokens": 24051,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6746
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

_source line 13_

The literature map is too large for direct reading. Let me extract it via subagent while I process the paper framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "9117ddc6-654d-45d8-92e2-d310bf6bb1ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BJFJFFCm2dgBWSN2ndSXBB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6746,
      "cache_read_input_tokens": 24051,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6746
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

_source line 14_

<details open><summary>🔧 Tool call — Agent · `toolu_013Lrje7vQRGqSdwXn2BhLuJ`</summary>

```json
{
  "description": "Extract literature map data",
  "prompt": "Read the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7341df47-ab61-4a7f-ab4b-fc80cccd2794/tool-results/mcp-agent-ml-research-read_project_file-1778891987655.txt\n\nThis is a JSON file with schema: {result: string}. The inner `result` field contains a YAML string representing a literature_map.yaml for an ML research project called FREIGE (about evidence-grounded document-level relation extraction).\n\nExtract ALL papers from this literature map. For each paper, I need:\n- The citation key (e.g., author_year)\n- The title\n- The category/section it belongs to\n- A one-line summary of what the paper does\n\nGroup them by category. Return the COMPLETE list — do not skip any papers. This is critical for writing a Related Work section. Format as structured text, not YAML."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "1956675a-54f4-4e15-8dc8-f69771eef121",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BJFJFFCm2dgBWSN2ndSXBB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6746,
      "cache_read_input_tokens": 24051,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6746
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

### System

_source line 15_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "ad94f71e34c9ad9c0",
  "tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "description": "Extract literature map data",
  "task_type": "local_agent",
  "prompt": "Read the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7341df47-ab61-4a7f-ab4b-fc80cccd2794/tool-results/mcp-agent-ml-research-read_project_file-1778891987655.txt\n\nThis is a JSON file with schema: {result: string}. The inner `result` field contains a YAML string representing a literature_map.yaml for an ML research project called FREIGE (about evidence-grounded document-level relation extraction).\n\nExtract ALL papers from this literature map. For each paper, I need:\n- The citation key (e.g., author_year)\n- The title\n- The category/section it belongs to\n- A one-line summary of what the paper does\n\nGroup them by category. Return the COMPLETE list — do not skip any papers. This is critical for writing a Related Work section. Format as structured text, not YAML.",
  "uuid": "5e0c8021-57dc-477d-900d-0b874856628c",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794"
}
```

---

## Round 1

69 recorded events

### User

_source line 16 · 2026-05-16T00:40:02.588Z_

Read the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7341df47-ab61-4a7f-ab4b-fc80cccd2794/tool-results/mcp-agent-ml-research-read_project_file-1778891987655.txt

This is a JSON file with schema: {result: string}. The inner `result` field contains a YAML string representing a literature_map.yaml for an ML research project called FREIGE (about evidence-grounded document-level relation extraction).

Extract ALL papers from this literature map. For each paper, I need:
- The citation key (e.g., author_year)
- The title
- The category/section it belongs to
- A one-line summary of what the paper does

Group them by category. Return the COMPLETE list — do not skip any papers. This is critical for writing a Related Work section. Format as structured text, not YAML.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "30c628d2-a762-4b46-b99b-08ca5146fd09"
}
```

</details>

---

### System

_source line 17_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad94f71e34c9ad9c0",
  "tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7341df47-ab61-4a7f-ab4b-fc80cccd2794/tool-results/mcp-agent-ml-research-read_project_file-1778891987655.txt",
  "usage": {
    "total_tokens": 14288,
    "tool_uses": 1,
    "duration_ms": 3342
  },
  "last_tool_name": "Read",
  "uuid": "adffd6e5-cf9d-40dd-b2ac-6fad0ad539cd",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794"
}
```

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_01URrC59tJD6rdhJSmBSwmeY`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7341df47-ab61-4a7f-ab4b-fc80cccd2794/tool-results/mcp-agent-ml-research-read_project_file-1778891987655.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "e69e26c4-0699-465d-9ba1-1550fc8059b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018LqhDadQDoUsNgSwRZrfp9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14281,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14281,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 19 · 2026-05-16T00:40:06.179Z_

<details><summary>↩ Tool result · reported error · `toolu_01URrC59tJD6rdhJSmBSwmeY`</summary>

```text
File content (36391 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "77e26daf-8427-47bb-8adc-cc0679bf33d9",
  "tool_use_result": "Error: File content (36391 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### System

_source line 20_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad94f71e34c9ad9c0",
  "tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7341df47-ab61-4a7f-ab4b-fc80cccd2794/tool-results/mcp-agent-ml-research-read_project_file-1778891987655.txt",
  "usage": {
    "total_tokens": 15347,
    "tool_uses": 2,
    "duration_ms": 7035
  },
  "last_tool_name": "Read",
  "uuid": "f612aabc-2273-4e3b-a9cb-9f9b4b4b8c6c",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794"
}
```

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_01BApisSTT4eDBLGMAuVyA4y`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7341df47-ab61-4a7f-ab4b-fc80cccd2794/tool-results/mcp-agent-ml-research-read_project_file-1778891987655.txt",
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "5728ffd9-8570-4d24-a72a-5cec7834a471",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FFHu3BxPewZuxKZGdtK2Ti",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1053,
      "cache_read_input_tokens": 14281,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1053,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 22 · 2026-05-16T00:40:09.909Z_

<details><summary>↩ Tool result · reported error · `toolu_01BApisSTT4eDBLGMAuVyA4y`</summary>

```text
File content (36391 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "e4bb5d69-222e-45cd-8d3a-1a7324d296dd",
  "tool_use_result": "Error: File content (36391 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### System

_source line 23_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad94f71e34c9ad9c0",
  "tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7341df47-ab61-4a7f-ab4b-fc80cccd2794/tool-results/mcp-agent-ml-research-read_project_file-1778891987655.txt",
  "usage": {
    "total_tokens": 15351,
    "tool_uses": 3,
    "duration_ms": 7937
  },
  "last_tool_name": "Read",
  "uuid": "f9889f71-d398-4d0e-b75f-c3fd21cd657d",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794"
}
```

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Read · `toolu_01MACNaMieNBPrXaX5G4jzyn`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7341df47-ab61-4a7f-ab4b-fc80cccd2794/tool-results/mcp-agent-ml-research-read_project_file-1778891987655.txt",
  "offset": 500,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "efebae68-22a3-40f7-8a04-10a7e9184fce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FFHu3BxPewZuxKZGdtK2Ti",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1053,
      "cache_read_input_tokens": 14281,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1053,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 25 · 2026-05-16T00:40:10.547Z_

<details><summary>↩ Tool result · `toolu_01MACNaMieNBPrXaX5G4jzyn`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (500). The file has 1 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "ee529359-479e-42e1-9e1a-180fde9269ea"
}
```

</details>

---

### System

_source line 26_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad94f71e34c9ad9c0",
  "tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "description": "Running Check file size",
  "usage": {
    "total_tokens": 15814,
    "tool_uses": 4,
    "duration_ms": 11700
  },
  "last_tool_name": "Bash",
  "uuid": "726939ca-5224-4075-a125-2c36a54c4e5d",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794"
}
```

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Bash · `toolu_01GrEnsxemGA7ooy63uNX8mn`</summary>

```json
{
  "command": "wc -c /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7341df47-ab61-4a7f-ab4b-fc80cccd2794/tool-results/mcp-agent-ml-research-read_project_file-1778891987655.txt",
  "description": "Check file size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "a2010dc4-edfb-4d24-8729-b9ff9865f5cf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TAHc5ntkvLEqShWz5vW9mQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 461,
      "cache_read_input_tokens": 15334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 461,
        "ephemeral_1h_input_tokens": 0
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

### Tool result

_source line 28 · 2026-05-16T00:40:14.525Z_

<details><summary>↩ Tool result · `toolu_01GrEnsxemGA7ooy63uNX8mn`</summary>

```text
100624 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7341df47-ab61-4a7f-ab4b-fc80cccd2794/tool-results/mcp-agent-ml-research-read_project_file-1778891987655.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "3107fef6-0dd0-4ca1-a4ec-183526b14b7d"
}
```

</details>

---

### System

_source line 29_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad94f71e34c9ad9c0",
  "tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "description": "Running Parse JSON and print first 5000 chars of the YAML result",
  "usage": {
    "total_tokens": 16172,
    "tool_uses": 5,
    "duration_ms": 15824
  },
  "last_tool_name": "Bash",
  "uuid": "94799832-24f4-4f9b-ab56-55f9ba274515",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794"
}
```

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Bash · `toolu_011ttUeMnbYpNTn7na6XWoHK`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7341df47-ab61-4a7f-ab4b-fc80cccd2794/tool-results/mcp-agent-ml-research-read_project_file-1778891987655.txt', 'r') as f:\n    data = json.load(f)\n\nresult = data['result']\nprint(result[:5000])\n\"",
  "description": "Parse JSON and print first 5000 chars of the YAML result"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "c767a313-06c4-4671-86bb-02d91c9c0d6b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C7hfLcGHmqanznACjt3iR6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 287,
      "cache_read_input_tokens": 15795,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 287,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 71,
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

_source line 31 · 2026-05-16T00:40:18.538Z_

<details><summary>↩ Tool result · `toolu_011ttUeMnbYpNTn7na6XWoHK`</summary>

```text
{"success": true, "data": {"path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml", "content": "# Literature Map for faith-evidence-ie (FREIGE)\n# Focus: CED-as-training-stabilizer (D024) + RSFT for DocRE\n# Updated: 2026-05-16 (W4 expanded: +11 papers from literature scan; +15 papers from Related Work survey; +17 papers from Related Work expansion; +16 papers from Related Work extension scan)\n\npapers:\n\n  # === Category 1: Reward Diversity / Reward Shaping for RL Stability ===\n\n  - title: \"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization\"\n    authors: NVIDIA Labs\n    year: 2025\n    venue: ICML 2026\n    url: https://arxiv.org/abs/2601.05242\n    category: reward_diversity\n    role: closest_prior_work\n    key_finding: >\n      直接将 GRPO 应用于多 reward 组合时，不同 rollout 的 reward 组合在归一化后 collapse 为相同 advantage 值，\n      降低训练信号分辨率导致收敛失败。GDPO 对每个 reward 独立做 group-wise normalization 再聚合，\n      保留多 reward 的相对差异，显著提升训练稳定性。\n    relevance_to_ced_stabilizer: >\n      最直接相关。CED reward 本质上引入了独立于 extraction F1 的 reward 维度（evidence quality），\n      GDPO 的理论分析解释了为什么多维 reward 比单一 reward 更稳定——独立 reward 维度防止 advantage collapse。\n      但 GDPO 是方法论贡献，CED 是 task-specific reward 设计自然具备了这一特性。\n\n  - title: \"DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of LLMs\"\n    authors: Xiwen Chen et al.\n    year: 2025\n    venue: arXiv 2505.09655\n    url: https://arxiv.org/abs/2505.09655\n    category: reward_diversity\n    role: related_method\n    key_finding: >\n      GRPO 的标量 reward 无法区分语义多样但得分相同的输出（diversity-quality inconsistency）。\n      DRA 用子模互信息（SMI）对 reward 加权，给多样性高的 completion 更大权重，\n      等价于 Inverse Propensity Scoring 去偏，防止 policy 坍缩到先验模式。\n    relevance_to_ced_stabilizer: >\n      DRA 通过后处理 reward 注入多样性信号；CED 的 reward 本身就内含对比结构自然提供 diversity 信号。\n      机制互补但来源不同——CED 是 reward design 层面，DRA 是 optimization 层面。\n\n  - title: \"Shrinking the Variance: Shrinkage Baselines for RL with Verifiable Rewards\"\n    authors: Guanning Zeng et al.\n    year: 2025\n    venue: arXiv 2511.03710\n    url: https://arxiv.org/abs/2511.03710\n    category: reward_diversity\n    role: theoretical_support\n    key_finding: >\n      RLVR 中 per-prompt 均值 baseline 在低 generation 数下估计不准导致高 variance 梯度。\n      用 James-Stein shrinkage 混合 per-prompt 和 cross-prompt 均值，\n      构造可证明更低 variance 的 policy gradient estimator。\n    relevance_to_ced_stabilizer: >\n      理论支持：reward variance 对 gradient estimation 质量至关重要。\n      CED 的额外 reward 维度提供更丰富的 per-group variance，间接起到 variance 维持效果。\n\n  - title: \"Reward Shaping to Mitigate Reward Hacking in RLHF\"\n    authors: Anonymous\n    year: 2025\n    venue: arXiv 2502.18770\n    url: https://arxiv.org/abs/2502.18770\n    category: reward_diversity\n    role: background\n    key_finding: >\n      RL reward 应有界且先快速增长后缓慢收敛。系统研究 reward shaping 原则，\n      好的 reward 形状能抑制 reward hacking 并提升训练稳定性。\n    relevance_to_ced_stabilizer: >\n      CED reward 的 0-1 对比判别结构天然满足有界性，\n      且 evidence quality 的渐进提升符合\"先快后慢\"的 reward shaping 原则。\n\n  # === Category 2: Mode Collapse Prevention in GRPO/RLHF ===\n\n  - title: \"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\"\n    authors: ByteDance Seed, Tsinghua AIR\n    year: 2025\n    venue: NeurIPS 2025\n    url: https://arxiv.org/abs/2503.14476\n    category: mode_collapse_prevention\n    role: key_baseline\n    key_finding: >\n      Naive GRPO 存在 entropy collapse（policy 熵快速下降→输出同质化）。\n      根因：clipping 不对称性——概率 0.01 的 token 最多增到 0.012，而概率 0.9 的 token 可达 1.08，\n      低概率 token 难以增长，抑制探索。DAPO 提出 Clip-Higher（εhigh=0.28 > εlow=0.2）\n      为低概率 token 留更大增长空间，加 Dynamic Sampling 过滤 accuracy=0 或 1 的 prompt\n      （这些 prompt 产生零梯度，降低有效 batch size）。在 AIME 2024 达 50 分超越 DeepSeek-R1-Zero。\n    relevance_to_ced_stabilizer: >\n      DAPO 从 optimization 技巧角度解决 entropy collapse。CED reward 从 reward design 层面\n      防止 mode collapse——evidence quality 维度确保 reward 组内有足够 variance，\n      不会出现 all-same-reward 的零梯度 prompt。DAPO 的 Dynamic Sampling 过滤 accuracy=0/1 prompt\n      与我们观察到的 frac_zero_std→0.8 现象本质相同：extraction-only reward 下大量 prompt\n      产生零 advantage，CED 从源头（reward 设计）而非后处理（过滤）解决这个问题。\n\n  - title: \"Dr. GRPO: Removing Optimization Bias in GRPO\"\n    authors: Liu et al.\n    year: 2025\n    venue: COLM 2025\n    url: https://arxiv.org/abs/2503.20783\n    category: mode_collapse_prevention\n    role: related_analysis\n    key_finding: >\n      GRPO 的 std 归一化引入两个 bias：(1) difficulty bias——std(r) 归一化对低 variance 组\n      （全对/全错）给予过高 advantage 权重，trivial question 主导训练信号；\n      (2) length bias——per-token loss 的 1/|o_i| 项使长的错误回答被 under-penalize。\n      当 std(r)→0 时 advantage 爆炸或未定义，梯度数值不稳定。\n      Dr. GRPO 移除 std 归一化，用无偏 Monte Carlo advantage：Ã = R(q,o_i) - mean(R)。\n    relevance_to_ced_stabilizer: >\n      与我们的实验发现高度一致：extraction-only reward 下 frac_zero_std→0.8 正是\n      Dr. GRPO 分析的 difficulty bias 极端情况——大量 prompt 的所有 rollout 得到相同 F1，\n
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "fb1cd602-16ba-40a9-a4fb-0d519fb3f1cb"
}
```

</details>

---

### System

_source line 32_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad94f71e34c9ad9c0",
  "tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "description": "Running Parse and print chars 5000-15000 of the YAML content",
  "usage": {
    "total_tokens": 18799,
    "tool_uses": 6,
    "duration_ms": 20273
  },
  "last_tool_name": "Bash",
  "uuid": "860df51f-671e-42d7-9da3-8e96a9712d40",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794"
}
```

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Bash · `toolu_01CG1dP9b6bsSp5gm45ZiC2K`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7341df47-ab61-4a7f-ab4b-fc80cccd2794/tool-results/mcp-agent-ml-research-read_project_file-1778891987655.txt', 'r') as f:\n    data = json.load(f)\n\nresult = data['result']\n# It's a nested JSON - the result field itself is JSON\ninner = json.loads(result)\ncontent = inner['data']['content']\nprint(content[5000:15000])\n\"",
  "description": "Parse and print chars 5000-15000 of the YAML content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "65d0a3cf-f5a9-48ed-a478-4e761d13af35",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019McjmQP58LVF27indDBWfz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2554,
      "cache_read_input_tokens": 16082,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2554,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 73,
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

_source line 34 · 2026-05-16T00:40:22.961Z_

<details><summary>↩ Tool result · `toolu_01CG1dP9b6bsSp5gm45ZiC2K`</summary>

```text
xiv.org/abs/2504.19599
    category: mode_collapse_prevention
    role: alternative_framework
    key_finding: >
      将 KL 约束 reward 最大化的解析解直接嵌入梯度权重，
      variance 项自然平衡 exploration 与 exploitation，维持适度 entropy。
    relevance_to_ced_stabilizer: >
      GVPO 的 variance 项机制与 CED 维持 reward variance 的效果功能类似，
      但 GVPO 是算法层面 implicit regularization，CED 是 reward 层面 explicit structure。

  - title: "REINFORCE++: Stabilizing Critic-Free Policy Optimization with Global Advantage Normalization"
    authors: Jian Hu et al.
    year: 2025
    venue: arXiv 2501.03262
    url: https://arxiv.org/abs/2501.03262
    category: mode_collapse_prevention
    role: related_method
    key_finding: >
      Prompt-level (local) advantage normalization 导致不准确估计和过拟合。
      Global batch normalization 提供更稳定、理论无偏的 gradient estimator。
    relevance_to_ced_stabilizer: >
      解决 local normalization 的 variance 问题；CED 从 reward 端增加 variance 来源。
      两者在不同层面解决同一问题：防止 gradient signal 消失。

  - title: "DiverseGRPO: Mitigating Mode Collapse in Image Generation via Diversity-Aware GRPO"
    authors: Henglin Liu et al.
    year: 2025
    venue: arXiv 2512.21514
    url: https://arxiv.org/abs/2512.21514
    category: mode_collapse_prevention
    role: parallel_work
    key_finding: >
      图像生成中 GRPO 后期输出同质化。distributional reward modeling（谱聚类+exploratory reward）
      和 structure-aware regularization 实现 13-18% 语义多样性提升。
    relevance_to_ced_stabilizer: >
      跨域验证了 GRPO mode collapse 的普遍性，distributional reward 思路与 CED 精神相近——
      都是通过 reward 层面结构化信号维持输出多样性。

  - title: "Why GRPO Needs Normalization: A Local-Curvature Perspective on Adaptive Gradients"
    authors: Anonymous
    year: 2025
    venue: arXiv 2601.23135
    url: https://arxiv.org/abs/2601.23135
    category: mode_collapse_prevention
    role: theoretical_support
    key_finding: >
      GRPO 的 reward_std 归一化在温和条件下提供严格优于未归一化 REINFORCE 的收敛速率，
      收益由 prompt 间平均 reward std 刻画。
    relevance_to_ced_stabilizer: >
      直接理论支撑：reward_std 越大收敛越好。CED 通过 evidence quality 维度维持高 reward_std，
      从该理论看 CED 的稳定性优势是 reward_std 维持带来的收敛速率优势。

  # === Category 3: Contrastive Rewards in RL ===

  - title: "Improving Reinforcement Learning from Human Feedback Using Contrastive Rewards"
    authors: Shen, Zhang et al.
    year: 2024
    venue: arXiv 2403.07708
    url: https://arxiv.org/abs/2403.07708
    category: contrastive_reward
    role: closest_contrastive_precedent
    key_finding: >
      两步机制：(1) 离线采样 baseline response；(2) 用 baseline 计算 contrastive reward
      作为 PPO 的 penalty 项。效果：惩罚 reward uncertainty、根据任务难度自适应校准、
      减少 PPO 中的 variance。在 TL;DR 和 HH-RLHF 上持续优于标准 RLHF。
    relevance_to_ced_stabilizer: >
      最接近的对比 reward 先例。关键差异：(1) 它是对 learned RM 输出的后处理对比，
      CED 是 reward function 本身就是对比判别（evidence vs. corrupted evidence）；
      (2) 它在 PPO 中验证，CED 在 GRPO 中验证；
      (3) 它是 domain-agnostic penalty，CED 是 task-specific faithfulness signal。
      stabilizing 机制相通但实现路径根本不同。

  - title: "Improving Discriminative Capability of Reward Models in RLHF Using Contrastive Learning"
    authors: Anonymous
    year: 2024
    venue: EMNLP 2024
    url: https://aclanthology.org/2024.emnlp-main.852/
    category: contrastive_reward
    role: related_method
    key_finding: >
      无监督对比损失训练 reward model 充分捕捉对比数据区分度，
      带来更稳定的 PPO 训练 return 和 reward。
    relevance_to_ced_stabilizer: >
      验证对比训练 reward model → 更稳定 RL 训练链条。CED 不是对比训练 reward model，
      而是 reward function 本身就是对比判别，但 stabilizing 机制相通。

  - title: "Contrastive Preference Learning: Learning from Human Feedback without RL"
    authors: Anonymous
    year: 2024
    venue: ICLR 2025
    url: https://openreview.net/forum?id=iX1RjVQODj
    category: contrastive_reward
    role: background
    key_finding: >
      将 preference learning 重新表述为对比学习问题，无需显式 RL 即可从人类反馈中学习。
    relevance_to_ced_stabilizer: >
      对比框架在 preference alignment 中的通用性。CED 可被视为 task-specific contrastive preference signal。

  # === Category 4: Evidence-Based Rewards in IE/NLP ===

  - title: "Drift: Enhancing LLM Faithfulness in Rationale Generation"
    authors: Anonymous
    year: 2025
    venue: ACL 2025
    url: https://aclanthology.org/2025.acl-long.340.pdf
    category: evidence_reward
    role: related_method
    key_finding: >
      用 faithfulness reward 引导 LLM 生成更可靠的 rationale，提升 CoT 推理事实一致性。
    relevance_to_ced_stabilizer: >
      Faithfulness reward 用于生成质量的先例。CED 中 evidence discrimination
      本质上也是 faithfulness 信号——判断证据是否忠实支持抽取结果。

  - title: "Fine-Grained NLI-Based Faithfulness Evaluation for Diverse Summarisation Tasks (INFUSE)"
    authors: Anonymous
    year: 2024
    venue: EACL 2024
    url: https://aclanthology.org/2024.eacl-long.102/
    category: evidence_reward
    role: background
    key_finding: >
      变长前提+简化假设的细粒度 NLI faithfulness 评估，超越传统 NLI 在多任务摘要上的表现。
    relevance_to_ced_stabilizer: >
      NLI 作为 faithfulness 评估工具的进展。CED 中 NLI 组件用于判断 evidence 对 triple 的支持度。

  - title: "Enhancing Cross-Evidence Reasoning Graph for Document-Level Relation Extraction"
    authors: Anonymous
    year: 2024
    venue: PMC/Bioinformatics 2024
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11232587/
    category: evidence_reward
    role: background
    key_finding: >
      文档级关系抽取中用 cross-evidence reasoning graph 增强跨证据推理。
    relevance_to_ced_stabilizer: >
      DocRE 中 evidence 的重要性。但用 evidence 作为模型输入特征，
      我们用 evidence quality 作为 RL reward 信号——定位根本不同。

  # === Category 5: Multi-Objective RL for Text Generation ===

  - title: "Confronting Reward Model Overoptimization with Constrained RLHF"
    authors: Anonymous
    year: 2025
    venue: OpenReview
    url: https://openreview.net/forum?id=gkfUvn0fLU
    category: multi_objective_rl
    role: related_analysis
    key_finding: >
      多组件 RM 的 overoptimization 研究。component RM 间的相关性显著影响 overoptimization 临界点，
      用 constrained MDP 防止超出适当边界。
    relevance_to_ced_stabilizer: >
      CED 引入了与 extraction F1 低相关的 reward component（evidence quality），
      根据该论文分析低相关多组件 reward 更不易 overoptimize，
      可能是 CED 稳定性的另一个理论解释角度。

  - title: "On-Policy RL with Optimal Reward Baseline"
    authors: Anonymous
    year: 2025
    venue: arXiv 2505.23585
    url: https://arxiv.org/abs/2505.23585
    category: multi_objective_rl
    role: theoretical_support
    key_finding: >
      Optimal baseline 一致性地实现更高训练 reward 和更高 entropy，
      有效稳定训练并促进更多样的 policy exploration。
    relevance_to_ced_stabilizer: >
      CED reward 的多维特性可能起到类似 optimal baseline 效果——
      evidence quality 维度为 advantage estimation 提供更丰富的参照信号。

  # === Category 6: RSFT Methodology & Theory ===

  - title: "A Minimalist Approach to LLM Reasoning: from Rejection Sampling to Reinforce"
    authors: Xiao et al.
    year: 2025
    venue: arXiv 2504.11343
    url: https://arxiv.org/abs/2504.11343
    category: rsft_methodology
    role: key_theoretical_support
    key_finding: >
      RAFT（简单 rejection sampling baseline）在数学推理上与 GRPO/PPO 表现相当。
      消融实验表明 GRPO 的主要优势来自丢弃全错 prompt 而非 reward normalization。
      提出 Reinforce-Rej，在 RAFT 基础上过滤全对和全错 sample。
      关键洞察：GRPO 和 RAFT 的核心区别在于负样本处理——GRPO 混合正负样本训练，
      RAFT 只用正样本，但 RAFT 仍能达到相当性能，说明 rejection sampling 的简单性被低估了。
    relevance_to_rsft_docre: >
      直接支持我们的设计选择：(1) RSFT 在 DocRE 上成功而 GRPO 失败，
      与该论文发现一致——rejection sampling 的 offline 特性天然避免了 catastrophic forgetting；
      (2) GRPO 主要优势来自过滤全错 prompt，这与我们 RSFT 的 reward-based filtering 机制相同；
      (3) DocRE structured output 比 math reasoning 更难用 online RL 优化，
      强化了 offline RSFT 的合理性。

  - title: "Beyond Rejection Sampling: Trajectory Fusion for Scaling Mathematical Reasoning (TrajFusion)"
    authors: Jie Deng et al.
    year: 2026
    venue: arXiv 2602.04391
    url: https://arxiv.org/abs/2602.04391
    category: rsft_methodology
    role: method_component
    key_finding: >
      传统 RSFT 只用正确轨迹，丢弃错误轨迹。TrajFusion 将错误和正确轨迹交替拼接，
      显式建模试错推理过程，在困难数学问题上显著超越标准 RFT。
    relevance_to_rsft_docre: >
      Future work 方向：可考虑在 DocRE RSFT 中融合失败样本的信息。
      但 DocRE 的结构化输出（JSON triple）不同于 math 的 chain-of-thought，
      融合方式需要重新设计。

  - title: "Rejection Sampling Based Fine Tuning Secretly Performs PPO"
    authors: Anonymous
    year: 2025
    venue: ICML 2025
    url: https://openreview.net/forum?id=yQ2UivKlir
    category: rsft_methodology
    role: theoretical_support
    key_finding: >
      建立 RSFT 与 PPO 之间的理论联系：rejection sampling fine-tuning
      在特定条件下隐式执行 PPO with marginal KL constraints。
    relevance_to_rsft_docre: >
      为 RSFT 的有效性提供理论解释。我们的 RSFT 成功可被视为
      隐式执行了 constrained policy optimization，
      避免了显式 GRPO 在 structured output 上的不稳定性。

  # === Category 7: RL for Information Extraction ===

  - title: "R1-RE: Cross-Domain Relation Extraction with RLVR"
    authors: Runpeng Dai, Tong Zheng et al.
    year: 2025
    venue: arXiv 2507.04642
    url: https://arxiv.org/abs/2507.04642
    category: rl_for_ie
    role: direct_competitor
    key_finding: >
      首个将 RLVR（GRPO + verifiable reward）用于关系抽取的框架。
      将 RE 重构为推理任务，R1-RE-7B 在跨域 OOD 准确率约 70%，媲美 GPT-4o。
      Reward 设计：format reward (+1/-3) + metric reward (+2/-1.5)，先验证格式再加准确度。
      triplet extraction 用 F1-based reward（entity weight=1, triplet weight=3）。
      未报告 catastrophic forgetting——GRPO 训练后在 MATH-500/IFEval/GPQA 上性能不降反升，
      说明句子级 RE 的简单 reward 结构足以稳定 GRPO 训练。
    results:
      sem2010_in_domain: 91.8
      sem2010_ood: 66.5
      mdkg_in_domain: 88.1
      mdkg_ood: 65.8
    evidence_generation: false
    relevance_to_rsft_docre: >
      最直接竞争者。关键差异与讨论：
      (1) R1-RE 是句子级 RE，GRPO 成功；我们是文档级 RE，GRPO 失败→RSFT 成功。
      句子级 RE 每个 sample 只有 1 个 triple（binary classification），reward variance 天然充足；
      文档级 RE 每个 sample 有数十个 triple，F1 score 作为 reward 在 group 内趋于同质化（frac_zero_std→0.8）。
      (2) R1-RE 未报告 catastrophic forgetting，进一步支持"句子级简单 reward 可行，文档级需要 CED"的论点。
      (3) R1-RE 关注 OOD 泛化，无 evidence 组件；我们关注 evidence-grounded extraction quality。
      互补而非直接冲突——R1-RE 证明 RLVR for RE 可行，我们揭示文档级需要额外设计。

  - title: "MORE-R1: Guiding LVLM for Multimodal Object-Entity Relation Extraction via
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "49ad784e-7db4-43f4-a5fd-dc1f1b31e354"
}
```

</details>

---

### System

_source line 35_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad94f71e34c9ad9c0",
  "tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "description": "Running Print chars 15000-30000 of the YAML content",
  "usage": {
    "total_tokens": 23599,
    "tool_uses": 7,
    "duration_ms": 27418
  },
  "last_tool_name": "Bash",
  "uuid": "5a81705d-c8c6-4038-95fe-68d54cd74fa6",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794"
}
```

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Bash · `toolu_01RXLgbZbpghhbBuszHYBTSW`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7341df47-ab61-4a7f-ab4b-fc80cccd2794/tool-results/mcp-agent-ml-research-read_project_file-1778891987655.txt', 'r') as f:\n    data = json.load(f)\n\nresult = data['result']\ninner = json.loads(result)\ncontent = inner['data']['content']\nprint(content[15000:30000])\n\"",
  "description": "Print chars 15000-30000 of the YAML content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "748b305d-7daf-41be-970d-576fece5bbe9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SVF7nhXhXgH6xuGwXT1Uvi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4755,
      "cache_read_input_tokens": 18636,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4755,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
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

_source line 37 · 2026-05-16T00:40:30.138Z_

<details><summary>↩ Tool result · `toolu_01RXLgbZbpghhbBuszHYBTSW`</summary>

```text
 Stepwise Reasoning with RL"
    authors: Anonymous
    year: 2026
    venue: arXiv 2603.09478
    url: https://arxiv.org/abs/2603.09478
    category: rl_for_ie
    role: related_method
    key_finding: >
      多模态 RE 中用 GRPO + Progressive Sample-Mixing Strategy 优化 LVLM 推理能力。
      两阶段训练：SFT cold-start + GRPO RL。
    relevance_to_rsft_docre: >
      跨模态验证 RL for RE 趋势。其 Progressive Sample-Mixing 与我们
      RSFT 的 difficulty-aware sampling 思想相通，但在不同模态。

  - title: "REAR: Reinforced Reasoning Optimization for Event Argument Extraction with Relation-Aware Support"
    authors: Jianwen Luo et al.
    year: 2025
    venue: EMNLP 2025 Findings
    url: https://2025.emnlp.org/program/find_papers/
    category: rl_for_ie
    role: related_method
    key_finding: >
      将强化学习推理优化用于事件论元抽取，结合关系感知支持。
      不同于 DocRE 但同属 IE 领域的 RL 应用。
    relevance_to_rsft_docre: >
      验证 RL 在 IE 任务上的有效性趋势。我们的工作扩展到 DocRE + evidence，
      且使用 offline RSFT 而非 online RL。

  - title: "Adaptive Reinforcement Learning Planning: Harnessing LLMs for Complex Information Extraction"
    authors: Zepeng Ding et al.
    year: 2024
    venue: arXiv 2406.11455
    url: https://arxiv.org/abs/2406.11455
    category: rl_for_ie
    role: background
    key_finding: >
      将 LLM 顺序抽取建模为 MDP，用 DDQN 训练 decision module
      自适应选择实体抽取顺序，提升复杂 IE 性能。
    relevance_to_rsft_docre: >
      RL for IE 的早期工作。用 RL 优化抽取策略而非模型本身，
      与我们 RSFT 直接微调 LLM 的方法路径不同。

  - title: "Graph-R1: Towards Agentic GraphRAG Framework via End-to-end Reinforcement Learning"
    authors: Haoran Luo et al.
    year: 2025
    venue: ICML 2026
    url: https://arxiv.org/abs/2507.21892
    category: rl_for_ie
    role: background
    key_finding: >
      用端到端 RL 优化 GraphRAG agent 的多轮检索-推理循环，
      包含 knowledge hypergraph construction（n-ary relation extraction）。
    relevance_to_rsft_docre: >
      RL + knowledge extraction 的交叉点。Graph-R1 关注 QA 场景下的知识图谱构建，
      我们关注 DocRE 的训练优化，应用场景不同。

  # === Category 8: Recent LLM-based DocRE Methods ===

  - title: "RelPrior: Relation as a Prior - A Novel Paradigm for LLM-based Document-level Relation Extraction"
    authors: Anonymous
    year: 2025
    venue: arXiv 2511.08143
    url: https://arxiv.org/abs/2511.08143
    category: llm_docre
    role: key_baseline
    key_finding: >
      用 binary relation 作为先验过滤无关实体对，再用 predefined relation 匹配实体，
      避免 LLM 在 DocRE 中被无关实体对分散注意力。
      在 DocRED/Re-DocRED 上超越现有纯 LLM-based DocRE 方法。
    results:
      docred_dev_f1: 47.82
      docred_test_f1: 48.34
      re_docred_dev_f1: 55.94
      re_docred_test_f1: 54.80
      backbone: LLaMA3-8B
    evidence_generation: false
    relevance_to_rsft_docre: >
      我们的直接 baseline 之一。RelPrior_LLaMA3-8B 在 DocRED test F1=48.34,
      Re-DocRED test F1=54.80。我们的 RSFT 提升显著更优。
      RelPrior 是 inference paradigm 创新（两阶段筛选），我们是 training paradigm 创新（RSFT+CED），正交互补。

  - title: "LMRC: LLM with Relation Classifier for Document-Level Relation Extraction"
    authors: Xingzuo Li, Kehai Chen, Yunfei Long, Min Zhang
    year: 2024
    venue: arXiv 2408.13889
    url: https://arxiv.org/abs/2408.13889
    category: llm_docre
    role: related_method
    key_finding: >
      两阶段方法：先用 attention-based classifier 过滤 NA 实体对（RCP），
      再用 LLM 在精简候选空间中做多分类（RC）。
      注意：LMRC 依赖 BERT-based classifier 作为预筛选，非纯 LLM 方法。
    results:
      docred_dev_ign_f1: 58.16
      docred_dev_f1: 59.97
      docred_test_ign_f1: 58.49
      docred_test_f1: 60.52
      re_docred_test_ign_f1: 74.08
      re_docred_test_f1: 74.63
      backbone: BERT classifier + LLM
    evidence_generation: false
    relevance_to_rsft_docre: >
      LMRC 在 DocRED test F1=60.52, Re-DocRED test F1=74.63，性能显著高于纯 LLM 方法。
      但它依赖 BERT classifier 预筛选，本质上是 hybrid 方法而非纯 LLM generative。
      与我们端到端 LLM 生成方式不同——我们通过 RSFT 的 reward-based filtering 隐式解决 class imbalance。

  - title: "Ru-LLM: Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction"
    authors: Anonymous
    year: 2025
    venue: NLPCC 2025
    url: https://link.springer.com/chapter/10.1007/978-981-95-3343-5_11
    category: llm_docre
    role: related_method
    key_finding: >
      用频繁模式挖掘 + MCTS 搜索逻辑规则，转化为 prompt 约束 LLM 输出，
      再用 CoT 验证过滤不满足规则的 triple。
      在 DWIE、DocRED、Re-DocRED 上声称超越现有 LLM 方法和规则框架。
      具体 F1 未公开获取（Springer 付费墙），但声称超越 AutoRE 等 LLM baseline。
    results:
      note: "behind Springer paywall; claims SOTA over LLM baselines on DocRED/Re-DocRED/DWIE"
    evidence_generation: false
    relevance_to_rsft_docre: >
      规则约束方式与我们的 CED reward 在 motivation 上相似（都是引入外部知识约束），
      但 Ru-LLM 用 inference-time 规则验证（MCTS+CoT），我们用 training-time reward shaping（CED）。
      Ru-LLM 的规则是数据集级别的频繁模式，CED 是 instance-level 的 evidence faithfulness。

  - title: "GLiDRE: Generalist Lightweight model for Document-level Relation Extraction"
    authors: Anonymous
    year: 2025
    venue: arXiv 2508.00757
    url: https://arxiv.org/abs/2508.00757
    category: llm_docre
    role: background
    key_finding: >
      基于 dual-encoder 的轻量级零/少样本 DocRE 模型，
      预训练于 136K 文档的大规模 RE 数据。
      fully supervised Re-DocRED test F1=77.83，但这是 encoder-based 非 LLM generative。
      zero-shot Re-DocRED test F1=17.32（超越 LLaMA 3.3 70B 和 Mistral-Small 24B）。
    results:
      re_docred_dev_f1: 77.76
      re_docred_test_f1: 77.83
      re_docred_zero_shot_test_f1: 17.32
      fredo_in_domain_1doc_f1: 13.00
      fredo_in_domain_3doc_f1: 15.71
      backbone: "dual-encoder (few hundred M params)"
    evidence_generation: false
    relevance_to_rsft_docre: >
      不同范式（encoder-based vs LLM generative）。GLiDRE 的 fully supervised F1=77.83
      远超 LLM-based 方法（RelPrior 54.80），但依赖大规模预训练数据和 encoder 架构。
      与我们不直接可比——我们关注 LLM generative 范式下的训练优化。

  - title: "AutoRE: Document-Level Relation Extraction with Large Language Models"
    authors: Anonymous
    year: 2024
    venue: arXiv 2403.14888
    url: https://arxiv.org/abs/2403.14888
    category: llm_docre
    role: background
    key_finding: >
      RHF（Relation-Head-Facts）范式用 Mistral-7B + QLoRA 做端到端 DocRE。
      关键设计：先抽 relation，再抽 head entity，最后抽 fact triple。
    results:
      re_docred_dev_f1_mistral: 53.01
      re_docred_test_f1_mistral: 51.91
      re_docred_dev_f1_vicuna: 54.29
      re_docred_test_f1_vicuna: 53.84
      docred_dev_f1_llama3: 45.76
      docred_test_f1_llama3: 45.96
      re_docred_dev_f1_llama3: 52.28
      re_docred_test_f1_llama3: 51.97
      backbone: "Mistral-7B / Vicuna-7B / LLaMA3-8B (QLoRA)"
    evidence_generation: false
    relevance_to_rsft_docre: >
      QLoRA fine-tuning for DocRE 的先例。AutoRE_LLaMA3-8B 在 Re-DocRED test F1=51.97,
      DocRED test F1=45.96。我们的 SFT baseline 与之类似，
      RSFT 在此基础上引入 reward-guided sample selection 进一步提升。

  # === Category 9: Evidence Generation & Task Performance Trade-off ===
  # (NEW - 2026-05-15 evidence generation survey)

  - title: "Mind Your Step (by Step): Chain-of-Thought can Reduce Performance on Tasks where Thinking Makes Humans Worse"
    authors: Sprague et al.
    year: 2024
    venue: NeurIPS 2024
    url: https://arxiv.org/abs/2410.21333
    category: evidence_generation_tradeoff
    role: key_evidence
    key_finding: >
      CoT 在某些任务上降低性能高达 36.3%（o1-preview vs GPT-4o）。
      显式推理步骤引入 error accumulation，且模型可能 overfit 到解释格式而非任务结构。
      隐式推理（hidden activations）在分布偏移下优于显式 token-level 推理。
    relevance_to_evidence_tradeoff: >
      直接支持我们的核心发现：要求模型同时生成 evidence sentences 是一种"显式推理"，
      会对主任务（RE）产生性能代价（~8pp F1 下降）。
      Related Work 引用点：evidence generation 作为 structured explanation，
      与 CoT 共享"显式推理降低主任务性能"的普遍模式。

  - title: "Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion"
    authors: Xie et al. (Google Research)
    year: 2022
    venue: ACL Findings 2022
    url: https://arxiv.org/abs/2106.08657
    category: evidence_generation_tradeoff
    role: closest_docre_precedent
    key_finding: >
      Joint 训练 RE + evidence extraction，关键创新在 inference-stage fusion：
      分别在 extracted evidence 和 full document 上做 RE 预测再通过 blending layer 融合。
      DocRED 上提升 1.37 Ign F1。Silver evidence labels（启发式规则构建）即可提升 RE 性能。
    relevance_to_evidence_tradeoff: >
      最直接的 DocRE + evidence 先例。EIDER 的核心洞察是 evidence 需要 inference-stage 融合
      而非 joint generation——暗示 joint generation 会引入 noise。
      我们的 CED reranker 是 LLM-era 版本的 inference-stage fusion：
      先生成多个候选（含 evidence），再用 NLI 在推理阶段选最佳。
      Related Work 引用点：encoder-based DocRE 中 evidence 的使用方式，与我们 generative 范式的关键差异。

  - title: "Exploring the Trade-off Between Model Performance and Explanation Plausibility of Text Classifiers Using Human Rationales"
    authors: Resck, Raimundo, Poco
    year: 2024
    venue: NAACL Findings 2024
    url: https://arxiv.org/abs/2404.03098
    category: evidence_generation_tradeoff
    role: formal_framework
    key_finding: >
      用 multi-objective optimization 探索 performance vs explanation plausibility 的 Pareto frontier。
      引入 rationale 约束创建 contrastive loss，证实加入 rationale supervision 会降低主任务性能，
      但存在 Pareto optimal 解平衡两者。
    relevance_to_evidence_tradeoff: >
      提供了 performance-explainability trade-off 的形式化框架。
      我们的 evidence-grounded RE 降 8pp 正是 Pareto frontier 上的一个点。
      CED reranker 的效果可解读为：将系统从 evidence-constrained 点推向 Pareto frontier，
      在几乎不牺牲 evidence quality（evi_f1=0.8188）的前提下恢复 RE 性能。
      Related Work 引用点：evidence generation 的 performance cost 有理论依据。

  - title: "The Decreasing Value of Chain of Thought in Prompting"
    authors: Meincke, Mollick, Mollick, Shapiro
    year: 2025
    venue: Wharton Generative AI Labs Technical Report (SSRN)
    url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5285532
    category: evidence_generation_tradeoff
    role: empirical_support
    key_finding: >
      现代 reasoning models 上 CoT 收益微弱（4-13%），但 latency 增加 35-600%。
      更强的模型从显式推理中受益越少。CoT 可能在 easy questions 上引入 errors
      （variability 增加导致原本正确的被改错）。
    relevance_to_evidence_tradeoff: >
      支持"更强的 SFT 模型不需要在生成时显式输出 evidence"的论点。
      我们的 evidence-only SFT 的性能下降符合"显式推理的边际收益递减"模式。
      Related Work 引用点：evidence generation 的 accuracy cost 不是 DocRE-specific，而是 LLM 的普遍趋势。

  # === Category 10: Negative Transfer in Multi-task / Auxiliary-task Learning ===

  - title: "ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning"
    authors: Jiang, Chen et al.
    year: 2023
    venue: NeurIPS 2023
    url: https://arxiv.org/abs/2301.12618
    category: negative_transfer
    role: theoretical_framework
    key_finding: >
      辅助任务常导致 negative transfer，根因不仅是 gradient conflict 还有 auxiliary-target
      generalization gap。ForkMerge 周期性 fork 模型为多分支，搜索最优 task weights，
      动态 merge 过滤有害 task-parameter updates。在多个 benchmark 上减少 negative transfer。
    relevance_to_evidence_tradeoff: >
      Evidence generation 作为 auxiliary task 对 RE 的 negative transfer 可用此框架解释：
      evidence 和 RE 的 gradient 方向不完全对齐，joint training 时 evidence 任务"拖累"RE。
      CED reranker 本质上是将 evidence quality 从 training-time joint objective 解耦到
      inference-time verification，避免了 training-time 的 negative transfer。
      Related Work 引用点：auxiliary task 导致主任务性能下降的一般性理论。

  # === Category 11: Faithfulness vs Accuracy / Correctness Trade-off ===

  - title: "Correctness is not Faithfulness in RAG Attributions"
    authors: Wallat, Heuss, de Rijke, Anand
    year: 2024
    venue: SIGIR 2025
    url: https://arxiv.org/abs/2412.18004
    category: faithfulness_accuracy_tradeoff
    role: key_conceptual_framework
    key_finding: >
      Correctness 和 faithfulness 是独立维度，可能冲突。高达 57% 的 citations 是
      post-rationalized（事后编造而非真实依据）。Unfaithful attributions 可能 factually correct，
      但 foster misguided trust。必须同时检查 correctness 和 faithfulness。
    relevance_to_evidence_tradeoff: >
      直接相关。我们的 evidence-grounded RE 试图让模型输出 faithful evidence，
      但这与 relation correctness 产生张力（rel_f1 降 8pp）。
      CED reranker 通过 NLI verification 确保 evidence 是 faithful 的（非 post-rationalized），
      同时不牺牲 RE accuracy。
      Related Work 引用点：correctness-faithfulness 分离的概念框架。

  - title: "Evaluating Correctness and Faithfulness of Instruction-Following Models for Question Answering"
    authors: Adlakha, BehnamGhader, Lu, Meade, Reddy
    year: 2024
    venue: TACL 2024
    url: https://arxiv.org/abs/2307.16877
    category: faithfulness_accuracy_tradeoff
    role: evaluation_framework
    key_finding: >
      Instruction-following LLMs 在 correctness 上表现可比 fine-tuned models，
      但 faithfulness 普遍较差——模型会 hallucinate 而非忠实于提供的 evidence。
      传统 metrics 对 correctness 和 faithfulness 的评估均有缺陷。
    relevance_to_evidence_tradeoff: >
      解释了为什么 joint evidence+RE 生成性能差——模型在同时优化 correctness
      和 faithfulness 时，两个目标存在张力。单纯要求模型"同时输出正确 triples 和
      faithful evidence"是 multi-objective optimization 问题。
      Related Work 引用点：correctness vs faithfulness 评估方法论。

  - title: "Towards Faithful Model Explanation in NLP: A Survey"
    authors: Lyu, Havaldar, Stein et al.
    year: 2024
    venue: Computational Linguistics (MIT Press)
    url: https://aclanthology.org/2024.cl-2.6/
    category: faithfulness_accuracy_tradeoff
    role: comprehensive_survey
    key_finding: >
      系统综述 NLP 中 faithful explanation 的定义、评估和生成方法。
      识别了 faithfulness-performance trade-off 作为核心挑战：
      更 faithful 的解释不一定更有用，更有用的解释不一定 faithful。
      提出未来方向包括 multi-objective optimization 和 post-hoc verification。
    relevance_to_evidence_tradeoff: >
      权威综述为我们的 evidence generation trade-off 提供广泛文献背景。
      我们的 CED reranker 正是该综述建议的"post-hoc verification"方向的具体实例。
      Related Work 引用点：faithfulness 研究的全景综述，定位我们的工作。

  # === Category 12: Reranking / Verification as Bridge ===

  - title: "Genie: Achieving Human Parity in Content-Grounded Datasets Generation"
    authors: Yehudai, Carmeli, Mass et al.
    year: 2024
    venue: ICLR 2024
    url: https://arxiv.org/abs/2401.14367
    category: reranking_verification_bridge
    role: methodological_precedent
    key_finding: >
      三阶段流程：Content Preparation → Generation → NLI-based Filtering。
      用 fine-tuned T5-11B NLI 模型判断生成内容是否 entailed by source（faithfulness 检验），
      过滤不 faithful 的生成。在 LFQA、摘要、IE 上达到 human parity。
    relevance_to_evidence_tradeoff: >
      方法论上最接近我们的 CED reranker——都是用 NLI verification 作为 post-hoc filter/reranker，
      在不牺牲主任务质量的前提下确保 grounding quality。
      GENIE 验证了 NLI-based filtering 在内容生成中的有效性。
      关键差异：GENIE 是 data generation pipeline 的过滤，我们是 inference-time reranking。
      Related Work 引用点：NLI-based verification 作为 bridge 的成功先例。

  # === Category 13: Evidence-Grounded RL (NEW - 2026-05-15 scan) ===

  - title: "EvidenceRL: Reinforcing Evidence Consistency for Trustworthy Language Models"
    authors: Ben Tamo, Lu, Marteau, Nnamdi, Wang
    year: 2026
    venue: arXiv 2603.19532
    url: https://arxiv.org/abs/2603.19532
    category: evidence_grounded_rl
    role: closest_competitor
    key_finding: >
      用 GRPO 同时优化 grounding（evidence entailment）和 correctness（答案准确性）。
      在 cardiac diagnosis（Llama-3.2-3B）上 F1@3 从 37.0→54.5，grounding 从 47.6→78.2，
      hallucination 降 5 倍。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "3a4d802f-cc48-4c2d-9fa4-876f970a2254"
}
```

</details>

---

### System

_source line 38_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad94f71e34c9ad9c0",
  "tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "description": "Running Print chars 30000-45000 of the YAML content",
  "usage": {
    "total_tokens": 30572,
    "tool_uses": 8,
    "duration_ms": 33928
  },
  "last_tool_name": "Bash",
  "uuid": "dc3afa5f-cb23-4f9e-baba-b2a4985ee90a",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794"
}
```

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Bash · `toolu_01XJ4pG3RErM8k75PApx9ykm`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7341df47-ab61-4a7f-ab4b-fc80cccd2794/tool-results/mcp-agent-ml-research-read_project_file-1778891987655.txt', 'r') as f:\n    data = json.load(f)\n\nresult = data['result']\ninner = json.loads(result)\ncontent = inner['data']['content']\nprint(content[30000:45000])\n\"",
  "description": "Print chars 30000-45000 of the YAML content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "e3b95cb1-94b0-4395-875f-ec87c61b49ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019NYnvFRKWgeWC3icS1PUqq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6930,
      "cache_read_input_tokens": 23391,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6930,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 43,
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

_source line 40 · 2026-05-16T00:40:36.623Z_

<details><summary>↩ Tool result · `toolu_01XJ4pG3RErM8k75PApx9ykm`</summary>

```text
在 legal reasoning（Llama-3.1-8B）上 faithfulness 从 32.8%→67.6%。
      核心：证据一致性 reward 不牺牲 task accuracy 的前提下大幅提升 faithfulness。
    relevance_to_freige: >
      **最直接的 novelty 威胁。** EvidenceRL 与 FREIGE 共享核心 idea：用 GRPO + evidence faithfulness reward
      训练更可靠的模型。关键差异：(1) EvidenceRL 在 QA 域（cardiac/legal），不涉及 DocRE 的 structured output；
      (2) EvidenceRL 未报告 evidence generation 的 performance cost（evidence tax）——它的 grounding 和
      correctness 同时提升，而我们发现 DocRE 中两者存在 ~8pp 张力；
      (3) EvidenceRL 不涉及 task decoupling 现象（QLoRA-specific）；
      (4) EvidenceRL 无 inference-time reranking（CED reranker）。
      定位策略：EvidenceRL 证明 evidence-grounded RL 在 QA 域有效，
      我们揭示 DocRE structured output 带来的独特挑战（evidence tax、task decoupling）和解法（CED reranker）。

  # === Category 14: Multi-Objective GRPO (NEW - 2026-05-15 scan) ===

  - title: "MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems"
    authors: Ichihara, Jinnai, Morimura, Sakamoto, Mitsuhashi, Uchibe
    year: 2025
    venue: arXiv 2509.22047
    url: https://arxiv.org/abs/2509.22047
    category: multi_objective_grpo
    role: related_method
    key_finding: >
      GRPO 在多目标设置下易发生 reward hacking——只优化一个目标而牺牲其他目标。
      MO-GRPO 用 variance-based normalization 自动平衡多个 reward function 的权重，
      在多臂赌博机、控制、机器翻译、指令遵从四个域上实现稳定学习。
    relevance_to_freige: >
      CED reward 本质是多目标（extraction F1 + evidence quality）。MO-GRPO 的分析
      解释了为什么单一 extraction F1 reward 下模型可能 hack 到 "忽略 evidence 只抽 triple" 的策略。
      CED 从 reward 设计端解决，MO-GRPO 从算法端解决，互补视角。

  - title: "Multi-Objective and Mixed-Reward Reinforcement Learning via Reward-Decorrelated Policy Optimization"
    authors: Bai, Liu, Zhuang, Zhou, Weng, Chen, Wang, Cai
    year: 2026
    venue: arXiv 2605.13641
    url: https://arxiv.org/abs/2605.13641
    category: multi_objective_grpo
    role: related_method
    key_finding: >
      GRPO 聚合 mixed-reward 时直接求和再归一化会淹没弱信号 reward 维度。
      RDPO 用 Magnitude-Aware Quantile normalization + Mahalanobis whitening
      去相关 reward 子空间，改善 LLM post-training 的多目标平衡。
    relevance_to_freige: >
      CED reward 的 evidence quality 维度与 extraction F1 天然低相关（r<0.3），
      RDPO 的理论预测这种低相关多维 reward 更易优化。
      为 CED 的 training-stabilizing 效果提供另一个理论解释角度。

  # === Category 15: GRPO Theory (NEW - 2026-05-15 scan) ===

  - title: "GRPO is Secretly a Process Reward Model"
    authors: Sullivan, Koller
    year: 2025
    venue: under review at ICML 2026
    url: https://arxiv.org/abs/2509.21154
    category: grpo_theory
    role: theoretical_insight
    key_finding: >
      证明 GRPO + ORM 在特定条件下等价于 PRM-aware RL objective。
      提出 λ-GRPO 修正 GRPO 在不均匀 process step 上的 deficiency，
      在 downstream reasoning 上超越标准 GRPO 且训练更快收敛。
    relevance_to_freige: >
      DocRE structured output（multi-triple generation）可视为多步 process。
      GRPO 隐式的 PRM 性质可能解释了为什么 extraction-only reward
      在文档级 multi-triple 场景下训练信号不足——单一 outcome reward
      无法为每个 triple 的生成步骤提供有效 process-level credit assignment。
      CED 通过 evidence quality 为每个 triple 提供了更细粒度的信号，
      等效于增强了 process-level reward 的分辨率。

  - title: "Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges"
    authors: Wang et al. (23 authors)
    year: 2026
    venue: arXiv 2604.13602
    url: https://arxiv.org/abs/2604.13602
    category: grpo_theory
    role: theoretical_framework
    key_finding: >
      提出 Proxy Compression Hypothesis (PCH)：reward hacking 源于 objective compression、
      optimization amplification、evaluator-policy co-adaptation 三者交互。
      识别了 perception-reasoning decoupling 作为多模态中 reward hacking 的表现之一。
    relevance_to_freige: >
      PCH 框架可解释我们观察到的 extraction-evidence decoupling：
      QLoRA 的 compressed representation space 下，模型可能将 extraction 和 evidence
      两个子目标压缩到部分重叠的 proxy 空间，导致 optimization amplification
      使模型专注于更容易优化的 extraction 而忽略 evidence。
      bf16 下不复现可能因为 full-rank update 的 representation space 更充裕。

  # === Category 16: Training Precision & RL Stability (NEW - 2026-05-15 scan) ===

  - title: "Defeating the Training-Inference Mismatch via FP16"
    authors: Qi, Liu, Zhou, Pang, Du, Lee, Lin
    year: 2025
    venue: arXiv 2510.26788
    url: https://arxiv.org/abs/2510.26788
    category: training_precision_rl
    role: key_evidence
    key_finding: >
      BF16 在 RL fine-tuning 中引入大的 rounding error 导致 training-inference 不一致，
      BF16 训练常在 150-600 步崩溃。仅切换到 FP16 即可消除不一致，
      提供更稳定训练、更快收敛和更优性能，只需改几行代码。
    relevance_to_freige: >
      直接相关我们的 QLoRA GRPO 不稳定性发现。QLoRA 在 4-bit 量化基础上
      使用 bf16/fp16 adapter，量化+低精度的 compounding error 可能是
      task decoupling 现象的底层原因之一。该论文提供了 precision-instability
      的机制解释，支持我们 "QLoRA-specific decoupling" 的发现——
      低精度 representation 放大了多目标 RL 中子任务间的 gradient 干扰。

  # === Category 17: RL for Scientific IE (NEW - 2026-05-15 scan) ===

  - title: "R²GRPO: Better LLMs for Scientific Information Extraction with MimicSFT and Relevance and Rule-induced GRPO"
    authors: Li, Di, Liu, Jing, Qiu, Chen
    year: 2025
    venue: arXiv 2505.22068
    url: https://arxiv.org/abs/2505.22068
    category: rl_for_ie
    role: related_method
    key_finding: >
      两阶段方法：MimicSFT（structured reasoning template，无需高质量 CoT 数据）
      + R²GRPO（relevance reward + rule-mining reward），
      在科学信息抽取 RE benchmark 上超越 baseline LLM 和 specialized supervised model。
    relevance_to_freige: >
      R²GRPO 的 rule-based reward 设计与我们的 CED reward 有相似动机——
      都是引入 task-specific 结构化 reward 替代单纯 F1 metric reward。
      差异：R²GRPO 的 rule 是 dataset-level 频繁模式（类似 Ru-LLM），
      CED 是 instance-level evidence faithfulness 判别。
      R²GRPO 未涉及 evidence generation 或 DocRE。

  # === Category 18: LLM Alignment for IE (NEW - 2026-05-15 scan) ===

  - title: "ADELIE: Aligning Large Language Models on Information Extraction"
    authors: Qi, Peng, Wang, Xu, Hou, Li
    year: 2024
    venue: EMNLP 2024
    url: https://arxiv.org/abs/2405.05008
    category: llm_ie_alignment
    role: key_baseline
    key_finding: >
      构建 IEInstruct 高质量 IE alignment 语料库，用 SFT + DPO 训练 ADELIE。
      支持 closed/open/on-demand IE 三种模式。
      基于 LLaMA-2-7B/LLaMA-3.2-3B/Qwen2.5-1.5B，在多个 held-out IE dataset 上达 SOTA。
    relevance_to_freige: >
      ADELIE 是 IE alignment 的代表性工作，用 SFT+DPO 替代 RSFT+GRPO。
      我们的工作与 ADELIE 在 training paradigm 上有可比性——
      ADELIE 用 DPO（offline preference optimization），我们用 RSFT（offline rejection sampling）。
      关键差异：ADELIE 覆盖通用 IE，不涉及 evidence generation 或 DocRE-specific challenges；
      我们专注于 DocRE + evidence grounding 的 trade-off。

  # === Category 19: Unfaithful Reasoning / Post-Rationalization (NEW - 2026-05-15 scan) ===

  - title: "Chain-of-Thought Is Not Explainability"
    authors: Barez et al.
    year: 2025
    venue: Oxford WhiteBox Technical Report
    url: https://aigi.ox.ac.uk/wp-content/uploads/2025/07/Cot_Is_Not_Explainability.pdf
    category: unfaithful_reasoning
    role: conceptual_support
    key_finding: >
      CoT 仅仅 rationalize（事后合理化）而非 report（忠实报告）模型的真实决策过程。
      小的操纵即可改变 CoT 的推理链但不改变模型实际决策。
      模型会 silently correct 错误而不在 CoT 中体现。
    relevance_to_freige: >
      支持我们 evidence generation 分析的一个维度：模型生成的 evidence sentences
      可能是 post-rationalization 而非真正驱动 RE 决策的信号。
      CED reranker 用 NLI verification 检查 evidence 的实际 entailment
      而非信任模型自报告的 evidence，本质上是对 post-rationalization 的防御。

  - title: "Characterizing Large Language Models as Rationalizers of Knowledge-Grounded Dialogue"
    authors: Anonymous
    year: 2024
    venue: ACL Findings 2024
    url: https://aclanthology.org/2024.findings-acl.484.pdf
    category: unfaithful_reasoning
    role: empirical_evidence
    key_finding: >
      LLM 在 knowledge-grounded dialogue 中普遍表现为 rationalizer 而非 faithful reasoner，
      模型的 explanation 与其实际使用的 knowledge evidence 不一致。
    relevance_to_freige: >
      与我们的发现呼应：DocRE 中模型可能输出看似合理的 evidence sentences
      但实际 RE 决策并不依赖这些 evidence。这解释了为什么 joint evidence+RE 生成
      对 RE 性能有负面影响——模型在学习生成 "合理化解释" 而非 "可靠推理"。

  # === Category 20: Latent vs Explicit Reasoning Trade-off (NEW - 2026-05-15 scan) ===

  - title: "Reasoning Beyond Language: A Comprehensive Survey on Latent Chain-of-Thought Reasoning"
    authors: Chen, Zhao, Xia, Lu, Wang, Chen, Zhang, Wang, Li, Shen
    year: 2025
    venue: arXiv 2505.16782
    url: https://arxiv.org/abs/2505.16782
    category: latent_vs_explicit_reasoning
    role: survey
    key_finding: >
      Latent CoT 将推理从显式 token generation 解耦到 hidden state computation，
      在多项任务上达到与显式 CoT 相当或更优的性能，同时推理速度提升 20 倍以上。
      显式 CoT 的 sequential token-level 推理是 applicability 的瓶颈。
    relevance_to_freige: >
      为 evidence generation trade-off 提供更广泛的理论视角：
      evidence sentences 作为显式推理步骤（类似 CoT tokens）可能不是最优的推理形式。
      我们的 CED reranker 可被视为将 evidence reasoning 从 generation-time 显式推理
      转移到 inference-time 的 NLI-based 验证——类似 latent-to-explicit 的范式转换，
      但方向相反：不是让推理隐式化，而是让验证外部化。

  # =========================================================================
  # Related Work Survey (2026-05-15): 5 directions for FREIGE paper
  # =========================================================================

  # === Category 21: Evidence-Based / Faithful DocRE (Direction 1) ===

  - title: "DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction"
    authors: Youmi Ma, An Wang, Naoaki Okazaki
    year: 2023
    venue: EACL 2023
    url: https://arxiv.org/abs/2302.08675
    category: evidence_based_docre
    role: direct-competitor
    key_finding: >
      用 evidence 信息作为监督信号引导 DocRE 系统的 attention module 关注 evidence sentences。
      提出 evidence retrieval (ER) self-training 策略，在无 evidence 标注的大规模数据上自动生成
      silver evidence 训练 ER。DocRED 上 RE 和 ER 均达 SOTA。
      解决了 evidence retrieval 的两大问题：高内存消耗和标注有限。
    relevance_to_freige: >
      最重要的 evidence-based DocRE 先驱工作。DREEAM 用 evidence 引导 attention（encoder-based），
      我们用 evidence 引导 RL reward（generative LLM）。关键代际差异：
      (1) DREEAM 是 encoder-based（BERT/RoBERTa），我们是 LLM generative；
      (2) DREEAM 的 evidence 用于注意力监督，我们的 evidence 用于 reward 设计和 CED reranking；
      (3) DREEAM 未量化 evidence 对 RE 的 performance cost。
      Related Work 必引：evidence-based DocRE 的代表性工作。

  - title: "DocGNRE: Semi-automatic Data Enhancement for Document-Level Relation Extraction with Distant Supervision from Large Language Models"
    authors: Junpeng Li, Zixia Jia, Zilong Zheng
    year: 2023
    venue: EMNLP 2023
    url: https://arxiv.org/abs/2311.07314
    category: evidence_based_docre
    role: method-component
    key_finding: >
      用 LLM（ChatGPT）+ NLI 模块半自动生成 relation triples，增强 DocRE 数据集。
      特别擅长 re-annotating long-tail relation types。提供四个增强训练数据集。
      解决了 vanilla in-context learning 无法处理 DocRE 大量细粒度 relation types 的问题。
    relevance_to_freige: >
      DocGNRE 的 NLI 验证模块与我们 CED reranker 的 NLI scoring 思路类似——
      都用 NLI 检查生成内容是否被文档支持。差异：DocGNRE 用 NLI 过滤数据增强，
      我们用 NLI 做 inference-time reranking。DocGNRE 关注数据质量，我们关注训练范式。

  - title: "CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction"
    authors: Khai Phan Tran, Xue Li
    year: 2025
    venue: arXiv 2504.06529
    url: https://arxiv.org/abs/2504.06529
    category: evidence_based_docre
    role: direct-competitor
    key_finding: >
      用 attentional graph-based 架构捕捉同文档内语义相似实体对间的协作模式。
      文档转化为 bipartite graph（entity pair nodes + sentence nodes），
      三子图：Entity Pair 子图建模协作、Entity Pair-Sentence 子图捕捉语义关系、
      Sentence 子图辅助共指推理。在 DocRED 上 evidence retrieval 和 RE 均有提升。
    relevance_to_freige: >
      CDER 是最新的 encoder-based evidence retrieval 方法，验证了 evidence 对 DocRE 的价值。
      与我们的关键差异：(1) CDER 是 encoder-based pipeline，我们是 LLM generative；
      (2) CDER 用 evidence 作为输入特征，我们用 evidence quality 作为 reward/reranking 信号；
      (3) CDER 未探索 evidence generation 的 performance cost。

  - title: "Evidence-aware Document-level Relation Extraction"
    authors: Xu T, Hua W, Qu J, Li Z, Xu J, Liu A et al.
    year: 2022
    venue: CIKM 2022
    url: https://dl.acm.org/doi/10.1145/3511808.3557313
    category: evidence_based_docre
    role: background
    key_finding: >
      将 evidence sentence selection 建模为序列决策问题，
      用 RL 机制选择支撑关系的 evidence sentences。
      在 DocRED 上验证 evidence-aware 方法的有效性。
    relevance_to_freige: >
      早期将 RL 用于 DocRE evidence 的工作。其 RL 用于 evidence selection 策略，
      我们的 RL 用于整体模型微调（GRPO/RSFT）。证实 RL+evidence+DocRE 的组合有研究价值。

  # === Category 22: Faithfulness Cost in NLP (Direction 2) ===

  - title: "Does Faithfulness Conflict with Plausibility? An Empirical Study in Explainable AI across NLP Tasks"
    authors: Xiaolei Lu, Jianghong Ma
    year: 2024
    venue: arXiv 2404.00140
    url: https://arxiv.org/abs/2404.00140
    category: faithfulness_cost
    role: evaluation
    key_finding: >
      在 sentiment analysis、intent detection、topic labeling 三个 NLP 任务上
      系统比较 faithfulness 和 plausibility 的关系。传统 perturbation-based 方法
      （Shapley value、LIME）可同时达到较高 faithfulness 和 plausibility。
      关键发现：faithfulness 和 plausibility 并非必然冲突，
      可通过双目标优化同时提升。
    relevance_to_freige: >
      提供了 faithfulness-plausibility 关系的实证基础。我们的 evidence generation
      可视为 plausibility（evidence 看起来合理）vs faithfulness（evidence 真正驱动 RE）的张力。
      CED reranker 的 NLI verification 本质上是在检查 faithfulness 而非仅 plausibility。

  - title: "Faithfulness vs. Plausibility: On the (Un)Reliability of Explanations from Large Language Models"
    authors: Anonymous
    year: 2024
    venue: arXiv 2402.04614
    url: https://arxiv.org/abs/2402.04614
    category: faithfulness_cost
    role: key_evidence
    key_finding: >
      LLM 擅长生成 plausible 的解释，但这些解释不一定 faithful——
      不与 LLM 的实际推理过程对齐。Self-explanations 的 reliability 存疑。
      LLM 的解释行为更像 post-hoc rationalization 而非真实推理报告。
    relevance_to_freige: >
      直接支持我们的核心论点：要求 LLM 在 DocRE 中同时生成 evidence 可能
      只是让模型学会 post-hoc rationalize，而非真正基于 evidence 做 RE。
      CED reranker 的外部 NLI verification 正是为了对抗这种 unreliable self-explanation。

  - title: "Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps"
    authors: Anonymous
    year: 2025
    venue: EMNLP 2025
    url: https://aclanthology.org/2025.emnlp-main.504.pdf
    category: faithfulness_cost
    role: evaluation
    key_finding: >
      通过 unlearning 推理步骤来衡量 CoT 的 faithfulness。
      如果 unlearn 某个推理步骤后模型行为不变，说明该步骤不 faithful。
      揭示了 CoT 推理步骤的 faithfulness 在不同任务和模型间差异巨大。
    relevance_to_freige: >
      提供了量化 faithfulness 的方法论。可用类似思路评估我们模型生成的 evidence
      是否真正影响 RE 决策。CED reranker 的 evidence corruption test
      本质上是这种 faithfulness 检验的 inference-time 版本。

  # === Category 23: LoRA/QLoRA Training Artifacts (Direction 3) ===

  - title: "LoRA vs Full Fine-tuning: An Illusion of Equivalence"
    authors: Reece Shuttleworth, Jacob Andreas, Antonio Torralba, Pratyusha Sharma
    year: 2024
    venue: arXiv 2410.21228
    url: https://arxiv.org/abs/2410.21228
    category: lora_qlora_artifacts
    role: key_evidence
    key_finding: >
      LoRA 和 full fine-tuning 产生结构上根本不同的权重矩阵。LoRA 引入 intruder dimensions——
      奇异值分解中出现新的高秩奇异向量（与预训练权重高度不相似）。Full f
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "8a8f887f-e2f2-4581-b082-30f0e868b658"
}
```

</details>

---

### System

_source line 41_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad94f71e34c9ad9c0",
  "tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "description": "Running Print chars 45000-60000 of the YAML content",
  "usage": {
    "total_tokens": 37533,
    "tool_uses": 9,
    "duration_ms": 40814
  },
  "last_tool_name": "Bash",
  "uuid": "e3184c5b-a67e-4551-a0fe-44eb3d19331f",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794"
}
```

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Bash · `toolu_01Kfn8sThXJ9FsKTrBfZrWb4`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7341df47-ab61-4a7f-ab4b-fc80cccd2794/tool-results/mcp-agent-ml-research-read_project_file-1778891987655.txt', 'r') as f:\n    data = json.load(f)\n\nresult = data['result']\ninner = json.loads(result)\ncontent = inner['data']['content']\nprint(content[45000:60000])\n\"",
  "description": "Print chars 45000-60000 of the YAML content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "d57759c8-6aa8-4814-a940-bc9307f665c7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MYob5YPVFuWrTwZ7bi6ADA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6916,
      "cache_read_input_tokens": 30321,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6916,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
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

_source line 43 · 2026-05-16T00:40:43.504Z_

<details><summary>↩ Tool result · `toolu_01Kfn8sThXJ9FsKTrBfZrWb4`</summary>

```text
ine-tuning 不会。
      LoRA 的 forgetting 几乎全部集中在 intruder dimensions。
      缩小 intruder dimensions 的奇异值可显著恢复预训练分布建模能力，
      同时仅微小影响下游任务性能。
    relevance_to_freige: >
      直接解释我们的 QLoRA GRPO decoupling 现象。LoRA/QLoRA 的 intruder dimensions
      可能是 extraction-evidence decoupling 的结构性原因：
      4-bit 量化 + LoRA 低秩约束导致 extraction 和 evidence 任务被迫共享
      有限的 intruder dimensions，当 RL 优化 amplify 这些维度时，
      两个任务的 gradient 在 intruder space 中产生干扰导致 decoupling。
      bf16 full fine-tuning 无 intruder dimensions 问题，因此不复现。

  - title: "The Impact of LoRA on the Emergence of Clusters in Transformers"
    authors: Hugo Koubbi, Louis Hernandez, Matthieu Boussard
    year: 2024
    venue: arXiv 2402.15415
    url: https://arxiv.org/abs/2402.15415
    category: lora_qlora_artifacts
    role: theoretical_support
    key_finding: >
      用 mean-field self-attention toy model 研究 LoRA fine-tuning 的 forgetting 机制。
      LoRA 作为低秩扰动作用于交互粒子系统（tokens）。
      发现关于扰动范数和 Transformer 深度的 phase transition：
      超过某个阈值后从 non-forgetting 转变为 forgetting behavior。
      理论上界 time-to-deviation 与扰动大小和谱特性相关。
    relevance_to_freige: >
      提供了 LoRA forgetting 的理论框架。我们的 QLoRA GRPO decoupling 可能
      对应 phase transition 的临界区域——4-bit 量化使扰动有效范数增大，
      加上 GRPO 的 online 更新持续增大扰动，更容易触发 forgetting/decoupling phase transition。
      bf16 下扰动范数更可控，因此保持在 non-forgetting phase。

  - title: "QeRL: Beyond Efficiency -- Quantization-enhanced Reinforcement Learning for LLMs"
    authors: NVIDIA, MIT, HKU, THU
    year: 2025
    venue: arXiv 2510.11696
    url: https://arxiv.org/abs/2510.11696
    category: lora_qlora_artifacts
    role: direct-competitor
    key_finding: >
      标准量化引入静态确定性噪声，对 RL 后期训练不利。但精确控制的量化噪声
      可通过增加 policy entropy 促进探索。Adaptive Quantization Noise (AQN) 机制
      动态调整噪声。结合 NVFP4 + LoRA 实现 1.5x rollout 加速。
      首次在单张 H100 上实现 32B LLM 的 RL 训练。
    relevance_to_freige: >
      QeRL 证明量化噪声可以被利用而非消除。与我们的发现互补：
      我们发现 QLoRA 的量化在多目标 RL 中导致 task decoupling（负面影响），
      QeRL 发现适当控制的量化噪声可促进单目标 exploration（正面利用）。
      差异在于：单目标场景下噪声促进探索有益，
      多目标场景下噪声加剧不同子任务间的 gradient 干扰。

  - title: "The Impact of Quantization on Large Reasoning Model Reinforcement Learning"
    authors: Anonymous
    year: 2025
    venue: NeurIPS 2025 Workshop (Efficient Reasoning)
    url: https://arxiv.org/abs/2511.15694
    category: lora_qlora_artifacts
    role: key_evidence
    key_finding: >
      系统评估量化对 LRM RL 训练的影响。发现 quantization-aware RL training
      反而损害学习过程，PTQ 和 QLoRA 表现更好。
      post-RL 量化模型和 quantization-aware RL 模型在推理性能上存在显著差距。
    relevance_to_freige: >
      直接支持我们的观察：QLoRA GRPO 训练不稳定可能源于
      quantization 和 RL 优化的复杂交互。该论文在数学推理任务上的发现
      与我们在 DocRE 上的 task decoupling 观察一致——
      量化在 RL 训练过程中引入系统性干扰。

  # === Category 24: GRPO / Online RL for NLP Beyond RLHF (Direction 4) ===

  - title: "ReasoningNER: A Reasoning Paradigm for Named Entity Recognition"
    authors: Anonymous
    year: 2025
    venue: arXiv 2511.11978
    url: https://arxiv.org/abs/2511.11978
    category: grpo_nlp_applications
    role: direct-competitor
    key_finding: >
      三阶段 NER 框架：CoT Generation → CoT Tuning → GRPO Reasoning Enhancement。
      用 composite reward（entity F1 + format compliance）训练 GRPO policy。
      ReasoningNER-8B 零样本超 GPT-4 12.3 F1、超 DeepSeek-R1-32B 8.4 F1，
      1.7B 版本超 DeepSeek-R1-8B 10.5 F1。
    relevance_to_freige: >
      GRPO 成功应用于 IE（NER）的案例。NER reward 结构相对简单（entity-level F1），
      reward variance 天然较高（不同 span 组合产生多样 F1 分数）。
      再次支持：结构简单的 IE 任务 GRPO 成功，
      文档级多 triple + evidence 的复杂任务需要额外设计（CED/RSFT）。

  - title: "Posterior-GRPO: Rewarding Reasoning Processes in Code Generation"
    authors: Anonymous
    year: 2025
    venue: arXiv 2508.05170
    url: https://arxiv.org/abs/2508.05170
    category: grpo_nlp_applications
    role: method-component
    key_finding: >
      在代码生成中仅对成功输出的推理过程施加 process-based reward（条件 reward），
      有效抑制 reward hacking——模型不能通过错误推理碰巧生成正确代码来获得高 reward。
      通过将 reward 条件化于最终正确性，对齐内部推理与代码正确性。
    relevance_to_freige: >
      P-GRPO 的"仅对成功输出奖励推理过程"与我们 RSFT 的 rejection sampling 理念一致——
      都是只从高质量输出中学习。P-GRPO 的 conditional reward 思路可启发 CED 改进：
      只在 RE 正确时奖励 evidence quality，避免"evidence 好但 RE 错"的情况。

  # === Category 25: Rejection Sampling Fine-Tuning / Offline RL (Direction 5) ===

  - title: "OREO: Offline Reinforcement Learning for LLM Multi-Step Reasoning"
    authors: Anonymous
    year: 2024
    venue: arXiv 2412.16145
    url: https://arxiv.org/abs/2412.16145
    category: rsft_offline_rl
    role: direct-competitor
    key_finding: >
      基于 maximum entropy RL 的 offline 方法，联合学习 policy model 和 value function，
      优化 soft Bellman Equation。无需 paired preference data，
      实现更好的 credit assignment。学到的 value function 可免费引导 test-time tree search。
      在 GSM8K、MATH、ALFWorld 上超越现有 offline 方法。
    relevance_to_freige: >
      OREO 提供了比简单 RSFT 更理论化的 offline RL 框架。
      我们的 RSFT 可视为 OREO 的特例（无 value function，简单 threshold filtering）。
      Future work 方向：用 OREO 替代简单 RSFT 可能进一步提升 DocRE 性能。

  - title: "PCL-Reasoner-V1.5: Advancing Math Reasoning with Offline Reinforcement Learning"
    authors: Yao Lu, Dengdong Fan, Jianzheng Nie, Fan Xu, Jie Chen, Bin Zhou, Yonghong Tian
    year: 2026
    venue: arXiv 2601.14716
    url: https://arxiv.org/abs/2601.14716
    category: rsft_offline_rl
    role: key_evidence
    key_finding: >
      基于 Qwen2.5-32B 的数学推理模型。核心创新是 offline RL 方法，
      在训练稳定性和效率上优于 GRPO 等 online RL。
      AIME 2024 平均 90.9%，AIME 2025 平均 85.6%，
      在 Qwen2.5-32B post-training 中达 SOTA。
    relevance_to_freige: >
      强有力证据支持 offline RL > online RL 的论点。
      PCL-Reasoner 在数学推理上用 offline RL 超越 GRPO，
      与我们在 DocRE 上 RSFT 超越 GRPO 的发现一致。
      两个独立领域的 converging evidence 增强了
      "structured output 任务中 offline 方法优于 online GRPO"的普遍性论述。

  - title: "RS-DPO: A Hybrid Rejection Sampling and Direct Preference Optimization Method for Alignment of Large Language Models"
    authors: Anonymous
    year: 2024
    venue: NAACL 2024 Findings
    url: https://arxiv.org/abs/2402.10038
    category: rsft_offline_rl
    role: method-component
    key_finding: >
      系统性结合 rejection sampling 和 DPO。从 SFT 模型采样 k 个 response per prompt，
      根据 reward 分布识别 contrastive pairs，用 DPO 对齐。
      在有限资源环境下有效微调 LLM，超越独立的 RS、PPO 和 DPO。
    relevance_to_freige: >
      RS-DPO 提供了 rejection sampling 和 preference optimization 的桥梁方法。
      我们的 RSFT 只用正样本训练（SFT loss），RS-DPO 进一步利用负样本构造 preference pair。
      Future work 方向：可考虑用 RS-DPO 方式利用 RSFT rejected 样本做 DPO。

  - title: "RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment"
    authors: Anonymous
    year: 2024
    venue: TMLR 2024
    url: https://arxiv.org/abs/2304.06767
    category: rsft_offline_rl
    role: background
    key_finding: >
      RAFT 是 rejection sampling fine-tuning 的标准化框架：迭代式 generate → rank → filter → SFT。
      每轮生成 n 个 response，用 reward model 排序，取 top-k 做 SFT。
      在文本生成和对话上验证有效性，提供了 RSFT 的 canonical 实现。
    relevance_to_freige: >
      我们的 RSFT pipeline 直接基于 RAFT 框架。差异在于：
      (1) 我们用 verifiable reward（F1 score）替代 learned reward model；
      (2) 我们的 filtering 基于 extraction F1 threshold 而非 top-k ranking；
      (3) 我们额外引入 CED reward 维度用于 inference-time reranking。

  # === Category 7: Evidence-based DocRE (Expanded) ===

  - title: "EAAGRE: Evidence and Axial Attention Guided Document-level Relation Extraction"
    authors: Unknown (Computer Speech and Language)
    year: 2024
    venue: Computer Speech and Language 2024
    url: https://www.sciencedirect.com/science/article/abs/pii/S0885230824001116
    category: evidence_docre
    role: related_method
    key_finding: >
      联合考虑 evidence information 和 relation triple 的全局交互。
      直接引导 PLM encoder 最后一层的 top-k token attention 到 evidence sentences，
      不引入额外可训练参数。Axial attention 建模 relation triple 之间的全局相互依赖。
    relevance_to_freige: >
      与 DREEAM 属于同一 evidence-guided attention 范式。
      EAAGRE 的无参数 evidence attention 与我们 CED reranker 的 post-hoc 方式形成对比——
      前者在 encoder 内部注入 evidence signal，后者在 generation 后验证。
      证明 evidence 信号无论注入位置都能提升 DocRE 性能。

  - title: "GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction"
    authors: Yanxu Mao et al.
    year: 2024
    venue: arXiv 2407.21384
    url: https://arxiv.org/abs/2407.21384
    category: evidence_docre
    role: related_method
    key_finding: >
      用 GCN 构建多权重矩阵引导 attention 到 evidence sentences。
      采用 Teacher-Student 框架：Teacher 在全监督数据上推断 evidence 并分配 token 权重，
      Student 用这些权重作为监督信号训练。
    relevance_to_freige: >
      GEGA 的 Teacher-Student evidence distillation 与我们的 CED reranker 在动机上一致——
      都试图把 evidence quality 信号从外部注入 RE 系统。
      差异在于 GEGA 在 training-time 蒸馏，我们在 inference-time rerank。

  - title: "KnowRA: Knowledge Retrieval Augmented Method for Document-level Relation Extraction with Comprehensive Reasoning Abilities"
    authors: Chengcheng Mai et al.
    year: 2025
    venue: IJCAI 2025
    url: https://arxiv.org/abs/2501.00571
    category: evidence_docre
    role: related_method
    key_finding: >
      通过外部知识库检索增强 DocRE 推理。构建 document graph 并用共指消解增强，
      检索外部知识扩展为 document knowledge graph，并用知识过滤去除无关知识。
      Axial attention 建立跨句逻辑推理。
    relevance_to_freige: >
      KnowRA 代表 DocRE 中"更多外部信号"路线，与我们"让模型自己生成 evidence"路线形成对比。
      我们的工作表明 evidence generation 有固有代价（faithfulness tax），
      KnowRA 绕过这个问题通过检索而非生成。

  # === Category 8: Faithfulness in Structured Output / Evidence Quality ===

  - title: "G&O: A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction"
    authors: Yinghao Li et al.
    year: 2024
    venue: arXiv 2402.13364
    url: https://arxiv.org/abs/2402.13364
    category: faithfulness_structured
    role: related_method
    key_finding: >
      将 structured IE 拆为两步：先用自然语言生成内容，再组织为目标结构。
      G&O 有效分离内容生成和结构化过程，减轻同时完成两个正交任务的压力。
      在 zero-shot NER 和 RE 上显著提升 LLM 性能。
    relevance_to_freige: >
      直接支持我们的核心发现：要求模型同时做 relation extraction 和 evidence generation
      相当于同时做内容生成+结构化，两个任务存在固有冲突。
      G&O 的 decouple 策略与我们观察到的 task decoupling 现象相呼应，
      但 G&O 是 prompting 层面的解耦，我们发现 RL training 中的自发解耦。

  - title: "Improved Evidence Extraction and Metrics for Document Inconsistency Detection with LLMs"
    authors: Nelvin Tan et al.
    year: 2026
    venue: arXiv 2601.02627
    url: https://arxiv.org/abs/2601.02627
    category: faithfulness_structured
    role: related_method
    key_finding: >
      引入新的 evidence extraction 评估指标和 redact-and-retry 框架。
      提出 constrained filtering 方法，显著优于直接 prompting 的 evidence extraction。
      发布新的 semi-synthetic 数据集用于评估 evidence extraction。
    relevance_to_freige: >
      为 evidence extraction 质量评估提供新指标框架。
      我们的 EDCR 指标从 DocRE 角度评估 evidence quality，
      该工作从 document inconsistency 角度评估——两者互补。
      其 redact-and-retry 框架可启发 CED reranker 的迭代改进策略。

  - title: "Diagnosing Structural Failures in LLM-Based Evidence Extraction for Meta-Analysis"
    authors: Unknown
    year: 2026
    venue: arXiv 2602.10881
    url: https://arxiv.org/abs/2602.10881
    category: faithfulness_structured
    role: supporting_evidence
    key_finding: >
      LLM 在结构化 evidence extraction 中存在系统性 structural breakdown：
      role reversal、cross-analysis binding drift、instance compression、numeric misattribution。
      当任务需要稳定绑定 variables/roles/methods/effect-sizes 时性能急剧下降。
    relevance_to_freige: >
      强化我们的核心论点：LLM 生成结构化 evidence 存在系统性困难。
      我们发现的 faithfulness tax 可视为这类 structural failure 在 DocRE 场景的具体表现——
      模型在维持 relation extraction 准确性的同时难以忠实绑定 evidence sentences。

  - title: "Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion (APIE)"
    authors: Unknown
    year: 2025
    venue: AAAI 2026
    url: https://arxiv.org/abs/2508.10036
    category: faithfulness_structured
    role: related_method
    key_finding: >
      提出 dual-component uncertainty metric 量化 LLM 在 IE 中的 Format Uncertainty
      （结构语法困难）和 Content Uncertainty（语义不一致）。
      利用 introspective confusion 主动选择 few-shot examples 提升 IE 性能。
    relevance_to_freige: >
      APIE 的 format vs content uncertainty 分解与我们观察到的 RE vs evidence 冲突类似——
      format uncertainty 对应 structured output 的结构要求，
      content uncertainty 对应 evidence faithfulness。
      为理解 faithfulness tax 的来源提供额外理论视角。

  # === Category 9: RLHF/GRPO for Structured Tasks (Expanded) ===

  - title: "GRPO-LEAD: A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models"
    authors: Jixiao Zhang, Chunsheng Zuo
    year: 2025
    venue: EMNLP 2025
    url: https://arxiv.org/abs/2504.09696
    category: grpo_structured
    role: related_method
    key_finding: >
      增强 GRPO：(1) length-regularized rewards 鼓励简洁性；
      (2) 对错误解的显式惩罚提升精度；
      (3) difficulty-aware advantage reweighting 增强泛化。
      解决 GRPO 的 reward sparsity、verbosity 和难度忽视问题。
    relevance_to_freige: >
      GRPO-LEAD 的 length penalty 与我们观察到的 evidence generation 增加输出长度导致性能下降相关。
      其 difficulty-aware reweighting 可启发 CED reward 对不同难度 relation triple 的差异化处理。
      但 GRPO-LEAD 针对数学推理的单一任务，我们面对 multi-objective（RE + evidence）。

  - title: "E-GRPO: Entity-Aware Reward for Group Relative Policy Optimization"
    authors: Unknown
    year: 2025
    venue: ICLR 2026
    url: https://arxiv.org/pdf/2510.24694
    category: grpo_structured
    role: closest_prior_work
    key_finding: >
      提出 entity-aware reward function，对 negative samples 基于 entity match rate 给 partial credit。
      利用 ground-truth entities 作为 factual correctness 的 proxy，
      区分 "near-miss"（中间推理正确但最终答案错误）和完全失败。
    relevance_to_freige: >
      E-GRPO 的 entity-aware partial credit 与我们 CED reward 的设计理念高度一致——
      都是引入 task-specific fine-grained reward signal 替代 binary reward。
      差异在于 E-GRPO 用 entity match 作为 reward，我们用 evidence quality (NLI-based)。
      E-GRPO 是 training-time reward，CED 是 inference-time reranking。

  - title: "RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs"
    authors: Hangzhan Jin et al.
    year: 2025
    venue: arXiv 2508.16546
    url: https://arxiv.org/abs/2508.16546
    category: grpo_structured
    role: supporting_evidence
    key_finding: >
      RL-FT 可恢复 SFT 导致的大部分 OOD 性能损失，但当 SFT 造成严重 overfitting 时 RL 无法完全恢复。
      OOD 性能退化和恢复主要与 singular vector 方向旋转相关，而非 singular value 变化。
      恢复 top 20% singular values 对应方向可恢复 70-80% OOD 性能。
    relevance_to_freige: >
      解释我们的 RSFT→GRPO pipeline 设计合理性。
      RSFT（SFT 变体）可能引入 distribution shift，后续 GRPO 可部分修复。
      但如果 RSFT 过度拟合单一任务（如只优化 F1），GRPO 的修复能力有限——
      这与我们观察到的 QLoRA GRPO 中 task decoupling 一致。

  - title: "Aligning Instruction-Tuned LLMs for Event Extraction with Multi-objective Reinforcement Learning"
    authors: Unknown
    year: 2025
    venue: Springer 2025
    url: https://link.springer.com/chapter/10.1007/978-3-032-21300-6_50
    category: grpo_structured
    role: related_method
    key_finding: >
      将多目标强化学习应用于事件抽取，在 instruction-tuned LLM 基础上用 RL 优化抽取性能。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "0877e149-466e-4ce2-9d4a-77b439db09e5"
}
```

</details>

---

### System

_source line 44_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad94f71e34c9ad9c0",
  "tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "description": "Running Print chars 60000-75000 of the YAML content",
  "usage": {
    "total_tokens": 44598,
    "tool_uses": 10,
    "duration_ms": 47801
  },
  "last_tool_name": "Bash",
  "uuid": "5bfa5ce2-5322-4e9e-a875-b3d7cea93e29",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794"
}
```

---

### Tool call

_source line 45_

<details open><summary>🔧 Tool call — Bash · `toolu_013qchRzmxDD7T6YbbKRm93u`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7341df47-ab61-4a7f-ab4b-fc80cccd2794/tool-results/mcp-agent-ml-research-read_project_file-1778891987655.txt', 'r') as f:\n    data = json.load(f)\n\nresult = data['result']\ninner = json.loads(result)\ncontent = inner['data']['content']\nprint(content[60000:75000])\n\"",
  "description": "Print chars 60000-75000 of the YAML content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "71c8e8a9-16d0-4a0e-bc36-7aa91c20eb71",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V8DmTqtV4B3o1NTxvk5K1s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7020,
      "cache_read_input_tokens": 37237,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7020,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
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

_source line 46 · 2026-05-16T00:40:50.548Z_

<details><summary>↩ Tool result · `toolu_013qchRzmxDD7T6YbbKRm93u`</summary>

```text
    证明 RL 在 IE 任务中可以有效提升 LLM 的结构化输出质量。
    relevance_to_freige: >
      与我们的 GRPO for DocRE 属于同一 paradigm——用 RL 优化 IE 任务的 LLM。
      事件抽取的多目标（trigger identification + argument extraction）
      与 DocRE 的多目标（relation extraction + evidence generation）有结构相似性。

  # === Category 10: QLoRA vs Full Fine-tuning (Expanded) ===

  - title: "How Much is Too Much? Exploring LoRA Rank Trade-offs for Retaining Knowledge and Domain Robustness"
    authors: Darshita Rathore et al.
    year: 2025
    venue: IJCNLP-AACL 2025
    url: https://arxiv.org/abs/2512.15634
    category: qlora_fft_gap
    role: supporting_evidence
    key_finding: >
      中等 rank (r=32-64) 在表征能力和稳定性之间达到最佳平衡。
      LoRA 在某些推理任务上可与 full fine-tuning 媲美甚至超越。
      跨域评估时 LoRA-tuned 模型展现出 robust generalization，
      表明 LoRA 学习的是可迁移的抽象技能而非记忆领域特定事实。
    relevance_to_freige: >
      为我们的 QLoRA rank 选择提供实证指导。
      我们使用的 QLoRA (r=16) 可能处于 rank 不足区间，
      解释为何 QLoRA GRPO 出现 task decoupling——rank 太低无法同时编码两个任务的更新。
      建议未来实验尝试 r=32-64 观察是否缓解 decoupling。

  - title: "RandLoRA: Full-rank Parameter-Efficient Fine-tuning of Large Models"
    authors: Paul Albert et al.
    year: 2025
    venue: ICLR 2025
    url: https://arxiv.org/abs/2502.00987
    category: qlora_fft_gap
    role: related_method
    key_finding: >
      通过学习 fixed random matrices 的 diagonal scaling 实现 full-rank 更新，
      保持参数效率同时突破 low-rank 限制。
      在 vision-language 任务上显著缩小甚至消除 standard fine-tuning 与 LoRA 的性能差距。
    relevance_to_freige: >
      直接回应我们的 QLoRA 限制问题。
      如果 QLoRA 的 low-rank 约束导致 multi-objective GRPO 中 task decoupling，
      RandLoRA 的 full-rank PEFT 可能是解决方案——
      在保持内存效率的同时提供足够的表征能力同时编码 RE 和 evidence generation。

  # === Category 11: Multi-task Learning Trade-offs in IE (Expanded) ===

  - title: "C-LoRAE: Collaborative Multi-LoRA Experts with Achievement-based Multi-Tasks Loss for Unified Multimodal Information Extraction"
    authors: Unknown
    year: 2025
    venue: arXiv 2505.06303
    url: https://arxiv.org/abs/2505.06303
    category: mtl_ie_tradeoff
    role: closest_prior_work
    key_finding: >
      扩展 LoRA 引入 universal expert（跨任务共享知识）和 task-specific experts。
      用 mutual information maximization 促进 expert 间信息交换。
      Achievement-based multi-task loss 根据当前各任务性能动态平衡训练进度。
    relevance_to_freige: >
      C-LoRAE 的 universal + task-specific expert 架构直接对应我们的 RE + evidence 多任务设定。
      其 achievement-based loss 可启发 CED reward 中 RE 和 evidence 维度的动态权重调整。
      C-LoRAE 从架构层面解决 gradient conflict，我们从 reward design 层面解决。

  - title: "Ortho-LoRA: Disentangling Task Conflicts in Multi-Task LoRA via Orthogonal Gradient Projection"
    authors: Ziyu Yang et al.
    year: 2026
    venue: arXiv 2601.09684
    url: https://arxiv.org/abs/2601.09684
    category: mtl_ie_tradeoff
    role: related_method
    key_finding: >
      针对 LoRA 的 bipartite 结构设计 gradient projection 方法。
      动态将冲突任务梯度投影到彼此的正交补空间，在 LoRA 固有子空间内解决冲突。
      解决 multi-task LoRA 中的 negative transfer 问题。
    relevance_to_freige: >
      直接解释我们的 QLoRA GRPO task decoupling：
      RE 和 evidence generation 的 gradient 在 low-rank 空间中冲突，
      QLoRA 的有限容量加剧这种冲突导致 task 自发解耦。
      Ortho-LoRA 的正交投影方法可作为 QLoRA GRPO 的改进方向。

  - title: "Proactive Gradient Conflict Mitigation in Multi-Task Learning: A Sparse Training Perspective"
    authors: Zhi Zhang et al.
    year: 2024
    venue: arXiv 2411.18615
    url: https://arxiv.org/abs/2411.18615
    category: mtl_ie_tradeoff
    role: supporting_evidence
    key_finding: >
      从 Sparse Training 角度缓解 gradient conflict：
      选择原始模型参数子集同时学习多任务，冻结其余参数。
      将高维空间优化问题转为低维问题，限制每个任务的 gradient update 影响范围。
      可与 gradient manipulation 技术结合进一步提升效果。
    relevance_to_freige: >
      QLoRA 本质上就是一种 sparse training（只更新 low-rank adapter），
      但 sparse training 的 proactive conflict mitigation 需要 task-aware 的参数选择，
      而 QLoRA 的参数选择是 task-agnostic 的。
      这解释了为什么 QLoRA 在 multi-objective GRPO 中表现不如预期——
      它的 sparsity 模式不是为多任务优化设计的。

  # === Category 12: Generative IE Surveys ===

  - title: "Large Language Models for Generative Information Extraction: A Survey"
    authors: Unknown
    year: 2024
    venue: Frontiers of Computer Science 2024
    url: https://arxiv.org/abs/2312.17617
    category: survey
    role: survey
    key_finding: >
      全面综述 LLM 在 IE 各子任务（NER、RE、EE 等）中的应用。
      按 IE 子任务和技术分类，实证分析最先进方法和新兴趋势。
      指出 LLM-based IE 面临 structured output 质量和效率挑战。
    relevance_to_freige: >
      为我们的工作提供 broader context。FREIGE 属于 generative IE 范式——
      用 LLM 生成结构化 RE 输出。该 survey 的分类框架帮助定位 FREIGE 在 generative IE 生态中的位置：
      我们是首个系统研究 generative DocRE 中 evidence generation 代价的工作。

  # === Category 13: Inference-Time Reranking / Best-of-N (New from 2025-05-16 scan) ===

  - title: "Is Best-of-N the Best of Them? Coverage, Scaling, and Optimality in Inference-Time Alignment"
    authors: Audrey Huang et al.
    year: 2025
    venue: ICML 2025
    url: https://arxiv.org/abs/2503.21878
    category: inference_time_reranking
    role: key_baseline
    key_finding: >
      Best-of-N sampling provably suffers from reward hacking when N is large.
      提出 InferenceTimePessimism 算法，通过 pessimism in the face of uncertainty
      实现 scaling-monotonic 性能（性能不随 N 增大而退化）。
      强调 pre-trained policy 对高质量 response 的 coverage 是 BoN 成功的关键。
    relevance_to_freige: >
      直接对应 CED reranker 的理论基础。CED 作为 inference-time reward model 选择最佳候选，
      该论文的 pessimism 原则可指导 CED reranker 的 threshold 设计——
      避免过度信任 CED score 导致 reward hacking。

  - title: "Inference-Time Reward Hacking in Large Language Models"
    authors: Yiwei Chen et al.
    year: 2025
    venue: NeurIPS 2025 Spotlight
    url: https://arxiv.org/abs/2506.19248
    category: inference_time_reranking
    role: related_analysis
    key_finding: >
      证明 BoN 中 true reward 先升后降的 hacking pattern 是所有 inference-time 机制的固有属性。
      提出 Best-of-Poisson (BoP) 高效近似最优 reward-KL tradeoff policy，
      以及 HedgeTune 自动寻找最优 inference-time 参数。
    relevance_to_freige: >
      CED reranker 本质上是 inference-time 对齐。此论文警示：
      即使 CED score 是高质量 reward，过度优化（选 N 过大）仍可能退化。
      HedgeTune 的思路可用于自动选择 CED reranker 的最优 N。

  - title: "Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models"
    authors: Yinlam Chow et al.
    year: 2024
    venue: ICLR 2025
    url: https://arxiv.org/abs/2412.15287
    category: inference_time_reranking
    role: method_component
    key_finding: >
      提出 inference-aware fine-tuning 范式：训练时直接优化 BoN inference 策略的性能。
      设计 imitation learning 和 RL 方法克服 BoN 中不可微的 argmax 操作。
      BoN-aware 模型隐式学习 exploration-exploitation meta-strategy，
      交替生成最优 response 和多样性 response。
    relevance_to_freige: >
      FREIGE 的 RSFT+CED reranker 是 train-then-rerank 两阶段。
      此论文暗示更优方案：将 CED reranker 信号直接融入训练目标，
      使模型生成 BoN-aware 的多样输出而非事后选择。

  - title: "Evaluation of Best-of-N Sampling Strategies for Language Model Alignment"
    authors: Yuki Ichihara et al.
    year: 2025
    venue: TMLR 2025
    url: https://arxiv.org/abs/2502.12668
    category: inference_time_reranking
    role: evaluation
    key_finding: >
      系统评估 BoN 采样的 reward hacking 问题。
      提出 Stochastic Regularized BoN (SRBoN) 有理论保证的方法。
      发现简单的 Sentence Length Regularized BoN 也能获得 comparable 性能。
    relevance_to_freige: >
      CED reranker 的 regularization 策略参考。
      FREIGE 中 CED score 作为 evidence quality proxy，
      可借鉴 SRBoN 的正则化思路防止 CED reranker over-optimize evidence 而牺牲 extraction quality。

  - title: "Regularized Best-of-N Sampling with Minimum Bayes Risk Objective for Language Model Alignment"
    authors: Yuu Jinnai et al.
    year: 2024
    venue: NAACL 2025
    url: https://arxiv.org/abs/2404.01054
    category: inference_time_reranking
    role: related_method
    key_finding: >
      MBR-BoN：用 Minimum Bayes Risk 目标作为 proximity regularizer 缓解 reward hacking。
      MBR 目标量化 response 与 reference policy 的接近程度。
      在 AlpacaFarm 和 hh-rlhf 上优于 vanilla BoN 和 MBR decoding。
    relevance_to_freige: >
      CED reranker 可借鉴 MBR 正则化——在选择最高 CED score 候选时，
      同时考虑候选与 base policy 的接近程度，防止选择过度偏离 extraction pattern 的输出。

  # === Category 14: RSFT Methodology Advances (New from 2025-05-16 scan) ===

  - title: "AdaSTaR: Adaptive Data Sampling for Training Self-Taught Reasoners"
    authors: Hyung Won Chung et al.
    year: 2025
    venue: NeurIPS 2025
    url: https://arxiv.org/abs/2505.16322
    category: rsft_methodology
    role: related_method
    key_finding: >
      RFT/RSFT 的随机数据采样导致训练不均衡——已解决的样本被过度训练，困难样本训练不足。
      AdaSTaR 引入两个自适应采样原则：(1) diversity sampling 促进均衡，
      (2) curriculum sampling 根据模型能力动态调整数据难度。
      在 6 个 benchmark 全部取得最优，训练 FLOPs 平均减少 58.6%。
    relevance_to_freige: >
      直接适用于 FREIGE 的 RSFT 阶段。当前 RSFT 随机采样 CED-filtered 数据，
      AdaSTaR 的 curriculum 策略可优化采样——先训简单 relation pair，再逐步引入困难的多跳关系。
      其 diversity sampling 也可缓解 RSFT 数据中 relation type 分布不均的问题。

  - title: "RIFT: Repurposing Negative Samples via Reward-Informed Fine-Tuning"
    authors: Unknown
    year: 2026
    venue: arXiv 2601.09253
    url: https://arxiv.org/abs/2601.09253
    category: rsft_methodology
    role: direct_competitor
    key_finding: >
      RSFT 的 hard rejection 丢弃大量计算昂贵的负样本。
      RIFT 保留所有轨迹，用标量 reward 重新加权 loss，
      正 reward 样本鼓励正确行为，负 reward 样本提供反向梯度。
      引入 stabilized loss 解决 naive reward integration 的训练坍塌问题。
    relevance_to_freige: >
      FREIGE 的 RSFT 同样面临 hard rejection 的效率问题——大量生成但 CED 不达标的样本被丢弃。
      RIFT 的 soft reweighting 可替代 binary CED 筛选：
      用 CED score 作为连续 reward 加权 SFT loss，充分利用所有生成样本。

  # === Category 15: NLI for Evidence Scoring / Faithfulness (New from 2025-05-16 scan) ===

  - title: "FaithLens: Detecting and Explaining Faithfulness Hallucination"
    authors: Unknown
    year: 2025
    venue: arXiv 2512.20182
    url: https://arxiv.org/abs/2512.20182
    category: faithfulness_nli
    role: method_component
    key_finding: >
      8B 参数模型通过合成训练数据 + rule-based RL 优化，
      在 12 个 faithfulness 检测任务上超越 GPT-4.1 和 o3。
      联合预测 binary label 和生成解释，提升可信度。
    relevance_to_freige: >
      FaithLens 的方法验证了 CED 的核心假设：小模型可以做高质量 faithfulness 判断。
      其 rule-based RL 训练策略可启发 CED reward model 的进一步优化——
      除 NLI entailment score 外，加入 explanation quality reward。

  - title: "PrefixNLI: Detecting Factual Inconsistencies as Soon as They Arise"
    authors: Sapir Harary et al.
    year: 2025
    venue: arXiv 2511.01359
    url: https://arxiv.org/abs/2511.01359
    category: faithfulness_nli
    role: method_component
    key_finding: >
      将 NLI 从完整句子推广到任意文本前缀，训练 MiniTruePrefixes 模型。
      在 prefix-level entailment 上超越 baseline NLI 模型 5-14 F1。
      集成到 controlled decoding 框架后，LLaMA-3.2-3B 匹配 8B 模型的 faithfulness。
    relevance_to_freige: >
      PrefixNLI 可强化 CED 的实时性：不必等生成完成再评估 evidence faithfulness，
      在 autoregressive 生成过程中即时检测 unfaithful evidence。
      可作为 GRPO training 中的 token-level reward signal。

  - title: "Revisiting NLI: Towards Cost-Effective and Human-Aligned Metrics for Evaluating LLMs in Question Answering"
    authors: Unknown
    year: 2025
    venue: arXiv 2511.07659
    url: https://arxiv.org/abs/2511.07659
    category: faithfulness_nli
    role: evaluation
    key_finding: >
      轻量 NLI scoring + 简单 lexical-match flag 在 long-form QA 上匹配 GPT-4o 准确率 (89.9%)，
      参数量少几个数量级。引入 DIVER-QA benchmark（3000 样本，人工标注）。
    relevance_to_freige: >
      直接支持 CED 的设计选择：用轻量 NLI 模型（而非昂贵 LLM）评估 evidence quality。
      DIVER-QA 的评估方法可迁移到 DocRE evidence evaluation，
      验证 CED score 与人类判断的一致性。

  - title: "Benchmarking LLM Faithfulness in RAG with Evolving Leaderboards"
    authors: Manveer Singh Tamber et al.
    year: 2025
    venue: EMNLP Industry 2025
    url: https://arxiv.org/abs/2505.04847
    category: faithfulness_nli
    role: evaluation
    key_finding: >
      FaithJudge 框架：利用多样化人工标注 hallucination 样本池改进 LLM-as-judge 评估。
      建立 evolving leaderboard 跟踪 LLM 在 RAG faithfulness 上的表现。
      覆盖 summarization、QA、data-to-text 三类任务。
    relevance_to_freige: >
      提供 faithfulness evaluation 的 benchmark 框架。
      FREIGE 的 EDCR 指标衡量 evidence-extraction decoupling，
      FaithJudge 的人工标注方法可用于验证 EDCR 指标的有效性。

  # === Category 16: Evidence-Grounded DocRE Recent Work (New from 2025-05-16 scan) ===

  - title: "DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning"
    authors: Xu et al.
    year: 2025
    venue: ICML 2025
    url: https://proceedings.mlr.press/v267/xu25am.html
    category: llm_docre
    role: direct_competitor
    key_finding: >
      构建 Document-level Knowledge Graph 捕获实体间结构信息，
      结合 Sentence-level Semantic RAG 检索相关上下文语义信息。
      设计 hybrid-prompt tuning 方法在 LLM 上集成结构和语义理解。
    relevance_to_freige: >
      ICML 2025 的 LLM-based DocRE 方法。与 FREIGE 的区别：
      DocKS-RAG 用 retrieval 增强输入，FREIGE 用 evidence generation 增强输出。
      DocKS-RAG 不显式生成 evidence，而 FREIGE 将 evidence 作为显式输出。

  - title: "COREX: Document-level Relation Extraction Framework with Consistent Two-Hop Reasoning and Evidence Sentence Prediction"
    authors: Unknown
    year: 2024
    venue: IEEE IJCNN 2024
    url: https://ieeexplore.ieee.org/document/10650330/
    category: evidence_based_docre
    role: direct_competitor
    key_finding: >
      提出高效 two-hop reasoning 表示，由 evidence prediction 和 RE 联合监督。
      修正 Adaptive Focal Loss 解决类别不均衡。
      Weighted Fusion Layer 优化 evidence 利用。
    relevance_to_freige: >
      与 FREIGE 同属 evidence-enhanced DocRE，但方法路线不同：
      COREX 是 discriminative 模型用 evidence 注意力引导，
      FREIGE 是 generative 模型显式生成 evidence text。
      COREX 的 evidence-RE 联合训练与 FREIGE 的多任务 GRPO 思路类似。

  - title: "Grounded Knowledge Graph Extraction via LLMs: An Anchor-Constrained Framework with Provenance Tracking"
    authors: Unknown
    year: 2025
    venue: Computers 2025
    url: https://www.mdpi.com/2073-431X/15/3/178
    category: evidence_based_docre
    role: related_method
    key_finding: >
      AEVS 框架：anchor discovery → grounded extraction → verification → supplement。
      为每个三元组提供 character-level provenance，使 faithfulness 可验证。
      Hallucination rate 0.23-20.23%，每样本 2.83-4.28 次 LLM 调用。
    relevance_to_freige: >
      AEVS 的 provenance tracking 理念与 FREIGE 的 evidence generation 一致——
      都试图让 extraction 结果可溯源。区别：AEVS 用 anchor 约束生成，
      FREIGE 用 CED reward 训练模型自主生成 faithful evidence。
      AEVS 的 verification 步骤类似 CED 的 entailment 检验。

  # === Category 17: QLoRA/Quantization Fine-tuning Artifacts (New from 2025-05-16 scan) ===

  - title: "Accurate and Efficient Fine-Tuning of Quantized Large Language Models Through Optimal Balance in Adaptation"
    authors: Shinhyuk Seo et al.
    year: 2024
    venue: TACL 2025
    url: https://arxiv.org/abs/2407.17029
    category: lora_qlora_artifacts
    role: related_analysis
    key_finding: >
      识别量化 LLM + LoRA 的不平衡问题：adapter 输入输出过于复杂而有效可训练性不足，导致欠拟合。
      Q-BLoRA 简化 adapter 输入输出同时增大 rank 缓解欠拟合。
      QA-BLoRA 进一步支持低精度部署。
    relevance_to_freige: >
      直接解释 FREIGE 中 QLoRA GRPO 导致 evidence-extraction decoupling 的机制：
      量化权重的有限表征精度 + LoRA 的 rank 限制 = 双重欠拟合，
      多任务（RE + evidence）在此瓶颈下竞争导致任务自发解耦。
      Q-BLoRA 的
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "d284f9b6-b211-4eb9-a893-80a528de02a5"
}
```

</details>

---

### System

_source line 47_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad94f71e34c9ad9c0",
  "tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "description": "Running Print chars 75000 to end of the YAML content",
  "usage": {
    "total_tokens": 51770,
    "tool_uses": 11,
    "duration_ms": 54658
  },
  "last_tool_name": "Bash",
  "uuid": "62f897dd-0315-4bfb-b382-ca0d524edc32",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794"
}
```

---

### Tool call

_source line 48_

<details open><summary>🔧 Tool call — Bash · `toolu_015ZP5dCjXp5DYi1V31nYZ5S`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7341df47-ab61-4a7f-ab4b-fc80cccd2794/tool-results/mcp-agent-ml-research-read_project_file-1778891987655.txt', 'r') as f:\n    data = json.load(f)\n\nresult = data['result']\ninner = json.loads(result)\ncontent = inner['data']['content']\nprint(content[75000:])\n\"",
  "description": "Print chars 75000 to end of the YAML content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "65a5c6c8-b172-4b31-9c21-6dd50403736f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019vZdWZZYHVo9VuARHVfdDm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7127,
      "cache_read_input_tokens": 44257,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7127,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
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

_source line 49 · 2026-05-16T00:40:57.404Z_

<details><summary>↩ Tool result · `toolu_015ZP5dCjXp5DYi1V31nYZ5S`</summary>

```text
balanced adaptation 可能缓解此问题。

  - title: "CLoQ: Enhancing Fine-Tuning of Quantized LLMs via Calibrated LoRA Initialization"
    authors: Unknown
    year: 2025
    venue: arXiv 2501.18475
    url: https://arxiv.org/abs/2501.18475
    category: lora_qlora_artifacts
    role: related_method
    key_finding: >
      QLoRA 中量化误差影响 LoRA 训练。CLoQ 用校准数据集最小化原始 LLM 与量化+LoRA 版本的
      逐层差异，闭式构造最优 LoRA 初始化，无需反向传播。
      在 ultra low-bit 宽度下显著优于现有方法。
    relevance_to_freige: >
      CLoQ 的初始化策略可缓解 FREIGE 中 QLoRA GRPO 的起点问题——
      更好的 LoRA 初始化 → 更小的量化-原始模型差距 → 
      GRPO 训练起步时 RE 和 evidence 任务的表征空间更均衡，可能减轻 decoupling。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "0e706f31-cdc1-4910-99e4-36eb8ecce465"
}
```

</details>

---

### System

_source line 50_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad94f71e34c9ad9c0",
  "tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "description": "Running Parse YAML and extract all papers grouped by category",
  "usage": {
    "total_tokens": 52359,
    "tool_uses": 12,
    "duration_ms": 64662
  },
  "last_tool_name": "Bash",
  "uuid": "771cfdcd-0624-4fcb-a59c-379fa446adca",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794"
}
```

---

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — Bash · `toolu_01TfX6oF2SCNJfsV7aXRtAcg`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json, yaml\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7341df47-ab61-4a7f-ab4b-fc80cccd2794/tool-results/mcp-agent-ml-research-read_project_file-1778891987655.txt', 'r') as f:\n    data = json.load(f)\n\nresult = data['result']\ninner = json.loads(result)\ncontent = inner['data']['content']\n\n# Parse YAML\nparsed = yaml.safe_load(content)\npapers = parsed['papers']\n\n# Group by category\nfrom collections import OrderedDict\ncategories = OrderedDict()\nfor p in papers:\n    cat = p.get('category', 'unknown')\n    if cat not in categories:\n        categories[cat] = []\n    categories[cat].append(p)\n\nprint(f\"TOTAL PAPERS: {len(papers)}\")\nprint(f\"TOTAL CATEGORIES: {len(categories)}\")\nprint()\n\nfor cat, cat_papers in categories.items():\n    print(f\"=== {cat} ({len(cat_papers)} papers) ===\")\n    for p in cat_papers:\n        # Build citation key from authors + year\n        authors = p.get('authors', 'Unknown')\n        year = p.get('year', '?')\n        title = p.get('title', 'Untitled')\n        role = p.get('role', '')\n        venue = p.get('venue', '')\n        \n        # Extract key finding first line as summary\n        kf = p.get('key_finding', '').strip()\n        # Take first sentence or first 200 chars\n        first_sentence = kf.split('。')[0].split('. ')[0][:200] if kf else 'N/A'\n        \n        print(f\"  [{role}] {title}\")\n        print(f\"    Authors: {authors} | Year: {year} | Venue: {venue}\")\n        print(f\"    Summary: {first_sentence}\")\n        print()\n\nPYEOF",
  "description": "Parse YAML and extract all papers grouped by category"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "de841e88-878a-460b-b671-5cd7302de77d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xm8HpGQFyvXrm2MuL7BGn3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 587,
      "cache_read_input_tokens": 51384,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 587,
        "ephemeral_1h_input_tokens": 0
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

### Tool result

_source line 52 · 2026-05-16T00:41:07.599Z_

<details><summary>↩ Tool result · `toolu_01TfX6oF2SCNJfsV7aXRtAcg`</summary>

```text
&lt;persisted-output>
Output too large (30.2KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7341df47-ab61-4a7f-ab4b-fc80cccd2794/tool-results/bfrdeyd6f.txt

Preview (first 2KB):
TOTAL PAPERS: 101
TOTAL CATEGORIES: 32

=== reward_diversity (4 papers) ===
  [closest_prior_work] GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization
    Authors: NVIDIA Labs | Year: 2025 | Venue: ICML 2026
    Summary: 直接将 GRPO 应用于多 reward 组合时，不同 rollout 的 reward 组合在归一化后 collapse 为相同 advantage 值， 降低训练信号分辨率导致收敛失败

  [related_method] DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of LLMs
    Authors: Xiwen Chen et al. | Year: 2025 | Venue: arXiv 2505.09655
    Summary: GRPO 的标量 reward 无法区分语义多样但得分相同的输出（diversity-quality inconsistency）

  [theoretical_support] Shrinking the Variance: Shrinkage Baselines for RL with Verifiable Rewards
    Authors: Guanning Zeng et al. | Year: 2025 | Venue: arXiv 2511.03710
    Summary: RLVR 中 per-prompt 均值 baseline 在低 generation 数下估计不准导致高 variance 梯度

  [background] Reward Shaping to Mitigate Reward Hacking in RLHF
    Authors: Anonymous | Year: 2025 | Venue: arXiv 2502.18770
    Summary: RL reward 应有界且先快速增长后缓慢收敛

=== mode_collapse_prevention (6 papers) ===
  [key_baseline] DAPO: An Open-Source LLM Reinforcement Learning System at Scale
    Authors: ByteDance Seed, Tsinghua AIR | Year: 2025 | Venue: NeurIPS 2025
    Summary: Naive GRPO 存在 entropy collapse（policy 熵快速下降→输出同质化）

  [related_analysis] Dr. GRPO: Removing Optimization Bias in GRPO
    Authors: Liu et al. | Year: 2025 | Venue: COLM 2025
    Summary: GRPO 的 std 归一化引入两个 bias：(1) difficulty bias——std(r) 归一化对低 variance 组 （全对/全错）给予过高 advantage 权重，trivial question 主导训练信号； (2) length bias——per-token loss 的 1/|o_i| 项使长的错误回答被 under-penalize

  [alternative_framework] GVPO: Group Variance Policy Optimization for LLM Post-Training
    Authors: Anonymous | Year: 2025 | Venue: NeurIPS 2025
    Summary: 将 KL 约束 reward 最大化的解析解直接嵌入梯度权重， variance 项自然平衡 exploration 与 exploitation，维持适度 entropy

  [related_method] REINFORCE++: Stabilizing Critic-Free Policy Optimization with Global Advantage Normalization
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "9ab09321-5aea-48de-96db-0098e8a6efd6"
}
```

</details>

---

### System

_source line 53_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ad94f71e34c9ad9c0",
  "tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7341df47-ab61-4a7f-ab4b-fc80cccd2794/tool-results/bfrdeyd6f.txt",
  "usage": {
    "total_tokens": 54020,
    "tool_uses": 13,
    "duration_ms": 68292
  },
  "last_tool_name": "Read",
  "uuid": "48b5ea8e-6372-4c5c-90eb-95f1dc9d6e0d",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794"
}
```

---

### Tool call

_source line 54_

<details open><summary>🔧 Tool call — Read · `toolu_01BAuKjPWWsvcHEg7JPv52uy`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7341df47-ab61-4a7f-ab4b-fc80cccd2794/tool-results/bfrdeyd6f.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "0ae08c3c-8aa4-4a5c-8d7d-8f5d365fd186",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GcktWiV7aSrYBq4sogFCph",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1588,
      "cache_read_input_tokens": 51971,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1588,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 73,
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

_source line 55 · 2026-05-16T00:41:11.135Z_

<details><summary>↩ Tool result · `toolu_01BAuKjPWWsvcHEg7JPv52uy`</summary>

```text
1	TOTAL PAPERS: 101
2	TOTAL CATEGORIES: 32
3	
4	=== reward_diversity (4 papers) ===
5	  [closest_prior_work] GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization
6	    Authors: NVIDIA Labs | Year: 2025 | Venue: ICML 2026
7	    Summary: 直接将 GRPO 应用于多 reward 组合时，不同 rollout 的 reward 组合在归一化后 collapse 为相同 advantage 值， 降低训练信号分辨率导致收敛失败
8	
9	  [related_method] DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of LLMs
10	    Authors: Xiwen Chen et al. | Year: 2025 | Venue: arXiv 2505.09655
11	    Summary: GRPO 的标量 reward 无法区分语义多样但得分相同的输出（diversity-quality inconsistency）
12	
13	  [theoretical_support] Shrinking the Variance: Shrinkage Baselines for RL with Verifiable Rewards
14	    Authors: Guanning Zeng et al. | Year: 2025 | Venue: arXiv 2511.03710
15	    Summary: RLVR 中 per-prompt 均值 baseline 在低 generation 数下估计不准导致高 variance 梯度
16	
17	  [background] Reward Shaping to Mitigate Reward Hacking in RLHF
18	    Authors: Anonymous | Year: 2025 | Venue: arXiv 2502.18770
19	    Summary: RL reward 应有界且先快速增长后缓慢收敛
20	
21	=== mode_collapse_prevention (6 papers) ===
22	  [key_baseline] DAPO: An Open-Source LLM Reinforcement Learning System at Scale
23	    Authors: ByteDance Seed, Tsinghua AIR | Year: 2025 | Venue: NeurIPS 2025
24	    Summary: Naive GRPO 存在 entropy collapse（policy 熵快速下降→输出同质化）
25	
26	  [related_analysis] Dr. GRPO: Removing Optimization Bias in GRPO
27	    Authors: Liu et al. | Year: 2025 | Venue: COLM 2025
28	    Summary: GRPO 的 std 归一化引入两个 bias：(1) difficulty bias——std(r) 归一化对低 variance 组 （全对/全错）给予过高 advantage 权重，trivial question 主导训练信号； (2) length bias——per-token loss 的 1/|o_i| 项使长的错误回答被 under-penalize
29	
30	  [alternative_framework] GVPO: Group Variance Policy Optimization for LLM Post-Training
31	    Authors: Anonymous | Year: 2025 | Venue: NeurIPS 2025
32	    Summary: 将 KL 约束 reward 最大化的解析解直接嵌入梯度权重， variance 项自然平衡 exploration 与 exploitation，维持适度 entropy
33	
34	  [related_method] REINFORCE++: Stabilizing Critic-Free Policy Optimization with Global Advantage Normalization
35	    Authors: Jian Hu et al. | Year: 2025 | Venue: arXiv 2501.03262
36	    Summary: Prompt-level (local) advantage normalization 导致不准确估计和过拟合
37	
38	  [parallel_work] DiverseGRPO: Mitigating Mode Collapse in Image Generation via Diversity-Aware GRPO
39	    Authors: Henglin Liu et al. | Year: 2025 | Venue: arXiv 2512.21514
40	    Summary: 图像生成中 GRPO 后期输出同质化
41	
42	  [theoretical_support] Why GRPO Needs Normalization: A Local-Curvature Perspective on Adaptive Gradients
43	    Authors: Anonymous | Year: 2025 | Venue: arXiv 2601.23135
44	    Summary: GRPO 的 reward_std 归一化在温和条件下提供严格优于未归一化 REINFORCE 的收敛速率， 收益由 prompt 间平均 reward std 刻画
45	
46	=== contrastive_reward (3 papers) ===
47	  [closest_contrastive_precedent] Improving Reinforcement Learning from Human Feedback Using Contrastive Rewards
48	    Authors: Shen, Zhang et al. | Year: 2024 | Venue: arXiv 2403.07708
49	    Summary: 两步机制：(1) 离线采样 baseline response；(2) 用 baseline 计算 contrastive reward 作为 PPO 的 penalty 项
50	
51	  [related_method] Improving Discriminative Capability of Reward Models in RLHF Using Contrastive Learning
52	    Authors: Anonymous | Year: 2024 | Venue: EMNLP 2024
53	    Summary: 无监督对比损失训练 reward model 充分捕捉对比数据区分度， 带来更稳定的 PPO 训练 return 和 reward
54	
55	  [background] Contrastive Preference Learning: Learning from Human Feedback without RL
56	    Authors: Anonymous | Year: 2024 | Venue: ICLR 2025
57	    Summary: 将 preference learning 重新表述为对比学习问题，无需显式 RL 即可从人类反馈中学习
58	
59	=== evidence_reward (3 papers) ===
60	  [related_method] Drift: Enhancing LLM Faithfulness in Rationale Generation
61	    Authors: Anonymous | Year: 2025 | Venue: ACL 2025
62	    Summary: 用 faithfulness reward 引导 LLM 生成更可靠的 rationale，提升 CoT 推理事实一致性
63	
64	  [background] Fine-Grained NLI-Based Faithfulness Evaluation for Diverse Summarisation Tasks (INFUSE)
65	    Authors: Anonymous | Year: 2024 | Venue: EACL 2024
66	    Summary: 变长前提+简化假设的细粒度 NLI faithfulness 评估，超越传统 NLI 在多任务摘要上的表现
67	
68	  [background] Enhancing Cross-Evidence Reasoning Graph for Document-Level Relation Extraction
69	    Authors: Anonymous | Year: 2024 | Venue: PMC/Bioinformatics 2024
70	    Summary: 文档级关系抽取中用 cross-evidence reasoning graph 增强跨证据推理
71	
72	=== multi_objective_rl (2 papers) ===
73	  [related_analysis] Confronting Reward Model Overoptimization with Constrained RLHF
74	    Authors: Anonymous | Year: 2025 | Venue: OpenReview
75	    Summary: 多组件 RM 的 overoptimization 研究
76	
77	  [theoretical_support] On-Policy RL with Optimal Reward Baseline
78	    Authors: Anonymous | Year: 2025 | Venue: arXiv 2505.23585
79	    Summary: Optimal baseline 一致性地实现更高训练 reward 和更高 entropy， 有效稳定训练并促进更多样的 policy exploration
80	
81	=== rsft_methodology (5 papers) ===
82	  [key_theoretical_support] A Minimalist Approach to LLM Reasoning: from Rejection Sampling to Reinforce
83	    Authors: Xiao et al. | Year: 2025 | Venue: arXiv 2504.11343
84	    Summary: RAFT（简单 rejection sampling baseline）在数学推理上与 GRPO/PPO 表现相当
85	
86	  [method_component] Beyond Rejection Sampling: Trajectory Fusion for Scaling Mathematical Reasoning (TrajFusion)
87	    Authors: Jie Deng et al. | Year: 2026 | Venue: arXiv 2602.04391
88	    Summary: 传统 RSFT 只用正确轨迹，丢弃错误轨迹
89	
90	  [theoretical_support] Rejection Sampling Based Fine Tuning Secretly Performs PPO
91	    Authors: Anonymous | Year: 2025 | Venue: ICML 2025
92	    Summary: 建立 RSFT 与 PPO 之间的理论联系：rejection sampling fine-tuning 在特定条件下隐式执行 PPO with marginal KL constraints
93	
94	  [related_method] AdaSTaR: Adaptive Data Sampling for Training Self-Taught Reasoners
95	    Authors: Hyung Won Chung et al. | Year: 2025 | Venue: NeurIPS 2025
96	    Summary: RFT/RSFT 的随机数据采样导致训练不均衡——已解决的样本被过度训练，困难样本训练不足
97	
98	  [direct_competitor] RIFT: Repurposing Negative Samples via Reward-Informed Fine-Tuning
99	    Authors: Unknown | Year: 2026 | Venue: arXiv 2601.09253
100	    Summary: RSFT 的 hard rejection 丢弃大量计算昂贵的负样本
101	
102	=== rl_for_ie (6 papers) ===
103	  [direct_competitor] R1-RE: Cross-Domain Relation Extraction with RLVR
104	    Authors: Runpeng Dai, Tong Zheng et al. | Year: 2025 | Venue: arXiv 2507.04642
105	    Summary: 首个将 RLVR（GRPO + verifiable reward）用于关系抽取的框架
106	
107	  [related_method] MORE-R1: Guiding LVLM for Multimodal Object-Entity Relation Extraction via Stepwise Reasoning with RL
108	    Authors: Anonymous | Year: 2026 | Venue: arXiv 2603.09478
109	    Summary: 多模态 RE 中用 GRPO + Progressive Sample-Mixing Strategy 优化 LVLM 推理能力
110	
111	  [related_method] REAR: Reinforced Reasoning Optimization for Event Argument Extraction with Relation-Aware Support
112	    Authors: Jianwen Luo et al. | Year: 2025 | Venue: EMNLP 2025 Findings
113	    Summary: 将强化学习推理优化用于事件论元抽取，结合关系感知支持
114	
115	  [background] Adaptive Reinforcement Learning Planning: Harnessing LLMs for Complex Information Extraction
116	    Authors: Zepeng Ding et al. | Year: 2024 | Venue: arXiv 2406.11455
117	    Summary: 将 LLM 顺序抽取建模为 MDP，用 DDQN 训练 decision module 自适应选择实体抽取顺序，提升复杂 IE 性能
118	
119	  [background] Graph-R1: Towards Agentic GraphRAG Framework via End-to-end Reinforcement Learning
120	    Authors: Haoran Luo et al. | Year: 2025 | Venue: ICML 2026
121	    Summary: 用端到端 RL 优化 GraphRAG agent 的多轮检索-推理循环， 包含 knowledge hypergraph construction（n-ary relation extraction）
122	
123	  [related_method] R²GRPO: Better LLMs for Scientific Information Extraction with MimicSFT and Relevance and Rule-induced GRPO
124	    Authors: Li, Di, Liu, Jing, Qiu, Chen | Year: 2025 | Venue: arXiv 2505.22068
125	    Summary: 两阶段方法：MimicSFT（structured reasoning template，无需高质量 CoT 数据） + R²GRPO（relevance reward + rule-mining reward）， 在科学信息抽取 RE benchmark 上超越 baseline LLM 和 specialized supervised model
126	
127	=== llm_docre (6 papers) ===
128	  [key_baseline] RelPrior: Relation as a Prior - A Novel Paradigm for LLM-based Document-level Relation Extraction
129	    Authors: Anonymous | Year: 2025 | Venue: arXiv 2511.08143
130	    Summary: 用 binary relation 作为先验过滤无关实体对，再用 predefined relation 匹配实体， 避免 LLM 在 DocRE 中被无关实体对分散注意力
131	
132	  [related_method] LMRC: LLM with Relation Classifier for Document-Level Relation Extraction
133	    Authors: Xingzuo Li, Kehai Chen, Yunfei Long, Min Zhang | Year: 2024 | Venue: arXiv 2408.13889
134	    Summary: 两阶段方法：先用 attention-based classifier 过滤 NA 实体对（RCP）， 再用 LLM 在精简候选空间中做多分类（RC）
135	
136	  [related_method] Ru-LLM: Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction
137	    Authors: Anonymous | Year: 2025 | Venue: NLPCC 2025
138	    Summary: 用频繁模式挖掘 + MCTS 搜索逻辑规则，转化为 prompt 约束 LLM 输出， 再用 CoT 验证过滤不满足规则的 triple
139	
140	  [background] GLiDRE: Generalist Lightweight model for Document-level Relation Extraction
141	    Authors: Anonymous | Year: 2025 | Venue: arXiv 2508.00757
142	    Summary: 基于 dual-encoder 的轻量级零/少样本 DocRE 模型， 预训练于 136K 文档的大规模 RE 数据
143	
144	  [background] AutoRE: Document-Level Relation Extraction with Large Language Models
145	    Authors: Anonymous | Year: 2024 | Venue: arXiv 2403.14888
146	    Summary: RHF（Relation-Head-Facts）范式用 Mistral-7B + QLoRA 做端到端 DocRE
147	
148	  [direct_competitor] DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning
149	    Authors: Xu et al. | Year: 2025 | Venue: ICML 2025
150	    Summary: 构建 Document-level Knowledge Graph 捕获实体间结构信息， 结合 Sentence-level Semantic RAG 检索相关上下文语义信息
151	
152	=== evidence_generation_tradeoff (4 papers) ===
153	  [key_evidence] Mind Your Step (by Step): Chain-of-Thought can Reduce Performance on Tasks where Thinking Makes Humans Worse
154	    Authors: Sprague et al. | Year: 2024 | Venue: NeurIPS 2024
155	    Summary: CoT 在某些任务上降低性能高达 36.3%（o1-preview vs GPT-4o）
156	
157	  [closest_docre_precedent] Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion
158	    Authors: Xie et al. (Google Research) | Year: 2022 | Venue: ACL Findings 2022
159	    Summary: Joint 训练 RE + evidence extraction，关键创新在 inference-stage fusion： 分别在 extracted evidence 和 full document 上做 RE 预测再通过 blending layer 融合
160	
161	  [formal_framework] Exploring the Trade-off Between Model Performance and Explanation Plausibility of Text Classifiers Using Human Rationales
162	    Authors: Resck, Raimundo, Poco | Year: 2024 | Venue: NAACL Findings 2024
163	    Summary: 用 multi-objective optimization 探索 performance vs explanation plausibility 的 Pareto frontier
164	
165	  [empirical_support] The Decreasing Value of Chain of Thought in Prompting
166	    Authors: Meincke, Mollick, Mollick, Shapiro | Year: 2025 | Venue: Wharton Generative AI Labs Technical Report (SSRN)
167	    Summary: 现代 reasoning models 上 CoT 收益微弱（4-13%），但 latency 增加 35-600%
168	
169	=== negative_transfer (1 papers) ===
170	  [theoretical_framework] ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning
171	    Authors: Jiang, Chen et al. | Year: 2023 | Venue: NeurIPS 2023
172	    Summary: 辅助任务常导致 negative transfer，根因不仅是 gradient conflict 还有 auxiliary-target generalization gap
173	
174	=== faithfulness_accuracy_tradeoff (3 papers) ===
175	  [key_conceptual_framework] Correctness is not Faithfulness in RAG Attributions
176	    Authors: Wallat, Heuss, de Rijke, Anand | Year: 2024 | Venue: SIGIR 2025
177	    Summary: Correctness 和 faithfulness 是独立维度，可能冲突
178	
179	  [evaluation_framework] Evaluating Correctness and Faithfulness of Instruction-Following Models for Question Answering
180	    Authors: Adlakha, BehnamGhader, Lu, Meade, Reddy | Year: 2024 | Venue: TACL 2024
181	    Summary: Instruction-following LLMs 在 correctness 上表现可比 fine-tuned models， 但 faithfulness 普遍较差——模型会 hallucinate 而非忠实于提供的 evidence
182	
183	  [comprehensive_survey] Towards Faithful Model Explanation in NLP: A Survey
184	    Authors: Lyu, Havaldar, Stein et al. | Year: 2024 | Venue: Computational Linguistics (MIT Press)
185	    Summary: 系统综述 NLP 中 faithful explanation 的定义、评估和生成方法
186	
187	=== reranking_verification_bridge (1 papers) ===
188	  [methodological_precedent] Genie: Achieving Human Parity in Content-Grounded Datasets Generation
189	    Authors: Yehudai, Carmeli, Mass et al. | Year: 2024 | Venue: ICLR 2024
190	    Summary: 三阶段流程：Content Preparation → Generation → NLI-based Filtering
191	
192	=== evidence_grounded_rl (1 papers) ===
193	  [closest_competitor] EvidenceRL: Reinforcing Evidence Consistency for Trustworthy Language Models
194	    Authors: Ben Tamo, Lu, Marteau, Nnamdi, Wang | Year: 2026 | Venue: arXiv 2603.19532
195	    Summary: 用 GRPO 同时优化 grounding（evidence entailment）和 correctness（答案准确性）
196	
197	=== multi_objective_grpo (2 papers) ===
198	  [related_method] MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems
199	    Authors: Ichihara, Jinnai, Morimura, Sakamoto, Mitsuhashi, Uchibe | Year: 2025 | Venue: arXiv 2509.22047
200	    Summary: GRPO 在多目标设置下易发生 reward hacking——只优化一个目标而牺牲其他目标
201	
202	  [related_method] Multi-Objective and Mixed-Reward Reinforcement Learning via Reward-Decorrelated Policy Optimization
203	    Authors: Bai, Liu, Zhuang, Zhou, Weng, Chen, Wang, Cai | Year: 2026 | Venue: arXiv 2605.13641
204	    Summary: GRPO 聚合 mixed-reward 时直接求和再归一化会淹没弱信号 reward 维度
205	
206	=== grpo_theory (2 papers) ===
207	  [theoretical_insight] GRPO is Secretly a Process Reward Model
208	    Authors: Sullivan, Koller | Year: 2025 | Venue: under review at ICML 2026
209	    Summary: 证明 GRPO + ORM 在特定条件下等价于 PRM-aware RL objective
210	
211	  [theoretical_framework] Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges
212	    Authors: Wang et al. (23 authors) | Year: 2026 | Venue: arXiv 2604.13602
213	    Summary: 提出 Proxy Compression Hypothesis (PCH)：reward hacking 源于 objective compression、 optimization amplification、evaluator-policy co-adaptation 三者交互
214	
215	=== training_precision_rl (1 papers) ===
216	  [key_evidence] Defeating the Training-Inference Mismatch via FP16
217	    Authors: Qi, Liu, Zhou, Pang, Du, Lee, Lin | Year: 2025 | Venue: arXiv 2510.26788
218	    Summary: BF16 在 RL fine-tuning 中引入大的 rounding error 导致 training-inference 不一致， BF16 训练常在 150-600 步崩溃
219	
220	=== llm_ie_alignment (1 papers) ===
221	  [key_baseline] ADELIE: Aligning Large Language Models on Information Extraction
222	    Authors: Qi, Peng, Wang, Xu, Hou, Li | Year: 2024 | Venue: EMNLP 2024
223	    Summary: 构建 IEInstruct 高质量 IE alignment 语料库，用 SFT + DPO 训练 ADELIE
224	
225	=== unfaithful_reasoning (2 papers) ===
226	  [conceptual_support] Chain-of-Thought Is Not Explainability
227	    Authors: Barez et al. | Year: 2025 | Venue: Oxford WhiteBox Technical Report
228	    Summary: CoT 仅仅 rationalize（事后合理化）而非 report（忠实报告）模型的真实决策过程
229	
230	  [empirical_evidence] Characterizing Large Language Models as Rationalizers of Knowledge-Grounded Dialogue
231	    Authors: Anonymous | Year: 2024 | Venue: ACL Findings 2024
232	    Summary: LLM 在 knowledge-grounded dialogue 中普遍表现为 rationalizer 而非 faithful reasoner， 模型的 explanation 与其实际使用的 knowledge evidence 不一致
233	
234	=== latent_vs_explicit_reasoning (1 papers) ===
235	  [survey] Reasoning Beyond Language: A Comprehensive Survey on Latent Chain-of-Thought Reasoning
236	    Authors: Chen, Zhao, Xia, Lu, Wang, Chen, Zhang, Wang, Li, Shen | Year: 2025 | Venue: arXiv 2505.16782
237	    Summary: Latent CoT 将推理从显式 token generation 解耦到 hidden state computation， 在多项任务上达到与显式 CoT 相当或更优的性能，同时推理速度提升 20 倍以上
238	
239	=== evidence_based_docre (6 papers) ===
240	  [direct-competitor] DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction
241	    Authors: Youmi Ma, An Wang, Naoaki Okazaki | Year: 2023 | Venue: EACL 2023
242	    Summary: 用 evidence 信息作为监督信号引导 DocRE 系统的 attention module 关注 evidence sentences
243	
244	  [method-component] DocGNRE: Semi-automatic Data Enhancement for Document-Level Relation Extraction with Distant Supervision from Large Language Models
245	    Authors: Junpeng Li, Zixia Jia, Zilong Zheng | Year: 2023 | Venue: EMNLP 2023
246	    Summary: 用 LLM（ChatGPT）+ NLI 模块半自动生成 relation triples，增强 DocRE 数据集
247	
248	  [direct-competitor] CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction
249	    Authors: Khai Phan Tran, Xue Li | Year: 2025 | Venue: arXiv 2504.06529
250	    Summary: 用 attentional graph-based 架构捕捉同文档内语义相似实体对间的协作模式
251	
252	  [background] Evidence-aware Document-level Relation Extraction
253	    Authors: Xu T, Hua W, Qu J, Li Z, Xu J, Liu A et al. | Year: 2022 | Venue: CIKM 2022
254	    Summary: 将 evidence sentence selection 建模为序列决策问题， 用 RL 机制选择支撑关系的 evidence sentences
255	
256	  [direct_competitor] COREX: Document-level Relation Extraction Framework with Consistent Two-Hop Reasoning and Evidence Sentence Prediction
257	    Authors: Unknown | Year: 2024 | Venue: IEEE IJCNN 2024
258	    Summary: 提出高效 two-hop reasoning 表示，由 evidence prediction 和 RE 联合监督
259	
260	  [related_method] Grounded Knowledge Graph Extraction via LLMs: An Anchor-Constrained Framework with Provenance Tracking
261	    Authors: Unknown | Year: 2025 | Venue: Computers 2025
262	    Summary: AEVS 框架：anchor discovery → grounded extraction → verification → supplement
263	
264	=== faithfulness_cost (3 papers) ===
265	  [evaluation] Does Faithfulness Conflict with Plausibility? An Empirical Study in Explainable AI across NLP Tasks
266	    Authors: Xiaolei Lu, Jianghong Ma | Year: 2024 | Venue: arXiv 2404.00140
267	    Summary: 在 sentiment analysis、intent detection、topic labeling 三个 NLP 任务上 系统比较 faithfulness 和 plausibility 的关系
268	
269	  [key_evidence] Faithfulness vs. Plausibility: On the (Un)Reliability of Explanations from Large Language Models
270	    Authors: Anonymous | Year: 2024 | Venue: arXiv 2402.04614
271	    Summary: LLM 擅长生成 plausible 的解释，但这些解释不一定 faithful—— 不与 LLM 的实际推理过程对齐
272	
273	  [evaluation] Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps
274	    Authors: Anonymous | Year: 2025 | Venue: EMNLP 2025
275	    Summary: 通过 unlearning 推理步骤来衡量 CoT 的 faithfulness
276	
277	=== lora_qlora_artifacts (6 papers) ===
278	  [key_evidence] LoRA vs Full Fine-tuning: An Illusion of Equivalence
279	    Authors: Reece Shuttleworth, Jacob Andreas, Antonio Torralba, Pratyusha Sharma | Year: 2024 | Venue: arXiv 2410.21228
280	    Summary: LoRA 和 full fine-tuning 产生结构上根本不同的权重矩阵
281	
282	  [theoretical_support] The Impact of LoRA on the Emergence of Clusters in Transformers
283	    Authors: Hugo Koubbi, Louis Hernandez, Matthieu Boussard | Year: 2024 | Venue: arXiv 2402.15415
284	    Summary: 用 mean-field self-attention toy model 研究 LoRA fine-tuning 的 forgetting 机制
285	
286	  [direct-competitor] QeRL: Beyond Efficiency -- Quantization-enhanced Reinforcement Learning for LLMs
287	    Authors: NVIDIA, MIT, HKU, THU | Year: 2025 | Venue: arXiv 2510.11696
288	    Summary: 标准量化引入静态确定性噪声，对 RL 后期训练不利
289	
290	  [key_evidence] The Impact of Quantization on Large Reasoning Model Reinforcement Learning
291	    Authors: Anonymous | Year: 2025 | Venue: NeurIPS 2025 Workshop (Efficient Reasoning)
292	    Summary: 系统评估量化对 LRM RL 训练的影响
293	
294	  [related_analysis] Accurate and Efficient Fine-Tuning of Quantized Large Language Models Through Optimal Balance in Adaptation
295	    Authors: Shinhyuk Seo et al. | Year: 2024 | Venue: TACL 2025
296	    Summary: 识别量化 LLM + LoRA 的不平衡问题：adapter 输入输出过于复杂而有效可训练性不足，导致欠拟合
297	
298	  [related_method] CLoQ: Enhancing Fine-Tuning of Quantized LLMs via Calibrated LoRA Initialization
299	    Authors: Unknown | Year: 2025 | Venue: arXiv 2501.18475
300	    Summary: QLoRA 中量化误差影响 LoRA 训练
301	
302	=== grpo_nlp_applications (2 papers) ===
303	  [direct-competitor] ReasoningNER: A Reasoning Paradigm for Named Entity Recognition
304	    Authors: Anonymous | Year: 2025 | Venue: arXiv 2511.11978
305	    Summary: 三阶段 NER 框架：CoT Generation → CoT Tuning → GRPO Reasoning Enhancement
306	
307	  [method-component] Posterior-GRPO: Rewarding Reasoning Processes in Code Generation
308	    Authors: Anonymous | Year: 2025 | Venue: arXiv 2508.05170
309	    Summary: 在代码生成中仅对成功输出的推理过程施加 process-based reward（条件 reward）， 有效抑制 reward hacking——模型不能通过错误推理碰巧生成正确代码来获得高 reward
310	
311	=== rsft_offline_rl (4 papers) ===
312	  [direct-competitor] OREO: Offline Reinforcement Learning for LLM Multi-Step Reasoning
313	    Authors: Anonymous | Year: 2024 | Venue: arXiv 2412.16145
314	    Summary: 基于 maximum entropy RL 的 offline 方法，联合学习 policy model 和 value function， 优化 soft Bellman Equation
315	
316	  [key_evidence] PCL-Reasoner-V1.5: Advancing Math Reasoning with Offline Reinforcement Learning
317	    Authors: Yao Lu, Dengdong Fan, Jianzheng Nie, Fan Xu, Jie Chen, Bin Zhou, Yonghong Tian | Year: 2026 | Venue: arXiv 2601.14716
318	    Summary: 基于 Qwen2.5-32B 的数学推理模型
319	
320	  [method-component] RS-DPO: A Hybrid Rejection Sampling and Direct Preference Optimization Method for Alignment of Large Language Models
321	    Authors: Anonymous | Year: 2024 | Venue: NAACL 2024 Findings
322	    Summary: 系统性结合 rejection sampling 和 DPO
323	
324	  [background] RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment
325	    Authors: Anonymous | Year: 2024 | Venue: TMLR 2024
326	    Summary: RAFT 是 rejection sampling fine-tuning 的标准化框架：迭代式 generate → rank → filter → SFT
327	
328	=== evidence_docre (3 papers) ===
329	  [related_method] EAAGRE: Evidence and Axial Attention Guided Document-level Relation Extraction
330	    Authors: Unknown (Computer Speech and Language) | Year: 2024 | Venue: Computer Speech and Language 2024
331	    Summary: 联合考虑 evidence information 和 relation triple 的全局交互
332	
333	  [related_method] GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction
334	    Authors: Yanxu Mao et al. | Year: 2024 | Venue: arXiv 2407.21384
335	    Summary: 用 GCN 构建多权重矩阵引导 attention 到 evidence sentences
336	
337	  [related_method] KnowRA: Knowledge Retrieval Augmented Method for Document-level Relation Extraction with Comprehensive Reasoning Abilities
338	    Authors: Chengcheng Mai et al. | Year: 2025 | Venue: IJCAI 2025
339	    Summary: 通过外部知识库检索增强 DocRE 推理
340	
341	=== faithfulness_structured (4 papers) ===
342	  [related_method] G&O: A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction
343	    Authors: Yinghao Li et al. | Year: 2024 | Venue: arXiv 2402.13364
344	    Summary: 将 structured IE 拆为两步：先用自然语言生成内容，再组织为目标结构
345	
346	  [related_method] Improved Evidence Extraction and Metrics for Document Inconsistency Detection with LLMs
347	    Authors: Nelvin Tan et al. | Year: 2026 | Venue: arXiv 2601.02627
348	    Summary: 引入新的 evidence extraction 评估指标和 redact-and-retry 框架
349	
350	  [supporting_evidence] Diagnosing Structural Failures in LLM-Based Evidence Extraction for Meta-Analysis
351	    Authors: Unknown | Year: 2026 | Venue: arXiv 2602.10881
352	    Summary: LLM 在结构化 evidence extraction 中存在系统性 structural breakdown： role reversal、cross-analysis binding drift、instance compression、numeric misattribution
353	
354	  [related_method] Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion (APIE)
355	    Authors: Unknown | Year: 2025 | Venue: AAAI 2026
356	    Summary: 提出 dual-component uncertainty metric 量化 LLM 在 IE 中的 Format Uncertainty （结构语法困难）和 Content Uncertainty（语义不一致）
357	
358	=== grpo_structured (4 papers) ===
359	  [related_method] GRPO-LEAD: A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models
360	    Authors: Jixiao Zhang, Chunsheng Zuo | Year: 2025 | Venue: EMNLP 2025
361	    Summary: 增强 GRPO：(1) length-regularized rewards 鼓励简洁性； (2) 对错误解的显式惩罚提升精度； (3) difficulty-aware advantage reweighting 增强泛化
362	
363	  [closest_prior_work] E-GRPO: Entity-Aware Reward for Group Relative Policy Optimization
364	    Authors: Unknown | Year: 2025 | Venue: ICLR 2026
365	    Summary: 提出 entity-aware reward function，对 negative samples 基于 entity match rate 给 partial credit
366	
367	  [supporting_evidence] RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs
368	    Authors: Hangzhan Jin et al. | Year: 2025 | Venue: arXiv 2508.16546
369	    Summary: RL-FT 可恢复 SFT 导致的大部分 OOD 性能损失，但当 SFT 造成严重 overfitting 时 RL 无法完全恢复
370	
371	  [related_method] Aligning Instruction-Tuned LLMs for Event Extraction with Multi-objective Reinforcement Learning
372	    Authors: Unknown | Year: 2025 | Venue: Springer 2025
373	    Summary: 将多目标强化学习应用于事件抽取，在 instruction-tuned LLM 基础上用 RL 优化抽取性能
374	
375	=== qlora_fft_gap (2 papers) ===
376	  [supporting_evidence] How Much is Too Much? Exploring LoRA Rank Trade-offs for Retaining Knowledge and Domain Robustness
377	    Authors: Darshita Rathore et al. | Year: 2025 | Venue: IJCNLP-AACL 2025
378	    Summary: 中等 rank (r=32-64) 在表征能力和稳定性之间达到最佳平衡
379	
380	  [related_method] RandLoRA: Full-rank Parameter-Efficient Fine-tuning of Large Models
381	    Authors: Paul Albert et al. | Year: 2025 | Venue: ICLR 2025
382	    Summary: 通过学习 fixed random matrices 的 diagonal scaling 实现 full-rank 更新， 保持参数效率同时突破 low-rank 限制
383	
384	=== mtl_ie_tradeoff (3 papers) ===
385	  [closest_prior_work] C-LoRAE: Collaborative Multi-LoRA Experts with Achievement-based Multi-Tasks Loss for Unified Multimodal Information Extraction
386	    Authors: Unknown | Year: 2025 | Venue: arXiv 2505.06303
387	    Summary: 扩展 LoRA 引入 universal expert（跨任务共享知识）和 task-specific experts
388	
389	  [related_method] Ortho-LoRA: Disentangling Task Conflicts in Multi-Task LoRA via Orthogonal Gradient Projection
390	    Authors: Ziyu Yang et al. | Year: 2026 | Venue: arXiv 2601.09684
391	    Summary: 针对 LoRA 的 bipartite 结构设计 gradient projection 方法
392	
393	  [supporting_evidence] Proactive Gradient Conflict Mitigation in Multi-Task Learning: A Sparse Training Perspective
394	    Authors: Zhi Zhang et al. | Year: 2024 | Venue: arXiv 2411.18615
395	    Summary: 从 Sparse Training 角度缓解 gradient conflict： 选择原始模型参数子集同时学习多任务，冻结其余参数
396	
397	=== survey (1 papers) ===
398	  [survey] Large Language Models for Generative Information Extraction: A Survey
399	    Authors: Unknown | Year: 2024 | Venue: Frontiers of Computer Science 2024
400	    Summary: 全面综述 LLM 在 IE 各子任务（NER、RE、EE 等）中的应用
401	
402	=== inference_time_reranking (5 papers) ===
403	  [key_baseline] Is Best-of-N the Best of Them? Coverage, Scaling, and Optimality in Inference-Time Alignment
404	    Authors: Audrey Huang et al. | Year: 2025 | Venue: ICML 2025
405	    Summary: Best-of-N sampling provably suffers from reward hacking when N is large
406	
407	  [related_analysis] Inference-Time Reward Hacking in Large Language Models
408	    Authors: Yiwei Chen et al. | Year: 2025 | Venue: NeurIPS 2025 Spotlight
409	    Summary: 证明 BoN 中 true reward 先升后降的 hacking pattern 是所有 inference-time 机制的固有属性
410	
411	  [method_component] Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models
412	    Authors: Yinlam Chow et al. | Year: 2024 | Venue: ICLR 2025
413	    Summary: 提出 inference-aware fine-tuning 范式：训练时直接优化 BoN inference 策略的性能
414	
415	  [evaluation] Evaluation of Best-of-N Sampling Strategies for Language Model Alignment
416	    Authors: Yuki Ichihara et al. | Year: 2025 | Venue: TMLR 2025
417	    Summary: 系统评估 BoN 采样的 reward hacking 问题
418	
419	  [related_method] Regularized Best-of-N Sampling with Minimum Bayes Risk Objective for Language Model Alignment
420	    Authors: Yuu Jinnai et al. | Year: 2024 | Venue: NAACL 2025
421	    Summary: MBR-BoN：用 Minimum Bayes Risk 目标作为 proximity regularizer 缓解 reward hacking
422	
423	=== faithfulness_nli (4 papers) ===
424	  [method_component] FaithLens: Detecting and Explaining Faithfulness Hallucination
425	    Authors: Unknown | Year: 2025 | Venue: arXiv 2512.20182
426	    Summary: 8B 参数模型通过合成训练数据 + rule-based RL 优化， 在 12 个 faithfulness 检测任务上超越 GPT-4.1 和 o3
427	
428	  [method_component] PrefixNLI: Detecting Factual Inconsistencies as Soon as They Arise
429	    Authors: Sapir Harary et al. | Year: 2025 | Venue: arXiv 2511.01359
430	    Summary: 将 NLI 从完整句子推广到任意文本前缀，训练 MiniTruePrefixes 模型
431	
432	  [evaluation] Revisiting NLI: Towards Cost-Effective and Human-Aligned Metrics for Evaluating LLMs in Question Answering
433	    Authors: Unknown | Year: 2025 | Venue: arXiv 2511.07659
434	    Summary: 轻量 NLI scoring + 简单 lexical-match flag 在 long-form QA 上匹配 GPT-4o 准确率 (89.9%)， 参数量少几个数量级
435	
436	  [evaluation] Benchmarking LLM Faithfulness in RAG with Evolving Leaderboards
437	    Authors: Manveer Singh Tamber et al. | Year: 2025 | Venue: EMNLP Industry 2025
438	    Summary: FaithJudge 框架：利用多样化人工标注 hallucination 样本池改进 LLM-as-judge 评估
439	
440	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "95197b5f-7f15-4c99-945e-44fae6ba93d7"
}
```

</details>

---

### System

_source line 56_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "ad94f71e34c9ad9c0",
  "tool_use_id": "toolu_013Lrje7vQRGqSdwXn2BhLuJ",
  "status": "completed",
  "output_file": "",
  "summary": "Extract literature map data",
  "usage": {
    "total_tokens": 65927,
    "tool_uses": 13,
    "duration_ms": 322968
  },
  "uuid": "d6b53829-1e7a-4a04-9551-af5087f841bb",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794"
}
```

---

### Tool result

_source line 57 · 2026-05-16T00:45:25.566Z_

<details><summary>↩ Tool result · `toolu_013Lrje7vQRGqSdwXn2BhLuJ`</summary>

```text
Here is the complete extraction of all 101 papers from the FREIGE literature map, grouped by 32 categories.

---

## Category 1: reward_diversity (4 papers)

1. **GDPO** -- "GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization"
   - Authors: NVIDIA Labs | 2025 | ICML 2026
   - Role: closest_prior_work
   - Summary: Per-reward independent group-wise normalization before aggregation prevents advantage collapse when combining multiple rewards in GRPO.

2. **DRA-GRPO** -- "DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of LLMs"
   - Authors: Xiwen Chen et al. | 2025 | arXiv 2505.09655
   - Role: related_method
   - Summary: Uses submodular mutual information to reweight rewards, giving higher weight to diverse completions to prevent policy collapse to prior modes.

3. **Shrinkage Baselines** -- "Shrinking the Variance: Shrinkage Baselines for RL with Verifiable Rewards"
   - Authors: Guanning Zeng et al. | 2025 | arXiv 2511.03710
   - Role: theoretical_support
   - Summary: James-Stein shrinkage mixing per-prompt and cross-prompt mean baselines yields provably lower-variance policy gradient estimators in RLVR.

4. **Reward Shaping** -- "Reward Shaping to Mitigate Reward Hacking in RLHF"
   - Authors: Anonymous | 2025 | arXiv 2502.18770
   - Role: background
   - Summary: Systematically studies reward shaping principles; bounded rewards with fast-then-slow growth suppress reward hacking and improve training stability.

---

## Category 2: mode_collapse_prevention (6 papers)

5. **DAPO** -- "DAPO: An Open-Source LLM Reinforcement Learning System at Scale"
   - Authors: ByteDance Seed, Tsinghua AIR | 2025 | NeurIPS 2025
   - Role: key_baseline
   - Summary: Addresses GRPO entropy collapse via Clip-Higher (asymmetric clipping) and Dynamic Sampling that filters zero-gradient prompts; achieves 50 on AIME 2024.

6. **Dr. GRPO** -- "Dr. GRPO: Removing Optimization Bias in GRPO"
   - Authors: Liu et al. | 2025 | COLM 2025
   - Role: related_analysis
   - Summary: Identifies difficulty bias and length bias from GRPO's std normalization; proposes unbiased Monte Carlo advantage by removing std normalization.

7. **GVPO** -- "GVPO: Group Variance Policy Optimization for LLM Post-Training"
   - Authors: Anonymous | 2025 | NeurIPS 2025
   - Role: alternative_framework
   - Summary: Embeds the analytic solution of KL-constrained reward maximization into gradient weights; variance term naturally balances exploration and exploitation.

8. **REINFORCE++** -- "REINFORCE++: Stabilizing Critic-Free Policy Optimization with Global Advantage Normalization"
   - Authors: Jian Hu et al. | 2025 | arXiv 2501.03262
   - Role: related_method
   - Summary: Global batch normalization for advantage estimation provides a more stable, theoretically unbiased gradient estimator than local prompt-level normalization.

9. **DiverseGRPO** -- "DiverseGRPO: Mitigating Mode Collapse in Image Generation via Diversity-Aware GRPO"
   - Authors: Henglin Liu et al. | 2025 | arXiv 2512.21514
   - Role: parallel_work
   - Summary: Addresses GRPO output homogenization in image generation via distributional reward modeling (spectral clustering + exploratory reward), achieving 13-18% semantic diversity gain.

10. **GRPO Normalization Theory** -- "Why GRPO Needs Normalization: A Local-Curvature Perspective on Adaptive Gradients"
    - Authors: Anonymous | 2025 | arXiv 2601.23135
    - Role: theoretical_support
    - Summary: Proves GRPO's reward_std normalization provides strictly better convergence rates than unnormalized REINFORCE; benefit characterized by average inter-prompt reward std.

---

## Category 3: contrastive_reward (3 papers)

11. **Contrastive Rewards for RLHF** -- "Improving Reinforcement Learning from Human Feedback Using Contrastive Rewards"
    - Authors: Shen, Zhang et al. | 2024 | arXiv 2403.07708
    - Role: closest_contrastive_precedent
    - Summary: Offline-sampled baseline responses compute contrastive reward as PPO penalty; penalizes reward uncertainty, adaptively calibrates by task difficulty, reduces variance.

12. **Contrastive RM Training** -- "Improving Discriminative Capability of Reward Models in RLHF Using Contrastive Learning"
    - Authors: Anonymous | 2024 | EMNLP 2024
    - Role: related_method
    - Summary: Unsupervised contrastive loss trains reward models to better capture discriminative features, leading to more stable PPO training returns.

13. **CPL** -- "Contrastive Preference Learning: Learning from Human Feedback without RL"
    - Authors: Anonymous | 2024 | ICLR 2025
    - Role: background
    - Summary: Reformulates preference learning as contrastive learning, enabling learning from human feedback without explicit RL.

---

## Category 4: evidence_reward (3 papers)

14. **Drift** -- "Drift: Enhancing LLM Faithfulness in Rationale Generation"
    - Authors: Anonymous | 2025 | ACL 2025
    - Role: related_method
    - Summary: Uses faithfulness reward to guide LLMs toward more reliable rationale generation, improving factual consistency of CoT reasoning.

15. **INFUSE** -- "Fine-Grained NLI-Based Faithfulness Evaluation for Diverse Summarisation Tasks"
    - Authors: Anonymous | 2024 | EACL 2024
    - Role: background
    - Summary: Variable-length premise + simplified hypothesis for fine-grained NLI faithfulness evaluation, surpassing traditional NLI on multi-task summarization.

16. **Cross-Evidence Reasoning Graph** -- "Enhancing Cross-Evidence Reasoning Graph for Document-Level Relation Extraction"
    - Authors: Anonymous | 2024 | PMC/Bioinformatics 2024
    - Role: background
    - Summary: Uses cross-evidence reasoning graph to enhance cross-evidence reasoning in document-level relation extraction.

---

## Category 5: multi_objective_rl (2 papers)

17. **Constrained RLHF** -- "Confronting Reward Model Overoptimization with Constrained RLHF"
    - Authors: Anonymous | 2025 | OpenReview
    - Role: related_analysis
    - Summary: Studies overoptimization in multi-component reward models; inter-component correlation significantly affects the overoptimization threshold; uses constrained MDP.

18. **Optimal Reward Baseline** -- "On-Policy RL with Optimal Reward Baseline"
    - Authors: Anonymous | 2025 | arXiv 2505.23585
    - Role: theoretical_support
    - Summary: Optimal baseline consistently achieves higher training reward and higher entropy, stabilizing training and promoting more diverse policy exploration.

---

## Category 6: rsft_methodology (5 papers)

19. **Minimalist RSFT** -- "A Minimalist Approach to LLM Reasoning: from Rejection Sampling to Reinforce"
    - Authors: Xiao et al. | 2025 | arXiv 2504.11343
    - Role: key_theoretical_support
    - Summary: RAFT (simple rejection sampling) matches GRPO/PPO on math reasoning; GRPO's main advantage comes from discarding all-wrong prompts, not reward normalization.

20. **TrajFusion** -- "Beyond Rejection Sampling: Trajectory Fusion for Scaling Mathematical Reasoning"
    - Authors: Jie Deng et al. | 2026 | arXiv 2602.04391
    - Role: method_component
    - Summary: Interleaves failed and correct trajectories to explicitly model trial-and-error reasoning, significantly outperforming standard RFT on hard math problems.

21. **RSFT = PPO** -- "Rejection Sampling Based Fine Tuning Secretly Performs PPO"
    - Authors: Anonymous | 2025 | ICML 2025
    - Role: theoretical_support
    - Summary: Establishes theoretical link between RSFT and PPO: rejection sampling fine-tuning implicitly performs PPO with marginal KL constraints under certain conditions.

22. **AdaSTaR** -- "AdaSTaR: Adaptive Data Sampling for Training Self-Taught Reasoners"
    - Authors: Hyung Won Chung et al. | 2025 | NeurIPS 2025
    - Role: related_method
    - Summary: Introduces diversity sampling + curriculum sampling for RFT/RSFT to address training imbalance; achieves SOTA on 6 benchmarks with 58.6% fewer training FLOPs.

23. **RIFT** -- "RIFT: Repurposing Negative Samples via Reward-Informed Fine-Tuning"
    - Authors: Unknown | 2026 | arXiv 2601.09253
    - Role: direct_competitor
    - Summary: Instead of hard rejection, reweights all trajectories by scalar reward; positive samples encourage correct behavior, negative samples provide reverse gradients.

---

## Category 7: rl_for_ie (6 papers)

24. **R1-RE** -- "R1-RE: Cross-Domain Relation Extraction with RLVR"
    - Authors: Runpeng Dai, Tong Zheng et al. | 2025 | arXiv 2507.04642
    - Role: direct_competitor
    - Summary: First RLVR (GRPO + verifiable reward) framework for relation extraction; R1-RE-7B achieves ~70% cross-domain OOD accuracy, matching GPT-4o on sentence-level RE.

25. **MORE-R1** -- "MORE-R1: Guiding LVLM for Multimodal Object-Entity Relation Extraction via Stepwise Reasoning with RL"
    - Authors: Anonymous | 2026 | arXiv 2603.09478
    - Role: related_method
    - Summary: Uses GRPO + Progressive Sample-Mixing Strategy to optimize LVLM reasoning for multimodal RE.

26. **REAR** -- "REAR: Reinforced Reasoning Optimization for Event Argument Extraction with Relation-Aware Support"
    - Authors: Jianwen Luo et al. | 2025 | EMNLP 2025 Findings
    - Role: related_method
    - Summary: Applies RL reasoning optimization to event argument extraction with relation-aware support.

27. **Adaptive RL Planning for IE** -- "Adaptive Reinforcement Learning Planning: Harnessing LLMs for Complex Information Extraction"
    - Authors: Zepeng Ding et al. | 2024 | arXiv 2406.11455
    - Role: background
    - Summary: Models LLM sequential extraction as MDP, trains DDQN decision module to adaptively select entity extraction order for complex IE.

28. **Graph-R1** -- "Graph-R1: Towards Agentic GraphRAG Framework via End-to-end Reinforcement Learning"
    - Authors: Haoran Luo et al. | 2025 | ICML 2026
    - Role: background
    - Summary: End-to-end RL optimizes GraphRAG agent's multi-round retrieval-reasoning loop including knowledge hypergraph construction.

29. **R2GRPO** -- "R2GRPO: Better LLMs for Scientific Information Extraction with MimicSFT and Relevance and Rule-induced GRPO"
    - Authors: Li, Di, Liu, Jing, Qiu, Chen | 2025 | arXiv 2505.22068
    - Role: related_method
    - Summary: Two-stage MimicSFT + R2GRPO (relevance reward + rule-mining reward) surpasses baseline LLMs and specialized models on scientific IE RE benchmarks.

---

## Category 8: llm_docre (6 papers)

30. **RelPrior** -- "RelPrior: Relation as a Prior - A Novel Paradigm for LLM-based Document-level Relation Extraction"
    - Authors: Anonymous | 2025 | arXiv 2511.08143
    - Role: key_baseline
    - Summary: Uses binary relation as prior to filter irrelevant entity pairs, then matches predefined relations; LLaMA3-8B achieves DocRED test F1=48.34, Re-DocRED test F1=54.80.

31. **LMRC** -- "LMRC: LLM with Relation Classifier for Document-Level Relation Extraction"
    - Authors: Xingzuo Li, Kehai Chen, Yunfei Long, Min Zhang | 2024 | arXiv 2408.13889
    - Role: related_method
    - Summary: Two-stage: BERT attention-based classifier filters NA entity pairs, then LLM does multi-class classification; DocRED test F1=60.52, Re-DocRED test F1=74.63 (hybrid method).

32. **Ru-LLM** -- "Ru-LLM: Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction"
    - Authors: Anonymous | 2025 | NLPCC 2025
    - Role: related_method
    - Summary: Mines frequent pattern logical rules via MCTS, converts to prompt constraints on LLM output, then CoT-verifies rule satisfaction.

33. **GLiDRE** -- "GLiDRE: Generalist Lightweight model for Document-level Relation Extraction"
    - Authors: Anonymous | 2025 | arXiv 2508.00757
    - Role: background
    - Summary: Dual-encoder lightweight zero/few-shot DocRE model pretrained on 136K documents; fully supervised Re-DocRED test F1=77.83 (encoder-based, not LLM generative).

34. **AutoRE** -- "AutoRE: Document-Level Relation Extraction with Large Language Models"
    - Authors: Anonymous | 2024 | arXiv 2403.14888
    - Role: background
    - Summary: RHF (Relation-Head-Facts) paradigm using Mistral-7B + QLoRA for end-to-end DocRE; Re-DocRED test F1=51.91 (Mistral), 51.97 (LLaMA3-8B).

35. **DocKS-RAG** -- "DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning"
    - Authors: Xu et al. | 2025 | ICML 2025
    - Role: direct_competitor
    - Summary: Builds document-level knowledge graph for structural info + sentence-level semantic RAG for context; hybrid-prompt tuning integrates both into LLM.

---

## Category 9: evidence_generation_tradeoff (4 papers)

36. **Mind Your Step** -- "Mind Your Step (by Step): Chain-of-Thought can Reduce Performance on Tasks where Thinking Makes Humans Worse"
    - Authors: Sprague et al. | 2024 | NeurIPS 2024
    - Role: key_evidence
    - Summary: CoT reduces performance by up to 36.3% on certain tasks; explicit reasoning steps introduce error accumulation; implicit reasoning outperforms under distribution shift.

37. **EIDER** -- "Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion"
    - Authors: Xie et al. (Google Research) | 2022 | ACL Findings 2022
    - Role: closest_docre_precedent
    - Summary: Joint RE + evidence extraction with inference-stage fusion: separate RE predictions on extracted evidence and full document, blended via fusion layer; +1.37 Ign F1 on DocRED.

38. **Performance-Explanation Trade-off** -- "Exploring the Trade-off Between Model Performance and Explanation Plausibility of Text Classifiers Using Human Rationales"
    - Authors: Resck, Raimundo, Poco | 2024 | NAACL Findings 2024
    - Role: formal_framework
    - Summary: Multi-objective optimization exploring the Pareto frontier of performance vs. explanation plausibility; confirms rationale supervision reduces main task performance.

39. **Decreasing Value of CoT** -- "The Decreasing Value of Chain of Thought in Prompting"
    - Authors: Meincke, Mollick, Mollick, Shapiro | 2025 | Wharton Technical Report (SSRN)
    - Role: empirical_support
    - Summary: On modern reasoning models, CoT benefit is marginal (4-13%) but latency increases 35-600%; stronger models benefit less from explicit reasoning.

---

## Category 10: negative_transfer (1 paper)

40. **ForkMerge** -- "ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning"
    - Authors: Jiang, Chen et al. | 2023 | NeurIPS 2023
    - Role: theoretical_framework
    - Summary: Auxiliary tasks cause negative transfer from both gradient conflict and auxiliary-target generalization gap; periodic fork-and-merge with dynamic task weight search filters harmful updates.

---

## Category 11: faithfulness_accuracy_tradeoff (3 papers)

41. **Correctness != Faithfulness** -- "Correctness is not Faithfulness in RAG Attributions"
    - Authors: Wallat, Heuss, de Rijke, Anand | 2024 | SIGIR 2025
    - Role: key_conceptual_framework
    - Summary: Correctness and faithfulness are independent dimensions that can conflict; up to 57% of citations are post-rationalized rather than genuine bases for answers.

42. **Evaluating Correctness & Faithfulness** -- "Evaluating Correctness and Faithfulness of Instruction-Following Models for Question Answering"
    - Authors: Adlakha, BehnamGhader, Lu, Meade, Reddy | 2024 | TACL 2024
    - Role: evaluation_framework
    - Summary: Instruction-following LLMs match fine-tuned models on correctness but are consistently poor on faithfulness -- they hallucinate rather than ground in provided evidence.

43. **Faithful Explanation Survey** -- "Towards Faithful Model Explanation in NLP: A Survey"
    - Authors: Lyu, Havaldar, Stein et al. | 2024 | Computational Linguistics (MIT Press)
    - Role: comprehensive_survey
    - Summary: Comprehensive survey of faithful explanation in NLP; identifies faithfulness-performance trade-off as core challenge; recommends multi-objective optimization and post-hoc verification.

---

## Category 12: reranking_verification_bridge (1 paper)

44. **Genie** -- "Genie: Achieving Human Parity in Content-Grounded Datasets Generation"
    - Authors: Yehudai, Carmeli, Mass et al. | 2024 | ICLR 2024
    - Role: methodological_precedent
    - Summary: Three-stage pipeline (Content Preparation, Generation, NLI-based Filtering) using fine-tuned T5-11B NLI to filter unfaithful generation; achieves human parity on LFQA/summarization/IE.

---

## Category 13: evidence_grounded_rl (1 paper)

45. **EvidenceRL** -- "EvidenceRL: Reinforcing Evidence Consistency for Trustworthy Language Models"
    - Authors: Ben Tamo, Lu, Marteau, Nnamdi, Wang | 2026 | arXiv 2603.19532
    - Role: closest_competitor
    - Summary: Uses GRPO to jointly optimize grounding (evidence entailment) and correctness; cardiac diagnosis F1@3 37.0->54.5, grounding 47.6->78.2, hallucination reduced 5x.

---

## Category 14: multi_objective_grpo (2 papers)

46. **MO-GRPO** -- "MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems"
    - Authors: Ichihara, Jinnai, Morimura, Sakamoto, Mitsuhashi, Uchibe | 2025 | arXiv 2509.22047
    - Role: related_method
    - Summary: GRPO under multi-objective settings easily reward-hacks one objective at the cost of others; variance-based normalization auto-balances multiple reward functions.

47. **RDPO** -- "Multi-Objective and Mixed-Reward Reinforcement Learning via Reward-Decorrelated Policy Optimization"
    - Authors: Bai, Liu, Zhuang, Zhou, Weng, Chen, Wang, Cai | 2026 | arXiv 2605.13641
    - Role: related_method
    - Summary: Direct summation + normalization of mixed rewards drowns out weak signal dimensions; Mahalanobis whitening + magnitude-aware quantile normalization decorrelate reward subspaces.

---

## Category 15: grpo_theory (2 papers)

48. **GRPO = PRM** -- "GRPO is Secretly a Process Reward Model"
    - Authors: Sullivan, Koller | 2025 | under review at ICML 2026
    - Role: theoretical_insight
    - Summary: Proves GRPO + ORM is equivalent to a PRM-aware RL objective under certain conditions; proposes lambda-GRPO correcting deficiency on uneven process steps.

49. **Reward Hacking Survey** -- "Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges"
    - Authors: Wang et al. (23 authors) | 2026 | arXiv 2604.13602
    - Role: theoretical_framework
    - Summary: Proposes Proxy Compression Hypothesis (PCH): reward hacking stems from objective compression, optimization amplification, and evaluator-policy co-adaptation interaction.

---

## Category 16: training_precision_rl (1 paper)

50. **FP16 for RL** -- "Defeating the Training-Inference Mismatch via FP16"
    - Authors: Qi, Liu, Zhou, Pang, Du, Lee, Lin | 2025 | arXiv 2510.26788
    - Role: key_evidence
    - Summary: BF16 introduces large rounding errors in RL fine-tuning causing training-inference mismatch; BF16 training collapses at 150-600 steps; switching to FP16 eliminates the issue.

---

## Category 17: llm_ie_alignment (1 paper)

51. **ADELIE** -- "ADELIE: Aligning Large Language Models on Information Extraction"
    - Authors: Qi, Peng, Wang, Xu, Hou, Li | 2024 | EMNLP 2024
    - Role: key_baseline
    - Summary: Builds IEInstruct high-quality IE alignment corpus; trains with SFT + DPO; supports closed/open/on-demand IE modes; SOTA on multiple held-out IE datasets.

---

## Category 18: unfaithful_reasoning (2 papers)

52. **CoT != Explainability** -- "Chain-of-Thought Is Not Explainability"
    - Authors: Barez et al. | 2025 | Oxford WhiteBox Technical Report
    - Role: conceptual_support
    - Summary: CoT merely rationalizes (post-hoc) rather than faithfully reports the model's actual decision process; small manipulations change CoT chains without affecting decisions.

53. **LLMs as Rationalizers** -- "Characterizing Large Language Models as Rationalizers of Knowledge-Grounded Dialogue"
    - Authors: Anonymous | 2024 | ACL Findings 2024
    - Role: empirical_evidence
    - Summary: LLMs in knowledge-grounded dialogue consistently act as rationalizers not faithful reasoners; their explanations are inconsistent with the knowledge evidence they actually use.

---

## Category 19: latent_vs_explicit_reasoning (1 paper)

54. **Latent CoT Survey** -- "Reasoning Beyond Language: A Comprehensive Survey on Latent Chain-of-Thought Reasoning"
    - Authors: Chen, Zhao, Xia, Lu, Wang, Chen, Zhang, Wang, Li, Shen | 2025 | arXiv 2505.16782
    - Role: survey
    - Summary: Latent CoT decouples reasoning from explicit token generation to hidden state computation; matches or exceeds explicit CoT performance with 20x+ inference speedup.

---

## Category 20: evidence_based_docre (6 papers)

55. **DREEAM** -- "DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction"
    - Authors: Youmi Ma, An Wang, Naoaki Okazaki | 2023 | EACL 2023
    - Role: direct-competitor
    - Summary: Uses evidence as supervision signal to guide DocRE attention modules; proposes evidence retrieval self-training for silver evidence generation at scale; SOTA on DocRED.

56. **DocGNRE** -- "DocGNRE: Semi-automatic Data Enhancement for Document-Level Relation Extraction with Distant Supervision from Large Language Models"
    - Authors: Junpeng Li, Zixia Jia, Zilong Zheng | 2023 | EMNLP 2023
    - Role: method-component
    - Summary: Uses LLM (ChatGPT) + NLI module to semi-automatically generate relation triples for DocRE data augmentation, especially for long-tail relation types.

57. **CDER** -- "CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction"
    - Authors: Khai Phan Tran, Xue Li | 2025 | arXiv 2504.06529
    - Role: direct-competitor
    - Summary: Attentional graph-based architecture capturing collaborative patterns among semantically similar entity pairs within documents via bipartite graph with three subgraphs.

58. **Evidence-aware DocRE** -- "Evidence-aware Document-level Relation Extraction"
    - Authors: Xu T, Hua W, Qu J, Li Z, Xu J, Liu A et al. | 2022 | CIKM 2022
    - Role: background
    - Summary: Models evidence sentence selection as a sequential decision problem using RL mechanism to select supporting evidence sentences for relations.

59. **COREX** -- "COREX: Document-level Relation Extraction Framework with Consistent Two-Hop Reasoning and Evidence Sentence Prediction"
    - Authors: Unknown | 2024 | IEEE IJCNN 2024
    - Role: direct_competitor
    - Summary: Efficient two-hop reasoning representation jointly supervised by evidence prediction and RE; modified Adaptive Focal Loss for class imbalance; Weighted Fusion Layer for evidence.

60. **Grounded KG Extraction** -- "Grounded Knowledge Graph Extraction via LLMs: An Anchor-Constrained Framework with Provenance Tracking"
    - Authors: Unknown | 2025 | Computers 2025
    - Role: related_method
    - Summary: AEVS framework (anchor discovery, grounded extraction, verification, supplement) providing character-level provenance for each triple; hallucination rate 0.23-20.23%.

---

## Category 21: faithfulness_cost (3 papers)

61. **Faithfulness vs Plausibility (Empirical)** -- "Does Faithfulness Conflict with Plausibility? An Empirical Study in Explainable AI across NLP Tasks"
    - Authors: Xiaolei Lu, Jianghong Ma | 2024 | arXiv 2404.00140
    - Role: evaluation
    - Summary: Systematically compares faithfulness and plausibility across sentiment analysis, intent detection, topic labeling; finds they need not conflict and can be jointly optimized.

62. **Faithfulness vs Plausibility (LLM)** -- "Faithfulness vs. Plausibility: On the (Un)Reliability of Explanations from Large Language Models"
    - Authors: Anonymous | 2024 | arXiv 2402.04614
    - Role: key_evidence
    - Summary: LLMs generate plausible but not necessarily faithful explanations; self-explanations behave more like post-hoc rationalization than true reasoning reports.

63. **Unlearning CoT Faithfulness** -- "Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps"
    - Authors: Anonymous | 2025 | EMNLP 2025
    - Role: evaluation
    - Summary: Measures CoT faithfulness by unlearning individual reasoning steps; if model behavior is unchanged after unlearning, the step was not faithful.

---

## Category 22: lora_qlora_artifacts (6 papers)

64. **LoRA vs FFT** -- "LoRA vs Full Fine-tuning: An Illusion of Equivalence"
    - Authors: Reece Shuttleworth, Jacob Andreas, Antonio Torralba, Pratyusha Sharma | 2024 | arXiv 2410.21228
    - Role: key_evidence
    - Summary: LoRA and full fine-tuning produce structurally different weight matrices; LoRA introduces "intruder dimensions" (new high-rank singular vectors); forgetting concentrates in these dimensions.

65. **LoRA Cluster Impact** -- "The Impact of LoRA on the Emergence of Clusters in Transformers"
    - Authors: Hugo Koubbi, Louis Hernandez, Matthieu Boussard | 2024 | arXiv 2402.15415
    - Role: theoretical_support
    - Summary: Mean-field self-attention toy model reveals phase transition in LoRA forgetting behavior depending on perturbation norm and Transformer depth.

66. **QeRL** -- "QeRL: Beyond Efficiency -- Quantization-enhanced Reinforcement Learning for LLMs"
    - Authors: NVIDIA, MIT, HKU, THU | 2025 | arXiv 2510.11696
    - Role: direct-competitor
    - Summary: Standard quantization introduces static deterministic noise harmful to RL; Adaptive Quantization Noise (AQN) dynamically adjusts noise to promote exploration; enables 32B RL on single H100.

67. **Quantization Impact on RL** -- "The Impact of Quantization on Large Reasoning Model Reinforcement Learning"
    - Authors: Anonymous | 2025 | NeurIPS 2025 Workshop (Efficient Reasoning)
    - Role: key_evidence
    - Summary: Quantization-aware RL training actually harms the learning process; PTQ and QLoRA perform better; significant gap between post-RL quantized and quantization-aware RL models.

68. **Q-BLoRA** -- "Accurate and Efficient Fine-Tuning of Quantized Large Language Models Through Optimal Balance in Adaptation"
    - Authors: Shinhyuk Seo et al. | 2024 | TACL 2025
    - Role: related_analysis
    - Summary: Identifies imbalance in quantized LLM + LoRA: overly complex adapter I/O with insufficient effective trainability causes underfitting; Q-BLoRA simplifies I/O while increasing rank.

69. **CLoQ** -- "CLoQ: Enhancing Fine-Tuning of Quantized LLMs via Calibrated LoRA Initialization"
    - Authors: Unknown | 2025 | arXiv 2501.18475
    - Role: related_method
    - Summary: Quantization errors affect LoRA training; closed-form optimal LoRA initialization by minimizing per-layer difference between original and quantized+LoRA models on calibration data.

---

## Category 23: grpo_nlp_applications (2 papers)

70. **ReasoningNER** -- "ReasoningNER: A Reasoning Paradigm for Named Entity Recognition"
    - Authors: Anonymous | 2025 | arXiv 2511.11978
    - Role: direct-competitor
    - Summary: Three-stage NER framework (CoT Generation, CoT Tuning, GRPO Reasoning Enhancement) with composite reward; 8B model beats GPT-4 by 12.3 F1 on zero-shot NER.

71. **Posterior-GRPO** -- "Posterior-GRPO: Rewarding Reasoning Processes in Code Generation"
    - Authors: Anonymous | 2025 | arXiv 2508.05170
    - Role: method-component
    - Summary: Applies process-based reward only to successful outputs' reasoning processes; prevents reward hacking via incorrect reasoning that accidentally produces correct code.

---

## Category 24: rsft_offline_rl (4 papers)

72. **OREO** -- "OREO: Offline Reinforcement Learning for LLM Multi-Step Reasoning"
    - Authors: Anonymous | 2024 | arXiv 2412.16145
    - Role: direct-competitor
    - Summary: Maximum entropy RL offline method jointly learning policy and value function via soft Bellman Equation; better credit assignment without paired preference data; beats existing offline methods on GSM8K/MATH.

73. **PCL-Reasoner** -- "PCL-Reasoner-V1.5: Advancing Math Reasoning with Offline Reinforcement Learning"
    - Authors: Yao Lu, Dengdong Fan, Jianzheng Nie, Fan Xu, Jie Chen, Bin Zhou, Yonghong Tian | 2026 | arXiv 2601.14716
    - Role: key_evidence
    - Summary: Qwen2.5-32B-based math reasoning model using offline RL that surpasses GRPO and other online RL in training stability and efficiency; AIME 2024 avg 90.9%.

74. **RS-DPO** -- "RS-DPO: A Hybrid Rejection Sampling and Direct Preference Optimization Method for Alignment of Large Language Models"
    - Authors: Anonymous | 2024 | NAACL 2024 Findings
    - Role: method-component
    - Summary: Systematically combines rejection sampling and DPO; samples k responses per prompt, identifies contrastive pairs from reward distribution, then applies DPO alignment.

75. **RAFT** -- "RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment"
    - Authors: Anonymous | 2024 | TMLR 2024
    - Role: background
    - Summary: Canonical RSFT framework: iterative generate, rank, filter, SFT; generates n responses, ranks by reward model, takes top-k for SFT. Validated on text generation and dialogue.

---

## Category 25: evidence_docre (3 papers)

76. **EAAGRE** -- "EAAGRE: Evidence and Axial Attention Guided Document-level Relation Extraction"
    - Authors: Unknown (Computer Speech and Language) | 2024 | Computer Speech and Language 2024
    - Role: related_method
    - Summary: Guides PLM encoder's top-k token attention to evidence sentences without extra trainable parameters; axial attention models global interdependence among relation triples.

77. **GEGA** -- "GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction"
    - Authors: Yanxu Mao et al. | 2024 | arXiv 2407.21384
    - Role: related_method
    - Summary: GCN with multi-weight matrices guides attention to evidence sentences; Teacher-Student framework distills evidence weights from full supervision to student model.

78. **KnowRA** -- "KnowRA: Knowledge Retrieval Augmented Method for Document-level Relation Extraction with Comprehensive Reasoning Abilities"
    - Authors: Chengcheng Mai et al. | 2025 | IJCAI 2025
    - Role: related_method
    - Summary: External knowledge retrieval augments DocRE reasoning via document knowledge graph construction with coreference enhancement and knowledge filtering; axial attention for cross-sentence reasoning.

---

## Category 26: faithfulness_structured (4 papers)

79. **G&O** -- "G&O: A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction"
    - Authors: Yinghao Li et al. | 2024 | arXiv 2402.13364
    - Role: related_method
    - Summary: Decomposes structured IE into two steps: generate content in natural language first, then organize into target structure; separates content generation from structuring.

80. **Evidence Extraction Metrics** -- "Improved Evidence Extraction and Metrics for Document Inconsistency Detection with LLMs"
    - Authors: Nelvin Tan et al. | 2026 | arXiv 2601.02627
    - Role: related_method
    - Summary: Introduces new evidence extraction evaluation metrics and redact-and-retry framework; constrained filtering significantly outperforms direct prompting for evidence extraction.

81. **Structural Failures in Evidence Extraction** -- "Diagnosing Structural Failures in LLM-Based Evidence Extraction for Meta-Analysis"
    - Authors: Unknown | 2026 | arXiv 2602.10881
    - Role: supporting_evidence
    - Summary: LLMs exhibit systematic structural breakdowns in evidence extraction: role reversal, cross-analysis binding drift, instance compression, numeric misattribution.

82. **APIE** -- "Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion"
    - Authors: Unknown | 2025 | AAAI 2026
    - Role: related_method
    - Summary: Dual-component uncertainty metric quantifying Format Uncertainty (structural syntax difficulty) and Content Uncertainty (semantic inconsistency) in LLM-based IE.

---

## Category 27: grpo_structured (4 papers)

83. **GRPO-LEAD** -- "GRPO-LEAD: A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models"
    - Authors: Jixiao Zhang, Chunsheng Zuo | 2025 | EMNLP 2025
    - Role: related_method
    - Summary: Enhanced GRPO with length-regularized rewards, explicit error penalties, and difficulty-aware advantage reweighting for math reasoning.

84. **E-GRPO** -- "E-GRPO: Entity-Aware Reward for Group Relative Policy Optimization"
    - Authors: Unknown | 2025 | ICLR 2026
    - Role: closest_prior_work
    - Summary: Entity-aware reward function giving partial credit to negative samples based on entity match rate; uses ground-truth entities as factual correctness proxy to distinguish near-misses.

85. **RL vs SFT** -- "RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs"
    - Authors: Hangzhan Jin et al. | 2025 | arXiv 2508.16546
    - Role: supporting_evidence
    - Summary: RL-FT recovers most OOD performance lost by SFT, but cannot fully recover when SFT causes severe overfitting; recovery tied to singular vector direction rotation.

86. **Multi-objective RL for EE** -- "Aligning Instruction-Tuned LLMs for Event Extraction with Multi-objective Reinforcement Learning"
    - Authors: Unknown | 2025 | Springer 2025
    - Role: related_method
    - Summary: Applies multi-objective RL to event extraction on instruction-tuned LLMs, improving structured output quality.

---

## Category 28: qlora_fft_gap (2 papers)

87. **LoRA Rank Trade-offs** -- "How Much is Too Much? Exploring LoRA Rank Trade-offs for Retaining Knowledge and Domain Robustness"
    - Authors: Darshita Rathore et al. | 2025 | IJCNLP-AACL 2025
    - Role: supporting_evidence
    - Summary: Medium rank (r=32-64) achieves optimal balance between representation capacity and stability; LoRA-tuned models show robust generalization via transferable abstract skills.

88. **RandLoRA** -- "RandLoRA: Full-rank Parameter-Efficient Fine-tuning of Large Models"
    - Authors: Paul Albert et al. | 2025 | ICLR 2025
    - Role: related_method
    - Summary: Learns diagonal scaling of fixed random matrices to achieve full-rank updates while maintaining parameter efficiency; eliminates LoRA-FFT performance gap on vision-language tasks.

---

## Category 29: mtl_ie_tradeoff (3 papers)

89. **C-LoRAE** -- "C-LoRAE: Collaborative Multi-LoRA Experts with Achievement-based Multi-Tasks Loss for Unified Multimodal Information Extraction"
    - Authors: Unknown | 2025 | arXiv 2505.06303
    - Role: closest_prior_work
    - Summary: Extends LoRA with universal expert (cross-task shared) + task-specific experts; mutual information maximization promotes inter-expert exchange; achievement-based loss dynamically balances task progress.

90. **Ortho-LoRA** -- "Ortho-LoRA: Disentangling Task Conflicts in Multi-Task LoRA via Orthogonal Gradient Projection"
    - Authors: Ziyu Yang et al. | 2026 | arXiv 2601.09684
    - Role: related_method
    - Summary: Dynamically projects conflicting task gradients onto each other's orthogonal complement within LoRA's intrinsic subspace to resolve multi-task gradient conflicts.

91. **Sparse Training for MTL** -- "Proactive Gradient Conflict Mitigation in Multi-Task Learning: A Sparse Training Perspective"
    - Authors: Zhi Zhang et al. | 2024 | arXiv 2411.18615
    - Role: supporting_evidence
    - Summary: Selects subset of original model parameters for multi-task learning, freezing the rest; reduces high-dimensional optimization to lower-dimensional problem limiting each task's gradient influence range.

---

## Category 30: survey (1 paper)

92. **Generative IE Survey** -- "Large Language Models for Generative Information Extraction: A Survey"
    - Authors: Unknown | 2024 | Frontiers of Computer Science 2024
    - Role: survey
    - Summary: Comprehensive survey of LLMs in IE subtasks (NER, RE, EE, etc.); categorizes by subtask and technique; identifies structured output quality and efficiency as key challenges.

---

## Category 31: inference_time_reranking (5 papers)

93. **Best-of-N Optimality** -- "Is Best-of-N the Best of Them? Coverage, Scaling, and Optimality in Inference-Time Alignment"
    - Authors: Audrey Huang et al. | 2025 | ICML 2025
    - Role: key_baseline
    - Summary: BoN provably suffers from reward hacking at large N; proposes InferenceTimePessimism for scaling-monotonic performance; pre-trained policy coverage is key to BoN success.

94. **Inference-Time Reward Hacking** -- "Inference-Time Reward Hacking in Large Language Models"
    - Authors: Yiwei Chen et al. | 2025 | NeurIPS 2025 Spotlight
    - Role: related_analysis
    - Summary: Proves true reward first rises then falls (hacking pattern) is inherent to all inference-time mechanisms; proposes Best-of-Poisson (BoP) and HedgeTune for optimal reward-KL tradeoff.

95. **Inference-Aware Fine-Tuning** -- "Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models"
    - Authors: Yinlam Chow et al. | 2024 | ICLR 2025
    - Role: method_component
    - Summary: Trains model to directly optimize BoN inference performance; imitation learning and RL overcome non-differentiable argmax; model learns exploration-exploitation meta-strategy.

96. **BoN Evaluation** -- "Evaluation of Best-of-N Sampling Strategies for Language Model Alignment"
    - Authors: Yuki Ichihara et al. | 2025 | TMLR 2025
    - Role: evaluation
    - Summary: Systematic BoN reward hacking evaluation; proposes Stochastic Regularized BoN (SRBoN) with theoretical guarantees; simple sentence-length regularized BoN achieves comparable performance.

97. **MBR-BoN** -- "Regularized Best-of-N Sampling with Minimum Bayes Risk Objective for Language Model Alignment"
    - Authors: Yuu Jinnai et al. | 2024 | NAACL 2025
    - Role: related_method
    - Summary: Uses Minimum Bayes Risk objective as proximity regularizer for BoN to mitigate reward hacking; outperforms vanilla BoN and MBR decoding on AlpacaFarm and hh-rlhf.

---

## Category 32: faithfulness_nli (4 papers)

98. **FaithLens** -- "FaithLens: Detecting and Explaining Faithfulness Hallucination"
    - Authors: Unknown | 2025 | arXiv 2512.20182
    - Role: method_component
    - Summary: 8B model trained with synthetic data + rule-based RL outperforms GPT-4.1 and o3 on 12 faithfulness detection tasks; jointly predicts binary labels and generates explanations.

99. **PrefixNLI** -- "PrefixNLI: Detecting Factual Inconsistencies as Soon as They Arise"
    - Authors: Sapir Harary et al. | 2025 | arXiv 2511.01359
    - Role: method_component
    - Summary: Extends NLI from complete sentences to arbitrary text prefixes; MiniTruePrefixes model surpasses baseline NLI by 5-14 F1 on prefix-level entailment; enables controlled decoding.

100. **NLI for QA Evaluation** -- "Revisiting NLI: Towards Cost-Effective and Human-Aligned Metrics for Evaluating LLMs in Question Answering"
     - Authors: Unknown | 2025 | arXiv 2511.07659
     - Role: evaluation
     - Summary: Lightweight NLI scoring + lexical-match flag matches GPT-4o accuracy (89.9%) on long-form QA with orders of magnitude fewer parameters.

101. **FaithJudge** -- "Benchmarking LLM Faithfulness in RAG with Evolving Leaderboards"
     - Authors: Manveer Singh Tamber et al. | 2025 | EMNLP Industry 2025
     - Role: evaluation
     - Summary: FaithJudge framework with diverse human-annotated hallucination sample pools for improved LLM-as-judge evaluation; evolving leaderboard across summarization, QA, and data-to-text.

---

**Total: 101 papers across 32 categories.**

agentId: ad94f71e34c9ad9c0 (use SendMessage with to: 'ad94f71e34c9ad9c0' to continue this agent)
&lt;usage>total_tokens: 77420
tool_uses: 13
duration_ms: 322978&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "042ef0f4-2f37-4c4e-8dd4-12e59fc3f310",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Read the file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7341df47-ab61-4a7f-ab4b-fc80cccd2794/tool-results/mcp-agent-ml-research-read_project_file-1778891987655.txt\n\nThis is a JSON file with schema: {result: string}. The inner `result` field contains a YAML string representing a literature_map.yaml for an ML research project called FREIGE (about evidence-grounded document-level relation extraction).\n\nExtract ALL papers from this literature map. For each paper, I need:\n- The citation key (e.g., author_year)\n- The title\n- The category/section it belongs to\n- A one-line summary of what the paper does\n\nGroup them by category. Return the COMPLETE list — do not skip any papers. This is critical for writing a Related Work section. Format as structured text, not YAML.",
    "agentId": "ad94f71e34c9ad9c0",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the complete extraction of all 101 papers from the FREIGE literature map, grouped by 32 categories.\n\n---\n\n## Category 1: reward_diversity (4 papers)\n\n1. **GDPO** -- \"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization\"\n   - Authors: NVIDIA Labs | 2025 | ICML 2026\n   - Role: closest_prior_work\n   - Summary: Per-reward independent group-wise normalization before aggregation prevents advantage collapse when combining multiple rewards in GRPO.\n\n2. **DRA-GRPO** -- \"DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of LLMs\"\n   - Authors: Xiwen Chen et al. | 2025 | arXiv 2505.09655\n   - Role: related_method\n   - Summary: Uses submodular mutual information to reweight rewards, giving higher weight to diverse completions to prevent policy collapse to prior modes.\n\n3. **Shrinkage Baselines** -- \"Shrinking the Variance: Shrinkage Baselines for RL with Verifiable Rewards\"\n   - Authors: Guanning Zeng et al. | 2025 | arXiv 2511.03710\n   - Role: theoretical_support\n   - Summary: James-Stein shrinkage mixing per-prompt and cross-prompt mean baselines yields provably lower-variance policy gradient estimators in RLVR.\n\n4. **Reward Shaping** -- \"Reward Shaping to Mitigate Reward Hacking in RLHF\"\n   - Authors: Anonymous | 2025 | arXiv 2502.18770\n   - Role: background\n   - Summary: Systematically studies reward shaping principles; bounded rewards with fast-then-slow growth suppress reward hacking and improve training stability.\n\n---\n\n## Category 2: mode_collapse_prevention (6 papers)\n\n5. **DAPO** -- \"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\"\n   - Authors: ByteDance Seed, Tsinghua AIR | 2025 | NeurIPS 2025\n   - Role: key_baseline\n   - Summary: Addresses GRPO entropy collapse via Clip-Higher (asymmetric clipping) and Dynamic Sampling that filters zero-gradient prompts; achieves 50 on AIME 2024.\n\n6. **Dr. GRPO** -- \"Dr. GRPO: Removing Optimization Bias in GRPO\"\n   - Authors: Liu et al. | 2025 | COLM 2025\n   - Role: related_analysis\n   - Summary: Identifies difficulty bias and length bias from GRPO's std normalization; proposes unbiased Monte Carlo advantage by removing std normalization.\n\n7. **GVPO** -- \"GVPO: Group Variance Policy Optimization for LLM Post-Training\"\n   - Authors: Anonymous | 2025 | NeurIPS 2025\n   - Role: alternative_framework\n   - Summary: Embeds the analytic solution of KL-constrained reward maximization into gradient weights; variance term naturally balances exploration and exploitation.\n\n8. **REINFORCE++** -- \"REINFORCE++: Stabilizing Critic-Free Policy Optimization with Global Advantage Normalization\"\n   - Authors: Jian Hu et al. | 2025 | arXiv 2501.03262\n   - Role: related_method\n   - Summary: Global batch normalization for advantage estimation provides a more stable, theoretically unbiased gradient estimator than local prompt-level normalization.\n\n9. **DiverseGRPO** -- \"DiverseGRPO: Mitigating Mode Collapse in Image Generation via Diversity-Aware GRPO\"\n   - Authors: Henglin Liu et al. | 2025 | arXiv 2512.21514\n   - Role: parallel_work\n   - Summary: Addresses GRPO output homogenization in image generation via distributional reward modeling (spectral clustering + exploratory reward), achieving 13-18% semantic diversity gain.\n\n10. **GRPO Normalization Theory** -- \"Why GRPO Needs Normalization: A Local-Curvature Perspective on Adaptive Gradients\"\n    - Authors: Anonymous | 2025 | arXiv 2601.23135\n    - Role: theoretical_support\n    - Summary: Proves GRPO's reward_std normalization provides strictly better convergence rates than unnormalized REINFORCE; benefit characterized by average inter-prompt reward std.\n\n---\n\n## Category 3: contrastive_reward (3 papers)\n\n11. **Contrastive Rewards for RLHF** -- \"Improving Reinforcement Learning from Human Feedback Using Contrastive Rewards\"\n    - Authors: Shen, Zhang et al. | 2024 | arXiv 2403.07708\n    - Role: closest_contrastive_precedent\n    - Summary: Offline-sampled baseline responses compute contrastive reward as PPO penalty; penalizes reward uncertainty, adaptively calibrates by task difficulty, reduces variance.\n\n12. **Contrastive RM Training** -- \"Improving Discriminative Capability of Reward Models in RLHF Using Contrastive Learning\"\n    - Authors: Anonymous | 2024 | EMNLP 2024\n    - Role: related_method\n    - Summary: Unsupervised contrastive loss trains reward models to better capture discriminative features, leading to more stable PPO training returns.\n\n13. **CPL** -- \"Contrastive Preference Learning: Learning from Human Feedback without RL\"\n    - Authors: Anonymous | 2024 | ICLR 2025\n    - Role: background\n    - Summary: Reformulates preference learning as contrastive learning, enabling learning from human feedback without explicit RL.\n\n---\n\n## Category 4: evidence_reward (3 papers)\n\n14. **Drift** -- \"Drift: Enhancing LLM Faithfulness in Rationale Generation\"\n    - Authors: Anonymous | 2025 | ACL 2025\n    - Role: related_method\n    - Summary: Uses faithfulness reward to guide LLMs toward more reliable rationale generation, improving factual consistency of CoT reasoning.\n\n15. **INFUSE** -- \"Fine-Grained NLI-Based Faithfulness Evaluation for Diverse Summarisation Tasks\"\n    - Authors: Anonymous | 2024 | EACL 2024\n    - Role: background\n    - Summary: Variable-length premise + simplified hypothesis for fine-grained NLI faithfulness evaluation, surpassing traditional NLI on multi-task summarization.\n\n16. **Cross-Evidence Reasoning Graph** -- \"Enhancing Cross-Evidence Reasoning Graph for Document-Level Relation Extraction\"\n    - Authors: Anonymous | 2024 | PMC/Bioinformatics 2024\n    - Role: background\n    - Summary: Uses cross-evidence reasoning graph to enhance cross-evidence reasoning in document-level relation extraction.\n\n---\n\n## Category 5: multi_objective_rl (2 papers)\n\n17. **Constrained RLHF** -- \"Confronting Reward Model Overoptimization with Constrained RLHF\"\n    - Authors: Anonymous | 2025 | OpenReview\n    - Role: related_analysis\n    - Summary: Studies overoptimization in multi-component reward models; inter-component correlation significantly affects the overoptimization threshold; uses constrained MDP.\n\n18. **Optimal Reward Baseline** -- \"On-Policy RL with Optimal Reward Baseline\"\n    - Authors: Anonymous | 2025 | arXiv 2505.23585\n    - Role: theoretical_support\n    - Summary: Optimal baseline consistently achieves higher training reward and higher entropy, stabilizing training and promoting more diverse policy exploration.\n\n---\n\n## Category 6: rsft_methodology (5 papers)\n\n19. **Minimalist RSFT** -- \"A Minimalist Approach to LLM Reasoning: from Rejection Sampling to Reinforce\"\n    - Authors: Xiao et al. | 2025 | arXiv 2504.11343\n    - Role: key_theoretical_support\n    - Summary: RAFT (simple rejection sampling) matches GRPO/PPO on math reasoning; GRPO's main advantage comes from discarding all-wrong prompts, not reward normalization.\n\n20. **TrajFusion** -- \"Beyond Rejection Sampling: Trajectory Fusion for Scaling Mathematical Reasoning\"\n    - Authors: Jie Deng et al. | 2026 | arXiv 2602.04391\n    - Role: method_component\n    - Summary: Interleaves failed and correct trajectories to explicitly model trial-and-error reasoning, significantly outperforming standard RFT on hard math problems.\n\n21. **RSFT = PPO** -- \"Rejection Sampling Based Fine Tuning Secretly Performs PPO\"\n    - Authors: Anonymous | 2025 | ICML 2025\n    - Role: theoretical_support\n    - Summary: Establishes theoretical link between RSFT and PPO: rejection sampling fine-tuning implicitly performs PPO with marginal KL constraints under certain conditions.\n\n22. **AdaSTaR** -- \"AdaSTaR: Adaptive Data Sampling for Training Self-Taught Reasoners\"\n    - Authors: Hyung Won Chung et al. | 2025 | NeurIPS 2025\n    - Role: related_method\n    - Summary: Introduces diversity sampling + curriculum sampling for RFT/RSFT to address training imbalance; achieves SOTA on 6 benchmarks with 58.6% fewer training FLOPs.\n\n23. **RIFT** -- \"RIFT: Repurposing Negative Samples via Reward-Informed Fine-Tuning\"\n    - Authors: Unknown | 2026 | arXiv 2601.09253\n    - Role: direct_competitor\n    - Summary: Instead of hard rejection, reweights all trajectories by scalar reward; positive samples encourage correct behavior, negative samples provide reverse gradients.\n\n---\n\n## Category 7: rl_for_ie (6 papers)\n\n24. **R1-RE** -- \"R1-RE: Cross-Domain Relation Extraction with RLVR\"\n    - Authors: Runpeng Dai, Tong Zheng et al. | 2025 | arXiv 2507.04642\n    - Role: direct_competitor\n    - Summary: First RLVR (GRPO + verifiable reward) framework for relation extraction; R1-RE-7B achieves ~70% cross-domain OOD accuracy, matching GPT-4o on sentence-level RE.\n\n25. **MORE-R1** -- \"MORE-R1: Guiding LVLM for Multimodal Object-Entity Relation Extraction via Stepwise Reasoning with RL\"\n    - Authors: Anonymous | 2026 | arXiv 2603.09478\n    - Role: related_method\n    - Summary: Uses GRPO + Progressive Sample-Mixing Strategy to optimize LVLM reasoning for multimodal RE.\n\n26. **REAR** -- \"REAR: Reinforced Reasoning Optimization for Event Argument Extraction with Relation-Aware Support\"\n    - Authors: Jianwen Luo et al. | 2025 | EMNLP 2025 Findings\n    - Role: related_method\n    - Summary: Applies RL reasoning optimization to event argument extraction with relation-aware support.\n\n27. **Adaptive RL Planning for IE** -- \"Adaptive Reinforcement Learning Planning: Harnessing LLMs for Complex Information Extraction\"\n    - Authors: Zepeng Ding et al. | 2024 | arXiv 2406.11455\n    - Role: background\n    - Summary: Models LLM sequential extraction as MDP, trains DDQN decision module to adaptively select entity extraction order for complex IE.\n\n28. **Graph-R1** -- \"Graph-R1: Towards Agentic GraphRAG Framework via End-to-end Reinforcement Learning\"\n    - Authors: Haoran Luo et al. | 2025 | ICML 2026\n    - Role: background\n    - Summary: End-to-end RL optimizes GraphRAG agent's multi-round retrieval-reasoning loop including knowledge hypergraph construction.\n\n29. **R2GRPO** -- \"R2GRPO: Better LLMs for Scientific Information Extraction with MimicSFT and Relevance and Rule-induced GRPO\"\n    - Authors: Li, Di, Liu, Jing, Qiu, Chen | 2025 | arXiv 2505.22068\n    - Role: related_method\n    - Summary: Two-stage MimicSFT + R2GRPO (relevance reward + rule-mining reward) surpasses baseline LLMs and specialized models on scientific IE RE benchmarks.\n\n---\n\n## Category 8: llm_docre (6 papers)\n\n30. **RelPrior** -- \"RelPrior: Relation as a Prior - A Novel Paradigm for LLM-based Document-level Relation Extraction\"\n    - Authors: Anonymous | 2025 | arXiv 2511.08143\n    - Role: key_baseline\n    - Summary: Uses binary relation as prior to filter irrelevant entity pairs, then matches predefined relations; LLaMA3-8B achieves DocRED test F1=48.34, Re-DocRED test F1=54.80.\n\n31. **LMRC** -- \"LMRC: LLM with Relation Classifier for Document-Level Relation Extraction\"\n    - Authors: Xingzuo Li, Kehai Chen, Yunfei Long, Min Zhang | 2024 | arXiv 2408.13889\n    - Role: related_method\n    - Summary: Two-stage: BERT attention-based classifier filters NA entity pairs, then LLM does multi-class classification; DocRED test F1=60.52, Re-DocRED test F1=74.63 (hybrid method).\n\n32. **Ru-LLM** -- \"Ru-LLM: Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction\"\n    - Authors: Anonymous | 2025 | NLPCC 2025\n    - Role: related_method\n    - Summary: Mines frequent pattern logical rules via MCTS, converts to prompt constraints on LLM output, then CoT-verifies rule satisfaction.\n\n33. **GLiDRE** -- \"GLiDRE: Generalist Lightweight model for Document-level Relation Extraction\"\n    - Authors: Anonymous | 2025 | arXiv 2508.00757\n    - Role: background\n    - Summary: Dual-encoder lightweight zero/few-shot DocRE model pretrained on 136K documents; fully supervised Re-DocRED test F1=77.83 (encoder-based, not LLM generative).\n\n34. **AutoRE** -- \"AutoRE: Document-Level Relation Extraction with Large Language Models\"\n    - Authors: Anonymous | 2024 | arXiv 2403.14888\n    - Role: background\n    - Summary: RHF (Relation-Head-Facts) paradigm using Mistral-7B + QLoRA for end-to-end DocRE; Re-DocRED test F1=51.91 (Mistral), 51.97 (LLaMA3-8B).\n\n35. **DocKS-RAG** -- \"DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning\"\n    - Authors: Xu et al. | 2025 | ICML 2025\n    - Role: direct_competitor\n    - Summary: Builds document-level knowledge graph for structural info + sentence-level semantic RAG for context; hybrid-prompt tuning integrates both into LLM.\n\n---\n\n## Category 9: evidence_generation_tradeoff (4 papers)\n\n36. **Mind Your Step** -- \"Mind Your Step (by Step): Chain-of-Thought can Reduce Performance on Tasks where Thinking Makes Humans Worse\"\n    - Authors: Sprague et al. | 2024 | NeurIPS 2024\n    - Role: key_evidence\n    - Summary: CoT reduces performance by up to 36.3% on certain tasks; explicit reasoning steps introduce error accumulation; implicit reasoning outperforms under distribution shift.\n\n37. **EIDER** -- \"Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion\"\n    - Authors: Xie et al. (Google Research) | 2022 | ACL Findings 2022\n    - Role: closest_docre_precedent\n    - Summary: Joint RE + evidence extraction with inference-stage fusion: separate RE predictions on extracted evidence and full document, blended via fusion layer; +1.37 Ign F1 on DocRED.\n\n38. **Performance-Explanation Trade-off** -- \"Exploring the Trade-off Between Model Performance and Explanation Plausibility of Text Classifiers Using Human Rationales\"\n    - Authors: Resck, Raimundo, Poco | 2024 | NAACL Findings 2024\n    - Role: formal_framework\n    - Summary: Multi-objective optimization exploring the Pareto frontier of performance vs. explanation plausibility; confirms rationale supervision reduces main task performance.\n\n39. **Decreasing Value of CoT** -- \"The Decreasing Value of Chain of Thought in Prompting\"\n    - Authors: Meincke, Mollick, Mollick, Shapiro | 2025 | Wharton Technical Report (SSRN)\n    - Role: empirical_support\n    - Summary: On modern reasoning models, CoT benefit is marginal (4-13%) but latency increases 35-600%; stronger models benefit less from explicit reasoning.\n\n---\n\n## Category 10: negative_transfer (1 paper)\n\n40. **ForkMerge** -- \"ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning\"\n    - Authors: Jiang, Chen et al. | 2023 | NeurIPS 2023\n    - Role: theoretical_framework\n    - Summary: Auxiliary tasks cause negative transfer from both gradient conflict and auxiliary-target generalization gap; periodic fork-and-merge with dynamic task weight search filters harmful updates.\n\n---\n\n## Category 11: faithfulness_accuracy_tradeoff (3 papers)\n\n41. **Correctness != Faithfulness** -- \"Correctness is not Faithfulness in RAG Attributions\"\n    - Authors: Wallat, Heuss, de Rijke, Anand | 2024 | SIGIR 2025\n    - Role: key_conceptual_framework\n    - Summary: Correctness and faithfulness are independent dimensions that can conflict; up to 57% of citations are post-rationalized rather than genuine bases for answers.\n\n42. **Evaluating Correctness & Faithfulness** -- \"Evaluating Correctness and Faithfulness of Instruction-Following Models for Question Answering\"\n    - Authors: Adlakha, BehnamGhader, Lu, Meade, Reddy | 2024 | TACL 2024\n    - Role: evaluation_framework\n    - Summary: Instruction-following LLMs match fine-tuned models on correctness but are consistently poor on faithfulness -- they hallucinate rather than ground in provided evidence.\n\n43. **Faithful Explanation Survey** -- \"Towards Faithful Model Explanation in NLP: A Survey\"\n    - Authors: Lyu, Havaldar, Stein et al. | 2024 | Computational Linguistics (MIT Press)\n    - Role: comprehensive_survey\n    - Summary: Comprehensive survey of faithful explanation in NLP; identifies faithfulness-performance trade-off as core challenge; recommends multi-objective optimization and post-hoc verification.\n\n---\n\n## Category 12: reranking_verification_bridge (1 paper)\n\n44. **Genie** -- \"Genie: Achieving Human Parity in Content-Grounded Datasets Generation\"\n    - Authors: Yehudai, Carmeli, Mass et al. | 2024 | ICLR 2024\n    - Role: methodological_precedent\n    - Summary: Three-stage pipeline (Content Preparation, Generation, NLI-based Filtering) using fine-tuned T5-11B NLI to filter unfaithful generation; achieves human parity on LFQA/summarization/IE.\n\n---\n\n## Category 13: evidence_grounded_rl (1 paper)\n\n45. **EvidenceRL** -- \"EvidenceRL: Reinforcing Evidence Consistency for Trustworthy Language Models\"\n    - Authors: Ben Tamo, Lu, Marteau, Nnamdi, Wang | 2026 | arXiv 2603.19532\n    - Role: closest_competitor\n    - Summary: Uses GRPO to jointly optimize grounding (evidence entailment) and correctness; cardiac diagnosis F1@3 37.0->54.5, grounding 47.6->78.2, hallucination reduced 5x.\n\n---\n\n## Category 14: multi_objective_grpo (2 papers)\n\n46. **MO-GRPO** -- \"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems\"\n    - Authors: Ichihara, Jinnai, Morimura, Sakamoto, Mitsuhashi, Uchibe | 2025 | arXiv 2509.22047\n    - Role: related_method\n    - Summary: GRPO under multi-objective settings easily reward-hacks one objective at the cost of others; variance-based normalization auto-balances multiple reward functions.\n\n47. **RDPO** -- \"Multi-Objective and Mixed-Reward Reinforcement Learning via Reward-Decorrelated Policy Optimization\"\n    - Authors: Bai, Liu, Zhuang, Zhou, Weng, Chen, Wang, Cai | 2026 | arXiv 2605.13641\n    - Role: related_method\n    - Summary: Direct summation + normalization of mixed rewards drowns out weak signal dimensions; Mahalanobis whitening + magnitude-aware quantile normalization decorrelate reward subspaces.\n\n---\n\n## Category 15: grpo_theory (2 papers)\n\n48. **GRPO = PRM** -- \"GRPO is Secretly a Process Reward Model\"\n    - Authors: Sullivan, Koller | 2025 | under review at ICML 2026\n    - Role: theoretical_insight\n    - Summary: Proves GRPO + ORM is equivalent to a PRM-aware RL objective under certain conditions; proposes lambda-GRPO correcting deficiency on uneven process steps.\n\n49. **Reward Hacking Survey** -- \"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges\"\n    - Authors: Wang et al. (23 authors) | 2026 | arXiv 2604.13602\n    - Role: theoretical_framework\n    - Summary: Proposes Proxy Compression Hypothesis (PCH): reward hacking stems from objective compression, optimization amplification, and evaluator-policy co-adaptation interaction.\n\n---\n\n## Category 16: training_precision_rl (1 paper)\n\n50. **FP16 for RL** -- \"Defeating the Training-Inference Mismatch via FP16\"\n    - Authors: Qi, Liu, Zhou, Pang, Du, Lee, Lin | 2025 | arXiv 2510.26788\n    - Role: key_evidence\n    - Summary: BF16 introduces large rounding errors in RL fine-tuning causing training-inference mismatch; BF16 training collapses at 150-600 steps; switching to FP16 eliminates the issue.\n\n---\n\n## Category 17: llm_ie_alignment (1 paper)\n\n51. **ADELIE** -- \"ADELIE: Aligning Large Language Models on Information Extraction\"\n    - Authors: Qi, Peng, Wang, Xu, Hou, Li | 2024 | EMNLP 2024\n    - Role: key_baseline\n    - Summary: Builds IEInstruct high-quality IE alignment corpus; trains with SFT + DPO; supports closed/open/on-demand IE modes; SOTA on multiple held-out IE datasets.\n\n---\n\n## Category 18: unfaithful_reasoning (2 papers)\n\n52. **CoT != Explainability** -- \"Chain-of-Thought Is Not Explainability\"\n    - Authors: Barez et al. | 2025 | Oxford WhiteBox Technical Report\n    - Role: conceptual_support\n    - Summary: CoT merely rationalizes (post-hoc) rather than faithfully reports the model's actual decision process; small manipulations change CoT chains without affecting decisions.\n\n53. **LLMs as Rationalizers** -- \"Characterizing Large Language Models as Rationalizers of Knowledge-Grounded Dialogue\"\n    - Authors: Anonymous | 2024 | ACL Findings 2024\n    - Role: empirical_evidence\n    - Summary: LLMs in knowledge-grounded dialogue consistently act as rationalizers not faithful reasoners; their explanations are inconsistent with the knowledge evidence they actually use.\n\n---\n\n## Category 19: latent_vs_explicit_reasoning (1 paper)\n\n54. **Latent CoT Survey** -- \"Reasoning Beyond Language: A Comprehensive Survey on Latent Chain-of-Thought Reasoning\"\n    - Authors: Chen, Zhao, Xia, Lu, Wang, Chen, Zhang, Wang, Li, Shen | 2025 | arXiv 2505.16782\n    - Role: survey\n    - Summary: Latent CoT decouples reasoning from explicit token generation to hidden state computation; matches or exceeds explicit CoT performance with 20x+ inference speedup.\n\n---\n\n## Category 20: evidence_based_docre (6 papers)\n\n55. **DREEAM** -- \"DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction\"\n    - Authors: Youmi Ma, An Wang, Naoaki Okazaki | 2023 | EACL 2023\n    - Role: direct-competitor\n    - Summary: Uses evidence as supervision signal to guide DocRE attention modules; proposes evidence retrieval self-training for silver evidence generation at scale; SOTA on DocRED.\n\n56. **DocGNRE** -- \"DocGNRE: Semi-automatic Data Enhancement for Document-Level Relation Extraction with Distant Supervision from Large Language Models\"\n    - Authors: Junpeng Li, Zixia Jia, Zilong Zheng | 2023 | EMNLP 2023\n    - Role: method-component\n    - Summary: Uses LLM (ChatGPT) + NLI module to semi-automatically generate relation triples for DocRE data augmentation, especially for long-tail relation types.\n\n57. **CDER** -- \"CDER: Collaborative Evidence Retrieval for Document-level Relation Extraction\"\n    - Authors: Khai Phan Tran, Xue Li | 2025 | arXiv 2504.06529\n    - Role: direct-competitor\n    - Summary: Attentional graph-based architecture capturing collaborative patterns among semantically similar entity pairs within documents via bipartite graph with three subgraphs.\n\n58. **Evidence-aware DocRE** -- \"Evidence-aware Document-level Relation Extraction\"\n    - Authors: Xu T, Hua W, Qu J, Li Z, Xu J, Liu A et al. | 2022 | CIKM 2022\n    - Role: background\n    - Summary: Models evidence sentence selection as a sequential decision problem using RL mechanism to select supporting evidence sentences for relations.\n\n59. **COREX** -- \"COREX: Document-level Relation Extraction Framework with Consistent Two-Hop Reasoning and Evidence Sentence Prediction\"\n    - Authors: Unknown | 2024 | IEEE IJCNN 2024\n    - Role: direct_competitor\n    - Summary: Efficient two-hop reasoning representation jointly supervised by evidence prediction and RE; modified Adaptive Focal Loss for class imbalance; Weighted Fusion Layer for evidence.\n\n60. **Grounded KG Extraction** -- \"Grounded Knowledge Graph Extraction via LLMs: An Anchor-Constrained Framework with Provenance Tracking\"\n    - Authors: Unknown | 2025 | Computers 2025\n    - Role: related_method\n    - Summary: AEVS framework (anchor discovery, grounded extraction, verification, supplement) providing character-level provenance for each triple; hallucination rate 0.23-20.23%.\n\n---\n\n## Category 21: faithfulness_cost (3 papers)\n\n61. **Faithfulness vs Plausibility (Empirical)** -- \"Does Faithfulness Conflict with Plausibility? An Empirical Study in Explainable AI across NLP Tasks\"\n    - Authors: Xiaolei Lu, Jianghong Ma | 2024 | arXiv 2404.00140\n    - Role: evaluation\n    - Summary: Systematically compares faithfulness and plausibility across sentiment analysis, intent detection, topic labeling; finds they need not conflict and can be jointly optimized.\n\n62. **Faithfulness vs Plausibility (LLM)** -- \"Faithfulness vs. Plausibility: On the (Un)Reliability of Explanations from Large Language Models\"\n    - Authors: Anonymous | 2024 | arXiv 2402.04614\n    - Role: key_evidence\n    - Summary: LLMs generate plausible but not necessarily faithful explanations; self-explanations behave more like post-hoc rationalization than true reasoning reports.\n\n63. **Unlearning CoT Faithfulness** -- \"Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps\"\n    - Authors: Anonymous | 2025 | EMNLP 2025\n    - Role: evaluation\n    - Summary: Measures CoT faithfulness by unlearning individual reasoning steps; if model behavior is unchanged after unlearning, the step was not faithful.\n\n---\n\n## Category 22: lora_qlora_artifacts (6 papers)\n\n64. **LoRA vs FFT** -- \"LoRA vs Full Fine-tuning: An Illusion of Equivalence\"\n    - Authors: Reece Shuttleworth, Jacob Andreas, Antonio Torralba, Pratyusha Sharma | 2024 | arXiv 2410.21228\n    - Role: key_evidence\n    - Summary: LoRA and full fine-tuning produce structurally different weight matrices; LoRA introduces \"intruder dimensions\" (new high-rank singular vectors); forgetting concentrates in these dimensions.\n\n65. **LoRA Cluster Impact** -- \"The Impact of LoRA on the Emergence of Clusters in Transformers\"\n    - Authors: Hugo Koubbi, Louis Hernandez, Matthieu Boussard | 2024 | arXiv 2402.15415\n    - Role: theoretical_support\n    - Summary: Mean-field self-attention toy model reveals phase transition in LoRA forgetting behavior depending on perturbation norm and Transformer depth.\n\n66. **QeRL** -- \"QeRL: Beyond Efficiency -- Quantization-enhanced Reinforcement Learning for LLMs\"\n    - Authors: NVIDIA, MIT, HKU, THU | 2025 | arXiv 2510.11696\n    - Role: direct-competitor\n    - Summary: Standard quantization introduces static deterministic noise harmful to RL; Adaptive Quantization Noise (AQN) dynamically adjusts noise to promote exploration; enables 32B RL on single H100.\n\n67. **Quantization Impact on RL** -- \"The Impact of Quantization on Large Reasoning Model Reinforcement Learning\"\n    - Authors: Anonymous | 2025 | NeurIPS 2025 Workshop (Efficient Reasoning)\n    - Role: key_evidence\n    - Summary: Quantization-aware RL training actually harms the learning process; PTQ and QLoRA perform better; significant gap between post-RL quantized and quantization-aware RL models.\n\n68. **Q-BLoRA** -- \"Accurate and Efficient Fine-Tuning of Quantized Large Language Models Through Optimal Balance in Adaptation\"\n    - Authors: Shinhyuk Seo et al. | 2024 | TACL 2025\n    - Role: related_analysis\n    - Summary: Identifies imbalance in quantized LLM + LoRA: overly complex adapter I/O with insufficient effective trainability causes underfitting; Q-BLoRA simplifies I/O while increasing rank.\n\n69. **CLoQ** -- \"CLoQ: Enhancing Fine-Tuning of Quantized LLMs via Calibrated LoRA Initialization\"\n    - Authors: Unknown | 2025 | arXiv 2501.18475\n    - Role: related_method\n    - Summary: Quantization errors affect LoRA training; closed-form optimal LoRA initialization by minimizing per-layer difference between original and quantized+LoRA models on calibration data.\n\n---\n\n## Category 23: grpo_nlp_applications (2 papers)\n\n70. **ReasoningNER** -- \"ReasoningNER: A Reasoning Paradigm for Named Entity Recognition\"\n    - Authors: Anonymous | 2025 | arXiv 2511.11978\n    - Role: direct-competitor\n    - Summary: Three-stage NER framework (CoT Generation, CoT Tuning, GRPO Reasoning Enhancement) with composite reward; 8B model beats GPT-4 by 12.3 F1 on zero-shot NER.\n\n71. **Posterior-GRPO** -- \"Posterior-GRPO: Rewarding Reasoning Processes in Code Generation\"\n    - Authors: Anonymous | 2025 | arXiv 2508.05170\n    - Role: method-component\n    - Summary: Applies process-based reward only to successful outputs' reasoning processes; prevents reward hacking via incorrect reasoning that accidentally produces correct code.\n\n---\n\n## Category 24: rsft_offline_rl (4 papers)\n\n72. **OREO** -- \"OREO: Offline Reinforcement Learning for LLM Multi-Step Reasoning\"\n    - Authors: Anonymous | 2024 | arXiv 2412.16145\n    - Role: direct-competitor\n    - Summary: Maximum entropy RL offline method jointly learning policy and value function via soft Bellman Equation; better credit assignment without paired preference data; beats existing offline methods on GSM8K/MATH.\n\n73. **PCL-Reasoner** -- \"PCL-Reasoner-V1.5: Advancing Math Reasoning with Offline Reinforcement Learning\"\n    - Authors: Yao Lu, Dengdong Fan, Jianzheng Nie, Fan Xu, Jie Chen, Bin Zhou, Yonghong Tian | 2026 | arXiv 2601.14716\n    - Role: key_evidence\n    - Summary: Qwen2.5-32B-based math reasoning model using offline RL that surpasses GRPO and other online RL in training stability and efficiency; AIME 2024 avg 90.9%.\n\n74. **RS-DPO** -- \"RS-DPO: A Hybrid Rejection Sampling and Direct Preference Optimization Method for Alignment of Large Language Models\"\n    - Authors: Anonymous | 2024 | NAACL 2024 Findings\n    - Role: method-component\n    - Summary: Systematically combines rejection sampling and DPO; samples k responses per prompt, identifies contrastive pairs from reward distribution, then applies DPO alignment.\n\n75. **RAFT** -- \"RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment\"\n    - Authors: Anonymous | 2024 | TMLR 2024\n    - Role: background\n    - Summary: Canonical RSFT framework: iterative generate, rank, filter, SFT; generates n responses, ranks by reward model, takes top-k for SFT. Validated on text generation and dialogue.\n\n---\n\n## Category 25: evidence_docre (3 papers)\n\n76. **EAAGRE** -- \"EAAGRE: Evidence and Axial Attention Guided Document-level Relation Extraction\"\n    - Authors: Unknown (Computer Speech and Language) | 2024 | Computer Speech and Language 2024\n    - Role: related_method\n    - Summary: Guides PLM encoder's top-k token attention to evidence sentences without extra trainable parameters; axial attention models global interdependence among relation triples.\n\n77. **GEGA** -- \"GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction\"\n    - Authors: Yanxu Mao et al. | 2024 | arXiv 2407.21384\n    - Role: related_method\n    - Summary: GCN with multi-weight matrices guides attention to evidence sentences; Teacher-Student framework distills evidence weights from full supervision to student model.\n\n78. **KnowRA** -- \"KnowRA: Knowledge Retrieval Augmented Method for Document-level Relation Extraction with Comprehensive Reasoning Abilities\"\n    - Authors: Chengcheng Mai et al. | 2025 | IJCAI 2025\n    - Role: related_method\n    - Summary: External knowledge retrieval augments DocRE reasoning via document knowledge graph construction with coreference enhancement and knowledge filtering; axial attention for cross-sentence reasoning.\n\n---\n\n## Category 26: faithfulness_structured (4 papers)\n\n79. **G&O** -- \"G&O: A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction\"\n    - Authors: Yinghao Li et al. | 2024 | arXiv 2402.13364\n    - Role: related_method\n    - Summary: Decomposes structured IE into two steps: generate content in natural language first, then organize into target structure; separates content generation from structuring.\n\n80. **Evidence Extraction Metrics** -- \"Improved Evidence Extraction and Metrics for Document Inconsistency Detection with LLMs\"\n    - Authors: Nelvin Tan et al. | 2026 | arXiv 2601.02627\n    - Role: related_method\n    - Summary: Introduces new evidence extraction evaluation metrics and redact-and-retry framework; constrained filtering significantly outperforms direct prompting for evidence extraction.\n\n81. **Structural Failures in Evidence Extraction** -- \"Diagnosing Structural Failures in LLM-Based Evidence Extraction for Meta-Analysis\"\n    - Authors: Unknown | 2026 | arXiv 2602.10881\n    - Role: supporting_evidence\n    - Summary: LLMs exhibit systematic structural breakdowns in evidence extraction: role reversal, cross-analysis binding drift, instance compression, numeric misattribution.\n\n82. **APIE** -- \"Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion\"\n    - Authors: Unknown | 2025 | AAAI 2026\n    - Role: related_method\n    - Summary: Dual-component uncertainty metric quantifying Format Uncertainty (structural syntax difficulty) and Content Uncertainty (semantic inconsistency) in LLM-based IE.\n\n---\n\n## Category 27: grpo_structured (4 papers)\n\n83. **GRPO-LEAD** -- \"GRPO-LEAD: A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models\"\n    - Authors: Jixiao Zhang, Chunsheng Zuo | 2025 | EMNLP 2025\n    - Role: related_method\n    - Summary: Enhanced GRPO with length-regularized rewards, explicit error penalties, and difficulty-aware advantage reweighting for math reasoning.\n\n84. **E-GRPO** -- \"E-GRPO: Entity-Aware Reward for Group Relative Policy Optimization\"\n    - Authors: Unknown | 2025 | ICLR 2026\n    - Role: closest_prior_work\n    - Summary: Entity-aware reward function giving partial credit to negative samples based on entity match rate; uses ground-truth entities as factual correctness proxy to distinguish near-misses.\n\n85. **RL vs SFT** -- \"RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs\"\n    - Authors: Hangzhan Jin et al. | 2025 | arXiv 2508.16546\n    - Role: supporting_evidence\n    - Summary: RL-FT recovers most OOD performance lost by SFT, but cannot fully recover when SFT causes severe overfitting; recovery tied to singular vector direction rotation.\n\n86. **Multi-objective RL for EE** -- \"Aligning Instruction-Tuned LLMs for Event Extraction with Multi-objective Reinforcement Learning\"\n    - Authors: Unknown | 2025 | Springer 2025\n    - Role: related_method\n    - Summary: Applies multi-objective RL to event extraction on instruction-tuned LLMs, improving structured output quality.\n\n---\n\n## Category 28: qlora_fft_gap (2 papers)\n\n87. **LoRA Rank Trade-offs** -- \"How Much is Too Much? Exploring LoRA Rank Trade-offs for Retaining Knowledge and Domain Robustness\"\n    - Authors: Darshita Rathore et al. | 2025 | IJCNLP-AACL 2025\n    - Role: supporting_evidence\n    - Summary: Medium rank (r=32-64) achieves optimal balance between representation capacity and stability; LoRA-tuned models show robust generalization via transferable abstract skills.\n\n88. **RandLoRA** -- \"RandLoRA: Full-rank Parameter-Efficient Fine-tuning of Large Models\"\n    - Authors: Paul Albert et al. | 2025 | ICLR 2025\n    - Role: related_method\n    - Summary: Learns diagonal scaling of fixed random matrices to achieve full-rank updates while maintaining parameter efficiency; eliminates LoRA-FFT performance gap on vision-language tasks.\n\n---\n\n## Category 29: mtl_ie_tradeoff (3 papers)\n\n89. **C-LoRAE** -- \"C-LoRAE: Collaborative Multi-LoRA Experts with Achievement-based Multi-Tasks Loss for Unified Multimodal Information Extraction\"\n    - Authors: Unknown | 2025 | arXiv 2505.06303\n    - Role: closest_prior_work\n    - Summary: Extends LoRA with universal expert (cross-task shared) + task-specific experts; mutual information maximization promotes inter-expert exchange; achievement-based loss dynamically balances task progress.\n\n90. **Ortho-LoRA** -- \"Ortho-LoRA: Disentangling Task Conflicts in Multi-Task LoRA via Orthogonal Gradient Projection\"\n    - Authors: Ziyu Yang et al. | 2026 | arXiv 2601.09684\n    - Role: related_method\n    - Summary: Dynamically projects conflicting task gradients onto each other's orthogonal complement within LoRA's intrinsic subspace to resolve multi-task gradient conflicts.\n\n91. **Sparse Training for MTL** -- \"Proactive Gradient Conflict Mitigation in Multi-Task Learning: A Sparse Training Perspective\"\n    - Authors: Zhi Zhang et al. | 2024 | arXiv 2411.18615\n    - Role: supporting_evidence\n    - Summary: Selects subset of original model parameters for multi-task learning, freezing the rest; reduces high-dimensional optimization to lower-dimensional problem limiting each task's gradient influence range.\n\n---\n\n## Category 30: survey (1 paper)\n\n92. **Generative IE Survey** -- \"Large Language Models for Generative Information Extraction: A Survey\"\n    - Authors: Unknown | 2024 | Frontiers of Computer Science 2024\n    - Role: survey\n    - Summary: Comprehensive survey of LLMs in IE subtasks (NER, RE, EE, etc.); categorizes by subtask and technique; identifies structured output quality and efficiency as key challenges.\n\n---\n\n## Category 31: inference_time_reranking (5 papers)\n\n93. **Best-of-N Optimality** -- \"Is Best-of-N the Best of Them? Coverage, Scaling, and Optimality in Inference-Time Alignment\"\n    - Authors: Audrey Huang et al. | 2025 | ICML 2025\n    - Role: key_baseline\n    - Summary: BoN provably suffers from reward hacking at large N; proposes InferenceTimePessimism for scaling-monotonic performance; pre-trained policy coverage is key to BoN success.\n\n94. **Inference-Time Reward Hacking** -- \"Inference-Time Reward Hacking in Large Language Models\"\n    - Authors: Yiwei Chen et al. | 2025 | NeurIPS 2025 Spotlight\n    - Role: related_analysis\n    - Summary: Proves true reward first rises then falls (hacking pattern) is inherent to all inference-time mechanisms; proposes Best-of-Poisson (BoP) and HedgeTune for optimal reward-KL tradeoff.\n\n95. **Inference-Aware Fine-Tuning** -- \"Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models\"\n    - Authors: Yinlam Chow et al. | 2024 | ICLR 2025\n    - Role: method_component\n    - Summary: Trains model to directly optimize BoN inference performance; imitation learning and RL overcome non-differentiable argmax; model learns exploration-exploitation meta-strategy.\n\n96. **BoN Evaluation** -- \"Evaluation of Best-of-N Sampling Strategies for Language Model Alignment\"\n    - Authors: Yuki Ichihara et al. | 2025 | TMLR 2025\n    - Role: evaluation\n    - Summary: Systematic BoN reward hacking evaluation; proposes Stochastic Regularized BoN (SRBoN) with theoretical guarantees; simple sentence-length regularized BoN achieves comparable performance.\n\n97. **MBR-BoN** -- \"Regularized Best-of-N Sampling with Minimum Bayes Risk Objective for Language Model Alignment\"\n    - Authors: Yuu Jinnai et al. | 2024 | NAACL 2025\n    - Role: related_method\n    - Summary: Uses Minimum Bayes Risk objective as proximity regularizer for BoN to mitigate reward hacking; outperforms vanilla BoN and MBR decoding on AlpacaFarm and hh-rlhf.\n\n---\n\n## Category 32: faithfulness_nli (4 papers)\n\n98. **FaithLens** -- \"FaithLens: Detecting and Explaining Faithfulness Hallucination\"\n    - Authors: Unknown | 2025 | arXiv 2512.20182\n    - Role: method_component\n    - Summary: 8B model trained with synthetic data + rule-based RL outperforms GPT-4.1 and o3 on 12 faithfulness detection tasks; jointly predicts binary labels and generates explanations.\n\n99. **PrefixNLI** -- \"PrefixNLI: Detecting Factual Inconsistencies as Soon as They Arise\"\n    - Authors: Sapir Harary et al. | 2025 | arXiv 2511.01359\n    - Role: method_component\n    - Summary: Extends NLI from complete sentences to arbitrary text prefixes; MiniTruePrefixes model surpasses baseline NLI by 5-14 F1 on prefix-level entailment; enables controlled decoding.\n\n100. **NLI for QA Evaluation** -- \"Revisiting NLI: Towards Cost-Effective and Human-Aligned Metrics for Evaluating LLMs in Question Answering\"\n     - Authors: Unknown | 2025 | arXiv 2511.07659\n     - Role: evaluation\n     - Summary: Lightweight NLI scoring + lexical-match flag matches GPT-4o accuracy (89.9%) on long-form QA with orders of magnitude fewer parameters.\n\n101. **FaithJudge** -- \"Benchmarking LLM Faithfulness in RAG with Evolving Leaderboards\"\n     - Authors: Manveer Singh Tamber et al. | 2025 | EMNLP Industry 2025\n     - Role: evaluation\n     - Summary: FaithJudge framework with diverse human-annotated hallucination sample pools for improved LLM-as-judge evaluation; evolving leaderboard across summarization, QA, and data-to-text.\n\n---\n\n**Total: 101 papers across 32 categories.**"
      }
    ],
    "totalDurationMs": 322978,
    "totalTokens": 77420,
    "totalToolUseCount": 13,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11906,
      "cache_read_input_tokens": 53559,
      "output_tokens": 11954,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11906
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11954,
          "cache_read_input_tokens": 53559,
          "cache_creation_input_tokens": 11906,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11906,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 4,
      "searchCount": 0,
      "bashCount": 9,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
```

</details>

---

### Assistant

_source line 58_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me organize the Related Work section based on:

1. The paper framing (FREIGE: evidence-grounded DocRE, decoupling spectrum, RSFT, CED, EDCR)
2. The 101 papers across 32 categories from the literature map

The required structure:
- Document-level Relation Extraction (traditional → LLM methods)
- Evidence-based Information Extraction (evidence grounding in IE)
- Rejection Sampling and Reward-based Fine-tuning (RAFT, RSFT, BoN theory)


- RL for Structured Generation (GRPO/DPO in structured tasks, QLoRA artifacts)

Now I'm drafting the Related Work section using papers from the literature map, being careful to use proper citation keys derived from the paper names like DREEAM, RelPrior, and LMRC in the \cite{} format.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "893a5bce-a773-4150-b445-1ac7a7942328",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013qccvTSGrTyEuHFuWKyrhV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12429,
      "cache_read_input_tokens": 30797,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12429
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

_source line 59_

Now let me check if the target directory exists.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "36719196-b479-4269-9539-f602f6da8fab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013qccvTSGrTyEuHFuWKyrhV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12429,
      "cache_read_input_tokens": 30797,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12429
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

_source line 60_

<details open><summary>🔧 Tool call — Bash · `toolu_011k3XL3ou4oXG3nTjhYWc1q`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/paper/sections/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
  "description": "Check if paper/sections directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "00607ad5-931d-4e86-917d-12f798054c43",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013qccvTSGrTyEuHFuWKyrhV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12429,
      "cache_read_input_tokens": 30797,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12429
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

_source line 61 · 2026-05-16T00:45:36.822Z_

<details><summary>↩ Tool result · `toolu_011k3XL3ou4oXG3nTjhYWc1q`</summary>

```text
DIR_NOT_FOUND
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "ab9cb608-543e-4e9e-8db7-e949548c5891",
  "tool_use_result": {
    "stdout": "DIR_NOT_FOUND",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 62_

<details open><summary>🔧 Tool call — Bash · `toolu_01Gm82FGfS6QrXMJeC28evWa`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/ 2>/dev/null && echo \"---\" && ls /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/paper/ 2>/dev/null || echo \"NO_PAPER_DIR\"",
  "description": "Check artifacts directory structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "a0632855-3a9f-481e-a139-e897795e8a4d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tog25Lr3fcVSAwdk5xT6p6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 412,
      "cache_read_input_tokens": 43226,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 412
      },
      "output_tokens": 60,
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

_source line 63 · 2026-05-16T00:45:40.338Z_

<details><summary>↩ Tool result · `toolu_01Gm82FGfS6QrXMJeC28evWa`</summary>

```text
_project
ced_eval_commands.md
ced_stabilizer_literature_survey.md
cuda3_diagnostic.md
d024_literature_survey.md
diag_mvp2_grpo_flatnli_r3.md
diagnose_plan_001.md
diversity_probe.py
diversity_probe_results.md
dream_reports
edcr_analysis.md
edcr_analysis_r2b.md
edcr_diagnostic_table.md
eval_progress_check_0515.md
eval_script_audit.md
eval_status_check.md
freige
gap_analysis_w3.md
grpo_forgetting_dynamics.pdf
grpo_forgetting_dynamics.png
kl_analysis_report.md
literature_quantization_rl.md
literature_survey_evidence_overhead.md
manifest.yaml
metrics_summary.csv
metrics_summary_table.md
mvp2_eval_rsft_r2b_maxtok1536_r2
plan_001_flat_nli_seed45
plan_003
plan_003_edcr_cross_method_table.md
plan_003_edcr_diagnostic
plan_003_edcr_diagnostic.md
plan_009
plan_009_dynamics_data.json
plan_009_dynamics_figure
plan_009_forgetting_data.csv
plan_009_forgetting_data_v5.csv
plan_009_forgetting_figure
plan_009_grpo_forgetting
plan_012_dpo_ced
plan_012_dpo_ced_1ep_analysis.md
process_check_report.md
related_work_gap_analysis.md
related_work_survey
rsft_gen_progress_check.md
rsft_pipeline_commands.md
status_check_loop4.md
topk_ablation_lit_review.md
training_health_check.md
training_trajectory_loop4.md
trl_grpo_stability_research.md
---
NO_PAPER_DIR
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "e4bec1b3-693d-4bd1-a428-749182116d80",
  "tool_use_result": {
    "stdout": "_project\nced_eval_commands.md\nced_stabilizer_literature_survey.md\ncuda3_diagnostic.md\nd024_literature_survey.md\ndiag_mvp2_grpo_flatnli_r3.md\ndiagnose_plan_001.md\ndiversity_probe.py\ndiversity_probe_results.md\ndream_reports\nedcr_analysis.md\nedcr_analysis_r2b.md\nedcr_diagnostic_table.md\neval_progress_check_0515.md\neval_script_audit.md\neval_status_check.md\nfreige\ngap_analysis_w3.md\ngrpo_forgetting_dynamics.pdf\ngrpo_forgetting_dynamics.png\nkl_analysis_report.md\nliterature_quantization_rl.md\nliterature_survey_evidence_overhead.md\nmanifest.yaml\nmetrics_summary.csv\nmetrics_summary_table.md\nmvp2_eval_rsft_r2b_maxtok1536_r2\nplan_001_flat_nli_seed45\nplan_003\nplan_003_edcr_cross_method_table.md\nplan_003_edcr_diagnostic\nplan_003_edcr_diagnostic.md\nplan_009\nplan_009_dynamics_data.json\nplan_009_dynamics_figure\nplan_009_forgetting_data.csv\nplan_009_forgetting_data_v5.csv\nplan_009_forgetting_figure\nplan_009_grpo_forgetting\nplan_012_dpo_ced\nplan_012_dpo_ced_1ep_analysis.md\nprocess_check_report.md\nrelated_work_gap_analysis.md\nrelated_work_survey\nrsft_gen_progress_check.md\nrsft_pipeline_commands.md\nstatus_check_loop4.md\ntopk_ablation_lit_review.md\ntraining_health_check.md\ntraining_trajectory_loop4.md\ntrl_grpo_stability_research.md\n---\nNO_PAPER_DIR",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 64_

<details open><summary>🔧 Tool call — Bash · `toolu_01TttXcbQ94XGGELmdDBuxxm`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/paper/sections",
  "description": "Create paper/sections directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "c6709c8a-37a2-499d-8a41-805b25bf7b72",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UeFoWpLLkm3XiyehE8o5LR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 668,
      "cache_read_input_tokens": 43638,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 668
      },
      "output_tokens": 62,
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

_source line 65 · 2026-05-16T00:45:43.582Z_

<details><summary>↩ Tool result · `toolu_01TttXcbQ94XGGELmdDBuxxm`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "c4232d9e-5ba3-4130-8b55-ee259c4d9000",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  }
}
```

</details>

---

### Assistant

_source line 66_

Now writing the Related Work draft.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "630d49f2-d24c-4fdc-8761-a0c667b30c13",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019WqZbrJpCGSDzH8vgvur8w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 230,
      "cache_read_input_tokens": 44306,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 230
      },
      "output_tokens": 2,
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

_source line 67_

<details open><summary>🔧 Tool call — Write · `toolu_01QF3WVoG3MxHwLW8CJctwBR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/paper/sections/related_work.md",
  "content": "\\section{Related Work}\n\n\\subsection{Document-Level Relation Extraction}\n\nDocument-level relation extraction (DocRE) requires identifying relations between entity pairs scattered across multiple sentences, demanding cross-sentence reasoning over long contexts. Encoder-based methods have established strong baselines: DREEAM \\cite{ma2023dreeam} guides attention with evidence supervision and self-training, while EIDER \\cite{xie2022eider} fuses predictions from extracted evidence and the full document at inference time. CDER \\cite{tran2025cder} captures collaborative patterns among semantically similar entity pairs via bipartite graphs, and EAAGRE \\cite{eaagre2024} guides attention to evidence sentences without extra trainable parameters. These encoder methods, however, are limited to predefined relation schemas and cannot generalize to open-domain settings.\n\nRecent work has turned to LLMs for DocRE. AutoRE \\cite{autore2024} introduces a Relation-Head-Facts paradigm using Mistral-7B with QLoRA. RelPrior \\cite{relprior2025} uses binary relation priors to filter irrelevant entity pairs before matching predefined relations, achieving DocRED test F1 of 48.34 with LLaMA3-8B. LMRC \\cite{li2024lmrc} combines a BERT-based classifier for NA filtering with LLM multi-class classification, reaching Re-DocRED F1 of 74.63. DocKS-RAG \\cite{xu2025docksrag} integrates document-level knowledge graphs with sentence-level semantic RAG via hybrid-prompt tuning. GLiDRE \\cite{glidre2025} trains a lightweight dual-encoder for zero/few-shot DocRE. A comprehensive survey by \\citet{generative_ie_survey2024} identifies structured output quality and efficiency as key challenges for LLM-based IE.\n\nWhile these methods advance extraction accuracy, none jointly produces verifiable evidence sentences alongside relational triples. FREIGE addresses this gap by formulating evidence-grounded DocRE as a unified generation task.\n\n\\subsection{Evidence-Based Information Extraction}\n\nEvidence grounding has been explored primarily through encoder architectures in DocRE. DREEAM \\cite{ma2023dreeam} pioneered evidence retrieval self-training to generate silver evidence at scale. Evidence-aware DocRE \\cite{xu2022evidence_aware} models evidence sentence selection as a sequential decision problem using reinforcement learning. GEGA \\cite{mao2024gega} uses GCN with multi-weight matrices to guide attention to evidence sentences via a teacher-student framework. COREX \\cite{corex2024} jointly supervises two-hop reasoning and evidence prediction with adaptive focal loss. KnowRA \\cite{mai2025knowra} augments DocRE with external knowledge retrieval and coreference-enhanced document knowledge graphs. Beyond DocRE, Grounded KG Extraction \\cite{grounded_kg2025} provides character-level provenance tracking for each extracted triple.\n\nIn the broader NLP landscape, the tension between faithfulness and task performance is well-documented. \\citet{sprague2024mind_your_step} show that chain-of-thought can reduce performance by up to 36.3\\% on certain tasks due to error accumulation. \\citet{resck2024performance_explanation} formally explore the Pareto frontier between performance and explanation plausibility via multi-objective optimization. \\citet{wallat2024correctness_faithfulness} demonstrate that correctness and faithfulness are independent dimensions, with up to 57\\% of citations being post-rationalized. \\citet{lyu2024faithful_survey} survey faithful explanations in NLP, identifying the faithfulness-performance trade-off as a core challenge. These findings motivate our framing of the ``evidence generation tax''---the cost in extraction accuracy incurred by requiring models to simultaneously produce supporting evidence.\n\n\\subsection{Rejection Sampling and Reward-Based Fine-Tuning}\n\nRejection sampling fine-tuning (RSFT) iteratively generates candidate responses, scores them with a reward function, and fine-tunes on the top-ranked outputs. RAFT \\cite{raft2024} establishes the canonical framework: generate $n$ responses per prompt, rank by reward, and train on the top-$k$. \\citet{xiao2025minimalist_rsft} show that this simple approach matches GRPO and PPO on mathematical reasoning, with GRPO's advantage stemming mainly from discarding all-wrong prompts rather than reward normalization. The theoretical connection to policy optimization is formalized by \\citet{rsft_ppo2025}, who prove RSFT implicitly performs PPO with marginal KL constraints.\n\nSeveral extensions improve RSFT's sample efficiency. AdaSTaR \\cite{chung2025adaptar} introduces diversity and curriculum sampling to address training imbalance, achieving SOTA with 58.6\\% fewer FLOPs. TrajFusion \\cite{deng2026trajfusion} interleaves failed and correct trajectories to model trial-and-error reasoning. RIFT \\cite{rift2026} replaces hard rejection with soft reweighting of all trajectories by scalar reward, providing reverse gradients from negative samples. RS-DPO \\cite{rsdpo2024} systematically combines rejection sampling with DPO by identifying contrastive pairs from the reward distribution.\n\nAt inference time, Best-of-N (BoN) sampling applies the same generate-and-select principle without further training. \\citet{huang2025bon_optimality} prove BoN provably suffers from reward hacking at large $N$ and propose InferenceTimePessimism for scaling-monotonic performance. \\citet{chen2025inference_reward_hacking} show that the true reward first rises then falls under all inference-time mechanisms. Genie \\cite{yehudai2024genie} demonstrates NLI-based filtering in a three-stage pipeline achieving human parity on content-grounded generation.\n\nFREIGE adopts RSFT with NLI-based scoring (CED) as its primary training strategy, and uses CED as an inference-time reranker---bridging RSFT and BoN paradigms while avoiding the decoupling pathology observed with online RL methods.\n\n\\subsection{Reinforcement Learning for Structured Generation}\n\nGroup Relative Policy Optimization (GRPO) has emerged as a prominent critic-free RL method for LLMs. DAPO \\cite{dapo2025} addresses GRPO's entropy collapse via asymmetric clipping and dynamic sampling. Dr.\\ GRPO \\cite{dr_grpo2025} identifies difficulty and length biases from standard normalization. REINFORCE++ \\cite{hu2025reinforcepp} proposes global batch normalization for more stable gradient estimation. In structured IE, R1-RE \\cite{dai2025r1re} applies GRPO with verifiable rewards for cross-domain sentence-level RE, and R2GRPO \\cite{li2025r2grpo} combines relevance and rule-mining rewards for scientific IE. E-GRPO \\cite{egrpo2025} designs entity-aware rewards giving partial credit based on entity match rate. ReasoningNER \\cite{reasoningner2025} uses a three-stage GRPO framework beating GPT-4 on zero-shot NER.\n\nHowever, applying RL to structured extraction tasks introduces pathologies not observed in reasoning benchmarks. \\citet{jin2025rl_vs_sft} show RL fine-tuning cannot fully recover performance when SFT causes severe overfitting. EvidenceRL \\cite{bentamo2026evidencerl}, the closest concurrent work to ours, uses GRPO to jointly optimize evidence entailment and correctness in clinical diagnosis---but does not report extraction-evidence decoupling. MO-GRPO \\cite{ichihara2025mogrpo} and RDPO \\cite{bai2026rdpo} address reward hacking in multi-objective settings, while \\citet{wang2026reward_hacking_survey} propose the Proxy Compression Hypothesis explaining reward hacking as objective compression.\n\nA critical confound in RL for LLMs is quantization. QeRL \\cite{qerl2025} shows standard quantization introduces deterministic noise harmful to RL exploration. \\citet{quantization_rl_impact2025} find quantization-aware RL training actually harms learning, with post-training quantization performing better. \\citet{shuttleworth2024lora_vs_fft} reveal LoRA and full fine-tuning produce structurally different weight matrices, with forgetting concentrated in ``intruder dimensions.'' Q-BLoRA \\cite{seo2024qblora} identifies an imbalance between overly complex adapter I/O and insufficient trainability in quantized LLMs. CLoQ \\cite{cloq2025} addresses quantization errors via calibrated LoRA initialization. These findings align with our observation that QLoRA amplifies the evidence-extraction decoupling from mild to catastrophic, acting not as the root cause but as a catastrophic amplifier of an inherent RL-for-IE pathology.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "4f275112-cac3-44e4-aab9-e986751815b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019WqZbrJpCGSDzH8vgvur8w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 230,
      "cache_read_input_tokens": 44306,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 230
      },
      "output_tokens": 2,
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

_source line 68 · 2026-05-16T00:46:45.087Z_

<details><summary>↩ Tool result · `toolu_01QF3WVoG3MxHwLW8CJctwBR`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/paper/sections/related_work.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "23094561-ba33-4af7-b8ed-039967c69770",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/paper/sections/related_work.md",
    "content": "\\section{Related Work}\n\n\\subsection{Document-Level Relation Extraction}\n\nDocument-level relation extraction (DocRE) requires identifying relations between entity pairs scattered across multiple sentences, demanding cross-sentence reasoning over long contexts. Encoder-based methods have established strong baselines: DREEAM \\cite{ma2023dreeam} guides attention with evidence supervision and self-training, while EIDER \\cite{xie2022eider} fuses predictions from extracted evidence and the full document at inference time. CDER \\cite{tran2025cder} captures collaborative patterns among semantically similar entity pairs via bipartite graphs, and EAAGRE \\cite{eaagre2024} guides attention to evidence sentences without extra trainable parameters. These encoder methods, however, are limited to predefined relation schemas and cannot generalize to open-domain settings.\n\nRecent work has turned to LLMs for DocRE. AutoRE \\cite{autore2024} introduces a Relation-Head-Facts paradigm using Mistral-7B with QLoRA. RelPrior \\cite{relprior2025} uses binary relation priors to filter irrelevant entity pairs before matching predefined relations, achieving DocRED test F1 of 48.34 with LLaMA3-8B. LMRC \\cite{li2024lmrc} combines a BERT-based classifier for NA filtering with LLM multi-class classification, reaching Re-DocRED F1 of 74.63. DocKS-RAG \\cite{xu2025docksrag} integrates document-level knowledge graphs with sentence-level semantic RAG via hybrid-prompt tuning. GLiDRE \\cite{glidre2025} trains a lightweight dual-encoder for zero/few-shot DocRE. A comprehensive survey by \\citet{generative_ie_survey2024} identifies structured output quality and efficiency as key challenges for LLM-based IE.\n\nWhile these methods advance extraction accuracy, none jointly produces verifiable evidence sentences alongside relational triples. FREIGE addresses this gap by formulating evidence-grounded DocRE as a unified generation task.\n\n\\subsection{Evidence-Based Information Extraction}\n\nEvidence grounding has been explored primarily through encoder architectures in DocRE. DREEAM \\cite{ma2023dreeam} pioneered evidence retrieval self-training to generate silver evidence at scale. Evidence-aware DocRE \\cite{xu2022evidence_aware} models evidence sentence selection as a sequential decision problem using reinforcement learning. GEGA \\cite{mao2024gega} uses GCN with multi-weight matrices to guide attention to evidence sentences via a teacher-student framework. COREX \\cite{corex2024} jointly supervises two-hop reasoning and evidence prediction with adaptive focal loss. KnowRA \\cite{mai2025knowra} augments DocRE with external knowledge retrieval and coreference-enhanced document knowledge graphs. Beyond DocRE, Grounded KG Extraction \\cite{grounded_kg2025} provides character-level provenance tracking for each extracted triple.\n\nIn the broader NLP landscape, the tension between faithfulness and task performance is well-documented. \\citet{sprague2024mind_your_step} show that chain-of-thought can reduce performance by up to 36.3\\% on certain tasks due to error accumulation. \\citet{resck2024performance_explanation} formally explore the Pareto frontier between performance and explanation plausibility via multi-objective optimization. \\citet{wallat2024correctness_faithfulness} demonstrate that correctness and faithfulness are independent dimensions, with up to 57\\% of citations being post-rationalized. \\citet{lyu2024faithful_survey} survey faithful explanations in NLP, identifying the faithfulness-performance trade-off as a core challenge. These findings motivate our framing of the ``evidence generation tax''---the cost in extraction accuracy incurred by requiring models to simultaneously produce supporting evidence.\n\n\\subsection{Rejection Sampling and Reward-Based Fine-Tuning}\n\nRejection sampling fine-tuning (RSFT) iteratively generates candidate responses, scores them with a reward function, and fine-tunes on the top-ranked outputs. RAFT \\cite{raft2024} establishes the canonical framework: generate $n$ responses per prompt, rank by reward, and train on the top-$k$. \\citet{xiao2025minimalist_rsft} show that this simple approach matches GRPO and PPO on mathematical reasoning, with GRPO's advantage stemming mainly from discarding all-wrong prompts rather than reward normalization. The theoretical connection to policy optimization is formalized by \\citet{rsft_ppo2025}, who prove RSFT implicitly performs PPO with marginal KL constraints.\n\nSeveral extensions improve RSFT's sample efficiency. AdaSTaR \\cite{chung2025adaptar} introduces diversity and curriculum sampling to address training imbalance, achieving SOTA with 58.6\\% fewer FLOPs. TrajFusion \\cite{deng2026trajfusion} interleaves failed and correct trajectories to model trial-and-error reasoning. RIFT \\cite{rift2026} replaces hard rejection with soft reweighting of all trajectories by scalar reward, providing reverse gradients from negative samples. RS-DPO \\cite{rsdpo2024} systematically combines rejection sampling with DPO by identifying contrastive pairs from the reward distribution.\n\nAt inference time, Best-of-N (BoN) sampling applies the same generate-and-select principle without further training. \\citet{huang2025bon_optimality} prove BoN provably suffers from reward hacking at large $N$ and propose InferenceTimePessimism for scaling-monotonic performance. \\citet{chen2025inference_reward_hacking} show that the true reward first rises then falls under all inference-time mechanisms. Genie \\cite{yehudai2024genie} demonstrates NLI-based filtering in a three-stage pipeline achieving human parity on content-grounded generation.\n\nFREIGE adopts RSFT with NLI-based scoring (CED) as its primary training strategy, and uses CED as an inference-time reranker---bridging RSFT and BoN paradigms while avoiding the decoupling pathology observed with online RL methods.\n\n\\subsection{Reinforcement Learning for Structured Generation}\n\nGroup Relative Policy Optimization (GRPO) has emerged as a prominent critic-free RL method for LLMs. DAPO \\cite{dapo2025} addresses GRPO's entropy collapse via asymmetric clipping and dynamic sampling. Dr.\\ GRPO \\cite{dr_grpo2025} identifies difficulty and length biases from standard normalization. REINFORCE++ \\cite{hu2025reinforcepp} proposes global batch normalization for more stable gradient estimation. In structured IE, R1-RE \\cite{dai2025r1re} applies GRPO with verifiable rewards for cross-domain sentence-level RE, and R2GRPO \\cite{li2025r2grpo} combines relevance and rule-mining rewards for scientific IE. E-GRPO \\cite{egrpo2025} designs entity-aware rewards giving partial credit based on entity match rate. ReasoningNER \\cite{reasoningner2025} uses a three-stage GRPO framework beating GPT-4 on zero-shot NER.\n\nHowever, applying RL to structured extraction tasks introduces pathologies not observed in reasoning benchmarks. \\citet{jin2025rl_vs_sft} show RL fine-tuning cannot fully recover performance when SFT causes severe overfitting. EvidenceRL \\cite{bentamo2026evidencerl}, the closest concurrent work to ours, uses GRPO to jointly optimize evidence entailment and correctness in clinical diagnosis---but does not report extraction-evidence decoupling. MO-GRPO \\cite{ichihara2025mogrpo} and RDPO \\cite{bai2026rdpo} address reward hacking in multi-objective settings, while \\citet{wang2026reward_hacking_survey} propose the Proxy Compression Hypothesis explaining reward hacking as objective compression.\n\nA critical confound in RL for LLMs is quantization. QeRL \\cite{qerl2025} shows standard quantization introduces deterministic noise harmful to RL exploration. \\citet{quantization_rl_impact2025} find quantization-aware RL training actually harms learning, with post-training quantization performing better. \\citet{shuttleworth2024lora_vs_fft} reveal LoRA and full fine-tuning produce structurally different weight matrices, with forgetting concentrated in ``intruder dimensions.'' Q-BLoRA \\cite{seo2024qblora} identifies an imbalance between overly complex adapter I/O and insufficient trainability in quantized LLMs. CLoQ \\cite{cloq2025} addresses quantization errors via calibrated LoRA initialization. These findings align with our observation that QLoRA amplifies the evidence-extraction decoupling from mild to catastrophic, acting not as the root cause but as a catastrophic amplifier of an inherent RL-for-IE pathology.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 69_

Now let me register it as an artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "f6c65058-b6fd-4d70-833b-5190d62cab52",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X7vkwhpJASK6mtxohK1sXW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2299,
      "cache_read_input_tokens": 44536,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2299
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

### Tool call

_source line 70_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017qBcBiZfrdtwpBd92Am4bs`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__append_idea,mcp__agent-ml-research__save_project_file",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "03079bfc-8a8b-4a2c-9e3f-d5b2b9db9890",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X7vkwhpJASK6mtxohK1sXW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2299,
      "cache_read_input_tokens": 44536,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2299
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

### Tool result

_source line 71 · 2026-05-16T00:46:48.385Z_

<details><summary>↩ Tool result · `toolu_017qBcBiZfrdtwpBd92Am4bs`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__append_idea"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "e50417bd-0e93-4568-9782-01d18da3ee67",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__append_idea,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 72_

<details><summary>Logged reasoning block</summary>

```text
The save_project_file tool says paper sections should use `write_paper_section` / `edit_paper_section`. Let me search for those tools.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "f08f1bbf-2d78-4f50-a3a4-7fb16129471f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011yWAmcEDYUN8G2tkCRNmYi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 567,
      "cache_read_input_tokens": 46835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 567
      },
      "output_tokens": 40,
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

_source line 73_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JsxMavxEK9BYDQEcJhrGF2`</summary>

```json
{
  "query": "write_paper_section register_artifact",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "c1626f1d-0238-4e99-8821-dd1f17c7ed23",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011yWAmcEDYUN8G2tkCRNmYi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 567,
      "cache_read_input_tokens": 46835,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 567
      },
      "output_tokens": 40,
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

_source line 74 · 2026-05-16T00:46:52.648Z_

<details><summary>↩ Tool result · `toolu_01JsxMavxEK9BYDQEcJhrGF2`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "96824dae-886c-4b86-a5ed-8de4d86e1f57",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "write_paper_section register_artifact",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 75_

<details><summary>Logged reasoning block</summary>

```text
The tool search didn't find `write_paper_section` or `register_artifact` as separate tools. Let me search more specifically.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "f7ce9edf-3e8d-4028-8618-b20d61374b94",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CEqewtFv5Vd7NR46FvRL5K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 406,
      "cache_read_input_tokens": 47402,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 406
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

_source line 76_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01CSSzb9yYFkmFHWhRK8C1ba`</summary>

```json
{
  "query": "+register_artifact",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "d2691925-c96e-4a0e-a81d-a5c2785f2679",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CEqewtFv5Vd7NR46FvRL5K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 406,
      "cache_read_input_tokens": 47402,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 406
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

_source line 77 · 2026-05-16T00:46:56.569Z_

<details><summary>↩ Tool result · `toolu_01CSSzb9yYFkmFHWhRK8C1ba`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "0fc956e3-edbf-4406-b9b1-7502a7fa6ecb",
  "tool_use_result": {
    "matches": [],
    "query": "+register_artifact",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 78_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014HFb395sdWZDvQZjX8Tw1j`</summary>

```json
{
  "query": "+write_paper_section",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "02c2a404-2a1a-4fbb-b546-b9c48c056f8e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CEqewtFv5Vd7NR46FvRL5K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 406,
      "cache_read_input_tokens": 47402,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 406
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

_source line 79 · 2026-05-16T00:46:56.666Z_

<details><summary>↩ Tool result · `toolu_014HFb395sdWZDvQZjX8Tw1j`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "d6ab8f29-48fb-43e6-b972-988a486ec362",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "+write_paper_section",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 80_

No dedicated `register_artifact` or `write_paper_section` tools available. The file is already written to the artifacts directory. Let me verify the word count.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "eb86bb89-918c-46f8-8521-b6838a725f32",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PZDDvA1RGiLJSs3RTjUb9A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 506,
      "cache_read_input_tokens": 47808,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 506
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

### Tool call

_source line 81_

<details open><summary>🔧 Tool call — Bash · `toolu_01R4UQJuqXzUNnZkQzU2hsLV`</summary>

```json
{
  "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/paper/sections/related_work.md",
  "description": "Count words in related work draft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "016f1f9e-4d2b-4bf3-84ee-f8339147abf0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PZDDvA1RGiLJSs3RTjUb9A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 506,
      "cache_read_input_tokens": 47808,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 506
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

### Tool result

_source line 82 · 2026-05-16T00:47:01.206Z_

<details><summary>↩ Tool result · `toolu_01R4UQJuqXzUNnZkQzU2hsLV`</summary>

```text
961 /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/paper/sections/related_work.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "a885fcf0-4127-42b5-bd16-369fdf57bd46",
  "tool_use_result": {
    "stdout": "961 /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/paper/sections/related_work.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 83_

Related Work 初稿已写入 `artifacts/paper/sections/related_work.md`（961 词，在 800-1200 目标范围内）。

结构如下：

1. **Document-Level Relation Extraction** — 从 encoder 方法（DREEAM, EIDER, CDER, EAAGRE）到 LLM 方法（AutoRE, RelPrior, LMRC, DocKS-RAG, GLiDRE），指出无方法同时输出证据
2. **Evidence-Based Information Extraction** — DocRE 中的 evidence grounding（DREEAM, Evidence-aware DocRE, GEGA, COREX, KnowRA），以及 faithfulness-performance trade-off 的广泛文献支撑（Mind Your Step, Performance-Explanation Trade-off, Correctness≠Faithfulness），引出 "evidence generation tax" 概念
3. **Rejection Sampling and Reward-Based Fine-Tuning** — RAFT 框架、RSFT=PPO 理论联系、AdaSTaR/TrajFusion/RIFT 扩展、BoN 推理时选择及其 reward hacking 问题，连接到 FREIGE 的 CED-based RSFT + reranker 方案
4. **RL for Structured Generation** — GRPO 及其变体（DAPO, Dr. GRPO, REINFORCE++）、IE 领域应用（R1-RE, R2GRPO, E-GRPO, ReasoningNER）、QLoRA artifacts 文献（QeRL, LoRA vs FFT, Q-BLoRA），支撑 decoupling 发现和 QLoRA-as-amplifier 论点

所有引用均来自 `literature_map.yaml`，覆盖 32 个 category 中的 ~50 篇关键论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "uuid": "4f0c1b07-f307-4796-be95-3f488e4aba92",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uh2TphRP6w5qa26isTZoMr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 207,
      "cache_read_input_tokens": 48314,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 207
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

_source line 84_

Related Work 初稿已写入 `artifacts/paper/sections/related_work.md`（961 词，在 800-1200 目标范围内）。

结构如下：

1. **Document-Level Relation Extraction** — 从 encoder 方法（DREEAM, EIDER, CDER, EAAGRE）到 LLM 方法（AutoRE, RelPrior, LMRC, DocKS-RAG, GLiDRE），指出无方法同时输出证据
2. **Evidence-Based Information Extraction** — DocRE 中的 evidence grounding（DREEAM, Evidence-aware DocRE, GEGA, COREX, KnowRA），以及 faithfulness-performance trade-off 的广泛文献支撑（Mind Your Step, Performance-Explanation Trade-off, Correctness≠Faithfulness），引出 "evidence generation tax" 概念
3. **Rejection Sampling and Reward-Based Fine-Tuning** — RAFT 框架、RSFT=PPO 理论联系、AdaSTaR/TrajFusion/RIFT 扩展、BoN 推理时选择及其 reward hacking 问题，连接到 FREIGE 的 CED-based RSFT + reranker 方案
4. **RL for Structured Generation** — GRPO 及其变体（DAPO, Dr. GRPO, REINFORCE++）、IE 领域应用（R1-RE, R2GRPO, E-GRPO, ReasoningNER）、QLoRA artifacts 文献（QeRL, LoRA vs FFT, Q-BLoRA），支撑 decoupling 发现和 QLoRA-as-amplifier 论点

所有引用均来自 `literature_map.yaml`，覆盖 32 个 category 中的 ~50 篇关键论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 452159,
  "duration_api_ms": 450844,
  "num_turns": 14,
  "stop_reason": "end_turn",
  "session_id": "7341df47-ab61-4a7f-ab4b-fc80cccd2794",
  "total_cost_usd": 1.55045125,
  "usage": {
    "input_tokens": 22,
    "cache_creation_input_tokens": 37074,
    "cache_read_input_tokens": 455957,
    "output_tokens": 4702,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 37074,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 497,
        "cache_read_input_tokens": 48314,
        "cache_creation_input_tokens": 207,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 207
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1620,
      "outputTokens": 15,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001695,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 37,
      "outputTokens": 19744,
      "cacheReadInputTokens": 828205,
      "cacheCreationInputTokens": 102539,
      "webSearchRequests": 0,
      "costUSD": 1.5487562499999998,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "b9b03059-b259-48d6-a9d1-acb3d72cc2fc"
}
```

</details>

---
