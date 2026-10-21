# agent / loop_12.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_12.md`
- **Structured JSON:** [`85149e59d860b6e377a8.json`](../../sessions/85/85149e59d860b6e377a8.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: max_wall_time
updated: '2026-05-15T18:59:23+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westb-13313 的 cuda:0 和 cuda:1，不得使用其他设备
- DAF 口径：论文中只能用 aggregate DAF=90.41%（0.9041），禁止混入 weighted DAF=0.9614（plan-005 分析指标，仅限内部报告）
- plan-006-deep-internal registry conclusion 已改为 **negative**（Director 指令，D065: 2-way vs 3-way 无显著差异）
- plan-008 系列已 **killed**（D058，3 次失败），不要重试
- 论文数据源：主文只引 plan-012-full（11 tasks / 245 eps），prescreening 30-task 数据仅 appendix
- seed-robustness-extended 实验必须与 seed-robustness-core 完全一致的训练配置（implicit_router_sft.py 原版，不改代码）

### 2. 🖥️ 基础设施快照
- 服务器：westb-13313，账号 root，2× RTX 5090
- 工作目录：/root/autodl-tmp/simgate-modular-routing/
- Python：/root/miniconda3/bin/python（aml-train 镜像，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- 训练脚本：src/implicit_router_sft.py
- 数据：data/plan-004-implicit/implicit_sft.jsonl（2040 samples）
- Episode 数据：results/plan-012-full/（245 episodes, 11 tasks）
- plan-005 图表：服务器 artifacts/ 下 routing_heatmap.pdf, phase_heatmap.pdf, daf_scatter.pdf
- 活跃进程：无（plan-010-v2 训练 PID 516250/516604 已完成）

### 3. 📊 当前状态
**刚完成**：
- experiment_plan.yaml 元数据同步（5 项 plan 的 registry_id/status/conclusion 更新）
- plan-005 routing pattern analysis（success，3 张图 + failure taxonomy）
- plan-010-cross-task-v2（negative，CI bug 已修复）
- 僵尸 Worker worker_exp_plan-010-cross-task-v2 已 cancel

**等待中**：
- Worker `worker_exp_seed-robustness-extended_20260515T185804`：**pending_approval**（飞书审批卡已发）— seeds 46-49，cuda:0+cuda:1
- Worker `worker_analysis_penalty-sensitivity-curve_20260515T185824`：**running** — DAF vs penalty curve 分析（P=0,10,25,50,100,200,500）
- 用户审批 continue review → Round 8 启动（外部阻塞）

**Registry 活跃实验**：全部 DONE（69 个），无 RUNNING/ALLOCATED

### 4. 📋 待办
- seed-robustness-extended 审批通过 → Worker 自动启动训练（GPU0: seeds 46,47; GPU1: seeds 48,49）→ 完成后合并 8-seed 统计，更新 registry
- penalty-sensitivity-curve Worker 回调 → 注册 artifact（penalty_vs_daf.pdf）→ 汇报 Director → 结果直接回应 R6-C1
- 两项 Worker 都完成后 → 派 Paper Worker 同时处理：(a) §4.5 加 deep-internal ablation 1-2 句, (b) §4.4 整合 plan-005 图表, (c) Discussion 加 plan-010-v2 negative 1 句
- 用户审批 continue review → Round 8 启动 → Round 8 报告返回后按 review-report-action 处理
- Round 8 如有新 critical issue → 可能需要补实验（GPU 空闲可用）

### 5. 🎯 战略上下文
- **核心结论**：death avoidance 占 routing signal ~90%（C1），episode-level counterfactual labeling 是方法论贡献（C2 降级为 preliminary observation）
- **DDL**：EMNLP 2026 ARR 5/25，剩 10 天。关键路径：Round 8 审批 → 审稿 → 修复 → 终稿
- **覆盖率**：C1 83.3%, C1+C2 100%, C2 20%（但 C2 降级后 plan-002 success 足够）
- **R6-C1 是最大风险**：从 R4 起每轮 resurface，DAF penalty-dependence 质疑。penalty-sensitivity-curve 正在计算，是最直接防御。论文已用 death-asymmetry label fraction 78.9% 作为 penalty-independent 补充指标
- **易错点**：(1) 0.9614 vs 0.9041 口径混淆——0.9614 是 weighted DAF（plan-005），0.9041 是 aggregate DAF（plan-012-full），论文只用后者; (2) docs/paper/ 和 artifacts/_project/paper/latex/ 是两套 tex，docs/paper/ 是较新版本（有 penalty sensitivity 讨论）; (3) seed-robustness 的 implicit_router_sft.py 曾被修改过（ga 8→1 导致 plan-008 系列全部失败），必须确认用的是 .bak 恢复后的正确版本


---
