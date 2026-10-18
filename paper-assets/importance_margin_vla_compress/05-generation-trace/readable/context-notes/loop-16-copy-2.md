# agent / loop_16.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_16.md`
- **Structured JSON:** [`892eb939a88a8ce1dc54.json`](../../sessions/89/892eb939a88a8ce1dc54.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 16
reason: idle_timeout
updated: '2026-05-28T22:09:11+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单严格按 `get_project_status` 的 `execution.gpu_ids`：4 台服务器各 cuda:0-3，w27 实际只有 GPU0/GPU1
- π0.5 eval 必须用 strict metric（非 lenient），论文数据全部基于 strict 版本（D265 教训：旧版 lenient 结果因 zero-masking bug 不可用）
- Attn k=0.75 seed43 统一用 cqa1=52.0%（w27 不支持 attention scoring，w27 数据不可用）
- Random k=0.9 seed43 统一用 v2=35.0%（D292），不引用旧版 32.4%
- **实验硬截止 May 28 20:00 BJT，CoRL 2026 Paper May 29 提交**——距截止约 6h
- 脚本内 GPU 编号始终从 0 开始（框架自动注入 CUDA_VISIBLE_DEVICES）
- w27 代码未同步，仅支持 none/random/l2norm，不要在 w27 上跑 attention 实验

### 2. 🖥️ 基础设施快照
- **westd-27271**: w27，工作目录 ~/runs/importance_margin_vla_compress/，2 GPU（0,1），仅支持 random/l2norm
- **westd-38929**: w38，工作目录 ~/runs/importance_margin_vla_compress/，4 GPU（0-3）
- **westd-41074**: w41，工作目录 ~/runs/importance_margin_vla_compress/，4 GPU（0-3）
- **cqa1-33015**: cqa1，工作目录 ~/runs/importance_margin_vla_compress/，4 GPU（0-3），支持 attention
- 所有服务器：aml-train 镜像，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 日志路径：`~/runs/importance_margin_vla_compress/{exp_id}.log`
- **活跃 cron（10 个，reconcile 确认全部仍在运行）**:
  - w38: eval_pi05_l2norm_k095_long_seed45_strict_w38 (pid=106960), eval_pi05_random_k095_long_seed45_strict_w38 (pid=155733), eval_pi05_random_k07_long_seed45_strict_w38 (pid=156371), eval_pi05_attn_k085_long_seed46_strict_w38 (pid=218239)
  - w41: eval_pi05_attn_k07_long_seed45_strict_w41 (pid=684035), eval_pi05_random_k085_long_seed46_strict_w41 (pid=697206), eval_pi05_l2norm_k075_long_seed46_strict_w41 (pid=697663), eval_openvla_random_k095_long_seed43_w41 (pid=700644)
  - w27: eval_openvla_l2norm_k095_long_seed43_w27 (刚创建 ~2min)
  - 未确认服务器: eval_openvla_random_k095_goal_seed42_v4 (pid=147681)

### 3. 📊 当前状态
**刚完成**：Session-start 初始化——read_registry、reconcile_crons、读 ROADMAP/report.md/memory.md，向 Director 发送启动汇报。

**发现的关键问题**：
1. **cqa1 无任何 cron 监控**——疑似 4 GPU 全部空闲，距截止仅 ~6h 这是重大资源浪费
2. **Registry 有 8 个 stale RUNNING 实验**（May 26-27 创建，无 cron）：eval_pi05_l2norm_k09_long_seed43_strict_cqa1, eval_pi05_l2norm_k095_long_seed43_strict_w38, eval_openvla_attn_k075_long_seed42(conclusion=failed), eval_pi05_l2norm_k085_long_seed42, eval_openvla_random_k095_object_seed42, eval_pi05_random_k07_long_seed42, eval_openvla_random_k075_goal_seed42, eval_openvla_attn_k075_goal_seed42——这些几乎肯定已完成，registry 未更新
3. eval_openvla_random_k095_goal_seed42_v4 不在 registry 中（count=0），服务器未知

**2 个 Worker 运行中**：
- `worker_analysis_data_consolidation_precheck` (05:45 UTC, turn 2)：构建数据交叉验证表
- `worker_diagnose_all_servers_status_check` (06:00 UTC, turn 22)：正在 SSH 检查各服务器 + 更新 stale registry 条目，即将完成

**5 个 QUEUED 实验**等待部署：eval_pi05_random_k085_goal_seed43, eval_pi05_l2norm_k05_long_seed43, eval_pi05_random_k095_goal_seed43, eval_pi05_l2norm_k07_goal_seed43, eval_pi05_random_k03_long_seed43

### 4. 📋 待办（条件触发式）
- worker_diagnose_all_servers_status_check 完成 → 读回调确认 cqa1 实际 GPU 状态 + stale RUNNING 实验清理结果 → 立即请求 Director 分配 cqa1 GPU 给 QUEUED 实验并部署
- worker_analysis_data_consolidation_precheck 完成 → 读验证表，确认数据一致性问题 → 修正 ROADMAP 数据表
- 任一 seed45/46 cron 回调 → 收割结果、更新 registry/ROADMAP、级联部署下一个实验
- OV 实验（OV Random k=0.95 Long s43, OV L2norm k=0.95 Long s43）完成 → OV Long cliff curve 闭合检查
- 距截止 30min（19:30 BJT）→ 停止新部署，全面收割所有已完成实验数据，最终数据整合
- 全部 cliff curve 闭合 → 通知 Director，Paper Agent 更新 figures

### 5. 🎯 战略上下文
- **核心发现**：Importance Margin Inverted-U（peak k=0.9, 46pp）+ Attn cliff+plateau + Random anti-monotonicity（V-shape），支持 2-Axis Framework（scoring method × connector × task 三维交互）
- **当前阶段**：π0.5 18/18 完成，OV Long 18/18 完成，Crossover 16/16 完成。正在收集 seed45/46 扩展 error bar（从 2-seed 到 4-seed）
- **ROADMAP 数据表已确认（2-seed）**：Importance Margin Profile 6/6 全闭合，Attn cliff+plateau 6/6 全闭合
- **易错点**：
  - 不要混淆 lenient/strict——本项目论文全用 strict
  - cqa1 可能有前序实验的残留进程——部署前 Worker 必须先 nvidia-smi 确认
  - OV 实验需 ~7h（500 episodes × 10 tasks），新部署 OV 实验已来不及在截止前完成，只部署 π0.5（~2-3h）
  - metrics 格式不一致（比例 0.8 vs 百分比 80%），最终收割时统一转百分比
  - eval_openvla_random_k095_goal_seed42_v4 不在 registry 中，需要定位其服务器和状态


---
