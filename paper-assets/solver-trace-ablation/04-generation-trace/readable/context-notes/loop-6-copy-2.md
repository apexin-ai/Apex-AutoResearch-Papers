# agent / loop_6.md

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_6.md`
- **Structured JSON:** [`0240c0d9e1745642a5b1.json`](../../sessions/02/0240c0d9e1745642a5b1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: idle_timeout
updated: '2026-05-14T14:25:21+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 **只有 westd-39279:cuda:0 和 cuda:1**。submit_training_job 的 gpu 参数永远从 0 开始（框架映射物理 GPU）
- submit_training_job 命令必须 `bash -c "export CUDA_VISIBLE_DEVICES=N && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 ..."`——tmux 用 sh，source 是 bash built-in
- 训练数据约束 C001：所有 FOL 实验统一 `train_500_seed42.jsonl`，不用 `proofwriter_fol_500.jsonl`
- 磁盘约束 C003：`log_completions=False` + `save_total_limit=1`，output_dir 放 `/root/autodl-tmp/outputs/`。之前发生过 250G 爆满事故
- plan013 vs plan017 公式结构不同（convex vs additive），不可简化为 "additive vs convex" 对照（D027）
- β=0.1 三 seed 已出：s42 genuine、s43/s44 conclusion duplication artifact。**不可报 raw 3-seed mean ISR**（被膨胀值污染），需按 hacking mode 分层报告

### 2. 🖥️ 基础设施快照
- **服务器**: westd-39279，account=root，2× RTX PRO 6000 Blackwell 94GB
- **工作目录**: `/root/solver-trace-ablation/`
- **Python**: conda 环境，激活命令 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **CUDA**: 12.8, PyTorch 2.10.0+cu128, transformers/trl/vllm/accelerate 预装
- **Solvers**: Prover9 (LADR 2009-11A 编译), SWI-Prolog 8.4.2 (`/usr/bin/swipl`), Z3 4.16.0.0
- **模型**: Qwen3-4B（7.6GB，ModelScope 下载）
- **磁盘**: 系统盘 30GB (~22G free)，数据盘 `/root/autodl-tmp/` 250GB (~199G free)
- **活跃进程**:
  - plan006-prolog-exec-s44: PID 479357, cuda:0, cron 监控中
  - plan006-prolog-exec-s43-r3: PID 483820, cuda:1, cron 监控中
- **活跃 crons**: 2 个，分别监控上述两个实验

### 3. 📊 当前状态

**刚完成的关键事项**：
- plan009-sft-baseline-s42-r4: **DONE (success)** — SFT baseline PR=14%, ISR=0.08, 无 hacking patterns。对照 GRPO exec-only PR=93%/ISR=0.123，证明 hacking 是 GRPO RL 特异性而非通用 finetuning artifact
- plan018-additive-random-b01-s44: **ANALYZING** — 训练完成，有 running worker (`worker_eval_plan018-random-b01-s44`) 正在跑 eval

**RUNNING（cron 监控中）**:
| exp_id | GPU | PID | 说明 |
|--------|-----|-----|------|
| plan006-prolog-exec-s44 | cuda:0 | 479357 | Prolog exec-only seed=44，第三 seed for Claim 3 |
| plan006-prolog-exec-s43-r3 | cuda:1 | 483820 | Prolog exec-only seed=43 r3 (warmup_ratio=0.0 对齐 s42) |

**等待中**:
- plan018-additive-random-b01-s43-r2: QUEUED，等 GPU 释放（random β=0.1 s43 控制组 r2）
- plan006-prolog-sta-s43/s44: PREPARING，Prolog exec+STA 多 seed（数据就绪，等 GPU）

**Running workers**: worker_eval_plan018-random-b01-s44, worker_read_eval-results-check

### 4. 📋 待办（条件触发式）
- **plan018-s44 eval worker 返回** → 更新 registry metrics + 与 plan002-b01-s44 (ISR β=0.1 s44) 对比 → 更新 report.md → 汇报 Director
- **plan006-prolog-exec-s43-r3 cron 回调(DONE)** → spawn eval worker 跑 `eval_sta.py` Prolog eval → 对比 s42 (PR=83%, ISR=0.031) → 更新 registry
- **plan006-prolog-exec-s44 cron 回调(DONE)** → 同上 eval → 三 seed Prolog exec-only 出齐后做统计汇总
- **Prolog exec-only 3 seed 全部出齐** → 汇报 Director Claim 3 证据链 + 是否启动 prolog-sta s43/s44
- **plan006 两个实验完成释放 GPU** → 立即提交 plan018-random-b01-s43-r2 (QUEUED) + plan006-prolog-sta（按优先级排）
- **3-seed random β=0.1 全部出齐 (s42+s43+s44)** → 3-seed mean±std ISR vs random 定稿数据 → Table 1 + Table 2 可写

### 5. 🎯 战略上下文
- **DDL**: EMNLP ARR 2026-05-25，剩 11 天，GPU budget 充裕 (528 GPU·h available, ~12h needed)
- **论文核心**：Goodhart 主线诊断/分析论文。3 Claims: (1) ISR 作为 hacking 诊断工具, (2) ISR-as-reward 展现 meta-level Goodhart (D043 pivot 后: β=0.1 2/3 seeds gaming ISR 本身), (3) 跨 logic type 泛化
- **Claim 2 已 pivot (D041/D043)**：从 "ISR sweet spot" 转为 "meta-Goodhart"——ISR β=0.1 只有 1/3 seed genuine，2/3 通过 conclusion duplication 膨胀 ISR。ISR 作为 reward 不可靠，核心价值在诊断
- **SFT baseline 刚出 (plan009-r4)**：PR=14% (vs GRPO 93%)，无 hacking。这是 "hacking is GRPO-specific" 的关键证据，**尚未写入 paper_framing.md 和 ROADMAP.md**，下一轮应更新
- **最易判断错的事**：(1) 不要把 s43/s44 的高 ISR (0.83/0.90) 当 genuine improvement——那是 conclusion duplication artifact (D042/D043)。(2) Prolog exec+STA 的 50% eval PR 里有一半是格式解析错误，不是策略差异。(3) plan013 (convex random) 和 plan017 (additive random) 公式不同，不可直接对比
- **决策链关键节点**: D010(reward公式转向) → D031(β=0.1 random control 紧急) → D038(taxonomy 足够跳过 LLM-judge) → D041(Claim 2 pivot to meta-Goodhart) → D043(β=0.1 叙事降级) → D044(strict hacking 定义) → D045(跨 logic Goodhart 确认)


---
