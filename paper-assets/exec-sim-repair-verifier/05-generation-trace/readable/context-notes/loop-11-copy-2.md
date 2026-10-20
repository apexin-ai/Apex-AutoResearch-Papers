# agent / loop_11.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_11.md`
- **Structured JSON:** [`2549b049a36f2ccccc33.json`](../../sessions/25/2549b049a36f2ccccc33.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: idle_timeout
updated: '2026-05-14T19:35:53+00:00'
---

### 1. 🔴 硬约束 / 红线
- **GPU 白名单**: 只能用 `cuda:0, cuda:1, cuda:2, cuda:3`（westd 4x5090）。home-1x5090 只有 `cuda:0`。违规用其他卡会被 CRITICAL
- **D063 方法论红线**: checkpoint 选择**必须在 val set (9335 samples) 上做**，test set (9784) 只报最终数字。之前所有 repo-level CLS checkpoint sweep 都在 test set 上做的，属于 cherry-picking，论文数字需全部在 val set 上重新验证
- **Apple-to-apple 比较**: CLS vs CWM 必须用 westd conda 数据（同 server/env/data），不能跨 server 比
- **eval_repo_cls.py 的 max_seq_length 陷阱**: 该脚本硬编码 default=2048，不像 verifier/cwm 那样自动按 split 切换。val 评估必须手动传 `--max_seq_length 8192`，否则截断严重（D077 教训）
- **8B 训练用 num_workers=0**: D072/D073 教训，DataLoader 子进程会被平台 SIGTERM 误杀导致崩溃
- **CWM 8B v3 已 FAILED (EXIT_CODE=2)**: 脚本名错误。实际 CWM 8B 训练可能通过 PID 266816 在跑（出现在 v3 failure_reason 里），但未被 registry 正式追踪——**必须 SSH 确认 cuda:2 上实际在跑什么**

### 2. 🖥️ 基础设施快照
- **westd** (seetacloud-westd-4x5090, root): 工作目录 `/home/sonny/exec-sim-repair-verifier`
  - Python: `/root/miniconda3/bin/python`（conda base 环境，不用 venv）
  - 模型: Qwen3-4B/8B（HF cache 或本地 checkpoint）
  - Checkpoints:
    - CLS 8B seed42: `checkpoints_repo_cls_8b_conda/` (200, 400, 600 — 完成)
    - CLS 8B seed123: `checkpoints_repo_cls_8b_seed123_conda/` (200, 1800-3000 — 训练中)
    - CWM 8B: `checkpoints_repo_cwm_8b_conda/` (400-1600 — 训练中/状态不明)
    - CWM 4B v12: `checkpoints_repo_cwm_conda_v12/` (300-700)
    - CWM 4B seed123: `checkpoints_repo_cwm_seed123_conda/` (200-600)
- **home** (home-1x5090, sonny): 工作目录同路径，有 CLS v5/seed123 4B checkpoints
- **GPU 分布 (ROADMAP 记录, 需 SSH 确认)**:
  - westd cuda:0: CWM seed123 eval (~25%, ETA ~02:30 UTC May 15)
  - westd cuda:1: CWM v12 eval (~25%, ETA ~02:20 UTC May 15)
  - westd cuda:2: 8B CWM 训练 (PID 210568? 或 266816? — 状态不明, v3 FAILED)
  - westd cuda:3: 8B CLS seed123 训练 (PID 266444, tmux: repo-level-cls-8b-seed123-conda)
- **活跃 Cron**: 0（reconcile 返回空）
- **活跃 Worker**: 0（最近 20 个全部 done/cancelled）

### 3. 📊 当前状态
**刚发生的事**: 上一个 session 在处理大量 8B 训练崩溃和重启（D070-D079），经历了 v1→v2→v3 三次重启周期（CLS 8B seed123 和 CWM 8B 都是）。根因是 DataLoader num_workers>0 被平台误杀 + resume checkpoint 路径写错。

**Registry RUNNING (3 条，但有脏数据)**:
1. `repo-level-cls-8b-seed123-conda-v3` — westd cuda:3, PID 266444 (可能是真的在跑)
2. `repo-level-cls-8b-seed123-conda-v2` — 大概率是被 v3 supersede 的残留条目
3. `repo-level-cwm-8b-conda-v2` — 大概率是残留条目; v3 已 FAILED, 实际 cuda:2 上跑的进程未被 registry 追踪

**⚠️ 第一优先级**: SSH 到 westd 确认 cuda:2 和 cuda:3 上实际在跑什么进程。Registry 和实际可能严重脱节。清理 v2 stale entries，确认 CWM 8B 是否还在训练。

**等待中的关键事件**:
- CWM v12 全量 eval 完成 (westd cuda:1, ETA ~02:20 UTC May 15) → 解除 D057 论文阻塞
- CWM seed123 全量 eval 完成 (westd cuda:0, ETA ~02:30 UTC May 15) → paired bootstrap
- 8B 训练完成 → 启动 8B eval pipeline

**总览**: 成功 36 / 负向 3 / 失败 16 / 共 65

### 4. 📋 待办（条件触发式）
- **立即** → SSH westd 确认 4 张 GPU 实际进程，修正 registry 脏数据（v2 stale entries）
- CWM v12 eval 完成 → 提取 accuracy/F1，与 CLS 对比算 repo-level gap（C1 核心数据），更新 ROADMAP 和 report.md，汇报 Director
- CWM seed123 eval 完成 → paired bootstrap with CWM v12 → 统计显著性
- CWM v12 + seed123 都完成 → D057 论文阻塞解除，可以开始 paper number finalization
- **D063 val sweep 条件满足**（home cuda:0 空闲）→ 对所有 CLS 4B checkpoints 跑 val set sweep → 选 best checkpoint → test set 最终 eval。注意 eval_repo_cls.py 需手动传 `--max_seq_length 8192`
- CLS 8B seed123 训练完成（cuda:3）→ 8B multi-seed eval pipeline
- CWM 8B 训练完成/确认状态（cuda:2）→ 8B CWM eval pipeline
- **所有 eval 完成** → val set 选 checkpoint → test set 最终数字 → Paper Agent patch → 提交前 reference-audit
- **如果 CWM 8B 训练实际已死** → 立即从最新 checkpoint resume，不要等

### 5. 🎯 战略上下文
**核心结论链**: D001(MVP) → D004(P2P~1%, reframe) → D007(CWM≈CLS on function-level, adopt Complexity-Dependent Advantage) → D008(repo-level go/no-go: ≥3pp full push) → D057(论文阻塞等 CWM v12 全量 eval)

**项目核心 story**: Classification 和 Generation 在简单函数级代码上等效 (~87% F1)，但 classification 随复杂度增加优势显现。Repo-level 4B gap 已约 ~18pp (CLS 78.43% vs CWM ~58%)。8B CLS seed42 = 84.52%。CWM 的失败模式是 token exhaustion + string prediction。

**最容易判断错的事**:
1. **Registry 里 RUNNING 不等于真的在跑** — 这个项目经历了大量重启，v2 条目很可能是 stale。必须 SSH 确认
2. **ROADMAP 里的 checkpoint sweep 数字全在 test set 上** — 不能直接用于论文，需 val set 重做
3. **CWM 8B 状态最混乱** — v1 failed, v2 "RUNNING"(可能 stale), v3 failed(EXIT_CODE=2), 有个 PID 266816 出现在 v3 failure_reason 里但没注册。务必先搞清楚这个
4. **DDL 紧张**: EMNLP ARR May 25，剩 11 天。CWM eval 还有 ~8h，8B 训练不知道还要多久，val sweep 还没开始。时间线可行但零余量
5. **不要碰论文** — D063 val sweep 没做完之前，paper 里的 repo-level 数字全是 test-set cherry-picked 的，改了也白改


---
