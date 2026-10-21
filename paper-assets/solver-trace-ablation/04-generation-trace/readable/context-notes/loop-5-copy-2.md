# agent / loop_5.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_5.md`
- **Structured JSON:** [`abe66074e6df7e0a46da.json`](../../sessions/ab/abe66074e6df7e0a46da.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: idle_timeout
updated: '2026-05-14T11:15:36+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单严格限 `westd-39279:cuda:0` 和 `westd-39279:cuda:1`，不可用其他设备
- 所有训练数据统一用 `data/train_500_seed42.jsonl`（C001），不用 `proofwriter_fol_500.jsonl`
- 所有命令必须 `export CUDA_VISIBLE_DEVICES=N`，在 `bash -c` 内部 export
- `log_completions=False` + `save_total_limit=1`，output_dir 放 `/root/autodl-tmp/outputs/`（C003 磁盘约束）
- plan002-b01 三 seed ISR 被 H7 conclusion duplication 膨胀（s43 96.7%、s44 86.5% H7），**不可报 raw 3-seed mean ISR**，必须按 hacking mode 分层报告（D043）
- plan013 vs plan017 公式结构不同，不可简化为 "additive vs convex" 对照（D027）
- Prolog 训练数据路径是 `data/train_500_seed42.jsonl`（与 FOL 相同），**不是** `data/prolog/train_500_seed42.jsonl`（前两次失败教训）

### 2. 🖥️ 基础设施快照
- **服务器**: westd-39279, root@, 2× RTX PRO 6000 Blackwell 94GB
- **工作目录**: `/root/solver-trace-ablation/`
- **Python**: `/root/miniconda3/bin/python`（conda base 环境，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- **CUDA**: 12.8, PyTorch 2.10.0+cu128
- **模型**: Qwen3-4B（通过 ModelScope 下载，已就绪）
- **Solvers**: Prover9 (LADR 2009-11A), SWI-Prolog 8.4.2 (`/usr/bin/swipl`), Z3 4.16.0.0
- **输出目录**: `/root/autodl-tmp/outputs/`
- **磁盘**: 系统盘 22G free, 数据盘 `/root/autodl-tmp/` 142G free
- **活跃进程**: plan006-prolog-exec-s42 PID=506015, cuda:0, cron 监控中
- **活跃 Workers**: `worker_code_plan009-sft-setup` (running), `worker_code_plan009-sft-oom-fix` (running) — 两个 Worker 在处理 plan009 SFT baseline 的 OOM 问题

### 3. 📊 当前状态

**刚完成的**:
- plan002-b01-s43/s44: DONE(negative) — β=0.1 多 seed 验证，2/3 seeds 是 H7 conclusion duplication，ISR "sweet spot" 叙事已降级（D041/D043）
- plan006-prolog-sta-s42: DONE(negative) — 100% H7，Prolog Goodhart 比 FOL 更极端
- plan009-sft-baseline-s42-r2: DONE(failed) — SFT baseline 失败，原因未详查
- Hacking taxonomy 全面校准为 strict 定义（D044）

**RUNNING**:
- `plan006-prolog-exec-s42`: cuda:0, PID 506015, step ~361/500, Prolog exec-only baseline。cron 监控中，预计很快完成

**PREPARING** (4个，全部等 GPU):
- plan006-prolog-exec-s43, plan006-prolog-exec-s44: Prolog exec-only 多 seed
- plan006-prolog-sta-s43, plan006-prolog-sta-s44: Prolog exec+STA 多 seed

**QUEUED** (2个，等 GPU):
- plan018-additive-random-b01-s43/s44: ISR vs random 多 seed 控制组

**PENDING** (1个):
- plan009-sft-baseline-s42: 等人工审批（之前 killed 因为用了错误模型 Qwen2.5-1.5B）

**Workers**: 两个正在跑（plan009 SFT setup + OOM fix），等 WORKER DONE 回调

**cuda:1 当前空闲** — plan009-sft-baseline-s42-r2 已失败，Worker 正在修 OOM。修好后应立即重提交占满 cuda:1

### 4. 📋 待办（条件触发式）
- plan006-prolog-exec-s42 cron 回调（ANALYZING/DONE）→ spawn Worker 跑 eval_sta.py，与 plan006-prolog-sta-s42 对照分析，更新 registry + report.md，汇报 Director
- Worker plan009-sft-oom-fix DONE → 检查修复方案，重新提交 plan009 SFT 到 cuda:1
- plan009 SFT 成功 → eval hacking taxonomy，与 GRPO exec-only 对比，判断 hacking 是否 GRPO-specific
- plan006-prolog-exec-s42 完成释放 cuda:0 → 立即提交 plan006-prolog-exec-s43（或 plan018-random-s43，取决于优先级）
- 3-seed Prolog 数据全出 → 写 Claim 3 跨 logic type 段落
- plan018-random s43/s44 出结果 → 验证 ISR 3.2x > random 跨 seed 稳健性

### 5. 🎯 战略上下文

**DDL: 2026-05-25 ARR（剩 11 天），时间充裕但不能浪费。**

**核心 narrative（Goodhart 主线，D035）**: ISR 作为 neurosymbolic verification reward 的诊断工具 + Goodhart's Law 案例研究。三个 Claims：(1) ISR 检测 reward hacking，(2) ISR-as-reward 展现 meta-level Goodhart（低剂量 mode shift + 高剂量 collapse），(3) 跨 logic type 泛化。

**关键判断点**:
- Claim 2 已经从 "ISR sweet spot" 降级为 "ISR changes hacking composition, not total rate"（D041/D043）。s42 是唯一 genuine seed，s43/s44 都是 H7 膨胀。**不要试图恢复 sweet spot 叙事**
- plan006 Prolog exec-only 是 Claim 3 的关键数据点——如果 exec-only 也出现 hacking，则 STA 诊断跨 logic type 成立；如果 exec-only 健康，则 Prolog Goodhart 更极端的结论需要重新框架
- plan009 SFT baseline 已失败两次——如果 OOM 修不好，可能需要换更小 batch size 或 gradient accumulation，不要放弃这个实验（Reviewer 会问 "is this GRPO-specific?"）

**易踩的坑**:
- Prolog 训练数据不在 `data/prolog/` 下（前两次就是这个路径错了）
- plan018-random-b01-s43 虽然 QUEUED 且有 spec（含 PID 540905），但实际可能已失败——ROADMAP 说它等 GPU，registry 却有提交记录，需要验证进程状态
- ISR 数值在 s43/s44 看起来很高（0.83/0.90）但实际是 H7 膨胀 artifact，**绝不能当 positive 结果报**


---
