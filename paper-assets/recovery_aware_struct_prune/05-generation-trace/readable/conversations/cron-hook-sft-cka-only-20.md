# cron hook sft cka only 20

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 58
- **Recorded user turns:** 1
- **Tool calls:** 29
- **Original source:** `logs/chats/cron_hook_sft_cka_only_20.jsonl`
- **Structured JSON:** [`3e422f50bf53ddaa90a3.json`](../../sessions/3e/3e422f50bf53ddaa90a3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

58 recorded events

### User

_source line 1 · 2026-05-17T23:39:30.491542+00:00_

[HANDOFF] 你是 Main Agent，这是 Loop #19。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- westb-23072 SSH 不可达（等用户添加公钥），禁止对 westb 派任何 SSH Worker，会超时浪费
- gpu_ids 白名单：cuda:0-3（两台服务器各自的 0-3），不得越界
- D051 裁定：MATH-500 GRPO vs SFT 对比不可用于 C3 论证（max_new_tokens 配置不公平），只作 supplementary
- CKA-only pruning 用 `--mode rasp --alpha 1` + dummy importance 实现，不是独立 mode
- GRPO 模型必须用 train_grpo_v5.py（含 dapo loss、repetition_penalty、format_reward），不要用旧版本
- ARR May 25 deadline，不得因 "等更多数据" 而拖延 paper draft

### 2. 🖥️ 基础设施快照
- **westb-23072**（root）：工作目录 /root/recovery_aware_struct_prune，模型/数据 /root/autodl-tmp/recovery_aware_struct_prune/。Python: /root/miniconda3/bin/python。**当前 SSH 不可达。**
- **westd-11672**（root）：工作目录 /root/recovery_aware_struct_prune，模型/数据 /root/autodl-tmp/recovery_aware_struct_prune/。Python: /root/miniconda3/bin/python。磁盘 ~312GB 可用。
- W&B project: recovery_aware_struct_prune（run_name = exp_id）
- 预置镜像: aml-train（两台均有）

**活跃进程（9 个 cron 监控中）：**

| exp_id | server | gpu | pid | 内容 |
|--------|--------|-----|-----|------|
| grpo_cka_only_20 | westb | cuda:0 | 725227 | GRPO 100步训练 CKA-only |
| grpo_random_20 | westb | cuda:1 | 719679 | GRPO 100步训练 Random |
| eval_math500_grpo_standard_20 | westd | cuda:1 | 14556 | MATH-500 评测 |
| eval_math500_grpo_rasp_20_v3 | westd | cuda:3 | 31706 | MATH-500 无超时 |
| eval_sft_cka_only_20_n1319 | westd | cuda:0 | 49475 | GSM8K N=1319 |
| eval_postprune_standard_30 | westd | cuda:0 | 47667 | GSM8K N=200 |
| eval_math500_grpo_unpruned | westd | cuda:2 | 64467 | MATH-500 unpruned baseline |
| eval_math500_sft_cka_only_20 | westd | cuda:2 | 65395 | MATH-500 SFT CKA-only |

### 3. 📊 当前状态
- **刚完成**：D056 paper_framing.md 全面改写（Recovery Capacity Gradient 为核心贡献），Paper Agent intro rewrite worker 已完成或结束
- **正在等待**：上述 9 个 cron 回调（westb 2个GRPO训练 + westd 6个eval）
- **eval_postprune_cka_only_30** 状态 DONE(failed)，cron 仍显示 pid=59403 running——可能是新重试进程，需确认
- **Workers**：当前 0 个 running（违反 L1 "Worker 池<2=失职"，但 westb blocked + westd 全在跑 eval，没有可执行的非 GPU 任务除了 paper writing）
- **Paper writing**：D056 framing 定稿后需 framing-reaudit 全文 re-audit，然后继续 draft

### 4. 📋 待办（条件触发式）
- westb SSH 恢复 → 立即读 grpo_cka_only_20 + grpo_random_20 的 step 100 final metrics → 更新 C2 证据表 → 启动 fair GRPO retrain (D051: grpo_rasp_20_fair + grpo_standard_20_fair)
- eval_math500_grpo_standard_20 完成 → 确认 500/500 最终 accuracy → 与 SFT Standard MATH-500 (26%) 对比 → 更新 C1 证据
- eval_math500_grpo_rasp_20_v3 完成 → 同上，与 SFT RASP MATH-500 (24.2%) 对比
- eval_math500_grpo_unpruned 完成 → 确认 unpruned GRPO MATH-500 baseline → C1 cross-benchmark 完整
- eval_math500_sft_cka_only_20 完成 → CKA-only SFT MATH-500 baseline → 如 > 26%(Standard SFT) 则 CKA-only 有 OOD 优势
- eval_sft_cka_only_20_n1319 完成 → 确认 ~63% 收敛 → SFT equalization observation 完整
- 所有 MATH-500 + step 100 数据到齐 → Paper Agent Full Draft → framing-reaudit → 逐章写作
- eval_postprune_cka_only_30 failed → 需诊断原因（可能 OOM 或 sparsity cliff 导致死循环输出）

### 5. 🎯 战略上下文
- **核心结论**：Pruning criterion 决定 RL recovery capacity。梯度: CKA-only > Random > Standard > RASP。机制：gradient importance scoring 移除了 "不重要但 representationally unique" 的结构，破坏 RL 探索多样性。
- **决策链关键节点**：D044(pivot to decoupling) → D053(CKA-only最稳定,逆转预期) → D054(C2升级) → D055(C1收窄为in-distribution) → D056(framing定稿)
- **易错点 1**：不要把 GSM8K decoupling 说成 "GRPO doesn't work"——MATH-500 上 GRPO 确实提升 OOD，decoupling 只是 saturation effect
- **易错点 2**：CKA-only 的 "super-recovery"（frac_zero_std 从 0.35 降到 0.125，低于初始 0.175）是核心 novelty，不要淡化为普通 recovery
- **易错点 3**：D051 裁定 MATH-500 GRPO 数据 config 不公平（max_new_tokens 差异），fair retrain 需要在 westb 上用 identical config 重跑——这被 SSH 阻塞
- **最大风险**：ARR May 25 仅剩 7 天，westb SSH 不通则 step 100 final numbers + fair retrain 都拿不到。如果 SSH 持续阻塞，需要 Director 决策是否用 step 70 数据写论文

## 项目硬约束 (memory.md 节选)

## 决策约束

### D055: C1 收窄为 in-distribution decoupling (2026-05-17)
C1 从 "universal decoupling" 收窄为 in-distribution decoupling。MATH-500 等 cross-benchmark 数据用于界定边界。

### D054: C2 升级为 recovery capacity hierarchy (2026-05-17)
C2 从 "collapse gradient" 升级为 "recovery capacity hierarchy"。

### D053: CKA-only GRPO 最稳定 (provisional)
CKA-only 剪枝的 GRPO 训练最稳定，逆转了原始 hypothesis（预测它最快 collapse）。Redundancy-Stability Tradeoff: 保留冗余结构 = GRPO 更稳定。

### D052: C3 降级为 observation
C2 collapse gradient 升为主力 contribution。

### D051: MATH-500 GRPO 对比不可用于 C3
配置不公平（GRPO max_new_tokens 远大于 SFT 实际使用量），partial results 仅作 supplementary evidence。

### D044: 核心叙事 pivot
从 "RASP enables better RL recovery" pivot 为 "universal decoupling"。Reward 涨但 accuracy 不跟是 universal 现象（unpruned 也是），不是 pruning-specific。

### D049: 维持 C1 双现象
不采纳 "pruning disables GRPO" 叙事。C1 = collapse + decoupling 双现象。

### D050: RASP-RLVR 降级为 ablation
Negative result，不是 core contribution。

## 可查的历史
前 63 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
完整聊天归档可用 `recall_session_history("关键词")` 搜索。

## 第一个动作要求
1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）
2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:sft_cka_only_20",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-17T23:39:42.881145+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__main_agent_post_to_director",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__main_agent_post_to_director",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-17T23:39:42.931939+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-17T23:39:47.148392+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "limit": "0",
  "fields": "['*']",
  "filters": "{'status': 'RUNNING'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "recovery_aware_struct_prune",
    "limit": "0",
    "fields": "['*']",
    "filters": "{'status': 'RUNNING'}"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T23:39:47.148800+00:00_

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
  "session": "cron:hook:sft_cka_only_20",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T23:39:47.703693+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval_math500_sft_cka_only_20\": {\"created_at\": \"2026-05-17T22:59:03.755Z\", \"hypothesis\": \"CKA-only SFT MATH-500 baseline. With SFT Standard=26%, SFT RASP=24.2%, if CKA-only SFT > 26%, CKA-only scoring has OOD advantage. Future comparison with GRPO CKA-only MATH-500 tests C1 decoupling for CKA-only method.\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20\", \"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/math500_sft_cka_only_20.json\", \"data_count\": 500, \"data_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20\", \"eval_data\": \"MATH-500\", \"gpu\": \"cuda:2\", \"model_name\": \"sft_cka_only_20\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"RUNNING\", \"updated_at\": \"2026-05-17T23:20:20.522Z\"}, \"eval_math500_grpo_unpruned\": {\"created_at\": \"2026-05-17T18:14:45.810Z\", \"hypothesis\": \"MATH-500 accuracy for unpruned GRPO v2 (step-100). Establishes MATH-500 baseline: if unpruned post-GRPO ≈ 73.6% (pre-GRPO), confirms decoupling pattern holds on harder benchmark. If higher, GRPO genuinely helps unpruned but not pruned = pruning-specific failure.\", \"parent\": \"eval_math500_unpruned\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"grpo_unpruned_v2\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_v2/ --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_unpruned.json\\\"\", \"data_count\": 500, \"data_path\": \"MATH-500\", \"eval_data\": \"MATH-500 (500 problems, max_new_tokens=4096)\", \"gpu\": [\"cuda:2\"], \"log_pa
…[truncated 7508 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 555
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T23:39:48.006892+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "file": "report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "recovery_aware_struct_prune",
    "file": "report.md"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-17T23:39:48.007330+00:00_

called mcp__agent-ml-research__read_roadmap

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap</summary>

```json
{
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-17T23:40:12.682523+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 9, \"results\": [{\"exp_id\": \"eval_math500_grpo_standard_20\", \"success\": true, \"actions\": [\"Job still running (pid=14556)\"]}, {\"exp_id\": \"grpo_random_20\", \"success\": true, \"actions\": [\"Job still running (pid=719679)\"]}, {\"exp_id\": \"grpo_cka_only_20\", \"success\": true, \"actions\": [\"Job still running (pid=725227)\"]}, {\"exp_id\": \"eval_math500_grpo_rasp_20_v3\", \"success\": true, \"actions\": [\"Job still running (pid=31706)\"]}, {\"exp_id\": \"eval_sft_cka_only_20_n1319\", \"success\": true, \"actions\": [\"Job still running (pid=49475)\"]}, {\"exp_id\": \"eval_postprune_cka_only_30\", \"success\": true, \"actions\": [\"Job still running (pid=59403)\"]}, {\"exp_id\": \"eval_postprune_standard_30\", \"success\": true, \"actions\": [\"Job still running (pid=47667)\"]}, {\"exp_id\": \"eval_math500_grpo_unpruned\", \"success\": true, \"actions\": [\"Job still running (pid=64467)\"]}, {\"exp_id\": \"eval_math500_sft_cka_only_20\", \"success\": true, \"actions\": [\"Job still running (pid=65395)\"]}]}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 25533
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T23:40:12.683346+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/report.md\", \"content\": \"# Handover — 2026-05-17\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| eval_math500_sft_cka_only_20 | CKA-only SFT MATH-500 baseline. With SFT Standard=26%, SFT RASP=24.2%, if CKA-only SFT > 26%, CKA-only scoring has OOD advantage. Future comparison with GRPO CKA-only MATH-500 tests C1 decoupling for CKA-only method. | — | — | — |\\n| eval_sft_cka_only_20_n1319 | CKA-only 20% post-SFT GSM8K N=1319. Post-prune 38.5% highest among all scoring methods. If post-SFT also highest, CKA-only has SFT advantage. If converges to ~60%, confirms SFT equalizes all scoring methods. N=200 pilot showed 64.0%. | — | — | — |\\n| eval_postprune_standard_30 | Standard 30% post-prune GSM8K accuracy (N=200). At 20% Standard post-prune was 17.5%, at 25% was ~15%. 30% should show further degradation. Compared with RASP 30% post-prune (running) to verify RASP advantage persists at higher sparsity. Extends multi-sparsity degradation curve. | — | — | — |\\n\\n## 待处理\\n- eval_math500_grpo_unpruned: MATH-500 accuracy for unpruned GRPO v2 (step-100). Establishes MATH-500 baseline: if unpruned post-GRPO ≈ 73.6% (pre-GRPO), confirms decoupling pattern holds on harder benchmark. If higher, GRPO genuinely helps unpruned but not pruned = pruning-specific failure.（等待人工审批）\\n- eval_math500_sft_rasp_25: MATH-500 accuracy for RASP 25% post-SFT. Extends MATH-500 cross-benchmark data to 25% sparsity. If MATH-500 recovery rate at 25% &lt; 20% (RASP 20% SFT = 24.2%), confirms sparsity gradient on harder benchmark. Parent: sft_rasp_25.（准备中）\\n- eval_humaneval_sft_standard_20_2048: HumanEval pass@1 for SFT Standard 20% with max_new_tokens=2048. Completes 5-way HumanEval@2048 matrix. Compares SFT Standard vs SFT RASP (10.37%) code generation after recovery. Que
…[truncated 4578 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 24676
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-17T23:40:12.734236+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/ROADMAP.md\", \"content\": \"# recovery_aware_struct_prune — Research Dashboard\\n\\n> 最后更新: 2026-05-17 23:27 UTC | 更新原因: D056 framing rewrite + westb SSH blocker + current status refresh\\n\\n## 核心方向\\nPruning criterion determines RL recovery capacity: CKA-only (representational diversity preservation) enables active super-recovery, gradient-based scoring destroys it. 4-method gradient as main contribution. 详见 paper_framing.md (D056 全面改写)。\\n\\n## 当前进展\\n**Research Phase — Framing Finalized (D056)**\\n- Core 20% data: ✅ 4-method GRPO dynamics complete (step 70 confirmed, step 100 data on westb pending SSH fix)\\n- C1 (in-distribution saturation): 等 MATH-500 final results 确认\\n- C2 (recovery capacity gradient): step 70 数据已充分支撑，等 step 100 final numbers\\n- 30% sparsity cliff: RASP 0%, Standard 3% (interim), CKA-only 0% — universal\\n- Inference speedup: RASP 37.8% vs Standard 7.7% confirmed\\n- SFT equalization: all methods converge 59-64% (not significant)\\n- Paper writing: Paper Agent active (intro rewrite worker running)\\n- **阻塞**: westb SSH unreachable — 无法读 GRPO final data、无法启动 fair retrain\\n\\n## 近期任务\\n- [ ] 修复 westb SSH 连接（等用户添加公钥）\\n- [ ] 读取 GRPO 100-step final dynamics (grpo_cka_only_20 + grpo_random_20) on westb\\n- [ ] 启动 fair GRPO retrain: grpo_rasp_20_fair + grpo_standard_20_fair on westb (D051 fix)\\n- [ ] 确认 eval_sft_cka_only_20_n1319 最终结果\\n- [ ] 确认 eval_math500_grpo_standard_20 最终结果 (500/500)\\n- [ ] 确认 eval_postprune_standard_30 最终结果\\n- [ ] Agent 处理 westd worker 结果后汇报\\n- [ ] Paper Agent 完成 intro rewrite\\n- [ ] 所有关键数据到齐后 → Paper Agent Full Draft\\n\\n## GPU 预算\\n- westb-23072: cuda:0, cuda:1 (2 GPUs) — **SSH 阻塞，无法使用**\\n- westd-11672: cuda:0, cuda:1, cuda:2, cuda:3 (4 GPUs) — evals running/idle\\n\\n## 关键里程碑\\n| 里程碑 | 状态 | 备注 |\\n|--------|------|------|\\n| MVP Pass | ✅ D014 | RASP 31% vs Standard 27% pos
…[truncated 2184 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 24726
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-17T23:40:37.680957+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/skills/resource-saturation.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/skills/resource-saturation.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-17T23:40:39.086244+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/agent_142071c9.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "Read",
  "elapsed_ms": 1405
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-17T23:40:39.136953+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/skills/framing-reaudit.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/skills/framing-reaudit.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-17T23:40:39.490407+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/.claude/sessions/agent_142071c9.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-17T23:40:39.490813+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "file": "paper_framing.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "recovery_aware_struct_prune",
    "file": "paper_framing.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-17T23:40:39.592301+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper_framing.md\", \"content\": \"# Paper Framing — recovery_aware_struct_prune\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR May 25 submission)\\n- Deadline: ARR May 25, 2026\\n\\n## Core Insight (Recovery Capacity Gradient)\\nStructural pruning criterion determines post-RLVR recovery capacity of reasoning LLMs. We discover a **recovery capacity gradient** across pruning methods during GRPO training: CKA-only (pure representational diversity preservation) enables **active super-recovery** from transient RL instability, while gradient-based importance scoring progressively destroys this capacity.\\n\\nThe gradient: **CKA-only > Random > Standard > RASP**\\n\\nMechanism: Gradient importance scoring (used in Standard and RASP) removes structures that are \\\"unimportant\\\" by gradient metrics but **representationally unique** — precisely the diversity that RL exploration requires. CKA-only scoring removes only truly redundant structures (high pairwise similarity), preserving the full representational vocabulary that enables policy recovery from training perturbations.\\n\\nSeparately, GRPO reward-accuracy decoupling is an **in-distribution saturation effect**: on GSM8K (saturated), reward rises but accuracy is unchanged; on MATH-500 (unsaturated), GRPO genuinely improves OOD reasoning.\\n\\n## Core Claims (2 + 1 observation)\\n\\n### C1: GRPO reward-accuracy decoupling is in-distribution specific (saturation effect)\\nGRPO does not improve reasoning accuracy on saturated benchmarks for ANY model: unpruned (81.27% = SFT 81.27%, identical 1072/1319), Standard-pruned (58.91% vs SFT 59.29%), RASP-pruned (60.65% vs SFT 61.49%). Reward rises dramatically (unpruned: 0→0.661) but accuracy is unchanged on GSM8K.\\n\\nHowever, on MATH-500 (unsaturated OOD benchmark), GRPO provides genuine improvement: Standard +6.7pp (32.7% vs SF
…[truncated 10631 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-17T23:41:02.498894+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/resource-saturation.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/resource-saturation.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-17T23:41:02.951968+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "Glob",
  "elapsed_ms": 453
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-17T23:41:03.002613+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/framing-reaudit.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/framing-reaudit.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-17T23:41:04.708598+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "Glob",
  "elapsed_ms": 1705
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-17T23:41:04.759291+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__get_worker_status,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__load_project_config",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__get_worker_status,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__load_project_config",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-17T23:41:04.759757+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-17T23:41:19.170791+00:00_

called mcp__agent-ml-research__load_project_config

<details open><summary>🔧 Tool call — mcp__agent-ml-research__load_project_config</summary>

```json
{
  "project_name": "recovery_aware_struct_prune",
  "section": "execution"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "mcp__agent-ml-research__load_project_config",
  "tool_args": {
    "project_name": "recovery_aware_struct_prune",
    "section": "execution"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-17T23:41:19.221432+00:00_

{"result":"{\"success\": true, \"data\": {\"project\": \"recovery_aware_struct_prune\", \"section\": \"execution\", \"config\": {\"execution\": {\"gpu_ids\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"project_path\": \"/root/recovery_aware_struct_prune\", \"servers\": [{\"account\": \"root\", \"server\": \"westb-23072\"}, {\"account\": \"root\", \"server\": \"westd-11672\"}]}}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "mcp__agent-ml-research__load_project_config",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-17T23:41:19.773579+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "file": "memory.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "recovery_aware_struct_prune",
    "file": "memory.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-17T23:41:20.175429+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/memory.md\", \"content\": \"# Project Memory — recovery_aware_struct_prune\\n\\n## 基础设施经验\\n\\n### tokenizer 同步问题 (2026-05-17)\\nSFT 模型在 server A 训练后，server B 上 eval 会失败（AutoTokenizer 找不到 tokenizer 文件）。原因：HF Trainer save_pretrained 可能不保存 tokenizer，或 rsync 时遗漏。修复：从基础模型复制 tokenizer_config.json, tokenizer.json, special_tokens_map.json 等文件到 SFT checkpoint 目录。\\n\\n### GRPO 模型 MATH-500 eval 超时 (2026-05-17)\\nGRPO 模型在 MATH-500 上生成极长推理链 (~112s/problem vs SFT ~25s)，6h timeout 仅完成 193/500 题。v3 已去除 timeout 限制。D051 裁定 MATH-500 GRPO 对比不可用于 C3 论证（GRPO 和 SFT 的 max_new_tokens 配置不公平）。\\n\\n### eval_humaneval EXIT_CODE=129 (2026-05-17)\\nEXIT_CODE=129 = SIGHUP (128+1)，进程已完成全部评测并保存结果后 SSH 断连。结果有效，不需重跑。\\n\\n### sft_cka_only_20 跨服务器传输 (2026-05-17)\\nsft_cka_only_20 模型只存在于 westb-23072。通过 EC2 跳板中转 rsync 成功传输到 westd。磁盘清理后 westd 有 312GB 可用。\\n\\n### CKA-only pruning 实现方式 (2026-05-17)\\nprune.py 没有 cka_only mode。用 dummy importance (全1) + `--mode rasp --alpha 1` 实现：score = 1 × (1-F(h)) = 纯 CKA-only scoring。CKA-only 只剪 MLP（303/784 groups），0 attn heads（CKA overlap 在 attn 不够高）。\\n\\n## 关键实验发现\\n\\n### HumanEval@2048 超加性交互效应 (2026-05-17)\\nRASP 单独不帮 HumanEval（SFT RASP 10.37% < SFT Standard 11.59%），GRPO 单独不帮（GRPO Standard 10.37%），但 RASP+GRPO = 14.63% 是最优。这是超加性交互，不是独立主效应。意味着 C1 应从\\\"独立主效应\\\"改为\\\"RASP 保留了 GRPO 可以利用的结构\\\"。代码生成对剪枝极度敏感（67-77% 相对下降 vs GSM8K 25-35%）。N=164 下剪枝模型间差异未达统计显著性。\\n\\n### 30% sparsity cliff (2026-05-17 confirmed)\\nRASP 30% post-prune: **0% accuracy** (0/200), 97% truncated, avg_len=3984。Standard 30%: 3.0% @ 139/200。存在 25%→30% 的 hard cliff：模型完全丧失推理能力。对比 20%(RASP 29%, Standard 17.5%) 和 25%(RASP 21%, Standard 16%)，降解曲线在 30% 断崖。CKA-only 30% (28.92% actual sparsity) eval 重试中。\\n\\n### GRPO collapse 在 25% 同样发生 (2026-05-17)\\ngrpo_rasp_25: 100/100 steps, frac_reward_zero_std=0.875, reward=0.009, entropy=0.043。与 RASP 20% 类似（frac_zero_std=0.95
…[truncated 1806 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 401
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-17T23:41:20.627382+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "filters": "{'exp_id': 'eval_postprune_cka_only_30'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "recovery_aware_struct_prune",
    "filters": "{'exp_id': 'eval_postprune_cka_only_30'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-17T23:41:21.030820+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4106}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 403
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-17T23:41:36.831381+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__list_workers,mcp__agent-ml-research__read_experiment_plan_with_status",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__list_workers,mcp__agent-ml-research__read_experiment_plan_with_status",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-17T23:41:36.831706+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-17T23:41:38.039429+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-17T23:41:38.140682+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/method.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/results.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "Glob",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-17T23:41:41.151121+00:00_

called mcp__agent-ml-research__list_workers

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_workers</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "status": "running"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "mcp__agent-ml-research__list_workers",
  "tool_args": {
    "project": "recovery_aware_struct_prune",
    "status": "running"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-17T23:41:41.603251+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [], \"count\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-17T23:41:42.105534+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/method.md",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/method.md",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-17T23:41:42.306776+00:00_

1	# Method
2	
3	## 3.1 Overview
4	
5	We study the interaction between structural pruning decisions and post-pruning recovery paradigms in reasoning LLMs. Our methodology has three components: (1) Recovery-Aware Structural Pruning (RASP), a scoring function that incorporates functional redundancy into pruning decisions; (2) a two-stage recovery pipeline (SFT warmup followed by GRPO alignment); and (3) a collapse diagnostic framework that uses GRPO training dynamics to reveal structural damage patterns. Figure 1 illustrates the overall framework.
6	
7	## 3.2 Recovery-Aware Structural Pruning (RASP)
8	
9	### Scoring Function
10	
11	RASP assigns each structural group (attention head or MLP intermediate group) a composite score that balances structural importance against functional uniqueness. For a structural group $h$ in layer $l$, the score is:
12	
13	$$S(h) = I(h) \times (1 - F(h))^{\alpha}$$
14	
15	where $I(h)$ denotes the structural importance of group $h$, $F(h)$ denotes the functional overlap of $h$ with other groups in the same layer, and $\alpha \geq 0$ controls the weight placed on functional uniqueness. Groups with the lowest scores are pruned first.
16	
17	**Structural Importance $I(h)$.**  We compute importance via first-order Taylor expansion over a calibration set of reasoning traces. Given input-output pairs $(x, y)$ from the calibration set, the importance of group $h$ is:
18	
19	$$I(h) = \left| \sum_{(x,y) \in \mathcal{D}_{\text{cal}}} \frac{\partial \mathcal{L}(x, y)}{\partial h} \cdot h \right|$$
20	
21	This measures the expected change in loss when group $h$ is removed, approximated to first order.
22	
23	**Functional Overlap $F(h)$.**  We quantify redundancy using Centered Kernel Alignment (CKA; Kornblith et al., 2019) computed between group $h$ and all other groups within the same layer. Given activation matrices $X_h, X_{h'}$ collected over the calibration set, the linear CKA between groups $h$ and $h'$ is:
24	
25	$$\text{CKA}(h, h') = \frac{\|X_
…[truncated 254 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-17T23:41:42.357395+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/results.md",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/results.md",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-17T23:41:42.408067+00:00_

1	# Experiments and Results
2	
3	## 4.1 GRPO Reward-Accuracy Decoupling is Universal (Claim 1)
4	
5	We evaluate whether GRPO training improves reasoning accuracy beyond the SFT baseline. Table 1 reports GSM8K accuracy for all three pruning conditions under both recovery paradigms.
6	
7	**Table 1: GRPO reward-accuracy decoupling across pruning conditions.** $N = 1{,}319$ GSM8K test problems, greedy decoding, seed 42.
8	
9	| Model | SFT Acc (%) | GRPO Acc (%) | $\Delta$ (pp) | Peak Reward | Collapse |
10	|-------|-------------|--------------|---------------|-------------|----------|
11	| Unpruned | 81.27 | 81.27 | 0.00 | 0.661 | None |
12	| Standard 20% | 59.29 | 58.91 | -0.38 | 0.096 | Transient |
13	| RASP 20% | 61.49 | 60.65 | -0.84 | 0.039 | Permanent |
14	
15	*Sources: eval\_sft\_unpruned\_full, eval\_grpo\_unpruned\_v2\_step100, eval\_sft\_standard\_full\_westd, eval\_grpo\_standard\_step50\_full, eval\_sft\_rasp\_full\_westd, eval\_grpo\_rasp\_v9\_step5.*
16	
17	The unpruned model provides the strongest evidence for universal decoupling. GRPO drives reward from 0 to 0.661 over 100 steps, yet GSM8K accuracy remains exactly 81.27% (1,072/1,319 correct answers, identical to SFT). The model produces 1,072 of the same correct answers under both conditions. Reward improvement reflects changes in output format and length distribution, not genuine reasoning gains. This result holds despite stable training with no collapse and sustained gradient flow throughout all 100 steps (final grad\_norm = 6.97, final entropy = 0.194).
18	
19	For pruned models, the pattern is consistent: Standard achieves its best GRPO accuracy at step 50 (58.91%), 0.38pp below SFT. RASP achieves 60.65% at step 5, 0.84pp below SFT. Neither pruning condition shows any accuracy benefit from GRPO. The GRPO accuracy for RASP at step 10 is 61.87% ($p = 0.52$ vs step 5), confirming that early collapse onset does not reduce accuracy below the SFT baseline either.
20	
21	We additionally verify this decoupl
…[truncated 959 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-17T23:42:17.397054+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/writing_plan.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/writing_plan.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-17T23:42:17.598217+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/writing_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "Glob",
  "elapsed_ms": 201
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-17T23:42:17.648894+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/method.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/method.md"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-17T23:42:18.100920+00:00_

1	# Method
2	
3	## 3.1 Overview
4	
5	We study the interaction between structural pruning decisions and post-pruning recovery paradigms in reasoning LLMs. Our methodology has three components: (1) Recovery-Aware Structural Pruning (RASP), a scoring function that incorporates functional redundancy into pruning decisions; (2) a two-stage recovery pipeline (SFT warmup followed by GRPO alignment); and (3) a collapse diagnostic framework that uses GRPO training dynamics to reveal structural damage patterns. Figure 1 illustrates the overall framework.
6	
7	## 3.2 Recovery-Aware Structural Pruning (RASP)
8	
9	### Scoring Function
10	
11	RASP assigns each structural group (attention head or MLP intermediate group) a composite score that balances structural importance against functional uniqueness. For a structural group $h$ in layer $l$, the score is:
12	
13	$$S(h) = I(h) \times (1 - F(h))^{\alpha}$$
14	
15	where $I(h)$ denotes the structural importance of group $h$, $F(h)$ denotes the functional overlap of $h$ with other groups in the same layer, and $\alpha \geq 0$ controls the weight placed on functional uniqueness. Groups with the lowest scores are pruned first.
16	
17	**Structural Importance $I(h)$.**  We compute importance via first-order Taylor expansion over a calibration set of reasoning traces. Given input-output pairs $(x, y)$ from the calibration set, the importance of group $h$ is:
18	
19	$$I(h) = \left| \sum_{(x,y) \in \mathcal{D}_{\text{cal}}} \frac{\partial \mathcal{L}(x, y)}{\partial h} \cdot h \right|$$
20	
21	This measures the expected change in loss when group $h$ is removed, approximated to first order.
22	
23	**Functional Overlap $F(h)$.**  We quantify redundancy using Centered Kernel Alignment (CKA; Kornblith et al., 2019) computed between group $h$ and all other groups within the same layer. Given activation matrices $X_h, X_{h'}$ collected over the calibration set, the linear CKA between groups $h$ and $h'$ is:
24	
25	$$\text{CKA}(h, h') = \frac{\|X_
…[truncated 5112 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-17T23:42:18.101350+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/results.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/results.md"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-17T23:42:18.151898+00:00_

1	# Experiments and Results
2	
3	## 4.1 GRPO Reward-Accuracy Decoupling is Universal (Claim 1)
4	
5	We evaluate whether GRPO training improves reasoning accuracy beyond the SFT baseline. Table 1 reports GSM8K accuracy for all three pruning conditions under both recovery paradigms.
6	
7	**Table 1: GRPO reward-accuracy decoupling across pruning conditions.** $N = 1{,}319$ GSM8K test problems, greedy decoding, seed 42.
8	
9	| Model | SFT Acc (%) | GRPO Acc (%) | $\Delta$ (pp) | Peak Reward | Collapse |
10	|-------|-------------|--------------|---------------|-------------|----------|
11	| Unpruned | 81.27 | 81.27 | 0.00 | 0.661 | None |
12	| Standard 20% | 59.29 | 58.91 | -0.38 | 0.096 | Transient |
13	| RASP 20% | 61.49 | 60.65 | -0.84 | 0.039 | Permanent |
14	
15	*Sources: eval\_sft\_unpruned\_full, eval\_grpo\_unpruned\_v2\_step100, eval\_sft\_standard\_full\_westd, eval\_grpo\_standard\_step50\_full, eval\_sft\_rasp\_full\_westd, eval\_grpo\_rasp\_v9\_step5.*
16	
17	The unpruned model provides the strongest evidence for universal decoupling. GRPO drives reward from 0 to 0.661 over 100 steps, yet GSM8K accuracy remains exactly 81.27% (1,072/1,319 correct answers, identical to SFT). The model produces 1,072 of the same correct answers under both conditions. Reward improvement reflects changes in output format and length distribution, not genuine reasoning gains. This result holds despite stable training with no collapse and sustained gradient flow throughout all 100 steps (final grad\_norm = 6.97, final entropy = 0.194).
18	
19	For pruned models, the pattern is consistent: Standard achieves its best GRPO accuracy at step 50 (58.91%), 0.38pp below SFT. RASP achieves 60.65% at step 5, 0.84pp below SFT. Neither pruning condition shows any accuracy benefit from GRPO. The GRPO accuracy for RASP at step 10 is 61.87% ($p = 0.52$ vs step 5), confirming that early collapse onset does not reduce accuracy below the SFT baseline either.
20	
21	We additionally verify this decoupl
…[truncated 8687 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-17T23:42:42.689413+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "file": "writing_plan.yaml",
  "max_chars": "6000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "recovery_aware_struct_prune",
    "file": "writing_plan.yaml",
    "max_chars": "6000"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-17T23:42:42.811660+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/writing_plan.yaml\", \"content\": \"meta:\\n  venue: EMNLP 2026\\n  track: main\\n  template: \\\"\\\"\\n  template_note: \\\"ARR May 25 submission. ACL template already set up in docs/paper/. Complete rewrite with new narrative (D045).\\\"\\n  page_limit: 8\\n  deadline: 2026-05-25\\n  core_claim: \\\"GRPO reward-accuracy decoupling is universal post-SFT; pruning additionally causes GRPO training collapse whose severity diagnoses structural damage type, revealing a Redundancy-Stability Tradeoff where structures optimal for SFT recovery are exactly those needed for RLVR stability.\\\"\\n  created_at: 2026-05-16T06:00:00Z\\n  updated_at: 2026-05-16T06:00:00Z\\n  framing_version: D045\\n  previous_narrative: \\\"Redundancy Paradox (RASP as universally superior) — invalidated by GRPO failure evidence\\\"\\n  narrative_shift: \\\"RASP reframed from 'best pruning method' to 'diagnostic tool' revealing fundamental pruning-alignment interaction\\\"\\n\\npaper_outline:\\n  - section: abstract\\n    word_budget: 200\\n    core_bullets:\\n      - \\\"Problem: The prune-recover-align pipeline for reasoning LLMs assumes alignment is independent of pruning decisions\\\"\\n      - \\\"Finding 1: GRPO reward improvement never translates to accuracy gain post-SFT (universal decoupling: unpruned 81.27%→81.27%, reward 0→0.661)\\\"\\n      - \\\"Finding 2: Pruning causes GRPO training collapse; severity gradient RASP (step 10, permanent) > Standard (step 60, transient) > Unpruned (never)\\\"\\n      - \\\"Finding 3: Redundancy-Stability Tradeoff — CKA-aware pruning benefits SFT (+2.2pp) but accelerates RLVR collapse 6×\\\"\\n      - \\\"Implication: Optimal pruning is fundamentally conditioned on recovery paradigm\\\"\\n    dependencies: [experiments, method]\\n    tables: []\\n    figures: []\\n    registry_refs: [eval_grpo_unpruned_v2_step100, e
…[truncated 4778 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 122
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-17T23:43:13.428539+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-17T23:43:13.579588+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/backup/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/backup/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/backup/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/backup/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/acl.sty
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/acl_natbib.bst
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/references.bib
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/method.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/results.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/tables/table1_postprune.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects
…[truncated 285 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "Glob",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-17T23:43:17.446508+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/introduction.tex",
  "limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/introduction.tex",
    "limit": "40"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-17T23:43:17.447032+00:00_

1	\section{Introduction}
2	\label{sec:intro}
3	
4	Large Language Models (LLMs) trained with Reinforcement Learning with Verifiable Rewards (RLVR) achieve strong mathematical reasoning~\citep{deepseek2025r1,shao2024grpo}, but their parameter counts and extended chain-of-thought traces make deployment costly.
5	Structured pruning, which removes entire attention heads or MLP channels, provides a hardware-friendly compression path that reduces both memory and latency without specialized sparse-computation support~\citep{llmpruner2023,graspprune2026}.
6	Because structured pruning at moderate sparsity severely degrades reasoning ability, a post-pruning recovery stage is essential.
7	The standard compression pipeline therefore proceeds in three stages: prune, recover via Supervised Fine-Tuning (SFT), then align via RLVR to restore reasoning quality.
8	This final alignment step appears straightforward: on an unpruned DeepSeek-R1-Distill-Qwen-7B~\citep{deepseek2025r1}, 100 steps of Group Relative Policy Optimization (GRPO;~\citealp{shao2024grpo}) raises the reward from 0 to 0.661.
9	Yet accuracy on GSM8K~\citep{cobbe2021gsm8k} remains exactly 81.27\%, with 1,072 of 1,319 test problems producing identical correct answers before and after alignment.
10	The reward improvement is an illusion: GRPO learns to produce outputs that score higher rewards without solving additional problems.
11	
12	This observation has immediate practical consequences for the compression pipeline.
13	\citet{selfhealing2025} report that RLVR-based recovery restores pruned reasoning models to 95\%+ of original performance at 25\% compression, establishing RLVR as the preferred recovery paradigm.
14	However, their evaluation reports only final-checkpoint accuracy and does not document per-step training dynamics during GRPO.
15	If GRPO reward gains fail to reflect genuine reasoning improvement even on unpruned models, the claim that RLVR ``recovers'' pruned models demands scrutiny.
16	The problem becomes a
…[truncated 3652 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-17T23:43:17.758525+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/experiments.tex",
  "limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/experiments.tex",
    "limit": "40"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-17T23:43:17.809231+00:00_

1	
2	\section{Experiments}
3	\label{sec:experiments}
4	
5	\subsection{Experimental Setup}
6	\label{sec:exp_setup}
7	
8	\paragraph{Base model.}
9	We evaluate \rasp{} on DeepSeek-R1-Distill-Qwen-7B~\citep{deepseek2025r1}, a 7B-parameter reasoning model built on the Qwen2.5 architecture~\citep{qwen2.5} with 28 transformer layers.
10	The model uses Grouped Query Attention (GQA;~\citealp{ainslie2023gqa}) with 28 query heads and 4 key-value heads per layer (group size $G{=}7$), and an MLP intermediate dimension of 18{,}944.
11	As a reasoning-distilled model whose chain-of-thought capabilities originate from reinforcement learning, it provides a direct testbed for studying how structural pruning interacts with RLVR-based recovery.
12	
13	\paragraph{Evaluation.}
14	We evaluate on GSM8K~\citep{cobbe2021gsm8k}, a benchmark of 1{,}319 grade-school math problems requiring multi-step arithmetic reasoning.
15	We report exact-match accuracy: the final numerical answer is extracted from the model's generation and compared against the ground truth.
16	For rapid iteration during development, we use a fixed 100-problem subset ($N{=}100$); final results use the full test set ($N{=}1{,}319$).
17	We define recovery $\Delta$ as the accuracy gain from post-prune to post-recovery, capturing how much reasoning ability the recovery pipeline restores independent of initial pruning damage.
18	
19	\paragraph{Hardware.}
20	All experiments run on a single node with 2$\times$ NVIDIA RTX PRO 6000 GPUs (94\,GB VRAM each).
21	The two pruning variants (Standard and \rasp{}) are trained in parallel on separate GPUs to ensure identical wall-clock conditions.
22	
23	\subsection{Pruning Configuration}
24	\label{sec:pruning_config}
25	
26	\paragraph{Sparsity and granularity.}
27	We apply 20\% structured sparsity by scoring and ranking both attention GQA groups (each comprising 1 KV head and 7 query heads) and MLP channel groups in a unified importance list; at 20\% sparsity, the global ranking preferentiall
…[truncated 1551 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-17T23:44:28.223859+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

```json
{
  "task_type": "paper:intro-rewrite-d056",
  "project": "recovery_aware_struct_prune",
  "tool_groups": "['knowledge']",
  "task_prompt": "## 任务：重写 introduction.tex，对齐 D056 framing\n\n### 背景\n论文 framing 在 D056 发生了根本性变化。当前 introduction.tex 基于旧 framing (D045)，需要全面重写。\n\n### 关键变化 (D045 → D056)\n**旧 framing**: 3 pruning methods (Unpruned, Standard, RASP)，RASP 作为 diagnostic tool 揭示 Redundancy-Stability Tradeoff。C1=universal decoupling, C2=collapse gradient (3 methods), C3=tradeoff。\n\n**新 framing (D056)**: 4 pruning methods 对比 (CKA-only, Random, Standard, RASP + Unpruned 作为 control)。核心贡献从 RASP 转向 Recovery Capacity Gradient。\n- C1: GRPO reward-accuracy decoupling 是 in-distribution saturation effect（GSM8K 饱和所以 accuracy 不变，MATH-500 上 GRPO 确实提升 OOD reasoning）\n- C2 (MAIN CONTRIBUTION): Recovery Capacity Gradient — 4 种 pruning criterion 决定 RL recovery capacity:\n  - CKA-only: active super-recovery（frac_zero_std 从 0.35 降到 0.125，低于初始 0.175）\n  - Random: stagnation after partial recovery\n  - Standard: borderline collapse (transient dip step 60)\n  - RASP: permanent collapse (step 10)\n- Observation: SFT equalizes all scoring methods (59-64%, p>0.1); 30% sparsity cliff is universal\n- Core insight: Gradient importance scoring removes \"unimportant but representationally unique\" structures, destroying RL exploration diversity. CKA-only preserves all unique structures.\n\n### 你的任务\n1. `read_project_file(project=\"recovery_aware_struct_prune\", file=\"paper_framing.md\", max_chars=0)` 获取完整 D056 framing\n2. 读取当前 introduction.tex: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/introduction.tex`\n3. 重写 introduction.tex，对齐 D056 framing\n\n### 写作要求\n- 遵循 5 段结构：背景 → 问题重要性 → 现有不足 → 本文核心想法 → 贡献列表\n- Hook: 不要用 \"LLMs have shown remarkable capabilities\" 开头。从具体问题切入：pruning criterion 决定 RL recovery capacity\n- 4-method gradient (CKA-only > Random > Standard > RASP) 是核心卖点\n- CKA-only 的 \"super-recovery\"（低于初始 baseline）是关键 novelty\n- C1 重新定义为 in-distribution saturation effect，不是 \"universal decoupling\"\n- 贡献列表必须与 D056 paper_framing.md 的 Claims 一致\n- 保留有效的引用 (\\citep, \\citet)，不要编造新引用\n- 严格遵循去 AI 写作风格：禁止 em-dash (—)，禁止 -ing 短语结尾，禁止 \"Furthermore/Moreover/Additionally\" 连续使用，避免 \"delve/leverage/utilize\"\n- LaTeX 格式，保持 \\section{Introduction} \\label{sec:intro} 开头\n\n### 产出\n直接覆盖写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/introduction.tex`",
  "context": "项目路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/\n论文目录: paper/\n当前 framing 版本: D056 (2026-05-17)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "paper:intro-rewrite-d056",
    "project": "recovery_aware_struct_prune",
    "tool_groups": "['knowledge']",
    "task_prompt": "## 任务：重写 introduction.tex，对齐 D056 framing\n\n### 背景\n论文 framing 在 D056 发生了根本性变化。当前 introduction.tex 基于旧 framing (D045)，需要全面重写。\n\n### 关键变化 (D045 → D056)\n**旧 framing**: 3 pruning methods (Unpruned, Standard, RASP)，RASP 作为 diagnostic tool 揭示 Redundancy-Stability Tradeoff。C1=universal decoupling, C2=collapse gradient (3 methods), C3=tradeoff。\n\n**新 framing (D056)**: 4 pruning methods 对比 (CKA-only, Random, Standard, RASP + Unpruned 作为 control)。核心贡献从 RASP 转向 Recovery Capacity Gradient。\n- C1: GRPO reward-accuracy decoupling 是 in-distribution saturation effect（GSM8K 饱和所以 accuracy 不变，MATH-500 上 GRPO 确实提升 OOD reasoning）\n- C2 (MAIN CONTRIBUTION): Recovery Capacity Gradient — 4 种 pruning criterion 决定 RL recovery capacity:\n  - CKA-only: active super-recovery（frac_zero_std 从 0.35 降到 0.125，低于初始 0.175）\n  - Random: stagnation after partial recovery\n  - Standard: borderline collapse (transient dip step 60)\n  - RASP: permanent collapse (step 10)\n- Observation: SFT equalizes all scoring methods (59-64%, p>0.1); 30% sparsity cliff is universal\n- Core insight: Gradient importance scoring removes \"unimportant but representationally unique\" structures, destroying RL exploration diversity. CKA-only preserves all unique structures.\n\n### 你的任务\n1. `read_project_file(project=\"recovery_aware_struct_prune\", file=\"paper_framing.md\", max_chars=0)` 获取完整 D056 framing\n2. 读取当前 introduction.tex: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/introduction.tex`\n3. 重写 introduction.tex，对齐 D056 framing\n\n### 写作要求\n- 遵循 5 段结构：背景 → 问题重要性 → 现有不足 → 本文核心想法 → 贡献列表\n- Hook: 不要用 \"LLMs have shown remarkable capabilities\" 开头。从具体问题切入：pruning criterion 决定 RL recovery capacity\n- 4-method gradient (CKA-only > Random > Standard > RASP) 是核心卖点\n- CKA-only 的 \"super-recovery\"（低于初始 baseline）是关键 novelty\n- C1 重新定义为 in-distribution saturation effect，不是 \"universal decoupling\"\n- 贡献列表必须与 D056 paper_framing.md 的 Claims 一致\n- 保留有效的引用 (\\citep, \\citet)，不要编造新引用\n- 严格遵循去 AI 写作风格：禁止 em-dash (—)，禁止 -ing 短语结尾，禁止 \"Furthermore/Moreover/Additionally\" 连续使用，避免 \"delve/leverage/utilize\"\n- LaTeX 格式，保持 \\section{Introduction} \\label{sec:intro} 开头\n\n### 产出\n直接覆盖写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/introduction.tex`",
    "context": "项目路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/\n论文目录: paper/\n当前 framing 版本: D056 (2026-05-17)"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-17T23:44:46.969488+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_paper_intro-rewrite-d056_20260517T234428\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/logs/workers/worker_paper_intro-rewrite-d056_20260517T234428.log\", \"setup_data\": {}, \"message\": \"Worker worker_paper_intro-rewrite-d056_20260517T234428 started. Use get_worker_status('worker_paper_intro-rewrite-d056_20260517T234428') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 18745
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-17T23:44:50.794299+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

```json
{
  "task_type": "paper:method-rewrite-d056",
  "project": "recovery_aware_struct_prune",
  "tool_groups": "['knowledge']",
  "task_prompt": "## 任务：重写 method.tex，对齐 D056 framing（4-method 比较框架）\n\n### 背景\n论文 framing 在 D056 从 \"RASP 作为 diagnostic tool\" 转为 \"4-method 比较框架揭示 Recovery Capacity Gradient\"。当前 method.tex 只描述 3 种 pruning conditions (Unpruned, Standard, RASP)，需要加入 CKA-only 和 Random 方法。\n\n### 关键变化\n1. **从 RASP-centric 转向 comparative framework**: 论文的核心不再是 \"RASP 这个方法\"，而是 \"通过 4 种 pruning criterion 的对比揭示 recovery capacity gradient\"\n2. **4 种方法**:\n   - Standard (gradient importance only): S(h) = I(h), α=0\n   - RASP (composite): S(h) = I(h) × (1-F(h))^α, α=1.0\n   - CKA-only (pure diversity preservation): S(h) = 1 × (1-F(h))^1 = (1-F(h))。实现方式：dummy importance (全1) + mode=rasp + alpha=1。只剪 MLP (303/784 groups), 0 attn heads\n   - Random: 随机分数 (seed=42)，lower bound baseline\n3. **Collapse diagnostic framework** 基本不变\n4. **Experimental design** 扩展为 4+1 条件（4 pruning methods + Unpruned control）\n\n### 你的任务\n1. `read_project_file(project=\"recovery_aware_struct_prune\", file=\"paper_framing.md\", max_chars=0)` 获取完整 D056 framing\n2. 读取当前 method.tex: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/method.tex`\n3. 也参考 method.md: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/method.md`\n4. 重写 method.tex\n\n### 方法框架重构\n- §3.1 Overview: 从 \"RASP + pipeline + diagnostics\" 改为 \"4-method comparative framework for studying pruning-RL interaction\"\n- §3.2 Pruning Criterion Design Space: 描述 4 种 scoring function 作为 \"controlled variable\"\n  - Unified scoring formula: S(h) = I(h)^a × (1-F(h))^b，不同 (a,b) 组合产生 4 种 criterion\n  - Standard: (a=1, b=0) — gradient importance only\n  - RASP: (a=1, b=1) — composite score\n  - CKA-only: (a=0, b=1) — pure diversity preservation, removes only redundant structures\n  - Random: random score — lower bound baseline\n- §3.3 Two-Stage Recovery Pipeline: SFT + GRPO（不变）\n- §3.4 Collapse Diagnostic Framework: frac_zero_std, grad_norm, completion length（基本不变）\n- §3.5 Experimental Design: 5 model conditions (4 pruning + Unpruned), DeepSeek-R1-Distill-Qwen-7B, 20% structured sparsity, GSM8K + MATH-500\n\n### 写作要求\n- LaTeX 格式，保持 \\section \\subsection 结构\n- 数学公式保持精确\n- 去 AI 风格：禁止 em-dash, -ing phrases, 连续 Furthermore/Moreover\n- 保留已有的有效引用，不编造新引用\n- 简洁直接，不冗余\n\n### 产出\n直接覆盖写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/method.tex`",
  "context": "项目路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/\n论文目录: paper/\nCKA-only 实现细节：prune.py 没有独立 cka_only mode。用 dummy importance (全1) + --mode rasp --alpha 1 实现：score = 1 × (1-F(h)) = 纯 CKA-only scoring。CKA-only 只剪 MLP（303/784 groups），0 attn heads（CKA overlap 在 attn 不够高）。\nRandom 实现：random scoring with seed 42。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "paper:method-rewrite-d056",
    "project": "recovery_aware_struct_prune",
    "tool_groups": "['knowledge']",
    "task_prompt": "## 任务：重写 method.tex，对齐 D056 framing（4-method 比较框架）\n\n### 背景\n论文 framing 在 D056 从 \"RASP 作为 diagnostic tool\" 转为 \"4-method 比较框架揭示 Recovery Capacity Gradient\"。当前 method.tex 只描述 3 种 pruning conditions (Unpruned, Standard, RASP)，需要加入 CKA-only 和 Random 方法。\n\n### 关键变化\n1. **从 RASP-centric 转向 comparative framework**: 论文的核心不再是 \"RASP 这个方法\"，而是 \"通过 4 种 pruning criterion 的对比揭示 recovery capacity gradient\"\n2. **4 种方法**:\n   - Standard (gradient importance only): S(h) = I(h), α=0\n   - RASP (composite): S(h) = I(h) × (1-F(h))^α, α=1.0\n   - CKA-only (pure diversity preservation): S(h) = 1 × (1-F(h))^1 = (1-F(h))。实现方式：dummy importance (全1) + mode=rasp + alpha=1。只剪 MLP (303/784 groups), 0 attn heads\n   - Random: 随机分数 (seed=42)，lower bound baseline\n3. **Collapse diagnostic framework** 基本不变\n4. **Experimental design** 扩展为 4+1 条件（4 pruning methods + Unpruned control）\n\n### 你的任务\n1. `read_project_file(project=\"recovery_aware_struct_prune\", file=\"paper_framing.md\", max_chars=0)` 获取完整 D056 framing\n2. 读取当前 method.tex: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/method.tex`\n3. 也参考 method.md: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/method.md`\n4. 重写 method.tex\n\n### 方法框架重构\n- §3.1 Overview: 从 \"RASP + pipeline + diagnostics\" 改为 \"4-method comparative framework for studying pruning-RL interaction\"\n- §3.2 Pruning Criterion Design Space: 描述 4 种 scoring function 作为 \"controlled variable\"\n  - Unified scoring formula: S(h) = I(h)^a × (1-F(h))^b，不同 (a,b) 组合产生 4 种 criterion\n  - Standard: (a=1, b=0) — gradient importance only\n  - RASP: (a=1, b=1) — composite score\n  - CKA-only: (a=0, b=1) — pure diversity preservation, removes only redundant structures\n  - Random: random score — lower bound baseline\n- §3.3 Two-Stage Recovery Pipeline: SFT + GRPO（不变）\n- §3.4 Collapse Diagnostic Framework: frac_zero_std, grad_norm, completion length（基本不变）\n- §3.5 Experimental Design: 5 model conditions (4 pruning + Unpruned), DeepSeek-R1-Distill-Qwen-7B, 20% structured sparsity, GSM8K + MATH-500\n\n### 写作要求\n- LaTeX 格式，保持 \\section \\subsection 结构\n- 数学公式保持精确\n- 去 AI 风格：禁止 em-dash, -ing phrases, 连续 Furthermore/Moreover\n- 保留已有的有效引用，不编造新引用\n- 简洁直接，不冗余\n\n### 产出\n直接覆盖写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/method.tex`",
    "context": "项目路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/\n论文目录: paper/\nCKA-only 实现细节：prune.py 没有独立 cka_only mode。用 dummy importance (全1) + --mode rasp --alpha 1 实现：score = 1 × (1-F(h)) = 纯 CKA-only scoring。CKA-only 只剪 MLP（303/784 groups），0 attn heads（CKA overlap 在 attn 不够高）。\nRandom 实现：random scoring with seed 42。"
  }
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-17T23:45:20.923994+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

```json
{
  "task_type": "paper:experiments-rewrite-d056",
  "project": "recovery_aware_struct_prune",
  "tool_groups": "['knowledge']",
  "task_prompt": "## 任务：重写 experiments.tex，对齐 D056 framing（C1 saturation + C2 recovery gradient + observation）\n\n### 背景\n论文 framing D056 将 claims 重构为 C1 (in-distribution saturation) + C2 (recovery capacity gradient, main) + observation。当前 experiments.tex 基于旧 framing (3 claims, 3 methods)，需要全面重写。\n\n### 关键数据（从 registry 和 memory 确认的结果）\n\n**C1 数据 — In-Distribution Saturation Effect:**\nGSM8K (N=1319, greedy, seed 42):\n| Model | SFT Acc | GRPO Acc | Δ | Peak Reward |\n|-------|---------|----------|---|-------------|\n| Unpruned | 81.27% | 81.27% | 0.00 | 0.661 |\n| Standard 20% | 59.29% | 58.91% | -0.38 | 0.096 |\n| RASP 20% | 61.49% | 60.65% | -0.84 | 0.039 |\n\nMATH-500 (部分结果):\n| Model | SFT Acc | GRPO Acc | Δ |\n|-------|---------|----------|---|\n| Standard 20% | 26.0% | 32.7% (interim@309/500) | +6.7pp |\n| RASP 20% | 24.2% | ~30.7% (interim) | +6.5pp |\n（MATH-500 数据仍在收集中，用 interim 数据标注）\n\n**C2 数据 — Recovery Capacity Gradient (MAIN):**\n4 methods at 20% sparsity, GRPO 100 steps, identical config:\n| Method | frac_zero_std (step 70) | reward (step 70) | KL | Recovery |\n|--------|------------------------|------------------|------|----------|\n| CKA-only | 0.125 | 0.308 | 0.0016 | Active super-recovery (below initial 0.175) |\n| Random | 0.300 | 0.190 | 0.0045 | Stagnation after partial recovery |\n| Standard | 0.525 | 0.065 | — | Borderline collapse (transient dip step 60) |\n| RASP | 0.950 | 0.021 | — | Permanent collapse (step 10) |\n\n注意：step 70 数据是 confirmed，step 100 final 数据在 westb 上等 SSH 恢复。用 step 70 数据写，标注为 \"as of step 70\"。\n\n**Observation 数据 — SFT Equalization + 30% Cliff:**\nPost-SFT GSM8K (N=1319):\n- Unpruned: 81.27%\n- RASP 20%: 61.49%\n- Standard 20%: 59.29%\n- CKA-only 20%: ~63% (N=1319 结果 running, pilot N=200=64%)\n- Random 20%: 60.0% (N=200)\n- All pruned methods: 59-64%, p>0.1 for all pairs\n\n30% sparsity cliff:\n- RASP 30%: 0% (0/200), 97% truncated\n- CKA-only 30%: 0% (actual sparsity 28.92%)\n- Standard 30%: 3% (interim)\n\n**Additional: Inference speedup:**\n- RASP 20%: 37.8% latency reduction, 28.5% memory reduction\n- Standard 20%: 7.7% latency reduction, 28.4% memory reduction\n\n### 你的任务\n1. `read_project_file(project=\"recovery_aware_struct_prune\", file=\"paper_framing.md\", max_chars=0)` 获取完整 D056 framing\n2. 读取当前 experiments.tex: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/experiments.tex`\n3. 也参考 results.md: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/results.md`\n4. 重写 experiments.tex\n\n### 结构要求\n- §4.1 Experimental Setup: 扩展为 5 conditions (4 pruning + Unpruned), 两个 benchmark (GSM8K + MATH-500)\n- §4.2 Recovery Capacity Gradient (C2, Main): 4-method gradient 表 + 分析。这是最重要的 section，给充分篇幅\n- §4.3 In-Distribution Saturation Effect (C1): GSM8K decoupling + MATH-500 genuine improvement\n- §4.4 SFT Equalization and Sparsity Cliff (Observation): convergence + 30% cliff\n- §4.5 Alpha Ablation: 保留现有数据\n- §4.6 Inference Efficiency: RASP vs Standard speedup asymmetry\n\n### 写作要求\n- 数据来源必须标注（标明 exp_id 或 W&B run）\n- 正在运行的实验用 interim 数据标注\n- 去 AI 风格：禁止 em-dash, -ing phrases, 连续 Furthermore/Moreover\n- LaTeX 格式\n- 每个数字服务于叙事推进，不堆砌\n- Table 和 Figure 有信息密度要求\n\n### 产出\n直接覆盖写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/experiments.tex`",
  "context": "项目路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/\n论文目录: paper/\nD051 裁定: MATH-500 GRPO vs SFT 对比不可用于 C3 论证（max_new_tokens 配置不公平），只作 supplementary。\n数据状态: step 70 confirmed, step 100 在 westb 等 SSH 恢复。MATH-500 evals 正在 westd 上运行。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:sft_cka_only_20",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "paper:experiments-rewrite-d056",
    "project": "recovery_aware_struct_prune",
    "tool_groups": "['knowledge']",
    "task_prompt": "## 任务：重写 experiments.tex，对齐 D056 framing（C1 saturation + C2 recovery gradient + observation）\n\n### 背景\n论文 framing D056 将 claims 重构为 C1 (in-distribution saturation) + C2 (recovery capacity gradient, main) + observation。当前 experiments.tex 基于旧 framing (3 claims, 3 methods)，需要全面重写。\n\n### 关键数据（从 registry 和 memory 确认的结果）\n\n**C1 数据 — In-Distribution Saturation Effect:**\nGSM8K (N=1319, greedy, seed 42):\n| Model | SFT Acc | GRPO Acc | Δ | Peak Reward |\n|-------|---------|----------|---|-------------|\n| Unpruned | 81.27% | 81.27% | 0.00 | 0.661 |\n| Standard 20% | 59.29% | 58.91% | -0.38 | 0.096 |\n| RASP 20% | 61.49% | 60.65% | -0.84 | 0.039 |\n\nMATH-500 (部分结果):\n| Model | SFT Acc | GRPO Acc | Δ |\n|-------|---------|----------|---|\n| Standard 20% | 26.0% | 32.7% (interim@309/500) | +6.7pp |\n| RASP 20% | 24.2% | ~30.7% (interim) | +6.5pp |\n（MATH-500 数据仍在收集中，用 interim 数据标注）\n\n**C2 数据 — Recovery Capacity Gradient (MAIN):**\n4 methods at 20% sparsity, GRPO 100 steps, identical config:\n| Method | frac_zero_std (step 70) | reward (step 70) | KL | Recovery |\n|--------|------------------------|------------------|------|----------|\n| CKA-only | 0.125 | 0.308 | 0.0016 | Active super-recovery (below initial 0.175) |\n| Random | 0.300 | 0.190 | 0.0045 | Stagnation after partial recovery |\n| Standard | 0.525 | 0.065 | — | Borderline collapse (transient dip step 60) |\n| RASP | 0.950 | 0.021 | — | Permanent collapse (step 10) |\n\n注意：step 70 数据是 confirmed，step 100 final 数据在 westb 上等 SSH 恢复。用 step 70 数据写，标注为 \"as of step 70\"。\n\n**Observation 数据 — SFT Equalization + 30% Cliff:**\nPost-SFT GSM8K (N=1319):\n- Unpruned: 81.27%\n- RASP 20%: 61.49%\n- Standard 20%: 59.29%\n- CKA-only 20%: ~63% (N=1319 结果 running, pilot N=200=64%)\n- Random 20%: 60.0% (N=200)\n- All pruned methods: 59-64%, p>0.1 for all pairs\n\n30% sparsity cliff:\n- RASP 30%: 0% (0/200), 97% truncated\n- CKA-only 30%: 0% (actual sparsity 28.92%)\n- Standard 30%: 3% (interim)\n\n**Additional: Inference speedup:**\n- RASP 20%: 37.8% latency reduction, 28.5% memory reduction\n- Standard 20%: 7.7% latency reduction, 28.4% memory reduction\n\n### 你的任务\n1. `read_project_file(project=\"recovery_aware_struct_prune\", file=\"paper_framing.md\", max_chars=0)` 获取完整 D056 framing\n2. 读取当前 experiments.tex: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/experiments.tex`\n3. 也参考 results.md: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/results.md`\n4. 重写 experiments.tex\n\n### 结构要求\n- §4.1 Experimental Setup: 扩展为 5 conditions (4 pruning + Unpruned), 两个 benchmark (GSM8K + MATH-500)\n- §4.2 Recovery Capacity Gradient (C2, Main): 4-method gradient 表 + 分析。这是最重要的 section，给充分篇幅\n- §4.3 In-Distribution Saturation Effect (C1): GSM8K decoupling + MATH-500 genuine improvement\n- §4.4 SFT Equalization and Sparsity Cliff (Observation): convergence + 30% cliff\n- §4.5 Alpha Ablation: 保留现有数据\n- §4.6 Inference Efficiency: RASP vs Standard speedup asymmetry\n\n### 写作要求\n- 数据来源必须标注（标明 exp_id 或 W&B run）\n- 正在运行的实验用 interim 数据标注\n- 去 AI 风格：禁止 em-dash, -ing phrases, 连续 Furthermore/Moreover\n- LaTeX 格式\n- 每个数字服务于叙事推进，不堆砌\n- Table 和 Figure 有信息密度要求\n\n### 产出\n直接覆盖写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/experiments.tex`",
    "context": "项目路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/\n论文目录: paper/\nD051 裁定: MATH-500 GRPO vs SFT 对比不可用于 C3 论证（max_new_tokens 配置不公平），只作 supplementary。\n数据状态: step 70 confirmed, step 100 在 westb 等 SSH 恢复。MATH-500 evals 正在 westd 上运行。"
  }
}
```

</details>

---

### Assistant

_source line 58 · 2026-05-17T23:59:30.767923+00:00_

Now I have the full picture. The entire paper (intro, method, experiments) is based on the OLD D045 framing (3 methods, RASP as diagnostic). D056 fundamentally changed the narrative to 4-method recovery capacity gradient. All sections need rewriting.

Spawning paper rewrite workers now to fix Worker pool = 0 and advance the paper toward ARR May 25.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:sft_cka_only_20"
}
```

</details>

---
