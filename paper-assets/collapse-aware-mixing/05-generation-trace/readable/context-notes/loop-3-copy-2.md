# agent / loop_3.md

**collapse aware mixing** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_3.md`
- **Structured JSON:** [`15cd1899879d2b0ae696.json`](../../sessions/15/15cd1899879d2b0ae696.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_messages
updated: '2026-05-13T23:37:57+00:00'
---

### 1. 🔴 硬约束 / 红线
- 只能用 **cuda:0**（gpu_ids 白名单仅 `["cuda:0"]`），服务器 **cqa1-38874**
- submit 命令必须包含 `source /etc/network_turbo && export REQUESTS_CA_BUNDLE=... && export SSL_CERT_FILE=... && export HF_HUB_DISABLE_XET=1 && export HF_HOME=/root/autodl-tmp/.hf_cache && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`（缺任何一项都会崩，已踩坑 4 次）
- **不要创建 venv**，服务器用 conda base 环境
- 模型/数据/输出必须写 `/root/autodl-tmp/`，根分区只有 30GB
- compare_eff_rank_vs_ngram.py 的 verdict 不可直接引用——阈值不对称（generated eff_rank rel=0.5% vs n-gram rel=10%，差 20 倍），需统一阈值重新判定
- SVD vs Gram Matrix 命名不一致（代码用 SVD σ_i，paper 写 Gram λ_i=σ_i²），论文需统一

### 2. 🖥️ 基础设施快照
- **服务器**: cqa1-38874, 1× RTX PRO 6000 96GB
- **工作目录**: `/root/collapse-aware-mixing/`
- **Python**: `/root/miniconda3/bin/python`（conda base，不用 venv）
- **v7 输出**: `/root/autodl-tmp/output_v7/`（18 checkpoints across G0/G1/G2）
- **v5 输出**: `/root/autodl-tmp/output/`（G0 完整，其余废弃）
- **HF cache**: `/root/autodl-tmp/.hf_cache`
- **模型**: EleutherAI/pythia-1b（pretrained from HF）
- **数据集**: wikitext-103-raw-v1, 20M tokens/gen, 5000 holdout seqs
- **活跃进程**: pivot_b_full_18ckpt (PID 109597, tmux session, cuda:0) — 状态 QUEUED
- **活跃 Worker**: `worker_check_pivot_b_full_urgent_20260513T233635` (running) — 正在检查 pivot_b_full_18ckpt 状态
- **Cron**: reconcile 返回 0 条活跃 cron

### 3. 📊 当前状态
**刚做完**: pivot_b_verification (DONE/negative) — 在 3 个 final checkpoint 上对比 generated eff_rank vs n-gram entropy。结论：generated eff_rank 信号极强（63.89→3.87→1.06, -98.3%），但在 3-checkpoint 粗粒度对比下 n-gram 检测更早（G1 step 152 vs G1 final）。compare verdict "PIVOT_B_LOSES" 但方法论不公平（3 vs 18 checkpoints）。

**正在做**: pivot_b_full_18ckpt (QUEUED) — 在全部 18 个 checkpoint 上跑 generated eff_rank，与 n-gram 的 18 checkpoint 数据做公平对比。这是 D013 关键问题的最终回答：generated eff_rank 是否比 n-gram 更早/更平滑。一个 Worker 正在检查此实验状态。

**Registry 概览**:
- QUEUED: pivot_b_full_18ckpt
- PREPARING: mvp_pilot_v8, mvp_pilot_v8_r2, mvp_pilot_v3, mvp_pilot_v2（全部是历史残留，可忽略）
- DONE: pivot_b_verification (negative), mvp_pilot_v7 (failed/G2 KL shape mismatch), mvp_pilot_v5 (failed/timeout), mvp_pilot_v4 (failed/lr divergence), mvp_pilot (failed/conda)

**等待中**: Worker 回调 pivot_b_full_18ckpt 结果

### 4. 📋 待办（条件触发式）
- **pivot_b_full_18ckpt Worker 回调到达** → 分析 18-checkpoint generated eff_rank 曲线 vs n-gram 曲线，判定：
  - generated eff_rank 在 n-gram 之前下降 → **Pivot B GO**，更新 paper_framing.md claim 为 "self-referential spectral eff_rank is leading indicator"，准备 PI 控制器实验（控制信号改为 generation-side eff_rank）
  - generated eff_rank 与 n-gram 同步或更晚，但曲线更平滑 → **Pivot B MARGINAL**，走 D015 Q3 路径：跑端到端 PI 对比证明平滑信号→更好控制
  - generated eff_rank 不比 n-gram 有任何优势 → **Pivot B KILL**，走 D015 Q2 路径：negative result paper（"holdout eff_rank 与 collapse 解耦" 本身有价值），需补 multi-scale + multi-seed 验证（~3-4 天 GPU）
- **mvp_pilot_v8/v8_r2/v3/v2 (PREPARING)** → 历史残留实验，建议清理（状态不会推进，无 cron 监控）
- **Director 审批 Framing 调整** → 如收到 [FRAMING APPROVED]，按 framing-reaudit skill 做全文 re-audit

### 5. 🎯 战略上下文
**核心决策链**: D001(MVP方案) → D003(切wikitext) → D005(lr=2e-6) → D007(降至20M) → D011(holdout eff_rank 上升，假设挑战) → D014(C1 definitively falsified) → D012(Pivot B首选) → D016(Pivot B 信号确认GO，需全checkpoint数据) → **等待 pivot_b_full_18ckpt 结果**

**核心结论**:
1. **原假设 C1 被 definitively falsified**: holdout eff_rank 在 model collapse 过程中不仅不下降，反而微升（+0.96%）。PPL 同样失灵（+2.4%）。所有 holdout-side 指标均对 collapse 失灵。
2. **Pivot B 方向确认**: generation-side eff_rank 暴跌 -98.3%，信号极强。但需证明比 n-gram entropy 有额外价值（D013）。
3. **Direction C (per-layer holdout eff_rank) 已 KILLED**: 所有层变化 <1%。
4. **SIGMA 论文已占 "谱分析检测 collapse" 位置**: 我们的差异化 = "passive monitoring → active closed-loop control"。

**易错点**:
- **不要把 3-checkpoint 粗粒度 verdict ("PIVOT_B_LOSES") 当最终结论** — 那是方法论不公平的对比，全 18 checkpoint 数据才是最终判定
- **不要混淆 holdout eff_rank (~677-683, 稳定) 和 generated eff_rank (~64→4→1, 暴跌)** — 同一个指标在不同观测面上表现完全相反
- **DDL 2026-05-25**，剩 12 天。时间线：pivot 验证(几小时) + P0 实验(~4天) + full-scale(~5天) + writing(~2天) = 非常紧凑，H100 不到位会卡死
- **PI 控制器代码尚不存在**，是非平凡工程任务，controlled_pipeline.py 中控制信号需从 holdout eff_rank 改为 generation-side 信号
- **padding_side=right 问题未修复**: v7 评估阶段仍有 68 次 right-padding 警告，不影响 holdout 指标但可能影响 n-gram/coverage 计算


---
