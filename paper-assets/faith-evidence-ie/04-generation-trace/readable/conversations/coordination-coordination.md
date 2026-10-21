# Project coordination

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 20
- **Recorded user turns:** 2
- **Tool calls:** 8
- **Original source:** `logs/chats/feishu_group_oc_c10d8c34544498f36f499ff2bc6355a5_briefer.jsonl`
- **Structured JSON:** [`18b057c44a2626d7df1e.json`](../../sessions/18/18b057c44a2626d7df1e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

8 recorded events

### User

_source line 1 · 2026-05-14T11:08:20.315207+00:00_

[飞书用户 曹晓玉 (ou_ede2a978d615f30441645de8c66d0b75)]: Agent 们到目前为止一共做过多少个实验，结果都是怎么样的？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c10d8c34544498f36f499ff2bc6355a5:briefer",
  "source": "feishu:oc_c10d8c34544498f36f499ff2bc6355a5"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-14T11:08:26.736449+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c10d8c34544498f36f499ff2bc6355a5:briefer",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-14T11:08:27.267736+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c10d8c34544498f36f499ff2bc6355a5:briefer",
  "tool": "ToolSearch",
  "elapsed_ms": 531
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T11:08:29.982599+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "faith-evidence-ie",
  "limit": "0",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c10d8c34544498f36f499ff2bc6355a5:briefer",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "faith-evidence-ie",
    "limit": "0",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-14T11:08:30.534840+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"mvp2_grpo_ced_r2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:58:11.663Z\", \"updated_at\": \"2026-05-14T10:58:49.260Z\", \"spec\": {\"command\": \"accelerate launch --config_file freige/configs/accelerate_4gpu.yaml -m freige.training.grpo_trainer --model_name Qwen3-4B --learning_rate 2e-5 --kl_coef 0.05 --save_steps 20 --format_reward_weight 0.3 --f1_reward_weight 3.0 --ced_reward_weight 1.0 --num_iterations 2\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/docred\", \"data_count\": {\"train\": 3027, \"dev\": 985}, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"CED reward with balanced weights (format×0.3, f1×3.0, ced×1.0) + KL=0.05 + save_steps=20 + num_iterations=2 prevents mode collapse and improves Evi-F1\", \"parent\": \"mvp2_grpo_ced_r1\", \"hyperparams\": {\"learning_rate\": \"2e-5\", \"kl_coef\": 0.05, \"save_steps\": 20, \"num_iterations\": 2, \"format_reward_weight\": 0.3, \"f1_reward_weight\": 3, \"ced_reward_weight\": 1, \"per_device_batch_size\": 1, \"gradient_accumulation_steps\": 16, \"num_generations\": 4}}}, \"mvp2_grpo_ced_r1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:02:41.858Z\", \"updated_at\": \"2026-05-14T10:37:23.856Z\", \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp && accelerate launch --config_file freige/configs/accelerate_4gpu.yaml -m freige.training.grpo_trainer --model_name /root/autodl-tmp/models/Qwen3-4B --sft_adapter /root/autodl-tmp/sft_output --data_dir /root/autodl-tmp/data/docred --stage 3 --tau_start 0.3 --tau_end 0.5 --output_dir /root/autodl-tmp/grpo_s
…[truncated 10381 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c10d8c34544498f36f499ff2bc6355a5:briefer",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 552
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T11:08:30.585633+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "report.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c10d8c34544498f36f499ff2bc6355a5:briefer",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "faith-evidence-ie",
    "file": "report.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-14T11:08:31.093801+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/report.md\", \"content\": \"# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| mvp2_grpo_ced_r2 | — | — | — | — |\\n\\n## 待处理\\n- mvp2_sft_eval（准备中）\\n- mvp2_grpo_extract（准备中）\\n- mvp2_grpo_flatnli（准备中）\\n\\n## 近期结论\\n- **mvp2_grpo_ced_r1** (killed): —\\n- **mvp2_grpo_ced** (failed): —\\n- **precompute_nli_train** (success): —\\n\\n## 趋势\\n成功 4 / 负向 0 / 失败 1 / 共 6\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\ngpu-5090-4x-1: 无 GPU 信息\\nrtx5090-4x: 空闲 cuda:0, cuda:1, cuda:2, cuda:3\\n\\n## 告警\\n- mvp2_grpo_ced: 训练失败 — unknown\\n- mvp2_grpo_ced_r1: 已被终止 — unknown\\n\", \"total_chars\": 595, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c10d8c34544498f36f499ff2bc6355a5:briefer",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 508
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-14T11:08:57.569192+00:00_

截至目前 registry 中共 **10 个实验**，其中 7 个已执行（或正在执行），3 个仍在准备中。按时间顺序：

### 已完成（4 个成功 + 2 个失败/终止）

| 实验 | 状态 | 说明 |
|------|------|------|
| **mvp1_ced_signal** | ✅ 成功 | CED 信号验证——在 DocRED dev 上测试 NLI 打分能否区分正确/错误证据。结果：区分准确率 81.5%，平均 margin 0.48，与 Jaccard 相关性 0.34，**通过验证**。 |
| **smoke_test_grpo** | ✅ 成功 | GRPO 训练管线冒烟测试，确认 4 卡 accelerate + TRL 能跑通。 |
| **mvp2_sft_warmup** | ✅ 成功 | Qwen3-4B QLoRA SFT 热身训练（3 epoch），eval_loss=0.72，accuracy=83.5%。产出 adapter 供后续 GRPO 使用。 |
| **precompute_nli_train** | ✅ 成功 | 预计算训练集 NLI 缓存，为 CED reward 做准备。 |
| **mvp2_grpo_ced** | ❌ 失败 | 首次 GRPO+CED reward 尝试，跑了 ~36 分钟后因代码 bug 崩溃（`tail` 字段为 None 导致 AttributeError）。 |
| **mvp2_grpo_ced_r1** | ⚠️ 被终止 | 修复 bug 后重跑，在 step 80/189 发现 **mode collapse**（F1 跌到 0.001，format reward hacking）。诊断出三个根因并修复：checkpoint 保存策略、reward 权重不均衡、clip ratio 未生效（num_iterations=1）。 |

### 正在运行（1 个）

| 实验 | 说明 |
|------|------|
| **mvp2_grpo_ced_r2** | 基于 r1 的所有修复重跑：reward 加权（format×0.3, f1×3.0, ced×1.0）、KL=0.05、num_iterations=2、步级 checkpoint。目前运行中。 |

### 准备中（3 个，尚未启动）

- **mvp2_sft_eval** — SFT baseline 评测
- **mvp2_grpo_extract** — 纯抽取 reward（无证据 reward）的 GRPO 对照组
- **mvp2_grpo_flatnli** — Flat-NLI reward（无对比成分）的 GRPO 对照组

---

**整体进展**：项目今天（5/14）刚开始跑实验，目前处于 MVP2 阶段。CED 信号已验证有效，SFT 热身已完成，GRPO 训练经历两轮调试后第三轮（r2）正在跑。三个对照实验还在排队。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c10d8c34544498f36f499ff2bc6355a5:briefer"
}
```

</details>

---

## Round 2

12 recorded events

### User

_source line 9 · 2026-05-15T06:32:36.214286+00:00_

[飞书用户 孙震 (ou_8d2fa04f2efbff70669af1254093c4aa)]: 我现在需要你非常详细的给我讲一下这个idea的motivation，背景，当前工作，问题所在，我们的发现等，总之你要把你对这个idea的所有理解都告诉我

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_c10d8c34544498f36f499ff2bc6355a5:briefer",
  "source": "feishu:oc_c10d8c34544498f36f499ff2bc6355a5"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T06:32:45.292124+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "ROADMAP.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c10d8c34544498f36f499ff2bc6355a5:briefer",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "faith-evidence-ie",
    "file": "ROADMAP.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T06:32:45.869052+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md\", \"content\": \"# faith-evidence-ie — Research Dashboard\\n\\n> 最后更新: 2026-05-15 01:42 UTC | 更新原因: D036: 撤销 diversity crisis，恢复 4 卡并行 RSFT 生成\\n\\n## 核心方向\\nFREIGE: 用对比证据判别 (CED) 奖励训练 LLM 在文档级关系抽取中同时生成抽取结果和可验证证据。\\n\\n## 当前进展\\n- 阶段: MVP 验证（MVP-1 ✅, MVP-2 运行中 — GRPO 判死，离线 RL pivot 进行中）\\n- **MVP-1**: CED margin 0.4827, accuracy 81.5%, r=0.34 — PASS\\n- **SFT warmup**: 完成（eval loss 0.72, token accuracy 83.5%）\\n- **GRPO+QLoRA 全线 FAIL (D031/D033)**: CED 有效但在线 RL 导致 rel_f1 catastrophic forgetting\\n- **D034/D035 撤销 (D036)**: diversity crisis 为监控 bug（度量代码错误报 1.0/8，实际 7.11/8 median=8.0）\\n- **RSFT 生成**: T=0.7 diversity 充足，4 卡并行分片重启中（已完成 302/3027 docs，断点续传）\\n\\n## GPU 分配（2026-05-15 实况）\\n\\n| GPU | 状态 | 任务 |\\n|-----|------|------|\\n| cuda:0 | 🏃 启动中 | RSFT generate shard 0 |\\n| cuda:1 | 🏃 启动中 | RSFT generate shard 1（续跑已有 302 docs） |\\n| cuda:2 | 🏃 启动中 | RSFT generate shard 2 |\\n| cuda:3 | 🏃 启动中 | RSFT generate shard 3 |\\n\\n## MVP-2: 离线 RL 路线\\n\\n### RSFT 流水线（diversity gate 已通过）\\n1. ✅ 代码准备（含 generation_config 修复 + 分片并行 + diversity 监控修复）\\n2. 🏃 生成候选（4 卡并行，预计 ~3h 完成全量 3027 docs × 8 generations）\\n3. ⬜ CED 打分筛选\\n4. ⬜ RSFT 训练\\n5. ⬜ Eval\\n\\n### 方案 2: DPO + CED（RSFT 完成后考虑）\\n\\n### Contingency（RSFT 训练效果不佳时）\\n1. Prompt-level 多样性: 不同 prompt 模板 / 不同实体子集\\n2. CED 作为 reranker（推理时方案）\\n3. 全参微调（non-QLoRA）\\n\\n## 近期任务\\n- [ ] 4 卡并行 RSFT 生成完成（~3h）\\n- [ ] 合并 4 shard 输出\\n- [ ] CED 打分筛选 top candidates\\n- [ ] RSFT 训练\\n- [ ] Eval: rel_f1 / evidence quality\\n\\n## Post-MVP 流程（MVP-2 通过后）\\n1. complete_mvp() → paper_framing.md → experiment_plan.yaml → dream_simulate\\n\\n## GPU 预算\\n- 硬件: 4× RTX 5090 32GB\\n- GRPO 已消耗: ~60+ GPU-hours\\n- RSFT 生成预估: ~3h（4 卡并行）\\n- RSFT 训练预估: ~4-8h\\n\\n## 评审笔记（Research 阶段处理）\\n1. CED 重框定为 anti-reward-overoptimization mechanism\\n2. EDCR 升格为独立评估贡献\\n3. ~~NLI lexical overlap bias~~ → MVP-1 已验证 (r=0.34)\\n4.
…[truncated 1662 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c10d8c34544498f36f499ff2bc6355a5:briefer",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 576
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T06:32:45.869852+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "memory.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c10d8c34544498f36f499ff2bc6355a5:briefer",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "faith-evidence-ie",
    "file": "memory.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T06:32:46.223034+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/memory.md\", \"content\": \"# 文献调研：GRPO/RLHF 训练中的\\\"先遗忘后恢复\\\"现象\\n\\n日期：2026-05-14\\n\\n## 背景\\n\\nQwen3-4B + GRPO + QLoRA 4-bit 训练文档级关系抽取，观察到：\\n- Reward 上升但 eval rel_F1 崩塌（ckpt-20: 0.0077 vs SFT baseline 0.406）\\n- lr=5e-5 和 lr=5e-6 下都出现\\n- 存在\\\"先遗忘后缓慢恢复\\\"的 U 型曲线（step-10=0.003 → step-90=0.211），但恢复不足\\n\\n---\\n\\n## 论文 1：Mitigating the Alignment Tax of RLHF\\n\\n- **作者**：Yifei Lin, Yuxin Tan, et al.\\n- **年份/Venue**：2024, EMNLP 2024\\n- **arXiv**：2309.06256\\n\\n### 核心发现\\n- 定义了\\\"alignment tax\\\"：RLHF 对齐后模型遗忘预训练/SFT 阶段习得能力的现象\\n- 发现简单的**模型参数平均**（插值 SFT 和 RLHF 后模型权重）在 alignment-forgetting Pareto 前沿上表现最优\\n- 提出 **Heterogeneous Model Averaging (HMA)**：对不同层使用不同插值比例，最大化对齐收益同时最小化遗忘\\n\\n### 与我们场景的相关性\\n- **直接相关**。我们的 rel_F1 崩塌就是 alignment tax 的典型表现——GRPO 优化 reward 的过程中覆盖了 SFT 学到的抽取能力\\n- HMA 的层级插值思路可直接应用于 QLoRA adapter 权重\\n\\n### 推荐缓解方案\\n- 训练后对 SFT checkpoint 和 GRPO checkpoint 做权重插值（α=0.3~0.7）\\n- 或用 HMA 对不同 LoRA 层设置不同插值系数\\n\\n---\\n\\n## 论文 2：Online Merging Optimizers for Boosting Rewards and Mitigating Tax in Alignment\\n\\n- **作者**：Lu et al. (Qwen 团队)\\n- **年份/Venue**：2024, arXiv 2405.17931\\n- **开源**：github.com/QwenLM/online_merging_optimizers\\n\\n### 核心发现\\n- 在 RLHF 每个优化步骤中实时合并 RL policy 和 SFT 模型参数，持续调节训练方向\\n- 将梯度与 SFT-pretrained 参数差合并，引导梯度朝着\\\"在 SFT 优化方向上最大化 reward\\\"的方向前进\\n- 在 Qwen 和 LLaMA 系列（1.8B-8B）、DPO/KTO 等多种 RLHF 算法上验证有效\\n- 14 个 benchmark 上同时提升对齐 reward 并降低 alignment tax\\n\\n### 与我们场景的相关性\\n- **高度相关**。该方法正是为解决我们观察到的问题设计的——reward 上升但能力退化\\n- 来自 Qwen 团队，与我们使用的 Qwen3-4B 模型同源，兼容性好\\n- 在训练过程中在线缓解，而非事后补救\\n\\n### 推荐缓解方案\\n- 在 GRPO 训练中集成 Online Merging Optimizer，每步将 LoRA 更新方向锚定在 SFT 附近\\n\\n---\\n\\n## 论文 3：Robust Policy Optimization to Prevent Catastrophic Forgetting (FRPO)\\n\\n- **作者**：Sabbaghi, Hassani, Javanmard et al.\\n- **年份/Venue**：2025, arXiv 2602.08813\\n\\n### 核心发现\\n- 指出即使小幅下游更新也会破坏 RLHF 学到的行为（如安全性），暴露 cata
…[truncated 12698 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c10d8c34544498f36f499ff2bc6355a5:briefer",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 353
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T06:32:47.281701+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "ideas.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c10d8c34544498f36f499ff2bc6355a5:briefer",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "faith-evidence-ie",
    "file": "ideas.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T06:32:47.334598+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ideas.md\", \"content\": \"# Idea Inbox\\n\\n## 待验证\\n\\n- [2026-05-14] **GRPO 遗忘缓解方案 A**：增大 KL 系数（0.001→0.04）+ 扩大 LoRA rank（r=4→r=16）+ 降低 lr 至 1e-6。文献调研表明 GRPO+QLoRA 低秩+低KL 是已知不稳定组合，这是最低成本的修复。\\n- [2026-05-14] **GRPO 遗忘缓解方案 B**：分层 Reward 设计——将单一 reward 分解为 format_reward + entity_reward + relation_reward，消除 reward hacking 捷径。参考 RL-Struct (arXiv 2512.00319) 的层级约束方法。\\n- [2026-05-14] **GRPO 遗忘缓解方案 C**：集成 Qwen 团队的 Online Merging Optimizer (arXiv 2405.17931)，在 GRPO 每步将 LoRA 更新方向锚定在 SFT 附近，训练中在线缓解 alignment tax。\\n## ACTIVE\\n\", \"total_chars\": 484, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c10d8c34544498f36f499ff2bc6355a5:briefer",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 52
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T06:32:47.737025+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "decisions.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c10d8c34544498f36f499ff2bc6355a5:briefer",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "faith-evidence-ie",
    "file": "decisions.yaml",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-15T06:32:47.738729+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/decisions.yaml\", \"content\": \"_next_id: 37\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 04:21 UTC\\n  summary: MVP 设计：两阶段验证——MVP-1 CED 信号验证（离线）→ MVP-2 端到端训练验证\\n  rationale: CED 是核心创新，必须先验证 DeBERTa NLI 能在 DocRED 上区分金标证据与实体共现干扰句（MVP-1），再投入 GPU\\n    跑完整训练流水线（MVP-2）。MVP-1 失败则 idea 需 pivot，避免浪费 GPU。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 05:46 UTC\\n  summary: 'MVP-1 PASS: CED 信号验证通过，核心假设成立（margin 0.48, accuracy 81.5%, Pearson r 0.34）'\\n  rationale: CED margin 4.8× 超过阈值，DeBERTa 判别力主要来自语义蕴含而非词汇重叠（r=0.34 远低于 0.7）。三个需关注项：33.4%\\n    gold p_pos < τ=0.5（τ 可能需调低）、44.4% 无 hard negatives（退化为 flat NLI）、少数负 margin 样本（标注噪声）。这些不影响\\n    MVP 结论但影响 Research 阶段 CED 调参。\\n  related_experiments:\\n  - exp_id: mvp1_ced_signal\\n    role: primary\\n    result: PASS — mean_margin=0.4827, accuracy=81.5%, pearson_r=0.3406\\n  depends_on: []\\n- id: D003\\n  date: 2026-05-14 06:02 UTC\\n  summary: 'Smoke test 功能性 PASS: ZeRO-2 + QLoRA 兼容，4.9GB/卡，授权启动 MVP-2 SFT'\\n  rationale: Smoke test 自报 FAIL 是假阴性——synthetic data format-only reward 产生零 variance，数学上无梯度是正常行为。关键目标全部达成：ZeRO-2+QLoRA+GRPOTrainer\\n    兼容、显存充裕（4.9/32GB）、有 reward variance 时梯度正常。Reviewer 独立确认功能性 PASS。\\n  related_experiments:\\n  - exp_id: smoke_test_grpo\\n    role: infrastructure\\n    result: 功能性 PASS (ZeRO-2+QLoRA, 4×5090, 4.9GB/卡)\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 07:26 UTC\\n  summary: 发现 rtx5090-4x 和 gpu-5090-4x-1 为同一台机器（4 GPU），GRPO 三路对比改为串行\\n  rationale: Reviewer 核实两个 SSH endpoint 返回相同 hostname 和 PID。实际资源 = 4× RTX 5090 32GB，非\\n    8 张。串行 3 路 GRPO 预估 ~7-10h（每路 ~2-3h），今天内可完成 MVP-2，暂不需要额外申请 GPU。\\n  related_experiments: []\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-14 10:03 UTC\\n  summary: CED r1 训练 step 40 后 mode collapse，启动早停+checkpoint 抢救+cliprange 排查\\n  rationale: Reviewer 审查发现 step 40 后所有指标退化（total_rewar
…[truncated 24936 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c10d8c34544498f36f499ff2bc6355a5:briefer",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T06:32:47.839771+00:00_

called mcp__agent-ml-research__load_project_config

<details open><summary>🔧 Tool call — mcp__agent-ml-research__load_project_config</summary>

```json
{
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_c10d8c34544498f36f499ff2bc6355a5:briefer",
  "tool": "mcp__agent-ml-research__load_project_config",
  "tool_args": {
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T06:32:48.382537+00:00_

Error executing tool load_project_config: 1 validation error for load_project_configArguments
project_name
  Field required [type=missing, input_value={'project': 'faith-evidence-ie'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/missing

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_c10d8c34544498f36f499ff2bc6355a5:briefer",
  "tool": "mcp__agent-ml-research__load_project_config",
  "elapsed_ms": 542
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-15T06:34:15.039989+00:00_

信息读完了，下面给你完整讲解。

---

## 一、研究背景与 Motivation

### 任务：文档级关系抽取 (Document-level Relation Extraction, DocRE)

传统的关系抽取处理单个句子，但真实世界中很多关系横跨多个句子。DocRE 要求模型阅读一整篇文档（通常几十个句子），抽取出实体之间的关系三元组 `(head, relation, tail)`，**并且指出支持该关系的证据句子**。

### 核心痛点：证据不可信

现有模型在抽取关系方面表现尚可，但在选择证据句子时存在严重问题——它们倾向于**"spray-and-pray"**（广撒网），大量引用与目标实体共现但实际不支持该关系的**干扰句 (distractor sentences)**。

举例：文档里有 10 个句子提到了实体 A 和实体 B，但只有第 3、7 句真正说明了它们之间的关系。现有模型会把 10 个句子全列上去——虽然证据召回率很高（漏的少），但**精度很差**，里面混入了大量噪声。这种"忠实性"问题使得模型的输出无法被用户信任和验证。

### 为什么现有方法解决不了

- **SFT (Supervised Fine-Tuning)**：模型学会了格式和大致模式，但没有显式信号教它区分"真正支持关系的句子"和"仅仅提到相同实体的干扰句"
- **现有评估指标**：标准的 Evi-F1 只看证据句子是否覆盖了标注，不惩罚引用干扰句

---

## 二、核心 Idea：FREIGE + CED Reward

### FREIGE 是什么

**FREIGE** = Faithful Relation Extraction with Interpretable Grounded Evidence。核心主张：用**强化学习 (RL)** 训练 LLM，让模型在做关系抽取的同时生成**可验证的、忠实的证据**。

### CED 是什么

**CED (Contrastive Evidence Discrimination)** 是本项目提出的核心奖励机制。原理：

1. 对模型预测的每个三元组 `(h, r, t)`，取出模型引用的证据句子
2. 用 NLI 模型（DeBERTa）判断：这些证据句子是否**语义蕴含**了该三元组的语言化表述
3. **对比**：同时对"正确证据"和"干扰句"做 NLI 打分，计算两者的**margin**
4. 如果 margin 大（正确证据的 NLI 分远高于干扰句），说明模型选对了；如果 margin 小或为负，说明模型在乱引用

CED 的关键设计点在于**"对比"**——不是简单看证据本身好不好，而是看模型能否**区分**真正的证据和干扰句。这比 flat NLI（只看绝对 NLI 分数）更强，因为它直接瞄准了 distractor 问题。

### 为什么用 RL 而不是直接 SFT

SFT 只能模仿标注数据中的证据选择模式，但标注本身可能不完美，且模型无法从"错误选择"中学到教训。RL 通过 reward 信号让模型**自己探索**——生成多种输出，CED 打分告诉它哪种更好，模型从中学习。

### 新提出的评估指标：EDCR

项目还提出了 **EDCR (Evidence Distractor Citation Rate)**——衡量模型引用干扰句的比例。SFT baseline 的 EDCR 高达 71.18%，说明超过七成的被引证据实际上是干扰句。这正是 CED 要攻击的靶点。

---

## 三、实验进展

### MVP-1：CED 信号验证（离线，已通过 ✅）

在 DocRED dev 集上用 DeBERTa-v3-base 计算 CED 分数，验证 NLI 模型能否区分金标证据和干扰句：

| 指标 | 结果 | 阈值 |
|------|------|------|
| Mean CED margin | **0.4827** | 需 > 0 |
| 判别准确率 | **81.5%** | 需显著 > 50% |
| Margin 与词汇重叠的 Pearson r | **0.34** | 需 < 0.7（排除 NLI 只看字面重叠） |

**结论**：CED 信号有效，NLI 判别力主要来自语义蕴含而非词汇重叠。核心假设成立。

注意事项：33.4% 的金标样本 NLI 分低于阈值 τ=0.5（可能需调参），44.4% 的样本没有 hard negative（退化为 flat NLI），少数样本出现负 margin（标注噪声）。

### MVP-2：端到端训练验证（经历了大量迭代）

#### 阶段 A：SFT Warmup（已完成 ✅）

用 Qwen3-4B + QLoRA 4-bit 在 DocRED 上做 SFT，作为后续 RL 的起点：
- Eval loss 0.72, token accuracy 83.5%
- Baseline 指标：**rel_F1 = 40.57%, Evi-F1 = 79.79%, EDCR = 71.18%**

#### 阶段 B：GRPO 在线 RL（全线失败 ❌）

这是项目迄今最大的挫折和最重要的发现。做了 **30+ 个实验**，在多种配置下尝试用 GRPO 在线 RL 训练，全部失败。关键历程：

**第一轮（r1-r2）**：发现 mode collapse——模型在训练 40 步后 F1 归零，只学会生成格式正确但内容随机的输出。根因：无 checkpoint 保存、reward 权重失衡（format reward 远大于 F1 reward）、clip ratio 未生效。

**第二轮（r3-r5, kl_coef 调参）**：发现 QLoRA 4-bit 与 kl_coef > 0 不兼容——量化噪声导致 ref model 和 training model 的 log-probs 有系统性偏差，KL 从第一步就是天文数字（10^10 量级），训练直接爆炸。最终确定 kl_coef 必须为 0 或极小值 (0.01)。

**三路 ablation 对比（D020 配置，kl=0.01）**：
| Reward 类型 | 结果 | 存活步数 |
|---|---|---|
| CED (对比证据判别) | **存活 100 步** ✅ | 100 |
| Extract-only (仅抽取 F1) | Mode collapse ❌ | ~30 |
| Flat-NLI (非对比 NLI) | Mode collapse ❌ | ~25 |

**核心发现**：只有 CED reward 能维持 GRPO 训练不崩溃。这比预想的更强——CED 不仅改善证据质量，还是 GRPO 训练本身能否存活的关键。Extract-only 和 flat-NLI 都因为 reward signal 太稀疏导致 mode collapse。

**但即使 CED 训练存活，eval 仍然失败**：

| lr | 最佳 rel_F1 | SFT baseline | 差距 |
|---|---|---|---|
| 5e-5 | 0.217 (step 90) | 0.4057 | -46% |
| 5e-6 | 0.0138 (ckpt 100) | 0.4057 | -97% |

**灾难性遗忘**：GRPO 优化 reward 的过程中，不可逆地破坏了 SFT 学到的关系抽取能力。但有趣的是，**evi_f1 从 0.628 单调上升到 0.850**（超过 SFT baseline 的 0.798），说明 CED 确实教会了模型更好的证据选择，只是关系抽取能力被摧毁了。

**根因诊断**：不是超参问题，是 GRPO + QLoRA 在结构化生成任务上的根本性局限。QLoRA 低秩空间无法同时维持 SFT 能力和 RL 优化目标，在线 RL 的策略偏移在前 20 步即不可逆地破坏关系抽取能力。

#### 阶段 C：Pivot 到 RSFT 离线 RL（进行中 🏃）

鉴于在线 RL 全线失败，项目 pivot 到 **Rejection Sampling Fine-Tuning (RSFT)**：

1. **生成候选**：用 SFT 模型对每个训练样本生成 N=8 个候选输出（temperature=0.7）
2. **CED 打分筛选**：用 CED reward 对候选打分，筛选最优样本
3. **SFT 训练**：在筛选后的高质量数据上做 SFT

优势：完全避免在线 RL 的策略偏移问题，CED 只作为离线打分器使用。

**当前状态**（截至 2026-05-15）：4 卡并行生成候选中，已完成约 87.7%（~2369/2701 docs），diversity 7.52/8 (median=8.0)，format 正确率 99.6-100%。预计还有 3 小时后完成，之后进入 CED 打分筛选和 RSFT 训练阶段。

中间还出现了一个 diversity 监控 bug（报告 1.0/8，实际 7.11/8），已定位为度量代码归一化逻辑错误并修复。

---

## 四、关键发现总结

1. **CED signal 有效**（MVP-1 verified）：NLI 能区分金标证据和干扰句，margin = 0.48, accuracy = 81.5%
2. **CED 是 GRPO 存活的必要条件**：三路 ablation 中只有 CED 维持训练稳定，extract-only 和 flat-NLI 均 collapse。CED 的对比性 evidence discrimination 提供了更丰富的梯度信号
3. **但在线 RL (GRPO+QLoRA) 导致不可逆的灾难性遗忘**：evi_f1 ↑ 同时 rel_f1 ↓↓↓，证明 CED 教会了证据选择但 RL 摧毁了抽取能力
4. **QLoRA 4-bit 与 KL 惩罚不兼容**：量化噪声导致 KL 计算失真，kl_coef > 0.01 即触发 KL 爆炸
5. **EDCR 71.18%** 证实 SFT 模型严重依赖干扰句，CED 有明确攻击面
6. **离线 RL (RSFT) 是可行路径**：避免策略偏移，CED 作为打分器仍可发挥作用

---

## 五、当前状态与下一步

- **正在做**：RSFT 候选生成（4 卡并行，接近完成）
- **接下来**：合并 4 个 shard → CED 打分筛选 → RSFT 训练 → Eval
- **后备方案**：如果 RSFT 效果不好，考虑 DPO + CED scoring、prompt-level 多样性、CED 作为推理时 reranker
- **论文方向**：CED 可重框定为 "anti-reward-overoptimization mechanism"，GRPO 的负面结果本身有论文价值（证明在线 RL 在结构化生成任务上的局限性）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_c10d8c34544498f36f499ff2bc6355a5:briefer"
}
```

</details>

---
