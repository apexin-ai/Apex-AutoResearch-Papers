# reviewer / loop_11.md

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_11.md`
- **Structured JSON:** [`3dae176e92a331093cfc.json`](../../sessions/3d/3dae176e92a331093cfc.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: max_wall_time
updated: '2026-05-21T01:43:57+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：westd-34887 (cuda:0,1) + westd-41718 (cuda:0,1)，共 4 卡 RTX PRO 6000 96GB
- benchmark_eval.py `--allocation` 默认是 `global_topk`（不是 uniform）——所有声称 uniform 的实验必须显式传 `--allocation uniform`
- MSE 训练用独立脚本 `src/train_perlayer_mse.py`，不接受 `--loss_type`/`--dataset`/`--lambda_max` 等参数——与 `train.py` 参数不通用
- MSE 的 lambda_max=1000（非 KL 的 5000），改了就不是 controlled comparison
- Table 4 caption 已明确 "uniform allocation at 30%, global allocation at 50%"——两列 allocation 不同，填数据时必须对应

### 2. 🖥️ 基础设施快照
- 服务器：westd-34887 (root) + westd-41718 (root)
- 工作目录：远程 `/root/distill_sparse_swiglu/`，本地 `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/`
- Python：`/root/miniconda3/bin/python`（conda base，不用 venv）
- 模型：`/root/autodl-tmp/models/llama-3.1-8b`、`mistral-7b`、`qwen2.5-14b`
- HF cache：`/root/autodl-tmp/.hf_cache`，离线模式（HF_HUB_OFFLINE=1）
- wandb：DISABLED（WANDB_MODE=disabled）
- 截至 handoff 时：westd-34887 双卡空闲，westd-41718 cuda:1 在跑 RevKL 30% uniform eval（PID 279686 nohup，应已完成或接近完成）

### 3. 📊 当前状态
**刚完成**：
- Round 18 Action Matrix 全面审查，已 post 给 Director（含 per-layer KL 实验设计评估、RevKL downstream 预测、cross-seed Jaccard 风险分析、novelty 策略评估）
- Table 4 allocation 混用问题已被 Agent 修正（caption 改为 30%=uniform, 50%=global）
- ±std 公式不一致已修正（Mistral 改为 sample std，ARC-c 6.4pp）
- MSE 50% s123 确认不可用（sparsity 仅 5.1%，PPL=15789）
- STE 30% tied-score bug 已确认并处理（D090，Table 4 用‡标注）

**Registry 状态**（需关注的）：
- `mse50_s123`: RUNNING（实际已完成+失败，registry 未更新）
- `revkl_30_s42_uniform_eval` / `reverse_kl_30_s42_uniform_eval`: 可能已完成（两个重复进程）
- 5+ 个已完成实验仍在 RUNNING/PREPARING 状态（历史遗留，未清理）

**等待中**：
- Round 18 审稿报告 rebuttal 方案执行
- Director 决策：是否执行 W4 per-layer KL 实验

### 4. 📋 待办
- RevKL uniform eval 完成 → 核实 7-task downstream 数据，特别关注 MMLU（预测 ≤ KL 的 40.7%）；确认数值后 post 给 Director
- Director 批准 W4 per-layer KL → 审查代码实现，确认训练步数 ≥ 5000（否则每层仅 ~31 次更新不够收敛）；监控 3-seed 结果，预期 PPL 在 12-15 之间
- per-layer KL PPL ≈ end-to-end KL (< 10) → **立即 flag critical**：coupling 假说被削弱，论文叙事需要 major pivot
- per-layer KL PPL ≈ MSE (> 18) → 强证据支持 coupling scope 假说，post info 确认
- W7 cross-seed Jaccard 结果出来 → 确认 seed divergence < 15%；如果 > 30% 需要在 claim 中加 qualifier
- Agent 补 MoC / Activation Pattern Clustering 引用 → WebSearch 验证 arxiv ID 真实性（幻觉引用 = desk-reject）
- Q3 BCE 30% uniform PPL=15.71 → 这个数字异常（vs global=11.25），需要核实数据来源是否正确

### 5. 🎯 战略上下文
**核心叙事**：KL distillation 发现与 magnitude 完全不同的 neuron importance patterns（Jaccard 32-54%）。关键不是 "用 KL"，而是 "coupling alignment 是 critical design dimension"。JSD≈KL at 30% 证明 specific divergence 不重要，coupling 才重要。

**决策链**：D085（taxonomy 锁定 coupling alignment）→ D088（Mistral 3-seed 入表 mean±std）→ D089（Round 16 补 30% ablation）→ D090（STE 排除）

**最容易判断错的事**：
1. **不要把 Table 4 30% 列和 50% 列当成同一 allocation**——30% 是 uniform，50% 是 global。填数据时看错列 = 数据不一致
2. **MSE 的 lambda_max 不能改**——s123 失败是 seed sensitivity，不是 lambda 不够。改 lambda 就不是 controlled comparison
3. **per-layer KL 实验结果如果太好（≈ end-to-end KL），这是坏消息不是好消息**——说明 coupling 不重要，削弱论文核心论点。不要习惯性地把低 PPL 当成 positive
4. **审稿人 R2 的 novelty concern 本质上可能不可解**——目标不只是移动 R2，而是让 AC 有理由接受。per-layer KL 实验是给 AC 的弹药，不只是给 R2 的回答
5. **DDL = 2026-05-25（4 天后）**，EMNLP ARR May cycle


---
