# Research conversation: <project_context> # 项目: cost-verify-agent-rl ## 运行环境 - 服务器名: bjb1-17606 - SSH 账户: root（调用 ssh_execute / submit_training_ — Part 2 of 2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../research-conversation-project-context-cost-verify-agent-rl-bjb1-17606-ssh-root-ssh-execute-submit-tr-copy-101.md) · [Structured JSON](../../../sessions/b6/b67f8a8f02ae0f620210.json)

## Round 1

### Tool result

_source line 225 · 2026-05-15T23:35:18.875Z_

<details><summary>↩ Tool result · `toolu_01VgN1oFQzQyY3RoEbnMayBg`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/phase_b_prereq_analysis.md
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "8d84ac72-0146-4a15-8cbc-679f27f7b126",
  "isSidechain": false,
  "promptId": "dbebae8f-5a7a-4ba2-81a2-7aab9dd844f6",
  "type": "user",
  "uuid": "92d8a166-2845-4cb2-a9b7-9302286e213d",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/phase_b_prereq_analysis.md",
    "content": "# Phase B 前置条件技术方案\n\n## 概要\n\nPhase B (B-IAVR selective verification) 有两个前置条件。经代码分析，两者技术风险均低，总预估 4-6 Worker-hours。\n\n---\n\n## 前置 1: `&lt;VERIFY>` Special Token 注册\n\n### 现状\n\n- Qwen3-1.7B tokenizer 将 `&lt;VERIFY>` 拆成 3 个 sub-token: `<` (27) + `VERIFY` (46223) + `>` (29)\n- B-IAVR 代码已实现（`ragen/biavr/verify_mechanism.py`），用字符串前缀匹配 `parse_verify_token()` 检测 `&lt;VERIFY>`\n- `ctx_manager.py` 在 `biavr_enabled` 时不添加 generation prompt prefix（让模型自由选择 `&lt;VERIFY>` 或 `&lt;think>`）\n\n### 关键发现：无需 resize_token_embeddings\n\n| 属性 | 值 |\n|---|---|\n| `config.json` vocab_size | 151936 |\n| tokenizer vocab_size | 151643 |\n| tokenizer len (含 added_tokens) | 151669 |\n| 添加 `&lt;VERIFY>` 后 | 151670 |\n| 剩余空闲 slot | **266** |\n\n模型 embedding 层已分配 151936 维，添加 `&lt;VERIFY>` (id=151669→151670) 不触发 resize。这消除了 FSDP/vLLM 同步 resize 的风险。\n\n### 方案：离线注册 + 保存扩展 tokenizer\n\n**步骤 1: 创建扩展 tokenizer（一次性脚本）**\n\n```python\nfrom transformers import AutoTokenizer\ntokenizer = AutoTokenizer.from_pretrained(SFT_CHECKPOINT_PATH)\ntokenizer.add_special_tokens({\"additional_special_tokens\": [\"&lt;VERIFY>\"]})\ntokenizer.save_pretrained(EXTENDED_TOKENIZER_PATH)\n# 同时 copy model weights（不变）到同一目录\n```\n\n输出目录作为 Phase B 的 `model_path`。\n\n**步骤 2: 确认传播链一致**\n\ntokenizer 在 4 处加载，需全部指向扩展版本：\n\n| 加载点 | 文件 | 方式 |\n|---|---|---|\n| train.py `main()` | `train.py:L176` | `hf_tokenizer(model_path)` — 改 config model_path 即可 |\n| FSDP actor `_build_model_optimizer` | `fsdp_workers.py:L308` | `hf_tokenizer(local_path)` — local_path 来自 model.path，同上 |\n| FSDP ref | 同上 | 同 actor |\n| vLLM rollout | `agent_proxy.py` VllmWrapperWg | `LLM(model_name)` — vLLM 自动从 model_name 读 tokenizer |\n\n结论：只要 `model_path` 指向含扩展 tokenizer 的目录，所有组件自动对齐。\n\n**步骤 3: 新 token 嵌入初始化**\n\nQwen3 embedding 层 151936 维中 [151669, 151936) 为零初始化。`&lt;VERIFY>` 获得 id 151669，初始嵌入接近零向量。\n\n建议：不做额外初始化。GRPO 训练会自然学习该 embedding。理由：\n- `&lt;VERIFY>` 语义全新（非已有概念的同义词），无合理初始化目标\n- 初始阶段 lambda_init=0，verify 无惩罚，模型有充分空间探索\n- 类似 `&lt;think>` 等 tag 在 SFT 阶段也是从 chat template 学来的\n\n### 代码改动清单\n\n| 文件 | 改动 | 说明 |\n|---|---|---|\n| `scripts/prepare_biavr_tokenizer.py` | **新建** | 一次性脚本：加载 SFT checkpoint tokenizer → add `&lt;VERIFY>` → 保存到新目录 |\n| `config/_alfworld_phase_b.yaml` | 修改 `model_path` | 指向扩展 tokenizer 的 checkpoint 目录 |\n| 无其他代码改动 | — | 框架自动从 model_path 读 tokenizer |\n\n### 风险与 Fallback\n\n| 风险 | 概率 | Fallback |\n|---|---|---|\n| vLLM 不认新 special token | 低 | vLLM 从 tokenizer.json 读 added_tokens，HF 格式兼容 |\n| 新 token embedding 训练不收敛 | 低 | 用 `&lt;think>` 平均 embedding 作初始化（`prepare_biavr_tokenizer.py` 中可选） |\n| 模型倾向全部 verify 或全部不 verify | 中 | Lagrangian multiplier 自适应调节 verify rate，已在 reward.py 实现 |\n| **不注册也能跑** | — | 当前 3-token 方案已可工作，注册 special token 是优化而非必须 |\n\n**预估工作量：1-2 Worker-hours**（脚本编写 + 验证 tokenizer 一致性 + dry-run 测试）\n\n---\n\n## 前置 2: a_pre 推理开销量化\n\n### 度量定义\n\na_pre（pre-verification action）是 B-IAVR 在 VERIFY 步生成的 counterfactual：用无 self-guidance 的 prompt 做 greedy decode，与实际 action 对比以判断 verification 是否 informative。\n\n**核心度量：token 数**（非 latency/FLOPs），理由：\n1. 论文 cost-efficiency metric 基于 token 数（与模型调用次数/长度成正比）\n2. Latency 受 batch size、GPU 利用率等运行时因素影响，不可复现\n3. Token 数直接映射到 FLOPs（FLOPs ≈ 6 × params × tokens for decode）\n\n### 度量体系\n\n| 度量名 | 定义 | 计算方式 |\n|---|---|---|\n| `C_verify_per_step` | 单次 verification 的 token 开销 | a_pre 生成的 token 数（max_tokens=256，实际通常更短） |\n| `C_always_on` | Always-On 每 episode 总开销 | Σ(每步 self-guidance token 数) |\n| `C_biavr(β)` | B-IAVR 目标 verify_rate=β 下的开销 | β × N_turns × avg(C_verify_per_step) |\n| `savings(β)` | 相对 always-on 的节省比 | 1 - C_biavr(β) / C_always_on |\n| `a_pre_overhead_ratio` | a_pre 占总推理的比例 | a_pre_tokens / (a_pre_tokens + normal_response_tokens) |\n\n### 测量方案\n\n**Phase A 数据收集（不需要额外实验）：**\n\nPhase A always-on self-guidance 的每步 response 已包含 self-guidance reasoning。从 Phase A rollout 数据中可直接提取：\n\n```python\n# 从 rollout_states 中提取每步 response\nfor episode in rollout_states:\n    for turn in episode['turns']:\n        response_tokens = tokenizer.encode(turn['response'])\n        # 记录：total_tokens, think_tokens, answer_tokens\n```\n\n**a_pre 开销估算（不需要真正生成 a_pre）：**\n\n`pre_action.py` 中 `compute_pre_action_prompt` 设定 `max_tokens=256, temperature=0, top_k=1`。实际 a_pre 生成的 ALFWorld action 很短（典型 5-15 tokens，如 `go to desk 1`）。但 a_pre 还包括 `&lt;think>...&lt;/think>` 推理，估计 30-80 tokens。\n\n精确量化需运行一次 a_pre batch inference。方案：\n\n1. 从 Phase A 最新 checkpoint 加载模型\n2. 取 100 个 rollout 步的 conversation_history\n3. 用 `build_pre_action_messages` 构建 a_pre prompt\n4. 用 vLLM greedy decode 生成\n5. 统计 token 数分布\n\n### 实现方案\n\n**步骤 1: 在 `agent_proxy.py` 添加 a_pre token 计数**\n\n`_compute_and_update_a_pre` 方法（agent_proxy.py:411-435）已实现 a_pre 生成逻辑。只需在 biavr_tracker 中增加 token 统计：\n\n```python\n# agent_proxy.py, _compute_and_update_a_pre 中：\na_pre_tokens = len(tokenizer.encode(a_pre_response))\nself.biavr_tracker.record_a_pre_cost(a_pre_tokens)\n```\n\n**步骤 2: 扩展 BIAVRTracker**\n\n在 `ragen/biavr/reward.py` 的 `BIAVRTracker` 中增加：\n\n```python\n_a_pre_token_counts: List[int] = field(default_factory=list)\n\ndef record_a_pre_cost(self, n_tokens: int):\n    self._a_pre_token_counts.append(n_tokens)\n\n@property\ndef avg_a_pre_tokens(self) -> float:\n    return sum(self._a_pre_token_counts) / max(len(self._a_pre_token_counts), 1)\n\ndef get_metrics(self) -> dict:\n    # 在现有 metrics 基础上增加：\n    metrics[\"biavr/avg_a_pre_tokens\"] = self.avg_a_pre_tokens\n    metrics[\"biavr/total_a_pre_tokens\"] = sum(self._a_pre_token_counts)\n    return metrics\n```\n\n**步骤 3: 基线开销脚本**\n\n```python\n# scripts/quantify_a_pre_cost.py\n# 从 Phase A rollout 数据计算 always-on baseline\n# 从 a_pre dry-run 计算 per-verify 开销\n# 输出：C_always_on, C_verify_per_step, projected savings at β=0.3\n```\n\n### 代码改动清单\n\n| 文件 | 改动 | 说明 |\n|---|---|---|\n| `ragen/biavr/reward.py` | 扩展 `BIAVRTracker` | 添加 a_pre token 计数和统计 |\n| `ragen/llm_agent/agent_proxy.py` | `_compute_and_update_a_pre` | 记录 a_pre response token 数 |\n| `scripts/quantify_a_pre_cost.py` | **新建** | 基线开销量化脚本 |\n| `ragen/biavr/tests/test_biavr.py` | 增加测试 | 测试 token 计数逻辑 |\n\n### 风险与 Fallback\n\n| 风险 | 概率 | Fallback |\n|---|---|---|\n| a_pre 推理显著拖慢训练 | 中 | 采样子集（每 N 步做一次 a_pre），或异步计算 |\n| a_pre response 过长（接近 max_tokens=256） | 低 | ALFWorld action 短，调低 max_tokens 到 128 |\n| Phase A 还没产出可用 rollout 数据 | 取决于 Phase A 进度 | 用 SFT checkpoint 做 zero-shot rollout 估算 |\n\n**预估工作量：2-3 Worker-hours**（tracker 扩展 + 脚本 + 从 Phase A 数据分析）\n\n---\n\n## 总结\n\n| 前置条件 | 方案 | 核心改动 | 工作量 | 阻塞风险 |\n|---|---|---|---|---|\n| `&lt;VERIFY>` token 注册 | 离线扩展 tokenizer，无需 resize_embeddings | 1 个新脚本 + 改 config | 1-2h | 低 |\n| a_pre 开销量化 | BIAVRTracker 扩展 + 基线脚本 | 3 文件改动 + 1 个新脚本 | 2-3h | 低（依赖 Phase A 数据） |\n| **合计** | | | **4-6h** | |\n\n### 关键前提\n\n1. Phase A 需先跑出至少一轮 rollout 数据用于 a_pre 开销基线估算\n2. `&lt;VERIFY>` token 注册可与 Phase A 并行进行（互不阻塞）\n3. 如果 Phase A 验证 3-token `&lt;VERIFY>` 序列已够用（模型能学会完整输出），可跳过 special token 注册\n\n### 建议执行顺序\n\n1. Phase A 实验继续推进，收集 rollout 数据\n2. 并行：准备 `&lt;VERIFY>` 扩展 tokenizer（prepare_biavr_tokenizer.py）\n3. Phase A 有数据后：运行 a_pre 开销量化脚本\n4. 两个前置条件完成 → 启动 Phase B 实验\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "8d84ac72-0146-4a15-8cbc-679f27f7b126",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7daea697-1682-4b50-9618-236c1a95e17f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

</details>

---


### Assistant

_source line 226 · 2026-05-15T23:35:27.754Z_

文档已保存到 `artifacts/phase_b_prereq_analysis.md`。

核心结论：

**前置 1（`&lt;VERIFY>` token）**：Qwen3-1.7B 的 embedding 层有 151936 slot，tokenizer 只用了 151669，添加 `&lt;VERIFY>` 后为 151670 — **不需要 resize_token_embeddings**。只需一个离线脚本扩展 tokenizer 并保存到新目录，改 config 的 model_path 即可，所有组件（FSDP actor/ref、vLLM rollout）自动对齐。工作量 1-2h。

**前置 2（a_pre 开销量化）**：核心度量用 token 数而非 latency。在 `BIAVRTracker` 中增加 a_pre token 统计，配合一个基线量化脚本从 Phase A rollout 数据计算 always-on 开销。工作量 2-3h，依赖 Phase A 产出 rollout 数据。

**总预估 4-6 Worker-hours，两个前置条件可与 Phase A 并行推进。**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92d8a166-2845-4cb2-a9b7-9302286e213d",
  "isSidechain": false,
  "requestId": "req_011Cb5ENbFdWCxzA3NfdoSkT",
  "type": "assistant",
  "uuid": "4ab576b7-06c7-4a5f-b71e-198e1c8f7d16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "7daea697-1682-4b50-9618-236c1a95e17f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MjU7M5mafWRmdaDGjrzvqH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3925,
      "cache_read_input_tokens": 99603,
      "output_tokens": 326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3925,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 326,
          "cache_read_input_tokens": 99603,
          "cache_creation_input_tokens": 3925,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3925
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


### Runtime record

_source line 227_

```json
{
  "type": "last-prompt",
  "leafUuid": "4ab576b7-06c7-4a5f-b71e-198e1c8f7d16",
  "sessionId": "7daea697-1682-4b50-9618-236c1a95e17f"
}
```

---


### Runtime record

_source line 228_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze Phase B prerequisites for B-IAVR implementation",
  "sessionId": "7daea697-1682-4b50-9618-236c1a95e17f"
}
```

---
