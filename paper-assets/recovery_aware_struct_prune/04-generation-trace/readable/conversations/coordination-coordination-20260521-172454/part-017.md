# Project coordination (archived snapshot) — Part 17 of 17

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Conversation logs

[← Part 16](part-016.md) · [Transcript overview](../coordination-coordination-20260521-172454.md) · [Structured JSON](../../../sessions/96/9695be0a51d6cda07fb1.json)

## Round 885

### Tool call

_source line 10441 · 2026-05-21T16:12:02.511316+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/structure_overlap_cka_vs_standard_20.md",
  "content": "# CKA-only 20% vs Standard 20% Structural Overlap Analysis\n\n## Model & Pruning Parameters\n- Base model: DeepSeek-R1-Distill-Qwen-7B (28 layers)\n- Original MLP intermediate_size: 18944, group_size: 676, groups/layer: 28, total MLP groups: 784\n- Attention: Neither method prunes attention (num_kv_heads = 4/layer preserved)\n- Both methods remove exactly 200/784 MLP groups (20% sparsity)\n\n## Per-Layer MLP Pruning Comparison\n\n| Layer | CKA-only removed | Standard removed | CKA-only dim | Standard dim | Category |\n|-------|-----------------|-----------------|--------------|--------------|----------|\n| 0 | 16 | 16 | 8128 | 8128 | Both heavy-prune |\n| 1 | 16 | 16 | 8128 | 8128 | Both heavy-prune |\n| 2 | 16 | 16 | 8128 | 8128 | Both heavy-prune |\n| 3 | 16 | 16 | 8128 | 8128 | Both heavy-prune |\n| 4 | 16 | 16 | 8128 | 8128 | Both heavy-prune |\n| 5 | 16 | 16 | 8128 | 8128 | Both heavy-prune |\n| 6 | 16 | 0 | 8128 | 18944 | CKA-only unique |\n| 7 | 1 | 0 | 18268 | 18944 | CKA-only unique |\n| 8 | 16 | 0 | 8128 | 18944 | CKA-only unique |\n| 9 | 16 | 0 | 8128 | 18944 | CKA-only unique |\n| 10 | 0 | 0 | 18944 | 18944 | Both retain |\n| 11 | 0 | 0 | 18944 | 18944 | Both retain |\n| 12 | 0 | 0 | 18944 | 18944 | Both retain |\n| 13 | 0 | 0 | 18944 | 18944 | Both retain |\n| 14 | 0 | 0 | 18944 | 18944 | Both retain |\n| 15 | 0 | 0 | 18944 | 18944 | Both retain |\n| 16 | 0 | 7 | 18944 | 14212 | Standard unique |\n| 17 | 0 | 4 | 18944 | 16240 | Standard unique |\n| 18 | 0 | 7 | 18944 | 14212 | Standard unique |\n| 19 | 4 | 16 | 16240 | 8128 | Both prune (Standard heavier) |\n| 20 | 2 | 2 | 17592 | 17592 | Both prune (equal) |\n| 21 | 11 | 8 | 11508 | 13536 | Both prune (CKA heavier) |\n| 22 | 0 | 4 | 18944 | 16240 | Standard unique |\n| 23 | 8 | 16 | 13536 | 8128 | Both prune (Standard heavier) |\n| 24 | 14 | 16 | 9480 | 8128 | Both prune (Standard heavier) |\n| 25 | 0 | 16 | 18944 | 8128 | Standard unique |\n| 26 | 0 | 8 | 18944 | 13536 | Standard unique |\n| 27 | 16 | 0 | 8128 | 18944 | CKA-only unique |\n\n## Regional Summary\n\n| Region | Layers | CKA-only groups removed | Standard groups removed |\n|--------|--------|------------------------|------------------------|\n| Early (L0-9) | 0-9 | 145 (72.5% of budget) | 96 (48.0% of budget) |\n| Middle (L10-15) | 10-15 | 0 (0%) | 0 (0%) |\n| Late (L16-27) | 16-27 | 55 (27.5% of budget) | 104 (52.0% of budget) |\n| **Total** | 0-27 | **200** | **200** |\n\n## Unique Pruning Decisions\n\n### CKA-only uniquely prunes (Standard retains)\n- Layers 6, 7, 8, 9, 27: ~65 groups\n- Interpretation: CKA identifies these layers as having redundant representations (high inter-layer similarity), but magnitude-based importance scores them as important\n\n### Standard uniquely prunes (CKA-only retains)\n- Layers 16, 17, 18, 22, 25, 26: ~46 groups\n- Interpretation: Magnitude importance scores these late layers as unimportant, but CKA identifies them as having unique representational capacity\n\n## Jaccard Overlap Bounds\n- Pruned set Jaccard: **7.0% – 49.3%** (lower/upper bound)\n- Retained set Jaccard: **54.1% – 79.1%**\n- Note: Exact values require group-level masks (not saved during original pruning runs)\n\n## Key Insight\nCKA-only concentrates pruning budget on early layers (L0-9) that have redundant representations, preserving late-layer functional specialization critical for reasoning. Standard distributes pruning more uniformly based on magnitude, sacrificing late-layer capacity. This explains CKA-only's growing advantage at higher sparsity (25%: +9.25pp GSM8K) — late layers matter more for downstream task performance.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_2d56471446f147ebef110a443640b554",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/structure_overlap_cka_vs_standard_20.md",
    "content": "# CKA-only 20% vs Standard 20% Structural Overlap Analysis\n\n## Model & Pruning Parameters\n- Base model: DeepSeek-R1-Distill-Qwen-7B (28 layers)\n- Original MLP intermediate_size: 18944, group_size: 676, groups/layer: 28, total MLP groups: 784\n- Attention: Neither method prunes attention (num_kv_heads = 4/layer preserved)\n- Both methods remove exactly 200/784 MLP groups (20% sparsity)\n\n## Per-Layer MLP Pruning Comparison\n\n| Layer | CKA-only removed | Standard removed | CKA-only dim | Standard dim | Category |\n|-------|-----------------|-----------------|--------------|--------------|----------|\n| 0 | 16 | 16 | 8128 | 8128 | Both heavy-prune |\n| 1 | 16 | 16 | 8128 | 8128 | Both heavy-prune |\n| 2 | 16 | 16 | 8128 | 8128 | Both heavy-prune |\n| 3 | 16 | 16 | 8128 | 8128 | Both heavy-prune |\n| 4 | 16 | 16 | 8128 | 8128 | Both heavy-prune |\n| 5 | 16 | 16 | 8128 | 8128 | Both heavy-prune |\n| 6 | 16 | 0 | 8128 | 18944 | CKA-only unique |\n| 7 | 1 | 0 | 18268 | 18944 | CKA-only unique |\n| 8 | 16 | 0 | 8128 | 18944 | CKA-only unique |\n| 9 | 16 | 0 | 8128 | 18944 | CKA-only unique |\n| 10 | 0 | 0 | 18944 | 18944 | Both retain |\n| 11 | 0 | 0 | 18944 | 18944 | Both retain |\n| 12 | 0 | 0 | 18944 | 18944 | Both retain |\n| 13 | 0 | 0 | 18944 | 18944 | Both retain |\n| 14 | 0 | 0 | 18944 | 18944 | Both retain |\n| 15 | 0 | 0 | 18944 | 18944 | Both retain |\n| 16 | 0 | 7 | 18944 | 14212 | Standard unique |\n| 17 | 0 | 4 | 18944 | 16240 | Standard unique |\n| 18 | 0 | 7 | 18944 | 14212 | Standard unique |\n| 19 | 4 | 16 | 16240 | 8128 | Both prune (Standard heavier) |\n| 20 | 2 | 2 | 17592 | 17592 | Both prune (equal) |\n| 21 | 11 | 8 | 11508 | 13536 | Both prune (CKA heavier) |\n| 22 | 0 | 4 | 18944 | 16240 | Standard unique |\n| 23 | 8 | 16 | 13536 | 8128 | Both prune (Standard heavier) |\n| 24 | 14 | 16 | 9480 | 8128 | Both prune (Standard heavier) |\n| 25 | 0 | 16 | 18944 | 8128 | Standard unique |\n| 26 | 0 | 8 | 18944 | 13536 | Standard unique |\n| 27 | 16 | 0 | 8128 | 18944 | CKA-only unique |\n\n## Regional Summary\n\n| Region | Layers | CKA-only groups removed | Standard groups removed |\n|--------|--------|------------------------|------------------------|\n| Early (L0-9) | 0-9 | 145 (72.5% of budget) | 96 (48.0% of budget) |\n| Middle (L10-15) | 10-15 | 0 (0%) | 0 (0%) |\n| Late (L16-27) | 16-27 | 55 (27.5% of budget) | 104 (52.0% of budget) |\n| **Total** | 0-27 | **200** | **200** |\n\n## Unique Pruning Decisions\n\n### CKA-only uniquely prunes (Standard retains)\n- Layers 6, 7, 8, 9, 27: ~65 groups\n- Interpretation: CKA identifies these layers as having redundant representations (high inter-layer similarity), but magnitude-based importance scores them as important\n\n### Standard uniquely prunes (CKA-only retains)\n- Layers 16, 17, 18, 22, 25, 26: ~46 groups\n- Interpretation: Magnitude importance scores these late layers as unimportant, but CKA identifies them as having unique representational capacity\n\n## Jaccard Overlap Bounds\n- Pruned set Jaccard: **7.0% – 49.3%** (lower/upper bound)\n- Retained set Jaccard: **54.1% – 79.1%**\n- Note: Exact values require group-level masks (not saved during original pruning runs)\n\n## Key Insight\nCKA-only concentrates pruning budget on early layers (L0-9) that have redundant representations, preserving late-layer functional specialization critical for reasoning. Standard distributes pruning more uniformly based on magnitude, sacrificing late-layer capacity. This explains CKA-only's growing advantage at higher sparsity (25%: +9.25pp GSM8K) — late layers matter more for downstream task performance.\n"
  }
}
```

</details>

---


### Tool result

_source line 10442 · 2026-05-21T16:12:02.562194+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/structure_overlap_cka_vs_standard_20.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_2d56471446f147ebef110a443640b554",
  "tool": "Write",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 10443 · 2026-05-21T16:12:07.385875+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_2d56471446f147ebef110a443640b554",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 10444 · 2026-05-21T16:12:07.486820+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_2d56471446f147ebef110a443640b554",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 10445 · 2026-05-21T16:12:13.636643+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "structure_overlap_cka_vs_standard_20",
  "type": "data",
  "description": "Per-layer MLP pruning comparison between CKA-only 20% and Standard 20%: Jaccard overlap bounds, regional distribution, unique pruning decisions. For Q4 reviewer response and paper Table/Figure.",
  "project": "recovery_aware_struct_prune",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/structure_overlap_cka_vs_standard_20.md",
  "tags": "['overlap', 'Q4', 'rebuttal', 'pruning-mask', 'cka-only', 'standard']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_2d56471446f147ebef110a443640b554",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "structure_overlap_cka_vs_standard_20",
    "type": "data",
    "description": "Per-layer MLP pruning comparison between CKA-only 20% and Standard 20%: Jaccard overlap bounds, regional distribution, unique pruning decisions. For Q4 reviewer response and paper Table/Figure.",
    "project": "recovery_aware_struct_prune",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/structure_overlap_cka_vs_standard_20.md",
    "tags": "['overlap', 'Q4', 'rebuttal', 'pruning-mask', 'cka-only', 'standard']"
  }
}
```

</details>

---


### Tool result

_source line 10446 · 2026-05-21T16:12:13.788016+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_bc2152\", \"name\": \"structure_overlap_cka_vs_standard_20\", \"type\": \"data\", \"description\": \"Per-layer MLP pruning comparison between CKA-only 20% and Standard 20%: Jaccard overlap bounds, regional distribution, unique pruning decisions. For Q4 reviewer response and paper Table/Figure.\", \"path\": \"projects/recovery_aware_struct_prune/artifacts/_project/data/structure_overlap_cka_vs_standard_20.md\", \"url\": null, \"project\": \"recovery_aware_struct_prune\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-21T16:12:13.635935+00:00\", \"tags\": [\"overlap\", \"Q4\", \"rebuttal\", \"pruning-mask\", \"cka-only\", \"standard\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_2d56471446f147ebef110a443640b554",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 10447 · 2026-05-21T16:12:24.572533+00:00_

called mcp__agent-ml-research__main_agent_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__main_agent_post_to_director</summary>

```json
{
  "text": "[资源] GPU 6/6 | Worker 0 | 全部满载\n\n## Q4 Overlap 分析数据已整理\n\nArtifact `structure_overlap_cka_vs_standard_20` (art_20260521_bc2152) 已注册，包含：\n- 28 层 per-layer MLP 剪枝对比表（CKA-only removed / Standard removed / 维度 / 分类）\n- Regional summary 表（Early/Middle/Late 占比）\n- Unique pruning decisions 列表\n- Jaccard bounds + key insight\n\nPaper Agent 可直接从 artifact 读取数据写入论文。\n\n## α=4.0 启动计划\n\n模型路径确认 DeepSeek-R1-Distill-Qwen-7B。脚本就绪 `westd:/root/recovery_aware_struct_prune/scripts/run_alpha4_pipeline.sh`。\n\n预计 westd cuda:2 (sft_cka_only_25_v2, 56% done) 最先完成（~1-1.5h）。一释放即在该卡启动，`bash scripts/run_alpha4_pipeline.sh 2`。总时长 ~4h。",
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_2d56471446f147ebef110a443640b554",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "tool_args": {
    "text": "[资源] GPU 6/6 | Worker 0 | 全部满载\n\n## Q4 Overlap 分析数据已整理\n\nArtifact `structure_overlap_cka_vs_standard_20` (art_20260521_bc2152) 已注册，包含：\n- 28 层 per-layer MLP 剪枝对比表（CKA-only removed / Standard removed / 维度 / 分类）\n- Regional summary 表（Early/Middle/Late 占比）\n- Unique pruning decisions 列表\n- Jaccard bounds + key insight\n\nPaper Agent 可直接从 artifact 读取数据写入论文。\n\n## α=4.0 启动计划\n\n模型路径确认 DeepSeek-R1-Distill-Qwen-7B。脚本就绪 `westd:/root/recovery_aware_struct_prune/scripts/run_alpha4_pipeline.sh`。\n\n预计 westd cuda:2 (sft_cka_only_25_v2, 56% done) 最先完成（~1-1.5h）。一释放即在该卡启动，`bash scripts/run_alpha4_pipeline.sh 2`。总时长 ~4h。",
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---


### Tool result

_source line 10448 · 2026-05-21T16:12:28.190387+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_04e6cf8fe41be27a49d5657e80962f12:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_2d56471446f147ebef110a443640b554",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "elapsed_ms": 3617
}
```

</details>

---


### Assistant

_source line 10449 · 2026-05-21T16:12:30.376650+00:00_

Artifact 已注册。向 Director 确认。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_2d56471446f147ebef110a443640b554"
}
```

</details>

---


## Round 886

## Round 886

2 recorded events


### User

_source line 10450 · 2026-05-21T17:24:01.336377+00:00_

[WRITE HANDOFF] 请立即写你的 handoff。

**格式硬约束**:
- 整条回复**只能**是 &lt;handoff>...&lt;/handoff> 标签包裹
- 禁止在标签外写任何寒暄 / 说明 / 确认（"好的"/"我开始写"/"写完了"等）

**必须覆盖以下 5 个 section（缺一不可，无内容写 N/A）**:

### 1. 🔴 硬约束 / 红线
  本项目特定的不可违反约束（GPU 设备号、服务器名、账号、路径限制等）。
  写本项目特定的，不要抄 CLAUDE.md 通用 L1 红线。
  下一个"你"第一眼看到的就是这里，写错了会被 Director CRITICAL。

### 2. 🖥️ 基础设施快照
  - 服务器名 + 工作目录 + Python 路径 + conda env
  - 模型路径 / 数据集路径 / wandb config / HF cache
  - 活跃进程：PID + tmux session + cron 任务 ID
  写一次就稳定，下一个"你"不用再 SSH 探查。

### 3. 📊 当前状态
  - 你刚做完什么 / 正在做什么
  - registry 里 RUNNING/PREPARING 的实验列表 + 一句话摘要
  - 等待中的 Worker 回调 / Cron / Director 决策

### 4. 📋 待办（条件触发式）
  格式 "条件 X 满足 → 动作 Y"。例如:
  - "Falcon-H1R 下载完成 → sed 修 MODEL_PATH → dry-run → 提交"
  - "pilot_011 出 GC4 结果 → ≥2pp 转架构 narrative，<2pp 写 null-result"

### 5. 🎯 战略上下文
  - 项目核心结论 / 决策链（D001..）
  - 下一个"你"最容易判断错的事 / 容易踩的坑

**写作原则**：
- 第 1 节必须是项目特定的（不是通用 L1 红线）
- 第 2 节让下一轮 BOOT 后能立即开工，避免重新 SSH 探查
- 简洁 > 完整：每节 5-10 行足够，长 handoff 不等于好 handoff

示例格式:
&lt;handoff>
### 1. 🔴 硬约束 / 红线
- 本项目只能用 cuda:4 / cuda:5（之前两次违规 cuda:0 被 Director CRITICAL）
- submit_training_job 不支持 shell builtin（source/conda activate 全不行）

### 2. 🖥️ 基础设施快照
- 服务器：westd-8x6000，工作目录 /root/autodl-tmp/hybrid_reasoning_phases
- Python：/root/miniconda3/bin/python（绝对路径，不走 conda activate）
- 模型：/root/autodl-tmp/qwen35_4b_direct
- 活跃：pilot_011 (PID 203221, tmux=pilot_011, cuda:4)

### 3. 📊 当前状态
我刚完成 pilot_010 分析，正在等 pilot_011 (Falcon-H1R) CoT 生成完成（6/50）。
registry: pilot_011 RUNNING；其他全 DONE。

### 4. 📋 待办
- pilot_011 cron 回调 → spawn worker 跑 probe + GC4 计算
- GC4 ≥2pp → 转架构 narrative；<2pp → null-result paper outline 已就绪

### 5. 🎯 战略上下文
Falcon-H1R 是最后一个数据点。已知 4B/9B GC4 都 FAIL。
易错：不要把 GC4-par (Falcon parallel) 和 GC4-seq (Qwen sequential) 直接对比。
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_2d56471446f147ebef110a443640b554",
  "source": "system:ralph_loop"
}
```

</details>

---


### Assistant

_source line 10451 · 2026-05-21T17:24:54.151730+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-29022 cuda:0/1/2/3, westb-23072 cuda:0/1。超出范围必须 push back Director
- CUDA_VISIBLE_DEVICES 禁止在 command 中设置，框架从 registry GPU 字段自动注入
- eval_math500.py 参数是 `--output_path`（非 --output_dir），没有 `--n_samples` 和 `--temperature`
- MATH-500 eval 全部必须 `--max_new_tokens 2048`（D097 决策：@4096 数据不可用）
- submit_training_job 的 command 必须 `bash -c` 包裹，模型路径用绝对路径
- output_dir 必须在 `/root/autodl-tmp/` 数据盘，不能用相对路径（根分区只 30GB）
- 基础模型是 DeepSeek-R1-Distill-Qwen-7B（不是 Qwen2.5-7B-Instruct），所有实验包括 alpha ablation 都用这个

### 2. 🖥️ 基础设施快照
- **westd-29022**: 4×GPU, `/root/recovery_aware_struct_prune/`（代码）, `/root/autodl-tmp/recovery_aware_struct_prune/`（模型+数据）
- **westb-23072**: 2×GPU, 同上路径结构
- Python: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`（conda 环境，非 venv）
- 基础模型: `/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B`
- 日志目录: `/root/runs/recovery_aware_struct_prune/`
- α=4.0 pipeline 脚本: `westd:/root/recovery_aware_struct_prune/scripts/run_alpha4_pipeline.sh`
- 活跃进程:
  - westd cuda:0: eval_math500_grpo_cka_only_25_v2 (PID 379999, ~49%, ~2h remaining)
  - westd cuda:1: eval_math500_grpo_random_20_v2 (PID 382470, ~15%, ~9h)
  - westd cuda:2: eval_math500_sft_cka_only_25_v2 (PID 380074, ~56%, ~1.5h) ← 最先完成
  - westd cuda:3: eval_math500_sft_random_20 (PID 385685, ~8%, ~9h)
  - westb cuda:0: eval_math500_grpo_standard_25_v2 (PID 99426, ~21%, ~6.5h)
  - westb cuda:1: eval_math500_sft_standard_25_v2 (PID 104592, ~2%, ~9h)
- 5 个 cron 活跃（eval_math500_grpo_cka_only_25_v2, eval_math500_sft_cka_only_25_v2, eval_math500_grpo_random_20_v2, eval_math500_grpo_standard_25_v2）。eval_math500_sft_random_20 和 eval_math500_sft_standard_25_v2 的 cron 需确认是否已注册

### 3. 📊 当前状态
刚完成：
- eval_gsm8k_sft_standard_25 收割完毕（50.87%, 671/1319），registry DONE/success
- 完整 cross-sparsity GSM8K 表已汇报 Director（15%/20%/25% × 4 methods）
- Q4 结构重叠分析完成，artifact 已注册 (art_20260521_bc2152)
- α=4.0 pipeline 脚本已写好，等 GPU 释放

Registry RUNNING: 6 个 MATH-500 @2048 eval（见上方进程列表）
Registry PREPARING: eval_math500_sft_random_20 已转 RUNNING

无活跃 Worker。等 cron 回调。

### 4. 📋 待办（条件触发式）
- westd cuda:2 (sft_cka_only_25_v2) cron 回调完成 → harvest metrics + complete_experiment + **立即在 cuda:2 启动 α=4.0 pipeline** (`bash scripts/run_alpha4_pipeline.sh 2`)，注册为新实验 (prune→SFT→GRPO→eval 共 ~4h)
- westd cuda:0 (grpo_cka_only_25_v2) cron 回调完成 → harvest + complete_experiment，释放的 GPU 待 Director 分配
- 任何 MATH-500 eval 完成 → harvest accuracy/stderr/truncation_rate + update_registry DONE + 报 Director
- 全部 25% MATH-500 数据到手 (CKA-only SFT/GRPO + Standard SFT/GRPO) → 汇总完整 25% cross-method MATH-500 表报 Director，他会派 Paper Agent patch
- α=4.0 GRPO 完成 → 报告 reward trajectory + GSM8K accuracy，回答 reviewer "RASP collapse 是否仅是超参问题"
- Dense baseline 澄清待 Director 确认：paper 中用 90.83%（原始模型）还是 81.27%（Dense+SFT）

### 5. 🎯 战略上下文
- **DDL: EMNLP 2026 ARR, 还剩 ~3 天 (May 25)**
- Round 5 审稿评分 3.0，正在做 rebuttal 所需的补充实验
- 核心结论：CKA-only 在所有 sparsity 上持续优于 Standard，25% 差距最大（GSM8K +9.25pp SFT, +7.73pp GRPO）
- GRPO recovery delta 总体很小（-0.93 ~ +0.99 pp），不是 magic bullet
- D097 决策：所有 MATH-500 eval 必须 @2048（之前误用 @4096 的数据全部作废重跑）
- 已有 MATH-500 @2048 20% 数据：CKA-only SFT 29.0%/GRPO 29.2%, Standard SFT 25.8%/GRPO 26.4%, RASP SFT 22.6%/GRPO 24.0%。缺 25% 和 Random 20%
- 25% Standard SFT MATH-500 v1 = 13.0%（已采用，v2 在 westb cuda:1 重跑中）
- 易错点：eval_math500_sft_standard_25 的 v1 结果（13.0%）已被 Director 采用并写入 registry，westb cuda:1 上跑的是 v2 重跑验证。不要覆盖 v1 数据
- 易错点：Random 20% SFT 模型只在 westd 上，westb 没有。SCP 太慢不值得
- α=4.0 实验目的：Table 6 显示 α=4.0 post-prune accuracy 最高（40%），reviewer 质疑 RASP collapse 可能仅是超参问题。如果 α=4.0 GRPO 也 collapse → 证明不是超参问题；如果改善 → 需要更新 narrative
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_2d56471446f147ebef110a443640b554"
}
```

</details>

---
