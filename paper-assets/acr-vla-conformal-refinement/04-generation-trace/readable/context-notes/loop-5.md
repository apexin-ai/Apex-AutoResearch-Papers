# director / loop_5.md

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_5.md`
- **Structured JSON:** [`2eebcdf985d38cb5e3f2.json`](../../sessions/2e/2eebcdf985d38cb5e3f2.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_messages
updated: '2026-05-15T17:03:45+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：bjb1-32546 cuda:0-5, bjb1-18228 cuda:0-3, bjb2-28827 cuda:0-5, bjb2-40593 cuda:0
- bjb1-32546 cuda:0 当前双占（两个实验共享），不要再往上部署第三个
- evaluate.py 的 `--output_file` 在 acr_vla mode 下有 bug（传了参数但实际 None），所有已完成实验的 JSON 都需要用 parse_log_to_json.py 从日志提取
- 统计分析脚本 dry-run 数据全部过时（6-7 task partial），正式分析必须用 10-task FINAL 数据替换
- Fisher test 不要 pool 不同 norm 条件（Reviewer 已 flag L240-243 方法论问题），每个 norm 单独检验

### 2. 🖥️ 基础设施快照
- **bjb1-32546**：6 GPU A6000, 工作目录 /root/acr-vla-conformal-refinement, 分析脚本在 /root/acr-vla-conformal-refinement/scripts/（parse_log_to_json.py, analyze_fisher_exact.py, plot_magnitude_curve.py, summarize_object_table.py）
- **bjb1-18228**：4 GPU, 同工作目录
- **bjb2-28827**：6 GPU, 同工作目录，注意 scripts/ 目录未同步（只在 bjb1-32546 上有）
- **bjb2-40593**：1 GPU (cuda:0)
- 日志路径：`/root/runs/acr-vla-conformal-refinement/` 或 `/root/acr-vla-conformal-refinement/logs/`
- CRM checkpoint：crm-train-v3-norm-perdof (337,438 params), crm-train-v3-norm-obsonly

### 3. 📊 当前状态
**已锁定结果（seed=42, 10-task FINAL）**：
- Object 6-way：obs_only 0.1 = **19%** (+7pp vs argmin 12%) ✅, perdof 11%, scalar 9%, VLA-only K=1 12%
- Spatial perdof magnitude sweep 完成：norm 0.03/0.05/0.1/0.3 = 30/31/35/26%（倒 U 型，仅 0.1 ≈ argmin）
- Spatial obs_only magnitude sweep：norm 0.05/0.1/0.2 全部 35%（flat line，norm-robust）

**RUNNING 实验（~17 个）**：
- **seed=43 六方 object eval**（bjb1-18228 cuda:1-3 + bjb1-32546 cuda:1-3）：obs_only/argmin/perdof/scalar/VLA-mean/obs-only-norm02，进度 0-3.5/10，ETA 6-12h。**这是 go/no-go gate**——合并双 seed 后 Fisher test 决定统计显著性
- VLA-only-object-seed43（bjb1-32546 cuda:0，与 mag-obsonly-norm003-object 双占）
- Object magnitude sweep：bjb2-28827 上 obs_only norm=0.05/0.3 + perdof norm=0.05（刚部署）
- VLA-mean object seed=42（bjb1-32546 cuda:5，7.5/10）
- obs_only object norm=0.2 seed=42（bjb1-32546 cuda:4，5/10）
- eval-acr-object-v4-default（bjb2-28827，待 GPU 释放部署）
- obsonly-norm003-b2 spatial（bjb2-40593 cuda:0，4/10）

### 4. 📋 待办
- seed=43 obs_only + argmin 完成 → 立即跑 Fisher exact test（合并 200 trials），p < 0.05 则核心 claim 成立
- seed=43 gap < +5pp → 警告 Director，可能需要额外 seed 或降低 claim 强度
- VLA-mean object seed=42 完成 → 如果 ≈12%（= argmin），强化 "obs_only 优势来自 learned correction 而非 sample selection" 的论点
- magnitude sweep 全部完成 → 用 plot_magnitude_curve.py 生成 fig3（先修 xlabel "Perturbation norm" → "Correction magnitude (ε)"）
- eval-acr-object-v4-default 完成 → 证明 magnitude control 价值的 ablation 数据
- GPU 释放 → 优先部署 seed=43 缺失条件或 object magnitude 配对实验，不要空卡 >10min
- output_file bug 修复 → 在 seed=43 批量完成前修好，避免再手动 parse

### 5. 🎯 战略上下文
- **核心结论 Scenario C 已确认**：obs_only CRM 是唯一有效的 conditioning 方式（object +7pp, spatial flat but robust）；perdof/scalar 无价值甚至有害
- **论文 narrative 需调整**：spatial magnitude 是 null result（obs_only flat at 35%），magnitude sensitivity story 必须基于 object benchmark；perdof 不只是"高 norm 崩塌"，而是"仅 norm=0.1 勉强持平，其余全低于 argmin"
- **obs_only 19% 超出 writing_plan 预测 16%**，但 argmin 也从 6.7%→12% 升高，gap 从 +12.3pp 压缩到 +7pp
- **统计显著性是最大风险**：单 seed p ≈ 0.18，必须等 seed=43 合并。如果 seed=43 obs_only < 16%，合并后可能不达标
- **T1 崩塌证据**：perdof norm=0.3 让 T1（最简单 task）从 100% 跌到 50%，obs_only 保持 100%——论文 case study 用
- **CoRL DDL 还剩 ~11 天**，seed=43 是 critical path
- **易错点**：(1) 不要用 dry-run 的过时数据做正式结论 (2) 不要 pool 不同 norm 做 Fisher test (3) plot xlabel 是 correction magnitude 不是 perturbation norm (4) 部署前必须 nvidia-smi 查 GPU 空闲


---
