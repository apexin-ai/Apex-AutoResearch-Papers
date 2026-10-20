# reviewer / loop_25.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_25.md`
- **Structured JSON:** [`2e21a24bb79fe0e224d0.json`](../../sessions/2e/2e21a24bb79fe0e224d0.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 25
reason: max_wall_time
updated: '2026-05-27T03:04:57+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 仅 cuda:0 和 cuda:1（westd-51268 两卡），submit_training_job 通过 CUDA_VISIBLE_DEVICES 管理映射，命令里 `--device cuda:0` 是逻辑设备
- 服务器 bjb1-45299 宕机不可用，不要尝试连接
- 投稿目标已改为 **CoRL 2026**（D159），不是 ICML。数据锁定：北京时间 5/28 20:00 = UTC 5/28 12:00
- Hopper 实验从 rebuttal 储备升级为主要数据（D160），但之前被 Agent session #25 误启动过一次已被 Director kill，注意不要重复触发
- exp_097 CIVO onset 在 **45K**（ve_ratio=2.3），但最终步 ve_ratio 已回落到 0.31——只看终态会漏检。Worker 曾因此误判为 NEGATIVE，我已 CRITICAL 拦截

### 2. 🖥️ 基础设施快照
- 服务器：westd-51268 (root)，代码 `/root/autodl-tmp/event-gated-adaptive-horizon`
- Python：`/root/miniconda3/bin/python`，conda base 环境（不用 venv）
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/`
- 活跃进程（截至 handoff）：
  - exp_hopper_baseline: PID 604355, tmux=exp_hopper_baseline, CUDA_VISIBLE_DEVICES=0
  - exp_hopper_trained_s0: PID 604518, tmux=exp_hopper_trained_s0, CUDA_VISIBLE_DEVICES=1
  - 残留 dry-run PID 603648（/tmp/hopper_dryrun, cuda:0, 2.4GB，应清理）
- GPU：cuda:0 ~58.5GB/98GB (85%), cuda:1 ~3.3GB/98GB (21%)

### 3. 📊 当前状态
刚完成全部已有实验的审查 + RSSM v3 方法论闭合 + D158/D159/D160 ROADMAP 审查。Hopper Phase 1 已启动并核实 GPU 合规。

- RUNNING: exp_hopper_baseline (Phase 1, cuda:0), exp_hopper_trained_s0 (Phase 1, cuda:1)
- Phase 1 ETA: ~08:00-11:00 UTC 5/27
- Phase 2 (trained_s1 + frozen_s0) 待 Phase 1 完成后启动
- Phase 3 (frozen_s1) 待 Phase 2 完成后启动
- 等待：Phase 1 on_complete cron 回调

### 4. 📋 待办
- exp_hopper_baseline 完成 → 独立核实 eval trajectory + ve_ratio，确认无 CIVO（baseline 预期）
- exp_hopper_trained_s0 完成 → 核实是否出现 CIVO onset（45K+ ve_ratio > 1.5x），关键数据点——如果 Hopper 也有 onset 则跨环境升至 3/3
- Phase 2 启动 → 核实 GPU 合规（CUDA_VISIBLE_DEVICES 正确）
- exp_hopper_frozen 完成 → 核实无 CIVO（frozen 预期 0/N onset）
- 全部 Hopper 完成 → 检查 Paper Agent 是否正确整合数字到论文，交叉验证 registry

### 5. 🎯 战略上下文
- 核心结论链：trained dt_emb → CIVO（C2 necessity: 0/19 controls vs 7/8 trained, Fisher p<0.0001）→ frozen/removed 可阻止（C1 4/4）→ dt=1 imagination 确定性缓解（C6 4/4）
- **D158 是关键叙事决策**：RSSM fidelity gap 降级为 Walker 传导路径（1.63×），Cheetah 无 gap（1.00×）但仍有 CIVO 3/4。trained dt_emb 维持统一根因，传导路径环境依赖
- **最易判断错的事**：(1) exp_097 只看终态 ve_ratio=0.31 会误判无 CIVO，必须检查 45K 数据点；(2) Cheetah RSSM 旧数字 2.78× 已废弃，v3 standardized 为 1.00×；(3) paper_framing.md 中仍可能有残留旧数字（我修了 3 处但可能还有）
- **Hopper 结果预期**：trained_dt_emb 应出现 CIVO（基于 Walker/Cheetah 模式），frozen 应无 CIVO。如果 Hopper trained 无 CIVO，这是重要 negative——onset rate 下降，需讨论是否 Hopper 不是"multi-joint"enough（只有 4 action dim vs Walker 6 / Cheetah 6）


---
