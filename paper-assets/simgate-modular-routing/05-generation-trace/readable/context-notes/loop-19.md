# agent / loop_19.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_19.md`
- **Structured JSON:** [`030593200113ef6274d9.json`](../../sessions/03/030593200113ef6274d9.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 19
reason: max_wall_time
updated: '2026-05-17T21:27:02+00:00'
---

### 1. 🔴 硬约束 / 红线
- westb-14838 有 4 张 RTX PRO 6000 (98GB)，westb-13313 有 2 张 RTX 5090 (32GB)
- 72B AWQ 在 13313 必须 TP=2（32GB×2），在 14838 可 TP=1（98GB 单卡够）
- SSH Worker 必须显式传 `server="westb-14838"` 或 `server="westb-13313"`，不传会默认连 13313
- 14838 的 72B 用 offline vLLM（in-process），不需要 API server；13313 同理
- Blackwell SM 12.0 需要 `VLLM_USE_FLASHINFER_SAMPLER=0` 环境变量
- report.md 是 auto-generated，每次 update_registry 会覆盖手动修改

### 2. 🖥️ 基础设施快照
- **westb-13313**: host=connect.westb.seetacloud.com:13313, user=root, 2× RTX 5090 32GB
  - 工作目录: /root/autodl-tmp/simgate-modular-routing/
  - 模型: /root/autodl-tmp/models/Qwen2.5-72B-Instruct-AWQ (TP=2)
  - 结果: /root/autodl-tmp/simgate-modular-routing/results/backbone_72b/
  - 活跃: PID 617494 (tmux backbone-scaling-70b, cuda:0+1, 72B sequential collection)
  - Cron: backbone-scaling-70b (interval 300s, monitors tmux session name)

- **westb-14838**: host=connect.westb.seetacloud.com:14838, user=root, 4× RTX PRO 6000 98GB
  - 工作目录: /root/autodl-tmp/simgate-modular-routing/
  - 模型: /root/autodl-tmp/models/Qwen2.5-72B-Instruct-AWQ (TP=1 per card)
  - 结果: /root/autodl-tmp/simgate-modular-routing/results/backbone_72b/
  - 活跃: PID 321045 (cuda:0), PID 69734 (cuda:1). PID 321159 (cuda:2) DEAD.
  - cuda:2+3 空闲（7B vLLM 已 kill）
  - Cron: backbone-scaling-70b-parallel (interval 600s, monitors PID 321045)

- **论文目录**: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/
- **vLLM version**: 0.21.0

### 3. 📊 当前状态
**刚做完**: Director 批准补跑 measure-melting-point 5 episodes (cuda:2)。Worker `worker_code_72b-supplement-measure-melting_20260517T212605` 正在执行。

**Registry RUNNING/ANALYZING**:
- backbone-scaling-70b (ANALYZING, 实际仍 RUNNING on 13313, 状态无法回退)
- backbone-scaling-70b-parallel (RUNNING on 14838 cuda:0+1, cuda:2 dead)

**已完成本 session**:
- retry-control-baseline: DONE (success) — death_rate=40.9% ≈ baseline, 证实 reflexion 收益来自自我纠错
- reflexion-internal-baseline: DONE (negative) — death_rate=31.4%, 远不足以消除 death dominance
- ARR submission checklist: 创建完毕，3 项必须修复（checklist include, B2 license, C1 GPU model）
- responsibleNLPchecklist.tex: 已创建，内容完整
- signal_reversal.pdf (Figure 3): 已更新为 3-environment 版本（+ALFWorld）
- 5 citations verified and added to references.bib
- cuda:3 7B vLLM 已 kill

**等待中**:
- Worker 回调: 72b-supplement-measure-melting（~20min 完成 5 eps）
- 回调后: 需要计算 11-task aggregate death rate 并汇报 Director（论文 Table 4 用）

### 4. 📋 待办（条件触发式）
- 72b-supplement Worker 回调 → spawn analysis worker 统计全部 220 eps death rate (per-task + aggregate)，对比 7B baseline，汇报 Director
- backbone-scaling-70b cron 回调（13313 全部完成） → 标记 DONE，合并两台数据
- backbone-scaling-70b-parallel cron 回调（321045 退出） → 检查 69734 是否也完成，标记 DONE
- Director 确认 72B 结果 → spawn paper worker 写入论文（正文 if death_rate 显著降低, appendix if moderate）
- Paper Agent 完成 ARR 3 项修复后 → 确认编译通过，跑 acl-pubcheck

### 5. 🎯 战略上下文
- **核心结论**: DAF=90.4%, 78.9% routing labels driven by death asymmetry (penalty-independent)。论文是 diagnostic framework，不是 routing method。
- **72B 是最后的关键实验**: 如果 72B death_rate 显著低于 7B (42.9%)，说明 backbone scaling 能降低 death → 写入正文作为 testable prediction 验证。如果 72B det death_rate 也同比降低 → DAF 仍 dominant → 更强 claim。
- **DDL**: EMNLP 2026 ARR，2026-05-25（剩 7 天）
- **易错点**: 
  - 72B data 分散在两台服务器，合并时需 deduplicate（同一 task 两边都有数据，取 20 即可）
  - 13313 cron 监控 tmux session name 不是 PID（检测方式不同）
  - registry backbone-scaling-70b 卡在 ANALYZING 无法回退 RUNNING，完成时直接 → DONE


---
