# director / loop_4.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_4.md`
- **Structured JSON:** [`7d7a8c039cbff1b6bea4.json`](../../sessions/7d/7d7a8c039cbff1b6bea4.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: max_messages
updated: '2026-05-15T13:40:10+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：bjb1-18228(4×4090), bjb1-32546(6×4090), bjb2-28827(6×4090), bjb2-40593(1×4090D) — 共 17 卡，不得在其他服务器/GPU 上启动实验
- Object obs_only +6.6pp 是项目唯一存活信号，任何操作不得干扰 bjb1-32546 上的 object 6-way eval 和 bjb1-18228 上的 seed=43 三方对比
- paper_framing.md 已更新为 Scenario C（obs_only > perdof），不要回退到 Scenario A 语言（per-DOF fundamentally richer）
- writing_plan.yaml 中 object 数字必须用占位符，数据未锁定前不写具体数字

### 2. 🖥️ 基础设施快照
- **bjb1-18228** (connect.bjb1.seetacloud.com): cuda:0 mag-obsonly-norm03-r2, cuda:1 eval-perdof-object-seed43(PID 365925), cuda:2 eval-obs-only-object-seed43(PID 356495), cuda:3 eval-argmin-object-seed43(PID 356701)
- **bjb1-32546** (connect.bjb1.seetacloud.com): 6 卡 object 6-way eval seed=42 (reconvla/perdof/obs_only-0.1/scalar/obs_only-0.2/vla_mean), 6/10 tasks 时快照
- **bjb2-28827** (connect.bjb2.seetacloud.com): 6 卡 magnitude sweep (perdof-003/005/02/03 + obsonly-005/02), 6-7/10 tasks
- **bjb2-40593** (connect.bjb2.seetacloud.com): cuda:0 obsonly-norm003-b2, 3/10 tasks
- 工作目录: /root/acr-vla-conformal-refinement
- Python: /root/miniconda3/bin/python (conda base)
- 所有 eval 用 nohup 独立进程 + cron 监控，不依赖 Agent session

### 3. 📊 当前状态
刚完成 paper_framing.md 从 Scenario A 到 Scenario C 的全面重写（D032 magnitude narrative 修正）。Spatial benchmark 全锁（argmin 34%, perdof 35%, obs_only 35%, scalar 32%）。

**RUNNING 实验（17 个）**:
- Object 6-way seed=42: ~6/10 tasks, ETA 几小时
- D031 seed=43 三方 (obs_only/argmin/perdof): 刚启动，ETA ~15h
- Magnitude sweep 6-way: 6-7/10 tasks, ETA ~3-6h
- obsonly-norm003-b2: 3/10 tasks
- mag-obsonly-norm03-r2: 进行中

**等待中**: Agent 在准备 Fisher exact + bootstrap CI 统计分析代码。Agent 队列中有 writing_plan.yaml 占位符修复指令待处理。

### 4. 📋 待办
- Object 10-task 完成（cron 回调）→ 汇总 10-task 全表，obs_only vs argmin final gap；若 <3pp → 项目 dead，通知用户；若 3-5pp → 灰区，加速 seed=43；若 ≥5pp → 存活，准备论文
- Seed=43 三方完成 → Fisher exact test (combined 200 trials)；p<0.05 → 开启 Paper Agent CoRL 初稿；p≥0.05 → 项目 dead
- Magnitude sweep 10-task 完成 → norm sensitivity curve 绘图，确认 D032 narrative（obs_only 高 norm 鲁棒 vs perdof 崩塌）
- VLA-mean object 10-task 出来后 → 比较 vs obs_only gap；若 VLA-mean 接近 obs_only → CRM 增量 claim 被压缩，需要调整 framing
- 所有数据锁定后 → Paper Agent 启动 CoRL 初稿（DDL abstract May 26, paper Jun 2）

### 5. 🎯 战略上下文
**决策链核心**: D003(MVP pass) → D017-D019(CRM 拖累发现+修复) → D027-D030(per-DOF 全面判死，spatial 全锁) → D031(seed=43 统计显著性方案) → D032(magnitude narrative 从"全局优势"修正为"鲁棒性 story")

**最容易判断错的事**:
1. 不要被 obs_only 6/10 task 的 +6.6pp 冲昏——T7-T10 如果都是双方 0% 的难 task，gap 会被稀释到 <5pp 灰区
2. VLA-mean 在 object 上 10%（6-task），如果继续逼近 obs_only 13.3%，则"CRM correction 比 mean aggregation 好"的 claim 站不住
3. Magnitude sweep norm=0.05 gap 仅 +2.9pp（7t），不要 claim "obs_only 在所有 norm 下优于 perdof"——正确表述是"obs_only 在高 norm (≥0.2) 下显著优于 perdof"
4. Agent 频繁卡死（本 session 内 3 次 idle >7min），reset 后发综合指令比 urgent message 更有效


---
