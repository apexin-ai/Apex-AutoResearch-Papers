# director / loop_3.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_3.md`
- **Structured JSON:** [`5cdb5165cbdac08f5702.json`](../../sessions/5c/5cdb5165cbdac08f5702.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_messages
updated: '2026-05-14T21:17:32+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 westd-19828 的 cuda:0 和 cuda:1（项目配置白名单，不可越界）
- kill 实验进程必须用 `kill -9` + `ps -p` 验证死亡——之前 kill_job 只杀 tmux session，python 子进程逃脱成 orphan 导致 a025_s42 数据损坏（v2 事故）
- TY Granger 不能作为 "gold standard" 引用——D013 已确认 TY 在 N=11 下 d_max sensitivity 从 0% 到 94% 震荡，完全不可用于区分真/伪关联
- MAUVE 绝对值不可信（FAISS clustering 样本不足警告），仅可做跨条件相对对比
- α-sweep 同一 α 值内跨 seed 代码必须一致（a025_s42 因此重跑了 3 次）

### 2. 🖥️ 基础设施快照
- 服务器：westd-19828，工作目录 `/root/distrib_canary_collapse/`
- Python：conda base 环境（aml-train 镜像），`/root/miniconda3/bin/python`
- 训练脚本：`iterative_train.py`（含 `--synthetic_ratio` α 参数 + `--accumulate` 模式 + EXIT_CODE sentinel）
- 子采样已修复：L117/L122 为 `.shuffle(seed=seed).select(range(N))`
- 活跃进程：
  - alpha_sweep_a000_s42: PID 46721, cuda:0, α=0.0, ~Gen 5-6/10, 预计 ~1.5h
  - alpha_sweep_a025_s42_v3: PID 53074, cuda:1, α=0.25, ~Gen 0/10, 预计 ~4h
- Cron：两个实验均有 PID-based cron 监控
- 结果目录：`results/alpha_sweep/a{000,025}_s42/`，MVP 数据在 `results/mvp/`
- 分析产出：`artifacts/` 下有 `ccf_maxlag7_report.md`, `method_ablation_report.md`, `dmax_sensitivity_report.md`

### 3. 📊 当前状态
**刚完成**：plan_002 Phase 1 全部分析（method ablation + d_max sensitivity），导致 Claim 3 从 "TY 纠正 naive" 重构为 "方法选择敏感性"（D013）。a025 数据损坏修复完毕（v3 干净重启）。

**RUNNING**：
- alpha_sweep_a000_s42 (cuda:0, α=0.0 null control)
- alpha_sweep_a025_s42_v3 (cuda:1, α=0.25)

**排队序列**（完成即提交下一个）：
- cuda:0: a000_s42 → a000_s43 → a000_s44 → a050_s42 → a050_s43 → a050_s44 → plan_006_s42
- cuda:1: a025_s42_v3 → a025_s43 → a025_s44 → a075_s42 → a075_s43 → a075_s44 → plan_006_s43

**等待中**：
- Dream dream_20260514T184925 pending（full review mode），完成后会注入 session
- Agent 正在处理 GPU 状态检查 + d_max sensitivity 分析指令（队列中）
- α-sweep 聚合分析脚本 Worker 准备中

### 4. 📋 待办（条件触发式）
- a000_s42 完成 → 收集 metrics + 立即 submit a000_s43，α=0.0 控制组数据可提前做 partial analysis
- a025_s42_v3 完成 → 收集 metrics + submit a025_s43，这是首个用修复代码跑的 α<1.0 结果
- Dream 回调 `[DREAM dream_20260514T184925]` → Read `dream-report-action.skill.md` 按协议处理（注意：Dream 基于旧 framing，D013 重构后部分建议可能过时）
- α-sweep 首批 4 个 α 各 1 seed 完成 → 初步 phase diagram + 方法 ablation Phase 2（pooled panel TY）
- plan_006 排到时 → 提交 20-gen extended run，分析时必须加 rolling-window（gen 5-20 子序列）排除初始跳变 artifact
- d_max sensitivity 分析 Worker 回调 → 验证结果与 Reviewer 审查一致（预期 token_entropy→distinct_1 在 d_max=1 下仍显著或不显著，决定论文呈现方式）

### 5. 🎯 战略上下文
**项目**: 映射迭代合成数据训练中 canary 指标的可预测性边界。Target AAAI 2027 (~Aug 2026)。

**决策链**（关键节点）：
- D006: Framing = "Delineating Predictability Boundaries"
- D009: MVP 4-seed STRONG PASS，进入 Research 阶段
- D010: plan_003 修正 perplexity 通道叙述——"弱信号"非"断裂"，ECE→perplexity 反向因果
- D011-D012: plan_002 Phase 1 — 75% 伪回归率但 TY d_max 在 N=11 下不稳定，ECE 降为 secondary canary
- D013: **最重要** — d_max sensitivity 证实 TY 在 N=11 下完全失效 → Claim 3 重构为"方法选择敏感性"（更强贡献）

**最容易判断错的事**：
1. **不要把 TY 当 ground truth**——这是 D011→D13 的核心教训。Claim 1 证据链是多方法一致性，不是 TY 背书
2. **Claim 3 的自引用张力**——"方法不可靠"和"我们的结论可信"之间需要显式论证"多方法收敛 ≠ 单方法可靠"，已加入 Anticipated Reviewer Concerns 但论文写作时容易遗漏
3. **plan_006 是 framing 判定实验**——如果 N=21 下 token_entropy→perplexity 多方法一致显著，narrative 从 "canary only predicts diversity" 升级为 "dual lead horizons"；如果不显著，当前 framing 不变。不要提前按升级后的 framing 写论文
4. **ECE 地位未定**——secondary canary 待 plan_006 确认，不要在论文中过早定性
5. **experiment_plan.yaml 刚同步过**——plan_002 加了 registry_id，plan_003 修了格式，plan_006 升 P0


---
