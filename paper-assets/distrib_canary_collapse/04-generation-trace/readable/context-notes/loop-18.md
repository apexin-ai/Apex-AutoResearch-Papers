# director / loop_18.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_18.md`
- **Structured JSON:** [`eeb0880019d6609cd492.json`](../../sessions/ee/eeb0880019d6609cd492.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 18
reason: max_messages
updated: '2026-05-22T19:59:02+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-17855 (cuda:0-5) + westd-19828 (cuda:0-1) = 8 GPU，不得使用其他设备
- D102 标准：downstream=mauve, threshold=true_3sigma_d105, n_perm=5000，不可更改
- D102 启动前必须验证：(1) gen_10/metrics.json 存在且非空 (2) 训练 PID 已退出（M075 教训）
- `--num_generations` 语义是"从 start_gen 再跑 N 代"不是"总共 N 代"（M076 教训）
- 1.4B 标准模型 = `pythia-1.4b-deduped`（D196 确认），phase_diagram_14b/ 路径的 non-deduped 数据是历史遗留不计入
- D079: ≤3B 用 fp32, >3B 用 bf16
- D189: 论文语言约束——"consistent across" ≠ "scale-invariant"
- 1.4B 是 additive evidence，不是 core claim，不改 abstract 的 "primarily Pythia-410M"

### 2. 🖥️ 基础设施快照
- 服务器 1：westd-17855 (connect.westd.seetacloud.com)，root，6 GPU (A6000 or similar)
- 服务器 2：westd-19828 (connect.westd.seetacloud.com)，root，2 GPU
- 工作目录：`/root/autodl-tmp/distrib_canary_collapse`
- Python/conda：aml-train 镜像，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- D102 分析脚本：`run_5method_analysis_d102.py`（两台服务器已统一，MD5 一致）
- 训练脚本：`iterative_train.py`，默认模型 pythia-410m
- 1.4B 结果路径：`results/scale/14b_*`（不是 `results/phase_diagram_14b/`）
- 活跃进程：上次检查时 17855 上 6 个 1.4B 实验在跑（tmux sessions），19828 两个 GPU 空闲。需要重新 SSH 确认当前状态（距上次检查已过 16h+）

### 3. 📊 当前状态
**刚做完**：
- t10_a050 双路径溯源完成——根因是模型变体差异 (deduped 4/8 vs non-deduped 0/8)，非 seed variance (D196)
- 派了 2 个 Worker (t10_a075-kill-d102 + t10_a060-kill-d102) 执行 kill+D102，但 Agent idle 16h 未收到回调

**RUNNING 实验（上次已知，需重新确认）**：
- 17855: t10_a045 (cuda:4), t10_a060_v2 (cuda:3), t15_a045 (cuda:5), t15_a050 (cuda:1), t15_a060_v2 (cuda:0)
- 17855:cuda:2 t10_a075_v2 — Worker 已派 kill+D102 但结果未知
- 19828:cuda:0 t15_a075 — 上次 report 显示空闲，可能已完成或 crash
- 19828:cuda:1 — 空闲，计划部署 t10_a050 s43 cross-seed 但未执行

**关键未知**：t10_a075 D102 结果（KEY DISCRIMINATOR: ≥6/8 → Scenario B, <6/8 → Scenario C）。Agent 16h 未响应，Worker 可能早已完成但回调丢失。

### 4. 📋 待办
- **立即**：SSH 17855+19828 全面扫描所有实验状态（gen_10 完成否、进程存活否）——16h 信息断档需要补
- t10_a075 gen_10 完成 → kill 进程 → D102 → 汇报 PermG（≥6/8 = Scenario B confirmed, <6/8 = Scenario C）
- t10_a060 gen_10 完成 → kill → D102 → sync-dip scale verification
- t10_a045 gen_10 完成 → D102 → 410M 是 0/8, 预期 1.4B 也 0/8
- T=15 cells gen_10 完成 → 逐个 D102
- 19828 空闲 GPU → 部署 t10_a050 s43 (pythia-1.4b-deduped, seed=43) cross-seed
- 确认 410M 实验用的 model 是 deduped 还是 non-deduped → 影响论文 scale comparison 措辞
- 所有 1.4B D102 完成 → 汇总 phase diagram 1.4B overlay → Director 判定场景 A/B/C → Paper Agent 填充 discussion templates
- R10 审稿结果返回 → 按 review-report-action skill 处理

### 5. 🎯 战略上下文
- **论文**："Mapping the Detectability Landscape of Iterative Model Collapse"，目标 EMNLP 2026 ARR June (DDL ~6/15, 距今 ~24 天)
- **当前分数** R8=3.0 (Findings) → 目标 3.5 (Borderline Conference)。R9 全修复 → R10 已提交审稿
- **410M phase diagram 20/20 COMPLETE**，6/8 ceiling confirmed，steepness k_obs=15.7 vs k_H0≈5-6
- **1.4B 是 additive evidence**：8 cells (T=10/15 × α=0.45/0.50/0.60/0.75)，用于论文 Discussion 加分
- **场景预评估**：A(30% positive) / B(55% onset shift, most likely) / C(15% weak)
- **t10_a050 1.4B**：4/8 (deduped)，onset boundary 不稳定，与 410M (s42=6/8 s43=0/8) 模式一致
- **entropy one-step saturation at 1.4B**：gen_0→1 drops 26.8%，破坏 Granger temporal gradient；ECE channel 更 robust（+49.3% gradual）
- **易错点**：(1) 不要混淆 scale/ 和 phase_diagram_14b/ 路径 (2) 不要在 gen_10 未完成时跑 D102 (3) --num_generations 是增量不是总量 (4) 不要报告截断数据的结果给用户
- **决策链**：D189(1.4B=additive) → D192(shape comparison) → D193-195(提分策略) → D196(deduped=标准)
- **Paper Agent** 已准备 4 个 discussion template (A/B/C/D scenarios)，等 1.4B 数据填充
- **文献蒸馏**：He2025 引用 + Truong 反向定位 + detection→action gap 待 Paper Agent 处理（排在 R10 后）


---
