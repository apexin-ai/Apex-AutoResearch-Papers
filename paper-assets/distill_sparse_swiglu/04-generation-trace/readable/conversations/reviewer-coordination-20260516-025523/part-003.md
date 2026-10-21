# Reviewer coordination (archived snapshot) — Part 3 of 3

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Conversation logs

[← Part 2](part-002.md) · [Transcript overview](../reviewer-coordination-20260516-025523.md) · [Structured JSON](../../../sessions/06/06432cb43ef15613c9fc.json)

## Round 77

### Tool call

_source line 1582 · 2026-05-16T02:54:07.759474+00:00_

called mcp__agent-ml-research__read_roadmap

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap</summary>

```json
{
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9377f94f5f31e719154474b70f5c3d18:reviewer",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1583 · 2026-05-16T02:54:07.860370+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/ROADMAP.md\", \"content\": \"# distill_sparse_swiglu — Research Dashboard\\n\\n> 最后更新: 2026-05-16 02:53 UTC | 更新原因: D030: 30% downstream collapse + per-layer sparsity imbalance root cause; new P0 uniform allocation ablation\\n\\n## 核心方向\\nKL distillation 使 SwiGLU LLM 的 contextual sparsity prediction 不再需要 error compensation 和 static bias correction，实现最简推理管线。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research + 审稿进行中（EMNLP 2026 ARR May, DDL 2026-05-25）\\n- **实验**: plan_001-006 全部完成，plan_008 部分完成（30% 训练+PPL done，downstream 崩溃）\\n- **Claim 1 (KL >> all baselines)**: ✅ PPL 层面确认\\n- **Claim 2 (SPON orthogonal)**: ✅ 确认\\n- **Claim 3 (sparsity scaling)**: ⚠️ 重大发现 — 见下方\\n\\n### ⚠️ 关键发现：Per-Layer Sparsity 不均匀导致 Downstream 崩溃 (D030)\\n- 30% KL: PPL 8.98（+47%），但 MMLU 28.74%（≈随机）、GSM8K 7.43%（-85%）\\n- **根因**：全局 top-k 将 sparsity 集中在后层（Layer 26-31: 41-70%，Layer 31=70.3%）\\n- PPL 是平均指标（前层好即可），downstream 依赖后层精确输出 → 后层在\\\"崩溃区\\\"运行\\n- **PPL 作为 sparse model 质量指标完全不可信** — 潜在新 contribution\\n- 待验证：uniform per-layer allocation 是否修复 downstream collapse\\n\\n## 近期任务\\n- [ ] **[P0] 提取 50% per-layer sparsity 分布**：确认同样的后层集中模式\\n- [ ] **[P0] 实现 uniform per-layer allocation**：每层独立 top-k，不需重新训练\\n- [ ] **[P0] Uniform 30%+50% 消融实验**：PPL + 4 task downstream，与 global 对比\\n- [ ] plan_007 benchmark eval 统一重跑（benchmark_eval.py 就绪后）\\n- [ ] plan_009 Mistral 泛化验证\\n- [ ] 修复 lm_eval_teal_50pct registry model 字段错误\\n- [ ] 根据 uniform 实验结果决定是否更新 paper_framing.md Claim 3\\n\\n## GPU 预算\\n- 分配: westd-34887 cuda:0 + cuda:1\\n- 当前: Agent 处理 worker_done 队列中，即将启动 uniform per-layer 实验\\n- 累计 GPU·h: ~90h used / plan 总预算 ~196h\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D030 | 2026-05-16 | 30% KL 不能作为推荐配置；per-layer sparsity 不均匀是 downstream | lm_eval_kl_30pct_s42, kl_sparsity30_s42_v3 |\\n| D029 | 2026-05-16 | 统一 few-shot 设置：plan_007 用 benchm
…[truncated 1031 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9377f94f5f31e719154474b70f5c3d18:reviewer",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1584 · 2026-05-16T02:54:34.589306+00:00_

called mcp__agent-ml-research__reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__reviewer_post_to_director</summary>

```json
{
  "text": "[severity: info] ROADMAP D030 更新审查 — 方向正确，几处需同步\n\n## 审查结论：PASS\n\nROADMAP 正确反映了 per-layer sparsity 不均匀作为 downstream collapse 根因的发现，P0 优先级设置合理。\n\n## 需同步的事项\n\n1. **\"[P0] 提取 50% per-layer sparsity 分布\"已完成**：我在上一条审查中已独立提取并发送了完整的 50% per-layer 数据（Layer 17=0.301 min → Layer 29=0.701 max）。确认 50% 呈现同样的后层集中模式。此项可标 ✅。\n\n2. **Mistral 泛化数据缺失**：ROADMAP 提到 plan_009 Mistral 验证为 todo，但此前 session 已完成 Mistral downstream eval（MMLU 27.58%、GSM8K 0.76%，与 Llama 同样模式）。建议补入证据链。\n\n3. **lm_eval_teal_50pct registry model 字段错误**：已标为 todo ✅，确认需修正 \"Qwen2.5-7B-Instruct\" → \"llama-3.1-8b\"。\n\n## GPU 预算评估\n90h / 196h (46%) 已用，9 天剩余。Uniform allocation 实验预计 < 5 GPU-hours（PPL + downstream × 2 sparsity levels）。**算力充足，无 deadline 风险**。\n\n## 方向判断\nUniform per-layer allocation 作为 pivot 方向有充分数据支撑（两个 sparsity level 的 per-layer 数据 + downstream 崩溃 + 代码可行性确认）。如果实验成功，论文 story 从\"KL distillation improves PPL\"升级为\"per-layer allocation insight + simple fix\"，contribution 更强。",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9377f94f5f31e719154474b70f5c3d18:reviewer",
  "tool": "mcp__agent-ml-research__reviewer_post_to_director",
  "tool_args": {
    "text": "[severity: info] ROADMAP D030 更新审查 — 方向正确，几处需同步\n\n## 审查结论：PASS\n\nROADMAP 正确反映了 per-layer sparsity 不均匀作为 downstream collapse 根因的发现，P0 优先级设置合理。\n\n## 需同步的事项\n\n1. **\"[P0] 提取 50% per-layer sparsity 分布\"已完成**：我在上一条审查中已独立提取并发送了完整的 50% per-layer 数据（Layer 17=0.301 min → Layer 29=0.701 max）。确认 50% 呈现同样的后层集中模式。此项可标 ✅。\n\n2. **Mistral 泛化数据缺失**：ROADMAP 提到 plan_009 Mistral 验证为 todo，但此前 session 已完成 Mistral downstream eval（MMLU 27.58%、GSM8K 0.76%，与 Llama 同样模式）。建议补入证据链。\n\n3. **lm_eval_teal_50pct registry model 字段错误**：已标为 todo ✅，确认需修正 \"Qwen2.5-7B-Instruct\" → \"llama-3.1-8b\"。\n\n## GPU 预算评估\n90h / 196h (46%) 已用，9 天剩余。Uniform allocation 实验预计 < 5 GPU-hours（PPL + downstream × 2 sparsity levels）。**算力充足，无 deadline 风险**。\n\n## 方向判断\nUniform per-layer allocation 作为 pivot 方向有充分数据支撑（两个 sparsity level 的 per-layer 数据 + downstream 崩溃 + 代码可行性确认）。如果实验成功，论文 story 从\"KL distillation improves PPL\"升级为\"per-layer allocation insight + simple fix\"，contribution 更强。",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---


### Tool result

_source line 1585 · 2026-05-16T02:54:38.819309+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_dbbf8d2c695f1e79e11713aebc107790:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9377f94f5f31e719154474b70f5c3d18:reviewer",
  "tool": "mcp__agent-ml-research__reviewer_post_to_director",
  "elapsed_ms": 4230
}
```

</details>

---


### Tool call

_source line 1586 · 2026-05-16T02:54:43.140090+00:00_

called ScheduleWakeup

<details open><summary>🔧 Tool call — ScheduleWakeup</summary>

```json
{
  "delaySeconds": "270",
  "reason": "Check if uniform per-layer ablation experiment has been launched on free GPUs",
  "prompt": "Continue from where you left off."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_9377f94f5f31e719154474b70f5c3d18:reviewer",
  "tool": "ScheduleWakeup",
  "tool_args": {
    "delaySeconds": "270",
    "reason": "Check if uniform per-layer ablation experiment has been launched on free GPUs",
    "prompt": "Continue from where you left off."
  }
}
```

</details>

---


### Tool result

_source line 1587 · 2026-05-16T02:54:43.190658+00:00_

Next wakeup scheduled for 02:59:00 (in 257s).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_9377f94f5f31e719154474b70f5c3d18:reviewer",
  "tool": "ScheduleWakeup",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 1588 · 2026-05-16T02:54:45.441563+00:00_

ROADMAP 审查通过。方向正确，P0 优先级合理，GPU 预算充足。提醒 Director：50% per-layer 数据我已提取完毕可标 done。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9377f94f5f31e719154474b70f5c3d18:reviewer"
}
```

</details>

---


## Round 78

## Round 78

2 recorded events


### User

_source line 1589 · 2026-05-16T02:54:45.918770+00:00_

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
  "session": "feishu:group:oc_9377f94f5f31e719154474b70f5c3d18:reviewer",
  "source": "system:ralph_loop"
}
```

</details>

---


### Assistant

_source line 1590 · 2026-05-16T02:55:23.534911+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- GPU 只能用 cuda:0 和 cuda:1（westd-34887，C001 约束）。每次审查 RUNNING 实验必查 CUDA_VISIBLE_DEVICES 是否越界。
- lm_eval_teal_50pct registry 中 model 字段写错为 "Qwen2.5-7B-Instruct"，实际是 llama-3.1-8b。Agent 尚未修正，审查时注意不要被 registry metadata 误导。
- ssh_read_only 不支持 shell metacharacters（`|`, `2>/dev/null`, `&&`）。用纯命令，不拼管道。

### 2. 🖥️ 基础设施快照
- 服务器：westd-34887(root)，项目目录 /root/distill_sparse_swiglu/
- Python：/root/miniconda3/bin/python（conda base）
- 模型：/root/distill_sparse_swiglu/models/llama-3.1-8b, /root/autodl-tmp/models/Mistral-7B-v0.3
- HF cache：/root/autodl-tmp/.hf_cache（HF_HUB_OFFLINE=1 必须设置，AutoDL 网络不稳）
- 日志目录：/root/runs/distill_sparse_swiglu/
- 结果目录：/root/distill_sparse_swiglu/results/
- 本地 workspace：/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/
- 活跃进程：截至 handoff 时两个 GPU 均空闲（lm_eval_kl_30pct_s42 和 lm_eval_teal_50pct 均已完成）

### 3. 📊 当前状态
刚完成两个 P0 诊断实验的审查并发了 3 条 critical review：
1. **TEAL 50% downstream** (DONE): 崩溃与 KL 50% 一致，确认 50% collapse 是 universal
2. **30% KL downstream** (DONE, negative): MMLU 28.74%≈随机，ARC-c 37.37%≈50% 水平。30% 不能作为推荐配置
3. **Per-layer sparsity 根因分析** (已完成): 30% 和 50% 都呈现后层过度剪枝（Layer 31=70%），统一解释所有 downstream failure

Registry PREPARING 但未启动：lm_eval_teal_30pct（建立完整曲线）
Director 刚批准 D030，ROADMAP 已更新，P0 是 uniform per-layer allocation 消融实验。
两个 GPU 空闲，等 Agent 实现 _perlayer_topk_masks 并启动实验。

### 4. 📋 待办
- Agent 提交 uniform per-layer 30%/50% 实验 → 审查代码改动是否只改了 mask 选取逻辑（不应改 predictor 训练）→ 监控 GPU 合规 → 结果出来后对比 global vs uniform downstream
- Uniform 30% MMLU > 40% → 支持 "per-layer allocation insight" 作为核心 contribution，审查论文 narrative pivot
- Uniform 30% MMLU ≈ 28% (仍随机) → per-layer 分布不是唯一根因，需要更深入的诊断（可能是 predictor 训练目标本身的问题）
- lm_eval_teal_30pct 完成 → 对比 TEAL 30% vs KL 30% downstream，补全 sparsity-task tradeoff 曲线
- 论文章节提交审查 → 按 5.1-5.2 维度审查（method/related work workers 已完成，可能很快提交）

### 5. 🎯 战略上下文
**决策链**：D025(retracted)→D026(sparsity destroys representations)→D027/D028(50% collapse universal)→D030(per-layer imbalance root cause)

**核心结论**：KL predictor 在 PPL 上显著优于 baselines（Claim 1 成立），但 PPL 优势完全不 translate 到 downstream tasks。根因是全局 top-k 将 sparsity 集中在后层（Layer 26-31 达 50-70%），而这些层对 downstream 至关重要。

**最容易判断错的事**：
1. 不要被 PPL 数字迷惑——PPL 8.98（仅+47%）但 MMLU 已崩溃到随机。PPL 作为 sparse model 质量指标不可信。
2. ARC-c 在 30% 和 50% 几乎一样（37.37% vs 37.71%），不是 noise，是后层 sparsity 在两个 target 下都在崩溃区（~70%）。
3. uniform per-layer 实验是 make-or-break：成功则论文有清晰 contribution（insight + fix），失败则需要根本性 rethink。
4. DDL 2026-05-25（9 天），GPU 预算充足（90/196h used），不存在算力瓶颈。
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_9377f94f5f31e719154474b70f5c3d18:reviewer"
}
```

</details>

---
