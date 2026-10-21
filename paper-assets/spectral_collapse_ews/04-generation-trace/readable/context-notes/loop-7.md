# agent / loop_7.md

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_7.md`
- **Structured JSON:** [`2995cc40c783cfcf7a40.json`](../../sessions/29/2995cc40c783cfcf7a40.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: idle_timeout
updated: '2026-05-23T03:04:33+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目仅有 rtx6000-diagprobe 一台服务器，GPU 白名单 cuda:0 / cuda:1（共 2 张 RTX PRO 6000 Blackwell）
- 磁盘：根分区 ~30GB，checkpoint 必须写 `/root/autodl-tmp/spectral_collapse_ews/`。exp_014 曾因磁盘满在 Gen 6 崩溃，提交实验前必须 `check_disk_before_experiment`
- EMNLP 2026 ARR DDL = **May 25**。Round 2 修订已提交（apr_20260522T183554_d8x0），但 r=0.2 和 r=0.5 的多 seed 数据尚未集成到论文——这两个实验完成后需要立即整合并 commit 补充修订
- submit_training_job 命令必须自带环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/spectral_collapse_ews && ...`
- 模型已离线缓存，训练命令需加 `HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1`

### 2. 🖥️ 基础设施快照
- **服务器**: rtx6000-diagprobe，2× RTX PRO 6000 Blackwell Server Edition
- **工作目录**: `/root/spectral_collapse_ews`
- **Python**: `/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- **激活**: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **模型缓存**: EleutherAI/pythia-410m-deduped + pythia-1b-deduped（均已离线缓存）
- **Checkpoint 盘**: `/root/autodl-tmp/spectral_collapse_ews/checkpoints_phase1/`
- **活跃进程**:
  - exp_017 (r=0.2 seed43, cuda:1) — cron 监控中，上次检查 ~Gen 6/10
  - exp_018 (r=0.5 seed43, cuda:0) — cron 监控中，上次检查 ~Gen 1/10
- **lm_eval 注意**: 新版本输出 `results_TIMESTAMP.json` 而非 `results.json`，Worker 收集脚本需 glob 匹配

### 3. 📊 当前状态
- **Round 2 修订已提交审稿系统**，等待用户确认审稿模式（推荐 continue）
- **论文 + response letter 已 committed**（7 commits），主文 ≤ 8 页 ✓
- **exp_017** (r=0.2 seed43, cuda:1): RUNNING，预计 May 23 ~03:00 UTC 完成。提供 r=0.2 的第 2 个 seed
- **exp_018** (r=0.5 seed43, cuda:0): RUNNING，预计 May 24 完成。提供 r=0.5 的第 2 个 seed
- **exp_016** (r=0.3 seed44): 已完成 ✅，3-seed 数据已集成到论文
- **无活跃 Worker**，无待处理 Director 决策
- **Seed 覆盖实际状态**: r=0 ✅3-seed | r=0.2 🔄1-seed+exp_017运行中 | r=0.25 ✅3-seed | r=0.3 ✅3-seed | r=0.5 ⬜1-seed+exp_018运行中

### 4. 📋 待办（条件触发式）
- **exp_017 cron 回调到达** → spawn Worker 用 `artifacts/plan_018/exp017_integration_template.md` 收集 r=0.2 seed43 per-gen 数据 → 计算 2-seed mean/std → 更新 Table 3 r=0.2 行 → update registry → commit 论文 → 汇报 Director
- **exp_018 cron 回调到达** → spawn Worker 用 `artifacts/plan_018/exp018_integration_template.md` 收集 r=0.5 seed43 per-gen 数据 → 计算 2-seed mean/std → 更新 Table 3 r=0.5 行 → update registry → commit 论文 → 汇报 Director
- **两个实验都完成后** → 全文一致性扫描（旧值残留检查）→ 最终 Round 2 补充提交准备
- **Round 2 审稿报告到手** → 按 `review-report-action` skill 处理（Holistic Pass → Per-Comment Action Matrix）
- **exp_017 如果 negative**（风险极低，Gen 0-5 已显示 Type II 特征）→ 仍需汇报 Director，不得默跑下一个

### 5. 🎯 战略上下文
- **核心结论**: SLV（谱对数体积）是递归合成训练中模型坍缩的可靠早期预警信号。坍缩遵循三阶段谱模式（decompression → onset → acceleration）。临界混合比 r_crit ∈ (0.25, 0.3]：r ≤ 0.25 出现 Type II 轨迹（瞬时下降+恢复），r ≥ 0.3 出现 Type III（单调扩张，无坍缩）
- **审稿状态**: Round 1 得分 3.0（Findings 线），目标 3.5（Borderline Conference）。15/16 issues resolved。关键修复：MF2 SLV 公式修正、MF3 多 seed 覆盖、signal attenuation reframe
- **易判断错的事**: (1) D-4 (distinct-4) 高方差（CV 远高于 SLV），不要期望 D-4 的 cross-seed 一致性达到 SLV 水平；(2) Reviewer 认为定性叙事升级可行（"全 ratio trajectory type 一致"），但定量升级需要 3-seed——目前 r=0.2 和 r=0.5 只有 2-seed，统计意义不充分；(3) exp_014b 在 registry 中状态是 ALLOCATED 但 conclusion=success，这是 resume 实验的遗留状态不一致，不影响数据
- **决策链关键节点**: D029 收紧 r_crit 到 (0.25, 0.3] → D031 撤回下修保持 Type II 分类 → D034 non-decreasing condition 改用 cross-seed mean → D036 r=0.2/0.5 第三 seed 降为 best-effort
- **整合效率**: integration template + 数据收集脚本已就绪（`artifacts/plan_018/`），数据到手后 ~30min 可完成整合


---
