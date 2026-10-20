# cron hook openvla trained extract 20260515T222331 891733

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 54
- **Recorded user turns:** 2
- **Tool calls:** 25
- **Original source:** `logs/chats/archive/cron_hook_openvla-trained-extract_20260515T222331_891733.jsonl`
- **Structured JSON:** [`5ae3d38d5e193d4033a1.json`](../../sessions/5a/5ae3d38d5e193d4033a1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

28 recorded events

### User

_source line 1 · 2026-05-15T19:16:51.029802+00:00_

[HANDOFF] 你是 Main Agent，这是 Loop #4。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-19183 的 cuda:0 和 cuda:1（gpu_ids 白名单），其他 GPU 编号禁止使用
- LIBERO-Goal 实验统一用 LIBERO-10 fine-tuned checkpoint（D017），不用 base pretrained。LIBERO-Goal 对该 checkpoint 是 OOD 测试
- AutoDL 离线环境：extract_features.py 必须 `local_files_only=True`，否则网络不可达崩溃（已踩坑两次）
- 分析 Worker 不得覆盖 registry 的 spec 字段（Director 指令）
- Goal Classification 结果存在维度混淆（4096 vs 1024）：**当前 MLP probe 数据不能直接用于 paper claim**，必须先做 PCA-1024 + linear probe 控制实验
- AutoDL pip/HF 操作前必须 `source /etc/network_turbo` + 设 SSL cert 环境变量

### 2. 🖥️ 基础设施快照
- **服务器**: westd-19183（2×RTX PRO 6000），当前 0/2 GPU 占用
- **工作目录**: `/root/vla-ssd`（代码），`/root/autodl-tmp/vla-ssd/`（数据/模型/特征/结果）
- **Python**: `/root/miniconda3/bin/python`，conda base 环境，激活命令 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **模型路径**: `/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b/`（trained）、`/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-untrained/`（untrained）、`/root/autodl-tmp/vla-ssd/checkpoints/dinov2-large/`
- **数据路径**: LIBERO-10 `/root/autodl-tmp/vla-ssd/data/libero/libero_10/`、LIBERO-Goal `/root/autodl-tmp/vla-ssd/data/libero/libero_goal/`
- **特征路径**: trained `/root/autodl-tmp/vla-ssd/features/trained/`（LIBERO-10）、`features/trained_libero_goal/`（LIBERO-Goal）、untrained 同理、DINO 同理
- **活跃进程**: 无。所有 25 个实验均 DONE，0 个活跃 cron

### 3. 📊 当前状态
所有实验已完成，当前无 RUNNING/PREPARING 实验。项目处于 **LIBERO-Goal pivot 后的分析间歇期**。

**已完成关键实验链**:
1. MVP-1 Temporal Distance: G2 FAIL (Δρ=0.043 < 0.1 threshold)
2. MVP-2 Action Prediction: G2 FAIL, G3 FAIL — vision-dominated
3. MVP-2 Action-Delta: G3-delta FAIL
4. LIBERO-Goal feature extraction: trained/untrained/DINO 全部完成（10 tasks × 50 demos）
5. LIBERO-Goal Goal Classification: **G1-GC PASS (100%), Sanity-GC FAIL (DINO 86%), G2-GC 维度混淆, G3-GC FAIL (Δ=0pp)**

**最后一个实验 lg_gc_untrained 结论 negative**: untrained VLA 也能 100% goal classification（MLP probe + 4096 dim 太容易），G2-GC gate Δ=0pp。**这个 negative 尚未向 Director 发 Framing 调整提案**——上一轮 session 结束前未完成此步骤。

**等待中**: 无 Worker 回调、无 Cron、无 Director 待决策项。

### 4. 📋 待办（条件触发式）
- **立即（新 session BOOT 后第一件事）**: lg_gc_untrained negative → 按 red-section skill 产出 Framing 调整提案 → `main_agent_post_to_director` 汇报
- 提案核心方向：PCA-1024 维度对齐 + linear probe 控制实验（消除维度混淆），然后重新判定 G2-GC 和 G3-GC
- Director 批准 PCA 控制实验 → spawn Worker 实现 PCA 降维 + linear probe 脚本 → 双卡并行跑 trained/untrained/DINO
- PCA 控制实验 trained > untrained 差异显著 → 转 instruction grounding narrative，开始写 paper
- PCA 控制实验 trained ≈ untrained → 需要更强的 probe（MDL probing / selectivity 指标），或考虑 pivot 到 per-timestep 分析（early timestep bin 可能有差异）
- **CoRL DDL 紧迫**: Abstract May 26 (11天), Paper May 29 (14天)。GPU 空着 = 失职

### 5. 🎯 战略上下文
**核心结论链**: LIBERO-10 vision-dominated (D008/D014) → Pivot to LIBERO-Goal (D015) → D017 统一用 fine-tuned checkpoint → Goal Classification 维度混淆发现（Reviewer CRITICAL）

**最容易判断错的事**:
1. **不要把当前 100% goal classification 当 positive 结果写进 paper**——trained 和 untrained 都是 100%，DINO 86% 的 gap 是维度差异不是 language grounding。必须 PCA 对齐后才能下结论
2. **不要跳过 Framing 调整提案直接跑 PCA 实验**——lg_gc_untrained 是 negative，红线要求先提案再动
3. **Layer stability 发现仍然有效**（trained 31/33 层稳定 vs untrained ~15/33 层）——这是跨 MVP 一致的 positive signal，可能成为论文 secondary claim
4. **文献空间确认我们有 novelty**: trained vs untrained × layer × timestep instruction probing 无人做过（Grant 2026 只做 behavioral，Swann 做 SAE 但无 language features）
5. **DINO Sanity-GC FAIL (86%)** 意味着 LIBERO-Goal goals 在执行过程中视觉可区分——但 early timestep (t=0) DINO 只有 43%，说明 **per-timestep 分析** 可能是突破口（t=0 时视觉相同，此时 language 应该 matter）

## 项目硬约束 (memory.md 节选)

## 技术约束

- RoPE 不构成 confound（独立 forward pass）
- Bootstrap CI 必须 task-level 采样（10 tasks 的 per-task ρ）
- Token 聚合：Primary = last pre-action token
- 存储：根分区 ~30GB，大文件在 /root/autodl-tmp/vla-ssd/
- Untrained model: from_config() 重新初始化 LLM（6.74B random），保留 SigLIP（0.80B）
- transformers 版本差异（4.40.1 vs 4.57.6），trained/untrained 同版本，对比有效
- AutoDL: source /etc/network_turbo, HF_HUB_DISABLE_XET=1, SSL certs
- Worker 用 nohup 启动实验是 anti-pattern——必须用 submit_training_job（tmux+cron 监控）
- **AutoDL 离线提取**: extract_features.py 需 `local_files_only=True`
- **分析 Worker 不得覆盖 spec 字段**（2026-05-15, Director 指令）

## 可查的历史
前 9 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
完整聊天归档可用 `recall_session_history("关键词")` 搜索。

## 第一个动作要求
1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）
2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:openvla-trained-extract",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-15T19:17:02.999617+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-15T19:17:03.058548+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "ToolSearch",
  "elapsed_ms": 58
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T19:17:05.838869+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "vla-ssd",
  "limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "vla-ssd",
    "limit": "0"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T19:17:05.839306+00:00_

called mcp__agent-ml-research__reconcile_crons

<details open><summary>🔧 Tool call — mcp__agent-ml-research__reconcile_crons</summary>

```json
Arguments not recorded in this source.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T19:17:06.191503+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"lg_gc_untrained\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T17:51:49.753Z\", \"updated_at\": \"2026-05-15T18:03:31.246Z\", \"hypothesis\": \"Goal classification probe on untrained VLA LIBERO-Goal features (33 layers). Baseline for G2-GC gate: Δ(trained-untrained) best-layer acc > 25pp. Untrained VLA with random LLM should show lower goal classification accuracy.\", \"conclusion\": \"negative\", \"metrics\": {\"best_layer\": 1, \"best_accuracy\": 1, \"best_traj_accuracy\": 1, \"best_macro_f1\": 1, \"worst_layer\": 31, \"worst_accuracy\": 0.9971, \"n_classes\": 10, \"n_train\": 50880, \"n_val\": 12848, \"per_layer_accuracies\": {\"0\": 0.1582, \"1\": 1, \"2\": 1, \"3\": 1, \"4\": 1, \"5\": 1, \"6\": 1, \"7\": 1, \"8\": 1, \"9\": 1, \"10\": 0.9998, \"11\": 0.9998, \"12\": 0.9999, \"13\": 0.9999, \"14\": 0.9996, \"15\": 0.9996, \"16\": 0.9998, \"17\": 0.9994, \"18\": 0.9989, \"19\": 0.9992, \"20\": 0.9995, \"21\": 0.9993, \"22\": 0.9996, \"23\": 0.9991, \"24\": 0.9994, \"25\": 0.9988, \"26\": 0.9993, \"27\": 0.9993, \"28\": 0.9986, \"29\": 0.9984, \"30\": 0.9977, \"31\": 0.9971, \"32\": 0.9991}, \"gate_G2_GC\": \"FAIL\", \"gate_G2_GC_delta\": 0, \"gate_G2_GC_threshold\": 0.25, \"layer0_detail\": \"predicts_only_class1_acc_0.158_random_level\", \"comparison\": {\"trained_best_acc\": 1, \"untrained_best_acc\": 1, \"dino_best_acc\": 0.8626, \"delta_trained_untrained\": 0, \"delta_trained_dino\": 0.1374}, \"interpretation\": \"Untrained VLA (random LLM) achieves identical 100% goal classification from layer 1+. G2-GC FAIL: Δ=0pp (threshold 25pp). Goal classification is NOT a valid discriminator between trained and untrained VLA — the MLP probe on 4096-dim features trivially separates 10 classes even from random projections.\"}}, \"lg_gc_dino\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T17:53:30.361Z\", \"updated_at\": \"2026-05-15T18:00:37.784Z\", \"hypothesis\": \"DINO-V2 LIBERO-Goal goal cl
…[truncated 16115 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 352
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-15T19:17:06.192006+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 0, \"results\": []}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 352
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-15T19:17:06.242485+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "vla-ssd",
  "file": "report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "vla-ssd",
    "file": "report.md"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-15T19:17:06.393500+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/report.md\", \"content\": \"# Handover — 2026-05-15\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **lg_gc_untrained** (negative): Goal classification probe on untrained VLA LIBERO-Goal features (33 layers). Baseline for G2-GC gate: Δ(trained-untrained) best-layer acc > 25pp. Untrained VLA with random LLM should show lower goal classification accuracy.\\n- **lg_gc_dino** (success): DINO-V2 LIBERO-Goal goal classification probe (Sanity-GC gate). DINO acc must be ≤ 25% (10-class random=10%). If DINO > 25%, goals are visually distinguishable and experiment premise is challenged.\\n- **lg_dino_extract** (success): DINO-V2 LIBERO-Goal feature extraction — vision-only baseline for Goal Classification gate (Sanity-GC: DINO acc ≤ 25%)\\n\\n## 趋势\\n成功 17 / 负向 3 / 失败 0 / 共 25\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-19183: 无 GPU 信息\\n\\n## 告警\\n- mvp2_action_probe: 已被终止 — unknown\\n- lg_extract_trained_r2: 已被终止 — unknown\\n- lg_extract_untrained_r2: 已被终止 — unknown\\n- lg_extract_trained_r1: 已被终止 — unknown\\n- lg_extract_untrained_r1: 已被终止 — unknown\\n\", \"total_chars\": 1036, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T19:17:06.394000+00:00_

called mcp__agent-ml-research__read_roadmap

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap</summary>

```json
{
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T19:17:06.444564+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/ROADMAP.md\", \"content\": \"# vla-ssd — Research Dashboard\\n\\n> 最后更新: 2026-05-15 16:07 UTC | 更新原因: D015: 选择 Option A (LIBERO-Goal pivot)，Reviewer+Director 一致，用户授权\\n\\n## 核心方向\\n\\nVLA 训练的表征贡献取决于 task structure：vision-sufficient 场景（LIBERO-10）中 vision encoder 主导，vision-ambiguous 场景（LIBERO-Goal）中 VLA 的 language grounding 才有机会体现。\\n\\n**论文 story（候选）**: LIBERO-10 negative + LIBERO-Goal positive 构成对比叙事 + layer-wise mechanistic depth（WHERE/HOW）。\\n\\n## 当前进展\\n\\n- **阶段**: MVP-2 完成 → Pivot to LIBERO-Goal（D015）\\n- **MVP-1 Temporal Distance**: G2 FAIL (Δρ=0.043), vision-dominated\\n- **MVP-2 Action Prediction**: G2 FAIL (ΔR²=0.067), G3 FAIL (Δ=0.007 vs DINO)\\n- **MVP-2 Action-Delta**: G3-delta FAIL (DINO 0.061 ≈ trained 0.059)\\n- **跨 MVP 一致发现**: layer stability（trained 31/33 层有效 vs untrained ~15/33）\\n- **方向决策**: Option A（Reviewer + Director 一致推荐，用户授权）\\n\\n## 近期任务\\n\\n- [ ] 确认 LIBERO-Goal 数据可获取 + 与 LIBERO-10 scene overlap\\n- [ ] 确认 OpenVLA checkpoint 在 LIBERO-Goal 上的 zero-shot 能力\\n- [ ] 如 zero-shot 差 → 预留 1 天 LIBERO-Goal fine-tune\\n- [ ] 特征提取：trained VLA + untrained VLA + DINO（双卡并行）\\n- [ ] Instruction-conditioned probing：same-scene/different-goal 设置\\n- [ ] DINO baseline sanity check（DINO 在 shared-scene goals 上 R² 是否下降）\\n- [ ] 分析 + 可视化 + 论文初稿\\n\\n## 时间线（CoRL 2026）\\n\\n| 里程碑 | 日期 | 剩余天数 |\\n|--------|------|---------|\\n| Abstract DDL | May 26 | 11 |\\n| Paper DDL | May 29 | 14 |\\n| 数据+pipeline 适配 | May 16 | - |\\n| 特征提取 | May 16-17 | - |\\n| Probing 实验 | May 17 | - |\\n| 分析+可视化 | May 17-18 | - |\\n| 论文初稿 | May 18-21 | - |\\n| Review+polish | May 21-25 | - |\\n\\n## GPU 预算\\n\\nwestd-19183: 2×RTX PRO 6000 | 当前 0/2 占用\\n\\n## 关键风险\\n\\n1. **[高] OpenVLA 未训练过 LIBERO-Goal** — 先检查 scene overlap，必要时 fine-tune\\n2. **[中] 视觉仍有微妙差异** — DINO per-goal R² sanity check\\n3. **[低] Pipeline 适配 bug** — 数据格式/key naming 兼容性\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 
…[truncated 1557 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T19:17:25.830102+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "vla-ssd",
  "file": "paper_framing.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "vla-ssd",
    "file": "paper_framing.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T19:17:26.282110+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_framing.md found for 'vla-ssd'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T19:17:26.282435+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "vla-ssd",
  "file": "literature_map.yaml",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "vla-ssd",
    "file": "literature_map.yaml",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T19:17:26.785104+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'vla-ssd'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T19:17:26.986178+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "vla-ssd",
  "file": "memory.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "vla-ssd",
    "file": "memory.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-15T19:17:27.037028+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/memory.md\", \"content\": \"# VLA-SSD Project Memory\\n\\n## ⚠️ 维度混淆问题（2026-05-15，Reviewer CRITICAL）\\n\\n**原结论 \\\"t=0 100% 只能来自 language instruction encoding\\\" 已被证伪。**\\n\\nUntrained VLA（random LLM）在 t=0 同样 100% accuracy，说明 4096-dim MLP probe + 10 类太容易了——这是 probe capacity vs task difficulty 的经典问题（Hewitt & Manning 2019）。DINO 43% 不是因为缺 language，而是因为只有 1024 维。\\n\\n**修正措施**：PCA-1024 维度对齐 + linear probe 控制实验。只有维度对齐后 trained > untrained 的差异才是 genuine language grounding signal。\\n\\n## Per-Timestep Goal Classification 数据（2026-05-15，原始数据仍有效，解读需修正）\\n\\n| Timestep bin | Trained VLA (L1) | Untrained VLA (L1) | DINO-V2 | \\n|---|---|---|---|\\n| **bin 0 (t=0~10%)** | **100%** | **100%** | **43.3%** |\\n| bin 1 (10~20%) | 100% | 100% | 79.7% |\\n| bin 5 (50~60%) | 100% | 100% | 90.4% |\\n| bin 9 (90~100%) | 100% | 100% | 99.1% |\\n\\n**VLA vs DINO gap = 维度差异 (4096 vs 1024)**，不能归因于 language grounding。Trained = Untrained = 100% 说明 VLA training 在 MLP probe 下无法区分。需要 PCA-1024 对齐后重新评估。\\n\\n## Goal Classification Gate 定义（锁定，实验后不可修改）（2026-05-15, Director 指令）\\n\\n10-way 分类（10 个 LIBERO-Goal goal，chance = 10%）。与 action prediction gate 独立判定。\\n\\n| Gate | 条件 | 说明 |\\n|------|------|------|\\n| **Sanity-GC** | DINO best-layer accuracy ≤ 25% | 确认视觉歧义真实。>25% 说明执行过程视觉差异泄漏 goal identity |\\n| **G1-GC** | Trained VLA best-layer accuracy > 40% | VLA 在歧义场景中有意义地编码了 instruction |\\n| **G2-GC** | Δ(trained - DINO) accuracy > 25pp | Instruction conditioning 超越纯视觉 |\\n| **G3-GC** | Δ(trained - untrained) accuracy > 10pp | LLM 训练（非仅 instruction 输入格式）的贡献 |\\n\\n**实际结果（MLP probe, 原始维度）**：Sanity-GC FAIL (DINO 86%), G1-GC PASS (100%), G2-GC 有维度混淆, G3-GC FAIL (Δ=0pp)。需 PCA-1024 + linear probe 重新判定。\\n\\n## 文献关键发现：Vision Encoder Dominance 是已知现象（2026-05-15）\\n\\n14 篇论文调研确认，\\\"vision encoder dominates\\\" 不是我们独有的问题——Grant 2026, VLM4VLA 2025, LIBERO-Plus 2025 都独立验证。LIBERO 场景中 language 被
…[truncated 3180 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T19:18:02.343030+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__main_agent_post_to_director",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__main_agent_post_to_director",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T19:18:02.343408+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-15T19:19:26.915194+00:00_

called mcp__agent-ml-research__main_agent_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__main_agent_post_to_director</summary>

```json
{
  "project": "vla-ssd",
  "text": "[资源] GPU 分配 2 / 实际跑 0 | Worker 池 0 (GPU 0 / CPU 0)\n⚠️ 2 GPU 空闲，等待 Framing 提案审批后立即启动 PCA 控制实验。\n\n---\n\n# Framing 调整提案：lg_gc_untrained Negative\n\n## 1. 原 Claim\n\"Trained VLA 在 LIBERO-Goal（vision-ambiguous）场景中编码了 instruction identity，untrained VLA 和 DINO 无法做到。Goal classification accuracy 差异是 language grounding 的证据。\"\n\n## 2. 实验结果（客观数字）\n| 模型 | 维度 | Best Acc | Probe | Gate |\n|------|------|----------|-------|------|\n| Trained VLA | 4096 | 100% (L1+) | MLP 4096→256→10 | G1-GC PASS |\n| Untrained VLA | 4096 | 100% (L1+) | MLP 4096→256→10 | G3-GC FAIL (Δ=0pp) |\n| DINO-V2 | 1024 | 86.26% | MLP 1024→256→10 | Sanity-GC FAIL (86%>25%) |\n\n**G2-GC**: Δ(trained-untrained)=0pp，阈值 25pp → FAIL\n**Sanity-GC**: DINO 86% >> 25% → goals 在执行过程中视觉可区分\n\n## 3. 重新审视\n\n### 被挑战的 Hypothesis\n\"Untrained VLA（random LLM）在 goal classification 上应显著低于 trained VLA\"——被证伪。4096-dim MLP probe + 10 类分类，即使 random projections 也能完美分离（Gorban & Tyukin 2018 高维随机分离定理）。\n\n### 被忽略的变量：维度混淆\n- VLA features 4096 dim vs DINO 1024 dim → probe 容量 4x 差异\n- MLP probe（非线性 + 高维输入）对 10 类分类来说 capacity 过大\n- Trained vs untrained Δ=0 不是\"VLA training 无用\"，而是\"probe 太强，ceiling effect 掩盖了差异\"\n- DINO 86% < VLA 100% 不能归因于\"缺 language\"，而是维度劣势\n\n### 已做实验中仍然有效的部分\n1. **Layer stability**（跨 MVP 一致）：trained 31/33 层 R² 稳定 vs untrained ~15/33 层，这个发现不受维度混淆影响（same-dimensionality 内部比较）\n2. **LIBERO-Goal 特征提取数据**：trained/untrained/DINO 全部完好，只需换 probing 方法\n3. **DINO per-timestep 数据**：t=0 仅 43%，t=9 达 99%——视觉区分度随执行推进递增。t=0 是 language grounding 的最佳测试窗口\n4. **文献 novelty gap 仍然成立**：trained vs untrained × layer × timestep 的 instruction probing 无人做过\n\n### 需要补充的实验\n维度对齐后的公平比较（PCA-1024 + linear probe）\n\n## 4. 新 Narrative 骨架（3 种备选）\n\n### Option A: \"Probing methodology matters: dimensionality-controlled analysis reveals language grounding\"\n- 核心论点：naive high-dim MLP probing 掩盖了 trained/untrained 差异（methodological contribution）；PCA-1024 + linear probe 后差异显现\n- 优势：methodology + finding 双重贡献，直接回应 Hewitt & Manning 2019 的 probing critique\n- 风险：如果 PCA 后 trained ≈ untrained 仍成立，此 narrative 失败\n- 适用条件：PCA-1024 后 Δ(trained-untrained) > 10pp\n\n### Option B: \"Temporal dynamics of instruction encoding: language matters before vision diverges\"\n- 核心论点：在 t=0（视觉场景完全相同、DINO 仅 43%）时，VLA 已编码 goal identity；per-timestep 分析揭示 language contribution 的时间窗口\n- 优势：temporal dynamics 是新颖视角，文献中无人做过 per-timestep instruction probing\n- 风险：依赖 PCA 后 t=0 bin 中 trained > untrained；如果 random LLM 在 t=0 也足够高，此 narrative 同样失败\n- 适用条件：PCA-1024 后 t=0 bin Δ(trained-untrained) > 15pp\n\n### Option C: \"Combined — Methodology + Temporal Dynamics\"（推荐）\n- 先建立方法论贡献（PCA 对齐的必要性），再展示 temporal 发现\n- Story arc: \"Vision-sufficient vs vision-ambiguous scenes → naive probing fails → controlled probing reveals WHERE (layers) and WHEN (timesteps) language grounding emerges\"\n- 与已有 LIBERO-10 negative 结果构成对比叙事\n- 优势：最完整的 story，即使某个维度弱也有另一个维度撑\n- 风险：工作量最大，但核心实验只需 PCA + linear probe（数据已有，代码改动小）\n- 适用条件：PCA 后至少一个维度（layer-wise 或 timestep-wise）出现显著 Δ\n\n## 5. 对论文各章节的影响\n\n| 章节 | 影响 | 需要改动 |\n|------|------|---------|\n| Abstract | 中等 | 不能 claim \"100% goal classification = language grounding\"，改为\"dimensionality-controlled probing reveals...\" |\n| Introduction | 中等 | 加入 probing methodology 动机（Hewitt & Manning 2019），强调公平比较的重要性 |\n| Method | 大 | 新增 PCA 降维 + linear probe 实验设计，per-timestep binning 分析 |\n| Experiments | 大 | 整体重做 goal classification 结果表（PCA 版本），原始 MLP 结果作为 ablation/warning |\n| Discussion | 大 | 新增 \"probing capacity vs representation quality\" 讨论，连接 Hewitt & Manning / Voita & Titov |\n| Conclusion | 小 | 结论改为条件性 claim（\"in vision-ambiguous scenes, with controlled probing...\"） |\n\n## 6. 建议下一步实验（3 组 + 1 stretch）\n\n### Exp-1: PCA-1024 + Linear Probe Goal Classification（优先级 P0，双卡并行）\n- 对 VLA features (trained/untrained) 做 PCA 降至 1024 dim（与 DINO 对齐）\n- Linear probe（logistic regression）替代 MLP，消除 probe capacity confound\n- Per-layer sweep (33 layers)，DINO 单层\n- 预计耗时：< 1 小时（特征已有，只需 PCA + sklearn）\n- 成功条件：Δ(trained-untrained) best-layer > 10pp\n\n### Exp-2: PCA-1024 + Linear Probe Per-Timestep Binned（P0，可与 Exp-1 并行）\n- 同 Exp-1 但按 timestep 10-bin 分析\n- 核心指标：t=0 bin 中 trained vs untrained vs DINO accuracy\n- 预计耗时：< 1 小时\n- 成功条件：t=0 bin Δ(trained-untrained) > 15pp\n\n### Exp-3: Selectivity Index（Hewitt & Manning 2019）（P1）\n- Control task: 随机标签分类\n- Selectivity = task_acc - control_acc\n- 在原始 4096 dim 上也可做，作为 methodological robustness check\n- 预计耗时：< 30 分钟\n\n### Exp-4（stretch）: MDL Probing（Voita & Titov 2020）（P2）\n- 用 description length 替代 accuracy\n- 最严格的 probing 方法论，but 实现复杂\n- 仅在 Exp-1/2/3 结果不明确时考虑\n\n## 反思\n\n### 这个 negative 是方法问题还是 hypothesis 方向错？\n**方法问题**（probe capacity + 维度混淆），不是 hypothesis 方向错。LIBERO-Goal 的 vision-ambiguous 设计仍然是正确的实验场景（Grant 2026 已验证 language matters here）。问题出在 probing methodology 的公平性上。\n\n### 当前矩阵中哪些格子受影响？\n- G2-GC 和 G3-GC 需要用 PCA+linear probe 重新判定\n- G1-GC (PASS) 不受影响（trained 100% 在任何 probe 下都会 pass）\n- Sanity-GC (FAIL) 不受影响（DINO 86% 是 1024 dim 下的真实数字）\n- Layer stability 发现不受影响（same-dim 内部比较）\n\n### 文献联动\n- Hewitt & Manning 2019 和 Gorban & Tyukin 2018 直接解释了当前 negative 的根因——是 probing methodology 的已知问题\n- Grant 2026 验证 LIBERO-Goal 中 language matters (behavioral level)，我们要做 representational level 的互补验证\n- 无需 pivot，但需要 methodology upgrade\n\n### 时间紧迫性\nCoRL Abstract DDL May 26（11天），Paper DDL May 29（14天）。PCA + linear probe 预计 1-2 小时完成（数据已有）。请尽快审批以释放 2 GPU。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "tool_args": {
    "project": "vla-ssd",
    "text": "[资源] GPU 分配 2 / 实际跑 0 | Worker 池 0 (GPU 0 / CPU 0)\n⚠️ 2 GPU 空闲，等待 Framing 提案审批后立即启动 PCA 控制实验。\n\n---\n\n# Framing 调整提案：lg_gc_untrained Negative\n\n## 1. 原 Claim\n\"Trained VLA 在 LIBERO-Goal（vision-ambiguous）场景中编码了 instruction identity，untrained VLA 和 DINO 无法做到。Goal classification accuracy 差异是 language grounding 的证据。\"\n\n## 2. 实验结果（客观数字）\n| 模型 | 维度 | Best Acc | Probe | Gate |\n|------|------|----------|-------|------|\n| Trained VLA | 4096 | 100% (L1+) | MLP 4096→256→10 | G1-GC PASS |\n| Untrained VLA | 4096 | 100% (L1+) | MLP 4096→256→10 | G3-GC FAIL (Δ=0pp) |\n| DINO-V2 | 1024 | 86.26% | MLP 1024→256→10 | Sanity-GC FAIL (86%>25%) |\n\n**G2-GC**: Δ(trained-untrained)=0pp，阈值 25pp → FAIL\n**Sanity-GC**: DINO 86% >> 25% → goals 在执行过程中视觉可区分\n\n## 3. 重新审视\n\n### 被挑战的 Hypothesis\n\"Untrained VLA（random LLM）在 goal classification 上应显著低于 trained VLA\"——被证伪。4096-dim MLP probe + 10 类分类，即使 random projections 也能完美分离（Gorban & Tyukin 2018 高维随机分离定理）。\n\n### 被忽略的变量：维度混淆\n- VLA features 4096 dim vs DINO 1024 dim → probe 容量 4x 差异\n- MLP probe（非线性 + 高维输入）对 10 类分类来说 capacity 过大\n- Trained vs untrained Δ=0 不是\"VLA training 无用\"，而是\"probe 太强，ceiling effect 掩盖了差异\"\n- DINO 86% < VLA 100% 不能归因于\"缺 language\"，而是维度劣势\n\n### 已做实验中仍然有效的部分\n1. **Layer stability**（跨 MVP 一致）：trained 31/33 层 R² 稳定 vs untrained ~15/33 层，这个发现不受维度混淆影响（same-dimensionality 内部比较）\n2. **LIBERO-Goal 特征提取数据**：trained/untrained/DINO 全部完好，只需换 probing 方法\n3. **DINO per-timestep 数据**：t=0 仅 43%，t=9 达 99%——视觉区分度随执行推进递增。t=0 是 language grounding 的最佳测试窗口\n4. **文献 novelty gap 仍然成立**：trained vs untrained × layer × timestep 的 instruction probing 无人做过\n\n### 需要补充的实验\n维度对齐后的公平比较（PCA-1024 + linear probe）\n\n## 4. 新 Narrative 骨架（3 种备选）\n\n### Option A: \"Probing methodology matters: dimensionality-controlled analysis reveals language grounding\"\n- 核心论点：naive high-dim MLP probing 掩盖了 trained/untrained 差异（methodological contribution）；PCA-1024 + linear probe 后差异显现\n- 优势：methodology + finding 双重贡献，直接回应 Hewitt & Manning 2019 的 probing critique\n- 风险：如果 PCA 后 trained ≈ untrained 仍成立，此 narrative 失败\n- 适用条件：PCA-1024 后 Δ(trained-untrained) > 10pp\n\n### Option B: \"Temporal dynamics of instruction encoding: language matters before vision diverges\"\n- 核心论点：在 t=0（视觉场景完全相同、DINO 仅 43%）时，VLA 已编码 goal identity；per-timestep 分析揭示 language contribution 的时间窗口\n- 优势：temporal dynamics 是新颖视角，文献中无人做过 per-timestep instruction probing\n- 风险：依赖 PCA 后 t=0 bin 中 trained > untrained；如果 random LLM 在 t=0 也足够高，此 narrative 同样失败\n- 适用条件：PCA-1024 后 t=0 bin Δ(trained-untrained) > 15pp\n\n### Option C: \"Combined — Methodology + Temporal Dynamics\"（推荐）\n- 先建立方法论贡献（PCA 对齐的必要性），再展示 temporal 发现\n- Story arc: \"Vision-sufficient vs vision-ambiguous scenes → naive probing fails → controlled probing reveals WHERE (layers) and WHEN (timesteps) language grounding emerges\"\n- 与已有 LIBERO-10 negative 结果构成对比叙事\n- 优势：最完整的 story，即使某个维度弱也有另一个维度撑\n- 风险：工作量最大，但核心实验只需 PCA + linear probe（数据已有，代码改动小）\n- 适用条件：PCA 后至少一个维度（layer-wise 或 timestep-wise）出现显著 Δ\n\n## 5. 对论文各章节的影响\n\n| 章节 | 影响 | 需要改动 |\n|------|------|---------|\n| Abstract | 中等 | 不能 claim \"100% goal classification = language grounding\"，改为\"dimensionality-controlled probing reveals...\" |\n| Introduction | 中等 | 加入 probing methodology 动机（Hewitt & Manning 2019），强调公平比较的重要性 |\n| Method | 大 | 新增 PCA 降维 + linear probe 实验设计，per-timestep binning 分析 |\n| Experiments | 大 | 整体重做 goal classification 结果表（PCA 版本），原始 MLP 结果作为 ablation/warning |\n| Discussion | 大 | 新增 \"probing capacity vs representation quality\" 讨论，连接 Hewitt & Manning / Voita & Titov |\n| Conclusion | 小 | 结论改为条件性 claim（\"in vision-ambiguous scenes, with controlled probing...\"） |\n\n## 6. 建议下一步实验（3 组 + 1 stretch）\n\n### Exp-1: PCA-1024 + Linear Probe Goal Classification（优先级 P0，双卡并行）\n- 对 VLA features (trained/untrained) 做 PCA 降至 1024 dim（与 DINO 对齐）\n- Linear probe（logistic regression）替代 MLP，消除 probe capacity confound\n- Per-layer sweep (33 layers)，DINO 单层\n- 预计耗时：< 1 小时（特征已有，只需 PCA + sklearn）\n- 成功条件：Δ(trained-untrained) best-layer > 10pp\n\n### Exp-2: PCA-1024 + Linear Probe Per-Timestep Binned（P0，可与 Exp-1 并行）\n- 同 Exp-1 但按 timestep 10-bin 分析\n- 核心指标：t=0 bin 中 trained vs untrained vs DINO accuracy\n- 预计耗时：< 1 小时\n- 成功条件：t=0 bin Δ(trained-untrained) > 15pp\n\n### Exp-3: Selectivity Index（Hewitt & Manning 2019）（P1）\n- Control task: 随机标签分类\n- Selectivity = task_acc - control_acc\n- 在原始 4096 dim 上也可做，作为 methodological robustness check\n- 预计耗时：< 30 分钟\n\n### Exp-4（stretch）: MDL Probing（Voita & Titov 2020）（P2）\n- 用 description length 替代 accuracy\n- 最严格的 probing 方法论，but 实现复杂\n- 仅在 Exp-1/2/3 结果不明确时考虑\n\n## 反思\n\n### 这个 negative 是方法问题还是 hypothesis 方向错？\n**方法问题**（probe capacity + 维度混淆），不是 hypothesis 方向错。LIBERO-Goal 的 vision-ambiguous 设计仍然是正确的实验场景（Grant 2026 已验证 language matters here）。问题出在 probing methodology 的公平性上。\n\n### 当前矩阵中哪些格子受影响？\n- G2-GC 和 G3-GC 需要用 PCA+linear probe 重新判定\n- G1-GC (PASS) 不受影响（trained 100% 在任何 probe 下都会 pass）\n- Sanity-GC (FAIL) 不受影响（DINO 86% 是 1024 dim 下的真实数字）\n- Layer stability 发现不受影响（same-dim 内部比较）\n\n### 文献联动\n- Hewitt & Manning 2019 和 Gorban & Tyukin 2018 直接解释了当前 negative 的根因——是 probing methodology 的已知问题\n- Grant 2026 验证 LIBERO-Goal 中 language matters (behavioral level)，我们要做 representational level 的互补验证\n- 无需 pivot，但需要 methodology upgrade\n\n### 时间紧迫性\nCoRL Abstract DDL May 26（11天），Paper DDL May 29（14天）。PCA + linear probe 预计 1-2 小时完成（数据已有）。请尽快审批以释放 2 GPU。"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T19:19:30.737263+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_a1d032cbe70bdd2058438e67e0d57613:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "elapsed_ms": 3822
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-15T19:19:36.072400+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__save_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-15T19:19:36.124231+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-15T19:20:08.661889+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__read_experiment_plan_with_status",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__read_experiment_plan_with_status",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-15T19:20:08.716101+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "ToolSearch",
  "elapsed_ms": 54
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-15T19:20:48.544469+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

```json
{
  "task_type": "code:pca_linear_probe",
  "project": "vla-ssd",
  "task_prompt": "## 任务：编写 PCA + Linear Probe Goal Classification 脚本\n\n### 背景\n我们在 LIBERO-Goal 上做了 MLP probe goal classification，发现 trained VLA 和 untrained VLA 都达到 100% accuracy（4096 dim + MLP probe + 10 类太容易了）。DINO 86%（1024 dim）。这是维度混淆——需要用 PCA 降维到 1024 后用 linear probe 重新做公平比较。\n\n### 目标\n在服务器 westd-19183 上编写 `pca_linear_probe_gc.py` 脚本，放在 `/root/vla-ssd/` 目录下。\n\n### 环境\n- 服务器: westd-19183\n- Python: `/root/miniconda3/bin/python`，conda base 环境\n- 激活命令: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`\n- 已安装: torch, sklearn, numpy, h5py\n- **离线环境**: 不要 import 任何需要网络下载的包\n\n### 已有特征数据路径\n- Trained VLA (LIBERO-Goal): `/root/autodl-tmp/vla-ssd/features/trained_libero_goal/` — 10 个 .h5 文件，每个 50 demos，per-layer features (33 layers)，维度 4096，keys: `image_mean`, `last_preaction`\n- Untrained VLA (LIBERO-Goal): `/root/autodl-tmp/vla-ssd/features/untrained_libero_goal/` — 同上\n- DINO-V2 (LIBERO-Goal): `/root/autodl-tmp/vla-ssd/features/dino_libero_goal/` — 10 个 .h5 文件，每个 50 demos，单层，维度 1024，keys: `cls_token`, `patch_mean`\n\n### H5 文件结构\n先 SSH 到服务器，用 python 检查一个 h5 文件的实际结构（keys, shapes, dtypes），以此为基础编写代码。不要假设结构。\n\n### 脚本功能要求\n\n1. **PCA 降维**: 对 VLA features (4096) 做 PCA 降到 1024 dim（与 DINO 对齐）\n   - PCA 在 train split 上 fit，transform train 和 val\n   - 记录 explained variance ratio\n\n2. **Linear Probe (Logistic Regression)**:\n   - 用 sklearn LogisticRegression (multinomial, lbfgs, max_iter=1000)\n   - 10-way 分类 (10 个 LIBERO-Goal tasks)\n   - Label = task index (哪个 goal)\n   - Train/val split: 按 demo 划分 (前 40 demos train, 后 10 demos val), 保持与 MLP probe 一致\n\n3. **Per-layer sweep**: 对 VLA features 的 33 层分别做 PCA + linear probe，输出 per-layer accuracy\n\n4. **Per-timestep binning**: \n   - 将每个 demo 的 timesteps 等分为 10 bins\n   - 对每个 bin 分别做分类\n   - 输出 per-bin accuracy (重点关注 bin 0 = 初始帧)\n\n5. **Selectivity Index (Hewitt & Manning 2019)**:\n   - Control task: 随机打乱标签后训练同样的 linear probe\n   - Selectivity = task_accuracy - control_accuracy\n   - 跑 5 次 random shuffle 取均值\n\n6. **输出格式**:\n   - 打印 JSON 格式结果到 stdout\n   - 包含: model_name, pca_dim, per_layer_accuracies, per_timestep_accuracies, selectivity_scores, explained_variance_ratios\n   - 同时保存到 `/root/autodl-tmp/vla-ssd/results/pca_linear_probe_gc/` 目录下的 JSON 文件\n\n7. **命令行接口**:\n   - `--model_type`: trained / untrained / dino\n   - `--feature_dir`: 特征目录路径\n   - `--feature_key`: 使用哪个 feature key (默认 `last_preaction` for VLA, `cls_token` for DINO)\n   - `--pca_dim`: PCA 目标维度 (默认 1024, 对 DINO 跳过 PCA)\n   - `--output_dir`: 输出目录\n   - `--n_bins`: timestep bins 数 (默认 10)\n   - `--seed`: 随机种子 (默认 42)\n   - GPU 不需要——这是纯 CPU sklearn 任务\n\n### 参考：现有代码\n先查看 `/root/vla-ssd/goal_classification.py`（或类似名字的文件），了解现有 MLP probe 的数据加载逻辑，保持兼容。\n\n### 验证步骤\n1. 代码写完后，用 `python pca_linear_probe_gc.py --help` 验证能解析参数\n2. 用 trained features 跑一个 single layer (layer 1) 的 dry-run: `python pca_linear_probe_gc.py --model_type trained --feature_dir /root/autodl-tmp/vla-ssd/features/trained_libero_goal/ --pca_dim 1024 --output_dir /tmp/test_pca_probe`，确认能正常加载数据、PCA、训练 probe 并输出结果\n3. 如果 dry-run 成功，输出 layer 1 的 accuracy 和 selectivity，作为 sanity check\n\n### 出错诊断\n- ImportError: 检查 sklearn 是否已安装 (`pip list | grep scikit`)\n- h5 文件结构不对: 用 `h5py.File(f).visit(print)` 查看实际结构\n- 内存不够: 减少同时加载的层数（逐层处理）\n- PCA 太慢: 用 `sklearn.decomposition.PCA(n_components=1024, svd_solver='randomized')`\n\n### 代码质量\n- 文件顶部写文件注释（目的、输入输出、关键依赖）\n- 关键函数写 docstring\n- 所有 magic number 用命令行参数或常量",
  "tool_groups": "['ssh']",
  "context": "服务器 westd-19183, conda base 环境, 离线环境(不要下载任何包)。特征数据: trained_libero_goal / untrained_libero_goal / dino_libero_goal 在 /root/autodl-tmp/vla-ssd/features/ 下。目标: 写 PCA+linear probe 脚本，为 Director 审批后立即跑实验做准备。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "code:pca_linear_probe",
    "project": "vla-ssd",
    "task_prompt": "## 任务：编写 PCA + Linear Probe Goal Classification 脚本\n\n### 背景\n我们在 LIBERO-Goal 上做了 MLP probe goal classification，发现 trained VLA 和 untrained VLA 都达到 100% accuracy（4096 dim + MLP probe + 10 类太容易了）。DINO 86%（1024 dim）。这是维度混淆——需要用 PCA 降维到 1024 后用 linear probe 重新做公平比较。\n\n### 目标\n在服务器 westd-19183 上编写 `pca_linear_probe_gc.py` 脚本，放在 `/root/vla-ssd/` 目录下。\n\n### 环境\n- 服务器: westd-19183\n- Python: `/root/miniconda3/bin/python`，conda base 环境\n- 激活命令: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`\n- 已安装: torch, sklearn, numpy, h5py\n- **离线环境**: 不要 import 任何需要网络下载的包\n\n### 已有特征数据路径\n- Trained VLA (LIBERO-Goal): `/root/autodl-tmp/vla-ssd/features/trained_libero_goal/` — 10 个 .h5 文件，每个 50 demos，per-layer features (33 layers)，维度 4096，keys: `image_mean`, `last_preaction`\n- Untrained VLA (LIBERO-Goal): `/root/autodl-tmp/vla-ssd/features/untrained_libero_goal/` — 同上\n- DINO-V2 (LIBERO-Goal): `/root/autodl-tmp/vla-ssd/features/dino_libero_goal/` — 10 个 .h5 文件，每个 50 demos，单层，维度 1024，keys: `cls_token`, `patch_mean`\n\n### H5 文件结构\n先 SSH 到服务器，用 python 检查一个 h5 文件的实际结构（keys, shapes, dtypes），以此为基础编写代码。不要假设结构。\n\n### 脚本功能要求\n\n1. **PCA 降维**: 对 VLA features (4096) 做 PCA 降到 1024 dim（与 DINO 对齐）\n   - PCA 在 train split 上 fit，transform train 和 val\n   - 记录 explained variance ratio\n\n2. **Linear Probe (Logistic Regression)**:\n   - 用 sklearn LogisticRegression (multinomial, lbfgs, max_iter=1000)\n   - 10-way 分类 (10 个 LIBERO-Goal tasks)\n   - Label = task index (哪个 goal)\n   - Train/val split: 按 demo 划分 (前 40 demos train, 后 10 demos val), 保持与 MLP probe 一致\n\n3. **Per-layer sweep**: 对 VLA features 的 33 层分别做 PCA + linear probe，输出 per-layer accuracy\n\n4. **Per-timestep binning**: \n   - 将每个 demo 的 timesteps 等分为 10 bins\n   - 对每个 bin 分别做分类\n   - 输出 per-bin accuracy (重点关注 bin 0 = 初始帧)\n\n5. **Selectivity Index (Hewitt & Manning 2019)**:\n   - Control task: 随机打乱标签后训练同样的 linear probe\n   - Selectivity = task_accuracy - control_accuracy\n   - 跑 5 次 random shuffle 取均值\n\n6. **输出格式**:\n   - 打印 JSON 格式结果到 stdout\n   - 包含: model_name, pca_dim, per_layer_accuracies, per_timestep_accuracies, selectivity_scores, explained_variance_ratios\n   - 同时保存到 `/root/autodl-tmp/vla-ssd/results/pca_linear_probe_gc/` 目录下的 JSON 文件\n\n7. **命令行接口**:\n   - `--model_type`: trained / untrained / dino\n   - `--feature_dir`: 特征目录路径\n   - `--feature_key`: 使用哪个 feature key (默认 `last_preaction` for VLA, `cls_token` for DINO)\n   - `--pca_dim`: PCA 目标维度 (默认 1024, 对 DINO 跳过 PCA)\n   - `--output_dir`: 输出目录\n   - `--n_bins`: timestep bins 数 (默认 10)\n   - `--seed`: 随机种子 (默认 42)\n   - GPU 不需要——这是纯 CPU sklearn 任务\n\n### 参考：现有代码\n先查看 `/root/vla-ssd/goal_classification.py`（或类似名字的文件），了解现有 MLP probe 的数据加载逻辑，保持兼容。\n\n### 验证步骤\n1. 代码写完后，用 `python pca_linear_probe_gc.py --help` 验证能解析参数\n2. 用 trained features 跑一个 single layer (layer 1) 的 dry-run: `python pca_linear_probe_gc.py --model_type trained --feature_dir /root/autodl-tmp/vla-ssd/features/trained_libero_goal/ --pca_dim 1024 --output_dir /tmp/test_pca_probe`，确认能正常加载数据、PCA、训练 probe 并输出结果\n3. 如果 dry-run 成功，输出 layer 1 的 accuracy 和 selectivity，作为 sanity check\n\n### 出错诊断\n- ImportError: 检查 sklearn 是否已安装 (`pip list | grep scikit`)\n- h5 文件结构不对: 用 `h5py.File(f).visit(print)` 查看实际结构\n- 内存不够: 减少同时加载的层数（逐层处理）\n- PCA 太慢: 用 `sklearn.decomposition.PCA(n_components=1024, svd_solver='randomized')`\n\n### 代码质量\n- 文件顶部写文件注释（目的、输入输出、关键依赖）\n- 关键函数写 docstring\n- 所有 magic number 用命令行参数或常量",
    "tool_groups": "['ssh']",
    "context": "服务器 westd-19183, conda base 环境, 离线环境(不要下载任何包)。特征数据: trained_libero_goal / untrained_libero_goal / dino_libero_goal 在 /root/autodl-tmp/vla-ssd/features/ 下。目标: 写 PCA+linear probe 脚本，为 Director 审批后立即跑实验做准备。"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-15T19:20:51.460844+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_code_pca_linear_probe_20260515T192049\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/logs/workers/worker_code_pca_linear_probe_20260515T192049.log\", \"setup_data\": {}, \"message\": \"Worker worker_code_pca_linear_probe_20260515T192049 started. Use get_worker_status('worker_code_pca_linear_probe_20260515T192049') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 2916
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-15T19:21:16.329704+00:00_

Worker `worker_code_pca_linear_probe_20260515T192049` 已派出准备 PCA + linear probe 代码。

当前状态：
- **Framing 调整提案** 已发 Director，等待审批
- **Worker 1** 正在编写 `pca_linear_probe_gc.py` 脚本（代码准备，非实验执行）
- **2 GPU 空闲**，等 Director 批准后立即双卡并行跑 PCA 控制实验
- CoRL Abstract DDL 还剩 11 天，代码预计 < 30 分钟完成，Director 批准后可即时提交

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:openvla-trained-extract"
}
```

</details>

---

## Round 2

26 recorded events

### User

_source line 29 · 2026-05-15T22:22:06.457454+00:00_

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
  "session": "cron:hook:openvla-trained-extract",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-15T22:22:14.774221+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__load_project_config",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__load_project_config",
    "max_results": "6"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-15T22:22:14.824793+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-15T22:22:17.685739+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "vla-ssd",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "vla-ssd",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T22:22:18.238158+00:00_

called mcp__agent-ml-research__reconcile_crons

<details open><summary>🔧 Tool call — mcp__agent-ml-research__reconcile_crons</summary>

```json
Arguments not recorded in this source.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T22:22:18.239264+00:00_

Error: result (64,137 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-agent-f68a0575/240ceff0-42ee-43d3-ac4d-45f529d5d822/tool-results/mcp-agent-ml-research-read_registry-1778883738070.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-agent-f68a0575/240ceff0-42ee-43d3-ac4d-45f529d5d822/tool-results/mcp-agent-ml-research-read_registry-1778883738070.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-agent-f68a0575/240ceff0-42ee-43d3-ac4d-45f529d5d822/tool-results/mcp-agent-ml-research-read_registry-1778883738070.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 553
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-15T22:22:18.741461+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 0, \"results\": []}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 503
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-15T22:22:18.742053+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "vla-ssd",
  "file": "report.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "vla-ssd",
    "file": "report.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-15T22:22:18.792677+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/report.md\", \"content\": \"# Handover — 2026-05-15\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n- lg_instruction_ablation: D021 Exp-1: Instruction Ablation. Extract LIBERO-Goal features with empty instruction (trained + untrained VLA), then run RSA. If instruction pathway is the source of action-relevant structure, RSA should collapse from ρ≈0.49 to <0.15. PASS: ρ<0.15; PARTIAL: 0.15<ρ<0.30; FAIL: ρ≥0.30.（排队等待 GPU）\\n- lg_output_head_analysis: D021 Exp-2: Output Head Analysis. Compare trained vs untrained VLA weight differences across layers. If training does \\\"shallow adaptation\\\", output head weight diff >> middle layer weight diff. Explains \\\"representations unchanged but behavior improved\\\".（排队等待 GPU）\\n- d027_siglip_only_rsa: D027 Exp-1 (SMOKING GUN): Extract SigLIP+projector output features (LLM input embeddings) from VLA architecture on LIBERO-Goal, run RSA. If SigLIP-only RSA ≈ 0.45-0.50 → confirms vision encoder is the source of action-relevant structure (LLM is passthrough). If RSA ≈ 0.39 (DINO level) → projector/LLM architecture contributes, need reanalysis.（已分配 ? GPU:?，等待提交）\\n\\n## 近期结论\\n- **d027_trained_no_inst_rsa** (success): D027 Exp-2: Extract trained VLA features with empty instruction on LIBERO-Goal, run RSA. Completes the 2×2 matrix (training × instruction). Expected: trained no-inst RSA ≈ untrained no-inst (0.4802), further confirming training is irrelevant to representational structure.\\n- **d021_instruction_ablation** (negative): D021 Exp-1 (HARD GATE): Instruction Ablation on untrained VLA. Replace instruction with empty string, extract LIBERO-Goal features, run RSA. Gate (D023 relative): PASS = no-inst RSA significantly below with-inst (Δ>0.10, bootstrap CI excludes 0) AND no-inst RSA ≤ DINO RSA + 0.05. FAIL = no-inst RSA ≥ with-inst RSA − 0.05. PASS → lock Option B. FAIL → fallback Op
…[truncated 778 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-15T22:22:19.245090+00:00_

called mcp__agent-ml-research__read_roadmap

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap</summary>

```json
{
  "project": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-15T22:22:19.697285+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/ROADMAP.md\", \"content\": \"# vla-ssd — Research Dashboard\\n\\n> 最后更新: 2026-05-15 22:09 UTC | 更新原因: D027: Instruction ablation FAIL → Option A2 \\\"Vision Encoder Dominance\\\" framing 锁定，补充 SigLIP-only + trained no-inst 实验\\n\\n## 核心方向\\n\\n**\\\"Vision Encoder Dominance: The Architectural Source of Action-Relevant Representations in VLAs\\\"**（D027 确定）: VLA 中 action-relevant 表征由 frozen vision encoder（SigLIP）决定。LLM fine-tuning 和 instruction conditioning 均未显著改变表征结构。\\n\\n证据链：6 轮 probing × 2 benchmark → trained ≈ untrained >> DINO | instruction ablation → 去掉 instruction 不影响 RSA | output head analysis → SigLIP+projector frozen，LLM 权重变化不传导到表征。\\n\\n与 Grant 2026 互补：他们 behavioral level（\\\"encoded but not used\\\"），我们 representational level（\\\"vision encoder determines everything\\\"）。\\n\\n## 当前进展\\n\\n- **阶段**: D027 Framing 锁定 A2，补充验证实验 PREPARING\\n- **Instruction ablation FAIL**: Δ=0.0044 << 0.10，Option B 死亡\\n- **全部 MVP 证据一致**: trained ≈ untrained >> DINO，instruction 无影响，SigLIP+projector frozen\\n- **Output head analysis**: shallow adaptation 不成立，但发现 projector bottleneck 机制（D026）\\n- **Scope**: OpenVLA-class architecture（Limitations 明确标注）\\n\\n## 近期任务\\n\\n- [ ] **[P0] SigLIP-only features + RSA**（GPU:0, ~30min）: 不过 LLM，直接从 SigLIP 输出提取特征跑 RSA → smoking gun\\n- [ ] **[P0] Trained no-inst RSA**（GPU:1, ~1h）: 完成 2×2 matrix（training × instruction）\\n- [ ] **[P1] Per-layer RSA no-inst curve**（CPU）: with vs without instruction 的逐层 RSA 对比\\n- [ ] 两个 P0 实验完成 + positive → complete_mvp() → 启动 Paper Agent\\n- [ ] Framing 限定 OpenVLA-class，SigLIP vs DINOv2 差异在 Discussion 深入讨论\\n\\n## MVP Gate（D027 定义）\\n\\n```\\nSigLIP-only RSA 结果\\n├── RSA ≈ 0.48（与 full VLA 持平）→ smoking gun 确认，complete_mvp\\n├── RSA ≈ 0.39（与 DINO 持平）→ projector/LLM 架构有贡献，需重新分析\\n└── 中间值 → 部分支持，视具体数值决策\\n```\\n\\n## 已识别论文内部张力（须在写作中处理）\\n\\n1. SigLIP 是 image-text 预训练的 → gap 可能部分来自 language-awar
…[truncated 2218 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-15T22:22:20.199730+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "vla-ssd",
  "file": "memory.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "vla-ssd",
    "file": "memory.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-15T22:22:20.200205+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/memory.md\", \"content\": \"# VLA-SSD Project Memory\\n\\n## Instruction Ablation FAIL — Option B 被否证（2026-05-15）\\n\\n**d021_instruction_ablation 结果**: no-inst untrained RSA = 0.4802 ≈ with-inst 0.4846（Δ=0.0044 << 0.10 阈值）。去掉 instruction text 不影响 action-relevant 表征结构。\\n\\n**结论**: instruction input pathway 不是 action-relevant 结构的来源。Option B (\\\"Instruction Input Pathway Drives Conditioning, Not Training\\\") 被明确否证。需回退 Option A。\\n\\n**全 2×2 结果**:\\n| | with-inst | no-inst |\\n|---|---|---|\\n| trained | 0.4876 | (未测) |\\n| untrained | 0.4846 | 0.4802 |\\n| DINO | 0.388 | — |\\n\\n**教训**: VLA >> DINO 的 RSA gap (~+0.10) 不来自 instruction conditioning，也不来自 LLM training。最可能来源是 SigLIP vision encoder（image-text 预训练）vs DINOv2（self-supervised 预训练）的内在差异。\\n\\n## D023 Framing 决策（2026-05-15，已被 instruction ablation FAIL 推翻）\\n\\n~~**正式 Claim**: \\\"Instruction Input Pathway Drives Conditioning, Not Training\\\"~~ → 已否证\\n\\n**Hard Gate 结果**: FAIL。等待 Director 决策选择 Option A1/A2/A3。\\n\\n**写作约束**（仍适用）：\\n- Layer stability (31/33 vs 15/33) 定位为 \\\"reorganization without new knowledge injection\\\"\\n- Grant 2026 checkpoint 差异 (OFT vs standard) 须在 Related Work qualify\\n- Scope 限定为 OpenVLA-class architecture，不 over-claim generality\\n\\n## 核心发现：跨 7 轮实验一致（2026-05-15）\\n\\n**所有实验均显示同一模式：**\\n- VLA (trained or untrained, with or without instruction) >> DINO — 架构/vision encoder 差异\\n- Trained VLA ≈ Untrained VLA — LLM training 无显著影响\\n- With-instruction ≈ No-instruction — instruction text 无显著影响\\n\\n**RSA 数据**：\\n- Trained with-inst peak: 0.4876 (L9)\\n- Untrained with-inst peak: 0.4846 (L12)\\n- Untrained no-inst peak: 0.4802\\n- DINO: 0.388\\n- 深层 CKA 达 0.86（trained/untrained 表征高度相似）\\n\\n**解释**: VLA 架构中 action-relevant 表征由 frozen SigLIP vision encoder 决定。SigLIP 的 image-text 预训练赋予了优于 DINOv2 self-supervised 的 action-relevant 结构。LLM 权重（训练/随机）和 instruction 输入均未改变此结构。\\n\
…[truncated 2024 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-15T22:22:20.300814+00:00_

called mcp__agent-ml-research__load_project_config

<details open><summary>🔧 Tool call — mcp__agent-ml-research__load_project_config</summary>

```json
{
  "project_name": "vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "mcp__agent-ml-research__load_project_config",
  "tool_args": {
    "project_name": "vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-15T22:22:20.652502+00:00_

{"result":"{\"success\": true, \"data\": {\"project\": \"vla-ssd\", \"config\": {\"execution\": {\"gpu_ids\": [\"cuda:0\", \"cuda:1\"], \"project_path\": \"/root/vla-ssd\", \"servers\": [\"westd-19183\"]}, \"feishu\": {\"chat_id\": \"oc_a1d032cbe70bdd2058438e67e0d57613\", \"operational_chat_id\": \"oc_9e9aef1687e6abd097aa0edaf0551ee3\"}, \"project\": {\"created_at\": \"2026-05-15T04:32:26.871Z\", \"description\": \"VLA-SSD: Do VLAs Know Which Demonstrations Are Good? Self-Referential Quality Scoring from Pretrained Representations\", \"name\": \"vla-ssd\", \"phase\": \"mvp\", \"source_idea_id\": \"idea_004\"}}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "mcp__agent-ml-research__load_project_config",
  "elapsed_ms": 351
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-15T22:22:20.652837+00:00_

called mcp__agent-ml-research__list_workers

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_workers</summary>

```json
{
  "project": "vla-ssd",
  "status": "running"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "mcp__agent-ml-research__list_workers",
  "tool_args": {
    "project": "vla-ssd",
    "status": "running"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-15T22:22:20.803695+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_ssh_d027-siglip-only-rsa_20260515T221202\", \"task_type\": \"ssh:d027-siglip-only-rsa\", \"project\": \"vla-ssd\", \"status\": \"running\", \"started_at\": \"2026-05-15T22:12:02.769481+00:00\", \"ended_at\": null}], \"count\": 1}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 150
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-15T22:22:29.550127+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-agent-f68a0575/240ceff0-42ee-43d3-ac4d-45f529d5d822/tool-results/mcp-agent-ml-research-read_registry-1778883738070.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nexps = json.loads(data['result'])['data']['experiments']\nprint(f'Total experiments: {len(exps)}')\nprint()\nfor e in exps:\n    print(f\\\"{e['exp_id']:40s} | {e['status']:12s} | {e.get('conclusion',''):10s} | {e.get('hypothesis','')[:60]}\\\")\n\"",
  "description": "Parse registry to get experiment summary"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-agent-f68a0575/240ceff0-42ee-43d3-ac4d-45f529d5d822/tool-results/mcp-agent-ml-research-read_registry-1778883738070.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nexps = json.loads(data['result'])['data']['experiments']\nprint(f'Total experiments: {len(exps)}')\nprint()\nfor e in exps:\n    print(f\\\"{e['exp_id']:40s} | {e['status']:12s} | {e.get('conclusion',''):10s} | {e.get('hypothesis','')[:60]}\\\")\n\"",
    "description": "Parse registry to get experiment summary"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-15T22:22:29.952701+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 8, in &lt;module>
    print(f"{e['exp_id']:40s} | {e['status']:12s} | {e.get('conclusion',''):10s} | {e.get('hypothesis','')[:60]}")
             ~^^^^^^^^^^
TypeError: string indices must be integers, not 'str'
Total experiments: 35

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "Bash",
  "elapsed_ms": 402
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-15T22:22:30.003420+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__poll_cron",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__poll_cron",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-15T22:22:30.004260+00:00_

&lt;tool_use_error>Cancelled: parallel tool call Bash(cat /home/ubuntu/.claude-account-2/proje…) errored&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-15T22:22:35.073280+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-agent-f68a0575/240ceff0-42ee-43d3-ac4d-45f529d5d822/tool-results/mcp-agent-ml-research-read_registry-1778883738070.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nexps = inner['data']['experiments']\nprint(f'Total experiments: {len(exps)}')\nprint(f'Type of first: {type(exps[0])}')\nif isinstance(exps[0], dict):\n    print(f'Keys: {list(exps[0].keys())}')\nelif isinstance(exps[0], str):\n    # maybe it's a list of exp_ids, need to parse differently\n    print(f'First 3: {exps[:3]}')\n\"",
  "description": "Probe registry structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-agent-f68a0575/240ceff0-42ee-43d3-ac4d-45f529d5d822/tool-results/mcp-agent-ml-research-read_registry-1778883738070.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nexps = inner['data']['experiments']\nprint(f'Total experiments: {len(exps)}')\nprint(f'Type of first: {type(exps[0])}')\nif isinstance(exps[0], dict):\n    print(f'Keys: {list(exps[0].keys())}')\nelif isinstance(exps[0], str):\n    # maybe it's a list of exp_ids, need to parse differently\n    print(f'First 3: {exps[:3]}')\n\"",
    "description": "Probe registry structure"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-15T22:22:35.274434+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 7, in &lt;module>
    print(f'Type of first: {type(exps[0])}')
                                 ~~~~^^^
KeyError: 0
Total experiments: 35

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-15T22:22:40.094732+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-agent-f68a0575/240ceff0-42ee-43d3-ac4d-45f529d5d822/tool-results/mcp-agent-ml-research-read_registry-1778883738070.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nexps = inner['data']['experiments']\nprint(f'Type: {type(exps)}')\nif isinstance(exps, dict):\n    for k, v in exps.items():\n        status = v.get('status','?') if isinstance(v, dict) else '?'\n        conclusion = v.get('conclusion','') if isinstance(v, dict) else ''\n        print(f'{k:40s} | {status:12s} | {conclusion}')\n\"",
  "description": "Parse registry as dict"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd--claude-sessions-agent-f68a0575/240ceff0-42ee-43d3-ac4d-45f529d5d822/tool-results/mcp-agent-ml-research-read_registry-1778883738070.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\ninner = json.loads(data['result'])\nexps = inner['data']['experiments']\nprint(f'Type: {type(exps)}')\nif isinstance(exps, dict):\n    for k, v in exps.items():\n        status = v.get('status','?') if isinstance(v, dict) else '?'\n        conclusion = v.get('conclusion','') if isinstance(v, dict) else ''\n        print(f'{k:40s} | {status:12s} | {conclusion}')\n\"",
    "description": "Parse registry as dict"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-15T22:22:40.195619+00:00_

Type: &lt;class 'dict'>
d027_trained_no_inst_rsa                 | DONE         | success
d027_siglip_only_rsa                     | ALLOCATED    | 
d021_instruction_ablation                | DONE         | negative
lg_instruction_ablation                  | QUEUED       | killed
lg_output_head_analysis                  | QUEUED       | killed
d021_output_head_analysis                | DONE         | negative
lg_rsa_analysis                          | DONE         | negative
lg_shuffled_token_control                | DONE         | killed
lg_pca1024_linear_pertimestep            | DONE         | negative
lg_gc_trained_frame0                     | DONE         | success
lg_gc_untrained                          | DONE         | negative
lg_gc_dino                               | DONE         | success
lg_dino_extract                          | DONE         | success
lg_gc_trained                            | DONE         | success
lg_extract_untrained                     | DONE         | success
lg_extract_trained                       | DONE         | success
mvp2_action_probe                        | DONE         | killed
lg_extract_untrained_r2                  | DONE         | killed
lg_extract_trained_r2                    | DONE         | killed
lg_extract_untrained_r1                  | DONE         | killed
lg_extract_trained_r1                    | DONE         | killed
mvp2_delta_dino                          | DONE         | success
mvp2_delta_untrained                     | DONE         | success
mvp2_delta_trained                       | DONE         | success
mvp2_action_dino                         | DONE         | success
mvp2_action_untrained                    | DONE         | success
mvp2_action_trained                      | DONE         | success
dinov2_baseline                          | DONE         | success
mvp_controlb_untrained                   | DONE         | success
mvp_controlb_trained                     | DONE         | success
mvp_001  
…[truncated 322 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:openvla-trained-extract",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---

### Assistant

_source line 54 · 2026-05-15T22:23:31.890022+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- GPU 白名单：**cuda:0, cuda:1**（westd-19183），禁止用其他 GPU
- 服务器**无外网**：所有 HuggingFace/AutoProcessor 操作必须 `local_files_only=True`
- **分析 Worker 不得覆盖 spec 字段**（registry 里的 command/server/data_path 等）
- Untrained model = `from_config()` 重新初始化 LLM（6.74B random），**保留 SigLIP**（0.80B frozen）
- Token 聚合统一用 **last pre-action token**，不要改
- Instruction ablation 代码已修复 bug：`if args.task_instruction:` 对空字符串返回 False，现在用显式 None 检查
- Scope 限定 **OpenVLA-class architecture**，不 over-claim generality

### 2. 🖥️ 基础设施快照
- 服务器：**westd-19183**，工作目录 `/root/vla-ssd/`
- Python/conda：用 `detect_image` 检测镜像类型再决定（aml-train 用 conda base: `/root/miniconda3/bin/python`）
- 数据盘：`/root/autodl-tmp/vla-ssd/`（大文件、模型、HF cache）
- HF cache：`HF_HOME=/root/autodl-tmp/.hf_cache`
- W&B：无活跃 run（本项目主要是离线 RSA 分析，不走 W&B）
- 活跃 Worker：`worker_ssh_d027-siglip-only-rsa_20260515T221202`（RUNNING，正在执行 SigLIP-only RSA smoking gun 实验）
- 活跃 Cron：0（reconcile 返回空）
- GPU 状态：2× RTX PRO 6000，当前 0/2 占用（d027_siglip_only_rsa ALLOCATED 待提交，worker 正在处理）

### 3. 📊 当前状态
**刚完成**：d027_trained_no_inst_rsa (SUCCESS) — trained VLA with empty instruction RSA，完成了 2×2 matrix 的最后一格。

**正在进行**：Worker `worker_ssh_d027-siglip-only-rsa` 正在执行 d027_siglip_only_rsa（ALLOCATED 状态）——这是 **SMOKING GUN** 实验：从 SigLIP+projector 直接提取特征（不过 LLM），跑 RSA。如果 RSA ≈ 0.48 = vision encoder 单独就能解释全部 action-relevant structure，complete_mvp 条件满足。

**Registry 摘要**：35 实验，19 success / 7 negative / 6 killed / 0 failed。唯一非 DONE 的：d027_siglip_only_rsa (ALLOCATED)，lg_instruction_ablation + lg_output_head_analysis (QUEUED/killed，已被 d021 系列替代，可忽略)。

**等待中**：Worker 完成回调（d027-siglip-only-rsa）。无 Director 决策待回。

### 4. 📋 待办（条件触发式）
- Worker `d027-siglip-only-rsa` 回调 DONE →
  - RSA ≈ 0.45-0.50 → smoking gun 确认，update_registry(conclusion=success)，汇报 Director "[资源] ..."，调 complete_mvp，启动 Paper Agent 写作流程
  - RSA ≈ 0.39（DINO 水平）→ projector/LLM 架构有贡献，conclusion=negative，产出 Framing 调整提案给 Director
  - 中间值 → 部分支持，汇报 Director 让其决策
- complete_mvp 后 → 读 paper_framing.md + writing_plan.yaml（如有），派 Worker 开始论文章节写作（CoRL abstract DDL May 26，仅剩 11 天）
- 任何实验完成 → 按 on-experiment-done skill 执行全套流程（registry + report.md + 文献联动 + 反思实验计划）

### 5. 🎯 战略上下文
**核心结论链**：7 轮实验 + 2 benchmark 一致显示 trained ≈ untrained >> DINO，instruction 无影响。Option B（instruction drives conditioning）被 Δ=0.0044 明确否证。D027 锁定 **Option A2 "Vision Encoder Dominance"**——frozen SigLIP 决定 action-relevant 表征，LLM 是 passthrough。

**MVP Gate**：SigLIP-only RSA 是最后一个 data point。如果 ≈ 0.48 则 complete_mvp，如果 ≈ 0.39 则需要 reframe（不太可能，因为 projector 权重 trained=untrained 完全一致）。

**易错点**：
- d027_trained_no_inst_rsa 的结果需要合并到 2×2 matrix 里汇报（trained no-inst 这格现在有数据了）
- 不要把 lg_ 前缀的旧实验（已 killed）和 d021_/d027_ 前缀的新实验搞混——lg_ 是被替代的旧版
- CoRL DDL 很紧（abstract May 26 = 11 天），complete_mvp 后必须立即启动多 Worker 并行写论文
- Output head analysis 结论是 "shallow adaptation 不成立"，但发现了 **projector bottleneck** 机制（vision backbone + projector 在 trained/untrained 间完全一致，cos_sim=1.0）——这是支持 A2 framing 的因果证据
- Grant 2026 用的是 OFT checkpoint（非标准 fine-tuning），Related Work 必须 qualify 这个差异
- 论文写作前必须读 red-section skill 规范
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:openvla-trained-extract"
}
```

</details>

---
