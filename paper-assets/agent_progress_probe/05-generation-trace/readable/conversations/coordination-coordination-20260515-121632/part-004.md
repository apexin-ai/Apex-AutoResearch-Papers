# Project coordination (archived snapshot) — Part 4 of 4

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Conversation logs

[← Part 3](part-003.md) · [Transcript overview](../coordination-coordination-20260515-121632.md) · [Structured JSON](../../../sessions/55/557711ce4f09dabadfb4.json)

## Round 124

### Tool call

_source line 1827 · 2026-05-15T12:15:16.501416+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

````json
{
  "task_type": "experiment:gold-3annotator-eval",
  "project": "agent_progress_probe",
  "task_prompt": "## 任务：用 3 个 gold set 子集（A/B/C）分别跑评估 + bootstrap\n\n### 背景\n3 位标注者的 gold set 已构建。需要跑 3 组评估：\n- Set A: 3-annotator MV (N=52) — 最严格但太小\n- Set B: ≥2-annotator agreed (N=505) — 论文首选\n- Set C: All available incl single-annotator (N=512) — robustness\n\n### 服务器信息\n- 服务器：bjb2-23165\n- 项目路径：`/root/autodl-tmp/agent_progress_probe/`\n- OH 轨迹：`/root/autodl-tmp/openhands_data/openhands_trajectories.jsonl`\n- Python：conda base（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）\n\n### Step 1：上传 3 个 gold CSV\n\n读取本地文件并通过 ssh_execute 写入服务器：\n\n1. `/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/gold_set/gold_3annotator_A.csv`\n   → 服务器 `/root/autodl-tmp/agent_progress_probe/artifacts/gold_set/gold_3annotator_A.csv`\n\n2. `/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/gold_set/gold_2plus_agreed_B.csv`\n   → 服务器 `/root/autodl-tmp/agent_progress_probe/artifacts/gold_set/gold_2plus_agreed_B.csv`\n\n3. `/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/gold_set/gold_all_available_C.csv`\n   → 服务器 `/root/autodl-tmp/agent_progress_probe/artifacts/gold_set/gold_all_available_C.csv`\n\n### Step 2：验证脚本修复\n\n确认两个脚本已包含所有修复（canonical hyperparams + gold exclusion + OH trajectories）：\n```bash\ncd /root/autodl-tmp/agent_progress_probe\ngrep -c \"gold_noabs\" evaluate_gold_set.py gold_bootstrap_ci.py\ngrep -c \"openhands\\|oh_traj\" evaluate_gold_set.py gold_bootstrap_ci.py\ngrep \"learning_rate\\|n_estimators\" evaluate_gold_set.py gold_bootstrap_ci.py | head -6\n```\n\n### Step 3：跑 3 组评估\n\n对每个 set 依次运行 evaluate + bootstrap：\n\n```bash\ncd /root/autodl-tmp/agent_progress_probe\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base\n```\n\n**Set A (N=52)**:\n```bash\npython evaluate_gold_set.py \\\n  --gold_csv artifacts/gold_set/gold_3annotator_A.csv \\\n  --output_dir artifacts/gold_set/eval_setA \\\n  --oh_trajectories /root/autodl-tmp/openhands_data/openhands_trajectories.jsonl \\\n  --device cuda:2 2>&1 | tee /tmp/eval_setA.log\n\npython gold_bootstrap_ci.py \\\n  --gold_csv artifacts/gold_set/gold_3annotator_A.csv \\\n  --oh_trajectories /root/autodl-tmp/openhands_data/openhands_trajectories.jsonl \\\n  --output artifacts/gold_set/bootstrap_setA.json \\\n  --n_bootstrap 10000 --seed 42 \\\n  --device cuda:2 2>&1 | tee /tmp/bootstrap_setA.log\n```\n\n**Set B (N=505)**:\n```bash\npython evaluate_gold_set.py \\\n  --gold_csv artifacts/gold_set/gold_2plus_agreed_B.csv \\\n  --output_dir artifacts/gold_set/eval_setB \\\n  --oh_trajectories /root/autodl-tmp/openhands_data/openhands_trajectories.jsonl \\\n  --device cuda:2 2>&1 | tee /tmp/eval_setB.log\n\npython gold_bootstrap_ci.py \\\n  --gold_csv artifacts/gold_set/gold_2plus_agreed_B.csv \\\n  --oh_trajectories /root/autodl-tmp/openhands_data/openhands_trajectories.jsonl \\\n  --output artifacts/gold_set/bootstrap_setB.json \\\n  --n_bootstrap 10000 --seed 42 \\\n  --device cuda:2 2>&1 | tee /tmp/bootstrap_setB.log\n```\n\n**Set C (N=512)**:\n```bash\npython evaluate_gold_set.py \\\n  --gold_csv artifacts/gold_set/gold_all_available_C.csv \\\n  --output_dir artifacts/gold_set/eval_setC \\\n  --oh_trajectories /root/autodl-tmp/openhands_data/openhands_trajectories.jsonl \\\n  --device cuda:2 2>&1 | tee /tmp/eval_setC.log\n\npython gold_bootstrap_ci.py \\\n  --gold_csv artifacts/gold_set/gold_all_available_C.csv \\\n  --oh_trajectories /root/autodl-tmp/openhands_data/openhands_trajectories.jsonl \\\n  --output artifacts/gold_set/bootstrap_setC.json \\\n  --n_bootstrap 10000 --seed 42 \\\n  --device cuda:2 2>&1 | tee /tmp/bootstrap_setC.log\n```\n\n### Step 4：读取所有结果\n\n```bash\nfor s in A B C; do\n  echo \"=== Set $s ===\"\n  cat artifacts/gold_set/eval_set${s}/results.json\n  echo \"---\"\n  cat artifacts/gold_set/bootstrap_set${s}.json\n  echo \"\"\ndone\n```\n\n### Step 5：验证 eval/bootstrap 一致性\n\n对每个 set，确认 bootstrap 的 GB/RF F1 与 eval 一致（±0.5pp）。\n\n### 产出要求\n\n最终输出必须包含完整的对比表：\n\n1. **per-model macro-F1 跨 4 组**：\n\n| Model | N=195 (old) | Set A (N=52) | Set B (N=505) | Set C (N=512) |\n|-------|-------------|--------------|---------------|---------------|\n| GB    | 0.764       | ?            | ?             | ?             |\n| RF    | 0.752       | ?            | ?             | ?             |\n| MV    | 0.718       | ?            | ?             | ?             |\n| Probe | 0.735       | ?            | ?             | ?             |\n| TWV   | 0.768       | ?            | ?             | ?             |\n\n2. **bootstrap p-values 跨 3 组**：\n\n| Test | Set A p | Set B p | Set C p |\n|------|---------|---------|---------|\n| GB vs MV | ? | ? | ? |\n| GB vs Probe | ? | ? | ? |\n| RF vs GB | ? | ? | ? |\n\n3. **每个 set 的匹配 N**（gold windows 中多少成功匹配到 non_abstain）\n4. **eval vs bootstrap 一致性确认**\n",
  "tool_groups": "['ssh', 'knowledge']"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_7a45a04b9175db9d7ef3c837fd6c6630",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "experiment:gold-3annotator-eval",
    "project": "agent_progress_probe",
    "task_prompt": "## 任务：用 3 个 gold set 子集（A/B/C）分别跑评估 + bootstrap\n\n### 背景\n3 位标注者的 gold set 已构建。需要跑 3 组评估：\n- Set A: 3-annotator MV (N=52) — 最严格但太小\n- Set B: ≥2-annotator agreed (N=505) — 论文首选\n- Set C: All available incl single-annotator (N=512) — robustness\n\n### 服务器信息\n- 服务器：bjb2-23165\n- 项目路径：`/root/autodl-tmp/agent_progress_probe/`\n- OH 轨迹：`/root/autodl-tmp/openhands_data/openhands_trajectories.jsonl`\n- Python：conda base（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）\n\n### Step 1：上传 3 个 gold CSV\n\n读取本地文件并通过 ssh_execute 写入服务器：\n\n1. `/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/gold_set/gold_3annotator_A.csv`\n   → 服务器 `/root/autodl-tmp/agent_progress_probe/artifacts/gold_set/gold_3annotator_A.csv`\n\n2. `/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/gold_set/gold_2plus_agreed_B.csv`\n   → 服务器 `/root/autodl-tmp/agent_progress_probe/artifacts/gold_set/gold_2plus_agreed_B.csv`\n\n3. `/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/artifacts/gold_set/gold_all_available_C.csv`\n   → 服务器 `/root/autodl-tmp/agent_progress_probe/artifacts/gold_set/gold_all_available_C.csv`\n\n### Step 2：验证脚本修复\n\n确认两个脚本已包含所有修复（canonical hyperparams + gold exclusion + OH trajectories）：\n```bash\ncd /root/autodl-tmp/agent_progress_probe\ngrep -c \"gold_noabs\" evaluate_gold_set.py gold_bootstrap_ci.py\ngrep -c \"openhands\\|oh_traj\" evaluate_gold_set.py gold_bootstrap_ci.py\ngrep \"learning_rate\\|n_estimators\" evaluate_gold_set.py gold_bootstrap_ci.py | head -6\n```\n\n### Step 3：跑 3 组评估\n\n对每个 set 依次运行 evaluate + bootstrap：\n\n```bash\ncd /root/autodl-tmp/agent_progress_probe\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base\n```\n\n**Set A (N=52)**:\n```bash\npython evaluate_gold_set.py \\\n  --gold_csv artifacts/gold_set/gold_3annotator_A.csv \\\n  --output_dir artifacts/gold_set/eval_setA \\\n  --oh_trajectories /root/autodl-tmp/openhands_data/openhands_trajectories.jsonl \\\n  --device cuda:2 2>&1 | tee /tmp/eval_setA.log\n\npython gold_bootstrap_ci.py \\\n  --gold_csv artifacts/gold_set/gold_3annotator_A.csv \\\n  --oh_trajectories /root/autodl-tmp/openhands_data/openhands_trajectories.jsonl \\\n  --output artifacts/gold_set/bootstrap_setA.json \\\n  --n_bootstrap 10000 --seed 42 \\\n  --device cuda:2 2>&1 | tee /tmp/bootstrap_setA.log\n```\n\n**Set B (N=505)**:\n```bash\npython evaluate_gold_set.py \\\n  --gold_csv artifacts/gold_set/gold_2plus_agreed_B.csv \\\n  --output_dir artifacts/gold_set/eval_setB \\\n  --oh_trajectories /root/autodl-tmp/openhands_data/openhands_trajectories.jsonl \\\n  --device cuda:2 2>&1 | tee /tmp/eval_setB.log\n\npython gold_bootstrap_ci.py \\\n  --gold_csv artifacts/gold_set/gold_2plus_agreed_B.csv \\\n  --oh_trajectories /root/autodl-tmp/openhands_data/openhands_trajectories.jsonl \\\n  --output artifacts/gold_set/bootstrap_setB.json \\\n  --n_bootstrap 10000 --seed 42 \\\n  --device cuda:2 2>&1 | tee /tmp/bootstrap_setB.log\n```\n\n**Set C (N=512)**:\n```bash\npython evaluate_gold_set.py \\\n  --gold_csv artifacts/gold_set/gold_all_available_C.csv \\\n  --output_dir artifacts/gold_set/eval_setC \\\n  --oh_trajectories /root/autodl-tmp/openhands_data/openhands_trajectories.jsonl \\\n  --device cuda:2 2>&1 | tee /tmp/eval_setC.log\n\npython gold_bootstrap_ci.py \\\n  --gold_csv artifacts/gold_set/gold_all_available_C.csv \\\n  --oh_trajectories /root/autodl-tmp/openhands_data/openhands_trajectories.jsonl \\\n  --output artifacts/gold_set/bootstrap_setC.json \\\n  --n_bootstrap 10000 --seed 42 \\\n  --device cuda:2 2>&1 | tee /tmp/bootstrap_setC.log\n```\n\n### Step 4：读取所有结果\n\n```bash\nfor s in A B C; do\n  echo \"=== Set $s ===\"\n  cat artifacts/gold_set/eval_set${s}/results.json\n  echo \"---\"\n  cat artifacts/gold_set/bootstrap_set${s}.json\n  echo \"\"\ndone\n```\n\n### Step 5：验证 eval/bootstrap 一致性\n\n对每个 set，确认 bootstrap 的 GB/RF F1 与 eval 一致（±0.5pp）。\n\n### 产出要求\n\n最终输出必须包含完整的对比表：\n\n1. **per-model macro-F1 跨 4 组**：\n\n| Model | N=195 (old) | Set A (N=52) | Set B (N=505) | Set C (N=512) |\n|-------|-------------|--------------|---------------|---------------|\n| GB    | 0.764       | ?            | ?             | ?             |\n| RF    | 0.752       | ?            | ?             | ?             |\n| MV    | 0.718       | ?            | ?             | ?             |\n| Probe | 0.735       | ?            | ?             | ?             |\n| TWV   | 0.768       | ?            | ?             | ?             |\n\n2. **bootstrap p-values 跨 3 组**：\n\n| Test | Set A p | Set B p | Set C p |\n|------|---------|---------|---------|\n| GB vs MV | ? | ? | ? |\n| GB vs Probe | ? | ? | ? |\n| RF vs GB | ? | ? | ? |\n\n3. **每个 set 的匹配 N**（gold windows 中多少成功匹配到 non_abstain）\n4. **eval vs bootstrap 一致性确认**\n",
    "tool_groups": "['ssh', 'knowledge']"
  }
}
````

</details>

---


### Tool result

_source line 1828 · 2026-05-15T12:15:22.075226+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_experiment_gold-3annotator-eval_20260515T121516\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/logs/workers/worker_experiment_gold-3annotator-eval_20260515T121516.log\", \"setup_data\": {}, \"message\": \"Worker worker_experiment_gold-3annotator-eval_20260515T121516 started. Use get_worker_status('worker_experiment_gold-3annotator-eval_20260515T121516') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_7a45a04b9175db9d7ef3c837fd6c6630",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 5573
}
```

</details>

---


### Tool call

_source line 1829 · 2026-05-15T12:15:42.705853+00:00_

called mcp__agent-ml-research__main_agent_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__main_agent_post_to_director</summary>

```json
{
  "text": "[资源] GPU 分配 1 (cuda:2) / 实际跑 0 | Worker 池 2 (GPU 0 / CPU 2)\n\n## 3-Annotator IAA + Gold Set 评估进行中\n\n### IAA 结果\n\n**覆盖统计**：\n- 3-annotator: **52** windows（太小，不足以做论文主表）\n- 2-annotator: **591** windows\n- 1-annotator: **7** windows\n\n**Per-batch stagnation rates（揭示标注者偏差）**：\n- B1: 40.1% stag — 最倾向 stagnation\n- B3: 34.7% stag\n- B2: 19.5% stag — 强 progress 偏差\n\n**3-annotator IAA (N=52)**：\n\n| 指标 | 值 |\n|---|---|\n| Fleiss' κ | **0.390** (fair) |\n| B1 vs B2 κ | 0.485 |\n| B1 vs B3 κ | 0.406 |\n| B2 vs B3 κ | 0.330 |\n| 3/3 unanimous | 63.5% (33/52) |\n| 2:1 majority | 36.5% (19/52) |\n\n**2-annotator agreement**: 453/591 agree (76.6%), 138/591 disagree (23.4%)\n\n**Source effect**: SWE unanimous rate 59.5% vs OH 73.3%\n\n### Gold Set 构建\n\n| Set | 构成 | N | prog | stag |\n|---|---|---|---|---|\n| **A** | 3-annotator MV | 52 | 40 | 12 |\n| **B** | ≥2 agreed | 505 | 372 | 133 |\n| **C** | All available | 512 | 376 | 136 |\n\n⚠️ **Set A 太小（N=52）**，bootstrap CI 会很宽。建议论文用 **Set B（N=505）** 作为主表。\n\n### 已派发\nWorker `gold-3annotator-eval` 正在 bjb2-23165 上跑 A/B/C 三组 evaluate + bootstrap（共 6 次运行）。",
  "project": "agent_progress_probe"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_7a45a04b9175db9d7ef3c837fd6c6630",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "tool_args": {
    "text": "[资源] GPU 分配 1 (cuda:2) / 实际跑 0 | Worker 池 2 (GPU 0 / CPU 2)\n\n## 3-Annotator IAA + Gold Set 评估进行中\n\n### IAA 结果\n\n**覆盖统计**：\n- 3-annotator: **52** windows（太小，不足以做论文主表）\n- 2-annotator: **591** windows\n- 1-annotator: **7** windows\n\n**Per-batch stagnation rates（揭示标注者偏差）**：\n- B1: 40.1% stag — 最倾向 stagnation\n- B3: 34.7% stag\n- B2: 19.5% stag — 强 progress 偏差\n\n**3-annotator IAA (N=52)**：\n\n| 指标 | 值 |\n|---|---|\n| Fleiss' κ | **0.390** (fair) |\n| B1 vs B2 κ | 0.485 |\n| B1 vs B3 κ | 0.406 |\n| B2 vs B3 κ | 0.330 |\n| 3/3 unanimous | 63.5% (33/52) |\n| 2:1 majority | 36.5% (19/52) |\n\n**2-annotator agreement**: 453/591 agree (76.6%), 138/591 disagree (23.4%)\n\n**Source effect**: SWE unanimous rate 59.5% vs OH 73.3%\n\n### Gold Set 构建\n\n| Set | 构成 | N | prog | stag |\n|---|---|---|---|---|\n| **A** | 3-annotator MV | 52 | 40 | 12 |\n| **B** | ≥2 agreed | 505 | 372 | 133 |\n| **C** | All available | 512 | 376 | 136 |\n\n⚠️ **Set A 太小（N=52）**，bootstrap CI 会很宽。建议论文用 **Set B（N=505）** 作为主表。\n\n### 已派发\nWorker `gold-3annotator-eval` 正在 bjb2-23165 上跑 A/B/C 三组 evaluate + bootstrap（共 6 次运行）。",
    "project": "agent_progress_probe"
  }
}
```

</details>

---


### Tool result

_source line 1830 · 2026-05-15T12:15:43.910845+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_63420dd00d01b9171927f4964f580182:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_7a45a04b9175db9d7ef3c837fd6c6630",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "elapsed_ms": 1204
}
```

</details>

---


### Assistant

_source line 1831 · 2026-05-15T12:15:45.895347+00:00_

3-annotator 覆盖只有 52 个 windows（Set A 太小），Set B（505 windows）是论文实用选项。Fleiss' κ=0.390（fair）。现在派 worker 跑 A/B/C 三组评估。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_7a45a04b9175db9d7ef3c837fd6c6630"
}
```

</details>

---


## Round 125

## Round 125

2 recorded events


### User

_source line 1832 · 2026-05-15T12:15:45.909241+00:00_

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
  "session": "feishu:group:oc_7a45a04b9175db9d7ef3c837fd6c6630",
  "source": "system:ralph_loop"
}
```

</details>

---


### Assistant

_source line 1833 · 2026-05-15T12:16:32.321753+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- 本项目只能用 **cuda:2**（gpu_ids 白名单）
- `evaluate_gold_set.py` 和 `gold_bootstrap_ci.py` 的 canonical 超参数：**GB lr=0.05, n=200, depth=5; RF n=100, depth=10**。任何偏离都会产生不可信数字
- structural 模型训练必须排除 gold windows（`gold_noabs_set` 逻辑），否则数据泄漏
- `gold_bootstrap_ci.py` 必须带 `--oh_trajectories` 参数，否则 OH 窗口特征全零 → F1 膨胀 3.8pp
- windows_labeled.jsonl 无 `source` 字段，用 `"__openhands__" in trajectory_id` 区分 SWE/OH

### 2. 🖥️ 基础设施快照
- 服务器：**bjb2-23165**，工作目录 `/root/autodl-tmp/agent_progress_probe/`
- Python：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- OH 轨迹：`/root/autodl-tmp/openhands_data/openhands_trajectories.jsonl`
- SWE 轨迹：`data/swe_agent_trajectories_5000.jsonl`
- Probe checkpoint：`checkpoints/best_model.pt`（SWE in-domain），`checkpoints_full/best_model.pt`（full train）
- split_info：`checkpoints/split_info.json`（train N=10,634, gold 排除后 10,595）
- 本地产出：`artifacts/gold_set/` 下有 `eval_canonical/`, `bootstrap_ci_ohfix.json`, 多个 gold CSV
- 活跃进程：无 GPU 进程跑。Worker `gold-3annotator-eval` 正在跑 A/B/C 三组 eval+bootstrap（6 次运行）
- 另有 Worker `gold-consensus-results` (fetch) 已完成但其 N=601 结果已被 3-annotator 方案取代

### 3. 📊 当前状态
**正在做**：等待 Worker `worker_experiment_gold-3annotator-eval_20260515T121516` 完成——它在 bjb2-23165 上用 3 个 gold set 子集（A/B/C）分别跑 evaluate_gold_set.py + gold_bootstrap_ci.py，共 6 次运行。

**registry**：
- `gold-set-eval-v1` DONE — metrics 已更新为 canonical+leakage-free 数字（GB=0.764, p=0.012 on N=195）
- 其余 31 实验全 DONE（ROADMAP 31/32）

**等待中**：
- Worker `gold-3annotator-eval` 回调 → 处理 A/B/C 三组结果 → 注册实验 → 汇报 Director
- Director 决策：论文用 Set B (N=505) 还是其他子集
- Batch 3 标注意味着之前 N=195 的数字（GB=0.764, MV=0.718）可能需要全部替换

### 4. 📋 待办
- `gold-3annotator-eval` worker 回调 → 读结果 → 注册 `gold-set-eval-v3-A/B/C` 到 registry → 构建对比表（N=195 vs A vs B vs C）→ 汇报 Director
- Director 确认用哪个 Set → 更新 §6.7 和论文中所有 gold set 数字
- 之前 N=601 (2-annotator consensus) 的结果作废——已被 3-annotator 方案替代，不要引用
- Camera-ready BibTeX 修复仍 pending（ratner2017snorkel year, dawid1979em volume/pages, "and others"）

### 5. 🎯 战略上下文
- **核心结论**：lightweight structural features (30-dim) 足以检测 agent stagnation，跨 agent 迁移（SWE→OH），且显著优于 MV silver labels（p<0.05）
- **3-annotator IAA 偏低**：Fleiss' κ=0.390（fair），B2 标注者系统性倾向 progress（stag rate 仅 19.5% vs B1 40.1%）。3-annotator 覆盖只有 52 windows（Set A 太小），论文几乎必须用 Set B (N=505)
- **易错点**：
  1. 不要用 N=195 或 N=601 的旧数字——最终论文数字取决于 Director 选哪个 Set
  2. eval 和 bootstrap 的 GB/RF F1 必须一致（±0.5pp），如不一致说明 OH 轨迹或数据流有 bug
  3. `evaluate_gold_set.py` 在服务器上的版本可能与本地不同（服务器被多个 worker 修改过），以服务器版本为准
  4. 所有 structural 模型每次评估都重新训练（无 checkpoint），所以超参数和训练数据（含 gold exclusion）直接影响结果
- **EMNLP 2026 ARR 5/25 deadline**，约 10 天。Gold set 数字确定后立即更新论文
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_7a45a04b9175db9d7ef3c837fd6c6630"
}
```

</details>

---
