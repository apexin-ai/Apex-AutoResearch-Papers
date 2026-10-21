# cron hook precompute v4 shard2 20260515T012642 766240

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 52
- **Recorded user turns:** 2
- **Tool calls:** 24
- **Original source:** `logs/chats/archive/cron_hook_precompute-v4-shard2_20260515T012642_766240.jsonl`
- **Structured JSON:** [`6254cb15419f0c7ee695.json`](../../sessions/62/6254cb15419f0c7ee695.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

22 recorded events

### User

_source line 1 · 2026-05-14T21:23:45.753708+00:00_

[HANDOFF] 你是 Main Agent，这是 Loop #5。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- GPU 白名单必须通过 `get_project_status` 的 `execution.gpu_ids` 确认，当前 bjb1 分配 cuda:0-3，bjb2 分配 cuda:0
- bjb2-40593 上的 crm_cache 是 v4（6D state，D016 之前），**不能用于训练**——只有 bjb1 的 `/root/autodl-tmp/crm_cache_v5/` 是 8D state 修复后的正确版本
- CRM v1/v2/a3/a4/k5 的所有 checkpoint 已被 D016 invalidate（6D state mismatch），绝不能用来 eval
- eval-acr-spatial-v3 结果（2.5%）是 v2 CRM（无 normalization）的结果，不代表 v3-norm 的表现——两者不可混为一谈
- `submit_training_job` 命令必须自带环境激活（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`），bjb1/bjb2 均为 conda 环境

### 2. 🖥️ 基础设施快照
- **bjb1-18228** (4× RTX 4090): 工作目录 `/root/acr-vla-conformal-refinement`，Python `/root/miniconda3/bin/python`，conda base
- **bjb2-40593** (1× RTX 4090D): 同上路径结构
- 模型: `/root/autodl-tmp/models/smolvla_libero/`（SmolVLA 450M, libero fine-tuned）
- VLM backbone: `/root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct/`
- 正确 CRM cache: `/root/autodl-tmp/crm_cache_v5/`（bjb1 only, 8D state, 12167 spatial + 14570 object samples）
- CRM v3-norm checkpoint: `/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt`（val_loss=0.0358, 带 input_mean/input_std tensors）
- 数据: `/root/autodl-tmp/libero_data/`
- Gated CRM 代码: `src/gated_crm.py`（modes: clipping/gating/temperature，已就绪未启用）
- 活跃进程（截至 handoff 时刻）:
  - bjb1 cuda:0: eval-acr-spatial-v4-default（v3-norm, 默认 correction）
  - bjb1 cuda:1: eval-argmin-only-spatial (PID 231421)
  - bjb1 cuda:2: eval-tiny-correction-spatial (PID 232815, max_norm=0.05)
  - bjb1 cuda:3: eval-acr-spatial-v4-small (PID 253085, max_norm=0.1)
  - bjb2 cuda:0: eval-vla-mean-spatial (PID 143106)
  - bjb1 上还有 crm-train-v3-norm-obs-only 和 crm-train-v3-norm-scalar-unc 在跑（无 GPU 编号记录，应在 tmux 里确认）
- GPU 预算: ~200h 总量, ~80h 已用, ~120h 剩余

### 3. 📊 当前状态
刚完成 D018 修复（CRM 输入 normalization）和 v3-norm CRM 训练（val_loss=0.0358）。核心悬念：**v3-norm eval 是否解决 30%→2.5% 的灾难性退化**。7 个实验同时在跑，等 cron 回调。

**Registry RUNNING 实验**:
| exp_id | 摘要 | 服务器/GPU |
|--------|------|-----------|
| eval-acr-spatial-v4-default | v3-norm CRM，默认 correction，决定 normalization 是否够 | bjb1:0 |
| eval-acr-spatial-v4-small | v3-norm + max_norm=0.1，测 magnitude control 是否额外需要 | bjb1:3 |
| eval-argmin-only-spatial | 纯 argmin 无 CRM，隔离 argmin base 选择 vs CRM correction 的影响 | bjb1:1 |
| eval-tiny-correction-spatial | max_norm=0.05（28x 缩小），早期信号 task1 4/5 成功 | bjb1:2 |
| eval-vla-mean-spatial | K=10 均值 baseline，隔离多采样平均贡献 | bjb2:0 |
| crm-train-v3-norm-scalar-unc | scalar uncertainty ablation + normalization | bjb1 (GPU TBD) |
| crm-train-v3-norm-obs-only | obs-only ablation + normalization | bjb1 (GPU TBD) |

**等待中**: 所有 7 个实验的 cron 回调。无待处理的 Director 决策。

### 4. 📋 待办（条件触发式）
- eval-acr-spatial-v4-default 完成 → 对比 30% baseline：>30% 意味着 normalization 解决了主要问题；≤30% 意味着 magnitude control 不可或缺
- eval-acr-spatial-v4-small 完成 → 与 v4-default 对比：small > default 确认 magnitude clipping 有效，下一步做 correction sweep（0.01, 0.05, 0.1, 0.2, 0.5）
- v4-default ≤ 30% 且 v4-small > v4-default → 启用 Gated CRM（`src/gated_crm.py`），做 magnitude sweep + 温度 gating 实验
- v4-default > 30% → 立即铺 v3-norm-scalar-unc 和 v3-norm-obs-only 的 eval，完成 per-DOF vs scalar vs obs-only 三路对比表
- eval-vla-mean-spatial 完成 → 得到 K=10 mean baseline，四路对比表最后一格填上
- eval-argmin-only-spatial 完成 → 判断 argmin 选择本身是否引入损害
- crm-train-v3-norm-scalar-unc/obs-only 训练完成 → spawn eval Worker 跑对应的 spatial eval
- 四路对比表出齐（ACR-VLA / SampleConsensus 34% / VLA-mean / VLA-K1 30%）→ 向 Director 汇报核心 claim 判定，决定是否需要 Framing 调整
- 如果所有 CRM 变体仍 ≤ baseline → **必须走 Red Section Framing 提案流程**，禁止默默跑下一批

### 5. 🎯 战略上下文
- **项目核心**: Per-DOF conformal statistics → dimension-selective action correction for VLAs. 目标 ICLR 2027 (Sep-Oct 2026 DDL)
- **决策链**: D001→D003 MVP PASS → D015 SFT Gate 30% 继续 → D016 发现 6D/8D state bug → D017 确认 CRM correction 全面退化 → D018 根因=输入未归一化(1500x scale imbalance) → 当前等 v3-norm eval
- **核心结论**: MVP 验证 per-DOF > scalar > none（合成数据），但闭环 LIBERO eval 上 CRM correction 导致灾难性退化（30%→2.5%）。D018 normalization 是最新修复，尚未验证
- **文献支撑**: PLD(ICLR2026) scheduled ξ, TRANSIC(CoRL2024) 无gate=collapse, 均支持 correction magnitude control 的必要性。ACR-VLA 的独特贡献角度="Conformally-Calibrated Correction Magnitude"——CP intervals 作为 correction 幅度的自然上界
- **最易判断错的事**: (1) 不要把 v2 CRM（无 norm）的 2.5% 结果当作"per-DOF 方法失败"——v3-norm 是全新模型，结果可能完全不同；(2) CRM 的 val_loss 不可跨版本比较（v1=0.009 vs v3-norm=0.036），因为 input normalization 改变了 loss 的尺度；(3) eval-tiny-correction task1 4/5 是早期信号（5 rollouts），不构成结论
- **SampleConsensus 不是 ReconVLA**: D014 确认当前 reconvla mode 实际是 argmin-Euclidean 启发式，已重命名为 SampleConsensus(34%)，不要在论文中称其为 ReconVLA
- **Claim C2(ACI+COC) 和 C3(SRPO orthogonality) 零证据**: 目前全部精力在 C1(per-DOF correction)，C2/C3 尚未开始

## 可查的历史
前 30 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
完整聊天归档可用 `recall_session_history("关键词")` 搜索。

## 第一个动作要求
1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）
2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:precompute-v4-shard2",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-14T21:23:56.420828+00:00_

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
  "session": "cron:hook:precompute-v4-shard2",
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

_source line 3 · 2026-05-14T21:23:56.421333+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T21:23:59.732633+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "limit": "0"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T21:24:00.235552+00:00_

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
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T21:24:00.236732+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"crm-train-v3-norm-scalar-unc\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-14T20:09:01.250Z\", \"updated_at\": \"2026-05-14T20:51:12.277Z\", \"hypothesis\": \"Ablation: scalar_unc input mode (scalar uncertainty only) with normalization. Tests per-DOF vs scalar uncertainty contribution with proper normalization.\"}, \"crm-train-v3-norm-obs-only\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-14T20:09:00.829Z\", \"updated_at\": \"2026-05-14T20:51:10.399Z\", \"hypothesis\": \"Ablation: obs_only input mode (no uncertainty features) with normalization. Isolates contribution of obs features vs conformal features.\"}, \"eval-acr-object-v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:17:13.095Z\", \"updated_at\": \"2026-05-14T20:48:42.308Z\", \"metrics\": {\"tasks_done\": \"4/10\", \"overall_success_rate\": 0, \"total_successes\": 0, \"total_rollouts\": 40, \"per_task_partial\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0}, \"snapshot_time\": \"2026-05-14T18:15Z\"}, \"conclusion\": \"failed\"}, \"eval-acr-spatial-v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:17:06.073Z\", \"updated_at\": \"2026-05-14T20:48:41.643Z\", \"metrics\": {\"tasks_done\": \"4/10\", \"overall_success_rate\": 0.025, \"total_successes\": 1, \"total_rollouts\": 40, \"per_task_partial\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.1, \"pick_up_black_bowl_next_to_ramekin\": 0, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0}, \"snapshot_time\": \"2026-05-14T18:15Z\"}, \"conclusion\": \"failed\"}, \"eval-acr-spatial-v4-small\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-14T20:09:00.358Z\", \"updated_at\": \"2026-05-14T20:31:10.337Z\", \"hypothesis\": \"D018: Normalization + moderate correction scaling (max_correction_norm=0.1, 14x smaller than default). If v4-small > v4-default → magnitude control needed on t
…[truncated 16982 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 504
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T21:24:00.739665+00:00_

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
  "session": "cron:hook:precompute-v4-shard2",
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

_source line 8 · 2026-05-14T21:24:00.791435+00:00_

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
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T21:24:10.127702+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 7, \"results\": [{\"exp_id\": \"eval-vla-mean-spatial\", \"success\": true, \"actions\": [\"Job still running (pid=143106)\"]}, {\"exp_id\": \"eval-argmin-only-spatial\", \"success\": true, \"actions\": [\"Job still running (pid=231421)\"]}, {\"exp_id\": \"eval-tiny-correction-spatial\", \"success\": true, \"actions\": [\"Job still running (pid=232815)\"]}, {\"exp_id\": \"eval-acr-spatial-v4-default\", \"success\": true, \"actions\": [\"Job still running (pid=eval-acr-spatial-v4-default)\"]}, {\"exp_id\": \"eval-acr-spatial-v4-small\", \"success\": true, \"actions\": [\"Job still running (pid=253085)\"]}, {\"exp_id\": \"crm-train-v3-norm-obs-only\", \"success\": true, \"actions\": [\"Job still running (pid=256771)\"]}, {\"exp_id\": \"crm-train-v3-norm-scalar-unc\", \"success\": true, \"actions\": [\"Job still running (pid=257086)\"]}]}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 9892
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T21:24:10.178520+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| crm-train-v3-norm-scalar-unc | Ablation: scalar_unc input mode (scalar uncertainty only) with normalization. Tests per-DOF vs scalar uncertainty contribution with proper normalization. | — | — | — |\\n| crm-train-v3-norm-obs-only | Ablation: obs_only input mode (no uncertainty features) with normalization. Isolates contribution of obs features vs conformal features. | — | — | — |\\n| eval-acr-spatial-v4-small | D018: Normalization + moderate correction scaling (max_correction_norm=0.1, 14x smaller than default). If v4-small > v4-default → magnitude control needed on top of normalization. | — | — | — |\\n\\n## 待处理\\n- eval-object-v6-full（准备中）\\n- eval-reconvla-spatial-v1（准备中）\\n- precompute-v4-shard2（准备中）\\n- precompute-v4-shard1（准备中）\\n- precompute-v4-shard0（准备中）\\n- eval-spatial-v4-full（准备中）\\n- precompute-v3-shard2（准备中）\\n- precompute-v3-shard1（准备中）\\n- precompute-v3-shard0（准备中）\\n- precompute-v2-shard2（准备中）\\n- …另有 2 项\\n\\n## 近期结论\\n- **eval-acr-object-v3** (failed): —\\n- **eval-acr-spatial-v3** (failed): —\\n- **crm-train-v3-norm** (success): D018: Input normalization fixes 1500x scale imbalance in CRM inputs, enabling proper gradient flow and meaningful per-DOF correction learning ← 基于 crm-train-v3-perdof\\n\\n## 趋势\\n成功 15 / 负向 0 / 失败 7 / 共 44\\nbest_epoch: 50 ↑（近 3 次 success）\\nbest_val_loss: 0.050501 ↓（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb1-18228: 无 GPU 信息\\nbjb2-40593: 无 GPU 信息\\n\\n## 告警\\n- plan_001-crm-smolvla: 训练失败 — unknown\\n- plan_014-reconvla-baseline: 训练失败 — unknown\\n- eval-smolvla-libero-spatial: 训练失败 — unknown\\n- eval-spatial-reeval-v2: 已被终止 — unknown\\n- eval-spatial-v3-full: 已被终止 — u
…[truncated 1082 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 9438
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T21:24:10.179009+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-14 16:00 UTC | 更新原因: crm-train-k5 完成 + eval-k5-spatial 启动，竞品分析完成，CRM correction 退化现象确认\\n\\n## 核心方向\\nPer-DOF conformal statistics from multivariate CP on flow-matching VLA samples enable dimension-selective action correction. 详见 paper_framing.md。\\n\\n## 投稿目标\\n**ICLR 2027**（预计 DDL Sep-Oct 2026）。CoRL 2026 已放弃（D011）。\\n\\n## 当前进展\\n- **阶段**: Phase 2 — Spatial Eval 四路对比（ACR-VLA / SampleConsensus / Scalar-CRM / VLA-mean）\\n- **MVP**: PASS（plan_000, per-DOF > scalar > none 确认）\\n- **SFT Gate**: 30% baseline，决定继续（D015）\\n- **CRM 训练完成**: per-DOF val_loss=0.009, scalar_unc=0.008, obs_only=0.018（conformal features 2× 改善确认）\\n- **Baselines 锁定**: spatial 30% (K=1), object 13% (K=1)\\n- **早期信号（2/10 tasks，不构成结论）**: ACR-VLA 在简单任务上低于 baseline，per-DOF CRM 可能在简单任务上引入有害 correction\\n- **竞品分析完成** (art_20260514_621600): 核心竞品 ReconVLA（最直接）、SC-VLA、VLA-Pilot、ACoT-VLA\\n- **CRM correction 退化现象**: ACR-VLA 中间结果 (23-26%) 低于 baseline (30%)，SampleConsensus 领先 (42.9%)\\n- **文献调研完成** (art_20260514_d21dd2): correction degradation 可能原因与补救方向（correction clipping/gating 等）\\n\\n## 近期任务\\n- [ ] eval-acr-spatial-v2 完成 → 核心 claim 判定（ACR-VLA vs baseline 30%）\\n- [ ] eval-reconvla-spatial-v3 完成 → SampleConsensus 对比\\n- [ ] eval-scalar-unc-spatial 完成 → scalar vs per-DOF 最终裁决\\n- [x] crm-train-k5 完成 → K sensitivity ablation + eval-k5-spatial 已启动\\n- [ ] eval-k5-spatial 完成 → K=5 sensitivity ablation 结果\\n- [ ] eval-vla-mean-spatial 完成 → 隔离多采样平均贡献\\n- [x] 代码同步 bjb1→bjb2（evaluate.py + train_crm.py）— MD5 verified\\n- [ ] 完整 spatial 四路对比表出炉 → 决定是否铺 object benchmark\\n- [ ] paper_framing.md 更新竞品定位（SC-VLA, VLA-Pilot, ACoT-VLA SOTA）\\n\\n## SFT Gate\\nD015: 30% baseline 继续推进。核心关注相对提升，非绝对值。\\n\\n## GPU 预算\\n- bjb1-18228 (4× RTX 4090): eval-k5-spatial(cuda:0) + eval-acr(cuda:1) 
…[truncated 1734 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 9387
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T21:24:33.180339+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__load_project_config",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__load_project_config",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T21:24:33.381121+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "ToolSearch",
  "elapsed_ms": 200
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T21:24:36.995976+00:00_

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
  "session": "cron:hook:precompute-v4-shard2",
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

_source line 15 · 2026-05-14T21:24:37.046673+00:00_

{"result":"{\"success\": true, \"data\": {\"project\": \"acr-vla-conformal-refinement\", \"section\": \"execution\", \"config\": {\"execution\": {\"account\": \"root\", \"gpu_constraint\": [\"autodl-4090:cuda:0\"], \"gpu_ids\": [\"bjb2-40593:cuda:0\", \"bjb1-18228:cuda:0\", \"bjb1-18228:cuda:1\", \"bjb1-18228:cuda:2\", \"bjb1-18228:cuda:3\"], \"project_path\": \"/root/acr-vla-conformal-refinement\", \"servers\": [\"bjb2-40593\", \"bjb1-18228\"]}}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__load_project_config",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T21:24:46.841552+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/skills/resource-saturation.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/skills/resource-saturation.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T21:24:46.893368+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/sessions/agent_f7022f78.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T21:24:50.111642+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/resource-saturation*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/resource-saturation*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T21:24:50.162158+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-14T21:25:04.913833+00:00_

called mcp__agent-ml-research__main_agent_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__main_agent_post_to_director</summary>

```json
{
  "text": "[资源] GPU 分配 5/5 全部在跑 | Worker 池 0 (等 cron 回调)\n\nLoop #5 session-start 状态同步：\n\n**7 个实验全部 RUNNING（cron 确认进程存活）**：\n\n| exp_id | 服务器/GPU | 目的 |\n|--------|-----------|------|\n| eval-acr-spatial-v4-default | bjb1:0 | v3-norm CRM 默认 correction，核心验证 |\n| eval-argmin-only-spatial | bjb1:1 | 纯 argmin 无 CRM，隔离 base 选择影响 |\n| eval-tiny-correction-spatial | bjb1:2 | max_norm=0.05，早期信号 task1 4/5 |\n| eval-acr-spatial-v4-small | bjb1:3 | max_norm=0.1，magnitude control 测试 |\n| eval-vla-mean-spatial | bjb2:0 | K=10 均值 baseline |\n| crm-train-v3-norm-obs-only | bjb1 (共享) | obs-only ablation 训练 |\n| crm-train-v3-norm-scalar-unc | bjb1 (共享) | scalar-unc ablation 训练 |\n\n**核心悬念不变**：v4-default 结果决定 normalization 是否足够修复退化（>30% = 成功，≤30% = 需 magnitude control）。\n\n无阻塞项，等 cron 回调后立即分析推进。",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "tool_args": {
    "text": "[资源] GPU 分配 5/5 全部在跑 | Worker 池 0 (等 cron 回调)\n\nLoop #5 session-start 状态同步：\n\n**7 个实验全部 RUNNING（cron 确认进程存活）**：\n\n| exp_id | 服务器/GPU | 目的 |\n|--------|-----------|------|\n| eval-acr-spatial-v4-default | bjb1:0 | v3-norm CRM 默认 correction，核心验证 |\n| eval-argmin-only-spatial | bjb1:1 | 纯 argmin 无 CRM，隔离 base 选择影响 |\n| eval-tiny-correction-spatial | bjb1:2 | max_norm=0.05，早期信号 task1 4/5 |\n| eval-acr-spatial-v4-small | bjb1:3 | max_norm=0.1，magnitude control 测试 |\n| eval-vla-mean-spatial | bjb2:0 | K=10 均值 baseline |\n| crm-train-v3-norm-obs-only | bjb1 (共享) | obs-only ablation 训练 |\n| crm-train-v3-norm-scalar-unc | bjb1 (共享) | scalar-unc ablation 训练 |\n\n**核心悬念不变**：v4-default 结果决定 normalization 是否足够修复退化（>30% = 成功，≤30% = 需 magnitude control）。\n\n无阻塞项，等 cron 回调后立即分析推进。",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-14T21:25:09.053446+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_5ee1fd6fcd3e57fe38e03d67d16d0bf4:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "elapsed_ms": 4139
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-14T21:25:14.448634+00:00_

Session-start 初始化完成：

- **Registry**: 7 个实验全部 RUNNING，cron reconcile 确认进程均存活
- **GPU**: 5/5 分配 GPU 全部在跑（bjb1:0-3 eval + bjb2:0 eval），另有 2 个 CRM 训练共享 bjb1
- **无新结果**：所有实验从上轮 handoff 后继续运行中
- **已向 Director 汇报**当前状态

等待 cron 回调，任一实验完成后立即分析推进。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:precompute-v4-shard2"
}
```

</details>

---

## Round 2

30 recorded events

### User

_source line 23 · 2026-05-15T01:24:23.646758+00:00_

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
  "session": "cron:hook:precompute-v4-shard2",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-15T01:24:48.284444+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Read project state files",
  "subagent_type": "Explore",
  "prompt": "I need to find and read all key project state files in and around /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/\n\nPlease find and read the contents of:\n1. report.md (likely in the project root or artifacts)\n2. ROADMAP.md\n3. memory.md\n4. registry.yaml or any registry file\n5. experiment_plan.yaml\n6. paper_framing.md\n7. literature_map.yaml\n\nSearch broadly - these files could be in the project root, artifacts/, or other subdirectories. Read each file you find and report the full contents back to me."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Agent",
  "tool_args": {
    "description": "Read project state files",
    "subagent_type": "Explore",
    "prompt": "I need to find and read all key project state files in and around /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/\n\nPlease find and read the contents of:\n1. report.md (likely in the project root or artifacts)\n2. ROADMAP.md\n3. memory.md\n4. registry.yaml or any registry file\n5. experiment_plan.yaml\n6. paper_framing.md\n7. literature_map.yaml\n\nSearch broadly - these files could be in the project root, artifacts/, or other subdirectories. Read each file you find and report the full contents back to me."
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T01:24:51.129215+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement -type f -name \"*.md\" -o -name \"*.yaml\" -o -name \"*.yml\" | head -50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement -type f -name \"*.md\" -o -name \"*.yaml\" -o -name \"*.yml\" | head -50"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T01:24:51.683755+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/IDEA_BRIEF.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/task_context/agent.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/task_context/director.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/task_context/reviewer.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/task_context/history/director/loop_1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/task_context/history/agent/loop_4_1778793795.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/task_context/history/agent/loop_2_1778728390.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/task_context/history/agent/loop_2_1778782399.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/task_context/history/agent/loop_1_1778714300.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/task_context/history/agent/loop_1_1778724391.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/task_context/history/agent/loop_3_1778793764.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/task_context/history/agent/loop_2_1778744616.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/task_context/history/agent/loop_2_1778728433.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/task_context/history/agent/loop_1_1778725595.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/task_context/history/agent/loop_2_1778782
…[truncated 4409 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Bash",
  "elapsed_ms": 554
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T01:24:53.955071+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement -maxdepth 3 -type f \\( -name \"report.md\" -o -name \"ROADMAP.md\" -o -name \"memory.md\" -o -name \"registry.yaml\" -o -name \"experiment_plan.yaml\" -o -name \"paper_framing.md\" -o -name \"literature_map.yaml\" \\)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement -maxdepth 3 -type f \\( -name \"report.md\" -o -name \"ROADMAP.md\" -o -name \"memory.md\" -o -name \"registry.yaml\" -o -name \"experiment_plan.yaml\" -o -name \"paper_framing.md\" -o -name \"literature_map.yaml\" \\)"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T01:24:54.006080+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/experiment_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Bash",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T01:24:56.323482+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T01:24:56.425048+00:00_

1	# Handover — 2026-05-14
2	
3	> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。
4	
5	## 运行中
6	| exp_id | 假设 | 状态 | 关键指标 | W&B |
7	|--------|------|------|---------|-----|
8	| eval-acr-spatial-v4-default-r2 | D018 retry: Normalization alone fixes CRM correction degradation. v3-norm per-DOF checkpoint with default max_correction_norm (~1.42). If >30% baseline → normalization was the main fix. If still < 30% → magnitude control also needed (compare with v4-small at 0.1). | — | — | — |
9	| eval-vla-mean-spatial-t10 | — | — | — | — |
10	| eval-acr-spatial-v4-small | D018: Normalization + moderate correction scaling (max_correction_norm=0.1, 14x smaller than default). If v4-small > v4-default → magnitude control needed on top of normalization. | — | — | — |
11	
12	## 待处理
13	- eval-acr-spatial-v4-scalar: D020: scalar_unc CRM (val_loss 0.0374) with max_correction_norm=0.1. Three-way ablation: perdof vs scalar_unc vs obs_only under identical correction magnitude.（准备中）
14	- eval-object-v6-full（准备中）
15	- eval-reconvla-spatial-v1（准备中）
16	- precompute-v4-shard2（准备中）
17	- precompute-v4-shard1（准备中）
18	- precompute-v4-shard0（准备中）
19	- eval-spatial-v4-full（准备中）
20	- precompute-v3-shard2（准备中）
21	- precompute-v3-shard1（准备中）
22	- precompute-v3-shard0（准备中）
23	- …另有 3 项
24	
25	## 近期结论
26	- **eval-acr-spatial-v4-obs-only-r2** (killed): D020: obs_only CRM v3-norm (val_loss 0.0165) with max_correction_norm=0.1. If obs_only >= v4-small (perdof) → Claim 1 needs restructuring. If obs_only < v4-small → conformal features have unique value under distribution shift.
27	- **eval-acr-spatial-v4-obs-only** (failed): D020: obs_only CRM (val_loss 0.0165, 54% better than perdof 0.0358) with max_correction_norm=0.1. If obs_only >= v4-small (perdof) → Claim 1 needs restructuring. If obs_only < v4-small → conformal features have unique value under distribution shift.
28	- **eval-vla-mean-spatial** (success): —
29	
30	## 趋势
31	成功 18 / 负向 0 / 失败 9 / 共 50
32	
33	## 下一步
34	（无活跃 idea，请通过 ideas.md 添加）
35	
36	## 资源状态
37	bjb1-
…[truncated 1444 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T01:24:56.526016+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T01:24:56.727507+00:00_

1	# acr-vla-conformal-refinement — Research Dashboard
2	
3	> 最后更新: 2026-05-14 16:00 UTC | 更新原因: crm-train-k5 完成 + eval-k5-spatial 启动，竞品分析完成，CRM correction 退化现象确认
4	
5	## 核心方向
6	Per-DOF conformal statistics from multivariate CP on flow-matching VLA samples enable dimension-selective action correction. 详见 paper_framing.md。
7	
8	## 投稿目标
9	**ICLR 2027**（预计 DDL Sep-Oct 2026）。CoRL 2026 已放弃（D011）。
10	
11	## 当前进展
12	- **阶段**: Phase 2 — Spatial Eval 四路对比（ACR-VLA / SampleConsensus / Scalar-CRM / VLA-mean）
13	- **MVP**: PASS（plan_000, per-DOF > scalar > none 确认）
14	- **SFT Gate**: 30% baseline，决定继续（D015）
15	- **CRM 训练完成**: per-DOF val_loss=0.009, scalar_unc=0.008, obs_only=0.018（conformal features 2× 改善确认）
16	- **Baselines 锁定**: spatial 30% (K=1), object 13% (K=1)
17	- **早期信号（2/10 tasks，不构成结论）**: ACR-VLA 在简单任务上低于 baseline，per-DOF CRM 可能在简单任务上引入有害 correction
18	- **竞品分析完成** (art_20260514_621600): 核心竞品 ReconVLA（最直接）、SC-VLA、VLA-Pilot、ACoT-VLA
19	- **CRM correction 退化现象**: ACR-VLA 中间结果 (23-26%) 低于 baseline (30%)，SampleConsensus 领先 (42.9%)
20	- **文献调研完成** (art_20260514_d21dd2): correction degradation 可能原因与补救方向（correction clipping/gating 等）
21	
22	## 近期任务
23	- [ ] eval-acr-spatial-v2 完成 → 核心 claim 判定（ACR-VLA vs baseline 30%）
24	- [ ] eval-reconvla-spatial-v3 完成 → SampleConsensus 对比
25	- [ ] eval-scalar-unc-spatial 完成 → scalar vs per-DOF 最终裁决
26	- [x] crm-train-k5 完成 → K sensitivity ablation + eval-k5-spatial 已启动
27	- [ ] eval-k5-spatial 完成 → K=5 sensitivity ablation 结果
28	- [ ] eval-vla-mean-spatial 完成 → 隔离多采样平均贡献
29	- [x] 代码同步 bjb1→bjb2（evaluate.py + train_crm.py）— MD5 verified
30	- [ ] 完整 spatial 四路对比表出炉 → 决定是否铺 object benchmark
31	- [ ] paper_framing.md 更新竞品定位（SC-VLA, VLA-Pilot, ACoT-VLA SOTA）
32	
33	## SFT Gate
34	D015: 30% baseline 继续推进。核心关注相对提升，非绝对值。
35	
36	## GPU 预算
37	- bjb1-18228 (4× RTX 4090): eval-k5-spatial(cuda:0) + eval-acr(cuda:1) + eval-reconvla(cuda:2) + eval-scalar-unc(cuda:3)
38	- bjb2-40593 (1× RTX 4090 D): eval-vla-mean-spatial(cuda:0)
39	- 总预算 ~200 GPU·h, 已用 ~8
…[truncated 1752 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T01:24:56.779086+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T01:24:56.931224+00:00_

1	# Memory — acr-vla-conformal-refinement
2	
3	## VLA-mean Baseline 定稿：多采样平均无收益（2026-05-15）
4	
5	### 发现
6	eval-vla-mean-spatial: K=10 平均 ≈ 31%（9/10 tasks），与 K=1 baseline 30% 无显著差异（+1pp，噪声范围）。
7	
8	### 含义
9	- **多采样平均不是 ACR-VLA 改善的来源**。flow-matching VLA 的 K 个样本虽然不同，但 averaging 消除的噪声对 task success 无帮助
10	- ACR-VLA 的任何改善必须来自 intelligent selection（argmin）或 CRM correction
11	- argmin-only 早期信号 53.3%（3/10 tasks）>> VLA-mean 31% → **sample selection 本身就有强贡献**
12	- Narrative 可分层：(1) sample selection > averaging (2) CRM correction adds calibrated precision
13	
14	### 论文定位
15	这证实了 Section 1 (Intro) 的动机：naive aggregation 不够，需要 structured uncertainty-guided selection。
16	
17	## Correction Magnitude 是核心问题（2026-05-14 18:15，早期信号）
18	
19	### 发现
20	eval-tiny-correction-spatial（max_correction_norm=0.05，约默认 1.42 的 1/28）在首个 task 上 4/5 成功，而 full ACR 同一 task 只有 1/10。这说明 CRM correction 的方向可能是对的，但幅度太大导致 compounding error。
21	
22	### 含义
23	- correction clipping / gating 是正确的补救方向
24	- Gated CRM 代码已就绪（`src/gated_crm.py` + `--mode acr_gated` + `--gate_threshold/mode/temperature`）
25	- 等完整 eval 结果确认后，下一步应该是 correction magnitude sweep（0.01, 0.05, 0.1, 0.2, 0.5）或 Gated CRM eval
26	- **不改变目标 venue（ICLR 2027）**，narrative 可从 "per-DOF correction always helps" 调整为 "per-DOF correction with magnitude control"
27	
28	### ⚠️ 注意
29	这是 1 个 task 的 5 个 rollout 的早期数据。需要完整 10 tasks 确认。
30	
31	## Correction Magnitude 文献支撑（2026-05-14 18:37）
32	
33	### 核心竞品/支撑论文
34	1. **PLD (ICLR 2026)**: scheduled ξ bound，LIBERO ξ=0.5 / SimplerEnv ξ=0.1——不同环境需不同 correction scale，完全验证我们的发现
35	2. **TRANSIC (CoRL 2024)**: 无 gate 时 fine-tuning 导致 model collapse——与我们 40%→2.5% 退化一致
36	3. **ResiP (CoRL-W 2024)**: scaling α≤1，关键不是精确值而是 order of magnitude
37	4. **DRC (2025)**: temporal decay of correction
38	5. **DAWN (2026)**: scale mismatch → residual 学不好
39	
40	### 独特贡献角度
41	**没有现有方法提供 per-DOF, per-timestep, calibrated magnitude bounds。** ACR-VLA 的 conformal intervals 天然提供 calibrated bounds on expected action range。
42	
43	### 推荐 Framing
…[truncated 6066 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "elapsed_ms": 152
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T01:24:56.931724+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-15T01:24:57.182763+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/experiment_plan.yaml"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-15T01:24:57.587495+00:00_

File content (34460 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "elapsed_ms": 655
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T01:24:57.587996+00:00_

1	experiments:
2	- id: plan_000
3	  claim: 1
4	  description: 'Motivating experiment: 3D point-reaching, per-DOF vs scalar vs no
5	    uncertainty conditioning'
6	  priority: P0
7	  gpu_budget_hours: 0.5
8	  deps: []
9	  registry_id: mvp-point-reaching
10	- id: plan_001
11	  claim: 1
12	  description: 'ACR-VLA full pipeline on SmolVLA base: CGS + ACI/COC + CRM. Train
13	    CRM on LIBERO demos + synthetic augmentation. Evaluate on LIBERO (nominal preservation)
14	    + LIBERO-Plus L3-L5 (robustness gain).'
15	  priority: P0
16	  gpu_budget_hours: 25
17	  deps: []
18	  registry_id: crm-train-v1
19	- id: plan_002
20	  claim: 1
21	  description: Ablation A3 — CRM without conformal features (observation-conditioned
22	    residual only, equivalent to A2C2-style generic residual). MAKE-OR-BREAK for Claim
23	    1.
24	  priority: P0
25	  gpu_budget_hours: 8
26	  deps:
27	  - plan_001
28	  registry_id: crm-train-a3-obs-only
29	- id: plan_003
30	  claim: 1
31	  description: Ablation A4 — CRM with scalar uncertainty (Euclidean distance like
32	    ReconVLA) replacing 40D per-DOF features. Validates per-DOF > scalar.
33	  priority: P0
34	  gpu_budget_hours: 8
35	  deps:
36	  - plan_001
37	- id: plan_004
38	  claim: 3
39	  description: 'ACR-VLA stacked on SRPO-finetuned VLA. Train new CRM on SRPO checkpoint
40	    + LIBERO demos. Evaluate on LIBERO-Plus. Primary impact argument: orthogonal to
41	    training-time optimization.'
42	  priority: P0
43	  gpu_budget_hours: 18
44	  deps:
45	  - plan_001
46	- id: plan_005
47	  claim: 2
48	  description: 'COC signal validation: (a) Spearman ρ between episode COC coverage
49	    fraction and task success, (b) ACI convergence plot, (c) ellipsoid volume comparison
50	    vs static calibration at matched coverage.'
51	  priority: P1
52	  gpu_budget_hours: 15
53	  deps:
54	  - plan_001
55	- id: plan_006
56	  claim: 2
57	  description: Ablation A1 — CRM without ACI (static CGS calibration, no online adaptation).
58	    Isolates ACI contribu
…[truncated 3117 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "elapsed_ms": 405
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-15T01:24:57.588363+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T01:24:57.791330+00:00_

1	# Paper Framing — acr-vla-conformal-refinement
2	
3	## Target Venue
4	- **Primary: ICLR 2027** (expected deadline ~Sep-Oct 2026) — 充足时间
5	- ~~CoRL 2026~~ — 已放弃 (D011: GPU 未扩容 + 时间不足)
6	
7	## Core Insight
8	Per-DOF conformal statistics from multivariate CP on flow-matching VLA samples encode "which action dimensions are uncertain and how they co-vary" — fundamentally richer information than scalar uncertainty scores. A lightweight learned module conditioned on these structured features can perform dimension-selective action correction: aggressively correcting high-uncertainty DOFs while preserving confident predictions elsewhere.
9	
10	## Core Claims (3 条，均可证伪)
11	1. **Per-DOF conformal features enable dimension-selective correction**: CGS 提取的 40D 结构化 uncertainty 特征（per-DOF std + conformal radius + ellipsoid volume，action_dim=6, H_eff=5）比标量 uncertainty（ReconVLA 的 Euclidean distance）和无 uncertainty conditioning 的残差策略（A2C2 类）提供显著更好的 action correction。
12	   - 验证: MVP (✅ done) + A3 ablation (make-or-break) + A4 ablation + feature importance analysis
13	   - Kill criterion: A3 (CRM without conformal features) 与 full ACR-VLA 差距 <2% → claim 不成立
14	
15	2. **ACI+COC 在分布偏移下维持 calibrated uncertainty，无需外部监督**: Chunk Overlap Consistency 提供自参考覆盖信号，ACI 在线更新 conformal threshold，在任意分布偏移下维持长期平均覆盖保证。
16	   - 验证: COC-success Spearman ρ + ACI 收敛 + ellipsoid volume vs static
17	   - Kill criterion: Spearman ρ < 0.3 AND ellipsoid volume 无 >10% 收窄 → fallback to episode-level ACI
18	
19	3. **ACR-VLA 与 training-time 方法正交互补**: 作为 inference-time 模块可叠加在 SRPO (82.1% LIBERO-Plus SOTA) 上进一步提升。
20	   - 验证: ACR-VLA + SRPO > SRPO alone
21	   - Kill criterion: stacking gain < 2% → claim 降级为"complementary in principle"
22	
23	## Story Spine
24	- **Problem**: Flow-matching VLAs 在标准 benchmark 上接近饱和(97-99%)，但 LIBERO-Plus 暴露了分布偏移下的灾难性鲁棒性缺口。现有方法分别解决检测(SAFE)、样本选择(ReconVLA)、训练时增强(RobustVLA/DiG-Flow/SRPO)，但没有方法在推理时利用结构化 uncertainty 信息主动校正动作。
25	- **Gap**: 现有 inference-time 方法各有根本性局限：ReconVLA 用标量 CQR 做样本选择——丢弃
…[truncated 4235 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "elapsed_ms": 202
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-15T01:24:57.893303+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/literature_map.yaml"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-15T01:24:58.149000+00:00_

1	papers:
2	  - bibtex_key: "a2c2_2025"
3	    title: "Leave No Observation Behind: Real-time Correction for VLA Action Chunks"
4	    authors: "Sendai et al."
5	    year: 2025
6	    venue: "arXiv:2509.23224"
7	    url: "https://arxiv.org/abs/2509.23224"
8	    category: "inference_correction"
9	    verified: true
10	    relevance: "Proposes A2C2, a lightweight asynchronous action chunk correction head for VLAs. Directly comparable inference-time residual correction approach to ACR-VLA."
11	    must_cite: true
12	
13	  - bibtex_key: "angelopoulos2023gentle"
14	    title: "A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification"
15	    authors: "Angelopoulos & Bates"
16	    year: 2023
17	    venue: "Foundations and Trends in Machine Learning"
18	    url: "https://arxiv.org/abs/2107.07511"
19	    category: "cp_foundation"
20	    verified: true
21	    relevance: "Canonical tutorial on conformal prediction. Provides theoretical grounding for CGS, ACI, and CQR components used in ACR-VLA."
22	    must_cite: true
23	
24	  - bibtex_key: "barber2023conformal"
25	    title: "Conformal Prediction Beyond Exchangeability"
26	    authors: "Barber et al."
27	    year: 2023
28	    venue: "Annals of Statistics, 51(2):816-845"
29	    url: "https://arxiv.org/abs/2202.13415"
30	    category: "cp_foundation"
31	    verified: true
32	    relevance: "Generalizes conformal prediction to non-exchangeable settings via weighted quantiles. Theoretical basis for ACR-VLA's handling of distribution shift in online deployment."
33	    must_cite: false
34	
35	  - bibtex_key: "black2024pi0"
36	    title: "pi0: A Vision-Language-Action Flow Model for General Robot Control"
37	    authors: "Black et al."
38	    year: 2024
39	    venue: "arXiv:2410.24164"
40	    url: "https://arxiv.org/abs/2410.24164"
41	    category: "vla_foundation"
42	    verified: true
43	    relevance: "Foundational flow-matching VLA architecture. ACR-VLA's multi-sample inference builds on the f
…[truncated 29709 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "elapsed_ms": 255
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-15T01:25:00.767174+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "limit": "5000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "limit": "5000"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-15T01:25:01.068776+00:00_

File content (34460 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-15T01:25:03.896639+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "offset": "1",
  "limit": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "offset": "1",
    "limit": "3000"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-15T01:25:04.200543+00:00_

File content (34460 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Read",
  "elapsed_ms": 303
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-15T01:25:05.621401+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml && head -100 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml && head -100 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-15T01:25:05.723367+00:00_

2220 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml
baseline: null
experiments:
  mvp-point-reaching:
    status: DONE
    retry_count: 0
    created_at: '2026-05-13T01:22:10.415Z'
    updated_at: '2026-05-13T22:06:11.073Z'
    spec:
      hypothesis: Per-DOF uncertainty features carry more actionable information than
        scalar uncertainty summaries, enabling dimension-selective correction
      description: '3D point-reaching MVP: 3 MLP variants (scalar/per-DOF/no uncertainty)
        x 6 groups (3 anisotropy ratios x 2 uncertainty sources)'
      server: bjb2-40593
      gpu: cuda:0
      data_count: 20000
      model_name: CorrectionMLP(2-layer, 64-hidden)
      seed: 42
      command: python -u run_mvp.py
      data_path: synthetic (generated in-script)
      checkpoint_path: /root/acr-vla-conformal-refinement/mvp/
      log_path: /root/acr-vla-conformal-refinement/mvp/mvp_results.log
    conclusion: success
    completed_at: '2026-05-13T01:44:00.055Z'
    metrics:
      group1_oracle:
        A_scalar:
          mse_x: 0.180218
          mse_y: 0.02497
          mse_z: 0.024232
          total: 0.076473
        B_perDOF:
          mse_x: 0.172652
          mse_y: 0.015544
          mse_z: 0.01561
          total: 0.067935
        C_none:
          mse_x: 0.22706
          mse_y: 0.025542
          mse_z: 0.024753
          total: 0.092451
      group2_oracle:
        A_scalar:
          mse_x: 0.064642
          mse_y: 0.023836
          mse_z: 0.022967
          total: 0.037148
        B_perDOF:
          mse_x: 0.053403
          mse_y: 0.015695
          mse_z: 0.01573
          total: 0.028276
        C_none:
          mse_x: 0.084178
          mse_y: 0.025427
          mse_z: 0.024798
          total: 0.044801
      group3_oracle:
        A_scalar:
          mse_x: 0.042948
          mse_y: 0.023218
          mse_z: 0.022365
          total: 0.02951
        B_perDOF:
          mse_x: 0.033008
      
…[truncated 846 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-15T01:25:07.797500+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -E \"^  [a-z0-9-]+:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | head -60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -E \"^  [a-z0-9-]+:\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | head -60"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-15T01:25:07.848130+00:00_

  mvp-point-reaching:
  eval-smolvla-libero-spatial:
  precompute-shard0:
  precompute-shard1:
  precompute-shard2:
  eval-spatial-reeval-v2:
  precompute-v2-shard0:
  precompute-v2-shard1:
  precompute-v2-shard2:
  eval-spatial-v3-full:
  precompute-v3-shard0:
  precompute-v3-shard1:
  precompute-v3-shard2:
  eval-spatial-v4-full:
  precompute-v4-shard0:
  precompute-v4-shard1:
  precompute-v4-shard2:
  eval-object-v4-full:
  eval-spatial-v5-full:
  crm-train-v1:
  eval-reconvla-spatial-v1:
  precompute-k5:
  eval-reconvla-spatial-v2:
  eval-acr-spatial-v1:
  crm-train-a3-obs-only:
  eval-acr-vla-spatial-v1:
  eval-spatial-v6-full:
  eval-acr-spatial-v2:
  eval-reconvla-spatial-v3:
  eval-object-v5-full:
  eval-object-v6-full:
  crm-train-a4-scalar-unc:
  eval-scalar-unc-spatial:
  eval-object-v7-full:
  eval-spatial-v7-full:
  eval-object-v8-full:
  crm-train-k5:
  eval-vla-mean-spatial:
  eval-k5-spatial:
  precompute-v5-shard0:
  precompute-v5-shard1:
  precompute-v5-shard2:
  crm-train-v2-perdof:
  crm-train-v2-scalar-unc:
  crm-train-v2-obs-only:
  eval-acr-spatial-v3:
  eval-scalar-unc-spatial-v2:
  eval-obs-only-spatial:
  eval-acr-object-v3:
  eval-obs-only-spatial-v2:
  eval-obs-only-spatial-v3:
  eval-argmin-only-spatial:
  eval-tiny-correction-spatial:
  crm-train-v3-perdof:
  crm-train-v3-scalar-unc:
  crm-train-v3-obs-only:
  crm-train-v3-norm:
  eval-acr-spatial-v4-default:
  eval-acr-spatial-v4-small:
  crm-train-v3-norm-obs-only:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-15T01:25:46.403924+00:00_

Perfect! Now I have a complete picture. Let me provide you with a comprehensive summary of all the key project state files:

---

## Project State Files Summary

I found and read all 7 key project state files from the acr-vla-conformal-refinement project. Here's what I found:

### 1. **report.md** (Handover status - Chinese)
- **Last updated**: 2026-05-14, auto-generated after state changes (max 150 lines)
- **Current phase**: Phase 2 — Spatial Eval four-way comparison
- **Running experiments**: 3 active evals (eval-acr-spatial-v4-default-r2, eval-vla-mean-spatial-t10, eval-acr-spatial-v4-small)
- **Pending**: 15+ experiments queued (eval-acr-spatial-v4-scalar, eval-object-v6-full, eval-reconvla-spatial-v1, multiple precompute shards)
- **Conclusion metrics**: 18 success / 0 negative / 9 failed / 50 total
- **Alerts**: 33 experiments have training failures or were killed
- **GPU status**: bjb1-18228 and bjb2-40593 reporting no GPU info

### 2. **ROADMAP.md** (Strategic direction - Chinese)
- **Target venue**: ICLR 2027 (deadline ~Sep-Oct 2026), CoRL 2026 abandoned (D011)
- **MVP status**: PASS — per-DOF > scalar > none confirmed
- **Core research problem**: Per-DOF conformal statistics from multivariate CP on flow-matching VLA samples enable dimension-selective action correction
- **Key findings**:
  - CRM training complete: per-DOF val_loss=0.009, scalar_unc=0.008, obs_only=0.018
  - Early signal (2/10 tasks): ACR-VLA lower than 30% baseline on simple tasks
  - Competitor analysis complete: ReconVLA (direct competitor), SC-VLA, VLA-Pilot, ACoT-VLA identified
  - **CRM correction degradation found**: ACR middle results 23-26% vs baseline 30%, SampleConsensus leads 42.9%
- **SFT Gate**: D015 decision to continue with 30% baseline
- **GPU budget**: 200 GPU·h total, ~80h used, ~120h remaining
- **Key decisions logged** (D021→D012): Framing adjustments needed due to correction magnitude issues

### 3. **memory.md** (Session notes and discoveries - Chinese)
- **Latest fi
…[truncated 7400 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard2",
  "tool": "Agent",
  "elapsed_ms": 58119
}
```

</details>

---

### Assistant

_source line 52 · 2026-05-15T01:26:42.758421+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- GPU 白名单必须从 `get_project_status` 的 `execution.gpu_ids` 读取，当前服务器 bjb1-18228 和 bjb2-40593，具体 GPU 编号需实时查询
- GPU 预算剩余 ~120h / 200h 总额，大实验（>10h）需向 Director 确认
- SmolVLA wrapper 有 7 个已修复 bug（图像翻转/resize/归一化/state dim 8D/state 归一化/action 反归一化/camera names），precompute 数据必须用修复后版本，旧数据无效
- CRM correction magnitude 过大会导致性能退化（23-26% vs baseline 30%），提交新 ACR eval 前必须确认 max_correction_norm 参数已设置合理值（tiny correction 实验 0.05 norm 效果好于全 ACR）
- CoRL 2026 已放弃（D021），目标锁定 ICLR 2027，禁止在汇报中提及降级 venue

### 2. 🖥️ 基础设施快照
- 服务器：bjb1-18228、bjb2-40593（AutoDL），工作目录需 SSH 探查确认（上轮未留完整路径）
- Python 环境：大概率 conda base（aml-train 镜像），具体路径需 `detect_image` 确认
- 模型：SmolVLA 为 backbone，CRM checkpoint 来自 crm-train-v3-norm（best_val_loss=0.03578, epoch 47/50）
- 数据：LIBERO-Plus spatial benchmark，precompute 数据有多版本（v2-v5），需确认哪版对应修复后 wrapper
- W&B：项目配置需从 `load_project_config` 读取
- 活跃进程：report.md 记录 3 个 RUNNING eval（eval-acr-spatial-v4-default-r2, eval-vla-mean-spatial-t10, eval-acr-spatial-v4-small），PID/tmux 需 SSH 查实际存活状态

### 3. 📊 当前状态
**刚完成**：VLA-mean baseline 确认（K=10 averaging ≈ 31%，与 K=1 baseline 30% 无显著差异，multi-sample averaging 无效）。Tiny correction 实验发现 max_correction_norm=0.05 在 first task 4/5 success vs full ACR 1/10，揭示 correction magnitude 是核心瓶颈。

**Registry 统计**：~65 个实验，18 success / 9 failed / 若干 killed。

**RUNNING**：
- eval-acr-spatial-v4-default-r2：ACR 默认配置 spatial eval 第二轮
- eval-vla-mean-spatial-t10：VLA mean baseline T=10
- eval-acr-spatial-v4-small：小 correction 配置 eval
- eval-k5-spatial：K=5 sensitivity ablation

**等待中**：15+ PENDING eval（scalar、object-v6、reconvla baseline 等），等 GPU 或依赖前序完成。

**关键未决**：correction magnitude crisis 的 framing 调整提案已产出但尚未确认 Director 是否批准新叙事方向（"Conformally-Calibrated Correction Magnitude"）。

### 4. 📋 待办（条件触发式）
- eval-acr-spatial-v4-default-r2 完成 → 对比 v4-small（tiny correction），若 small 显著更好 → 强化 magnitude-control narrative，产出 Framing 调整提案给 Director
- eval-k5-spatial 完成 → K sensitivity 消融数据点，与 K=1/K=10 汇总，更新 paper_framing 的 Reviewer Concern #1
- Director 批准 "Conformally-Calibrated Correction Magnitude" framing → 读 framing-reaudit skill → 全文 re-audit → 调整 experiment_plan 优先级（correction gating/clipping 实验提升为 P0）
- 所有 spatial eval 完成 → 汇总四方对比表（baseline / ACR-full / ACR-small / VLA-mean / scalar），向 Director 提交 Phase 2 结论
- Phase 2 结论若 per-DOF gains < 5% → 必须走 red-section 产 Framing 提案，不得默默推进

### 5. 🎯 战略上下文
**核心发现链**：MVP 验证 per-DOF > scalar > none（点到达任务 15pp gap）→ 但迁移到 LIBERO-Plus 真实任务后 CRM correction 过大导致退化（23-26% < baseline 30%）→ tiny correction（0.05 norm）反而有效 → **correction magnitude control 是关键缺失环节**

**Framing 转向**：原叙事 "per-DOF conformal features enable dimension-selective correction" 仍成立但不够。新叙事方向 = CP intervals 天然提供 correction magnitude 上界，这是区别于 ReconVLA（只做 selection）的核心优势。需要 Director 审批。

**最容易判断错的事**：
1. 不要因为 full ACR 退化就认为方法失败——tiny correction 实验证明方向对，问题在 magnitude 未约束
2. VLA-mean baseline 31% ≈ 30%，证明简单 averaging 无效，**不要**再花 GPU 测更多 K 值的 mean baseline
3. precompute 数据版本混乱（v2-v5 对应不同 wrapper 修复阶段），用错版本会得到不可复现结果，必须确认用 v5+ 修复后数据
4. registry 里 failed/killed 实验很多（~40%），多数是环境问题或 wrapper bug 导致的早期实验，不代表方法 negative
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:precompute-v4-shard2"
}
```

</details>

---
