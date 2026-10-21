# director / loop_3.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_3.md`
- **Structured JSON:** [`d9486597c5164104ff36.json`](../../sessions/d9/d9486597c5164104ff36.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-05-14T10:48:57+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：cuda:0/1/2/3（westd-47453 上的 4× RTX 6000 Pro 96GB）。不可使用其他 GPU。
- 诊断实验不可与 grid-b 训练共享 GPU（之前共享导致速度减半，被 Reviewer CRITICAL，已 kill）
- `pretrain_weighted.py` 默认 contamination_ratio=0.2（非 0.4），所有实验必须显式传 `--contamination_ratio 0.4`
- train_loss 跨方法不可比（uniform 是 unweighted，adaptive/grid 是 weighted），MVP 判定只能用 held-out eval perplexity
- adaptive 的 registry conclusion="success" 仅指训练完成，不代表假设验证（方案 C：不改 registry，report 中标注）

### 2. 🖥️ 基础设施快照
- 服务器：westd-47453 (connect.westd.seetacloud.com)，用户 root
- 工作目录：/root/provenance_weight_training
- Python：/root/miniconda3/bin/python（conda base 环境）
- 模型：/root/autodl-tmp/provenance_weight_training/output/models/（uniform/adaptive/grid_b 各 seed）
- 基础模型：models/Qwen/Qwen3-0.6B
- 数据：data/scored_data.jsonl（371K docs, 含 q_score）、data/human/eval_holdout.jsonl（67K docs, 纯人类）
- Eval 脚本：evaluation/eval_pipeline.py + eval_perplexity.py
- Auto-eval watcher：PID 74145，每 60 秒扫描新 checkpoint 并自动跑 eval
- 活跃进程（截至 handoff）：
  - cuda:0: grid_b_seed42_batch（串行 6 个 b 值，b=1.5 约 40%）
  - cuda:1: grid_b2_0_seed123（刚启动）
  - cuda:2: grid_b3_0_seed123（刚启动，PID 90129）
  - cuda:3: grid_b1_5_seed123（约 42%）

### 3. 📊 当前状态
MVP 验证进行中，核心假设：adaptive b* ≥ 90% grid-best perplexity improvement。

**已完成 + eval：**
| Method | b | Seed | Eval PPL |
|--------|---|------|----------|
| uniform | — | mean | 17.694 ± 0.008 |
| adaptive | b*(batch) | mean | 17.639 ± 0.006 |
| grid_b | 0.5 | 42 | 17.651 |
| grid_b | 0.5 | 123 | 17.638 |
| grid_b | 1.0 | 42 | 17.692 |

**关键发现：** adaptive 一致微优于 grid_b b=0.5（当前 grid-best），ratio ≈ 115%，MVP PASS 方向。b=1.0 ≈ uniform，说明 b 选择敏感。

**运行中（4 卡满载）：** grid_b seed42 batch b=1.5 + seed123 b=1.5/2.0/3.0。还差 seed42 的 b=2.0/3.0/5.0、seed123 的 b=5.0、seed456 全部 6 值。

**诊断实验未完成：** contamination=100% 和 contamination=0% 都被 kill 了（共享 GPU 问题）。需要等 GPU 空闲后重跑。这是回答"PPL 对污染是否敏感"的关键数据。

### 4. 📋 待办
- grid_b seed42/seed123 round 完成 → 检查 auto-eval 产出 → 汇总 b-PPL curve
- grid_b seed123 round 1 剩余（b=1.5）+ round 2（b=2.0/3.0/5.0）完成 → cuda:1/2/3 释放 → 启动 seed456 ×6 并行 + 重跑诊断实验（contamination=0% 和 100%，20M tokens，显式传 --contamination_ratio）
- 全部 18 个 grid-b eval 出齐 → bootstrap CI + Cohen's d → 正式 MVP gate 判定（D004: adaptive ≥ 90% grid-best improvement）
- MVP PASS → 调 complete_mvp()，读 post-mvp-kickoff skill，写 experiment_plan.yaml，跑 dream_simulate
- MVP FAIL → 按 D004 三级 kill criteria 分级处理
- 效应量若 < 1% relative PPL（Reviewer 建议的最小有意义差异）→ narrative 转向 "方法正确性 + grid search 替代 + 计算成本节省"，full paper 加 60% 污染和 3B 模型展示效应放大

### 5. 🎯 战略上下文
- 决策链：D001(AAAI) → D003(改 EMNLP ARR May 25 主攻) → D004(MVP 协议) → D005-D008(detector 从 ModernBERT 转 TF-IDF 解决 q-score 极化) → D009(gate AUC 从 0.95 降至 0.90)
- paper_framing.md 已有骨架，两条 narrative 路径：Path A (adaptive > grid-best) / Path B (adaptive ≈ grid-best 省计算)。Reviewer 评估 Path B 更稳健
- **最易判断错的事：** train_loss 数值——adaptive(9.27) vs uniform(7.31) 看起来像是回退，但这是加权口径差异，不是真实性能差距。必须用 eval PPL 比较。
- **效应量风险：** 0.3% relative PPL 改善很小。Reviewer 警告即使技术上 PASS，论文说服力取决于效应量。full paper 需要更高污染比例(60%)和更大模型(3B)来放大效应。诊断实验（contamination=0% baseline）能回答"污染到底伤害多大"，是论文 story 前提。
- **ROADMAP 未更新：** 近期任务 checklist 过时（还写着"等待 GPU 服务器"），需要刷新。


---
