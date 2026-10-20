# reviewer / loop_6.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_6.md`
- **Structured JSON:** [`a3e94ad4fd49e21c7112.json`](../../sessions/a3/a3e94ad4fd49e21c7112.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_wall_time
updated: '2026-05-14T00:46:06+00:00'
---

### 1. 🔴 硬约束 / 红线
- **westd 上必须用 conda python**（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`），系统 python3.10 的 transformers 是 5.8.0，conda python3.12 的 transformers 是 4.57.6。之前 CWM v11 因混合版本导致 checkpoint 不可用（D055）。
- **home 上系统 python3.10 是正确的**（transformers 4.57.6），但 `.bashrc` 有非交互 guard 阻止 conda 初始化——tmux 启动的进程默认走 `/usr/bin/python3`，在 home 上这恰好是对的。
- **eval 脚本必须通过 wrapper 调用**：`run_repo_eval.sh` / `run_eval.sh` / `auto_eval_on_complete.sh`，不要裸调 `python3 eval_repo_*.py`（shebang 已改为 `/root/miniconda3/bin/python3`，但保险起见用 wrapper）。
- **D052 GO 判决的 CWM 数据 (v11) 已失效**——真实 repo-level CLS-CWM gap 取决于 CWM v12 结果，不要在审查中引用 "gap 10.3pp" 作为已验证事实。

### 2. 🖥️ 基础设施快照
- **westd**（seetacloud-westd-4x5090 = westd-48478，同一台机器）：root 账号，项目目录 `/home/sonny/exec-sim-repair-verifier`，conda python `/root/miniconda3/bin/python`，4×RTX 5090 (32GB each)
- **home**（home-1x5090）：sonny 账号，同一项目目录 `/home/sonny/exec-sim-repair-verifier`，系统 python `/usr/bin/python3`（3.10, transformers 4.57.6），1×RTX 5090
- **模型缓存**：westd `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-4B` 和 `Qwen3-8B`
- **数据**：`/home/sonny/exec-sim-repair-verifier/data/swebench_full/`（70748 训练样本，9784 测试）
- **活跃进程**（截至 handoff 时全部仍 RUNNING，预计 2026-05-14 09:30-14:00 完成）：
  - westd GPU 0: CWM seed123-conda (PID 183048, tmux=cwm_seed123)
  - westd GPU 1: CWM v12 seed42 (PID 181202, tmux 未记录)
  - westd GPU 2: CLS v5-conda seed42 (PID 187002, tmux=cls-v5-conda)
  - westd GPU 3: CLS 8b-conda seed42 (PID 185438, tmux=cls8b-conda)
  - home GPU 0: CLS seed123-home (PID 3001112, tmux 未记录)

### 3. 📊 当前状态
已完成的审查：
- 环境一致性全链路审计（D053→D054→D055），确认 5 个实验均使用正确 transformers 版本
- eval 管道审查：`run_repo_eval.sh`、`auto_eval_on_complete.sh` 创建完毕，conda 激活 + 环境验证已内置
- 实验矩阵覆盖率审查（含场景分析：CWM v12 好/中/差三种情况对 story 的影响）
- `all_experiments_parsed.json` 数据质量审查（发现 unparseable_pct 字段 bug + experiment_plan.yaml 不同步）

Registry: 5 个 RUNNING（上述），其余 54 个 DONE/FAILED/KILLED。
无等待中的 Worker 回调或 Cron。

### 4. 📋 待办（条件触发式）
- **5 个训练完成 → 审查 eval 结果**：重点是 CWM v12 的 accuracy 和 unparseable 率——这决定 C1 repo-level claim 的强度。CWM v12 若 <70% → C1 confirmed；73-77% → 需 bootstrap 判断显著性；>78% → 需提醒 Director 考虑 pivot。
- **CLS v5-conda eval 出结果 → 与 CLS v5 (home) 对比**：如果差异 >2pp，说明跨服务器有硬件差异，需在论文中 disclose。
- **CLS 8b-conda eval 出结果 → 与 CLS v5 4B 对比**：验证 repo-level scaling effect（function-level 8B 比 4B 高 2.43pp）。
- **paired bootstrap 完成 → 审查统计显著性**：检查 p-value、CI、TOST 是否合理。
- **Director 转发论文章节审查请求 → 按 §5 模板审查**（先查 Agent 是否看过 red-section skill）。
- **Director 转发 Framing 调整提案 → Read `negative-framing-review.skill.md` 后四维度审查**。

### 5. 🎯 战略上下文
- **核心决策链**：D046（超参修正）→ D049（并行训练布局）→ D052（D008 GO）→ D053（环境差异发现）→ D054（环境修复）→ D055（CWM v11 失效）
- **最容易判断错的事**：ROADMAP 说 "repo-level gap 10.3pp" 但这个数字基于已失效的 CWM v11。**不要**把它当已验证事实，CWM v12 才是真正的 apple-to-apple 数据点。
- **experiment_plan.yaml 不同步**：`per-test-precision-recall`、`block-corr-empirical`、`per-test-majority-voting` 在 plan 中显示 planned 但 registry 中已 DONE。用 registry 为准。
- **C2 的真正缺口是 `diagnostic-rerepair`**（P1, downstream proof-of-concept），不是 per-test-precision-recall（已完成）。paper_framing.md 允许将 rerepair 作为 future work。
- **ARR deadline 2026-05-25**，还有 11 天。训练今天完成 → eval 今天完成 → bootstrap + 论文 patch 可以 1-2 天内完成，时间充裕。


---
