# agent / loop_4.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_4.md`
- **Structured JSON:** [`dc0569b4d8f0d7504787.json`](../../sessions/dc/dc0569b4d8f0d7504787.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: idle_timeout
updated: '2026-05-14T08:10:03+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-39279 的 cuda:0 和 cuda:1，禁止用其他卡
- 训练日志 ISR 是 binary approximation (_fast_fn)，**禁止用于论文或跨实验对比**——所有 checkpoint 必须用 eval_sta.py (full STA) 重新评估真实 ISR（D013/D015）
- plan013 random reward 的 held-out ISR=0.535 是 tautological artifact（trivial 2-component proofs），不是真实结构质量（D018）
- checkpoint 路径注意：save_total_limit=1 时模型直接保存在 output_dir 根目录，不在 checkpoint-500 子目录（plan014 首次失败的教训）
- ISR 定位已明确为 syntactic component necessity metric，不是 semantic faithfulness（D019/D021/D022），downstream NLI 验证已降级为 limitation/future work

### 2. 🖥️ 基础设施快照
- 服务器：westd-39279，账号 root，2× RTX PRO 6000 96GB
- 环境：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，Python `/root/miniconda3/bin/python3`
- 项目路径：`/root/solver-trace-ablation`
- 模型：`/root/autodl-tmp/models/Qwen3-4B`
- 数据：训练 `data/train_500_seed42.jsonl` (500条)，eval `data/proofwriter_fol_100.jsonl` (100条)
- 输出根：`/root/autodl-tmp/outputs/`
- 活跃进程：plan017-additive-random-s42 (PID 207116, cuda:1, tmux session)，有 cron 监控
- Worker 活跃：`worker_analysis_plan001-exec-only-s44_20260514T050751`（正在分析 s44 日志 + 跑 eval_sta.py）

### 3. 📊 当前状态
**刚发生**：plan001-exec-only-s44 (exec-only seed=44, 第3 seed) 训练完成，cron 已转 ANALYZING。我派了 Worker 去读训练日志 + 运行 eval_sta.py，**该 Worker 尚未回调**。

**Registry 关键状态**：
- `plan001-exec-only-s44` — ANALYZING，cuda:0，Worker 正在分析
- `plan017-additive-random-s42` — RUNNING，cuda:1，additive random control 实验（隔离 ISR signal vs variance regularization）

**已完成关键实验的 eval_sta 真实指标**：
- plan001-s42-r2 (exec-only): eval PR=93%, ISR=0.1232, proved-only ISR=0.1324
- plan001-s43-r4 (exec-only): eval PR=14%, ISR=0（退化，87% hit max_new_tokens）
- plan013-r4 (random reward): eval PR=100%, ISR=0.535（但是 tautological artifact）
- plan002 (additive β=0.3): eval PR=18%, ISR=0.0257（negative）
- plan014 (downstream NLI): negative，Spearman ρ=-0.049

**总计**：29 实验，success 6 / negative 7 / failed 14

### 4. 📋 待办（条件触发式）
- Worker s44 分析回调到达 → 根据 eval PR 判断：若 PR≥80% 则 success（与 s42 一致），若 PR<30% 则 negative（与 s43 一致）→ update_registry 转 DONE → 更新 report.md → 汇报 Director 含 3-seed mean±std
- plan017-additive-random-s42 cron 完成回调 → 派 Worker 分析日志 + eval_sta.py → 与 plan002 (additive ISR) 对比：若 ISR(additive ISR) > ISR(additive random) → ISR signal 有结构价值；若 ≈ → ISR 无结构价值
- s44 + plan017 都出结果 → 汇总完整 ISR 对比表（exec-only 3-seed mean、additive ISR、additive random、random reward）→ 向 Director 汇报 narrative 判断
- cuda:0 在 s44 eval 完成后空闲 → 检查 experiment_plan.yaml 排下一个实验（plan015 curriculum / plan016 extended training / plan006 Prolog）

### 5. 🎯 战略上下文
- **DDL 2026-05-25（剩 11 天）**，Dream 审稿进行中，best 4/6 Borderline Reject
- **Framing 已转向**（D010/D011）：从 "STA detects hacking" → "STA as diagnostic metric + additive bonus integration"
- **核心 confound**（D014）：GRPO 500步后 random reward 也能饱和 prove_rate → 论文论证必须聚焦 ISR 差异而非 prove_rate 差异
- **plan002 additive ISR 已 negative**（D020）：β=0.3 additive bonus PR=18%/ISR=0.0257，远差于 exec-only。这意味着 ISR 作为 reward component 可能干扰训练。plan017 additive random 是关键对照——如果 random 也同样差，说明是 additive 公式本身的问题而非 ISR 特有
- **跨 seed 不稳定是核心风险**：s42 PR=93% vs s43 PR=14%，s44 是 tiebreaker。如果 s44 也退化，3-seed mean 会很低（~40%），exec-only baseline 可靠性受质疑
- **易错点**：不要把训练日志里的 ISR 当真实 ISR 用（binary approximation）；不要把 plan013 的 ISR=0.535 当成 random reward 真的有结构质量（tautological proof artifact）


---
