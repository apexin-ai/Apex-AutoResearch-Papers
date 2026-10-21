# reviewer / loop_3.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_3.md`
- **Structured JSON:** [`caab6182891c1f59365a.json`](../../sessions/ca/caab6182891c1f59365a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-05-14T03:47:23+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：cuda:0 + cuda:1（2× RTX 5090 32GB），项目独占，无越界风险但必须核实每次提交
- GPU0 连续 4 次进程异常终止（v2 vLLM crash → v3 被 cleanup worker 误杀 → v4 崩溃 → v5 当前运行中）。审查 GPU0 实验时**必须独立核实进程存活**，不信 registry status
- Agent 的 cleanup worker 有误杀活跃进程的前科（v3 的 PID 544942 被当僵尸杀掉，实际在跑 ep15-18；gpu1-extra 被 SIGHUP）。审查时如果看到进程被标为"僵尸/未启动"，**先 stat 输出文件 mtime + 检查 CPU 使用率**再下结论
- `episode_level_collection.py` 不加 `--start_episode` 会从 ep 0 追加写，已发生过数据重复。审查新实验必查是否带 `--start_episode` 或 `--reuse_dirs`
- constraints.yaml 和 experiment_matrix.yaml 均未创建（标记 ⚠️），无法做约束/覆盖度自动审查

### 2. 🖥️ 基础设施快照
- 服务器：westb-13313(root)，工作目录 `/root/autodl-tmp/simgate-modular-routing`
- Python：`/root/miniconda3/bin/python`（conda base 环境，非 venv）
- 模型：Qwen2.5-7B-Instruct，路径 `/root/autodl-tmp/models/Qwen/Qwen2___5-7B-Instruct/`，vLLM 推理
- 数据：`results/plan_c/`（plan-001b 全量收集），`results/prescreening/`（5 ep/task 预筛），`results/research/`（MVP 阶段）
- 权威分析源：`results/death_decomposition_report.json`（30 tasks / 249 eps 预分析，aggregate: Δ_full=38.33, Δ_nd=0.48, DAF=0.9875, r=0.9864）
- W&B：未配置（不检查 W&B）
- 活跃进程（截至 handoff）：
  - GPU0: gpu0-v5 PID 698985 (python) + 699929 (vLLM)，运行 ~1h，做 measure-melting-point 20eps + lifespan-longest-lived ep19
  - GPU1: freeze-chem PID 788063 (python) + 789051 (vLLM)，运行 ~33min，做 freeze+chemistry-mix 各 20eps。Registry 仍 PREPARING 未更新为 RUNNING

### 3. 📊 当前状态
**刚完成**：
- Introduction v4 审查通过（Overall 7，R2 全部 warning 修复确认）
- Method v1 审查（Overall 4，5 个 warning：τ 阈值代码中不存在、249 vs 600 算术矛盾、prescreening 描述误导、deterministic 未操作性定义、priority ordering 不准确）
- fnlt-v2 完成确认（40 eps，0% 死亡率，success）
- gpu0-v4 数据重复发现→Agent 已清理→gpu0-v5 重启
- gpu0-v3 进程误杀发现并报告

**RUNNING/PREPARING**：
- `plan-001b-gpu0-v5` (RUNNING): measure-melting-point 20eps + lifespan-longest-lived ep19，GPU0，~1h 运行中，measure-melting-point 已 17/20 eps
- `plan-001b-gpu1-freeze-chem` (PREPARING but actually RUNNING): freeze+chemistry-mix 各 20eps，GPU1，~33min，registry 未更新
- 无等待中的 Worker 回调或 Director 决策

### 4. 📋 待办（条件触发式）
- gpu0-v5 完成通知 → 核实 measure-melting-point 20 eps + lifespan-longest-lived ep19 数据完整性，特别关注 measure-melting-point 的 DAF（预分析 59%，是论文关键异常值，20 eps 全量数据可能改变）
- gpu1-freeze-chem 完成通知 → 核实 freeze + chemistry-mix 各 20 eps，检查是否有 prescreening 数据需合并
- 两个 GPU 实验全部完成 → plan-001b 全量数据就绪，decomposition 应重跑最终版。核实最终 DAF/Δ_full/r 是否与 PLACEHOLDER 一致，不一致需通知 Director 更新论文数字
- Method v2 提交 → 复审 5 个 warning 是否修复（最关键：τ 删除/定义、249→600 统一、deterministic 操作性定义）
- Director 转发 Framing 提案 → Read negative-framing-review skill 后按四维度审
- 任何实验结束 → 独立 nvidia-smi 验证无越界进程（L1 #4）

### 5. 🎯 战略上下文
- **核心结论**：Death avoidance ≈ 99% routing signal（D013 framing pivot）。论文是 empirical finding paper，不是 router 架构 paper
- **决策链**：D008 (1-step fail) → D010 (episode-level) → D011 (safety-aware) → D013 (death avoidance dominance pivot) → D015 (r=0.989 确认) → D016 (find-non-living-thing 翻转评估) → D017 (C1 Tier B claim)
- **易判断错的事**：
  1. GPU 利用率 0% ≠ 进程 stuck。ScienceWorld 交互式 agent 的 GPU 是 bursty 的（7B 模型毫秒级推理，大部分时间 CPU 侧环境交互）。判断进程活跃看**文件 mtime**，不看 nvidia-smi utilization
  2. registry 数字和 report.json 数字有差异（registry: 37.9/0.2/0.989 vs JSON: 38.33/0.48/0.9864）。论文应以 JSON 为准。paper_framing.md 已更新但 registry 未改
  3. Agent 的 gpu0-v3 notes 说"从未启动"是错的——实际跑了 ep15-18。不要信 Agent 对历史事件的描述，核实时读文件/进程状态
  4. "25 of 30 DAF ≥ 95%" 已用 per-task 数据验证正确。5 个 outlier：find-non-living-thing (DAF=-0.0), grow-plant (null), find-living-thing (0.89), find-plant (0.94), measure-melting-point-unknown (0.59)
  5. death_aware_labeling.py 实际用 strict equality（τ=0），不存在 threshold 超参。Method 写了 τ 但代码没有——这是 R1 审查发现，等 Method v2 修复


---
