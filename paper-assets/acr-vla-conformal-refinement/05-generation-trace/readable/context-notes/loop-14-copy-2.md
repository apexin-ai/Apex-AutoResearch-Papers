# agent / loop_14.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_14.md`
- **Structured JSON:** [`246801a29e11f341bab2.json`](../../sessions/24/246801a29e11f341bab2.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: idle_timeout
updated: '2026-05-16T11:10:07+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单严格 17 张：bjb2-40593:cuda:0, bjb1-18228:cuda:0-3, bjb1-32546:cuda:0-5, bjb2-28827:cuda:0-5。白名单外的 GPU 绝对不能碰，Director 指令也不行
- bjb2-40593 环境有坑：无 .git repo、CRM cache 路径是旧的、曾出现 OOM SIGKILL（系统 RAM）。只部署轻量 eval，不要在上面跑需要大内存的任务
- submit_training_job 命令必须用 `bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/acr-vla-conformal-refinement && ..."` 包裹。裸 `python` 会 EXIT_CODE=127
- kill 实验前必须 `ps aux | grep` 完整命令行逐参数比对。曾因 norm03/norm003 混淆误杀有效进程，空闲 9 小时
- exp_id 中 norm 值用 `p` 替代小数点：norm-0p3 = 0.3。禁止歧义缩写（norm03）

### 2. 🖥️ 基础设施快照
- **服务器 × 4**：bjb1-18228 (4 GPU), bjb1-32546 (6 GPU), bjb2-28827 (6 GPU), bjb2-40593 (1 GPU)
- **工作目录**：`/root/acr-vla-conformal-refinement`（所有服务器相同）
- **Python**：`/root/miniconda3/bin/python`，conda base 环境。不用 venv
- **CRM checkpoints**：`/root/autodl-tmp/checkpoints/crm_v3_norm/{obs_only,perdof,scalar_unc}/crm_best.pt`
- **HF cache**：`/root/autodl-tmp/.hf_cache`（必须设 HF_HOME + HF_HUB_OFFLINE=1 + TRANSFORMERS_OFFLINE=1）
- **活跃进程 16 个**（全部 RUNNING，按服务器分）：
  - **bjb1-18228**: cuda:0 eval-obs-only-object-norm01-seed45 | cuda:1 eval-perdof-object-seed44 (PID 452982) | cuda:2 eval-obs-only-object-norm02-seed44-r2 (PID 428406, **P0**) | cuda:3 eval-argmin-object-seed44-r2 (PID 428117, **P0**)
  - **bjb1-32546**: cuda:0 eval-scalar-object-seed44-r2 (PID 226878) | cuda:1 eval-vla-mean-object-seed44 (PID 212655) | cuda:2 eval-obs-only-object-norm03-seed44 (PID 220777) | cuda:3 eval-obs-only-object-norm02-seed45 (PID 233544) | cuda:4 eval-obs-only-object-norm01-seed44 (PID 227086) | cuda:5 eval-obs-only-object-default-seed44 (PID 229751)
  - **bjb2-28827**: cuda:0 eval-scalar-object-seed45 (PID 224623) | cuda:1 eval-perdof-object-norm02-seed45 (PID 222824) | cuda:2 eval-mag-perdof-norm03-object-r3 (PID 140759, **⚠️ 进程消失 miss 4/5**) | cuda:4 eval-vla-only-object-seed45 (PID 221407) | cuda:5 eval-argmin-object-seed45 (PID 215932)
  - **bjb2-40593**: cuda:0 eval-perdof-object-default-seed44 (PID 316382)
- **bjb2-28827:cuda:3 空闲**——seed45 部署时漏了这张卡

### 3. 📊 当前状态
上一轮 session 完成了：magnitude curves 双曲线（obs_only 6/6 + perdof 6/6, D039 confirmed），seed43 FINAL 结果确认（D038: ε=0.2 唯一可辩护配置），seed44/45 全面部署（16 个 eval 同时跑），Narrative B 修正完成。

**关键等待**：
- **P0 seed44 obs_only ε=0.2** (bjb1-18228:cuda:2) + **argmin** (bjb1-18228:cuda:3)——这两个决定 3-seed Fisher test 结果，决定最终 narrative（Dual claim vs Robustness-only）
- **⚠️ eval-mag-perdof-norm03-object-r3** (bjb2-28827:cuda:2) reconcile 报"process gone, miss 4/5"——需要立即诊断：这是 seed42 perdof norm=0.3 的补跑（预期结果 ~4%），不是 P0 但空占 GPU

**0 个 Worker 在跑**——因为处于 WRITE HANDOFF 状态，但新 session BOOT 后必须立即拉起 Worker 处理 perdof-norm03 告警 + 准备论文写作

### 4. 📋 待办（条件触发式）
- eval-mag-perdof-norm03-object-r3 告警 → SSH 诊断进程状态；若确认死亡则标 DONE(failed)/重跑，释放 bjb2-28827:cuda:2
- P0 seed44 (obs_only + argmin) cron 回调到达 → 立即跑 3-seed Fisher test：obs_only=[22,16,X] vs argmin=[12,17,Y]；p<0.05 → Dual claim narrative，p>0.05 → Robustness-only (Narrative B)
- seed45 全部完成 → 4-seed pooled analysis，更新 paper_framing.md 的 headline result
- bjb2-28827:cuda:3 空闲 → 部署缺失的 seed45 实验（如 vla-mean-seed45 或 obs_only-norm03-seed45）
- 所有 seed44 完成 → 派 Worker 开始画 magnitude curve figure（论文核心 figure，最高优先级）
- Fisher test 结果出来 → 派 Worker 写 abstract 最终版（DDL May 26）

### 5. 🎯 战略上下文
**核心结论链**：perdof 死亡(D027) → obs_only 唯一存活(D029-D030) → ε=0.2 最优(D038) → magnitude robustness claim 成立(D039)。Spatial 全死，论文只写 Object。

**决策分叉点**：3-seed Fisher test 决定论文力度。
- p<0.05 → Dual claim（improvement + robustness），headline = "+Xpp, p<0.05"
- p>0.05 → Narrative B（robustness-only），magnitude curve figure 为核心贡献，不 claim statistical improvement

**易错点**：
- 不要把不同 seed 的绝对值直接对比（seed42 obs_only=22% 不等于 seed43 也会 22%，seed 间方差 6pp）
- Pooled 2-seed 已是 p≈0.12，seed44 需要 obs_only≥20% + argmin≤14% 才可能翻到 p<0.05，概率不大
- Narrative B 已经写好草稿 (narrative_b_draft.md)，不需要从头来
- eval-mag-perdof-norm03-object-r3 是 seed42 的 perdof norm=0.3 补跑，已知 seed42 norm=0.3 perdof=4%，即使此实验死了也不影响核心 claim（D039 双曲线已有足够数据点）
- CoRL abstract DDL ~May 26（10天），full paper DDL ~Jun 2（17天）——时间紧但够用，前提是 seed44 P0 不出幺蛾子


---
