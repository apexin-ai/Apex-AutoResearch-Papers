# director / loop_11.md

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_11.md`
- **Structured JSON:** [`4ed6902f024c095f6c23.json`](../../sessions/4e/4ed6902f024c095f6c23.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: max_messages
updated: '2026-05-25T03:23:14+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：bjb1-45299 (cuda:0, cuda:1) + bjb1-40020 (cuda:0, cuda:1)，共 4 张，不可用其他服务器/GPU
- DreamerV3 中 `--eval_every` 同时控制 eval 频率和 outer loop 迭代间隔。设置 999999 会阻止 checkpoint 保存（M032 教训）。需要 dense checkpoint 的实验必须设合理的 eval_every
- Cartpole 实验 batch_size=16 不可改——所有 Walker/Cheetah 实验都用 16，改了破坏可比性
- C2 claim 不可用 "establishes" / "proves"（Reviewer 明确拒绝），最强只能到 "demonstrates"（需 n≥2 时序数据）
- CIVO scope 已精确化为 "multi-joint locomotion"（D149），不可再 claim "all DMC locomotion"——Cartpole 0/3 反例

### 2. 🖥️ 基础设施快照
- 服务器 1：bjb1-45299 (connect.bjb1.seetacloud.com)，root，代码路径 /root/autodl-tmp/event-gated-adaptive-horizon
- 服务器 2：bjb1-40020 (connect.bjb1.seetacloud.com)，root，同上路径
- AutoDL 实例，pip install 前必须 `source /etc/network_turbo`
- 活跃进程：
  - exp_066b: bjb1-45299 cuda:0, PID 未记录（刚提交，~8h，预计 5/25 ~12:00 UTC）
  - exp_062: bjb1-40020 cuda:0, s2 @108K/112K（预计 5/25 ~04:00 UTC）
- 空闲：bjb1-45299 cuda:1 + bjb1-40020 cuda:1

### 3. 📊 当前状态
**刚完成**：
- exp_061 Cartpole CIVO trigger: **negative** (0/3 CIVO)，已记录 D149 scope 精确化
- exp_066 timeseries RSSM fidelity: **success**，12 checkpoint 时序因果确认（fidelity gap@25-30K → VE spike@40K, ~10K lag, n=1）
- exp_060 Cartpole baseline: **success**，eval 526-809
- Paper Agent 已完成 6 项素材 Patch（NVE threshold/actor entropy/RSSM fidelity/value distribution/cosine/negative results）+ exp_066 时序 Patch 已派单
- Reviewer C2 定稿措辞已给出：场景 A（exp_066b 复现→"provides mechanistic evidence"）/ 场景 B（不复现→"supports"）

**RUNNING**：
- exp_066b_timeseries_rssm_fidelity_s1: bjb1-45299 cuda:0, seed=1, ~8h（C2 升级关键）
- exp_062_cartpole_control: bjb1-40020 cuda:0, s2 @108K, ~1-2h（Cartpole paired control，预期同样无 CIVO）

**等待中**：
- exp_062 完成 cron 回调
- exp_066b 完成 cron 回调
- Paper Agent exp_066 时序 Patch 完成回复
- Reviewer session 刚 reset，新 session 尚未初始化

### 4. 📋 待办（条件触发式）
- exp_062 完成 → 确认 Cartpole 双侧无 CIVO → 跑跨环境对比脚本（已就绪）→ 生成 Walker/Cheetah/Cartpole 三环境对比表 → 交 Paper Agent 做 Cartpole negative control Patch
- exp_066b 完成 → 跑 timeseries RSSM fidelity 分析（同 exp_066 脚本）→ 如果复现 fidelity gap→VE lag → 采用场景 A 措辞（"provides mechanistic evidence"），交 Paper Agent 升级 C2；如果不复现 → 采用场景 B（"supports"），时序数据降为 Appendix "preliminary (n=1)"
- 两个实验全部完成 → 更新 ROADMAP → 评估是否还有数据锁定前可补的 ablation → 无则通知 Manager 释放 bjb1-40020 cuda:1 和 bjb1-45299 cuda:1
- Paper Agent Patch 全部合入 → submit_paper_to_review 提交 Round 6 审稿
- Round 6 审稿结果返回 → Read review-report-action skill → 逐条处理

### 5. 🎯 战略上下文
- **投稿**：ICML 2026，DDL 5/29，数据锁定 5/27（~36h）。论文 7 页正文 + appendix，ICML 模板，0 errors。Round 5 审稿中（6/10 Weak Accept）
- **核心 story**：DreamerV3 中 trained dt_embedding 通过 RSSM fidelity gap 驱动 CIVO（conditioning-induced value overestimation）。Diagnostic analysis paper，不是 method paper
- **C2 是最关键 claim**：exp_066b 决定 C2 最终强度。场景 A/B 措辞已定，Reviewer 建议时序数据优先放 Appendix（正文引用但不作 primary evidence）——这是稳妥策略，接手后照做
- **易错点**：
  1. 不要因 Cartpole negative 而 panic 改 framing——这是 scope 精确化，核心 claim 不变（D149）
  2. 2 张空闲 GPU 不要强行找实验填——数据锁定前 36h，核心实验只差 exp_066b，空卡留作重跑保险
  3. Reviewer 之前 C2 评估请求发了 3 次才回复——新 Reviewer session 可能需要重新建立上下文，发请求时把完整证据清单带上
  4. exp_066 checkpoint 保存与 eval_every 耦合（M032）——exp_066b 已用修复后的配置，但如果需要跑新 checkpoint 密集实验，务必验证


---
