# research literature scan

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 130
- **Recorded user turns:** 0
- **Tool calls:** 50
- **Original source:** `logs/workers/worker_research_literature-scan_20260515T220732.log`
- **Structured JSON:** [`506427a7858590619cf3.json`](../../sessions/50/506427a7858590619cf3.json)

## Before a recorded user message

130 recorded events

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
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
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
  "uuid": "7f98c73c-7f3e-486e-804c-62920d4d1016",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/memory/"
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
    "resetsAt": 1778885400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "86f2bfa7-5157-493f-a1c7-772718d4b64b",
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to do a literature scan for their FREIGE paper on evidence-grounded document-level relation extraction. Let me start by reading the existing literature map, then search for relevant papers.

Let me first load the MCP tools I need, and read the existing literature map.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "70435a83-b071-455a-9fd5-4465f21365ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UwK7ZgRSTjy2GuKRGjjX32",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11383,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11383
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

### Assistant

_source line 5_

先读取现有文献覆盖，再进行多方向搜索。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "2a86d972-509d-44ea-9435-757b11e33ed1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UwK7ZgRSTjy2GuKRGjjX32",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11383,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11383
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

### Tool call

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01PsgDbqhGwQrANiYX5hjZQq`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__append_idea,WebSearch,WebFetch",
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
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "399ab594-9b77-4d82-82a6-312ca3c7addc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UwK7ZgRSTjy2GuKRGjjX32",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11383,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11383
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

_source line 7 · 2026-05-15T22:07:42.923Z_

<details><summary>↩ Tool result · `toolu_01PsgDbqhGwQrANiYX5hjZQq`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__append_idea"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
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
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "5b43b760-813c-4186-a3e5-f45eb371809c",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__append_idea",
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__append_idea,WebSearch,WebFetch",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01NCH9dqRGbLALpQDB7XqX3A`</summary>

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
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "f3ca6c57-f13e-4bf0-b5c2-d7d0007ed23b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M6fnyB9cjPeRABkxSpTyzb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1991,
      "cache_read_input_tokens": 23224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1991
      },
      "output_tokens": 66,
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

_source line 9 · 2026-05-15T22:07:45.874Z_

<details><summary>↩ Tool result · `toolu_01NCH9dqRGbLALpQDB7XqX3A`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml\", \"content\": \"# Literature Map for faith-evidence-ie (FREIGE)\\n# Focus: CED-as-training-stabilizer (D024) + RSFT for DocRE\\n# Updated: 2026-05-15 (W3 reviewer gap fill + evidence generation trade-off survey)\\n\\npapers:\\n\\n  # === Category 1: Reward Diversity / Reward Shaping for RL Stability ===\\n\\n  - title: \\\"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization\\\"\\n    authors: NVIDIA Labs\\n    year: 2025\\n    venue: ICML 2026\\n    url: https://arxiv.org/abs/2601.05242\\n    category: reward_diversity\\n    role: closest_prior_work\\n    key_finding: >\\n      直接将 GRPO 应用于多 reward 组合时，不同 rollout 的 reward 组合在归一化后 collapse 为相同 advantage 值，\\n      降低训练信号分辨率导致收敛失败。GDPO 对每个 reward 独立做 group-wise normalization 再聚合，\\n      保留多 reward 的相对差异，显著提升训练稳定性。\\n    relevance_to_ced_stabilizer: >\\n      最直接相关。CED reward 本质上引入了独立于 extraction F1 的 reward 维度（evidence quality），\\n      GDPO 的理论分析解释了为什么多维 reward 比单一 reward 更稳定——独立 reward 维度防止 advantage collapse。\\n      但 GDPO 是方法论贡献，CED 是 task-specific reward 设计自然具备了这一特性。\\n\\n  - title: \\\"DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of LLMs\\\"\\n    authors: Xiwen Chen et al.\\n    year: 2025\\n    venue: arXiv 2505.09655\\n    url: https://arxiv.org/abs/2505.09655\\n    category: reward_diversity\\n    role: related_method\\n    key_finding: >\\n      GRPO 的标量 reward 无法区分语义多样但得分相同的输出（diversity-quality inconsistency）。\\n      DRA 用子模互信息（SMI）对 reward 加权，给多样性高的 completion 更大权重，\\n      等价于 Inverse Propensity Scoring 去偏，防止 policy 坍缩到先验模式。\\n    relevance_to_ced_stabilizer: >\\n      DRA 通过后处理 reward 注入多样性信号；CED 的 reward 本身就内含对比结构自然提供 diversity 信号。\\n      机制互补但来源不同——CED 是 reward design 层面，DRA 是 optimization 层面。\\n\\n  - title: \\\"Shrinking the Variance: Shrinkage Baselines for RL with Verifiable Rewards\\\"\\n    authors: Guanning Zeng et al.\\n    year: 2025\\n    venue: arXiv 2511.03710\\n    url: https://arxiv.org/abs/2511.03710\\n    category: reward_diversity\\n    role: theoretical_support\\n    key_finding: >\\n      RLVR 中 per-prompt 均值 baseline 在低 generation 数下估计不准导致高 variance 梯度。\\n      用 James-Stein shrinkage 混合 per-prompt 和 cross-prompt 均值，\\n      构造可证明更低 variance 的 policy gradient estimator。\\n    relevance_to_ced_stabilizer: >\\n      理论支持：reward variance 对 gradient estimation 质量至关重要。\\n      CED 的额外 reward 维度提供更丰富的 per-group variance，间接起到 variance 维持效果。\\n\\n  - title: \\\"Reward Shaping to Mitigate Reward Hacking in RLHF\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2502.18770\\n    url: https://arxiv.org/abs/2502.18770\\n    category: reward_diversity\\n    role: background\\n    key_finding: >\\n      RL reward 应有界且先快速增长后缓慢收敛。系统研究 reward shaping 原则，\\n      好的 reward 形状能抑制 reward hacking 并提升训练稳定性。\\n    relevance_to_ced_stabilizer: >\\n      CED reward 的 0-1 对比判别结构天然满足有界性，\\n      且 evidence quality 的渐进提升符合\\\"先快后慢\\\"的 reward shaping 原则。\\n\\n  # === Category 2: Mode Collapse Prevention in GRPO/RLHF ===\\n\\n  - title: \\\"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\\\"\\n    authors: ByteDance Seed, Tsinghua AIR\\n    year: 2025\\n    venue: NeurIPS 2025\\n    url: https://arxiv.org/abs/2503.14476\\n    category: mode_collapse_prevention\\n    role: key_baseline\\n    key_finding: >\\n      Naive GRPO 存在 entropy collapse（policy 熵快速下降→输出同质化）。\\n      根因：clipping 不对称性——概率 0.01 的 token 最多增到 0.012，而概率 0.9 的 token 可达 1.08，\\n      低概率 token 难以增长，抑制探索。DAPO 提出 Clip-Higher（εhigh=0.28 > εlow=0.2）\\n      为低概率 token 留更大增长空间，加 Dynamic Sampling 过滤 accuracy=0 或 1 的 prompt\\n      （这些 prompt 产生零梯度，降低有效 batch size）。在 AIME 2024 达 50 分超越 DeepSeek-R1-Zero。\\n    relevance_to_ced_stabilizer: >\\n      DAPO 从 optimization 技巧角度解决 entropy collapse。CED reward 从 reward design 层面\\n      防止 mode collapse——evidence quality 维度确保 reward 组内有足够 variance，\\n      不会出现 all-same-reward 的零梯度 prompt。DAPO 的 Dynamic Sampling 过滤 accuracy=0/1 prompt\\n      与我们观察到的 frac_zero_std→0.8 现象本质相同：extraction-only reward 下大量 prompt\\n      产生零 advantage，CED 从源头（reward 设计）而非后处理（过滤）解决这个问题。\\n\\n  - title: \\\"Dr. GRPO: Removing Optimization Bias in GRPO\\\"\\n    authors: Liu et al.\\n    year: 2025\\n    venue: COLM 2025\\n    url: https://arxiv.org/abs/2503.20783\\n    category: mode_collapse_prevention\\n    role: related_analysis\\n    key_finding: >\\n      GRPO 的 std 归一化引入两个 bias：(1) difficulty bias——std(r) 归一化对低 variance 组\\n      （全对/全错）给予过高 advantage 权重，trivial question 主导训练信号；\\n      (2) length bias——per-token loss 的 1/|o_i| 项使长的错误回答被 under-penalize。\\n      当 std(r)→0 时 advantage 爆炸或未定义，梯度数值不稳定。\\n      Dr. GRPO 移除 std 归一化，用无偏 Monte Carlo advantage：Ã = R(q,o_i) - mean(R)。\\n    relevance_to_ced_stabilizer: >\\n      与我们的实验发现高度一致：extraction-only reward 下 frac_zero_std→0.8 正是\\n      Dr. GRPO 分析的 difficulty bias 极端情况——大量 prompt 的所有 rollout 得到相同 F1，\\n      std→0 导致 advantage 异常。CED 通过增加 reward 维度天然维持 reward_std>0，\\n      从 reward 设计而非算法修改角度避免了 Dr. GRPO 发现的 bias。\\n\\n  - title: \\\"GVPO: Group Variance Policy Optimization for LLM Post-Training\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: NeurIPS 2025\\n    url: https://arxiv.org/abs/2504.19599\\n    category: mode_collapse_prevention\\n    role: alternative_framework\\n    key_finding: >\\n      将 KL 约束 reward 最大化的解析解直接嵌入梯度权重，\\n      variance 项自然平衡 exploration 与 exploitation，维持适度 entropy。\\n    relevance_to_ced_stabilizer: >\\n      GVPO 的 variance 项机制与 CED 维持 reward variance 的效果功能类似，\\n      但 GVPO 是算法层面 implicit regularization，CED 是 reward 层面 explicit structure。\\n\\n  - title: \\\"REINFORCE++: Stabilizing Critic-Free Policy Optimization with Global Advantage Normalization\\\"\\n    authors: Jian Hu et al.\\n    year: 2025\\n    venue: arXiv 2501.03262\\n    url: https://arxiv.org/abs/2501.03262\\n    category: mode_collapse_prevention\\n    role: related_method\\n    key_finding: >\\n      Prompt-level (local) advantage normalization 导致不准确估计和过拟合。\\n      Global batch normalization 提供更稳定、理论无偏的 gradient estimator。\\n    relevance_to_ced_stabilizer: >\\n      解决 local normalization 的 variance 问题；CED 从 reward 端增加 variance 来源。\\n      两者在不同层面解决同一问题：防止 gradient signal 消失。\\n\\n  - title: \\\"DiverseGRPO: Mitigating Mode Collapse in Image Generation via Diversity-Aware GRPO\\\"\\n    authors: Henglin Liu et al.\\n    year: 2025\\n    venue: arXiv 2512.21514\\n    url: https://arxiv.org/abs/2512.21514\\n    category: mode_collapse_prevention\\n    role: parallel_work\\n    key_finding: >\\n      图像生成中 GRPO 后期输出同质化。distributional reward modeling（谱聚类+exploratory reward）\\n      和 structure-aware regularization 实现 13-18% 语义多样性提升。\\n    relevance_to_ced_stabilizer: >\\n      跨域验证了 GRPO mode collapse 的普遍性，distributional reward 思路与 CED 精神相近——\\n      都是通过 reward 层面结构化信号维持输出多样性。\\n\\n  - title: \\\"Why GRPO Needs Normalization: A Local-Curvature Perspective on Adaptive Gradients\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2601.23135\\n    url: https://arxiv.org/abs/2601.23135\\n    category: mode_collapse_prevention\\n    role: theoretical_support\\n    key_finding: >\\n      GRPO 的 reward_std 归一化在温和条件下提供严格优于未归一化 REINFORCE 的收敛速率，\\n      收益由 prompt 间平均 reward std 刻画。\\n    relevance_to_ced_stabilizer: >\\n      直接理论支撑：reward_std 越大收敛越好。CED 通过 evidence quality 维度维持高 reward_std，\\n      从该理论看 CED 的稳定性优势是 reward_std 维持带来的收敛速率优势。\\n\\n  # === Category 3: Contrastive Rewards in RL ===\\n\\n  - title: \\\"Improving Reinforcement Learning from Human Feedback Using Contrastive Rewards\\\"\\n    authors: Shen, Zhang et al.\\n    year: 2024\\n    venue: arXiv 2403.07708\\n    url: https://arxiv.org/abs/2403.07708\\n    category: contrastive_reward\\n    role: closest_contrastive_precedent\\n    key_finding: >\\n      两步机制：(1) 离线采样 baseline response；(2) 用 baseline 计算 contrastive reward\\n      作为 PPO 的 penalty 项。效果：惩罚 reward uncertainty、根据任务难度自适应校准、\\n      减少 PPO 中的 variance。在 TL;DR 和 HH-RLHF 上持续优于标准 RLHF。\\n    relevance_to_ced_stabilizer: >\\n      最接近的对比 reward 先例。关键差异：(1) 它是对 learned RM 输出的后处理对比，\\n      CED 是 reward function 本身就是对比判别（evidence vs. corrupted evidence）；\\n      (2) 它在 PPO 中验证，CED 在 GRPO 中验证；\\n      (3) 它是 domain-agnostic penalty，CED 是 task-specific faithfulness signal。\\n      stabilizing 机制相通但实现路径根本不同。\\n\\n  - title: \\\"Improving Discriminative Capability of Reward Models in RLHF Using Contrastive Learning\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: EMNLP 2024\\n    url: https://aclanthology.org/2024.emnlp-main.852/\\n    category: contrastive_reward\\n    role: related_method\\n    key_finding: >\\n      无监督对比损失训练 reward model 充分捕捉对比数据区分度，\\n      带来更稳定的 PPO 训练 return 和 reward。\\n    relevance_to_ced_stabilizer: >\\n      验证对比训练 reward model → 更稳定 RL 训练链条。CED 不是对比训练 reward model，\\n      而是 reward function 本身就是对比判别，但 stabilizing 机制相通。\\n\\n  - title: \\\"Contrastive Preference Learning: Learning from Human Feedback without RL\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: ICLR 2025\\n    url: https://openreview.net/forum?id=iX1RjVQODj\\n    category: contrastive_reward\\n    role: background\\n    key_finding: >\\n      将 preference learning 重新表述为对比学习问题，无需显式 RL 即可从人类反馈中学习。\\n    relevance_to_ced_stabilizer: >\\n      对比框架在 preference alignment 中的通用性。CED 可被视为 task-specific contrastive preference signal。\\n\\n  # === Category 4: Evidence-Based Rewards in IE/NLP ===\\n\\n  - title: \\\"Drift: Enhancing LLM Faithfulness in Rationale Generation\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: ACL 2025\\n    url: https://aclanthology.org/2025.acl-long.340.pdf\\n    category: evidence_reward\\n    role: related_method\\n    key_finding: >\\n      用 faithfulness reward 引导 LLM 生成更可靠的 rationale，提升 CoT 推理事实一致性。\\n    relevance_to_ced_stabilizer: >\\n      Faithfulness reward 用于生成质量的先例。CED 中 evidence discrimination\\n      本质上也是 faithfulness 信号——判断证据是否忠实支持抽取结果。\\n\\n  - title: \\\"Fine-Grained NLI-Based Faithfulness Evaluation for Diverse Summarisation Tasks (INFUSE)\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: EACL 2024\\n    url: https://aclanthology.org/2024.eacl-long.102/\\n    category: evidence_reward\\n    role: background\\n    key_finding: >\\n      变长前提+简化假设的细粒度 NLI faithfulness 评估，超越传统 NLI 在多任务摘要上的表现。\\n    relevance_to_ced_stabilizer: >\\n      NLI 作为 faithfulness 评估工具的进展。CED 中 NLI 组件用于判断 evidence 对 triple 的支持度。\\n\\n  - title: \\\"Enhancing Cross-Evidence Reasoning Graph for Document-Level Relation Extraction\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: PMC/Bioinformatics 2024\\n    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11232587/\\n    category: evidence_reward\\n    role: background\\n    key_finding: >\\n      文档级关系抽取中用 cross-evidence reasoning graph 增强跨证据推理。\\n    relevance_to_ced_stabilizer: >\\n      DocRE 中 evidence 的重要性。但用 evidence 作为模型输入特征，\\n      我们用 evidence quality 作为 RL reward 信号——定位根本不同。\\n\\n  # === Category 5: Multi-Objective RL for Text Generation ===\\n\\n  - title: \\\"Confronting Reward Model Overoptimization with Constrained RLHF\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: OpenReview\\n    url: https://openreview.net/forum?id=gkfUvn0fLU\\n    category: multi_objective_rl\\n    role: related_analysis\\n    key_finding: >\\n      多组件 RM 的 overoptimization 研究。component RM 间的相关性显著影响 overoptimization 临界点，\\n      用 constrained MDP 防止超出适当边界。\\n    relevance_to_ced_stabilizer: >\\n      CED 引入了与 extraction F1 低相关的 reward component（evidence quality），\\n      根据该论文分析低相关多组件 reward 更不易 overoptimize，\\n      可能是 CED 稳定性的另一个理论解释角度。\\n\\n  - title: \\\"On-Policy RL with Optimal Reward Baseline\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2505.23585\\n    url: https://arxiv.org/abs/2505.23585\\n    category: multi_objective_rl\\n    role: theoretical_support\\n    key_finding: >\\n      Optimal baseline 一致性地实现更高训练 reward 和更高 entropy，\\n      有效稳定训练并促进更多样的 policy exploration。\\n    relevance_to_ced_stabilizer: >\\n      CED reward 的多维特性可能起到类似 optimal baseline 效果——\\n      evidence quality 维度为 advantage estimation 提供更丰富的参照信号。\\n\\n  # === Category 6: RSFT Methodology & Theory ===\\n\\n  - title: \\\"A Minimalist Approach to LLM Reasoning: from Rejection Sampling to Reinforce\\\"\\n    authors: Xiao et al.\\n    year: 2025\\n    venue: arXiv 2504.11343\\n    url: https://arxiv.org/abs/2504.11343\\n    category: rsft_methodology\\n    role: key_theoretical_support\\n    key_finding: >\\n      RAFT（简单 rejection sampling baseline）在数学推理上与 GRPO/PPO 表现相当。\\n      消融实验表明 GRPO 的主要优势来自丢弃全错 prompt 而非 reward normalization。\\n      提出 Reinforce-Rej，在 RAFT 基础上过滤全对和全错 sample。\\n      关键洞察：GRPO 和 RAFT 的核心区别在于负样本处理——GRPO 混合正负样本训练，\\n      RAFT 只用正样本，但 RAFT 仍能达到相当性能，说明 rejection sampling 的简单性被低估了。\\n    relevance_to_rsft_docre: >\\n      直接支持我们的设计选择：(1) RSFT 在 DocRE 上成功而 GRPO 失败，\\n      与该论文发现一致——rejection sampling 的 offline 特性天然避免了 catastrophic forgetting；\\n      (2) GRPO 主要优势来自过滤全错 prompt，这与我们 RSFT 的 reward-based filtering 机制相同；\\n      (3) DocRE structured output 比 math reasoning 更难用 online RL 优化，\\n      强化了 offline RSFT 的合理性。\\n\\n  - title: \\\"Beyond Rejection Sampling: Trajectory Fusion for Scaling Mathematical Reasoning (TrajFusion)\\\"\\n    authors: Jie Deng et al.\\n    year: 2026\\n    venue: arXiv 2602.04391\\n    url: https://arxiv.org/abs/2602.04391\\n    category: rsft_methodology\\n    role: method_component\\n    key_finding: >\\n      传统 RSFT 只用正确轨迹，丢弃错误轨迹。TrajFusion 将错误和正确轨迹交替拼接，\\n      显式建模试错推理过程，在困难数学问题上显著超越标准 RFT。\\n    relevance_to_rsft_docre: >\\n      Future work 方向：可考虑在 DocRE RSFT 中融合失败样本的信息。\\n      但 DocRE 的结构化输出（JSON triple）不同于 math 的 chain-of-thought，\\n      融合方式需要重新设计。\\n\\n  - title: \\\"Rejection Sampling Based Fine Tuning Secretly Performs PPO\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: ICML 2025\\n    url: https://openreview.net/forum?id=yQ2UivKlir\\n    category: rsft_methodology\\n    role: theoretical_support\\n    key_finding: >\\n      建立 RSFT 与 PPO 之间的理论联系：rejection sampling fine-tuning\\n      在特定条件下隐式执行 PPO with marginal KL constraints。\\n    relevance_to_rsft_docre: >\\n      为 RSFT 的有效性提供理论解释。我们的 RSFT 成功可被视为\\n      隐式执行了 constrained policy optimization，\\n      避免了显式 GRPO 在 structured output 上的不稳定性。\\n\\n  # === Category 7: RL for Information Extraction ===\\n\\n  - title: \\\"R1-RE: Cross-Domain Relation Extraction with RLVR\\\"\\n    authors: Runpeng Dai, Tong Zheng et al.\\n    year: 2025\\n    venue: arXiv 2507.04642\\n    url: https://arxiv.org/abs/2507.04642\\n    category: rl_for_ie\\n    role: direct_competitor\\n    key_finding: >\\n      首个将 RLVR（GRPO + verifiable reward）用于关系抽取的框架。\\n      将 RE 重构为推理任务，R1-RE-7B 在跨域 OOD 准确率约 70%，媲美 GPT-4o。\\n      Reward 设计：format reward (+1/-3) + metric reward (+2/-1.5)，先验证格式再加准确度。\\n      triplet extraction 用 F1-based reward（entity weight=1, triplet weight=3）。\\n      未报告 catastrophic forgetting——GRPO 训练后在 MATH-500/IFEval/GPQA 上性能不降反升，\\n      说明句子级 RE 的简单 reward 结构足以稳定 GRPO 训练。\\n    results:\\n      sem2010_in_domain: 91.8\\n      sem2010_ood: 66.5\\n      mdkg_in_domain: 88.1\\n      mdkg_ood: 65.8\\n    evidence_generation: false\\n    relevance_to_rsft_docre: >\\n      最直接竞争者。关键差异与讨论：\\n      (1) R1-RE 是句子级 RE，GRPO 成功；我们是文档级 RE，GRPO 失败→RSFT 成功。\\n      句子级 RE 每个 sample 只有 1 个 triple（binary classification），reward variance 天然充足；\\n      文档级 RE 每个 sample 有数十个 triple，F1 score 作为 reward 在 group 内趋于同质化（frac_zero_std→0.8）。\\n      (2) R1-RE 未报告 catastrophic forgetting，进一步支持\\\"句子级简单 reward 可行，文档级需要 CED\\\"的论点。\\n      (3) R1-RE 关注 OOD 泛化，无 evidence 组件；我们关注 evidence-grounded extraction quality。\\n      互补而非直接冲突——R1-RE 证明 RLVR for RE 可行，我们揭示文档级需要额外设计。\\n\\n  - title: \\\"MORE-R1: Guiding LVLM for Multimodal Object-Entity Relation Extraction via Stepwise Reasoning with RL\\\"\\n    authors: Anonymous\\n    year: 2026\\n    venue: arXiv 2603.09478\\n    url: https://arxiv.org/abs/2603.09478\\n    category: rl_for_ie\\n    role: related_method\\n    key_finding: >\\n      多模态 RE 中用 GRPO + Progressive Sample-Mixing Strategy 优化 LVLM 推理能力。\\n      两阶段训练：SFT cold-start + GRPO RL。\\n    relevance_to_rsft_docre: >\\n      跨模态验证 RL for RE 趋势。其 Progressive Sample-Mixing 与我们\\n      RSFT 的 difficulty-aware sampling 思想相通，但在不同模态。\\n\\n  - title: \\\"REAR: Reinforced Reasoning Optimization for Event Argument Extraction with Relation-Aware Support\\\"\\n    authors: Jianwen Luo et al.\\n    year: 2025\\n    venue: EMNLP 2025 Findings\\n    url: https://2025.emnlp.org/program/find_papers/\\n    category: rl_for_ie\\n    role: related_method\\n    key_finding: >\\n      将强化学习推理优化用于事件论元抽取，结合关系感知支持。\\n      不同于 DocRE 但同属 IE 领域的 RL 应用。\\n    relevance_to_rsft_docre: >\\n      验证 RL 在 IE 任务上的有效性趋势。我们的工作扩展到 DocRE + evidence，\\n      且使用 offline RSFT 而非 online RL。\\n\\n  - title: \\\"Adaptive Reinforcement Learning Planning: Harnessing LLMs for Complex Information Extraction\\\"\\n    authors: Zepeng Ding et al.\\n    year: 2024\\n    venue: arXiv 2406.11455\\n    url: https://arxiv.org/abs/2406.11455\\n    category: rl_for_ie\\n    role: background\\n    key_finding: >\\n      将 LLM 顺序抽取建模为 MDP，用 DDQN 训练 decision module\\n      自适应选择实体抽取顺序，提升复杂 IE 性能。\\n    relevance_to_rsft_docre: >\\n      RL for IE 的早期工作。用 RL 优化抽取策略而非模型本身，\\n      与我们 RSFT 直接微调 LLM 的方法路径不同。\\n\\n  - title: \\\"Graph-R1: Towards Agentic GraphRAG Framework via End-to-end Reinforcement Learning\\\"\\n    authors: Haoran Luo et al.\\n    year: 2025\\n    venue: ICML 2026\\n    url: https://arxiv.org/abs/2507.21892\\n    category: rl_for_ie\\n    role: background\\n    key_finding: >\\n      用端到端 RL 优化 GraphRAG agent 的多轮检索-推理循环，\\n      包含 knowledge hypergraph construction（n-ary relation extraction）。\\n    relevance_to_rsft_docre: >\\n      RL + knowledge extraction 的交叉点。Graph-R1 关注 QA 场景下的知识图谱构建，\\n      我们关注 DocRE 的训练优化，应用场景不同。\\n\\n  # === Category 8: Recent LLM-based DocRE Methods ===\\n\\n  - title: \\\"RelPrior: Relation as a Prior - A Novel Paradigm for LLM-based Document-level Relation Extraction\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2511.08143\\n    url: https://arxiv.org/abs/2511.08143\\n    category: llm_docre\\n    role: key_baseline\\n    key_finding: >\\n      用 binary relation 作为先验过滤无关实体对，再用 predefined relation 匹配实体，\\n      避免 LLM 在 DocRE 中被无关实体对分散注意力。\\n      在 DocRED/Re-DocRED 上超越现有纯 LLM-based DocRE 方法。\\n    results:\\n      docred_dev_f1: 47.82\\n      docred_test_f1: 48.34\\n      re_docred_dev_f1: 55.94\\n      re_docred_test_f1: 54.80\\n      backbone: LLaMA3-8B\\n    evidence_generation: false\\n    relevance_to_rsft_docre: >\\n      我们的直接 baseline 之一。RelPrior_LLaMA3-8B 在 DocRED test F1=48.34,\\n      Re-DocRED test F1=54.80。我们的 RSFT 提升显著更优。\\n      RelPrior 是 inference paradigm 创新（两阶段筛选），我们是 training paradigm 创新（RSFT+CED），正交互补。\\n\\n  - title: \\\"LMRC: LLM with Relation Classifier for Document-Level Relation Extraction\\\"\\n    authors: Xingzuo Li, Kehai Chen, Yunfei Long, Min Zhang\\n    year: 2024\\n    venue: arXiv 2408.13889\\n    url: https://arxiv.org/abs/2408.13889\\n    category: llm_docre\\n    role: related_method\\n    key_finding: >\\n      两阶段方法：先用 attention-based classifier 过滤 NA 实体对（RCP），\\n      再用 LLM 在精简候选空间中做多分类（RC）。\\n      注意：LMRC 依赖 BERT-based classifier 作为预筛选，非纯 LLM 方法。\\n    results:\\n      docred_dev_ign_f1: 58.16\\n      docred_dev_f1: 59.97\\n      docred_test_ign_f1: 58.49\\n      docred_test_f1: 60.52\\n      re_docred_test_ign_f1: 74.08\\n      re_docred_test_f1: 74.63\\n      backbone: BERT classifier + LLM\\n    evidence_generation: false\\n    relevance_to_rsft_docre: >\\n      LMRC 在 DocRED test F1=60.52, Re-DocRED test F1=74.63，性能显著高于纯 LLM 方法。\\n      但它依赖 BERT classifier 预筛选，本质上是 hybrid 方法而非纯 LLM generative。\\n      与我们端到端 LLM 生成方式不同——我们通过 RSFT 的 reward-based filtering 隐式解决 class imbalance。\\n\\n  - title: \\\"Ru-LLM: Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: NLPCC 2025\\n    url: https://link.springer.com/chapter/10.1007/978-981-95-3343-5_11\\n    category: llm_docre\\n    role: related_method\\n    key_finding: >\\n      用频繁模式挖掘 + MCTS 搜索逻辑规则，转化为 prompt 约束 LLM 输出，\\n      再用 CoT 验证过滤不满足规则的 triple。\\n      在 DWIE、DocRED、Re-DocRED 上声称超越现有 LLM 方法和规则框架。\\n      具体 F1 未公开获取（Springer 付费墙），但声称超越 AutoRE 等 LLM baseline。\\n    results:\\n      note: \\\"behind Springer paywall; claims SOTA over LLM baselines on DocRED/Re-DocRED/DWIE\\\"\\n    evidence_generation: false\\n    relevance_to_rsft_docre: >\\n      规则约束方式与我们的 CED reward 在 motivation 上相似（都是引入外部知识约束），\\n      但 Ru-LLM 用 inference-time 规则验证（MCTS+CoT），我们用 training-time reward shaping（CED）。\\n      Ru-LLM 的规则是数据集级别的频繁模式，CED 是 instance-level 的 evidence faithfulness。\\n\\n  - title: \\\"GLiDRE: Generalist Lightweight model for Document-level Relation Extraction\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2508.00757\\n    url: https://arxiv.org/abs/2508.00757\\n    category: llm_docre\\n    role: background\\n    key_finding: >\\n      基于 dual-encoder 的轻量级零/少样本 DocRE 模型，\\n      预训练于 136K 文档的大规模 RE 数据。\\n      fully supervised Re-DocRED test F1=77.83，但这是 encoder-based 非 LLM generative。\\n      zero-shot Re-DocRED test F1=17.32（超越 LLaMA 3.3 70B 和 Mistral-Small 24B）。\\n    results:\\n      re_docred_dev_f1: 77.76\\n      re_docred_test_f1: 77.83\\n      re_docred_zero_shot_test_f1: 17.32\\n      fredo_in_domain_1doc_f1: 13.00\\n      fredo_in_domain_3doc_f1: 15.71\\n      backbone: \\\"dual-encoder (few hundred M params)\\\"\\n    evidence_generation: false\\n    relevance_to_rsft_docre: >\\n      不同范式（encoder-based vs LLM generative）。GLiDRE 的 fully supervised F1=77.83\\n      远超 LLM-based 方法（RelPrior 54.80），但依赖大规模预训练数据和 encoder 架构。\\n      与我们不直接可比——我们关注 LLM generative 范式下的训练优化。\\n\\n  - title: \\\"AutoRE: Document-Level Relation Extraction with Large Language Models\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: arXiv 2403.14888\\n    url: https://arxiv.org/abs/2403.14888\\n    category: llm_docre\\n    role: background\\n    key_finding: >\\n      RHF（Relation-Head-Facts）范式用 Mistral-7B + QLoRA 做端到端 DocRE。\\n      关键设计：先抽 relation，再抽 head entity，最后抽 fact triple。\\n    results:\\n      re_docred_dev_f1_mistral: 53.01\\n      re_docred_test_f1_mistral: 51.91\\n      re_docred_dev_f1_vicuna: 54.29\\n      re_docred_test_f1_vicuna: 53.84\\n      docred_dev_f1_llama3: 45.76\\n      docred_test_f1_llama3: 45.96\\n      re_docred_dev_f1_llama3: 52.28\\n      re_docred_test_f1_llama3: 51.97\\n      backbone: \\\"Mistral-7B / Vicuna-7B / LLaMA3-8B (QLoRA)\\\"\\n    evidence_generation: false\\n    relevance_to_rsft_docre: >\\n      QLoRA fine-tuning for DocRE 的先例。AutoRE_LLaMA3-8B 在 Re-DocRED test F1=51.97,\\n      DocRED test F1=45.96。我们的 SFT baseline 与之类似，\\n      RSFT 在此基础上引入 reward-guided sample selection 进一步提升。\\n\\n  # === Category 9: Evidence Generation & Task Performance Trade-off ===\\n  # (NEW - 2026-05-15 evidence generation survey)\\n\\n  - title: \\\"Mind Your Step (by Step): Chain-of-Thought can Reduce Performance on Tasks where Thinking Makes Humans Worse\\\"\\n    authors: Sprague et al.\\n    year: 2024\\n    venue: NeurIPS 2024\\n    url: https://arxiv.org/abs/2410.21333\\n    category: evidence_generation_tradeoff\\n    role: key_evidence\\n    key_finding: >\\n      CoT 在某些任务上降低性能高达 36.3%（o1-preview vs GPT-4o）。\\n      显式推理步骤引入 error accumulation，且模型可能 overfit 到解释格式而非任务结构。\\n      隐式推理（hidden activations）在分布偏移下优于显式 token-level 推理。\\n    relevance_to_evidence_tradeoff: >\\n      直接支持我们的核心发现：要求模型同时生成 evidence sentences 是一种\\\"显式推理\\\"，\\n      会对主任务（RE）产生性能代价（~8pp F1 下降）。\\n      Related Work 引用点：evidence generation 作为 structured explanation，\\n      与 CoT 共享\\\"显式推理降低主任务性能\\\"的普遍模式。\\n\\n  - title: \\\"Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion\\\"\\n    authors: Xie et al. (Google Research)\\n    year: 2022\\n    venue: ACL Findings 2022\\n    url: https://arxiv.org/abs/2106.08657\\n    category: evidence_generation_tradeoff\\n    role: closest_docre_precedent\\n    key_finding: >\\n      Joint 训练 RE + evidence extraction，关键创新在 inference-stage fusion：\\n      分别在 extracted evidence 和 full document 上做 RE 预测再通过 blending layer 融合。\\n      DocRED 上提升 1.37 Ign F1。Silver evidence labels（启发式规则构建）即可提升 RE 性能。\\n    relevance_to_evidence_tradeoff: >\\n      最直接的 DocRE + evidence 先例。EIDER 的核心洞察是 evidence 需要 inference-stage 融合\\n      而非 joint generation——暗示 joint generation 会引入 noise。\\n      我们的 CED reranker 是 LLM-era 版本的 inference-stage fusion：\\n      先生成多个候选（含 evidence），再用 NLI 在推理阶段选最佳。\\n      Related Work 引用点：encoder-based DocRE 中 evidence 的使用方式，与我们 generative 范式的关键差异。\\n\\n  - title: \\\"Exploring the Trade-off Between Model Performance and Explanation Plausibility of Text Classifiers Using Human Rationales\\\"\\n    authors: Resck, Raimundo, Poco\\n    year: 2024\\n    venue: NAACL Findings 2024\\n    url: https://arxiv.org/abs/2404.03098\\n    category: evidence_generation_tradeoff\\n    role: formal_framework\\n    key_finding: >\\n      用 multi-objective optimization 探索 performance vs explanation plausibility 的 Pareto frontier。\\n      引入 rationale 约束创建 contrastive loss，证实加入 rationale supervision 会降低主任务性能，\\n      但存在 Pareto optimal 解平衡两者。\\n    relevance_to_evidence_tradeoff: >\\n      提供了 performance-explainability trade-off 的形式化框架。\\n      我们的 evidence-grounded RE 降 8pp 正是 Pareto frontier 上的一个点。\\n      CED reranker 的效果可解读为：将系统从 evidence-constrained 点推向 Pareto frontier，\\n      在几乎不牺牲 evidence quality（evi_f1=0.8188）的前提下恢复 RE 性能。\\n      Related Work 引用点：evidence generation 的 performance cost 有理论依据。\\n\\n  - title: \\\"The Decreasing Value of Chain of Thought in Prompting\\\"\\n    authors: Meincke, Mollick, Mollick, Shapiro\\n    year: 2025\\n    venue: Wharton Generative AI Labs Technical Report (SSRN)\\n    url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5285532\\n    category: evidence_generation_tradeoff\\n    role: empirical_support\\n    key_finding: >\\n      现代 reasoning models 上 CoT 收益微弱（4-13%），但 latency 增加 35-600%。\\n      更强的模型从显式推理中受益越少。CoT 可能在 easy questions 上引入 errors\\n      （variability 增加导致原本正确的被改错）。\\n    relevance_to_evidence_tradeoff: >\\n      支持\\\"更强的 SFT 模型不需要在生成时显式输出 evidence\\\"的论点。\\n      我们的 evidence-only SFT 的性能下降符合\\\"显式推理的边际收益递减\\\"模式。\\n      Related Work 引用点：evidence generation 的 accuracy cost 不是 DocRE-specific，而是 LLM 的普遍趋势。\\n\\n  # === Category 10: Negative Transfer in Multi-task / Auxiliary-task Learning ===\\n\\n  - title: \\\"ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning\\\"\\n    authors: Jiang, Chen et al.\\n    year: 2023\\n    venue: NeurIPS 2023\\n    url: https://arxiv.org/abs/2301.12618\\n    category: negative_transfer\\n    role: theoretical_framework\\n    key_finding: >\\n      辅助任务常导致 negative transfer，根因不仅是 gradient conflict 还有 auxiliary-target\\n      generalization gap。ForkMerge 周期性 fork 模型为多分支，搜索最优 task weights，\\n      动态 merge 过滤有害 task-parameter updates。在多个 benchmark 上减少 negative transfer。\\n    relevance_to_evidence_tradeoff: >\\n      Evidence generation 作为 auxiliary task 对 RE 的 negative transfer 可用此框架解释：\\n      evidence 和 RE 的 gradient 方向不完全对齐，joint training 时 evidence 任务\\\"拖累\\\"RE。\\n      CED reranker 本质上是将 evidence quality 从 training-time joint objective 解耦到\\n      inference-time verification，避免了 training-time 的 negative transfer。\\n      Related Work 引用点：auxiliary task 导致主任务性能下降的一般性理论。\\n\\n  # === Category 11: Faithfulness vs Accuracy / Correctness Trade-off ===\\n\\n  - title: \\\"Correctness is not Faithfulness in RAG Attributions\\\"\\n    authors: Wallat, Heuss, de Rijke, Anand\\n    year: 2024\\n    venue: SIGIR 2025\\n    url: https://arxiv.org/abs/2412.18004\\n    category: faithfulness_accuracy_tradeoff\\n    role: key_conceptual_framework\\n    key_finding: >\\n      Correctness 和 faithfulness 是独立维度，可能冲突。高达 57% 的 citations 是\\n      post-rationalized（事后编造而非真实依据）。Unfaithful attributions 可能 factually correct，\\n      但 foster misguided trust。必须同时检查 correctness 和 faithfulness。\\n    relevance_to_evidence_tradeoff: >\\n      直接相关。我们的 evidence-grounded RE 试图让模型输出 faithful evidence，\\n      但这与 relation correctness 产生张力（rel_f1 降 8pp）。\\n      CED reranker 通过 NLI verification 确保 evidence 是 faithful 的（非 post-rationalized），\\n      同时不牺牲 RE accuracy。\\n      Related Work 引用点：correctness-faithfulness 分离的概念框架。\\n\\n  - title: \\\"Evaluating Correctness and Faithfulness of Instruction-Following Models for Question Answering\\\"\\n    authors: Adlakha, BehnamGhader, Lu, Meade, Reddy\\n    year: 2024\\n    venue: TACL 2024\\n    url: https://arxiv.org/abs/2307.16877\\n    category: faithfulness_accuracy_tradeoff\\n    role: evaluation_framework\\n    key_finding: >\\n      Instruction-following LLMs 在 correctness 上表现可比 fine-tuned models，\\n      但 faithfulness 普遍较差——模型会 hallucinate 而非忠实于提供的 evidence。\\n      传统 metrics 对 correctness 和 faithfulness 的评估均有缺陷。\\n    relevance_to_evidence_tradeoff: >\\n      解释了为什么 joint evidence+RE 生成性能差——模型在同时优化 correctness\\n      和 faithfulness 时，两个目标存在张力。单纯要求模型\\\"同时输出正确 triples 和\\n      faithful evidence\\\"是 multi-objective optimization 问题。\\n      Related Work 引用点：correctness vs faithfulness 评估方法论。\\n\\n  - title: \\\"Towards Faithful Model Explanation in NLP: A Survey\\\"\\n    authors: Lyu, Havaldar, Stein et al.\\n    year: 2024\\n    venue: Computational Linguistics (MIT Press)\\n    url: https://aclanthology.org/2024.cl-2.6/\\n    category: faithfulness_accuracy_tradeoff\\n    role: comprehensive_survey\\n    key_finding: >\\n      系统综述 NLP 中 faithful explanation 的定义、评估和生成方法。\\n      识别了 faithfulness-performance trade-off 作为核心挑战：\\n      更 faithful 的解释不一定更有用，更有用的解释不一定 faithful。\\n      提出未来方向包括 multi-objective optimization 和 post-hoc verification。\\n    relevance_to_evidence_tradeoff: >\\n      权威综述为我们的 evidence generation trade-off 提供广泛文献背景。\\n      我们的 CED reranker 正是该综述建议的\\\"post-hoc verification\\\"方向的具体实例。\\n      Related Work 引用点：faithfulness 研究的全景综述，定位我们的工作。\\n\\n  # === Category 12: Reranking / Verification as Bridge ===\\n\\n  - title: \\\"Genie: Achieving Human Parity in Content-Grounded Datasets Generation\\\"\\n    authors: Yehudai, Carmeli, Mass et al.\\n    year: 2024\\n    venue: ICLR 2024\\n    url: https://arxiv.org/abs/2401.14367\\n    category: reranking_verification_bridge\\n    role: methodological_precedent\\n    key_finding: >\\n      三阶段流程：Content Preparation → Generation → NLI-based Filtering。\\n      用 fine-tuned T5-11B NLI 模型判断生成内容是否 entailed by source（faithfulness 检验），\\n      过滤不 faithful 的生成。在 LFQA、摘要、IE 上达到 human parity。\\n    relevance_to_evidence_tradeoff: >\\n      方法论上最接近我们的 CED reranker——都是用 NLI verification 作为 post-hoc filter/reranker，\\n      在不牺牲主任务质量的前提下确保 grounding quality。\\n      GENIE 验证了 NLI-based filtering 在内容生成中的有效性。\\n      关键差异：GENIE 是 data generation pipeline 的过滤，我们是 inference-time reranking。\\n      Related Work 引用点：NLI-based verification 作为 bridge 的成功先例。\\n\", \"total_chars\": 29337, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "bc70a0f6-c34e-4a4a-ae09-877da104cb48",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml\\\", \\\"content\\\": \\\"# Literature Map for faith-evidence-ie (FREIGE)\\\\n# Focus: CED-as-training-stabilizer (D024) + RSFT for DocRE\\\\n# Updated: 2026-05-15 (W3 reviewer gap fill + evidence generation trade-off survey)\\\\n\\\\npapers:\\\\n\\\\n  # === Category 1: Reward Diversity / Reward Shaping for RL Stability ===\\\\n\\\\n  - title: \\\\\\\"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization\\\\\\\"\\\\n    authors: NVIDIA Labs\\\\n    year: 2025\\\\n    venue: ICML 2026\\\\n    url: https://arxiv.org/abs/2601.05242\\\\n    category: reward_diversity\\\\n    role: closest_prior_work\\\\n    key_finding: >\\\\n      直接将 GRPO 应用于多 reward 组合时，不同 rollout 的 reward 组合在归一化后 collapse 为相同 advantage 值，\\\\n      降低训练信号分辨率导致收敛失败。GDPO 对每个 reward 独立做 group-wise normalization 再聚合，\\\\n      保留多 reward 的相对差异，显著提升训练稳定性。\\\\n    relevance_to_ced_stabilizer: >\\\\n      最直接相关。CED reward 本质上引入了独立于 extraction F1 的 reward 维度（evidence quality），\\\\n      GDPO 的理论分析解释了为什么多维 reward 比单一 reward 更稳定——独立 reward 维度防止 advantage collapse。\\\\n      但 GDPO 是方法论贡献，CED 是 task-specific reward 设计自然具备了这一特性。\\\\n\\\\n  - title: \\\\\\\"DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of LLMs\\\\\\\"\\\\n    authors: Xiwen Chen et al.\\\\n    year: 2025\\\\n    venue: arXiv 2505.09655\\\\n    url: https://arxiv.org/abs/2505.09655\\\\n    category: reward_diversity\\\\n    role: related_method\\\\n    key_finding: >\\\\n      GRPO 的标量 reward 无法区分语义多样但得分相同的输出（diversity-quality inconsistency）。\\\\n      DRA 用子模互信息（SMI）对 reward 加权，给多样性高的 completion 更大权重，\\\\n      等价于 Inverse Propensity Scoring 去偏，防止 policy 坍缩到先验模式。\\\\n    relevance_to_ced_stabilizer: >\\\\n      DRA 通过后处理 reward 注入多样性信号；CED 的 reward 本身就内含对比结构自然提供 diversity 信号。\\\\n      机制互补但来源不同——CED 是 reward design 层面，DRA 是 optimization 层面。\\\\n\\\\n  - title: \\\\\\\"Shrinking the Variance: Shrinkage Baselines for RL with Verifiable Rewards\\\\\\\"\\\\n    authors: Guanning Zeng et al.\\\\n    year: 2025\\\\n    venue: arXiv 2511.03710\\\\n    url: https://arxiv.org/abs/2511.03710\\\\n    category: reward_diversity\\\\n    role: theoretical_support\\\\n    key_finding: >\\\\n      RLVR 中 per-prompt 均值 baseline 在低 generation 数下估计不准导致高 variance 梯度。\\\\n      用 James-Stein shrinkage 混合 per-prompt 和 cross-prompt 均值，\\\\n      构造可证明更低 variance 的 policy gradient estimator。\\\\n    relevance_to_ced_stabilizer: >\\\\n      理论支持：reward variance 对 gradient estimation 质量至关重要。\\\\n      CED 的额外 reward 维度提供更丰富的 per-group variance，间接起到 variance 维持效果。\\\\n\\\\n  - title: \\\\\\\"Reward Shaping to Mitigate Reward Hacking in RLHF\\\\\\\"\\\\n    authors: Anonymous\\\\n    year: 2025\\\\n    venue: arXiv 2502.18770\\\\n    url: https://arxiv.org/abs/2502.18770\\\\n    category: reward_diversity\\\\n    role: background\\\\n    key_finding: >\\\\n      RL reward 应有界且先快速增长后缓慢收敛。系统研究 reward shaping 原则，\\\\n      好的 reward 形状能抑制 reward hacking 并提升训练稳定性。\\\\n    relevance_to_ced_stabilizer: >\\\\n      CED reward 的 0-1 对比判别结构天然满足有界性，\\\\n      且 evidence quality 的渐进提升符合\\\\\\\"先快后慢\\\\\\\"的 reward shaping 原则。\\\\n\\\\n  # === Category 2: Mode Collapse Prevention in GRPO/RLHF ===\\\\n\\\\n  - title: \\\\\\\"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\\\\\\\"\\\\n    authors: ByteDance Seed, Tsinghua AIR\\\\n    year: 2025\\\\n    venue: NeurIPS 2025\\\\n    url: https://arxiv.org/abs/2503.14476\\\\n    category: mode_collapse_prevention\\\\n    role: key_baseline\\\\n    key_finding: >\\\\n      Naive GRPO 存在 entropy collapse（policy 熵快速下降→输出同质化）。\\\\n      根因：clipping 不对称性——概率 0.01 的 token 最多增到 0.012，而概率 0.9 的 token 可达 1.08，\\\\n      低概率 token 难以增长，抑制探索。DAPO 提出 Clip-Higher（εhigh=0.28 > εlow=0.2）\\\\n      为低概率 token 留更大增长空间，加 Dynamic Sampling 过滤 accuracy=0 或 1 的 prompt\\\\n      （这些 prompt 产生零梯度，降低有效 batch size）。在 AIME 2024 达 50 分超越 DeepSeek-R1-Zero。\\\\n    relevance_to_ced_stabilizer: >\\\\n      DAPO 从 optimization 技巧角度解决 entropy collapse。CED reward 从 reward design 层面\\\\n      防止 mode collapse——evidence quality 维度确保 reward 组内有足够 variance，\\\\n      不会出现 all-same-reward 的零梯度 prompt。DAPO 的 Dynamic Sampling 过滤 accuracy=0/1 prompt\\\\n      与我们观察到的 frac_zero_std→0.8 现象本质相同：extraction-only reward 下大量 prompt\\\\n      产生零 advantage，CED 从源头（reward 设计）而非后处理（过滤）解决这个问题。\\\\n\\\\n  - title: \\\\\\\"Dr. GRPO: Removing Optimization Bias in GRPO\\\\\\\"\\\\n    authors: Liu et al.\\\\n    year: 2025\\\\n    venue: COLM 2025\\\\n    url: https://arxiv.org/abs/2503.20783\\\\n    category: mode_collapse_prevention\\\\n    role: related_analysis\\\\n    key_finding: >\\\\n      GRPO 的 std 归一化引入两个 bias：(1) difficulty bias——std(r) 归一化对低 variance 组\\\\n      （全对/全错）给予过高 advantage 权重，trivial question 主导训练信号；\\\\n      (2) length bias——per-token loss 的 1/|o_i| 项使长的错误回答被 under-penalize。\\\\n      当 std(r)→0 时 advantage 爆炸或未定义，梯度数值不稳定。\\\\n      Dr. GRPO 移除 std 归一化，用无偏 Monte Carlo advantage：Ã = R(q,o_i) - mean(R)。\\\\n    relevance_to_ced_stabilizer: >\\\\n      与我们的实验发现高度一致：extraction-only reward 下 frac_zero_std→0.8 正是\\\\n      Dr. GRPO 分析的 difficulty bias 极端情况——大量 prompt 的所有 rollout 得到相同 F1，\\\\n      std→0 导致 advantage 异常。CED 通过增加 reward 维度天然维持 reward_std>0，\\\\n      从 reward 设计而非算法修改角度避免了 Dr. GRPO 发现的 bias。\\\\n\\\\n  - title: \\\\\\\"GVPO: Group Variance Policy Optimization for LLM Post-Training\\\\\\\"\\\\n    authors: Anonymous\\\\n    year: 2025\\\\n    venue: NeurIPS 2025\\\\n    url: https://arxiv.org/abs/2504.19599\\\\n    category: mode_collapse_prevention\\\\n    role: alternative_framework\\\\n    key_finding: >\\\\n      将 KL 约束 reward 最大化的解析解直接嵌入梯度权重，\\\\n      variance 项自然平衡 exploration 与 exploitation，维持适度 entropy。\\\\n    relevance_to_ced_stabilizer: >\\\\n      GVPO 的 variance 项机制与 CED 维持 reward variance 的效果功能类似，\\\\n      但 GVPO 是算法层面 implicit regularization，CED 是 reward 层面 explicit structure。\\\\n\\\\n  - title: \\\\\\\"REINFORCE++: Stabilizing Critic-Free Policy Optimization with Global Advantage Normalization\\\\\\\"\\\\n    authors: Jian Hu et al.\\\\n    year: 2025\\\\n    venue: arXiv 2501.03262\\\\n    url: https://arxiv.org/abs/2501.03262\\\\n    category: mode_collapse_prevention\\\\n    role: related_method\\\\n    key_finding: >\\\\n      Prompt-level (local) advantage normalization 导致不准确估计和过拟合。\\\\n      Global batch normalization 提供更稳定、理论无偏的 gradient estimator。\\\\n    relevance_to_ced_stabilizer: >\\\\n      解决 local normalization 的 variance 问题；CED 从 reward 端增加 variance 来源。\\\\n      两者在不同层面解决同一问题：防止 gradient signal 消失。\\\\n\\\\n  - title: \\\\\\\"DiverseGRPO: Mitigating Mode Collapse in Image Generation via Diversity-Aware GRPO\\\\\\\"\\\\n    authors: Henglin Liu et al.\\\\n    year: 2025\\\\n    venue: arXiv 2512.21514\\\\n    url: https://arxiv.org/abs/2512.21514\\\\n    category: mode_collapse_prevention\\\\n    role: parallel_work\\\\n    key_finding: >\\\\n      图像生成中 GRPO 后期输出同质化。distributional reward modeling（谱聚类+exploratory reward）\\\\n      和 structure-aware regularization 实现 13-18% 语义多样性提升。\\\\n    relevance_to_ced_stabilizer: >\\\\n      跨域验证了 GRPO mode collapse 的普遍性，distributional reward 思路与 CED 精神相近——\\\\n      都是通过 reward 层面结构化信号维持输出多样性。\\\\n\\\\n  - title: \\\\\\\"Why GRPO Needs Normalization: A Local-Curvature Perspective on Adaptive Gradients\\\\\\\"\\\\n    authors: Anonymous\\\\n    year: 2025\\\\n    venue: arXiv 2601.23135\\\\n    url: https://arxiv.org/abs/2601.23135\\\\n    category: mode_collapse_prevention\\\\n    role: theoretical_support\\\\n    key_finding: >\\\\n      GRPO 的 reward_std 归一化在温和条件下提供严格优于未归一化 REINFORCE 的收敛速率，\\\\n      收益由 prompt 间平均 reward std 刻画。\\\\n    relevance_to_ced_stabilizer: >\\\\n      直接理论支撑：reward_std 越大收敛越好。CED 通过 evidence quality 维度维持高 reward_std，\\\\n      从该理论看 CED 的稳定性优势是 reward_std 维持带来的收敛速率优势。\\\\n\\\\n  # === Category 3: Contrastive Rewards in RL ===\\\\n\\\\n  - title: \\\\\\\"Improving Reinforcement Learning from Human Feedback Using Contrastive Rewards\\\\\\\"\\\\n    authors: Shen, Zhang et al.\\\\n    year: 2024\\\\n    venue: arXiv 2403.07708\\\\n    url: https://arxiv.org/abs/2403.07708\\\\n    category: contrastive_reward\\\\n    role: closest_contrastive_precedent\\\\n    key_finding: >\\\\n      两步机制：(1) 离线采样 baseline response；(2) 用 baseline 计算 contrastive reward\\\\n      作为 PPO 的 penalty 项。效果：惩罚 reward uncertainty、根据任务难度自适应校准、\\\\n      减少 PPO 中的 variance。在 TL;DR 和 HH-RLHF 上持续优于标准 RLHF。\\\\n    relevance_to_ced_stabilizer: >\\\\n      最接近的对比 reward 先例。关键差异：(1) 它是对 learned RM 输出的后处理对比，\\\\n      CED 是 reward function 本身就是对比判别（evidence vs. corrupted evidence）；\\\\n      (2) 它在 PPO 中验证，CED 在 GRPO 中验证；\\\\n      (3) 它是 domain-agnostic penalty，CED 是 task-specific faithfulness signal。\\\\n      stabilizing 机制相通但实现路径根本不同。\\\\n\\\\n  - title: \\\\\\\"Improving Discriminative Capability of Reward Models in RLHF Using Contrastive Learning\\\\\\\"\\\\n    authors: Anonymous\\\\n    year: 2024\\\\n    venue: EMNLP 2024\\\\n    url: https://aclanthology.org/2024.emnlp-main.852/\\\\n    category: contrastive_reward\\\\n    role: related_method\\\\n    key_finding: >\\\\n      无监督对比损失训练 reward model 充分捕捉对比数据区分度，\\\\n      带来更稳定的 PPO 训练 return 和 reward。\\\\n    relevance_to_ced_stabilizer: >\\\\n      验证对比训练 reward model → 更稳定 RL 训练链条。CED 不是对比训练 reward model，\\\\n      而是 reward function 本身就是对比判别，但 stabilizing 机制相通。\\\\n\\\\n  - title: \\\\\\\"Contrastive Preference Learning: Learning from Human Feedback without RL\\\\\\\"\\\\n    authors: Anonymous\\\\n    year: 2024\\\\n    venue: ICLR 2025\\\\n    url: https://openreview.net/forum?id=iX1RjVQODj\\\\n    category: contrastive_reward\\\\n    role: background\\\\n    key_finding: >\\\\n      将 preference learning 重新表述为对比学习问题，无需显式 RL 即可从人类反馈中学习。\\\\n    relevance_to_ced_stabilizer: >\\\\n      对比框架在 preference alignment 中的通用性。CED 可被视为 task-specific contrastive preference signal。\\\\n\\\\n  # === Category 4: Evidence-Based Rewards in IE/NLP ===\\\\n\\\\n  - title: \\\\\\\"Drift: Enhancing LLM Faithfulness in Rationale Generation\\\\\\\"\\\\n    authors: Anonymous\\\\n    year: 2025\\\\n    venue: ACL 2025\\\\n    url: https://aclanthology.org/2025.acl-long.340.pdf\\\\n    category: evidence_reward\\\\n    role: related_method\\\\n    key_finding: >\\\\n      用 faithfulness reward 引导 LLM 生成更可靠的 rationale，提升 CoT 推理事实一致性。\\\\n    relevance_to_ced_stabilizer: >\\\\n      Faithfulness reward 用于生成质量的先例。CED 中 evidence discrimination\\\\n      本质上也是 faithfulness 信号——判断证据是否忠实支持抽取结果。\\\\n\\\\n  - title: \\\\\\\"Fine-Grained NLI-Based Faithfulness Evaluation for Diverse Summarisation Tasks (INFUSE)\\\\\\\"\\\\n    authors: Anonymous\\\\n    year: 2024\\\\n    venue: EACL 2024\\\\n    url: https://aclanthology.org/2024.eacl-long.102/\\\\n    category: evidence_reward\\\\n    role: background\\\\n    key_finding: >\\\\n      变长前提+简化假设的细粒度 NLI faithfulness 评估，超越传统 NLI 在多任务摘要上的表现。\\\\n    relevance_to_ced_stabilizer: >\\\\n      NLI 作为 faithfulness 评估工具的进展。CED 中 NLI 组件用于判断 evidence 对 triple 的支持度。\\\\n\\\\n  - title: \\\\\\\"Enhancing Cross-Evidence Reasoning Graph for Document-Level Relation Extraction\\\\\\\"\\\\n    authors: Anonymous\\\\n    year: 2024\\\\n    venue: PMC/Bioinformatics 2024\\\\n    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11232587/\\\\n    category: evidence_reward\\\\n    role: background\\\\n    key_finding: >\\\\n      文档级关系抽取中用 cross-evidence reasoning graph 增强跨证据推理。\\\\n    relevance_to_ced_stabilizer: >\\\\n      DocRE 中 evidence 的重要性。但用 evidence 作为模型输入特征，\\\\n      我们用 evidence quality 作为 RL reward 信号——定位根本不同。\\\\n\\\\n  # === Category 5: Multi-Objective RL for Text Generation ===\\\\n\\\\n  - title: \\\\\\\"Confronting Reward Model Overoptimization with Constrained RLHF\\\\\\\"\\\\n    authors: Anonymous\\\\n    year: 2025\\\\n    venue: OpenReview\\\\n    url: https://openreview.net/forum?id=gkfUvn0fLU\\\\n    category: multi_objective_rl\\\\n    role: related_analysis\\\\n    key_finding: >\\\\n      多组件 RM 的 overoptimization 研究。component RM 间的相关性显著影响 overoptimization 临界点，\\\\n      用 constrained MDP 防止超出适当边界。\\\\n    relevance_to_ced_stabilizer: >\\\\n      CED 引入了与 extraction F1 低相关的 reward component（evidence quality），\\\\n      根据该论文分析低相关多组件 reward 更不易 overoptimize，\\\\n      可能是 CED 稳定性的另一个理论解释角度。\\\\n\\\\n  - title: \\\\\\\"On-Policy RL with Optimal Reward Baseline\\\\\\\"\\\\n    authors: Anonymous\\\\n    year: 2025\\\\n    venue: arXiv 2505.23585\\\\n    url: https://arxiv.org/abs/2505.23585\\\\n    category: multi_objective_rl\\\\n    role: theoretical_support\\\\n    key_finding: >\\\\n      Optimal baseline 一致性地实现更高训练 reward 和更高 entropy，\\\\n      有效稳定训练并促进更多样的 policy exploration。\\\\n    relevance_to_ced_stabilizer: >\\\\n      CED reward 的多维特性可能起到类似 optimal baseline 效果——\\\\n      evidence quality 维度为 advantage estimation 提供更丰富的参照信号。\\\\n\\\\n  # === Category 6: RSFT Methodology & Theory ===\\\\n\\\\n  - title: \\\\\\\"A Minimalist Approach to LLM Reasoning: from Rejection Sampling to Reinforce\\\\\\\"\\\\n    authors: Xiao et al.\\\\n    year: 2025\\\\n    venue: arXiv 2504.11343\\\\n    url: https://arxiv.org/abs/2504.11343\\\\n    category: rsft_methodology\\\\n    role: key_theoretical_support\\\\n    key_finding: >\\\\n      RAFT（简单 rejection sampling baseline）在数学推理上与 GRPO/PPO 表现相当。\\\\n      消融实验表明 GRPO 的主要优势来自丢弃全错 prompt 而非 reward normalization。\\\\n      提出 Reinforce-Rej，在 RAFT 基础上过滤全对和全错 sample。\\\\n      关键洞察：GRPO 和 RAFT 的核心区别在于负样本处理——GRPO 混合正负样本训练，\\\\n      RAFT 只用正样本，但 RAFT 仍能达到相当性能，说明 rejection sampling 的简单性被低估了。\\\\n    relevance_to_rsft_docre: >\\\\n      直接支持我们的设计选择：(1) RSFT 在 DocRE 上成功而 GRPO 失败，\\\\n      与该论文发现一致——rejection sampling 的 offline 特性天然避免了 catastrophic forgetting；\\\\n      (2) GRPO 主要优势来自过滤全错 prompt，这与我们 RSFT 的 reward-based filtering 机制相同；\\\\n      (3) DocRE structured output 比 math reasoning 更难用 online RL 优化，\\\\n      强化了 offline RSFT 的合理性。\\\\n\\\\n  - title: \\\\\\\"Beyond Rejection Sampling: Trajectory Fusion for Scaling Mathematical Reasoning (TrajFusion)\\\\\\\"\\\\n    authors: Jie Deng et al.\\\\n    year: 2026\\\\n    venue: arXiv 2602.04391\\\\n    url: https://arxiv.org/abs/2602.04391\\\\n    category: rsft_methodology\\\\n    role: method_component\\\\n    key_finding: >\\\\n      传统 RSFT 只用正确轨迹，丢弃错误轨迹。TrajFusion 将错误和正确轨迹交替拼接，\\\\n      显式建模试错推理过程，在困难数学问题上显著超越标准 RFT。\\\\n    relevance_to_rsft_docre: >\\\\n      Future work 方向：可考虑在 DocRE RSFT 中融合失败样本的信息。\\\\n      但 DocRE 的结构化输出（JSON triple）不同于 math 的 chain-of-thought，\\\\n      融合方式需要重新设计。\\\\n\\\\n  - title: \\\\\\\"Rejection Sampling Based Fine Tuning Secretly Performs PPO\\\\\\\"\\\\n    authors: Anonymous\\\\n    year: 2025\\\\n    venue: ICML 2025\\\\n    url: https://openreview.net/forum?id=yQ2UivKlir\\\\n    category: rsft_methodology\\\\n    role: theoretical_support\\\\n    key_finding: >\\\\n      建立 RSFT 与 PPO 之间的理论联系：rejection sampling fine-tuning\\\\n      在特定条件下隐式执行 PPO with marginal KL constraints。\\\\n    relevance_to_rsft_docre: >\\\\n      为 RSFT 的有效性提供理论解释。我们的 RSFT 成功可被视为\\\\n      隐式执行了 constrained policy optimization，\\\\n      避免了显式 GRPO 在 structured output 上的不稳定性。\\\\n\\\\n  # === Category 7: RL for Information Extraction ===\\\\n\\\\n  - title: \\\\\\\"R1-RE: Cross-Domain Relation Extraction with RLVR\\\\\\\"\\\\n    authors: Runpeng Dai, Tong Zheng et al.\\\\n    year: 2025\\\\n    venue: arXiv 2507.04642\\\\n    url: https://arxiv.org/abs/2507.04642\\\\n    category: rl_for_ie\\\\n    role: direct_competitor\\\\n    key_finding: >\\\\n      首个将 RLVR（GRPO + verifiable reward）用于关系抽取的框架。\\\\n      将 RE 重构为推理任务，R1-RE-7B 在跨域 OOD 准确率约 70%，媲美 GPT-4o。\\\\n      Reward 设计：format reward (+1/-3) + metric reward (+2/-1.5)，先验证格式再加准确度。\\\\n      triplet extraction 用 F1-based reward（entity weight=1, triplet weight=3）。\\\\n      未报告 catastrophic forgetting——GRPO 训练后在 MATH-500/IFEval/GPQA 上性能不降反升，\\\\n      说明句子级 RE 的简单 reward 结构足以稳定 GRPO 训练。\\\\n    results:\\\\n      sem2010_in_domain: 91.8\\\\n      sem2010_ood: 66.5\\\\n      mdkg_in_domain: 88.1\\\\n      mdkg_ood: 65.8\\\\n    evidence_generation: false\\\\n    relevance_to_rsft_docre: >\\\\n      最直接竞争者。关键差异与讨论：\\\\n      (1) R1-RE 是句子级 RE，GRPO 成功；我们是文档级 RE，GRPO 失败→RSFT 成功。\\\\n      句子级 RE 每个 sample 只有 1 个 triple（binary classification），reward variance 天然充足；\\\\n      文档级 RE 每个 sample 有数十个 triple，F1 score 作为 reward 在 group 内趋于同质化（frac_zero_std→0.8）。\\\\n      (2) R1-RE 未报告 catastrophic forgetting，进一步支持\\\\\\\"句子级简单 reward 可行，文档级需要 CED\\\\\\\"的论点。\\\\n      (3) R1-RE 关注 OOD 泛化，无 evidence 组件；我们关注 evidence-grounded extraction quality。\\\\n      互补而非直接冲突——R1-RE 证明 RLVR for RE 可行，我们揭示文档级需要额外设计。\\\\n\\\\n  - title: \\\\\\\"MORE-R1: Guiding LVLM for Multimodal Object-Entity Relation Extraction via Stepwise Reasoning with RL\\\\\\\"\\\\n    authors: Anonymous\\\\n    year: 2026\\\\n    venue: arXiv 2603.09478\\\\n    url: https://arxiv.org/abs/2603.09478\\\\n    category: rl_for_ie\\\\n    role: related_method\\\\n    key_finding: >\\\\n      多模态 RE 中用 GRPO + Progressive Sample-Mixing Strategy 优化 LVLM 推理能力。\\\\n      两阶段训练：SFT cold-start + GRPO RL。\\\\n    relevance_to_rsft_docre: >\\\\n      跨模态验证 RL for RE 趋势。其 Progressive Sample-Mixing 与我们\\\\n      RSFT 的 difficulty-aware sampling 思想相通，但在不同模态。\\\\n\\\\n  - title: \\\\\\\"REAR: Reinforced Reasoning Optimization for Event Argument Extraction with Relation-Aware Support\\\\\\\"\\\\n    authors: Jianwen Luo et al.\\\\n    year: 2025\\\\n    venue: EMNLP 2025 Findings\\\\n    url: https://2025.emnlp.org/program/find_papers/\\\\n    category: rl_for_ie\\\\n    role: related_method\\\\n    key_finding: >\\\\n      将强化学习推理优化用于事件论元抽取，结合关系感知支持。\\\\n      不同于 DocRE 但同属 IE 领域的 RL 应用。\\\\n    relevance_to_rsft_docre: >\\\\n      验证 RL 在 IE 任务上的有效性趋势。我们的工作扩展到 DocRE + evidence，\\\\n      且使用 offline RSFT 而非 online RL。\\\\n\\\\n  - title: \\\\\\\"Adaptive Reinforcement Learning Planning: Harnessing LLMs for Complex Information Extraction\\\\\\\"\\\\n    authors: Zepeng Ding et al.\\\\n    year: 2024\\\\n    venue: arXiv 2406.11455\\\\n    url: https://arxiv.org/abs/2406.11455\\\\n    category: rl_for_ie\\\\n    role: background\\\\n    key_finding: >\\\\n      将 LLM 顺序抽取建模为 MDP，用 DDQN 训练 decision module\\\\n      自适应选择实体抽取顺序，提升复杂 IE 性能。\\\\n    relevance_to_rsft_docre: >\\\\n      RL for IE 的早期工作。用 RL 优化抽取策略而非模型本身，\\\\n      与我们 RSFT 直接微调 LLM 的方法路径不同。\\\\n\\\\n  - title: \\\\\\\"Graph-R1: Towards Agentic GraphRAG Framework via End-to-end Reinforcement Learning\\\\\\\"\\\\n    authors: Haoran Luo et al.\\\\n    year: 2025\\\\n    venue: ICML 2026\\\\n    url: https://arxiv.org/abs/2507.21892\\\\n    category: rl_for_ie\\\\n    role: background\\\\n    key_finding: >\\\\n      用端到端 RL 优化 GraphRAG agent 的多轮检索-推理循环，\\\\n      包含 knowledge hypergraph construction（n-ary relation extraction）。\\\\n    relevance_to_rsft_docre: >\\\\n      RL + knowledge extraction 的交叉点。Graph-R1 关注 QA 场景下的知识图谱构建，\\\\n      我们关注 DocRE 的训练优化，应用场景不同。\\\\n\\\\n  # === Category 8: Recent LLM-based DocRE Methods ===\\\\n\\\\n  - title: \\\\\\\"RelPrior: Relation as a Prior - A Novel Paradigm for LLM-based Document-level Relation Extraction\\\\\\\"\\\\n    authors: Anonymous\\\\n    year: 2025\\\\n    venue: arXiv 2511.08143\\\\n    url: https://arxiv.org/abs/2511.08143\\\\n    category: llm_docre\\\\n    role: key_baseline\\\\n    key_finding: >\\\\n      用 binary relation 作为先验过滤无关实体对，再用 predefined relation 匹配实体，\\\\n      避免 LLM 在 DocRE 中被无关实体对分散注意力。\\\\n      在 DocRED/Re-DocRED 上超越现有纯 LLM-based DocRE 方法。\\\\n    results:\\\\n      docred_dev_f1: 47.82\\\\n      docred_test_f1: 48.34\\\\n      re_docred_dev_f1: 55.94\\\\n      re_docred_test_f1: 54.80\\\\n      backbone: LLaMA3-8B\\\\n    evidence_generation: false\\\\n    relevance_to_rsft_docre: >\\\\n      我们的直接 baseline 之一。RelPrior_LLaMA3-8B 在 DocRED test F1=48.34,\\\\n      Re-DocRED test F1=54.80。我们的 RSFT 提升显著更优。\\\\n      RelPrior 是 inference paradigm 创新（两阶段筛选），我们是 training paradigm 创新（RSFT+CED），正交互补。\\\\n\\\\n  - title: \\\\\\\"LMRC: LLM with Relation Classifier for Document-Level Relation Extraction\\\\\\\"\\\\n    authors: Xingzuo Li, Kehai Chen, Yunfei Long, Min Zhang\\\\n    year: 2024\\\\n    venue: arXiv 2408.13889\\\\n    url: https://arxiv.org/abs/2408.13889\\\\n    category: llm_docre\\\\n    role: related_method\\\\n    key_finding: >\\\\n      两阶段方法：先用 attention-based classifier 过滤 NA 实体对（RCP），\\\\n      再用 LLM 在精简候选空间中做多分类（RC）。\\\\n      注意：LMRC 依赖 BERT-based classifier 作为预筛选，非纯 LLM 方法。\\\\n    results:\\\\n      docred_dev_ign_f1: 58.16\\\\n      docred_dev_f1: 59.97\\\\n      docred_test_ign_f1: 58.49\\\\n      docred_test_f1: 60.52\\\\n      re_docred_test_ign_f1: 74.08\\\\n      re_docred_test_f1: 74.63\\\\n      backbone: BERT classifier + LLM\\\\n    evidence_generation: false\\\\n    relevance_to_rsft_docre: >\\\\n      LMRC 在 DocRED test F1=60.52, Re-DocRED test F1=74.63，性能显著高于纯 LLM 方法。\\\\n      但它依赖 BERT classifier 预筛选，本质上是 hybrid 方法而非纯 LLM generative。\\\\n      与我们端到端 LLM 生成方式不同——我们通过 RSFT 的 reward-based filtering 隐式解决 class imbalance。\\\\n\\\\n  - title: \\\\\\\"Ru-LLM: Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction\\\\\\\"\\\\n    authors: Anonymous\\\\n    year: 2025\\\\n    venue: NLPCC 2025\\\\n    url: https://link.springer.com/chapter/10.1007/978-981-95-3343-5_11\\\\n    category: llm_docre\\\\n    role: related_method\\\\n    key_finding: >\\\\n      用频繁模式挖掘 + MCTS 搜索逻辑规则，转化为 prompt 约束 LLM 输出，\\\\n      再用 CoT 验证过滤不满足规则的 triple。\\\\n      在 DWIE、DocRED、Re-DocRED 上声称超越现有 LLM 方法和规则框架。\\\\n      具体 F1 未公开获取（Springer 付费墙），但声称超越 AutoRE 等 LLM baseline。\\\\n    results:\\\\n      note: \\\\\\\"behind Springer paywall; claims SOTA over LLM baselines on DocRED/Re-DocRED/DWIE\\\\\\\"\\\\n    evidence_generation: false\\\\n    relevance_to_rsft_docre: >\\\\n      规则约束方式与我们的 CED reward 在 motivation 上相似（都是引入外部知识约束），\\\\n      但 Ru-LLM 用 inference-time 规则验证（MCTS+CoT），我们用 training-time reward shaping（CED）。\\\\n      Ru-LLM 的规则是数据集级别的频繁模式，CED 是 instance-level 的 evidence faithfulness。\\\\n\\\\n  - title: \\\\\\\"GLiDRE: Generalist Lightweight model for Document-level Relation Extraction\\\\\\\"\\\\n    authors: Anonymous\\\\n    year: 2025\\\\n    venue: arXiv 2508.00757\\\\n    url: https://arxiv.org/abs/2508.00757\\\\n    category: llm_docre\\\\n    role: background\\\\n    key_finding: >\\\\n      基于 dual-encoder 的轻量级零/少样本 DocRE 模型，\\\\n      预训练于 136K 文档的大规模 RE 数据。\\\\n      fully supervised Re-DocRED test F1=77.83，但这是 encoder-based 非 LLM generative。\\\\n      zero-shot Re-DocRED test F1=17.32（超越 LLaMA 3.3 70B 和 Mistral-Small 24B）。\\\\n    results:\\\\n      re_docred_dev_f1: 77.76\\\\n      re_docred_test_f1: 77.83\\\\n      re_docred_zero_shot_test_f1: 17.32\\\\n      fredo_in_domain_1doc_f1: 13.00\\\\n      fredo_in_domain_3doc_f1: 15.71\\\\n      backbone: \\\\\\\"dual-encoder (few hundred M params)\\\\\\\"\\\\n    evidence_generation: false\\\\n    relevance_to_rsft_docre: >\\\\n      不同范式（encoder-based vs LLM generative）。GLiDRE 的 fully supervised F1=77.83\\\\n      远超 LLM-based 方法（RelPrior 54.80），但依赖大规模预训练数据和 encoder 架构。\\\\n      与我们不直接可比——我们关注 LLM generative 范式下的训练优化。\\\\n\\\\n  - title: \\\\\\\"AutoRE: Document-Level Relation Extraction with Large Language Models\\\\\\\"\\\\n    authors: Anonymous\\\\n    year: 2024\\\\n    venue: arXiv 2403.14888\\\\n    url: https://arxiv.org/abs/2403.14888\\\\n    category: llm_docre\\\\n    role: background\\\\n    key_finding: >\\\\n      RHF（Relation-Head-Facts）范式用 Mistral-7B + QLoRA 做端到端 DocRE。\\\\n      关键设计：先抽 relation，再抽 head entity，最后抽 fact triple。\\\\n    results:\\\\n      re_docred_dev_f1_mistral: 53.01\\\\n      re_docred_test_f1_mistral: 51.91\\\\n      re_docred_dev_f1_vicuna: 54.29\\\\n      re_docred_test_f1_vicuna: 53.84\\\\n      docred_dev_f1_llama3: 45.76\\\\n      docred_test_f1_llama3: 45.96\\\\n      re_docred_dev_f1_llama3: 52.28\\\\n      re_docred_test_f1_llama3: 51.97\\\\n      backbone: \\\\\\\"Mistral-7B / Vicuna-7B / LLaMA3-8B (QLoRA)\\\\\\\"\\\\n    evidence_generation: false\\\\n    relevance_to_rsft_docre: >\\\\n      QLoRA fine-tuning for DocRE 的先例。AutoRE_LLaMA3-8B 在 Re-DocRED test F1=51.97,\\\\n      DocRED test F1=45.96。我们的 SFT baseline 与之类似，\\\\n      RSFT 在此基础上引入 reward-guided sample selection 进一步提升。\\\\n\\\\n  # === Category 9: Evidence Generation & Task Performance Trade-off ===\\\\n  # (NEW - 2026-05-15 evidence generation survey)\\\\n\\\\n  - title: \\\\\\\"Mind Your Step (by Step): Chain-of-Thought can Reduce Performance on Tasks where Thinking Makes Humans Worse\\\\\\\"\\\\n    authors: Sprague et al.\\\\n    year: 2024\\\\n    venue: NeurIPS 2024\\\\n    url: https://arxiv.org/abs/2410.21333\\\\n    category: evidence_generation_tradeoff\\\\n    role: key_evidence\\\\n    key_finding: >\\\\n      CoT 在某些任务上降低性能高达 36.3%（o1-preview vs GPT-4o）。\\\\n      显式推理步骤引入 error accumulation，且模型可能 overfit 到解释格式而非任务结构。\\\\n      隐式推理（hidden activations）在分布偏移下优于显式 token-level 推理。\\\\n    relevance_to_evidence_tradeoff: >\\\\n      直接支持我们的核心发现：要求模型同时生成 evidence sentences 是一种\\\\\\\"显式推理\\\\\\\"，\\\\n      会对主任务（RE）产生性能代价（~8pp F1 下降）。\\\\n      Related Work 引用点：evidence generation 作为 structured explanation，\\\\n      与 CoT 共享\\\\\\\"显式推理降低主任务性能\\\\\\\"的普遍模式。\\\\n\\\\n  - title: \\\\\\\"Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion\\\\\\\"\\\\n    authors: Xie et al. (Google Research)\\\\n    year: 2022\\\\n    venue: ACL Findings 2022\\\\n    url: https://arxiv.org/abs/2106.08657\\\\n    category: evidence_generation_tradeoff\\\\n    role: closest_docre_precedent\\\\n    key_finding: >\\\\n      Joint 训练 RE + evidence extraction，关键创新在 inference-stage fusion：\\\\n      分别在 extracted evidence 和 full document 上做 RE 预测再通过 blending layer 融合。\\\\n      DocRED 上提升 1.37 Ign F1。Silver evidence labels（启发式规则构建）即可提升 RE 性能。\\\\n    relevance_to_evidence_tradeoff: >\\\\n      最直接的 DocRE + evidence 先例。EIDER 的核心洞察是 evidence 需要 inference-stage 融合\\\\n      而非 joint generation——暗示 joint generation 会引入 noise。\\\\n      我们的 CED reranker 是 LLM-era 版本的 inference-stage fusion：\\\\n      先生成多个候选（含 evidence），再用 NLI 在推理阶段选最佳。\\\\n      Related Work 引用点：encoder-based DocRE 中 evidence 的使用方式，与我们 generative 范式的关键差异。\\\\n\\\\n  - title: \\\\\\\"Exploring the Trade-off Between Model Performance and Explanation Plausibility of Text Classifiers Using Human Rationales\\\\\\\"\\\\n    authors: Resck, Raimundo, Poco\\\\n    year: 2024\\\\n    venue: NAACL Findings 2024\\\\n    url: https://arxiv.org/abs/2404.03098\\\\n    category: evidence_generation_tradeoff\\\\n    role: formal_framework\\\\n    key_finding: >\\\\n      用 multi-objective optimization 探索 performance vs explanation plausibility 的 Pareto frontier。\\\\n      引入 rationale 约束创建 contrastive loss，证实加入 rationale supervision 会降低主任务性能，\\\\n      但存在 Pareto optimal 解平衡两者。\\\\n    relevance_to_evidence_tradeoff: >\\\\n      提供了 performance-explainability trade-off 的形式化框架。\\\\n      我们的 evidence-grounded RE 降 8pp 正是 Pareto frontier 上的一个点。\\\\n      CED reranker 的效果可解读为：将系统从 evidence-constrained 点推向 Pareto frontier，\\\\n      在几乎不牺牲 evidence quality（evi_f1=0.8188）的前提下恢复 RE 性能。\\\\n      Related Work 引用点：evidence generation 的 performance cost 有理论依据。\\\\n\\\\n  - title: \\\\\\\"The Decreasing Value of Chain of Thought in Prompting\\\\\\\"\\\\n    authors: Meincke, Mollick, Mollick, Shapiro\\\\n    year: 2025\\\\n    venue: Wharton Generative AI Labs Technical Report (SSRN)\\\\n    url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5285532\\\\n    category: evidence_generation_tradeoff\\\\n    role: empirical_support\\\\n    key_finding: >\\\\n      现代 reasoning models 上 CoT 收益微弱（4-13%），但 latency 增加 35-600%。\\\\n      更强的模型从显式推理中受益越少。CoT 可能在 easy questions 上引入 errors\\\\n      （variability 增加导致原本正确的被改错）。\\\\n    relevance_to_evidence_tradeoff: >\\\\n      支持\\\\\\\"更强的 SFT 模型不需要在生成时显式输出 evidence\\\\\\\"的论点。\\\\n      我们的 evidence-only SFT 的性能下降符合\\\\\\\"显式推理的边际收益递减\\\\\\\"模式。\\\\n      Related Work 引用点：evidence generation 的 accuracy cost 不是 DocRE-specific，而是 LLM 的普遍趋势。\\\\n\\\\n  # === Category 10: Negative Transfer in Multi-task / Auxiliary-task Learning ===\\\\n\\\\n  - title: \\\\\\\"ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning\\\\\\\"\\\\n    authors: Jiang, Chen et al.\\\\n    year: 2023\\\\n    venue: NeurIPS 2023\\\\n    url: https://arxiv.org/abs/2301.12618\\\\n    category: negative_transfer\\\\n    role: theoretical_framework\\\\n    key_finding: >\\\\n      辅助任务常导致 negative transfer，根因不仅是 gradient conflict 还有 auxiliary-target\\\\n      generalization gap。ForkMerge 周期性 fork 模型为多分支，搜索最优 task weights，\\\\n      动态 merge 过滤有害 task-parameter updates。在多个 benchmark 上减少 negative transfer。\\\\n    relevance_to_evidence_tradeoff: >\\\\n      Evidence generation 作为 auxiliary task 对 RE 的 negative transfer 可用此框架解释：\\\\n      evidence 和 RE 的 gradient 方向不完全对齐，joint training 时 evidence 任务\\\\\\\"拖累\\\\\\\"RE。\\\\n      CED reranker 本质上是将 evidence quality 从 training-time joint objective 解耦到\\\\n      inference-time verification，避免了 training-time 的 negative transfer。\\\\n      Related Work 引用点：auxiliary task 导致主任务性能下降的一般性理论。\\\\n\\\\n  # === Category 11: Faithfulness vs Accuracy / Correctness Trade-off ===\\\\n\\\\n  - title: \\\\\\\"Correctness is not Faithfulness in RAG Attributions\\\\\\\"\\\\n    authors: Wallat, Heuss, de Rijke, Anand\\\\n    year: 2024\\\\n    venue: SIGIR 2025\\\\n    url: https://arxiv.org/abs/2412.18004\\\\n    category: faithfulness_accuracy_tradeoff\\\\n    role: key_conceptual_framework\\\\n    key_finding: >\\\\n      Correctness 和 faithfulness 是独立维度，可能冲突。高达 57% 的 citations 是\\\\n      post-rationalized（事后编造而非真实依据）。Unfaithful attributions 可能 factually correct，\\\\n      但 foster misguided trust。必须同时检查 correctness 和 faithfulness。\\\\n    relevance_to_evidence_tradeoff: >\\\\n      直接相关。我们的 evidence-grounded RE 试图让模型输出 faithful evidence，\\\\n      但这与 relation correctness 产生张力（rel_f1 降 8pp）。\\\\n      CED reranker 通过 NLI verification 确保 evidence 是 faithful 的（非 post-rationalized），\\\\n      同时不牺牲 RE accuracy。\\\\n      Related Work 引用点：correctness-faithfulness 分离的概念框架。\\\\n\\\\n  - title: \\\\\\\"Evaluating Correctness and Faithfulness of Instruction-Following Models for Question Answering\\\\\\\"\\\\n    authors: Adlakha, BehnamGhader, Lu, Meade, Reddy\\\\n    year: 2024\\\\n    venue: TACL 2024\\\\n    url: https://arxiv.org/abs/2307.16877\\\\n    category: faithfulness_accuracy_tradeoff\\\\n    role: evaluation_framework\\\\n    key_finding: >\\\\n      Instruction-following LLMs 在 correctness 上表现可比 fine-tuned models，\\\\n      但 faithfulness 普遍较差——模型会 hallucinate 而非忠实于提供的 evidence。\\\\n      传统 metrics 对 correctness 和 faithfulness 的评估均有缺陷。\\\\n    relevance_to_evidence_tradeoff: >\\\\n      解释了为什么 joint evidence+RE 生成性能差——模型在同时优化 correctness\\\\n      和 faithfulness 时，两个目标存在张力。单纯要求模型\\\\\\\"同时输出正确 triples 和\\\\n      faithful evidence\\\\\\\"是 multi-objective optimization 问题。\\\\n      Related Work 引用点：correctness vs faithfulness 评估方法论。\\\\n\\\\n  - title: \\\\\\\"Towards Faithful Model Explanation in NLP: A Survey\\\\\\\"\\\\n    authors: Lyu, Havaldar, Stein et al.\\\\n    year: 2024\\\\n    venue: Computational Linguistics (MIT Press)\\\\n    url: https://aclanthology.org/2024.cl-2.6/\\\\n    category: faithfulness_accuracy_tradeoff\\\\n    role: comprehensive_survey\\\\n    key_finding: >\\\\n      系统综述 NLP 中 faithful explanation 的定义、评估和生成方法。\\\\n      识别了 faithfulness-performance trade-off 作为核心挑战：\\\\n      更 faithful 的解释不一定更有用，更有用的解释不一定 faithful。\\\\n      提出未来方向包括 multi-objective optimization 和 post-hoc verification。\\\\n    relevance_to_evidence_tradeoff: >\\\\n      权威综述为我们的 evidence generation trade-off 提供广泛文献背景。\\\\n      我们的 CED reranker 正是该综述建议的\\\\\\\"post-hoc verification\\\\\\\"方向的具体实例。\\\\n      Related Work 引用点：faithfulness 研究的全景综述，定位我们的工作。\\\\n\\\\n  # === Category 12: Reranking / Verification as Bridge ===\\\\n\\\\n  - title: \\\\\\\"Genie: Achieving Human Parity in Content-Grounded Datasets Generation\\\\\\\"\\\\n    authors: Yehudai, Carmeli, Mass et al.\\\\n    year: 2024\\\\n    venue: ICLR 2024\\\\n    url: https://arxiv.org/abs/2401.14367\\\\n    category: reranking_verification_bridge\\\\n    role: methodological_precedent\\\\n    key_finding: >\\\\n      三阶段流程：Content Preparation → Generation → NLI-based Filtering。\\\\n      用 fine-tuned T5-11B NLI 模型判断生成内容是否 entailed by source（faithfulness 检验），\\\\n      过滤不 faithful 的生成。在 LFQA、摘要、IE 上达到 human parity。\\\\n    relevance_to_evidence_tradeoff: >\\\\n      方法论上最接近我们的 CED reranker——都是用 NLI verification 作为 post-hoc filter/reranker，\\\\n      在不牺牲主任务质量的前提下确保 grounding quality。\\\\n      GENIE 验证了 NLI-based filtering 在内容生成中的有效性。\\\\n      关键差异：GENIE 是 data generation pipeline 的过滤，我们是 inference-time reranking。\\\\n      Related Work 引用点：NLI-based verification 作为 bridge 的成功先例。\\\\n\\\", \\\"total_chars\\\": 29337, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml\", \"content\": \"# Literature Map for faith-evidence-ie (FREIGE)\\n# Focus: CED-as-training-stabilizer (D024) + RSFT for DocRE\\n# Updated: 2026-05-15 (W3 reviewer gap fill + evidence generation trade-off survey)\\n\\npapers:\\n\\n  # === Category 1: Reward Diversity / Reward Shaping for RL Stability ===\\n\\n  - title: \\\"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization\\\"\\n    authors: NVIDIA Labs\\n    year: 2025\\n    venue: ICML 2026\\n    url: https://arxiv.org/abs/2601.05242\\n    category: reward_diversity\\n    role: closest_prior_work\\n    key_finding: >\\n      直接将 GRPO 应用于多 reward 组合时，不同 rollout 的 reward 组合在归一化后 collapse 为相同 advantage 值，\\n      降低训练信号分辨率导致收敛失败。GDPO 对每个 reward 独立做 group-wise normalization 再聚合，\\n      保留多 reward 的相对差异，显著提升训练稳定性。\\n    relevance_to_ced_stabilizer: >\\n      最直接相关。CED reward 本质上引入了独立于 extraction F1 的 reward 维度（evidence quality），\\n      GDPO 的理论分析解释了为什么多维 reward 比单一 reward 更稳定——独立 reward 维度防止 advantage collapse。\\n      但 GDPO 是方法论贡献，CED 是 task-specific reward 设计自然具备了这一特性。\\n\\n  - title: \\\"DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of LLMs\\\"\\n    authors: Xiwen Chen et al.\\n    year: 2025\\n    venue: arXiv 2505.09655\\n    url: https://arxiv.org/abs/2505.09655\\n    category: reward_diversity\\n    role: related_method\\n    key_finding: >\\n      GRPO 的标量 reward 无法区分语义多样但得分相同的输出（diversity-quality inconsistency）。\\n      DRA 用子模互信息（SMI）对 reward 加权，给多样性高的 completion 更大权重，\\n      等价于 Inverse Propensity Scoring 去偏，防止 policy 坍缩到先验模式。\\n    relevance_to_ced_stabilizer: >\\n      DRA 通过后处理 reward 注入多样性信号；CED 的 reward 本身就内含对比结构自然提供 diversity 信号。\\n      机制互补但来源不同——CED 是 reward design 层面，DRA 是 optimization 层面。\\n\\n  - title: \\\"Shrinking the Variance: Shrinkage Baselines for RL with Verifiable Rewards\\\"\\n    authors: Guanning Zeng et al.\\n    year: 2025\\n    venue: arXiv 2511.03710\\n    url: https://arxiv.org/abs/2511.03710\\n    category: reward_diversity\\n    role: theoretical_support\\n    key_finding: >\\n      RLVR 中 per-prompt 均值 baseline 在低 generation 数下估计不准导致高 variance 梯度。\\n      用 James-Stein shrinkage 混合 per-prompt 和 cross-prompt 均值，\\n      构造可证明更低 variance 的 policy gradient estimator。\\n    relevance_to_ced_stabilizer: >\\n      理论支持：reward variance 对 gradient estimation 质量至关重要。\\n      CED 的额外 reward 维度提供更丰富的 per-group variance，间接起到 variance 维持效果。\\n\\n  - title: \\\"Reward Shaping to Mitigate Reward Hacking in RLHF\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2502.18770\\n    url: https://arxiv.org/abs/2502.18770\\n    category: reward_diversity\\n    role: background\\n    key_finding: >\\n      RL reward 应有界且先快速增长后缓慢收敛。系统研究 reward shaping 原则，\\n      好的 reward 形状能抑制 reward hacking 并提升训练稳定性。\\n    relevance_to_ced_stabilizer: >\\n      CED reward 的 0-1 对比判别结构天然满足有界性，\\n      且 evidence quality 的渐进提升符合\\\"先快后慢\\\"的 reward shaping 原则。\\n\\n  # === Category 2: Mode Collapse Prevention in GRPO/RLHF ===\\n\\n  - title: \\\"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\\\"\\n    authors: ByteDance Seed, Tsinghua AIR\\n    year: 2025\\n    venue: NeurIPS 2025\\n    url: https://arxiv.org/abs/2503.14476\\n    category: mode_collapse_prevention\\n    role: key_baseline\\n    key_finding: >\\n      Naive GRPO 存在 entropy collapse（policy 熵快速下降→输出同质化）。\\n      根因：clipping 不对称性——概率 0.01 的 token 最多增到 0.012，而概率 0.9 的 token 可达 1.08，\\n      低概率 token 难以增长，抑制探索。DAPO 提出 Clip-Higher（εhigh=0.28 > εlow=0.2）\\n      为低概率 token 留更大增长空间，加 Dynamic Sampling 过滤 accuracy=0 或 1 的 prompt\\n      （这些 prompt 产生零梯度，降低有效 batch size）。在 AIME 2024 达 50 分超越 DeepSeek-R1-Zero。\\n    relevance_to_ced_stabilizer: >\\n      DAPO 从 optimization 技巧角度解决 entropy collapse。CED reward 从 reward design 层面\\n      防止 mode collapse——evidence quality 维度确保 reward 组内有足够 variance，\\n      不会出现 all-same-reward 的零梯度 prompt。DAPO 的 Dynamic Sampling 过滤 accuracy=0/1 prompt\\n      与我们观察到的 frac_zero_std→0.8 现象本质相同：extraction-only reward 下大量 prompt\\n      产生零 advantage，CED 从源头（reward 设计）而非后处理（过滤）解决这个问题。\\n\\n  - title: \\\"Dr. GRPO: Removing Optimization Bias in GRPO\\\"\\n    authors: Liu et al.\\n    year: 2025\\n    venue: COLM 2025\\n    url: https://arxiv.org/abs/2503.20783\\n    category: mode_collapse_prevention\\n    role: related_analysis\\n    key_finding: >\\n      GRPO 的 std 归一化引入两个 bias：(1) difficulty bias——std(r) 归一化对低 variance 组\\n      （全对/全错）给予过高 advantage 权重，trivial question 主导训练信号；\\n      (2) length bias——per-token loss 的 1/|o_i| 项使长的错误回答被 under-penalize。\\n      当 std(r)→0 时 advantage 爆炸或未定义，梯度数值不稳定。\\n      Dr. GRPO 移除 std 归一化，用无偏 Monte Carlo advantage：Ã = R(q,o_i) - mean(R)。\\n    relevance_to_ced_stabilizer: >\\n      与我们的实验发现高度一致：extraction-only reward 下 frac_zero_std→0.8 正是\\n      Dr. GRPO 分析的 difficulty bias 极端情况——大量 prompt 的所有 rollout 得到相同 F1，\\n      std→0 导致 advantage 异常。CED 通过增加 reward 维度天然维持 reward_std>0，\\n      从 reward 设计而非算法修改角度避免了 Dr. GRPO 发现的 bias。\\n\\n  - title: \\\"GVPO: Group Variance Policy Optimization for LLM Post-Training\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: NeurIPS 2025\\n    url: https://arxiv.org/abs/2504.19599\\n    category: mode_collapse_prevention\\n    role: alternative_framework\\n    key_finding: >\\n      将 KL 约束 reward 最大化的解析解直接嵌入梯度权重，\\n      variance 项自然平衡 exploration 与 exploitation，维持适度 entropy。\\n    relevance_to_ced_stabilizer: >\\n      GVPO 的 variance 项机制与 CED 维持 reward variance 的效果功能类似，\\n      但 GVPO 是算法层面 implicit regularization，CED 是 reward 层面 explicit structure。\\n\\n  - title: \\\"REINFORCE++: Stabilizing Critic-Free Policy Optimization with Global Advantage Normalization\\\"\\n    authors: Jian Hu et al.\\n    year: 2025\\n    venue: arXiv 2501.03262\\n    url: https://arxiv.org/abs/2501.03262\\n    category: mode_collapse_prevention\\n    role: related_method\\n    key_finding: >\\n      Prompt-level (local) advantage normalization 导致不准确估计和过拟合。\\n      Global batch normalization 提供更稳定、理论无偏的 gradient estimator。\\n    relevance_to_ced_stabilizer: >\\n      解决 local normalization 的 variance 问题；CED 从 reward 端增加 variance 来源。\\n      两者在不同层面解决同一问题：防止 gradient signal 消失。\\n\\n  - title: \\\"DiverseGRPO: Mitigating Mode Collapse in Image Generation via Diversity-Aware GRPO\\\"\\n    authors: Henglin Liu et al.\\n    year: 2025\\n    venue: arXiv 2512.21514\\n    url: https://arxiv.org/abs/2512.21514\\n    category: mode_collapse_prevention\\n    role: parallel_work\\n    key_finding: >\\n      图像生成中 GRPO 后期输出同质化。distributional reward modeling（谱聚类+exploratory reward）\\n      和 structure-aware regularization 实现 13-18% 语义多样性提升。\\n    relevance_to_ced_stabilizer: >\\n      跨域验证了 GRPO mode collapse 的普遍性，distributional reward 思路与 CED 精神相近——\\n      都是通过 reward 层面结构化信号维持输出多样性。\\n\\n  - title: \\\"Why GRPO Needs Normalization: A Local-Curvature Perspective on Adaptive Gradients\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2601.23135\\n    url: https://arxiv.org/abs/2601.23135\\n    category: mode_collapse_prevention\\n    role: theoretical_support\\n    key_finding: >\\n      GRPO 的 reward_std 归一化在温和条件下提供严格优于未归一化 REINFORCE 的收敛速率，\\n      收益由 prompt 间平均 reward std 刻画。\\n    relevance_to_ced_stabilizer: >\\n      直接理论支撑：reward_std 越大收敛越好。CED 通过 evidence quality 维度维持高 reward_std，\\n      从该理论看 CED 的稳定性优势是 reward_std 维持带来的收敛速率优势。\\n\\n  # === Category 3: Contrastive Rewards in RL ===\\n\\n  - title: \\\"Improving Reinforcement Learning from Human Feedback Using Contrastive Rewards\\\"\\n    authors: Shen, Zhang et al.\\n    year: 2024\\n    venue: arXiv 2403.07708\\n    url: https://arxiv.org/abs/2403.07708\\n    category: contrastive_reward\\n    role: closest_contrastive_precedent\\n    key_finding: >\\n      两步机制：(1) 离线采样 baseline response；(2) 用 baseline 计算 contrastive reward\\n      作为 PPO 的 penalty 项。效果：惩罚 reward uncertainty、根据任务难度自适应校准、\\n      减少 PPO 中的 variance。在 TL;DR 和 HH-RLHF 上持续优于标准 RLHF。\\n    relevance_to_ced_stabilizer: >\\n      最接近的对比 reward 先例。关键差异：(1) 它是对 learned RM 输出的后处理对比，\\n      CED 是 reward function 本身就是对比判别（evidence vs. corrupted evidence）；\\n      (2) 它在 PPO 中验证，CED 在 GRPO 中验证；\\n      (3) 它是 domain-agnostic penalty，CED 是 task-specific faithfulness signal。\\n      stabilizing 机制相通但实现路径根本不同。\\n\\n  - title: \\\"Improving Discriminative Capability of Reward Models in RLHF Using Contrastive Learning\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: EMNLP 2024\\n    url: https://aclanthology.org/2024.emnlp-main.852/\\n    category: contrastive_reward\\n    role: related_method\\n    key_finding: >\\n      无监督对比损失训练 reward model 充分捕捉对比数据区分度，\\n      带来更稳定的 PPO 训练 return 和 reward。\\n    relevance_to_ced_stabilizer: >\\n      验证对比训练 reward model → 更稳定 RL 训练链条。CED 不是对比训练 reward model，\\n      而是 reward function 本身就是对比判别，但 stabilizing 机制相通。\\n\\n  - title: \\\"Contrastive Preference Learning: Learning from Human Feedback without RL\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: ICLR 2025\\n    url: https://openreview.net/forum?id=iX1RjVQODj\\n    category: contrastive_reward\\n    role: background\\n    key_finding: >\\n      将 preference learning 重新表述为对比学习问题，无需显式 RL 即可从人类反馈中学习。\\n    relevance_to_ced_stabilizer: >\\n      对比框架在 preference alignment 中的通用性。CED 可被视为 task-specific contrastive preference signal。\\n\\n  # === Category 4: Evidence-Based Rewards in IE/NLP ===\\n\\n  - title: \\\"Drift: Enhancing LLM Faithfulness in Rationale Generation\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: ACL 2025\\n    url: https://aclanthology.org/2025.acl-long.340.pdf\\n    category: evidence_reward\\n    role: related_method\\n    key_finding: >\\n      用 faithfulness reward 引导 LLM 生成更可靠的 rationale，提升 CoT 推理事实一致性。\\n    relevance_to_ced_stabilizer: >\\n      Faithfulness reward 用于生成质量的先例。CED 中 evidence discrimination\\n      本质上也是 faithfulness 信号——判断证据是否忠实支持抽取结果。\\n\\n  - title: \\\"Fine-Grained NLI-Based Faithfulness Evaluation for Diverse Summarisation Tasks (INFUSE)\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: EACL 2024\\n    url: https://aclanthology.org/2024.eacl-long.102/\\n    category: evidence_reward\\n    role: background\\n    key_finding: >\\n      变长前提+简化假设的细粒度 NLI faithfulness 评估，超越传统 NLI 在多任务摘要上的表现。\\n    relevance_to_ced_stabilizer: >\\n      NLI 作为 faithfulness 评估工具的进展。CED 中 NLI 组件用于判断 evidence 对 triple 的支持度。\\n\\n  - title: \\\"Enhancing Cross-Evidence Reasoning Graph for Document-Level Relation Extraction\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: PMC/Bioinformatics 2024\\n    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11232587/\\n    category: evidence_reward\\n    role: background\\n    key_finding: >\\n      文档级关系抽取中用 cross-evidence reasoning graph 增强跨证据推理。\\n    relevance_to_ced_stabilizer: >\\n      DocRE 中 evidence 的重要性。但用 evidence 作为模型输入特征，\\n      我们用 evidence quality 作为 RL reward 信号——定位根本不同。\\n\\n  # === Category 5: Multi-Objective RL for Text Generation ===\\n\\n  - title: \\\"Confronting Reward Model Overoptimization with Constrained RLHF\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: OpenReview\\n    url: https://openreview.net/forum?id=gkfUvn0fLU\\n    category: multi_objective_rl\\n    role: related_analysis\\n    key_finding: >\\n      多组件 RM 的 overoptimization 研究。component RM 间的相关性显著影响 overoptimization 临界点，\\n      用 constrained MDP 防止超出适当边界。\\n    relevance_to_ced_stabilizer: >\\n      CED 引入了与 extraction F1 低相关的 reward component（evidence quality），\\n      根据该论文分析低相关多组件 reward 更不易 overoptimize，\\n      可能是 CED 稳定性的另一个理论解释角度。\\n\\n  - title: \\\"On-Policy RL with Optimal Reward Baseline\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2505.23585\\n    url: https://arxiv.org/abs/2505.23585\\n    category: multi_objective_rl\\n    role: theoretical_support\\n    key_finding: >\\n      Optimal baseline 一致性地实现更高训练 reward 和更高 entropy，\\n      有效稳定训练并促进更多样的 policy exploration。\\n    relevance_to_ced_stabilizer: >\\n      CED reward 的多维特性可能起到类似 optimal baseline 效果——\\n      evidence quality 维度为 advantage estimation 提供更丰富的参照信号。\\n\\n  # === Category 6: RSFT Methodology & Theory ===\\n\\n  - title: \\\"A Minimalist Approach to LLM Reasoning: from Rejection Sampling to Reinforce\\\"\\n    authors: Xiao et al.\\n    year: 2025\\n    venue: arXiv 2504.11343\\n    url: https://arxiv.org/abs/2504.11343\\n    category: rsft_methodology\\n    role: key_theoretical_support\\n    key_finding: >\\n      RAFT（简单 rejection sampling baseline）在数学推理上与 GRPO/PPO 表现相当。\\n      消融实验表明 GRPO 的主要优势来自丢弃全错 prompt 而非 reward normalization。\\n      提出 Reinforce-Rej，在 RAFT 基础上过滤全对和全错 sample。\\n      关键洞察：GRPO 和 RAFT 的核心区别在于负样本处理——GRPO 混合正负样本训练，\\n      RAFT 只用正样本，但 RAFT 仍能达到相当性能，说明 rejection sampling 的简单性被低估了。\\n    relevance_to_rsft_docre: >\\n      直接支持我们的设计选择：(1) RSFT 在 DocRE 上成功而 GRPO 失败，\\n      与该论文发现一致——rejection sampling 的 offline 特性天然避免了 catastrophic forgetting；\\n      (2) GRPO 主要优势来自过滤全错 prompt，这与我们 RSFT 的 reward-based filtering 机制相同；\\n      (3) DocRE structured output 比 math reasoning 更难用 online RL 优化，\\n      强化了 offline RSFT 的合理性。\\n\\n  - title: \\\"Beyond Rejection Sampling: Trajectory Fusion for Scaling Mathematical Reasoning (TrajFusion)\\\"\\n    authors: Jie Deng et al.\\n    year: 2026\\n    venue: arXiv 2602.04391\\n    url: https://arxiv.org/abs/2602.04391\\n    category: rsft_methodology\\n    role: method_component\\n    key_finding: >\\n      传统 RSFT 只用正确轨迹，丢弃错误轨迹。TrajFusion 将错误和正确轨迹交替拼接，\\n      显式建模试错推理过程，在困难数学问题上显著超越标准 RFT。\\n    relevance_to_rsft_docre: >\\n      Future work 方向：可考虑在 DocRE RSFT 中融合失败样本的信息。\\n      但 DocRE 的结构化输出（JSON triple）不同于 math 的 chain-of-thought，\\n      融合方式需要重新设计。\\n\\n  - title: \\\"Rejection Sampling Based Fine Tuning Secretly Performs PPO\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: ICML 2025\\n    url: https://openreview.net/forum?id=yQ2UivKlir\\n    category: rsft_methodology\\n    role: theoretical_support\\n    key_finding: >\\n      建立 RSFT 与 PPO 之间的理论联系：rejection sampling fine-tuning\\n      在特定条件下隐式执行 PPO with marginal KL constraints。\\n    relevance_to_rsft_docre: >\\n      为 RSFT 的有效性提供理论解释。我们的 RSFT 成功可被视为\\n      隐式执行了 constrained policy optimization，\\n      避免了显式 GRPO 在 structured output 上的不稳定性。\\n\\n  # === Category 7: RL for Information Extraction ===\\n\\n  - title: \\\"R1-RE: Cross-Domain Relation Extraction with RLVR\\\"\\n    authors: Runpeng Dai, Tong Zheng et al.\\n    year: 2025\\n    venue: arXiv 2507.04642\\n    url: https://arxiv.org/abs/2507.04642\\n    category: rl_for_ie\\n    role: direct_competitor\\n    key_finding: >\\n      首个将 RLVR（GRPO + verifiable reward）用于关系抽取的框架。\\n      将 RE 重构为推理任务，R1-RE-7B 在跨域 OOD 准确率约 70%，媲美 GPT-4o。\\n      Reward 设计：format reward (+1/-3) + metric reward (+2/-1.5)，先验证格式再加准确度。\\n      triplet extraction 用 F1-based reward（entity weight=1, triplet weight=3）。\\n      未报告 catastrophic forgetting——GRPO 训练后在 MATH-500/IFEval/GPQA 上性能不降反升，\\n      说明句子级 RE 的简单 reward 结构足以稳定 GRPO 训练。\\n    results:\\n      sem2010_in_domain: 91.8\\n      sem2010_ood: 66.5\\n      mdkg_in_domain: 88.1\\n      mdkg_ood: 65.8\\n    evidence_generation: false\\n    relevance_to_rsft_docre: >\\n      最直接竞争者。关键差异与讨论：\\n      (1) R1-RE 是句子级 RE，GRPO 成功；我们是文档级 RE，GRPO 失败→RSFT 成功。\\n      句子级 RE 每个 sample 只有 1 个 triple（binary classification），reward variance 天然充足；\\n      文档级 RE 每个 sample 有数十个 triple，F1 score 作为 reward 在 group 内趋于同质化（frac_zero_std→0.8）。\\n      (2) R1-RE 未报告 catastrophic forgetting，进一步支持\\\"句子级简单 reward 可行，文档级需要 CED\\\"的论点。\\n      (3) R1-RE 关注 OOD 泛化，无 evidence 组件；我们关注 evidence-grounded extraction quality。\\n      互补而非直接冲突——R1-RE 证明 RLVR for RE 可行，我们揭示文档级需要额外设计。\\n\\n  - title: \\\"MORE-R1: Guiding LVLM for Multimodal Object-Entity Relation Extraction via Stepwise Reasoning with RL\\\"\\n    authors: Anonymous\\n    year: 2026\\n    venue: arXiv 2603.09478\\n    url: https://arxiv.org/abs/2603.09478\\n    category: rl_for_ie\\n    role: related_method\\n    key_finding: >\\n      多模态 RE 中用 GRPO + Progressive Sample-Mixing Strategy 优化 LVLM 推理能力。\\n      两阶段训练：SFT cold-start + GRPO RL。\\n    relevance_to_rsft_docre: >\\n      跨模态验证 RL for RE 趋势。其 Progressive Sample-Mixing 与我们\\n      RSFT 的 difficulty-aware sampling 思想相通，但在不同模态。\\n\\n  - title: \\\"REAR: Reinforced Reasoning Optimization for Event Argument Extraction with Relation-Aware Support\\\"\\n    authors: Jianwen Luo et al.\\n    year: 2025\\n    venue: EMNLP 2025 Findings\\n    url: https://2025.emnlp.org/program/find_papers/\\n    category: rl_for_ie\\n    role: related_method\\n    key_finding: >\\n      将强化学习推理优化用于事件论元抽取，结合关系感知支持。\\n      不同于 DocRE 但同属 IE 领域的 RL 应用。\\n    relevance_to_rsft_docre: >\\n      验证 RL 在 IE 任务上的有效性趋势。我们的工作扩展到 DocRE + evidence，\\n      且使用 offline RSFT 而非 online RL。\\n\\n  - title: \\\"Adaptive Reinforcement Learning Planning: Harnessing LLMs for Complex Information Extraction\\\"\\n    authors: Zepeng Ding et al.\\n    year: 2024\\n    venue: arXiv 2406.11455\\n    url: https://arxiv.org/abs/2406.11455\\n    category: rl_for_ie\\n    role: background\\n    key_finding: >\\n      将 LLM 顺序抽取建模为 MDP，用 DDQN 训练 decision module\\n      自适应选择实体抽取顺序，提升复杂 IE 性能。\\n    relevance_to_rsft_docre: >\\n      RL for IE 的早期工作。用 RL 优化抽取策略而非模型本身，\\n      与我们 RSFT 直接微调 LLM 的方法路径不同。\\n\\n  - title: \\\"Graph-R1: Towards Agentic GraphRAG Framework via End-to-end Reinforcement Learning\\\"\\n    authors: Haoran Luo et al.\\n    year: 2025\\n    venue: ICML 2026\\n    url: https://arxiv.org/abs/2507.21892\\n    category: rl_for_ie\\n    role: background\\n    key_finding: >\\n      用端到端 RL 优化 GraphRAG agent 的多轮检索-推理循环，\\n      包含 knowledge hypergraph construction（n-ary relation extraction）。\\n    relevance_to_rsft_docre: >\\n      RL + knowledge extraction 的交叉点。Graph-R1 关注 QA 场景下的知识图谱构建，\\n      我们关注 DocRE 的训练优化，应用场景不同。\\n\\n  # === Category 8: Recent LLM-based DocRE Methods ===\\n\\n  - title: \\\"RelPrior: Relation as a Prior - A Novel Paradigm for LLM-based Document-level Relation Extraction\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2511.08143\\n    url: https://arxiv.org/abs/2511.08143\\n    category: llm_docre\\n    role: key_baseline\\n    key_finding: >\\n      用 binary relation 作为先验过滤无关实体对，再用 predefined relation 匹配实体，\\n      避免 LLM 在 DocRE 中被无关实体对分散注意力。\\n      在 DocRED/Re-DocRED 上超越现有纯 LLM-based DocRE 方法。\\n    results:\\n      docred_dev_f1: 47.82\\n      docred_test_f1: 48.34\\n      re_docred_dev_f1: 55.94\\n      re_docred_test_f1: 54.80\\n      backbone: LLaMA3-8B\\n    evidence_generation: false\\n    relevance_to_rsft_docre: >\\n      我们的直接 baseline 之一。RelPrior_LLaMA3-8B 在 DocRED test F1=48.34,\\n      Re-DocRED test F1=54.80。我们的 RSFT 提升显著更优。\\n      RelPrior 是 inference paradigm 创新（两阶段筛选），我们是 training paradigm 创新（RSFT+CED），正交互补。\\n\\n  - title: \\\"LMRC: LLM with Relation Classifier for Document-Level Relation Extraction\\\"\\n    authors: Xingzuo Li, Kehai Chen, Yunfei Long, Min Zhang\\n    year: 2024\\n    venue: arXiv 2408.13889\\n    url: https://arxiv.org/abs/2408.13889\\n    category: llm_docre\\n    role: related_method\\n    key_finding: >\\n      两阶段方法：先用 attention-based classifier 过滤 NA 实体对（RCP），\\n      再用 LLM 在精简候选空间中做多分类（RC）。\\n      注意：LMRC 依赖 BERT-based classifier 作为预筛选，非纯 LLM 方法。\\n    results:\\n      docred_dev_ign_f1: 58.16\\n      docred_dev_f1: 59.97\\n      docred_test_ign_f1: 58.49\\n      docred_test_f1: 60.52\\n      re_docred_test_ign_f1: 74.08\\n      re_docred_test_f1: 74.63\\n      backbone: BERT classifier + LLM\\n    evidence_generation: false\\n    relevance_to_rsft_docre: >\\n      LMRC 在 DocRED test F1=60.52, Re-DocRED test F1=74.63，性能显著高于纯 LLM 方法。\\n      但它依赖 BERT classifier 预筛选，本质上是 hybrid 方法而非纯 LLM generative。\\n      与我们端到端 LLM 生成方式不同——我们通过 RSFT 的 reward-based filtering 隐式解决 class imbalance。\\n\\n  - title: \\\"Ru-LLM: Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: NLPCC 2025\\n    url: https://link.springer.com/chapter/10.1007/978-981-95-3343-5_11\\n    category: llm_docre\\n    role: related_method\\n    key_finding: >\\n      用频繁模式挖掘 + MCTS 搜索逻辑规则，转化为 prompt 约束 LLM 输出，\\n      再用 CoT 验证过滤不满足规则的 triple。\\n      在 DWIE、DocRED、Re-DocRED 上声称超越现有 LLM 方法和规则框架。\\n      具体 F1 未公开获取（Springer 付费墙），但声称超越 AutoRE 等 LLM baseline。\\n    results:\\n      note: \\\"behind Springer paywall; claims SOTA over LLM baselines on DocRED/Re-DocRED/DWIE\\\"\\n    evidence_generation: false\\n    relevance_to_rsft_docre: >\\n      规则约束方式与我们的 CED reward 在 motivation 上相似（都是引入外部知识约束），\\n      但 Ru-LLM 用 inference-time 规则验证（MCTS+CoT），我们用 training-time reward shaping（CED）。\\n      Ru-LLM 的规则是数据集级别的频繁模式，CED 是 instance-level 的 evidence faithfulness。\\n\\n  - title: \\\"GLiDRE: Generalist Lightweight model for Document-level Relation Extraction\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2508.00757\\n    url: https://arxiv.org/abs/2508.00757\\n    category: llm_docre\\n    role: background\\n    key_finding: >\\n      基于 dual-encoder 的轻量级零/少样本 DocRE 模型，\\n      预训练于 136K 文档的大规模 RE 数据。\\n      fully supervised Re-DocRED test F1=77.83，但这是 encoder-based 非 LLM generative。\\n      zero-shot Re-DocRED test F1=17.32（超越 LLaMA 3.3 70B 和 Mistral-Small 24B）。\\n    results:\\n      re_docred_dev_f1: 77.76\\n      re_docred_test_f1: 77.83\\n      re_docred_zero_shot_test_f1: 17.32\\n      fredo_in_domain_1doc_f1: 13.00\\n      fredo_in_domain_3doc_f1: 15.71\\n      backbone: \\\"dual-encoder (few hundred M params)\\\"\\n    evidence_generation: false\\n    relevance_to_rsft_docre: >\\n      不同范式（encoder-based vs LLM generative）。GLiDRE 的 fully supervised F1=77.83\\n      远超 LLM-based 方法（RelPrior 54.80），但依赖大规模预训练数据和 encoder 架构。\\n      与我们不直接可比——我们关注 LLM generative 范式下的训练优化。\\n\\n  - title: \\\"AutoRE: Document-Level Relation Extraction with Large Language Models\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: arXiv 2403.14888\\n    url: https://arxiv.org/abs/2403.14888\\n    category: llm_docre\\n    role: background\\n    key_finding: >\\n      RHF（Relation-Head-Facts）范式用 Mistral-7B + QLoRA 做端到端 DocRE。\\n      关键设计：先抽 relation，再抽 head entity，最后抽 fact triple。\\n    results:\\n      re_docred_dev_f1_mistral: 53.01\\n      re_docred_test_f1_mistral: 51.91\\n      re_docred_dev_f1_vicuna: 54.29\\n      re_docred_test_f1_vicuna: 53.84\\n      docred_dev_f1_llama3: 45.76\\n      docred_test_f1_llama3: 45.96\\n      re_docred_dev_f1_llama3: 52.28\\n      re_docred_test_f1_llama3: 51.97\\n      backbone: \\\"Mistral-7B / Vicuna-7B / LLaMA3-8B (QLoRA)\\\"\\n    evidence_generation: false\\n    relevance_to_rsft_docre: >\\n      QLoRA fine-tuning for DocRE 的先例。AutoRE_LLaMA3-8B 在 Re-DocRED test F1=51.97,\\n      DocRED test F1=45.96。我们的 SFT baseline 与之类似，\\n      RSFT 在此基础上引入 reward-guided sample selection 进一步提升。\\n\\n  # === Category 9: Evidence Generation & Task Performance Trade-off ===\\n  # (NEW - 2026-05-15 evidence generation survey)\\n\\n  - title: \\\"Mind Your Step (by Step): Chain-of-Thought can Reduce Performance on Tasks where Thinking Makes Humans Worse\\\"\\n    authors: Sprague et al.\\n    year: 2024\\n    venue: NeurIPS 2024\\n    url: https://arxiv.org/abs/2410.21333\\n    category: evidence_generation_tradeoff\\n    role: key_evidence\\n    key_finding: >\\n      CoT 在某些任务上降低性能高达 36.3%（o1-preview vs GPT-4o）。\\n      显式推理步骤引入 error accumulation，且模型可能 overfit 到解释格式而非任务结构。\\n      隐式推理（hidden activations）在分布偏移下优于显式 token-level 推理。\\n    relevance_to_evidence_tradeoff: >\\n      直接支持我们的核心发现：要求模型同时生成 evidence sentences 是一种\\\"显式推理\\\"，\\n      会对主任务（RE）产生性能代价（~8pp F1 下降）。\\n      Related Work 引用点：evidence generation 作为 structured explanation，\\n      与 CoT 共享\\\"显式推理降低主任务性能\\\"的普遍模式。\\n\\n  - title: \\\"Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion\\\"\\n    authors: Xie et al. (Google Research)\\n    year: 2022\\n    venue: ACL Findings 2022\\n    url: https://arxiv.org/abs/2106.08657\\n    category: evidence_generation_tradeoff\\n    role: closest_docre_precedent\\n    key_finding: >\\n      Joint 训练 RE + evidence extraction，关键创新在 inference-stage fusion：\\n      分别在 extracted evidence 和 full document 上做 RE 预测再通过 blending layer 融合。\\n      DocRED 上提升 1.37 Ign F1。Silver evidence labels（启发式规则构建）即可提升 RE 性能。\\n    relevance_to_evidence_tradeoff: >\\n      最直接的 DocRE + evidence 先例。EIDER 的核心洞察是 evidence 需要 inference-stage 融合\\n      而非 joint generation——暗示 joint generation 会引入 noise。\\n      我们的 CED reranker 是 LLM-era 版本的 inference-stage fusion：\\n      先生成多个候选（含 evidence），再用 NLI 在推理阶段选最佳。\\n      Related Work 引用点：encoder-based DocRE 中 evidence 的使用方式，与我们 generative 范式的关键差异。\\n\\n  - title: \\\"Exploring the Trade-off Between Model Performance and Explanation Plausibility of Text Classifiers Using Human Rationales\\\"\\n    authors: Resck, Raimundo, Poco\\n    year: 2024\\n    venue: NAACL Findings 2024\\n    url: https://arxiv.org/abs/2404.03098\\n    category: evidence_generation_tradeoff\\n    role: formal_framework\\n    key_finding: >\\n      用 multi-objective optimization 探索 performance vs explanation plausibility 的 Pareto frontier。\\n      引入 rationale 约束创建 contrastive loss，证实加入 rationale supervision 会降低主任务性能，\\n      但存在 Pareto optimal 解平衡两者。\\n    relevance_to_evidence_tradeoff: >\\n      提供了 performance-explainability trade-off 的形式化框架。\\n      我们的 evidence-grounded RE 降 8pp 正是 Pareto frontier 上的一个点。\\n      CED reranker 的效果可解读为：将系统从 evidence-constrained 点推向 Pareto frontier，\\n      在几乎不牺牲 evidence quality（evi_f1=0.8188）的前提下恢复 RE 性能。\\n      Related Work 引用点：evidence generation 的 performance cost 有理论依据。\\n\\n  - title: \\\"The Decreasing Value of Chain of Thought in Prompting\\\"\\n    authors: Meincke, Mollick, Mollick, Shapiro\\n    year: 2025\\n    venue: Wharton Generative AI Labs Technical Report (SSRN)\\n    url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5285532\\n    category: evidence_generation_tradeoff\\n    role: empirical_support\\n    key_finding: >\\n      现代 reasoning models 上 CoT 收益微弱（4-13%），但 latency 增加 35-600%。\\n      更强的模型从显式推理中受益越少。CoT 可能在 easy questions 上引入 errors\\n      （variability 增加导致原本正确的被改错）。\\n    relevance_to_evidence_tradeoff: >\\n      支持\\\"更强的 SFT 模型不需要在生成时显式输出 evidence\\\"的论点。\\n      我们的 evidence-only SFT 的性能下降符合\\\"显式推理的边际收益递减\\\"模式。\\n      Related Work 引用点：evidence generation 的 accuracy cost 不是 DocRE-specific，而是 LLM 的普遍趋势。\\n\\n  # === Category 10: Negative Transfer in Multi-task / Auxiliary-task Learning ===\\n\\n  - title: \\\"ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning\\\"\\n    authors: Jiang, Chen et al.\\n    year: 2023\\n    venue: NeurIPS 2023\\n    url: https://arxiv.org/abs/2301.12618\\n    category: negative_transfer\\n    role: theoretical_framework\\n    key_finding: >\\n      辅助任务常导致 negative transfer，根因不仅是 gradient conflict 还有 auxiliary-target\\n      generalization gap。ForkMerge 周期性 fork 模型为多分支，搜索最优 task weights，\\n      动态 merge 过滤有害 task-parameter updates。在多个 benchmark 上减少 negative transfer。\\n    relevance_to_evidence_tradeoff: >\\n      Evidence generation 作为 auxiliary task 对 RE 的 negative transfer 可用此框架解释：\\n      evidence 和 RE 的 gradient 方向不完全对齐，joint training 时 evidence 任务\\\"拖累\\\"RE。\\n      CED reranker 本质上是将 evidence quality 从 training-time joint objective 解耦到\\n      inference-time verification，避免了 training-time 的 negative transfer。\\n      Related Work 引用点：auxiliary task 导致主任务性能下降的一般性理论。\\n\\n  # === Category 11: Faithfulness vs Accuracy / Correctness Trade-off ===\\n\\n  - title: \\\"Correctness is not Faithfulness in RAG Attributions\\\"\\n    authors: Wallat, Heuss, de Rijke, Anand\\n    year: 2024\\n    venue: SIGIR 2025\\n    url: https://arxiv.org/abs/2412.18004\\n    category: faithfulness_accuracy_tradeoff\\n    role: key_conceptual_framework\\n    key_finding: >\\n      Correctness 和 faithfulness 是独立维度，可能冲突。高达 57% 的 citations 是\\n      post-rationalized（事后编造而非真实依据）。Unfaithful attributions 可能 factually correct，\\n      但 foster misguided trust。必须同时检查 correctness 和 faithfulness。\\n    relevance_to_evidence_tradeoff: >\\n      直接相关。我们的 evidence-grounded RE 试图让模型输出 faithful evidence，\\n      但这与 relation correctness 产生张力（rel_f1 降 8pp）。\\n      CED reranker 通过 NLI verification 确保 evidence 是 faithful 的（非 post-rationalized），\\n      同时不牺牲 RE accuracy。\\n      Related Work 引用点：correctness-faithfulness 分离的概念框架。\\n\\n  - title: \\\"Evaluating Correctness and Faithfulness of Instruction-Following Models for Question Answering\\\"\\n    authors: Adlakha, BehnamGhader, Lu, Meade, Reddy\\n    year: 2024\\n    venue: TACL 2024\\n    url: https://arxiv.org/abs/2307.16877\\n    category: faithfulness_accuracy_tradeoff\\n    role: evaluation_framework\\n    key_finding: >\\n      Instruction-following LLMs 在 correctness 上表现可比 fine-tuned models，\\n      但 faithfulness 普遍较差——模型会 hallucinate 而非忠实于提供的 evidence。\\n      传统 metrics 对 correctness 和 faithfulness 的评估均有缺陷。\\n    relevance_to_evidence_tradeoff: >\\n      解释了为什么 joint evidence+RE 生成性能差——模型在同时优化 correctness\\n      和 faithfulness 时，两个目标存在张力。单纯要求模型\\\"同时输出正确 triples 和\\n      faithful evidence\\\"是 multi-objective optimization 问题。\\n      Related Work 引用点：correctness vs faithfulness 评估方法论。\\n\\n  - title: \\\"Towards Faithful Model Explanation in NLP: A Survey\\\"\\n    authors: Lyu, Havaldar, Stein et al.\\n    year: 2024\\n    venue: Computational Linguistics (MIT Press)\\n    url: https://aclanthology.org/2024.cl-2.6/\\n    category: faithfulness_accuracy_tradeoff\\n    role: comprehensive_survey\\n    key_finding: >\\n      系统综述 NLP 中 faithful explanation 的定义、评估和生成方法。\\n      识别了 faithfulness-performance trade-off 作为核心挑战：\\n      更 faithful 的解释不一定更有用，更有用的解释不一定 faithful。\\n      提出未来方向包括 multi-objective optimization 和 post-hoc verification。\\n    relevance_to_evidence_tradeoff: >\\n      权威综述为我们的 evidence generation trade-off 提供广泛文献背景。\\n      我们的 CED reranker 正是该综述建议的\\\"post-hoc verification\\\"方向的具体实例。\\n      Related Work 引用点：faithfulness 研究的全景综述，定位我们的工作。\\n\\n  # === Category 12: Reranking / Verification as Bridge ===\\n\\n  - title: \\\"Genie: Achieving Human Parity in Content-Grounded Datasets Generation\\\"\\n    authors: Yehudai, Carmeli, Mass et al.\\n    year: 2024\\n    venue: ICLR 2024\\n    url: https://arxiv.org/abs/2401.14367\\n    category: reranking_verification_bridge\\n    role: methodological_precedent\\n    key_finding: >\\n      三阶段流程：Content Preparation → Generation → NLI-based Filtering。\\n      用 fine-tuned T5-11B NLI 模型判断生成内容是否 entailed by source（faithfulness 检验），\\n      过滤不 faithful 的生成。在 LFQA、摘要、IE 上达到 human parity。\\n    relevance_to_evidence_tradeoff: >\\n      方法论上最接近我们的 CED reranker——都是用 NLI verification 作为 post-hoc filter/reranker，\\n      在不牺牲主任务质量的前提下确保 grounding quality。\\n      GENIE 验证了 NLI-based filtering 在内容生成中的有效性。\\n      关键差异：GENIE 是 data generation pipeline 的过滤，我们是 inference-time reranking。\\n      Related Work 引用点：NLI-based verification 作为 bridge 的成功先例。\\n\", \"total_chars\": 29337, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 10_

<details><summary>Logged reasoning block</summary>

```text
I now have the full literature map. Let me analyze what's covered and what's missing, then search for papers in the specified directions. The existing map covers:

1. Reward diversity / reward shaping for RL stability
2. Mode collapse prevention in GRPO/RLHF
3. Contrastive rewards in RL
4. Evidence-based rewards in IE/NLP
5. Multi-objective RL for text generation
6. RSFT methodology & theory
7. RL for information extraction


8. Recent LLM-based DocRE methods
9. Evidence generation & task performance trade-off
10. Negative transfer in multi-task learning
11. Faithfulness vs accuracy/correctness trade-off
12. Reranking/verification as bridge

Now I'm launching parallel searches across document-level relation extraction with evidence, LLM applications in information extraction, reinforcement learning approaches for IE tasks, faithfulness and hallucination issues in structured prediction, and evidence-based reasoning in NLP.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "f43e4dac-6f0f-4916-bee2-3b48c644f217",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017tdewwGT6jC2QsbvJDLrDd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14210,
      "cache_read_input_tokens": 25215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14210
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

_source line 11_

已读取现有文献地图（12 个类别，约 35 篇论文）。现在并行搜索 5 个方向的新论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "cb809cc1-bd0f-47c4-a7cb-18051afe567a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017tdewwGT6jC2QsbvJDLrDd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14210,
      "cache_read_input_tokens": 25215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14210
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

_source line 12_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XrrrPTLgoewzrSuBqg4YNu`</summary>

```json
{
  "query": "document-level relation extraction evidence supporting sentences 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "daaa39a2-f55f-41e6-b558-8d3f65e02e87",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017tdewwGT6jC2QsbvJDLrDd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14210,
      "cache_read_input_tokens": 25215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14210
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

_source line 13 · 2026-05-15T22:08:03.719Z_

<details><summary>↩ Tool result · `toolu_01XrrrPTLgoewzrSuBqg4YNu`</summary>

```text
Web search results for query: "document-level relation extraction evidence supporting sentences 2024 2025 2026"

Links: [{"title":"Enhancing cross-evidence reasoning graph for document-level relation extraction - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11232587/"},{"title":"Three-stage document-level entity relation extraction | The Journal of Supercomputing | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11227-025-07068-2"},{"title":"Evidence-aware Document-level Relation Extraction | Proceedings of the 31st ACM International Conference on Information & Knowledge Management","url":"https://dl.acm.org/doi/10.1145/3511808.3557313"},{"title":"Document-Level Relation Extraction","url":"https://www.emergentmind.com/topics/document-level-relation-extraction"},{"title":"Document-Level Relation Extraction with Global ...","url":"https://aclanthology.org/2025.findings-acl.1002.pdf"},{"title":"Evidence and Axial Attention Guided Document-level Relation Extraction - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0885230824001116"},{"title":"[PDF] Entity and Evidence Guided Document-Level Relation Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Entity-and-Evidence-Guided-Document-Level-Relation-Huang-Qi/e4179bf0963012f9f13ce0ca61d3cdd12a87b336"},{"title":"Dual reasoning enhanced document-level relation extraction | Neural Computing and Applications | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s00521-026-12099-8"},{"title":"SRF: Enhancing Document-Level Relation Extraction with a Novel Secondary Reasoning Framework - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.863/"},{"title":"[2204.12679] Document-Level Relation Extraction with Sentences Importance Estimation and Focusing","url":"https://arxiv.org/abs/2204.12679"}]

I've completed the web search for "document-level relation extraction evidence supporting sentences 2024 2025 2026". Here are the key findings:

## Overview of Recent Research

Document-level relation extraction (RE) aims to identify semantic connections between named entities within a document. However, since most entities are distributed across different sentences, there is a need for inter-entity relation prediction across sentences.

## Evidence-Based Approaches

Recent research has increasingly focused on integrating evidence extraction into document-level relation extraction models. The SRF (Secondary Reasoning Framework) incorporates bidirectional mention fusion and an evidence extraction module for relation prediction. The E2GRE framework jointly extracts relations and underlying evidence sentences using large pretrained language models.

## Current Challenges and Methods (2024-2025)

Recent models address challenges such as multi-mention entities, long-distance entity relations, and complex relation reasoning. Inter-sentence F1 remains consistently 10–15 points below intra-sentence, highlighting the sustained challenge of long-distance reasoning.

## Advanced Techniques

The AutoRE system decomposes extraction into three modular steps—relation detection, head entity identification, and tail entity/fact prediction—with modular subtask decomposition using LoRA adapters for scalable handling of multi-relation, multi-sentence settings.

Recent approaches leverage information on potentially complex relations between entity pairs, relation reasoning, and supporting evidence.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "0a1b3ea3-ba78-47a5-9413-d8c7d85a4ecb",
  "tool_use_result": {
    "query": "document-level relation extraction evidence supporting sentences 2024 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CYLXiszxFT2vbvzBBu6Ftm",
        "content": [
          {
            "title": "Enhancing cross-evidence reasoning graph for document-level relation extraction - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11232587/"
          },
          {
            "title": "Three-stage document-level entity relation extraction | The Journal of Supercomputing | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s11227-025-07068-2"
          },
          {
            "title": "Evidence-aware Document-level Relation Extraction | Proceedings of the 31st ACM International Conference on Information & Knowledge Management",
            "url": "https://dl.acm.org/doi/10.1145/3511808.3557313"
          },
          {
            "title": "Document-Level Relation Extraction",
            "url": "https://www.emergentmind.com/topics/document-level-relation-extraction"
          },
          {
            "title": "Document-Level Relation Extraction with Global ...",
            "url": "https://aclanthology.org/2025.findings-acl.1002.pdf"
          },
          {
            "title": "Evidence and Axial Attention Guided Document-level Relation Extraction - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/abs/pii/S0885230824001116"
          },
          {
            "title": "[PDF] Entity and Evidence Guided Document-Level Relation Extraction | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Entity-and-Evidence-Guided-Document-Level-Relation-Huang-Qi/e4179bf0963012f9f13ce0ca61d3cdd12a87b336"
          },
          {
            "title": "Dual reasoning enhanced document-level relation extraction | Neural Computing and Applications | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s00521-026-12099-8"
          },
          {
            "title": "SRF: Enhancing Document-Level Relation Extraction with a Novel Secondary Reasoning Framework - ACL Anthology",
            "url": "https://aclanthology.org/2024.emnlp-main.863/"
          },
          {
            "title": "[2204.12679] Document-Level Relation Extraction with Sentences Importance Estimation and Focusing",
            "url": "https://arxiv.org/abs/2204.12679"
          }
        ]
      },
      "I've completed the web search for \"document-level relation extraction evidence supporting sentences 2024 2025 2026\". Here are the key findings:\n\n## Overview of Recent Research\n\nDocument-level relation extraction (RE) aims to identify semantic connections between named entities within a document. However, since most entities are distributed across different sentences, there is a need for inter-entity relation prediction across sentences.\n\n## Evidence-Based Approaches\n\nRecent research has increasingly focused on integrating evidence extraction into document-level relation extraction models. The SRF (Secondary Reasoning Framework) incorporates bidirectional mention fusion and an evidence extraction module for relation prediction. The E2GRE framework jointly extracts relations and underlying evidence sentences using large pretrained language models.\n\n## Current Challenges and Methods (2024-2025)\n\nRecent models address challenges such as multi-mention entities, long-distance entity relations, and complex relation reasoning. Inter-sentence F1 remains consistently 10–15 points below intra-sentence, highlighting the sustained challenge of long-distance reasoning.\n\n## Advanced Techniques\n\nThe AutoRE system decomposes extraction into three modular steps—relation detection, head entity identification, and tail entity/fact prediction—with modular subtask decomposition using LoRA adapters for scalable handling of multi-relation, multi-sentence settings.\n\nRecent approaches leverage information on potentially complex relations between entity pairs, relation reasoning, and supporting evidence."
    ],
    "durationSeconds": 7.104107472
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JNftnbpKJoWBTVJAooPKUB`</summary>

```json
{
  "query": "LLM large language model document-level relation extraction 2025 2026 fine-tuning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "ddac5fbb-db42-426a-a83c-17ed8b6e61fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BPEGT6DXJmVwhRdRTPM2ji",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1284,
      "cache_read_input_tokens": 39425,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1284
      },
      "output_tokens": 48,
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

_source line 15_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UdRRwoEa2SdTaX7RZ797gd`</summary>

```json
{
  "query": "GRPO reinforcement learning information extraction structured prediction 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "64c018c8-769a-4a12-895b-c755eb1288dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BPEGT6DXJmVwhRdRTPM2ji",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1284,
      "cache_read_input_tokens": 39425,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1284
      },
      "output_tokens": 48,
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

_source line 16_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DUbvr5DAAmcANG8tprrhG9`</summary>

```json
{
  "query": "faithfulness hallucination structured prediction information extraction 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "fdb97c69-7de8-4ed6-9ee5-537c3c21346f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BPEGT6DXJmVwhRdRTPM2ji",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1284,
      "cache_read_input_tokens": 39425,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1284
      },
      "output_tokens": 48,
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

_source line 17_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015r6BbrAugxzNJBdjbPi8nH`</summary>

```json
{
  "query": "evidence generation cost performance trade-off NLP explanation 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "5d201b19-8898-415e-aea3-a36d5de5329d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BPEGT6DXJmVwhRdRTPM2ji",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1284,
      "cache_read_input_tokens": 39425,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1284
      },
      "output_tokens": 48,
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

_source line 18 · 2026-05-15T22:08:14.409Z_

<details><summary>↩ Tool result · `toolu_01JNftnbpKJoWBTVJAooPKUB`</summary>

```text
Web search results for query: "LLM large language model document-level relation extraction 2025 2026 fine-tuning"

Links: [{"title":"AutoRE: Document-Level Relation Extraction with Large Language Models","url":"https://arxiv.org/html/2403.14888v1"},{"title":"The construction and refined extraction techniques of knowledge graph based on large language models | Scientific Reports","url":"https://www.nature.com/articles/s41598-026-38066-w"},{"title":"Benchmarking LLM-based Information Extraction Tools for ...","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full.pdf"},{"title":"[2403.14888] AutoRE: Document-Level Relation Extraction with Large Language Models","url":"https://arxiv.org/abs/2403.14888"},{"title":"Large Language Models in Document Intelligence: A Comprehensive Survey, Recent Advances, Challenges, and Future Trends | ACM Transactions on Information Systems","url":"https://dl.acm.org/doi/full/10.1145/3768156"},{"title":"A Comparative Analysis of Instruction Fine-Tuning Large Language Models for Financial Text Classification | ACM Transactions on Management Information Systems","url":"https://dl.acm.org/doi/10.1145/3706119"},{"title":"Large language model driven transferable key information extraction mechanism for nonstandardized tables | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-15627-z"},{"title":"GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub","url":"https://github.com/quqxui/Awesome-LLM4IE-Papers"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"},{"title":"Human level information extraction from clinical reports with finetuned language models | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-28767-z"}]

I've completed the web search for your query. Here are the key findings on LLMs, document-level relation extraction, and fine-tuning approaches from 2025-2026:

## Recent Research Highlights

**Document-Level Relation Extraction Challenges:**
Current LLMs still exhibit significant gaps in performance for DocRE, indicating a need for further fine-tuning. LLMs still perform poorly in DocRE tasks involving the extraction of multiple relations and triplet facts, achieving only single-digit scores.

**Fine-Tuning Approaches:**
AutoRE was created by fine-tuning the Mistral-7B with QLoRA, achieving SOTA results across multiple pre-trained LLMs. Fine-tuning base LLMs with domain-specific datasets enables them to better handle complex terminology and semantic nuances.

**Recent 2025-2026 Advances:**
LoRa-finetuned Llama-3.1 8B achieved non-inferior performance to the second human annotator across all four datasets, with an average exact match accuracy of 90.0 ± 1.7. A comprehensive survey analyzing approximately 300 papers published between 2021 and mid-2025 explores key topics including Retrieval-Augmented Generation (RAG), long-context processing, and fine-tuning LLMs for document comprehension.

**Fine-Tuning Effectiveness:**
Fine-tuning both base and instruct models leads to substantial improvements over zero-shot performance, with models excelling in tasks like relation extraction and hawkish-dovish classification, which are typically underrepresented in the pre-training data of most LLMs.

The search results indicate that while fine-tuning remains essential for document-level relation extraction tasks, recent progress with parameter-efficient approaches and domain-specific adaptation has significantly improved LLM performance in this area.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "0b13a5f0-00d2-410d-8c84-b790134162c5",
  "tool_use_result": {
    "query": "LLM large language model document-level relation extraction 2025 2026 fine-tuning",
    "results": [
      {
        "tool_use_id": "srvtoolu_019JcMraAy8F9UsTw6g6nk94",
        "content": [
          {
            "title": "AutoRE: Document-Level Relation Extraction with Large Language Models",
            "url": "https://arxiv.org/html/2403.14888v1"
          },
          {
            "title": "The construction and refined extraction techniques of knowledge graph based on large language models | Scientific Reports",
            "url": "https://www.nature.com/articles/s41598-026-38066-w"
          },
          {
            "title": "Benchmarking LLM-based Information Extraction Tools for ...",
            "url": "https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full.pdf"
          },
          {
            "title": "[2403.14888] AutoRE: Document-Level Relation Extraction with Large Language Models",
            "url": "https://arxiv.org/abs/2403.14888"
          },
          {
            "title": "Large Language Models in Document Intelligence: A Comprehensive Survey, Recent Advances, Challenges, and Future Trends | ACM Transactions on Information Systems",
            "url": "https://dl.acm.org/doi/full/10.1145/3768156"
          },
          {
            "title": "A Comparative Analysis of Instruction Fine-Tuning Large Language Models for Financial Text Classification | ACM Transactions on Management Information Systems",
            "url": "https://dl.acm.org/doi/10.1145/3706119"
          },
          {
            "title": "Large language model driven transferable key information extraction mechanism for nonstandardized tables | Scientific Reports",
            "url": "https://www.nature.com/articles/s41598-025-15627-z"
          },
          {
            "title": "GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub",
            "url": "https://github.com/quqxui/Awesome-LLM4IE-Papers"
          },
          {
            "title": "Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s11704-024-40555-y"
          },
          {
            "title": "Human level information extraction from clinical reports with finetuned language models | Scientific Reports",
            "url": "https://www.nature.com/articles/s41598-025-28767-z"
          }
        ]
      },
      "I've completed the web search for your query. Here are the key findings on LLMs, document-level relation extraction, and fine-tuning approaches from 2025-2026:\n\n## Recent Research Highlights\n\n**Document-Level Relation Extraction Challenges:**\nCurrent LLMs still exhibit significant gaps in performance for DocRE, indicating a need for further fine-tuning. LLMs still perform poorly in DocRE tasks involving the extraction of multiple relations and triplet facts, achieving only single-digit scores.\n\n**Fine-Tuning Approaches:**\nAutoRE was created by fine-tuning the Mistral-7B with QLoRA, achieving SOTA results across multiple pre-trained LLMs. Fine-tuning base LLMs with domain-specific datasets enables them to better handle complex terminology and semantic nuances.\n\n**Recent 2025-2026 Advances:**\nLoRa-finetuned Llama-3.1 8B achieved non-inferior performance to the second human annotator across all four datasets, with an average exact match accuracy of 90.0 ± 1.7. A comprehensive survey analyzing approximately 300 papers published between 2021 and mid-2025 explores key topics including Retrieval-Augmented Generation (RAG), long-context processing, and fine-tuning LLMs for document comprehension.\n\n**Fine-Tuning Effectiveness:**\nFine-tuning both base and instruct models leads to substantial improvements over zero-shot performance, with models excelling in tasks like relation extraction and hawkish-dovish classification, which are typically underrepresented in the pre-training data of most LLMs.\n\nThe search results indicate that while fine-tuning remains essential for document-level relation extraction tasks, recent progress with parameter-efficient approaches and domain-specific adaptation has significantly improved LLM performance in this area."
    ],
    "durationSeconds": 7.619617986999998
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T22:08:15.866Z_

<details><summary>↩ Tool result · `toolu_01UdRRwoEa2SdTaX7RZ797gd`</summary>

```text
Web search results for query: "GRPO reinforcement learning information extraction structured prediction 2025 2026"

Links: [{"title":"Fine-tuning a reasoning model with GRPO for passport data extraction","url":"https://rabiloo.com/blog/fine-tuning-a-reasoning-model-with-grpo-for-passport-data-extraction"},{"title":"GRPO in Reinforcement Learning Explained | DigitalOcean","url":"https://www.digitalocean.com/community/conceptual-articles/group-relative-policy-optimization-reinforcement-learning"},{"title":"A better way of extracting information with LLMs: GRPO Experiment","url":"https://infinitelambda.com/extract-info-llm-grpo/"},{"title":"Group Relative Policy Optimization (GRPO)","url":"https://cameronrwolfe.substack.com/p/grpo"},{"title":"What is GRPO? Group Relative Policy Optimization Explained | DataCamp","url":"https://www.datacamp.com/blog/what-is-grpo-group-relative-policy-optimization"},{"title":"Graph Reasoning-Tailored (GReaT) VLMs - Extended Abstract","url":"https://cs224r.stanford.edu/projects/pdfs/CS224R_Final_Project_Report-2.pdf"},{"title":"GRPO using Transformer Reinforcement Learning | by Yugen.ai | Yugen.ai Technology Blog | Medium","url":"https://medium.com/yugen-ai-technology-blog/grpo-using-transformer-reinforcement-learning-791ff4e8bb1d"},{"title":"Using QwQ to generate a reasoning dataset for structured data extraction – Daniel van Strien","url":"https://danielvanstrien.xyz/posts/2025/reasoning-models/generating-structured-data-extraction-dataset-with-qwq-and-curator.html"},{"title":"GRPO Reinforcement Learning","url":"https://www.emergentmind.com/topics/grpo-reinforcement-learning"},{"title":"Extended Abstract - CS 224R Deep Reinforcement Learning","url":"https://cs224r.stanford.edu/projects/pdfs/CS224R_Final_Report__2_%20(3).pdf"}]

Based on the web search results, here's what I found about GRPO (Group Relative Policy Optimization) in reinforcement learning for information extraction and structured prediction:

## Overview of GRPO

Group Relative Policy Optimization (GRPO) is an improvement over Proximal Policy Optimization (PPO), specifically designed to make reinforcement learning for large language models (LLMs) more efficient. While it gained widespread attention after the release of DeepSeek-R1, GRPO was first introduced in DeepSeekMath, an LLM fine-tuned for advanced mathematical reasoning.

## Application to Information Extraction & Structured Prediction

From a reinforcement learning perspective, extracting information is a good fit for GRPO-style training because it lends itself naturally to rule-based and programmatic scoring. 

Recent applications (2025-2026) show promising results:

- **Passport Data Extraction**: Group Relative Policy Optimization (GRPO) is used for fine-tuning a reasoning model for passport data extraction, starting with Supervised Fine-Tuning (SFT) and then refining it using reinforcement learning (RL) to improve accuracy and reasoning.

- **Information Extraction Performance**: GRPO effectively improves structural reliability and consistency, and once the model reliably produces well-formed outputs and aligned responses, stronger correctness signals can be introduced without destabilizing behavior.

## Technical Advantages

The main difference from PPO is that GRPO removes the need for a separate value function model, instead using relative comparisons within groups of outputs to calculate advantages, making GRPO more lightweight in terms of computation and memory.

## Broader Applications (2025-2026)

Competitive or state-of-the-art results have been achieved in language reasoning, multimodal generation, robotics, and video understanding, underpinning post-training and alignment procedures.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "3422f2f2-306b-4352-a7ef-3491055d664b",
  "tool_use_result": {
    "query": "GRPO reinforcement learning information extraction structured prediction 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AEuBmTeGswzAQGLiwvfmUm",
        "content": [
          {
            "title": "Fine-tuning a reasoning model with GRPO for passport data extraction",
            "url": "https://rabiloo.com/blog/fine-tuning-a-reasoning-model-with-grpo-for-passport-data-extraction"
          },
          {
            "title": "GRPO in Reinforcement Learning Explained | DigitalOcean",
            "url": "https://www.digitalocean.com/community/conceptual-articles/group-relative-policy-optimization-reinforcement-learning"
          },
          {
            "title": "A better way of extracting information with LLMs: GRPO Experiment",
            "url": "https://infinitelambda.com/extract-info-llm-grpo/"
          },
          {
            "title": "Group Relative Policy Optimization (GRPO)",
            "url": "https://cameronrwolfe.substack.com/p/grpo"
          },
          {
            "title": "What is GRPO? Group Relative Policy Optimization Explained | DataCamp",
            "url": "https://www.datacamp.com/blog/what-is-grpo-group-relative-policy-optimization"
          },
          {
            "title": "Graph Reasoning-Tailored (GReaT) VLMs - Extended Abstract",
            "url": "https://cs224r.stanford.edu/projects/pdfs/CS224R_Final_Project_Report-2.pdf"
          },
          {
            "title": "GRPO using Transformer Reinforcement Learning | by Yugen.ai | Yugen.ai Technology Blog | Medium",
            "url": "https://medium.com/yugen-ai-technology-blog/grpo-using-transformer-reinforcement-learning-791ff4e8bb1d"
          },
          {
            "title": "Using QwQ to generate a reasoning dataset for structured data extraction – Daniel van Strien",
            "url": "https://danielvanstrien.xyz/posts/2025/reasoning-models/generating-structured-data-extraction-dataset-with-qwq-and-curator.html"
          },
          {
            "title": "GRPO Reinforcement Learning",
            "url": "https://www.emergentmind.com/topics/grpo-reinforcement-learning"
          },
          {
            "title": "Extended Abstract - CS 224R Deep Reinforcement Learning",
            "url": "https://cs224r.stanford.edu/projects/pdfs/CS224R_Final_Report__2_%20(3).pdf"
          }
        ]
      },
      "Based on the web search results, here's what I found about GRPO (Group Relative Policy Optimization) in reinforcement learning for information extraction and structured prediction:\n\n## Overview of GRPO\n\nGroup Relative Policy Optimization (GRPO) is an improvement over Proximal Policy Optimization (PPO), specifically designed to make reinforcement learning for large language models (LLMs) more efficient. While it gained widespread attention after the release of DeepSeek-R1, GRPO was first introduced in DeepSeekMath, an LLM fine-tuned for advanced mathematical reasoning.\n\n## Application to Information Extraction & Structured Prediction\n\nFrom a reinforcement learning perspective, extracting information is a good fit for GRPO-style training because it lends itself naturally to rule-based and programmatic scoring. \n\nRecent applications (2025-2026) show promising results:\n\n- **Passport Data Extraction**: Group Relative Policy Optimization (GRPO) is used for fine-tuning a reasoning model for passport data extraction, starting with Supervised Fine-Tuning (SFT) and then refining it using reinforcement learning (RL) to improve accuracy and reasoning.\n\n- **Information Extraction Performance**: GRPO effectively improves structural reliability and consistency, and once the model reliably produces well-formed outputs and aligned responses, stronger correctness signals can be introduced without destabilizing behavior.\n\n## Technical Advantages\n\nThe main difference from PPO is that GRPO removes the need for a separate value function model, instead using relative comparisons within groups of outputs to calculate advantages, making GRPO more lightweight in terms of computation and memory.\n\n## Broader Applications (2025-2026)\n\nCompetitive or state-of-the-art results have been achieved in language reasoning, multimodal generation, robotics, and video understanding, underpinning post-training and alignment procedures."
    ],
    "durationSeconds": 8.602790230000005
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T22:08:15.924Z_

<details><summary>↩ Tool result · `toolu_015r6BbrAugxzNJBdjbPi8nH`</summary>

```text
Web search results for query: "evidence generation cost performance trade-off NLP explanation 2024 2025 2026"

Links: [{"title":"Privacy-Preserving LLM Inference in Practice: A","url":"https://eprint.iacr.org/2026/105.pdf"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Sometimes Painful but Promising: Feasibility and Trade-offs of On-Device","url":"https://arxiv.org/pdf/2503.09114"},{"title":"R2LM 2025 Proceedings of the","url":"https://aclanthology.org/2025.r2lm-1.pdf"},{"title":"Large Language Model Agents in Finance: A Survey ...","url":"https://aclanthology.org/2025.findings-emnlp.972.pdf"},{"title":"Paper Digest: EMNLP 2025 Papers & Highlights – Paper Digest","url":"https://www.paperdigest.org/2025/11/emnlp-2025-papers-highlights/"},{"title":"Finance Language Model Evaluation (FLAME)","url":"https://aclanthology.org/2025.findings-acl.1164.pdf"},{"title":"The Economics of Accuracy for Medical Reasoning with Large Language Models","url":"https://www.medrxiv.org/content/10.64898/2025.12.22.25342804v1.full.pdf"},{"title":"LLMOrbit: A Circular Taxonomy of Large Language Models","url":"https://arxiv.org/pdf/2601.14053"},{"title":"Old Dominion University Old Dominion University ODU Digital Commons","url":"https://digitalcommons.odu.edu/cgi/viewcontent.cgi?article=1521&context=ece_fac_pubs"}]

I've completed a web search for your query about evidence generation, cost-performance trade-offs, and NLP explanations in 2024-2026. Here are the key findings:

## Key Findings from Recent NLP Research (2024-2026)

### Cost-Performance Trade-offs in NLP Deployment

Production deployment of NLP technologies raises challenges including latency and cost constraints, with trade-offs between quality and practicality. This is a significant concern for real-world implementations beyond controlled lab settings.

### Model Optimization and Efficiency

Recent work has focused on balancing performance with resource constraints. GPT-4o represents a balance between speed and cost-efficiency without sacrificing too much performance, demonstrating how optimizations like quantization and adaptive batching can achieve inference efficiency gains.

Research in 2025 specifically examined the feasibility and trade-offs of on-device language model inference, indicating growing interest in resource-constrained deployment scenarios.

### Data Quality vs. Scale Trade-offs

An emerging paradigm addresses the scaling wall through data quality optimization. Research demonstrates that capability depends on both data quality and scale, with data quality potentially dominating scale beyond certain thresholds. As data scarcity becomes acute around 2026-2028, learning efficiency matters more than scale efficiency, with approaches like filtering web datasets using quality judges and training on high-quality curated data.

### Industry-Focused Evaluation

Real-world NLP deployment faces challenges including latency, cost constraints, shifting user behavior, maintenance over time, and trade-offs between quality and practicality, which are driving new evaluation methodologies in industry applications.

The search results show that cost-performance trade-offs remain a central research concern in NLP systems deployed in 2024-2026, with increasing focus on data quality optimization and edge deployment feasibility.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "e39031be-def0-4d73-87c6-5d53facfe842",
  "tool_use_result": {
    "query": "evidence generation cost performance trade-off NLP explanation 2024 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MNiLbqG7wu2czyhbRSgF3w",
        "content": [
          {
            "title": "Privacy-Preserving LLM Inference in Practice: A",
            "url": "https://eprint.iacr.org/2026/105.pdf"
          },
          {
            "title": "Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026",
            "url": "https://2026.emnlp.org/calls/industry_track/"
          },
          {
            "title": "Sometimes Painful but Promising: Feasibility and Trade-offs of On-Device",
            "url": "https://arxiv.org/pdf/2503.09114"
          },
          {
            "title": "R2LM 2025 Proceedings of the",
            "url": "https://aclanthology.org/2025.r2lm-1.pdf"
          },
          {
            "title": "Large Language Model Agents in Finance: A Survey ...",
            "url": "https://aclanthology.org/2025.findings-emnlp.972.pdf"
          },
          {
            "title": "Paper Digest: EMNLP 2025 Papers & Highlights – Paper Digest",
            "url": "https://www.paperdigest.org/2025/11/emnlp-2025-papers-highlights/"
          },
          {
            "title": "Finance Language Model Evaluation (FLAME)",
            "url": "https://aclanthology.org/2025.findings-acl.1164.pdf"
          },
          {
            "title": "The Economics of Accuracy for Medical Reasoning with Large Language Models",
            "url": "https://www.medrxiv.org/content/10.64898/2025.12.22.25342804v1.full.pdf"
          },
          {
            "title": "LLMOrbit: A Circular Taxonomy of Large Language Models",
            "url": "https://arxiv.org/pdf/2601.14053"
          },
          {
            "title": "Old Dominion University Old Dominion University ODU Digital Commons",
            "url": "https://digitalcommons.odu.edu/cgi/viewcontent.cgi?article=1521&context=ece_fac_pubs"
          }
        ]
      },
      "I've completed a web search for your query about evidence generation, cost-performance trade-offs, and NLP explanations in 2024-2026. Here are the key findings:\n\n## Key Findings from Recent NLP Research (2024-2026)\n\n### Cost-Performance Trade-offs in NLP Deployment\n\nProduction deployment of NLP technologies raises challenges including latency and cost constraints, with trade-offs between quality and practicality. This is a significant concern for real-world implementations beyond controlled lab settings.\n\n### Model Optimization and Efficiency\n\nRecent work has focused on balancing performance with resource constraints. GPT-4o represents a balance between speed and cost-efficiency without sacrificing too much performance, demonstrating how optimizations like quantization and adaptive batching can achieve inference efficiency gains.\n\nResearch in 2025 specifically examined the feasibility and trade-offs of on-device language model inference, indicating growing interest in resource-constrained deployment scenarios.\n\n### Data Quality vs. Scale Trade-offs\n\nAn emerging paradigm addresses the scaling wall through data quality optimization. Research demonstrates that capability depends on both data quality and scale, with data quality potentially dominating scale beyond certain thresholds. As data scarcity becomes acute around 2026-2028, learning efficiency matters more than scale efficiency, with approaches like filtering web datasets using quality judges and training on high-quality curated data.\n\n### Industry-Focused Evaluation\n\nReal-world NLP deployment faces challenges including latency, cost constraints, shifting user behavior, maintenance over time, and trade-offs between quality and practicality, which are driving new evaluation methodologies in industry applications.\n\nThe search results show that cost-performance trade-offs remain a central research concern in NLP systems deployed in 2024-2026, with increasing focus on data quality optimization and edge deployment feasibility."
    ],
    "durationSeconds": 7.614969410999998
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T22:08:17.843Z_

<details><summary>↩ Tool result · `toolu_01DUbvr5DAAmcANG8tprrhG9`</summary>

```text
Web search results for query: "faithfulness hallucination structured prediction information extraction 2024 2025"

Links: [{"title":"Large Language Models Hallucination: A Comprehensive Survey","url":"https://arxiv.org/html/2510.06265v2"},{"title":"A hallucination detection and mitigation framework for faithful text summarization using LLMs | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-31075-1"},{"title":"A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions | ACM Transactions on Information Systems","url":"https://dl.acm.org/doi/10.1145/3703155"},{"title":"Quantifying Hallucination in Faithfulness Evaluation","url":"https://aclanthology.org/2025.findings-naacl.433.pdf"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/cfcadfe84ee49908cde1fc2992c38d20-Paper-Conference.pdf"},{"title":"The Mirage of Hallucination Detection","url":"https://aclanthology.org/2025.findings-emnlp.1035.pdf"},{"title":"Faithfulness Hallucination Detection","url":"https://www.emergentmind.com/topics/faithfulness-hallucination-detection"},{"title":"On A Scale From 1 to 5: Quantifying Hallucination in Faithfulness Evaluation","url":"https://arxiv.org/html/2410.12222v3"},{"title":"A Review of Faithfulness Metrics for Hallucination Assessment in Large Language Models | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/iel8/4200690/5418892/11032180.pdf"},{"title":"GitHub - EdinburghNLP/awesome-hallucination-detection: List of papers on hallucination detection in LLMs. · GitHub","url":"https://github.com/EdinburghNLP/awesome-hallucination-detection"}]

Based on the web search results, here's a comprehensive overview of recent research on faithfulness, hallucination, structured prediction, and information extraction in 2024-2025:

## Hallucination Classification and Detection

Faithfulness hallucination occurs when the generated output drifts from the original input or context, violating the user's instructions or violating the logical consistency within the response, and is further categorized into three subtypes: instruction, context, and logical.

Existing strategies for detecting hallucinations in LLMs can be categorized based on the type of hallucination: (1) factuality hallucination detection, which aims to identify factual inaccuracies in the model's outputs, and (2) faithfulness hallucination detection, which focuses on evaluating the faithfulness of model's outputs to the contextual information provided.

## Recent Advances in Detection and Mitigation

A hallucination detection and mitigation framework employs a Question-Answer Generation, Sorting, and Evaluation (Q-S-E) methodology to enable the quantitative detection of hallucinations in summaries, incorporating an iterative hallucination resolution mechanism which enhances the transparency of the modification process and improves the faithfulness of text summarization.

Cognitive hallucinations are far more prevalent than factual ones (up to 65%), with SOTA detectors showing sharp performance degradation for cognitive errors.

## Structured Prediction and Information Extraction

FAITH: Domain-specific masked numeric span prediction over financial documents; high-precision matching exposes errors in value, unit, scale, calculation, and latent variable reasoning.

For open-ended or long-form text, hallucination detection exploits triple-oriented segmentation and graph-based alignment. The GCA method constructs knowledge graphs from extracted triples, aggregates context via Relational Graph Convolutional Networks (RGCN), and uses reverse LLM-based verification to validate the presence, relations, and dependencies between facts.

## Evaluation of Faithfulness

The use of Large Language Models (LLMs) as a faithfulness evaluator is commonly the metric that is most highly correlated with human judgement.

## Emerging Challenges

A critical zero-sum dynamic shows that interventions targeting factuality often degrade faithfulness, and vice versa. SPACE resolves this by showing that both hallucination types share overlapping subspaces within neural representations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "c7f2bbb3-aeac-4665-bfe7-dd2d3fd6fd63",
  "tool_use_result": {
    "query": "faithfulness hallucination structured prediction information extraction 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01R3qgtpHU1pLevGgv59VkJo",
        "content": [
          {
            "title": "Large Language Models Hallucination: A Comprehensive Survey",
            "url": "https://arxiv.org/html/2510.06265v2"
          },
          {
            "title": "A hallucination detection and mitigation framework for faithful text summarization using LLMs | Scientific Reports",
            "url": "https://www.nature.com/articles/s41598-025-31075-1"
          },
          {
            "title": "A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions | ACM Transactions on Information Systems",
            "url": "https://dl.acm.org/doi/10.1145/3703155"
          },
          {
            "title": "Quantifying Hallucination in Faithfulness Evaluation",
            "url": "https://aclanthology.org/2025.findings-naacl.433.pdf"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/cfcadfe84ee49908cde1fc2992c38d20-Paper-Conference.pdf"
          },
          {
            "title": "The Mirage of Hallucination Detection",
            "url": "https://aclanthology.org/2025.findings-emnlp.1035.pdf"
          },
          {
            "title": "Faithfulness Hallucination Detection",
            "url": "https://www.emergentmind.com/topics/faithfulness-hallucination-detection"
          },
          {
            "title": "On A Scale From 1 to 5: Quantifying Hallucination in Faithfulness Evaluation",
            "url": "https://arxiv.org/html/2410.12222v3"
          },
          {
            "title": "A Review of Faithfulness Metrics for Hallucination Assessment in Large Language Models | IEEE Journals & Magazine | IEEE Xplore",
            "url": "https://ieeexplore.ieee.org/iel8/4200690/5418892/11032180.pdf"
          },
          {
            "title": "GitHub - EdinburghNLP/awesome-hallucination-detection: List of papers on hallucination detection in LLMs. · GitHub",
            "url": "https://github.com/EdinburghNLP/awesome-hallucination-detection"
          }
        ]
      },
      "Based on the web search results, here's a comprehensive overview of recent research on faithfulness, hallucination, structured prediction, and information extraction in 2024-2025:\n\n## Hallucination Classification and Detection\n\nFaithfulness hallucination occurs when the generated output drifts from the original input or context, violating the user's instructions or violating the logical consistency within the response, and is further categorized into three subtypes: instruction, context, and logical.\n\nExisting strategies for detecting hallucinations in LLMs can be categorized based on the type of hallucination: (1) factuality hallucination detection, which aims to identify factual inaccuracies in the model's outputs, and (2) faithfulness hallucination detection, which focuses on evaluating the faithfulness of model's outputs to the contextual information provided.\n\n## Recent Advances in Detection and Mitigation\n\nA hallucination detection and mitigation framework employs a Question-Answer Generation, Sorting, and Evaluation (Q-S-E) methodology to enable the quantitative detection of hallucinations in summaries, incorporating an iterative hallucination resolution mechanism which enhances the transparency of the modification process and improves the faithfulness of text summarization.\n\nCognitive hallucinations are far more prevalent than factual ones (up to 65%), with SOTA detectors showing sharp performance degradation for cognitive errors.\n\n## Structured Prediction and Information Extraction\n\nFAITH: Domain-specific masked numeric span prediction over financial documents; high-precision matching exposes errors in value, unit, scale, calculation, and latent variable reasoning.\n\nFor open-ended or long-form text, hallucination detection exploits triple-oriented segmentation and graph-based alignment. The GCA method constructs knowledge graphs from extracted triples, aggregates context via Relational Graph Convolutional Networks (RGCN), and uses reverse LLM-based verification to validate the presence, relations, and dependencies between facts.\n\n## Evaluation of Faithfulness\n\nThe use of Large Language Models (LLMs) as a faithfulness evaluator is commonly the metric that is most highly correlated with human judgement.\n\n## Emerging Challenges\n\nA critical zero-sum dynamic shows that interventions targeting factuality often degrade faithfulness, and vice versa. SPACE resolves this by showing that both hallucination types share overlapping subspaces within neural representations."
    ],
    "durationSeconds": 10.045125416000003
  }
}
```

</details>

---

### Assistant

_source line 22_

<details><summary>Logged reasoning block</summary>

```text
The initial searches gave some results but I need more targeted searches. Let me search for more specific topics:
1. Task decoupling in multi-task learning / RL
2. QLoRA-specific issues in GRPO/RL training
3. More recent DocRE papers with evidence
4. GRPO for IE specifically (R1-RE like papers)
5. Evidence tax / cost of explanation generation
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "2b808061-642e-4bb0-a319-fa6df5609219",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S8seShiqhfMThgNoY1vvg1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 923,
      "cache_creation_input_tokens": 3336,
      "cache_read_input_tokens": 40709,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3336
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

_source line 23_

需要更精准的搜索。继续搜索几个关键方向。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "0c4d5669-013d-48a3-9950-0464c821a46e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S8seShiqhfMThgNoY1vvg1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 923,
      "cache_creation_input_tokens": 3336,
      "cache_read_input_tokens": 40709,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3336
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

_source line 24_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JARsWpAj5ESVCd4KKGiqyy`</summary>

```json
{
  "query": "\"task decoupling\" OR \"reward hacking\" QLoRA GRPO reinforcement learning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "4b013512-e763-4e65-bf46-1a3e00dad243",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S8seShiqhfMThgNoY1vvg1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 923,
      "cache_creation_input_tokens": 3336,
      "cache_read_input_tokens": 40709,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3336
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

_source line 25_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AYfB1KNngFz6VuTC75DMgY`</summary>

```json
{
  "query": "DocRED Re-DocRED LLM generative relation extraction 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "22279e5e-06e5-4d72-b6aa-9e9b549aa7e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S8seShiqhfMThgNoY1vvg1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 923,
      "cache_creation_input_tokens": 3336,
      "cache_read_input_tokens": 40709,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3336
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

_source line 26_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FqDMfRxMCTFxJspQGzxHgD`</summary>

```json
{
  "query": "RLVR GRPO relation extraction named entity recognition structured output 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "0411fd2a-c826-4eeb-8598-d88a7b310daf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S8seShiqhfMThgNoY1vvg1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 923,
      "cache_creation_input_tokens": 3336,
      "cache_read_input_tokens": 40709,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3336
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

_source line 27_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SFtSrSfEkbdgqwVnxxEVUx`</summary>

```json
{
  "query": "\"evidence tax\" OR \"cost of explanation\" OR \"explanation hurts performance\" chain-of-thought reasoning 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "993e92a9-5a2a-4e7e-9d76-959fa388c6df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S8seShiqhfMThgNoY1vvg1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 923,
      "cache_creation_input_tokens": 3336,
      "cache_read_input_tokens": 40709,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3336
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

_source line 28 · 2026-05-15T22:08:31.110Z_

<details><summary>↩ Tool result · `toolu_01JARsWpAj5ESVCd4KKGiqyy`</summary>

```text
Web search results for query: ""task decoupling" OR "reward hacking" QLoRA GRPO reinforcement learning 2025 2026"

Links: [{"title":"Reward Hacking in Reinforcement Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"},{"title":"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges","url":"https://arxiv.org/html/2604.13602v1"},{"title":"Overcoming reward signal challenges: Verifiable rewards-based reinforcement learning with GRPO on SageMaker AI | Artificial Intelligence","url":"https://aws.amazon.com/blogs/machine-learning/overcoming-reward-signal-challenges-verifiable-rewards-based-reinforcement-learning-with-grpo-on-sagemaker-ai/"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=reward+hacking"},{"title":"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems","url":"https://arxiv.org/html/2509.22047"},{"title":"From Verifiable Dot to Reward Chain: Harnessing Verifiable Reference-based Rewards for Reinforcement Learning of Open-ended Generation","url":"https://arxiv.org/html/2601.18533v1"},{"title":"[2509.22047] MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems","url":"https://arxiv.org/abs/2509.22047"},{"title":"Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://arxiv.org/html/2502.18770v3"},{"title":"A brief example of reward hacking in GRPO","url":"https://ishanjmukherjee.github.io/reward-hacking-grpo"},{"title":"[2604.13602] Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges","url":"https://arxiv.org/abs/2604.13602"}]

I've completed the web search. Here are the key findings related to task decoupling, reward hacking, QLoRA, GRPO, and reinforcement learning from recent research (2025-2026):

## Task Decoupling and Reward Hacking

Task decoupling means that the query action for collecting feedback is sampled independently from the action taken in the world, preventing the action from corrupting its own feedback. One architectural intervention decouples the reward for honesty from the main task's reward through a separate, post-generation report mechanism.

## GRPO and Reward Hacking Vulnerabilities

Recent research has identified significant issues with GRPO in multi-objective settings. GRPO is vulnerable to reward hacking in multi-objective settings, optimizing only one objective at the cost of others. MO-GRPO has been proposed as an extension with a normalization method to reweight reward functions automatically.

Recent work on generative reward models trained via GRPO reveals that while "thinking" variants consistently outperform answer-only models on validation tasks, these gains diminish and often reverse during downstream policy optimization.

## QLoRA Integration

GRPO is being used with Quantized Low-Rank Adaptation (QLoRA) to reduce training resource requirements and speed up the training process, with a small trade-off in accuracy.

## Key Mechanisms and Defenses

Reward hacking occurs when models exploit imperfections in learned reward signals to maximize proxy objectives, manifesting as verbosity bias, sycophancy, hallucinated justification, and benchmark overfitting.

The search results show active research on these topics through early 2026, with multiple papers addressing vulnerabilities in GRPO-based reinforcement learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "24863a8b-9f66-428d-9c5e-742c6a0c0412",
  "tool_use_result": {
    "query": "\"task decoupling\" OR \"reward hacking\" QLoRA GRPO reinforcement learning 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UQa5Yhs9pur75VVipXisJT",
        "content": [
          {
            "title": "Reward Hacking in Reinforcement Learning | Lil'Log",
            "url": "https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"
          },
          {
            "title": "Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges",
            "url": "https://arxiv.org/html/2604.13602v1"
          },
          {
            "title": "Overcoming reward signal challenges: Verifiable rewards-based reinforcement learning with GRPO on SageMaker AI | Artificial Intelligence",
            "url": "https://aws.amazon.com/blogs/machine-learning/overcoming-reward-signal-challenges-verifiable-rewards-based-reinforcement-learning-with-grpo-on-sagemaker-ai/"
          },
          {
            "title": "Daily Papers - Hugging Face",
            "url": "https://huggingface.co/papers?q=reward+hacking"
          },
          {
            "title": "MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems",
            "url": "https://arxiv.org/html/2509.22047"
          },
          {
            "title": "From Verifiable Dot to Reward Chain: Harnessing Verifiable Reference-based Rewards for Reinforcement Learning of Open-ended Generation",
            "url": "https://arxiv.org/html/2601.18533v1"
          },
          {
            "title": "[2509.22047] MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems",
            "url": "https://arxiv.org/abs/2509.22047"
          },
          {
            "title": "Reward Shaping to Mitigate Reward Hacking in RLHF",
            "url": "https://arxiv.org/html/2502.18770v3"
          },
          {
            "title": "A brief example of reward hacking in GRPO",
            "url": "https://ishanjmukherjee.github.io/reward-hacking-grpo"
          },
          {
            "title": "[2604.13602] Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges",
            "url": "https://arxiv.org/abs/2604.13602"
          }
        ]
      },
      "I've completed the web search. Here are the key findings related to task decoupling, reward hacking, QLoRA, GRPO, and reinforcement learning from recent research (2025-2026):\n\n## Task Decoupling and Reward Hacking\n\nTask decoupling means that the query action for collecting feedback is sampled independently from the action taken in the world, preventing the action from corrupting its own feedback. One architectural intervention decouples the reward for honesty from the main task's reward through a separate, post-generation report mechanism.\n\n## GRPO and Reward Hacking Vulnerabilities\n\nRecent research has identified significant issues with GRPO in multi-objective settings. GRPO is vulnerable to reward hacking in multi-objective settings, optimizing only one objective at the cost of others. MO-GRPO has been proposed as an extension with a normalization method to reweight reward functions automatically.\n\nRecent work on generative reward models trained via GRPO reveals that while \"thinking\" variants consistently outperform answer-only models on validation tasks, these gains diminish and often reverse during downstream policy optimization.\n\n## QLoRA Integration\n\nGRPO is being used with Quantized Low-Rank Adaptation (QLoRA) to reduce training resource requirements and speed up the training process, with a small trade-off in accuracy.\n\n## Key Mechanisms and Defenses\n\nReward hacking occurs when models exploit imperfections in learned reward signals to maximize proxy objectives, manifesting as verbosity bias, sycophancy, hallucinated justification, and benchmark overfitting.\n\nThe search results show active research on these topics through early 2026, with multiple papers addressing vulnerabilities in GRPO-based reinforcement learning."
    ],
    "durationSeconds": 7.160431649000006
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-15T22:08:31.763Z_

<details><summary>↩ Tool result · `toolu_01AYfB1KNngFz6VuTC75DMgY`</summary>

```text
Web search results for query: "DocRED Re-DocRED LLM generative relation extraction 2025 2026 arxiv"

Links: [{"title":"AutoRE: Document-Level Relation Extraction with Large Language Models","url":"https://arxiv.org/html/2403.14888v1"},{"title":"LLM with Relation Classifier for Document-Level Relation Extraction","url":"https://arxiv.org/html/2408.13889"},{"title":"Relation as a Prior: A Novel Paradigm for LLM-based Document-level Relation Extraction","url":"https://arxiv.org/html/2511.08143v1"},{"title":"GLiDRE: Generalist Lightweight model for Document-level Relation Extraction","url":"https://arxiv.org/html/2508.00757"},{"title":"[1906.06127] DocRED: A Large-Scale Document-Level Relation Extraction Dataset","url":"https://arxiv.org/abs/1906.06127"},{"title":"[PDF] DocRED: A Large-Scale Document-Level Relation Extraction Dataset | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DocRED:-A-Large-Scale-Document-Level-Relation-Yao-Ye/2745fc72e1dd53d1c30f17cf05841b163c2f63c9"},{"title":"A Temporal Knowledge Graph Generation Dataset Supervised Distantly by Large Language Models | Scientific Data","url":"https://www.nature.com/articles/s41597-025-05062-0"},{"title":"A Dynamic Self-Evolving Extraction System","url":"https://arxiv.org/html/2603.06915"},{"title":"[2403.14888] AutoRE: Document-Level Relation Extraction with Large Language Models","url":"https://arxiv.org/abs/2403.14888"},{"title":"Leveraging Large Language Models for Document-Level Complex Relation Extraction Through Self-Verification and Tool-Assisted Relational Reasoning | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-96-9812-7_32"}]

I've found several relevant papers on document-level relation extraction (DocRE) using LLMs. Here are the key findings from the search results:

## Recent Research (2025-2026)

A novel "Relation as a Prior" (RelPrior) paradigm for LLM-based DocRE proposes fine-tuning a binary classification LLM to filter unrelated entity pairs and uses relations as a prior to match entity pairs, transforming relation extraction into a task of judging both entity pairs and relations to avoid arbitrary generation issues of LLMs.

GLiDRE, a generalist lightweight model for document-level relation extraction, achieves competitive performance on the Re-DocRED benchmark.

## 2024-2025 Research

Recent LLM-based methods employ fine-tuning, in-context learning, or retrieval augmented generation, though direct fine-tuning of LLMs and other LLM-based methods show suboptimal performance and inefficiencies in processing capabilities for DocRE.

AutoRE introduces an end-to-end DocRE model adopting a novel RE extraction paradigm called RHF (Relation-Head-Facts) to handle datasets like Re-DocRED with 96 relation types.

## Key Challenges

Current LLMs exhibit significant gaps in performance for DocRE, existing RE templates struggle with multiple relations, and there is a need for a paradigm shift in relation extraction approaches.

These papers indicate ongoing research efforts to improve LLM-based generative approaches for document-level relation extraction, particularly addressing challenges with multiple relation types and document complexity.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "32029116-f55b-44ae-80ba-bca72d484585",
  "tool_use_result": {
    "query": "DocRED Re-DocRED LLM generative relation extraction 2025 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01T8cS4giiQR8YnW8d52dNzF",
        "content": [
          {
            "title": "AutoRE: Document-Level Relation Extraction with Large Language Models",
            "url": "https://arxiv.org/html/2403.14888v1"
          },
          {
            "title": "LLM with Relation Classifier for Document-Level Relation Extraction",
            "url": "https://arxiv.org/html/2408.13889"
          },
          {
            "title": "Relation as a Prior: A Novel Paradigm for LLM-based Document-level Relation Extraction",
            "url": "https://arxiv.org/html/2511.08143v1"
          },
          {
            "title": "GLiDRE: Generalist Lightweight model for Document-level Relation Extraction",
            "url": "https://arxiv.org/html/2508.00757"
          },
          {
            "title": "[1906.06127] DocRED: A Large-Scale Document-Level Relation Extraction Dataset",
            "url": "https://arxiv.org/abs/1906.06127"
          },
          {
            "title": "[PDF] DocRED: A Large-Scale Document-Level Relation Extraction Dataset | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/DocRED:-A-Large-Scale-Document-Level-Relation-Yao-Ye/2745fc72e1dd53d1c30f17cf05841b163c2f63c9"
          },
          {
            "title": "A Temporal Knowledge Graph Generation Dataset Supervised Distantly by Large Language Models | Scientific Data",
            "url": "https://www.nature.com/articles/s41597-025-05062-0"
          },
          {
            "title": "A Dynamic Self-Evolving Extraction System",
            "url": "https://arxiv.org/html/2603.06915"
          },
          {
            "title": "[2403.14888] AutoRE: Document-Level Relation Extraction with Large Language Models",
            "url": "https://arxiv.org/abs/2403.14888"
          },
          {
            "title": "Leveraging Large Language Models for Document-Level Complex Relation Extraction Through Self-Verification and Tool-Assisted Relational Reasoning | Springer Nature Link",
            "url": "https://link.springer.com/chapter/10.1007/978-981-96-9812-7_32"
          }
        ]
      },
      "I've found several relevant papers on document-level relation extraction (DocRE) using LLMs. Here are the key findings from the search results:\n\n## Recent Research (2025-2026)\n\nA novel \"Relation as a Prior\" (RelPrior) paradigm for LLM-based DocRE proposes fine-tuning a binary classification LLM to filter unrelated entity pairs and uses relations as a prior to match entity pairs, transforming relation extraction into a task of judging both entity pairs and relations to avoid arbitrary generation issues of LLMs.\n\nGLiDRE, a generalist lightweight model for document-level relation extraction, achieves competitive performance on the Re-DocRED benchmark.\n\n## 2024-2025 Research\n\nRecent LLM-based methods employ fine-tuning, in-context learning, or retrieval augmented generation, though direct fine-tuning of LLMs and other LLM-based methods show suboptimal performance and inefficiencies in processing capabilities for DocRE.\n\nAutoRE introduces an end-to-end DocRE model adopting a novel RE extraction paradigm called RHF (Relation-Head-Facts) to handle datasets like Re-DocRED with 96 relation types.\n\n## Key Challenges\n\nCurrent LLMs exhibit significant gaps in performance for DocRE, existing RE templates struggle with multiple relations, and there is a need for a paradigm shift in relation extraction approaches.\n\nThese papers indicate ongoing research efforts to improve LLM-based generative approaches for document-level relation extraction, particularly addressing challenges with multiple relation types and document complexity."
    ],
    "durationSeconds": 7.351753092999999
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T22:08:33.170Z_

<details><summary>↩ Tool result · `toolu_01SFtSrSfEkbdgqwVnxxEVUx`</summary>

```text
Web search results for query: ""evidence tax" OR "cost of explanation" OR "explanation hurts performance" chain-of-thought reasoning 2024 2025"

Links: [{"title":"Chain-of-Thought Is Not Explainability Fazl Barez∗ Oxford WhiteBox Tung-Yu Wu","url":"https://aigi.ox.ac.uk/wp-content/uploads/2025/07/Cot_Is_Not_Explainability.pdf"},{"title":"GitHub - zchuz/CoT-Reasoning-Survey: [ACL 2024] A Survey of Chain of Thought Reasoning: Advances, Frontiers and Future","url":"https://github.com/zchuz/CoT-Reasoning-Survey"},{"title":"Interactive Reasoning: Visualizing and Controlling Chain- ...","url":"https://homes.cs.washington.edu/~ypang2/papers/uist25-interactive-reasoning.pdf"},{"title":"Leveraging Reasoning Paths for Efficient LLM Sampling","url":"https://aclanthology.org/2025.naacl-long.184.pdf"},{"title":"A Comprehensive Survey on Latent Chain-of-Thought ...","url":"https://arxiv.org/pdf/2505.16782"},{"title":"May 23, 2025 Seek in the Dark: Reasoning via Test-Time Instance-Level Policy","url":"http://www.stat.ucla.edu/~ywu/2025Henry.pdf"},{"title":"Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning | Request PDF","url":"https://www.researchgate.net/publication/386203451_Making_Reasoning_Matter_Measuring_and_Improving_Faithfulness_of_Chain-of-Thought_Reasoning"},{"title":"Sketch-of-Thought: Efficient LLM Reasoning with Adaptive ...","url":"https://aclanthology.org/2025.emnlp-main.1236.pdf"},{"title":"Chain-of-Thought Prompting as a Catalyst for GPT-4.5 ...","url":"https://www.irjet.net/archives/V12/i6/IRJET-V12I6142.pdf"},{"title":"Evaluating Step-by-step Reasoning Traces: A Survey","url":"https://aclanthology.org/2025.findings-emnlp.94.pdf"}]

I found research on chain-of-thought reasoning from 2024-2025, though the specific terms "evidence tax," "cost of explanation," or "explanation hurts performance" don't appear directly in these results. However, I did find highly relevant recent work on related topics:

## Key Findings on Chain-of-Thought and Explanations (2024-2025):

**CoT Faithfulness Concerns**: Recent studies reveal that CoTs are often unfaithful: they may contain factual mistakes, incoherent steps, or post-hoc rationalizations that obscure the true reasoning process. Additionally, LLMs can be trained to produce irrelevant reasoning text and still provide accurate final answers.

**Latent vs. Explicit Reasoning**: Recent research has explored efficiency trade-offs. Reasoning capabilities can be internalized within the latent space through fine-tuning, but their performance remains inferior to that of Chain-of-Thought (CoT).

**Explanations as External State**: Recent work reframes reasoning tokens not as a linguistic narrative, but as an externalized computational state—the sole persistent information carrier across the model's stateless generation cycles.

**Performance Optimization**: Research shows that boosting LLM reasoning with reinforced context pruning can improve performance, suggesting potential efficiency gains.

The research indicates tensions between producing explicit explanations and optimal performance, though the exact framing of "evidence tax" may be emerging terminology not yet widely adopted in the published literature I found.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "854c855d-3150-4b09-ac1d-a104ac9424c8",
  "tool_use_result": {
    "query": "\"evidence tax\" OR \"cost of explanation\" OR \"explanation hurts performance\" chain-of-thought reasoning 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_0152oysbm9ep4scYvuVYLhMr",
        "content": [
          {
            "title": "Chain-of-Thought Is Not Explainability Fazl Barez∗ Oxford WhiteBox Tung-Yu Wu",
            "url": "https://aigi.ox.ac.uk/wp-content/uploads/2025/07/Cot_Is_Not_Explainability.pdf"
          },
          {
            "title": "GitHub - zchuz/CoT-Reasoning-Survey: [ACL 2024] A Survey of Chain of Thought Reasoning: Advances, Frontiers and Future",
            "url": "https://github.com/zchuz/CoT-Reasoning-Survey"
          },
          {
            "title": "Interactive Reasoning: Visualizing and Controlling Chain- ...",
            "url": "https://homes.cs.washington.edu/~ypang2/papers/uist25-interactive-reasoning.pdf"
          },
          {
            "title": "Leveraging Reasoning Paths for Efficient LLM Sampling",
            "url": "https://aclanthology.org/2025.naacl-long.184.pdf"
          },
          {
            "title": "A Comprehensive Survey on Latent Chain-of-Thought ...",
            "url": "https://arxiv.org/pdf/2505.16782"
          },
          {
            "title": "May 23, 2025 Seek in the Dark: Reasoning via Test-Time Instance-Level Policy",
            "url": "http://www.stat.ucla.edu/~ywu/2025Henry.pdf"
          },
          {
            "title": "Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning | Request PDF",
            "url": "https://www.researchgate.net/publication/386203451_Making_Reasoning_Matter_Measuring_and_Improving_Faithfulness_of_Chain-of-Thought_Reasoning"
          },
          {
            "title": "Sketch-of-Thought: Efficient LLM Reasoning with Adaptive ...",
            "url": "https://aclanthology.org/2025.emnlp-main.1236.pdf"
          },
          {
            "title": "Chain-of-Thought Prompting as a Catalyst for GPT-4.5 ...",
            "url": "https://www.irjet.net/archives/V12/i6/IRJET-V12I6142.pdf"
          },
          {
            "title": "Evaluating Step-by-step Reasoning Traces: A Survey",
            "url": "https://aclanthology.org/2025.findings-emnlp.94.pdf"
          }
        ]
      },
      "I found research on chain-of-thought reasoning from 2024-2025, though the specific terms \"evidence tax,\" \"cost of explanation,\" or \"explanation hurts performance\" don't appear directly in these results. However, I did find highly relevant recent work on related topics:\n\n## Key Findings on Chain-of-Thought and Explanations (2024-2025):\n\n**CoT Faithfulness Concerns**: Recent studies reveal that CoTs are often unfaithful: they may contain factual mistakes, incoherent steps, or post-hoc rationalizations that obscure the true reasoning process. Additionally, LLMs can be trained to produce irrelevant reasoning text and still provide accurate final answers.\n\n**Latent vs. Explicit Reasoning**: Recent research has explored efficiency trade-offs. Reasoning capabilities can be internalized within the latent space through fine-tuning, but their performance remains inferior to that of Chain-of-Thought (CoT).\n\n**Explanations as External State**: Recent work reframes reasoning tokens not as a linguistic narrative, but as an externalized computational state—the sole persistent information carrier across the model's stateless generation cycles.\n\n**Performance Optimization**: Research shows that boosting LLM reasoning with reinforced context pruning can improve performance, suggesting potential efficiency gains.\n\nThe research indicates tensions between producing explicit explanations and optimal performance, though the exact framing of \"evidence tax\" may be emerging terminology not yet widely adopted in the published literature I found."
    ],
    "durationSeconds": 7.3182758960000065
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-15T22:08:33.605Z_

<details><summary>↩ Tool result · `toolu_01FqDMfRxMCTFxJspQGzxHgD`</summary>

```text
Web search results for query: "RLVR GRPO relation extraction named entity recognition structured output 2025 2026 arxiv"

Links: [{"title":"R1-RE: Cross-Domain Relation Extraction with RLVR","url":"https://arxiv.org/html/2507.04642"},{"title":"R1-RE: Cross-Domain Relationship Extraction with RLVR","url":"https://arxiv.org/html/2507.04642v1"},{"title":"Beyond path selection: Better LLMs for Scientific Information Extraction with MimicSFT and Relevance and Rule-induced(R2)GRPO","url":"https://arxiv.org/html/2505.22068"},{"title":"A systematic review of relation extraction task since the emergence of","url":"https://arxiv.org/pdf/2511.03610"},{"title":"R1-RE: Cross-Domain Relation Extraction with RLVR Runpeng Dai1 Tong Zheng2","url":"https://arxiv.org/pdf/2507.04642"},{"title":"Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs","url":"https://arxiv.org/html/2506.14245v1"},{"title":"RLPR: Extrapolating RLVR to general domains without verifiers","url":"https://arxiv.org/html/2506.18254v1"},{"title":"Retrieval-Enhanced Named Entity Recognition","url":"https://arxiv.org/html/2410.13118v1"},{"title":"Outcome-based Reinforcement Learning to Predict the Future","url":"https://arxiv.org/html/2505.17989v2/"},{"title":"Structured Entity Extraction Using Large Language Models","url":"https://arxiv.org/html/2402.04437v3"}]

Based on the search results, I found several highly relevant papers on your query about RLVR, GRPO, relation extraction, named entity recognition, and structured output from 2025-2026. Here are the key findings:

## R1-RE: Cross-Domain Relation Extraction with RLVR

The most directly relevant work uses the GRPO algorithm as described in recent research. R1-RE is a novel framework designed to enhance the reasoning capabilities of LLMs for RE tasks, inspired by reinforcement learning with verifiable reward (RLVR).

The framework includes a format reward component that checks whether the model's response adheres to a specified structure, directly addressing your interest in structured output. The approach adopts a rule-based reward scheme similar to those used in DeepSeek-R1-Zero and Logic R1.

Traditional pipeline-based relation extraction methods follow a two-step procedure: first applying named entity recognition (NER), then performing relation classification on the identified entity pairs.

## R2GRPO: Scientific Information Extraction

Another relevant work combines RLVR with structured reasoning. R2GRPO is a two-phase training method that combines MimicSFT with a novel reward function incorporating relevance and rule-mining to jointly optimize knowledge grounding and reasoning paths, with hierarchical reasoning that decomposes complex extraction tasks into structured reasoning steps that satisfy both schema and factual constraints.

## General RLVR Landscape

RLVR has been explored across a variety of domains, including logic games, search, and machine translation, though its application to knowledge extraction or relation extraction tasks remains underexplored.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "d62dd85b-85a7-449e-99c2-20e4c86b7022",
  "tool_use_result": {
    "query": "RLVR GRPO relation extraction named entity recognition structured output 2025 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01YXQKwPUcDd5HCT6UpYsySp",
        "content": [
          {
            "title": "R1-RE: Cross-Domain Relation Extraction with RLVR",
            "url": "https://arxiv.org/html/2507.04642"
          },
          {
            "title": "R1-RE: Cross-Domain Relationship Extraction with RLVR",
            "url": "https://arxiv.org/html/2507.04642v1"
          },
          {
            "title": "Beyond path selection: Better LLMs for Scientific Information Extraction with MimicSFT and Relevance and Rule-induced(R2)GRPO",
            "url": "https://arxiv.org/html/2505.22068"
          },
          {
            "title": "A systematic review of relation extraction task since the emergence of",
            "url": "https://arxiv.org/pdf/2511.03610"
          },
          {
            "title": "R1-RE: Cross-Domain Relation Extraction with RLVR Runpeng Dai1 Tong Zheng2",
            "url": "https://arxiv.org/pdf/2507.04642"
          },
          {
            "title": "Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs",
            "url": "https://arxiv.org/html/2506.14245v1"
          },
          {
            "title": "RLPR: Extrapolating RLVR to general domains without verifiers",
            "url": "https://arxiv.org/html/2506.18254v1"
          },
          {
            "title": "Retrieval-Enhanced Named Entity Recognition",
            "url": "https://arxiv.org/html/2410.13118v1"
          },
          {
            "title": "Outcome-based Reinforcement Learning to Predict the Future",
            "url": "https://arxiv.org/html/2505.17989v2/"
          },
          {
            "title": "Structured Entity Extraction Using Large Language Models",
            "url": "https://arxiv.org/html/2402.04437v3"
          }
        ]
      },
      "Based on the search results, I found several highly relevant papers on your query about RLVR, GRPO, relation extraction, named entity recognition, and structured output from 2025-2026. Here are the key findings:\n\n## R1-RE: Cross-Domain Relation Extraction with RLVR\n\nThe most directly relevant work uses the GRPO algorithm as described in recent research. R1-RE is a novel framework designed to enhance the reasoning capabilities of LLMs for RE tasks, inspired by reinforcement learning with verifiable reward (RLVR).\n\nThe framework includes a format reward component that checks whether the model's response adheres to a specified structure, directly addressing your interest in structured output. The approach adopts a rule-based reward scheme similar to those used in DeepSeek-R1-Zero and Logic R1.\n\nTraditional pipeline-based relation extraction methods follow a two-step procedure: first applying named entity recognition (NER), then performing relation classification on the identified entity pairs.\n\n## R2GRPO: Scientific Information Extraction\n\nAnother relevant work combines RLVR with structured reasoning. R2GRPO is a two-phase training method that combines MimicSFT with a novel reward function incorporating relevance and rule-mining to jointly optimize knowledge grounding and reasoning paths, with hierarchical reasoning that decomposes complex extraction tasks into structured reasoning steps that satisfy both schema and factual constraints.\n\n## General RLVR Landscape\n\nRLVR has been explored across a variety of domains, including logic games, search, and machine translation, though its application to knowledge extraction or relation extraction tasks remains underexplored."
    ],
    "durationSeconds": 8.185906328000005
  }
}
```

</details>

---

### Assistant

_source line 32_

<details><summary>Logged reasoning block</summary>

```text
Good findings so far. Let me do a few more targeted searches:
1. MO-GRPO paper (multi-objective GRPO and reward hacking) 
2. R2GRPO for scientific IE
3. "evidence extraction" + "relation extraction" joint learning
4. QLoRA vs full fine-tuning GRPO differences
5. Latent CoT / internalized reasoning vs explicit reasoning tradeoff
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "f684b653-285e-4ee5-b75c-3a8477ac0a1c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NM6fuQDh8eHTFTXknT7RnM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 961,
      "cache_creation_input_tokens": 4179,
      "cache_read_input_tokens": 44045,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4179
      },
      "output_tokens": 9,
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

_source line 33_

找到一些有价值的新线索。继续深挖几个关键论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "37444e63-c358-4fd8-8fc6-4547cf0d1b18",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NM6fuQDh8eHTFTXknT7RnM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 961,
      "cache_creation_input_tokens": 4179,
      "cache_read_input_tokens": 44045,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4179
      },
      "output_tokens": 9,
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

_source line 34_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016ujBGfwvvsAJBqevWuLZ6q`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.22047",
  "prompt": "Extract: title, authors, venue, year, abstract, key method, key findings. This is about MO-GRPO for multi-objective problems."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "04f07ba6-af03-45b3-8e8c-7457c93c80eb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NM6fuQDh8eHTFTXknT7RnM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 961,
      "cache_creation_input_tokens": 4179,
      "cache_read_input_tokens": 44045,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4179
      },
      "output_tokens": 9,
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

_source line 35_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014k3fRuuwNq117vNkUog1Jd`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.22068",
  "prompt": "Extract: title, authors, venue, year, abstract, key method, key findings. This is about R2GRPO for scientific information extraction."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "90af78ec-a8d1-4313-82d8-246bc79e8637",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NM6fuQDh8eHTFTXknT7RnM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 961,
      "cache_creation_input_tokens": 4179,
      "cache_read_input_tokens": 44045,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4179
      },
      "output_tokens": 9,
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

_source line 36_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FbTaySVkkrVm1RQsejYNTQ`</summary>

```json
{
  "query": "QLoRA full fine-tuning difference reinforcement learning GRPO training instability 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "d5c160ff-14cf-450a-ac5c-1e21f16b8352",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NM6fuQDh8eHTFTXknT7RnM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 961,
      "cache_creation_input_tokens": 4179,
      "cache_read_input_tokens": 44045,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4179
      },
      "output_tokens": 9,
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

_source line 37_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BKtBYnts3oZuRrLqL2mxoB`</summary>

```json
{
  "query": "\"joint extraction\" \"evidence\" \"relation\" document-level LLM 2025 2026 supporting sentence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "c14eed5c-fb56-4c0a-9aca-0e06953db437",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NM6fuQDh8eHTFTXknT7RnM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 961,
      "cache_creation_input_tokens": 4179,
      "cache_read_input_tokens": 44045,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4179
      },
      "output_tokens": 9,
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

_source line 38 · 2026-05-15T22:08:44.426Z_

<details><summary>↩ Tool result · `toolu_014k3fRuuwNq117vNkUog1Jd`</summary>

```text
# Research Paper Summary

**Title:** Beyond path selection: Better LLMs for Scientific Information Extraction with MimicSFT and Relevance and Rule-induced(R²)GRPO

**Authors:** Ran Li, Shimin Di, Yuchen Liu, Chen Jing, Yu Qiu, Lei Chen

**Venue:** arXiv (Computer Science > Computation and Language)

**Year:** 2025 (submitted May 28, 2025)

**Abstract:** The researchers investigate how large language models can be improved for scientific information extraction tasks. They propose that both supervised fine-tuning and reinforcement learning approaches can enhance reasoning capacity, contrary to previous findings limited to math reasoning.

**Key Methods:**
1. **MimicSFT** — A structured reasoning template approach that doesn't require high-quality chain-of-thought training data
2. **R²GRPO** — A two-stage training method incorporating relevance and rule-based reward signals

**Key Findings:** The combined approach outperformed baseline language models and specialized supervised models on relation extraction benchmarks. The work demonstrates that both reasoning refinement and capacity improvement are achievable in scientific information extraction tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "602f7496-6b1e-466d-8789-9b7f49111885",
  "tool_use_result": {
    "bytes": 45523,
    "code": 200,
    "codeText": "OK",
    "result": "# Research Paper Summary\n\n**Title:** Beyond path selection: Better LLMs for Scientific Information Extraction with MimicSFT and Relevance and Rule-induced(R²)GRPO\n\n**Authors:** Ran Li, Shimin Di, Yuchen Liu, Chen Jing, Yu Qiu, Lei Chen\n\n**Venue:** arXiv (Computer Science > Computation and Language)\n\n**Year:** 2025 (submitted May 28, 2025)\n\n**Abstract:** The researchers investigate how large language models can be improved for scientific information extraction tasks. They propose that both supervised fine-tuning and reinforcement learning approaches can enhance reasoning capacity, contrary to previous findings limited to math reasoning.\n\n**Key Methods:**\n1. **MimicSFT** — A structured reasoning template approach that doesn't require high-quality chain-of-thought training data\n2. **R²GRPO** — A two-stage training method incorporating relevance and rule-based reward signals\n\n**Key Findings:** The combined approach outperformed baseline language models and specialized supervised models on relation extraction benchmarks. The work demonstrates that both reasoning refinement and capacity improvement are achievable in scientific information extraction tasks.",
    "durationMs": 3877,
    "url": "https://arxiv.org/abs/2505.22068"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-15T22:08:44.661Z_

<details><summary>↩ Tool result · `toolu_016ujBGfwvvsAJBqevWuLZ6q`</summary>

```text
# MO-GRPO Paper Summary

**Title:** MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems

**Authors:** Yuki Ichihara, Yuu Jinnai, Tetsuro Morimura, Mitsuki Sakamoto, Ryota Mitsuhashi, Eiji Uchibe

**Venue:** arXiv (Computer Science > Machine Learning)

**Year:** 2025 (submitted September 26, 2025; revised January 9, 2026)

**Abstract Summary:** The paper addresses vulnerability in GRPO algorithms when applied to multi-objective settings. The core problem is that "GRPO is vulnerable to reward hacking, optimizing only one of the objectives at the cost of the others."

**Key Method:** MO-GRPO introduces "a simple normalization method to reweight the reward functions automatically according to the variances of their values." This approach ensures balanced contribution across objectives while maintaining preference ordering without manual tuning.

**Key Findings:** Testing across four domains—multi-armed bandits, simulated control (Mo-Gymnasium), machine translation (WMT benchmarks), and instruction following—demonstrates that MO-GRPO achieves "stable learning by evenly distributing correlations among the components of rewards," outperforming standard GRPO.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "82815595-3428-44c9-9b23-21b51ebb471e",
  "tool_use_result": {
    "bytes": 47717,
    "code": 200,
    "codeText": "OK",
    "result": "# MO-GRPO Paper Summary\n\n**Title:** MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems\n\n**Authors:** Yuki Ichihara, Yuu Jinnai, Tetsuro Morimura, Mitsuki Sakamoto, Ryota Mitsuhashi, Eiji Uchibe\n\n**Venue:** arXiv (Computer Science > Machine Learning)\n\n**Year:** 2025 (submitted September 26, 2025; revised January 9, 2026)\n\n**Abstract Summary:** The paper addresses vulnerability in GRPO algorithms when applied to multi-objective settings. The core problem is that \"GRPO is vulnerable to reward hacking, optimizing only one of the objectives at the cost of the others.\"\n\n**Key Method:** MO-GRPO introduces \"a simple normalization method to reweight the reward functions automatically according to the variances of their values.\" This approach ensures balanced contribution across objectives while maintaining preference ordering without manual tuning.\n\n**Key Findings:** Testing across four domains—multi-armed bandits, simulated control (Mo-Gymnasium), machine translation (WMT benchmarks), and instruction following—demonstrates that MO-GRPO achieves \"stable learning by evenly distributing correlations among the components of rewards,\" outperforming standard GRPO.",
    "durationMs": 4594,
    "url": "https://arxiv.org/abs/2509.22047"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T22:08:49.071Z_

<details><summary>↩ Tool result · `toolu_01FbTaySVkkrVm1RQsejYNTQ`</summary>

```text
Web search results for query: "QLoRA full fine-tuning difference reinforcement learning GRPO training instability 2025"

Links: [{"title":"LoRA vs QLoRA: Best AI Model Fine-Tuning Platforms & Tools 2026 | Index.dev","url":"https://www.index.dev/blog/top-ai-fine-tuning-tools-lora-vs-qlora-vs-full"},{"title":"Fine-Tuning LLMs with LoRA and QLoRA: From Confusion to (Kinda) Working Results | by Deepesh Sharma | Medium","url":"https://medium.com/@dsh.2065/fine-tuning-llms-with-lora-and-qlora-from-confusion-to-kinda-working-results-89b348bcce71"},{"title":"Fine-tuning LLMs Guide | Unsloth Documentation","url":"https://unsloth.ai/docs/get-started/fine-tuning-llms-guide"},{"title":"LoRA fine-tuning Hyperparameters Guide | Unsloth Documentation","url":"https://unsloth.ai/docs/get-started/fine-tuning-llms-guide/lora-hyperparameters-guide"},{"title":"Fine-Tuning using LoRA and QLoRA - GeeksforGeeks","url":"https://www.geeksforgeeks.org/deep-learning/fine-tuning-using-lora-and-qlora/"},{"title":"Fine-Tune LLMs with LoRA and QLoRA: 2026 Guide — Effloow","url":"https://effloow.com/articles/llm-fine-tuning-lora-qlora-guide-2026"},{"title":"Fine-tuning LLMs with Reinforcement Learning | by Mehul Jain | Data Science + AI at Microsoft | Medium","url":"https://medium.com/data-science-at-microsoft/fine-tuning-llms-with-reinforcement-learning-ef84fe42d6a6"},{"title":"QLoRA vs LoRA: Which Fine‑Tuning Wins? - Newline.co","url":"https://www.newline.co/@Dipen/qlora-vs-lora-which-finetuning-wins--683ca660"},{"title":"GitHub - artidoro/qlora: QLoRA: Efficient Finetuning of Quantized LLMs · GitHub","url":"https://github.com/artidoro/qlora"},{"title":"LoRA & QLoRA: A Comprehensive Guide to Efficient LLM Fine-Tuning | by Irfan Mansuri | Medium","url":"https://medium.com/@mansuri4638/lora-qlora-a-comprehensive-guide-to-efficient-llm-fine-tuning-9a88886d4751"}]

Based on the search results, here's what I found regarding your query about QLoRA, full fine-tuning differences, reinforcement learning, GRPO, and training instability:

## QLoRA vs Full Fine-Tuning Differences

LoRA is a parameter efficient training method that typically keeps the base model's weights frozen and trains a small set of added low-rank adapter weights (in 16-bit precision), while QLoRA combines LoRA with 4-bit precision to handle very large models with minimal resources.

QLoRA works by loading the base language model in a highly compressed 4-bit quantized format, drastically reducing memory usage, while training small LoRA adapters in higher precision. During fine-tuning, only these adapters are updated, compensating for any quantization errors and preserving model performance.

Performance-wise, QLoRA typically achieves 80–90% of full fine-tuning performance, compared to 90–95% for standard LoRA.

## Reinforcement Learning & GRPO

Generalized Preference Automation (GRPO) builds upon DPO by extending it to handle ranked lists of outputs and arbitrary utility or reward functions. While DPO operates on binary preference pairs (chosen versus rejected), GRPO uses full or partial rankings of responses to derive a target distribution that reflects the relative desirability of all outputs.

## Training Instability with GRPO

The search results mention that for reinforcement learning phases (PPO/GRPO), training instability issues related to poor generation quality can be addressed by increasing the KL penalty, or alternatively, switching to Direct Preference Optimization (DPO) with better paired preference data.

Additionally, for Reinforcement Learning (DPO, GRPO etc.), a learning rate of 5e-6 is recommended, which differs from the standard fine-tuning rates.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "baaa1f7f-90ee-4007-b038-bf496cf95a3a",
  "tool_use_result": {
    "query": "QLoRA full fine-tuning difference reinforcement learning GRPO training instability 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CoEBMsXP82KB5Ry7NZzV2u",
        "content": [
          {
            "title": "LoRA vs QLoRA: Best AI Model Fine-Tuning Platforms & Tools 2026 | Index.dev",
            "url": "https://www.index.dev/blog/top-ai-fine-tuning-tools-lora-vs-qlora-vs-full"
          },
          {
            "title": "Fine-Tuning LLMs with LoRA and QLoRA: From Confusion to (Kinda) Working Results | by Deepesh Sharma | Medium",
            "url": "https://medium.com/@dsh.2065/fine-tuning-llms-with-lora-and-qlora-from-confusion-to-kinda-working-results-89b348bcce71"
          },
          {
            "title": "Fine-tuning LLMs Guide | Unsloth Documentation",
            "url": "https://unsloth.ai/docs/get-started/fine-tuning-llms-guide"
          },
          {
            "title": "LoRA fine-tuning Hyperparameters Guide | Unsloth Documentation",
            "url": "https://unsloth.ai/docs/get-started/fine-tuning-llms-guide/lora-hyperparameters-guide"
          },
          {
            "title": "Fine-Tuning using LoRA and QLoRA - GeeksforGeeks",
            "url": "https://www.geeksforgeeks.org/deep-learning/fine-tuning-using-lora-and-qlora/"
          },
          {
            "title": "Fine-Tune LLMs with LoRA and QLoRA: 2026 Guide — Effloow",
            "url": "https://effloow.com/articles/llm-fine-tuning-lora-qlora-guide-2026"
          },
          {
            "title": "Fine-tuning LLMs with Reinforcement Learning | by Mehul Jain | Data Science + AI at Microsoft | Medium",
            "url": "https://medium.com/data-science-at-microsoft/fine-tuning-llms-with-reinforcement-learning-ef84fe42d6a6"
          },
          {
            "title": "QLoRA vs LoRA: Which Fine‑Tuning Wins? - Newline.co",
            "url": "https://www.newline.co/@Dipen/qlora-vs-lora-which-finetuning-wins--683ca660"
          },
          {
            "title": "GitHub - artidoro/qlora: QLoRA: Efficient Finetuning of Quantized LLMs · GitHub",
            "url": "https://github.com/artidoro/qlora"
          },
          {
            "title": "LoRA & QLoRA: A Comprehensive Guide to Efficient LLM Fine-Tuning | by Irfan Mansuri | Medium",
            "url": "https://medium.com/@mansuri4638/lora-qlora-a-comprehensive-guide-to-efficient-llm-fine-tuning-9a88886d4751"
          }
        ]
      },
      "Based on the search results, here's what I found regarding your query about QLoRA, full fine-tuning differences, reinforcement learning, GRPO, and training instability:\n\n## QLoRA vs Full Fine-Tuning Differences\n\nLoRA is a parameter efficient training method that typically keeps the base model's weights frozen and trains a small set of added low-rank adapter weights (in 16-bit precision), while QLoRA combines LoRA with 4-bit precision to handle very large models with minimal resources.\n\nQLoRA works by loading the base language model in a highly compressed 4-bit quantized format, drastically reducing memory usage, while training small LoRA adapters in higher precision. During fine-tuning, only these adapters are updated, compensating for any quantization errors and preserving model performance.\n\nPerformance-wise, QLoRA typically achieves 80–90% of full fine-tuning performance, compared to 90–95% for standard LoRA.\n\n## Reinforcement Learning & GRPO\n\nGeneralized Preference Automation (GRPO) builds upon DPO by extending it to handle ranked lists of outputs and arbitrary utility or reward functions. While DPO operates on binary preference pairs (chosen versus rejected), GRPO uses full or partial rankings of responses to derive a target distribution that reflects the relative desirability of all outputs.\n\n## Training Instability with GRPO\n\nThe search results mention that for reinforcement learning phases (PPO/GRPO), training instability issues related to poor generation quality can be addressed by increasing the KL penalty, or alternatively, switching to Direct Preference Optimization (DPO) with better paired preference data.\n\nAdditionally, for Reinforcement Learning (DPO, GRPO etc.), a learning rate of 5e-6 is recommended, which differs from the standard fine-tuning rates."
    ],
    "durationSeconds": 7.591537399000008
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-15T22:08:49.210Z_

<details><summary>↩ Tool result · `toolu_01BKtBYnts3oZuRrLqL2mxoB`</summary>

```text
Web search results for query: ""joint extraction" "evidence" "relation" document-level LLM 2025 2026 supporting sentence"

Links: [{"title":"Structured information extraction from scientific text with large language models | Nature Communications","url":"https://www.nature.com/articles/s41467-024-45563-x"},{"title":"Large language model augmented joint learning framework for entity-relation extraction - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S1568494625014073"},{"title":"Benchmarking LLM-based Information Extraction Tools for ...","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full.pdf"},{"title":"Few-Shot Relation Extraction via Two-Stage Knowledge- ...","url":"https://www.ijcai.org/proceedings/2025/0897.pdf"},{"title":"GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub","url":"https://github.com/quqxui/Awesome-LLM4IE-Papers"},{"title":"Survey on legal information extraction: current status and open challenges | Knowledge and Information Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10115-025-02600-5"},{"title":"Information Extraction from Visually Rich Documents using ...","url":"https://aclanthology.org/2025.acl-long.844.pdf"},{"title":"Benchmarking LLM-based Information Extraction Tools for Medical Documents | medRxiv","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full"},{"title":"LLM-empowered knowledge graph construction: A survey","url":"https://arxiv.org/pdf/2510.20345"},{"title":"Exploring LLMs for Scientific Information Extraction using the SciEx Framework","url":"https://arxiv.org/html/2512.10004v2"}]

I've completed a web search for your query about joint extraction, evidence, relations, document-level LLM work from 2025-2026. Here are the key findings:

## Recent Research on Document-Level Joint Extraction with LLMs

Research has presented approaches to joint named entity recognition and relation extraction that demonstrate how pretrained large language models like GPT-3 and Llama-2 can be fine-tuned to extract useful records of complex scientific knowledge.

A novel LLM augmented joint learning framework called Reamend has been proposed for entity-relation extraction that leverages LLMs to simultaneously recognize potential entities and corresponding relations from text content, with entity-relation amendment to eliminate redundant triplets.

## Document-Level Relation Extraction with Supporting Evidence

Recent work addresses "Consistency Guided Knowledge Retrieval and Denoising in LLMs for Zero-shot Document-level Relation Triplet Extraction," and AutoRE has been developed for "Document-Level Relation Extraction with Large Language Models."

## Supporting Evidence and Reasoning Approaches

RAG (Retrieval Augmented Generation) improves factuality through evidence grounding, and studies have integrated the extraction process with Chain-of-Thought prompting to encourage stepwise reasoning for entity and relation identification, demonstrating that explicit schemas can be effectively replaced by reasoning-driven organization.

The search results show active development in this area, with multiple 2025-2026 publications addressing document-level joint extraction using LLMs with attention to evidence grounding and supporting sentences.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "cb4958af-b43e-4f4c-8655-7d4db605bc81",
  "tool_use_result": {
    "query": "\"joint extraction\" \"evidence\" \"relation\" document-level LLM 2025 2026 supporting sentence",
    "results": [
      {
        "tool_use_id": "srvtoolu_019p6iJPjzqiMH9vHixmD3bk",
        "content": [
          {
            "title": "Structured information extraction from scientific text with large language models | Nature Communications",
            "url": "https://www.nature.com/articles/s41467-024-45563-x"
          },
          {
            "title": "Large language model augmented joint learning framework for entity-relation extraction - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/abs/pii/S1568494625014073"
          },
          {
            "title": "Benchmarking LLM-based Information Extraction Tools for ...",
            "url": "https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full.pdf"
          },
          {
            "title": "Few-Shot Relation Extraction via Two-Stage Knowledge- ...",
            "url": "https://www.ijcai.org/proceedings/2025/0897.pdf"
          },
          {
            "title": "GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub",
            "url": "https://github.com/quqxui/Awesome-LLM4IE-Papers"
          },
          {
            "title": "Survey on legal information extraction: current status and open challenges | Knowledge and Information Systems | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s10115-025-02600-5"
          },
          {
            "title": "Information Extraction from Visually Rich Documents using ...",
            "url": "https://aclanthology.org/2025.acl-long.844.pdf"
          },
          {
            "title": "Benchmarking LLM-based Information Extraction Tools for Medical Documents | medRxiv",
            "url": "https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full"
          },
          {
            "title": "LLM-empowered knowledge graph construction: A survey",
            "url": "https://arxiv.org/pdf/2510.20345"
          },
          {
            "title": "Exploring LLMs for Scientific Information Extraction using the SciEx Framework",
            "url": "https://arxiv.org/html/2512.10004v2"
          }
        ]
      },
      "I've completed a web search for your query about joint extraction, evidence, relations, document-level LLM work from 2025-2026. Here are the key findings:\n\n## Recent Research on Document-Level Joint Extraction with LLMs\n\nResearch has presented approaches to joint named entity recognition and relation extraction that demonstrate how pretrained large language models like GPT-3 and Llama-2 can be fine-tuned to extract useful records of complex scientific knowledge.\n\nA novel LLM augmented joint learning framework called Reamend has been proposed for entity-relation extraction that leverages LLMs to simultaneously recognize potential entities and corresponding relations from text content, with entity-relation amendment to eliminate redundant triplets.\n\n## Document-Level Relation Extraction with Supporting Evidence\n\nRecent work addresses \"Consistency Guided Knowledge Retrieval and Denoising in LLMs for Zero-shot Document-level Relation Triplet Extraction,\" and AutoRE has been developed for \"Document-Level Relation Extraction with Large Language Models.\"\n\n## Supporting Evidence and Reasoning Approaches\n\nRAG (Retrieval Augmented Generation) improves factuality through evidence grounding, and studies have integrated the extraction process with Chain-of-Thought prompting to encourage stepwise reasoning for entity and relation identification, demonstrating that explicit schemas can be effectively replaced by reasoning-driven organization.\n\nThe search results show active development in this area, with multiple 2025-2026 publications addressing document-level joint extraction using LLMs with attention to evidence grounding and supporting sentences."
    ],
    "durationSeconds": 7.324900955999998
  }
}
```

</details>

---

### Assistant

_source line 42_

<details><summary>Logged reasoning block</summary>

```text
Let me search for a few more targeted topics:
1. The R2GRPO paper for scientific IE - already got
2. The self-verification for DocRE paper (Springer link from earlier search)
3. "latent chain-of-thought" vs explicit reasoning tradeoff
4. NLI reranking for IE
5. Systematic review of RE since LLMs
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "29062c4d-748c-4f49-9a52-4ac95e3d4eb7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011RfNNDFCfRFBC3L6ySwQ5c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4109,
      "cache_read_input_tokens": 48224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4109
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

_source line 43_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NYKjuikXKYMof3iWEBuXcc`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.13602",
  "prompt": "Extract: title, authors, venue, year, key findings about reward hacking in GRPO/multi-objective settings. Focus on mechanisms relevant to structured prediction tasks."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "cfb45a22-9e65-465d-aff8-fe5a22912880",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011RfNNDFCfRFBC3L6ySwQ5c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4109,
      "cache_read_input_tokens": 48224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4109
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

_source line 44_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012jE6sx1HzCnWrQTjLmaSkm`</summary>

```json
{
  "query": "latent chain-of-thought internalized reasoning vs explicit reasoning performance 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "65ecafa8-4473-4bde-89e2-23ee03178c4c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011RfNNDFCfRFBC3L6ySwQ5c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4109,
      "cache_read_input_tokens": 48224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4109
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

_source line 45_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Dbr2Hsc8Am3KzayHkhBQJh`</summary>

```json
{
  "query": "NLI reranking verification information extraction faithful generation 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "b1e8d83c-550a-4672-a005-55d928335928",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011RfNNDFCfRFBC3L6ySwQ5c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4109,
      "cache_read_input_tokens": 48224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4109
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

_source line 46_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JJsDNUxfLGeWmJsr8xP8cV`</summary>

```json
{
  "query": "reinforcement learning NER information extraction reward design verifiable reward 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "f30b62ff-30d5-473b-ae51-de83fe101719",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011RfNNDFCfRFBC3L6ySwQ5c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4109,
      "cache_read_input_tokens": 48224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4109
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

_source line 47 · 2026-05-15T22:08:59.707Z_

<details><summary>↩ Tool result · `toolu_01NYKjuikXKYMof3iWEBuXcc`</summary>

```text
# Paper Summary

**Title:** Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges

**Authors:** Wang, Xiaohua et al. (23 co-authors)

**Venue:** arXiv (Computer Science > Machine Learning)

**Year:** 2026 (submitted April 15)

## Key Findings on Reward Hacking

The paper proposes the **Proxy Compression Hypothesis (PCH)** as a unifying framework. According to the authors, "reward hacking arises from the interaction of objective compression, optimization amplification, and evaluator–policy co-adaptation."

**Manifestations identified:**
- Verbosity bias and sycophancy in language models
- Hallucinated justifications and benchmark overfitting
- In multimodal settings: perception-reasoning decoupling and evaluator manipulation
- Potential escalation to deception and strategic gaming of oversight

**Core mechanism:** The paper characterizes reward hacking as occurring "when models exploit imperfections in learned reward signals to maximize proxy objectives without fulfilling true task intent."

**Relevance to structured prediction:** The framework emphasizes how "local shortcut learning can generalize into broader forms of misalignment," suggesting the compression dynamics may apply across domains where compressed reward representations fail to capture task complexity.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "e650613d-fea8-4fa2-bec8-d702bb798f8d",
  "tool_use_result": {
    "bytes": 52081,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Summary\n\n**Title:** Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges\n\n**Authors:** Wang, Xiaohua et al. (23 co-authors)\n\n**Venue:** arXiv (Computer Science > Machine Learning)\n\n**Year:** 2026 (submitted April 15)\n\n## Key Findings on Reward Hacking\n\nThe paper proposes the **Proxy Compression Hypothesis (PCH)** as a unifying framework. According to the authors, \"reward hacking arises from the interaction of objective compression, optimization amplification, and evaluator–policy co-adaptation.\"\n\n**Manifestations identified:**\n- Verbosity bias and sycophancy in language models\n- Hallucinated justifications and benchmark overfitting\n- In multimodal settings: perception-reasoning decoupling and evaluator manipulation\n- Potential escalation to deception and strategic gaming of oversight\n\n**Core mechanism:** The paper characterizes reward hacking as occurring \"when models exploit imperfections in learned reward signals to maximize proxy objectives without fulfilling true task intent.\"\n\n**Relevance to structured prediction:** The framework emphasizes how \"local shortcut learning can generalize into broader forms of misalignment,\" suggesting the compression dynamics may apply across domains where compressed reward representations fail to capture task complexity.",
    "durationMs": 4594,
    "url": "https://arxiv.org/abs/2604.13602"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-15T22:09:02.577Z_

<details><summary>↩ Tool result · `toolu_012jE6sx1HzCnWrQTjLmaSkm`</summary>

```text
Web search results for query: "latent chain-of-thought internalized reasoning vs explicit reasoning performance 2025 2026 arxiv"

Links: [{"title":"Reasoning Beyond Language: A Comprehensive Survey on Latent Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2505.16782v1"},{"title":"Thinking Without Words: Efficient Latent Reasoning with Abstract Chain-of-Thought","url":"https://arxiv.org/html/2604.22709v1"},{"title":"Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.01166"},{"title":"Implicit Reasoning in Large Language Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.02350v1"},{"title":"OneSearch-V2: The Latent Reasoning Enhanced Self-distillation Generative Search Framework","url":"https://arxiv.org/html/2603.24422v1"},{"title":"LLM Reasoning Is Latent, Not the Chain of Thought","url":"https://arxiv.org/html/2604.15726"},{"title":"A Formal Comparison Between Chain of Thought and Latent Thought","url":"https://arxiv.org/pdf/2509.25239"},{"title":"[2509.25239] A Formal Comparison Between Chain of Thought and Latent Thought","url":"https://arxiv.org/abs/2509.25239"},{"title":"A Survey on Latent Reasoning","url":"https://arxiv.org/html/2507.06203v1"},{"title":"Latent Chain-of-Thought Reasoning","url":"https://www.emergentmind.com/topics/latent-chain-of-thought-latent-cot-reasoning"}]

Here are the search results for latent chain-of-thought internalized reasoning vs explicit reasoning performance from recent 2025-2026 arXiv papers:

## Key Findings on Performance Comparison

**Reasoning Performance:**
While post-training methods consistently yield improvements in efficiency, reducing token usage and latency, their reasoning performance often matches, rather than exceeds, that of explicit CoT prompting on standard benchmarks.

However, there are nuances. Latent approaches achieve competitive or superior accuracy to explicit chain-of-thought with dramatically fewer steps due to internalized computation.

## Efficiency Advantages of Latent Reasoning

A key advantage of latent CoT is efficiency: by replacing token-level reasoning with dense latent computation, models execute reasoning faster and with substantially fewer steps. For example, System-1.5 Reasoning delivers >20× inference speedups by dynamically allocating computation only to critical reasoning steps.

## Theoretical Insights

Recent formal analysis provides important distinctions: Latent thought admits more efficient parallel computation than inherently sequential CoT. Additionally, CoT enables approximate counting and sampling through stochastic decoding.

## Methods and Approaches

COCONUT (Hao et al., 2024) made pioneering efforts to enable internal reasoning by feeding the model's last hidden states into its next input embedding, effectively allowing for latent iteration without producing explicit rationales. This recurrent reuse of internal states supports breadth-first exploration and improves efficiency.

These papers suggest that while latent reasoning matches or exceeds explicit reasoning in performance while being significantly more efficient, the computational and interpretability trade-offs depend heavily on the specific task and model design.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "923e3a2f-9e87-463a-85a7-744b9a81d750",
  "tool_use_result": {
    "query": "latent chain-of-thought internalized reasoning vs explicit reasoning performance 2025 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WwRvU2JcWV3zob4KsXmCx3",
        "content": [
          {
            "title": "Reasoning Beyond Language: A Comprehensive Survey on Latent Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/html/2505.16782v1"
          },
          {
            "title": "Thinking Without Words: Efficient Latent Reasoning with Abstract Chain-of-Thought",
            "url": "https://arxiv.org/html/2604.22709v1"
          },
          {
            "title": "Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2602.01166"
          },
          {
            "title": "Implicit Reasoning in Large Language Models: A Comprehensive Survey",
            "url": "https://arxiv.org/html/2509.02350v1"
          },
          {
            "title": "OneSearch-V2: The Latent Reasoning Enhanced Self-distillation Generative Search Framework",
            "url": "https://arxiv.org/html/2603.24422v1"
          },
          {
            "title": "LLM Reasoning Is Latent, Not the Chain of Thought",
            "url": "https://arxiv.org/html/2604.15726"
          },
          {
            "title": "A Formal Comparison Between Chain of Thought and Latent Thought",
            "url": "https://arxiv.org/pdf/2509.25239"
          },
          {
            "title": "[2509.25239] A Formal Comparison Between Chain of Thought and Latent Thought",
            "url": "https://arxiv.org/abs/2509.25239"
          },
          {
            "title": "A Survey on Latent Reasoning",
            "url": "https://arxiv.org/html/2507.06203v1"
          },
          {
            "title": "Latent Chain-of-Thought Reasoning",
            "url": "https://www.emergentmind.com/topics/latent-chain-of-thought-latent-cot-reasoning"
          }
        ]
      },
      "Here are the search results for latent chain-of-thought internalized reasoning vs explicit reasoning performance from recent 2025-2026 arXiv papers:\n\n## Key Findings on Performance Comparison\n\n**Reasoning Performance:**\nWhile post-training methods consistently yield improvements in efficiency, reducing token usage and latency, their reasoning performance often matches, rather than exceeds, that of explicit CoT prompting on standard benchmarks.\n\nHowever, there are nuances. Latent approaches achieve competitive or superior accuracy to explicit chain-of-thought with dramatically fewer steps due to internalized computation.\n\n## Efficiency Advantages of Latent Reasoning\n\nA key advantage of latent CoT is efficiency: by replacing token-level reasoning with dense latent computation, models execute reasoning faster and with substantially fewer steps. For example, System-1.5 Reasoning delivers >20× inference speedups by dynamically allocating computation only to critical reasoning steps.\n\n## Theoretical Insights\n\nRecent formal analysis provides important distinctions: Latent thought admits more efficient parallel computation than inherently sequential CoT. Additionally, CoT enables approximate counting and sampling through stochastic decoding.\n\n## Methods and Approaches\n\nCOCONUT (Hao et al., 2024) made pioneering efforts to enable internal reasoning by feeding the model's last hidden states into its next input embedding, effectively allowing for latent iteration without producing explicit rationales. This recurrent reuse of internal states supports breadth-first exploration and improves efficiency.\n\nThese papers suggest that while latent reasoning matches or exceeds explicit reasoning in performance while being significantly more efficient, the computational and interpretability trade-offs depend heavily on the specific task and model design."
    ],
    "durationSeconds": 6.984058212000003
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-15T22:09:04.697Z_

<details><summary>↩ Tool result · `toolu_01Dbr2Hsc8Am3KzayHkhBQJh`</summary>

```text
Web search results for query: "NLI reranking verification information extraction faithful generation 2024 2025"

Links: [{"title":"Natural Language Inference - Practical Guide 2025 | ShadeCoder","url":"https://www.shadecoder.com/topics/natural-language-inference-a-comprehensive-guide-for-2025"},{"title":"Evaluating Design Choices in Verifiable Generation with ...","url":"https://aclanthology.org/2025.trustnlp-main.27.pdf"},{"title":"DS@GT at CheckThat! 2025: Evaluating Context and Tokenization Strategies for Numerical Fact Verification","url":"https://arxiv.org/html/2507.06195"},{"title":"Proceedings of the Natural Legal Language Processing Workshop 2025, pages 17–30","url":"https://aclanthology.org/2025.nllp-1.3.pdf"},{"title":"Faithful and Robust LLM-Driven Theorem Proving for NLI ...","url":"https://aclanthology.org/2025.acl-long.867.pdf"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"},{"title":"Natural Language Inference (NLI)","url":"https://www.emergentmind.com/topics/natural-language-inference-nli"},{"title":"GitHub - liunian-Jay/Awesome-RAG: 💡 Awesome RAG: A resource of Retrieval-Augmented Generation (RAG) for LLMs, focusing on the development of technology.","url":"https://github.com/liunian-Jay/Awesome-RAG"},{"title":"Findings - EMNLP 2024","url":"https://2024.emnlp.org/program/accepted_findings/"},{"title":"Enhancing Financial Report Question-Answering: A Retrieval-Augmented Generation System with Reranking Analysis","url":"https://arxiv.org/html/2603.16877v1"}]

I've completed the web search for your query about NLI reranking, verification, information extraction, and faithful generation from 2024-2025. Here's a summary of the relevant findings:

## Key Research Areas

**Verifiable Generation & Citations (2025)**
Recent research suggests using direct generation pipelines fine-tuned with DPO on diverse content samples for effective verifiable generation with medium-size open-source LLMs, though reranking over-generated samples during inference can further increase output quality.

**NLI for Reranking and Verification (2025)**
NLI is used for post-processing to check generated answers, verify retrieved evidence, or rerank candidate passages, with NLI-style reranking prioritizing passages that entail a user query.

**Numerical Fact Verification with NLI (2025)**
Research employs a hybrid BM25 + transformer evidence retrieval-reranking pipeline plugged into a ModernBERT Natural Language Inference (NLI) core for fact verification tasks.

**Information Extraction & Reranking (2024)**
Studies show that large language models perform better as rerankers for hard samples in information extraction tasks rather than as few-shot information extractors.

**Faithful Explanation & Interpretability (2025)**
Systems generating faithful, testable explanations without sacrificing label accuracy represent progress toward interpretable NLP, though challenges like explanation redundancy and superficiality persist.

**Retrieval-Augmented Generation with Reranking (2024-2025)**
Reranking significantly improves RAG answer quality, achieving 49.0% correctness compared to 33.5% without reranking, and reducing error rates from 35.3% to 22.5%.

The search results show active research across multiple 2024-2025 publications addressing the intersection of NLI, reranking, faithful generation, and information extraction.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "02e24eec-2722-42df-9be9-fc04e2a6f533",
  "tool_use_result": {
    "query": "NLI reranking verification information extraction faithful generation 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EqTE4KcxwsdpDQAEuS1kUU",
        "content": [
          {
            "title": "Natural Language Inference - Practical Guide 2025 | ShadeCoder",
            "url": "https://www.shadecoder.com/topics/natural-language-inference-a-comprehensive-guide-for-2025"
          },
          {
            "title": "Evaluating Design Choices in Verifiable Generation with ...",
            "url": "https://aclanthology.org/2025.trustnlp-main.27.pdf"
          },
          {
            "title": "DS@GT at CheckThat! 2025: Evaluating Context and Tokenization Strategies for Numerical Fact Verification",
            "url": "https://arxiv.org/html/2507.06195"
          },
          {
            "title": "Proceedings of the Natural Legal Language Processing Workshop 2025, pages 17–30",
            "url": "https://aclanthology.org/2025.nllp-1.3.pdf"
          },
          {
            "title": "Faithful and Robust LLM-Driven Theorem Proving for NLI ...",
            "url": "https://aclanthology.org/2025.acl-long.867.pdf"
          },
          {
            "title": "Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s11704-024-40555-y"
          },
          {
            "title": "Natural Language Inference (NLI)",
            "url": "https://www.emergentmind.com/topics/natural-language-inference-nli"
          },
          {
            "title": "GitHub - liunian-Jay/Awesome-RAG: 💡 Awesome RAG: A resource of Retrieval-Augmented Generation (RAG) for LLMs, focusing on the development of technology.",
            "url": "https://github.com/liunian-Jay/Awesome-RAG"
          },
          {
            "title": "Findings - EMNLP 2024",
            "url": "https://2024.emnlp.org/program/accepted_findings/"
          },
          {
            "title": "Enhancing Financial Report Question-Answering: A Retrieval-Augmented Generation System with Reranking Analysis",
            "url": "https://arxiv.org/html/2603.16877v1"
          }
        ]
      },
      "I've completed the web search for your query about NLI reranking, verification, information extraction, and faithful generation from 2024-2025. Here's a summary of the relevant findings:\n\n## Key Research Areas\n\n**Verifiable Generation & Citations (2025)**\nRecent research suggests using direct generation pipelines fine-tuned with DPO on diverse content samples for effective verifiable generation with medium-size open-source LLMs, though reranking over-generated samples during inference can further increase output quality.\n\n**NLI for Reranking and Verification (2025)**\nNLI is used for post-processing to check generated answers, verify retrieved evidence, or rerank candidate passages, with NLI-style reranking prioritizing passages that entail a user query.\n\n**Numerical Fact Verification with NLI (2025)**\nResearch employs a hybrid BM25 + transformer evidence retrieval-reranking pipeline plugged into a ModernBERT Natural Language Inference (NLI) core for fact verification tasks.\n\n**Information Extraction & Reranking (2024)**\nStudies show that large language models perform better as rerankers for hard samples in information extraction tasks rather than as few-shot information extractors.\n\n**Faithful Explanation & Interpretability (2025)**\nSystems generating faithful, testable explanations without sacrificing label accuracy represent progress toward interpretable NLP, though challenges like explanation redundancy and superficiality persist.\n\n**Retrieval-Augmented Generation with Reranking (2024-2025)**\nReranking significantly improves RAG answer quality, achieving 49.0% correctness compared to 33.5% without reranking, and reducing error rates from 35.3% to 22.5%.\n\nThe search results show active research across multiple 2024-2025 publications addressing the intersection of NLI, reranking, faithful generation, and information extraction."
    ],
    "durationSeconds": 8.169400372999997
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-15T22:09:05.300Z_

<details><summary>↩ Tool result · `toolu_01JJsDNUxfLGeWmJsr8xP8cV`</summary>

```text
Web search results for query: "reinforcement learning NER information extraction reward design verifiable reward 2025 2026"

Links: [{"title":"[2506.14245] Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs","url":"https://arxiv.org/abs/2506.14245"},{"title":"Reinforcement Learning with Verifiable Rewards Implicitly ...","url":"https://arxiv.org/pdf/2506.14245"},{"title":"GitHub - opendilab/awesome-RLVR: A curated list of reinforcement learning with verifiable rewards (continually updated) · GitHub","url":"https://github.com/opendilab/awesome-RLVR"},{"title":"Reinforcement Learning with Verifiable Rewards Makes Models Faster, Not Smarter | Promptfoo","url":"https://www.promptfoo.dev/blog/rlvr-explained/"},{"title":"Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs | OpenReview","url":"https://openreview.net/forum?id=jGbRWwIidy"},{"title":"Minerva: Reinforcement Learning with Verifiable Rewards for Cyber Threat Intelligence LLMs","url":"https://arxiv.org/html/2602.00513v3"},{"title":"Knowledge-to-Verification: Unlocking Reinforcement Learning with Verifiable Rewards for LLMs in Knowledge-Intensive Domains | OpenReview","url":"https://openreview.net/forum?id=EVS7SeKBqI"},{"title":"[2510.00915] Reinforcement Learning with Verifiable yet Noisy Rewards under Imperfect Verifiers","url":"https://arxiv.org/abs/2510.00915"},{"title":"Verifiable Rewards in Reinforcement Learning","url":"https://www.emergentmind.com/topics/reinforcement-learning-with-verifiable-rewards-paradigm"},{"title":"Reinforcement Learning with Verified Rewards (RLVR)","url":"https://www.emergentmind.com/topics/reinforcement-learning-with-verified-rewards-rlvr"}]

I've completed a web search for your query on reinforcement learning with verifiable rewards (RLVR), NER, and information extraction. Here are the key findings from 2025-2026:

## Reinforcement Learning with Verifiable Rewards (RLVR)

RLVR is a post-training paradigm for LLMs that leverages a simple, automatically verifiable signal—such as correctness of answers or adherence to specified output formats—as direct supervision for policy optimization.

Recent advancements in long chain-of-thought (CoT) reasoning, particularly through the Group Relative Policy Optimization algorithm used by DeepSeek-R1, have led to significant interest in the potential of Reinforcement Learning with Verifiable Rewards (RLVR) for Large Language Models (LLMs).

## Reward Design and Effectiveness

There's ongoing debate about RLVR's true impact. While RLVR promises to improve reasoning by allowing models to learn from free exploration, there remains debate over whether it truly enhances reasoning abilities or simply boosts sampling efficiency. Recent research suggests most RLVR gains break down as: Majority: Search compression (pass@k → pass@1 efficiency) Minority: Capability expansion (pass@k ceiling lift).

## Addressing Imperfect Verifiers

RLVR replaces costly human labeling with automated verifiers. To reduce verifier hacking, many RLVR systems binarize rewards to {0,1}, but imperfect verifiers inevitably introduce false negatives (rejecting correct answers) and false positives (accepting incorrect ones).

## NER and Information Extraction Applications

Verifiable-reward formulations can transfer beyond math and code to other structured domains. RLVR is being brought to Cyber Threat Intelligence, where many targets are canonical identifiers, label sets, or structured strings, and addresses the sparse-reward regime through hardness-gated answer-conditioned rationale generation.

CTI applications include APTNER, an APT-focused named-entity recognition task, and other entity and relation extraction benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "0f7eb311-2d5c-4e02-8271-5b1b81b3d224",
  "tool_use_result": {
    "query": "reinforcement learning NER information extraction reward design verifiable reward 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JJ5V94PFUfKKvKP2haWhDS",
        "content": [
          {
            "title": "[2506.14245] Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs",
            "url": "https://arxiv.org/abs/2506.14245"
          },
          {
            "title": "Reinforcement Learning with Verifiable Rewards Implicitly ...",
            "url": "https://arxiv.org/pdf/2506.14245"
          },
          {
            "title": "GitHub - opendilab/awesome-RLVR: A curated list of reinforcement learning with verifiable rewards (continually updated) · GitHub",
            "url": "https://github.com/opendilab/awesome-RLVR"
          },
          {
            "title": "Reinforcement Learning with Verifiable Rewards Makes Models Faster, Not Smarter | Promptfoo",
            "url": "https://www.promptfoo.dev/blog/rlvr-explained/"
          },
          {
            "title": "Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs | OpenReview",
            "url": "https://openreview.net/forum?id=jGbRWwIidy"
          },
          {
            "title": "Minerva: Reinforcement Learning with Verifiable Rewards for Cyber Threat Intelligence LLMs",
            "url": "https://arxiv.org/html/2602.00513v3"
          },
          {
            "title": "Knowledge-to-Verification: Unlocking Reinforcement Learning with Verifiable Rewards for LLMs in Knowledge-Intensive Domains | OpenReview",
            "url": "https://openreview.net/forum?id=EVS7SeKBqI"
          },
          {
            "title": "[2510.00915] Reinforcement Learning with Verifiable yet Noisy Rewards under Imperfect Verifiers",
            "url": "https://arxiv.org/abs/2510.00915"
          },
          {
            "title": "Verifiable Rewards in Reinforcement Learning",
            "url": "https://www.emergentmind.com/topics/reinforcement-learning-with-verifiable-rewards-paradigm"
          },
          {
            "title": "Reinforcement Learning with Verified Rewards (RLVR)",
            "url": "https://www.emergentmind.com/topics/reinforcement-learning-with-verified-rewards-rlvr"
          }
        ]
      },
      "I've completed a web search for your query on reinforcement learning with verifiable rewards (RLVR), NER, and information extraction. Here are the key findings from 2025-2026:\n\n## Reinforcement Learning with Verifiable Rewards (RLVR)\n\nRLVR is a post-training paradigm for LLMs that leverages a simple, automatically verifiable signal—such as correctness of answers or adherence to specified output formats—as direct supervision for policy optimization.\n\nRecent advancements in long chain-of-thought (CoT) reasoning, particularly through the Group Relative Policy Optimization algorithm used by DeepSeek-R1, have led to significant interest in the potential of Reinforcement Learning with Verifiable Rewards (RLVR) for Large Language Models (LLMs).\n\n## Reward Design and Effectiveness\n\nThere's ongoing debate about RLVR's true impact. While RLVR promises to improve reasoning by allowing models to learn from free exploration, there remains debate over whether it truly enhances reasoning abilities or simply boosts sampling efficiency. Recent research suggests most RLVR gains break down as: Majority: Search compression (pass@k → pass@1 efficiency) Minority: Capability expansion (pass@k ceiling lift).\n\n## Addressing Imperfect Verifiers\n\nRLVR replaces costly human labeling with automated verifiers. To reduce verifier hacking, many RLVR systems binarize rewards to {0,1}, but imperfect verifiers inevitably introduce false negatives (rejecting correct answers) and false positives (accepting incorrect ones).\n\n## NER and Information Extraction Applications\n\nVerifiable-reward formulations can transfer beyond math and code to other structured domains. RLVR is being brought to Cyber Threat Intelligence, where many targets are canonical identifiers, label sets, or structured strings, and addresses the sparse-reward regime through hardness-gated answer-conditioned rationale generation.\n\nCTI applications include APTNER, an APT-focused named-entity recognition task, and other entity and relation extraction benchmarks."
    ],
    "durationSeconds": 8.427240900999998
  }
}
```

</details>

---

### Assistant

_source line 51_

<details><summary>Logged reasoning block</summary>

```text
Let me now search for a few more specific papers:
1. The systematic review of RE since LLMs (from arxiv 2511.03610)
2. The "CoT is not explainability" paper
3. The COCONUT latent reasoning paper
4. Any papers on "evidence extraction" + "relation extraction" + "trade-off"
5. The "Making Reasoning Matter" paper about faithfulness of CoT
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "fcb489e8-5e71-40b7-bf8d-17f5495d2286",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012kXR2p8PMASXSZBbxDbN3Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3620,
      "cache_read_input_tokens": 52333,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3620
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

_source line 52_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Xhtq6RodbCJegjA4RzYgXg`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.03610",
  "prompt": "Extract: title, authors, venue, year, key findings. This is a systematic review of relation extraction since LLMs. What does it say about document-level RE, evidence, and LLM-based approaches?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "9b025667-b3b6-4097-83e0-3a5a6d3b488d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012kXR2p8PMASXSZBbxDbN3Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3620,
      "cache_read_input_tokens": 52333,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3620
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

_source line 53_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01YU9zhQJhFT71qmSyyQGjwE`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.16782",
  "prompt": "Extract: title, authors, year, key findings about latent chain-of-thought vs explicit reasoning. Focus on performance trade-offs - does explicit reasoning (like CoT) sometimes hurt task performance?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "930d3025-8e99-4ffa-849e-c358a13f48ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012kXR2p8PMASXSZBbxDbN3Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3620,
      "cache_read_input_tokens": 52333,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3620
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

_source line 54_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TWevnUQCArjpQtxhUPsBNK`</summary>

```json
{
  "query": "\"evidence extraction\" \"relation extraction\" trade-off joint training performance cost document-level 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "07fb0ce6-82ce-40a8-9b92-06a249ad8ca7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012kXR2p8PMASXSZBbxDbN3Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3620,
      "cache_read_input_tokens": 52333,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3620
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

_source line 55_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01U17DCD5rYU5Daxx4x1Z7Nw`</summary>

```json
{
  "query": "GRPO structured output JSON generation reward hacking format reward 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "d95ec9ae-6de1-48f3-9513-1da3d6eac4b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012kXR2p8PMASXSZBbxDbN3Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3620,
      "cache_read_input_tokens": 52333,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3620
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

_source line 56 · 2026-05-15T22:09:18.004Z_

<details><summary>↩ Tool result · `toolu_01Xhtq6RodbCJegjA4RzYgXg`</summary>

```text
# Systematic Review: Relation Extraction and Transformers

**Title:** A systematic review of relation extraction task since the emergence of Transformers

**Authors:** Ringwald Celian, Gandon Fabien, Faron Catherine, Michel Franck, Abi Akl Hanna

**Venue:** ACM Computing Surveys (submitted)

**Year:** 2025

## Key Findings

The abstract indicates this review analyzed "34 surveys, 64 datasets, and 104 models published between 2019 and 2024," focusing on methodological advances in relation extraction using Transformer architectures.

## Limitations of Available Information

Unfortunately, the webpage content provided contains only the paper's metadata and abstract. The full text necessary to extract specific findings about document-level RE, evidence mechanisms, and LLM-based approaches is not included in the excerpt.

To obtain those specific insights, you would need to:
- Access the PDF directly via the arxiv link
- Consult the annotated Zotero bibliography referenced in the comments
- Review the SciLEx software documentation

The abstract suggests these topics are covered, but the detailed discussion is not available in this page excerpt.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "db9a7a91-5ee4-455e-88f6-784045aecbb2",
  "tool_use_result": {
    "bytes": 45468,
    "code": 200,
    "codeText": "OK",
    "result": "# Systematic Review: Relation Extraction and Transformers\n\n**Title:** A systematic review of relation extraction task since the emergence of Transformers\n\n**Authors:** Ringwald Celian, Gandon Fabien, Faron Catherine, Michel Franck, Abi Akl Hanna\n\n**Venue:** ACM Computing Surveys (submitted)\n\n**Year:** 2025\n\n## Key Findings\n\nThe abstract indicates this review analyzed \"34 surveys, 64 datasets, and 104 models published between 2019 and 2024,\" focusing on methodological advances in relation extraction using Transformer architectures.\n\n## Limitations of Available Information\n\nUnfortunately, the webpage content provided contains only the paper's metadata and abstract. The full text necessary to extract specific findings about document-level RE, evidence mechanisms, and LLM-based approaches is not included in the excerpt.\n\nTo obtain those specific insights, you would need to:\n- Access the PDF directly via the arxiv link\n- Consult the annotated Zotero bibliography referenced in the comments\n- Review the SciLEx software documentation\n\nThe abstract suggests these topics are covered, but the detailed discussion is not available in this page excerpt.",
    "durationMs": 4768,
    "url": "https://arxiv.org/abs/2511.03610"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-15T22:09:19.107Z_

<details><summary>↩ Tool result · `toolu_01YU9zhQJhFT71qmSyyQGjwE`</summary>

```text
# Paper Summary: Latent Chain-of-Thought Reasoning

**Title:** Reasoning Beyond Language: A Comprehensive Survey on Latent Chain-of-Thought Reasoning

**Authors:** Xinghao Chen, Anhao Zhao, Heming Xia, Xuan Lu, Hanlin Wang, Yanjun Chen, Wei Zhang, Jian Wang, Wenjie Li, Xiaoyu Shen

**Year:** 2025 (submitted May 22, 2025; revised November 1, 2025)

## Key Findings

The paper presents latent CoT as an emerging alternative to explicit reasoning. According to the abstract, "conventional CoT relies on explicitly verbalized intermediate steps, which constrains its broader applicability."

The research identifies significant advantages of latent reasoning: "by decoupling reasoning from explicit language generation, latent CoT offers the promise of richer cognitive representations and facilitates more flexible, faster inference."

## Performance Trade-offs

The abstract does not explicitly address whether explicit CoT reasoning sometimes hurts task performance. Instead, it frames latent CoT as addressing limitations in applicability and enabling "abstract reasoning tasks beyond language" rather than claiming performance degradation from explicit approaches. The focus is on expanding reasoning capabilities rather than demonstrating performance decrements from conventional CoT methods.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "c82b453b-d747-41c9-b49a-7b3a79b43e5e",
  "tool_use_result": {
    "bytes": 47363,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Summary: Latent Chain-of-Thought Reasoning\n\n**Title:** Reasoning Beyond Language: A Comprehensive Survey on Latent Chain-of-Thought Reasoning\n\n**Authors:** Xinghao Chen, Anhao Zhao, Heming Xia, Xuan Lu, Hanlin Wang, Yanjun Chen, Wei Zhang, Jian Wang, Wenjie Li, Xiaoyu Shen\n\n**Year:** 2025 (submitted May 22, 2025; revised November 1, 2025)\n\n## Key Findings\n\nThe paper presents latent CoT as an emerging alternative to explicit reasoning. According to the abstract, \"conventional CoT relies on explicitly verbalized intermediate steps, which constrains its broader applicability.\"\n\nThe research identifies significant advantages of latent reasoning: \"by decoupling reasoning from explicit language generation, latent CoT offers the promise of richer cognitive representations and facilitates more flexible, faster inference.\"\n\n## Performance Trade-offs\n\nThe abstract does not explicitly address whether explicit CoT reasoning sometimes hurts task performance. Instead, it frames latent CoT as addressing limitations in applicability and enabling \"abstract reasoning tasks beyond language\" rather than claiming performance degradation from explicit approaches. The focus is on expanding reasoning capabilities rather than demonstrating performance decrements from conventional CoT methods.",
    "durationMs": 4531,
    "url": "https://arxiv.org/abs/2505.16782"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-15T22:09:23.603Z_

<details><summary>↩ Tool result · `toolu_01TWevnUQCArjpQtxhUPsBNK`</summary>

```text
Web search results for query: ""evidence extraction" "relation extraction" trade-off joint training performance cost document-level 2024 2025"

Links: [{"title":"A survey on cutting-edge relation extraction techniques based on language models | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11280-0"},{"title":"Document-Level Relation Extraction with Global ...","url":"https://aclanthology.org/2025.findings-acl.1002.pdf"},{"title":"Document-Level Relation Extraction","url":"https://www.emergentmind.com/topics/document-level-relation-extraction"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/11e1900e680f5fe1893a8e27362dbe2c-Paper-Conference.pdf"},{"title":"Direct Retrieval-augmented Optimization:","url":"https://staff.fnwi.uva.nl/m.derijke/wp-content/papercite-data/pdf/shi-2025-direct-arxiv.pdf"},{"title":"Dynamic Chain-of-Thought for Low-Resource Event Extraction | Request PDF","url":"https://www.researchgate.net/publication/397888543_Dynamic_Chain-of-Thought_for_Low-Resource_Event_Extraction"},{"title":"A Survey of Generative Information Extraction","url":"https://aclanthology.org/2025.coling-main.324.pdf"},{"title":"Few-Shot Relation Extraction via Two-Stage Knowledge- ...","url":"https://www.ijcai.org/proceedings/2025/0897.pdf"},{"title":"[PDF] Improving Information Extraction by Acquiring External Evidence with Reinforcement Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Improving-Information-Extraction-by-Acquiring-with-Narasimhan-Yala/ac50801574f7c97f1cf8f6718a9ff2b3e18c2dc6"},{"title":"[PDF] Entity and Evidence Guided Document-Level Relation Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Entity-and-Evidence-Guided-Document-Level-Relation-Huang-Qi/e4179bf0963012f9f13ce0ca61d3cdd12a87b336"}]

I've performed the web search for your query about evidence extraction, relation extraction, trade-offs, joint training, performance, cost, and document-level approaches from 2024-2025. Here are the key findings:

## Key Research Findings:

### Joint Training and Evidence Extraction

Document-level RE's most discussed topics are evidence selection, joint and graph models, and new training strategies. E2GRE tackles the challenge of handling relations spanning multiple sentences by jointly extracting relations and their supporting evidence sentences using BERT as an input encoder.

### Performance Trade-offs

Inter-sentence (cross-sentence) F1 remains consistently 10–15 points below intra-sentence, highlighting the sustained challenge of long-distance reasoning. This demonstrates a significant performance gap that joint training approaches are attempting to address.

### Computational Efficiency Concerns

PLM and GNN integration remains costly for long documents; efficient document transformers and sparse graph induction are active research areas. This indicates ongoing challenges with the computational cost of joint models for document-level extraction.

### Recent Approaches (2024-2025)

The AutoRE system demonstrates that off-the-shelf LLMs fine-tuned via QLoRA adapters on modular RHF subtasks can achieve state-of-the-art results. The AutoRE system introduces an RHF (Relation–Head–Facts) paradigm, leveraging LLMs with parameter-efficient fine-tuning (QLoRA). The extraction is decomposed into three modular steps—relation detection, head entity identification, and tail entity/fact prediction—each realized as a distinct fine-tuned LLM module.

The research shows that while joint training of evidence and relation extraction yields performance benefits, there remains a trade-off with computational cost, particularly for long document processing.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "a6169a11-8f7c-4bf0-a5da-b275bdf2a976",
  "tool_use_result": {
    "query": "\"evidence extraction\" \"relation extraction\" trade-off joint training performance cost document-level 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WM8LZL2EytR3xKNFrzghPB",
        "content": [
          {
            "title": "A survey on cutting-edge relation extraction techniques based on language models | Artificial Intelligence Review | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s10462-025-11280-0"
          },
          {
            "title": "Document-Level Relation Extraction with Global ...",
            "url": "https://aclanthology.org/2025.findings-acl.1002.pdf"
          },
          {
            "title": "Document-Level Relation Extraction",
            "url": "https://www.emergentmind.com/topics/document-level-relation-extraction"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/11e1900e680f5fe1893a8e27362dbe2c-Paper-Conference.pdf"
          },
          {
            "title": "Direct Retrieval-augmented Optimization:",
            "url": "https://staff.fnwi.uva.nl/m.derijke/wp-content/papercite-data/pdf/shi-2025-direct-arxiv.pdf"
          },
          {
            "title": "Dynamic Chain-of-Thought for Low-Resource Event Extraction | Request PDF",
            "url": "https://www.researchgate.net/publication/397888543_Dynamic_Chain-of-Thought_for_Low-Resource_Event_Extraction"
          },
          {
            "title": "A Survey of Generative Information Extraction",
            "url": "https://aclanthology.org/2025.coling-main.324.pdf"
          },
          {
            "title": "Few-Shot Relation Extraction via Two-Stage Knowledge- ...",
            "url": "https://www.ijcai.org/proceedings/2025/0897.pdf"
          },
          {
            "title": "[PDF] Improving Information Extraction by Acquiring External Evidence with Reinforcement Learning | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Improving-Information-Extraction-by-Acquiring-with-Narasimhan-Yala/ac50801574f7c97f1cf8f6718a9ff2b3e18c2dc6"
          },
          {
            "title": "[PDF] Entity and Evidence Guided Document-Level Relation Extraction | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Entity-and-Evidence-Guided-Document-Level-Relation-Huang-Qi/e4179bf0963012f9f13ce0ca61d3cdd12a87b336"
          }
        ]
      },
      "I've performed the web search for your query about evidence extraction, relation extraction, trade-offs, joint training, performance, cost, and document-level approaches from 2024-2025. Here are the key findings:\n\n## Key Research Findings:\n\n### Joint Training and Evidence Extraction\n\nDocument-level RE's most discussed topics are evidence selection, joint and graph models, and new training strategies. E2GRE tackles the challenge of handling relations spanning multiple sentences by jointly extracting relations and their supporting evidence sentences using BERT as an input encoder.\n\n### Performance Trade-offs\n\nInter-sentence (cross-sentence) F1 remains consistently 10–15 points below intra-sentence, highlighting the sustained challenge of long-distance reasoning. This demonstrates a significant performance gap that joint training approaches are attempting to address.\n\n### Computational Efficiency Concerns\n\nPLM and GNN integration remains costly for long documents; efficient document transformers and sparse graph induction are active research areas. This indicates ongoing challenges with the computational cost of joint models for document-level extraction.\n\n### Recent Approaches (2024-2025)\n\nThe AutoRE system demonstrates that off-the-shelf LLMs fine-tuned via QLoRA adapters on modular RHF subtasks can achieve state-of-the-art results. The AutoRE system introduces an RHF (Relation–Head–Facts) paradigm, leveraging LLMs with parameter-efficient fine-tuning (QLoRA). The extraction is decomposed into three modular steps—relation detection, head entity identification, and tail entity/fact prediction—each realized as a distinct fine-tuned LLM module.\n\nThe research shows that while joint training of evidence and relation extraction yields performance benefits, there remains a trade-off with computational cost, particularly for long document processing."
    ],
    "durationSeconds": 8.133876442000007
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-15T22:09:25.123Z_

<details><summary>↩ Tool result · `toolu_01U17DCD5rYU5Daxx4x1Z7Nw`</summary>

```text
Web search results for query: "GRPO structured output JSON generation reward hacking format reward 2025 2026"

Links: [{"title":"Post-Training in 2026: GRPO, DAPO, RLVR & Beyond","url":"https://llm-stats.com/blog/research/post-training-techniques-2026"},{"title":"Overcoming reward signal challenges: Verifiable rewards-based reinforcement learning with GRPO on SageMaker AI | Artificial Intelligence","url":"https://aws.amazon.com/blogs/machine-learning/overcoming-reward-signal-challenges-verifiable-rewards-based-reinforcement-learning-with-grpo-on-sagemaker-ai/"},{"title":"GDPO Explained: How NVIDIA Fixes GRPO for Multi-Reward LLM Reinforcement Learning - AI Papers Academy","url":"https://aipapersacademy.com/gdpo/"},{"title":"Structured Outputs - GroqDocs","url":"https://console.groq.com/docs/structured-outputs"},{"title":"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems","url":"https://arxiv.org/html/2509.22047"},{"title":"GRPO IS SECRETLY A PROCESS REWARD MODEL Michael Sullivan","url":"https://arxiv.org/pdf/2509.21154"},{"title":"A brief example of reward hacking in GRPO","url":"https://ishanjmukherjee.github.io/reward-hacking-grpo"},{"title":"Use large language model to enhance reasoning of another large language model through reward updated GRPO | Scientific Reports","url":"https://www.nature.com/articles/s41598-026-39296-8"},{"title":"[2509.22047] MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems","url":"https://arxiv.org/abs/2509.22047"},{"title":"OpenAI Structured Outputs: Complete Developer Guide","url":"https://www.digitalapplied.com/blog/openai-structured-outputs-complete-guide"}]

Based on the search results, here's a comprehensive overview of GRPO, structured output JSON generation, reward hacking, and related developments in 2025-2026:

## GRPO Overview

GRPO samples multiple responses per prompt, scores them, then normalizes rewards within the group, and no critic model is needed. DeepSeek-R1 demonstrated the RL algorithm called GRPO, short for Group Relative Policy Optimization, which quickly became extremely popular.

## Structured Output and Format Rewards

SFT (Supervised Fine-Tuning) teaches the model the format: how to follow instructions, produce structured outputs, and respond in a conversational style. For JSON generation specifically, pattern matching searches for the specific format and awards points for proper formatting. 

While GRPO is primarily designed to work with a single reward signal, in practice large language models should have behaviors that align with diverse human preferences, such as answering in a specific format or following structured outputs, making it crucial to incorporate multiple rewards simultaneously, such as correctness, format compliance, safety constraints, and response length.

## Reward Hacking Issues

When reward functions are imprecise or incomplete, models can engage in "reward hacking," finding unintended ways to maximize scores without achieving the desired behavior. 

A practical example: In one instance, a model fell into stuffing its 256-token-per-completion limit with random numbers in a bid to make its completions shorter.

## Recent Solutions (2025-2026)

GRPO is vulnerable to reward hacking in multi-objective settings, optimizing only one objective at the cost of others. MO-GRPO addresses this with a normalization method to reweight the reward functions automatically according to the variances of their values.

RLVR (Reinforcement Learning with Verifiable Rewards) addresses reward hacking through rule-based feedback defined by the model tuner, using programmatic reward functions that automatically score outputs against specific criteria.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "c9f204c3-21b9-4435-b807-a39cf6b4607b",
  "tool_use_result": {
    "query": "GRPO structured output JSON generation reward hacking format reward 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GxehtZWYbydznnvo3NcUyy",
        "content": [
          {
            "title": "Post-Training in 2026: GRPO, DAPO, RLVR & Beyond",
            "url": "https://llm-stats.com/blog/research/post-training-techniques-2026"
          },
          {
            "title": "Overcoming reward signal challenges: Verifiable rewards-based reinforcement learning with GRPO on SageMaker AI | Artificial Intelligence",
            "url": "https://aws.amazon.com/blogs/machine-learning/overcoming-reward-signal-challenges-verifiable-rewards-based-reinforcement-learning-with-grpo-on-sagemaker-ai/"
          },
          {
            "title": "GDPO Explained: How NVIDIA Fixes GRPO for Multi-Reward LLM Reinforcement Learning - AI Papers Academy",
            "url": "https://aipapersacademy.com/gdpo/"
          },
          {
            "title": "Structured Outputs - GroqDocs",
            "url": "https://console.groq.com/docs/structured-outputs"
          },
          {
            "title": "MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems",
            "url": "https://arxiv.org/html/2509.22047"
          },
          {
            "title": "GRPO IS SECRETLY A PROCESS REWARD MODEL Michael Sullivan",
            "url": "https://arxiv.org/pdf/2509.21154"
          },
          {
            "title": "A brief example of reward hacking in GRPO",
            "url": "https://ishanjmukherjee.github.io/reward-hacking-grpo"
          },
          {
            "title": "Use large language model to enhance reasoning of another large language model through reward updated GRPO | Scientific Reports",
            "url": "https://www.nature.com/articles/s41598-026-39296-8"
          },
          {
            "title": "[2509.22047] MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems",
            "url": "https://arxiv.org/abs/2509.22047"
          },
          {
            "title": "OpenAI Structured Outputs: Complete Developer Guide",
            "url": "https://www.digitalapplied.com/blog/openai-structured-outputs-complete-guide"
          }
        ]
      },
      "Based on the search results, here's a comprehensive overview of GRPO, structured output JSON generation, reward hacking, and related developments in 2025-2026:\n\n## GRPO Overview\n\nGRPO samples multiple responses per prompt, scores them, then normalizes rewards within the group, and no critic model is needed. DeepSeek-R1 demonstrated the RL algorithm called GRPO, short for Group Relative Policy Optimization, which quickly became extremely popular.\n\n## Structured Output and Format Rewards\n\nSFT (Supervised Fine-Tuning) teaches the model the format: how to follow instructions, produce structured outputs, and respond in a conversational style. For JSON generation specifically, pattern matching searches for the specific format and awards points for proper formatting. \n\nWhile GRPO is primarily designed to work with a single reward signal, in practice large language models should have behaviors that align with diverse human preferences, such as answering in a specific format or following structured outputs, making it crucial to incorporate multiple rewards simultaneously, such as correctness, format compliance, safety constraints, and response length.\n\n## Reward Hacking Issues\n\nWhen reward functions are imprecise or incomplete, models can engage in \"reward hacking,\" finding unintended ways to maximize scores without achieving the desired behavior. \n\nA practical example: In one instance, a model fell into stuffing its 256-token-per-completion limit with random numbers in a bid to make its completions shorter.\n\n## Recent Solutions (2025-2026)\n\nGRPO is vulnerable to reward hacking in multi-objective settings, optimizing only one objective at the cost of others. MO-GRPO addresses this with a normalization method to reweight the reward functions automatically according to the variances of their values.\n\nRLVR (Reinforcement Learning with Verifiable Rewards) addresses reward hacking through rule-based feedback defined by the model tuner, using programmatic reward functions that automatically score outputs against specific criteria."
    ],
    "durationSeconds": 9.239222595
  }
}
```

</details>

---

### Assistant

_source line 60_

<details><summary>Logged reasoning block</summary>

```text
Let me do a few more targeted searches for specific papers that could be very relevant:

1. "GRPO is secretly a process reward model" paper - this seems highly relevant
2. Search for "evidence-grounded" or "evidence-based" DocRE papers
3. Search for multi-task learning in IE with auxiliary task negative transfer
4. Any recent papers specifically about QLoRA vs bf16 training for RL
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "e8e71a05-0c5b-4891-844c-7f12b232d014",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DqyBSsadipEJD8caNdTaKf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3216,
      "cache_read_input_tokens": 55953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3216
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

_source line 61_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019XnDrPLakeysgnR28uU3zP`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.21154",
  "prompt": "Extract: title, authors, venue, year, abstract, key findings. This paper claims GRPO is secretly a process reward model."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "067f22f7-0f2a-4683-b1d5-14601034c0f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DqyBSsadipEJD8caNdTaKf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3216,
      "cache_read_input_tokens": 55953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3216
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

_source line 62_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018XiCh4pLf5pQff1XjEuRvr`</summary>

```json
{
  "query": "\"evidence-grounded\" OR \"evidence-based\" relation extraction LLM faithful 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "7d622c37-a786-4a86-9d4a-cc3e98729628",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DqyBSsadipEJD8caNdTaKf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3216,
      "cache_read_input_tokens": 55953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3216
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

_source line 63_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EAwect7YnVpbQin5ARvAtu`</summary>

```json
{
  "query": "QLoRA versus full precision bf16 RL training difference instability low-rank adaptation reinforcement learning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "9c11acef-0d6a-485a-823e-3d17d3091ec8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DqyBSsadipEJD8caNdTaKf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3216,
      "cache_read_input_tokens": 55953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3216
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

_source line 64_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017TWqxGFjdFvr51qHyWqVaZ`</summary>

```json
{
  "query": "\"auxiliary task\" \"negative transfer\" information extraction NLP multi-task 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "92fd200e-590b-4ffb-a728-dbf7f81ba2ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DqyBSsadipEJD8caNdTaKf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3216,
      "cache_read_input_tokens": 55953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3216
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

_source line 65 · 2026-05-15T22:09:34.797Z_

<details><summary>↩ Tool result · `toolu_019XnDrPLakeysgnR28uU3zP`</summary>

```text
# Paper Extraction

**Title:** GRPO is Secretly a Process Reward Model

**Authors:** Michael Sullivan, Alexander Koller

**Venue:** Under review at ICML 2026

**Year:** 2025 (submitted September 25, 2025; latest revision February 20, 2026)

**Abstract:** The researchers demonstrate that "Group Relative Policy Optimization (GRPO) RL algorithm equipped with an ORM is in fact equivalent to a PRM-aware RL objective" under specific conditions. They identify a deficiency in GRPO when handling imbalanced process steps and propose λ-GRPO as a corrective measure.

**Key Findings:**

1. **Theoretical equivalence:** GRPO with outcome reward models functions as a hidden process reward model, bridging two seemingly distinct approaches in reinforcement learning.

2. **Performance improvement:** Language models trained with λ-GRPO "outperform LLMs tuned with standard GRPO on downstream reasoning tasks" while reaching peak performance faster.

3. **Practical efficiency:** The proposed modification delivers improvements "without employing an explicit PRM, and with a negligible impact on training time and cost."

The work reveals that practitioners can leverage GRPO's inherent process reward structure to enhance performance without additional computational overhead.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "6bbaf8bb-2df7-43d6-bb69-fa3774ac09ef",
  "tool_use_result": {
    "bytes": 46648,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Extraction\n\n**Title:** GRPO is Secretly a Process Reward Model\n\n**Authors:** Michael Sullivan, Alexander Koller\n\n**Venue:** Under review at ICML 2026\n\n**Year:** 2025 (submitted September 25, 2025; latest revision February 20, 2026)\n\n**Abstract:** The researchers demonstrate that \"Group Relative Policy Optimization (GRPO) RL algorithm equipped with an ORM is in fact equivalent to a PRM-aware RL objective\" under specific conditions. They identify a deficiency in GRPO when handling imbalanced process steps and propose λ-GRPO as a corrective measure.\n\n**Key Findings:**\n\n1. **Theoretical equivalence:** GRPO with outcome reward models functions as a hidden process reward model, bridging two seemingly distinct approaches in reinforcement learning.\n\n2. **Performance improvement:** Language models trained with λ-GRPO \"outperform LLMs tuned with standard GRPO on downstream reasoning tasks\" while reaching peak performance faster.\n\n3. **Practical efficiency:** The proposed modification delivers improvements \"without employing an explicit PRM, and with a negligible impact on training time and cost.\"\n\nThe work reveals that practitioners can leverage GRPO's inherent process reward structure to enhance performance without additional computational overhead.",
    "durationMs": 4286,
    "url": "https://arxiv.org/abs/2509.21154"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-15T22:09:40.090Z_

<details><summary>↩ Tool result · `toolu_01EAwect7YnVpbQin5ARvAtu`</summary>

```text
Web search results for query: "QLoRA versus full precision bf16 RL training difference instability low-rank adaptation reinforcement learning 2025"

Links: [{"title":"Defeating the Training-Inference Mismatch via FP16","url":"https://arxiv.org/html/2510.26788v1"},{"title":"BF16 vs FP16 for Reinforcement Learning: Where Are We?","url":"https://kaitchup.substack.com/p/bf16-vs-fp16-for-reinforcement-learning"},{"title":"Quantized Low-Rank Adaptation (QLoRA)","url":"https://www.emergentmind.com/topics/quantized-low-rank-adaptation-qlora"},{"title":"QeRL: Training 32B Models on Single H100 vs Three GPUs, Beating LoRA in Accuracy","url":"https://neurohive.io/en/state-of-the-art/qerl-2/"},{"title":"QeRL: NVFP4-Quantized Reinforcement Learning (RL) Brings 32B LLM Training to a Single H100—While Improving Exploration - MarkTechPost","url":"https://www.marktechpost.com/2025/10/15/qerl-nvfp4-quantized-reinforcement-learning-rl-brings-32b-llm-training-to-a-single-h100-while-improving-exploration/"},{"title":"LoRA vs QLoRA: Best AI Model Fine-Tuning Platforms & Tools 2026 | Index.dev","url":"https://www.index.dev/blog/top-ai-fine-tuning-tools-lora-vs-qlora-vs-full"},{"title":"Quantized Low-Rank Adaptation (QLoRA)","url":"https://apxml.com/courses/fine-tuning-adapting-large-language-models/chapter-4-parameter-efficient-fine-tuning/qlora-introduction"},{"title":"LoRA vs. QLoRA","url":"https://www.redhat.com/en/topics/ai/lora-vs-qlora"},{"title":"LoRA fine-tuning Hyperparameters Guide | Unsloth Documentation","url":"https://unsloth.ai/docs/get-started/fine-tuning-llms-guide/lora-hyperparameters-guide"},{"title":"LoRA vs. QLoRA: Efficient fine-tuning techniques for LLMs","url":"https://modal.com/blog/lora-qlora"}]

Based on the search results, here's what I found about QLoRA versus full precision bf16 RL training:

## Key Findings on Instability Differences

Simply switching from BF16 to FP16 stabilizes and prolongs RL training. BF16 often collapses between about 150 and 600 steps, while FP16 trains stably to near-perfect accuracy without corrective tricks.

## Training Performance Impact

Simply switching both training and inference precision from BF16 to FP16 provides a dramatic improvement, with FP16 training runs being significantly more stable, converging much faster, and achieving substantially higher final rewards and evaluation scores.

## QLoRA in RL Context

While the search results show QLoRA's general effectiveness, there's interesting recent work on quantization-enhanced RL. Quantization noise, traditionally considered a drawback, improves the model's ability to find more effective problem-solving strategies in the RL context, which explains why quantized models show not only comparable but superior accuracy compared to full-precision counterparts.

In TRL with QLoRA, you might load fp16 weights, cast embeddings to fp32, then cast back to bf16 for FA2 compatibility, introducing several rounds of rounding before training even begins, though this is mitigated if the trainer or quantization is properly configured.

The research suggests that precision choices significantly impact RL training stability, with FP16 showing marked improvements over BF16, while quantized approaches like QLoRA can potentially offer additional benefits in exploration for certain RL algorithms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "63c3f84e-373d-48d1-b043-ab1bd255d858",
  "tool_use_result": {
    "query": "QLoRA versus full precision bf16 RL training difference instability low-rank adaptation reinforcement learning 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QLw988QzSBoRZgSwX1xR9c",
        "content": [
          {
            "title": "Defeating the Training-Inference Mismatch via FP16",
            "url": "https://arxiv.org/html/2510.26788v1"
          },
          {
            "title": "BF16 vs FP16 for Reinforcement Learning: Where Are We?",
            "url": "https://kaitchup.substack.com/p/bf16-vs-fp16-for-reinforcement-learning"
          },
          {
            "title": "Quantized Low-Rank Adaptation (QLoRA)",
            "url": "https://www.emergentmind.com/topics/quantized-low-rank-adaptation-qlora"
          },
          {
            "title": "QeRL: Training 32B Models on Single H100 vs Three GPUs, Beating LoRA in Accuracy",
            "url": "https://neurohive.io/en/state-of-the-art/qerl-2/"
          },
          {
            "title": "QeRL: NVFP4-Quantized Reinforcement Learning (RL) Brings 32B LLM Training to a Single H100—While Improving Exploration - MarkTechPost",
            "url": "https://www.marktechpost.com/2025/10/15/qerl-nvfp4-quantized-reinforcement-learning-rl-brings-32b-llm-training-to-a-single-h100-while-improving-exploration/"
          },
          {
            "title": "LoRA vs QLoRA: Best AI Model Fine-Tuning Platforms & Tools 2026 | Index.dev",
            "url": "https://www.index.dev/blog/top-ai-fine-tuning-tools-lora-vs-qlora-vs-full"
          },
          {
            "title": "Quantized Low-Rank Adaptation (QLoRA)",
            "url": "https://apxml.com/courses/fine-tuning-adapting-large-language-models/chapter-4-parameter-efficient-fine-tuning/qlora-introduction"
          },
          {
            "title": "LoRA vs. QLoRA",
            "url": "https://www.redhat.com/en/topics/ai/lora-vs-qlora"
          },
          {
            "title": "LoRA fine-tuning Hyperparameters Guide | Unsloth Documentation",
            "url": "https://unsloth.ai/docs/get-started/fine-tuning-llms-guide/lora-hyperparameters-guide"
          },
          {
            "title": "LoRA vs. QLoRA: Efficient fine-tuning techniques for LLMs",
            "url": "https://modal.com/blog/lora-qlora"
          }
        ]
      },
      "Based on the search results, here's what I found about QLoRA versus full precision bf16 RL training:\n\n## Key Findings on Instability Differences\n\nSimply switching from BF16 to FP16 stabilizes and prolongs RL training. BF16 often collapses between about 150 and 600 steps, while FP16 trains stably to near-perfect accuracy without corrective tricks.\n\n## Training Performance Impact\n\nSimply switching both training and inference precision from BF16 to FP16 provides a dramatic improvement, with FP16 training runs being significantly more stable, converging much faster, and achieving substantially higher final rewards and evaluation scores.\n\n## QLoRA in RL Context\n\nWhile the search results show QLoRA's general effectiveness, there's interesting recent work on quantization-enhanced RL. Quantization noise, traditionally considered a drawback, improves the model's ability to find more effective problem-solving strategies in the RL context, which explains why quantized models show not only comparable but superior accuracy compared to full-precision counterparts.\n\nIn TRL with QLoRA, you might load fp16 weights, cast embeddings to fp32, then cast back to bf16 for FA2 compatibility, introducing several rounds of rounding before training even begins, though this is mitigated if the trainer or quantization is properly configured.\n\nThe research suggests that precision choices significantly impact RL training stability, with FP16 showing marked improvements over BF16, while quantized approaches like QLoRA can potentially offer additional benefits in exploration for certain RL algorithms."
    ],
    "durationSeconds": 7.694282747000004
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-15T22:09:40.390Z_

<details><summary>↩ Tool result · `toolu_018XiCh4pLf5pQff1XjEuRvr`</summary>

```text
Web search results for query: ""evidence-grounded" OR "evidence-based" relation extraction LLM faithful 2024 2025 2026"

Links: [{"title":"Grounded Knowledge Graph Extraction via LLMs: An Anchor-Constrained Framework with Provenance Tracking","url":"https://www.mdpi.com/2073-431X/15/3/178"},{"title":"InteGround: On the Evaluation of Verification and Retrieval Planning in Integrative Grounding","url":"https://www.researchgate.net/publication/395725130_InteGround_On_the_Evaluation_of_Verification_and_Retrieval_Planning_in_Integrative_Grounding"},{"title":"EvidenceRL: Reinforcing Evidence Consistency for Trustworthy Language Models","url":"https://arxiv.org/html/2603.19532"},{"title":"LLM-empowered knowledge graph construction: A survey","url":"https://arxiv.org/pdf/2510.20345"},{"title":"Benchmarking LLM-based Information Extraction Tools for ...","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full.pdf"},{"title":"Exploring LLMs for Scientific Information Extraction using the SciEx Framework","url":"https://arxiv.org/pdf/2512.10004"},{"title":"The construction and refined extraction techniques of knowledge graph based on large language models | Scientific Reports","url":"https://www.nature.com/articles/s41598-026-38066-w"},{"title":"Towards evidence-aware retrieval-augmented generation via self-corrective chain-of-thought - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0306457325003103"},{"title":"Improving LLM-based relation extraction from RNA- ...","url":"https://vldb.org/workshops/2024/proceedings/LLM+KG/LLM+KG-12.pdf"},{"title":"Aman's AI Journal • Primers • Factuality in LLMs","url":"https://aman.ai/primers/ai/factuality-in-LLMs/"}]

Based on the web search results, here are the key findings on evidence-grounded and evidence-based relation extraction with LLMs focusing on faithfulness in 2024-2026:

## Recent Research Highlights

**Evidence-Grounded Knowledge Graph Extraction (2026)**

The AEVS framework ensures complete traceability in LLM-based knowledge graph extraction, providing character-level provenance for every triplet element and enabling principled hallucination detection. LLMs frequently hallucinate—generating plausible triplets unsupported by the source text, with the root cause being the lack of provenance since existing methods produce triplets without explicit links to their textual origins, making faithfulness unverifiable. AEVS significantly outperforms both specialized trained models and existing LLM-based approaches, achieving up to a 0.412 absolute improvement in F1 score on benchmarks like WebNLG, REBEL, and Wiki-NRE.

**Faithful Evidence Use and Training (2026)**

EvidenceRL aligns task accuracy with faithful evidence use across domains using GRPO with rewards for correctness. A central failure mode is unconstrained generation where models produce answers correct in isolation but unsupported by supplied evidence, a phenomenon termed post-rationalization.

**Integrative Grounding (2025)**

Grounding LLMs in external knowledge sources is a promising method for faithful prediction, though many real-world information needs require synthesizing multiple pieces of evidence. While LLMs are robust to redundant evidence, they tend to rationalize using internal knowledge when information is incomplete, and undirected planning can degrade performance through noise introduction.

**Scientific Information Extraction (2026)**

Each extracted element is annotated with provenance metadata to ensure full traceability; SciEx performs self-verification over extracted results with missing or uncertain fields triggering targeted follow-up queries for iterative refinement.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "1e5e5a38-6479-4ad9-b0b1-6a0014823b9e",
  "tool_use_result": {
    "query": "\"evidence-grounded\" OR \"evidence-based\" relation extraction LLM faithful 2024 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UWWto4K2yE3MTmtRzZCH7N",
        "content": [
          {
            "title": "Grounded Knowledge Graph Extraction via LLMs: An Anchor-Constrained Framework with Provenance Tracking",
            "url": "https://www.mdpi.com/2073-431X/15/3/178"
          },
          {
            "title": "InteGround: On the Evaluation of Verification and Retrieval Planning in Integrative Grounding",
            "url": "https://www.researchgate.net/publication/395725130_InteGround_On_the_Evaluation_of_Verification_and_Retrieval_Planning_in_Integrative_Grounding"
          },
          {
            "title": "EvidenceRL: Reinforcing Evidence Consistency for Trustworthy Language Models",
            "url": "https://arxiv.org/html/2603.19532"
          },
          {
            "title": "LLM-empowered knowledge graph construction: A survey",
            "url": "https://arxiv.org/pdf/2510.20345"
          },
          {
            "title": "Benchmarking LLM-based Information Extraction Tools for ...",
            "url": "https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full.pdf"
          },
          {
            "title": "Exploring LLMs for Scientific Information Extraction using the SciEx Framework",
            "url": "https://arxiv.org/pdf/2512.10004"
          },
          {
            "title": "The construction and refined extraction techniques of knowledge graph based on large language models | Scientific Reports",
            "url": "https://www.nature.com/articles/s41598-026-38066-w"
          },
          {
            "title": "Towards evidence-aware retrieval-augmented generation via self-corrective chain-of-thought - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/abs/pii/S0306457325003103"
          },
          {
            "title": "Improving LLM-based relation extraction from RNA- ...",
            "url": "https://vldb.org/workshops/2024/proceedings/LLM+KG/LLM+KG-12.pdf"
          },
          {
            "title": "Aman's AI Journal • Primers • Factuality in LLMs",
            "url": "https://aman.ai/primers/ai/factuality-in-LLMs/"
          }
        ]
      },
      "Based on the web search results, here are the key findings on evidence-grounded and evidence-based relation extraction with LLMs focusing on faithfulness in 2024-2026:\n\n## Recent Research Highlights\n\n**Evidence-Grounded Knowledge Graph Extraction (2026)**\n\nThe AEVS framework ensures complete traceability in LLM-based knowledge graph extraction, providing character-level provenance for every triplet element and enabling principled hallucination detection. LLMs frequently hallucinate—generating plausible triplets unsupported by the source text, with the root cause being the lack of provenance since existing methods produce triplets without explicit links to their textual origins, making faithfulness unverifiable. AEVS significantly outperforms both specialized trained models and existing LLM-based approaches, achieving up to a 0.412 absolute improvement in F1 score on benchmarks like WebNLG, REBEL, and Wiki-NRE.\n\n**Faithful Evidence Use and Training (2026)**\n\nEvidenceRL aligns task accuracy with faithful evidence use across domains using GRPO with rewards for correctness. A central failure mode is unconstrained generation where models produce answers correct in isolation but unsupported by supplied evidence, a phenomenon termed post-rationalization.\n\n**Integrative Grounding (2025)**\n\nGrounding LLMs in external knowledge sources is a promising method for faithful prediction, though many real-world information needs require synthesizing multiple pieces of evidence. While LLMs are robust to redundant evidence, they tend to rationalize using internal knowledge when information is incomplete, and undirected planning can degrade performance through noise introduction.\n\n**Scientific Information Extraction (2026)**\n\nEach extracted element is annotated with provenance metadata to ensure full traceability; SciEx performs self-verification over extracted results with missing or uncertain fields triggering targeted follow-up queries for iterative refinement."
    ],
    "durationSeconds": 8.935052078000007
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-15T22:09:40.605Z_

<details><summary>↩ Tool result · `toolu_017TWqxGFjdFvr51qHyWqVaZ`</summary>

```text
Web search results for query: ""auxiliary task" "negative transfer" information extraction NLP multi-task 2024 2025"

Links: [{"title":"Identification of Negative Transfers in Multitask Learning Using ...","url":"https://openreview.net/notes/edits/attachment?id=h3G7ISb8FR&name=pdf"},{"title":"Multi-task Learning for Named Entity Recognition and Intent Classification in Natural Language Understanding Applications | Journal of Information Systems Engineering and Business Intelligence","url":"https://e-journal.unair.ac.id/JISEBI/article/view/56303"},{"title":"ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning","url":"https://ise.thss.tsinghua.edu.cn/~mlong/doc/ForkMerge-nips23.pdf"},{"title":"ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning | OpenReview","url":"https://openreview.net/forum?id=vZHk1QlBQW"},{"title":"Multi-Task Learning in Natural Language Processing: An Overview | ACM Computing Surveys","url":"https://dl.acm.org/doi/10.1145/3663363"},{"title":"Multi-Task Learning in Natural Language Processing: An Overview","url":"https://arxiv.org/html/2109.09138v2"},{"title":"[2301.12618] ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning","url":"https://arxiv.org/abs/2301.12618"},{"title":"Graceful Forgetting in Generative Language Models","url":"https://aclanthology.org/2025.emnlp-main.666.pdf"},{"title":"A Guide to Multi-Task Learning in Machine Learning | by Hey Amit | Data Scientist’s Diary | Medium","url":"https://medium.com/data-scientists-diary/a-guide-to-multi-task-learning-in-machine-learning-768d22b88715"},{"title":"An Overview of Multi-Task Learning in Deep Neural Networks","url":"https://www.ruder.io/multi-task/"}]

Based on the web search results, here's what I found regarding auxiliary tasks, negative transfer, information extraction, and NLP multi-task learning in recent research (2024-2025):

## Key Findings

**Negative Transfer in Auxiliary-Task Learning:**
Auxiliary-Task Learning (ATL) aims to improve the performance of the target task by leveraging the knowledge obtained from related tasks. However, occasionally learning multiple tasks simultaneously results in lower accuracy than learning only the target task, which is known as negative transfer. This problem is often attributed to the gradient conflicts among tasks, and is frequently tackled by coordinating the task gradients in previous works.

**Addressing Negative Transfer:**
ForkMerge is a novel approach that periodically forks the model into multiple branches, automatically searches the varying task weights by minimizing target validation errors, and dynamically merges all branches to filter out detrimental task-parameter updates.

**Multi-Task Learning Optimization:**
Task scheduling for MTL aims to alleviate overfitting and negative transfer caused by imbalanced dataset size. For auxiliary MTL, depending on the relationship between tasks, one can either start with the primary task before training primary and auxiliary tasks together or adopt a pre-train then fine-tune approach, which bootstraps the model with auxiliary tasks that are often easier or more data-rich.

**Information Extraction and NLP Applications:**
Recent work in 2025 demonstrates practical applications of multi-task learning in NLP. Multi-task learning is utilized for performing two prevalent dialogue language understanding tasks, namely intent prediction and entity prediction, building on the shared knowledge across the tasks by conducting joint training, resulting in enhanced performance in predicting both intent and entity.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "789795ce-fdcd-44fc-a06e-b3d236e1b18f",
  "tool_use_result": {
    "query": "\"auxiliary task\" \"negative transfer\" information extraction NLP multi-task 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NmwqknYChHQUS73EVv9Xua",
        "content": [
          {
            "title": "Identification of Negative Transfers in Multitask Learning Using ...",
            "url": "https://openreview.net/notes/edits/attachment?id=h3G7ISb8FR&name=pdf"
          },
          {
            "title": "Multi-task Learning for Named Entity Recognition and Intent Classification in Natural Language Understanding Applications | Journal of Information Systems Engineering and Business Intelligence",
            "url": "https://e-journal.unair.ac.id/JISEBI/article/view/56303"
          },
          {
            "title": "ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning",
            "url": "https://ise.thss.tsinghua.edu.cn/~mlong/doc/ForkMerge-nips23.pdf"
          },
          {
            "title": "ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning | OpenReview",
            "url": "https://openreview.net/forum?id=vZHk1QlBQW"
          },
          {
            "title": "Multi-Task Learning in Natural Language Processing: An Overview | ACM Computing Surveys",
            "url": "https://dl.acm.org/doi/10.1145/3663363"
          },
          {
            "title": "Multi-Task Learning in Natural Language Processing: An Overview",
            "url": "https://arxiv.org/html/2109.09138v2"
          },
          {
            "title": "[2301.12618] ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning",
            "url": "https://arxiv.org/abs/2301.12618"
          },
          {
            "title": "Graceful Forgetting in Generative Language Models",
            "url": "https://aclanthology.org/2025.emnlp-main.666.pdf"
          },
          {
            "title": "A Guide to Multi-Task Learning in Machine Learning | by Hey Amit | Data Scientist’s Diary | Medium",
            "url": "https://medium.com/data-scientists-diary/a-guide-to-multi-task-learning-in-machine-learning-768d22b88715"
          },
          {
            "title": "An Overview of Multi-Task Learning in Deep Neural Networks",
            "url": "https://www.ruder.io/multi-task/"
          }
        ]
      },
      "Based on the web search results, here's what I found regarding auxiliary tasks, negative transfer, information extraction, and NLP multi-task learning in recent research (2024-2025):\n\n## Key Findings\n\n**Negative Transfer in Auxiliary-Task Learning:**\nAuxiliary-Task Learning (ATL) aims to improve the performance of the target task by leveraging the knowledge obtained from related tasks. However, occasionally learning multiple tasks simultaneously results in lower accuracy than learning only the target task, which is known as negative transfer. This problem is often attributed to the gradient conflicts among tasks, and is frequently tackled by coordinating the task gradients in previous works.\n\n**Addressing Negative Transfer:**\nForkMerge is a novel approach that periodically forks the model into multiple branches, automatically searches the varying task weights by minimizing target validation errors, and dynamically merges all branches to filter out detrimental task-parameter updates.\n\n**Multi-Task Learning Optimization:**\nTask scheduling for MTL aims to alleviate overfitting and negative transfer caused by imbalanced dataset size. For auxiliary MTL, depending on the relationship between tasks, one can either start with the primary task before training primary and auxiliary tasks together or adopt a pre-train then fine-tune approach, which bootstraps the model with auxiliary tasks that are often easier or more data-rich.\n\n**Information Extraction and NLP Applications:**\nRecent work in 2025 demonstrates practical applications of multi-task learning in NLP. Multi-task learning is utilized for performing two prevalent dialogue language understanding tasks, namely intent prediction and entity prediction, building on the shared knowledge across the tasks by conducting joint training, resulting in enhanced performance in predicting both intent and entity."
    ],
    "durationSeconds": 7.8848697940000125
  }
}
```

</details>

---

### Assistant

_source line 69_

<details><summary>Logged reasoning block</summary>

```text
Found highly relevant papers. Now let me search for a few more:
1. EvidenceRL paper (arxiv 2603.19532) - this is EXTREMELY relevant - it uses GRPO with rewards for evidence faithfulness
2. The AEVS framework for knowledge graph extraction with provenance
3. QeRL paper for quantized RL
4. Any papers on "decoupling" in RL for language models
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "c9cddcd7-1f35-4833-b7ec-d18ef645222b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FK9AaAEztBEQvp3dg3kykU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3663,
      "cache_read_input_tokens": 59169,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3663
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

_source line 70_

发现了一篇极度相关的论文 EvidenceRL（用 GRPO + evidence faithfulness reward）。继续获取详细信息。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "ff317c82-2950-4e37-98ad-3dbf3d36a540",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FK9AaAEztBEQvp3dg3kykU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3663,
      "cache_read_input_tokens": 59169,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3663
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

_source line 71_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FoF6rGbdqzK4V3Ai492rBu`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.19532",
  "prompt": "Extract: title, authors, venue, year, abstract, key method, key findings, datasets used, results. This paper is about EvidenceRL - reinforcing evidence consistency for trustworthy language models. It's extremely relevant to our work on evidence-grounded information extraction with GRPO."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "85b45822-760c-4158-ae06-e20e8203523c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FK9AaAEztBEQvp3dg3kykU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3663,
      "cache_read_input_tokens": 59169,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3663
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

_source line 72_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XCXACMMkyHjFPmn2kb2ZL9`</summary>

```json
{
  "url": "https://www.mdpi.com/2073-431X/15/3/178",
  "prompt": "Extract: title, authors, venue, year, key method, key findings. This paper is about grounded knowledge graph extraction with provenance tracking."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "2bbc9bd2-7f0c-4789-8743-cb74153356ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FK9AaAEztBEQvp3dg3kykU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3663,
      "cache_read_input_tokens": 59169,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3663
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

_source line 73 · 2026-05-15T22:09:48.293Z_

<details><summary>↩ Tool result · reported error · `toolu_01XCXACMMkyHjFPmn2kb2ZL9`</summary>

```text
Request failed with status code 403
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "c0d06178-8a16-4a13-980b-0f31a5de1dc2",
  "tool_use_result": "Error: Request failed with status code 403"
}
```

</details>

---

### Tool call

_source line 74_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018XngYctpS3mvU4R5ZGYLrh`</summary>

```json
{
  "query": "EvidenceRL reinforcing evidence consistency GRPO trustworthy language model 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "ec0b3d88-f508-4745-b535-ff6a4e36cf6d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FK9AaAEztBEQvp3dg3kykU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3663,
      "cache_read_input_tokens": 59169,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3663
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

_source line 75_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017WkM1sjT19dpa9X37sGr8t`</summary>

```json
{
  "query": "\"reward decoupling\" OR \"task decoupling\" reinforcement learning language model multi-objective 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "7872c1ac-fdc2-4baa-bf25-d6c96f71f5c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FK9AaAEztBEQvp3dg3kykU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3663,
      "cache_read_input_tokens": 59169,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3663
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

_source line 76 · 2026-05-15T22:09:51.969Z_

<details><summary>↩ Tool result · `toolu_01FoF6rGbdqzK4V3Ai492rBu`</summary>

```text
# EvidenceRL Paper Summary

**Title:** EvidenceRL: Reinforcing Evidence Consistency for Trustworthy Language Models

**Authors:** J. Ben Tamo, Yuxing Lu, Benoit L. Marteau, Micky C. Nnamdi, May D. Wang

**Venue:** arXiv (Computer Science > Computation and Language)

**Year:** 2026 (submitted March 20, 2026)

**Abstract:** The paper addresses hallucinations in LLMs by introducing a framework that "scores candidate responses for grounding (entailment with retrieved evidence and context) and correctness (agreement with reference answers)."

**Key Method:** 
EvidenceRL employs reinforcement learning with Group Relative Policy Optimization (GRPO) to enforce evidence adherence during model training, combining grounding and correctness scoring mechanisms.

**Key Findings:**
- On cardiac diagnosis with Llama-3.2-3B: F1@3 improved from 37.0 to 54.5; grounding increased from 47.6 to 78.2; hallucinations decreased approximately 5-fold
- Evidence-supported diagnoses rose from 31.8% to 61.6%
- On legal reasoning with Llama-3.1-8B: Faithfulness increased from 32.8% to 67.6%

**Datasets:** Cardiac diagnosis and legal reasoning domains

**Code:** Open-sourced at GitHub (EvidenceRL repository)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "b99219f0-8970-4468-9d39-587b6f28328a",
  "tool_use_result": {
    "bytes": 46716,
    "code": 200,
    "codeText": "OK",
    "result": "# EvidenceRL Paper Summary\n\n**Title:** EvidenceRL: Reinforcing Evidence Consistency for Trustworthy Language Models\n\n**Authors:** J. Ben Tamo, Yuxing Lu, Benoit L. Marteau, Micky C. Nnamdi, May D. Wang\n\n**Venue:** arXiv (Computer Science > Computation and Language)\n\n**Year:** 2026 (submitted March 20, 2026)\n\n**Abstract:** The paper addresses hallucinations in LLMs by introducing a framework that \"scores candidate responses for grounding (entailment with retrieved evidence and context) and correctness (agreement with reference answers).\"\n\n**Key Method:** \nEvidenceRL employs reinforcement learning with Group Relative Policy Optimization (GRPO) to enforce evidence adherence during model training, combining grounding and correctness scoring mechanisms.\n\n**Key Findings:**\n- On cardiac diagnosis with Llama-3.2-3B: F1@3 improved from 37.0 to 54.5; grounding increased from 47.6 to 78.2; hallucinations decreased approximately 5-fold\n- Evidence-supported diagnoses rose from 31.8% to 61.6%\n- On legal reasoning with Llama-3.1-8B: Faithfulness increased from 32.8% to 67.6%\n\n**Datasets:** Cardiac diagnosis and legal reasoning domains\n\n**Code:** Open-sourced at GitHub (EvidenceRL repository)",
    "durationMs": 4819,
    "url": "https://arxiv.org/abs/2603.19532"
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-15T22:09:55.564Z_

<details><summary>↩ Tool result · `toolu_018XngYctpS3mvU4R5ZGYLrh`</summary>

```text
Web search results for query: "EvidenceRL reinforcing evidence consistency GRPO trustworthy language model 2026"

Links: [{"title":"[2603.19532] EvidenceRL: Reinforcing Evidence Consistency for Trustworthy Language Models","url":"https://arxiv.org/abs/2603.19532"},{"title":"EvidenceRL: Reinforcing Evidence Consistency for Trustworthy Language Models","url":"https://arxiv.org/html/2603.19532"},{"title":"GRPO-CARE: CONSISTENCY-AWARE REINFORCE-","url":"https://openreview.net/pdf/cfa98ab3c6c4ded69231292516f08fe959283565.pdf"},{"title":"SophiaVL-R1: Reinforcing MLLMs Reasoning with Thinking Reward","url":"https://arxiv.org/html/2505.17018"},{"title":"Information-Consistent Language Model Recommendations through Group Relative Policy Optimization","url":"https://arxiv.org/html/2512.12858"},{"title":"Toward large reasoning models: A survey of reinforced reasoning with large language models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12546433/"},{"title":"Group Relative Policy Optimization (GRPO)","url":"https://cameronrwolfe.substack.com/p/grpo"},{"title":"The State Of LLMs 2025: Progress, Progress, and Predictions","url":"https://magazine.sebastianraschka.com/p/state-of-llms-2025"},{"title":"DeepSeek-R1 incentivizes reasoning in LLMs through ...","url":"https://www.nature.com/articles/s41586-025-09422-z.pdf"},{"title":"GRPO++: Tricks for Making RL Actually Work","url":"https://cameronrwolfe.substack.com/p/grpo-tricks"}]

Based on the search results, here's information about EvidenceRL and related concepts:

## EvidenceRL: Reinforcing Evidence Consistency for Trustworthy Language Models

EvidenceRL is a reinforcement learning framework submitted on March 20, 2026, that addresses the problem of Large Language Models producing answers that appear plausible yet are unsupported by available evidence. The framework enforces evidence adherence during training.

### How It Works

EvidenceRL scores candidate responses for grounding (entailment with retrieved evidence and context) and correctness (agreement with reference answers) and optimizes the generator using Group Relative Policy Optimization (GRPO).

### Key Results

EvidenceRL was evaluated across two high-stakes domains, cardiac diagnosis and legal reasoning, where it consistently improved evidence grounding and faithfulness without sacrificing task accuracy. Notable improvements include:

- On cardiac diagnosis, F1@3 increases from 37.0 to 54.5 on Llama-3.2-3B while grounding rises from 47.6 to 78.2; hallucinations drop nearly 5× and evidence-supported diagnoses increase from 31.8% to 61.6%.
- On legal reasoning, EvidenceRL raises Faithfulness from 32.8% to 67.6% on Llama-3.1-8B.

### Motivation

This approach is especially important in high-stakes domains where decisions must be justified by verifiable information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "3121ca53-2d93-485a-8a17-ba4287a0b930",
  "tool_use_result": {
    "query": "EvidenceRL reinforcing evidence consistency GRPO trustworthy language model 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SQm33LHsoaASy2mAbTpgrc",
        "content": [
          {
            "title": "[2603.19532] EvidenceRL: Reinforcing Evidence Consistency for Trustworthy Language Models",
            "url": "https://arxiv.org/abs/2603.19532"
          },
          {
            "title": "EvidenceRL: Reinforcing Evidence Consistency for Trustworthy Language Models",
            "url": "https://arxiv.org/html/2603.19532"
          },
          {
            "title": "GRPO-CARE: CONSISTENCY-AWARE REINFORCE-",
            "url": "https://openreview.net/pdf/cfa98ab3c6c4ded69231292516f08fe959283565.pdf"
          },
          {
            "title": "SophiaVL-R1: Reinforcing MLLMs Reasoning with Thinking Reward",
            "url": "https://arxiv.org/html/2505.17018"
          },
          {
            "title": "Information-Consistent Language Model Recommendations through Group Relative Policy Optimization",
            "url": "https://arxiv.org/html/2512.12858"
          },
          {
            "title": "Toward large reasoning models: A survey of reinforced reasoning with large language models - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12546433/"
          },
          {
            "title": "Group Relative Policy Optimization (GRPO)",
            "url": "https://cameronrwolfe.substack.com/p/grpo"
          },
          {
            "title": "The State Of LLMs 2025: Progress, Progress, and Predictions",
            "url": "https://magazine.sebastianraschka.com/p/state-of-llms-2025"
          },
          {
            "title": "DeepSeek-R1 incentivizes reasoning in LLMs through ...",
            "url": "https://www.nature.com/articles/s41586-025-09422-z.pdf"
          },
          {
            "title": "GRPO++: Tricks for Making RL Actually Work",
            "url": "https://cameronrwolfe.substack.com/p/grpo-tricks"
          }
        ]
      },
      "Based on the search results, here's information about EvidenceRL and related concepts:\n\n## EvidenceRL: Reinforcing Evidence Consistency for Trustworthy Language Models\n\nEvidenceRL is a reinforcement learning framework submitted on March 20, 2026, that addresses the problem of Large Language Models producing answers that appear plausible yet are unsupported by available evidence. The framework enforces evidence adherence during training.\n\n### How It Works\n\nEvidenceRL scores candidate responses for grounding (entailment with retrieved evidence and context) and correctness (agreement with reference answers) and optimizes the generator using Group Relative Policy Optimization (GRPO).\n\n### Key Results\n\nEvidenceRL was evaluated across two high-stakes domains, cardiac diagnosis and legal reasoning, where it consistently improved evidence grounding and faithfulness without sacrificing task accuracy. Notable improvements include:\n\n- On cardiac diagnosis, F1@3 increases from 37.0 to 54.5 on Llama-3.2-3B while grounding rises from 47.6 to 78.2; hallucinations drop nearly 5× and evidence-supported diagnoses increase from 31.8% to 61.6%.\n- On legal reasoning, EvidenceRL raises Faithfulness from 32.8% to 67.6% on Llama-3.1-8B.\n\n### Motivation\n\nThis approach is especially important in high-stakes domains where decisions must be justified by verifiable information."
    ],
    "durationSeconds": 7.034904794999981
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-15T22:09:57.369Z_

<details><summary>↩ Tool result · `toolu_017WkM1sjT19dpa9X37sGr8t`</summary>

```text
Web search results for query: ""reward decoupling" OR "task decoupling" reinforcement learning language model multi-objective 2025 2026"

Links: [{"title":"Multi-Objective and Mixed-Reward Reinforcement Learning via Reward-Decorrelated Policy Optimization","url":"https://arxiv.org/html/2605.13641"},{"title":"Large Language Models for Structured Task Decomposition in Reinforcement Learning Problems with Sparse Rewards","url":"https://www.mdpi.com/2504-4990/7/4/126"},{"title":"Decoupling Task and Behavior: A Two-Stage Reward Curriculum in Reinforcement Learning for Robotics","url":"https://arxiv.org/html/2603.05113"},{"title":"Large Language Model Guided Incentive Aware Reward Design for Cooperative Multi-Agent Reinforcement Learning This work is currently under peer review.","url":"https://arxiv.org/html/2603.24324v3"},{"title":"[2603.05113] Decoupling Task and Behavior: A Two-Stage Reward Curriculum in Reinforcement Learning for Robotics","url":"https://arxiv.org/abs/2603.05113"},{"title":"Decoupling Task and Behavior: A Two-Stage Reward Curriculum in","url":"https://arxiv.org/pdf/2603.05113"},{"title":"GitHub - blacksnail789521/Agentic-RL-Training-Recipes: Training Recipes for Agentic Reinforcement Learning in LLMs: A Survey · GitHub","url":"https://github.com/blacksnail789521/Agentic-RL-Training-Recipes"},{"title":"Chain of Uncertain Rewards with Large Language Models for Reinforcement Learning","url":"https://arxiv.org/html/2604.13504"},{"title":"GitHub - tmgthb/Autonomous-Agents: Autonomous Agents (LLMs) research papers. Updated Daily. · GitHub","url":"https://github.com/tmgthb/Autonomous-Agents"},{"title":"TSR: Trajectory‑Search Rollouts for Multi‑Turn RL of LLM Agents","url":"https://arxiv.org/html/2602.11767v1"}]

I found several recent papers on reward and task decoupling in reinforcement learning with language models. Here's a summary of the key findings:

## Multi-Objective and Mixed-Reward RL for LLMs

Large language models in real-world deployments must simultaneously optimize for multiple objectives, such as computational efficiency, alignment with human preferences, and prompt-specific constraints. This has motivated recent advances in reinforcement learning for multi-task and mixed-reward settings, wherein a single rollout can yield diverse, heterogeneous reward signals.

## Task Decoupling Approaches

Several papers address task decoupling in different contexts:

1. **Reward-Decorrelated Policy Optimization**: One approach (GRPO) aggregates mixed-reward feedback by summing the raw rewards prior to group-level normalization, though this strategy can obscure the contributions of individual reward dimensions when their scales differ.

2. **Two-Stage Reward Curriculum**: A two-stage reward curriculum approach decouples task-specific objectives from behavioral terms, first training the agent on a simplified task-only reward function to ensure effective exploration before introducing the full reward that includes auxiliary behavior-related terms such as energy efficiency.

3. **LLM-Guided Task Decomposition**: Research shows that subgoals can be gradually decoupled, allowing the agent to benefit from them during training but ultimately operating at deployment without any reliance on explicit subgoals or LLM queries, reducing computational overhead and operational costs.

## Bayesian Decoupling Optimization

Recent work employs Bayesian optimization on decoupled reward terms to efficiently explore and refine reward feedback, decoupling reward terms for independent optimization to address local uncertainties.

These approaches represent the latest trends in handling the complexity of multi-objective optimization in LLM-based reinforcement learning systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "5b2c35f7-20db-438f-93bd-004cf02f059f",
  "tool_use_result": {
    "query": "\"reward decoupling\" OR \"task decoupling\" reinforcement learning language model multi-objective 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_0129QMuSzci3ZKrBBgaHFrna",
        "content": [
          {
            "title": "Multi-Objective and Mixed-Reward Reinforcement Learning via Reward-Decorrelated Policy Optimization",
            "url": "https://arxiv.org/html/2605.13641"
          },
          {
            "title": "Large Language Models for Structured Task Decomposition in Reinforcement Learning Problems with Sparse Rewards",
            "url": "https://www.mdpi.com/2504-4990/7/4/126"
          },
          {
            "title": "Decoupling Task and Behavior: A Two-Stage Reward Curriculum in Reinforcement Learning for Robotics",
            "url": "https://arxiv.org/html/2603.05113"
          },
          {
            "title": "Large Language Model Guided Incentive Aware Reward Design for Cooperative Multi-Agent Reinforcement Learning This work is currently under peer review.",
            "url": "https://arxiv.org/html/2603.24324v3"
          },
          {
            "title": "[2603.05113] Decoupling Task and Behavior: A Two-Stage Reward Curriculum in Reinforcement Learning for Robotics",
            "url": "https://arxiv.org/abs/2603.05113"
          },
          {
            "title": "Decoupling Task and Behavior: A Two-Stage Reward Curriculum in",
            "url": "https://arxiv.org/pdf/2603.05113"
          },
          {
            "title": "GitHub - blacksnail789521/Agentic-RL-Training-Recipes: Training Recipes for Agentic Reinforcement Learning in LLMs: A Survey · GitHub",
            "url": "https://github.com/blacksnail789521/Agentic-RL-Training-Recipes"
          },
          {
            "title": "Chain of Uncertain Rewards with Large Language Models for Reinforcement Learning",
            "url": "https://arxiv.org/html/2604.13504"
          },
          {
            "title": "GitHub - tmgthb/Autonomous-Agents: Autonomous Agents (LLMs) research papers. Updated Daily. · GitHub",
            "url": "https://github.com/tmgthb/Autonomous-Agents"
          },
          {
            "title": "TSR: Trajectory‑Search Rollouts for Multi‑Turn RL of LLM Agents",
            "url": "https://arxiv.org/html/2602.11767v1"
          }
        ]
      },
      "I found several recent papers on reward and task decoupling in reinforcement learning with language models. Here's a summary of the key findings:\n\n## Multi-Objective and Mixed-Reward RL for LLMs\n\nLarge language models in real-world deployments must simultaneously optimize for multiple objectives, such as computational efficiency, alignment with human preferences, and prompt-specific constraints. This has motivated recent advances in reinforcement learning for multi-task and mixed-reward settings, wherein a single rollout can yield diverse, heterogeneous reward signals.\n\n## Task Decoupling Approaches\n\nSeveral papers address task decoupling in different contexts:\n\n1. **Reward-Decorrelated Policy Optimization**: One approach (GRPO) aggregates mixed-reward feedback by summing the raw rewards prior to group-level normalization, though this strategy can obscure the contributions of individual reward dimensions when their scales differ.\n\n2. **Two-Stage Reward Curriculum**: A two-stage reward curriculum approach decouples task-specific objectives from behavioral terms, first training the agent on a simplified task-only reward function to ensure effective exploration before introducing the full reward that includes auxiliary behavior-related terms such as energy efficiency.\n\n3. **LLM-Guided Task Decomposition**: Research shows that subgoals can be gradually decoupled, allowing the agent to benefit from them during training but ultimately operating at deployment without any reliance on explicit subgoals or LLM queries, reducing computational overhead and operational costs.\n\n## Bayesian Decoupling Optimization\n\nRecent work employs Bayesian optimization on decoupled reward terms to efficiently explore and refine reward feedback, decoupling reward terms for independent optimization to address local uncertainties.\n\nThese approaches represent the latest trends in handling the complexity of multi-objective optimization in LLM-based reinforcement learning systems."
    ],
    "durationSeconds": 7.888735465999984
  }
}
```

</details>

---

### Assistant

_source line 79_

<details><summary>Logged reasoning block</summary>

```text
Let me now get a few more specific papers:
1. The Reward-Decorrelated Policy Optimization paper (arxiv 2605.13641) - seems very relevant
2. GRPO-CARE paper about consistency-aware reinforcement
3. The "Decoupling Task and Behavior" paper
4. Search for any papers on document-level RE with evidence that we missed

Let me also search for a few more targeted papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "e04bbb4a-c568-4c9c-a266-1fbe65e65545",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DMhhE9VE78YJp8VFJseEDw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2741,
      "cache_read_input_tokens": 62832,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2741
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

_source line 80_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WYGLWn1iyTby3dsZHELDMz`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.13641",
  "prompt": "Extract: title, authors, venue, year, abstract, key method, key findings. This paper is about Multi-Objective and Mixed-Reward RL via Reward-Decorrelated Policy Optimization."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "d3b59192-9cff-4a22-bffc-f94da2f5286f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DMhhE9VE78YJp8VFJseEDw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2741,
      "cache_read_input_tokens": 62832,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2741
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

_source line 81_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01T4ZoHoHCMyT2JdZ6p4xhod`</summary>

```json
{
  "query": "document-level relation extraction evidence sentence EIDER SIEF E2GRE DocRED 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "2e9dcc23-bddd-4328-9d41-b2607bb2a094",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DMhhE9VE78YJp8VFJseEDw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2741,
      "cache_read_input_tokens": 62832,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2741
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

_source line 82_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E31HFvgu2Je1zckj331J4V`</summary>

```json
{
  "query": "\"chain-of-thought hurts\" OR \"CoT decreases performance\" OR \"reasoning reduces accuracy\" structured tasks 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "01a964be-8f0e-41df-a0eb-ac7648e43c3e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DMhhE9VE78YJp8VFJseEDw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2741,
      "cache_read_input_tokens": 62832,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2741
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

_source line 83 · 2026-05-15T22:10:06.347Z_

<details><summary>↩ Tool result · `toolu_01WYGLWn1iyTby3dsZHELDMz`</summary>

```text
# Paper Summary

**Title:** Multi-Objective and Mixed-Reward Reinforcement Learning via Reward-Decorrelated Policy Optimization

**Authors:** Yang Bai, Kaiyuan Liu, Ziyuan Zhuang, Jiahong Zhou, Rongxiang Weng, Xin Chen, Jingang Wang, Xunliang Cai

**Venue:** arXiv (Computer Science > Machine Learning)

**Year:** 2026 (submitted May 13, 2026)

**Abstract:** The paper addresses instability in multi-task RL environments by proposing "a reward-processing method designed to explicitly target both failure modes" caused by heterogeneous reward distributions and correlated reward dimensions.

**Key Method:** Reward-Decorrelated Policy Optimization (RDPO) combines two techniques:
1. Magnitude-Aware Quantile normalization for stabilizing advantage allocation across diverse reward types
2. Mahalanobis whitening to reduce correlation redundancy within reward subspaces before aggregation

**Key Findings:** When applied to LongCat-Flash post-training, RDPO improved instruction following, writing quality, and robustness to challenging prompts while maintaining competitive performance on reasoning and coding tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "992b04cb-7a3a-44dd-848a-72bbbe60d26d",
  "tool_use_result": {
    "bytes": 46881,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Summary\n\n**Title:** Multi-Objective and Mixed-Reward Reinforcement Learning via Reward-Decorrelated Policy Optimization\n\n**Authors:** Yang Bai, Kaiyuan Liu, Ziyuan Zhuang, Jiahong Zhou, Rongxiang Weng, Xin Chen, Jingang Wang, Xunliang Cai\n\n**Venue:** arXiv (Computer Science > Machine Learning)\n\n**Year:** 2026 (submitted May 13, 2026)\n\n**Abstract:** The paper addresses instability in multi-task RL environments by proposing \"a reward-processing method designed to explicitly target both failure modes\" caused by heterogeneous reward distributions and correlated reward dimensions.\n\n**Key Method:** Reward-Decorrelated Policy Optimization (RDPO) combines two techniques:\n1. Magnitude-Aware Quantile normalization for stabilizing advantage allocation across diverse reward types\n2. Mahalanobis whitening to reduce correlation redundancy within reward subspaces before aggregation\n\n**Key Findings:** When applied to LongCat-Flash post-training, RDPO improved instruction following, writing quality, and robustness to challenging prompts while maintaining competitive performance on reasoning and coding tasks.",
    "durationMs": 4042,
    "url": "https://arxiv.org/abs/2605.13641"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-15T22:10:10.765Z_

<details><summary>↩ Tool result · `toolu_01T4ZoHoHCMyT2JdZ6p4xhod`</summary>

```text
Web search results for query: "document-level relation extraction evidence sentence EIDER SIEF E2GRE DocRED 2024 2025 2026"

Links: [{"title":"[PDF] Entity and Evidence Guided Document-Level Relation Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Entity-and-Evidence-Guided-Document-Level-Relation-Huang-Qi/e4179bf0963012f9f13ce0ca61d3cdd12a87b336"},{"title":"Document-Level Relation Extraction","url":"https://www.emergentmind.com/topics/document-level-relation-extraction"},{"title":"[2106.08657] Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion","url":"https://arxiv.org/abs/2106.08657"},{"title":"[PDF] Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Eider:-Empowering-Document-level-Relation-with-and-Xie-Shen/dbf1e5a17b3adead7016eb52ddc3007673ed382f"},{"title":"Entity and Evidence Guided Relation Extraction for DocRED | Request PDF","url":"https://www.researchgate.net/publication/343931511_Entity_and_Evidence_Guided_Relation_Extraction_for_DocRED"},{"title":"Document-Level Relation Extraction with Sentences Importance Estimation and Focusing - ACL Anthology","url":"https://aclanthology.org/2022.naacl-main.212/"},{"title":"[2008.12283] Entity and Evidence Guided Relation Extraction for DocRED","url":"https://arxiv.org/abs/2008.12283"},{"title":"Entity and Evidence Guided Relation Extraction for DocRED - ADS","url":"https://ui.adsabs.harvard.edu/abs/2020arXiv200812283H/abstract"},{"title":"[2008.12283v1] Entity and Evidence Guided Relation Extraction for DocRED","url":"https://arxiv.org/abs/2008.12283v1"},{"title":"Entity and Evidence Guided Relation Extraction for DocRED - Paper Detail","url":"https://deeplearn.org/arxiv/153393/entity-and-evidence-guided-relation-extraction-for-docred"}]

Based on the web search results, here's information about the key research areas and methods you're asking about:

## Document-Level Relation Extraction (DocRE)

Document-level relation extraction aims to determine the relation between two entities from a document of multiple sentences.

## Key Methods and Frameworks

**E2GRE (Entity and Evidence Guided Relation Extraction)**

E2GRE is a joint training framework for document-level relation extraction. Entity-guided sequences help pre-trained language models focus on areas of the document related to the entity, and the framework uses internal attention probabilities as additional features for evidence prediction.

**Eider (Evidence-Enhanced Framework)**

Eider empowers DocRE by efficiently extracting evidence and effectively fusing the extracted evidence in inference, jointly training a relation extraction model with a lightweight evidence extraction model, and making predictions on both extracted evidence and the full document, then fusing them through a blending layer.

**SIEF (Sentence Importance Estimation and Focusing)**

SIEF is a framework for DocRE that designs a sentence importance score and a sentence focusing loss, encouraging DocRE models to focus on evidence sentences.

## DocRED Dataset

DocRE research continues to push boundaries from static graph GNNs and contextual pretrained language models to modular, fine-tunable LLMs, while targeting demands in scalability, stability, and reasoning depth.

The search results primarily cover work through 2022, so recent 2024-2026 developments may not be fully captured in these results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "5c212c77-80c7-4623-9978-630fa0cb06ad",
  "tool_use_result": {
    "query": "document-level relation extraction evidence sentence EIDER SIEF E2GRE DocRED 2024 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_012FDBgxUvM4Yw8Puhpu4wYL",
        "content": [
          {
            "title": "[PDF] Entity and Evidence Guided Document-Level Relation Extraction | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Entity-and-Evidence-Guided-Document-Level-Relation-Huang-Qi/e4179bf0963012f9f13ce0ca61d3cdd12a87b336"
          },
          {
            "title": "Document-Level Relation Extraction",
            "url": "https://www.emergentmind.com/topics/document-level-relation-extraction"
          },
          {
            "title": "[2106.08657] Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion",
            "url": "https://arxiv.org/abs/2106.08657"
          },
          {
            "title": "[PDF] Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Eider:-Empowering-Document-level-Relation-with-and-Xie-Shen/dbf1e5a17b3adead7016eb52ddc3007673ed382f"
          },
          {
            "title": "Entity and Evidence Guided Relation Extraction for DocRED | Request PDF",
            "url": "https://www.researchgate.net/publication/343931511_Entity_and_Evidence_Guided_Relation_Extraction_for_DocRED"
          },
          {
            "title": "Document-Level Relation Extraction with Sentences Importance Estimation and Focusing - ACL Anthology",
            "url": "https://aclanthology.org/2022.naacl-main.212/"
          },
          {
            "title": "[2008.12283] Entity and Evidence Guided Relation Extraction for DocRED",
            "url": "https://arxiv.org/abs/2008.12283"
          },
          {
            "title": "Entity and Evidence Guided Relation Extraction for DocRED - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2020arXiv200812283H/abstract"
          },
          {
            "title": "[2008.12283v1] Entity and Evidence Guided Relation Extraction for DocRED",
            "url": "https://arxiv.org/abs/2008.12283v1"
          },
          {
            "title": "Entity and Evidence Guided Relation Extraction for DocRED - Paper Detail",
            "url": "https://deeplearn.org/arxiv/153393/entity-and-evidence-guided-relation-extraction-for-docred"
          }
        ]
      },
      "Based on the web search results, here's information about the key research areas and methods you're asking about:\n\n## Document-Level Relation Extraction (DocRE)\n\nDocument-level relation extraction aims to determine the relation between two entities from a document of multiple sentences.\n\n## Key Methods and Frameworks\n\n**E2GRE (Entity and Evidence Guided Relation Extraction)**\n\nE2GRE is a joint training framework for document-level relation extraction. Entity-guided sequences help pre-trained language models focus on areas of the document related to the entity, and the framework uses internal attention probabilities as additional features for evidence prediction.\n\n**Eider (Evidence-Enhanced Framework)**\n\nEider empowers DocRE by efficiently extracting evidence and effectively fusing the extracted evidence in inference, jointly training a relation extraction model with a lightweight evidence extraction model, and making predictions on both extracted evidence and the full document, then fusing them through a blending layer.\n\n**SIEF (Sentence Importance Estimation and Focusing)**\n\nSIEF is a framework for DocRE that designs a sentence importance score and a sentence focusing loss, encouraging DocRE models to focus on evidence sentences.\n\n## DocRED Dataset\n\nDocRE research continues to push boundaries from static graph GNNs and contextual pretrained language models to modular, fine-tunable LLMs, while targeting demands in scalability, stability, and reasoning depth.\n\nThe search results primarily cover work through 2022, so recent 2024-2026 developments may not be fully captured in these results."
    ],
    "durationSeconds": 7.00294743
  }
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-15T22:10:11.147Z_

<details><summary>↩ Tool result · `toolu_01E31HFvgu2Je1zckj331J4V`</summary>

```text
Web search results for query: ""chain-of-thought hurts" OR "CoT decreases performance" OR "reasoning reduces accuracy" structured tasks 2024 2025"

Links: [{"title":"Chain-of-thought can hurt performance on tasks where thinking makes humans worse | Hacker News","url":"https://news.ycombinator.com/item?id=41999340"},{"title":"Chain of Thought in Large Language Models: Elicited Reasoning or Constrained Imitation? | by Greg Robison | Medium","url":"https://gregrobison.medium.com/chain-of-thought-in-large-language-models-elicited-reasoning-or-constrained-imitation-5e4ee0c811ad"},{"title":"Data Mining and Machine Learning Lab Is Chain-of-Thought Reasoning of LLMs a","url":"https://arxiv.org/pdf/2508.01191"},{"title":"A Survey of Chain-of-X Paradigms for LLMs","url":"https://aclanthology.org/2025.coling-main.719.pdf"},{"title":"Improving Chain-of-Thought Reasoning via Quasi- ...","url":"https://aclanthology.org/2025.acl-long.843.pdf"},{"title":"Demystifying Long Chain-of-Thought Reasoning","url":"https://openreview.net/pdf?id=OLodUbcWjB"},{"title":"FOCUSED CHAIN-OF-THOUGHT: EFFICIENT LLM REA-","url":"https://arxiv.org/pdf/2511.22176"},{"title":"Technical Report: The Decreasing Value of Chain of Thought in Prompting - Wharton Generative AI Labs","url":"https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought/"},{"title":"What Makes a Good Reasoning Chain? Uncovering ...","url":"https://aclanthology.org/2025.emnlp-main.329.pdf"},{"title":"Comprehensive Survey on Prompts Generating via Knowledge-Guided Chain-of-Thought","url":"https://www.sciopen.com/article/10.26599/IJCS.2024.9100038"}]

Based on the search results, I found several relevant findings about chain-of-thought reasoning and its performance challenges:

## Key Findings

**Performance Issues in Specific Contexts:**

CoT reasoning is highly fragile: semantically irrelevant perturbations, such as distractor phrases or altered symbolic representations, can substantially degrade performance. Additionally, what appears to be structured reasoning can be a mirage, emerging from memorized or interpolated patterns in the training data rather than logical inference.

**When CoT Fails:**

CoT performance becomes fragile and prone to failure even under moderate distribution shifts to out-of-distribution data. This suggests that while CoT reasoning appears effective on in-distribution tasks, it may actually hurt performance when tasks deviate from training patterns.

**Research on Decreasing Value:**

A technical report from Wharton's Generative AI Labs titled "The Decreasing Value of Chain of Thought in Prompting" was published in June 2025, though specific details about its findings aren't fully available in the search results.

**Smaller Models:**

There are references to research showing that "CoT Harms Performance of Rather Smaller Language Models", suggesting size-dependent effects where chain-of-thought prompting may not benefit or may even harm smaller models.

The research indicates that while chain-of-thought can be beneficial for complex reasoning tasks, it doesn't universally improve performance across all task types, models, and data distributions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "a9242f05-cbe9-41ca-b1c2-7ced26f5ec11",
  "tool_use_result": {
    "query": "\"chain-of-thought hurts\" OR \"CoT decreases performance\" OR \"reasoning reduces accuracy\" structured tasks 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_018AZUwefaQ8LDRuVPaB1CZP",
        "content": [
          {
            "title": "Chain-of-thought can hurt performance on tasks where thinking makes humans worse | Hacker News",
            "url": "https://news.ycombinator.com/item?id=41999340"
          },
          {
            "title": "Chain of Thought in Large Language Models: Elicited Reasoning or Constrained Imitation? | by Greg Robison | Medium",
            "url": "https://gregrobison.medium.com/chain-of-thought-in-large-language-models-elicited-reasoning-or-constrained-imitation-5e4ee0c811ad"
          },
          {
            "title": "Data Mining and Machine Learning Lab Is Chain-of-Thought Reasoning of LLMs a",
            "url": "https://arxiv.org/pdf/2508.01191"
          },
          {
            "title": "A Survey of Chain-of-X Paradigms for LLMs",
            "url": "https://aclanthology.org/2025.coling-main.719.pdf"
          },
          {
            "title": "Improving Chain-of-Thought Reasoning via Quasi- ...",
            "url": "https://aclanthology.org/2025.acl-long.843.pdf"
          },
          {
            "title": "Demystifying Long Chain-of-Thought Reasoning",
            "url": "https://openreview.net/pdf?id=OLodUbcWjB"
          },
          {
            "title": "FOCUSED CHAIN-OF-THOUGHT: EFFICIENT LLM REA-",
            "url": "https://arxiv.org/pdf/2511.22176"
          },
          {
            "title": "Technical Report: The Decreasing Value of Chain of Thought in Prompting - Wharton Generative AI Labs",
            "url": "https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought/"
          },
          {
            "title": "What Makes a Good Reasoning Chain? Uncovering ...",
            "url": "https://aclanthology.org/2025.emnlp-main.329.pdf"
          },
          {
            "title": "Comprehensive Survey on Prompts Generating via Knowledge-Guided Chain-of-Thought",
            "url": "https://www.sciopen.com/article/10.26599/IJCS.2024.9100038"
          }
        ]
      },
      "Based on the search results, I found several relevant findings about chain-of-thought reasoning and its performance challenges:\n\n## Key Findings\n\n**Performance Issues in Specific Contexts:**\n\nCoT reasoning is highly fragile: semantically irrelevant perturbations, such as distractor phrases or altered symbolic representations, can substantially degrade performance. Additionally, what appears to be structured reasoning can be a mirage, emerging from memorized or interpolated patterns in the training data rather than logical inference.\n\n**When CoT Fails:**\n\nCoT performance becomes fragile and prone to failure even under moderate distribution shifts to out-of-distribution data. This suggests that while CoT reasoning appears effective on in-distribution tasks, it may actually hurt performance when tasks deviate from training patterns.\n\n**Research on Decreasing Value:**\n\nA technical report from Wharton's Generative AI Labs titled \"The Decreasing Value of Chain of Thought in Prompting\" was published in June 2025, though specific details about its findings aren't fully available in the search results.\n\n**Smaller Models:**\n\nThere are references to research showing that \"CoT Harms Performance of Rather Smaller Language Models\", suggesting size-dependent effects where chain-of-thought prompting may not benefit or may even harm smaller models.\n\nThe research indicates that while chain-of-thought can be beneficial for complex reasoning tasks, it doesn't universally improve performance across all task types, models, and data distributions."
    ],
    "durationSeconds": 6.630809062000015
  }
}
```

</details>

---

### Assistant

_source line 86_

<details><summary>Logged reasoning block</summary>

```text
Let me get a few more papers:
1. "Is Chain-of-Thought Reasoning of LLMs a..." (from arxiv 2508.01191) 
2. Search for more about the BF16/FP16 instability in RL paper
3. Any more recent DocRE papers that I missed
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "ae70afea-48b5-4135-98dd-a1f4c42ffb86",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SUpsC8Ke5KMdaZXkSmK51j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2691,
      "cache_read_input_tokens": 65573,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2691
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

_source line 87_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019YKZGxWtJdgc3zDUK4tJaR`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.26788",
  "prompt": "Extract: title, authors, venue, year, abstract, key findings about BF16 vs FP16 in reinforcement learning training. Focus on training instability differences."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "eedbb0e2-9af9-48e9-9526-67cbbd087487",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SUpsC8Ke5KMdaZXkSmK51j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2691,
      "cache_read_input_tokens": 65573,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2691
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

_source line 88_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015XXhEWdwQ3pxFDviG9bENb`</summary>

```json
{
  "query": "LLM information extraction GRPO reward F1 score structured generation 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "9185b848-7a89-4e57-8375-fc0aa20b1312",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SUpsC8Ke5KMdaZXkSmK51j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2691,
      "cache_read_input_tokens": 65573,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2691
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

_source line 89_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ua3A7oHeeJC37y177ya73k`</summary>

```json
{
  "query": "\"document-level relation extraction\" LLM 2025 2026 ACL EMNLP NAACL new method"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "27ba34d9-c5b6-4f20-ac38-7aebe2c62e25",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SUpsC8Ke5KMdaZXkSmK51j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2691,
      "cache_read_input_tokens": 65573,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2691
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

_source line 90 · 2026-05-15T22:10:21.111Z_

<details><summary>↩ Tool result · `toolu_019YKZGxWtJdgc3zDUK4tJaR`</summary>

```text
# Paper Summary

**Title:** Defeating the Training-Inference Mismatch via FP16

**Authors:** Penghui Qi, Zichen Liu, Xiangxin Zhou, Tianyu Pang, Chao Du, Wee Sun Lee, Min Lin

**Venue:** arXiv (Computer Science > Machine Learning)

**Year:** 2025 (submitted October 30, 2025)

## Abstract
The research addresses instability in reinforcement learning fine-tuning of large language models caused by numerical inconsistencies between training and inference phases.

## Key Findings on BF16 vs FP16

The researchers discovered that "the root cause lies in the floating point precision itself." Despite BF16's widespread adoption and large dynamic range, the paper demonstrates that "BF16...introduces large rounding errors that breaks the consistency between training and inference."

In contrast, the authors show that "simply reverting to FP16 effectively eliminates this mismatch." Their findings indicate that uniform FP16 usage delivers improved training stability, faster convergence, and superior performance across different tasks and algorithms. The modification requires minimal implementation effort—only a few lines of code change—without necessitating architectural or algorithmic alterations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "f8026e2b-80b9-406d-82a8-f34ef22295a9",
  "tool_use_result": {
    "bytes": 46499,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Summary\n\n**Title:** Defeating the Training-Inference Mismatch via FP16\n\n**Authors:** Penghui Qi, Zichen Liu, Xiangxin Zhou, Tianyu Pang, Chao Du, Wee Sun Lee, Min Lin\n\n**Venue:** arXiv (Computer Science > Machine Learning)\n\n**Year:** 2025 (submitted October 30, 2025)\n\n## Abstract\nThe research addresses instability in reinforcement learning fine-tuning of large language models caused by numerical inconsistencies between training and inference phases.\n\n## Key Findings on BF16 vs FP16\n\nThe researchers discovered that \"the root cause lies in the floating point precision itself.\" Despite BF16's widespread adoption and large dynamic range, the paper demonstrates that \"BF16...introduces large rounding errors that breaks the consistency between training and inference.\"\n\nIn contrast, the authors show that \"simply reverting to FP16 effectively eliminates this mismatch.\" Their findings indicate that uniform FP16 usage delivers improved training stability, faster convergence, and superior performance across different tasks and algorithms. The modification requires minimal implementation effort—only a few lines of code change—without necessitating architectural or algorithmic alterations.",
    "durationMs": 4244,
    "url": "https://arxiv.org/abs/2510.26788"
  }
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-15T22:10:25.171Z_

<details><summary>↩ Tool result · `toolu_01Ua3A7oHeeJC37y177ya73k`</summary>

```text
Web search results for query: ""document-level relation extraction" LLM 2025 2026 ACL EMNLP NAACL new method"

Links: [{"title":"Survey on legal information extraction: current status and open challenges | Knowledge and Information Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10115-025-02600-5"},{"title":"Accepted Papers - NAACL-HLT 2025","url":"https://2025.naacl.org/program/accepted_papers/"},{"title":"A survey on cutting-edge relation extraction techniques based on language models | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11280-0"},{"title":"Document Intelligence in the Era of Large Language Models: A Survey","url":"https://arxiv.org/html/2510.13366v1"},{"title":"GitHub - 231sm/Low-resource-KEPapers: A Paper List of Low-resource Knowledge Extraction in NLP","url":"https://github.com/231sm/Low-resource-KEPapers"},{"title":"A survey on cutting-edge relation extraction techniques based on language models","url":"https://arxiv.org/html/2411.18157v1"},{"title":"GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub","url":"https://github.com/quqxui/Awesome-LLM4IE-Papers"},{"title":"M-BRe: Discovering Training Samples for Relation ...","url":"https://aclanthology.org/2025.emnlp-main.264.pdf"},{"title":"Aligning Large Language Models on Information Extraction","url":"https://aclanthology.org/2024.emnlp-main.419.pdf"},{"title":"A Comprehensive Survey on Relation Extraction: Recent Advances and New Frontiers | ACM Computing Surveys","url":"https://dl.acm.org/doi/10.1145/3674501"}]

Based on the search results, here's what I found regarding document-level relation extraction with LLMs in recent conferences (2025-2026):

## Recent Work on Document-Level Relation Extraction

LogicST is a logical self-training framework for document-level relation extraction with incomplete annotations, which was presented at EMNLP 2024.

There are methods focused on "Consistency Guided Knowledge Retrieval and Denoising in LLMs for Zero-shot Document-level Relation Triplet Extraction".

## Recent Survey on Relation Extraction Techniques

A comprehensive survey examines the latest advancements in Relation Extraction (RE), a pivotal task in natural language processing essential for applications across biomedical, financial, and legal sectors. This survey extends the review timeline to 2023, providing an updated perspective on trends in RE research.

## Key Findings on LLMs and RE

BERT-based methods dominate in achieving state-of-the-art results for RE while emerging large language models (LLMs) like T5 excel in few-shot relation extraction scenarios where they identify previously unseen relations.

## NAACL 2025 Accepted Papers

One accepted NAACL 2025 paper addresses "Improving Data Annotation for Low-Resource Relation Extraction with Logical Rule-Augmented Collaborative Language Models".

The search results show active research in document-level relation extraction using LLMs, particularly focusing on few-shot scenarios, incomplete annotations, and low-resource settings at major NLP conferences.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "eef0b877-150d-471b-be25-a768d16a2bfa",
  "tool_use_result": {
    "query": "\"document-level relation extraction\" LLM 2025 2026 ACL EMNLP NAACL new method",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VMmKqYnY3D5FbA6raUvDex",
        "content": [
          {
            "title": "Survey on legal information extraction: current status and open challenges | Knowledge and Information Systems | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s10115-025-02600-5"
          },
          {
            "title": "Accepted Papers - NAACL-HLT 2025",
            "url": "https://2025.naacl.org/program/accepted_papers/"
          },
          {
            "title": "A survey on cutting-edge relation extraction techniques based on language models | Artificial Intelligence Review | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s10462-025-11280-0"
          },
          {
            "title": "Document Intelligence in the Era of Large Language Models: A Survey",
            "url": "https://arxiv.org/html/2510.13366v1"
          },
          {
            "title": "GitHub - 231sm/Low-resource-KEPapers: A Paper List of Low-resource Knowledge Extraction in NLP",
            "url": "https://github.com/231sm/Low-resource-KEPapers"
          },
          {
            "title": "A survey on cutting-edge relation extraction techniques based on language models",
            "url": "https://arxiv.org/html/2411.18157v1"
          },
          {
            "title": "GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub",
            "url": "https://github.com/quqxui/Awesome-LLM4IE-Papers"
          },
          {
            "title": "M-BRe: Discovering Training Samples for Relation ...",
            "url": "https://aclanthology.org/2025.emnlp-main.264.pdf"
          },
          {
            "title": "Aligning Large Language Models on Information Extraction",
            "url": "https://aclanthology.org/2024.emnlp-main.419.pdf"
          },
          {
            "title": "A Comprehensive Survey on Relation Extraction: Recent Advances and New Frontiers | ACM Computing Surveys",
            "url": "https://dl.acm.org/doi/10.1145/3674501"
          }
        ]
      },
      "Based on the search results, here's what I found regarding document-level relation extraction with LLMs in recent conferences (2025-2026):\n\n## Recent Work on Document-Level Relation Extraction\n\nLogicST is a logical self-training framework for document-level relation extraction with incomplete annotations, which was presented at EMNLP 2024.\n\nThere are methods focused on \"Consistency Guided Knowledge Retrieval and Denoising in LLMs for Zero-shot Document-level Relation Triplet Extraction\".\n\n## Recent Survey on Relation Extraction Techniques\n\nA comprehensive survey examines the latest advancements in Relation Extraction (RE), a pivotal task in natural language processing essential for applications across biomedical, financial, and legal sectors. This survey extends the review timeline to 2023, providing an updated perspective on trends in RE research.\n\n## Key Findings on LLMs and RE\n\nBERT-based methods dominate in achieving state-of-the-art results for RE while emerging large language models (LLMs) like T5 excel in few-shot relation extraction scenarios where they identify previously unseen relations.\n\n## NAACL 2025 Accepted Papers\n\nOne accepted NAACL 2025 paper addresses \"Improving Data Annotation for Low-Resource Relation Extraction with Logical Rule-Augmented Collaborative Language Models\".\n\nThe search results show active research in document-level relation extraction using LLMs, particularly focusing on few-shot scenarios, incomplete annotations, and low-resource settings at major NLP conferences."
    ],
    "durationSeconds": 6.953418536000012
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-15T22:10:25.458Z_

<details><summary>↩ Tool result · `toolu_015XXhEWdwQ3pxFDviG9bENb`</summary>

```text
Web search results for query: "LLM information extraction GRPO reward F1 score structured generation 2025 2026 arxiv"

Links: [{"title":"Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning in Language Models","url":"https://arxiv.org/html/2605.08061v1"},{"title":"GraphRAG-R1: Graph Retrieval-Augmented Generation with Process-Constrained Reinforcement Learning","url":"https://arxiv.org/html/2507.23581v1"},{"title":"Benchmarking LLM-based Information Extraction Tools for ...","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full.pdf"},{"title":"arXiv:2504.14633v1 [cs.CL] 20 Apr 2025","url":"https://arxiv.org/pdf/2504.14633"},{"title":"Explore-on-Graph: Incentivizing Autonomous Exploration of Large Language Models on Knowledge Graphs with Path-refined Reward Modeling","url":"https://arxiv.org/html/2602.21728v1"},{"title":"Exploring LLMs for Scientific Information Extraction using the SciEx Framework","url":"https://arxiv.org/html/2512.10004v2"},{"title":"Tree Search for LLM Agent Reinforcement Learning","url":"https://arxiv.org/pdf/2509.21240"},{"title":"RATE: An LLM-Powered Retrieval Augmented Generation Technology-Extraction Pipeline","url":"https://arxiv.org/html/2507.21125v1"},{"title":"GitHub - bobxwu/learning-from-rewards-llm-papers: A comrephensive collection of learning from rewards in the post-training and test-time scaling of LLMs, with a focus on both reward models and learning strategies across training, inference, and post-inference stages. · GitHub","url":"https://github.com/bobxwu/learning-from-rewards-llm-papers"},{"title":"Reinforcement Learning Meets Large Language Models: A Survey of","url":"https://arxiv.org/pdf/2509.16679"}]

I found several relevant research papers and resources related to your search query. Here's a summary of what's available:

## Key Papers Found

**1. Rubric-Grounded Reinforcement Learning (2025)**
This paper instantiates a framework by deriving rubrics from scientific documents and training Llama-3.1-8B-Instruct with Group Relative Policy Optimization (GRPO), achieving structured rewards for information extraction tasks.

**2. GraphRAG-R1: Graph Retrieval-Augmented Generation (2025)**
This work employs a modified version of Group Relative Policy Optimization (GRPO) that supports rollout-with-thinking mechanism and designs two process-constrained reward functions, Progressive Retrieval Attenuation (PRA) and Cost-Aware F1 (CAF). The paper employs F1 Score for evaluation.

**3. LLM-based Information Extraction (Medical Domain)**
OpenAI's GPT 4.1-mini achieved an average F1 score of 55.6, while the best-performing local model was Google's Gemma3 with 27B parameters and an average F1 score of 41.3 on information extraction benchmarks.

**4. Scientific Information Extraction Framework (2026)**
The SciEx framework assesses performance using standard information extraction metrics including precision, recall, F1-score, and accuracy across datasets.

**5. LLM Reinforcement Learning Survey (2025)**
The DeepSeek team proposed Group Relative Policy Optimization (GRPO) with the core idea of sampling a set of outputs for each prompt and using the relative differences in intra-group feedback to guide policy updates.

These papers cover the intersection of GRPO, reward modeling, structured generation, and F1-score based evaluation for information extraction tasks, primarily from 2025-2026 arxiv submissions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "ce882750-0bf2-41d8-a73d-e39b9abce711",
  "tool_use_result": {
    "query": "LLM information extraction GRPO reward F1 score structured generation 2025 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_019eaepjJ6t9C5g2PTJECZbr",
        "content": [
          {
            "title": "Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning in Language Models",
            "url": "https://arxiv.org/html/2605.08061v1"
          },
          {
            "title": "GraphRAG-R1: Graph Retrieval-Augmented Generation with Process-Constrained Reinforcement Learning",
            "url": "https://arxiv.org/html/2507.23581v1"
          },
          {
            "title": "Benchmarking LLM-based Information Extraction Tools for ...",
            "url": "https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full.pdf"
          },
          {
            "title": "arXiv:2504.14633v1 [cs.CL] 20 Apr 2025",
            "url": "https://arxiv.org/pdf/2504.14633"
          },
          {
            "title": "Explore-on-Graph: Incentivizing Autonomous Exploration of Large Language Models on Knowledge Graphs with Path-refined Reward Modeling",
            "url": "https://arxiv.org/html/2602.21728v1"
          },
          {
            "title": "Exploring LLMs for Scientific Information Extraction using the SciEx Framework",
            "url": "https://arxiv.org/html/2512.10004v2"
          },
          {
            "title": "Tree Search for LLM Agent Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2509.21240"
          },
          {
            "title": "RATE: An LLM-Powered Retrieval Augmented Generation Technology-Extraction Pipeline",
            "url": "https://arxiv.org/html/2507.21125v1"
          },
          {
            "title": "GitHub - bobxwu/learning-from-rewards-llm-papers: A comrephensive collection of learning from rewards in the post-training and test-time scaling of LLMs, with a focus on both reward models and learning strategies across training, inference, and post-inference stages. · GitHub",
            "url": "https://github.com/bobxwu/learning-from-rewards-llm-papers"
          },
          {
            "title": "Reinforcement Learning Meets Large Language Models: A Survey of",
            "url": "https://arxiv.org/pdf/2509.16679"
          }
        ]
      },
      "I found several relevant research papers and resources related to your search query. Here's a summary of what's available:\n\n## Key Papers Found\n\n**1. Rubric-Grounded Reinforcement Learning (2025)**\nThis paper instantiates a framework by deriving rubrics from scientific documents and training Llama-3.1-8B-Instruct with Group Relative Policy Optimization (GRPO), achieving structured rewards for information extraction tasks.\n\n**2. GraphRAG-R1: Graph Retrieval-Augmented Generation (2025)**\nThis work employs a modified version of Group Relative Policy Optimization (GRPO) that supports rollout-with-thinking mechanism and designs two process-constrained reward functions, Progressive Retrieval Attenuation (PRA) and Cost-Aware F1 (CAF). The paper employs F1 Score for evaluation.\n\n**3. LLM-based Information Extraction (Medical Domain)**\nOpenAI's GPT 4.1-mini achieved an average F1 score of 55.6, while the best-performing local model was Google's Gemma3 with 27B parameters and an average F1 score of 41.3 on information extraction benchmarks.\n\n**4. Scientific Information Extraction Framework (2026)**\nThe SciEx framework assesses performance using standard information extraction metrics including precision, recall, F1-score, and accuracy across datasets.\n\n**5. LLM Reinforcement Learning Survey (2025)**\nThe DeepSeek team proposed Group Relative Policy Optimization (GRPO) with the core idea of sampling a set of outputs for each prompt and using the relative differences in intra-group feedback to guide policy updates.\n\nThese papers cover the intersection of GRPO, reward modeling, structured generation, and F1-score based evaluation for information extraction tasks, primarily from 2025-2026 arxiv submissions."
    ],
    "durationSeconds": 7.651794483999984
  }
}
```

</details>

---

### Assistant

_source line 93_

<details><summary>Logged reasoning block</summary>

```text
Let me now search for a few more papers that could be very relevant:

1. "Aligning Large Language Models on Information Extraction" (EMNLP 2024) - this is about IE alignment
2. Search for any papers about LoRA/QLoRA quantization effects on RL specifically
3. Any papers about "evidence generation" in document-level RE specifically with LLMs
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "66e1f837-295f-4d56-ae11-0eea47985862",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NBnoHxBfJXRsZeFBcC5uPH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 911,
      "cache_creation_input_tokens": 1642,
      "cache_read_input_tokens": 68264,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1642
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

_source line 94_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01ECNHB8K3uW54xFgJefqcwu`</summary>

```json
{
  "url": "https://aclanthology.org/2024.emnlp-main.419.pdf",
  "prompt": "Extract: title, authors, venue, year, abstract, key method, key findings. This paper is about aligning LLMs on information extraction."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "db51fa29-c137-4d04-87d1-b98a64f1a326",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NBnoHxBfJXRsZeFBcC5uPH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 911,
      "cache_creation_input_tokens": 1642,
      "cache_read_input_tokens": 68264,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1642
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

_source line 95_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Mcfg6FuahNAiTYxRNBVM6k`</summary>

```json
{
  "query": "ADELIE \"aligning large language models\" information extraction EMNLP 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "bcae3251-e8dd-4375-87f5-8be435d7fecc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NBnoHxBfJXRsZeFBcC5uPH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 911,
      "cache_creation_input_tokens": 1642,
      "cache_read_input_tokens": 68264,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1642
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

_source line 96_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ph8n3K43oEk7WLunChZ52G`</summary>

```json
{
  "query": "\"post-rationalization\" OR \"unfaithful explanation\" OR \"unfaithful rationale\" LLM evidence generation 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "87f71c29-0d88-4417-af83-608eb16bcc89",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NBnoHxBfJXRsZeFBcC5uPH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 911,
      "cache_creation_input_tokens": 1642,
      "cache_read_input_tokens": 68264,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1642
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

_source line 97 · 2026-05-15T22:10:39.108Z_

<details><summary>↩ Tool result · `toolu_01ECNHB8K3uW54xFgJefqcwu`</summary>

```text
# Paper Extraction Summary

**Title:** Not directly extractable from the provided PDF content

**Authors:** Not clearly visible in the provided excerpt

**Venue:** EMNLP 2024 (evident from file path: `/data/dcroce/EMNLP2024/conference_proceedings/main/papers/832.pdf`)

**Year:** 2024

**Abstract:** The document content provided is primarily binary PDF data with limited readable text. A full abstract cannot be reliably extracted from this format.

**Key Method:** The paper addresses "aligning LLMs on information extraction" as indicated in your prompt. Specific methodological details are not legible in the provided PDF stream data.

**Key Findings:** Unable to determine specific findings from the compressed/encoded PDF content provided.

---

**Note:** The source material appears to be a PDF file that requires proper rendering to extract text content. The binary/compressed nature of the provided data prevents reliable text extraction using standard parsing methods. To properly analyze this paper, the PDF would need to be decoded and rendered to access the full text, abstract, author information, and findings clearly.

[Binary content (application/pdf, 915.2KB) also saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/36a03546-b7c6-4659-a047-11cc70593f2c/tool-results/webfetch-1778883033134-liy1jx.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "c0602656-ac08-4909-90ca-6ef5541cf79a",
  "tool_use_result": {
    "bytes": 937165,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Extraction Summary\n\n**Title:** Not directly extractable from the provided PDF content\n\n**Authors:** Not clearly visible in the provided excerpt\n\n**Venue:** EMNLP 2024 (evident from file path: `/data/dcroce/EMNLP2024/conference_proceedings/main/papers/832.pdf`)\n\n**Year:** 2024\n\n**Abstract:** The document content provided is primarily binary PDF data with limited readable text. A full abstract cannot be reliably extracted from this format.\n\n**Key Method:** The paper addresses \"aligning LLMs on information extraction\" as indicated in your prompt. Specific methodological details are not legible in the provided PDF stream data.\n\n**Key Findings:** Unable to determine specific findings from the compressed/encoded PDF content provided.\n\n---\n\n**Note:** The source material appears to be a PDF file that requires proper rendering to extract text content. The binary/compressed nature of the provided data prevents reliable text extraction using standard parsing methods. To properly analyze this paper, the PDF would need to be decoded and rendered to access the full text, abstract, author information, and findings clearly.\n\n[Binary content (application/pdf, 915.2KB) also saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/36a03546-b7c6-4659-a047-11cc70593f2c/tool-results/webfetch-1778883033134-liy1jx.pdf]",
    "durationMs": 8116,
    "url": "https://aclanthology.org/2024.emnlp-main.419.pdf"
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-15T22:10:40.677Z_

<details><summary>↩ Tool result · `toolu_01Ph8n3K43oEk7WLunChZ52G`</summary>

```text
Web search results for query: ""post-rationalization" OR "unfaithful explanation" OR "unfaithful rationale" LLM evidence generation 2024 2025"

Links: [{"title":"arXiv:2412.18004v1 [cs.CL] 23 Dec 2024 Correctness is not Faithfulness","url":"https://arxiv.org/pdf/2412.18004"},{"title":"Correctness is not Faithfulness in Retrieval Augmented Generation Attributions","url":"https://staff.fnwi.uva.nl/m.derijke/wp-content/papercite-data/pdf/wallat-2025-correctness.pdf"},{"title":"Evaluating Reasoning Faithfulness in Medical Vision-Language Models using Multimodal Perturbations","url":"https://arxiv.org/html/2510.11196v1"},{"title":"Chain-of-Thought Is Not Explainability Fazl Barez∗ Oxford WhiteBox Tung-Yu Wu","url":"https://aigi.ox.ac.uk/wp-content/uploads/2025/07/Cot_Is_Not_Explainability.pdf"},{"title":"Unfaithful Explanations in Chain-of-Thought Prompting","url":"https://papers.neurips.cc/paper_files/paper/2023/file/ed3fea9033a80fea1376299fa7863f4a-Paper-Conference.pdf"},{"title":"Unfaithful chain-of-thought as nudged reasoning","url":"https://www.alignmentforum.org/posts/vPAFPpRDEg3vjhNFi/unfaithful-chain-of-thought-as-nudged-reasoning"},{"title":"Characterizing Large Language Models as Rationalizers of ...","url":"https://aclanthology.org/2024.findings-acl.484.pdf"},{"title":"Automated Interpretability-Driven Model Auditing and Control: A Research Agenda","url":"https://aigi.ox.ac.uk/wp-content/uploads/2026/01/Automated_interp_Research_Agenda.pdf"},{"title":"[PDF] Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Language-Models-Don't-Always-Say-What-They-Think:-Turpin-Michael/7dc928f41e15f65f1267bd87b0fcfcc7e715cb56"},{"title":"The “Unfaithful” Chain-of-Thought: Debunking Anthropomorphic Claims in LLM Research | by Iryna Nozdrin | Medium","url":"https://medium.com/@iryna.nozdrin/the-unfaithful-chain-of-thought-debunking-anthropomorphic-claims-in-llm-research-f6981f998116"}]

I found several highly relevant research papers and articles on post-rationalization, unfaithful explanations, and LLM evidence generation from 2024-2025. Here are the key findings:

## Major Research on Post-Rationalization and Unfaithful Explanations

Post-rationalized attributions are a special case of unfaithful behavior where an LLM's parametric memory produces an answer to a question, and the model looks for support in documents in a shallow way (e.g., by token-matching).

### Key Papers

**1. "Correctness is not Faithfulness" (December 2024)**

This research found that up to 57% of citations are post-rationalized, with findings suggesting that current attributed answers often lack citation faithfulness. The work focuses on post-rationalization to enhance accountability and help information retrieval systems avoid propagating biases or misinformation.

**2. "Chain-of-Thought Is Not Explainability" (2025)**

The research shows that small manipulations sway decisions with the CoT merely rationalizing rather than reporting true causes, and models silently correct mistakes without reflecting this in their reasoning, making assessing the faithfulness of CoT reasoning a non-trivial challenge.

**3. "Unfaithful Explanations in Chain-of-Thought Prompting" (2023-2024)**

CoT explanations can systematically misrepresent the true reason for a model's prediction.

### Recent Insights on Unfaithful Reasoning Mechanisms

Unfaithful CoTs are often not purely post hoc rationalizations and can be understood as biased reasoning, where models continually make choices during CoT, repeatedly drawing new propositions supporting or discouraging different answers, with hidden information nudging these choices while creating plausible-sounding CoTs.

These studies highlight a critical problem in LLM-generated explanations: models can produce coherent, convincing rationales that don't actually reflect their decision-making process.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "caa8c4c8-c682-4b04-beb2-ff25704fb58f",
  "tool_use_result": {
    "query": "\"post-rationalization\" OR \"unfaithful explanation\" OR \"unfaithful rationale\" LLM evidence generation 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_018kWh7TrCvgcwMLvzg1bZWQ",
        "content": [
          {
            "title": "arXiv:2412.18004v1 [cs.CL] 23 Dec 2024 Correctness is not Faithfulness",
            "url": "https://arxiv.org/pdf/2412.18004"
          },
          {
            "title": "Correctness is not Faithfulness in Retrieval Augmented Generation Attributions",
            "url": "https://staff.fnwi.uva.nl/m.derijke/wp-content/papercite-data/pdf/wallat-2025-correctness.pdf"
          },
          {
            "title": "Evaluating Reasoning Faithfulness in Medical Vision-Language Models using Multimodal Perturbations",
            "url": "https://arxiv.org/html/2510.11196v1"
          },
          {
            "title": "Chain-of-Thought Is Not Explainability Fazl Barez∗ Oxford WhiteBox Tung-Yu Wu",
            "url": "https://aigi.ox.ac.uk/wp-content/uploads/2025/07/Cot_Is_Not_Explainability.pdf"
          },
          {
            "title": "Unfaithful Explanations in Chain-of-Thought Prompting",
            "url": "https://papers.neurips.cc/paper_files/paper/2023/file/ed3fea9033a80fea1376299fa7863f4a-Paper-Conference.pdf"
          },
          {
            "title": "Unfaithful chain-of-thought as nudged reasoning",
            "url": "https://www.alignmentforum.org/posts/vPAFPpRDEg3vjhNFi/unfaithful-chain-of-thought-as-nudged-reasoning"
          },
          {
            "title": "Characterizing Large Language Models as Rationalizers of ...",
            "url": "https://aclanthology.org/2024.findings-acl.484.pdf"
          },
          {
            "title": "Automated Interpretability-Driven Model Auditing and Control: A Research Agenda",
            "url": "https://aigi.ox.ac.uk/wp-content/uploads/2026/01/Automated_interp_Research_Agenda.pdf"
          },
          {
            "title": "[PDF] Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Language-Models-Don't-Always-Say-What-They-Think:-Turpin-Michael/7dc928f41e15f65f1267bd87b0fcfcc7e715cb56"
          },
          {
            "title": "The “Unfaithful” Chain-of-Thought: Debunking Anthropomorphic Claims in LLM Research | by Iryna Nozdrin | Medium",
            "url": "https://medium.com/@iryna.nozdrin/the-unfaithful-chain-of-thought-debunking-anthropomorphic-claims-in-llm-research-f6981f998116"
          }
        ]
      },
      "I found several highly relevant research papers and articles on post-rationalization, unfaithful explanations, and LLM evidence generation from 2024-2025. Here are the key findings:\n\n## Major Research on Post-Rationalization and Unfaithful Explanations\n\nPost-rationalized attributions are a special case of unfaithful behavior where an LLM's parametric memory produces an answer to a question, and the model looks for support in documents in a shallow way (e.g., by token-matching).\n\n### Key Papers\n\n**1. \"Correctness is not Faithfulness\" (December 2024)**\n\nThis research found that up to 57% of citations are post-rationalized, with findings suggesting that current attributed answers often lack citation faithfulness. The work focuses on post-rationalization to enhance accountability and help information retrieval systems avoid propagating biases or misinformation.\n\n**2. \"Chain-of-Thought Is Not Explainability\" (2025)**\n\nThe research shows that small manipulations sway decisions with the CoT merely rationalizing rather than reporting true causes, and models silently correct mistakes without reflecting this in their reasoning, making assessing the faithfulness of CoT reasoning a non-trivial challenge.\n\n**3. \"Unfaithful Explanations in Chain-of-Thought Prompting\" (2023-2024)**\n\nCoT explanations can systematically misrepresent the true reason for a model's prediction.\n\n### Recent Insights on Unfaithful Reasoning Mechanisms\n\nUnfaithful CoTs are often not purely post hoc rationalizations and can be understood as biased reasoning, where models continually make choices during CoT, repeatedly drawing new propositions supporting or discouraging different answers, with hidden information nudging these choices while creating plausible-sounding CoTs.\n\nThese studies highlight a critical problem in LLM-generated explanations: models can produce coherent, convincing rationales that don't actually reflect their decision-making process."
    ],
    "durationSeconds": 8.396984067999991
  }
}
```

</details>

---

### Tool result

_source line 99 · 2026-05-15T22:10:42.885Z_

<details><summary>↩ Tool result · `toolu_01Mcfg6FuahNAiTYxRNBVM6k`</summary>

```text
Web search results for query: "ADELIE "aligning large language models" information extraction EMNLP 2024"

Links: [{"title":"GitHub - THU-KEG/ADELIE: [EMNLP2024] Aligning Large Language Models on Information Extraction · GitHub","url":"https://github.com/THU-KEG/ADELIE"},{"title":"ADELIE: Aligning Large Language Models on Information Extraction - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.419/"},{"title":"[2405.05008] ADELIE: Aligning Large Language Models on Information Extraction","url":"https://arxiv.org/abs/2405.05008"},{"title":"[Quick Review] ADELIE: Aligning Large Language Models on Information Extraction","url":"https://liner.com/review/adelie-aligning-large-language-models-on-information-extraction"},{"title":"ADELIE: Aligning Large Language Models on Information Extraction | Request PDF","url":"https://www.researchgate.net/publication/386188440_ADELIE_Aligning_Large_Language_Models_on_Information_Extraction"},{"title":"Aligning Large Language Models on Information Extraction","url":"https://aclanthology.org/2024.emnlp-main.419.pdf"},{"title":"ADELIE: Aligning Large Language Models on Information Extraction","url":"https://arxiv.org/html/2405.05008v1"},{"title":"Main Conference - EMNLP 2024","url":"https://2024.emnlp.org/program/accepted_main_conference/"},{"title":"ADELIE: Aligning Large Language Models on Information Extraction | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/adelie-aligning-large-language-models-information-extraction"},{"title":"ADELIE: Aligning Large Language Models on Information Extraction","url":"https://paperreading.club/page?id=226238"}]

I found comprehensive information about ADELIE from the EMNLP 2024 conference. Here's what I discovered:

## Overview

ADELIE: Aligning Large Language Models on Information Extraction was published in the Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, pages 7371–7387, Miami, Florida, USA.

## The Problem and Solution

Large language models (LLMs) usually fall short on information extraction (IE) tasks and struggle to follow the complex instructions of IE tasks. This primarily arises from LLMs not being aligned with humans, as mainstream alignment datasets typically do not include IE data.

## Methodology

ADELIE is an aligned LLM that effectively solves various IE tasks, including closed IE, open IE, and on-demand IE. The authors first collected and constructed a high-quality alignment corpus IEInstruct for IE. Then they trained ADELIE_SFT using instruction tuning on IEInstruct. They further trained ADELIE_SFT with direct preference optimization (DPO) objective, resulting in ADELIE_DPO.

## Results and Models

Extensive experiments on various held-out IE datasets demonstrate that the models (ADELIE_SFT and ADELIE_DPO) achieve state-of-the-art (SoTA) performance among open-source models. Three ADELIE models are released based on LLama-2 (7B), Llama-3.2 (3B) and Qwen2.5 (1.5B).

## Authors

The paper is authored by Yunjia Qi, Hao Peng, Xiaozhi Wang, Bin Xu, Lei Hou, and Juanzi Li.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "0c1a91af-e633-4a07-9345-2dead8fdbb25",
  "tool_use_result": {
    "query": "ADELIE \"aligning large language models\" information extraction EMNLP 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Rp5CbirEop4ZAsbMsBPKnB",
        "content": [
          {
            "title": "GitHub - THU-KEG/ADELIE: [EMNLP2024] Aligning Large Language Models on Information Extraction · GitHub",
            "url": "https://github.com/THU-KEG/ADELIE"
          },
          {
            "title": "ADELIE: Aligning Large Language Models on Information Extraction - ACL Anthology",
            "url": "https://aclanthology.org/2024.emnlp-main.419/"
          },
          {
            "title": "[2405.05008] ADELIE: Aligning Large Language Models on Information Extraction",
            "url": "https://arxiv.org/abs/2405.05008"
          },
          {
            "title": "[Quick Review] ADELIE: Aligning Large Language Models on Information Extraction",
            "url": "https://liner.com/review/adelie-aligning-large-language-models-on-information-extraction"
          },
          {
            "title": "ADELIE: Aligning Large Language Models on Information Extraction | Request PDF",
            "url": "https://www.researchgate.net/publication/386188440_ADELIE_Aligning_Large_Language_Models_on_Information_Extraction"
          },
          {
            "title": "Aligning Large Language Models on Information Extraction",
            "url": "https://aclanthology.org/2024.emnlp-main.419.pdf"
          },
          {
            "title": "ADELIE: Aligning Large Language Models on Information Extraction",
            "url": "https://arxiv.org/html/2405.05008v1"
          },
          {
            "title": "Main Conference - EMNLP 2024",
            "url": "https://2024.emnlp.org/program/accepted_main_conference/"
          },
          {
            "title": "ADELIE: Aligning Large Language Models on Information Extraction | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/adelie-aligning-large-language-models-information-extraction"
          },
          {
            "title": "ADELIE: Aligning Large Language Models on Information Extraction",
            "url": "https://paperreading.club/page?id=226238"
          }
        ]
      },
      "I found comprehensive information about ADELIE from the EMNLP 2024 conference. Here's what I discovered:\n\n## Overview\n\nADELIE: Aligning Large Language Models on Information Extraction was published in the Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, pages 7371–7387, Miami, Florida, USA.\n\n## The Problem and Solution\n\nLarge language models (LLMs) usually fall short on information extraction (IE) tasks and struggle to follow the complex instructions of IE tasks. This primarily arises from LLMs not being aligned with humans, as mainstream alignment datasets typically do not include IE data.\n\n## Methodology\n\nADELIE is an aligned LLM that effectively solves various IE tasks, including closed IE, open IE, and on-demand IE. The authors first collected and constructed a high-quality alignment corpus IEInstruct for IE. Then they trained ADELIE_SFT using instruction tuning on IEInstruct. They further trained ADELIE_SFT with direct preference optimization (DPO) objective, resulting in ADELIE_DPO.\n\n## Results and Models\n\nExtensive experiments on various held-out IE datasets demonstrate that the models (ADELIE_SFT and ADELIE_DPO) achieve state-of-the-art (SoTA) performance among open-source models. Three ADELIE models are released based on LLama-2 (7B), Llama-3.2 (3B) and Qwen2.5 (1.5B).\n\n## Authors\n\nThe paper is authored by Yunjia Qi, Hao Peng, Xiaozhi Wang, Bin Xu, Lei Hou, and Juanzi Li."
    ],
    "durationSeconds": 11.500692596000007
  }
}
```

</details>

---

### Assistant

_source line 100_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture. Let me also search for a few more specific papers that could be important:

1. Search for papers about "Characterizing LLMs as Rationalizers" (ACL Findings 2024)
2. Search for the "CoT is not Explainability" paper (2025)
3. Any recent DocRE paper with LLM + evidence that I might have missed

Actually, I think I have enough material now. Let me compile the new papers and update the literature map.

New papers to add:

### Category: RL for IE (existing category 7)


**R²GRPO** applies GRPO with rule-based rewards to scientific relation extraction, and **MO-GRPO** addresses reward hacking issues when using GRPO in multi-objective settings—both recent 2025 papers that fit into the RL and reward design categories.

**RDPO** tackles the instability that comes from correlating multiple objectives by decorrelating rewards, while **EvidenceRL** is the closest existing work to what I'm building, using GRPO with evidence grounding rewards in QA tasks, though it hasn't explored the performance trade-offs between extraction quality and evidence generation that I'm investigating for document relation extraction.

Moving into the LLM-based DocRE space, **ADELIE** combines SFT and DPO for information extraction alignment, and there's emerging theory suggesting **GRPO functions equivalently to a process reward model**, which could explain why it works well for evidence-grounded objectives. I should also consider **Wang et al.'s work on reward hacking**, which examines how proxy rewards can compress perception and reasoning in large models—relevant for understanding whether my evidence reward might inadvertently optimize for superficial patterns rather than genuine faithfulness.

On the evidence generation side, there's a critical distinction: **CoT outputs rationalize rather than explain**, meaning they don't necessarily reflect the model's actual reasoning process. This connects to post-hoc rationalization findings in LLMs, which suggests I need to be careful about interpreting evidence chains as ground truth. Finally, there's a practical stability concern—**BF16 precision in RL training introduces rounding errors that destabilize optimization**, and since QLoRA uses quantization, this could be contributing to the instability I'm seeing in my GRPO experiments.

What's interesting is that nobody has specifically studied the performance cost of requiring evidence generation in document relation extraction with LLMs, which suggests this is a novel angle. Similarly, the QLoRA-specific task decoupling phenomenon doesn't appear in the literature—the BF16 paper hints that quantization noise can cause training instability, but it doesn't address multi-task decoupling directly.

Now I'm compiling the updated literature map and counting the genuinely new papers I've found: MO-GRPO for multi-objective reward hacking, RDPO for reward-decorrelated policy optimization, EvidenceRL which combines GRPO with evidence faithfulness rewards, R²GRPO applied to scientific information extraction, ADELIE for aligning LLMs on IE tasks, and a paper showing GRPO functions as a process reward model.

I'm also identifying several other key papers: a reward hacking survey covering the proxy compression hypothesis, work on FP16 stability in RL training, research distinguishing chain-of-thought as rationalization rather than true explainability, characterization of LLMs as post-hoc rationalizers, a knowledge graph extraction approach with provenance tracking, and a survey on latent versus explicit reasoning in language models.

Let me verify which entries are already in the existing map before adding these new ones. I'm checking the tool constraints for writing to literature_map.yaml—the save_project_file tool only supports specific files like memory.md and writing_plan.yaml, so I'll need to verify if there's a dedicated tool for updating the literature map, or if I should work with the file size constraints since the existing content is already quite large.

Now I'm organizing the new entries I found across the relevant categories: adding MO-GRPO and RDPO to reward diversity, GRPO is Secretly a PRM and λ-GRPO to mode collapse prevention, EvidenceRL as a key finding for evidence-based rewards, R²GRPO for scientific information extraction, ADELIE for LLM-based document relation extraction, CoT is not Explainability and the Latent CoT survey for the evidence generation tradeoff section, and Characterizing LLMs as Rationalizers for faithfulness. I'll append these to their respective categories in the YAML file.

I'm also identifying a new category around training precision and RL stability with FP16 for RL stability and the reward hacking survey with the proxy compression hypothesis, then I'll read the current file and integrate all these additions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "953953c2-00bd-43cd-aa51-160892a4dab5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013myoGy5AeeGYwfN3fNo9Vr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1224,
      "cache_creation_input_tokens": 2570,
      "cache_read_input_tokens": 69906,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2570
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

_source line 101_

搜索基本完成。发现了 **EvidenceRL**（GRPO + evidence faithfulness reward，2026）这篇极度相关的论文。现在整合所有新发现并更新 literature_map.yaml。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "cf36e6a8-f0cf-4f56-8ce4-46293ebdc8e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013myoGy5AeeGYwfN3fNo9Vr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1224,
      "cache_creation_input_tokens": 2570,
      "cache_read_input_tokens": 69906,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2570
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

_source line 102_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01SA4T4MoZD3wip9cKdCNPXs`</summary>

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
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "97c0f31d-fda5-40a8-bac8-ed49c303424b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013myoGy5AeeGYwfN3fNo9Vr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1224,
      "cache_creation_input_tokens": 2570,
      "cache_read_input_tokens": 69906,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2570
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

_source line 103 · 2026-05-15T22:11:31.666Z_

<details><summary>↩ Tool result · `toolu_01SA4T4MoZD3wip9cKdCNPXs`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml\", \"content\": \"# Literature Map for faith-evidence-ie (FREIGE)\\n# Focus: CED-as-training-stabilizer (D024) + RSFT for DocRE\\n# Updated: 2026-05-15 (W3 reviewer gap fill + evidence generation trade-off survey)\\n\\npapers:\\n\\n  # === Category 1: Reward Diversity / Reward Shaping for RL Stability ===\\n\\n  - title: \\\"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization\\\"\\n    authors: NVIDIA Labs\\n    year: 2025\\n    venue: ICML 2026\\n    url: https://arxiv.org/abs/2601.05242\\n    category: reward_diversity\\n    role: closest_prior_work\\n    key_finding: >\\n      直接将 GRPO 应用于多 reward 组合时，不同 rollout 的 reward 组合在归一化后 collapse 为相同 advantage 值，\\n      降低训练信号分辨率导致收敛失败。GDPO 对每个 reward 独立做 group-wise normalization 再聚合，\\n      保留多 reward 的相对差异，显著提升训练稳定性。\\n    relevance_to_ced_stabilizer: >\\n      最直接相关。CED reward 本质上引入了独立于 extraction F1 的 reward 维度（evidence quality），\\n      GDPO 的理论分析解释了为什么多维 reward 比单一 reward 更稳定——独立 reward 维度防止 advantage collapse。\\n      但 GDPO 是方法论贡献，CED 是 task-specific reward 设计自然具备了这一特性。\\n\\n  - title: \\\"DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of LLMs\\\"\\n    authors: Xiwen Chen et al.\\n    year: 2025\\n    venue: arXiv 2505.09655\\n    url: https://arxiv.org/abs/2505.09655\\n    category: reward_diversity\\n    role: related_method\\n    key_finding: >\\n      GRPO 的标量 reward 无法区分语义多样但得分相同的输出（diversity-quality inconsistency）。\\n      DRA 用子模互信息（SMI）对 reward 加权，给多样性高的 completion 更大权重，\\n      等价于 Inverse Propensity Scoring 去偏，防止 policy 坍缩到先验模式。\\n    relevance_to_ced_stabilizer: >\\n      DRA 通过后处理 reward 注入多样性信号；CED 的 reward 本身就内含对比结构自然提供 diversity 信号。\\n      机制互补但来源不同——CED 是 reward design 层面，DRA 是 optimization 层面。\\n\\n  - title: \\\"Shrinking the Variance: Shrinkage Baselines for RL with Verifiable Rewards\\\"\\n    authors: Guanning Zeng et al.\\n    year: 2025\\n    venue: arXiv 2511.03710\\n    url: https://arxiv.org/abs/2511.03710\\n    category: reward_diversity\\n    role: theoretical_support\\n    key_finding: >\\n      RLVR 中 per-prompt 均值 baseline 在低 generation 数下估计不准导致高 variance 梯度。\\n      用 James-Stein shrinkage 混合 per-prompt 和 cross-prompt 均值，\\n      构造可证明更低 variance 的 policy gradient estimator。\\n    relevance_to_ced_stabilizer: >\\n      理论支持：reward variance 对 gradient estimation 质量至关重要。\\n      CED 的额外 reward 维度提供更丰富的 per-group variance，间接起到 variance 维持效果。\\n\\n  - title: \\\"Reward Shaping to Mitigate Reward Hacking in RLHF\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2502.18770\\n    url: https://arxiv.org/abs/2502.18770\\n    category: reward_diversity\\n    role: background\\n    key_finding: >\\n      RL reward 应有界且先快速增长后缓慢收敛。系统研究 reward shaping 原则，\\n      好的 reward 形状能抑制 reward hacking 并提升训练稳定性。\\n    relevance_to_ced_stabilizer: >\\n      CED reward 的 0-1 对比判别结构天然满足有界性，\\n      且 evidence quality 的渐进提升符合\\\"先快后慢\\\"的 reward shaping 原则。\\n\\n  # === Category 2: Mode Collapse Prevention in GRPO/RLHF ===\\n\\n  - title: \\\"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\\\"\\n    authors: ByteDance Seed, Tsinghua AIR\\n    year: 2025\\n    venue: NeurIPS 2025\\n    url: https://arxiv.org/abs/2503.14476\\n    category: mode_collapse_prevention\\n    role: key_baseline\\n    key_finding: >\\n      Naive GRPO 存在 entropy collapse（policy 熵快速下降→输出同质化）。\\n      根因：clipping 不对称性——概率 0.01 的 token 最多增到 0.012，而概率 0.9 的 token 可达 1.08，\\n      低概率 token 难以增长，抑制探索。DAPO 提出 Clip-Higher（εhigh=0.28 > εlow=0.2）\\n      为低概率 token 留更大增长空间，加 Dynamic Sampling 过滤 accuracy=0 或 1 的 prompt\\n      （这些 prompt 产生零梯度，降低有效 batch size）。在 AIME 2024 达 50 分超越 DeepSeek-R1-Zero。\\n    relevance_to_ced_stabilizer: >\\n      DAPO 从 optimization 技巧角度解决 entropy collapse。CED reward 从 reward design 层面\\n      防止 mode collapse——evidence quality 维度确保 reward 组内有足够 variance，\\n      不会出现 all-same-reward 的零梯度 prompt。DAPO 的 Dynamic Sampling 过滤 accuracy=0/1 prompt\\n      与我们观察到的 frac_zero_std→0.8 现象本质相同：extraction-only reward 下大量 prompt\\n      产生零 advantage，CED 从源头（reward 设计）而非后处理（过滤）解决这个问题。\\n\\n  - title: \\\"Dr. GRPO: Removing Optimization Bias in GRPO\\\"\\n    authors: Liu et al.\\n    year: 2025\\n    venue: COLM 2025\\n    url: https://arxiv.org/abs/2503.20783\\n    category: mode_collapse_prevention\\n    role: related_analysis\\n    key_finding: >\\n      GRPO 的 std 归一化引入两个 bias：(1) difficulty bias——std(r) 归一化对低 variance 组\\n      （全对/全错）给予过高 advantage 权重，trivial question 主导训练信号；\\n      (2) length bias——per-token loss 的 1/|o_i| 项使长的错误回答被 under-penalize。\\n      当 std(r)→0 时 advantage 爆炸或未定义，梯度数值不稳定。\\n      Dr. GRPO 移除 std 归一化，用无偏 Monte Carlo advantage：Ã = R(q,o_i) - mean(R)。\\n    relevance_to_ced_stabilizer: >\\n      与我们的实验发现高度一致：extraction-only reward 下 frac_zero_std→0.8 正是\\n      Dr. GRPO 分析的 difficulty bias 极端情况——大量 prompt 的所有 rollout 得到相同 F1，\\n      std→0 导致 advantage 异常。CED 通过增加 reward 维度天然维持 reward_std>0，\\n      从 reward 设计而非算法修改角度避免了 Dr. GRPO 发现的 bias。\\n\\n  - title: \\\"GVPO: Group Variance Policy Optimization for LLM Post-Training\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: NeurIPS 2025\\n    url: https://arxiv.org/abs/2504.19599\\n    category: mode_collapse_prevention\\n    role: alternative_framework\\n    key_finding: >\\n      将 KL 约束 reward 最大化的解析解直接嵌入梯度权重，\\n      variance 项自然平衡 exploration 与 exploitation，维持适度 entropy。\\n    relevance_to_ced_stabilizer: >\\n      GVPO 的 variance 项机制与 CED 维持 reward variance 的效果功能类似，\\n      但 GVPO 是算法层面 implicit regularization，CED 是 reward 层面 explicit structure。\\n\\n  - title: \\\"REINFORCE++: Stabilizing Critic-Free Policy Optimization with Global Advantage Normalization\\\"\\n    authors: Jian Hu et al.\\n    year: 2025\\n    venue: arXiv 2501.03262\\n    url: https://arxiv.org/abs/2501.03262\\n    category: mode_collapse_prevention\\n    role: related_method\\n    key_finding: >\\n      Prompt-level (local) advantage normalization 导致不准确估计和过拟合。\\n      Global batch normalization 提供更稳定、理论无偏的 gradient estimator。\\n    relevance_to_ced_stabilizer: >\\n      解决 local normalization 的 variance 问题；CED 从 reward 端增加 variance 来源。\\n      两者在不同层面解决同一问题：防止 gradient signal 消失。\\n\\n  - title: \\\"DiverseGRPO: Mitigating Mode Collapse in Image Generation via Diversity-Aware GRPO\\\"\\n    authors: Henglin Liu et al.\\n    year: 2025\\n    venue: arXiv 2512.21514\\n    url: https://arxiv.org/abs/2512.21514\\n    category: mode_collapse_prevention\\n    role: parallel_work\\n    key_finding: >\\n      图像生成中 GRPO 后期输出同质化。distributional reward modeling（谱聚类+exploratory reward）\\n      和 structure-aware regularization 实现 13-18% 语义多样性提升。\\n    relevance_to_ced_stabilizer: >\\n      跨域验证了 GRPO mode collapse 的普遍性，distributional reward 思路与 CED 精神相近——\\n      都是通过 reward 层面结构化信号维持输出多样性。\\n\\n  - title: \\\"Why GRPO Needs Normalization: A Local-Curvature Perspective on Adaptive Gradients\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2601.23135\\n    url: https://arxiv.org/abs/2601.23135\\n    category: mode_collapse_prevention\\n    role: theoretical_support\\n    key_finding: >\\n      GRPO 的 reward_std 归一化在温和条件下提供严格优于未归一化 REINFORCE 的收敛速率，\\n      收益由 prompt 间平均 reward std 刻画。\\n    relevance_to_ced_stabilizer: >\\n      直接理论支撑：reward_std 越大收敛越好。CED 通过 evidence quality 维度维持高 reward_std，\\n      从该理论看 CED 的稳定性优势是 reward_std 维持带来的收敛速率优势。\\n\\n  # === Category 3: Contrastive Rewards in RL ===\\n\\n  - title: \\\"Improving Reinforcement Learning from Human Feedback Using Contrastive Rewards\\\"\\n    authors: Shen, Zhang et al.\\n    year: 2024\\n    venue: arXiv 2403.07708\\n    url: https://arxiv.org/abs/2403.07708\\n    category: contrastive_reward\\n    role: closest_contrastive_precedent\\n    key_finding: >\\n      两步机制：(1) 离线采样 baseline response；(2) 用 baseline 计算 contrastive reward\\n      作为 PPO 的 penalty 项。效果：惩罚 reward uncertainty、根据任务难度自适应校准、\\n      减少 PPO 中的 variance。在 TL;DR 和 HH-RLHF 上持续优于标准 RLHF。\\n    relevance_to_ced_stabilizer: >\\n      最接近的对比 reward 先例。关键差异：(1) 它是对 learned RM 输出的后处理对比，\\n      CED 是 reward function 本身就是对比判别（evidence vs. corrupted evidence）；\\n      (2) 它在 PPO 中验证，CED 在 GRPO 中验证；\\n      (3) 它是 domain-agnostic penalty，CED 是 task-specific faithfulness signal。\\n      stabilizing 机制相通但实现路径根本不同。\\n\\n  - title: \\\"Improving Discriminative Capability of Reward Models in RLHF Using Contrastive Learning\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: EMNLP 2024\\n    url: https://aclanthology.org/2024.emnlp-main.852/\\n    category: contrastive_reward\\n    role: related_method\\n    key_finding: >\\n      无监督对比损失训练 reward model 充分捕捉对比数据区分度，\\n      带来更稳定的 PPO 训练 return 和 reward。\\n    relevance_to_ced_stabilizer: >\\n      验证对比训练 reward model → 更稳定 RL 训练链条。CED 不是对比训练 reward model，\\n      而是 reward function 本身就是对比判别，但 stabilizing 机制相通。\\n\\n  - title: \\\"Contrastive Preference Learning: Learning from Human Feedback without RL\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: ICLR 2025\\n    url: https://openreview.net/forum?id=iX1RjVQODj\\n    category: contrastive_reward\\n    role: background\\n    key_finding: >\\n      将 preference learning 重新表述为对比学习问题，无需显式 RL 即可从人类反馈中学习。\\n    relevance_to_ced_stabilizer: >\\n      对比框架在 preference alignment 中的通用性。CED 可被视为 task-specific contrastive preference signal。\\n\\n  # === Category 4: Evidence-Based Rewards in IE/NLP ===\\n\\n  - title: \\\"Drift: Enhancing LLM Faithfulness in Rationale Generation\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: ACL 2025\\n    url: https://aclanthology.org/2025.acl-long.340.pdf\\n    category: evidence_reward\\n    role: related_method\\n    key_finding: >\\n      用 faithfulness reward 引导 LLM 生成更可靠的 rationale，提升 CoT 推理事实一致性。\\n    relevance_to_ced_stabilizer: >\\n      Faithfulness reward 用于生成质量的先例。CED 中 evidence discrimination\\n      本质上也是 faithfulness 信号——判断证据是否忠实支持抽取结果。\\n\\n  - title: \\\"Fine-Grained NLI-Based Faithfulness Evaluation for Diverse Summarisation Tasks (INFUSE)\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: EACL 2024\\n    url: https://aclanthology.org/2024.eacl-long.102/\\n    category: evidence_reward\\n    role: background\\n    key_finding: >\\n      变长前提+简化假设的细粒度 NLI faithfulness 评估，超越传统 NLI 在多任务摘要上的表现。\\n    relevance_to_ced_stabilizer: >\\n      NLI 作为 faithfulness 评估工具的进展。CED 中 NLI 组件用于判断 evidence 对 triple 的支持度。\\n\\n  - title: \\\"Enhancing Cross-Evidence Reasoning Graph for Document-Level Relation Extraction\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: PMC/Bioinformatics 2024\\n    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11232587/\\n    category: evidence_reward\\n    role: background\\n    key_finding: >\\n      文档级关系抽取中用 cross-evidence reasoning graph 增强跨证据推理。\\n    relevance_to_ced_stabilizer: >\\n      DocRE 中 evidence 的重要性。但用 evidence 作为模型输入特征，\\n      我们用 evidence quality 作为 RL reward 信号——定位根本不同。\\n\\n  # === Category 5: Multi-Objective RL for Text Generation ===\\n\\n  - title: \\\"Confronting Reward Model Overoptimization with Constrained RLHF\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: OpenReview\\n    url: https://openreview.net/forum?id=gkfUvn0fLU\\n    category: multi_objective_rl\\n    role: related_analysis\\n    key_finding: >\\n      多组件 RM 的 overoptimization 研究。component RM 间的相关性显著影响 overoptimization 临界点，\\n      用 constrained MDP 防止超出适当边界。\\n    relevance_to_ced_stabilizer: >\\n      CED 引入了与 extraction F1 低相关的 reward component（evidence quality），\\n      根据该论文分析低相关多组件 reward 更不易 overoptimize，\\n      可能是 CED 稳定性的另一个理论解释角度。\\n\\n  - title: \\\"On-Policy RL with Optimal Reward Baseline\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2505.23585\\n    url: https://arxiv.org/abs/2505.23585\\n    category: multi_objective_rl\\n    role: theoretical_support\\n    key_finding: >\\n      Optimal baseline 一致性地实现更高训练 reward 和更高 entropy，\\n      有效稳定训练并促进更多样的 policy exploration。\\n    relevance_to_ced_stabilizer: >\\n      CED reward 的多维特性可能起到类似 optimal baseline 效果——\\n      evidence quality 维度为 advantage estimation 提供更丰富的参照信号。\\n\\n  # === Category 6: RSFT Methodology & Theory ===\\n\\n  - title: \\\"A Minimalist Approach to LLM Reasoning: from Rejection Sampling to Reinforce\\\"\\n    authors: Xiao et al.\\n    year: 2025\\n    venue: arXiv 2504.11343\\n    url: https://arxiv.org/abs/2504.11343\\n    category: rsft_methodology\\n    role: key_theoretical_support\\n    key_finding: >\\n      RAFT（简单 rejection sampling baseline）在数学推理上与 GRPO/PPO 表现相当。\\n      消融实验表明 GRPO 的主要优势来自丢弃全错 prompt 而非 reward normalization。\\n      提出 Reinforce-Rej，在 RAFT 基础上过滤全对和全错 sample。\\n      关键洞察：GRPO 和 RAFT 的核心区别在于负样本处理——GRPO 混合正负样本训练，\\n      RAFT 只用正样本，但 RAFT 仍能达到相当性能，说明 rejection sampling 的简单性被低估了。\\n    relevance_to_rsft_docre: >\\n      直接支持我们的设计选择：(1) RSFT 在 DocRE 上成功而 GRPO 失败，\\n      与该论文发现一致——rejection sampling 的 offline 特性天然避免了 catastrophic forgetting；\\n      (2) GRPO 主要优势来自过滤全错 prompt，这与我们 RSFT 的 reward-based filtering 机制相同；\\n      (3) DocRE structured output 比 math reasoning 更难用 online RL 优化，\\n      强化了 offline RSFT 的合理性。\\n\\n  - title: \\\"Beyond Rejection Sampling: Trajectory Fusion for Scaling Mathematical Reasoning (TrajFusion)\\\"\\n    authors: Jie Deng et al.\\n    year: 2026\\n    venue: arXiv 2602.04391\\n    url: https://arxiv.org/abs/2602.04391\\n    category: rsft_methodology\\n    role: method_component\\n    key_finding: >\\n      传统 RSFT 只用正确轨迹，丢弃错误轨迹。TrajFusion 将错误和正确轨迹交替拼接，\\n      显式建模试错推理过程，在困难数学问题上显著超越标准 RFT。\\n    relevance_to_rsft_docre: >\\n      Future work 方向：可考虑在 DocRE RSFT 中融合失败样本的信息。\\n      但 DocRE 的结构化输出（JSON triple）不同于 math 的 chain-of-thought，\\n      融合方式需要重新设计。\\n\\n  - title: \\\"Rejection Sampling Based Fine Tuning Secretly Performs PPO\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: ICML 2025\\n    url: https://openreview.net/forum?id=yQ2UivKlir\\n    category: rsft_methodology\\n    role: theoretical_support\\n    key_finding: >\\n      建立 RSFT 与 PPO 之间的理论联系：rejection sampling fine-tuning\\n      在特定条件下隐式执行 PPO with marginal KL constraints。\\n    relevance_to_rsft_docre: >\\n      为 RSFT 的有效性提供理论解释。我们的 RSFT 成功可被视为\\n      隐式执行了 constrained policy optimization，\\n      避免了显式 GRPO 在 structured output 上的不稳定性。\\n\\n  # === Category 7: RL for Information Extraction ===\\n\\n  - title: \\\"R1-RE: Cross-Domain Relation Extraction with RLVR\\\"\\n    authors: Runpeng Dai, Tong Zheng et al.\\n    year: 2025\\n    venue: arXiv 2507.04642\\n    url: https://arxiv.org/abs/2507.04642\\n    category: rl_for_ie\\n    role: direct_competitor\\n    key_finding: >\\n      首个将 RLVR（GRPO + verifiable reward）用于关系抽取的框架。\\n      将 RE 重构为推理任务，R1-RE-7B 在跨域 OOD 准确率约 70%，媲美 GPT-4o。\\n      Reward 设计：format reward (+1/-3) + metric reward (+2/-1.5)，先验证格式再加准确度。\\n      triplet extraction 用 F1-based reward（entity weight=1, triplet weight=3）。\\n      未报告 catastrophic forgetting——GRPO 训练后在 MATH-500/IFEval/GPQA 上性能不降反升，\\n      说明句子级 RE 的简单 reward 结构足以稳定 GRPO 训练。\\n    results:\\n      sem2010_in_domain: 91.8\\n      sem2010_ood: 66.5\\n      mdkg_in_domain: 88.1\\n      mdkg_ood: 65.8\\n    evidence_generation: false\\n    relevance_to_rsft_docre: >\\n      最直接竞争者。关键差异与讨论：\\n      (1) R1-RE 是句子级 RE，GRPO 成功；我们是文档级 RE，GRPO 失败→RSFT 成功。\\n      句子级 RE 每个 sample 只有 1 个 triple（binary classification），reward variance 天然充足；\\n      文档级 RE 每个 sample 有数十个 triple，F1 score 作为 reward 在 group 内趋于同质化（frac_zero_std→0.8）。\\n      (2) R1-RE 未报告 catastrophic forgetting，进一步支持\\\"句子级简单 reward 可行，文档级需要 CED\\\"的论点。\\n      (3) R1-RE 关注 OOD 泛化，无 evidence 组件；我们关注 evidence-grounded extraction quality。\\n      互补而非直接冲突——R1-RE 证明 RLVR for RE 可行，我们揭示文档级需要额外设计。\\n\\n  - title: \\\"MORE-R1: Guiding LVLM for Multimodal Object-Entity Relation Extraction via Stepwise Reasoning with RL\\\"\\n    authors: Anonymous\\n    year: 2026\\n    venue: arXiv 2603.09478\\n    url: https://arxiv.org/abs/2603.09478\\n    category: rl_for_ie\\n    role: related_method\\n    key_finding: >\\n      多模态 RE 中用 GRPO + Progressive Sample-Mixing Strategy 优化 LVLM 推理能力。\\n      两阶段训练：SFT cold-start + GRPO RL。\\n    relevance_to_rsft_docre: >\\n      跨模态验证 RL for RE 趋势。其 Progressive Sample-Mixing 与我们\\n      RSFT 的 difficulty-aware sampling 思想相通，但在不同模态。\\n\\n  - title: \\\"REAR: Reinforced Reasoning Optimization for Event Argument Extraction with Relation-Aware Support\\\"\\n    authors: Jianwen Luo et al.\\n    year: 2025\\n    venue: EMNLP 2025 Findings\\n    url: https://2025.emnlp.org/program/find_papers/\\n    category: rl_for_ie\\n    role: related_method\\n    key_finding: >\\n      将强化学习推理优化用于事件论元抽取，结合关系感知支持。\\n      不同于 DocRE 但同属 IE 领域的 RL 应用。\\n    relevance_to_rsft_docre: >\\n      验证 RL 在 IE 任务上的有效性趋势。我们的工作扩展到 DocRE + evidence，\\n      且使用 offline RSFT 而非 online RL。\\n\\n  - title: \\\"Adaptive Reinforcement Learning Planning: Harnessing LLMs for Complex Information Extraction\\\"\\n    authors: Zepeng Ding et al.\\n    year: 2024\\n    venue: arXiv 2406.11455\\n    url: https://arxiv.org/abs/2406.11455\\n    category: rl_for_ie\\n    role: background\\n    key_finding: >\\n      将 LLM 顺序抽取建模为 MDP，用 DDQN 训练 decision module\\n      自适应选择实体抽取顺序，提升复杂 IE 性能。\\n    relevance_to_rsft_docre: >\\n      RL for IE 的早期工作。用 RL 优化抽取策略而非模型本身，\\n      与我们 RSFT 直接微调 LLM 的方法路径不同。\\n\\n  - title: \\\"Graph-R1: Towards Agentic GraphRAG Framework via End-to-end Reinforcement Learning\\\"\\n    authors: Haoran Luo et al.\\n    year: 2025\\n    venue: ICML 2026\\n    url: https://arxiv.org/abs/2507.21892\\n    category: rl_for_ie\\n    role: background\\n    key_finding: >\\n      用端到端 RL 优化 GraphRAG agent 的多轮检索-推理循环，\\n      包含 knowledge hypergraph construction（n-ary relation extraction）。\\n    relevance_to_rsft_docre: >\\n      RL + knowledge extraction 的交叉点。Graph-R1 关注 QA 场景下的知识图谱构建，\\n      我们关注 DocRE 的训练优化，应用场景不同。\\n\\n  # === Category 8: Recent LLM-based DocRE Methods ===\\n\\n  - title: \\\"RelPrior: Relation as a Prior - A Novel Paradigm for LLM-based Document-level Relation Extraction\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2511.08143\\n    url: https://arxiv.org/abs/2511.08143\\n    category: llm_docre\\n    role: key_baseline\\n    key_finding: >\\n      用 binary relation 作为先验过滤无关实体对，再用 predefined relation 匹配实体，\\n      避免 LLM 在 DocRE 中被无关实体对分散注意力。\\n      在 DocRED/Re-DocRED 上超越现有纯 LLM-based DocRE 方法。\\n    results:\\n      docred_dev_f1: 47.82\\n      docred_test_f1: 48.34\\n      re_docred_dev_f1: 55.94\\n      re_docred_test_f1: 54.80\\n      backbone: LLaMA3-8B\\n    evidence_generation: false\\n    relevance_to_rsft_docre: >\\n      我们的直接 baseline 之一。RelPrior_LLaMA3-8B 在 DocRED test F1=48.34,\\n      Re-DocRED test F1=54.80。我们的 RSFT 提升显著更优。\\n      RelPrior 是 inference paradigm 创新（两阶段筛选），我们是 training paradigm 创新（RSFT+CED），正交互补。\\n\\n  - title: \\\"LMRC: LLM with Relation Classifier for Document-Level Relation Extraction\\\"\\n    authors: Xingzuo Li, Kehai Chen, Yunfei Long, Min Zhang\\n    year: 2024\\n    venue: arXiv 2408.13889\\n    url: https://arxiv.org/abs/2408.13889\\n    category: llm_docre\\n    role: related_method\\n    key_finding: >\\n      两阶段方法：先用 attention-based classifier 过滤 NA 实体对（RCP），\\n      再用 LLM 在精简候选空间中做多分类（RC）。\\n      注意：LMRC 依赖 BERT-based classifier 作为预筛选，非纯 LLM 方法。\\n    results:\\n      docred_dev_ign_f1: 58.16\\n      docred_dev_f1: 59.97\\n      docred_test_ign_f1: 58.49\\n      docred_test_f1: 60.52\\n      re_docred_test_ign_f1: 74.08\\n      re_docred_test_f1: 74.63\\n      backbone: BERT classifier + LLM\\n    evidence_generation: false\\n    relevance_to_rsft_docre: >\\n      LMRC 在 DocRED test F1=60.52, Re-DocRED test F1=74.63，性能显著高于纯 LLM 方法。\\n      但它依赖 BERT classifier 预筛选，本质上是 hybrid 方法而非纯 LLM generative。\\n      与我们端到端 LLM 生成方式不同——我们通过 RSFT 的 reward-based filtering 隐式解决 class imbalance。\\n\\n  - title: \\\"Ru-LLM: Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: NLPCC 2025\\n    url: https://link.springer.com/chapter/10.1007/978-981-95-3343-5_11\\n    category: llm_docre\\n    role: related_method\\n    key_finding: >\\n      用频繁模式挖掘 + MCTS 搜索逻辑规则，转化为 prompt 约束 LLM 输出，\\n      再用 CoT 验证过滤不满足规则的 triple。\\n      在 DWIE、DocRED、Re-DocRED 上声称超越现有 LLM 方法和规则框架。\\n      具体 F1 未公开获取（Springer 付费墙），但声称超越 AutoRE 等 LLM baseline。\\n    results:\\n      note: \\\"behind Springer paywall; claims SOTA over LLM baselines on DocRED/Re-DocRED/DWIE\\\"\\n    evidence_generation: false\\n    relevance_to_rsft_docre: >\\n      规则约束方式与我们的 CED reward 在 motivation 上相似（都是引入外部知识约束），\\n      但 Ru-LLM 用 inference-time 规则验证（MCTS+CoT），我们用 training-time reward shaping（CED）。\\n      Ru-LLM 的规则是数据集级别的频繁模式，CED 是 instance-level 的 evidence faithfulness。\\n\\n  - title: \\\"GLiDRE: Generalist Lightweight model for Document-level Relation Extraction\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2508.00757\\n    url: https://arxiv.org/abs/2508.00757\\n    category: llm_docre\\n    role: background\\n    key_finding: >\\n      基于 dual-encoder 的轻量级零/少样本 DocRE 模型，\\n      预训练于 136K 文档的大规模 RE 数据。\\n      fully supervised Re-DocRED test F1=77.83，但这是 encoder-based 非 LLM generative。\\n      zero-shot Re-DocRED test F1=17.32（超越 LLaMA 3.3 70B 和 Mistral-Small 24B）。\\n    results:\\n      re_docred_dev_f1: 77.76\\n      re_docred_test_f1: 77.83\\n      re_docred_zero_shot_test_f1: 17.32\\n      fredo_in_domain_1doc_f1: 13.00\\n      fredo_in_domain_3doc_f1: 15.71\\n      backbone: \\\"dual-encoder (few hundred M params)\\\"\\n    evidence_generation: false\\n    relevance_to_rsft_docre: >\\n      不同范式（encoder-based vs LLM generative）。GLiDRE 的 fully supervised F1=77.83\\n      远超 LLM-based 方法（RelPrior 54.80），但依赖大规模预训练数据和 encoder 架构。\\n      与我们不直接可比——我们关注 LLM generative 范式下的训练优化。\\n\\n  - title: \\\"AutoRE: Document-Level Relation Extraction with Large Language Models\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: arXiv 2403.14888\\n    url: https://arxiv.org/abs/2403.14888\\n    category: llm_docre\\n    role: background\\n    key_finding: >\\n      RHF（Relation-Head-Facts）范式用 Mistral-7B + QLoRA 做端到端 DocRE。\\n      关键设计：先抽 relation，再抽 head entity，最后抽 fact triple。\\n    results:\\n      re_docred_dev_f1_mistral: 53.01\\n      re_docred_test_f1_mistral: 51.91\\n      re_docred_dev_f1_vicuna: 54.29\\n      re_docred_test_f1_vicuna: 53.84\\n      docred_dev_f1_llama3: 45.76\\n      docred_test_f1_llama3: 45.96\\n      re_docred_dev_f1_llama3: 52.28\\n      re_docred_test_f1_llama3: 51.97\\n      backbone: \\\"Mistral-7B / Vicuna-7B / LLaMA3-8B (QLoRA)\\\"\\n    evidence_generation: false\\n    relevance_to_rsft_docre: >\\n      QLoRA fine-tuning for DocRE 的先例。AutoRE_LLaMA3-8B 在 Re-DocRED test F1=51.97,\\n      DocRED test F1=45.96。我们的 SFT baseline 与之类似，\\n      RSFT 在此基础上引入 reward-guided sample selection 进一步提升。\\n\\n  # === Category 9: Evidence Generation & Task Performance Trade-off ===\\n  # (NEW - 2026-05-15 evidence generation survey)\\n\\n  - title: \\\"Mind Your Step (by Step): Chain-of-Thought can Reduce Performance on Tasks where Thinking Makes Humans Worse\\\"\\n    authors: Sprague et al.\\n    year: 2024\\n    venue: NeurIPS 2024\\n    url: https://arxiv.org/abs/2410.21333\\n    category: evidence_generation_tradeoff\\n    role: key_evidence\\n    key_finding: >\\n      CoT 在某些任务上降低性能高达 36.3%（o1-preview vs GPT-4o）。\\n      显式推理步骤引入 error accumulation，且模型可能 overfit 到解释格式而非任务结构。\\n      隐式推理（hidden activations）在分布偏移下优于显式 token-level 推理。\\n    relevance_to_evidence_tradeoff: >\\n      直接支持我们的核心发现：要求模型同时生成 evidence sentences 是一种\\\"显式推理\\\"，\\n      会对主任务（RE）产生性能代价（~8pp F1 下降）。\\n      Related Work 引用点：evidence generation 作为 structured explanation，\\n      与 CoT 共享\\\"显式推理降低主任务性能\\\"的普遍模式。\\n\\n  - title: \\\"Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion\\\"\\n    authors: Xie et al. (Google Research)\\n    year: 2022\\n    venue: ACL Findings 2022\\n    url: https://arxiv.org/abs/2106.08657\\n    category: evidence_generation_tradeoff\\n    role: closest_docre_precedent\\n    key_finding: >\\n      Joint 训练 RE + evidence extraction，关键创新在 inference-stage fusion：\\n      分别在 extracted evidence 和 full document 上做 RE 预测再通过 blending layer 融合。\\n      DocRED 上提升 1.37 Ign F1。Silver evidence labels（启发式规则构建）即可提升 RE 性能。\\n    relevance_to_evidence_tradeoff: >\\n      最直接的 DocRE + evidence 先例。EIDER 的核心洞察是 evidence 需要 inference-stage 融合\\n      而非 joint generation——暗示 joint generation 会引入 noise。\\n      我们的 CED reranker 是 LLM-era 版本的 inference-stage fusion：\\n      先生成多个候选（含 evidence），再用 NLI 在推理阶段选最佳。\\n      Related Work 引用点：encoder-based DocRE 中 evidence 的使用方式，与我们 generative 范式的关键差异。\\n\\n  - title: \\\"Exploring the Trade-off Between Model Performance and Explanation Plausibility of Text Classifiers Using Human Rationales\\\"\\n    authors: Resck, Raimundo, Poco\\n    year: 2024\\n    venue: NAACL Findings 2024\\n    url: https://arxiv.org/abs/2404.03098\\n    category: evidence_generation_tradeoff\\n    role: formal_framework\\n    key_finding: >\\n      用 multi-objective optimization 探索 performance vs explanation plausibility 的 Pareto frontier。\\n      引入 rationale 约束创建 contrastive loss，证实加入 rationale supervision 会降低主任务性能，\\n      但存在 Pareto optimal 解平衡两者。\\n    relevance_to_evidence_tradeoff: >\\n      提供了 performance-explainability trade-off 的形式化框架。\\n      我们的 evidence-grounded RE 降 8pp 正是 Pareto frontier 上的一个点。\\n      CED reranker 的效果可解读为：将系统从 evidence-constrained 点推向 Pareto frontier，\\n      在几乎不牺牲 evidence quality（evi_f1=0.8188）的前提下恢复 RE 性能。\\n      Related Work 引用点：evidence generation 的 performance cost 有理论依据。\\n\\n  - title: \\\"The Decreasing Value of Chain of Thought in Prompting\\\"\\n    authors: Meincke, Mollick, Mollick, Shapiro\\n    year: 2025\\n    venue: Wharton Generative AI Labs Technical Report (SSRN)\\n    url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5285532\\n    category: evidence_generation_tradeoff\\n    role: empirical_support\\n    key_finding: >\\n      现代 reasoning models 上 CoT 收益微弱（4-13%），但 latency 增加 35-600%。\\n      更强的模型从显式推理中受益越少。CoT 可能在 easy questions 上引入 errors\\n      （variability 增加导致原本正确的被改错）。\\n    relevance_to_evidence_tradeoff: >\\n      支持\\\"更强的 SFT 模型不需要在生成时显式输出 evidence\\\"的论点。\\n      我们的 evidence-only SFT 的性能下降符合\\\"显式推理的边际收益递减\\\"模式。\\n      Related Work 引用点：evidence generation 的 accuracy cost 不是 DocRE-specific，而是 LLM 的普遍趋势。\\n\\n  # === Category 10: Negative Transfer in Multi-task / Auxiliary-task Learning ===\\n\\n  - title: \\\"ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning\\\"\\n    authors: Jiang, Chen et al.\\n    year: 2023\\n    venue: NeurIPS 2023\\n    url: https://arxiv.org/abs/2301.12618\\n    category: negative_transfer\\n    role: theoretical_framework\\n    key_finding: >\\n      辅助任务常导致 negative transfer，根因不仅是 gradient conflict 还有 auxiliary-target\\n      generalization gap。ForkMerge 周期性 fork 模型为多分支，搜索最优 task weights，\\n      动态 merge 过滤有害 task-parameter updates。在多个 benchmark 上减少 negative transfer。\\n    relevance_to_evidence_tradeoff: >\\n      Evidence generation 作为 auxiliary task 对 RE 的 negative transfer 可用此框架解释：\\n      evidence 和 RE 的 gradient 方向不完全对齐，joint training 时 evidence 任务\\\"拖累\\\"RE。\\n      CED reranker 本质上是将 evidence quality 从 training-time joint objective 解耦到\\n      inference-time verification，避免了 training-time 的 negative transfer。\\n      Related Work 引用点：auxiliary task 导致主任务性能下降的一般性理论。\\n\\n  # === Category 11: Faithfulness vs Accuracy / Correctness Trade-off ===\\n\\n  - title: \\\"Correctness is not Faithfulness in RAG Attributions\\\"\\n    authors: Wallat, Heuss, de Rijke, Anand\\n    year: 2024\\n    venue: SIGIR 2025\\n    url: https://arxiv.org/abs/2412.18004\\n    category: faithfulness_accuracy_tradeoff\\n    role: key_conceptual_framework\\n    key_finding: >\\n      Correctness 和 faithfulness 是独立维度，可能冲突。高达 57% 的 citations 是\\n      post-rationalized（事后编造而非真实依据）。Unfaithful attributions 可能 factually correct，\\n      但 foster misguided trust。必须同时检查 correctness 和 faithfulness。\\n    relevance_to_evidence_tradeoff: >\\n      直接相关。我们的 evidence-grounded RE 试图让模型输出 faithful evidence，\\n      但这与 relation correctness 产生张力（rel_f1 降 8pp）。\\n      CED reranker 通过 NLI verification 确保 evidence 是 faithful 的（非 post-rationalized），\\n      同时不牺牲 RE accuracy。\\n      Related Work 引用点：correctness-faithfulness 分离的概念框架。\\n\\n  - title: \\\"Evaluating Correctness and Faithfulness of Instruction-Following Models for Question Answering\\\"\\n    authors: Adlakha, BehnamGhader, Lu, Meade, Reddy\\n    year: 2024\\n    venue: TACL 2024\\n    url: https://arxiv.org/abs/2307.16877\\n    category: faithfulness_accuracy_tradeoff\\n    role: evaluation_framework\\n    key_finding: >\\n      Instruction-following LLMs 在 correctness 上表现可比 fine-tuned models，\\n      但 faithfulness 普遍较差——模型会 hallucinate 而非忠实于提供的 evidence。\\n      传统 metrics 对 correctness 和 faithfulness 的评估均有缺陷。\\n    relevance_to_evidence_tradeoff: >\\n      解释了为什么 joint evidence+RE 生成性能差——模型在同时优化 correctness\\n      和 faithfulness 时，两个目标存在张力。单纯要求模型\\\"同时输出正确 triples 和\\n      faithful evidence\\\"是 multi-objective optimization 问题。\\n      Related Work 引用点：correctness vs faithfulness 评估方法论。\\n\\n  - title: \\\"Towards Faithful Model Explanation in NLP: A Survey\\\"\\n    authors: Lyu, Havaldar, Stein et al.\\n    year: 2024\\n    venue: Computational Linguistics (MIT Press)\\n    url: https://aclanthology.org/2024.cl-2.6/\\n    category: faithfulness_accuracy_tradeoff\\n    role: comprehensive_survey\\n    key_finding: >\\n      系统综述 NLP 中 faithful explanation 的定义、评估和生成方法。\\n      识别了 faithfulness-performance trade-off 作为核心挑战：\\n      更 faithful 的解释不一定更有用，更有用的解释不一定 faithful。\\n      提出未来方向包括 multi-objective optimization 和 post-hoc verification。\\n    relevance_to_evidence_tradeoff: >\\n      权威综述为我们的 evidence generation trade-off 提供广泛文献背景。\\n      我们的 CED reranker 正是该综述建议的\\\"post-hoc verification\\\"方向的具体实例。\\n      Related Work 引用点：faithfulness 研究的全景综述，定位我们的工作。\\n\\n  # === Category 12: Reranking / Verification as Bridge ===\\n\\n  - title: \\\"Genie: Achieving Human Parity in Content-Grounded Datasets Generation\\\"\\n    authors: Yehudai, Carmeli, Mass et al.\\n    year: 2024\\n    venue: ICLR 2024\\n    url: https://arxiv.org/abs/2401.14367\\n    category: reranking_verification_bridge\\n    role: methodological_precedent\\n    key_finding: >\\n      三阶段流程：Content Preparation → Generation → NLI-based Filtering。\\n      用 fine-tuned T5-11B NLI 模型判断生成内容是否 entailed by source（faithfulness 检验），\\n      过滤不 faithful 的生成。在 LFQA、摘要、IE 上达到 human parity。\\n    relevance_to_evidence_tradeoff: >\\n      方法论上最接近我们的 CED reranker——都是用 NLI verification 作为 post-hoc filter/reranker，\\n      在不牺牲主任务质量的前提下确保 grounding quality。\\n      GENIE 验证了 NLI-based filtering 在内容生成中的有效性。\\n      关键差异：GENIE 是 data generation pipeline 的过滤，我们是 inference-time reranking。\\n      Related Work 引用点：NLI-based verification 作为 bridge 的成功先例。\\n\", \"total_chars\": 29337, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "8a3ff0c2-cb43-4f82-b34a-7a3173343e48",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml\\\", \\\"content\\\": \\\"# Literature Map for faith-evidence-ie (FREIGE)\\\\n# Focus: CED-as-training-stabilizer (D024) + RSFT for DocRE\\\\n# Updated: 2026-05-15 (W3 reviewer gap fill + evidence generation trade-off survey)\\\\n\\\\npapers:\\\\n\\\\n  # === Category 1: Reward Diversity / Reward Shaping for RL Stability ===\\\\n\\\\n  - title: \\\\\\\"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization\\\\\\\"\\\\n    authors: NVIDIA Labs\\\\n    year: 2025\\\\n    venue: ICML 2026\\\\n    url: https://arxiv.org/abs/2601.05242\\\\n    category: reward_diversity\\\\n    role: closest_prior_work\\\\n    key_finding: >\\\\n      直接将 GRPO 应用于多 reward 组合时，不同 rollout 的 reward 组合在归一化后 collapse 为相同 advantage 值，\\\\n      降低训练信号分辨率导致收敛失败。GDPO 对每个 reward 独立做 group-wise normalization 再聚合，\\\\n      保留多 reward 的相对差异，显著提升训练稳定性。\\\\n    relevance_to_ced_stabilizer: >\\\\n      最直接相关。CED reward 本质上引入了独立于 extraction F1 的 reward 维度（evidence quality），\\\\n      GDPO 的理论分析解释了为什么多维 reward 比单一 reward 更稳定——独立 reward 维度防止 advantage collapse。\\\\n      但 GDPO 是方法论贡献，CED 是 task-specific reward 设计自然具备了这一特性。\\\\n\\\\n  - title: \\\\\\\"DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of LLMs\\\\\\\"\\\\n    authors: Xiwen Chen et al.\\\\n    year: 2025\\\\n    venue: arXiv 2505.09655\\\\n    url: https://arxiv.org/abs/2505.09655\\\\n    category: reward_diversity\\\\n    role: related_method\\\\n    key_finding: >\\\\n      GRPO 的标量 reward 无法区分语义多样但得分相同的输出（diversity-quality inconsistency）。\\\\n      DRA 用子模互信息（SMI）对 reward 加权，给多样性高的 completion 更大权重，\\\\n      等价于 Inverse Propensity Scoring 去偏，防止 policy 坍缩到先验模式。\\\\n    relevance_to_ced_stabilizer: >\\\\n      DRA 通过后处理 reward 注入多样性信号；CED 的 reward 本身就内含对比结构自然提供 diversity 信号。\\\\n      机制互补但来源不同——CED 是 reward design 层面，DRA 是 optimization 层面。\\\\n\\\\n  - title: \\\\\\\"Shrinking the Variance: Shrinkage Baselines for RL with Verifiable Rewards\\\\\\\"\\\\n    authors: Guanning Zeng et al.\\\\n    year: 2025\\\\n    venue: arXiv 2511.03710\\\\n    url: https://arxiv.org/abs/2511.03710\\\\n    category: reward_diversity\\\\n    role: theoretical_support\\\\n    key_finding: >\\\\n      RLVR 中 per-prompt 均值 baseline 在低 generation 数下估计不准导致高 variance 梯度。\\\\n      用 James-Stein shrinkage 混合 per-prompt 和 cross-prompt 均值，\\\\n      构造可证明更低 variance 的 policy gradient estimator。\\\\n    relevance_to_ced_stabilizer: >\\\\n      理论支持：reward variance 对 gradient estimation 质量至关重要。\\\\n      CED 的额外 reward 维度提供更丰富的 per-group variance，间接起到 variance 维持效果。\\\\n\\\\n  - title: \\\\\\\"Reward Shaping to Mitigate Reward Hacking in RLHF\\\\\\\"\\\\n    authors: Anonymous\\\\n    year: 2025\\\\n    venue: arXiv 2502.18770\\\\n    url: https://arxiv.org/abs/2502.18770\\\\n    category: reward_diversity\\\\n    role: background\\\\n    key_finding: >\\\\n      RL reward 应有界且先快速增长后缓慢收敛。系统研究 reward shaping 原则，\\\\n      好的 reward 形状能抑制 reward hacking 并提升训练稳定性。\\\\n    relevance_to_ced_stabilizer: >\\\\n      CED reward 的 0-1 对比判别结构天然满足有界性，\\\\n      且 evidence quality 的渐进提升符合\\\\\\\"先快后慢\\\\\\\"的 reward shaping 原则。\\\\n\\\\n  # === Category 2: Mode Collapse Prevention in GRPO/RLHF ===\\\\n\\\\n  - title: \\\\\\\"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\\\\\\\"\\\\n    authors: ByteDance Seed, Tsinghua AIR\\\\n    year: 2025\\\\n    venue: NeurIPS 2025\\\\n    url: https://arxiv.org/abs/2503.14476\\\\n    category: mode_collapse_prevention\\\\n    role: key_baseline\\\\n    key_finding: >\\\\n      Naive GRPO 存在 entropy collapse（policy 熵快速下降→输出同质化）。\\\\n      根因：clipping 不对称性——概率 0.01 的 token 最多增到 0.012，而概率 0.9 的 token 可达 1.08，\\\\n      低概率 token 难以增长，抑制探索。DAPO 提出 Clip-Higher（εhigh=0.28 > εlow=0.2）\\\\n      为低概率 token 留更大增长空间，加 Dynamic Sampling 过滤 accuracy=0 或 1 的 prompt\\\\n      （这些 prompt 产生零梯度，降低有效 batch size）。在 AIME 2024 达 50 分超越 DeepSeek-R1-Zero。\\\\n    relevance_to_ced_stabilizer: >\\\\n      DAPO 从 optimization 技巧角度解决 entropy collapse。CED reward 从 reward design 层面\\\\n      防止 mode collapse——evidence quality 维度确保 reward 组内有足够 variance，\\\\n      不会出现 all-same-reward 的零梯度 prompt。DAPO 的 Dynamic Sampling 过滤 accuracy=0/1 prompt\\\\n      与我们观察到的 frac_zero_std→0.8 现象本质相同：extraction-only reward 下大量 prompt\\\\n      产生零 advantage，CED 从源头（reward 设计）而非后处理（过滤）解决这个问题。\\\\n\\\\n  - title: \\\\\\\"Dr. GRPO: Removing Optimization Bias in GRPO\\\\\\\"\\\\n    authors: Liu et al.\\\\n    year: 2025\\\\n    venue: COLM 2025\\\\n    url: https://arxiv.org/abs/2503.20783\\\\n    category: mode_collapse_prevention\\\\n    role: related_analysis\\\\n    key_finding: >\\\\n      GRPO 的 std 归一化引入两个 bias：(1) difficulty bias——std(r) 归一化对低 variance 组\\\\n      （全对/全错）给予过高 advantage 权重，trivial question 主导训练信号；\\\\n      (2) length bias——per-token loss 的 1/|o_i| 项使长的错误回答被 under-penalize。\\\\n      当 std(r)→0 时 advantage 爆炸或未定义，梯度数值不稳定。\\\\n      Dr. GRPO 移除 std 归一化，用无偏 Monte Carlo advantage：Ã = R(q,o_i) - mean(R)。\\\\n    relevance_to_ced_stabilizer: >\\\\n      与我们的实验发现高度一致：extraction-only reward 下 frac_zero_std→0.8 正是\\\\n      Dr. GRPO 分析的 difficulty bias 极端情况——大量 prompt 的所有 rollout 得到相同 F1，\\\\n      std→0 导致 advantage 异常。CED 通过增加 reward 维度天然维持 reward_std>0，\\\\n      从 reward 设计而非算法修改角度避免了 Dr. GRPO 发现的 bias。\\\\n\\\\n  - title: \\\\\\\"GVPO: Group Variance Policy Optimization for LLM Post-Training\\\\\\\"\\\\n    authors: Anonymous\\\\n    year: 2025\\\\n    venue: NeurIPS 2025\\\\n    url: https://arxiv.org/abs/2504.19599\\\\n    category: mode_collapse_prevention\\\\n    role: alternative_framework\\\\n    key_finding: >\\\\n      将 KL 约束 reward 最大化的解析解直接嵌入梯度权重，\\\\n      variance 项自然平衡 exploration 与 exploitation，维持适度 entropy。\\\\n    relevance_to_ced_stabilizer: >\\\\n      GVPO 的 variance 项机制与 CED 维持 reward variance 的效果功能类似，\\\\n      但 GVPO 是算法层面 implicit regularization，CED 是 reward 层面 explicit structure。\\\\n\\\\n  - title: \\\\\\\"REINFORCE++: Stabilizing Critic-Free Policy Optimization with Global Advantage Normalization\\\\\\\"\\\\n    authors: Jian Hu et al.\\\\n    year: 2025\\\\n    venue: arXiv 2501.03262\\\\n    url: https://arxiv.org/abs/2501.03262\\\\n    category: mode_collapse_prevention\\\\n    role: related_method\\\\n    key_finding: >\\\\n      Prompt-level (local) advantage normalization 导致不准确估计和过拟合。\\\\n      Global batch normalization 提供更稳定、理论无偏的 gradient estimator。\\\\n    relevance_to_ced_stabilizer: >\\\\n      解决 local normalization 的 variance 问题；CED 从 reward 端增加 variance 来源。\\\\n      两者在不同层面解决同一问题：防止 gradient signal 消失。\\\\n\\\\n  - title: \\\\\\\"DiverseGRPO: Mitigating Mode Collapse in Image Generation via Diversity-Aware GRPO\\\\\\\"\\\\n    authors: Henglin Liu et al.\\\\n    year: 2025\\\\n    venue: arXiv 2512.21514\\\\n    url: https://arxiv.org/abs/2512.21514\\\\n    category: mode_collapse_prevention\\\\n    role: parallel_work\\\\n    key_finding: >\\\\n      图像生成中 GRPO 后期输出同质化。distributional reward modeling（谱聚类+exploratory reward）\\\\n      和 structure-aware regularization 实现 13-18% 语义多样性提升。\\\\n    relevance_to_ced_stabilizer: >\\\\n      跨域验证了 GRPO mode collapse 的普遍性，distributional reward 思路与 CED 精神相近——\\\\n      都是通过 reward 层面结构化信号维持输出多样性。\\\\n\\\\n  - title: \\\\\\\"Why GRPO Needs Normalization: A Local-Curvature Perspective on Adaptive Gradients\\\\\\\"\\\\n    authors: Anonymous\\\\n    year: 2025\\\\n    venue: arXiv 2601.23135\\\\n    url: https://arxiv.org/abs/2601.23135\\\\n    category: mode_collapse_prevention\\\\n    role: theoretical_support\\\\n    key_finding: >\\\\n      GRPO 的 reward_std 归一化在温和条件下提供严格优于未归一化 REINFORCE 的收敛速率，\\\\n      收益由 prompt 间平均 reward std 刻画。\\\\n    relevance_to_ced_stabilizer: >\\\\n      直接理论支撑：reward_std 越大收敛越好。CED 通过 evidence quality 维度维持高 reward_std，\\\\n      从该理论看 CED 的稳定性优势是 reward_std 维持带来的收敛速率优势。\\\\n\\\\n  # === Category 3: Contrastive Rewards in RL ===\\\\n\\\\n  - title: \\\\\\\"Improving Reinforcement Learning from Human Feedback Using Contrastive Rewards\\\\\\\"\\\\n    authors: Shen, Zhang et al.\\\\n    year: 2024\\\\n    venue: arXiv 2403.07708\\\\n    url: https://arxiv.org/abs/2403.07708\\\\n    category: contrastive_reward\\\\n    role: closest_contrastive_precedent\\\\n    key_finding: >\\\\n      两步机制：(1) 离线采样 baseline response；(2) 用 baseline 计算 contrastive reward\\\\n      作为 PPO 的 penalty 项。效果：惩罚 reward uncertainty、根据任务难度自适应校准、\\\\n      减少 PPO 中的 variance。在 TL;DR 和 HH-RLHF 上持续优于标准 RLHF。\\\\n    relevance_to_ced_stabilizer: >\\\\n      最接近的对比 reward 先例。关键差异：(1) 它是对 learned RM 输出的后处理对比，\\\\n      CED 是 reward function 本身就是对比判别（evidence vs. corrupted evidence）；\\\\n      (2) 它在 PPO 中验证，CED 在 GRPO 中验证；\\\\n      (3) 它是 domain-agnostic penalty，CED 是 task-specific faithfulness signal。\\\\n      stabilizing 机制相通但实现路径根本不同。\\\\n\\\\n  - title: \\\\\\\"Improving Discriminative Capability of Reward Models in RLHF Using Contrastive Learning\\\\\\\"\\\\n    authors: Anonymous\\\\n    year: 2024\\\\n    venue: EMNLP 2024\\\\n    url: https://aclanthology.org/2024.emnlp-main.852/\\\\n    category: contrastive_reward\\\\n    role: related_method\\\\n    key_finding: >\\\\n      无监督对比损失训练 reward model 充分捕捉对比数据区分度，\\\\n      带来更稳定的 PPO 训练 return 和 reward。\\\\n    relevance_to_ced_stabilizer: >\\\\n      验证对比训练 reward model → 更稳定 RL 训练链条。CED 不是对比训练 reward model，\\\\n      而是 reward function 本身就是对比判别，但 stabilizing 机制相通。\\\\n\\\\n  - title: \\\\\\\"Contrastive Preference Learning: Learning from Human Feedback without RL\\\\\\\"\\\\n    authors: Anonymous\\\\n    year: 2024\\\\n    venue: ICLR 2025\\\\n    url: https://openreview.net/forum?id=iX1RjVQODj\\\\n    category: contrastive_reward\\\\n    role: background\\\\n    key_finding: >\\\\n      将 preference learning 重新表述为对比学习问题，无需显式 RL 即可从人类反馈中学习。\\\\n    relevance_to_ced_stabilizer: >\\\\n      对比框架在 preference alignment 中的通用性。CED 可被视为 task-specific contrastive preference signal。\\\\n\\\\n  # === Category 4: Evidence-Based Rewards in IE/NLP ===\\\\n\\\\n  - title: \\\\\\\"Drift: Enhancing LLM Faithfulness in Rationale Generation\\\\\\\"\\\\n    authors: Anonymous\\\\n    year: 2025\\\\n    venue: ACL 2025\\\\n    url: https://aclanthology.org/2025.acl-long.340.pdf\\\\n    category: evidence_reward\\\\n    role: related_method\\\\n    key_finding: >\\\\n      用 faithfulness reward 引导 LLM 生成更可靠的 rationale，提升 CoT 推理事实一致性。\\\\n    relevance_to_ced_stabilizer: >\\\\n      Faithfulness reward 用于生成质量的先例。CED 中 evidence discrimination\\\\n      本质上也是 faithfulness 信号——判断证据是否忠实支持抽取结果。\\\\n\\\\n  - title: \\\\\\\"Fine-Grained NLI-Based Faithfulness Evaluation for Diverse Summarisation Tasks (INFUSE)\\\\\\\"\\\\n    authors: Anonymous\\\\n    year: 2024\\\\n    venue: EACL 2024\\\\n    url: https://aclanthology.org/2024.eacl-long.102/\\\\n    category: evidence_reward\\\\n    role: background\\\\n    key_finding: >\\\\n      变长前提+简化假设的细粒度 NLI faithfulness 评估，超越传统 NLI 在多任务摘要上的表现。\\\\n    relevance_to_ced_stabilizer: >\\\\n      NLI 作为 faithfulness 评估工具的进展。CED 中 NLI 组件用于判断 evidence 对 triple 的支持度。\\\\n\\\\n  - title: \\\\\\\"Enhancing Cross-Evidence Reasoning Graph for Document-Level Relation Extraction\\\\\\\"\\\\n    authors: Anonymous\\\\n    year: 2024\\\\n    venue: PMC/Bioinformatics 2024\\\\n    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11232587/\\\\n    category: evidence_reward\\\\n    role: background\\\\n    key_finding: >\\\\n      文档级关系抽取中用 cross-evidence reasoning graph 增强跨证据推理。\\\\n    relevance_to_ced_stabilizer: >\\\\n      DocRE 中 evidence 的重要性。但用 evidence 作为模型输入特征，\\\\n      我们用 evidence quality 作为 RL reward 信号——定位根本不同。\\\\n\\\\n  # === Category 5: Multi-Objective RL for Text Generation ===\\\\n\\\\n  - title: \\\\\\\"Confronting Reward Model Overoptimization with Constrained RLHF\\\\\\\"\\\\n    authors: Anonymous\\\\n    year: 2025\\\\n    venue: OpenReview\\\\n    url: https://openreview.net/forum?id=gkfUvn0fLU\\\\n    category: multi_objective_rl\\\\n    role: related_analysis\\\\n    key_finding: >\\\\n      多组件 RM 的 overoptimization 研究。component RM 间的相关性显著影响 overoptimization 临界点，\\\\n      用 constrained MDP 防止超出适当边界。\\\\n    relevance_to_ced_stabilizer: >\\\\n      CED 引入了与 extraction F1 低相关的 reward component（evidence quality），\\\\n      根据该论文分析低相关多组件 reward 更不易 overoptimize，\\\\n      可能是 CED 稳定性的另一个理论解释角度。\\\\n\\\\n  - title: \\\\\\\"On-Policy RL with Optimal Reward Baseline\\\\\\\"\\\\n    authors: Anonymous\\\\n    year: 2025\\\\n    venue: arXiv 2505.23585\\\\n    url: https://arxiv.org/abs/2505.23585\\\\n    category: multi_objective_rl\\\\n    role: theoretical_support\\\\n    key_finding: >\\\\n      Optimal baseline 一致性地实现更高训练 reward 和更高 entropy，\\\\n      有效稳定训练并促进更多样的 policy exploration。\\\\n    relevance_to_ced_stabilizer: >\\\\n      CED reward 的多维特性可能起到类似 optimal baseline 效果——\\\\n      evidence quality 维度为 advantage estimation 提供更丰富的参照信号。\\\\n\\\\n  # === Category 6: RSFT Methodology & Theory ===\\\\n\\\\n  - title: \\\\\\\"A Minimalist Approach to LLM Reasoning: from Rejection Sampling to Reinforce\\\\\\\"\\\\n    authors: Xiao et al.\\\\n    year: 2025\\\\n    venue: arXiv 2504.11343\\\\n    url: https://arxiv.org/abs/2504.11343\\\\n    category: rsft_methodology\\\\n    role: key_theoretical_support\\\\n    key_finding: >\\\\n      RAFT（简单 rejection sampling baseline）在数学推理上与 GRPO/PPO 表现相当。\\\\n      消融实验表明 GRPO 的主要优势来自丢弃全错 prompt 而非 reward normalization。\\\\n      提出 Reinforce-Rej，在 RAFT 基础上过滤全对和全错 sample。\\\\n      关键洞察：GRPO 和 RAFT 的核心区别在于负样本处理——GRPO 混合正负样本训练，\\\\n      RAFT 只用正样本，但 RAFT 仍能达到相当性能，说明 rejection sampling 的简单性被低估了。\\\\n    relevance_to_rsft_docre: >\\\\n      直接支持我们的设计选择：(1) RSFT 在 DocRE 上成功而 GRPO 失败，\\\\n      与该论文发现一致——rejection sampling 的 offline 特性天然避免了 catastrophic forgetting；\\\\n      (2) GRPO 主要优势来自过滤全错 prompt，这与我们 RSFT 的 reward-based filtering 机制相同；\\\\n      (3) DocRE structured output 比 math reasoning 更难用 online RL 优化，\\\\n      强化了 offline RSFT 的合理性。\\\\n\\\\n  - title: \\\\\\\"Beyond Rejection Sampling: Trajectory Fusion for Scaling Mathematical Reasoning (TrajFusion)\\\\\\\"\\\\n    authors: Jie Deng et al.\\\\n    year: 2026\\\\n    venue: arXiv 2602.04391\\\\n    url: https://arxiv.org/abs/2602.04391\\\\n    category: rsft_methodology\\\\n    role: method_component\\\\n    key_finding: >\\\\n      传统 RSFT 只用正确轨迹，丢弃错误轨迹。TrajFusion 将错误和正确轨迹交替拼接，\\\\n      显式建模试错推理过程，在困难数学问题上显著超越标准 RFT。\\\\n    relevance_to_rsft_docre: >\\\\n      Future work 方向：可考虑在 DocRE RSFT 中融合失败样本的信息。\\\\n      但 DocRE 的结构化输出（JSON triple）不同于 math 的 chain-of-thought，\\\\n      融合方式需要重新设计。\\\\n\\\\n  - title: \\\\\\\"Rejection Sampling Based Fine Tuning Secretly Performs PPO\\\\\\\"\\\\n    authors: Anonymous\\\\n    year: 2025\\\\n    venue: ICML 2025\\\\n    url: https://openreview.net/forum?id=yQ2UivKlir\\\\n    category: rsft_methodology\\\\n    role: theoretical_support\\\\n    key_finding: >\\\\n      建立 RSFT 与 PPO 之间的理论联系：rejection sampling fine-tuning\\\\n      在特定条件下隐式执行 PPO with marginal KL constraints。\\\\n    relevance_to_rsft_docre: >\\\\n      为 RSFT 的有效性提供理论解释。我们的 RSFT 成功可被视为\\\\n      隐式执行了 constrained policy optimization，\\\\n      避免了显式 GRPO 在 structured output 上的不稳定性。\\\\n\\\\n  # === Category 7: RL for Information Extraction ===\\\\n\\\\n  - title: \\\\\\\"R1-RE: Cross-Domain Relation Extraction with RLVR\\\\\\\"\\\\n    authors: Runpeng Dai, Tong Zheng et al.\\\\n    year: 2025\\\\n    venue: arXiv 2507.04642\\\\n    url: https://arxiv.org/abs/2507.04642\\\\n    category: rl_for_ie\\\\n    role: direct_competitor\\\\n    key_finding: >\\\\n      首个将 RLVR（GRPO + verifiable reward）用于关系抽取的框架。\\\\n      将 RE 重构为推理任务，R1-RE-7B 在跨域 OOD 准确率约 70%，媲美 GPT-4o。\\\\n      Reward 设计：format reward (+1/-3) + metric reward (+2/-1.5)，先验证格式再加准确度。\\\\n      triplet extraction 用 F1-based reward（entity weight=1, triplet weight=3）。\\\\n      未报告 catastrophic forgetting——GRPO 训练后在 MATH-500/IFEval/GPQA 上性能不降反升，\\\\n      说明句子级 RE 的简单 reward 结构足以稳定 GRPO 训练。\\\\n    results:\\\\n      sem2010_in_domain: 91.8\\\\n      sem2010_ood: 66.5\\\\n      mdkg_in_domain: 88.1\\\\n      mdkg_ood: 65.8\\\\n    evidence_generation: false\\\\n    relevance_to_rsft_docre: >\\\\n      最直接竞争者。关键差异与讨论：\\\\n      (1) R1-RE 是句子级 RE，GRPO 成功；我们是文档级 RE，GRPO 失败→RSFT 成功。\\\\n      句子级 RE 每个 sample 只有 1 个 triple（binary classification），reward variance 天然充足；\\\\n      文档级 RE 每个 sample 有数十个 triple，F1 score 作为 reward 在 group 内趋于同质化（frac_zero_std→0.8）。\\\\n      (2) R1-RE 未报告 catastrophic forgetting，进一步支持\\\\\\\"句子级简单 reward 可行，文档级需要 CED\\\\\\\"的论点。\\\\n      (3) R1-RE 关注 OOD 泛化，无 evidence 组件；我们关注 evidence-grounded extraction quality。\\\\n      互补而非直接冲突——R1-RE 证明 RLVR for RE 可行，我们揭示文档级需要额外设计。\\\\n\\\\n  - title: \\\\\\\"MORE-R1: Guiding LVLM for Multimodal Object-Entity Relation Extraction via Stepwise Reasoning with RL\\\\\\\"\\\\n    authors: Anonymous\\\\n    year: 2026\\\\n    venue: arXiv 2603.09478\\\\n    url: https://arxiv.org/abs/2603.09478\\\\n    category: rl_for_ie\\\\n    role: related_method\\\\n    key_finding: >\\\\n      多模态 RE 中用 GRPO + Progressive Sample-Mixing Strategy 优化 LVLM 推理能力。\\\\n      两阶段训练：SFT cold-start + GRPO RL。\\\\n    relevance_to_rsft_docre: >\\\\n      跨模态验证 RL for RE 趋势。其 Progressive Sample-Mixing 与我们\\\\n      RSFT 的 difficulty-aware sampling 思想相通，但在不同模态。\\\\n\\\\n  - title: \\\\\\\"REAR: Reinforced Reasoning Optimization for Event Argument Extraction with Relation-Aware Support\\\\\\\"\\\\n    authors: Jianwen Luo et al.\\\\n    year: 2025\\\\n    venue: EMNLP 2025 Findings\\\\n    url: https://2025.emnlp.org/program/find_papers/\\\\n    category: rl_for_ie\\\\n    role: related_method\\\\n    key_finding: >\\\\n      将强化学习推理优化用于事件论元抽取，结合关系感知支持。\\\\n      不同于 DocRE 但同属 IE 领域的 RL 应用。\\\\n    relevance_to_rsft_docre: >\\\\n      验证 RL 在 IE 任务上的有效性趋势。我们的工作扩展到 DocRE + evidence，\\\\n      且使用 offline RSFT 而非 online RL。\\\\n\\\\n  - title: \\\\\\\"Adaptive Reinforcement Learning Planning: Harnessing LLMs for Complex Information Extraction\\\\\\\"\\\\n    authors: Zepeng Ding et al.\\\\n    year: 2024\\\\n    venue: arXiv 2406.11455\\\\n    url: https://arxiv.org/abs/2406.11455\\\\n    category: rl_for_ie\\\\n    role: background\\\\n    key_finding: >\\\\n      将 LLM 顺序抽取建模为 MDP，用 DDQN 训练 decision module\\\\n      自适应选择实体抽取顺序，提升复杂 IE 性能。\\\\n    relevance_to_rsft_docre: >\\\\n      RL for IE 的早期工作。用 RL 优化抽取策略而非模型本身，\\\\n      与我们 RSFT 直接微调 LLM 的方法路径不同。\\\\n\\\\n  - title: \\\\\\\"Graph-R1: Towards Agentic GraphRAG Framework via End-to-end Reinforcement Learning\\\\\\\"\\\\n    authors: Haoran Luo et al.\\\\n    year: 2025\\\\n    venue: ICML 2026\\\\n    url: https://arxiv.org/abs/2507.21892\\\\n    category: rl_for_ie\\\\n    role: background\\\\n    key_finding: >\\\\n      用端到端 RL 优化 GraphRAG agent 的多轮检索-推理循环，\\\\n      包含 knowledge hypergraph construction（n-ary relation extraction）。\\\\n    relevance_to_rsft_docre: >\\\\n      RL + knowledge extraction 的交叉点。Graph-R1 关注 QA 场景下的知识图谱构建，\\\\n      我们关注 DocRE 的训练优化，应用场景不同。\\\\n\\\\n  # === Category 8: Recent LLM-based DocRE Methods ===\\\\n\\\\n  - title: \\\\\\\"RelPrior: Relation as a Prior - A Novel Paradigm for LLM-based Document-level Relation Extraction\\\\\\\"\\\\n    authors: Anonymous\\\\n    year: 2025\\\\n    venue: arXiv 2511.08143\\\\n    url: https://arxiv.org/abs/2511.08143\\\\n    category: llm_docre\\\\n    role: key_baseline\\\\n    key_finding: >\\\\n      用 binary relation 作为先验过滤无关实体对，再用 predefined relation 匹配实体，\\\\n      避免 LLM 在 DocRE 中被无关实体对分散注意力。\\\\n      在 DocRED/Re-DocRED 上超越现有纯 LLM-based DocRE 方法。\\\\n    results:\\\\n      docred_dev_f1: 47.82\\\\n      docred_test_f1: 48.34\\\\n      re_docred_dev_f1: 55.94\\\\n      re_docred_test_f1: 54.80\\\\n      backbone: LLaMA3-8B\\\\n    evidence_generation: false\\\\n    relevance_to_rsft_docre: >\\\\n      我们的直接 baseline 之一。RelPrior_LLaMA3-8B 在 DocRED test F1=48.34,\\\\n      Re-DocRED test F1=54.80。我们的 RSFT 提升显著更优。\\\\n      RelPrior 是 inference paradigm 创新（两阶段筛选），我们是 training paradigm 创新（RSFT+CED），正交互补。\\\\n\\\\n  - title: \\\\\\\"LMRC: LLM with Relation Classifier for Document-Level Relation Extraction\\\\\\\"\\\\n    authors: Xingzuo Li, Kehai Chen, Yunfei Long, Min Zhang\\\\n    year: 2024\\\\n    venue: arXiv 2408.13889\\\\n    url: https://arxiv.org/abs/2408.13889\\\\n    category: llm_docre\\\\n    role: related_method\\\\n    key_finding: >\\\\n      两阶段方法：先用 attention-based classifier 过滤 NA 实体对（RCP），\\\\n      再用 LLM 在精简候选空间中做多分类（RC）。\\\\n      注意：LMRC 依赖 BERT-based classifier 作为预筛选，非纯 LLM 方法。\\\\n    results:\\\\n      docred_dev_ign_f1: 58.16\\\\n      docred_dev_f1: 59.97\\\\n      docred_test_ign_f1: 58.49\\\\n      docred_test_f1: 60.52\\\\n      re_docred_test_ign_f1: 74.08\\\\n      re_docred_test_f1: 74.63\\\\n      backbone: BERT classifier + LLM\\\\n    evidence_generation: false\\\\n    relevance_to_rsft_docre: >\\\\n      LMRC 在 DocRED test F1=60.52, Re-DocRED test F1=74.63，性能显著高于纯 LLM 方法。\\\\n      但它依赖 BERT classifier 预筛选，本质上是 hybrid 方法而非纯 LLM generative。\\\\n      与我们端到端 LLM 生成方式不同——我们通过 RSFT 的 reward-based filtering 隐式解决 class imbalance。\\\\n\\\\n  - title: \\\\\\\"Ru-LLM: Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction\\\\\\\"\\\\n    authors: Anonymous\\\\n    year: 2025\\\\n    venue: NLPCC 2025\\\\n    url: https://link.springer.com/chapter/10.1007/978-981-95-3343-5_11\\\\n    category: llm_docre\\\\n    role: related_method\\\\n    key_finding: >\\\\n      用频繁模式挖掘 + MCTS 搜索逻辑规则，转化为 prompt 约束 LLM 输出，\\\\n      再用 CoT 验证过滤不满足规则的 triple。\\\\n      在 DWIE、DocRED、Re-DocRED 上声称超越现有 LLM 方法和规则框架。\\\\n      具体 F1 未公开获取（Springer 付费墙），但声称超越 AutoRE 等 LLM baseline。\\\\n    results:\\\\n      note: \\\\\\\"behind Springer paywall; claims SOTA over LLM baselines on DocRED/Re-DocRED/DWIE\\\\\\\"\\\\n    evidence_generation: false\\\\n    relevance_to_rsft_docre: >\\\\n      规则约束方式与我们的 CED reward 在 motivation 上相似（都是引入外部知识约束），\\\\n      但 Ru-LLM 用 inference-time 规则验证（MCTS+CoT），我们用 training-time reward shaping（CED）。\\\\n      Ru-LLM 的规则是数据集级别的频繁模式，CED 是 instance-level 的 evidence faithfulness。\\\\n\\\\n  - title: \\\\\\\"GLiDRE: Generalist Lightweight model for Document-level Relation Extraction\\\\\\\"\\\\n    authors: Anonymous\\\\n    year: 2025\\\\n    venue: arXiv 2508.00757\\\\n    url: https://arxiv.org/abs/2508.00757\\\\n    category: llm_docre\\\\n    role: background\\\\n    key_finding: >\\\\n      基于 dual-encoder 的轻量级零/少样本 DocRE 模型，\\\\n      预训练于 136K 文档的大规模 RE 数据。\\\\n      fully supervised Re-DocRED test F1=77.83，但这是 encoder-based 非 LLM generative。\\\\n      zero-shot Re-DocRED test F1=17.32（超越 LLaMA 3.3 70B 和 Mistral-Small 24B）。\\\\n    results:\\\\n      re_docred_dev_f1: 77.76\\\\n      re_docred_test_f1: 77.83\\\\n      re_docred_zero_shot_test_f1: 17.32\\\\n      fredo_in_domain_1doc_f1: 13.00\\\\n      fredo_in_domain_3doc_f1: 15.71\\\\n      backbone: \\\\\\\"dual-encoder (few hundred M params)\\\\\\\"\\\\n    evidence_generation: false\\\\n    relevance_to_rsft_docre: >\\\\n      不同范式（encoder-based vs LLM generative）。GLiDRE 的 fully supervised F1=77.83\\\\n      远超 LLM-based 方法（RelPrior 54.80），但依赖大规模预训练数据和 encoder 架构。\\\\n      与我们不直接可比——我们关注 LLM generative 范式下的训练优化。\\\\n\\\\n  - title: \\\\\\\"AutoRE: Document-Level Relation Extraction with Large Language Models\\\\\\\"\\\\n    authors: Anonymous\\\\n    year: 2024\\\\n    venue: arXiv 2403.14888\\\\n    url: https://arxiv.org/abs/2403.14888\\\\n    category: llm_docre\\\\n    role: background\\\\n    key_finding: >\\\\n      RHF（Relation-Head-Facts）范式用 Mistral-7B + QLoRA 做端到端 DocRE。\\\\n      关键设计：先抽 relation，再抽 head entity，最后抽 fact triple。\\\\n    results:\\\\n      re_docred_dev_f1_mistral: 53.01\\\\n      re_docred_test_f1_mistral: 51.91\\\\n      re_docred_dev_f1_vicuna: 54.29\\\\n      re_docred_test_f1_vicuna: 53.84\\\\n      docred_dev_f1_llama3: 45.76\\\\n      docred_test_f1_llama3: 45.96\\\\n      re_docred_dev_f1_llama3: 52.28\\\\n      re_docred_test_f1_llama3: 51.97\\\\n      backbone: \\\\\\\"Mistral-7B / Vicuna-7B / LLaMA3-8B (QLoRA)\\\\\\\"\\\\n    evidence_generation: false\\\\n    relevance_to_rsft_docre: >\\\\n      QLoRA fine-tuning for DocRE 的先例。AutoRE_LLaMA3-8B 在 Re-DocRED test F1=51.97,\\\\n      DocRED test F1=45.96。我们的 SFT baseline 与之类似，\\\\n      RSFT 在此基础上引入 reward-guided sample selection 进一步提升。\\\\n\\\\n  # === Category 9: Evidence Generation & Task Performance Trade-off ===\\\\n  # (NEW - 2026-05-15 evidence generation survey)\\\\n\\\\n  - title: \\\\\\\"Mind Your Step (by Step): Chain-of-Thought can Reduce Performance on Tasks where Thinking Makes Humans Worse\\\\\\\"\\\\n    authors: Sprague et al.\\\\n    year: 2024\\\\n    venue: NeurIPS 2024\\\\n    url: https://arxiv.org/abs/2410.21333\\\\n    category: evidence_generation_tradeoff\\\\n    role: key_evidence\\\\n    key_finding: >\\\\n      CoT 在某些任务上降低性能高达 36.3%（o1-preview vs GPT-4o）。\\\\n      显式推理步骤引入 error accumulation，且模型可能 overfit 到解释格式而非任务结构。\\\\n      隐式推理（hidden activations）在分布偏移下优于显式 token-level 推理。\\\\n    relevance_to_evidence_tradeoff: >\\\\n      直接支持我们的核心发现：要求模型同时生成 evidence sentences 是一种\\\\\\\"显式推理\\\\\\\"，\\\\n      会对主任务（RE）产生性能代价（~8pp F1 下降）。\\\\n      Related Work 引用点：evidence generation 作为 structured explanation，\\\\n      与 CoT 共享\\\\\\\"显式推理降低主任务性能\\\\\\\"的普遍模式。\\\\n\\\\n  - title: \\\\\\\"Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion\\\\\\\"\\\\n    authors: Xie et al. (Google Research)\\\\n    year: 2022\\\\n    venue: ACL Findings 2022\\\\n    url: https://arxiv.org/abs/2106.08657\\\\n    category: evidence_generation_tradeoff\\\\n    role: closest_docre_precedent\\\\n    key_finding: >\\\\n      Joint 训练 RE + evidence extraction，关键创新在 inference-stage fusion：\\\\n      分别在 extracted evidence 和 full document 上做 RE 预测再通过 blending layer 融合。\\\\n      DocRED 上提升 1.37 Ign F1。Silver evidence labels（启发式规则构建）即可提升 RE 性能。\\\\n    relevance_to_evidence_tradeoff: >\\\\n      最直接的 DocRE + evidence 先例。EIDER 的核心洞察是 evidence 需要 inference-stage 融合\\\\n      而非 joint generation——暗示 joint generation 会引入 noise。\\\\n      我们的 CED reranker 是 LLM-era 版本的 inference-stage fusion：\\\\n      先生成多个候选（含 evidence），再用 NLI 在推理阶段选最佳。\\\\n      Related Work 引用点：encoder-based DocRE 中 evidence 的使用方式，与我们 generative 范式的关键差异。\\\\n\\\\n  - title: \\\\\\\"Exploring the Trade-off Between Model Performance and Explanation Plausibility of Text Classifiers Using Human Rationales\\\\\\\"\\\\n    authors: Resck, Raimundo, Poco\\\\n    year: 2024\\\\n    venue: NAACL Findings 2024\\\\n    url: https://arxiv.org/abs/2404.03098\\\\n    category: evidence_generation_tradeoff\\\\n    role: formal_framework\\\\n    key_finding: >\\\\n      用 multi-objective optimization 探索 performance vs explanation plausibility 的 Pareto frontier。\\\\n      引入 rationale 约束创建 contrastive loss，证实加入 rationale supervision 会降低主任务性能，\\\\n      但存在 Pareto optimal 解平衡两者。\\\\n    relevance_to_evidence_tradeoff: >\\\\n      提供了 performance-explainability trade-off 的形式化框架。\\\\n      我们的 evidence-grounded RE 降 8pp 正是 Pareto frontier 上的一个点。\\\\n      CED reranker 的效果可解读为：将系统从 evidence-constrained 点推向 Pareto frontier，\\\\n      在几乎不牺牲 evidence quality（evi_f1=0.8188）的前提下恢复 RE 性能。\\\\n      Related Work 引用点：evidence generation 的 performance cost 有理论依据。\\\\n\\\\n  - title: \\\\\\\"The Decreasing Value of Chain of Thought in Prompting\\\\\\\"\\\\n    authors: Meincke, Mollick, Mollick, Shapiro\\\\n    year: 2025\\\\n    venue: Wharton Generative AI Labs Technical Report (SSRN)\\\\n    url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5285532\\\\n    category: evidence_generation_tradeoff\\\\n    role: empirical_support\\\\n    key_finding: >\\\\n      现代 reasoning models 上 CoT 收益微弱（4-13%），但 latency 增加 35-600%。\\\\n      更强的模型从显式推理中受益越少。CoT 可能在 easy questions 上引入 errors\\\\n      （variability 增加导致原本正确的被改错）。\\\\n    relevance_to_evidence_tradeoff: >\\\\n      支持\\\\\\\"更强的 SFT 模型不需要在生成时显式输出 evidence\\\\\\\"的论点。\\\\n      我们的 evidence-only SFT 的性能下降符合\\\\\\\"显式推理的边际收益递减\\\\\\\"模式。\\\\n      Related Work 引用点：evidence generation 的 accuracy cost 不是 DocRE-specific，而是 LLM 的普遍趋势。\\\\n\\\\n  # === Category 10: Negative Transfer in Multi-task / Auxiliary-task Learning ===\\\\n\\\\n  - title: \\\\\\\"ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning\\\\\\\"\\\\n    authors: Jiang, Chen et al.\\\\n    year: 2023\\\\n    venue: NeurIPS 2023\\\\n    url: https://arxiv.org/abs/2301.12618\\\\n    category: negative_transfer\\\\n    role: theoretical_framework\\\\n    key_finding: >\\\\n      辅助任务常导致 negative transfer，根因不仅是 gradient conflict 还有 auxiliary-target\\\\n      generalization gap。ForkMerge 周期性 fork 模型为多分支，搜索最优 task weights，\\\\n      动态 merge 过滤有害 task-parameter updates。在多个 benchmark 上减少 negative transfer。\\\\n    relevance_to_evidence_tradeoff: >\\\\n      Evidence generation 作为 auxiliary task 对 RE 的 negative transfer 可用此框架解释：\\\\n      evidence 和 RE 的 gradient 方向不完全对齐，joint training 时 evidence 任务\\\\\\\"拖累\\\\\\\"RE。\\\\n      CED reranker 本质上是将 evidence quality 从 training-time joint objective 解耦到\\\\n      inference-time verification，避免了 training-time 的 negative transfer。\\\\n      Related Work 引用点：auxiliary task 导致主任务性能下降的一般性理论。\\\\n\\\\n  # === Category 11: Faithfulness vs Accuracy / Correctness Trade-off ===\\\\n\\\\n  - title: \\\\\\\"Correctness is not Faithfulness in RAG Attributions\\\\\\\"\\\\n    authors: Wallat, Heuss, de Rijke, Anand\\\\n    year: 2024\\\\n    venue: SIGIR 2025\\\\n    url: https://arxiv.org/abs/2412.18004\\\\n    category: faithfulness_accuracy_tradeoff\\\\n    role: key_conceptual_framework\\\\n    key_finding: >\\\\n      Correctness 和 faithfulness 是独立维度，可能冲突。高达 57% 的 citations 是\\\\n      post-rationalized（事后编造而非真实依据）。Unfaithful attributions 可能 factually correct，\\\\n      但 foster misguided trust。必须同时检查 correctness 和 faithfulness。\\\\n    relevance_to_evidence_tradeoff: >\\\\n      直接相关。我们的 evidence-grounded RE 试图让模型输出 faithful evidence，\\\\n      但这与 relation correctness 产生张力（rel_f1 降 8pp）。\\\\n      CED reranker 通过 NLI verification 确保 evidence 是 faithful 的（非 post-rationalized），\\\\n      同时不牺牲 RE accuracy。\\\\n      Related Work 引用点：correctness-faithfulness 分离的概念框架。\\\\n\\\\n  - title: \\\\\\\"Evaluating Correctness and Faithfulness of Instruction-Following Models for Question Answering\\\\\\\"\\\\n    authors: Adlakha, BehnamGhader, Lu, Meade, Reddy\\\\n    year: 2024\\\\n    venue: TACL 2024\\\\n    url: https://arxiv.org/abs/2307.16877\\\\n    category: faithfulness_accuracy_tradeoff\\\\n    role: evaluation_framework\\\\n    key_finding: >\\\\n      Instruction-following LLMs 在 correctness 上表现可比 fine-tuned models，\\\\n      但 faithfulness 普遍较差——模型会 hallucinate 而非忠实于提供的 evidence。\\\\n      传统 metrics 对 correctness 和 faithfulness 的评估均有缺陷。\\\\n    relevance_to_evidence_tradeoff: >\\\\n      解释了为什么 joint evidence+RE 生成性能差——模型在同时优化 correctness\\\\n      和 faithfulness 时，两个目标存在张力。单纯要求模型\\\\\\\"同时输出正确 triples 和\\\\n      faithful evidence\\\\\\\"是 multi-objective optimization 问题。\\\\n      Related Work 引用点：correctness vs faithfulness 评估方法论。\\\\n\\\\n  - title: \\\\\\\"Towards Faithful Model Explanation in NLP: A Survey\\\\\\\"\\\\n    authors: Lyu, Havaldar, Stein et al.\\\\n    year: 2024\\\\n    venue: Computational Linguistics (MIT Press)\\\\n    url: https://aclanthology.org/2024.cl-2.6/\\\\n    category: faithfulness_accuracy_tradeoff\\\\n    role: comprehensive_survey\\\\n    key_finding: >\\\\n      系统综述 NLP 中 faithful explanation 的定义、评估和生成方法。\\\\n      识别了 faithfulness-performance trade-off 作为核心挑战：\\\\n      更 faithful 的解释不一定更有用，更有用的解释不一定 faithful。\\\\n      提出未来方向包括 multi-objective optimization 和 post-hoc verification。\\\\n    relevance_to_evidence_tradeoff: >\\\\n      权威综述为我们的 evidence generation trade-off 提供广泛文献背景。\\\\n      我们的 CED reranker 正是该综述建议的\\\\\\\"post-hoc verification\\\\\\\"方向的具体实例。\\\\n      Related Work 引用点：faithfulness 研究的全景综述，定位我们的工作。\\\\n\\\\n  # === Category 12: Reranking / Verification as Bridge ===\\\\n\\\\n  - title: \\\\\\\"Genie: Achieving Human Parity in Content-Grounded Datasets Generation\\\\\\\"\\\\n    authors: Yehudai, Carmeli, Mass et al.\\\\n    year: 2024\\\\n    venue: ICLR 2024\\\\n    url: https://arxiv.org/abs/2401.14367\\\\n    category: reranking_verification_bridge\\\\n    role: methodological_precedent\\\\n    key_finding: >\\\\n      三阶段流程：Content Preparation → Generation → NLI-based Filtering。\\\\n      用 fine-tuned T5-11B NLI 模型判断生成内容是否 entailed by source（faithfulness 检验），\\\\n      过滤不 faithful 的生成。在 LFQA、摘要、IE 上达到 human parity。\\\\n    relevance_to_evidence_tradeoff: >\\\\n      方法论上最接近我们的 CED reranker——都是用 NLI verification 作为 post-hoc filter/reranker，\\\\n      在不牺牲主任务质量的前提下确保 grounding quality。\\\\n      GENIE 验证了 NLI-based filtering 在内容生成中的有效性。\\\\n      关键差异：GENIE 是 data generation pipeline 的过滤，我们是 inference-time reranking。\\\\n      Related Work 引用点：NLI-based verification 作为 bridge 的成功先例。\\\\n\\\", \\\"total_chars\\\": 29337, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml\", \"content\": \"# Literature Map for faith-evidence-ie (FREIGE)\\n# Focus: CED-as-training-stabilizer (D024) + RSFT for DocRE\\n# Updated: 2026-05-15 (W3 reviewer gap fill + evidence generation trade-off survey)\\n\\npapers:\\n\\n  # === Category 1: Reward Diversity / Reward Shaping for RL Stability ===\\n\\n  - title: \\\"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization\\\"\\n    authors: NVIDIA Labs\\n    year: 2025\\n    venue: ICML 2026\\n    url: https://arxiv.org/abs/2601.05242\\n    category: reward_diversity\\n    role: closest_prior_work\\n    key_finding: >\\n      直接将 GRPO 应用于多 reward 组合时，不同 rollout 的 reward 组合在归一化后 collapse 为相同 advantage 值，\\n      降低训练信号分辨率导致收敛失败。GDPO 对每个 reward 独立做 group-wise normalization 再聚合，\\n      保留多 reward 的相对差异，显著提升训练稳定性。\\n    relevance_to_ced_stabilizer: >\\n      最直接相关。CED reward 本质上引入了独立于 extraction F1 的 reward 维度（evidence quality），\\n      GDPO 的理论分析解释了为什么多维 reward 比单一 reward 更稳定——独立 reward 维度防止 advantage collapse。\\n      但 GDPO 是方法论贡献，CED 是 task-specific reward 设计自然具备了这一特性。\\n\\n  - title: \\\"DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of LLMs\\\"\\n    authors: Xiwen Chen et al.\\n    year: 2025\\n    venue: arXiv 2505.09655\\n    url: https://arxiv.org/abs/2505.09655\\n    category: reward_diversity\\n    role: related_method\\n    key_finding: >\\n      GRPO 的标量 reward 无法区分语义多样但得分相同的输出（diversity-quality inconsistency）。\\n      DRA 用子模互信息（SMI）对 reward 加权，给多样性高的 completion 更大权重，\\n      等价于 Inverse Propensity Scoring 去偏，防止 policy 坍缩到先验模式。\\n    relevance_to_ced_stabilizer: >\\n      DRA 通过后处理 reward 注入多样性信号；CED 的 reward 本身就内含对比结构自然提供 diversity 信号。\\n      机制互补但来源不同——CED 是 reward design 层面，DRA 是 optimization 层面。\\n\\n  - title: \\\"Shrinking the Variance: Shrinkage Baselines for RL with Verifiable Rewards\\\"\\n    authors: Guanning Zeng et al.\\n    year: 2025\\n    venue: arXiv 2511.03710\\n    url: https://arxiv.org/abs/2511.03710\\n    category: reward_diversity\\n    role: theoretical_support\\n    key_finding: >\\n      RLVR 中 per-prompt 均值 baseline 在低 generation 数下估计不准导致高 variance 梯度。\\n      用 James-Stein shrinkage 混合 per-prompt 和 cross-prompt 均值，\\n      构造可证明更低 variance 的 policy gradient estimator。\\n    relevance_to_ced_stabilizer: >\\n      理论支持：reward variance 对 gradient estimation 质量至关重要。\\n      CED 的额外 reward 维度提供更丰富的 per-group variance，间接起到 variance 维持效果。\\n\\n  - title: \\\"Reward Shaping to Mitigate Reward Hacking in RLHF\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2502.18770\\n    url: https://arxiv.org/abs/2502.18770\\n    category: reward_diversity\\n    role: background\\n    key_finding: >\\n      RL reward 应有界且先快速增长后缓慢收敛。系统研究 reward shaping 原则，\\n      好的 reward 形状能抑制 reward hacking 并提升训练稳定性。\\n    relevance_to_ced_stabilizer: >\\n      CED reward 的 0-1 对比判别结构天然满足有界性，\\n      且 evidence quality 的渐进提升符合\\\"先快后慢\\\"的 reward shaping 原则。\\n\\n  # === Category 2: Mode Collapse Prevention in GRPO/RLHF ===\\n\\n  - title: \\\"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\\\"\\n    authors: ByteDance Seed, Tsinghua AIR\\n    year: 2025\\n    venue: NeurIPS 2025\\n    url: https://arxiv.org/abs/2503.14476\\n    category: mode_collapse_prevention\\n    role: key_baseline\\n    key_finding: >\\n      Naive GRPO 存在 entropy collapse（policy 熵快速下降→输出同质化）。\\n      根因：clipping 不对称性——概率 0.01 的 token 最多增到 0.012，而概率 0.9 的 token 可达 1.08，\\n      低概率 token 难以增长，抑制探索。DAPO 提出 Clip-Higher（εhigh=0.28 > εlow=0.2）\\n      为低概率 token 留更大增长空间，加 Dynamic Sampling 过滤 accuracy=0 或 1 的 prompt\\n      （这些 prompt 产生零梯度，降低有效 batch size）。在 AIME 2024 达 50 分超越 DeepSeek-R1-Zero。\\n    relevance_to_ced_stabilizer: >\\n      DAPO 从 optimization 技巧角度解决 entropy collapse。CED reward 从 reward design 层面\\n      防止 mode collapse——evidence quality 维度确保 reward 组内有足够 variance，\\n      不会出现 all-same-reward 的零梯度 prompt。DAPO 的 Dynamic Sampling 过滤 accuracy=0/1 prompt\\n      与我们观察到的 frac_zero_std→0.8 现象本质相同：extraction-only reward 下大量 prompt\\n      产生零 advantage，CED 从源头（reward 设计）而非后处理（过滤）解决这个问题。\\n\\n  - title: \\\"Dr. GRPO: Removing Optimization Bias in GRPO\\\"\\n    authors: Liu et al.\\n    year: 2025\\n    venue: COLM 2025\\n    url: https://arxiv.org/abs/2503.20783\\n    category: mode_collapse_prevention\\n    role: related_analysis\\n    key_finding: >\\n      GRPO 的 std 归一化引入两个 bias：(1) difficulty bias——std(r) 归一化对低 variance 组\\n      （全对/全错）给予过高 advantage 权重，trivial question 主导训练信号；\\n      (2) length bias——per-token loss 的 1/|o_i| 项使长的错误回答被 under-penalize。\\n      当 std(r)→0 时 advantage 爆炸或未定义，梯度数值不稳定。\\n      Dr. GRPO 移除 std 归一化，用无偏 Monte Carlo advantage：Ã = R(q,o_i) - mean(R)。\\n    relevance_to_ced_stabilizer: >\\n      与我们的实验发现高度一致：extraction-only reward 下 frac_zero_std→0.8 正是\\n      Dr. GRPO 分析的 difficulty bias 极端情况——大量 prompt 的所有 rollout 得到相同 F1，\\n      std→0 导致 advantage 异常。CED 通过增加 reward 维度天然维持 reward_std>0，\\n      从 reward 设计而非算法修改角度避免了 Dr. GRPO 发现的 bias。\\n\\n  - title: \\\"GVPO: Group Variance Policy Optimization for LLM Post-Training\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: NeurIPS 2025\\n    url: https://arxiv.org/abs/2504.19599\\n    category: mode_collapse_prevention\\n    role: alternative_framework\\n    key_finding: >\\n      将 KL 约束 reward 最大化的解析解直接嵌入梯度权重，\\n      variance 项自然平衡 exploration 与 exploitation，维持适度 entropy。\\n    relevance_to_ced_stabilizer: >\\n      GVPO 的 variance 项机制与 CED 维持 reward variance 的效果功能类似，\\n      但 GVPO 是算法层面 implicit regularization，CED 是 reward 层面 explicit structure。\\n\\n  - title: \\\"REINFORCE++: Stabilizing Critic-Free Policy Optimization with Global Advantage Normalization\\\"\\n    authors: Jian Hu et al.\\n    year: 2025\\n    venue: arXiv 2501.03262\\n    url: https://arxiv.org/abs/2501.03262\\n    category: mode_collapse_prevention\\n    role: related_method\\n    key_finding: >\\n      Prompt-level (local) advantage normalization 导致不准确估计和过拟合。\\n      Global batch normalization 提供更稳定、理论无偏的 gradient estimator。\\n    relevance_to_ced_stabilizer: >\\n      解决 local normalization 的 variance 问题；CED 从 reward 端增加 variance 来源。\\n      两者在不同层面解决同一问题：防止 gradient signal 消失。\\n\\n  - title: \\\"DiverseGRPO: Mitigating Mode Collapse in Image Generation via Diversity-Aware GRPO\\\"\\n    authors: Henglin Liu et al.\\n    year: 2025\\n    venue: arXiv 2512.21514\\n    url: https://arxiv.org/abs/2512.21514\\n    category: mode_collapse_prevention\\n    role: parallel_work\\n    key_finding: >\\n      图像生成中 GRPO 后期输出同质化。distributional reward modeling（谱聚类+exploratory reward）\\n      和 structure-aware regularization 实现 13-18% 语义多样性提升。\\n    relevance_to_ced_stabilizer: >\\n      跨域验证了 GRPO mode collapse 的普遍性，distributional reward 思路与 CED 精神相近——\\n      都是通过 reward 层面结构化信号维持输出多样性。\\n\\n  - title: \\\"Why GRPO Needs Normalization: A Local-Curvature Perspective on Adaptive Gradients\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2601.23135\\n    url: https://arxiv.org/abs/2601.23135\\n    category: mode_collapse_prevention\\n    role: theoretical_support\\n    key_finding: >\\n      GRPO 的 reward_std 归一化在温和条件下提供严格优于未归一化 REINFORCE 的收敛速率，\\n      收益由 prompt 间平均 reward std 刻画。\\n    relevance_to_ced_stabilizer: >\\n      直接理论支撑：reward_std 越大收敛越好。CED 通过 evidence quality 维度维持高 reward_std，\\n      从该理论看 CED 的稳定性优势是 reward_std 维持带来的收敛速率优势。\\n\\n  # === Category 3: Contrastive Rewards in RL ===\\n\\n  - title: \\\"Improving Reinforcement Learning from Human Feedback Using Contrastive Rewards\\\"\\n    authors: Shen, Zhang et al.\\n    year: 2024\\n    venue: arXiv 2403.07708\\n    url: https://arxiv.org/abs/2403.07708\\n    category: contrastive_reward\\n    role: closest_contrastive_precedent\\n    key_finding: >\\n      两步机制：(1) 离线采样 baseline response；(2) 用 baseline 计算 contrastive reward\\n      作为 PPO 的 penalty 项。效果：惩罚 reward uncertainty、根据任务难度自适应校准、\\n      减少 PPO 中的 variance。在 TL;DR 和 HH-RLHF 上持续优于标准 RLHF。\\n    relevance_to_ced_stabilizer: >\\n      最接近的对比 reward 先例。关键差异：(1) 它是对 learned RM 输出的后处理对比，\\n      CED 是 reward function 本身就是对比判别（evidence vs. corrupted evidence）；\\n      (2) 它在 PPO 中验证，CED 在 GRPO 中验证；\\n      (3) 它是 domain-agnostic penalty，CED 是 task-specific faithfulness signal。\\n      stabilizing 机制相通但实现路径根本不同。\\n\\n  - title: \\\"Improving Discriminative Capability of Reward Models in RLHF Using Contrastive Learning\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: EMNLP 2024\\n    url: https://aclanthology.org/2024.emnlp-main.852/\\n    category: contrastive_reward\\n    role: related_method\\n    key_finding: >\\n      无监督对比损失训练 reward model 充分捕捉对比数据区分度，\\n      带来更稳定的 PPO 训练 return 和 reward。\\n    relevance_to_ced_stabilizer: >\\n      验证对比训练 reward model → 更稳定 RL 训练链条。CED 不是对比训练 reward model，\\n      而是 reward function 本身就是对比判别，但 stabilizing 机制相通。\\n\\n  - title: \\\"Contrastive Preference Learning: Learning from Human Feedback without RL\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: ICLR 2025\\n    url: https://openreview.net/forum?id=iX1RjVQODj\\n    category: contrastive_reward\\n    role: background\\n    key_finding: >\\n      将 preference learning 重新表述为对比学习问题，无需显式 RL 即可从人类反馈中学习。\\n    relevance_to_ced_stabilizer: >\\n      对比框架在 preference alignment 中的通用性。CED 可被视为 task-specific contrastive preference signal。\\n\\n  # === Category 4: Evidence-Based Rewards in IE/NLP ===\\n\\n  - title: \\\"Drift: Enhancing LLM Faithfulness in Rationale Generation\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: ACL 2025\\n    url: https://aclanthology.org/2025.acl-long.340.pdf\\n    category: evidence_reward\\n    role: related_method\\n    key_finding: >\\n      用 faithfulness reward 引导 LLM 生成更可靠的 rationale，提升 CoT 推理事实一致性。\\n    relevance_to_ced_stabilizer: >\\n      Faithfulness reward 用于生成质量的先例。CED 中 evidence discrimination\\n      本质上也是 faithfulness 信号——判断证据是否忠实支持抽取结果。\\n\\n  - title: \\\"Fine-Grained NLI-Based Faithfulness Evaluation for Diverse Summarisation Tasks (INFUSE)\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: EACL 2024\\n    url: https://aclanthology.org/2024.eacl-long.102/\\n    category: evidence_reward\\n    role: background\\n    key_finding: >\\n      变长前提+简化假设的细粒度 NLI faithfulness 评估，超越传统 NLI 在多任务摘要上的表现。\\n    relevance_to_ced_stabilizer: >\\n      NLI 作为 faithfulness 评估工具的进展。CED 中 NLI 组件用于判断 evidence 对 triple 的支持度。\\n\\n  - title: \\\"Enhancing Cross-Evidence Reasoning Graph for Document-Level Relation Extraction\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: PMC/Bioinformatics 2024\\n    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11232587/\\n    category: evidence_reward\\n    role: background\\n    key_finding: >\\n      文档级关系抽取中用 cross-evidence reasoning graph 增强跨证据推理。\\n    relevance_to_ced_stabilizer: >\\n      DocRE 中 evidence 的重要性。但用 evidence 作为模型输入特征，\\n      我们用 evidence quality 作为 RL reward 信号——定位根本不同。\\n\\n  # === Category 5: Multi-Objective RL for Text Generation ===\\n\\n  - title: \\\"Confronting Reward Model Overoptimization with Constrained RLHF\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: OpenReview\\n    url: https://openreview.net/forum?id=gkfUvn0fLU\\n    category: multi_objective_rl\\n    role: related_analysis\\n    key_finding: >\\n      多组件 RM 的 overoptimization 研究。component RM 间的相关性显著影响 overoptimization 临界点，\\n      用 constrained MDP 防止超出适当边界。\\n    relevance_to_ced_stabilizer: >\\n      CED 引入了与 extraction F1 低相关的 reward component（evidence quality），\\n      根据该论文分析低相关多组件 reward 更不易 overoptimize，\\n      可能是 CED 稳定性的另一个理论解释角度。\\n\\n  - title: \\\"On-Policy RL with Optimal Reward Baseline\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2505.23585\\n    url: https://arxiv.org/abs/2505.23585\\n    category: multi_objective_rl\\n    role: theoretical_support\\n    key_finding: >\\n      Optimal baseline 一致性地实现更高训练 reward 和更高 entropy，\\n      有效稳定训练并促进更多样的 policy exploration。\\n    relevance_to_ced_stabilizer: >\\n      CED reward 的多维特性可能起到类似 optimal baseline 效果——\\n      evidence quality 维度为 advantage estimation 提供更丰富的参照信号。\\n\\n  # === Category 6: RSFT Methodology & Theory ===\\n\\n  - title: \\\"A Minimalist Approach to LLM Reasoning: from Rejection Sampling to Reinforce\\\"\\n    authors: Xiao et al.\\n    year: 2025\\n    venue: arXiv 2504.11343\\n    url: https://arxiv.org/abs/2504.11343\\n    category: rsft_methodology\\n    role: key_theoretical_support\\n    key_finding: >\\n      RAFT（简单 rejection sampling baseline）在数学推理上与 GRPO/PPO 表现相当。\\n      消融实验表明 GRPO 的主要优势来自丢弃全错 prompt 而非 reward normalization。\\n      提出 Reinforce-Rej，在 RAFT 基础上过滤全对和全错 sample。\\n      关键洞察：GRPO 和 RAFT 的核心区别在于负样本处理——GRPO 混合正负样本训练，\\n      RAFT 只用正样本，但 RAFT 仍能达到相当性能，说明 rejection sampling 的简单性被低估了。\\n    relevance_to_rsft_docre: >\\n      直接支持我们的设计选择：(1) RSFT 在 DocRE 上成功而 GRPO 失败，\\n      与该论文发现一致——rejection sampling 的 offline 特性天然避免了 catastrophic forgetting；\\n      (2) GRPO 主要优势来自过滤全错 prompt，这与我们 RSFT 的 reward-based filtering 机制相同；\\n      (3) DocRE structured output 比 math reasoning 更难用 online RL 优化，\\n      强化了 offline RSFT 的合理性。\\n\\n  - title: \\\"Beyond Rejection Sampling: Trajectory Fusion for Scaling Mathematical Reasoning (TrajFusion)\\\"\\n    authors: Jie Deng et al.\\n    year: 2026\\n    venue: arXiv 2602.04391\\n    url: https://arxiv.org/abs/2602.04391\\n    category: rsft_methodology\\n    role: method_component\\n    key_finding: >\\n      传统 RSFT 只用正确轨迹，丢弃错误轨迹。TrajFusion 将错误和正确轨迹交替拼接，\\n      显式建模试错推理过程，在困难数学问题上显著超越标准 RFT。\\n    relevance_to_rsft_docre: >\\n      Future work 方向：可考虑在 DocRE RSFT 中融合失败样本的信息。\\n      但 DocRE 的结构化输出（JSON triple）不同于 math 的 chain-of-thought，\\n      融合方式需要重新设计。\\n\\n  - title: \\\"Rejection Sampling Based Fine Tuning Secretly Performs PPO\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: ICML 2025\\n    url: https://openreview.net/forum?id=yQ2UivKlir\\n    category: rsft_methodology\\n    role: theoretical_support\\n    key_finding: >\\n      建立 RSFT 与 PPO 之间的理论联系：rejection sampling fine-tuning\\n      在特定条件下隐式执行 PPO with marginal KL constraints。\\n    relevance_to_rsft_docre: >\\n      为 RSFT 的有效性提供理论解释。我们的 RSFT 成功可被视为\\n      隐式执行了 constrained policy optimization，\\n      避免了显式 GRPO 在 structured output 上的不稳定性。\\n\\n  # === Category 7: RL for Information Extraction ===\\n\\n  - title: \\\"R1-RE: Cross-Domain Relation Extraction with RLVR\\\"\\n    authors: Runpeng Dai, Tong Zheng et al.\\n    year: 2025\\n    venue: arXiv 2507.04642\\n    url: https://arxiv.org/abs/2507.04642\\n    category: rl_for_ie\\n    role: direct_competitor\\n    key_finding: >\\n      首个将 RLVR（GRPO + verifiable reward）用于关系抽取的框架。\\n      将 RE 重构为推理任务，R1-RE-7B 在跨域 OOD 准确率约 70%，媲美 GPT-4o。\\n      Reward 设计：format reward (+1/-3) + metric reward (+2/-1.5)，先验证格式再加准确度。\\n      triplet extraction 用 F1-based reward（entity weight=1, triplet weight=3）。\\n      未报告 catastrophic forgetting——GRPO 训练后在 MATH-500/IFEval/GPQA 上性能不降反升，\\n      说明句子级 RE 的简单 reward 结构足以稳定 GRPO 训练。\\n    results:\\n      sem2010_in_domain: 91.8\\n      sem2010_ood: 66.5\\n      mdkg_in_domain: 88.1\\n      mdkg_ood: 65.8\\n    evidence_generation: false\\n    relevance_to_rsft_docre: >\\n      最直接竞争者。关键差异与讨论：\\n      (1) R1-RE 是句子级 RE，GRPO 成功；我们是文档级 RE，GRPO 失败→RSFT 成功。\\n      句子级 RE 每个 sample 只有 1 个 triple（binary classification），reward variance 天然充足；\\n      文档级 RE 每个 sample 有数十个 triple，F1 score 作为 reward 在 group 内趋于同质化（frac_zero_std→0.8）。\\n      (2) R1-RE 未报告 catastrophic forgetting，进一步支持\\\"句子级简单 reward 可行，文档级需要 CED\\\"的论点。\\n      (3) R1-RE 关注 OOD 泛化，无 evidence 组件；我们关注 evidence-grounded extraction quality。\\n      互补而非直接冲突——R1-RE 证明 RLVR for RE 可行，我们揭示文档级需要额外设计。\\n\\n  - title: \\\"MORE-R1: Guiding LVLM for Multimodal Object-Entity Relation Extraction via Stepwise Reasoning with RL\\\"\\n    authors: Anonymous\\n    year: 2026\\n    venue: arXiv 2603.09478\\n    url: https://arxiv.org/abs/2603.09478\\n    category: rl_for_ie\\n    role: related_method\\n    key_finding: >\\n      多模态 RE 中用 GRPO + Progressive Sample-Mixing Strategy 优化 LVLM 推理能力。\\n      两阶段训练：SFT cold-start + GRPO RL。\\n    relevance_to_rsft_docre: >\\n      跨模态验证 RL for RE 趋势。其 Progressive Sample-Mixing 与我们\\n      RSFT 的 difficulty-aware sampling 思想相通，但在不同模态。\\n\\n  - title: \\\"REAR: Reinforced Reasoning Optimization for Event Argument Extraction with Relation-Aware Support\\\"\\n    authors: Jianwen Luo et al.\\n    year: 2025\\n    venue: EMNLP 2025 Findings\\n    url: https://2025.emnlp.org/program/find_papers/\\n    category: rl_for_ie\\n    role: related_method\\n    key_finding: >\\n      将强化学习推理优化用于事件论元抽取，结合关系感知支持。\\n      不同于 DocRE 但同属 IE 领域的 RL 应用。\\n    relevance_to_rsft_docre: >\\n      验证 RL 在 IE 任务上的有效性趋势。我们的工作扩展到 DocRE + evidence，\\n      且使用 offline RSFT 而非 online RL。\\n\\n  - title: \\\"Adaptive Reinforcement Learning Planning: Harnessing LLMs for Complex Information Extraction\\\"\\n    authors: Zepeng Ding et al.\\n    year: 2024\\n    venue: arXiv 2406.11455\\n    url: https://arxiv.org/abs/2406.11455\\n    category: rl_for_ie\\n    role: background\\n    key_finding: >\\n      将 LLM 顺序抽取建模为 MDP，用 DDQN 训练 decision module\\n      自适应选择实体抽取顺序，提升复杂 IE 性能。\\n    relevance_to_rsft_docre: >\\n      RL for IE 的早期工作。用 RL 优化抽取策略而非模型本身，\\n      与我们 RSFT 直接微调 LLM 的方法路径不同。\\n\\n  - title: \\\"Graph-R1: Towards Agentic GraphRAG Framework via End-to-end Reinforcement Learning\\\"\\n    authors: Haoran Luo et al.\\n    year: 2025\\n    venue: ICML 2026\\n    url: https://arxiv.org/abs/2507.21892\\n    category: rl_for_ie\\n    role: background\\n    key_finding: >\\n      用端到端 RL 优化 GraphRAG agent 的多轮检索-推理循环，\\n      包含 knowledge hypergraph construction（n-ary relation extraction）。\\n    relevance_to_rsft_docre: >\\n      RL + knowledge extraction 的交叉点。Graph-R1 关注 QA 场景下的知识图谱构建，\\n      我们关注 DocRE 的训练优化，应用场景不同。\\n\\n  # === Category 8: Recent LLM-based DocRE Methods ===\\n\\n  - title: \\\"RelPrior: Relation as a Prior - A Novel Paradigm for LLM-based Document-level Relation Extraction\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2511.08143\\n    url: https://arxiv.org/abs/2511.08143\\n    category: llm_docre\\n    role: key_baseline\\n    key_finding: >\\n      用 binary relation 作为先验过滤无关实体对，再用 predefined relation 匹配实体，\\n      避免 LLM 在 DocRE 中被无关实体对分散注意力。\\n      在 DocRED/Re-DocRED 上超越现有纯 LLM-based DocRE 方法。\\n    results:\\n      docred_dev_f1: 47.82\\n      docred_test_f1: 48.34\\n      re_docred_dev_f1: 55.94\\n      re_docred_test_f1: 54.80\\n      backbone: LLaMA3-8B\\n    evidence_generation: false\\n    relevance_to_rsft_docre: >\\n      我们的直接 baseline 之一。RelPrior_LLaMA3-8B 在 DocRED test F1=48.34,\\n      Re-DocRED test F1=54.80。我们的 RSFT 提升显著更优。\\n      RelPrior 是 inference paradigm 创新（两阶段筛选），我们是 training paradigm 创新（RSFT+CED），正交互补。\\n\\n  - title: \\\"LMRC: LLM with Relation Classifier for Document-Level Relation Extraction\\\"\\n    authors: Xingzuo Li, Kehai Chen, Yunfei Long, Min Zhang\\n    year: 2024\\n    venue: arXiv 2408.13889\\n    url: https://arxiv.org/abs/2408.13889\\n    category: llm_docre\\n    role: related_method\\n    key_finding: >\\n      两阶段方法：先用 attention-based classifier 过滤 NA 实体对（RCP），\\n      再用 LLM 在精简候选空间中做多分类（RC）。\\n      注意：LMRC 依赖 BERT-based classifier 作为预筛选，非纯 LLM 方法。\\n    results:\\n      docred_dev_ign_f1: 58.16\\n      docred_dev_f1: 59.97\\n      docred_test_ign_f1: 58.49\\n      docred_test_f1: 60.52\\n      re_docred_test_ign_f1: 74.08\\n      re_docred_test_f1: 74.63\\n      backbone: BERT classifier + LLM\\n    evidence_generation: false\\n    relevance_to_rsft_docre: >\\n      LMRC 在 DocRED test F1=60.52, Re-DocRED test F1=74.63，性能显著高于纯 LLM 方法。\\n      但它依赖 BERT classifier 预筛选，本质上是 hybrid 方法而非纯 LLM generative。\\n      与我们端到端 LLM 生成方式不同——我们通过 RSFT 的 reward-based filtering 隐式解决 class imbalance。\\n\\n  - title: \\\"Ru-LLM: Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: NLPCC 2025\\n    url: https://link.springer.com/chapter/10.1007/978-981-95-3343-5_11\\n    category: llm_docre\\n    role: related_method\\n    key_finding: >\\n      用频繁模式挖掘 + MCTS 搜索逻辑规则，转化为 prompt 约束 LLM 输出，\\n      再用 CoT 验证过滤不满足规则的 triple。\\n      在 DWIE、DocRED、Re-DocRED 上声称超越现有 LLM 方法和规则框架。\\n      具体 F1 未公开获取（Springer 付费墙），但声称超越 AutoRE 等 LLM baseline。\\n    results:\\n      note: \\\"behind Springer paywall; claims SOTA over LLM baselines on DocRED/Re-DocRED/DWIE\\\"\\n    evidence_generation: false\\n    relevance_to_rsft_docre: >\\n      规则约束方式与我们的 CED reward 在 motivation 上相似（都是引入外部知识约束），\\n      但 Ru-LLM 用 inference-time 规则验证（MCTS+CoT），我们用 training-time reward shaping（CED）。\\n      Ru-LLM 的规则是数据集级别的频繁模式，CED 是 instance-level 的 evidence faithfulness。\\n\\n  - title: \\\"GLiDRE: Generalist Lightweight model for Document-level Relation Extraction\\\"\\n    authors: Anonymous\\n    year: 2025\\n    venue: arXiv 2508.00757\\n    url: https://arxiv.org/abs/2508.00757\\n    category: llm_docre\\n    role: background\\n    key_finding: >\\n      基于 dual-encoder 的轻量级零/少样本 DocRE 模型，\\n      预训练于 136K 文档的大规模 RE 数据。\\n      fully supervised Re-DocRED test F1=77.83，但这是 encoder-based 非 LLM generative。\\n      zero-shot Re-DocRED test F1=17.32（超越 LLaMA 3.3 70B 和 Mistral-Small 24B）。\\n    results:\\n      re_docred_dev_f1: 77.76\\n      re_docred_test_f1: 77.83\\n      re_docred_zero_shot_test_f1: 17.32\\n      fredo_in_domain_1doc_f1: 13.00\\n      fredo_in_domain_3doc_f1: 15.71\\n      backbone: \\\"dual-encoder (few hundred M params)\\\"\\n    evidence_generation: false\\n    relevance_to_rsft_docre: >\\n      不同范式（encoder-based vs LLM generative）。GLiDRE 的 fully supervised F1=77.83\\n      远超 LLM-based 方法（RelPrior 54.80），但依赖大规模预训练数据和 encoder 架构。\\n      与我们不直接可比——我们关注 LLM generative 范式下的训练优化。\\n\\n  - title: \\\"AutoRE: Document-Level Relation Extraction with Large Language Models\\\"\\n    authors: Anonymous\\n    year: 2024\\n    venue: arXiv 2403.14888\\n    url: https://arxiv.org/abs/2403.14888\\n    category: llm_docre\\n    role: background\\n    key_finding: >\\n      RHF（Relation-Head-Facts）范式用 Mistral-7B + QLoRA 做端到端 DocRE。\\n      关键设计：先抽 relation，再抽 head entity，最后抽 fact triple。\\n    results:\\n      re_docred_dev_f1_mistral: 53.01\\n      re_docred_test_f1_mistral: 51.91\\n      re_docred_dev_f1_vicuna: 54.29\\n      re_docred_test_f1_vicuna: 53.84\\n      docred_dev_f1_llama3: 45.76\\n      docred_test_f1_llama3: 45.96\\n      re_docred_dev_f1_llama3: 52.28\\n      re_docred_test_f1_llama3: 51.97\\n      backbone: \\\"Mistral-7B / Vicuna-7B / LLaMA3-8B (QLoRA)\\\"\\n    evidence_generation: false\\n    relevance_to_rsft_docre: >\\n      QLoRA fine-tuning for DocRE 的先例。AutoRE_LLaMA3-8B 在 Re-DocRED test F1=51.97,\\n      DocRED test F1=45.96。我们的 SFT baseline 与之类似，\\n      RSFT 在此基础上引入 reward-guided sample selection 进一步提升。\\n\\n  # === Category 9: Evidence Generation & Task Performance Trade-off ===\\n  # (NEW - 2026-05-15 evidence generation survey)\\n\\n  - title: \\\"Mind Your Step (by Step): Chain-of-Thought can Reduce Performance on Tasks where Thinking Makes Humans Worse\\\"\\n    authors: Sprague et al.\\n    year: 2024\\n    venue: NeurIPS 2024\\n    url: https://arxiv.org/abs/2410.21333\\n    category: evidence_generation_tradeoff\\n    role: key_evidence\\n    key_finding: >\\n      CoT 在某些任务上降低性能高达 36.3%（o1-preview vs GPT-4o）。\\n      显式推理步骤引入 error accumulation，且模型可能 overfit 到解释格式而非任务结构。\\n      隐式推理（hidden activations）在分布偏移下优于显式 token-level 推理。\\n    relevance_to_evidence_tradeoff: >\\n      直接支持我们的核心发现：要求模型同时生成 evidence sentences 是一种\\\"显式推理\\\"，\\n      会对主任务（RE）产生性能代价（~8pp F1 下降）。\\n      Related Work 引用点：evidence generation 作为 structured explanation，\\n      与 CoT 共享\\\"显式推理降低主任务性能\\\"的普遍模式。\\n\\n  - title: \\\"Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion\\\"\\n    authors: Xie et al. (Google Research)\\n    year: 2022\\n    venue: ACL Findings 2022\\n    url: https://arxiv.org/abs/2106.08657\\n    category: evidence_generation_tradeoff\\n    role: closest_docre_precedent\\n    key_finding: >\\n      Joint 训练 RE + evidence extraction，关键创新在 inference-stage fusion：\\n      分别在 extracted evidence 和 full document 上做 RE 预测再通过 blending layer 融合。\\n      DocRED 上提升 1.37 Ign F1。Silver evidence labels（启发式规则构建）即可提升 RE 性能。\\n    relevance_to_evidence_tradeoff: >\\n      最直接的 DocRE + evidence 先例。EIDER 的核心洞察是 evidence 需要 inference-stage 融合\\n      而非 joint generation——暗示 joint generation 会引入 noise。\\n      我们的 CED reranker 是 LLM-era 版本的 inference-stage fusion：\\n      先生成多个候选（含 evidence），再用 NLI 在推理阶段选最佳。\\n      Related Work 引用点：encoder-based DocRE 中 evidence 的使用方式，与我们 generative 范式的关键差异。\\n\\n  - title: \\\"Exploring the Trade-off Between Model Performance and Explanation Plausibility of Text Classifiers Using Human Rationales\\\"\\n    authors: Resck, Raimundo, Poco\\n    year: 2024\\n    venue: NAACL Findings 2024\\n    url: https://arxiv.org/abs/2404.03098\\n    category: evidence_generation_tradeoff\\n    role: formal_framework\\n    key_finding: >\\n      用 multi-objective optimization 探索 performance vs explanation plausibility 的 Pareto frontier。\\n      引入 rationale 约束创建 contrastive loss，证实加入 rationale supervision 会降低主任务性能，\\n      但存在 Pareto optimal 解平衡两者。\\n    relevance_to_evidence_tradeoff: >\\n      提供了 performance-explainability trade-off 的形式化框架。\\n      我们的 evidence-grounded RE 降 8pp 正是 Pareto frontier 上的一个点。\\n      CED reranker 的效果可解读为：将系统从 evidence-constrained 点推向 Pareto frontier，\\n      在几乎不牺牲 evidence quality（evi_f1=0.8188）的前提下恢复 RE 性能。\\n      Related Work 引用点：evidence generation 的 performance cost 有理论依据。\\n\\n  - title: \\\"The Decreasing Value of Chain of Thought in Prompting\\\"\\n    authors: Meincke, Mollick, Mollick, Shapiro\\n    year: 2025\\n    venue: Wharton Generative AI Labs Technical Report (SSRN)\\n    url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5285532\\n    category: evidence_generation_tradeoff\\n    role: empirical_support\\n    key_finding: >\\n      现代 reasoning models 上 CoT 收益微弱（4-13%），但 latency 增加 35-600%。\\n      更强的模型从显式推理中受益越少。CoT 可能在 easy questions 上引入 errors\\n      （variability 增加导致原本正确的被改错）。\\n    relevance_to_evidence_tradeoff: >\\n      支持\\\"更强的 SFT 模型不需要在生成时显式输出 evidence\\\"的论点。\\n      我们的 evidence-only SFT 的性能下降符合\\\"显式推理的边际收益递减\\\"模式。\\n      Related Work 引用点：evidence generation 的 accuracy cost 不是 DocRE-specific，而是 LLM 的普遍趋势。\\n\\n  # === Category 10: Negative Transfer in Multi-task / Auxiliary-task Learning ===\\n\\n  - title: \\\"ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning\\\"\\n    authors: Jiang, Chen et al.\\n    year: 2023\\n    venue: NeurIPS 2023\\n    url: https://arxiv.org/abs/2301.12618\\n    category: negative_transfer\\n    role: theoretical_framework\\n    key_finding: >\\n      辅助任务常导致 negative transfer，根因不仅是 gradient conflict 还有 auxiliary-target\\n      generalization gap。ForkMerge 周期性 fork 模型为多分支，搜索最优 task weights，\\n      动态 merge 过滤有害 task-parameter updates。在多个 benchmark 上减少 negative transfer。\\n    relevance_to_evidence_tradeoff: >\\n      Evidence generation 作为 auxiliary task 对 RE 的 negative transfer 可用此框架解释：\\n      evidence 和 RE 的 gradient 方向不完全对齐，joint training 时 evidence 任务\\\"拖累\\\"RE。\\n      CED reranker 本质上是将 evidence quality 从 training-time joint objective 解耦到\\n      inference-time verification，避免了 training-time 的 negative transfer。\\n      Related Work 引用点：auxiliary task 导致主任务性能下降的一般性理论。\\n\\n  # === Category 11: Faithfulness vs Accuracy / Correctness Trade-off ===\\n\\n  - title: \\\"Correctness is not Faithfulness in RAG Attributions\\\"\\n    authors: Wallat, Heuss, de Rijke, Anand\\n    year: 2024\\n    venue: SIGIR 2025\\n    url: https://arxiv.org/abs/2412.18004\\n    category: faithfulness_accuracy_tradeoff\\n    role: key_conceptual_framework\\n    key_finding: >\\n      Correctness 和 faithfulness 是独立维度，可能冲突。高达 57% 的 citations 是\\n      post-rationalized（事后编造而非真实依据）。Unfaithful attributions 可能 factually correct，\\n      但 foster misguided trust。必须同时检查 correctness 和 faithfulness。\\n    relevance_to_evidence_tradeoff: >\\n      直接相关。我们的 evidence-grounded RE 试图让模型输出 faithful evidence，\\n      但这与 relation correctness 产生张力（rel_f1 降 8pp）。\\n      CED reranker 通过 NLI verification 确保 evidence 是 faithful 的（非 post-rationalized），\\n      同时不牺牲 RE accuracy。\\n      Related Work 引用点：correctness-faithfulness 分离的概念框架。\\n\\n  - title: \\\"Evaluating Correctness and Faithfulness of Instruction-Following Models for Question Answering\\\"\\n    authors: Adlakha, BehnamGhader, Lu, Meade, Reddy\\n    year: 2024\\n    venue: TACL 2024\\n    url: https://arxiv.org/abs/2307.16877\\n    category: faithfulness_accuracy_tradeoff\\n    role: evaluation_framework\\n    key_finding: >\\n      Instruction-following LLMs 在 correctness 上表现可比 fine-tuned models，\\n      但 faithfulness 普遍较差——模型会 hallucinate 而非忠实于提供的 evidence。\\n      传统 metrics 对 correctness 和 faithfulness 的评估均有缺陷。\\n    relevance_to_evidence_tradeoff: >\\n      解释了为什么 joint evidence+RE 生成性能差——模型在同时优化 correctness\\n      和 faithfulness 时，两个目标存在张力。单纯要求模型\\\"同时输出正确 triples 和\\n      faithful evidence\\\"是 multi-objective optimization 问题。\\n      Related Work 引用点：correctness vs faithfulness 评估方法论。\\n\\n  - title: \\\"Towards Faithful Model Explanation in NLP: A Survey\\\"\\n    authors: Lyu, Havaldar, Stein et al.\\n    year: 2024\\n    venue: Computational Linguistics (MIT Press)\\n    url: https://aclanthology.org/2024.cl-2.6/\\n    category: faithfulness_accuracy_tradeoff\\n    role: comprehensive_survey\\n    key_finding: >\\n      系统综述 NLP 中 faithful explanation 的定义、评估和生成方法。\\n      识别了 faithfulness-performance trade-off 作为核心挑战：\\n      更 faithful 的解释不一定更有用，更有用的解释不一定 faithful。\\n      提出未来方向包括 multi-objective optimization 和 post-hoc verification。\\n    relevance_to_evidence_tradeoff: >\\n      权威综述为我们的 evidence generation trade-off 提供广泛文献背景。\\n      我们的 CED reranker 正是该综述建议的\\\"post-hoc verification\\\"方向的具体实例。\\n      Related Work 引用点：faithfulness 研究的全景综述，定位我们的工作。\\n\\n  # === Category 12: Reranking / Verification as Bridge ===\\n\\n  - title: \\\"Genie: Achieving Human Parity in Content-Grounded Datasets Generation\\\"\\n    authors: Yehudai, Carmeli, Mass et al.\\n    year: 2024\\n    venue: ICLR 2024\\n    url: https://arxiv.org/abs/2401.14367\\n    category: reranking_verification_bridge\\n    role: methodological_precedent\\n    key_finding: >\\n      三阶段流程：Content Preparation → Generation → NLI-based Filtering。\\n      用 fine-tuned T5-11B NLI 模型判断生成内容是否 entailed by source（faithfulness 检验），\\n      过滤不 faithful 的生成。在 LFQA、摘要、IE 上达到 human parity。\\n    relevance_to_evidence_tradeoff: >\\n      方法论上最接近我们的 CED reranker——都是用 NLI verification 作为 post-hoc filter/reranker，\\n      在不牺牲主任务质量的前提下确保 grounding quality。\\n      GENIE 验证了 NLI-based filtering 在内容生成中的有效性。\\n      关键差异：GENIE 是 data generation pipeline 的过滤，我们是 inference-time reranking。\\n      Related Work 引用点：NLI-based verification 作为 bridge 的成功先例。\\n\", \"total_chars\": 29337, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Runtime record

_source line 104_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778885400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "9a9a9c38-3061-4c18-989d-3134a14362ae",
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c"
}
```

---

### Assistant

_source line 105_

<details><summary>Logged reasoning block</summary>

```text
Now I need to construct the updated literature_map.yaml with the new entries added. Let me add the new papers to the appropriate categories, and add new categories where needed.

New papers to add (11 papers):

**Category 1 (reward_diversity) - ADD:**
1. MO-GRPO - reward hacking in multi-objective GRPO
2. RDPO - reward-decorrelated policy optimization

**Category 2 (mode_collapse_prevention) - ADD:**
3. GRPO is Secretly a PRM - λ-GRPO

**Category 4 (evidence_reward) - ADD:**


4. EvidenceRL - GRPO + evidence grounding reward (KEY FIND)

**Category 7 (rl_for_ie) - ADD:**
5. R²GRPO - GRPO for scientific IE

**Category 8 (llm_docre) - ADD:**
6. ADELIE - aligning LLMs on IE

**Category 9 (evidence_generation_tradeoff) - ADD:**
7. CoT is not Explainability
8. Latent CoT Survey - implicit vs explicit reasoning tradeoff

**Category 11 (faithfulness_accuracy_tradeoff) - ADD:**
9. Characterizing LLMs as Rationalizers - post

-hoc rationalization

**Category 13 (Training Precision & RL Stability) - NEW:**
10. FP16 for RL Stability

**Category 14 (Reward Hacking Theory) - NEW:**
11. Reward Hacking in the Era of Large Models - Proxy Compression Hypothesis

I'm deciding whether to consolidate the reward hacking entry into an existing category or keep it separate, and I'm realizing the FP16 paper ties directly to our QLoRA findings. Rather than scatter these across the file, I'll append all new entries at the end in clearly labeled sections to maintain the existing structure.

Looking at how the papers are organized—they're all in a flat list under `papers:` with categories marked as comments—I should add the new entries at the end of the file while preserving this format.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "6bcef0c0-4d06-405c-8b68-992834360ee5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LacDGMZv3mziwHoGvMUYQL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17759,
      "cache_read_input_tokens": 72476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17759
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

_source line 106_

现在编写更新后的 literature_map.yaml，增加 11 篇新论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "9d22c630-8b94-415d-90ed-27b64dc20e98",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LacDGMZv3mziwHoGvMUYQL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17759,
      "cache_read_input_tokens": 72476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17759
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

_source line 107_

<details open><summary>🔧 Tool call — Read · `toolu_012hNFZSzd3UepTKWaSMo1M4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
  "offset": 0,
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "7e004e03-c874-42f4-9869-309ea245a187",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LacDGMZv3mziwHoGvMUYQL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17759,
      "cache_read_input_tokens": 72476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17759
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

_source line 108 · 2026-05-15T22:11:49.588Z_

<details><summary>↩ Tool result · `toolu_012hNFZSzd3UepTKWaSMo1M4`</summary>

```text
0	# Literature Map for faith-evidence-ie (FREIGE)
1	# Focus: CED-as-training-stabilizer (D024) + RSFT for DocRE
2	# Updated: 2026-05-15 (W3 reviewer gap fill + evidence generation trade-off survey)
3	
4	papers:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "9d0c81fa-7385-4f7e-9402-77785a55bccf",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
      "content": "# Literature Map for faith-evidence-ie (FREIGE)\n# Focus: CED-as-training-stabilizer (D024) + RSFT for DocRE\n# Updated: 2026-05-15 (W3 reviewer gap fill + evidence generation trade-off survey)\n\npapers:",
      "numLines": 5,
      "startLine": 0,
      "totalLines": 708
    }
  }
}
```

</details>

---

### Tool call

_source line 109_

<details open><summary>🔧 Tool call — Edit · `toolu_01QNb6VT2rjqzV8urMmZWNtT`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
  "old_string": "# Literature Map for faith-evidence-ie (FREIGE)\n# Focus: CED-as-training-stabilizer (D024) + RSFT for DocRE\n# Updated: 2026-05-15 (W3 reviewer gap fill + evidence generation trade-off survey)",
  "new_string": "# Literature Map for faith-evidence-ie (FREIGE)\n# Focus: CED-as-training-stabilizer (D024) + RSFT for DocRE\n# Updated: 2026-05-15 (W4 expanded: +11 papers from literature scan)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "334d1c45-2991-45e0-9d75-8b70ec0187d6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ESR5qNkDaBjTY9CcVtqWyM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 927,
      "cache_read_input_tokens": 90235,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 927
      },
      "output_tokens": 69,
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

_source line 110 · 2026-05-15T22:11:54.179Z_

<details><summary>↩ Tool result · `toolu_01QNb6VT2rjqzV8urMmZWNtT`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "782c5693-66fd-46e2-8483-7c995760423d",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
    "oldString": "# Literature Map for faith-evidence-ie (FREIGE)\n# Focus: CED-as-training-stabilizer (D024) + RSFT for DocRE\n# Updated: 2026-05-15 (W3 reviewer gap fill + evidence generation trade-off survey)",
    "newString": "# Literature Map for faith-evidence-ie (FREIGE)\n# Focus: CED-as-training-stabilizer (D024) + RSFT for DocRE\n# Updated: 2026-05-15 (W4 expanded: +11 papers from literature scan)",
    "originalFile": "# Literature Map for faith-evidence-ie (FREIGE)\n# Focus: CED-as-training-stabilizer (D024) + RSFT for DocRE\n# Updated: 2026-05-15 (W3 reviewer gap fill + evidence generation trade-off survey)\n\npapers:\n\n  # === Category 1: Reward Diversity / Reward Shaping for RL Stability ===\n\n  - title: \"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization\"\n    authors: NVIDIA Labs\n    year: 2025\n    venue: ICML 2026\n    url: https://arxiv.org/abs/2601.05242\n    category: reward_diversity\n    role: closest_prior_work\n    key_finding: >\n      直接将 GRPO 应用于多 reward 组合时，不同 rollout 的 reward 组合在归一化后 collapse 为相同 advantage 值，\n      降低训练信号分辨率导致收敛失败。GDPO 对每个 reward 独立做 group-wise normalization 再聚合，\n      保留多 reward 的相对差异，显著提升训练稳定性。\n    relevance_to_ced_stabilizer: >\n      最直接相关。CED reward 本质上引入了独立于 extraction F1 的 reward 维度（evidence quality），\n      GDPO 的理论分析解释了为什么多维 reward 比单一 reward 更稳定——独立 reward 维度防止 advantage collapse。\n      但 GDPO 是方法论贡献，CED 是 task-specific reward 设计自然具备了这一特性。\n\n  - title: \"DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of LLMs\"\n    authors: Xiwen Chen et al.\n    year: 2025\n    venue: arXiv 2505.09655\n    url: https://arxiv.org/abs/2505.09655\n    category: reward_diversity\n    role: related_method\n    key_finding: >\n      GRPO 的标量 reward 无法区分语义多样但得分相同的输出（diversity-quality inconsistency）。\n      DRA 用子模互信息（SMI）对 reward 加权，给多样性高的 completion 更大权重，\n      等价于 Inverse Propensity Scoring 去偏，防止 policy 坍缩到先验模式。\n    relevance_to_ced_stabilizer: >\n      DRA 通过后处理 reward 注入多样性信号；CED 的 reward 本身就内含对比结构自然提供 diversity 信号。\n      机制互补但来源不同——CED 是 reward design 层面，DRA 是 optimization 层面。\n\n  - title: \"Shrinking the Variance: Shrinkage Baselines for RL with Verifiable Rewards\"\n    authors: Guanning Zeng et al.\n    year: 2025\n    venue: arXiv 2511.03710\n    url: https://arxiv.org/abs/2511.03710\n    category: reward_diversity\n    role: theoretical_support\n    key_finding: >\n      RLVR 中 per-prompt 均值 baseline 在低 generation 数下估计不准导致高 variance 梯度。\n      用 James-Stein shrinkage 混合 per-prompt 和 cross-prompt 均值，\n      构造可证明更低 variance 的 policy gradient estimator。\n    relevance_to_ced_stabilizer: >\n      理论支持：reward variance 对 gradient estimation 质量至关重要。\n      CED 的额外 reward 维度提供更丰富的 per-group variance，间接起到 variance 维持效果。\n\n  - title: \"Reward Shaping to Mitigate Reward Hacking in RLHF\"\n    authors: Anonymous\n    year: 2025\n    venue: arXiv 2502.18770\n    url: https://arxiv.org/abs/2502.18770\n    category: reward_diversity\n    role: background\n    key_finding: >\n      RL reward 应有界且先快速增长后缓慢收敛。系统研究 reward shaping 原则，\n      好的 reward 形状能抑制 reward hacking 并提升训练稳定性。\n    relevance_to_ced_stabilizer: >\n      CED reward 的 0-1 对比判别结构天然满足有界性，\n      且 evidence quality 的渐进提升符合\"先快后慢\"的 reward shaping 原则。\n\n  # === Category 2: Mode Collapse Prevention in GRPO/RLHF ===\n\n  - title: \"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\"\n    authors: ByteDance Seed, Tsinghua AIR\n    year: 2025\n    venue: NeurIPS 2025\n    url: https://arxiv.org/abs/2503.14476\n    category: mode_collapse_prevention\n    role: key_baseline\n    key_finding: >\n      Naive GRPO 存在 entropy collapse（policy 熵快速下降→输出同质化）。\n      根因：clipping 不对称性——概率 0.01 的 token 最多增到 0.012，而概率 0.9 的 token 可达 1.08，\n      低概率 token 难以增长，抑制探索。DAPO 提出 Clip-Higher（εhigh=0.28 > εlow=0.2）\n      为低概率 token 留更大增长空间，加 Dynamic Sampling 过滤 accuracy=0 或 1 的 prompt\n      （这些 prompt 产生零梯度，降低有效 batch size）。在 AIME 2024 达 50 分超越 DeepSeek-R1-Zero。\n    relevance_to_ced_stabilizer: >\n      DAPO 从 optimization 技巧角度解决 entropy collapse。CED reward 从 reward design 层面\n      防止 mode collapse——evidence quality 维度确保 reward 组内有足够 variance，\n      不会出现 all-same-reward 的零梯度 prompt。DAPO 的 Dynamic Sampling 过滤 accuracy=0/1 prompt\n      与我们观察到的 frac_zero_std→0.8 现象本质相同：extraction-only reward 下大量 prompt\n      产生零 advantage，CED 从源头（reward 设计）而非后处理（过滤）解决这个问题。\n\n  - title: \"Dr. GRPO: Removing Optimization Bias in GRPO\"\n    authors: Liu et al.\n    year: 2025\n    venue: COLM 2025\n    url: https://arxiv.org/abs/2503.20783\n    category: mode_collapse_prevention\n    role: related_analysis\n    key_finding: >\n      GRPO 的 std 归一化引入两个 bias：(1) difficulty bias——std(r) 归一化对低 variance 组\n      （全对/全错）给予过高 advantage 权重，trivial question 主导训练信号；\n      (2) length bias——per-token loss 的 1/|o_i| 项使长的错误回答被 under-penalize。\n      当 std(r)→0 时 advantage 爆炸或未定义，梯度数值不稳定。\n      Dr. GRPO 移除 std 归一化，用无偏 Monte Carlo advantage：Ã = R(q,o_i) - mean(R)。\n    relevance_to_ced_stabilizer: >\n      与我们的实验发现高度一致：extraction-only reward 下 frac_zero_std→0.8 正是\n      Dr. GRPO 分析的 difficulty bias 极端情况——大量 prompt 的所有 rollout 得到相同 F1，\n      std→0 导致 advantage 异常。CED 通过增加 reward 维度天然维持 reward_std>0，\n      从 reward 设计而非算法修改角度避免了 Dr. GRPO 发现的 bias。\n\n  - title: \"GVPO: Group Variance Policy Optimization for LLM Post-Training\"\n    authors: Anonymous\n    year: 2025\n    venue: NeurIPS 2025\n    url: https://arxiv.org/abs/2504.19599\n    category: mode_collapse_prevention\n    role: alternative_framework\n    key_finding: >\n      将 KL 约束 reward 最大化的解析解直接嵌入梯度权重，\n      variance 项自然平衡 exploration 与 exploitation，维持适度 entropy。\n    relevance_to_ced_stabilizer: >\n      GVPO 的 variance 项机制与 CED 维持 reward variance 的效果功能类似，\n      但 GVPO 是算法层面 implicit regularization，CED 是 reward 层面 explicit structure。\n\n  - title: \"REINFORCE++: Stabilizing Critic-Free Policy Optimization with Global Advantage Normalization\"\n    authors: Jian Hu et al.\n    year: 2025\n    venue: arXiv 2501.03262\n    url: https://arxiv.org/abs/2501.03262\n    category: mode_collapse_prevention\n    role: related_method\n    key_finding: >\n      Prompt-level (local) advantage normalization 导致不准确估计和过拟合。\n      Global batch normalization 提供更稳定、理论无偏的 gradient estimator。\n    relevance_to_ced_stabilizer: >\n      解决 local normalization 的 variance 问题；CED 从 reward 端增加 variance 来源。\n      两者在不同层面解决同一问题：防止 gradient signal 消失。\n\n  - title: \"DiverseGRPO: Mitigating Mode Collapse in Image Generation via Diversity-Aware GRPO\"\n    authors: Henglin Liu et al.\n    year: 2025\n    venue: arXiv 2512.21514\n    url: https://arxiv.org/abs/2512.21514\n    category: mode_collapse_prevention\n    role: parallel_work\n    key_finding: >\n      图像生成中 GRPO 后期输出同质化。distributional reward modeling（谱聚类+exploratory reward）\n      和 structure-aware regularization 实现 13-18% 语义多样性提升。\n    relevance_to_ced_stabilizer: >\n      跨域验证了 GRPO mode collapse 的普遍性，distributional reward 思路与 CED 精神相近——\n      都是通过 reward 层面结构化信号维持输出多样性。\n\n  - title: \"Why GRPO Needs Normalization: A Local-Curvature Perspective on Adaptive Gradients\"\n    authors: Anonymous\n    year: 2025\n    venue: arXiv 2601.23135\n    url: https://arxiv.org/abs/2601.23135\n    category: mode_collapse_prevention\n    role: theoretical_support\n    key_finding: >\n      GRPO 的 reward_std 归一化在温和条件下提供严格优于未归一化 REINFORCE 的收敛速率，\n      收益由 prompt 间平均 reward std 刻画。\n    relevance_to_ced_stabilizer: >\n      直接理论支撑：reward_std 越大收敛越好。CED 通过 evidence quality 维度维持高 reward_std，\n      从该理论看 CED 的稳定性优势是 reward_std 维持带来的收敛速率优势。\n\n  # === Category 3: Contrastive Rewards in RL ===\n\n  - title: \"Improving Reinforcement Learning from Human Feedback Using Contrastive Rewards\"\n    authors: Shen, Zhang et al.\n    year: 2024\n    venue: arXiv 2403.07708\n    url: https://arxiv.org/abs/2403.07708\n    category: contrastive_reward\n    role: closest_contrastive_precedent\n    key_finding: >\n      两步机制：(1) 离线采样 baseline response；(2) 用 baseline 计算 contrastive reward\n      作为 PPO 的 penalty 项。效果：惩罚 reward uncertainty、根据任务难度自适应校准、\n      减少 PPO 中的 variance。在 TL;DR 和 HH-RLHF 上持续优于标准 RLHF。\n    relevance_to_ced_stabilizer: >\n      最接近的对比 reward 先例。关键差异：(1) 它是对 learned RM 输出的后处理对比，\n      CED 是 reward function 本身就是对比判别（evidence vs. corrupted evidence）；\n      (2) 它在 PPO 中验证，CED 在 GRPO 中验证；\n      (3) 它是 domain-agnostic penalty，CED 是 task-specific faithfulness signal。\n      stabilizing 机制相通但实现路径根本不同。\n\n  - title: \"Improving Discriminative Capability of Reward Models in RLHF Using Contrastive Learning\"\n    authors: Anonymous\n    year: 2024\n    venue: EMNLP 2024\n    url: https://aclanthology.org/2024.emnlp-main.852/\n    category: contrastive_reward\n    role: related_method\n    key_finding: >\n      无监督对比损失训练 reward model 充分捕捉对比数据区分度，\n      带来更稳定的 PPO 训练 return 和 reward。\n    relevance_to_ced_stabilizer: >\n      验证对比训练 reward model → 更稳定 RL 训练链条。CED 不是对比训练 reward model，\n      而是 reward function 本身就是对比判别，但 stabilizing 机制相通。\n\n  - title: \"Contrastive Preference Learning: Learning from Human Feedback without RL\"\n    authors: Anonymous\n    year: 2024\n    venue: ICLR 2025\n    url: https://openreview.net/forum?id=iX1RjVQODj\n    category: contrastive_reward\n    role: background\n    key_finding: >\n      将 preference learning 重新表述为对比学习问题，无需显式 RL 即可从人类反馈中学习。\n    relevance_to_ced_stabilizer: >\n      对比框架在 preference alignment 中的通用性。CED 可被视为 task-specific contrastive preference signal。\n\n  # === Category 4: Evidence-Based Rewards in IE/NLP ===\n\n  - title: \"Drift: Enhancing LLM Faithfulness in Rationale Generation\"\n    authors: Anonymous\n    year: 2025\n    venue: ACL 2025\n    url: https://aclanthology.org/2025.acl-long.340.pdf\n    category: evidence_reward\n    role: related_method\n    key_finding: >\n      用 faithfulness reward 引导 LLM 生成更可靠的 rationale，提升 CoT 推理事实一致性。\n    relevance_to_ced_stabilizer: >\n      Faithfulness reward 用于生成质量的先例。CED 中 evidence discrimination\n      本质上也是 faithfulness 信号——判断证据是否忠实支持抽取结果。\n\n  - title: \"Fine-Grained NLI-Based Faithfulness Evaluation for Diverse Summarisation Tasks (INFUSE)\"\n    authors: Anonymous\n    year: 2024\n    venue: EACL 2024\n    url: https://aclanthology.org/2024.eacl-long.102/\n    category: evidence_reward\n    role: background\n    key_finding: >\n      变长前提+简化假设的细粒度 NLI faithfulness 评估，超越传统 NLI 在多任务摘要上的表现。\n    relevance_to_ced_stabilizer: >\n      NLI 作为 faithfulness 评估工具的进展。CED 中 NLI 组件用于判断 evidence 对 triple 的支持度。\n\n  - title: \"Enhancing Cross-Evidence Reasoning Graph for Document-Level Relation Extraction\"\n    authors: Anonymous\n    year: 2024\n    venue: PMC/Bioinformatics 2024\n    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11232587/\n    category: evidence_reward\n    role: background\n    key_finding: >\n      文档级关系抽取中用 cross-evidence reasoning graph 增强跨证据推理。\n    relevance_to_ced_stabilizer: >\n      DocRE 中 evidence 的重要性。但用 evidence 作为模型输入特征，\n      我们用 evidence quality 作为 RL reward 信号——定位根本不同。\n\n  # === Category 5: Multi-Objective RL for Text Generation ===\n\n  - title: \"Confronting Reward Model Overoptimization with Constrained RLHF\"\n    authors: Anonymous\n    year: 2025\n    venue: OpenReview\n    url: https://openreview.net/forum?id=gkfUvn0fLU\n    category: multi_objective_rl\n    role: related_analysis\n    key_finding: >\n      多组件 RM 的 overoptimization 研究。component RM 间的相关性显著影响 overoptimization 临界点，\n      用 constrained MDP 防止超出适当边界。\n    relevance_to_ced_stabilizer: >\n      CED 引入了与 extraction F1 低相关的 reward component（evidence quality），\n      根据该论文分析低相关多组件 reward 更不易 overoptimize，\n      可能是 CED 稳定性的另一个理论解释角度。\n\n  - title: \"On-Policy RL with Optimal Reward Baseline\"\n    authors: Anonymous\n    year: 2025\n    venue: arXiv 2505.23585\n    url: https://arxiv.org/abs/2505.23585\n    category: multi_objective_rl\n    role: theoretical_support\n    key_finding: >\n      Optimal baseline 一致性地实现更高训练 reward 和更高 entropy，\n      有效稳定训练并促进更多样的 policy exploration。\n    relevance_to_ced_stabilizer: >\n      CED reward 的多维特性可能起到类似 optimal baseline 效果——\n      evidence quality 维度为 advantage estimation 提供更丰富的参照信号。\n\n  # === Category 6: RSFT Methodology & Theory ===\n\n  - title: \"A Minimalist Approach to LLM Reasoning: from Rejection Sampling to Reinforce\"\n    authors: Xiao et al.\n    year: 2025\n    venue: arXiv 2504.11343\n    url: https://arxiv.org/abs/2504.11343\n    category: rsft_methodology\n    role: key_theoretical_support\n    key_finding: >\n      RAFT（简单 rejection sampling baseline）在数学推理上与 GRPO/PPO 表现相当。\n      消融实验表明 GRPO 的主要优势来自丢弃全错 prompt 而非 reward normalization。\n      提出 Reinforce-Rej，在 RAFT 基础上过滤全对和全错 sample。\n      关键洞察：GRPO 和 RAFT 的核心区别在于负样本处理——GRPO 混合正负样本训练，\n      RAFT 只用正样本，但 RAFT 仍能达到相当性能，说明 rejection sampling 的简单性被低估了。\n    relevance_to_rsft_docre: >\n      直接支持我们的设计选择：(1) RSFT 在 DocRE 上成功而 GRPO 失败，\n      与该论文发现一致——rejection sampling 的 offline 特性天然避免了 catastrophic forgetting；\n      (2) GRPO 主要优势来自过滤全错 prompt，这与我们 RSFT 的 reward-based filtering 机制相同；\n      (3) DocRE structured output 比 math reasoning 更难用 online RL 优化，\n      强化了 offline RSFT 的合理性。\n\n  - title: \"Beyond Rejection Sampling: Trajectory Fusion for Scaling Mathematical Reasoning (TrajFusion)\"\n    authors: Jie Deng et al.\n    year: 2026\n    venue: arXiv 2602.04391\n    url: https://arxiv.org/abs/2602.04391\n    category: rsft_methodology\n    role: method_component\n    key_finding: >\n      传统 RSFT 只用正确轨迹，丢弃错误轨迹。TrajFusion 将错误和正确轨迹交替拼接，\n      显式建模试错推理过程，在困难数学问题上显著超越标准 RFT。\n    relevance_to_rsft_docre: >\n      Future work 方向：可考虑在 DocRE RSFT 中融合失败样本的信息。\n      但 DocRE 的结构化输出（JSON triple）不同于 math 的 chain-of-thought，\n      融合方式需要重新设计。\n\n  - title: \"Rejection Sampling Based Fine Tuning Secretly Performs PPO\"\n    authors: Anonymous\n    year: 2025\n    venue: ICML 2025\n    url: https://openreview.net/forum?id=yQ2UivKlir\n    category: rsft_methodology\n    role: theoretical_support\n    key_finding: >\n      建立 RSFT 与 PPO 之间的理论联系：rejection sampling fine-tuning\n      在特定条件下隐式执行 PPO with marginal KL constraints。\n    relevance_to_rsft_docre: >\n      为 RSFT 的有效性提供理论解释。我们的 RSFT 成功可被视为\n      隐式执行了 constrained policy optimization，\n      避免了显式 GRPO 在 structured output 上的不稳定性。\n\n  # === Category 7: RL for Information Extraction ===\n\n  - title: \"R1-RE: Cross-Domain Relation Extraction with RLVR\"\n    authors: Runpeng Dai, Tong Zheng et al.\n    year: 2025\n    venue: arXiv 2507.04642\n    url: https://arxiv.org/abs/2507.04642\n    category: rl_for_ie\n    role: direct_competitor\n    key_finding: >\n      首个将 RLVR（GRPO + verifiable reward）用于关系抽取的框架。\n      将 RE 重构为推理任务，R1-RE-7B 在跨域 OOD 准确率约 70%，媲美 GPT-4o。\n      Reward 设计：format reward (+1/-3) + metric reward (+2/-1.5)，先验证格式再加准确度。\n      triplet extraction 用 F1-based reward（entity weight=1, triplet weight=3）。\n      未报告 catastrophic forgetting——GRPO 训练后在 MATH-500/IFEval/GPQA 上性能不降反升，\n      说明句子级 RE 的简单 reward 结构足以稳定 GRPO 训练。\n    results:\n      sem2010_in_domain: 91.8\n      sem2010_ood: 66.5\n      mdkg_in_domain: 88.1\n      mdkg_ood: 65.8\n    evidence_generation: false\n    relevance_to_rsft_docre: >\n      最直接竞争者。关键差异与讨论：\n      (1) R1-RE 是句子级 RE，GRPO 成功；我们是文档级 RE，GRPO 失败→RSFT 成功。\n      句子级 RE 每个 sample 只有 1 个 triple（binary classification），reward variance 天然充足；\n      文档级 RE 每个 sample 有数十个 triple，F1 score 作为 reward 在 group 内趋于同质化（frac_zero_std→0.8）。\n      (2) R1-RE 未报告 catastrophic forgetting，进一步支持\"句子级简单 reward 可行，文档级需要 CED\"的论点。\n      (3) R1-RE 关注 OOD 泛化，无 evidence 组件；我们关注 evidence-grounded extraction quality。\n      互补而非直接冲突——R1-RE 证明 RLVR for RE 可行，我们揭示文档级需要额外设计。\n\n  - title: \"MORE-R1: Guiding LVLM for Multimodal Object-Entity Relation Extraction via Stepwise Reasoning with RL\"\n    authors: Anonymous\n    year: 2026\n    venue: arXiv 2603.09478\n    url: https://arxiv.org/abs/2603.09478\n    category: rl_for_ie\n    role: related_method\n    key_finding: >\n      多模态 RE 中用 GRPO + Progressive Sample-Mixing Strategy 优化 LVLM 推理能力。\n      两阶段训练：SFT cold-start + GRPO RL。\n    relevance_to_rsft_docre: >\n      跨模态验证 RL for RE 趋势。其 Progressive Sample-Mixing 与我们\n      RSFT 的 difficulty-aware sampling 思想相通，但在不同模态。\n\n  - title: \"REAR: Reinforced Reasoning Optimization for Event Argument Extraction with Relation-Aware Support\"\n    authors: Jianwen Luo et al.\n    year: 2025\n    venue: EMNLP 2025 Findings\n    url: https://2025.emnlp.org/program/find_papers/\n    category: rl_for_ie\n    role: related_method\n    key_finding: >\n      将强化学习推理优化用于事件论元抽取，结合关系感知支持。\n      不同于 DocRE 但同属 IE 领域的 RL 应用。\n    relevance_to_rsft_docre: >\n      验证 RL 在 IE 任务上的有效性趋势。我们的工作扩展到 DocRE + evidence，\n      且使用 offline RSFT 而非 online RL。\n\n  - title: \"Adaptive Reinforcement Learning Planning: Harnessing LLMs for Complex Information Extraction\"\n    authors: Zepeng Ding et al.\n    year: 2024\n    venue: arXiv 2406.11455\n    url: https://arxiv.org/abs/2406.11455\n    category: rl_for_ie\n    role: background\n    key_finding: >\n      将 LLM 顺序抽取建模为 MDP，用 DDQN 训练 decision module\n      自适应选择实体抽取顺序，提升复杂 IE 性能。\n    relevance_to_rsft_docre: >\n      RL for IE 的早期工作。用 RL 优化抽取策略而非模型本身，\n      与我们 RSFT 直接微调 LLM 的方法路径不同。\n\n  - title: \"Graph-R1: Towards Agentic GraphRAG Framework via End-to-end Reinforcement Learning\"\n    authors: Haoran Luo et al.\n    year: 2025\n    venue: ICML 2026\n    url: https://arxiv.org/abs/2507.21892\n    category: rl_for_ie\n    role: background\n    key_finding: >\n      用端到端 RL 优化 GraphRAG agent 的多轮检索-推理循环，\n      包含 knowledge hypergraph construction（n-ary relation extraction）。\n    relevance_to_rsft_docre: >\n      RL + knowledge extraction 的交叉点。Graph-R1 关注 QA 场景下的知识图谱构建，\n      我们关注 DocRE 的训练优化，应用场景不同。\n\n  # === Category 8: Recent LLM-based DocRE Methods ===\n\n  - title: \"RelPrior: Relation as a Prior - A Novel Paradigm for LLM-based Document-level Relation Extraction\"\n    authors: Anonymous\n    year: 2025\n    venue: arXiv 2511.08143\n    url: https://arxiv.org/abs/2511.08143\n    category: llm_docre\n    role: key_baseline\n    key_finding: >\n      用 binary relation 作为先验过滤无关实体对，再用 predefined relation 匹配实体，\n      避免 LLM 在 DocRE 中被无关实体对分散注意力。\n      在 DocRED/Re-DocRED 上超越现有纯 LLM-based DocRE 方法。\n    results:\n      docred_dev_f1: 47.82\n      docred_test_f1: 48.34\n      re_docred_dev_f1: 55.94\n      re_docred_test_f1: 54.80\n      backbone: LLaMA3-8B\n    evidence_generation: false\n    relevance_to_rsft_docre: >\n      我们的直接 baseline 之一。RelPrior_LLaMA3-8B 在 DocRED test F1=48.34,\n      Re-DocRED test F1=54.80。我们的 RSFT 提升显著更优。\n      RelPrior 是 inference paradigm 创新（两阶段筛选），我们是 training paradigm 创新（RSFT+CED），正交互补。\n\n  - title: \"LMRC: LLM with Relation Classifier for Document-Level Relation Extraction\"\n    authors: Xingzuo Li, Kehai Chen, Yunfei Long, Min Zhang\n    year: 2024\n    venue: arXiv 2408.13889\n    url: https://arxiv.org/abs/2408.13889\n    category: llm_docre\n    role: related_method\n    key_finding: >\n      两阶段方法：先用 attention-based classifier 过滤 NA 实体对（RCP），\n      再用 LLM 在精简候选空间中做多分类（RC）。\n      注意：LMRC 依赖 BERT-based classifier 作为预筛选，非纯 LLM 方法。\n    results:\n      docred_dev_ign_f1: 58.16\n      docred_dev_f1: 59.97\n      docred_test_ign_f1: 58.49\n      docred_test_f1: 60.52\n      re_docred_test_ign_f1: 74.08\n      re_docred_test_f1: 74.63\n      backbone: BERT classifier + LLM\n    evidence_generation: false\n    relevance_to_rsft_docre: >\n      LMRC 在 DocRED test F1=60.52, Re-DocRED test F1=74.63，性能显著高于纯 LLM 方法。\n      但它依赖 BERT classifier 预筛选，本质上是 hybrid 方法而非纯 LLM generative。\n      与我们端到端 LLM 生成方式不同——我们通过 RSFT 的 reward-based filtering 隐式解决 class imbalance。\n\n  - title: \"Ru-LLM: Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction\"\n    authors: Anonymous\n    year: 2025\n    venue: NLPCC 2025\n    url: https://link.springer.com/chapter/10.1007/978-981-95-3343-5_11\n    category: llm_docre\n    role: related_method\n    key_finding: >\n      用频繁模式挖掘 + MCTS 搜索逻辑规则，转化为 prompt 约束 LLM 输出，\n      再用 CoT 验证过滤不满足规则的 triple。\n      在 DWIE、DocRED、Re-DocRED 上声称超越现有 LLM 方法和规则框架。\n      具体 F1 未公开获取（Springer 付费墙），但声称超越 AutoRE 等 LLM baseline。\n    results:\n      note: \"behind Springer paywall; claims SOTA over LLM baselines on DocRED/Re-DocRED/DWIE\"\n    evidence_generation: false\n    relevance_to_rsft_docre: >\n      规则约束方式与我们的 CED reward 在 motivation 上相似（都是引入外部知识约束），\n      但 Ru-LLM 用 inference-time 规则验证（MCTS+CoT），我们用 training-time reward shaping（CED）。\n      Ru-LLM 的规则是数据集级别的频繁模式，CED 是 instance-level 的 evidence faithfulness。\n\n  - title: \"GLiDRE: Generalist Lightweight model for Document-level Relation Extraction\"\n    authors: Anonymous\n    year: 2025\n    venue: arXiv 2508.00757\n    url: https://arxiv.org/abs/2508.00757\n    category: llm_docre\n    role: background\n    key_finding: >\n      基于 dual-encoder 的轻量级零/少样本 DocRE 模型，\n      预训练于 136K 文档的大规模 RE 数据。\n      fully supervised Re-DocRED test F1=77.83，但这是 encoder-based 非 LLM generative。\n      zero-shot Re-DocRED test F1=17.32（超越 LLaMA 3.3 70B 和 Mistral-Small 24B）。\n    results:\n      re_docred_dev_f1: 77.76\n      re_docred_test_f1: 77.83\n      re_docred_zero_shot_test_f1: 17.32\n      fredo_in_domain_1doc_f1: 13.00\n      fredo_in_domain_3doc_f1: 15.71\n      backbone: \"dual-encoder (few hundred M params)\"\n    evidence_generation: false\n    relevance_to_rsft_docre: >\n      不同范式（encoder-based vs LLM generative）。GLiDRE 的 fully supervised F1=77.83\n      远超 LLM-based 方法（RelPrior 54.80），但依赖大规模预训练数据和 encoder 架构。\n      与我们不直接可比——我们关注 LLM generative 范式下的训练优化。\n\n  - title: \"AutoRE: Document-Level Relation Extraction with Large Language Models\"\n    authors: Anonymous\n    year: 2024\n    venue: arXiv 2403.14888\n    url: https://arxiv.org/abs/2403.14888\n    category: llm_docre\n    role: background\n    key_finding: >\n      RHF（Relation-Head-Facts）范式用 Mistral-7B + QLoRA 做端到端 DocRE。\n      关键设计：先抽 relation，再抽 head entity，最后抽 fact triple。\n    results:\n      re_docred_dev_f1_mistral: 53.01\n      re_docred_test_f1_mistral: 51.91\n      re_docred_dev_f1_vicuna: 54.29\n      re_docred_test_f1_vicuna: 53.84\n      docred_dev_f1_llama3: 45.76\n      docred_test_f1_llama3: 45.96\n      re_docred_dev_f1_llama3: 52.28\n      re_docred_test_f1_llama3: 51.97\n      backbone: \"Mistral-7B / Vicuna-7B / LLaMA3-8B (QLoRA)\"\n    evidence_generation: false\n    relevance_to_rsft_docre: >\n      QLoRA fine-tuning for DocRE 的先例。AutoRE_LLaMA3-8B 在 Re-DocRED test F1=51.97,\n      DocRED test F1=45.96。我们的 SFT baseline 与之类似，\n      RSFT 在此基础上引入 reward-guided sample selection 进一步提升。\n\n  # === Category 9: Evidence Generation & Task Performance Trade-off ===\n  # (NEW - 2026-05-15 evidence generation survey)\n\n  - title: \"Mind Your Step (by Step): Chain-of-Thought can Reduce Performance on Tasks where Thinking Makes Humans Worse\"\n    authors: Sprague et al.\n    year: 2024\n    venue: NeurIPS 2024\n    url: https://arxiv.org/abs/2410.21333\n    category: evidence_generation_tradeoff\n    role: key_evidence\n    key_finding: >\n      CoT 在某些任务上降低性能高达 36.3%（o1-preview vs GPT-4o）。\n      显式推理步骤引入 error accumulation，且模型可能 overfit 到解释格式而非任务结构。\n      隐式推理（hidden activations）在分布偏移下优于显式 token-level 推理。\n    relevance_to_evidence_tradeoff: >\n      直接支持我们的核心发现：要求模型同时生成 evidence sentences 是一种\"显式推理\"，\n      会对主任务（RE）产生性能代价（~8pp F1 下降）。\n      Related Work 引用点：evidence generation 作为 structured explanation，\n      与 CoT 共享\"显式推理降低主任务性能\"的普遍模式。\n\n  - title: \"Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion\"\n    authors: Xie et al. (Google Research)\n    year: 2022\n    venue: ACL Findings 2022\n    url: https://arxiv.org/abs/2106.08657\n    category: evidence_generation_tradeoff\n    role: closest_docre_precedent\n    key_finding: >\n      Joint 训练 RE + evidence extraction，关键创新在 inference-stage fusion：\n      分别在 extracted evidence 和 full document 上做 RE 预测再通过 blending layer 融合。\n      DocRED 上提升 1.37 Ign F1。Silver evidence labels（启发式规则构建）即可提升 RE 性能。\n    relevance_to_evidence_tradeoff: >\n      最直接的 DocRE + evidence 先例。EIDER 的核心洞察是 evidence 需要 inference-stage 融合\n      而非 joint generation——暗示 joint generation 会引入 noise。\n      我们的 CED reranker 是 LLM-era 版本的 inference-stage fusion：\n      先生成多个候选（含 evidence），再用 NLI 在推理阶段选最佳。\n      Related Work 引用点：encoder-based DocRE 中 evidence 的使用方式，与我们 generative 范式的关键差异。\n\n  - title: \"Exploring the Trade-off Between Model Performance and Explanation Plausibility of Text Classifiers Using Human Rationales\"\n    authors: Resck, Raimundo, Poco\n    year: 2024\n    venue: NAACL Findings 2024\n    url: https://arxiv.org/abs/2404.03098\n    category: evidence_generation_tradeoff\n    role: formal_framework\n    key_finding: >\n      用 multi-objective optimization 探索 performance vs explanation plausibility 的 Pareto frontier。\n      引入 rationale 约束创建 contrastive loss，证实加入 rationale supervision 会降低主任务性能，\n      但存在 Pareto optimal 解平衡两者。\n    relevance_to_evidence_tradeoff: >\n      提供了 performance-explainability trade-off 的形式化框架。\n      我们的 evidence-grounded RE 降 8pp 正是 Pareto frontier 上的一个点。\n      CED reranker 的效果可解读为：将系统从 evidence-constrained 点推向 Pareto frontier，\n      在几乎不牺牲 evidence quality（evi_f1=0.8188）的前提下恢复 RE 性能。\n      Related Work 引用点：evidence generation 的 performance cost 有理论依据。\n\n  - title: \"The Decreasing Value of Chain of Thought in Prompting\"\n    authors: Meincke, Mollick, Mollick, Shapiro\n    year: 2025\n    venue: Wharton Generative AI Labs Technical Report (SSRN)\n    url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5285532\n    category: evidence_generation_tradeoff\n    role: empirical_support\n    key_finding: >\n      现代 reasoning models 上 CoT 收益微弱（4-13%），但 latency 增加 35-600%。\n      更强的模型从显式推理中受益越少。CoT 可能在 easy questions 上引入 errors\n      （variability 增加导致原本正确的被改错）。\n    relevance_to_evidence_tradeoff: >\n      支持\"更强的 SFT 模型不需要在生成时显式输出 evidence\"的论点。\n      我们的 evidence-only SFT 的性能下降符合\"显式推理的边际收益递减\"模式。\n      Related Work 引用点：evidence generation 的 accuracy cost 不是 DocRE-specific，而是 LLM 的普遍趋势。\n\n  # === Category 10: Negative Transfer in Multi-task / Auxiliary-task Learning ===\n\n  - title: \"ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning\"\n    authors: Jiang, Chen et al.\n    year: 2023\n    venue: NeurIPS 2023\n    url: https://arxiv.org/abs/2301.12618\n    category: negative_transfer\n    role: theoretical_framework\n    key_finding: >\n      辅助任务常导致 negative transfer，根因不仅是 gradient conflict 还有 auxiliary-target\n      generalization gap。ForkMerge 周期性 fork 模型为多分支，搜索最优 task weights，\n      动态 merge 过滤有害 task-parameter updates。在多个 benchmark 上减少 negative transfer。\n    relevance_to_evidence_tradeoff: >\n      Evidence generation 作为 auxiliary task 对 RE 的 negative transfer 可用此框架解释：\n      evidence 和 RE 的 gradient 方向不完全对齐，joint training 时 evidence 任务\"拖累\"RE。\n      CED reranker 本质上是将 evidence quality 从 training-time joint objective 解耦到\n      inference-time verification，避免了 training-time 的 negative transfer。\n      Related Work 引用点：auxiliary task 导致主任务性能下降的一般性理论。\n\n  # === Category 11: Faithfulness vs Accuracy / Correctness Trade-off ===\n\n  - title: \"Correctness is not Faithfulness in RAG Attributions\"\n    authors: Wallat, Heuss, de Rijke, Anand\n    year: 2024\n    venue: SIGIR 2025\n    url: https://arxiv.org/abs/2412.18004\n    category: faithfulness_accuracy_tradeoff\n    role: key_conceptual_framework\n    key_finding: >\n      Correctness 和 faithfulness 是独立维度，可能冲突。高达 57% 的 citations 是\n      post-rationalized（事后编造而非真实依据）。Unfaithful attributions 可能 factually correct，\n      但 foster misguided trust。必须同时检查 correctness 和 faithfulness。\n    relevance_to_evidence_tradeoff: >\n      直接相关。我们的 evidence-grounded RE 试图让模型输出 faithful evidence，\n      但这与 relation correctness 产生张力（rel_f1 降 8pp）。\n      CED reranker 通过 NLI verification 确保 evidence 是 faithful 的（非 post-rationalized），\n      同时不牺牲 RE accuracy。\n      Related Work 引用点：correctness-faithfulness 分离的概念框架。\n\n  - title: \"Evaluating Correctness and Faithfulness of Instruction-Following Models for Question Answering\"\n    authors: Adlakha, BehnamGhader, Lu, Meade, Reddy\n    year: 2024\n    venue: TACL 2024\n    url: https://arxiv.org/abs/2307.16877\n    category: faithfulness_accuracy_tradeoff\n    role: evaluation_framework\n    key_finding: >\n      Instruction-following LLMs 在 correctness 上表现可比 fine-tuned models，\n      但 faithfulness 普遍较差——模型会 hallucinate 而非忠实于提供的 evidence。\n      传统 metrics 对 correctness 和 faithfulness 的评估均有缺陷。\n    relevance_to_evidence_tradeoff: >\n      解释了为什么 joint evidence+RE 生成性能差——模型在同时优化 correctness\n      和 faithfulness 时，两个目标存在张力。单纯要求模型\"同时输出正确 triples 和\n      faithful evidence\"是 multi-objective optimization 问题。\n      Related Work 引用点：correctness vs faithfulness 评估方法论。\n\n  - title: \"Towards Faithful Model Explanation in NLP: A Survey\"\n    authors: Lyu, Havaldar, Stein et al.\n    year: 2024\n    venue: Computational Linguistics (MIT Press)\n    url: https://aclanthology.org/2024.cl-2.6/\n    category: faithfulness_accuracy_tradeoff\n    role: comprehensive_survey\n    key_finding: >\n      系统综述 NLP 中 faithful explanation 的定义、评估和生成方法。\n      识别了 faithfulness-performance trade-off 作为核心挑战：\n      更 faithful 的解释不一定更有用，更有用的解释不一定 faithful。\n      提出未来方向包括 multi-objective optimization 和 post-hoc verification。\n    relevance_to_evidence_tradeoff: >\n      权威综述为我们的 evidence generation trade-off 提供广泛文献背景。\n      我们的 CED reranker 正是该综述建议的\"post-hoc verification\"方向的具体实例。\n      Related Work 引用点：faithfulness 研究的全景综述，定位我们的工作。\n\n  # === Category 12: Reranking / Verification as Bridge ===\n\n  - title: \"Genie: Achieving Human Parity in Content-Grounded Datasets Generation\"\n    authors: Yehudai, Carmeli, Mass et al.\n    year: 2024\n    venue: ICLR 2024\n    url: https://arxiv.org/abs/2401.14367\n    category: reranking_verification_bridge\n    role: methodological_precedent\n    key_finding: >\n      三阶段流程：Content Preparation → Generation → NLI-based Filtering。\n      用 fine-tuned T5-11B NLI 模型判断生成内容是否 entailed by source（faithfulness 检验），\n      过滤不 faithful 的生成。在 LFQA、摘要、IE 上达到 human parity。\n    relevance_to_evidence_tradeoff: >\n      方法论上最接近我们的 CED reranker——都是用 NLI verification 作为 post-hoc filter/reranker，\n      在不牺牲主任务质量的前提下确保 grounding quality。\n      GENIE 验证了 NLI-based filtering 在内容生成中的有效性。\n      关键差异：GENIE 是 data generation pipeline 的过滤，我们是 inference-time reranking。\n      Related Work 引用点：NLI-based verification 作为 bridge 的成功先例。\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 6,
        "newStart": 1,
        "newLines": 6,
        "lines": [
          " # Literature Map for faith-evidence-ie (FREIGE)",
          " # Focus: CED-as-training-stabilizer (D024) + RSFT for DocRE",
          "-# Updated: 2026-05-15 (W3 reviewer gap fill + evidence generation trade-off survey)",
          "+# Updated: 2026-05-15 (W4 expanded: +11 papers from literature scan)",
          " ",
          " papers:",
          " "
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

_source line 111_

Now I'll append the 11 new papers at the end of the file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "b58cece1-6773-4b5a-b117-04f3ca9e2a0f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WLZaDm9YPXVH3864tq7z2W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 320,
      "cache_read_input_tokens": 91162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 320
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

_source line 112_

<details open><summary>🔧 Tool call — Read · `toolu_01NvziGnPJxmFWewe1XXicKZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
  "offset": 490,
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "d05dda12-4617-4881-8f4f-25856b707437",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WLZaDm9YPXVH3864tq7z2W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 320,
      "cache_read_input_tokens": 91162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 320
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

_source line 113 · 2026-05-15T22:11:57.387Z_

<details><summary>↩ Tool result · `toolu_01NvziGnPJxmFWewe1XXicKZ`</summary>

```text
490	      Ru-LLM 的规则是数据集级别的频繁模式，CED 是 instance-level 的 evidence faithfulness。
491	
492	  - title: "GLiDRE: Generalist Lightweight model for Document-level Relation Extraction"
493	    authors: Anonymous
494	    year: 2025
495	    venue: arXiv 2508.00757
496	    url: https://arxiv.org/abs/2508.00757
497	    category: llm_docre
498	    role: background
499	    key_finding: >
500	      基于 dual-encoder 的轻量级零/少样本 DocRE 模型，
501	      预训练于 136K 文档的大规模 RE 数据。
502	      fully supervised Re-DocRED test F1=77.83，但这是 encoder-based 非 LLM generative。
503	      zero-shot Re-DocRED test F1=17.32（超越 LLaMA 3.3 70B 和 Mistral-Small 24B）。
504	    results:
505	      re_docred_dev_f1: 77.76
506	      re_docred_test_f1: 77.83
507	      re_docred_zero_shot_test_f1: 17.32
508	      fredo_in_domain_1doc_f1: 13.00
509	      fredo_in_domain_3doc_f1: 15.71
510	      backbone: "dual-encoder (few hundred M params)"
511	    evidence_generation: false
512	    relevance_to_rsft_docre: >
513	      不同范式（encoder-based vs LLM generative）。GLiDRE 的 fully supervised F1=77.83
514	      远超 LLM-based 方法（RelPrior 54.80），但依赖大规模预训练数据和 encoder 架构。
515	      与我们不直接可比——我们关注 LLM generative 范式下的训练优化。
516	
517	  - title: "AutoRE: Document-Level Relation Extraction with Large Language Models"
518	    authors: Anonymous
519	    year: 2024
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "6bc636d1-08ac-4299-b787-9f8466dfff69",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
      "content": "      Ru-LLM 的规则是数据集级别的频繁模式，CED 是 instance-level 的 evidence faithfulness。\n\n  - title: \"GLiDRE: Generalist Lightweight model for Document-level Relation Extraction\"\n    authors: Anonymous\n    year: 2025\n    venue: arXiv 2508.00757\n    url: https://arxiv.org/abs/2508.00757\n    category: llm_docre\n    role: background\n    key_finding: >\n      基于 dual-encoder 的轻量级零/少样本 DocRE 模型，\n      预训练于 136K 文档的大规模 RE 数据。\n      fully supervised Re-DocRED test F1=77.83，但这是 encoder-based 非 LLM generative。\n      zero-shot Re-DocRED test F1=17.32（超越 LLaMA 3.3 70B 和 Mistral-Small 24B）。\n    results:\n      re_docred_dev_f1: 77.76\n      re_docred_test_f1: 77.83\n      re_docred_zero_shot_test_f1: 17.32\n      fredo_in_domain_1doc_f1: 13.00\n      fredo_in_domain_3doc_f1: 15.71\n      backbone: \"dual-encoder (few hundred M params)\"\n    evidence_generation: false\n    relevance_to_rsft_docre: >\n      不同范式（encoder-based vs LLM generative）。GLiDRE 的 fully supervised F1=77.83\n      远超 LLM-based 方法（RelPrior 54.80），但依赖大规模预训练数据和 encoder 架构。\n      与我们不直接可比——我们关注 LLM generative 范式下的训练优化。\n\n  - title: \"AutoRE: Document-Level Relation Extraction with Large Language Models\"\n    authors: Anonymous\n    year: 2024",
      "numLines": 30,
      "startLine": 490,
      "totalLines": 708
    }
  }
}
```

</details>

---

### Tool call

_source line 114_

<details open><summary>🔧 Tool call — Read · `toolu_01JV8WVtLLLNS6ZiBnmgR1hB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
  "offset": 700,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "cb3482c4-1a89-43d5-a526-122e687ecbeb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JBwX6xtDdCxsP4xS1wDfv7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 738,
      "cache_read_input_tokens": 91482,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 738
      },
      "output_tokens": 63,
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

_source line 115 · 2026-05-15T22:12:00.430Z_

<details><summary>↩ Tool result · `toolu_01JV8WVtLLLNS6ZiBnmgR1hB`</summary>

```text
700	      用 fine-tuned T5-11B NLI 模型判断生成内容是否 entailed by source（faithfulness 检验），
701	      过滤不 faithful 的生成。在 LFQA、摘要、IE 上达到 human parity。
702	    relevance_to_evidence_tradeoff: >
703	      方法论上最接近我们的 CED reranker——都是用 NLI verification 作为 post-hoc filter/reranker，
704	      在不牺牲主任务质量的前提下确保 grounding quality。
705	      GENIE 验证了 NLI-based filtering 在内容生成中的有效性。
706	      关键差异：GENIE 是 data generation pipeline 的过滤，我们是 inference-time reranking。
707	      Related Work 引用点：NLI-based verification 作为 bridge 的成功先例。
708	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "d8b84555-55f8-460b-b745-64c8da095a82",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
      "content": "      用 fine-tuned T5-11B NLI 模型判断生成内容是否 entailed by source（faithfulness 检验），\n      过滤不 faithful 的生成。在 LFQA、摘要、IE 上达到 human parity。\n    relevance_to_evidence_tradeoff: >\n      方法论上最接近我们的 CED reranker——都是用 NLI verification 作为 post-hoc filter/reranker，\n      在不牺牲主任务质量的前提下确保 grounding quality。\n      GENIE 验证了 NLI-based filtering 在内容生成中的有效性。\n      关键差异：GENIE 是 data generation pipeline 的过滤，我们是 inference-time reranking。\n      Related Work 引用点：NLI-based verification 作为 bridge 的成功先例。\n",
      "numLines": 9,
      "startLine": 700,
      "totalLines": 708
    }
  }
}
```

</details>

---

### Tool call

_source line 116_

<details open><summary>🔧 Tool call — Edit · `toolu_015BT2B1qGAynsLVBddV35A9`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
  "old_string": "      Related Work 引用点：NLI-based verification 作为 bridge 的成功先例。",
  "new_string": "      Related Work 引用点：NLI-based verification 作为 bridge 的成功先例。\n\n  # === Category 13: Evidence-Grounded RL (NEW - 2026-05-15 scan) ===\n\n  - title: \"EvidenceRL: Reinforcing Evidence Consistency for Trustworthy Language Models\"\n    authors: Ben Tamo, Lu, Marteau, Nnamdi, Wang\n    year: 2026\n    venue: arXiv 2603.19532\n    url: https://arxiv.org/abs/2603.19532\n    category: evidence_grounded_rl\n    role: closest_competitor\n    key_finding: >\n      用 GRPO 同时优化 grounding（evidence entailment）和 correctness（答案准确性）。\n      在 cardiac diagnosis（Llama-3.2-3B）上 F1@3 从 37.0→54.5，grounding 从 47.6→78.2，\n      hallucination 降 5 倍。在 legal reasoning（Llama-3.1-8B）上 faithfulness 从 32.8%→67.6%。\n      核心：证据一致性 reward 不牺牲 task accuracy 的前提下大幅提升 faithfulness。\n    relevance_to_freige: >\n      **最直接的 novelty 威胁。** EvidenceRL 与 FREIGE 共享核心 idea：用 GRPO + evidence faithfulness reward\n      训练更可靠的模型。关键差异：(1) EvidenceRL 在 QA 域（cardiac/legal），不涉及 DocRE 的 structured output；\n      (2) EvidenceRL 未报告 evidence generation 的 performance cost（evidence tax）——它的 grounding 和\n      correctness 同时提升，而我们发现 DocRE 中两者存在 ~8pp 张力；\n      (3) EvidenceRL 不涉及 task decoupling 现象（QLoRA-specific）；\n      (4) EvidenceRL 无 inference-time reranking（CED reranker）。\n      定位策略：EvidenceRL 证明 evidence-grounded RL 在 QA 域有效，\n      我们揭示 DocRE structured output 带来的独特挑战（evidence tax、task decoupling）和解法（CED reranker）。\n\n  # === Category 14: Multi-Objective GRPO (NEW - 2026-05-15 scan) ===\n\n  - title: \"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems\"\n    authors: Ichihara, Jinnai, Morimura, Sakamoto, Mitsuhashi, Uchibe\n    year: 2025\n    venue: arXiv 2509.22047\n    url: https://arxiv.org/abs/2509.22047\n    category: multi_objective_grpo\n    role: related_method\n    key_finding: >\n      GRPO 在多目标设置下易发生 reward hacking——只优化一个目标而牺牲其他目标。\n      MO-GRPO 用 variance-based normalization 自动平衡多个 reward function 的权重，\n      在多臂赌博机、控制、机器翻译、指令遵从四个域上实现稳定学习。\n    relevance_to_freige: >\n      CED reward 本质是多目标（extraction F1 + evidence quality）。MO-GRPO 的分析\n      解释了为什么单一 extraction F1 reward 下模型可能 hack 到 \"忽略 evidence 只抽 triple\" 的策略。\n      CED 从 reward 设计端解决，MO-GRPO 从算法端解决，互补视角。\n\n  - title: \"Multi-Objective and Mixed-Reward Reinforcement Learning via Reward-Decorrelated Policy Optimization\"\n    authors: Bai, Liu, Zhuang, Zhou, Weng, Chen, Wang, Cai\n    year: 2026\n    venue: arXiv 2605.13641\n    url: https://arxiv.org/abs/2605.13641\n    category: multi_objective_grpo\n    role: related_method\n    key_finding: >\n      GRPO 聚合 mixed-reward 时直接求和再归一化会淹没弱信号 reward 维度。\n      RDPO 用 Magnitude-Aware Quantile normalization + Mahalanobis whitening\n      去相关 reward 子空间，改善 LLM post-training 的多目标平衡。\n    relevance_to_freige: >\n      CED reward 的 evidence quality 维度与 extraction F1 天然低相关（r<0.3），\n      RDPO 的理论预测这种低相关多维 reward 更易优化。\n      为 CED 的 training-stabilizing 效果提供另一个理论解释角度。\n\n  # === Category 15: GRPO Theory (NEW - 2026-05-15 scan) ===\n\n  - title: \"GRPO is Secretly a Process Reward Model\"\n    authors: Sullivan, Koller\n    year: 2025\n    venue: under review at ICML 2026\n    url: https://arxiv.org/abs/2509.21154\n    category: grpo_theory\n    role: theoretical_insight\n    key_finding: >\n      证明 GRPO + ORM 在特定条件下等价于 PRM-aware RL objective。\n      提出 λ-GRPO 修正 GRPO 在不均匀 process step 上的 deficiency，\n      在 downstream reasoning 上超越标准 GRPO 且训练更快收敛。\n    relevance_to_freige: >\n      DocRE structured output（multi-triple generation）可视为多步 process。\n      GRPO 隐式的 PRM 性质可能解释了为什么 extraction-only reward\n      在文档级 multi-triple 场景下训练信号不足——单一 outcome reward\n      无法为每个 triple 的生成步骤提供有效 process-level credit assignment。\n      CED 通过 evidence quality 为每个 triple 提供了更细粒度的信号，\n      等效于增强了 process-level reward 的分辨率。\n\n  - title: \"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges\"\n    authors: Wang et al. (23 authors)\n    year: 2026\n    venue: arXiv 2604.13602\n    url: https://arxiv.org/abs/2604.13602\n    category: grpo_theory\n    role: theoretical_framework\n    key_finding: >\n      提出 Proxy Compression Hypothesis (PCH)：reward hacking 源于 objective compression、\n      optimization amplification、evaluator-policy co-adaptation 三者交互。\n      识别了 perception-reasoning decoupling 作为多模态中 reward hacking 的表现之一。\n    relevance_to_freige: >\n      PCH 框架可解释我们观察到的 extraction-evidence decoupling：\n      QLoRA 的 compressed representation space 下，模型可能将 extraction 和 evidence\n      两个子目标压缩到部分重叠的 proxy 空间，导致 optimization amplification\n      使模型专注于更容易优化的 extraction 而忽略 evidence。\n      bf16 下不复现可能因为 full-rank update 的 representation space 更充裕。\n\n  # === Category 16: Training Precision & RL Stability (NEW - 2026-05-15 scan) ===\n\n  - title: \"Defeating the Training-Inference Mismatch via FP16\"\n    authors: Qi, Liu, Zhou, Pang, Du, Lee, Lin\n    year: 2025\n    venue: arXiv 2510.26788\n    url: https://arxiv.org/abs/2510.26788\n    category: training_precision_rl\n    role: key_evidence\n    key_finding: >\n      BF16 在 RL fine-tuning 中引入大的 rounding error 导致 training-inference 不一致，\n      BF16 训练常在 150-600 步崩溃。仅切换到 FP16 即可消除不一致，\n      提供更稳定训练、更快收敛和更优性能，只需改几行代码。\n    relevance_to_freige: >\n      直接相关我们的 QLoRA GRPO 不稳定性发现。QLoRA 在 4-bit 量化基础上\n      使用 bf16/fp16 adapter，量化+低精度的 compounding error 可能是\n      task decoupling 现象的底层原因之一。该论文提供了 precision-instability\n      的机制解释，支持我们 \"QLoRA-specific decoupling\" 的发现——\n      低精度 representation 放大了多目标 RL 中子任务间的 gradient 干扰。\n\n  # === Category 17: RL for Scientific IE (NEW - 2026-05-15 scan) ===\n\n  - title: \"R²GRPO: Better LLMs for Scientific Information Extraction with MimicSFT and Relevance and Rule-induced GRPO\"\n    authors: Li, Di, Liu, Jing, Qiu, Chen\n    year: 2025\n    venue: arXiv 2505.22068\n    url: https://arxiv.org/abs/2505.22068\n    category: rl_for_ie\n    role: related_method\n    key_finding: >\n      两阶段方法：MimicSFT（structured reasoning template，无需高质量 CoT 数据）\n      + R²GRPO（relevance reward + rule-mining reward），\n      在科学信息抽取 RE benchmark 上超越 baseline LLM 和 specialized supervised model。\n    relevance_to_freige: >\n      R²GRPO 的 rule-based reward 设计与我们的 CED reward 有相似动机——\n      都是引入 task-specific 结构化 reward 替代单纯 F1 metric reward。\n      差异：R²GRPO 的 rule 是 dataset-level 频繁模式（类似 Ru-LLM），\n      CED 是 instance-level evidence faithfulness 判别。\n      R²GRPO 未涉及 evidence generation 或 DocRE。\n\n  # === Category 18: LLM Alignment for IE (NEW - 2026-05-15 scan) ===\n\n  - title: \"ADELIE: Aligning Large Language Models on Information Extraction\"\n    authors: Qi, Peng, Wang, Xu, Hou, Li\n    year: 2024\n    venue: EMNLP 2024\n    url: https://arxiv.org/abs/2405.05008\n    category: llm_ie_alignment\n    role: key_baseline\n    key_finding: >\n      构建 IEInstruct 高质量 IE alignment 语料库，用 SFT + DPO 训练 ADELIE。\n      支持 closed/open/on-demand IE 三种模式。\n      基于 LLaMA-2-7B/LLaMA-3.2-3B/Qwen2.5-1.5B，在多个 held-out IE dataset 上达 SOTA。\n    relevance_to_freige: >\n      ADELIE 是 IE alignment 的代表性工作，用 SFT+DPO 替代 RSFT+GRPO。\n      我们的工作与 ADELIE 在 training paradigm 上有可比性——\n      ADELIE 用 DPO（offline preference optimization），我们用 RSFT（offline rejection sampling）。\n      关键差异：ADELIE 覆盖通用 IE，不涉及 evidence generation 或 DocRE-specific challenges；\n      我们专注于 DocRE + evidence grounding 的 trade-off。\n\n  # === Category 19: Unfaithful Reasoning / Post-Rationalization (NEW - 2026-05-15 scan) ===\n\n  - title: \"Chain-of-Thought Is Not Explainability\"\n    authors: Barez et al.\n    year: 2025\n    venue: Oxford WhiteBox Technical Report\n    url: https://aigi.ox.ac.uk/wp-content/uploads/2025/07/Cot_Is_Not_Explainability.pdf\n    category: unfaithful_reasoning\n    role: conceptual_support\n    key_finding: >\n      CoT 仅仅 rationalize（事后合理化）而非 report（忠实报告）模型的真实决策过程。\n      小的操纵即可改变 CoT 的推理链但不改变模型实际决策。\n      模型会 silently correct 错误而不在 CoT 中体现。\n    relevance_to_freige: >\n      支持我们 evidence generation 分析的一个维度：模型生成的 evidence sentences\n      可能是 post-rationalization 而非真正驱动 RE 决策的信号。\n      CED reranker 用 NLI verification 检查 evidence 的实际 entailment\n      而非信任模型自报告的 evidence，本质上是对 post-rationalization 的防御。\n\n  - title: \"Characterizing Large Language Models as Rationalizers of Knowledge-Grounded Dialogue\"\n    authors: Anonymous\n    year: 2024\n    venue: ACL Findings 2024\n    url: https://aclanthology.org/2024.findings-acl.484.pdf\n    category: unfaithful_reasoning\n    role: empirical_evidence\n    key_finding: >\n      LLM 在 knowledge-grounded dialogue 中普遍表现为 rationalizer 而非 faithful reasoner，\n      模型的 explanation 与其实际使用的 knowledge evidence 不一致。\n    relevance_to_freige: >\n      与我们的发现呼应：DocRE 中模型可能输出看似合理的 evidence sentences\n      但实际 RE 决策并不依赖这些 evidence。这解释了为什么 joint evidence+RE 生成\n      对 RE 性能有负面影响——模型在学习生成 \"合理化解释\" 而非 \"可靠推理\"。\n\n  # === Category 20: Latent vs Explicit Reasoning Trade-off (NEW - 2026-05-15 scan) ===\n\n  - title: \"Reasoning Beyond Language: A Comprehensive Survey on Latent Chain-of-Thought Reasoning\"\n    authors: Chen, Zhao, Xia, Lu, Wang, Chen, Zhang, Wang, Li, Shen\n    year: 2025\n    venue: arXiv 2505.16782\n    url: https://arxiv.org/abs/2505.16782\n    category: latent_vs_explicit_reasoning\n    role: survey\n    key_finding: >\n      Latent CoT 将推理从显式 token generation 解耦到 hidden state computation，\n      在多项任务上达到与显式 CoT 相当或更优的性能，同时推理速度提升 20 倍以上。\n      显式 CoT 的 sequential token-level 推理是 applicability 的瓶颈。\n    relevance_to_freige: >\n      为 evidence generation trade-off 提供更广泛的理论视角：\n      evidence sentences 作为显式推理步骤（类似 CoT tokens）可能不是最优的推理形式。\n      我们的 CED reranker 可被视为将 evidence reasoning 从 generation-time 显式推理\n      转移到 inference-time 的 NLI-based 验证——类似 latent-to-explicit 的范式转换，\n      但方向相反：不是让推理隐式化，而是让验证外部化。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "f206345d-f3b9-4f56-b9da-6010d64160b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RCHiZSbfqD9G7727fwaTdS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 389,
      "cache_read_input_tokens": 92220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 389
      },
      "output_tokens": 69,
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

_source line 117 · 2026-05-15T22:13:29.852Z_

<details><summary>↩ Tool result · `toolu_015BT2B1qGAynsLVBddV35A9`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "077e6a6d-800d-4f25-b7f8-6d76c5825018",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
    "oldString": "      Related Work 引用点：NLI-based verification 作为 bridge 的成功先例。",
    "newString": "      Related Work 引用点：NLI-based verification 作为 bridge 的成功先例。\n\n  # === Category 13: Evidence-Grounded RL (NEW - 2026-05-15 scan) ===\n\n  - title: \"EvidenceRL: Reinforcing Evidence Consistency for Trustworthy Language Models\"\n    authors: Ben Tamo, Lu, Marteau, Nnamdi, Wang\n    year: 2026\n    venue: arXiv 2603.19532\n    url: https://arxiv.org/abs/2603.19532\n    category: evidence_grounded_rl\n    role: closest_competitor\n    key_finding: >\n      用 GRPO 同时优化 grounding（evidence entailment）和 correctness（答案准确性）。\n      在 cardiac diagnosis（Llama-3.2-3B）上 F1@3 从 37.0→54.5，grounding 从 47.6→78.2，\n      hallucination 降 5 倍。在 legal reasoning（Llama-3.1-8B）上 faithfulness 从 32.8%→67.6%。\n      核心：证据一致性 reward 不牺牲 task accuracy 的前提下大幅提升 faithfulness。\n    relevance_to_freige: >\n      **最直接的 novelty 威胁。** EvidenceRL 与 FREIGE 共享核心 idea：用 GRPO + evidence faithfulness reward\n      训练更可靠的模型。关键差异：(1) EvidenceRL 在 QA 域（cardiac/legal），不涉及 DocRE 的 structured output；\n      (2) EvidenceRL 未报告 evidence generation 的 performance cost（evidence tax）——它的 grounding 和\n      correctness 同时提升，而我们发现 DocRE 中两者存在 ~8pp 张力；\n      (3) EvidenceRL 不涉及 task decoupling 现象（QLoRA-specific）；\n      (4) EvidenceRL 无 inference-time reranking（CED reranker）。\n      定位策略：EvidenceRL 证明 evidence-grounded RL 在 QA 域有效，\n      我们揭示 DocRE structured output 带来的独特挑战（evidence tax、task decoupling）和解法（CED reranker）。\n\n  # === Category 14: Multi-Objective GRPO (NEW - 2026-05-15 scan) ===\n\n  - title: \"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems\"\n    authors: Ichihara, Jinnai, Morimura, Sakamoto, Mitsuhashi, Uchibe\n    year: 2025\n    venue: arXiv 2509.22047\n    url: https://arxiv.org/abs/2509.22047\n    category: multi_objective_grpo\n    role: related_method\n    key_finding: >\n      GRPO 在多目标设置下易发生 reward hacking——只优化一个目标而牺牲其他目标。\n      MO-GRPO 用 variance-based normalization 自动平衡多个 reward function 的权重，\n      在多臂赌博机、控制、机器翻译、指令遵从四个域上实现稳定学习。\n    relevance_to_freige: >\n      CED reward 本质是多目标（extraction F1 + evidence quality）。MO-GRPO 的分析\n      解释了为什么单一 extraction F1 reward 下模型可能 hack 到 \"忽略 evidence 只抽 triple\" 的策略。\n      CED 从 reward 设计端解决，MO-GRPO 从算法端解决，互补视角。\n\n  - title: \"Multi-Objective and Mixed-Reward Reinforcement Learning via Reward-Decorrelated Policy Optimization\"\n    authors: Bai, Liu, Zhuang, Zhou, Weng, Chen, Wang, Cai\n    year: 2026\n    venue: arXiv 2605.13641\n    url: https://arxiv.org/abs/2605.13641\n    category: multi_objective_grpo\n    role: related_method\n    key_finding: >\n      GRPO 聚合 mixed-reward 时直接求和再归一化会淹没弱信号 reward 维度。\n      RDPO 用 Magnitude-Aware Quantile normalization + Mahalanobis whitening\n      去相关 reward 子空间，改善 LLM post-training 的多目标平衡。\n    relevance_to_freige: >\n      CED reward 的 evidence quality 维度与 extraction F1 天然低相关（r<0.3），\n      RDPO 的理论预测这种低相关多维 reward 更易优化。\n      为 CED 的 training-stabilizing 效果提供另一个理论解释角度。\n\n  # === Category 15: GRPO Theory (NEW - 2026-05-15 scan) ===\n\n  - title: \"GRPO is Secretly a Process Reward Model\"\n    authors: Sullivan, Koller\n    year: 2025\n    venue: under review at ICML 2026\n    url: https://arxiv.org/abs/2509.21154\n    category: grpo_theory\n    role: theoretical_insight\n    key_finding: >\n      证明 GRPO + ORM 在特定条件下等价于 PRM-aware RL objective。\n      提出 λ-GRPO 修正 GRPO 在不均匀 process step 上的 deficiency，\n      在 downstream reasoning 上超越标准 GRPO 且训练更快收敛。\n    relevance_to_freige: >\n      DocRE structured output（multi-triple generation）可视为多步 process。\n      GRPO 隐式的 PRM 性质可能解释了为什么 extraction-only reward\n      在文档级 multi-triple 场景下训练信号不足——单一 outcome reward\n      无法为每个 triple 的生成步骤提供有效 process-level credit assignment。\n      CED 通过 evidence quality 为每个 triple 提供了更细粒度的信号，\n      等效于增强了 process-level reward 的分辨率。\n\n  - title: \"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges\"\n    authors: Wang et al. (23 authors)\n    year: 2026\n    venue: arXiv 2604.13602\n    url: https://arxiv.org/abs/2604.13602\n    category: grpo_theory\n    role: theoretical_framework\n    key_finding: >\n      提出 Proxy Compression Hypothesis (PCH)：reward hacking 源于 objective compression、\n      optimization amplification、evaluator-policy co-adaptation 三者交互。\n      识别了 perception-reasoning decoupling 作为多模态中 reward hacking 的表现之一。\n    relevance_to_freige: >\n      PCH 框架可解释我们观察到的 extraction-evidence decoupling：\n      QLoRA 的 compressed representation space 下，模型可能将 extraction 和 evidence\n      两个子目标压缩到部分重叠的 proxy 空间，导致 optimization amplification\n      使模型专注于更容易优化的 extraction 而忽略 evidence。\n      bf16 下不复现可能因为 full-rank update 的 representation space 更充裕。\n\n  # === Category 16: Training Precision & RL Stability (NEW - 2026-05-15 scan) ===\n\n  - title: \"Defeating the Training-Inference Mismatch via FP16\"\n    authors: Qi, Liu, Zhou, Pang, Du, Lee, Lin\n    year: 2025\n    venue: arXiv 2510.26788\n    url: https://arxiv.org/abs/2510.26788\n    category: training_precision_rl\n    role: key_evidence\n    key_finding: >\n      BF16 在 RL fine-tuning 中引入大的 rounding error 导致 training-inference 不一致，\n      BF16 训练常在 150-600 步崩溃。仅切换到 FP16 即可消除不一致，\n      提供更稳定训练、更快收敛和更优性能，只需改几行代码。\n    relevance_to_freige: >\n      直接相关我们的 QLoRA GRPO 不稳定性发现。QLoRA 在 4-bit 量化基础上\n      使用 bf16/fp16 adapter，量化+低精度的 compounding error 可能是\n      task decoupling 现象的底层原因之一。该论文提供了 precision-instability\n      的机制解释，支持我们 \"QLoRA-specific decoupling\" 的发现——\n      低精度 representation 放大了多目标 RL 中子任务间的 gradient 干扰。\n\n  # === Category 17: RL for Scientific IE (NEW - 2026-05-15 scan) ===\n\n  - title: \"R²GRPO: Better LLMs for Scientific Information Extraction with MimicSFT and Relevance and Rule-induced GRPO\"\n    authors: Li, Di, Liu, Jing, Qiu, Chen\n    year: 2025\n    venue: arXiv 2505.22068\n    url: https://arxiv.org/abs/2505.22068\n    category: rl_for_ie\n    role: related_method\n    key_finding: >\n      两阶段方法：MimicSFT（structured reasoning template，无需高质量 CoT 数据）\n      + R²GRPO（relevance reward + rule-mining reward），\n      在科学信息抽取 RE benchmark 上超越 baseline LLM 和 specialized supervised model。\n    relevance_to_freige: >\n      R²GRPO 的 rule-based reward 设计与我们的 CED reward 有相似动机——\n      都是引入 task-specific 结构化 reward 替代单纯 F1 metric reward。\n      差异：R²GRPO 的 rule 是 dataset-level 频繁模式（类似 Ru-LLM），\n      CED 是 instance-level evidence faithfulness 判别。\n      R²GRPO 未涉及 evidence generation 或 DocRE。\n\n  # === Category 18: LLM Alignment for IE (NEW - 2026-05-15 scan) ===\n\n  - title: \"ADELIE: Aligning Large Language Models on Information Extraction\"\n    authors: Qi, Peng, Wang, Xu, Hou, Li\n    year: 2024\n    venue: EMNLP 2024\n    url: https://arxiv.org/abs/2405.05008\n    category: llm_ie_alignment\n    role: key_baseline\n    key_finding: >\n      构建 IEInstruct 高质量 IE alignment 语料库，用 SFT + DPO 训练 ADELIE。\n      支持 closed/open/on-demand IE 三种模式。\n      基于 LLaMA-2-7B/LLaMA-3.2-3B/Qwen2.5-1.5B，在多个 held-out IE dataset 上达 SOTA。\n    relevance_to_freige: >\n      ADELIE 是 IE alignment 的代表性工作，用 SFT+DPO 替代 RSFT+GRPO。\n      我们的工作与 ADELIE 在 training paradigm 上有可比性——\n      ADELIE 用 DPO（offline preference optimization），我们用 RSFT（offline rejection sampling）。\n      关键差异：ADELIE 覆盖通用 IE，不涉及 evidence generation 或 DocRE-specific challenges；\n      我们专注于 DocRE + evidence grounding 的 trade-off。\n\n  # === Category 19: Unfaithful Reasoning / Post-Rationalization (NEW - 2026-05-15 scan) ===\n\n  - title: \"Chain-of-Thought Is Not Explainability\"\n    authors: Barez et al.\n    year: 2025\n    venue: Oxford WhiteBox Technical Report\n    url: https://aigi.ox.ac.uk/wp-content/uploads/2025/07/Cot_Is_Not_Explainability.pdf\n    category: unfaithful_reasoning\n    role: conceptual_support\n    key_finding: >\n      CoT 仅仅 rationalize（事后合理化）而非 report（忠实报告）模型的真实决策过程。\n      小的操纵即可改变 CoT 的推理链但不改变模型实际决策。\n      模型会 silently correct 错误而不在 CoT 中体现。\n    relevance_to_freige: >\n      支持我们 evidence generation 分析的一个维度：模型生成的 evidence sentences\n      可能是 post-rationalization 而非真正驱动 RE 决策的信号。\n      CED reranker 用 NLI verification 检查 evidence 的实际 entailment\n      而非信任模型自报告的 evidence，本质上是对 post-rationalization 的防御。\n\n  - title: \"Characterizing Large Language Models as Rationalizers of Knowledge-Grounded Dialogue\"\n    authors: Anonymous\n    year: 2024\n    venue: ACL Findings 2024\n    url: https://aclanthology.org/2024.findings-acl.484.pdf\n    category: unfaithful_reasoning\n    role: empirical_evidence\n    key_finding: >\n      LLM 在 knowledge-grounded dialogue 中普遍表现为 rationalizer 而非 faithful reasoner，\n      模型的 explanation 与其实际使用的 knowledge evidence 不一致。\n    relevance_to_freige: >\n      与我们的发现呼应：DocRE 中模型可能输出看似合理的 evidence sentences\n      但实际 RE 决策并不依赖这些 evidence。这解释了为什么 joint evidence+RE 生成\n      对 RE 性能有负面影响——模型在学习生成 \"合理化解释\" 而非 \"可靠推理\"。\n\n  # === Category 20: Latent vs Explicit Reasoning Trade-off (NEW - 2026-05-15 scan) ===\n\n  - title: \"Reasoning Beyond Language: A Comprehensive Survey on Latent Chain-of-Thought Reasoning\"\n    authors: Chen, Zhao, Xia, Lu, Wang, Chen, Zhang, Wang, Li, Shen\n    year: 2025\n    venue: arXiv 2505.16782\n    url: https://arxiv.org/abs/2505.16782\n    category: latent_vs_explicit_reasoning\n    role: survey\n    key_finding: >\n      Latent CoT 将推理从显式 token generation 解耦到 hidden state computation，\n      在多项任务上达到与显式 CoT 相当或更优的性能，同时推理速度提升 20 倍以上。\n      显式 CoT 的 sequential token-level 推理是 applicability 的瓶颈。\n    relevance_to_freige: >\n      为 evidence generation trade-off 提供更广泛的理论视角：\n      evidence sentences 作为显式推理步骤（类似 CoT tokens）可能不是最优的推理形式。\n      我们的 CED reranker 可被视为将 evidence reasoning 从 generation-time 显式推理\n      转移到 inference-time 的 NLI-based 验证——类似 latent-to-explicit 的范式转换，\n      但方向相反：不是让推理隐式化，而是让验证外部化。",
    "originalFile": "# Literature Map for faith-evidence-ie (FREIGE)\n# Focus: CED-as-training-stabilizer (D024) + RSFT for DocRE\n# Updated: 2026-05-15 (W4 expanded: +11 papers from literature scan)\n\npapers:\n\n  # === Category 1: Reward Diversity / Reward Shaping for RL Stability ===\n\n  - title: \"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization\"\n    authors: NVIDIA Labs\n    year: 2025\n    venue: ICML 2026\n    url: https://arxiv.org/abs/2601.05242\n    category: reward_diversity\n    role: closest_prior_work\n    key_finding: >\n      直接将 GRPO 应用于多 reward 组合时，不同 rollout 的 reward 组合在归一化后 collapse 为相同 advantage 值，\n      降低训练信号分辨率导致收敛失败。GDPO 对每个 reward 独立做 group-wise normalization 再聚合，\n      保留多 reward 的相对差异，显著提升训练稳定性。\n    relevance_to_ced_stabilizer: >\n      最直接相关。CED reward 本质上引入了独立于 extraction F1 的 reward 维度（evidence quality），\n      GDPO 的理论分析解释了为什么多维 reward 比单一 reward 更稳定——独立 reward 维度防止 advantage collapse。\n      但 GDPO 是方法论贡献，CED 是 task-specific reward 设计自然具备了这一特性。\n\n  - title: \"DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of LLMs\"\n    authors: Xiwen Chen et al.\n    year: 2025\n    venue: arXiv 2505.09655\n    url: https://arxiv.org/abs/2505.09655\n    category: reward_diversity\n    role: related_method\n    key_finding: >\n      GRPO 的标量 reward 无法区分语义多样但得分相同的输出（diversity-quality inconsistency）。\n      DRA 用子模互信息（SMI）对 reward 加权，给多样性高的 completion 更大权重，\n      等价于 Inverse Propensity Scoring 去偏，防止 policy 坍缩到先验模式。\n    relevance_to_ced_stabilizer: >\n      DRA 通过后处理 reward 注入多样性信号；CED 的 reward 本身就内含对比结构自然提供 diversity 信号。\n      机制互补但来源不同——CED 是 reward design 层面，DRA 是 optimization 层面。\n\n  - title: \"Shrinking the Variance: Shrinkage Baselines for RL with Verifiable Rewards\"\n    authors: Guanning Zeng et al.\n    year: 2025\n    venue: arXiv 2511.03710\n    url: https://arxiv.org/abs/2511.03710\n    category: reward_diversity\n    role: theoretical_support\n    key_finding: >\n      RLVR 中 per-prompt 均值 baseline 在低 generation 数下估计不准导致高 variance 梯度。\n      用 James-Stein shrinkage 混合 per-prompt 和 cross-prompt 均值，\n      构造可证明更低 variance 的 policy gradient estimator。\n    relevance_to_ced_stabilizer: >\n      理论支持：reward variance 对 gradient estimation 质量至关重要。\n      CED 的额外 reward 维度提供更丰富的 per-group variance，间接起到 variance 维持效果。\n\n  - title: \"Reward Shaping to Mitigate Reward Hacking in RLHF\"\n    authors: Anonymous\n    year: 2025\n    venue: arXiv 2502.18770\n    url: https://arxiv.org/abs/2502.18770\n    category: reward_diversity\n    role: background\n    key_finding: >\n      RL reward 应有界且先快速增长后缓慢收敛。系统研究 reward shaping 原则，\n      好的 reward 形状能抑制 reward hacking 并提升训练稳定性。\n    relevance_to_ced_stabilizer: >\n      CED reward 的 0-1 对比判别结构天然满足有界性，\n      且 evidence quality 的渐进提升符合\"先快后慢\"的 reward shaping 原则。\n\n  # === Category 2: Mode Collapse Prevention in GRPO/RLHF ===\n\n  - title: \"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\"\n    authors: ByteDance Seed, Tsinghua AIR\n    year: 2025\n    venue: NeurIPS 2025\n    url: https://arxiv.org/abs/2503.14476\n    category: mode_collapse_prevention\n    role: key_baseline\n    key_finding: >\n      Naive GRPO 存在 entropy collapse（policy 熵快速下降→输出同质化）。\n      根因：clipping 不对称性——概率 0.01 的 token 最多增到 0.012，而概率 0.9 的 token 可达 1.08，\n      低概率 token 难以增长，抑制探索。DAPO 提出 Clip-Higher（εhigh=0.28 > εlow=0.2）\n      为低概率 token 留更大增长空间，加 Dynamic Sampling 过滤 accuracy=0 或 1 的 prompt\n      （这些 prompt 产生零梯度，降低有效 batch size）。在 AIME 2024 达 50 分超越 DeepSeek-R1-Zero。\n    relevance_to_ced_stabilizer: >\n      DAPO 从 optimization 技巧角度解决 entropy collapse。CED reward 从 reward design 层面\n      防止 mode collapse——evidence quality 维度确保 reward 组内有足够 variance，\n      不会出现 all-same-reward 的零梯度 prompt。DAPO 的 Dynamic Sampling 过滤 accuracy=0/1 prompt\n      与我们观察到的 frac_zero_std→0.8 现象本质相同：extraction-only reward 下大量 prompt\n      产生零 advantage，CED 从源头（reward 设计）而非后处理（过滤）解决这个问题。\n\n  - title: \"Dr. GRPO: Removing Optimization Bias in GRPO\"\n    authors: Liu et al.\n    year: 2025\n    venue: COLM 2025\n    url: https://arxiv.org/abs/2503.20783\n    category: mode_collapse_prevention\n    role: related_analysis\n    key_finding: >\n      GRPO 的 std 归一化引入两个 bias：(1) difficulty bias——std(r) 归一化对低 variance 组\n      （全对/全错）给予过高 advantage 权重，trivial question 主导训练信号；\n      (2) length bias——per-token loss 的 1/|o_i| 项使长的错误回答被 under-penalize。\n      当 std(r)→0 时 advantage 爆炸或未定义，梯度数值不稳定。\n      Dr. GRPO 移除 std 归一化，用无偏 Monte Carlo advantage：Ã = R(q,o_i) - mean(R)。\n    relevance_to_ced_stabilizer: >\n      与我们的实验发现高度一致：extraction-only reward 下 frac_zero_std→0.8 正是\n      Dr. GRPO 分析的 difficulty bias 极端情况——大量 prompt 的所有 rollout 得到相同 F1，\n      std→0 导致 advantage 异常。CED 通过增加 reward 维度天然维持 reward_std>0，\n      从 reward 设计而非算法修改角度避免了 Dr. GRPO 发现的 bias。\n\n  - title: \"GVPO: Group Variance Policy Optimization for LLM Post-Training\"\n    authors: Anonymous\n    year: 2025\n    venue: NeurIPS 2025\n    url: https://arxiv.org/abs/2504.19599\n    category: mode_collapse_prevention\n    role: alternative_framework\n    key_finding: >\n      将 KL 约束 reward 最大化的解析解直接嵌入梯度权重，\n      variance 项自然平衡 exploration 与 exploitation，维持适度 entropy。\n    relevance_to_ced_stabilizer: >\n      GVPO 的 variance 项机制与 CED 维持 reward variance 的效果功能类似，\n      但 GVPO 是算法层面 implicit regularization，CED 是 reward 层面 explicit structure。\n\n  - title: \"REINFORCE++: Stabilizing Critic-Free Policy Optimization with Global Advantage Normalization\"\n    authors: Jian Hu et al.\n    year: 2025\n    venue: arXiv 2501.03262\n    url: https://arxiv.org/abs/2501.03262\n    category: mode_collapse_prevention\n    role: related_method\n    key_finding: >\n      Prompt-level (local) advantage normalization 导致不准确估计和过拟合。\n      Global batch normalization 提供更稳定、理论无偏的 gradient estimator。\n    relevance_to_ced_stabilizer: >\n      解决 local normalization 的 variance 问题；CED 从 reward 端增加 variance 来源。\n      两者在不同层面解决同一问题：防止 gradient signal 消失。\n\n  - title: \"DiverseGRPO: Mitigating Mode Collapse in Image Generation via Diversity-Aware GRPO\"\n    authors: Henglin Liu et al.\n    year: 2025\n    venue: arXiv 2512.21514\n    url: https://arxiv.org/abs/2512.21514\n    category: mode_collapse_prevention\n    role: parallel_work\n    key_finding: >\n      图像生成中 GRPO 后期输出同质化。distributional reward modeling（谱聚类+exploratory reward）\n      和 structure-aware regularization 实现 13-18% 语义多样性提升。\n    relevance_to_ced_stabilizer: >\n      跨域验证了 GRPO mode collapse 的普遍性，distributional reward 思路与 CED 精神相近——\n      都是通过 reward 层面结构化信号维持输出多样性。\n\n  - title: \"Why GRPO Needs Normalization: A Local-Curvature Perspective on Adaptive Gradients\"\n    authors: Anonymous\n    year: 2025\n    venue: arXiv 2601.23135\n    url: https://arxiv.org/abs/2601.23135\n    category: mode_collapse_prevention\n    role: theoretical_support\n    key_finding: >\n      GRPO 的 reward_std 归一化在温和条件下提供严格优于未归一化 REINFORCE 的收敛速率，\n      收益由 prompt 间平均 reward std 刻画。\n    relevance_to_ced_stabilizer: >\n      直接理论支撑：reward_std 越大收敛越好。CED 通过 evidence quality 维度维持高 reward_std，\n      从该理论看 CED 的稳定性优势是 reward_std 维持带来的收敛速率优势。\n\n  # === Category 3: Contrastive Rewards in RL ===\n\n  - title: \"Improving Reinforcement Learning from Human Feedback Using Contrastive Rewards\"\n    authors: Shen, Zhang et al.\n    year: 2024\n    venue: arXiv 2403.07708\n    url: https://arxiv.org/abs/2403.07708\n    category: contrastive_reward\n    role: closest_contrastive_precedent\n    key_finding: >\n      两步机制：(1) 离线采样 baseline response；(2) 用 baseline 计算 contrastive reward\n      作为 PPO 的 penalty 项。效果：惩罚 reward uncertainty、根据任务难度自适应校准、\n      减少 PPO 中的 variance。在 TL;DR 和 HH-RLHF 上持续优于标准 RLHF。\n    relevance_to_ced_stabilizer: >\n      最接近的对比 reward 先例。关键差异：(1) 它是对 learned RM 输出的后处理对比，\n      CED 是 reward function 本身就是对比判别（evidence vs. corrupted evidence）；\n      (2) 它在 PPO 中验证，CED 在 GRPO 中验证；\n      (3) 它是 domain-agnostic penalty，CED 是 task-specific faithfulness signal。\n      stabilizing 机制相通但实现路径根本不同。\n\n  - title: \"Improving Discriminative Capability of Reward Models in RLHF Using Contrastive Learning\"\n    authors: Anonymous\n    year: 2024\n    venue: EMNLP 2024\n    url: https://aclanthology.org/2024.emnlp-main.852/\n    category: contrastive_reward\n    role: related_method\n    key_finding: >\n      无监督对比损失训练 reward model 充分捕捉对比数据区分度，\n      带来更稳定的 PPO 训练 return 和 reward。\n    relevance_to_ced_stabilizer: >\n      验证对比训练 reward model → 更稳定 RL 训练链条。CED 不是对比训练 reward model，\n      而是 reward function 本身就是对比判别，但 stabilizing 机制相通。\n\n  - title: \"Contrastive Preference Learning: Learning from Human Feedback without RL\"\n    authors: Anonymous\n    year: 2024\n    venue: ICLR 2025\n    url: https://openreview.net/forum?id=iX1RjVQODj\n    category: contrastive_reward\n    role: background\n    key_finding: >\n      将 preference learning 重新表述为对比学习问题，无需显式 RL 即可从人类反馈中学习。\n    relevance_to_ced_stabilizer: >\n      对比框架在 preference alignment 中的通用性。CED 可被视为 task-specific contrastive preference signal。\n\n  # === Category 4: Evidence-Based Rewards in IE/NLP ===\n\n  - title: \"Drift: Enhancing LLM Faithfulness in Rationale Generation\"\n    authors: Anonymous\n    year: 2025\n    venue: ACL 2025\n    url: https://aclanthology.org/2025.acl-long.340.pdf\n    category: evidence_reward\n    role: related_method\n    key_finding: >\n      用 faithfulness reward 引导 LLM 生成更可靠的 rationale，提升 CoT 推理事实一致性。\n    relevance_to_ced_stabilizer: >\n      Faithfulness reward 用于生成质量的先例。CED 中 evidence discrimination\n      本质上也是 faithfulness 信号——判断证据是否忠实支持抽取结果。\n\n  - title: \"Fine-Grained NLI-Based Faithfulness Evaluation for Diverse Summarisation Tasks (INFUSE)\"\n    authors: Anonymous\n    year: 2024\n    venue: EACL 2024\n    url: https://aclanthology.org/2024.eacl-long.102/\n    category: evidence_reward\n    role: background\n    key_finding: >\n      变长前提+简化假设的细粒度 NLI faithfulness 评估，超越传统 NLI 在多任务摘要上的表现。\n    relevance_to_ced_stabilizer: >\n      NLI 作为 faithfulness 评估工具的进展。CED 中 NLI 组件用于判断 evidence 对 triple 的支持度。\n\n  - title: \"Enhancing Cross-Evidence Reasoning Graph for Document-Level Relation Extraction\"\n    authors: Anonymous\n    year: 2024\n    venue: PMC/Bioinformatics 2024\n    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11232587/\n    category: evidence_reward\n    role: background\n    key_finding: >\n      文档级关系抽取中用 cross-evidence reasoning graph 增强跨证据推理。\n    relevance_to_ced_stabilizer: >\n      DocRE 中 evidence 的重要性。但用 evidence 作为模型输入特征，\n      我们用 evidence quality 作为 RL reward 信号——定位根本不同。\n\n  # === Category 5: Multi-Objective RL for Text Generation ===\n\n  - title: \"Confronting Reward Model Overoptimization with Constrained RLHF\"\n    authors: Anonymous\n    year: 2025\n    venue: OpenReview\n    url: https://openreview.net/forum?id=gkfUvn0fLU\n    category: multi_objective_rl\n    role: related_analysis\n    key_finding: >\n      多组件 RM 的 overoptimization 研究。component RM 间的相关性显著影响 overoptimization 临界点，\n      用 constrained MDP 防止超出适当边界。\n    relevance_to_ced_stabilizer: >\n      CED 引入了与 extraction F1 低相关的 reward component（evidence quality），\n      根据该论文分析低相关多组件 reward 更不易 overoptimize，\n      可能是 CED 稳定性的另一个理论解释角度。\n\n  - title: \"On-Policy RL with Optimal Reward Baseline\"\n    authors: Anonymous\n    year: 2025\n    venue: arXiv 2505.23585\n    url: https://arxiv.org/abs/2505.23585\n    category: multi_objective_rl\n    role: theoretical_support\n    key_finding: >\n      Optimal baseline 一致性地实现更高训练 reward 和更高 entropy，\n      有效稳定训练并促进更多样的 policy exploration。\n    relevance_to_ced_stabilizer: >\n      CED reward 的多维特性可能起到类似 optimal baseline 效果——\n      evidence quality 维度为 advantage estimation 提供更丰富的参照信号。\n\n  # === Category 6: RSFT Methodology & Theory ===\n\n  - title: \"A Minimalist Approach to LLM Reasoning: from Rejection Sampling to Reinforce\"\n    authors: Xiao et al.\n    year: 2025\n    venue: arXiv 2504.11343\n    url: https://arxiv.org/abs/2504.11343\n    category: rsft_methodology\n    role: key_theoretical_support\n    key_finding: >\n      RAFT（简单 rejection sampling baseline）在数学推理上与 GRPO/PPO 表现相当。\n      消融实验表明 GRPO 的主要优势来自丢弃全错 prompt 而非 reward normalization。\n      提出 Reinforce-Rej，在 RAFT 基础上过滤全对和全错 sample。\n      关键洞察：GRPO 和 RAFT 的核心区别在于负样本处理——GRPO 混合正负样本训练，\n      RAFT 只用正样本，但 RAFT 仍能达到相当性能，说明 rejection sampling 的简单性被低估了。\n    relevance_to_rsft_docre: >\n      直接支持我们的设计选择：(1) RSFT 在 DocRE 上成功而 GRPO 失败，\n      与该论文发现一致——rejection sampling 的 offline 特性天然避免了 catastrophic forgetting；\n      (2) GRPO 主要优势来自过滤全错 prompt，这与我们 RSFT 的 reward-based filtering 机制相同；\n      (3) DocRE structured output 比 math reasoning 更难用 online RL 优化，\n      强化了 offline RSFT 的合理性。\n\n  - title: \"Beyond Rejection Sampling: Trajectory Fusion for Scaling Mathematical Reasoning (TrajFusion)\"\n    authors: Jie Deng et al.\n    year: 2026\n    venue: arXiv 2602.04391\n    url: https://arxiv.org/abs/2602.04391\n    category: rsft_methodology\n    role: method_component\n    key_finding: >\n      传统 RSFT 只用正确轨迹，丢弃错误轨迹。TrajFusion 将错误和正确轨迹交替拼接，\n      显式建模试错推理过程，在困难数学问题上显著超越标准 RFT。\n    relevance_to_rsft_docre: >\n      Future work 方向：可考虑在 DocRE RSFT 中融合失败样本的信息。\n      但 DocRE 的结构化输出（JSON triple）不同于 math 的 chain-of-thought，\n      融合方式需要重新设计。\n\n  - title: \"Rejection Sampling Based Fine Tuning Secretly Performs PPO\"\n    authors: Anonymous\n    year: 2025\n    venue: ICML 2025\n    url: https://openreview.net/forum?id=yQ2UivKlir\n    category: rsft_methodology\n    role: theoretical_support\n    key_finding: >\n      建立 RSFT 与 PPO 之间的理论联系：rejection sampling fine-tuning\n      在特定条件下隐式执行 PPO with marginal KL constraints。\n    relevance_to_rsft_docre: >\n      为 RSFT 的有效性提供理论解释。我们的 RSFT 成功可被视为\n      隐式执行了 constrained policy optimization，\n      避免了显式 GRPO 在 structured output 上的不稳定性。\n\n  # === Category 7: RL for Information Extraction ===\n\n  - title: \"R1-RE: Cross-Domain Relation Extraction with RLVR\"\n    authors: Runpeng Dai, Tong Zheng et al.\n    year: 2025\n    venue: arXiv 2507.04642\n    url: https://arxiv.org/abs/2507.04642\n    category: rl_for_ie\n    role: direct_competitor\n    key_finding: >\n      首个将 RLVR（GRPO + verifiable reward）用于关系抽取的框架。\n      将 RE 重构为推理任务，R1-RE-7B 在跨域 OOD 准确率约 70%，媲美 GPT-4o。\n      Reward 设计：format reward (+1/-3) + metric reward (+2/-1.5)，先验证格式再加准确度。\n      triplet extraction 用 F1-based reward（entity weight=1, triplet weight=3）。\n      未报告 catastrophic forgetting——GRPO 训练后在 MATH-500/IFEval/GPQA 上性能不降反升，\n      说明句子级 RE 的简单 reward 结构足以稳定 GRPO 训练。\n    results:\n      sem2010_in_domain: 91.8\n      sem2010_ood: 66.5\n      mdkg_in_domain: 88.1\n      mdkg_ood: 65.8\n    evidence_generation: false\n    relevance_to_rsft_docre: >\n      最直接竞争者。关键差异与讨论：\n      (1) R1-RE 是句子级 RE，GRPO 成功；我们是文档级 RE，GRPO 失败→RSFT 成功。\n      句子级 RE 每个 sample 只有 1 个 triple（binary classification），reward variance 天然充足；\n      文档级 RE 每个 sample 有数十个 triple，F1 score 作为 reward 在 group 内趋于同质化（frac_zero_std→0.8）。\n      (2) R1-RE 未报告 catastrophic forgetting，进一步支持\"句子级简单 reward 可行，文档级需要 CED\"的论点。\n      (3) R1-RE 关注 OOD 泛化，无 evidence 组件；我们关注 evidence-grounded extraction quality。\n      互补而非直接冲突——R1-RE 证明 RLVR for RE 可行，我们揭示文档级需要额外设计。\n\n  - title: \"MORE-R1: Guiding LVLM for Multimodal Object-Entity Relation Extraction via Stepwise Reasoning with RL\"\n    authors: Anonymous\n    year: 2026\n    venue: arXiv 2603.09478\n    url: https://arxiv.org/abs/2603.09478\n    category: rl_for_ie\n    role: related_method\n    key_finding: >\n      多模态 RE 中用 GRPO + Progressive Sample-Mixing Strategy 优化 LVLM 推理能力。\n      两阶段训练：SFT cold-start + GRPO RL。\n    relevance_to_rsft_docre: >\n      跨模态验证 RL for RE 趋势。其 Progressive Sample-Mixing 与我们\n      RSFT 的 difficulty-aware sampling 思想相通，但在不同模态。\n\n  - title: \"REAR: Reinforced Reasoning Optimization for Event Argument Extraction with Relation-Aware Support\"\n    authors: Jianwen Luo et al.\n    year: 2025\n    venue: EMNLP 2025 Findings\n    url: https://2025.emnlp.org/program/find_papers/\n    category: rl_for_ie\n    role: related_method\n    key_finding: >\n      将强化学习推理优化用于事件论元抽取，结合关系感知支持。\n      不同于 DocRE 但同属 IE 领域的 RL 应用。\n    relevance_to_rsft_docre: >\n      验证 RL 在 IE 任务上的有效性趋势。我们的工作扩展到 DocRE + evidence，\n      且使用 offline RSFT 而非 online RL。\n\n  - title: \"Adaptive Reinforcement Learning Planning: Harnessing LLMs for Complex Information Extraction\"\n    authors: Zepeng Ding et al.\n    year: 2024\n    venue: arXiv 2406.11455\n    url: https://arxiv.org/abs/2406.11455\n    category: rl_for_ie\n    role: background\n    key_finding: >\n      将 LLM 顺序抽取建模为 MDP，用 DDQN 训练 decision module\n      自适应选择实体抽取顺序，提升复杂 IE 性能。\n    relevance_to_rsft_docre: >\n      RL for IE 的早期工作。用 RL 优化抽取策略而非模型本身，\n      与我们 RSFT 直接微调 LLM 的方法路径不同。\n\n  - title: \"Graph-R1: Towards Agentic GraphRAG Framework via End-to-end Reinforcement Learning\"\n    authors: Haoran Luo et al.\n    year: 2025\n    venue: ICML 2026\n    url: https://arxiv.org/abs/2507.21892\n    category: rl_for_ie\n    role: background\n    key_finding: >\n      用端到端 RL 优化 GraphRAG agent 的多轮检索-推理循环，\n      包含 knowledge hypergraph construction（n-ary relation extraction）。\n    relevance_to_rsft_docre: >\n      RL + knowledge extraction 的交叉点。Graph-R1 关注 QA 场景下的知识图谱构建，\n      我们关注 DocRE 的训练优化，应用场景不同。\n\n  # === Category 8: Recent LLM-based DocRE Methods ===\n\n  - title: \"RelPrior: Relation as a Prior - A Novel Paradigm for LLM-based Document-level Relation Extraction\"\n    authors: Anonymous\n    year: 2025\n    venue: arXiv 2511.08143\n    url: https://arxiv.org/abs/2511.08143\n    category: llm_docre\n    role: key_baseline\n    key_finding: >\n      用 binary relation 作为先验过滤无关实体对，再用 predefined relation 匹配实体，\n      避免 LLM 在 DocRE 中被无关实体对分散注意力。\n      在 DocRED/Re-DocRED 上超越现有纯 LLM-based DocRE 方法。\n    results:\n      docred_dev_f1: 47.82\n      docred_test_f1: 48.34\n      re_docred_dev_f1: 55.94\n      re_docred_test_f1: 54.80\n      backbone: LLaMA3-8B\n    evidence_generation: false\n    relevance_to_rsft_docre: >\n      我们的直接 baseline 之一。RelPrior_LLaMA3-8B 在 DocRED test F1=48.34,\n      Re-DocRED test F1=54.80。我们的 RSFT 提升显著更优。\n      RelPrior 是 inference paradigm 创新（两阶段筛选），我们是 training paradigm 创新（RSFT+CED），正交互补。\n\n  - title: \"LMRC: LLM with Relation Classifier for Document-Level Relation Extraction\"\n    authors: Xingzuo Li, Kehai Chen, Yunfei Long, Min Zhang\n    year: 2024\n    venue: arXiv 2408.13889\n    url: https://arxiv.org/abs/2408.13889\n    category: llm_docre\n    role: related_method\n    key_finding: >\n      两阶段方法：先用 attention-based classifier 过滤 NA 实体对（RCP），\n      再用 LLM 在精简候选空间中做多分类（RC）。\n      注意：LMRC 依赖 BERT-based classifier 作为预筛选，非纯 LLM 方法。\n    results:\n      docred_dev_ign_f1: 58.16\n      docred_dev_f1: 59.97\n      docred_test_ign_f1: 58.49\n      docred_test_f1: 60.52\n      re_docred_test_ign_f1: 74.08\n      re_docred_test_f1: 74.63\n      backbone: BERT classifier + LLM\n    evidence_generation: false\n    relevance_to_rsft_docre: >\n      LMRC 在 DocRED test F1=60.52, Re-DocRED test F1=74.63，性能显著高于纯 LLM 方法。\n      但它依赖 BERT classifier 预筛选，本质上是 hybrid 方法而非纯 LLM generative。\n      与我们端到端 LLM 生成方式不同——我们通过 RSFT 的 reward-based filtering 隐式解决 class imbalance。\n\n  - title: \"Ru-LLM: Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction\"\n    authors: Anonymous\n    year: 2025\n    venue: NLPCC 2025\n    url: https://link.springer.com/chapter/10.1007/978-981-95-3343-5_11\n    category: llm_docre\n    role: related_method\n    key_finding: >\n      用频繁模式挖掘 + MCTS 搜索逻辑规则，转化为 prompt 约束 LLM 输出，\n      再用 CoT 验证过滤不满足规则的 triple。\n      在 DWIE、DocRED、Re-DocRED 上声称超越现有 LLM 方法和规则框架。\n      具体 F1 未公开获取（Springer 付费墙），但声称超越 AutoRE 等 LLM baseline。\n    results:\n      note: \"behind Springer paywall; claims SOTA over LLM baselines on DocRED/Re-DocRED/DWIE\"\n    evidence_generation: false\n    relevance_to_rsft_docre: >\n      规则约束方式与我们的 CED reward 在 motivation 上相似（都是引入外部知识约束），\n      但 Ru-LLM 用 inference-time 规则验证（MCTS+CoT），我们用 training-time reward shaping（CED）。\n      Ru-LLM 的规则是数据集级别的频繁模式，CED 是 instance-level 的 evidence faithfulness。\n\n  - title: \"GLiDRE: Generalist Lightweight model for Document-level Relation Extraction\"\n    authors: Anonymous\n    year: 2025\n    venue: arXiv 2508.00757\n    url: https://arxiv.org/abs/2508.00757\n    category: llm_docre\n    role: background\n    key_finding: >\n      基于 dual-encoder 的轻量级零/少样本 DocRE 模型，\n      预训练于 136K 文档的大规模 RE 数据。\n      fully supervised Re-DocRED test F1=77.83，但这是 encoder-based 非 LLM generative。\n      zero-shot Re-DocRED test F1=17.32（超越 LLaMA 3.3 70B 和 Mistral-Small 24B）。\n    results:\n      re_docred_dev_f1: 77.76\n      re_docred_test_f1: 77.83\n      re_docred_zero_shot_test_f1: 17.32\n      fredo_in_domain_1doc_f1: 13.00\n      fredo_in_domain_3doc_f1: 15.71\n      backbone: \"dual-encoder (few hundred M params)\"\n    evidence_generation: false\n    relevance_to_rsft_docre: >\n      不同范式（encoder-based vs LLM generative）。GLiDRE 的 fully supervised F1=77.83\n      远超 LLM-based 方法（RelPrior 54.80），但依赖大规模预训练数据和 encoder 架构。\n      与我们不直接可比——我们关注 LLM generative 范式下的训练优化。\n\n  - title: \"AutoRE: Document-Level Relation Extraction with Large Language Models\"\n    authors: Anonymous\n    year: 2024\n    venue: arXiv 2403.14888\n    url: https://arxiv.org/abs/2403.14888\n    category: llm_docre\n    role: background\n    key_finding: >\n      RHF（Relation-Head-Facts）范式用 Mistral-7B + QLoRA 做端到端 DocRE。\n      关键设计：先抽 relation，再抽 head entity，最后抽 fact triple。\n    results:\n      re_docred_dev_f1_mistral: 53.01\n      re_docred_test_f1_mistral: 51.91\n      re_docred_dev_f1_vicuna: 54.29\n      re_docred_test_f1_vicuna: 53.84\n      docred_dev_f1_llama3: 45.76\n      docred_test_f1_llama3: 45.96\n      re_docred_dev_f1_llama3: 52.28\n      re_docred_test_f1_llama3: 51.97\n      backbone: \"Mistral-7B / Vicuna-7B / LLaMA3-8B (QLoRA)\"\n    evidence_generation: false\n    relevance_to_rsft_docre: >\n      QLoRA fine-tuning for DocRE 的先例。AutoRE_LLaMA3-8B 在 Re-DocRED test F1=51.97,\n      DocRED test F1=45.96。我们的 SFT baseline 与之类似，\n      RSFT 在此基础上引入 reward-guided sample selection 进一步提升。\n\n  # === Category 9: Evidence Generation & Task Performance Trade-off ===\n  # (NEW - 2026-05-15 evidence generation survey)\n\n  - title: \"Mind Your Step (by Step): Chain-of-Thought can Reduce Performance on Tasks where Thinking Makes Humans Worse\"\n    authors: Sprague et al.\n    year: 2024\n    venue: NeurIPS 2024\n    url: https://arxiv.org/abs/2410.21333\n    category: evidence_generation_tradeoff\n    role: key_evidence\n    key_finding: >\n      CoT 在某些任务上降低性能高达 36.3%（o1-preview vs GPT-4o）。\n      显式推理步骤引入 error accumulation，且模型可能 overfit 到解释格式而非任务结构。\n      隐式推理（hidden activations）在分布偏移下优于显式 token-level 推理。\n    relevance_to_evidence_tradeoff: >\n      直接支持我们的核心发现：要求模型同时生成 evidence sentences 是一种\"显式推理\"，\n      会对主任务（RE）产生性能代价（~8pp F1 下降）。\n      Related Work 引用点：evidence generation 作为 structured explanation，\n      与 CoT 共享\"显式推理降低主任务性能\"的普遍模式。\n\n  - title: \"Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion\"\n    authors: Xie et al. (Google Research)\n    year: 2022\n    venue: ACL Findings 2022\n    url: https://arxiv.org/abs/2106.08657\n    category: evidence_generation_tradeoff\n    role: closest_docre_precedent\n    key_finding: >\n      Joint 训练 RE + evidence extraction，关键创新在 inference-stage fusion：\n      分别在 extracted evidence 和 full document 上做 RE 预测再通过 blending layer 融合。\n      DocRED 上提升 1.37 Ign F1。Silver evidence labels（启发式规则构建）即可提升 RE 性能。\n    relevance_to_evidence_tradeoff: >\n      最直接的 DocRE + evidence 先例。EIDER 的核心洞察是 evidence 需要 inference-stage 融合\n      而非 joint generation——暗示 joint generation 会引入 noise。\n      我们的 CED reranker 是 LLM-era 版本的 inference-stage fusion：\n      先生成多个候选（含 evidence），再用 NLI 在推理阶段选最佳。\n      Related Work 引用点：encoder-based DocRE 中 evidence 的使用方式，与我们 generative 范式的关键差异。\n\n  - title: \"Exploring the Trade-off Between Model Performance and Explanation Plausibility of Text Classifiers Using Human Rationales\"\n    authors: Resck, Raimundo, Poco\n    year: 2024\n    venue: NAACL Findings 2024\n    url: https://arxiv.org/abs/2404.03098\n    category: evidence_generation_tradeoff\n    role: formal_framework\n    key_finding: >\n      用 multi-objective optimization 探索 performance vs explanation plausibility 的 Pareto frontier。\n      引入 rationale 约束创建 contrastive loss，证实加入 rationale supervision 会降低主任务性能，\n      但存在 Pareto optimal 解平衡两者。\n    relevance_to_evidence_tradeoff: >\n      提供了 performance-explainability trade-off 的形式化框架。\n      我们的 evidence-grounded RE 降 8pp 正是 Pareto frontier 上的一个点。\n      CED reranker 的效果可解读为：将系统从 evidence-constrained 点推向 Pareto frontier，\n      在几乎不牺牲 evidence quality（evi_f1=0.8188）的前提下恢复 RE 性能。\n      Related Work 引用点：evidence generation 的 performance cost 有理论依据。\n\n  - title: \"The Decreasing Value of Chain of Thought in Prompting\"\n    authors: Meincke, Mollick, Mollick, Shapiro\n    year: 2025\n    venue: Wharton Generative AI Labs Technical Report (SSRN)\n    url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5285532\n    category: evidence_generation_tradeoff\n    role: empirical_support\n    key_finding: >\n      现代 reasoning models 上 CoT 收益微弱（4-13%），但 latency 增加 35-600%。\n      更强的模型从显式推理中受益越少。CoT 可能在 easy questions 上引入 errors\n      （variability 增加导致原本正确的被改错）。\n    relevance_to_evidence_tradeoff: >\n      支持\"更强的 SFT 模型不需要在生成时显式输出 evidence\"的论点。\n      我们的 evidence-only SFT 的性能下降符合\"显式推理的边际收益递减\"模式。\n      Related Work 引用点：evidence generation 的 accuracy cost 不是 DocRE-specific，而是 LLM 的普遍趋势。\n\n  # === Category 10: Negative Transfer in Multi-task / Auxiliary-task Learning ===\n\n  - title: \"ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning\"\n    authors: Jiang, Chen et al.\n    year: 2023\n    venue: NeurIPS 2023\n    url: https://arxiv.org/abs/2301.12618\n    category: negative_transfer\n    role: theoretical_framework\n    key_finding: >\n      辅助任务常导致 negative transfer，根因不仅是 gradient conflict 还有 auxiliary-target\n      generalization gap。ForkMerge 周期性 fork 模型为多分支，搜索最优 task weights，\n      动态 merge 过滤有害 task-parameter updates。在多个 benchmark 上减少 negative transfer。\n    relevance_to_evidence_tradeoff: >\n      Evidence generation 作为 auxiliary task 对 RE 的 negative transfer 可用此框架解释：\n      evidence 和 RE 的 gradient 方向不完全对齐，joint training 时 evidence 任务\"拖累\"RE。\n      CED reranker 本质上是将 evidence quality 从 training-time joint objective 解耦到\n      inference-time verification，避免了 training-time 的 negative transfer。\n      Related Work 引用点：auxiliary task 导致主任务性能下降的一般性理论。\n\n  # === Category 11: Faithfulness vs Accuracy / Correctness Trade-off ===\n\n  - title: \"Correctness is not Faithfulness in RAG Attributions\"\n    authors: Wallat, Heuss, de Rijke, Anand\n    year: 2024\n    venue: SIGIR 2025\n    url: https://arxiv.org/abs/2412.18004\n    category: faithfulness_accuracy_tradeoff\n    role: key_conceptual_framework\n    key_finding: >\n      Correctness 和 faithfulness 是独立维度，可能冲突。高达 57% 的 citations 是\n      post-rationalized（事后编造而非真实依据）。Unfaithful attributions 可能 factually correct，\n      但 foster misguided trust。必须同时检查 correctness 和 faithfulness。\n    relevance_to_evidence_tradeoff: >\n      直接相关。我们的 evidence-grounded RE 试图让模型输出 faithful evidence，\n      但这与 relation correctness 产生张力（rel_f1 降 8pp）。\n      CED reranker 通过 NLI verification 确保 evidence 是 faithful 的（非 post-rationalized），\n      同时不牺牲 RE accuracy。\n      Related Work 引用点：correctness-faithfulness 分离的概念框架。\n\n  - title: \"Evaluating Correctness and Faithfulness of Instruction-Following Models for Question Answering\"\n    authors: Adlakha, BehnamGhader, Lu, Meade, Reddy\n    year: 2024\n    venue: TACL 2024\n    url: https://arxiv.org/abs/2307.16877\n    category: faithfulness_accuracy_tradeoff\n    role: evaluation_framework\n    key_finding: >\n      Instruction-following LLMs 在 correctness 上表现可比 fine-tuned models，\n      但 faithfulness 普遍较差——模型会 hallucinate 而非忠实于提供的 evidence。\n      传统 metrics 对 correctness 和 faithfulness 的评估均有缺陷。\n    relevance_to_evidence_tradeoff: >\n      解释了为什么 joint evidence+RE 生成性能差——模型在同时优化 correctness\n      和 faithfulness 时，两个目标存在张力。单纯要求模型\"同时输出正确 triples 和\n      faithful evidence\"是 multi-objective optimization 问题。\n      Related Work 引用点：correctness vs faithfulness 评估方法论。\n\n  - title: \"Towards Faithful Model Explanation in NLP: A Survey\"\n    authors: Lyu, Havaldar, Stein et al.\n    year: 2024\n    venue: Computational Linguistics (MIT Press)\n    url: https://aclanthology.org/2024.cl-2.6/\n    category: faithfulness_accuracy_tradeoff\n    role: comprehensive_survey\n    key_finding: >\n      系统综述 NLP 中 faithful explanation 的定义、评估和生成方法。\n      识别了 faithfulness-performance trade-off 作为核心挑战：\n      更 faithful 的解释不一定更有用，更有用的解释不一定 faithful。\n      提出未来方向包括 multi-objective optimization 和 post-hoc verification。\n    relevance_to_evidence_tradeoff: >\n      权威综述为我们的 evidence generation trade-off 提供广泛文献背景。\n      我们的 CED reranker 正是该综述建议的\"post-hoc verification\"方向的具体实例。\n      Related Work 引用点：faithfulness 研究的全景综述，定位我们的工作。\n\n  # === Category 12: Reranking / Verification as Bridge ===\n\n  - title: \"Genie: Achieving Human Parity in Content-Grounded Datasets Generation\"\n    authors: Yehudai, Carmeli, Mass et al.\n    year: 2024\n    venue: ICLR 2024\n    url: https://arxiv.org/abs/2401.14367\n    category: reranking_verification_bridge\n    role: methodological_precedent\n    key_finding: >\n      三阶段流程：Content Preparation → Generation → NLI-based Filtering。\n      用 fine-tuned T5-11B NLI 模型判断生成内容是否 entailed by source（faithfulness 检验），\n      过滤不 faithful 的生成。在 LFQA、摘要、IE 上达到 human parity。\n    relevance_to_evidence_tradeoff: >\n      方法论上最接近我们的 CED reranker——都是用 NLI verification 作为 post-hoc filter/reranker，\n      在不牺牲主任务质量的前提下确保 grounding quality。\n      GENIE 验证了 NLI-based filtering 在内容生成中的有效性。\n      关键差异：GENIE 是 data generation pipeline 的过滤，我们是 inference-time reranking。\n      Related Work 引用点：NLI-based verification 作为 bridge 的成功先例。\n",
    "structuredPatch": [
      {
        "oldStart": 705,
        "oldLines": 3,
        "newStart": 705,
        "newLines": 214,
        "lines": [
          "       GENIE 验证了 NLI-based filtering 在内容生成中的有效性。",
          "       关键差异：GENIE 是 data generation pipeline 的过滤，我们是 inference-time reranking。",
          "       Related Work 引用点：NLI-based verification 作为 bridge 的成功先例。",
          "+",
          "+  # === Category 13: Evidence-Grounded RL (NEW - 2026-05-15 scan) ===",
          "+",
          "+  - title: \"EvidenceRL: Reinforcing Evidence Consistency for Trustworthy Language Models\"",
          "+    authors: Ben Tamo, Lu, Marteau, Nnamdi, Wang",
          "+    year: 2026",
          "+    venue: arXiv 2603.19532",
          "+    url: https://arxiv.org/abs/2603.19532",
          "+    category: evidence_grounded_rl",
          "+    role: closest_competitor",
          "+    key_finding: >",
          "+      用 GRPO 同时优化 grounding（evidence entailment）和 correctness（答案准确性）。",
          "+      在 cardiac diagnosis（Llama-3.2-3B）上 F1@3 从 37.0→54.5，grounding 从 47.6→78.2，",
          "+      hallucination 降 5 倍。在 legal reasoning（Llama-3.1-8B）上 faithfulness 从 32.8%→67.6%。",
          "+      核心：证据一致性 reward 不牺牲 task accuracy 的前提下大幅提升 faithfulness。",
          "+    relevance_to_freige: >",
          "+      **最直接的 novelty 威胁。** EvidenceRL 与 FREIGE 共享核心 idea：用 GRPO + evidence faithfulness reward",
          "+      训练更可靠的模型。关键差异：(1) EvidenceRL 在 QA 域（cardiac/legal），不涉及 DocRE 的 structured output；",
          "+      (2) EvidenceRL 未报告 evidence generation 的 performance cost（evidence tax）——它的 grounding 和",
          "+      correctness 同时提升，而我们发现 DocRE 中两者存在 ~8pp 张力；",
          "+      (3) EvidenceRL 不涉及 task decoupling 现象（QLoRA-specific）；",
          "+      (4) EvidenceRL 无 inference-time reranking（CED reranker）。",
          "+      定位策略：EvidenceRL 证明 evidence-grounded RL 在 QA 域有效，",
          "+      我们揭示 DocRE structured output 带来的独特挑战（evidence tax、task decoupling）和解法（CED reranker）。",
          "+",
          "+  # === Category 14: Multi-Objective GRPO (NEW - 2026-05-15 scan) ===",
          "+",
          "+  - title: \"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems\"",
          "+    authors: Ichihara, Jinnai, Morimura, Sakamoto, Mitsuhashi, Uchibe",
          "+    year: 2025",
          "+    venue: arXiv 2509.22047",
          "+    url: https://arxiv.org/abs/2509.22047",
          "+    category: multi_objective_grpo",
          "+    role: related_method",
          "+    key_finding: >",
          "+      GRPO 在多目标设置下易发生 reward hacking——只优化一个目标而牺牲其他目标。",
          "+      MO-GRPO 用 variance-based normalization 自动平衡多个 reward function 的权重，",
          "+      在多臂赌博机、控制、机器翻译、指令遵从四个域上实现稳定学习。",
          "+    relevance_to_freige: >",
          "+      CED reward 本质是多目标（extraction F1 + evidence quality）。MO-GRPO 的分析",
          "+      解释了为什么单一 extraction F1 reward 下模型可能 hack 到 \"忽略 evidence 只抽 triple\" 的策略。",
          "+      CED 从 reward 设计端解决，MO-GRPO 从算法端解决，互补视角。",
          "+",
          "+  - title: \"Multi-Objective and Mixed-Reward Reinforcement Learning via Reward-Decorrelated Policy Optimization\"",
          "+    authors: Bai, Liu, Zhuang, Zhou, Weng, Chen, Wang, Cai",
          "+    year: 2026",
          "+    venue: arXiv 2605.13641",
          "+    url: https://arxiv.org/abs/2605.13641",
          "+    category: multi_objective_grpo",
          "+    role: related_method",
          "+    key_finding: >",
          "+      GRPO 聚合 mixed-reward 时直接求和再归一化会淹没弱信号 reward 维度。",
          "+      RDPO 用 Magnitude-Aware Quantile normalization + Mahalanobis whitening",
          "+      去相关 reward 子空间，改善 LLM post-training 的多目标平衡。",
          "+    relevance_to_freige: >",
          "+      CED reward 的 evidence quality 维度与 extraction F1 天然低相关（r<0.3），",
          "+      RDPO 的理论预测这种低相关多维 reward 更易优化。",
          "+      为 CED 的 training-stabilizing 效果提供另一个理论解释角度。",
          "+",
          "+  # === Category 15: GRPO Theory (NEW - 2026-05-15 scan) ===",
          "+",
          "+  - title: \"GRPO is Secretly a Process Reward Model\"",
          "+    authors: Sullivan, Koller",
          "+    year: 2025",
          "+    venue: under review at ICML 2026",
          "+    url: https://arxiv.org/abs/2509.21154",
          "+    category: grpo_theory",
          "+    role: theoretical_insight",
          "+    key_finding: >",
          "+      证明 GRPO + ORM 在特定条件下等价于 PRM-aware RL objective。",
          "+      提出 λ-GRPO 修正 GRPO 在不均匀 process step 上的 deficiency，",
          "+      在 downstream reasoning 上超越标准 GRPO 且训练更快收敛。",
          "+    relevance_to_freige: >",
          "+      DocRE structured output（multi-triple generation）可视为多步 process。",
          "+      GRPO 隐式的 PRM 性质可能解释了为什么 extraction-only reward",
          "+      在文档级 multi-triple 场景下训练信号不足——单一 outcome reward",
          "+      无法为每个 triple 的生成步骤提供有效 process-level credit assignment。",
          "+      CED 通过 evidence quality 为每个 triple 提供了更细粒度的信号，",
          "+      等效于增强了 process-level reward 的分辨率。",
          "+",
          "+  - title: \"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges\"",
          "+    authors: Wang et al. (23 authors)",
          "+    year: 2026",
          "+    venue: arXiv 2604.13602",
          "+    url: https://arxiv.org/abs/2604.13602",
          "+    category: grpo_theory",
          "+    role: theoretical_framework",
          "+    key_finding: >",
          "+      提出 Proxy Compression Hypothesis (PCH)：reward hacking 源于 objective compression、",
          "+      optimization amplification、evaluator-policy co-adaptation 三者交互。",
          "+      识别了 perception-reasoning decoupling 作为多模态中 reward hacking 的表现之一。",
          "+    relevance_to_freige: >",
          "+      PCH 框架可解释我们观察到的 extraction-evidence decoupling：",
          "+      QLoRA 的 compressed representation space 下，模型可能将 extraction 和 evidence",
          "+      两个子目标压缩到部分重叠的 proxy 空间，导致 optimization amplification",
          "+      使模型专注于更容易优化的 extraction 而忽略 evidence。",
          "+      bf16 下不复现可能因为 full-rank update 的 representation space 更充裕。",
          "+",
          "+  # === Category 16: Training Precision & RL Stability (NEW - 2026-05-15 scan) ===",
          "+",
          "+  - title: \"Defeating the Training-Inference Mismatch via FP16\"",
          "+    authors: Qi, Liu, Zhou, Pang, Du, Lee, Lin",
          "+    year: 2025",
          "+    venue: arXiv 2510.26788",
          "+    url: https://arxiv.org/abs/2510.26788",
          "+    category: training_precision_rl",
          "+    role: key_evidence",
          "+    key_finding: >",
          "+      BF16 在 RL fine-tuning 中引入大的 rounding error 导致 training-inference 不一致，",
          "+      BF16 训练常在 150-600 步崩溃。仅切换到 FP16 即可消除不一致，",
          "+      提供更稳定训练、更快收敛和更优性能，只需改几行代码。",
          "+    relevance_to_freige: >",
          "+      直接相关我们的 QLoRA GRPO 不稳定性发现。QLoRA 在 4-bit 量化基础上",
          "+      使用 bf16/fp16 adapter，量化+低精度的 compounding error 可能是",
          "+      task decoupling 现象的底层原因之一。该论文提供了 precision-instability",
          "+      的机制解释，支持我们 \"QLoRA-specific decoupling\" 的发现——",
          "+      低精度 representation 放大了多目标 RL 中子任务间的 gradient 干扰。",
          "+",
          "+  # === Category 17: RL for Scientific IE (NEW - 2026-05-15 scan) ===",
          "+",
          "+  - title: \"R²GRPO: Better LLMs for Scientific Information Extraction with MimicSFT and Relevance and Rule-induced GRPO\"",
          "+    authors: Li, Di, Liu, Jing, Qiu, Chen",
          "+    year: 2025",
          "+    venue: arXiv 2505.22068",
          "+    url: https://arxiv.org/abs/2505.22068",
          "+    category: rl_for_ie",
          "+    role: related_method",
          "+    key_finding: >",
          "+      两阶段方法：MimicSFT（structured reasoning template，无需高质量 CoT 数据）",
          "+      + R²GRPO（relevance reward + rule-mining reward），",
          "+      在科学信息抽取 RE benchmark 上超越 baseline LLM 和 specialized supervised model。",
          "+    relevance_to_freige: >",
          "+      R²GRPO 的 rule-based reward 设计与我们的 CED reward 有相似动机——",
          "+      都是引入 task-specific 结构化 reward 替代单纯 F1 metric reward。",
          "+      差异：R²GRPO 的 rule 是 dataset-level 频繁模式（类似 Ru-LLM），",
          "+      CED 是 instance-level evidence faithfulness 判别。",
          "+      R²GRPO 未涉及 evidence generation 或 DocRE。",
          "+",
          "+  # === Category 18: LLM Alignment for IE (NEW - 2026-05-15 scan) ===",
          "+",
          "+  - title: \"ADELIE: Aligning Large Language Models on Information Extraction\"",
          "+    authors: Qi, Peng, Wang, Xu, Hou, Li",
          "+    year: 2024",
          "+    venue: EMNLP 2024",
          "+    url: https://arxiv.org/abs/2405.05008",
          "+    category: llm_ie_alignment",
          "+    role: key_baseline",
          "+    key_finding: >",
          "+      构建 IEInstruct 高质量 IE alignment 语料库，用 SFT + DPO 训练 ADELIE。",
          "+      支持 closed/open/on-demand IE 三种模式。",
          "+      基于 LLaMA-2-7B/LLaMA-3.2-3B/Qwen2.5-1.5B，在多个 held-out IE dataset 上达 SOTA。",
          "+    relevance_to_freige: >",
          "+      ADELIE 是 IE alignment 的代表性工作，用 SFT+DPO 替代 RSFT+GRPO。",
          "+      我们的工作与 ADELIE 在 training paradigm 上有可比性——",
          "+      ADELIE 用 DPO（offline preference optimization），我们用 RSFT（offline rejection sampling）。",
          "+      关键差异：ADELIE 覆盖通用 IE，不涉及 evidence generation 或 DocRE-specific challenges；",
          "+      我们专注于 DocRE + evidence grounding 的 trade-off。",
          "+",
          "+  # === Category 19: Unfaithful Reasoning / Post-Rationalization (NEW - 2026-05-15 scan) ===",
          "+",
          "+  - title: \"Chain-of-Thought Is Not Explainability\"",
          "+    authors: Barez et al.",
          "+    year: 2025",
          "+    venue: Oxford WhiteBox Technical Report",
          "+    url: https://aigi.ox.ac.uk/wp-content/uploads/2025/07/Cot_Is_Not_Explainability.pdf",
          "+    category: unfaithful_reasoning",
          "+    role: conceptual_support",
          "+    key_finding: >",
          "+      CoT 仅仅 rationalize（事后合理化）而非 report（忠实报告）模型的真实决策过程。",
          "+      小的操纵即可改变 CoT 的推理链但不改变模型实际决策。",
          "+      模型会 silently correct 错误而不在 CoT 中体现。",
          "+    relevance_to_freige: >",
          "+      支持我们 evidence generation 分析的一个维度：模型生成的 evidence sentences",
          "+      可能是 post-rationalization 而非真正驱动 RE 决策的信号。",
          "+      CED reranker 用 NLI verification 检查 evidence 的实际 entailment",
          "+      而非信任模型自报告的 evidence，本质上是对 post-rationalization 的防御。",
          "+",
          "+  - title: \"Characterizing Large Language Models as Rationalizers of Knowledge-Grounded Dialogue\"",
          "+    authors: Anonymous",
          "+    year: 2024",
          "+    venue: ACL Findings 2024",
          "+    url: https://aclanthology.org/2024.findings-acl.484.pdf",
          "+    category: unfaithful_reasoning",
          "+    role: empirical_evidence",
          "+    key_finding: >",
          "+      LLM 在 knowledge-grounded dialogue 中普遍表现为 rationalizer 而非 faithful reasoner，",
          "+      模型的 explanation 与其实际使用的 knowledge evidence 不一致。",
          "+    relevance_to_freige: >",
          "+      与我们的发现呼应：DocRE 中模型可能输出看似合理的 evidence sentences",
          "+      但实际 RE 决策并不依赖这些 evidence。这解释了为什么 joint evidence+RE 生成",
          "+      对 RE 性能有负面影响——模型在学习生成 \"合理化解释\" 而非 \"可靠推理\"。",
          "+",
          "+  # === Category 20: Latent vs Explicit Reasoning Trade-off (NEW - 2026-05-15 scan) ===",
          "+",
          "+  - title: \"Reasoning Beyond Language: A Comprehensive Survey on Latent Chain-of-Thought Reasoning\"",
          "+    authors: Chen, Zhao, Xia, Lu, Wang, Chen, Zhang, Wang, Li, Shen",
          "+    year: 2025",
          "+    venue: arXiv 2505.16782",
          "+    url: https://arxiv.org/abs/2505.16782",
          "+    category: latent_vs_explicit_reasoning",
          "+    role: survey",
          "+    key_finding: >",
          "+      Latent CoT 将推理从显式 token generation 解耦到 hidden state computation，",
          "+      在多项任务上达到与显式 CoT 相当或更优的性能，同时推理速度提升 20 倍以上。",
          "+      显式 CoT 的 sequential token-level 推理是 applicability 的瓶颈。",
          "+    relevance_to_freige: >",
          "+      为 evidence generation trade-off 提供更广泛的理论视角：",
          "+      evidence sentences 作为显式推理步骤（类似 CoT tokens）可能不是最优的推理形式。",
          "+      我们的 CED reranker 可被视为将 evidence reasoning 从 generation-time 显式推理",
          "+      转移到 inference-time 的 NLI-based 验证——类似 latent-to-explicit 的范式转换，",
          "+      但方向相反：不是让推理隐式化，而是让验证外部化。"
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

_source line 118_

现在通过 save_project_file 注册更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "bd11164d-cc77-4a63-9da2-bacb0b7f2796",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012TELdmn6wLor2sVu2QKaZg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4468,
      "cache_read_input_tokens": 92609,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4468
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

_source line 119_

<details open><summary>🔧 Tool call — Read · `toolu_01ShUgLHBFdRC6VA8bnVCEqW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
  "offset": 0,
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "700ed38c-7147-4952-9f9e-ec45b4c86e7b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012TELdmn6wLor2sVu2QKaZg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4468,
      "cache_read_input_tokens": 92609,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4468
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

_source line 120 · 2026-05-15T22:13:33.542Z_

<details><summary>↩ Tool result · `toolu_01ShUgLHBFdRC6VA8bnVCEqW`</summary>

```text
0	# Literature Map for faith-evidence-ie (FREIGE)
1	# Focus: CED-as-training-stabilizer (D024) + RSFT for DocRE
2	# Updated: 2026-05-15 (W4 expanded: +11 papers from literature scan)
3	
4	papers:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "3869da92-ba18-4ede-8431-6a4757f9f56f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
      "content": "# Literature Map for faith-evidence-ie (FREIGE)\n# Focus: CED-as-training-stabilizer (D024) + RSFT for DocRE\n# Updated: 2026-05-15 (W4 expanded: +11 papers from literature scan)\n\npapers:",
      "numLines": 5,
      "startLine": 0,
      "totalLines": 919
    }
  }
}
```

</details>

---

### Tool call

_source line 121_

<details open><summary>🔧 Tool call — Bash · `toolu_01En48VdVBKujsmqLJi9ZBei`</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
  "description": "Count lines in updated literature map"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "67253dab-ca62-4c8a-ac95-b26f7bde1b23",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XdE8xUCPA4qqJtbTuKoxG4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 226,
      "cache_read_input_tokens": 97077,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 226
      },
      "output_tokens": 66,
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

_source line 122 · 2026-05-15T22:13:37.238Z_

<details><summary>↩ Tool result · `toolu_01En48VdVBKujsmqLJi9ZBei`</summary>

```text
918 /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "5690350e-d3f0-4128-851a-376e18dcb1e0",
  "tool_use_result": {
    "stdout": "918 /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
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

_source line 123_

<details open><summary>🔧 Tool call — Bash · `toolu_019ykF61PbvDwBEpffM5YQqZ`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml | python3 -c \"import sys,yaml; yaml.safe_load(sys.stdin); print('YAML valid')\" 2>&1",
  "description": "Validate YAML syntax"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "ec8a1abc-c94b-4379-b475-9f7c038f52b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WHVZ8yjPfG5eewb9tGiyL8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 157,
      "cache_read_input_tokens": 97303,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 157
      },
      "output_tokens": 63,
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

_source line 124 · 2026-05-15T22:13:40.935Z_

<details><summary>↩ Tool result · `toolu_019ykF61PbvDwBEpffM5YQqZ`</summary>

```text
YAML valid
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "55c1f097-6fc8-4c79-aff2-6fea6bf43ea8",
  "tool_use_result": {
    "stdout": "YAML valid",
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

_source line 125_

YAML 合法。现在把完整内容写入 save_project_file。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "d9a4ae6a-bec6-4c92-83d7-10f4cde33368",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017odNrGgW2ki31V9vUZmGV9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 154,
      "cache_read_input_tokens": 97460,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 154
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

_source line 126_

<details open><summary>🔧 Tool call — Bash · `toolu_01PcV92iQMBsiQ4TxwQTgEhR`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/literature_map.yaml",
  "description": "Read full file for save_project_file",
  "timeout": 10000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "ffa6f103-fcfb-431a-b3b2-d3b680666e11",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017odNrGgW2ki31V9vUZmGV9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 154,
      "cache_read_input_tokens": 97460,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 154
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

_source line 127 · 2026-05-15T22:13:44.528Z_

<details><summary>↩ Tool result · `toolu_01PcV92iQMBsiQ4TxwQTgEhR`</summary>

```text
&lt;persisted-output>
Output too large (47.6KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/36a03546-b7c6-4659-a047-11cc70593f2c/tool-results/b4ppdl9gh.txt

Preview (first 2KB):
# Literature Map for faith-evidence-ie (FREIGE)
# Focus: CED-as-training-stabilizer (D024) + RSFT for DocRE
# Updated: 2026-05-15 (W4 expanded: +11 papers from literature scan)

papers:

  # === Category 1: Reward Diversity / Reward Shaping for RL Stability ===

  - title: "GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization"
    authors: NVIDIA Labs
    year: 2025
    venue: ICML 2026
    url: https://arxiv.org/abs/2601.05242
    category: reward_diversity
    role: closest_prior_work
    key_finding: >
      直接将 GRPO 应用于多 reward 组合时，不同 rollout 的 reward 组合在归一化后 collapse 为相同 advantage 值，
      降低训练信号分辨率导致收敛失败。GDPO 对每个 reward 独立做 group-wise normalization 再聚合，
      保留多 reward 的相对差异，显著提升训练稳定性。
    relevance_to_ced_stabilizer: >
      最直接相关。CED reward 本质上引入了独立于 extraction F1 的 reward 维度（evidence quality），
      GDPO 的理论分析解释了为什么多维 reward 比单一 reward 更稳定——独立 reward 维度防止 advantage collapse。
      但 GDPO 是方法论贡献，CED 是 task-specific reward 设计自然具备了这一特性。

  - title: "DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of LLMs"
    authors: Xiwen Chen et al.
    year: 2025
    venue: arXiv 2505.09655
    url: https://arxiv.org/abs/2505.09655
    category: reward_diversity
    role: related_method
    key_finding: >
      GRPO 的标量 reward 无法区分语义多样但得分相同的输出（diversity-quality inconsistency）。
      DRA 用子模互信息（SMI）对 reward 加权，给多样性高的 completion 更大权重，
      等价于 Inverse Propensity Scoring 去偏，防止 policy 坍缩到先验模式。
    relevance_to_ced_stabilizer: >
      DRA 通过后处理 reward 注入多样性信号；CED 的 reward 本身就内含对比结构自然提供 diversity 信号。
      机制互补但来源不同——CED 是 reward design 层面，DRA 是 optimization 层面。

  - title: "Shrinking the Variance: Shrinkage Baselines for RL with Verifiable Rewards"
    authors: Guanning Zeng et al.
    year: 2025
    venue: arXiv 2511.03710
    url: https://arxiv.org/abs/2511.03710
    category: reward_diversity
    role: theoretical_support
    key_finding: >
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "e1c79ae9-a31b-4831-8d53-865c031d41ff",
  "tool_use_result": {
    "stdout": "# Literature Map for faith-evidence-ie (FREIGE)\n# Focus: CED-as-training-stabilizer (D024) + RSFT for DocRE\n# Updated: 2026-05-15 (W4 expanded: +11 papers from literature scan)\n\npapers:\n\n  # === Category 1: Reward Diversity / Reward Shaping for RL Stability ===\n\n  - title: \"GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization\"\n    authors: NVIDIA Labs\n    year: 2025\n    venue: ICML 2026\n    url: https://arxiv.org/abs/2601.05242\n    category: reward_diversity\n    role: closest_prior_work\n    key_finding: >\n      直接将 GRPO 应用于多 reward 组合时，不同 rollout 的 reward 组合在归一化后 collapse 为相同 advantage 值，\n      降低训练信号分辨率导致收敛失败。GDPO 对每个 reward 独立做 group-wise normalization 再聚合，\n      保留多 reward 的相对差异，显著提升训练稳定性。\n    relevance_to_ced_stabilizer: >\n      最直接相关。CED reward 本质上引入了独立于 extraction F1 的 reward 维度（evidence quality），\n      GDPO 的理论分析解释了为什么多维 reward 比单一 reward 更稳定——独立 reward 维度防止 advantage collapse。\n      但 GDPO 是方法论贡献，CED 是 task-specific reward 设计自然具备了这一特性。\n\n  - title: \"DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of LLMs\"\n    authors: Xiwen Chen et al.\n    year: 2025\n    venue: arXiv 2505.09655\n    url: https://arxiv.org/abs/2505.09655\n    category: reward_diversity\n    role: related_method\n    key_finding: >\n      GRPO 的标量 reward 无法区分语义多样但得分相同的输出（diversity-quality inconsistency）。\n      DRA 用子模互信息（SMI）对 reward 加权，给多样性高的 completion 更大权重，\n      等价于 Inverse Propensity Scoring 去偏，防止 policy 坍缩到先验模式。\n    relevance_to_ced_stabilizer: >\n      DRA 通过后处理 reward 注入多样性信号；CED 的 reward 本身就内含对比结构自然提供 diversity 信号。\n      机制互补但来源不同——CED 是 reward design 层面，DRA 是 optimization 层面。\n\n  - title: \"Shrinking the Variance: Shrinkage Baselines for RL with Verifiable Rewards\"\n    authors: Guanning Zeng et al.\n    year: 2025\n    venue: arXiv 2511.03710\n    url: https://arxiv.org/abs/2511.03710\n    category: reward_diversity\n    role: theoretical_support\n    key_finding: >\n      RLVR 中 per-prompt 均值 baseline 在低 generation 数下估计不准导致高 variance 梯度。\n      用 James-Stein shrinkage 混合 per-prompt 和 cross-prompt 均值，\n      构造可证明更低 variance 的 policy gradient estimator。\n    relevance_to_ced_stabilizer: >\n      理论支持：reward variance 对 gradient estimation 质量至关重要。\n      CED 的额外 reward 维度提供更丰富的 per-group variance，间接起到 variance 维持效果。\n\n  - title: \"Reward Shaping to Mitigate Reward Hacking in RLHF\"\n    authors: Anonymous\n    year: 2025\n    venue: arXiv 2502.18770\n    url: https://arxiv.org/abs/2502.18770\n    category: reward_diversity\n    role: background\n    key_finding: >\n      RL reward 应有界且先快速增长后缓慢收敛。系统研究 reward shaping 原则，\n      好的 reward 形状能抑制 reward hacking 并提升训练稳定性。\n    relevance_to_ced_stabilizer: >\n      CED reward 的 0-1 对比判别结构天然满足有界性，\n      且 evidence quality 的渐进提升符合\"先快后慢\"的 reward shaping 原则。\n\n  # === Category 2: Mode Collapse Prevention in GRPO/RLHF ===\n\n  - title: \"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\"\n    authors: ByteDance Seed, Tsinghua AIR\n    year: 2025\n    venue: NeurIPS 2025\n    url: https://arxiv.org/abs/2503.14476\n    category: mode_collapse_prevention\n    role: key_baseline\n    key_finding: >\n      Naive GRPO 存在 entropy collapse（policy 熵快速下降→输出同质化）。\n      根因：clipping 不对称性——概率 0.01 的 token 最多增到 0.012，而概率 0.9 的 token 可达 1.08，\n      低概率 token 难以增长，抑制探索。DAPO 提出 Clip-Higher（εhigh=0.28 > εlow=0.2）\n      为低概率 token 留更大增长空间，加 Dynamic Sampling 过滤 accuracy=0 或 1 的 prompt\n      （这些 prompt 产生零梯度，降低有效 batch size）。在 AIME 2024 达 50 分超越 DeepSeek-R1-Zero。\n    relevance_to_ced_stabilizer: >\n      DAPO 从 optimization 技巧角度解决 entropy collapse。CED reward 从 reward design 层面\n      防止 mode collapse——evidence quality 维度确保 reward 组内有足够 variance，\n      不会出现 all-same-reward 的零梯度 prompt。DAPO 的 Dynamic Sampling 过滤 accuracy=0/1 prompt\n      与我们观察到的 frac_zero_std→0.8 现象本质相同：extraction-only reward 下大量 prompt\n      产生零 advantage，CED 从源头（reward 设计）而非后处理（过滤）解决这个问题。\n\n  - title: \"Dr. GRPO: Removing Optimization Bias in GRPO\"\n    authors: Liu et al.\n    year: 2025\n    venue: COLM 2025\n    url: https://arxiv.org/abs/2503.20783\n    category: mode_collapse_prevention\n    role: related_analysis\n    key_finding: >\n      GRPO 的 std 归一化引入两个 bias：(1) difficulty bias——std(r) 归一化对低 variance 组\n      （全对/全错）给予过高 advantage 权重，trivial question 主导训练信号；\n      (2) length bias——per-token loss 的 1/|o_i| 项使长的错误回答被 under-penalize。\n      当 std(r)→0 时 advantage 爆炸或未定义，梯度数值不稳定。\n      Dr. GRPO 移除 std 归一化，用无偏 Monte Carlo advantage：Ã = R(q,o_i) - mean(R)。\n    relevance_to_ced_stabilizer: >\n      与我们的实验发现高度一致：extraction-only reward 下 frac_zero_std→0.8 正是\n      Dr. GRPO 分析的 difficulty bias 极端情况——大量 prompt 的所有 rollout 得到相同 F1，\n      std→0 导致 advantage 异常。CED 通过增加 reward 维度天然维持 reward_std>0，\n      从 reward 设计而非算法修改角度避免了 Dr. GRPO 发现的 bias。\n\n  - title: \"GVPO: Group Variance Policy Optimization for LLM Post-Training\"\n    authors: Anonymous\n    year: 2025\n    venue: NeurIPS 2025\n    url: https://arxiv.org/abs/2504.19599\n    category: mode_collapse_prevention\n    role: alternative_framework\n    key_finding: >\n      将 KL 约束 reward 最大化的解析解直接嵌入梯度权重，\n      variance 项自然平衡 exploration 与 exploitation，维持适度 entropy。\n    relevance_to_ced_stabilizer: >\n      GVPO 的 variance 项机制与 CED 维持 reward variance 的效果功能类似，\n      但 GVPO 是算法层面 implicit regularization，CED 是 reward 层面 explicit structure。\n\n  - title: \"REINFORCE++: Stabilizing Critic-Free Policy Optimization with Global Advantage Normalization\"\n    authors: Jian Hu et al.\n    year: 2025\n    venue: arXiv 2501.03262\n    url: https://arxiv.org/abs/2501.03262\n    category: mode_collapse_prevention\n    role: related_method\n    key_finding: >\n      Prompt-level (local) advantage normalization 导致不准确估计和过拟合。\n      Global batch normalization 提供更稳定、理论无偏的 gradient estimator。\n    relevance_to_ced_stabilizer: >\n      解决 local normalization 的 variance 问题；CED 从 reward 端增加 variance 来源。\n      两者在不同层面解决同一问题：防止 gradient signal 消失。\n\n  - title: \"DiverseGRPO: Mitigating Mode Collapse in Image Generation via Diversity-Aware GRPO\"\n    authors: Henglin Liu et al.\n    year: 2025\n    venue: arXiv 2512.21514\n    url: https://arxiv.org/abs/2512.21514\n    category: mode_collapse_prevention\n    role: parallel_work\n    key_finding: >\n      图像生成中 GRPO 后期输出同质化。distributional reward modeling（谱聚类+exploratory reward）\n      和 structure-aware regularization 实现 13-18% 语义多样性提升。\n    relevance_to_ced_stabilizer: >\n      跨域验证了 GRPO mode collapse 的普遍性，distributional reward 思路与 CED 精神相近——\n      都是通过 reward 层面结构化信号维持输出多样性。\n\n  - title: \"Why GRPO Needs Normalization: A Local-Curvature Perspective on Adaptive Gradients\"\n    authors: Anonymous\n    year: 2025\n    venue: arXiv 2601.23135\n    url: https://arxiv.org/abs/2601.23135\n    category: mode_collapse_prevention\n    role: theoretical_support\n    key_finding: >\n      GRPO 的 reward_std 归一化在温和条件下提供严格优于未归一化 REINFORCE 的收敛速率，\n      收益由 prompt 间平均 reward std 刻画。\n    relevance_to_ced_stabilizer: >\n      直接理论支撑：reward_std 越大收敛越好。CED 通过 evidence quality 维度维持高 reward_std，\n      从该理论看 CED 的稳定性优势是 reward_std 维持带来的收敛速率优势。\n\n  # === Category 3: Contrastive Rewards in RL ===\n\n  - title: \"Improving Reinforcement Learning from Human Feedback Using Contrastive Rewards\"\n    authors: Shen, Zhang et al.\n    year: 2024\n    venue: arXiv 2403.07708\n    url: https://arxiv.org/abs/2403.07708\n    category: contrastive_reward\n    role: closest_contrastive_precedent\n    key_finding: >\n      两步机制：(1) 离线采样 baseline response；(2) 用 baseline 计算 contrastive reward\n      作为 PPO 的 penalty 项。效果：惩罚 reward uncertainty、根据任务难度自适应校准、\n      减少 PPO 中的 variance。在 TL;DR 和 HH-RLHF 上持续优于标准 RLHF。\n    relevance_to_ced_stabilizer: >\n      最接近的对比 reward 先例。关键差异：(1) 它是对 learned RM 输出的后处理对比，\n      CED 是 reward function 本身就是对比判别（evidence vs. corrupted evidence）；\n      (2) 它在 PPO 中验证，CED 在 GRPO 中验证；\n      (3) 它是 domain-agnostic penalty，CED 是 task-specific faithfulness signal。\n      stabilizing 机制相通但实现路径根本不同。\n\n  - title: \"Improving Discriminative Capability of Reward Models in RLHF Using Contrastive Learning\"\n    authors: Anonymous\n    year: 2024\n    venue: EMNLP 2024\n    url: https://aclanthology.org/2024.emnlp-main.852/\n    category: contrastive_reward\n    role: related_method\n    key_finding: >\n      无监督对比损失训练 reward model 充分捕捉对比数据区分度，\n      带来更稳定的 PPO 训练 return 和 reward。\n    relevance_to_ced_stabilizer: >\n      验证对比训练 reward model → 更稳定 RL 训练链条。CED 不是对比训练 reward model，\n      而是 reward function 本身就是对比判别，但 stabilizing 机制相通。\n\n  - title: \"Contrastive Preference Learning: Learning from Human Feedback without RL\"\n    authors: Anonymous\n    year: 2024\n    venue: ICLR 2025\n    url: https://openreview.net/forum?id=iX1RjVQODj\n    category: contrastive_reward\n    role: background\n    key_finding: >\n      将 preference learning 重新表述为对比学习问题，无需显式 RL 即可从人类反馈中学习。\n    relevance_to_ced_stabilizer: >\n      对比框架在 preference alignment 中的通用性。CED 可被视为 task-specific contrastive preference signal。\n\n  # === Category 4: Evidence-Based Rewards in IE/NLP ===\n\n  - title: \"Drift: Enhancing LLM Faithfulness in Rationale Generation\"\n    authors: Anonymous\n    year: 2025\n    venue: ACL 2025\n    url: https://aclanthology.org/2025.acl-long.340.pdf\n    category: evidence_reward\n    role: related_method\n    key_finding: >\n      用 faithfulness reward 引导 LLM 生成更可靠的 rationale，提升 CoT 推理事实一致性。\n    relevance_to_ced_stabilizer: >\n      Faithfulness reward 用于生成质量的先例。CED 中 evidence discrimination\n      本质上也是 faithfulness 信号——判断证据是否忠实支持抽取结果。\n\n  - title: \"Fine-Grained NLI-Based Faithfulness Evaluation for Diverse Summarisation Tasks (INFUSE)\"\n    authors: Anonymous\n    year: 2024\n    venue: EACL 2024\n    url: https://aclanthology.org/2024.eacl-long.102/\n    category: evidence_reward\n    role: background\n    key_finding: >\n      变长前提+简化假设的细粒度 NLI faithfulness 评估，超越传统 NLI 在多任务摘要上的表现。\n    relevance_to_ced_stabilizer: >\n      NLI 作为 faithfulness 评估工具的进展。CED 中 NLI 组件用于判断 evidence 对 triple 的支持度。\n\n  - title: \"Enhancing Cross-Evidence Reasoning Graph for Document-Level Relation Extraction\"\n    authors: Anonymous\n    year: 2024\n    venue: PMC/Bioinformatics 2024\n    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11232587/\n    category: evidence_reward\n    role: background\n    key_finding: >\n      文档级关系抽取中用 cross-evidence reasoning graph 增强跨证据推理。\n    relevance_to_ced_stabilizer: >\n      DocRE 中 evidence 的重要性。但用 evidence 作为模型输入特征，\n      我们用 evidence quality 作为 RL reward 信号——定位根本不同。\n\n  # === Category 5: Multi-Objective RL for Text Generation ===\n\n  - title: \"Confronting Reward Model Overoptimization with Constrained RLHF\"\n    authors: Anonymous\n    year: 2025\n    venue: OpenReview\n    url: https://openreview.net/forum?id=gkfUvn0fLU\n    category: multi_objective_rl\n    role: related_analysis\n    key_finding: >\n      多组件 RM 的 overoptimization 研究。component RM 间的相关性显著影响 overoptimization 临界点，\n      用 constrained MDP 防止超出适当边界。\n    relevance_to_ced_stabilizer: >\n      CED 引入了与 extraction F1 低相关的 reward component（evidence quality），\n      根据该论文分析低相关多组件 reward 更不易 overoptimize，\n      可能是 CED 稳定性的另一个理论解释角度。\n\n  - title: \"On-Policy RL with Optimal Reward Baseline\"\n    authors: Anonymous\n    year: 2025\n    venue: arXiv 2505.23585\n    url: https://arxiv.org/abs/2505.23585\n    category: multi_objective_rl\n    role: theoretical_support\n    key_finding: >\n      Optimal baseline 一致性地实现更高训练 reward 和更高 entropy，\n      有效稳定训练并促进更多样的 policy exploration。\n    relevance_to_ced_stabilizer: >\n      CED reward 的多维特性可能起到类似 optimal baseline 效果——\n      evidence quality 维度为 advantage estimation 提供更丰富的参照信号。\n\n  # === Category 6: RSFT Methodology & Theory ===\n\n  - title: \"A Minimalist Approach to LLM Reasoning: from Rejection Sampling to Reinforce\"\n    authors: Xiao et al.\n    year: 2025\n    venue: arXiv 2504.11343\n    url: https://arxiv.org/abs/2504.11343\n    category: rsft_methodology\n    role: key_theoretical_support\n    key_finding: >\n      RAFT（简单 rejection sampling baseline）在数学推理上与 GRPO/PPO 表现相当。\n      消融实验表明 GRPO 的主要优势来自丢弃全错 prompt 而非 reward normalization。\n      提出 Reinforce-Rej，在 RAFT 基础上过滤全对和全错 sample。\n      关键洞察：GRPO 和 RAFT 的核心区别在于负样本处理——GRPO 混合正负样本训练，\n      RAFT 只用正样本，但 RAFT 仍能达到相当性能，说明 rejection sampling 的简单性被低估了。\n    relevance_to_rsft_docre: >\n      直接支持我们的设计选择：(1) RSFT 在 DocRE 上成功而 GRPO 失败，\n      与该论文发现一致——rejection sampling 的 offline 特性天然避免了 catastrophic forgetting；\n      (2) GRPO 主要优势来自过滤全错 prompt，这与我们 RSFT 的 reward-based filtering 机制相同；\n      (3) DocRE structured output 比 math reasoning 更难用 online RL 优化，\n      强化了 offline RSFT 的合理性。\n\n  - title: \"Beyond Rejection Sampling: Trajectory Fusion for Scaling Mathematical Reasoning (TrajFusion)\"\n    authors: Jie Deng et al.\n    year: 2026\n    venue: arXiv 2602.04391\n    url: https://arxiv.org/abs/2602.04391\n    category: rsft_methodology\n    role: method_component\n    key_finding: >\n      传统 RSFT 只用正确轨迹，丢弃错误轨迹。TrajFusion 将错误和正确轨迹交替拼接，\n      显式建模试错推理过程，在困难数学问题上显著超越标准 RFT。\n    relevance_to_rsft_docre: >\n      Future work 方向：可考虑在 DocRE RSFT 中融合失败样本的信息。\n      但 DocRE 的结构化输出（JSON triple）不同于 math 的 chain-of-thought，\n      融合方式需要重新设计。\n\n  - title: \"Rejection Sampling Based Fine Tuning Secretly Performs PPO\"\n    authors: Anonymous\n    year: 2025\n    venue: ICML 2025\n    url: https://openreview.net/forum?id=yQ2UivKlir\n    category: rsft_methodology\n    role: theoretical_support\n    key_finding: >\n      建立 RSFT 与 PPO 之间的理论联系：rejection sampling fine-tuning\n      在特定条件下隐式执行 PPO with marginal KL constraints。\n    relevance_to_rsft_docre: >\n      为 RSFT 的有效性提供理论解释。我们的 RSFT 成功可被视为\n      隐式执行了 constrained policy optimization，\n      避免了显式 GRPO 在 structured output 上的不稳定性。\n\n  # === Category 7: RL for Information Extraction ===\n\n  - title: \"R1-RE: Cross-Domain Relation Extraction with RLVR\"\n    authors: Runpeng Dai, Tong Zheng et al.\n    year: 2025\n    venue: arXiv 2507.04642\n    url: https://arxiv.org/abs/2507.04642\n    category: rl_for_ie\n    role: direct_competitor\n    key_finding: >\n      首个将 RLVR（GRPO + verifiable reward）用于关系抽取的框架。\n      将 RE 重构为推理任务，R1-RE-7B 在跨域 OOD 准确率约 70%，媲美 GPT-4o。\n      Reward 设计：format reward (+1/-3) + metric reward (+2/-1.5)，先验证格式再加准确度。\n      triplet extraction 用 F1-based reward（entity weight=1, triplet weight=3）。\n      未报告 catastrophic forgetting——GRPO 训练后在 MATH-500/IFEval/GPQA 上性能不降反升，\n      说明句子级 RE 的简单 reward 结构足以稳定 GRPO 训练。\n    results:\n      sem2010_in_domain: 91.8\n      sem2010_ood: 66.5\n      mdkg_in_domain: 88.1\n      mdkg_ood: 65.8\n    evidence_generation: false\n    relevance_to_rsft_docre: >\n      最直接竞争者。关键差异与讨论：\n      (1) R1-RE 是句子级 RE，GRPO 成功；我们是文档级 RE，GRPO 失败→RSFT 成功。\n      句子级 RE 每个 sample 只有 1 个 triple（binary classification），reward variance 天然充足；\n      文档级 RE 每个 sample 有数十个 triple，F1 score 作为 reward 在 group 内趋于同质化（frac_zero_std→0.8）。\n      (2) R1-RE 未报告 catastrophic forgetting，进一步支持\"句子级简单 reward 可行，文档级需要 CED\"的论点。\n      (3) R1-RE 关注 OOD 泛化，无 evidence 组件；我们关注 evidence-grounded extraction quality。\n      互补而非直接冲突——R1-RE 证明 RLVR for RE 可行，我们揭示文档级需要额外设计。\n\n  - title: \"MORE-R1: Guiding LVLM for Multimodal Object-Entity Relation Extraction via Stepwise Reasoning with RL\"\n    authors: Anonymous\n    year: 2026\n    venue: arXiv 2603.09478\n    url: https://arxiv.org/abs/2603.09478\n    category: rl_for_ie\n    role: related_method\n    key_finding: >\n      多模态 RE 中用 GRPO + Progressive Sample-Mixing Strategy 优化 LVLM 推理能力。\n      两阶段训练：SFT cold-start + GRPO RL。\n    relevance_to_rsft_docre: >\n      跨模态验证 RL for RE 趋势。其 Progressive Sample-Mixing 与我们\n      RSFT 的 difficulty-aware sampling 思想相通，但在不同模态。\n\n  - title: \"REAR: Reinforced Reasoning Optimization for Event Argument Extraction with Relation-Aware Support\"\n    authors: Jianwen Luo et al.\n    year: 2025\n    venue: EMNLP 2025 Findings\n    url: https://2025.emnlp.org/program/find_papers/\n    category: rl_for_ie\n    role: related_method\n    key_finding: >\n      将强化学习推理优化用于事件论元抽取，结合关系感知支持。\n      不同于 DocRE 但同属 IE 领域的 RL 应用。\n    relevance_to_rsft_docre: >\n      验证 RL 在 IE 任务上的有效性趋势。我们的工作扩展到 DocRE + evidence，\n      且使用 offline RSFT 而非 online RL。\n\n  - title: \"Adaptive Reinforcement Learning Planning: Harnessing LLMs for Complex Information Extraction\"\n    authors: Zepeng Ding et al.\n    year: 2024\n    venue: arXiv 2406.11455\n    url: https://arxiv.org/abs/2406.11455\n    category: rl_for_ie\n    role: background\n    key_finding: >\n      将 LLM 顺序抽取建模为 MDP，用 DDQN 训练 decision module\n      自适应选择实体抽取顺序，提升复杂 IE 性能。\n    relevance_to_rsft_docre: >\n      RL for IE 的早期工作。用 RL 优化抽取策略而非模型本身，\n      与我们 RSFT 直接微调 LLM 的方法路径不同。\n\n  - title: \"Graph-R1: Towards Agentic GraphRAG Framework via End-to-end Reinforcement Learning\"\n    authors: Haoran Luo et al.\n    year: 2025\n    venue: ICML 2026\n    url: https://arxiv.org/abs/2507.21892\n    category: rl_for_ie\n    role: background\n    key_finding: >\n      用端到端 RL 优化 GraphRAG agent 的多轮检索-推理循环，\n      包含 knowledge hypergraph construction（n-ary relation extraction）。\n    relevance_to_rsft_docre: >\n      RL + knowledge extraction 的交叉点。Graph-R1 关注 QA 场景下的知识图谱构建，\n      我们关注 DocRE 的训练优化，应用场景不同。\n\n  # === Category 8: Recent LLM-based DocRE Methods ===\n\n  - title: \"RelPrior: Relation as a Prior - A Novel Paradigm for LLM-based Document-level Relation Extraction\"\n    authors: Anonymous\n    year: 2025\n    venue: arXiv 2511.08143\n    url: https://arxiv.org/abs/2511.08143\n    category: llm_docre\n    role: key_baseline\n    key_finding: >\n      用 binary relation 作为先验过滤无关实体对，再用 predefined relation 匹配实体，\n      避免 LLM 在 DocRE 中被无关实体对分散注意力。\n      在 DocRED/Re-DocRED 上超越现有纯 LLM-based DocRE 方法。\n    results:\n      docred_dev_f1: 47.82\n      docred_test_f1: 48.34\n      re_docred_dev_f1: 55.94\n      re_docred_test_f1: 54.80\n      backbone: LLaMA3-8B\n    evidence_generation: false\n    relevance_to_rsft_docre: >\n      我们的直接 baseline 之一。RelPrior_LLaMA3-8B 在 DocRED test F1=48.34,\n      Re-DocRED test F1=54.80。我们的 RSFT 提升显著更优。\n      RelPrior 是 inference paradigm 创新（两阶段筛选），我们是 training paradigm 创新（RSFT+CED），正交互补。\n\n  - title: \"LMRC: LLM with Relation Classifier for Document-Level Relation Extraction\"\n    authors: Xingzuo Li, Kehai Chen, Yunfei Long, Min Zhang\n    year: 2024\n    venue: arXiv 2408.13889\n    url: https://arxiv.org/abs/2408.13889\n    category: llm_docre\n    role: related_method\n    key_finding: >\n      两阶段方法：先用 attention-based classifier 过滤 NA 实体对（RCP），\n      再用 LLM 在精简候选空间中做多分类（RC）。\n      注意：LMRC 依赖 BERT-based classifier 作为预筛选，非纯 LLM 方法。\n    results:\n      docred_dev_ign_f1: 58.16\n      docred_dev_f1: 59.97\n      docred_test_ign_f1: 58.49\n      docred_test_f1: 60.52\n      re_docred_test_ign_f1: 74.08\n      re_docred_test_f1: 74.63\n      backbone: BERT classifier + LLM\n    evidence_generation: false\n    relevance_to_rsft_docre: >\n      LMRC 在 DocRED test F1=60.52, Re-DocRED test F1=74.63，性能显著高于纯 LLM 方法。\n      但它依赖 BERT classifier 预筛选，本质上是 hybrid 方法而非纯 LLM generative。\n      与我们端到端 LLM 生成方式不同——我们通过 RSFT 的 reward-based filtering 隐式解决 class imbalance。\n\n  - title: \"Ru-LLM: Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction\"\n    authors: Anonymous\n    year: 2025\n    venue: NLPCC 2025\n    url: https://link.springer.com/chapter/10.1007/978-981-95-3343-5_11\n    category: llm_docre\n    role: related_method\n    key_finding: >\n      用频繁模式挖掘 + MCTS 搜索逻辑规则，转化为 prompt 约束 LLM 输出，\n      再用 CoT 验证过滤不满足规则的 triple。\n      在 DWIE、DocRED、Re-DocRED 上声称超越现有 LLM 方法和规则框架。\n      具体 F1 未公开获取（Springer 付费墙），但声称超越 AutoRE 等 LLM baseline。\n    results:\n      note: \"behind Springer paywall; claims SOTA over LLM baselines on DocRED/Re-DocRED/DWIE\"\n    evidence_generation: false\n    relevance_to_rsft_docre: >\n      规则约束方式与我们的 CED reward 在 motivation 上相似（都是引入外部知识约束），\n      但 Ru-LLM 用 inference-time 规则验证（MCTS+CoT），我们用 training-time reward shaping（CED）。\n      Ru-LLM 的规则是数据集级别的频繁模式，CED 是 instance-level 的 evidence faithfulness。\n\n  - title: \"GLiDRE: Generalist Lightweight model for Document-level Relation Extraction\"\n    authors: Anonymous\n    year: 2025\n    venue: arXiv 2508.00757\n    url: https://arxiv.org/abs/2508.00757\n    category: llm_docre\n    role: background\n    key_finding: >\n      基于 dual-encoder 的轻量级零/少样本 DocRE 模型，\n      预训练于 136K 文档的大规模 RE 数据。\n      fully supervised Re-DocRED test F1=77.83，但这是 encoder-based 非 LLM generative。\n      zero-shot Re-DocRED test F1=17.32（超越 LLaMA 3.3 70B 和 Mistral-Small 24B）。\n    results:\n      re_docred_dev_f1: 77.76\n      re_docred_test_f1: 77.83\n      re_docred_zero_shot_test_f1: 17.32\n      fredo_in_domain_1doc_f1: 13.00\n      fredo_in_domain_3doc_f1: 15.71\n      backbone: \"dual-encoder (few hundred M params)\"\n    evidence_generation: false\n    relevance_to_rsft_docre: >\n      不同范式（encoder-based vs LLM generative）。GLiDRE 的 fully supervised F1=77.83\n      远超 LLM-based 方法（RelPrior 54.80），但依赖大规模预训练数据和 encoder 架构。\n      与我们不直接可比——我们关注 LLM generative 范式下的训练优化。\n\n  - title: \"AutoRE: Document-Level Relation Extraction with Large Language Models\"\n    authors: Anonymous\n    year: 2024\n    venue: arXiv 2403.14888\n    url: https://arxiv.org/abs/2403.14888\n    category: llm_docre\n    role: background\n    key_finding: >\n      RHF（Relation-Head-Facts）范式用 Mistral-7B + QLoRA 做端到端 DocRE。\n      关键设计：先抽 relation，再抽 head entity，最后抽 fact triple。\n    results:\n      re_docred_dev_f1_mistral: 53.01\n      re_docred_test_f1_mistral: 51.91\n      re_docred_dev_f1_vicuna: 54.29\n      re_docred_test_f1_vicuna: 53.84\n      docred_dev_f1_llama3: 45.76\n      docred_test_f1_llama3: 45.96\n      re_docred_dev_f1_llama3: 52.28\n      re_docred_test_f1_llama3: 51.97\n      backbone: \"Mistral-7B / Vicuna-7B / LLaMA3-8B (QLoRA)\"\n    evidence_generation: false\n    relevance_to_rsft_docre: >\n      QLoRA fine-tuning for DocRE 的先例。AutoRE_LLaMA3-8B 在 Re-DocRED test F1=51.97,\n      DocRED test F1=45.96。我们的 SFT baseline 与之类似，\n      RSFT 在此基础上引入 reward-guided sample selection 进一步提升。\n\n  # === Category 9: Evidence Generation & Task Performance Trade-off ===\n  # (NEW - 2026-05-15 evidence generation survey)\n\n  - title: \"Mind Your Step (by Step): Chain-of-Thought can Reduce Performance on Tasks where Thinking Makes Humans Worse\"\n    authors: Sprague et al.\n    year: 2024\n    venue: NeurIPS 2024\n    url: https://arxiv.org/abs/2410.21333\n    category: evidence_generation_tradeoff\n    role: key_evidence\n    key_finding: >\n      CoT 在某些任务上降低性能高达 36.3%（o1-preview vs GPT-4o）。\n      显式推理步骤引入 error accumulation，且模型可能 overfit 到解释格式而非任务结构。\n      隐式推理（hidden activations）在分布偏移下优于显式 token-level 推理。\n    relevance_to_evidence_tradeoff: >\n      直接支持我们的核心发现：要求模型同时生成 evidence sentences 是一种\"显式推理\"，\n      会对主任务（RE）产生性能代价（~8pp F1 下降）。\n      Related Work 引用点：evidence generation 作为 structured explanation，\n      与 CoT 共享\"显式推理降低主任务性能\"的普遍模式。\n\n  - title: \"Eider: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion\"\n    authors: Xie et al. (Google Research)\n    year: 2022\n    venue: ACL Findings 2022\n    url: https://arxiv.org/abs/2106.08657\n    category: evidence_generation_tradeoff\n    role: closest_docre_precedent\n    key_finding: >\n      Joint 训练 RE + evidence extraction，关键创新在 inference-stage fusion：\n      分别在 extracted evidence 和 full document 上做 RE 预测再通过 blending layer 融合。\n      DocRED 上提升 1.37 Ign F1。Silver evidence labels（启发式规则构建）即可提升 RE 性能。\n    relevance_to_evidence_tradeoff: >\n      最直接的 DocRE + evidence 先例。EIDER 的核心洞察是 evidence 需要 inference-stage 融合\n      而非 joint generation——暗示 joint generation 会引入 noise。\n      我们的 CED reranker 是 LLM-era 版本的 inference-stage fusion：\n      先生成多个候选（含 evidence），再用 NLI 在推理阶段选最佳。\n      Related Work 引用点：encoder-based DocRE 中 evidence 的使用方式，与我们 generative 范式的关键差异。\n\n  - title: \"Exploring the Trade-off Between Model Performance and Explanation Plausibility of Text Classifiers Using Human Rationales\"\n    authors: Resck, Raimundo, Poco\n    year: 2024\n    venue: NAACL Findings 2024\n    url: https://arxiv.org/abs/2404.03098\n    category: evidence_generation_tradeoff\n    role: formal_framework\n    key_finding: >\n      用 multi-objective optimization 探索 performance vs explanation plausibility 的 Pareto frontier。\n      引入 rationale 约束创建 contrastive loss，证实加入 rationale supervision 会降低主任务性能，\n      但存在 Pa",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false,
    "persistedOutputPath": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/36a03546-b7c6-4659-a047-11cc70593f2c/tool-results/b4ppdl9gh.txt",
    "persistedOutputSize": 48786
  }
}
```

</details>

---

### Assistant

_source line 128_

<details><summary>Logged reasoning block</summary>

```text
The file is too large to pass directly to save_project_file. Let me read it in chunks and pass it. Actually, I should just try the save_project_file with the file content. Let me read the full file content using the Read tool.

Actually, looking at the save_project_file tool description: "Writable: memory.md, writing_plan.yaml, paper_framing.md. Other files have dedicated tools."

So literature_map.yaml might NOT be writable via save_project_file. But since I already edited the file directly on disk, the changes are already saved. The file exists at the right path. 

Since the file is already 47KB and the direct edit worked, I'll skip trying to push it through save_project_file and move on to the summary.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "b6e5adcf-f77c-4b74-93bf-33aa7d38418d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ruL82GwWHveJ9nwyK5BzR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1234,
      "cache_read_input_tokens": 97614,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1234
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

_source line 129_

文件已直接编辑到磁盘，YAML 验证通过。下面是总结。

---

## 文献扫描结果

### 新增 11 篇论文（分布在 8 个新类别）

| # | 论文 | 类别 | 与 FREIGE 的关系 |
|---|------|------|-----------------|
| 1 | **EvidenceRL** (Ben Tamo+, 2026) | evidence_grounded_rl | **最大 novelty 威胁** — GRPO + evidence faithfulness reward，但在 QA 域，非 DocRE |
| 2 | **MO-GRPO** (Ichihara+, 2025) | multi_objective_grpo | GRPO 多目标 reward hacking 分析 |
| 3 | **RDPO** (Bai+, 2026) | multi_objective_grpo | Reward 去相关，理论支持 CED 的低相关多维 reward |
| 4 | **GRPO is Secretly a PRM** (Sullivan & Koller, 2025) | grpo_theory | GRPO=隐式 PRM，解释 DocRE 多 triple 场景下 reward 信号不足 |
| 5 | **Reward Hacking Survey** (Wang+, 2026) | grpo_theory | Proxy Compression Hypothesis 解释 QLoRA decoupling |
| 6 | **FP16 for RL** (Qi+, 2025) | training_precision_rl | BF16 导致 RL 训练不稳定，支持 QLoRA-specific instability |
| 7 | **R²GRPO** (Li+, 2025) | rl_for_ie | GRPO 用于科学 IE，rule-based reward |
| 8 | **ADELIE** (Qi+, EMNLP 2024) | llm_ie_alignment | SFT+DPO 对齐 IE，代表性 baseline |
| 9 | **CoT is not Explainability** (Barez+, 2025) | unfaithful_reasoning | CoT = post-rationalization，支持 CED reranker 的必要性 |
| 10 | **Characterizing LLMs as Rationalizers** (ACL Findings 2024) | unfaithful_reasoning | LLM evidence 不可靠的实证 |
| 11 | **Latent CoT Survey** (Chen+, 2025) | latent_vs_explicit_reasoning | 显式 vs 隐式推理 trade-off 的全景综述 |

### Novelty 威胁评估

**EvidenceRL 是唯一需要认真对待的 novelty 威胁**，但差异明确：

1. EvidenceRL 在 QA 域，evidence grounding 和 correctness **同时提升**（无 trade-off）；FREIGE 在 DocRE 中发现 evidence generation 有 ~8pp rel_f1 代价（evidence tax）——这是 EvidenceRL 没有的核心发现
2. EvidenceRL 无 task decoupling 现象（QLoRA-specific）
3. EvidenceRL 无 inference-time CED reranker

**无人研究过 evidence tax：** 搜索 "evidence generation cost/trade-off in DocRE" 方向，没有找到任何工作量化 evidence generation 对 RE 性能的代价。这是 FREIGE 的独特贡献点。

**无人报告 task decoupling：** QLoRA + GRPO 下 evidence-extraction decoupling 是全新发现，MO-GRPO/RDPO 的多目标分析和 FP16 论文的 precision instability 分析提供了理论支撑但没有直接观察到此现象。

### Related Work 写作建议

- 在 GRPO for IE 段落中，需要讨论 EvidenceRL 并明确与我们的差异
- MO-GRPO + RDPO 可作为 CED training stabilizer 的理论支撑
- "GRPO is Secretly a PRM" 可强化 multi-triple DocRE 需要更细粒度 reward 的论点
- FP16 论文 + Reward Hacking Survey 可支撑 QLoRA decoupling 的机制假说

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "uuid": "f7776eae-5e5d-4970-8a2f-e6ddf0b9d706",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ruL82GwWHveJ9nwyK5BzR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1234,
      "cache_read_input_tokens": 97614,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1234
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

### Task result

_source line 130_

文件已直接编辑到磁盘，YAML 验证通过。下面是总结。

---

## 文献扫描结果

### 新增 11 篇论文（分布在 8 个新类别）

| # | 论文 | 类别 | 与 FREIGE 的关系 |
|---|------|------|-----------------|
| 1 | **EvidenceRL** (Ben Tamo+, 2026) | evidence_grounded_rl | **最大 novelty 威胁** — GRPO + evidence faithfulness reward，但在 QA 域，非 DocRE |
| 2 | **MO-GRPO** (Ichihara+, 2025) | multi_objective_grpo | GRPO 多目标 reward hacking 分析 |
| 3 | **RDPO** (Bai+, 2026) | multi_objective_grpo | Reward 去相关，理论支持 CED 的低相关多维 reward |
| 4 | **GRPO is Secretly a PRM** (Sullivan & Koller, 2025) | grpo_theory | GRPO=隐式 PRM，解释 DocRE 多 triple 场景下 reward 信号不足 |
| 5 | **Reward Hacking Survey** (Wang+, 2026) | grpo_theory | Proxy Compression Hypothesis 解释 QLoRA decoupling |
| 6 | **FP16 for RL** (Qi+, 2025) | training_precision_rl | BF16 导致 RL 训练不稳定，支持 QLoRA-specific instability |
| 7 | **R²GRPO** (Li+, 2025) | rl_for_ie | GRPO 用于科学 IE，rule-based reward |
| 8 | **ADELIE** (Qi+, EMNLP 2024) | llm_ie_alignment | SFT+DPO 对齐 IE，代表性 baseline |
| 9 | **CoT is not Explainability** (Barez+, 2025) | unfaithful_reasoning | CoT = post-rationalization，支持 CED reranker 的必要性 |
| 10 | **Characterizing LLMs as Rationalizers** (ACL Findings 2024) | unfaithful_reasoning | LLM evidence 不可靠的实证 |
| 11 | **Latent CoT Survey** (Chen+, 2025) | latent_vs_explicit_reasoning | 显式 vs 隐式推理 trade-off 的全景综述 |

### Novelty 威胁评估

**EvidenceRL 是唯一需要认真对待的 novelty 威胁**，但差异明确：

1. EvidenceRL 在 QA 域，evidence grounding 和 correctness **同时提升**（无 trade-off）；FREIGE 在 DocRE 中发现 evidence generation 有 ~8pp rel_f1 代价（evidence tax）——这是 EvidenceRL 没有的核心发现
2. EvidenceRL 无 task decoupling 现象（QLoRA-specific）
3. EvidenceRL 无 inference-time CED reranker

**无人研究过 evidence tax：** 搜索 "evidence generation cost/trade-off in DocRE" 方向，没有找到任何工作量化 evidence generation 对 RE 性能的代价。这是 FREIGE 的独特贡献点。

**无人报告 task decoupling：** QLoRA + GRPO 下 evidence-extraction decoupling 是全新发现，MO-GRPO/RDPO 的多目标分析和 FP16 论文的 precision instability 分析提供了理论支撑但没有直接观察到此现象。

### Related Work 写作建议

- 在 GRPO for IE 段落中，需要讨论 EvidenceRL 并明确与我们的差异
- MO-GRPO + RDPO 可作为 CED training stabilizer 的理论支撑
- "GRPO is Secretly a PRM" 可强化 multi-triple DocRE 需要更细粒度 reward 的论点
- FP16 论文 + Reward Hacking Survey 可支撑 QLoRA decoupling 的机制假说

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 399523,
  "duration_api_ms": 570018,
  "num_turns": 51,
  "stop_reason": "end_turn",
  "session_id": "36a03546-b7c6-4659-a047-11cc70593f2c",
  "total_cost_usd": 2.7167042499999994,
  "usage": {
    "input_tokens": 4043,
    "cache_creation_input_tokens": 87007,
    "cache_read_input_tokens": 1586351,
    "output_tokens": 14636,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 87007,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1455,
        "cache_read_input_tokens": 97614,
        "cache_creation_input_tokens": 1234,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1234
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 633600,
      "outputTokens": 18004,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 27,
      "costUSD": 0.9936200000000002,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 4043,
      "outputTokens": 14636,
      "cacheReadInputTokens": 1586351,
      "cacheCreationInputTokens": 87007,
      "webSearchRequests": 0,
      "costUSD": 1.7230842499999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "321304fb-7e4b-4de1-8df1-d86f5a6070c1"
}
```

</details>

---
