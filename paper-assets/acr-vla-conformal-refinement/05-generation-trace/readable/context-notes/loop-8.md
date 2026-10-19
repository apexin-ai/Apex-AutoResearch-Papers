# director / loop_8.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_8.md`
- **Structured JSON:** [`ec9391c392a55810bcb8.json`](../../sessions/ec/ec9391c392a55810bcb8.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_messages
updated: '2026-05-16T15:19:07+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单严格按 `execution.gpu_ids` 分配，当前 4 台服务器共 17 卡，不得使用白名单外 GPU
- bjb2-28827 上实验用 nohup 启动（非 tmux），cron auto-resolve 会误判正常退出为 failed——每个实验完成后必须先读 JSON 输出确认再更新 registry，不依赖 cron
- eval-obs-only-object-norm02-seed44-r2 的 JSON 数据有效（16%, 16/100, 10/10 tasks），EXIT_CODE=129 是假阳性。Reviewer 已独立核实。**不要再重部署此实验**
- narrative_b_draft.md 是唯一有效的 fallback narrative 文档，fallback_narrative_draft.md 已废弃（含虚构数据）
- 部署命令必须显式设 `CUDA_VISIBLE_DEVICES=N`，部署前先 nvidia-smi 确认目标 GPU 无进程

### 2. 🖥️ 基础设施快照
- **bjb1-18228** (4× 4090): connect.bjb1.seetacloud.com, root, `/root/acr-vla-conformal-refinement`
- **bjb1-32546** (6× 4090): connect.bjb1.seetacloud.com, root, 同上
- **bjb2-28827** (6× 4090): connect.bjb2.seetacloud.com, root, 同上（nohup 启动，cron 有 bug）
- **bjb2-40593** (1× 4090 D): connect.bjb2.seetacloud.com, root, 同上
- 无 W&B / 无 Git remote / 无 conda（直接 pip venv）
- JSON 输出路径: `/root/acr-vla-conformal-refinement/logs/eval_object_*.json`
- P0 关键进程: eval-argmin-object-seed44-r2 PID=428117 bjb1-18228:cuda:3（应已完成）
- eval-obs-only-object-norm02-seed44-r2 已完成（JSON 有效，registry 需从 failed 改为 success）

### 3. 📊 当前状态
**卡在一件事上：argmin seed44 结果回收**。过去 4 轮 Agent reset 都未成功拿到这个数据。obs_only seed44 = 16% 已确认。argmin seed44-r2 (bjb1-18228:cuda:3) 上次 9/10 tasks (11/90=12.2%)，只差 orange_juice 1 个 task，已过 12+ 小时必定完成。

**Registry 待修复**：
- eval-obs-only-object-norm02-seed44-r2: 当前标 failed，应改 success (overall_sr=0.16)
- eval-vla-only-object-seed45: 当前标 failed，应改 success (overall_sr=0.09, 18/200, 注意 20 rollouts)

**RUNNING ~16 实验**：seed44 辅助组（perdof/scalar/vla-mean/norm01/norm03/default）在 bjb1-18228 和 bjb1-32546；seed45 组（argmin/scalar/perdof-norm02/vla-mean/default/norm02）在 bjb2-28827 和 bjb1-32546。

**Magnitude curve figure 已完成**，Reviewer 审核通过（collapse region 标注已修正为 "per-DOF collapse region"）。

### 4. 📋 待办
- **第一件事**：ssh_read_only bjb1-18228 读取 argmin seed44 JSON → update_registry → 计算 3-seed Fisher exact test（obs 54/300 vs argmin ?/300）→ 汇报 p 值
- Fisher p<0.05 → log_decision dual claim（improvement + robustness），通知用户 + Paper Agent
- Fisher p=0.05-0.10 → 等 seed45 obs_only ε=0.2 + argmin 完成做 4-seed pooled
- Fisher p>0.10 → log_decision 走 Narrative B（robustness-only，magnitude curve 为核心贡献），更新 ROADMAP + paper_framing.md
- eval-obs-only-object-norm03-seed45 需重部署（之前因 cuda:3 冲突被 kill），等 GPU 释放后用显式 CUDA_VISIBLE_DEVICES 部署
- bjb1-18228:cuda:2 如果被 r4 占用 → kill r4（不需要重跑，r2 数据有效）
- seed45 全部完成后 → 4-seed pooled 统计 + Paper Agent patch 最终数字

### 5. 🎯 战略上下文
- **决策链**: D033(object obs_only +7pp FINAL) → D035(kill criterion) → D037(零纠正非 bug) → D038(ε=0.2 唯一配置, pooled 2-seed +4.5pp p≈0.12) → D039(perdof default=0% catastrophic)
- **核心状态**: obs_only ε=0.2 是唯一存活路径。3-seed obs_only: 22%/16%/16% pooled 18%。Argmin: 12%/17%/?。Magnitude 双曲线完整（obs_only 安全 vs perdof 崩溃）
- **最易判断错的事**:
  1. 不要被 cron:on_failed 骗——bjb2-28827 的 nohup 实验正常完成也会触发 on_failed，必须读 JSON 确认
  2. eval-obs-only-object-norm02-seed44-r2 数据有效（16%），不要再重部署 r4
  3. seed42=22% 是 outlier，seed43/44 都是 16%。论文 claim 不能基于 seed42 单点
  4. 即使 Fisher p>0.05，magnitude 双曲线（obs_only safe vs perdof collapse）是独立于 p 值的 publishable contribution
- **CoRL DDL**: abstract ~May 26, full paper ~Jun 2。时间充裕但 narrative 决策不能再拖


---
