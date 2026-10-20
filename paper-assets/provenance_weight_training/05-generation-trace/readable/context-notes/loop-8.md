# director / loop_8.md

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_8.md`
- **Structured JSON:** [`97fa97a631355f9da0e5.json`](../../sessions/97/97fa97a631355f9da0e5.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: max_messages
updated: '2026-05-15T14:29:26+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0/1/2/3 @ westd-47453，严禁使用其他卡
- tau_06_seed42 conclusion 已修正为 **negative**（PPL 17.68 > baseline 17.65），不要当 success 引用
- τ-b* 因果方向：τ↑ → α_eff 下界更严 → b*↑ → 降权更强（Agent 已存 memory，论文写作必须用此方向）
- D025：τ 已降级为 empirical HP（不是理论推导），Claim 3 framing 相应调整
- seed456 b≥2.0 数据有 checkpoint resume artifact（D026），论文用 2 seeds + appendix 注明
- 聚合口径：论文用 ratio of means (89.9%) 而非 mean of ratios (91.0%)

### 2. 🖥️ 基础设施快照
- 服务器：westd-47453 (connect.westd.seetacloud.com)，root
- 工作目录：/root/provenance_weight_training
- Python：conda base 环境（aml-train 镜像）
- 4× RTX 6000 Pro 96GB，GPU 预算已消耗 ~115h / 剩余 ~65h
- W&B 未配置，Git 未配置（可选）
- 飞书 A+B+C 群均已配置，审稿 C 群 active

### 3. 📊 当前状态
**刚完成**：tau_06_seed42 conclusion 修正 + τ-b* 因果关系记忆存储

**RUNNING**（2 个）：
- tau_07_seed42 (cuda:0, PID 209824) — τ=0.7 sweep
- tau_05_seed42 (cuda:1) — τ=0.5 sweep

**ANALYZING**（1 个）：
- nmin1_seed42 — n_min=1 极端 case，等分析结果

**PREPARING**（5 个）：
- tau_09_seed42 — 刚因 tmux 冲突失败，Agent 派 Worker 清理后重提交 cuda:3
- tau_095_seed42 / adaptive_v2_seed42/123/456

**⚠️ cuda:2 和 cuda:3 空闲**——tau_09 重提交应占 cuda:3，cuda:2 需尽快派任务（tau_095 或 nmin4）

### 4. 📋 待办（条件触发式）
- tau_07/tau_05 完成 → 收集 PPL，更新 τ sweep 汇总表；如果 τ=0.5~0.9 PPL 方差 < 0.05 → Claim 3 (robustness) 成立
- nmin1 分析完成 → 检查是否 over-downweight（预期 b* 偏大、PPL 偏差）
- tau_09 重提交成功确认 → 检查 cuda:2 空闲 → 派 tau_095 或 nmin4
- 所有 τ sweep 完成 → 综合判断 Claim 3 强度；PPL 方差 ≥ 0.05 → 需调整 claim 或补 seed
- cuda:2/cuda:3 空闲 > 10min → 立即从排期表选下一个实验填入（优先级：tau_095 > nmin4 > batchsize8/16）
- P0 τ sweep + n_min + batchsize 全部完成 → 评估是否启动 P1（contamination_60 / cross_generator / llama3b）或直接进入论文写作

### 5. 🎯 战略上下文
- **投稿目标**：EMNLP 2026 ARR May 25（剩 10 天）
- **核心结论链**：
  - D023: dual-constraint (α_eff + ESS) 是正确框架
  - D029: ESS-only PPL=17.73 vs adaptive PPL=17.65 → min-intervention > max-intervention，Key Risk #1 resolved
  - Golden ratio PPL=17.654 ≈ adaptive 17.65 → oracle 知道真实比例也没明显优势，adaptive 接近 oracle
  - Grid-best b=0.5 PPL=17.651 ≈ adaptive → adaptive 自动找到了接近最优的 b*
- **最容易判错的事**：
  1. τ=0.6 是 negative（PPL 劣化），不要和之前被 kill 的 tau_0.6 混淆——它们是不同实验（后者是旧代码 bug 版本）
  2. 审稿阶段已启动（C 群），但你是 Research Director，不参与论文格式/投稿材料——那是 Review Director 的事
  3. GPU 预算看似充裕（~65h 剩余）但 P0 就要 ~40h，P1 如果要做需要申请扩容


---
