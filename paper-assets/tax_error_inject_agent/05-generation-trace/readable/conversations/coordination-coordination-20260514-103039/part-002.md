# Project coordination (archived snapshot) — Part 2 of 2

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../coordination-coordination-20260514-103039.md) · [Structured JSON](../../../sessions/a5/a5b5d6230544677b3ea5.json)

## Round 46

### Tool result

_source line 471 · 2026-05-14T10:29:36.824797+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_research_related-work-table_20260514T101016\", \"status\": \"done\", \"task_type\": \"research:related-work-table\", \"project\": \"tax_error_inject_agent\", \"started_at\": \"2026-05-14T10:10:16.357849+00:00\", \"ended_at\": \"2026-05-14T10:12:17.949623+00:00\", \"setup\": null, \"teardown\": null, \"setup_data\": {}, \"result\": {\"raw\": \"文件已写入 `/root/autodl-tmp/tax_error_inject_agent/docs/related_work_comparison.md`（63 行）。\\n\\n核心对比结论：\\n- **PALADIN** 只覆盖 tool error，TaxEI 将注入式训练扩展到 planning + context error\\n- **Agent-R / ETO** 依赖自然产生的错误，TaxEI 用 taxonomy 系统化控制注入\\n- **Reflexion / AgentRefine** 的 recovery 信号来自 LLM 自省，TaxEI 的 recovery 来自真实环境反馈\\n- **ReAct** 是纯 prompt baseline，无 error training\\n\\n所有信息已通过 WebSearch 交叉验证，无 [TBD] 标注。\"}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_d7cea5c11b07b354fd76b1095848e014",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 472 · 2026-05-14T10:29:41.291295+00:00_

called mcp__agent-ml-research__get_worker_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status</summary>

```json
{
  "worker_id": "worker_exp_mini-pipeline-e2e_20260514T094954",
  "verbose": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_d7cea5c11b07b354fd76b1095848e014",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "tool_args": {
    "worker_id": "worker_exp_mini-pipeline-e2e_20260514T094954",
    "verbose": "True"
  }
}
```

</details>

---


### Tool result

_source line 473 · 2026-05-14T10:29:41.341880+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_exp_mini-pipeline-e2e_20260514T094954\", \"status\": \"running\", \"task_type\": \"exp:mini-pipeline-e2e\", \"project\": \"tax_error_inject_agent\", \"started_at\": \"2026-05-14T09:49:54.761511+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}, \"progress\": {\"recent_tools\": [\"ssh_read_only\", \"ssh_read_only\", \"Bash\", \"ssh_read_only\", \"ssh_read_only\"], \"last_text\": \"TaxEI 155/195 (79%), ~3.3 min left. Waiting.\", \"turn_count\": 19}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_d7cea5c11b07b354fd76b1095848e014",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 474 · 2026-05-14T10:29:46.345762+00:00_

Mini-pipeline Worker 进展顺利——已进入 SFT 训练阶段（TaxEI 155/195 steps，约 79%）。等 callback。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_d7cea5c11b07b354fd76b1095848e014"
}
```

</details>

---


## Round 47

## Round 47

2 recorded events


### User

_source line 475 · 2026-05-14T10:29:56.720240+00:00_

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
  "session": "feishu:group:oc_d7cea5c11b07b354fd76b1095848e014",
  "source": "system:ralph_loop"
}
```

</details>

---


### Assistant

_source line 476 · 2026-05-14T10:30:39.992349+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- GPU 白名单：autodl-5090:cuda:0/1/2/3，不可用其他设备
- ms-swift 4.2.0 **不支持 `--config &lt;yaml>`**，正式训练必须用命令行参数传入
- eval 必须用 `--task_list eval/eval_tasks_47.json`（固化的 47 任务子集），否则与 baseline 不可比
- Qwen3 `enable_thinking=False`，训练数据用纯文本 `&lt;think>` 标签，不是原生 thinking mode
- 模型路径是 `/root/autodl-tmp/models/Qwen/Qwen3-8B`（注意 Qwen/ 子目录），之前 registry 写错过
- formatter.py 有 DRY_RUN / API_ERROR 安全检查，dry_run 数据不能混入正式训练

### 2. 🖥️ 基础设施快照
- **服务器**：autodl-5090，工作目录 `/root/autodl-tmp/tax_error_inject_agent/`
- **Python**：conda base，激活命令 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **PyTorch**：2.10.0+cu128，CUDA 12.8，4×RTX 5090 32GB
- **模型**：Qwen3-8B `/root/autodl-tmp/models/Qwen/Qwen3-8B/`，Qwen3-32B-AWQ `/root/autodl-tmp/models/Qwen/Qwen3-32B-AWQ/`（fallback teacher）
- **API**：base_url `http://47.94.22.126/v1`，模型 `openai/gpt-5.2`，key 通过 `request_secret("openrouter_api_key")` 或 .env
- **活跃进程**：traj_collect_500 PID 11045（轨迹收集，cron 监控中，~242/500 成功）
- **活跃 Worker**：`worker_exp_mini-pipeline-e2e_20260514T094954`（正在跑 SFT 训练阶段，TaxEI 155/195 steps）

### 3. 📊 当前状态
**刚完成**：所有代码修复（注入格式兼容、injection_detected 删除、API auth retry、recovery 失败处理、formatter 安全检查、eval 任务列表固化、SFT gradient_checkpointing OOM 修复、related work 对比表）。

**正在跑**：
- `mini-pipeline-e2e` Worker：用 ~242 条轨迹跑完整非 dry_run pipeline（注入→recovery→SFT→eval）。最新进度：TaxEI SFT 训练 155/195 steps (~79%)，接下来是 eval
- `traj_collect_500`：PID 11045，~242/500 成功轨迹，预计还需 ~2-3h

**Registry**：
- `traj_collect_500` — RUNNING，轨迹收集
- `vanilla-react-baseline` — DONE (success)，42.6% (20/47)
- `sft-dryrun-73` — DONE (success)，pipeline 验证

**等待中**：mini-pipeline Worker callback → 汇报 TaxEI vs vanilla 信号方向给 Director

### 4. 📋 待办
- mini-pipeline Worker 回调 → 分析 TaxEI vs vanilla clean SR + recovery rate，更新 registry，汇报 Director（含 [资源] 行）
- traj_collect_500 cron 回调（PID 11045 退出）→ 检查最终成功条数，若 ≥400 条立即启动正式 800 条 recovery generation + 正式 SFT 训练
- 正式 recovery generation 完成 → 格式化 SFT 数据（确认 wc -l + md5 不同）→ 并行训练 TaxEI-SFT (cuda:0) + vanilla-SFT (cuda:2)
- 正式训练完成 → eval with `--task_list eval/eval_tasks_47.json`，clean + inject 两轮，McNemar 统计检验
- Director 要求写论文 → 先 Read red-section skill，related work 对比表已就绪在 `docs/related_work_comparison.md`

### 5. 🎯 战略上下文
- **核心假设**：taxonomy-guided error injection 对 planning/context errors 提供超越 vanilla SFT 的恢复训练信号。Pass/Fail：TaxEI-SFT recovery rate ≥ vanilla-SFT + 5pp (McNemar p<0.05)
- **valid_unseen 只有 47 个任务**（非 ROADMAP 原写的 134），McNemar 统计效力受限
- **pick_cool_then_place 是 zero-shot 盲区**（0/7），TaxEI 在此类型最有可能体现差异
- **易踩坑**：formatter.py 输出看起来正确但内容可能相同（之前两个文件 md5 一样的教训），每次生成 SFT 数据后必须 wc -l + md5sum 验证
- **GPT-5.2 成功率 ~78%**（低于预期 93%），500 条需要 ~643 episodes
- **ms-swift 参数坑多**：参数名可能与 yaml key 不一致，首次用新参数先 `swift sft --help` 确认
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_d7cea5c11b07b354fd76b1095848e014"
}
```

</details>

---
