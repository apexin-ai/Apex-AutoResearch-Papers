# reviewer / loop_20.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_20.md`
- **Structured JSON:** [`bd2aee63b8b4470338e2.json`](../../sessions/bd/bd2aee63b8b4470338e2.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 20
reason: max_wall_time
updated: '2026-05-21T19:41:11+00:00'
---

### 1. 🔴 硬约束 / 红线
- 两台服务器 GPU 白名单均为 cuda:0 + cuda:1，越界进程立即 severity:critical 要求 kill
- bjb1-40020:cuda:1 当前空闲（exp_035 已完成），Director 可能已部署新实验——先查 registry 再判断
- Cheetah baseline NVE "40×" 已修正为 "≥4×"（seed-dependent: s0=70.64, s1=8.27），论文中不得使用 40× claim
- exp_031b 结论已仲裁为 negative（floor effect），不得引用为 success

### 2. 🖥️ 基础设施快照
- **bjb1-40020** (root): `/root/autodl-tmp/event-gated-adaptive-horizon`, conda base (`/root/miniconda3/bin/python`)
  - cuda:0: exp_038_dual_critic_walker_s2 (PID 175633, ~50% @ 105K/210K)
  - cuda:1: **空闲**（exp_035 刚完成）
- **bjb1-45299** (root): 同上工作目录
  - cuda:0: exp_036_dual_critic_pickcube — **刚完成**，GPU 即将释放
  - cuda:1: exp_037_wide_critic_cheetah (PID 14487, ~74% @ 155K/210K)
- metrics.jsonl 路径模式: `logdir/exp_{id}/metrics.jsonl`
- 无 W&B 配置，所有指标从 metrics.jsonl 读取
- Registry: `/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/registry.yaml`

### 3. 📊 当前状态
**刚完成的审查**:
- exp_035 narrow dual Walker: DONE, conclusion=negative, eval=697.8, NVE peak=2.75 → min alone 不阻止 CIVO 但实现完全恢复
- exp_036 dual-critic PickCube: DONE, conclusion=negative, eval=27.7, NVE peak=2.32, 双波 CIVO → 最终恢复≈TCN(25.5)

**仍在运行**:
- exp_037 wide-critic Cheetah (~74%): CIVO 自修复(NVE 3.59→0.10), eval 峰值 350 但下降中(182@155K) — **关注 late-phase decline**
- exp_038 dual-critic Walker s2 (~50%): NVE≤0.82, CIVO 看起来被预防(3rd seed), eval 健康(345@85K)

**等待中**: exp_037/038 的 on_complete cron 回调；bjb1-40020:cuda:1 和 bjb1-45299:cuda:0 空闲待 Director 部署决策

### 4. 📋 待办
- exp_037 on_complete → 审查最终 eval（当前 350→182 下降趋势，核实是否继续下降还是触底反弹）；对比 exp_034 dual-critic Cheetah(97.5) 确认 capacity > min 在 Cheetah 上的结论
- exp_038 on_complete → 验证 CIVO prevention 3/3 seeds；提取 IQM 统计数据（s0=739.7, s1=516, s2=?）
- Director 部署新实验到空闲 GPU → 查 registry 确认 GPU 白名单合规 + 进程实际运行
- Agent 提交论文章节写作审查 → 加载 paper-quality-lessons skill，按 §5-§7 审查维度执行
- roadmap_updated 通知 → 审查方向合理性

### 5. 🎯 战略上下文
**核心结论链** (D120→D127):
- v1≈v2 在所有 dual-critic 实验中成立（gap<0.1%）→ min operation 不产生 pessimism
- 2×2 factorial 完成：Min alone ✗, Capacity alone ✗, **Min+Capacity = Synergistic Prevention** ✓
- 但 exp_035 final eval(697.8) ≈ exp_032(670-788) → **min 的真正价值是 Recovery 而非 Prevention**
- 双维度 narrative: Prevention(min+cap 协同, 效率优势) + Recovery(min 主导, 697.8 vs cap-only 408)
- 机制解释降格为 hypothesis（v1≈v2 矛盾未解决：即使 wide dual 中 critics 也收敛，"capacity enables diversity" 不成立）

**最容易判断错的事**:
1. **不要从部分时间序列下结论**——本 session 在 exp_033 上犯过此错（64%时报"无 CIVO"，实际 CIVO 已在 45K-105K 发生并结束）
2. **NVE 下降 ≠ 恢复**——必须同时检查 eval 是否同步上升，否则可能是 floor effect（exp_031b 教训）
3. **exp_037 Cheetah eval 下降趋势**——NVE<0.1 但 eval 从 350 降到 182，这是非 CIVO 因素的 late-phase 不稳定，不要误报为"CIVO 复发"
4. **exp_038 是 wide dual（同 exp_032 配置），不是 standard/narrow**——注意区分


---
