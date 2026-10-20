# agent / loop_20.md

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_20.md`
- **Structured JSON:** [`4630f5528367dd36d6cf.json`](../../sessions/46/4630f5528367dd36d6cf.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 20
reason: idle_timeout
updated: '2026-05-19T10:42:14+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westb-13313 cuda:0, cuda:1（仅两张）。westd-18266 的 GPU 未在 gpu_ids 白名单中，之前用 cuda:0/1/2 跑 reflexion-dose-response-n345 是经 Director 特批的一次性操作，不可作为先例
- westb-14838 已死（GPU driver dead），不要往上面提交任何任务
- 实验都是数据收集（data collection），不是模型训练——没有 checkpoint 要保存，核心产出是 results/ 目录下的 JSON 数据文件
- DDL 2026-05-25（EMNLP 2026 ARR），剩 ~6 天，所有操作围绕论文冲刺

### 2. 🖥️ 基础设施快照
- **westb-13313**：2× RTX 5090，工作目录 `/root/autodl-tmp/simgate-modular-routing/`
  - 模型：`/root/autodl-tmp/models/Qwen/Qwen2.5-7B-Instruct`
  - vLLM 服务方式运行推理
  - Reflexion N=1 (DR=47.5%), N=2 (DR=40.0%) 数据在 `/root/autodl-tmp/simgate-modular-routing/results/reflexion_dose_response/`
  - Retry dose-response 数据在 `/root/autodl-tmp/simgate-modular-routing/results/retry_dose_response/`
- **westd-18266**：4× RTX PRO 6000 96GB，工作目录 `/root/autodl-tmp/simgate-modular-routing/`
  - Reflexion N=3/4/5 数据在 `/root/autodl-tmp/simgate-modular-routing/results/reflexion_dose_response/`
  - 日志：`/root/autodl-tmp/simgate-modular-routing/logs/reflexion_n3.log`（也查 n4, n5）
- 活跃进程：无（实验刚完成，无 RUNNING）
- Worker 在跑：`worker_analysis_reflexion-dose-response-n345_20260518T182923`（分析 Worker，刚派出）

### 3. 📊 当前状态
**刚做完**：收到 `reflexion-dose-response-n345` 的 cron 完成回调（进程正常退出，状态 ANALYZING）。已完成 session-start 初始化（read_registry + reconcile_crons + report.md + ROADMAP）。

**正在做**：已派 Worker（`worker_analysis_reflexion-dose-response-n345_20260518T182923`）SSH 到 westd-18266 分析 N=3/4/5 结果数据，计算 death rate，与 N=1/2 合并建立完整曲线。**Worker 回调尚未到达**。

**Registry 状态**：
- `reflexion-dose-response-n345`: ANALYZING — 等 Worker 分析完推进到 DONE
- 其他 106 个实验全部 DONE（success 43, negative 28, failed 14, killed 20）

**资源**：GPU 2/2 分配但 0 在跑（westb-13313 cuda:0/1 空闲）。Worker 池 1（CPU 任务）。

### 4. 📋 待办（条件触发式）
- **Worker 回调到达（reflexion-dose-response-n345 分析完成）→**：
  1. 读 Worker 产出的分析报告，提取 N=3/4/5 death rates
  2. 判断 conclusion（大概率 success：验证 plateau）
  3. `update_registry` 写入 metrics（death_rate_n3/n4/n5）、conclusion、checkpoint_path、log_path
  4. `register_artifact` 注册分析报告
  5. 合并完整曲线：Reflexion N=1(47.5%)→N=2(40.0%)→N=3(?)→N=4(?)→N=5(?) vs Retry N=1(51.2%)→N=3(40.9%)→N=5(43.5%)
  6. 向 Director 汇报（带 [资源] 行），附完整 dose-response 对比表
  7. 更新 report.md

- **分析确认 plateau →** 推进 ROADMAP 中的下一步：
  - P3 Dose-response 可视化（retry flat vs reflexion curve）— 派 Worker 画图
  - W2 72B matched 10-task DAF comparison
  - W3 1.7B per-class confusion matrix
  - W4 Per-task death rate differential CIs
  - 这些都可并行派 Worker

- **westb-13313 cuda:0/1 空闲 →** 分析完后评估是否有需要跑的实验，或用于 W2-W4 分析任务（这些是 CPU+API 任务，不一定需要 GPU）

### 5. 🎯 战略上下文
- **核心结论**：Episode-level counterfactual diagnostic framework 发现 78.9% routing labels 由 death asymmetry 驱动（penalty-independent）。Agent improvement baselines（reflexion/retry/72B）均确认 death dominance 是结构性现象，有收敛上限。
- **证据三角形**：7B baseline DR=51.2% → Retry plateau ~40-43% → Reflexion plateau ~35% → 72B DR=34.5% → Deterministic DR=16.3%。gap = 34.5% - 16.3% = 18.2pp 是不可逾越的结构性上限。
- **论文评分轨迹**：R13=2.5 → R24=7/10 (3.5 Borderline Conference)。目标 ≥3.5 冲 Conference。
- **易错点**：
  - Reflexion N=1/N=2 数据在 westb-13313，N=3/4/5 数据在 westd-18266，合并时注意数据源一致性（同 seed=42，同 10 个 death-prone tasks）
  - `reflexion-dose-response`（killed）不是 failed——它的 N=1/N=2 数据有效，只是 N=3+ 被 kill 让位给并行版
  - retry-dose-response 的 death rates 是 all-task aggregate（包含 non-death-prone），reflexion 的可能是 death-prone only——对比时确认口径一致
  - westd-18266 不在 gpu_ids 白名单，后续不要假设可以继续在上面提交实验


---
