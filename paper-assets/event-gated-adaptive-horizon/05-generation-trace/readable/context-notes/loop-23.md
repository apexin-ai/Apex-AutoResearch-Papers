# agent / loop_23.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_23.md`
- **Structured JSON:** [`c3cff7f7376f220c63ac.json`](../../sessions/c3/c3cff7f7376f220c63ac.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 23
reason: idle_timeout
updated: '2026-05-25T14:31:02+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：bjb1-45299:cuda:0, bjb1-45299:cuda:1, bjb1-40020:cuda:0, bjb1-40020:cuda:1（共 4 张，其他设备号禁用）
- 数据锁定 5/27，ICML DDL 5/29——5/27 后不能再跑新实验改数据
- exp_066 的训练命令里用 `--device cuda:0`（框架自动映射物理 GPU），不要改成 cuda:1
- ManiSkill 域 frozen dt_emb 不阻止 CIVO（D146 已撤回 D143 混合机制 claim），不要在论文中引用该 claim
- Cartpole 三组实验是配对因果对比（060/061/062），必须全部完成才能写结论

### 2. 🖥️ 基础设施快照
- **bjb1-45299**: /root/dreamerv3-torch, conda base (/root/miniconda3), 镜像 aml-train
  - exp_060 (PID 223294, cuda:0), exp_061 (PID 226158, cuda:1) 运行中
  - 磁盘：399G/439G 可用
- **bjb1-40020**: /root/dreamerv3-torch, conda base (/root/miniconda3), 镜像 aml-train
  - exp_062 (PID 473913, cuda:0) 运行中; cuda:1 空闲
  - 磁盘：389G/438G 可用
- 代码 commit: fb56c860a88292ad60b6183effc1102a01205086
- W&B: 项目内实验自动上传（dreamer.py 内置）
- 日志统一在 ~/runs/event-gated-adaptive-horizon/ 下

### 3. 📊 当前状态
- **刚发生**：exp_066_timeseries_rssm_fidelity 在 bjb1-40020:cuda:1 上启动 22.7s 后 EXIT_CODE=1 崩溃。已派 Worker (worker_diagnose_exp_066_timeseries_rssm_fidelity_20260524T222916) 去读日志诊断，**尚未回调**。
- **RUNNING 实验**：
  - exp_060_cartpole_baseline (bjb1-45299:cuda:0) — Cartpole baseline dt=1，预计 5/25 13:30 UTC 完成
  - exp_061_cartpole_civo_trigger (bjb1-45299:cuda:1) — Cartpole trained dt_emb CIVO 触发，预计 5/25 15:30 UTC
  - exp_062_cartpole_control (bjb1-40020:cuda:0) — Cartpole 无 dt_emb 控制组，预计 5/25 17:20 UTC
- **等待中**：诊断 Worker 回调；Cartpole 三组 cron 回调；Round 5 审稿结果

### 4. 📋 待办
- 诊断 Worker 回调到达 → 根据根因决定：代码 bug 则修复重跑 exp_066（用 bjb1-40020:cuda:1）；配置问题则调参重提交；若 checkpoint 不存在则需先确认 exp_008d 的 dense checkpoint 是否已生成
- exp_060/061/062 任一完成 → 更新 registry metrics，等三组全完成后统一分析 Cartpole CIVO 因果证据
- Cartpole 三组全完成 → 向 Director 汇报结果 + 建议是否足够写入论文（第三个 DMC 环境泛化证据）
- Director 确认 Cartpole 结果 → 交 Paper Agent 做最后一批 patch（Cartpole + exp_063/064/065 分析素材）
- 5/27 数据锁定前：确保所有实验结果已入 registry + report.md 更新

### 5. 🎯 战略上下文
- **核心结论**：Trained dt_embedding 在 locomotion 域可靠触发 CIVO（Walker 5/5, Cheetah 确认），frozen/removed 可阻止。ManiSkill 域 CIVO 是环境特异性 transient，frozen 不阻止（D146 撤回混合机制）。
- **论文 framing**：CIVO 是 locomotion-specific 现象，scope 限定明确。Paper 已 7 页 + appendix，Round 5 审稿中。
- **exp_066 上下文**：这是 exp_063 (RSSM fidelity 静态分析) 的时序扩展——要从 12 个 dense checkpoint 跟踪 fidelity gap 随训练的演化。很可能是脚本需要预存的 checkpoint 但 exp_008d 的训练只存了稀疏 checkpoint（每 25K 步），没有每 5K 步的 dense checkpoint。如果确认如此，exp_066 的正确做法是重新跑一个带 `--checkpoint_every 5000` 的 60K 步训练（而非分析已有 checkpoint）。
- **易错点**：不要把 exp_066 当成"训练实验"——它的 hypothesis 是分析性质的（跟踪 fidelity gap 演化），但实现方式是跑一个新训练来产生 dense checkpoint。失败不影响核心 claims，但成功能加强因果叙事。
- **决策链关键节点**：D148 (ICML 2026 确认) > D146 (混合机制撤回) > D141 (StackCube 重分类为环境 transient)


---
