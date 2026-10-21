# cron hook train crm k1 accg object seed42 20260517T234200 294669

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 67
- **Recorded user turns:** 2
- **Tool calls:** 32
- **Original source:** `logs/chats/archive/cron_hook_train-crm-k1-accg-object-seed42_20260517T234200_294669.jsonl`
- **Structured JSON:** [`2a679a281dde0bef0d2f.json`](../../sessions/2a/2a679a281dde0bef0d2f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

29 recorded events

### User

_source line 1 · 2026-05-17T19:13:05.040213+00:00_

[HANDOFF] 你是 Main Agent，这是 Loop #20。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- GPU 白名单 17 张：bjb2-28827 cuda:0-5, bjb1-32546 cuda:0-5, bjb1-18228 cuda:0-3, bjb2-40593 cuda:0。**严禁用白名单外 GPU**
- LIBERO 并发上限：每台服务器 ≤4 评估进程（M005 规则，违反导致 OOM/数据损坏）
- bjb1-18228 访问 HuggingFace 必须 `HF_ENDPOINT=https://hf-mirror.com`（nohup/background 进程需显式 export）
- submit_training_job 命令必须 `bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ..."` 包裹（裸 python 不可靠，EXIT_CODE=127）
- exp_id 中 norm 值用 `p` 替代小数点：norm-0p3 = 0.3。禁止缩写歧义命名（norm03）
- Kill 实验前必须 `ps aux | grep` 完整命令行逐参数比对，曾因 norm03/norm003 混淆误杀有效进程
- EXIT_CODE=129 (SIGHUP) 不等于失败——先查日志确认是否已完成再判定

### 2. 🖥️ 基础设施快照
- **bjb2-28827** (6×4090): 工作目录 `/root/acr-vla-conformal-refinement`，Python `/root/miniconda3/bin/python`
- **bjb1-32546** (6×4090): 同上路径
- **bjb1-18228** (4×4090): 同上路径。OpenVLA 模型 `/root/autodl-tmp/models/openvla-libero-object/`
- **bjb2-40593** (1×4090): 同上路径。历史环境问题多（无 .git, 旧 cache 路径），尽量只跑简单 eval
- **SmolVLA checkpoints**: `/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt` (obs_only), `perdof/crm_best.pt` (perdof)
- **K=1 ACCG checkpoint**: `/root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt` (fallback 单层 960D, negative)
- **K=1 multi-scale checkpoint**: train-crm-k1-accg-object-seed42-v2 训练产出（4×960D from layers [3,7,11,15]）
- **活跃 cron 监控** (14 个实验，全部 RUNNING with PID)：
  - eval-perdof-object-norm02-seed46 (PID 389051)
  - eval-perdof-object-norm01-seed47-bjb1 (PID 414817)
  - eval-obs-only-object-norm03-seed46 (PID 416568)
  - eval-perdof-object-norm01-seed46-r2 (PID 393646)
  - eval-obs-only-object-default-seed46 (PID 422357)
  - eval-perdof-object-default-seed46 (PID 423767)
  - eval-obs-only-object-norm005-seed43-r2 (PID 433500)
  - eval-perdof-object-norm02-seed47 (PID 404983)
  - eval-random-selection-object-seed42 (PID 395256)
  - eval-k1-crm-multiscale-object-seed43-r2 (PID 702904)
  - eval-k1-crm-multiscale-object-seed44-r2 (PID 703107)
  - eval-obs-only-object-norm01-seed46 (刚创建)
  - eval-obs-only-object-norm01-seed47 (刚创建)
  - eval-perdof-object-norm02-seed43-r3 (刚创建)
- **活跃 Worker**: `worker_fix_openvla-official-eval_20260517T191031` (修复 OpenVLA 0% SR bug)

### 3. 📊 当前状态
**刚做完**: 上一个 session 部署了大量 magnitude curve 多 seed 补充实验 + K=1 multi-scale eval + OpenVLA bug 修复 worker。17/17 GPU 全满。

**已锁定结论**:
- K=10 obs_only vs argmin: 17.5% vs 12.3%, Fisher p=0.0074 ✅ (Table 1 数据定稿)
- Magnitude sweep: obs_only 稳定 15-17.5%, perdof 崩塌到 0% ✅ (Figure 2 基础数据)
- K=1 fallback (单层 960D): 10.0% ≈ VLA-only 10.8%, 无增益 (D050)
- Direct correction ablation: 14% < obs_only 22%, CRM 价值在 selection 不在 correction

**正在等待**:
1. **14 个 cron 监控实验完成回调** — 主要是 magnitude curve 多 seed 补点 + K=1 multi-scale eval (seed43/44) + random selection baseline
2. **Worker `worker_fix_openvla-official-eval`** — 修复 transformers 5.8 DynamicCache bug 导致 OpenVLA 0% SR
3. **Director 决策**: multi-scale eval seed42 结果出来后需判断 framing 分叉（>13% → Scenario A; ≤11% → Scenario B）

### 4. 📋 待办（条件触发式）
- eval-k1-crm-multiscale-object-seed43-r2 / seed44-r2 完成 → 收集 3-seed mean → 如 mean > 13% 汇报 Director "K=1 multi-scale 有效, Scenario A"；如 ≤ 11% 汇报 "Claim 1 改为 mechanism insight, Scenario B"
- worker_fix_openvla-official-eval 完成 → 检查修复是否成功 → 成功则部署 OpenVLA VLA-only baseline (plan_801 重跑) → 失败则汇报 Director 评估降级 Claim 3
- eval-random-selection-object-seed42 完成 → 收集 SR → 预期远低于 obs_only，确认 CRM selection 非随机优势
- magnitude curve 各 seed 实验陆续完成 → 更新 Figure 2 multi-seed 均值±stderr → 当所有 norm 点都有 ≥3 seeds 时锁定 Figure 2
- OpenVLA baseline 修复后 → plan_802 (OpenVLA + K=1 CRM) → plan_803 (OpenVLA magnitude sweep)
- 所有 must-do 实验完成后 → 开始论文写作（abstract DDL ~May 26，仅剩 ~9 天）

### 5. 🎯 战略上下文
**核心 narrative (D049, Narrative B+)**: obs_only CRM 通过 observation embedding 的 uncertainty signal 做 sample selection，单步纠正 frozen VLA。三个 claims: (1) K=1 单采样纠正实用性, (2) conditioning-magnitude interaction insight, (3) 跨 VLA (SmolVLA + OpenVLA) 泛化。K=10 结果降为 supplementary。

**决策链关键节点**:
- D043: Narrative B 锁定（4-seed Fisher p=0.11 不够，后扩至 6-seed p=0.0074 才过）
- D049: 用户确认方向——K=1 重设计 + OpenVLA 验证
- D050: K=1 fallback negative，推动 multi-scale ACCG 设计

**最容易判断错的事**:
1. **K=1 multi-scale eval 结果的 framing 分叉**——不要急于下结论。seed42 单个结果不够，必须等 3-seed mean。seed42 是 obs_only K=10 的 outlier high (22% vs mean 17.5%)，K=1 可能也有类似偏高
2. **OpenVLA 0% 不是 CRM 问题**——是 transformers 5.8 DynamicCache bug 导致图像根本没被处理。修复方向是 patch generate() 的 cache handling，不要去动 CRM 代码
3. **perdof 已死**——全 norm 范围 perdof 都差于或等于 argmin，不要再投 GPU 给 perdof 探索。当前跑的 perdof seed 实验只为 Figure 2 error bars 完整性
4. **时间极紧**——CoRL abstract DDL ~May 26 (9天), full paper ~Jun 2 (16天)。实验窗口实际只剩 ~5 天，之后必须全力写论文

## 项目硬约束 (memory.md 节选)

## bjb2-40593 环境问题 (2026-05-14-15)

- 无 .git repo
- CRM cache 路径 /root/autodl-tmp/crm_cache/spatial/（旧路径，非 v5）
- Ghost PID 211962 已 kill
- scalar seed44 OOM SIGKILL（系统 RAM，非 GPU OOM）— 已在 bjb1-32546 重试

## [失败模式] submit_training_job EXIT_CODE=127 (2026-05-15)

tmux 用 `sh` 而非 `bash` 执行命令，`python` 等 conda/venv 命令不在 `sh` PATH 中。修复：命令必须用 `bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ..."` 包裹。裸 `python -u ...` 有时可行（取决于服务器 PATH 配置），但不可靠。

## [失败模式] EXIT_CODE=129 (SIGHUP) ≠ 真正失败 (2026-05-16)

**案例**: eval-argmin-object-seed44-r2 和 crm-train-v1 都报 EXIT_CODE=129，但实验已完成并保存了完整结果。
**根因**: tmux session 在主进程正常退出后收到 SIGHUP（终端断开或 session 被清理）。
**规则**: EXIT_CODE=129 时不要直接判定失败。先查日志末尾确认是否已打印 "Results saved" / 完成信息，再检查输出文件完整性。如果都正常，标记 conclusion=success。

## [失败模式] Kill 操作前必须逐参数比对 (2026-05-15)

**事故**: Worker 将 norm=0.3 (norm03) 误判为 norm=0.03 (norm003) 的重复实验，kill 了有效进程。cuda:0 空闲 9 小时。
**根因**: Worker 只看 session 名和 output_file 路径，未核对 `--max_correction_norm` 参数值。
**规则**: kill 实验前必须 `ps aux | grep` 完整命令行，逐项比对关键参数（mode, norm, checkpoint, benchmark）。名字相似 ≠ 同一实验。

## [失败模式] pooled_fisher_test.py 翻倍 bug (2026-05-16)

**事故**: 脚本 KNOWN_DATA 将所有 counts ×2（假设 n_rollouts=20），输出 p=0.035（实际 p=0.110）。差点导致错误切换到 Narrative A。
**规则**: 统计检验必须从 raw JSON 读取实际 trial counts，不能硬编码假设。任何 p<0.05 结果必须交叉验证（检查 N 是否与 registry 一致）。

## [部署规范] GPU 冲突防范 (2026-05-16)

**事故**: bjb2-28827 cuda:2/cuda:3 上多次出现双进程共存，互相竞争 compute，效率降低 ~50%。同一 output file 被两进程写入导致数据损坏。
**根因**: 部署命令未显式指定 CUDA_VISIBLE_DEVICES，或未确认目标 GPU 无已有进程。
**规则**:
1. 所有部署命令必须显式设 `CUDA_VISIBLE_DEVICES=N`
2. 部署前先 `nvidia-smi -i N` 确认目标 GPU 无进程
3. 部署后 20s 内验证进程在目标 GPU 上启动
4. 一张 GPU 只跑一个评估实验（除非 Director 明式批准共享）

## [失败模式] bjb1-18228 无法直接访问 huggingface.co (2026-05-17)

**症状**: `urllib.request.urlopen('https://huggingface.co/...')` 报 `Cannot assign requested address`
**根因**: 中国 AutoDL 服务器网络限制
**解决**: 必须设 `HF_ENDPOINT=https://hf-mirror.com`（~/.bashrc 已配置）。background/nohup 进程需手动 `source ~/.bashrc` 或显式 export。`huggingface-cli` 已废弃，用 `hf` 或 Python `huggingface_hub` API。

## 可查的历史
前 137 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
完整聊天归档可用 `recall_session_history("关键词")` 搜索。

## 第一个动作要求
1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）
2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-17T19:13:18.336469+00:00_

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
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
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

_source line 3 · 2026-05-17T19:13:18.337000+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-17T19:13:22.853306+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'RUNNING'}",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'RUNNING'}",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T19:13:23.457218+00:00_

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
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T19:13:23.457854+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-obs-only-object-norm02-k20-seed42\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-17T13:34:42.612Z\", \"updated_at\": \"2026-05-17T18:55:07.926Z\", \"hypothesis\": \"obs_only CRM (ε=0.2, K=20) seed42 on LIBERO-Object. K sweep 实验：K=20 vs K=10 (22%) 比较，验证增加 candidate 数量是否带来额外增益。若 K=20 ≈ K=10，说明 K=10 已接近饱和。\"}, \"eval-obs-only-object-norm02-k5-seed42\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-17T13:34:40.971Z\", \"updated_at\": \"2026-05-17T18:55:05.653Z\", \"hypothesis\": \"obs_only CRM (ε=0.2, K=5) seed42 on LIBERO-Object. K sweep 实验：K=5 vs K=10 (22%) 比较，验证 sample count 对 selection quality 的影响。若 K=5 显著低于 K=10，说明足够的 candidate 多样性对 CRM selection 关键。\"}, \"eval-k1-crm-multiscale-object-seed44-r2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-17T18:40:32.365Z\", \"updated_at\": \"2026-05-17T18:41:35.657Z\", \"hypothesis\": \"K=1 CRM with ACCG (multi-scale 4×960D) on LIBERO-Object seed44. Parallel deployment on bjb1-18228. Parent: train-crm-k1-accg-object-seed42-v2\", \"parent\": \"train-crm-k1-accg-object-seed42-v2\"}, \"eval-k1-crm-multiscale-object-seed43-r2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-17T18:40:31.417Z\", \"updated_at\": \"2026-05-17T18:41:33.191Z\", \"hypothesis\": \"K=1 CRM with ACCG (multi-scale 4×960D) on LIBERO-Object seed43. Parallel deployment on bjb1-18228. Parent: train-crm-k1-accg-object-seed42-v2\", \"parent\": \"train-crm-k1-accg-object-seed42-v2\"}, \"eval-k1-crm-multiscale-object-seed44\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-17T18:34:14.132Z\", \"updated_at\": \"2026-05-17T18:35:03.255Z\", \"hypothesis\": \"K=1 CRM with ACCG (multi-scale 4x960D from layers [3,7,11,15]) on LIBERO-Object seed44. Compare with fallback (single-stage) and VLA-only baseline (10.8%). Multi-scale features enable layer-wise importance weighting for more informative correction signals.\", \"parent\": \"train-crm-k1-accg-object-seed42-v2\"}, \"eval
…[truncated 3820 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 604
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T19:13:23.862440+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "file": "report.md"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-17T19:13:23.862834+00:00_

called mcp__agent-ml-research__read_roadmap

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap</summary>

```json
{
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-17T19:13:47.139572+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 13, \"results\": [{\"exp_id\": \"eval-perdof-object-norm02-seed46\", \"success\": true, \"actions\": [\"Job still running (pid=389051)\"]}, {\"exp_id\": \"eval-perdof-object-norm01-seed47-bjb1\", \"success\": true, \"actions\": [\"Job still running (pid=414817)\"]}, {\"exp_id\": \"eval-obs-only-object-norm03-seed46\", \"success\": true, \"actions\": [\"Job still running (pid=416568)\"]}, {\"exp_id\": \"eval-perdof-object-norm01-seed46-r2\", \"success\": true, \"actions\": [\"Job still running (pid=393646)\"]}, {\"exp_id\": \"eval-obs-only-object-default-seed46\", \"success\": true, \"actions\": [\"Job still running (pid=422357)\"]}, {\"exp_id\": \"eval-perdof-object-default-seed46\", \"success\": true, \"actions\": [\"Job still running (pid=423767)\"]}, {\"exp_id\": \"eval-obs-only-object-norm005-seed43-r2\", \"success\": true, \"actions\": [\"Job still running (pid=433500)\"]}, {\"exp_id\": \"eval-perdof-object-norm02-seed47\", \"success\": true, \"actions\": [\"Job still running (pid=404983)\"]}, {\"exp_id\": \"eval-random-selection-object-seed42\", \"success\": true, \"actions\": [\"Job still running (pid=395256)\"]}, {\"exp_id\": \"eval-k1-crm-multiscale-object-seed43-r2\", \"success\": true, \"actions\": [\"Job still running (pid=702904)\"]}, {\"exp_id\": \"eval-k1-crm-multiscale-object-seed44-r2\", \"success\": true, \"actions\": [\"Job still running (pid=703107)\"]}, {\"exp_id\": \"eval-obs-only-object-norm01-seed46\", \"success\": true, \"actions\": [\"Skipped (created 166s ago < interval 1200s)\"]}, {\"exp_id\": \"eval-perdof-object-norm02-seed43-r3\", \"success\": true, \"actions\": [\"Skipped (created 166s ago < interval 1200s)\"]}]}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 23682
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T19:13:47.140757+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-17T19:11:20Z; do not edit — regenerated by auto_build_report_facts) -->\\n## 📊 当前状态（auto-derived from registry）\\n\\n**总计**: 214 个实验 — DEPLOYED 1, DONE 185, PREPARING 12, RUNNING 16\\n**DONE 分布**: failed 31, killed 62, negative 17, success 75\\n\\n### GPU 占用\\n- **实际运行**: 12 张 — bjb1-32546:cuda:4(eval-perdof-object-norm01-seed46-r2), bjb1-32546:cuda:1(eval-perdof-object-norm01-seed47-bjb1), bjb1-32546:cuda:2(eval-obs-only-object-norm03-seed46), bjb2-28827:cuda:4(eval-perdof-object-norm02-seed46), bjb1-32546:cuda:3(eval-obs-only-object-default-seed46), bjb1-32546:cuda:5(eval-perdof-object-default-seed46), bjb1-32546:cuda:0(eval-obs-only-object-norm005-seed43-r2), bjb2-28827:cuda:2(eval-perdof-object-norm02-seed47), bjb2-40593:cuda:0(eval-random-selection-object-seed42), bjb2-28827:cuda:0(eval-k1-crm-multiscale-object-seed42), bjb1-32546:cuda:1(eval-k1-crm-multiscale-object-seed43), bjb1-32546:cuda:4(eval-k1-crm-multiscale-object-seed44)\\n\\n### 💾 磁盘余量\\n- **bjb2-40593**:\\n  - `/init`: 150M/150M 可用（已用 0%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 48G/437G 可用（已用 89%）\\n- **bjb1-18228**:\\n  - `/autodl-pub`: 1.3T/7.0T 可用（已用 83%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 400G/438G 可用（已用 4%）\\n- **bjb1-32546**:\\n  - `/autodl-pub`: 912G/7.0T 可用（已用 88%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 400G/438G 可用（已用 4%）\\n- **bjb2-28827**:\\n  - `/autodl-pub`: 3.7T/14T 可用（已用 74%）\\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\\n  - `/usr/bin/nvidia-smi`: 399G/439G 可用（已用 5%）\\n\\n### 🏃 RUNNING\\n| exp_id | server | gpu | pid | log |\\n|--------|--------|-----|-----|-----|\\n| `eval-perdof-object-norm01-seed46-r2` | bjb1-32546 | cuda:4 | 393646 | `—` |\\n| `eval-perdof-object-n
…[truncated 9384 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 23278
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-17T19:13:47.144449+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-17 18:33 UTC | 更新原因: 修正 GPU 总量 (22→17)、更新 plan_701 完成/plan_702 运行中/plan_801 根因定位、OpenVLA DynamicCache bug\\n\\n## 核心方向\\n**Narrative B+ (D049)**：obs_only CRM 单步纠正 frozen VLA。核心贡献：(1) K=1 单采样纠正（实用性），(2) conditioning-magnitude interaction insight，(3) 跨 VLA 验证（SmolVLA + OpenVLA）。K=10 结果作 supplementary。详见 paper_framing.md。\\n\\n## 投稿目标\\n**CoRL 2026**（abstract DDL ~May 26, full paper DDL ~Jun 2）。剩余 ~9 天 / ~16 天。\\n\\n## 当前进展\\n- **阶段**: K=1 multi-scale eval 中 + OpenVLA bug 修复中\\n- **K=10 已锁定**: obs_only 17.5% vs argmin 12.3%, Fisher p=0.0074 ✅（supplementary）\\n- **Magnitude sweep 已锁定**: obs_only 稳定 15-17.5%, perdof 崩塌 14%→0% ✅\\n- **D050**: K=1 ACCG fallback (1×960D) = VLA-only (10.0% vs 10.8%)，无增益\\n- **plan_700 ✅**: ACCG 架构设计完成（327K params, 4-layer hooks, action-conditioned gating）\\n- **plan_701 ✅**: multi-scale 训练完成（val_loss=0.007199，比 fallback 0.006505 高 10.7%）\\n- **plan_702 🔄**: multi-scale eval seed42 运行中（bjb2-28827 cuda:0），seed43/44 等 GPU 释放\\n- **plan_801 ❌**: OpenVLA 0% SR — 根因已定位：transformers 5.8 的 DynamicCache bug 导致图像未被处理，Worker 修复中\\n- **GPU**: 17/17 全满\\n\\n## D049 MUST-DO 进度\\n\\n| ID | 任务 | 状态 | 备注 |\\n|----|------|------|------|\\n| plan_700 | K=1 CRM 架构设计 | ✅ DONE | ACCG, Reviewer PASS |\\n| plan_701 | K=1 CRM 训练 (SmolVLA) | ✅ DONE | val_loss=0.007199 |\\n| plan_702 | K=1 CRM eval (≥3 seeds) | 🔄 seed42运行中 | seed43/44 等 GPU |\\n| plan_800 | OpenVLA 环境搭建 | ✅ DONE | 4 patches |\\n| plan_801 | OpenVLA VLA-only baseline | ❌ 0% (bug) | 根因: transformers 5.8 DynamicCache，修复中 |\\n| plan_802 | OpenVLA + K=1 CRM | ⏳ 等 801 修复 | |\\n| plan_803 | OpenVLA magnitude sweep | ⏳ 等 802 | |\\n\\n## 关键决策待定\\n\\n1. **Multi-scale eval → framing 分叉**（seed42 结果 ~数小时内）：\\n   - 3-seed mean > 13% → Scenario A: K=1 multi-scale 有效\\n   - 3-see
…[truncated 2804 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 23281
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-17T19:14:25.242544+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__get_worker_status,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__read_registry",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__get_worker_status,mcp__agent-ml-research__list_workers,mcp__agent-ml-research__read_registry",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-17T19:14:25.303975+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "ToolSearch",
  "elapsed_ms": 61
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-17T19:14:28.247294+00:00_

called mcp__agent-ml-research__list_workers

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_workers</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "status": "running",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "mcp__agent-ml-research__list_workers",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "status": "running",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-17T19:14:28.398181+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_fix_openvla-official-eval_20260517T191031\", \"task_type\": \"fix:openvla-official-eval\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"running\", \"started_at\": \"2026-05-17T19:10:31.602435+00:00\", \"ended_at\": null}], \"count\": 1}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 150
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-17T19:14:29.300787+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'conclusion': 'killed'}",
  "limit": "5",
  "fields": "['status', 'conclusion', 'metrics', 'failure_reason', 'updated_at', 'hypothesis']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'conclusion': 'killed'}",
    "limit": "5",
    "fields": "['status', 'conclusion', 'metrics', 'failure_reason', 'updated_at', 'hypothesis']"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-17T19:14:30.555335+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-obs-only-object-norm01-seed47\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T19:14:25.783Z\", \"hypothesis\": \"obs_only CRM (ε=0.1) seed=47 on LIBERO Object. 4th seed for magnitude curve low-norm point. Combined with seeds 42/45/46, provides error bar for obs_only at ε=0.1. Supports robustness narrative (obs_only stable across all norms).\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm02-seed45-r2\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T18:37:21.561Z\", \"hypothesis\": \"perdof CRM (ε=0.2) seed45 on LIBERO-Object. 补充 Figure 2 perdof magnitude curve ε=0.2 数据（seed42=11%, seed43=9%, seed44 running）。\", \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm005-seed43-r3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T18:37:20.319Z\", \"hypothesis\": \"obs_only CRM (ε=0.05) seed43 on LIBERO-Object. M006 补救重跑。seed42 ε=0.05=13%。\", \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"conclusion\": \"killed\"}, \"eval-obs-only-object-norm005-seed43\": {\"status\": \"PREPARING\", \"updated_at\": \"2026-05-17T13:54:04.955Z\", \"hypothesis\": \"obs_only CRM (ε=0.05) seed43 on LIBERO-Object. M006 补救：补充 magnitude curve 低 norm 段多 seed 数据。seed42 ε=0.05=13%。\", \"conclusion\": \"killed\"}, \"eval-perdof-object-norm02-seed45-deploy\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-17T13:52:58.983Z\", \"hypothesis\": \"perdof CRM (ε=0.2) seed45 on LIBERO-Object. 补充 Figure 2 perdof magnitude curve ε=0.2 数据（seed42=11%, seed43=9%, seed44 running）。\", \"failure_reason\": \"**根因**: MuJoCo EGL 渲染初始化 segfault（native crash）。\\n\\n**证据**:\\n- tmux 日志和应用日志均在 `[eval] 10 tasks loaded.` 后中断，无 Python traceback、无 segfault handler 输出\\n- 代码中有 SIGSEGV handler 但未被触发，说明崩溃发生在 native code（MuJoCo/EGL）且 handler 未能执行\\n- 同服务器多个实验表现相同模式（eval_object_obs_only_norm03_seed47、eval_object_perdof_norm01_seed47 等均在 \\\"10 tasks loaded\\\" 后死亡）\\n- 非 OOM：系统 R
…[truncated 516 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1254
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-17T19:14:30.605964+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'exp_id': 'eval-k1-crm-multiscale-object-seed42'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'exp_id': 'eval-k1-crm-multiscale-object-seed42'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-17T19:14:31.158413+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5194}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 552
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-17T19:15:30.311500+00:00_

called mcp__agent-ml-research__get_worker_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_worker_status</summary>

```json
{
  "worker_id": "worker_fix_openvla-official-eval_20260517T191031",
  "verbose": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "tool_args": {
    "worker_id": "worker_fix_openvla-official-eval_20260517T191031",
    "verbose": "True"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-17T19:15:30.764466+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_fix_openvla-official-eval_20260517T191031\", \"status\": \"running\", \"task_type\": \"fix:openvla-official-eval\", \"project\": \"acr-vla-conformal-refinement\", \"started_at\": \"2026-05-17T19:10:31.602435+00:00\", \"ended_at\": null, \"setup\": null, \"teardown\": null, \"setup_data\": {}, \"progress\": {\"recent_tools\": [\"ssh_execute\", \"ssh_execute\", \"ssh_execute\", \"ssh_execute\", \"ssh_execute\"], \"last_text\": \"Clone 仍在后台运行。同时开始在 conda env 中安装 PyTorch 和 transformers。\", \"turn_count\": 32}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "mcp__agent-ml-research__get_worker_status",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-17T19:15:31.417341+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": "{'status': 'RUNNING'}",
  "fields": "['status', 'spec', 'updated_at', 'hypothesis']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "filters": "{'status': 'RUNNING'}",
    "fields": "['status', 'spec', 'updated_at', 'hypothesis']"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-17T19:15:32.021994+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval-obs-only-object-norm02-k20-seed42\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-17T18:55:07.926Z\", \"hypothesis\": \"obs_only CRM (ε=0.2, K=20) seed42 on LIBERO-Object. K sweep 实验：K=20 vs K=10 (22%) 比较，验证增加 candidate 数量是否带来额外增益。若 K=20 ≈ K=10，说明 K=10 已接近饱和。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 20 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_k20_seed42.json\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only_v3_norm\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}}, \"eval-obs-only-object-norm02-k5-seed42\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-17T18:55:05.653Z\", \"hypothesis\": \"obs_only CRM (ε=0.2, K=5) seed42 on LIBERO-Object. K sweep 实验：K=5 vs K=10 (22%) 比较，验证 sample count 对 selection quality 的影响。若 K=5 显著低于 K=10，说明足够的 candidate 多样性对 CRM selection 关键。\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --mode crm_obs_only --benchmark object --n_rollouts 10 --seed 42 --K 5 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.2 --output_file logs/eval_object_obs_only_norm02_k5_seed42.json\", \"server\": \"bjb1-18228\", \"data_path\": \"LIBERO-Object\", \"data_count\": 100, \"model_name\": \"SmolVLA+CRM_obs_only_v3_norm\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt\", \"eval_data\": \"LIBERO-Object (10 tasks x 10 rollouts)\"}}, \"eval-k1-crm-multiscale-object-seed44-r2\": {\"status\": \"RUNNING\", \"updated_at\": \"2026-05-17T18:41:35.657Z\", \"
…[truncated 12725 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 604
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-17T19:16:18.820522+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__register_cron,mcp__agent-ml-research__update_registry",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__spawn_worker,mcp__agent-ml-research__register_cron,mcp__agent-ml-research__update_registry",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-17T19:16:18.882442+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "ToolSearch",
  "elapsed_ms": 61
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-17T19:17:01.781528+00:00_

called mcp__agent-ml-research__spawn_worker

<details open><summary>🔧 Tool call — mcp__agent-ml-research__spawn_worker</summary>

````json
{
  "task_type": "investigate:stale-running-and-exit129",
  "project": "acr-vla-conformal-refinement",
  "task_prompt": "## 任务：调查多个服务器上的实验状态\n\n你需要 SSH 到 3 台服务器，检查以下问题并汇报结果。\n\n### 服务器信息\n- bjb2-28827: 工作目录 `/root/acr-vla-conformal-refinement`\n- bjb1-32546: 工作目录 `/root/acr-vla-conformal-refinement`\n- bjb1-18228: 工作目录 `/root/acr-vla-conformal-refinement`\n\n### 检查 1：原始 multiscale 实验 PID 是否存活\n\n这些实验在 registry 中标记为 RUNNING，但没有 cron 监控。需要确认 PID 是否还在：\n\n- **bjb2-28827**: PID 455518 (eval-k1-crm-multiscale-object-seed42)\n  - 命令: `ps aux | grep 455518`\n  - 如果不存在: 检查输出文件 `logs/eval_k1_crm_multiscale_object_seed42.log` 末尾 50 行\n  - 同时检查 `/root/acr-vla-conformal-refinement/logs/` 下是否有 `eval_k1_crm_multiscale_object_seed42*.json` 结果文件\n\n- **bjb1-32546**: PID 503178 (eval-k1-crm-multiscale-object-seed43) 和 PID 504682 (eval-k1-crm-multiscale-object-seed44)\n  - 分别 `ps aux | grep PID`\n  - 如果不存在: 检查 `logs/eval_k1_crm_multiscale_object_seed43.log` 和 `logs/eval_k1_crm_multiscale_object_seed44.log` 末尾\n  - 同时检查是否有对应 JSON 结果文件\n\n### 检查 2：K sweep 实验状态（无 cron 监控）\n\n- **bjb1-18228**: 两个 K sweep 实验在此服务器运行，但没有 cron。\n  - `ps aux | grep evaluate.py` 查看所有评估进程\n  - 检查 `logs/eval_object_obs_only_norm02_k5_seed42.json` 是否存在且有结果\n  - 检查 `logs/eval_object_obs_only_norm02_k20_seed42.json` 是否存在且有结果\n  - 如果进程还在跑，记录 PID\n\n### 检查 3：EXIT_CODE=129 实验是否实际完成\n\nEXIT_CODE=129 可能是 SIGHUP，进程可能已正常完成。需检查输出文件。\n\n实验列表:\n1. **eval-perdof-object-norm02-seed45-r2**: 输出文件应为 `logs/eval_object_perdof_norm02_seed45*.json`\n2. **eval-obs-only-object-norm005-seed43-r3**: 输出文件应为 `logs/eval_object_obs_only_norm005_seed43*.json`\n3. **eval-obs-only-object-norm01-seed47**: 输出文件应为 `logs/eval_object_obs_only_norm01_seed47*.json`\n\n对每个: 在所有 3 台服务器上 `find logs/ -name \"*相关关键词*\" -newer /etc/hostname` 搜索。找到后 `cat` 文件内容（JSON 结果文件通常包含 success_rate 等指标）。同时检查日志文件末尾是否有 \"Results saved\" 或类似完成标志。\n\n### 检查 4：Checkpoint 文件验证\n\n- **bjb2-28827**: `ls -la /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt`\n- **bjb1-32546**: `ls -la /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best_multiscale.pt` 和 `ls -la /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt`\n  - 比较文件大小，判断是否相同文件\n\n### 检查 5：GPU 占用实况\n\n每台服务器运行 `nvidia-smi --query-gpu=index,utilization.gpu,memory.used,memory.total --format=csv,noheader` 查看 GPU 实际占用。\n\n### 输出格式\n\n请用以下格式汇报每项检查结果:\n```\n## 检查 1: 原始 multiscale PID 状态\n- bjb2-28827 PID 455518: [存活/已退出] [如有结果文件, 写内容摘要]\n- bjb1-32546 PID 503178: [存活/已退出] [...]\n- bjb1-32546 PID 504682: [存活/已退出] [...]\n\n## 检查 2: K sweep 状态\n- k5 (bjb1-18228): [运行中 PID=xxx / 已完成 SR=xx% / 不存在]\n- k20 (bjb1-18228): [运行中 PID=xxx / 已完成 SR=xx% / 不存在]\n\n## 检查 3: EXIT_CODE=129 实验结果\n- eval-perdof-object-norm02-seed45-r2: [有结果 SR=xx% / 无结果文件]\n- eval-obs-only-object-norm005-seed43-r3: [有结果 SR=xx% / 无结果文件]\n- eval-obs-only-object-norm01-seed47: [有结果 SR=xx% / 无结果文件]\n\n## 检查 4: Checkpoint 对比\n- crm_k1_best.pt: [size] on [servers]\n- crm_k1_best_multiscale.pt: [size] on [servers]\n- 判断: [相同/不同]\n\n## 检查 5: GPU 占用\n[每台服务器 nvidia-smi 输出]\n```\n",
  "tool_groups": "['ssh']",
  "tools": "['read_registry']"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "tool_args": {
    "task_type": "investigate:stale-running-and-exit129",
    "project": "acr-vla-conformal-refinement",
    "task_prompt": "## 任务：调查多个服务器上的实验状态\n\n你需要 SSH 到 3 台服务器，检查以下问题并汇报结果。\n\n### 服务器信息\n- bjb2-28827: 工作目录 `/root/acr-vla-conformal-refinement`\n- bjb1-32546: 工作目录 `/root/acr-vla-conformal-refinement`\n- bjb1-18228: 工作目录 `/root/acr-vla-conformal-refinement`\n\n### 检查 1：原始 multiscale 实验 PID 是否存活\n\n这些实验在 registry 中标记为 RUNNING，但没有 cron 监控。需要确认 PID 是否还在：\n\n- **bjb2-28827**: PID 455518 (eval-k1-crm-multiscale-object-seed42)\n  - 命令: `ps aux | grep 455518`\n  - 如果不存在: 检查输出文件 `logs/eval_k1_crm_multiscale_object_seed42.log` 末尾 50 行\n  - 同时检查 `/root/acr-vla-conformal-refinement/logs/` 下是否有 `eval_k1_crm_multiscale_object_seed42*.json` 结果文件\n\n- **bjb1-32546**: PID 503178 (eval-k1-crm-multiscale-object-seed43) 和 PID 504682 (eval-k1-crm-multiscale-object-seed44)\n  - 分别 `ps aux | grep PID`\n  - 如果不存在: 检查 `logs/eval_k1_crm_multiscale_object_seed43.log` 和 `logs/eval_k1_crm_multiscale_object_seed44.log` 末尾\n  - 同时检查是否有对应 JSON 结果文件\n\n### 检查 2：K sweep 实验状态（无 cron 监控）\n\n- **bjb1-18228**: 两个 K sweep 实验在此服务器运行，但没有 cron。\n  - `ps aux | grep evaluate.py` 查看所有评估进程\n  - 检查 `logs/eval_object_obs_only_norm02_k5_seed42.json` 是否存在且有结果\n  - 检查 `logs/eval_object_obs_only_norm02_k20_seed42.json` 是否存在且有结果\n  - 如果进程还在跑，记录 PID\n\n### 检查 3：EXIT_CODE=129 实验是否实际完成\n\nEXIT_CODE=129 可能是 SIGHUP，进程可能已正常完成。需检查输出文件。\n\n实验列表:\n1. **eval-perdof-object-norm02-seed45-r2**: 输出文件应为 `logs/eval_object_perdof_norm02_seed45*.json`\n2. **eval-obs-only-object-norm005-seed43-r3**: 输出文件应为 `logs/eval_object_obs_only_norm005_seed43*.json`\n3. **eval-obs-only-object-norm01-seed47**: 输出文件应为 `logs/eval_object_obs_only_norm01_seed47*.json`\n\n对每个: 在所有 3 台服务器上 `find logs/ -name \"*相关关键词*\" -newer /etc/hostname` 搜索。找到后 `cat` 文件内容（JSON 结果文件通常包含 success_rate 等指标）。同时检查日志文件末尾是否有 \"Results saved\" 或类似完成标志。\n\n### 检查 4：Checkpoint 文件验证\n\n- **bjb2-28827**: `ls -la /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt`\n- **bjb1-32546**: `ls -la /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best_multiscale.pt` 和 `ls -la /root/autodl-tmp/checkpoints/crm_k1/crm_k1_best.pt`\n  - 比较文件大小，判断是否相同文件\n\n### 检查 5：GPU 占用实况\n\n每台服务器运行 `nvidia-smi --query-gpu=index,utilization.gpu,memory.used,memory.total --format=csv,noheader` 查看 GPU 实际占用。\n\n### 输出格式\n\n请用以下格式汇报每项检查结果:\n```\n## 检查 1: 原始 multiscale PID 状态\n- bjb2-28827 PID 455518: [存活/已退出] [如有结果文件, 写内容摘要]\n- bjb1-32546 PID 503178: [存活/已退出] [...]\n- bjb1-32546 PID 504682: [存活/已退出] [...]\n\n## 检查 2: K sweep 状态\n- k5 (bjb1-18228): [运行中 PID=xxx / 已完成 SR=xx% / 不存在]\n- k20 (bjb1-18228): [运行中 PID=xxx / 已完成 SR=xx% / 不存在]\n\n## 检查 3: EXIT_CODE=129 实验结果\n- eval-perdof-object-norm02-seed45-r2: [有结果 SR=xx% / 无结果文件]\n- eval-obs-only-object-norm005-seed43-r3: [有结果 SR=xx% / 无结果文件]\n- eval-obs-only-object-norm01-seed47: [有结果 SR=xx% / 无结果文件]\n\n## 检查 4: Checkpoint 对比\n- crm_k1_best.pt: [size] on [servers]\n- crm_k1_best_multiscale.pt: [size] on [servers]\n- 判断: [相同/不同]\n\n## 检查 5: GPU 占用\n[每台服务器 nvidia-smi 输出]\n```\n",
    "tool_groups": "['ssh']",
    "tools": "['read_registry']"
  }
}
````

</details>

---

### Tool result

_source line 27 · 2026-05-17T19:17:04.697799+00:00_

{"result":"{\"success\": true, \"data\": {\"worker_id\": \"worker_investigate_stale-running-and-exit129_20260517T191702\", \"status\": \"running\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_investigate_stale-running-and-exit129_20260517T191702.log\", \"setup_data\": {}, \"message\": \"Worker worker_investigate_stale-running-and-exit129_20260517T191702 started. Use get_worker_status('worker_investigate_stale-running-and-exit129_20260517T191702') to check progress.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "mcp__agent-ml-research__spawn_worker",
  "elapsed_ms": 2916
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-17T19:17:39.882197+00:00_

called mcp__agent-ml-research__main_agent_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__main_agent_post_to_director</summary>

```json
{
  "text": "[资源] GPU 13-17/17 (实际占用待确认，调查 Worker 已派) | Worker 2 (GPU 0 / CPU 2) | 磁盘: bjb2-28827 399G可用(5%), bjb1-32546 400G(4%), bjb1-18228 400G(4%), bjb2-40593 48G(89%)\n\n**Loop #20 Session 启动汇报**\n\n## 实验状态\n- **Registry RUNNING**: 16 个实验\n- **Cron 监控**: 13 个活跃 cron（11 确认在跑，2 刚创建跳过首检）\n- **无 Cron 的 RUNNING 实验**: 5 个（原始 multiscale seed42/43/44 + K sweep k5/k20）— 已派调查 Worker\n\n## 活跃 Worker\n1. **OpenVLA 修复** (worker_fix_openvla-official-eval): turn 32，正在安装 PyTorch/transformers conda env\n2. **调查 Worker** (刚派): 检查 stale PID、EXIT_CODE=129 实验、GPU 冲突、checkpoint 一致性\n\n## 发现的问题（调查中）\n1. **GPU 冲突风险**: bjb1-32546 cuda:1/cuda:4 上原始 multiscale 实验 (seed43/44) 与 perdof 实验共享 GPU。-r2 版本已在 bjb1-18228 重新部署，原始版本可能已退出但 registry 未更新\n2. **K sweep 无 cron**: bjb1-18228 上 k5/k20 实验运行 ~5.5h 无监控，Worker 将确认 PID 后注册 cron\n3. **3 个 EXIT_CODE=129 实验**: eval-perdof-object-norm02-seed45-r2、eval-obs-only-object-norm005-seed43-r3、eval-obs-only-object-norm01-seed47 — 标记为 killed 但可能已完成，Worker 检查输出文件\n\n## 关键等待项（不变）\n1. K=1 multi-scale 3-seed mean → framing 分叉决策\n2. OpenVLA bug 修复 → Claim 3\n3. Magnitude curve 多 seed 补点 → Figure 2\n\n调查 Worker 完成后将更新 registry 并再次汇报具体数据。",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "tool_args": {
    "text": "[资源] GPU 13-17/17 (实际占用待确认，调查 Worker 已派) | Worker 2 (GPU 0 / CPU 2) | 磁盘: bjb2-28827 399G可用(5%), bjb1-32546 400G(4%), bjb1-18228 400G(4%), bjb2-40593 48G(89%)\n\n**Loop #20 Session 启动汇报**\n\n## 实验状态\n- **Registry RUNNING**: 16 个实验\n- **Cron 监控**: 13 个活跃 cron（11 确认在跑，2 刚创建跳过首检）\n- **无 Cron 的 RUNNING 实验**: 5 个（原始 multiscale seed42/43/44 + K sweep k5/k20）— 已派调查 Worker\n\n## 活跃 Worker\n1. **OpenVLA 修复** (worker_fix_openvla-official-eval): turn 32，正在安装 PyTorch/transformers conda env\n2. **调查 Worker** (刚派): 检查 stale PID、EXIT_CODE=129 实验、GPU 冲突、checkpoint 一致性\n\n## 发现的问题（调查中）\n1. **GPU 冲突风险**: bjb1-32546 cuda:1/cuda:4 上原始 multiscale 实验 (seed43/44) 与 perdof 实验共享 GPU。-r2 版本已在 bjb1-18228 重新部署，原始版本可能已退出但 registry 未更新\n2. **K sweep 无 cron**: bjb1-18228 上 k5/k20 实验运行 ~5.5h 无监控，Worker 将确认 PID 后注册 cron\n3. **3 个 EXIT_CODE=129 实验**: eval-perdof-object-norm02-seed45-r2、eval-obs-only-object-norm005-seed43-r3、eval-obs-only-object-norm01-seed47 — 标记为 killed 但可能已完成，Worker 检查输出文件\n\n## 关键等待项（不变）\n1. K=1 multi-scale 3-seed mean → framing 分叉决策\n2. OpenVLA bug 修复 → Claim 3\n3. Magnitude curve 多 seed 补点 → Figure 2\n\n调查 Worker 完成后将更新 registry 并再次汇报具体数据。",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-17T19:33:05.271935+00:00_

调查 Worker 已派出。现在向 Director 汇报 session 启动状态。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:train-crm-k1-accg-object-seed42"
}
```

</details>

---

## Round 2

38 recorded events

### User

_source line 30 · 2026-05-17T23:38:45.811387+00:00_

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
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-17T23:38:57.501100+00:00_

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
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
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

_source line 32 · 2026-05-17T23:38:57.551774+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-17T23:39:00.746428+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-17T23:39:00.746841+00:00_

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
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-17T23:39:01.649957+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "report.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "file": "report.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-17T23:39:01.855212+00:00_

Error: result (349,661 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-5a3cc89b/a20633b7-9b92-42b8-a2e4-ce0f33f0591a/tool-results/mcp-agent-ml-research-read_registry-1779061141719.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-5a3cc89b/a20633b7-9b92-42b8-a2e4-ce0f33f0591a/tool-results/mcp-agent-ml-research-read_registry-1779061141719.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 1108
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-17T23:39:01.855690+00:00_

called mcp__agent-ml-research__read_roadmap

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_roadmap</summary>

```json
{
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-17T23:39:32.011445+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 14, \"results\": [{\"exp_id\": \"eval-perdof-object-norm02-seed46\", \"success\": true, \"actions\": [\"Job still running (pid=389051)\"]}, {\"exp_id\": \"eval-obs-only-object-default-seed46\", \"success\": true, \"actions\": [\"Job still running (pid=422357)\"]}, {\"exp_id\": \"eval-perdof-object-default-seed46\", \"success\": true, \"actions\": [\"Job still running (pid=423767)\"]}, {\"exp_id\": \"eval-obs-only-object-norm005-seed43-r2\", \"success\": true, \"actions\": [\"Job still running (pid=433500)\"]}, {\"exp_id\": \"eval-perdof-object-norm02-seed47\", \"success\": true, \"actions\": [\"Job still running (pid=404983)\"]}, {\"exp_id\": \"eval-random-selection-object-seed42\", \"success\": true, \"actions\": [\"Job still running (pid=395256)\"]}, {\"exp_id\": \"eval-obs-only-object-norm01-seed46\", \"success\": true, \"actions\": [\"Job still running (pid=449068)\"]}, {\"exp_id\": \"eval-perdof-object-norm02-seed45-r3\", \"success\": true, \"actions\": [\"Job still running (pid=749540)\"]}, {\"exp_id\": \"eval-obs-only-object-norm01-seed48\", \"success\": true, \"actions\": [\"Job still running (pid=774337)\"]}, {\"exp_id\": \"eval-obs-only-object-norm03-seed48\", \"success\": true, \"actions\": [\"Job still running (pid=774538)\"]}, {\"exp_id\": \"eval-perdof-object-norm02-seed48\", \"success\": true, \"actions\": [\"Job still running (pid=488656)\"]}, {\"exp_id\": \"eval-random-selection-object-seed43\", \"success\": true, \"actions\": [\"Job still running (pid=492545)\"]}, {\"exp_id\": \"eval-obs-only-object-norm005-seed44\", \"success\": true, \"actions\": [\"Job still running (pid=549432)\"]}, {\"exp_id\": \"eval-perdof-object-norm005-seed44\", \"success\": true, \"actions\": [\"Job still running (pid=553043)\"]}]}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 31264
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-17T23:39:32.062452+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"# Handover — 2026-05-17\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| eval-perdof-object-norm02-seed45-r3 | perdof CRM (ε=0.2) seed45 on LIBERO-Object. r3 重试。补充 perdof magnitude curve ε=0.2 数据。 | — | — | — |\\n| eval-obs-only-object-norm03-seed48 | obs_only CRM (ε=0.3) seed48 on LIBERO-Object. 补充 magnitude curve high-norm 段 seed48 数据。扩展 error bars。 | — | — | — |\\n| eval-obs-only-object-norm01-seed48 | obs_only CRM (ε=0.1) seed48 on LIBERO-Object. 补充 magnitude curve low-norm 段 seed48 数据。扩展 error bars。 | — | — | — |\\n\\n## 待处理\\n- eval-random-selection-object-seed43: Random selection baseline (K=10 随机选一个 action) seed43 on LIBERO-Object. 多 seed 验证 CRM selection > random。seed42 RUNNING 中。（准备中）\\n- eval-obs-only-object-norm005-seed44: obs_only CRM (ε=0.05) seed44 on LIBERO-Object. 补充 Figure 2 低 norm 段数据。seed42=13%, seed43 running。（准备中）\\n- eval-perdof-object-norm02-seed48: perdof CRM (ε=0.2) seed48 on LIBERO-Object. 补充 magnitude curve ε=0.2 数据，扩展 error bars。（准备中）\\n- eval_obs_only_norm03_seed48（准备中）\\n- eval_obs_only_norm01_seed48（准备中）\\n- train-crm-k1-accg-object-seed42-full（准备中）\\n- plan_701-precompute-k1-spatial（准备中）\\n- plan_701-crm-k1-train: K=1 CRM 训练：使用多阶段 VLA 特征融合 + 组合损失函数（L2 + contrastive + uncertainty-weighted），训练专门用于 K=1 单采样纠正的 CRM 模型。目标是超越 K=1 VLA-only baseline (10.8%)。（准备中）\\n- eval-perdof-object-norm02-seed43: perdof CRM ε=0.2 seed43 on LIBERO-Object. 补充 perdof magnitude curve ε=0.2 数据（seed42=11%, seed43 之前仅 spatial 数据 9%）。与 obs_only ε=0.2 seed43=16% 配对对比。（准备中）\\n- eval-obs-only-object-norm01-seed46: obs_only CRM (ε=0.1) seed=46 on LIBERO Object. Extends magnitude curve low-norm segment to 3+ seeds. If consistent with seed42=19% and seed45 (running), strengthens robustness claim that obs_only maintains 
…[truncated 5787 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 30412
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-17T23:39:32.063300+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-17 22:56 UTC | 更新原因: D054/D055 + Agent系统性崩溃 + 实验锁定证据汇总 + 阻塞项更新\\n\\n## 核心方向\\n**待用户确认 framing（D051 选择已发出 ~12h，等待回复）**：\\n- Option A: K=10 升 primary，K=1 作 ablation（有硬统计证据）\\n- Option B: 纯 analysis paper（竞争力因 D054 OpenVLA diversity insight 提升）\\n详见 paper_framing.md。\\n\\n## 投稿目标\\n**CoRL 2026**（abstract DDL ~May 26, full paper DDL ~Jun 2）。剩余 ~8 天 / ~15 天。\\n\\n## 当前进展（已锁定证据）\\n| Evidence | 结果 | Claim 支撑 |\\n|----------|------|-----------|\\n| K=10 obs_only vs argmin | 17.5% vs 12.3%, Fisher p=0.0074 | Selection 有效 |\\n| K=1 correction (all configs) | ~10% ≈ VLA-only 10.8% | Selection > correction |\\n| Magnitude: obs_only | 稳定 13-17.5% 全 ε | obs_only 鲁棒 |\\n| Magnitude: perdof | 14%→10%→4.7%→0% 随 ε↑ | perdof 崩溃 |\\n| Latency | CRM 0.3ms, overhead 0.34% | 近零开销 |\\n| OpenVLA VLA-only | 69.0% (10 trials, 需 50 trials 确认) | Baseline reference |\\n| OpenVLA diversity (D054) | T=0.5 近确定性, 8/10 identical | **Cross-VLA boundary** |\\n| Random selection (partial) | ~15% (6/40), vs CRM 17.5% | 待完成确认 CRM>random |\\n\\n## 阻塞项\\n1. **⏳ 用户 D051 framing 选择** — Paper Agent 启动的前置条件\\n2. **⚠️ Agent 系统性崩溃** — 平台级问题，Manager 已上报运维。无法部署新实验或 kill 重复进程\\n\\n## 实验状态\\n- **正常推进** (不受 Agent 崩溃影响)：\\n  - bjb1-32546: 5 个 magnitude sweep >80%，2-3h 内陆续完成\\n  - bjb2-40593: random selection ~40%，~15h 完成\\n  - bjb1-18228 GPU0: K=5 orphan ~60%，~10h 完成\\n- **资源浪费** (需 Agent 执行但无法送达)：\\n  - bjb1-18228 GPU1/GPU2: 空闲 8+ 小时\\n  - bjb2-28827: 2-3 个重复实验占 GPU（已请 Manager 协调手动 kill）\\n- **已完成待消费**：3 个 Worker 结果（K=5/K=20 recovery、plan_802 feasibility、K-sweep retry）\\n\\n## 关键决策更新\\n- **D054**: OpenVLA 近确定性 → CRM selection 对 tokenized VLA 不可行\\n- **D055**: plan_802 corrector 降优先级 → diversity analysis 已足够支撑 Claim 3\\n\\n## 近期任务\\n- [ ] ⏳ 用户 D051 framing → Paper Agent 启动\\n- [ ] 
…[truncated 2116 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 30207
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-17T23:39:46.166893+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-5a3cc89b/a20633b7-9b92-42b8-a2e4-ce0f33f0591a/tool-results/mcp-agent-ml-research-read_registry-1779061141719.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']\n# Get RUNNING experiments\nrunning = [e for e in exps if e.get('status') == 'RUNNING']\npreparing = [e for e in exps if e.get('status') == 'PREPARING']\nprint('=== RUNNING ===')\nfor e in running:\n    print(f\\\"  {e['exp_id']} | server={e.get('server','?')} | gpu={e.get('gpu_id','?')} | pid={e.get('pid','?')}\\\")\nprint(f'\\n=== PREPARING ({len(preparing)}) ===')\nfor e in preparing:\n    print(f\\\"  {e['exp_id']}\\\")\nprint(f'\\nTotal exps: {len(exps)}, RUNNING: {len(running)}, PREPARING: {len(preparing)}')\n# Count by status\nfrom collections import Counter\nc = Counter(e.get('status') for e in exps)\nprint(f'Status dist: {dict(c)}')\n\"\n",
  "description": "Extract RUNNING/PREPARING experiments from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-5a3cc89b/a20633b7-9b92-42b8-a2e4-ce0f33f0591a/tool-results/mcp-agent-ml-research-read_registry-1779061141719.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']\n# Get RUNNING experiments\nrunning = [e for e in exps if e.get('status') == 'RUNNING']\npreparing = [e for e in exps if e.get('status') == 'PREPARING']\nprint('=== RUNNING ===')\nfor e in running:\n    print(f\\\"  {e['exp_id']} | server={e.get('server','?')} | gpu={e.get('gpu_id','?')} | pid={e.get('pid','?')}\\\")\nprint(f'\\n=== PREPARING ({len(preparing)}) ===')\nfor e in preparing:\n    print(f\\\"  {e['exp_id']}\\\")\nprint(f'\\nTotal exps: {len(exps)}, RUNNING: {len(running)}, PREPARING: {len(preparing)}')\n# Count by status\nfrom collections import Counter\nc = Counter(e.get('status') for e in exps)\nprint(f'Status dist: {dict(c)}')\n\"\n",
    "description": "Extract RUNNING/PREPARING experiments from registry"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-17T23:39:46.470076+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 7, in &lt;module>
    running = [e for e in exps if e.get('status') == 'RUNNING']
                                  ^^^^^
AttributeError: 'str' object has no attribute 'get'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "Bash",
  "elapsed_ms": 303
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-17T23:40:00.791846+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-5a3cc89b/a20633b7-9b92-42b8-a2e4-ce0f33f0591a/tool-results/mcp-agent-ml-research-read_registry-1779061141719.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult_str = data['result']\nresult = json.loads(result_str)\n# result['data'] might be a list of dicts or something else\nexps = result.get('data', [])\nif isinstance(exps, str):\n    exps = json.loads(exps)\nprint(type(exps))\nif isinstance(exps, list) and len(exps) > 0:\n    print(type(exps[0]))\n    if isinstance(exps[0], str):\n        print(exps[0][:200])\n    else:\n        print(list(exps[0].keys())[:10])\nelif isinstance(exps, dict):\n    print(list(exps.keys())[:10])\n\" 2>&1 | head -20\n",
  "description": "Check registry data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-5a3cc89b/a20633b7-9b92-42b8-a2e4-ce0f33f0591a/tool-results/mcp-agent-ml-research-read_registry-1779061141719.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult_str = data['result']\nresult = json.loads(result_str)\n# result['data'] might be a list of dicts or something else\nexps = result.get('data', [])\nif isinstance(exps, str):\n    exps = json.loads(exps)\nprint(type(exps))\nif isinstance(exps, list) and len(exps) > 0:\n    print(type(exps[0]))\n    if isinstance(exps[0], str):\n        print(exps[0][:200])\n    else:\n        print(list(exps[0].keys())[:10])\nelif isinstance(exps, dict):\n    print(list(exps.keys())[:10])\n\" 2>&1 | head -20\n",
    "description": "Check registry data structure"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-17T23:40:00.943735+00:00_

&lt;class 'dict'>
['experiments', 'count', 'total', 'baseline']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-17T23:40:06.426926+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-5a3cc89b/a20633b7-9b92-42b8-a2e4-ce0f33f0591a/tool-results/mcp-agent-ml-research-read_registry-1779061141719.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nfrom collections import Counter\nc = Counter(e.get('status') for e in exps)\nprint(f'Status dist: {dict(c)}')\nprint(f'Total: {len(exps)}')\nprint()\nrunning = [e for e in exps if e.get('status') == 'RUNNING']\nprint('=== RUNNING ===')\nfor e in running:\n    print(f\\\"  {e['exp_id']} | server={e.get('server','?')} | gpu={e.get('gpu_id','?')} | pid={e.get('pid','?')}\\\")\nprint()\npreparing = [e for e in exps if e.get('status') == 'PREPARING']\nprint(f'=== PREPARING ({len(preparing)}) ===')\nfor e in preparing:\n    print(f\\\"  {e['exp_id']}\\\")\n\"\n",
  "description": "Extract RUNNING/PREPARING experiments from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-5a3cc89b/a20633b7-9b92-42b8-a2e4-ce0f33f0591a/tool-results/mcp-agent-ml-research-read_registry-1779061141719.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nfrom collections import Counter\nc = Counter(e.get('status') for e in exps)\nprint(f'Status dist: {dict(c)}')\nprint(f'Total: {len(exps)}')\nprint()\nrunning = [e for e in exps if e.get('status') == 'RUNNING']\nprint('=== RUNNING ===')\nfor e in running:\n    print(f\\\"  {e['exp_id']} | server={e.get('server','?')} | gpu={e.get('gpu_id','?')} | pid={e.get('pid','?')}\\\")\nprint()\npreparing = [e for e in exps if e.get('status') == 'PREPARING']\nprint(f'=== PREPARING ({len(preparing)}) ===')\nfor e in preparing:\n    print(f\\\"  {e['exp_id']}\\\")\n\"\n",
    "description": "Extract RUNNING/PREPARING experiments from registry"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-17T23:40:06.628027+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 7, in &lt;module>
    c = Counter(e.get('status') for e in exps)
  File "/usr/lib/python3.14/collections/__init__.py", line 614, in __init__
    self.update(iterable, **kwds)
    ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.14/collections/__init__.py", line 709, in update
    _count_elements(self, iterable)
    ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "&lt;string>", line 7, in &lt;genexpr>
    c = Counter(e.get('status') for e in exps)
                ^^^^^
AttributeError: 'str' object has no attribute 'get'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-17T23:40:12.047443+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-5a3cc89b/a20633b7-9b92-42b8-a2e4-ce0f33f0591a/tool-results/mcp-agent-ml-research-read_registry-1779061141719.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps_data = result['data']['experiments']\n# Check what exps_data looks like\nif isinstance(exps_data, list):\n    print(f'list of {type(exps_data[0]).__name__}, len={len(exps_data)}')\n    if isinstance(exps_data[0], str):\n        # parse each\n        first = json.loads(exps_data[0])\n        print(list(first.keys())[:15])\nelif isinstance(exps_data, dict):\n    print(f'dict keys: {list(exps_data.keys())[:10]}')\n\" 2>&1\n",
  "description": "Debug registry data format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-5a3cc89b/a20633b7-9b92-42b8-a2e4-ce0f33f0591a/tool-results/mcp-agent-ml-research-read_registry-1779061141719.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps_data = result['data']['experiments']\n# Check what exps_data looks like\nif isinstance(exps_data, list):\n    print(f'list of {type(exps_data[0]).__name__}, len={len(exps_data)}')\n    if isinstance(exps_data[0], str):\n        # parse each\n        first = json.loads(exps_data[0])\n        print(list(first.keys())[:15])\nelif isinstance(exps_data, dict):\n    print(f'dict keys: {list(exps_data.keys())[:10]}')\n\" 2>&1\n",
    "description": "Debug registry data format"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-17T23:40:12.098095+00:00_

dict keys: ['eval-perdof-object-norm005-seed44', 'eval-obs-only-object-norm03-seed46', 'eval-obs-only-object-norm005-seed43', 'eval-perdof-object-norm02-seed43-r3', 'eval-random-selection-object-seed43', 'eval-obs-only-object-norm02-seed48', 'eval-obs-only-object-norm005-seed44', 'mag_perdof_norm02_seed43_r3', 'eval-perdof-object-norm02-seed45-r3', 'eval-perdof-object-norm02-seed48']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-17T23:40:18.523483+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-5a3cc89b/a20633b7-9b92-42b8-a2e4-ce0f33f0591a/tool-results/mcp-agent-ml-research-read_registry-1779061141719.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps_dict = result['data']['experiments']\nfrom collections import Counter\nc = Counter()\nrunning = []\npreparing = []\nfor eid, edata in exps_dict.items():\n    if isinstance(edata, str):\n        edata = json.loads(edata)\n    st = edata.get('status','?')\n    c[st] += 1\n    if st == 'RUNNING':\n        running.append((eid, edata))\n    elif st == 'PREPARING':\n        preparing.append((eid, edata))\nprint(f'Status dist: {dict(c)}')\nprint(f'Total: {sum(c.values())}')\nprint()\nprint('=== RUNNING ===')\nfor eid, e in running:\n    print(f'  {eid} | server={e.get(\\\"server\\\",\\\"?\\\")} | gpu={e.get(\\\"gpu_id\\\",\\\"?\\\")} | pid={e.get(\\\"pid\\\",\\\"?\\\")}')\nprint()\nprint(f'=== PREPARING ({len(preparing)}) ===')\nfor eid, e in preparing:\n    print(f'  {eid}')\n\"\n",
  "description": "Extract RUNNING/PREPARING experiments from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement--claude-sessions-agent-5a3cc89b/a20633b7-9b92-42b8-a2e4-ce0f33f0591a/tool-results/mcp-agent-ml-research-read_registry-1779061141719.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps_dict = result['data']['experiments']\nfrom collections import Counter\nc = Counter()\nrunning = []\npreparing = []\nfor eid, edata in exps_dict.items():\n    if isinstance(edata, str):\n        edata = json.loads(edata)\n    st = edata.get('status','?')\n    c[st] += 1\n    if st == 'RUNNING':\n        running.append((eid, edata))\n    elif st == 'PREPARING':\n        preparing.append((eid, edata))\nprint(f'Status dist: {dict(c)}')\nprint(f'Total: {sum(c.values())}')\nprint()\nprint('=== RUNNING ===')\nfor eid, e in running:\n    print(f'  {eid} | server={e.get(\\\"server\\\",\\\"?\\\")} | gpu={e.get(\\\"gpu_id\\\",\\\"?\\\")} | pid={e.get(\\\"pid\\\",\\\"?\\\")}')\nprint()\nprint(f'=== PREPARING ({len(preparing)}) ===')\nfor eid, e in preparing:\n    print(f'  {eid}')\n\"\n",
    "description": "Extract RUNNING/PREPARING experiments from registry"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-17T23:40:18.624651+00:00_

Status dist: {'PREPARING': 12, 'DONE': 201, 'RUNNING': 11, 'DEPLOYED': 1}
Total: 225

=== RUNNING ===
  eval-perdof-object-norm02-seed45-r3 | server=? | gpu=? | pid=?
  eval-obs-only-object-norm03-seed48 | server=? | gpu=? | pid=?
  eval-obs-only-object-norm01-seed48 | server=? | gpu=? | pid=?
  mag_obs_only_norm01_seed47 | server=? | gpu=? | pid=?
  mag_obs_only_norm01_seed46 | server=? | gpu=? | pid=?
  eval-random-selection-object-seed42 | server=? | gpu=? | pid=?
  eval-perdof-object-norm02-seed47 | server=? | gpu=? | pid=?
  eval-obs-only-object-norm005-seed43-r2 | server=? | gpu=? | pid=?
  eval-perdof-object-default-seed46 | server=? | gpu=? | pid=?
  eval-obs-only-object-default-seed46 | server=? | gpu=? | pid=?
  eval-perdof-object-norm02-seed46 | server=? | gpu=? | pid=?

=== PREPARING (12) ===
  eval-perdof-object-norm005-seed44
  eval-random-selection-object-seed43
  eval-obs-only-object-norm005-seed44
  eval-perdof-object-norm02-seed48
  eval_obs_only_norm03_seed48
  eval_obs_only_norm01_seed48
  train-crm-k1-accg-object-seed42-full
  plan_701-precompute-k1-spatial
  plan_701-crm-k1-train
  eval-perdof-object-norm02-seed43
  eval-obs-only-object-norm01-seed46
  eval-perdof-object-norm01-seed46

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-17T23:40:21.636334+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "memory.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "file": "memory.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-17T23:40:22.138607+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md\", \"content\": \"# Project Memory\\n\\n## plan_802 可行性分析结论 (2026-05-17)\\n\\nOpenVLA 7B (Llama-2-7b, hidden=4096) 与 SmolVLA CRM (obs_dim=960) 完全不兼容：\\n- Feature dim: 4096 vs 960\\n- Action 机制: deterministic token gen vs K-sample flow matching\\n- CRM 核心依赖的多 sample + CGS 在 OpenVLA 中不存在\\n\\n如果要做 OpenVLA + CRM，必须重新设计（放弃 conformal 保证，变成 obs_only residual correction）。\\n预估 precompute 2-4h/benchmark，训练 <30min，存储 ~200MB 全部 benchmark。\\n\", \"total_chars\": 395, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-17T23:40:22.389825+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "paper_framing.md",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "file": "paper_framing.md",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-17T23:40:22.490812+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md\", \"content\": \"# Paper Framing — acr-vla-conformal-refinement\\n\\n## Target Venue\\n- **Primary: CoRL 2026** (Abstract DDL ~May 26, Full paper DDL ~Jun 2)\\n- Narrative B+ (D049): mechanism insight + K=1 practicality + cross-VLA validation\\n\\n## Core Insight (Narrative B+ — ACTIVE, D049)\\nLightweight observation-conditioned residual correction can improve frozen VLA policies at inference time, even with a single forward pass (K=1). The conditioning-magnitude interaction is the critical, previously unidentified factor: observation features yield robust corrections across all magnitudes, while per-DOF conformal features cause progressive collapse. This insight holds across VLA backbones (SmolVLA + OpenVLA), establishing it as a general principle for safe inference-time VLA correction.\\n\\n## Headline Metrics\\n- **K=1 CRM (SmolVLA)**: TBD (plan_702, target: significant improvement over K=1 VLA-only 10.8%)\\n- **K=10 supplementary**: obs_only ε=0.2 6-seed pooled 17.5% vs argmin 12.3%, Fisher exact p=0.0074\\n- **Cross-VLA**: TBD (plan_802, OpenVLA + K=1 CRM)\\n- **Magnitude robustness**: obs_only stable 15-17.5% across all norms; perdof collapse 10%→0%\\n\\n## Core Claims (Narrative B+ — 4 claims)\\n\\n1. **K=1 observation-conditioned CRM improves frozen VLA at inference time**\\n   - Single forward pass + lightweight CRM (~330K-500K params) = practical deployment\\n   - Multi-stage VLA features as conditioning (not conformal statistics)\\n   - Compare to K=1 VLA-only baseline ONLY (not K=10 results)\\n   - Evidence: Table 1 (K=1 comparison group), Section 3 (method)\\n   - **K=10 as supplementary**: 10x sampling further improves to 17.5% (Fisher p=0.0074) but at 10x compute cost\\n\\n2. **Conditioning-magnitude interaction as a previously unidentified failure mode**\\n   - Same CRM architecture succeeds or
…[truncated 7818 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-17T23:40:27.559132+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__load_project_config,mcp__agent-ml-research__list_workers",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__load_project_config,mcp__agent-ml-research__list_workers",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-17T23:40:27.609758+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-17T23:40:30.893352+00:00_

called mcp__agent-ml-research__load_project_config

<details open><summary>🔧 Tool call — mcp__agent-ml-research__load_project_config</summary>

```json
{
  "project_name": "acr-vla-conformal-refinement",
  "section": "execution"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "mcp__agent-ml-research__load_project_config",
  "tool_args": {
    "project_name": "acr-vla-conformal-refinement",
    "section": "execution"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-17T23:40:30.944028+00:00_

{"result":"{\"success\": true, \"data\": {\"project\": \"acr-vla-conformal-refinement\", \"section\": \"execution\", \"config\": {\"execution\": {\"account\": \"root\", \"gpu_constraint\": [\"autodl-4090:cuda:0\"], \"gpu_ids\": [\"bjb2-40593:cuda:0\", \"bjb1-18228:cuda:0\", \"bjb1-18228:cuda:1\", \"bjb1-18228:cuda:2\", \"bjb1-18228:cuda:3\", \"bjb1-32546:cuda:0\", \"bjb1-32546:cuda:1\", \"bjb1-32546:cuda:2\", \"bjb1-32546:cuda:3\", \"bjb1-32546:cuda:4\", \"bjb1-32546:cuda:5\", \"bjb2-28827:cuda:0\", \"bjb2-28827:cuda:1\", \"bjb2-28827:cuda:2\", \"bjb2-28827:cuda:3\", \"bjb2-28827:cuda:4\", \"bjb2-28827:cuda:5\"], \"project_path\": \"/root/acr-vla-conformal-refinement\", \"servers\": [\"bjb2-40593\", \"bjb1-18228\", {\"account\": \"root\", \"server\": \"bjb1-32546\"}, {\"account\": \"root\", \"server\": \"bjb2-28827\"}]}}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "mcp__agent-ml-research__load_project_config",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-17T23:40:30.944451+00:00_

called mcp__agent-ml-research__list_workers

<details open><summary>🔧 Tool call — mcp__agent-ml-research__list_workers</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "status": "running"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "mcp__agent-ml-research__list_workers",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "status": "running"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-17T23:40:30.994953+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [], \"count\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-17T23:40:36.579263+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "decisions.yaml",
  "max_chars": "6000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "file": "decisions.yaml",
    "max_chars": "6000"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-17T23:40:36.780769+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/decisions.yaml\", \"content\": \"_next_id: 56\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 01:03 UTC\\n  summary: MVP 方案确定：3D Point-Reaching Motivating Experiment 验证 per-DOF conformal 特征的信息优势\\n  rationale: IDEA_BRIEF 已设计了完美的 go/no-go gate：用合成数据的 3D reaching task 对比 per-DOF vs\\n    标量 vs 无不确定性三种 conditioning，直接测试核心假设。成本极低（<0.5 GPU-hours），无需 VLA 基础设施，失败则提前止损。Pass\\n    标准明确：B 在非扰动轴 MSE 比 A 低 >10%。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 01:06 UTC\\n  summary: 采纳 Reviewer 建议完善 MVP：增加 B vs C 对比（>5% MSE）、K=10 estimated uncertainty variant、2:1/1.5:1\\n    各向异性 sweep\\n  rationale: Reviewer 正确指出 (1) 缺少 B vs C 对比会遗漏\\\"观测特征已足够\\\"的可能性，这直接关系核心 claim；(2) oracle\\n    uncertainty 与实际 pipeline 存在 gap，K=10 variant 几乎零成本可验证；(3) 5:1 比率过极端，需测试更温和情况。三项改进均不增加显著成本。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 01:47 UTC\\n  summary: MVP 通过，GO — 进入 research 阶段\\n  rationale: 全部 3 条 pass 标准满足且 margin 很大：per-DOF (B) 在非扰动轴 MSE 比标量 (A) 低 22-38%，比无\\n    uncertainty (C) 低 15-39%。K=10 estimated 和弱各向异性(1.5:1)下均成立。核心假设\\\"per-DOF conformal\\n    特征携带更多可操作信息\\\"得到验证。关注风险：oracle→K=10 衰减 ~15pp，真实 7-DOF 场景待验证。\\n  related_experiments:\\n  - exp_id: mvp-point-reaching\\n    role: MVP gate\\n    result: PASS — all 6 conditions met criteria\\n  depends_on:\\n  - D001\\n  - D002\\n- id: D004\\n  date: 2026-05-13 02:59 UTC\\n  summary: Horizon 策略：截取 chunk 前 H_eff=5 步，action_dim=6。CGS 输出 40D。\\n  rationale: SmolVLA chunk_size=50 远超原假设 H=5。receding-horizon 执行语义下只需关注近期 action 的\\n    uncertainty，远期 step 对当前校正无意义。H_eff=5 保持与 IDEA_BRIEF 设计一致，CGS 40D 可控（per-DOF std\\n    30 + radius 5 + volume 5），p/n=6/10=0.6 优于原假设 0.7。H_eff=10 留作 ablation。action_dim=6\\n    使 Ledoit-Wolf 更稳定。\\n  related_experiments: []\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-13 03:00 UTC\\n  summar
…[truncated 4615 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 201
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-17T23:40:42.752748+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "decisions.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "file": "decisions.yaml",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-17T23:40:42.804961+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/decisions.yaml\", \"content\": \"_next_id: 56\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 01:03 UTC\\n  summary: MVP 方案确定：3D Point-Reaching Motivating Experiment 验证 per-DOF conformal 特征的信息优势\\n  rationale: IDEA_BRIEF 已设计了完美的 go/no-go gate：用合成数据的 3D reaching task 对比 per-DOF vs\\n    标量 vs 无不确定性三种 conditioning，直接测试核心假设。成本极低（<0.5 GPU-hours），无需 VLA 基础设施，失败则提前止损。Pass\\n    标准明确：B 在非扰动轴 MSE 比 A 低 >10%。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 01:06 UTC\\n  summary: 采纳 Reviewer 建议完善 MVP：增加 B vs C 对比（>5% MSE）、K=10 estimated uncertainty variant、2:1/1.5:1\\n    各向异性 sweep\\n  rationale: Reviewer 正确指出 (1) 缺少 B vs C 对比会遗漏\\\"观测特征已足够\\\"的可能性，这直接关系核心 claim；(2) oracle\\n    uncertainty 与实际 pipeline 存在 gap，K=10 variant 几乎零成本可验证；(3) 5:1 比率过极端，需测试更温和情况。三项改进均不增加显著成本。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 01:47 UTC\\n  summary: MVP 通过，GO — 进入 research 阶段\\n  rationale: 全部 3 条 pass 标准满足且 margin 很大：per-DOF (B) 在非扰动轴 MSE 比标量 (A) 低 22-38%，比无\\n    uncertainty (C) 低 15-39%。K=10 estimated 和弱各向异性(1.5:1)下均成立。核心假设\\\"per-DOF conformal\\n    特征携带更多可操作信息\\\"得到验证。关注风险：oracle→K=10 衰减 ~15pp，真实 7-DOF 场景待验证。\\n  related_experiments:\\n  - exp_id: mvp-point-reaching\\n    role: MVP gate\\n    result: PASS — all 6 conditions met criteria\\n  depends_on:\\n  - D001\\n  - D002\\n- id: D004\\n  date: 2026-05-13 02:59 UTC\\n  summary: Horizon 策略：截取 chunk 前 H_eff=5 步，action_dim=6。CGS 输出 40D。\\n  rationale: SmolVLA chunk_size=50 远超原假设 H=5。receding-horizon 执行语义下只需关注近期 action 的\\n    uncertainty，远期 step 对当前校正无意义。H_eff=5 保持与 IDEA_BRIEF 设计一致，CGS 40D 可控（per-DOF std\\n    30 + radius 5 + volume 5），p/n=6/10=0.6 优于原假设 0.7。H_eff=10 留作 ablation。action_dim=6\\n    使 Ledoit-Wolf 更稳定。\\n  related_experiments: []\\n  depends_on:\\n  - D003\\n- id: D005\\n  date: 2026-05-13 03:00 UTC\\n  summar
…[truncated 44539 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 52
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-17T23:40:47.122030+00:00_

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
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
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

_source line 66 · 2026-05-17T23:40:47.172828+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:train-crm-k1-accg-object-seed42",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Assistant

_source line 67 · 2026-05-17T23:42:00.292841+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- GPU 白名单：bjb2-40593:cuda:0, bjb1-18228:cuda:0-3, bjb1-32546:cuda:0-5, bjb2-28827:cuda:0-5（共 17 张 4090）
- **D051 用户 framing 选择未返回**（已等 ~12h）——Paper Agent 启动的硬前置条件，不得擅自开写论文
- K=1 CRM 已死（D050/D051，6 次 negative）——不要再尝试任何 K=1 correction 变体
- plan_802 OpenVLA corrector 已降优先级（D055）——不训练 OpenVLA CRM，diversity analysis 已足够
- bjb2-28827 上可能有重复实验占 GPU（ROADMAP 提到 2-3 个），上轮 Agent 崩溃未能 kill

### 2. 🖥️ 基础设施快照
- **bjb2-40593**: cuda:0, 项目路径 /root/acr-vla-conformal-refinement, random-selection-object-seed42 (pid 395256) 运行中
- **bjb1-18228**: cuda:0-3, 同路径, 多路 magnitude sweep 运行中
- **bjb1-32546**: cuda:0-5, 同路径, magnitude sweep + random-selection-seed43 运行中
- **bjb2-28827**: cuda:0-5, 同路径, magnitude sweep 运行中（可能有重复进程需排查）
- 账号: root（所有服务器）
- Python/conda 环境: 未在 memory.md 记录，需 SSH 确认（上轮 Worker 用 `source /root/miniconda3/bin/activate` 模式）
- 活跃 cron 监控 14 个实验（全部 still running），无 W&B 项目配置（eval 实验不走 W&B）

### 3. 📊 当前状态
**刚完成**: D054/D055 OpenVLA diversity analysis（近确定性，CRM selection 不可行），K=1 multi-scale CRM 全 negative（D051）

**14 个 RUNNING 实验**（均为 LIBERO-Object eval，cron 监控中）:
- Magnitude sweep obs_only: norm01-seed46/48, norm03-seed48, norm005-seed43-r2/seed44, default-seed46
- Magnitude sweep perdof: norm02-seed45-r3/46/47/48, norm005-seed44, default-seed46
- Random selection: seed42 (~40% 进度, ~15h ETA), seed43
- Registry 还有 mag_obs_only_norm01_seed46/47 标记 RUNNING 但未在 cron 中（可能是 orphan）

**12 个 PREPARING**: 包括 random-selection-seed43, perdof-norm02-seed43/48, obs_only-norm005-seed44, train-crm-k1-accg-object-seed42-full, plan_701 系列（K=1 已死，这些应被 cancel）

**等待中**: D051 用户 framing 选择（Option A: K=10 升 primary / Option B: 纯 analysis paper）

### 4. 📋 待办（条件触发式）
- **用户回复 D051 framing 选择 → 更新 paper_framing.md → 启动 Paper Agent 写初稿**
- **magnitude sweep 完成（~2-3h 内陆续）→ 汇总 Figure 2 多 seed 均值±stderr 数据 → 更新 report.md**
- **random-selection-seed42 完成（~15h）→ 确认 CRM 17.5% > random ~15%（差距小，关键数据点）**
- **random-selection-seed43 完成 → pooled random vs CRM Fisher test**
- **Agent 恢复稳定 → kill bjb2-28827 重复进程 → 部署空闲 GPU 上的 PREPARING 实验**
- **所有 magnitude 数据回收 → Figure 脚本改为从 JSON 读取（当前硬编码数据过时）**
- plan_701 系列（K=1 redesign）和 train-crm-k1-accg-object-seed42-full 应 cancel（K=1 已全 negative）

### 5. 🎯 战略上下文
**核心结论链**: per-DOF conformal features 在 real VLA 上无价值（D029 spatial +1pp, D039 object default=0%）→ obs_only CRM 是唯一有效 conditioning → K=10 selection 有效但 K=1 correction 无效（D050/D051）→ OpenVLA 近确定性导致 selection 本身不适用（D054）→ 论文核心是 **mechanism insight**（conditioning-magnitude interaction），不是 SOTA improvement

**已锁定的硬证据**:
- K=10 obs_only vs argmin: 17.5% vs 12.3%, Fisher p=0.0074, Cohen's d=1.21
- Magnitude: obs_only 稳定 13-17.5% 全 ε; perdof 14%→10%→4.7%→0% 崩溃
- K=1 所有变体 ≈ VLA-only 10.8%
- Latency: CRM 0.3ms, overhead 0.34%

**最容易判断错的事**:
1. **不要把 K=10 和 K=1 混比**——论文 primary 是 K=10 selection（D049 用户确认），K=1 作为 negative result / analysis
2. **不要高估 random selection 的威胁**——当前 seed42 partial ~15% vs CRM 17.5%，差距可能不显著，但核心 narrative 是 mechanism insight 不依赖 absolute SR
3. **Spatial benchmark 是 null result**——所有方法 34-36%，CRM 无增益，论文如实报告为 limitation
4. **D011（放弃 CoRL）已被 D021 撤销**——CoRL 2026 仍是目标，abstract DDL ~May 26（~9 天），full paper DDL ~Jun 2（~16 天）
5. **PREPARING 中的 plan_701 系列是 zombie**——K=1 redesign 已被 D050/D051 证伪，不要部署
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:train-crm-k1-accg-object-seed42"
}
```

</details>

---
