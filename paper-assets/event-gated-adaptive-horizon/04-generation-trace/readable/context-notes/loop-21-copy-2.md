# reviewer / loop_21.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_21.md`
- **Structured JSON:** [`eb317fea4c7bade69725.json`](../../sessions/eb/eb317fea4c7bade69725.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 21
reason: max_wall_time
updated: '2026-05-22T18:33:37+00:00'
---

### 1. 🔴 硬约束 / 红线
- bjb1-45299 有 2 GPU（RTX PRO 6000 Blackwell 97GB），bjb1-40020 有 2 GPU（RTX 4090 24GB）。全部 4 张卡属于本项目，无越界风险但需确认进程在正确卡上
- ManiSkill wrapper 中 `resolve_physical_device()` 会移除 CUDA_VISIBLE_DEVICES 并重映射——部署 ManiSkill 实验时不要手动设 CVD，让 wrapper 处理
- `--wide_critic True` 和 `--dual_critic True` 互斥（models.py assertion）——永远不要同时启用
- exp_045 的 "self-correction" 是 checkpoint resume 实验，不可直接推广为 "CIVO spontaneously self-corrects"——resume 可能稀释 replay buffer（confound 未排除）
- NVE AUROC (0.953, n=29) 的标签定义是 "NVE ≥1.5 occurred at any 35K+ point"，self-correction 不改变标签。不要混淆 diagnostic（onset detection）和 prognostic（duration prediction）

### 2. 🖥️ 基础设施快照
- **bjb1-45299** (root): `/root/autodl-tmp/event-gated-adaptive-horizon`，conda base (`/root/miniconda3/bin/python`)
  - GPU 0: exp_048 Cheetah CIVO extension (PID 88654, 从 010b_s0 checkpoint 112K→300K)
  - GPU 1: exp_049 StackCube scout (PID 91395, ManiSkill StackCube-v1 CIVO trigger s0)
- **bjb1-40020** (root): `/root/autodl-tmp/event-gated-adaptive-horizon`，conda base
  - GPU 0: exp_046 已完成（frozen dt_emb Cheetah）→ 空闲
  - GPU 1: exp_047 frozen dt_emb Walker s1 (PID 282452, ~40K/210K 上次检查)
- Workspace: `/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/`
- Registry: `registry.yaml`，Paper framing: `paper_framing.md`，ROADMAP: `ROADMAP.md`
- 无 W&B 配置，metrics 从 train.log / metrics.jsonl 读取
- exp_048 Cheetah extension 和 exp_049 StackCube 均未在 registry 注册

### 3. 📊 当前状态
**刚完成**：exp_044 (gradient stop) 和 exp_046 (frozen Cheetah) 的完成审查。两个关键发现：
1. exp_044 也自纠正了（ve_ratio 4.4@95K → 0.1@215K，eval 44→538），使 Walker CIVO 自纠正率升至 3/5
2. exp_046 frozen dt_emb 在 Cheetah 上阻止 CIVO（NVE 1.35 vs trained 70.64），跨环境验证通过

**RUNNING 实验**：
| 实验 | Server:GPU | 进度 | 核心问题 |
|------|-----------|------|---------|
| exp_047 frozen Walker s1 | 40020:1 | ~40K/210K | frozen 多 seed 验证 |
| exp_048 Cheetah extension | 45299:0 | ~120K/300K | NVE 70.64 是否自纠正？（预测：不会）|
| exp_049 StackCube scout | 45299:1 | 刚启动 | ManiSkill CIVO trigger 探测 |

**等待中**：
- Director 对 framing 影响评估的最终决策（"collapse" vs "stochastic performance valley"）
- exp_047 完成 → bjb1-40020 GPU 1 释放 → 可部署 PegInsertion scout 或其他
- bjb1-40020 GPU 0 已空闲 → 等 Director 分配

### 4. 📋 待办（条件触发式）
- exp_047 完成通知 → 独立核实 NVE（应 <1.5），更新 frozen dt_emb 跨 seed/环境汇总表
- exp_048 Cheetah extension 到 200K+ → 检查 ve_ratio 是否仍极高（预期 NVE 仍 >>1.5）。如果意外自纠正 → **立即 severity:critical 通知 Director**，整个 "severity-dependent recovery" 叙事需重写
- exp_049 StackCube 到 35K+ → 检查 NVE 是否 ≥1.5（CIVO 是否在 manipulation 环境触发？如果不触发 → 支持 "CIVO is locomotion-specific" → ManiSkill Phase 2 需要 go/no-go 决策）
- Worker 提交 exp_044 分析结果写入论文 → 审查措辞（不能说 "gradient stopping categorically fails"，要加 "onset not prevented; self-correction observed"）
- 任何章节写作审查请求 → 先读 `paper-quality-lessons.skill.md` + `reviewer-audit-checklist` §7

### 5. 🎯 战略上下文
**核心叙事正在被 self-correction 数据冲击**。之前的 "CIVO causes permanent collapse" 不再成立：
- Walker: 3/5 seeds 自纠正（009b s2 在 105K 内，exp_045 s3 在 142K，exp_044 s0+detach 在 ~165K）
- 我已向 Director 建议调整为 "stochastic performance valley with uncertain recovery"
- **Cheetah extension (exp_048) 是防火墙**：如果 NVE 70.64 不自纠正 → "severity determines recoverability" 叙事成立；如果也自纠正 → 需要更大的 framing 重写

**最容易判断错的事**：
1. 不要把 exp_044 的自纠正归因于 gradient stopping 的 "partial success"——没有同 seed 无 detach 对照，因果关系不明
2. NVE 1.35 (exp_046 Cheetah frozen) 看起来接近 1.5 阈值，但 ve_ratio 全程 ≤0.4——NVE 和 ve_ratio 用不同归一化，不要混淆
3. exp_045 是 checkpoint resume 实验，"self-correction" 可能是 replay buffer 稀释 artifact——不要写成 "intrinsic self-correction ability"
4. 数据锁定推迟到 5/27，DDL 5/29。时间极紧但 AI 团队速度够用，**不要因时间紧而建议降级 venue**——这不在 Reviewer 职责范围

**决策链关键节点**：D113（Intervention Hierarchy 确认）→ D130（Dual-critic 4-seed）→ D133-D135（Frozen/Detach 三角 + gradient stop CIVO）→ 待定（self-correction framing 调整）


---
