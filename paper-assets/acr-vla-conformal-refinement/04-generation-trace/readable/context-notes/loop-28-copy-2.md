# agent / loop_28.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_28.md`
- **Structured JSON:** [`5a0a49cd971b7454f5db.json`](../../sessions/5a/5a0a49cd971b7454f5db.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 28
reason: idle_timeout
updated: '2026-05-27T02:33:39+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单必须通过 `get_project_status` 的 `execution.gpu_ids` 确认，历史分配涉及 6 台服务器 29 GPU（bjb1-18228, bjb1-32546, bjb2-24035, bjb2-28827, cqa1-32758, westd-49937）。bjb2-40593 已掉线，不可用
- GPU 部署前必须 `nvidia-smi` 检查显存占用 > 500MB 不启动（C001，3 起碰撞事故教训）
- SmolVLA CRM checkpoint 路径是 `/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt`，**不是** `crm_smolvla_3suite_unified`（后者不存在，反复导致部署失败）
- westd RTX PRO 6000 Blackwell GPU 与 4090 有 ~3pp 系统偏差，Table 2 要求同 GPU 型号配对对比（D158/D164）
- CoRL DDL 是 **2026-05-28 20:00 北京时间**（距现在 ~34h），论文已基本完成，审稿流程 pending 用户审批

### 2. 🖥️ 基础设施快照
- **bjb1-18228**: 3 个 RUNNING τ-sweep（cuda:1 tau025-long-s43, cuda:2 tau035-long-s43, 还有 smolvla-tau015-long-s43 ALLOCATED）
- **bjb1-32546**: 3 个 RUNNING τ-sweep（cuda:3 tau015-long-s42, cuda:4 tau025-long-s42, cuda:5 tau035-long-s42）
- **bjb2-24035**: 1 个 RUNNING（cuda:0 smolvla-tau025-object-s42-r2）
- **cqa1-32758**: 3 个 ANALYZING（smolvla-tau015/025/035-spatial-s43，刚完成待收割）
- **bjb2-28827**: 无活跃进程（之前有 stale RUNNING 需修正）
- **westd-49937**: 无活跃进程
- 代码仓库：各服务器 `/root/autodl-tmp/` 下工作目录
- Python 环境：服务器用 conda（`/root/miniconda3/bin/python`），不是 venv
- 活跃 cron 监控：7 个（6 RUNNING + 1 ALLOCATED 对应的实验）

### 3. 📊 当前状态
- **论文 v54（14页）已完成**，Table 1 + Table 2 锁定，Step 5 写作收敛，D169 Appendix τ-sweep patch 完成
- **submit_paper_to_review 已提交**，等待用户审批 review mode（P0 阻塞项）
- **τ-sweep 数据收割**：scatter_data.csv 89 行。仍有 6 个 RUNNING + 1 ALLOCATED + 3 个 ANALYZING 待处理
- **RUNNING (6)**：全部是 SmolVLA τ-sweep Long/Object suite 补充实验，分布在 bjb1-18228/bjb1-32546/bjb2-24035
- **ANALYZING (3)**：cqa1 上 smolvla-tau015/025/035-spatial-s43 刚跑完，需要收割结果追加到 scatter_data.csv
- **Stale RUNNING 待修正 (ROADMAP 提及 6 个)**：bjb1-18228 4 个 + bjb2-28827 2 个，需核实是否已完成但未更新 registry
- **Agent 稳定性问题**：连续 7 次 reset 后只处理 1-2 条消息就死，已向 Manager 升级
- 总 registry：1302 个实验（681 success, 94 negative, 119 failed, 243 killed）

### 4. 📋 待办（条件触发式）
- cqa1 ANALYZING 的 3 个 spatial-s43 τ-sweep → spawn Worker 收割结果 → 追加 scatter_data.csv → 更新 report.md
- 6 个 RUNNING τ-sweep cron 回调到达 → 收割 → 追加 scatter_data → 如果补全了则更新 Appendix 数据
- bjb1-18228 4 个 + bjb2-28827 2 个 stale RUNNING → spawn Worker SSH 核实进程状态 → 若已结束则 update_registry 修正
- 用户审批 review mode → 处理审稿报告
- smolvla-tau015-long-s43 (ALLOCATED on bjb1-18228) → 需 submit_on_allocated 提交
- 所有 τ-sweep 数据收齐后 → 最终更新 scatter_data.csv + Appendix 图表

### 5. 🎯 战略上下文
- **核心方法**：ACR-VLA = K=2 batched inference + pairwise L2 不确定性 + 自适应 CRM 校正，应用于冻结 flow-matching VLA
- **三个 Core Claims**：MC1（Adaptive ≥ CRM on 3/4 suites, recovery 19-38%）、MC2（cross-suite trigger rate ↔ Δ 单调正相关，within-suite 是 sensitivity analysis）、MC3（cross-VLA 模型能力依赖）
- **关键决策链**：D165-D169 连续修正了 MC1 framing（从 ALL suites 改为 3/4）、Goal CRM harm 数值（14.5→13.2pp）、τ-sweep 定位（从 MC2 within-suite 证据改为 sensitivity analysis）
- **易错点**：
  - within-suite τ-sweep 数据**不是** MC2 的证据，只是 sensitivity/robustness analysis（D169 决策）
  - Goal suite CRM 有 -13.2pp harm，是 MC1 "recovery" narrative 的核心数据点，数值已经 Director 审批锁定
  - pi05 376 missing_keys 是正常行为，不要当 bug 处理
  - DEPLOYED 状态的 6 个实验和 ANALYZING 的 4 个实验需要注意，可能是遗留未清理状态


---
