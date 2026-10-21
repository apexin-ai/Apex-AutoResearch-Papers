# agent / loop_10.md

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_10.md`
- **Structured JSON:** [`8bc0ca9203d7fda73486.json`](../../sessions/8b/8bc0ca9203d7fda73486.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: idle_timeout
updated: '2026-05-15T22:04:23+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 白名单**: gpu-6000pro-2 cuda:0, cuda:1 only。不得使用其他服务器或 GPU 编号
- **EDD 措辞禁令 (D027)**: 禁止写 "three models all achieve statistically significant EDD=4"。只有 Pythia d3v4 p=0.001 显著，OLMo p=0.091 边际，GPT-2 XL p=0.505 不显著。正确措辞强调 "方向一致性 + CI + p-values"
- **Cross-strategy d1v2 反转 (D015)**: 论文不得将 nucleus 和 temperature 归为同一类 "soft sampling"。temp09 holdout d1v2 AUC 低至 0.13/0.25，是 genuine structural shift 不可 z-score 修复
- **DCOL 已死**: v1-v6 全部失败。Plan A 已激活——Atlas/EDD 是 primary contribution。不再尝试 DCOL
- **DDL**: EMNLP ARR May 25——剩余 10 天。Phase 2 写作 + Phase 3 提交

### 2. 🖥️ 基础设施快照
- **服务器**: gpu-6000pro-2，工作目录 `/root/autodl-tmp/recursive_gen_depth_est`
- **Python**: conda base env (`/root/miniconda3/bin/python`)，aml-train 镜像
- **数据**: `/root/autodl-tmp/recursive_gen_depth_est/data/` 下各模型×策略子目录
- **结果**: `/root/autodl-tmp/recursive_gen_depth_est/results/`（feature_ablation/, shap_analysis/, w2_domain_bias/, xgb_lgbm_3cell/ 等）
- **W&B**: 未配置（RF/分析类实验不用 W&B）
- **活跃进程**: 无 RUNNING 实验。两卡空闲
- **活跃 Cron**: 0
- **活跃 Worker**: 2 个 running（worker_exp_plan_013_downstream_curation_poc 和 worker_exp_plan_015_dolma_supplement）

### 3. 📊 当前状态
Phase 1 实验全部完成（54 experiments: 32 success / 3 negative / 6 failed）。3×3 矩阵 9/9 DONE，EDD 三模型验证 DONE，所有 P0 实验完成。

**正在进行**:
- `downstream_curation_poc_001` (QUEUED) — Worker running，plan_013 下游 curation PoC
- `feature_ablation_9cell` (PREPARING, conclusion=failed) — 之前失败过，可能需要重试
- Worker `plan_015_dolma_supplement` running — Dolma 数据补充实验

**刚完成的关键工作**:
- SHAP TreeExplainer 9-cell 分析（替代审稿人质疑的 attention-importance 方法）
- Wild-data calibration: WikiText-103 100% 分类为 d0，RF 对 domain shift robust
- Domain bias (W2): seed group prediction at chance (10.2%)，无 domain bias
- XGBoost/LightGBM baseline: 与 RF 收敛于 78-79%，证明 19-dim 特征上限
- Paper polish + warning-level review fixes + Section 5.4 expansion（N2 dual backbone）

**审稿 Issue 追踪**:
- Critical open: R1-N1 (EDD 公式), R2-N2 (文献)
- Warning 待 Paper Agent: W3/W5/W6/R2-W2/R2-W4/R2-W6
- Rebuttal open: W2/W4/R2-W3

### 4. 📋 待办（条件触发式）
- Worker plan_013 (downstream_curation_poc) 完成 → 分析结果，更新 registry，决定是否纳入 Discussion
- Worker plan_015 (dolma_supplement) 完成 → 分析 Dolma 域数据结果，补充 wild-data calibration 叙事
- feature_ablation_9cell PREPARING/failed → 检查失败原因，决定是否重试（数据在 results/feature_ablation/ 已有大部分结果）
- 上述 Worker 完成后 → 全力推 Paper Agent：处理所有 Warning 级审稿修改，纳入 SHAP/domain-bias/XGB-LGBM 新数据
- Paper 修改完成 → Reviewer 对抗迭代 (max 5 rounds) → bibliography audit → 提交

### 5. 🎯 战略上下文
- **核心结论**: 递归生成深度可通过 19 维统计特征（以 p90_ppl 和 var_surprisal 为主导）以 70-85% 准确率估计。Atlas/EDD 是 primary contribution。三模型 EDD=4（d4v5 boundary），但统计显著性只有 Pythia 确切通过
- **决策链**: D011 (Plan A 激活) → D020 (取消 DCOL ablation) → D024 (EDD 连续衰减曲线叙事) → D027 (EDD 声明降级) → D029 (域偏差叙事调整)
- **最易判断错的事**: (1) 不要高估 EDD 统计强度——只能说方向一致，不能说三模型都显著; (2) Cross-strategy LOO 均值 59.1% 看着低，但 9/9 > chance 是核心; (3) feature_ablation_9cell 的 "failed" conclusion 可能只是部分 cells 未跑完而非真失败——检查 results/ 目录再决定; (4) 两个 running Worker 可能很快回调，准备好处理
- **GPU 利用**: 两卡当前空闲。Phase 2 写作期间 GPU 可用于补充实验（plan_013/plan_015 正在利用）


---
