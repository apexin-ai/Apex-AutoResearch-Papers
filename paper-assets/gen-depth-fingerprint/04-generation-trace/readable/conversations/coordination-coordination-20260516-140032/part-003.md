# Project coordination (archived snapshot) — Part 3 of 3

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Conversation logs

[← Part 2](part-002.md) · [Transcript overview](../coordination-coordination-20260516-140032.md) · [Structured JSON](../../../sessions/03/03a91f73c14f4b3e4193.json)

## Round 105

### Tool call

_source line 1184 · 2026-05-16T13:58:00.881238+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

````json
{
  "task_type": "ops:verify-baseline-ci",
  "project": "gen-depth-fingerprint",
  "task_prompt": "## 任务：检查并修正 8gen_baselines.json 中的 CI 异常\n\n**服务器**：autodl-5090\n**环境激活**：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`\n\n### 步骤\n\n1. 读取当前文件内容：\n```bash\npython3 -c \"\nimport json\nwith open('/root/gen-depth-fingerprint/results/8gen_baselines.json') as f:\n    d = json.load(f)\nprint(json.dumps(d, indent=2))\n\"\n```\n\n2. 分析每个 baseline 的 F1 点估计 vs CI。正常情况：点估计应在 CI 内。\n   - 如果 CI 下界 > 点估计，说明计算错误\n\n3. 检查生成此 JSON 的脚本（可能是 `/root/gen-depth-fingerprint/compute_8gen_baselines.py` 或类似名称）：\n```bash\nls /root/gen-depth-fingerprint/*baseline* /root/gen-depth-fingerprint/*8gen_base* 2>/dev/null\n```\n   读取脚本中 CI 计算逻辑，找到 bug。\n\n4. **如果发现 CI 计算错误**：\n   - 修正脚本中的 CI 计算（应该是 bootstrap resampling，对每个 held-out fold 的预测做 document-level resampling）\n   - 重新计算 CI 并更新 JSON 文件\n   \n   可能的 bug：CI 可能是在整体数据上算的而非 per-fold，或者 CI 是基于不同 metric（如 accuracy 而非 F1）\n\n5. **如果 CI 正确但点估计不对**：\n   - 点估计可能是某种 average 而 CI 是在不同数据分割上算的\n   - 确认哪个是正确的\n\n6. 修正后的 JSON 保持原格式，覆盖保存到 `/root/gen-depth-fingerprint/results/8gen_baselines.json`\n\n### 报告\n- 异常原因\n- 修正后的正确数值\n- 修正后所有 baseline 的 F1 + CI 完整表格",
  "tool_groups": "['ssh']"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a189a3add89efad7437b5c9f3e05fbf3",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "ops:verify-baseline-ci",
    "project": "gen-depth-fingerprint",
    "task_prompt": "## 任务：检查并修正 8gen_baselines.json 中的 CI 异常\n\n**服务器**：autodl-5090\n**环境激活**：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`\n\n### 步骤\n\n1. 读取当前文件内容：\n```bash\npython3 -c \"\nimport json\nwith open('/root/gen-depth-fingerprint/results/8gen_baselines.json') as f:\n    d = json.load(f)\nprint(json.dumps(d, indent=2))\n\"\n```\n\n2. 分析每个 baseline 的 F1 点估计 vs CI。正常情况：点估计应在 CI 内。\n   - 如果 CI 下界 > 点估计，说明计算错误\n\n3. 检查生成此 JSON 的脚本（可能是 `/root/gen-depth-fingerprint/compute_8gen_baselines.py` 或类似名称）：\n```bash\nls /root/gen-depth-fingerprint/*baseline* /root/gen-depth-fingerprint/*8gen_base* 2>/dev/null\n```\n   读取脚本中 CI 计算逻辑，找到 bug。\n\n4. **如果发现 CI 计算错误**：\n   - 修正脚本中的 CI 计算（应该是 bootstrap resampling，对每个 held-out fold 的预测做 document-level resampling）\n   - 重新计算 CI 并更新 JSON 文件\n   \n   可能的 bug：CI 可能是在整体数据上算的而非 per-fold，或者 CI 是基于不同 metric（如 accuracy 而非 F1）\n\n5. **如果 CI 正确但点估计不对**：\n   - 点估计可能是某种 average 而 CI 是在不同数据分割上算的\n   - 确认哪个是正确的\n\n6. 修正后的 JSON 保持原格式，覆盖保存到 `/root/gen-depth-fingerprint/results/8gen_baselines.json`\n\n### 报告\n- 异常原因\n- 修正后的正确数值\n- 修正后所有 baseline 的 F1 + CI 完整表格",
    "tool_groups": "['ssh']"
  }
}
````

</details>

---


### Tool result

_source line 1185 · 2026-05-16T13:58:06.406543+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_ops_verify-baseline-ci_20260516T135801\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/logs/workers/worker_ops_verify-baseline-ci_20260516T135801.log\", \"setup_data\": {}, \"message\": \"Worker worker_ops_verify-baseline-ci_20260516T135801 started. Use get_worker_status('worker_ops_verify-baseline-ci_20260516T135801') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a189a3add89efad7437b5c9f3e05fbf3",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 5525
}
```

</details>

---


## Round 106

## Round 106

3 recorded events


### User

_source line 1186 · 2026-05-16T13:58:46.902730+00:00_

[Director 指令] **紧急：baselines 度量不一致，需要修正**

Reviewer 发现 `8gen_baselines.json` 中 point estimate 和 CI 用了不同度量：
- Point estimate = macro-averaged per-generator binary F1
- CI = bootstrap on pooled predictions

论文需要的是 **pooled LOGO F1**（与我们的 0.762/0.694 同口径）。

请重新从 baselines LOGO 输出中提取 **pooled** 数字（不是 per-gen macro average），更新 `8gen_baselines.json`：

```python
# 每个 baseline 需要：
# - pooled_3class_f1: 所有样本 pool 在一起的 3-class F1
# - pooled_binary_f1: 所有样本 pool 在一起的 binary F1
# - pooled_binary_ci: bootstrap 95% CI (与 0.694 的 [0.688, 0.700] 同方法)
```

关键确认：**4det_surface 的 pooled binary F1 是否 > 0.694？** 如果是，这改变论文措辞。

用统一口径重算后汇报完整 baselines 表。最高优先级。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_a189a3add89efad7437b5c9f3e05fbf3",
  "source": "director"
}
```

</details>

---


### Tool call

_source line 1187 · 2026-05-16T13:59:15.899911+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

````json
{
  "task_type": "code:fix-baselines-pooled-metrics",
  "project": "gen-depth-fingerprint",
  "task_prompt": "## 任务：修正 baselines 度量为 pooled LOGO F1（统一口径）\n\n**最高优先级。**\n\n**服务器**：autodl-5090\n**GPU**：cuda:0（可能需要重跑 baseline 推理）\n**环境激活**：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`\n**项目路径**：/root/gen-depth-fingerprint/\n\n### 背景\n\n当前 `8gen_baselines.json` 的 point estimate 是 per-gen macro average，但论文需要 **pooled LOGO F1**：\n- 把所有 8 fold 的 held-out predictions pool 到一起\n- 在 pooled predictions 上计算 macro F1\n- 与我们的 7-feature 结果 (0.762/0.694) 同口径\n\n### 需要的输出\n\n对每个 baseline 计算：\n1. `pooled_3class_f1`: 所有 held-out predictions 合并后的 3-class macro F1\n2. `pooled_binary_f1`: 合并后 gen-1 vs gen-2+ 的 macro F1\n3. `pooled_binary_ci`: bootstrap 95% CI（document-level resampling, n=1000）\n\n### 方法\n\n1. 找到之前 baselines 脚本（计算 8gen_baselines.json 的脚本）：\n```bash\nls /root/gen-depth-fingerprint/*baseline* /root/gen-depth-fingerprint/compute_8gen* 2>/dev/null\n```\n\n2. 关键：需要保存每个 fold 的 held-out predictions（而不仅仅是 F1 分数）。如果之前脚本没保存 predictions，需要重跑 LOGO 并保存 predictions。\n\n3. 重跑 LOGO baseline evaluation：\n   - 对每个 baseline score，8-gen LOGO（hold out 1 generator, train on 7）\n   - XGBoost: n_estimators=100, max_depth=3（单特征 baseline 配置）\n   - 保存每个 fold 的 (y_true, y_pred) predictions\n   - Pool 所有 8 folds 的 predictions\n   - 计算 pooled macro F1（3-class, binary）\n   - Bootstrap CI on pooled predictions\n\n4. 同时重跑 ensemble 配置：\n   - 4-det ensemble: 4 scores as features, XGBoost 100/3\n   - 4-det + surface: 4 scores + ttr + hapax_ratio, XGBoost 100/3\n   - 7-feature (ours): 7 features, XGBoost **200/6**（论文配置！不是 100/3）\n\n5. **关键检查**：4det_surface 的 pooled binary F1 是否 > 0.694（我们的 7-feature）？\n\n### 数据位置\n\n- 原 6-gen features + baseline scores: `/root/gen-depth-fingerprint/data/features_all_models.csv`\n  - 检查是否包含 avg_logprob, fastdetectgpt, binoculars, ld_score 列\n- 新 Llama/Mistral: features_pythia410m.jsonl（有 7 features，但可能没有 baseline detection scores）\n\n如果新 generators 缺少 detection scores：\n- avg_logprob: 可以从 entropy_mean 近似（= -avg_logprob），或从 features 中现有 NLL 数据计算\n- fastdetectgpt/binoculars/ld_score: 需要从脚本中确认如何计算\n\n**检查现有代码了解 baseline scores 的来源，然后决定是重新计算还是有近似方法。**\n\n### 输出\n\n覆盖 `/root/gen-depth-fingerprint/results/8gen_baselines.json`:\n```json\n{\n  \"avg_logprob\": {\"pooled_3class_f1\": ..., \"pooled_binary_f1\": ..., \"pooled_binary_ci\": [lower, upper]},\n  \"fastdetectgpt\": {...},\n  \"ld_score\": {...},\n  \"binoculars\": {...},\n  \"4det_ensemble\": {\"pooled_3class_f1\": ..., \"pooled_binary_f1\": ..., \"pooled_binary_ci\": [...]},\n  \"4det_surface\": {\"pooled_3class_f1\": ..., \"pooled_binary_f1\": ..., \"pooled_binary_ci\": [...]},\n  \"7feature_ours\": {\"pooled_3class_f1\": ..., \"pooled_binary_f1\": ..., \"pooled_binary_ci\": [...]}\n}\n```\n\n**打印完整表格 + 明确回答：4det_surface pooled binary F1 是否 > 0.694？**",
  "tool_groups": "['ssh']"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_a189a3add89efad7437b5c9f3e05fbf3",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "code:fix-baselines-pooled-metrics",
    "project": "gen-depth-fingerprint",
    "task_prompt": "## 任务：修正 baselines 度量为 pooled LOGO F1（统一口径）\n\n**最高优先级。**\n\n**服务器**：autodl-5090\n**GPU**：cuda:0（可能需要重跑 baseline 推理）\n**环境激活**：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`\n**项目路径**：/root/gen-depth-fingerprint/\n\n### 背景\n\n当前 `8gen_baselines.json` 的 point estimate 是 per-gen macro average，但论文需要 **pooled LOGO F1**：\n- 把所有 8 fold 的 held-out predictions pool 到一起\n- 在 pooled predictions 上计算 macro F1\n- 与我们的 7-feature 结果 (0.762/0.694) 同口径\n\n### 需要的输出\n\n对每个 baseline 计算：\n1. `pooled_3class_f1`: 所有 held-out predictions 合并后的 3-class macro F1\n2. `pooled_binary_f1`: 合并后 gen-1 vs gen-2+ 的 macro F1\n3. `pooled_binary_ci`: bootstrap 95% CI（document-level resampling, n=1000）\n\n### 方法\n\n1. 找到之前 baselines 脚本（计算 8gen_baselines.json 的脚本）：\n```bash\nls /root/gen-depth-fingerprint/*baseline* /root/gen-depth-fingerprint/compute_8gen* 2>/dev/null\n```\n\n2. 关键：需要保存每个 fold 的 held-out predictions（而不仅仅是 F1 分数）。如果之前脚本没保存 predictions，需要重跑 LOGO 并保存 predictions。\n\n3. 重跑 LOGO baseline evaluation：\n   - 对每个 baseline score，8-gen LOGO（hold out 1 generator, train on 7）\n   - XGBoost: n_estimators=100, max_depth=3（单特征 baseline 配置）\n   - 保存每个 fold 的 (y_true, y_pred) predictions\n   - Pool 所有 8 folds 的 predictions\n   - 计算 pooled macro F1（3-class, binary）\n   - Bootstrap CI on pooled predictions\n\n4. 同时重跑 ensemble 配置：\n   - 4-det ensemble: 4 scores as features, XGBoost 100/3\n   - 4-det + surface: 4 scores + ttr + hapax_ratio, XGBoost 100/3\n   - 7-feature (ours): 7 features, XGBoost **200/6**（论文配置！不是 100/3）\n\n5. **关键检查**：4det_surface 的 pooled binary F1 是否 > 0.694（我们的 7-feature）？\n\n### 数据位置\n\n- 原 6-gen features + baseline scores: `/root/gen-depth-fingerprint/data/features_all_models.csv`\n  - 检查是否包含 avg_logprob, fastdetectgpt, binoculars, ld_score 列\n- 新 Llama/Mistral: features_pythia410m.jsonl（有 7 features，但可能没有 baseline detection scores）\n\n如果新 generators 缺少 detection scores：\n- avg_logprob: 可以从 entropy_mean 近似（= -avg_logprob），或从 features 中现有 NLL 数据计算\n- fastdetectgpt/binoculars/ld_score: 需要从脚本中确认如何计算\n\n**检查现有代码了解 baseline scores 的来源，然后决定是重新计算还是有近似方法。**\n\n### 输出\n\n覆盖 `/root/gen-depth-fingerprint/results/8gen_baselines.json`:\n```json\n{\n  \"avg_logprob\": {\"pooled_3class_f1\": ..., \"pooled_binary_f1\": ..., \"pooled_binary_ci\": [lower, upper]},\n  \"fastdetectgpt\": {...},\n  \"ld_score\": {...},\n  \"binoculars\": {...},\n  \"4det_ensemble\": {\"pooled_3class_f1\": ..., \"pooled_binary_f1\": ..., \"pooled_binary_ci\": [...]},\n  \"4det_surface\": {\"pooled_3class_f1\": ..., \"pooled_binary_f1\": ..., \"pooled_binary_ci\": [...]},\n  \"7feature_ours\": {\"pooled_3class_f1\": ..., \"pooled_binary_f1\": ..., \"pooled_binary_ci\": [...]}\n}\n```\n\n**打印完整表格 + 明确回答：4det_surface pooled binary F1 是否 > 0.694？**",
    "tool_groups": "['ssh']"
  }
}
````

</details>

---


### Tool result

_source line 1188 · 2026-05-16T13:59:21.470349+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_code_fix-baselines-pooled-metrics_20260516T135916\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/logs/workers/worker_code_fix-baselines-pooled-metrics_20260516T135916.log\", \"setup_data\": {}, \"message\": \"Worker worker_code_fix-baselines-pooled-metrics_20260516T135916 started. Use get_worker_status('worker_code_fix-baselines-pooled-metrics_20260516T135916') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_a189a3add89efad7437b5c9f3e05fbf3",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 5570
}
```

</details>

---


## Round 107

## Round 107

2 recorded events


### User

_source line 1189 · 2026-05-16T13:59:47.246069+00:00_

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
  "session": "feishu:group:oc_a189a3add89efad7437b5c9f3e05fbf3",
  "source": "system:ralph_loop"
}
```

</details>

---


### Assistant

_source line 1190 · 2026-05-16T14:00:32.454742+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- 服务器 autodl-5090 GPU 白名单：cuda:0/1/2/3（全部已分配本项目）
- tail_decay 公式必须是 **log-prob slope**（排序 avg log-prob rank 100-1000 线性回归斜率，值域 ≈ -0.002）。绝对不能用旧公式（NLL proportion，值为正数 ~0.098）
- `8gen_logo_results_BUGGY_DO_NOT_USE.json` 已标记废弃，**永远不要引用此文件**。正确结果在 `8gen_logo_unfiltered.json`
- D038 定稿：main results = 8 generators / 5 families / 全部 rp=1.0 / unfiltered。Gemma rp=1.1 仅进 appendix
- 论文数字唯一真源：`8gen_logo_unfiltered.json`（binary=0.694, 3-class=0.762, Mistral=0.633）

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090，工作目录 `/root/gen-depth-fingerprint/`
- Python：`/root/miniconda3/bin/python`，激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型缓存：`/root/autodl-tmp/models/`（Gemma, Llama via ModelScope, Qwen3-0.6B-Base）
- Reference model: Pythia-410M (`EleutherAI/pythia-410m`), 自动从 HF 下载
- 数据目录：`/root/gen-depth-fingerprint/data/{generator_name}/`
- 原 6-gen 特征：`/root/gen-depth-fingerprint/data/features_all_models.csv`（27529 条，含 baseline detection scores 列）
- 新 gen 特征：`data/{llama-3.2-3b,mistral-7b-v0.3}/features_pythia410m.jsonl`
- 结果目录：`/root/gen-depth-fingerprint/results/`
- 活跃进程：Gemma rp=1.1 生成（PID 305925, cuda:1, ~20% 完成，ETA ~UTC 16:00）
- Cron：`plan-016-gemma2-2b-rp11` 监控中

### 3. 📊 当前状态
**正在等待两个 Worker 回调**：
1. `worker_ops_verify-baseline-ci_20260516T135801` — 检查 CI 异常（已被后续任务 supersede）
2. `worker_code_fix-baselines-pooled-metrics_20260516T135916` — **关键**：重算 baselines 为 pooled LOGO F1（统一口径），Director 等这个结果决定论文措辞（4det_surface binary F1 是否 > 0.694）

**Registry RUNNING**：仅 `plan-016-gemma2-2b-rp11`（Gemma rp=1.1 生成，diagnostic/appendix 用）

**已完成的 8-gen artifacts**：
- `8gen_logo_unfiltered.json` ✓（主结果）
- `8gen_lofo_family.json` ✓（5-family LOFO）
- `8gen_feature_ablation.json` ✓（surface/reference/full ablation）
- `8gen_pooled_rho.json` ✓（Spearman correlations）
- `8gen_per_gen_spearman.json` ✓
- `8gen_baselines.json` ← **正在被重算覆盖**（pooled 口径修正）

### 4. 📋 待办（条件触发式）
- `worker_code_fix-baselines-pooled-metrics` 完成 → 汇报 Director pooled baselines 数字 + 明确回答"4det_surface > 0.694?"
- Gemma rp=1.1 cron 回调（进程退出）→ spawn Worker 确认完成 → filter+extract → 单独 held-out eval → 写 appendix cross-rp analysis
- Director 确认 baselines 数字后 → Paper Agent 更新 Table 2（baselines comparison table）
- 如果 4det_surface pooled binary > 0.694 → 论文措辞需从 "outperforms all baselines" 改为 "comparable to multi-detector ensemble"（D038 已预见此可能）

### 5. 🎯 战略上下文
- **DDL**: EMNLP 2026 ARR 2026-05-25（9 天）
- **D038 定稿配置**：8 gen / 5 family / rp=1.0 / unfiltered / tail_decay=slope
- **rp-LOFO gate FAILED**（Llama rp=1.1 binary=0.582 << 0.70）→ rp=1.0 和 rp=1.1 不可混合，Gemma rp=1.1 不进 main results
- **退化率高**：原 6-gen 也有 30-45% soft degeneration。论文 unfiltered 含 repetitive easy cases（filtered 后 F1 降 6-8pp）。这是 feature not bug — unfiltered 是 fair evaluation，filtered 放 appendix 作 robustness
- **易错点**：
  1. baselines 的 XGBoost 配置是 100/3（单特征防过拟合），7-feature ensemble 是 200/6。两者不能用相同配置
  2. `features_all_models.csv` 已包含 baseline detection scores (avg_logprob, fastdetectgpt, binoculars, ld_score 列)，但新 Llama/Mistral 的 JSONL 没有这些列 — baselines 需要对新 gen 做推理
  3. Gemma rp=1.0 几乎全退化（98% at depth≥1），不可用于 main results classification
  4. prompt_type_results.json 是 elaboration/rewriting 数字源，plan006_paraphrastic_comparison.json 是 paraphrastic 数字源 — 两者独立实验，continuation 数值略有差异
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_a189a3add89efad7437b5c9f3e05fbf3"
}
```

</details>

---
