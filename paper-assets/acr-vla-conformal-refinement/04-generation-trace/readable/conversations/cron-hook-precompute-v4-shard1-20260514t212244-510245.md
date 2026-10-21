# cron hook precompute v4 shard1 20260514T212244 510245

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 70
- **Recorded user turns:** 2
- **Tool calls:** 33
- **Original source:** `logs/chats/archive/cron_hook_precompute-v4-shard1_20260514T212244_510245.jsonl`
- **Structured JSON:** [`3f5fb95502c35aa4f7d9.json`](../../sessions/3f/3f5fb95502c35aa4f7d9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

26 recorded events

### User

_source line 1 · 2026-05-14T18:14:55.511945+00:00_

[HANDOFF] 你是 Main Agent，这是 Loop #4。

## 上一轮交接 (task_context)

### 1. 🔴 硬约束 / 红线
- GPU 白名单：`bjb1-18228:cuda:{0,1,2,3}` + `bjb2-40593:cuda:0`，共 5 张。**禁止使用任何白名单外 GPU**
- bjb1 有 4× RTX 4090，bjb2 有 1× RTX 4090 D
- AutoDL 实例 SSH 端口可能变化，连接失败不要重试，提示用户查控制台
- CRM 训练 ablation 系列**必须用 bs=32/lr=1e-3 baseline 超参**，否则 confound ablation 比较
- evaluate.py 中 `env.reset()` 必须在 `set_init_state()` **之前**调用（两轮 bug 历史，见 memory.md）
- SmolVLA 预处理 7 个坑全踩过（翻转/尺寸/值域/state 8D/归一化/反归一化/双摄像头），修改 wrapper 前**必须**对照 memory.md 中的正确预处理表
- `EXIT_CODE=129` 或 `EXIT_CODE=1` 不一定是训练失败——前者是 tmux SIGHUP，后者是 Python 3.12 SWIG cleanup warning。看 log 末尾判断

### 2. 🖥️ 基础设施快照
- **bjb1-18228** (4× RTX 4090)
  - 工作目录: `/root/acr-vla-conformal-refinement`
  - Python: aml-train 镜像，conda base (`/root/miniconda3/bin/python`)
  - 模型: `/root/autodl-tmp/models/smolvla_libero` + `/root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct`
  - HF cache: `/root/autodl-tmp/.hf_cache`
  - 活跃进程:
    - eval-acr-spatial-v3: PID 197057, cuda:0
    - eval-argmin-only-spatial: PID 231421, cuda:1
    - eval-tiny-correction-spatial: PID 232815, cuda:2
    - eval-acr-object-v3: PID 197803, cuda:3
- **bjb2-40593** (1× RTX 4090 D)
  - 工作目录: `/root/acr-vla-conformal-refinement`
  - Python: 同 aml-train 镜像 conda base
  - 活跃进程:
    - eval-vla-mean-spatial: PID 143106, cuda:0（cron 监控中，reconcile 确认 still running）
- **W&B**: 未配置（指标从 log 文件提取）
- **precompute 数据**: 需用修复后 wrapper 重做（旧 3-shard 数据基于 buggy wrapper）

### 3. 📊 当前状态
**刚完成**: D018 决策——CRM 失败根因确认为输入未归一化（feature scale 差 1500x），批准 CRM v3 normalization 修复。kill 了无诊断价值的 eval-obs-only-spatial-v3 和 eval-scalar-unc-spatial-v2。

**5 路 eval 全部 RUNNING**（全部 5 张 GPU 在跑）:
| exp_id | GPU | 内容 |
|--------|-----|------|
| eval-acr-spatial-v3 | bjb1:0 | **核心 claim**: ACR-VLA per-DOF CRM v2 vs baseline 30% on spatial |
| eval-argmin-only-spatial | bjb1:1 | **诊断**: 隔离 argmin 选择 vs CRM correction 的贡献 |
| eval-tiny-correction-spatial | bjb1:2 | **诊断**: 极小 correction clipping (0.05) 测试 over-correction 假说 |
| eval-acr-object-v3 | bjb1:3 | **跨 benchmark**: ACR-VLA on object |
| eval-vla-mean-spatial | bjb2:0 | **baseline**: K=10 mean action，隔离多采样平均贡献 |

**2 个 Worker 在跑**:
- `worker_verify_bjb2-cache-and-training`: 验证 bjb2 缓存和训练就绪状态
- `worker_monitor_bjb1-eval-progress`: 监控 bjb1 四路 eval 进展

**15 个 PREPARING 实验**（含 CRM v3 三路重训练 + precompute v2/v3/v4 shards），等当前 eval 完成释放 GPU 后推进。

**已锁定 baselines**: spatial 30% (K=1), object 13% (K=1), SampleConsensus 34% (spatial)

### 4. 📋 待办（条件触发式）
- eval-acr-spatial-v3 完成 → **关键裁决点**: 如果 ACR-VLA > 30% baseline → core claim 成立，铺 object + ablation；如果 ≤ 30% → **确认 CRM correction 退化**，需 framing 调整提案（red-section），等 Director 决策
- eval-argmin-only-spatial 完成 → 对比 VLA-mean baseline：argmin-only ≈ VLA-mean (40%) 说明 CRM delta 是 sole culprit；argmin-only << VLA-mean 说明 argmin 选择本身有问题
- eval-tiny-correction-spatial 完成 → tiny-correction >> full-correction 确认 over-correction 是主因 → correction clipping/gating 实验优先级提升
- eval-vla-mean-spatial 完成 → VLA K=10 mean baseline 锁定，完善四路对比表
- eval-acr-object-v3 完成 → 跨 benchmark 验证
- **5 路 eval 全部完成 → 完整四路对比表出炉 → 决定是否铺 object benchmark / 是否需要 CRM v3 normalization 修复**
- CRM v3 重训练启动条件：GPU 释放 + 用修复后 wrapper 重新 precompute（当前 precompute 数据基于 buggy wrapper，但 CRM v2 实际可能用的也是 buggy 数据，需确认一致性）
- Worker 回调到达 → 按 on-worker-done skill 处理

### 5. 🎯 战略上下文
- **投稿目标**: ICLR 2027 (DDL Sep-Oct 2026)，时间充裕
- **核心 claim**: Per-DOF conformal correction > scalar selection > no correction。当前处于**关键验证期**——5 路 eval 的结果决定 claim 是否成立
- **最大风险**: CRM correction 退化现象——早期信号 ACR-VLA 23-26% < baseline 30%。D016 确认了 state 维度不匹配 bug，D018 确认了 feature scale 未归一化。当前 eval-acr-spatial-v3 用的是 D016 修复后但**未做 normalization** 的 CRM v2。如果 v2 仍然退化，CRM v3 (normalization) 是下一个救命稻草
- **决策链**: D009→D010→D011(放弃CoRL)→D012→D013→D014(ReconVLA→SampleConsensus)→D015(SFT Gate 30% 继续)→D016(4-bug fix)→D017(kill 无效 ablation)→D018(normalization 修复批准)
- **竞品定位**: ReconVLA 是最直接竞品（scalar CP + argmin selection），当前 SampleConsensus baseline (34%) 低估了 ReconVLA（它用 CQR 分位数回归）。后续可能需要 CQR baseline
- **易错点**:
  - 不要把 CRM v2（无 normalization）和 CRM v3（有 normalization）的结果混在一起比较
  - precompute 数据有 buggy/fixed 两个版本，确认 CRM 训练用的是哪个版本
  - eval 结果中 2/10 tasks 的早期信号不能作为结论，必须等 10/10 完整结果
  - SampleConsensus 34% 是 raw argmin，不等于 ReconVLA 的 CQR argmin

## 可查的历史
前 24 轮 handoff 在 `task_context/history/agent/loop_*.md`，如有疑问可 Read 回查。
完整聊天归档可用 `recall_session_history("关键词")` 搜索。

## 第一个动作要求
1. 用 `read_registry` 确认当前 RUNNING/PREPARING 实验状态（防止幻觉记忆过时状态）
2. 回复一句话确认你看到了上面的硬约束 + 当前活跃实验，再开始任何工具调用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "cron:hook:precompute-v4-shard1",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-14T18:15:12.868752+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__list_workers",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__reconcile_crons,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_roadmap,mcp__agent-ml-research__main_agent_post_to_director,mcp__agent-ml-research__list_workers",
    "max_results": "6"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-14T18:15:12.969581+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T18:15:18.476895+00:00_

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
  "session": "cron:hook:precompute-v4-shard1",
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

_source line 5 · 2026-05-14T18:15:18.477335+00:00_

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
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "mcp__agent-ml-research__reconcile_crons"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T18:15:18.986363+00:00_

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
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "acr-vla-conformal-refinement",
    "file": "report.md"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-14T18:15:19.439746+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"crm-train-v3-obs-only\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T18:05:02.939Z\", \"updated_at\": \"2026-05-14T18:05:02.939Z\"}, \"crm-train-v3-scalar-unc\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T18:05:00.968Z\", \"updated_at\": \"2026-05-14T18:05:00.968Z\"}, \"crm-train-v3-perdof\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-14T18:04:54.552Z\", \"updated_at\": \"2026-05-14T18:04:54.552Z\"}, \"eval-tiny-correction-spatial\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-14T17:48:35.421Z\", \"updated_at\": \"2026-05-14T17:49:00.253Z\"}, \"eval-argmin-only-spatial\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-14T17:47:58.683Z\", \"updated_at\": \"2026-05-14T17:48:54.942Z\"}, \"eval-obs-only-spatial-v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:49:43.787Z\", \"updated_at\": \"2026-05-14T17:47:54.523Z\", \"conclusion\": \"killed\"}, \"eval-scalar-unc-spatial-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:17:08.413Z\", \"updated_at\": \"2026-05-14T17:47:53.188Z\", \"conclusion\": \"killed\"}, \"eval-obs-only-spatial-v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:43:42.283Z\", \"updated_at\": \"2026-05-14T12:46:47.663Z\", \"conclusion\": \"failed\"}, \"eval-obs-only-spatial\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:17:10.843Z\", \"updated_at\": \"2026-05-14T12:40:23.205Z\", \"conclusion\": \"failed\", \"metrics\": {\"error\": \"size mismatch: obs_only CRM net.0.weight [256,990] vs acr_vla expects [256,1030] — no crm_obs_only mode in evaluate.py\"}}, \"eval-acr-object-v3\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-14T12:17:13.095Z\", \"updated_at\": \"2026-05-14T12:22:43.768Z\"}, \"eval-acr-spatial-v3\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-14T12:17:06.073Z\", \"updated_at\": \"2026-05-14T12:22:36.712Z\"}, \"crm-train-v2-obs-only\": {\"status\": \"DONE\", \"created_at
…[truncated 13755 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 962
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T18:15:19.440252+00:00_

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
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "tool_args": {
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T18:15:19.792419+00:00_

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
  "session": "cron:hook:precompute-v4-shard1",
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

_source line 10 · 2026-05-14T18:15:31.025885+00:00_

{"result":"{\"success\": true, \"data\": {\"reconciled\": 5, \"results\": [{\"exp_id\": \"eval-vla-mean-spatial\", \"success\": true, \"actions\": [\"Job still running (pid=143106)\"]}, {\"exp_id\": \"eval-acr-spatial-v3\", \"success\": true, \"actions\": [\"Job still running (pid=197057)\"]}, {\"exp_id\": \"eval-argmin-only-spatial\", \"success\": true, \"actions\": [\"Job still running (pid=231421)\"]}, {\"exp_id\": \"eval-tiny-correction-spatial\", \"success\": true, \"actions\": [\"Job still running (pid=232815)\"]}, {\"exp_id\": \"eval-acr-object-v3\", \"success\": true, \"actions\": [\"Job still running (pid=197803)\"]}]}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "mcp__agent-ml-research__reconcile_crons",
  "elapsed_ms": 12548
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T18:15:31.026398+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md\", \"content\": \"# Handover — 2026-05-14\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| eval-tiny-correction-spatial | — | — | — | — |\\n| eval-argmin-only-spatial | — | — | — | — |\\n| eval-acr-object-v3 | — | — | — | — |\\n\\n## 待处理\\n- eval-object-v6-full（准备中）\\n- eval-reconvla-spatial-v1（准备中）\\n- precompute-v4-shard2（准备中）\\n- precompute-v4-shard1（准备中）\\n- precompute-v4-shard0（准备中）\\n- eval-spatial-v4-full（准备中）\\n- precompute-v3-shard2（准备中）\\n- precompute-v3-shard1（准备中）\\n- precompute-v3-shard0（准备中）\\n- precompute-v2-shard2（准备中）\\n- …另有 2 项\\n\\n## 近期结论\\n- **eval-obs-only-spatial-v3** (killed): —\\n- **eval-scalar-unc-spatial-v2** (killed): —\\n- **eval-obs-only-spatial-v2** (failed): —\\n\\n## 趋势\\n成功 14 / 负向 0 / 失败 5 / 共 38\\nbest_epoch: 50 ↑（近 3 次 success）\\nbest_val_loss: 0.050501 ↓（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb1-18228: 无 GPU 信息\\nbjb2-40593: 无 GPU 信息\\n\\n## 告警\\n- plan_001-crm-smolvla: 训练失败 — unknown\\n- plan_014-reconvla-baseline: 训练失败 — unknown\\n- eval-smolvla-libero-spatial: 训练失败 — unknown\\n- eval-spatial-reeval-v2: 已被终止 — unknown\\n- eval-spatial-v3-full: 已被终止 — unknown\\n- eval-object-v4-full: 已被终止 — unknown\\n- eval-spatial-v5-full: 已被终止 — unknown\\n- crm-train-v1: 已被终止 — unknown\\n- eval-reconvla-spatial-v2: 已被终止 — unknown\\n- eval-acr-spatial-v1: 已被终止 — unknown\\n- crm-train-a3-obs-only: 已被终止 — unknown\\n- eval-acr-vla-spatial-v1: 已被终止 — unknown\\n- eval-spatial-v6-full: 已被终止 — unknown\\n- eval-acr-spatial-v2: 已被终止 — unknown\\n- eval-object-v5-full: 已被终止 — unknown\\n- crm-train-a4-scalar-unc: 已被终止 — unknown\\n- eval-scalar-unc-spatial: 已被终止 — unknown\\n- eval-object-v7-full: 已被终止 — unknown\\n- crm-train-k5: 已被终止 — unknown\\n- eval-k5-spatial: 已被终止 — unknown\\n- eval-s
…[truncated 257 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 12040
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T18:15:31.077876+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md\", \"content\": \"# acr-vla-conformal-refinement — Research Dashboard\\n\\n> 最后更新: 2026-05-14 16:00 UTC | 更新原因: crm-train-k5 完成 + eval-k5-spatial 启动，竞品分析完成，CRM correction 退化现象确认\\n\\n## 核心方向\\nPer-DOF conformal statistics from multivariate CP on flow-matching VLA samples enable dimension-selective action correction. 详见 paper_framing.md。\\n\\n## 投稿目标\\n**ICLR 2027**（预计 DDL Sep-Oct 2026）。CoRL 2026 已放弃（D011）。\\n\\n## 当前进展\\n- **阶段**: Phase 2 — Spatial Eval 四路对比（ACR-VLA / SampleConsensus / Scalar-CRM / VLA-mean）\\n- **MVP**: PASS（plan_000, per-DOF > scalar > none 确认）\\n- **SFT Gate**: 30% baseline，决定继续（D015）\\n- **CRM 训练完成**: per-DOF val_loss=0.009, scalar_unc=0.008, obs_only=0.018（conformal features 2× 改善确认）\\n- **Baselines 锁定**: spatial 30% (K=1), object 13% (K=1)\\n- **早期信号（2/10 tasks，不构成结论）**: ACR-VLA 在简单任务上低于 baseline，per-DOF CRM 可能在简单任务上引入有害 correction\\n- **竞品分析完成** (art_20260514_621600): 核心竞品 ReconVLA（最直接）、SC-VLA、VLA-Pilot、ACoT-VLA\\n- **CRM correction 退化现象**: ACR-VLA 中间结果 (23-26%) 低于 baseline (30%)，SampleConsensus 领先 (42.9%)\\n- **文献调研完成** (art_20260514_d21dd2): correction degradation 可能原因与补救方向（correction clipping/gating 等）\\n\\n## 近期任务\\n- [ ] eval-acr-spatial-v2 完成 → 核心 claim 判定（ACR-VLA vs baseline 30%）\\n- [ ] eval-reconvla-spatial-v3 完成 → SampleConsensus 对比\\n- [ ] eval-scalar-unc-spatial 完成 → scalar vs per-DOF 最终裁决\\n- [x] crm-train-k5 完成 → K sensitivity ablation + eval-k5-spatial 已启动\\n- [ ] eval-k5-spatial 完成 → K=5 sensitivity ablation 结果\\n- [ ] eval-vla-mean-spatial 完成 → 隔离多采样平均贡献\\n- [x] 代码同步 bjb1→bjb2（evaluate.py + train_crm.py）— MD5 verified\\n- [ ] 完整 spatial 四路对比表出炉 → 决定是否铺 object benchmark\\n- [ ] paper_framing.md 更新竞品定位（SC-VLA, VLA-Pilot, ACoT-VLA SOTA）\\n\\n## SFT Gate\\nD015: 30% baseline 继续推进。核心关注相对提升，非绝对值。\\n\\n## GPU 预算\\n- bjb1-18228 (4× RTX 4090): eval-k5-spatial(cuda:0) + eval-acr(cuda:1) 
…[truncated 1734 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "mcp__agent-ml-research__read_roadmap",
  "elapsed_ms": 11637
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T18:15:31.129438+00:00_

{"result":"{\"success\": true, \"data\": {\"workers\": [{\"worker_id\": \"worker_verify_bjb2-cache-and-training-status_20260514T181357\", \"task_type\": \"verify:bjb2-cache-and-training-status\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"running\", \"started_at\": \"2026-05-14T18:13:57.186785+00:00\", \"ended_at\": null}, {\"worker_id\": \"worker_check_eval-progress-all_20260514T181427\", \"task_type\": \"check:eval-progress-all\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"running\", \"started_at\": \"2026-05-14T18:14:28.321766+00:00\", \"ended_at\": null}, {\"worker_id\": \"worker_monitor_eval-progress-check_20260514T181508\", \"task_type\": \"monitor:eval-progress-check\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"running\", \"started_at\": \"2026-05-14T18:15:08.884238+00:00\", \"ended_at\": null}, {\"worker_id\": \"worker_code_crm-v3-normalization-prep_20260514T181524\", \"task_type\": \"code:crm-v3-normalization-prep\", \"project\": \"acr-vla-conformal-refinement\", \"status\": \"running\", \"started_at\": \"2026-05-14T18:15:25.099743+00:00\", \"ended_at\": null}], \"count\": 4}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "mcp__agent-ml-research__list_workers",
  "elapsed_ms": 11337
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T18:15:53.661596+00:00_

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
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/skills/resource-saturation.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T18:15:53.712600+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/.claude/sessions/agent_327cd2f3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T18:15:56.281932+00:00_

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
  "session": "cron:hook:precompute-v4-shard1",
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

_source line 17 · 2026-05-14T18:15:56.332809+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T18:15:58.902433+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/resource-saturation*",
  "path": "/home/ubuntu/agent-ml-research"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/resource-saturation*",
    "path": "/home/ubuntu/agent-ml-research"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T18:15:59.053400+00:00_

/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Glob",
  "elapsed_ms": 150
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-14T18:16:01.524278+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/resource-saturation.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-14T18:16:01.575249+00:00_

1	---
2	name: resource-saturation
3	description: "当你准备向 Director 汇报前、收到 cron/worker 回调、审批通过准备开跑、怀疑 Worker 池不够饱和时,立即使用本 skill。四部分:A) GPU 分配率(分配了没跑=失职) B) GPU 效率 C) 非 GPU 任务并行(Worker 池<2=失职) D) 汇报必须带 [资源] 行。"
4	always: false
5	roles:
6	  - director
7	  - agent
8	---
9	
10	# 资源饱和度自检（硬约束）
11	
12	## A. GPU 分配率检查
13	
14	调 `get_project_resource_usage(project)` 看:
15	- 已分配给本项目的 GPU 总数和具体卡号
16	- 实际在跑任务的 GPU 数和具体卡号（交叉 registry RUNNING + nvidia-smi 进程）
17	- 分配了但没跑的 GPU 清单 ⚠️
18	
19	任何"分配了但没跑"的 GPU = 失职。必须立即:
20	- 派 Worker 铺 dry-run / 下一批实验代码准备
21	- 铺 ablation（从 experiment-matrix 空白格子里挑）
22	- 确实无实验可铺 → 向 Director 汇报"暂无可铺实验"+ 建议下一步方向(扩 ablation 维度 / 加 baseline / 加 benchmark)。**不要建议归还 GPU**——项目级 GPU 归还只在归档时由 `archive_project` 自动触发, 不是 Director 中途的动作
23	
24	**单实验不占多卡**: 分配 4 卡但实验只用 1 卡 → 另 3 卡必须并行跑其他实验,不能空占。
25	
26	## B. GPU 效率检查
27	
28	调 `get_gpu_health(server)`:
29	- 空闲 GPU（util < 10% 持续 > 5 min）→ 立即铺任务
30	- 低利用率（util < 50% 持续 > 15 min）→ spawn_worker 诊断（batch / IO / 同步）
31	- OOM 风险（显存 > 90% 持续 10 min）→ 主动降 batch / 调优
32	
33	## C. 非 GPU 任务并行
34	
35	GPU 在跑 ≠ 你空闲。以下 CPU / 网络任务**必须**派独立 Worker 并行:
36	- 下一批实验的数据集下载 / 预处理 / fingerprint
37	- 下一批实验的代码准备 / dry-run / 环境配置
38	- 论文文献调研 / related work 检索
39	- 已完成实验的 log 深度分析 / metric 聚合
40	- 论文章节起草
41	- 代码 review / refactor
42	
43	**硬约束**: 任一时刻 Worker 池 < 2 个 = 失职（除非真的全部下游阻塞在等 GPU,这时应当向 Director 申请扩 GPU）。
44	
45	## D. 汇报格式
46	
47	向 Director 汇报时开头必须带资源声明行:
48	
49	    [资源] GPU 分配 N / 实际在跑 M | Worker 池 K (其中 GPU 任务 A / CPU 任务 B)
50	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-14T18:16:14.260600+00:00_

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
  "session": "cron:hook:precompute-v4-shard1",
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

_source line 23 · 2026-05-14T18:16:14.413435+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "ToolSearch",
  "elapsed_ms": 152
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-14T18:16:35.059649+00:00_

called mcp__agent-ml-research__main_agent_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__main_agent_post_to_director</summary>

```json
{
  "text": "[资源] GPU 分配 5 / 实际在跑 5 | Worker 池 4 (GPU 任务 0 / CPU 任务 4)\n\n**Session #4 启动，状态同步完成。**\n\n**5 路 eval 全部 RUNNING**（reconcile_crons 确认 PID 存活）：\n| exp_id | 服务器:GPU | 内容 |\n|--------|-----------|------|\n| eval-acr-spatial-v3 | bjb1:0 | 核心 claim: ACR-VLA CRM v2 vs baseline 30% |\n| eval-argmin-only-spatial | bjb1:1 | 诊断: 隔离 argmin 选择贡献 |\n| eval-tiny-correction-spatial | bjb1:2 | 诊断: 极小 correction (0.05) 测试 over-correction |\n| eval-acr-object-v3 | bjb1:3 | 跨 benchmark: ACR-VLA on object |\n| eval-vla-mean-spatial | bjb2:0 | baseline: K=10 mean action |\n\n**4 个 Worker 活跃**：\n1. verify:bjb2-cache-and-training-status — bjb2 环境验证\n2. check:eval-progress-all — bjb1 四路 eval 进展监控\n3. monitor:eval-progress-check — eval 进展监控\n4. code:crm-v3-normalization-prep — CRM v3 normalization 代码准备（D018 批准）\n\n**PREPARING 队列**：CRM v3 三路重训练（crm-train-v3-perdof/scalar-unc/obs-only），等 GPU 释放后推进。\n\n**关键等待点**：5 路 eval 完成 → 完整四路对比表 → 决定 core claim 是否成立。无阻塞项，全速推进中。",
  "project": "acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "tool_args": {
    "text": "[资源] GPU 分配 5 / 实际在跑 5 | Worker 池 4 (GPU 任务 0 / CPU 任务 4)\n\n**Session #4 启动，状态同步完成。**\n\n**5 路 eval 全部 RUNNING**（reconcile_crons 确认 PID 存活）：\n| exp_id | 服务器:GPU | 内容 |\n|--------|-----------|------|\n| eval-acr-spatial-v3 | bjb1:0 | 核心 claim: ACR-VLA CRM v2 vs baseline 30% |\n| eval-argmin-only-spatial | bjb1:1 | 诊断: 隔离 argmin 选择贡献 |\n| eval-tiny-correction-spatial | bjb1:2 | 诊断: 极小 correction (0.05) 测试 over-correction |\n| eval-acr-object-v3 | bjb1:3 | 跨 benchmark: ACR-VLA on object |\n| eval-vla-mean-spatial | bjb2:0 | baseline: K=10 mean action |\n\n**4 个 Worker 活跃**：\n1. verify:bjb2-cache-and-training-status — bjb2 环境验证\n2. check:eval-progress-all — bjb1 四路 eval 进展监控\n3. monitor:eval-progress-check — eval 进展监控\n4. code:crm-v3-normalization-prep — CRM v3 normalization 代码准备（D018 批准）\n\n**PREPARING 队列**：CRM v3 三路重训练（crm-train-v3-perdof/scalar-unc/obs-only），等 GPU 释放后推进。\n\n**关键等待点**：5 路 eval 完成 → 完整四路对比表 → 决定 core claim 是否成立。无阻塞项，全速推进中。",
    "project": "acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-14T18:16:39.082599+00:00_

{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_5ee1fd6fcd3e57fe38e03d67d16d0bf4:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "mcp__agent-ml-research__main_agent_post_to_director",
  "elapsed_ms": 4022
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-14T18:16:44.706402+00:00_

Session #4 初始化完成。

- 5 路 eval 全部 RUNNING，5 张 GPU 满载
- 4 个 Worker 活跃（监控 + CRM v3 代码准备）
- 3 个 CRM v3 训练实验 PREPARING 等 GPU 释放
- 已向 Director 汇报当前状态

等待 Worker 回调或 cron 回调推进下一步。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:precompute-v4-shard1"
}
```

</details>

---

## Round 2

44 recorded events

### User

_source line 27 · 2026-05-14T21:20:28.052049+00:00_

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
  "session": "cron:hook:precompute-v4-shard1",
  "source": "system:ralph_loop"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-14T21:20:49.573368+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Read registry and project files",
  "subagent_type": "Explore",
  "prompt": "I need to understand the current state of a research project called \"acr-vla-conformal-refinement\". Please find and read the following files:\n\n1. Any registry.yaml or registry file in the project directory /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/\n2. report.md in the same directory\n3. ROADMAP.md in the same directory\n4. memory.md in the same directory\n5. experiment_plan.yaml in the same directory\n6. paper_framing.md in the same directory\n\nSearch broadly - files could be in the root of the project dir or in subdirectories. Read as much of each file as possible and report the full contents."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Agent",
  "tool_args": {
    "description": "Read registry and project files",
    "subagent_type": "Explore",
    "prompt": "I need to understand the current state of a research project called \"acr-vla-conformal-refinement\". Please find and read the following files:\n\n1. Any registry.yaml or registry file in the project directory /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/\n2. report.md in the same directory\n3. ROADMAP.md in the same directory\n4. memory.md in the same directory\n5. experiment_plan.yaml in the same directory\n6. paper_framing.md in the same directory\n\nSearch broadly - files could be in the root of the project dir or in subdirectories. Read as much of each file as possible and report the full contents."
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T21:20:50.226461+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T21:20:50.277361+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/chats/feishu_group_oc_5ee1fd6fcd3e57fe38e03d67d16d0bf4_director.lock
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/study_status.lock
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.lock
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/chats/feishu_group_oc_718f2ee7260b8649b47875a90c263a2a_reviewer.lock
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/decisions.lock
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/chats/feishu_group_oc_718f2ee7260b8649b47875a90c263a2a.lock
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.lock
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/checkpoints/mvp-point-reaching_PREPARING_20260513T012210.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/checkpoints/mvp-point-reaching_QUEUED_20260513T014344.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/checkpoints/mvp-point-reaching_RUNNING_20260513T014348.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/checkpoints/mvp-point-reaching_RUNNING_20260513T014355.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/checkpoints/mvp-point-reaching_DONE_20260513T014400.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/mvp-point-reaching/data/mvp_results.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_code_mvp-point-reaching_20260513T012320.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/logs/workers/worker_code_
…[truncated 13090 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T21:20:51.533469+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement -type f \\( -name \"registry.yaml\" -o -name \"registry\" -o -name \"report.md\" -o -name \"ROADMAP.md\" -o -name \"memory.md\" -o -name \"experiment_plan.yaml\" -o -name \"paper_framing.md\" \\) 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement -type f \\( -name \"registry.yaml\" -o -name \"registry\" -o -name \"report.md\" -o -name \"ROADMAP.md\" -o -name \"memory.md\" -o -name \"experiment_plan.yaml\" -o -name \"paper_framing.md\" \\) 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T21:20:51.735526+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T023849/median/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T023849/worst/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/dream_reports/dream_20260513T023849/best/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/experiment_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Bash",
  "elapsed_ms": 202
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T21:20:53.243926+00:00_

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
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T21:20:53.645408+00:00_

File content (31169 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T21:20:53.645748+00:00_

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
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T21:20:53.645985+00:00_

1	# Handover — 2026-05-14
2	
3	> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。
4	
5	## 运行中
6	| exp_id | 假设 | 状态 | 关键指标 | W&B |
7	|--------|------|------|---------|-----|
8	| crm-train-v3-norm-scalar-unc | Ablation: scalar_unc input mode (scalar uncertainty only) with normalization. Tests per-DOF vs scalar uncertainty contribution with proper normalization. | — | — | — |
9	| crm-train-v3-norm-obs-only | Ablation: obs_only input mode (no uncertainty features) with normalization. Isolates contribution of obs features vs conformal features. | — | — | — |
10	| eval-acr-spatial-v4-small | D018: Normalization + moderate correction scaling (max_correction_norm=0.1, 14x smaller than default). If v4-small > v4-default → magnitude control needed on top of normalization. | — | — | — |
11	
12	## 待处理
13	- eval-object-v6-full（准备中）
14	- eval-reconvla-spatial-v1（准备中）
15	- precompute-v4-shard2（准备中）
16	- precompute-v4-shard1（准备中）
17	- precompute-v4-shard0（准备中）
18	- eval-spatial-v4-full（准备中）
19	- precompute-v3-shard2（准备中）
20	- precompute-v3-shard1（准备中）
21	- precompute-v3-shard0（准备中）
22	- precompute-v2-shard2（准备中）
23	- …另有 2 项
24	
25	## 近期结论
26	- **eval-acr-object-v3** (failed): —
27	- **eval-acr-spatial-v3** (failed): —
28	- **crm-train-v3-norm** (success): D018: Input normalization fixes 1500x scale imbalance in CRM inputs, enabling proper gradient flow and meaningful per-DOF correction learning ← 基于 crm-train-v3-perdof
29	
30	## 趋势
31	成功 15 / 负向 0 / 失败 7 / 共 44
32	best_epoch: 50 ↑（近 3 次 success）
33	best_val_loss: 0.050501 ↓（近 3 次 success）
34	
35	## 下一步
36	（无活跃 idea，请通过 ideas.md 添加）
37	
38	## 资源状态
39	bjb1-18228: 无 GPU 信息
40	bjb2-40593: 无 GPU 信息
41	
42	## 告警
43	- plan_001-crm-smolvla: 训练失败 — unknown
44	- plan_014-reconvla-baseline: 训练失败 — unknown
45	- eval-smolvla-libero-spatial: 训练失败 — unknown
46	- eval-spatial-reeval-v2: 已被终止 — unknown
47	- eval-spatial-v3-full: 已被终止 — unknown
48	- eval-object-v4-full: 已被终止 — unknown
49	- eval-spatial-v5-full: 已被终止 — unknown
50	- crm-train-v1: 已被终止 — unknown
51	-
…[truncated 893 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-14T21:20:53.897673+00:00_

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
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-14T21:20:54.099873+00:00_

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
…[truncated 1563 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Read",
  "elapsed_ms": 202
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-14T21:20:54.100416+00:00_

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
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T21:20:54.301589+00:00_

1	# Memory — acr-vla-conformal-refinement
2	
3	## Correction Magnitude 是核心问题（2026-05-14 18:15，早期信号）
4	
5	### 发现
6	eval-tiny-correction-spatial（max_correction_norm=0.05，约默认 1.42 的 1/28）在首个 task 上 4/5 成功，而 full ACR 同一 task 只有 1/10。这说明 CRM correction 的方向可能是对的，但幅度太大导致 compounding error。
7	
8	### 含义
9	- correction clipping / gating 是正确的补救方向
10	- Gated CRM 代码已就绪（`src/gated_crm.py` + `--mode acr_gated` + `--gate_threshold/mode/temperature`）
11	- 等完整 eval 结果确认后，下一步应该是 correction magnitude sweep（0.01, 0.05, 0.1, 0.2, 0.5）或 Gated CRM eval
12	- **不改变目标 venue（ICLR 2027）**，narrative 可从 "per-DOF correction always helps" 调整为 "per-DOF correction with magnitude control"
13	
14	### ⚠️ 注意
15	这是 1 个 task 的 5 个 rollout 的早期数据。需要完整 10 tasks 确认。
16	
17	## Correction Magnitude 文献支撑（2026-05-14 18:37）
18	
19	### 核心竞品/支撑论文
20	1. **PLD (ICLR 2026)**: scheduled ξ bound，LIBERO ξ=0.5 / SimplerEnv ξ=0.1——不同环境需不同 correction scale，完全验证我们的发现
21	2. **TRANSIC (CoRL 2024)**: 无 gate 时 fine-tuning 导致 model collapse——与我们 40%→2.5% 退化一致
22	3. **ResiP (CoRL-W 2024)**: scaling α≤1，关键不是精确值而是 order of magnitude
23	4. **DRC (2025)**: temporal decay of correction
24	5. **DAWN (2026)**: scale mismatch → residual 学不好
25	
26	### 独特贡献角度
27	**没有现有方法提供 per-DOF, per-timestep, calibrated magnitude bounds。** ACR-VLA 的 conformal intervals 天然提供 calibrated bounds on expected action range。
28	
29	### 推荐 Framing 调整方向
30	"Conformally-Calibrated Correction Magnitude" — CP intervals 作为 correction 幅度的自然上界，不依赖固定超参数（α, ξ）或 binary gate。
31	
32	### 对比表（可用于论文 Table 1）
33	| Method | Bound Type | Per-DOF | Per-Timestep | Calibrated |
34	|--------|-----------|---------|-------------|------------|
35	| Silver 2018 | Action space | ✗ | ✗ | ✗ |
36	| Johannink 2019 | Fixed tube | ✗ | ✗ | ✗ |
37	| TRANSIC 2024 | Binary gate | ✗ | ✓ | ✗ |
38	| PLD 2026 | Scheduled ξ | ✗ | ~ | ✗ |
39	| **ACR-VLA** | **CP intervals** | **✓** | **✓** | **✓** |
40	
41	## CRM v3-norm 训练结果（2026-05-14 20:06）
42	
43	### 结果
44	- best_val_loss=0.03578 (epoch 47/50)，收敛稳定
45
…[truncated 5423 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-14T21:20:54.302491+00:00_

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
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/experiment_plan.yaml"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-14T21:20:54.506491+00:00_

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
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Read",
  "elapsed_ms": 203
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-14T21:20:54.506846+00:00_

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
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/paper_framing.md"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-14T21:20:54.557464+00:00_

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
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-14T21:20:57.776426+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "limit": "500",
  "offset": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "limit": "500",
    "offset": "0"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-14T21:20:57.777037+00:00_

0	baseline: null
1	experiments:
2	  mvp-point-reaching:
3	    status: DONE
4	    retry_count: 0
5	    created_at: '2026-05-13T01:22:10.415Z'
6	    updated_at: '2026-05-13T22:06:11.073Z'
7	    spec:
8	      hypothesis: Per-DOF uncertainty features carry more actionable information than
9	        scalar uncertainty summaries, enabling dimension-selective correction
10	      description: '3D point-reaching MVP: 3 MLP variants (scalar/per-DOF/no uncertainty)
11	        x 6 groups (3 anisotropy ratios x 2 uncertainty sources)'
12	      server: bjb2-40593
13	      gpu: cuda:0
14	      data_count: 20000
15	      model_name: CorrectionMLP(2-layer, 64-hidden)
16	      seed: 42
17	      command: python -u run_mvp.py
18	      data_path: synthetic (generated in-script)
19	      checkpoint_path: /root/acr-vla-conformal-refinement/mvp/
20	      log_path: /root/acr-vla-conformal-refinement/mvp/mvp_results.log
21	    conclusion: success
22	    completed_at: '2026-05-13T01:44:00.055Z'
23	    metrics:
24	      group1_oracle:
25	        A_scalar:
26	          mse_x: 0.180218
27	          mse_y: 0.02497
28	          mse_z: 0.024232
29	          total: 0.076473
30	        B_perDOF:
31	          mse_x: 0.172652
32	          mse_y: 0.015544
33	          mse_z: 0.01561
34	          total: 0.067935
35	        C_none:
36	          mse_x: 0.22706
37	          mse_y: 0.025542
38	          mse_z: 0.024753
39	          total: 0.092451
40	      group2_oracle:
41	        A_scalar:
42	          mse_x: 0.064642
43	          mse_y: 0.023836
44	          mse_z: 0.022967
45	          total: 0.037148
46	        B_perDOF:
47	          mse_x: 0.053403
48	          mse_y: 0.015695
49	          mse_z: 0.01573
50	          total: 0.028276
51	        C_none:
52	          mse_x: 0.084178
53	          mse_y: 0.025427
54	          mse_z: 0.024798
55	          total: 0.044801
56	      group3_oracle:
57	        A_scalar:
58	          mse_x: 0.042948
59	          mse_y: 0.023218
60	          mse_z: 0.022365
61	    
…[truncated 18490 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-14T21:20:57.928106+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "limit": "500",
  "offset": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "limit": "500",
    "offset": "500"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-14T21:20:57.928891+00:00_

500	    created_at: '2026-05-13T18:58:09.830Z'
501	    updated_at: '2026-05-13T20:07:52.129Z'
502	    spec:
503	      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
504	        base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1
505	        && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task
506	        10 --shard_id 0 --num_shards 3 --seed 42 --K 10 --cache_dir /root/autodl-tmp/crm_cache/
507	        2>&1"
508	      server: bjb1-18228
509	      gpu:
510	      - cuda:1
511	      pid: '69647'
512	      log_path: ~/runs/acr-vla-conformal-refinement/precompute-v4-shard0.log
513	      submitted_at: '2026-05-13T18:58:09.802Z'
514	      submitted_via: submit_training_job
515	      backend: tmux
516	      account: root
517	      checkpoint_path: /root/autodl-tmp/crm_cache/
518	    reproduce:
519	      finished_at: '2026-05-13T20:04:45.258Z'
520	    extra:
521	      hook_events:
522	      - event: on_complete
523	        action: agent
524	        ts: '2026-05-13T20:04:50.222546+00:00'
525	    conclusion: success
526	  precompute-v4-shard1:
527	    status: PREPARING
528	    retry_count: 0
529	    created_at: '2026-05-13T18:58:12.183Z'
530	    updated_at: '2026-05-13T20:07:53.062Z'
531	    spec:
532	      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
533	        base && cd /root/acr-vla-conformal-refinement && export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1
534	        && python -u src/train_crm.py --precompute --benchmark spatial object --max_demos_per_task
535	        10 --shard_id 1 --num_shards 3 --seed 42 --K 10 --cache_dir /root/autodl-tmp/crm_cache/
536	        2>&1"
537	      server: bjb1-18228
538	      gpu:
539	      - cuda:2
540	      pid: '69793'
541	      log_path: ~/runs/acr-vla-conformal-refinement/precompute-v4-shard1.log
542	      submitted_at: '2026-05-13T18:58:12.154Z'
543	      submitted_via: submit_trai
…[truncated 19526 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-14T21:21:00.246618+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "limit": "500",
  "offset": "1000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "limit": "500",
    "offset": "1000"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-14T21:21:00.448064+00:00_

1000	    retry_count: 0
1001	    created_at: '2026-05-13T23:28:33.119Z'
1002	    updated_at: '2026-05-13T23:29:33.175Z'
1003	    spec:
1004	      data_path: /root/autodl-tmp/libero_data/ (object)
1005	      data_count: 100
1006	      model_name: lerobot/smolvla_libero
1007	      seed: 42
1008	      hypothesis: SmolVLA baseline success rate on libero_object with fixed evaluate.py
1009	        (env.reset bug removed, 5-step zero-action stabilization)
1010	      checkpoint_source: lerobot/smolvla_libero
1011	      eval_data: libero_object 10 tasks x 10 rollouts
1012	    conclusion: killed
1013	  crm-train-a4-scalar-unc:
1014	    status: DONE
1015	    retry_count: 0
1016	    created_at: '2026-05-13T23:48:40.837Z'
1017	    updated_at: '2026-05-14T07:59:32.676Z'
1018	    spec:
1019	      command: CUDA_VISIBLE_DEVICES=3 python -u src/train_crm.py --benchmark spatial
1020	        object --epochs 50 --batch_size 32 --lr 0.001 --K 10 --seed 42 --input_mode
1021	        scalar_unc --output_dir /root/autodl-tmp/checkpoints/crm/scalar_unc/
1022	      server: bjb1-18228
1023	      gpu:
1024	      - cuda:3
1025	      pid: '121984'
1026	      data_path: /root/autodl-tmp/crm_cache/
1027	      data_count: 26737
1028	      model_name: CRM-scalar_unc (3D scalar uncertainty)
1029	      seed: 42
1030	      hypothesis: CRM with scalar Euclidean uncertainty (3D) performs worse than per-DOF
1031	        (40D), validating per-DOF advantage. Ablation A4, hyperparams matched to plan_001
1032	        (bs=32/lr=1e-3).
1033	      log_path: /root/autodl-tmp/checkpoints/crm/scalar_unc/train.log
1034	      checkpoint_path: /root/autodl-tmp/checkpoints/crm/scalar_unc/crm_best.pt
1035	      conclusion_note: Training converged. scalar val_loss 0.008379 < per-DOF 0.009046
1036	        — original hypothesis (scalar worse) NOT confirmed on val_loss. Hypothesis
1037	        pending eval-scalar-unc-spatial task success rate validation.
1038	    conclusion: killed
1039	    checkpoint_path: /root/autodl-tmp/c
…[truncated 21065 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-14T21:21:00.599828+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "limit": "500",
  "offset": "1500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "limit": "500",
    "offset": "1500"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-14T21:21:00.650958+00:00_

1500	        VLA K=1 (30%) and SampleConsensus (34%) on LIBERO spatial. CORE CLAIM experiment.
1501	      checkpoint_source: /root/autodl-tmp/checkpoints/crm_v2/perdof/crm_best.pt
1502	      eval_data: LIBERO spatial 10 tasks x 10 rollouts
1503	      wall_clock_seconds: 28899.4
1504	      gpu_hours: 8.03
1505	    metrics:
1506	      tasks_done: 4/10
1507	      overall_success_rate: 0.025
1508	      total_successes: 1
1509	      total_rollouts: 40
1510	      per_task_partial:
1511	        pick_up_black_bowl_between_plate_and_ramekin: 0.1
1512	        pick_up_black_bowl_next_to_ramekin: 0
1513	        pick_up_black_bowl_from_table_center: 0
1514	        pick_up_black_bowl_on_cookie_box: 0
1515	      snapshot_time: 2026-05-14T18:15Z
1516	    conclusion: failed
1517	    reproduce:
1518	      finished_at: '2026-05-14T20:18:44.725Z'
1519	    failure_reason: process dead 5× with no sentinel/W&B — auto-resolved as failed
1520	    completed_at: '2026-05-14T20:18:45.380Z'
1521	    extra:
1522	      hook_events:
1523	      - event: on_failed
1524	        action: agent
1525	        ts: '2026-05-14T20:18:46.631294+00:00'
1526	  eval-scalar-unc-spatial-v2:
1527	    status: DONE
1528	    retry_count: 0
1529	    created_at: '2026-05-14T12:17:08.413Z'
1530	    updated_at: '2026-05-14T17:47:53.188Z'
1531	    spec:
1532	      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
1533	        base && cd /root/acr-vla-conformal-refinement && CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl
1534	        MUJOCO_EGL_DEVICE_ID=0 python -u src/evaluate.py --mode crm_scalar --benchmark
1535	        spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v2/scalar_unc/crm_best.pt"
1536	      server: bjb1-18228
1537	      gpu:
1538	      - cuda:1
1539	      pid: '197324'
1540	      log_path: ~/runs/acr-vla-conformal-refinement/eval-scalar-unc-spatial-v2.log
1541	      submitted_at: '2026-05-14T12:17:08.325Z'
1542	      submitted_via: submit_tr
…[truncated 21394 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-14T21:21:22.913635+00:00_

Perfect! Now I have all the key files. Let me provide you with a comprehensive summary of the project's current state.

## Summary: ACR-VLA Conformal Refinement Research Project

### Project Overview
This is a research project targeting **ICLR 2027** (previously abandoned CoRL 2026) focused on developing **ACR-VLA (Action Correction via conformal Regression for Vision Language Action models)**.

**Core Innovation**: Per-DOF (degree-of-freedom) conformal statistics from multivariate conformal prediction enable dimension-selective action correction. The key hypothesis is that structured uncertainty features (40D per-DOF features vs scalar uncertainty) provide more actionable information for learned action correction.

### Current Status (as of May 14, 2026)

**Phase**: Phase 2 — Spatial Eval four-way comparison (ACR-VLA / SampleConsensus / Scalar-CRM / VLA-mean)

**MVP Status**: PASS (plan_000 complete, per-DOF > scalar > none confirmed)

**Key Milestones Completed**:
- MVP experiment validating per-DOF > scalar uncertainty (6.75% improvement)
- SmolVLA baseline locked at 30% spatial, 13% object (K=1)
- SampleConsensus (renamed from ReconVLA) baseline at 34% spatial
- CRM training v2 completed with bug fixes (8D state, argmin base, alpha=0.5, L2 clipping)
- Three major bug fixes implemented (D014-D018)

**Critical Issues Discovered**:
1. **CRM Correction Degradation**: Full ACR-VLA shows 2.5% success (23-26%) compared to 30% baseline — correction magnitude appears to be the problem
2. **Early Signal from Magnitude Sweep**: tiny-correction (max_norm=0.05) achieved 4/5 on first task vs 1/10 for full ACR-VLA, suggesting correction clipping/gating is needed
3. **Major bugs fixed**:
   - D016: State dimension mismatch (6D vs 8D) in CRM training
   - D018: Input normalization — 1500x scale imbalance in CRM features
   - D015: K=1 fix for vla_only mode (was unnecessarily running K=10)

### Baselines & Comparisons
- **VLA-only (K=1) baseline**: 30% spatial, 13% object
- **Sam
…[truncated 3469 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Agent",
  "elapsed_ms": 33340
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-14T21:21:27.182335+00:00_

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
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-14T21:21:27.634303+00:00_

1	# Handover — 2026-05-14
2	
3	> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。
4	
5	## 运行中
6	| exp_id | 假设 | 状态 | 关键指标 | W&B |
7	|--------|------|------|---------|-----|
8	| crm-train-v3-norm-scalar-unc | Ablation: scalar_unc input mode (scalar uncertainty only) with normalization. Tests per-DOF vs scalar uncertainty contribution with proper normalization. | — | — | — |
9	| crm-train-v3-norm-obs-only | Ablation: obs_only input mode (no uncertainty features) with normalization. Isolates contribution of obs features vs conformal features. | — | — | — |
10	| eval-acr-spatial-v4-small | D018: Normalization + moderate correction scaling (max_correction_norm=0.1, 14x smaller than default). If v4-small > v4-default → magnitude control needed on top of normalization. | — | — | — |
11	
12	## 待处理
13	- eval-object-v6-full（准备中）
14	- eval-reconvla-spatial-v1（准备中）
15	- precompute-v4-shard2（准备中）
16	- precompute-v4-shard1（准备中）
17	- precompute-v4-shard0（准备中）
18	- eval-spatial-v4-full（准备中）
19	- precompute-v3-shard2（准备中）
20	- precompute-v3-shard1（准备中）
21	- precompute-v3-shard0（准备中）
22	- precompute-v2-shard2（准备中）
23	- …另有 2 项
24	
25	## 近期结论
26	- **eval-acr-object-v3** (failed): —
27	- **eval-acr-spatial-v3** (failed): —
28	- **crm-train-v3-norm** (success): D018: Input normalization fixes 1500x scale imbalance in CRM inputs, enabling proper gradient flow and meaningful per-DOF correction learning ← 基于 crm-train-v3-perdof
29	
30	## 趋势
31	成功 15 / 负向 0 / 失败 7 / 共 44
32	best_epoch: 50 ↑（近 3 次 success）
33	best_val_loss: 0.050501 ↓（近 3 次 success）
34	
35	## 下一步
36	（无活跃 idea，请通过 ideas.md 添加）
37	
38	## 资源状态
39	bjb1-18228: 无 GPU 信息
40	bjb2-40593: 无 GPU 信息
41	
42	## 告警
43	- plan_001-crm-smolvla: 训练失败 — unknown
44	- plan_014-reconvla-baseline: 训练失败 — unknown
45	- eval-smolvla-libero-spatial: 训练失败 — unknown
46	- eval-spatial-reeval-v2: 已被终止 — unknown
47	- eval-spatial-v3-full: 已被终止 — unknown
48	- eval-object-v4-full: 已被终止 — unknown
49	- eval-spatial-v5-full: 已被终止 — unknown
50	- crm-train-v1: 已被终止 — unknown
51	-
…[truncated 893 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-14T21:21:27.634756+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "limit": "200"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-14T21:21:28.237166+00:00_

1	baseline: null
2	experiments:
3	  mvp-point-reaching:
4	    status: DONE
5	    retry_count: 0
6	    created_at: '2026-05-13T01:22:10.415Z'
7	    updated_at: '2026-05-13T22:06:11.073Z'
8	    spec:
9	      hypothesis: Per-DOF uncertainty features carry more actionable information than
10	        scalar uncertainty summaries, enabling dimension-selective correction
11	      description: '3D point-reaching MVP: 3 MLP variants (scalar/per-DOF/no uncertainty)
12	        x 6 groups (3 anisotropy ratios x 2 uncertainty sources)'
13	      server: bjb2-40593
14	      gpu: cuda:0
15	      data_count: 20000
16	      model_name: CorrectionMLP(2-layer, 64-hidden)
17	      seed: 42
18	      command: python -u run_mvp.py
19	      data_path: synthetic (generated in-script)
20	      checkpoint_path: /root/acr-vla-conformal-refinement/mvp/
21	      log_path: /root/acr-vla-conformal-refinement/mvp/mvp_results.log
22	    conclusion: success
23	    completed_at: '2026-05-13T01:44:00.055Z'
24	    metrics:
25	      group1_oracle:
26	        A_scalar:
27	          mse_x: 0.180218
28	          mse_y: 0.02497
29	          mse_z: 0.024232
30	          total: 0.076473
31	        B_perDOF:
32	          mse_x: 0.172652
33	          mse_y: 0.015544
34	          mse_z: 0.01561
35	          total: 0.067935
36	        C_none:
37	          mse_x: 0.22706
38	          mse_y: 0.025542
39	          mse_z: 0.024753
40	          total: 0.092451
41	      group2_oracle:
42	        A_scalar:
43	          mse_x: 0.064642
44	          mse_y: 0.023836
45	          mse_z: 0.022967
46	          total: 0.037148
47	        B_perDOF:
48	          mse_x: 0.053403
49	          mse_y: 0.015695
50	          mse_z: 0.01573
51	          total: 0.028276
52	        C_none:
53	          mse_x: 0.084178
54	          mse_y: 0.025427
55	          mse_z: 0.024798
56	          total: 0.044801
57	      group3_oracle:
58	        A_scalar:
59	          mse_x: 0.042948
60	          mse_y: 0.023218
61	          mse_z: 0.022365
62	   
…[truncated 4968 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-14T21:21:28.237629+00:00_

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
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-14T21:21:28.288357+00:00_

1	# Memory — acr-vla-conformal-refinement
2	
3	## Correction Magnitude 是核心问题（2026-05-14 18:15，早期信号）
4	
5	### 发现
6	eval-tiny-correction-spatial（max_correction_norm=0.05，约默认 1.42 的 1/28）在首个 task 上 4/5 成功，而 full ACR 同一 task 只有 1/10。这说明 CRM correction 的方向可能是对的，但幅度太大导致 compounding error。
7	
8	### 含义
9	- correction clipping / gating 是正确的补救方向
10	- Gated CRM 代码已就绪（`src/gated_crm.py` + `--mode acr_gated` + `--gate_threshold/mode/temperature`）
11	- 等完整 eval 结果确认后，下一步应该是 correction magnitude sweep（0.01, 0.05, 0.1, 0.2, 0.5）或 Gated CRM eval
12	- **不改变目标 venue（ICLR 2027）**，narrative 可从 "per-DOF correction always helps" 调整为 "per-DOF correction with magnitude control"
13	
14	### ⚠️ 注意
15	这是 1 个 task 的 5 个 rollout 的早期数据。需要完整 10 tasks 确认。
16	
17	## Correction Magnitude 文献支撑（2026-05-14 18:37）
18	
19	### 核心竞品/支撑论文
20	1. **PLD (ICLR 2026)**: scheduled ξ bound，LIBERO ξ=0.5 / SimplerEnv ξ=0.1——不同环境需不同 correction scale，完全验证我们的发现
21	2. **TRANSIC (CoRL 2024)**: 无 gate 时 fine-tuning 导致 model collapse——与我们 40%→2.5% 退化一致
22	3. **ResiP (CoRL-W 2024)**: scaling α≤1，关键不是精确值而是 order of magnitude
23	4. **DRC (2025)**: temporal decay of correction
24	5. **DAWN (2026)**: scale mismatch → residual 学不好
25	
26	### 独特贡献角度
27	**没有现有方法提供 per-DOF, per-timestep, calibrated magnitude bounds。** ACR-VLA 的 conformal intervals 天然提供 calibrated bounds on expected action range。
28	
29	### 推荐 Framing 调整方向
30	"Conformally-Calibrated Correction Magnitude" — CP intervals 作为 correction 幅度的自然上界，不依赖固定超参数（α, ξ）或 binary gate。
31	
32	### 对比表（可用于论文 Table 1）
33	| Method | Bound Type | Per-DOF | Per-Timestep | Calibrated |
34	|--------|-----------|---------|-------------|------------|
35	| Silver 2018 | Action space | ✗ | ✗ | ✗ |
36	| Johannink 2019 | Fixed tube | ✗ | ✗ | ✗ |
37	| TRANSIC 2024 | Binary gate | ✗ | ✓ | ✗ |
38	| PLD 2026 | Scheduled ξ | ✗ | ~ | ✗ |
39	| **ACR-VLA** | **CP intervals** | **✓** | **✓** | **✓** |
40	
41	## CRM v3-norm 训练结果（2026-05-14 20:06）
42	
43	### 结果
44	- best_val_loss=0.03578 (epoch 47/50)，收敛稳定
45
…[truncated 5423 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-14T21:21:33.608668+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "offset": "200",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "offset": "200",
    "limit": "500"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-14T21:21:33.860438+00:00_

200	      data_path: /root/autodl-tmp/libero_data/ (spatial)
201	      data_count: 10 tasks x 3 rollouts x 300 steps
202	      model_name: lerobot/smolvla_libero (450M, full fine-tuned on libero_spatial)
203	      seed: 42
204	      hypothesis: Validate smolvla_libero checkpoint with fixed wrapper (correct state
205	        repr, 256x256 images, 7D action) achieves >50% success on libero_spatial
206	      log_path: /tmp/eval_spatial_full.log
207	      checkpoint_source: lerobot/smolvla_libero (HuggingFace community checkpoint)
208	      failure_reason: 'smolvla_libero 0% on spatial - 6 wrapper bugs: image flip/size/normalization,
209	        state 6D→8D, state normalization, action denormalization all missing'
210	      checkpoint_path: N/A
211	    conclusion: failed
212	    completed_at: '2026-05-13T15:45:51.082Z'
213	  precompute-shard0:
214	    status: DONE
215	    retry_count: 0
216	    created_at: '2026-05-13T11:57:45.284Z'
217	    updated_at: '2026-05-13T15:26:05.433Z'
218	    spec:
219	      command: bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate
220	        base && cd /root/acr-vla-conformal-refinement && python -u src/train_crm.py
221	        --precompute --benchmark spatial object --max_demos_per_task 10 --shard_id
222	        0 --num_shards 3 --seed 42 --K 10"
223	      server: bjb1-18228
224	      gpu:
225	      - cuda:1
226	      pid: '46966'
227	      log_path: ~/runs/acr-vla-conformal-refinement/precompute-shard0.log
228	      submitted_at: '2026-05-13T11:57:45.270Z'
229	      submitted_via: submit_training_job
230	      backend: tmux
231	      account: root
232	      checkpoint_path: /root/autodl-tmp/crm_cache/
233	      wall_clock_seconds: 12500.2
234	      gpu_hours: 3.47
235	    conclusion: success
236	    completed_at: '2026-05-13T15:26:05.433Z'
237	  precompute-shard1:
238	    status: DONE
239	    retry_count: 0
240	    created_at: '2026-05-13T11:57:46.669Z'
241	    updated_at: '2026-05-13T15:26:06.485Z'
242	    spec:

…[truncated 20103 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-14T21:21:33.861049+00:00_

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
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md"
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-14T21:21:33.964566+00:00_

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
…[truncated 1563 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Read",
  "elapsed_ms": 103
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-14T21:21:39.433577+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "offset": "700",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "offset": "700",
    "limit": "500"
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-14T21:21:39.486483+00:00_

700	      - event: on_failed
701	        action: agent
702	        ts: '2026-05-13T20:26:37.521060+00:00'
703	      - event: on_failed
704	        action: agent
705	        ts: '2026-05-13T22:59:44.694612+00:00'
706	  precompute-k5:
707	    status: DONE
708	    retry_count: 0
709	    created_at: '2026-05-13T20:15:37.603Z'
710	    updated_at: '2026-05-13T22:12:39.543Z'
711	    spec:
712	      command: python -u src/train_crm.py --precompute --benchmark spatial object
713	        --K 5 --cache_dir /root/autodl-tmp/crm_cache_k5/
714	      server: bjb1-18228
715	      gpu:
716	      - cuda:3
717	      pid: '79517'
718	      log_path: ~/runs/acr-vla-conformal-refinement/precompute-k5.log
719	      data_path: /root/autodl-tmp/libero_data/
720	      data_count: 26737
721	      model_name: smolvla_libero
722	      seed: 42
723	      hypothesis: K=5 precompute for K sensitivity ablation (plan_015)
724	    reproduce:
725	      finished_at: '2026-05-13T22:09:33.445Z'
726	    extra:
727	      hook_events:
728	      - event: on_complete
729	        action: agent
730	        ts: '2026-05-13T22:09:34.396952+00:00'
731	    conclusion: success
732	    checkpoint_path: /root/autodl-tmp/crm_cache_k5/
733	    metrics:
734	      spatial_samples: 12167
735	      object_samples: 14570
736	      total_samples: 26737
737	      spatial_cache_mb: 106
738	      object_cache_mb: 127
739	      total_cache_mb: 233
740	      runtime_min: 107
741	    completed_at: '2026-05-13T22:12:39.543Z'
742	  eval-reconvla-spatial-v2:
743	    status: DONE
744	    retry_count: 0
745	    created_at: '2026-05-13T20:29:41.730Z'
746	    updated_at: '2026-05-13T23:12:10.958Z'
747	    spec:
748	      command: python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts
749	        10 --seed 42 --K 10
750	      server: bjb1-18228
751	      gpu:
752	      - cuda:2
753	      pid: '87787'
754	      log_path: ~/runs/acr-vla-conformal-refinement/eval-reconvla-spatial-v1.log
755	      data_path: /root/autodl-tm
…[truncated 19834 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-14T21:21:43.852814+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "offset": "1200",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "offset": "1200",
    "limit": "500"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-14T21:21:43.853521+00:00_

1200	      model_name: CRM (K=5, 337K params)
1201	      seed: 42
1202	      hypothesis: CRM with K=5 conformal samples for K sensitivity ablation (K=10
1203	        baseline val_loss=0.009046)
1204	      log_path: /root/autodl-tmp/checkpoints/crm/k5/train.log
1205	      checkpoint_source: from_scratch
1206	      checkpoint_path: /root/autodl-tmp/checkpoints/crm/k5/crm_best.pt
1207	    reproduce:
1208	      finished_at: '2026-05-14T04:12:42.247Z'
1209	    extra:
1210	      hook_events:
1211	      - event: on_complete
1212	        action: agent
1213	        ts: '2026-05-14T04:12:44.286094+00:00'
1214	    conclusion: killed
1215	    metrics:
1216	      best_val_loss: 0.008996
1217	      best_epoch: 50
1218	      total_epochs: 50
1219	      comparison: K=5 val_loss 0.008996 ≈ K=10 val_loss 0.009046, near identical
1220	    completed_at: '2026-05-14T07:21:32.072Z'
1221	    conclusion_note: invalidated by D016 C1 fix, 6D state mismatch — checkpoint trained
1222	      on wrong features
1223	  eval-vla-mean-spatial:
1224	    status: RUNNING
1225	    retry_count: 0
1226	    created_at: '2026-05-14T03:10:44.114Z'
1227	    updated_at: '2026-05-14T03:11:46.546Z'
1228	    spec:
1229	      command: CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python
1230	        -u src/evaluate.py --mode vla_only --baseline_mode mean --benchmark spatial
1231	        --n_rollouts 10 --seed 42
1232	      server: bjb2-40593
1233	      gpu:
1234	      - cuda:0
1235	      pid: '143106'
1236	      data_path: /root/autodl-tmp/libero_data/ (spatial)
1237	      data_count: 100
1238	      model_name: SmolVLA K=10 mean action (no conformal)
1239	      seed: 42
1240	      hypothesis: K=10 mean baseline isolates multi-sampling averaging contribution
1241	        vs conformal correction. Expected between vla_only K=1 (30%) and ACR-VLA.
1242	      checkpoint_source: lerobot/smolvla_libero
1243	      eval_data: LIBERO spatial 10 tasks x 10 rollouts
1244	      log_path: /root/autodl-tmp/eval_resul
…[truncated 21755 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-14T21:21:48.119063+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "offset": "1700",
  "limit": "400"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "offset": "1700",
    "limit": "400"
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-14T21:21:48.170102+00:00_

1700	      submitted_via: submit_training_job
1701	      backend: tmux
1702	      account: root
1703	      data_path: /root/autodl-tmp/libero_data/
1704	      data_count: 100
1705	      model_name: CRM obs_only v2 (990D, no conformal features)
1706	      seed: 42
1707	      hypothesis: obs_only CRM ablation — CRM without conformal features tests whether
1708	        per-DOF conformal intervals are necessary
1709	      checkpoint_source: /root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt
1710	      eval_data: LIBERO spatial 10 tasks x 10 rollouts
1711	      parent: crm-train-v2-obs-only
1712	      conclusion_note: 'Director order: 0/30 after 3 tasks, no diagnostic value. Freed
1713	        bjb1:2 for eval-tiny-correction-spatial.'
1714	      metrics:
1715	        tasks_completed: 3
1716	        total_tasks: 10
1717	        success_rate: 0
1718	        successes: 0
1719	        rollouts: 30
1720	      checkpoint_path: /root/autodl-tmp/checkpoints/crm_v2/obs_only/crm_best.pt
1721	      wall_clock_seconds: 17890.8
1722	      gpu_hours: 4.97
1723	    conclusion: killed
1724	    completed_at: '2026-05-14T17:47:54.523Z'
1725	  eval-argmin-only-spatial:
1726	    status: RUNNING
1727	    retry_count: 0
1728	    created_at: '2026-05-14T17:47:58.683Z'
1729	    updated_at: '2026-05-14T17:48:54.942Z'
1730	    spec:
1731	      command: python -u src/evaluate.py --mode reconvla --benchmark spatial --n_rollouts
1732	        10 --seed 42 --K 10
1733	      server: bjb1-18228
1734	      gpu:
1735	      - cuda:1
1736	      pid: '231421'
1737	      log_path: ~/runs/acr-vla-conformal-refinement/eval-argmin-only-spatial.log
1738	      submitted_at: '2026-05-14T17:47:58.583Z'
1739	      submitted_via: submit_training_job
1740	      backend: tmux
1741	      account: root
1742	      gpu_ids:
1743	      - cuda:1
1744	      data_path: /root/autodl-tmp/libero_data/ (spatial)
1745	      data_count: 100
1746	      model_name: SmolVLA K=10 argmin selection (no CRM correction)
1747	      seed
…[truncated 12416 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "cron:hook:precompute-v4-shard1",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---

### Assistant

_source line 70 · 2026-05-14T21:22:44.508552+00:00_

Now I have all the information needed. Let me write the handoff.

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- **bjb1-18228 GPU 白名单**: cuda:0/1/2/3（4× RTX 4090）。bjb2-40593 只有 cuda:0（1× RTX 4090D）
- **crm_cache_v5 是唯一有效缓存**（路径 `/root/autodl-tmp/crm_cache_v5/`，bjb1 上）。v1-v4 全部因 D016（6D state mismatch）失效。**不要用 bjb2 上的 crm_cache/**
- **crm_v3_norm 是唯一有效 CRM checkpoint**（路径 `/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt`，bjb1）。v1/v2 全部因 D016 失效
- **bjb2 上的代码/数据滞后于 bjb1**：bjb2 的 crm_cache 是 v4（6D state，pre-D016），不能在 bjb2 上训 CRM 或做 ACR eval。eval-vla-mean-spatial 在 bjb2 跑是因为它不需要 CRM
- **evaluate.py 在 bjb1 上用 conda 环境**：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，不是 venv
- **HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1** 是必须的环境变量（AutoDL 无外网）
- **不要在同一 tmux session 名重复提交**，会覆盖之前的进程

### 2. 🖥️ 基础设施快照
- **bjb1-18228**（主力）: 4× RTX 4090, 工作目录 `/root/acr-vla-conformal-refinement/`, Python `/root/miniconda3/bin/python`, conda base
  - 模型: `/root/autodl-tmp/models/smolvla_libero/`（SmolVLA 450M, libero_spatial 微调）
  - 数据: `/root/autodl-tmp/libero_data/`（spatial + object）
  - CRM 缓存: `/root/autodl-tmp/crm_cache_v5/`（8D state, D016 修复后, 26737 samples）
  - CRM checkpoint: `/root/autodl-tmp/checkpoints/crm_v3_norm/perdof/crm_best.pt`（含 input_mean/input_std 归一化参数）
  - Eval 结果: `/root/autodl-tmp/eval_results/`
  - 日志: `~/runs/acr-vla-conformal-refinement/`
- **bjb2-40593**（辅助）: 1× RTX 4090D, 同样工作目录结构, conda base
  - ⚠️ 数据/代码已同步但 crm_cache 是旧版（v4, 6D state）
- **活跃进程**:
  - eval-vla-mean-spatial: bjb2 cuda:0, PID 143106, RUNNING
  - eval-argmin-only-spatial: bjb1 cuda:1, PID 231421, RUNNING
  - eval-tiny-correction-spatial: bjb1 cuda:2, PID 232815, RUNNING（task1 partial 4/5，早期信号强）
  - eval-acr-spatial-v4-default: bjb1 cuda:0, RUNNING（CRM v3-norm, default correction）
  - eval-acr-spatial-v4-small: bjb1 cuda:3, PID 253085, RUNNING（max_correction_norm=0.1）
  - crm-train-v3-norm-obs-only: bjb1, RUNNING（ablation 训练）
  - crm-train-v3-norm-scalar-unc: bjb1, RUNNING（ablation 训练）
- **GPU 预算**: 总 ~200h, 已用 ~80h, 剩余 ~120h

### 3. 📊 当前状态
**刚完成**: crm-train-v3-norm（D018 归一化修复，best_val_loss=0.03578），已启动 v4 eval 对（default vs small correction）和两个 ablation 训练。向 Director 汇报了 D018 诊断结果 + correction magnitude 文献调研 + 早期信号分析。

**Registry RUNNING 实验**:
1. `eval-acr-spatial-v4-default` — 归一化后 CRM，默认 correction，核心测试：是否修复 40%→2.5% 退化
2. `eval-acr-spatial-v4-small` — 归一化 + max_correction_norm=0.1，对比实验
3. `eval-tiny-correction-spatial` — max_correction_norm=0.05（极端 clipping），task1 早期 4/5 成功（vs full ACR 1/10）
4. `eval-argmin-only-spatial` — argmin-only 无 CRM correction，隔离 selection vs correction 贡献
5. `eval-vla-mean-spatial` — K=10 mean baseline，隔离多采样平均贡献
6. `crm-train-v3-norm-obs-only` — obs_only ablation，归一化版
7. `crm-train-v3-norm-scalar-unc` — scalar_unc ablation，归一化版

**等待**: 7 个 RUNNING 实验的 cron 回调。没有等待 Director 决策的阻塞项。

### 4. 📋 待办（条件触发式）
- **eval-acr-spatial-v4-default 完成 → 核心判定**：≥30% → 归一化修复成功，CRM correction 有效；<30% → correction magnitude 是根本问题，需走 "Conformally-Calibrated Correction Magnitude" framing
- **eval-acr-spatial-v4-small 完成 → 与 v4-default 对比**：v4-small > v4-default → magnitude control 是必要的 on top of normalization；v4-small ≈ v4-default → 归一化已足够
- **eval-tiny-correction-spatial 完成 → 确认 clipping 效果**：完整 10 tasks 确认 max_norm=0.05 是否稳定优于 full correction。如是，correction magnitude 控制是论文核心贡献之一
- **crm-train-v3-norm-{obs-only,scalar-unc} 完成 → 启动对应 eval**：分别用 crm_obs_only 和 crm_scalar 模式 eval，补齐四路对比表
- **eval-vla-mean-spatial 完成 → 锁定 K=10 mean baseline**：VLA mean 30-40% 范围内说明多采样有贡献但 conformal correction 的增量是关键
- **eval-argmin-only-spatial 完成 → 隔离 argmin selection 贡献**：argmin ≈ SampleConsensus (34%) 且 > VLA mean → selection 本身有价值；argmin < VLA mean → selection 策略需检查
- **四路对比表齐全 → 向 Director 汇报，决定是否铺 object benchmark / 调整 framing**

### 5. 🎯 战略上下文
- **目标**: ICLR 2027（DDL Sep-Oct 2026），CoRL 2026 已放弃（D011）
- **核心 claim**: Per-DOF conformal features enable dimension-selective action correction → MVP 确认（6.75% improvement），但 LIBERO 闭环 eval 中 CRM correction 严重退化（30%→2.5%）
- **当前关键悬念**: D018 归一化修复 + correction magnitude 控制是否能挽救 ACR-VLA。eval-acr-spatial-v4-{default,small} 是 make-or-break 实验
- **Framing 备选**: 如果 correction magnitude 控制是必须的，推荐 "Conformally-Calibrated Correction Magnitude" — CP intervals 作为 correction 幅度的自然上界（文献支撑已就绪：PLD/TRANSIC/ResiP/DRC/DAWN，见 memory.md）
- **SampleConsensus baseline**: 34% spatial（≈ VLA 30%，+4pp），是最直接竞品
- **Baselines 已锁定**: VLA K=1 spatial 30%, object 13%
- **易错点**:
  - crm_cache_v5 只在 bjb1 上，bjb2 上的 cache 是旧版——不要在 bjb2 训 CRM
  - CRM v1/v2 checkpoint 全部因 D016 失效，只有 v3-norm 有效
  - eval-acr-spatial-v3 的 2.5% 是 D018 归一化修复前的数据，不能作为最终结论
  - EXIT_CODE=129 不一定是失败（crm-train-v1 教训），要看 log 最后输出
  - evaluate.py 的 `--mode crm_obs_only` 和 `--mode crm_scalar` 是后加的，确认代码里有对应分支再用
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "cron:hook:precompute-v4-shard1"
}
```

</details>

---
