# director / loop_7.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_7.md`
- **Structured JSON:** [`09bf90735cc462d2c1f9.json`](../../sessions/09/09bf90735cc462d2c1f9.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_messages
updated: '2026-05-16T11:09:01+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单严格按 `execution.gpu_ids` 分配，当前 4 台服务器共 17 卡，不得使用白名单外 GPU
- bjb2-28827 上实验用 nohup 启动（非 tmux），cron auto-resolve 会误判正常退出为 failed——每个实验完成后必须先读 JSON 输出确认再更新 registry，不依赖 cron
- narrative_b_draft.md 是唯一有效的 fallback narrative 文档，fallback_narrative_draft.md 已废弃（含虚构数据）
- 任何写入文档/narrative 的数据必须来自 registry 确认的实验结果，不确定的标 TBD

### 2. 🖥️ 基础设施快照
- **bjb1-18228** (4× 4090): connect.bjb1.seetacloud.com, root, `/root/acr-vla-conformal-refinement`
- **bjb1-32546** (6× 4090): connect.bjb1.seetacloud.com, root, 同上
- **bjb2-28827** (6× 4090): connect.bjb2.seetacloud.com, root, 同上
- **bjb2-40593** (1× 4090 D): connect.bjb2.seetacloud.com, root, 同上
- 无 W&B / 无 Git remote / 无 conda（直接 pip venv）
- JSON 输出路径: `/root/acr-vla-conformal-refinement/logs/eval_object_*.json`
- P0 进程: eval-obs-only-object-norm02-seed44-r2, PID=428406, bjb1-18228:cuda:2, ~10h+ running

### 3. 📊 当前状态
**刚完成**: Magnitude curves 双曲线全部完整（obs_only 6/6 + perdof 6/6），D039 logged。Narrative B 两轮修正完毕。Registry 滞后全部清理。Seed45 五组实验已部署运行。

**RUNNING (~17 实验)**:
- P0: eval-obs-only-object-norm02-seed44-r2 (bjb1-18228:cuda:2) — 决定项目最终 claim
- eval-argmin-object-seed44-r2 (bjb1-18228:cuda:3) — P0 配对 baseline
- seed44 其余: perdof/scalar/vla-mean/obs-only-norm01/obs-only-default/obs-only-norm03
- seed45: argmin + obs-only-norm02 + VLA-only + perdof + obs-only-norm01/norm03
- bjb2-40593: perdof-default-seed44

**等待**: seed44 obs_only ε=0.2 + argmin 完成回调 → 立即 3-seed Fisher test

### 4. 📋 待办
- seed44 obs_only ε=0.2 + argmin DONE → 立即 3-seed Fisher exact test + bootstrap CI → 据 p 值决策：p<0.05 走 dual claim / p=0.05-0.10 等 seed45 或弱化 / p>0.10 走 Narrative B
- seed45 完成 → 4-seed pooled 统计（如果 3-seed borderline）
- bjb2-28827 任何实验完成 → 先读 JSON 确认再更新 registry（cron bug workaround）
- magnitude sweep 完整后 → 派 Paper Agent 生成 magnitude curve figure（论文核心 figure，两条曲线 + error bar）
- 3-seed 统计锁定后 → Paper Agent patch 数字到论文各章节 + 写 Abstract 最终版

### 5. 🎯 战略上下文
- **决策链**: D033(object obs_only +7pp FINAL) → D035(kill criterion 触发) → D037(零纠正非 bug) → D038(ε=0.2 唯一配置, pooled +4.5pp p≈0.12) → D039(perdof default=0% catastrophic)
- **核心判断**: obs_only ε=0.2 是唯一存活路径。ε=0.1 已死(p=0.44)，perdof/scalar 全死。Spatial 无贡献。
- **最易判断错的事**: (1) seed44 如果 p>0.05 不代表项目失败——magnitude curve 双曲线对比（obs_only safe vs perdof collapse）是独立于 p 值的 publishable contribution；(2) 不要把 perdof 的 0% 错误归到 obs_only（fallback 文档已犯过此错）；(3) argmin seed43=17% 高于 seed42=12%，baseline 方差大，pooled 比较比单 seed 可靠
- **CoRL DDL**: abstract ~May 26, full paper ~Jun 2，时间充裕但 narrative 决策不能拖过 seed44 结果


---
