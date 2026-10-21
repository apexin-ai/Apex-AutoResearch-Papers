# agent / loop_10.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_10.md`
- **Structured JSON:** [`636537b3efd3510eb009.json`](../../sessions/63/636537b3efd3510eb009.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: idle_timeout
updated: '2026-05-15T16:34:41+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 白名单**: 只能用 `bjb2-40593:cuda:0`, `bjb1-18228:cuda:0-3`, `bjb1-32546:cuda:0-5`, `bjb2-28827:cuda:0-5`（共 17 张 4090）。白名单外的 GPU 即使 Director 指令也必须 push back。
- **submit_training_job 命令必须 bash -c 包裹**: tmux 用 `sh` 执行，裸 `python` 不可靠。格式: `bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -u ..."`
- **Kill 前必须 `ps aux | grep` 完整命令行逐参数比对**: 曾发生 norm=0.3 被误判为 norm=0.03 而 kill 的事故（cuda:0 空闲 9h）。
- **exp_id 中 norm 值用 `p` 替代小数点**: norm-0p3 = 0.3, norm-0p03 = 0.03。禁止 norm03 这种歧义命名。
- **项目唯一存活路径**: Object obs_only +6pp+ 维持 + seed=43 复现 → p<0.05。perdof claim 已死。不要在 perdof 上浪费 GPU。
- **bjb2-40593 无 .git repo**: 代码同步需要手动 rsync 或 scp，不能 git pull。

### 2. 🖥️ 基础设施快照
- **服务器 4 台**:
  - `bjb1-18228` (4× 4090): 工作目录 `/root/acr-vla-conformal-refinement`, Python `/root/miniconda3/bin/python`, conda base
  - `bjb1-32546` (6× 4090): 同上路径和环境, account=root
  - `bjb2-28827` (6× 4090): 同上路径和环境, account=root
  - `bjb2-40593` (1× 4090 D): 同上路径, **无 .git**, CRM cache 在 `/root/autodl-tmp/crm_cache/spatial/`
- **全部 17 张 GPU 满载**
- **活跃 cron 监控 10 个实验** (reconcile 刚确认):
  - `eval-mag-perdof-norm005` (bjb2-28827:cuda:1, PID 13456)
  - `eval-mag-perdof-norm02` (bjb2-28827:cuda:2, PID 13728)
  - `eval-mag-perdof-norm03` (bjb2-28827:cuda:3, PID 14260)
  - `eval-vla-mean-object` (bjb1-32546:cuda:5, PID 18808)
  - `eval-acr-object-obs-only-norm02` (bjb1-32546:cuda:4, PID 44270)
  - `eval-mag-obsonly-norm003-b2` (bjb2-40593:cuda:0, PID 227434)
  - `eval-mag-obsonly-norm03-r2` (bjb1-18228:cuda:0, PID 325264)
  - `eval-obs-only-object-seed43` (bjb1-18228:cuda:2, PID 356490)
  - `eval-argmin-object-seed43` (bjb1-18228:cuda:3, PID 356696)
  - `eval-perdof-object-seed43` (bjb1-18228:cuda:1, PID 365925)
- **无 cron 但 RUNNING**: `eval-mag-obsonly-norm03-object`, `eval-mag-obsonly-norm005-object`, `eval-obs-only-object-norm02-seed43`, `eval-scalar-object-seed43`, `eval-vla-mean-object-seed43` (bjb1-32546 和 bjb2-28827 上) — **需要确认这些是否有 cron 监控，否则是 orphan**
- **Worker 池: 0 running** — 当前无活跃 Worker

### 3. 📊 当前状态
- **刚完成**: `eval-mag-perdof-norm003` 刚被 reconcile 标记为 ANALYZING (EXIT_CODE=0)，7/10 tasks done, running avg 40.0%。**需要立即 spawn worker 分析结果**。
- **Registry**: 106 实验总计 — 15 RUNNING, 1 ANALYZING, 17 PREPARING, 73 DONE (28 success, 2 negative, 15 failed, 28 killed)
- **Phase 2d**: Object benchmark + seed=43 doubling 进行中，决定项目存亡
- **Object 关键数据 (seed=42 FINAL)**: obs_only 0.1 = **19.0%** (PROJECT HIGH), perdof = 11.0%, VLA-only = 12%, scalar = 9.0% (negative), argmin ≈ 6.7%
- **Spatial LOCKED**: 全部 CRM 变体 ≈ argmin baseline (34%)，spatial 上 CRM 无增益
- **Seed=43 六方 (obs_only/argmin/perdof/scalar/VLA-mean/obs-only-norm02) 全部已部署**, 等待完成
- **Magnitude sweep**: perdof 4 个 norm (0.03/0.05/0.2/0.3) 在 bjb2-28827 上跑; obs_only sweep 也在跑
- **等待中**: 无 pending Worker 回调; 10+ cron 监控回调会陆续触发; 无 pending Director 决策

### 4. 📋 待办（条件触发式）
- `eval-mag-perdof-norm003` ANALYZING → spawn worker 分析 10-task final result, update registry, 汇报 Director
- seed=43 任一完成 (obs_only/argmin/perdof) → spawn worker 分析, 与 seed=42 对比, 积累到 3 方都完成后做 Fisher exact test
- **seed=43 全部 6 方完成** → spawn worker 做完整统计分析 (Fisher exact test + bootstrap CI), 这是项目 go/no-go 决策点
- magnitude sweep 全部 10-task 完成 → 汇总 norm sensitivity curve, 确认 obs_only 是否在所有 norm 下 >= perdof
- Object argmin / VLA-mean 完成剩余 tasks → 锁定完整 comparison table
- **5 个无 cron 的 RUNNING 实验** → 立即检查是否有 cron 监控，若无则 spawn worker 补建或手动注册 cron
- 所有 object + seed=43 + magnitude sweep 完成 → 更新 paper_framing.md, 向 Director 汇报是否满足 p<0.05, 启动 Paper Agent
- GPU 释放后 → 从 PREPARING 队列中取 eval-acr-object-v4-default (ablation: 无 magnitude control) 优先提交

### 5. 🎯 战略上下文
- **核心结论链**: D025 perdof=argmin on matched tasks → D027 perdof claim dead → D030 spatial ALL CRM dead → D031 seed=43 doubling → D032 magnitude sweep narrative 修正 (obs_only spatial 全 norm 收敛 35%, 与 argmin 持平)
- **唯一活路**: Object obs_only 19.0% vs argmin 6.7% (+12.3pp) 的优势能否在 seed=43 复现 → Fisher exact test p<0.05
- **最容易判断错的事**: Spatial magnitude sweep 中期值 (4-7 tasks) 看起来 obs_only >> perdof, 但 10-task final 趋势是收敛到 ~35% baseline (D032)。**不要被中期膨胀值误导**。只有 10/10 final 数字可以写进 paper。
- **CoRL DDL**: abstract ~May 26 (11天), full paper ~Jun 2 (18天)。seed=43 结果是 go/no-go gate, 必须在 1-2 天内出。
- **论文 story 已转**: 从 "per-DOF conformal" 转为 "obs_only learned correction"。paper_framing.md 需要根据最终数据更新。
- **容易踩的坑**: (1) bjb2-40593 无 git, 别用 git pull; (2) submit_training_job 裸 python 会 EXIT_CODE=127; (3) 有 5 个 RUNNING 实验缺少 cron 监控信息, 可能是 orphan — 优先排查


---
