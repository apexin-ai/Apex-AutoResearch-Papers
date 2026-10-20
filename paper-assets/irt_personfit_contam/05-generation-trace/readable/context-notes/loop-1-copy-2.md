# agent / loop_1.md

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`bfff13a3ddacba22d4d9.json`](../../sessions/bf/bfff13a3ddacba22d4d9.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: idle_timeout
updated: '2026-05-21T11:13:53+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-35694 cuda:0/1/2/3（4 张 RTX PRO 6000 Blackwell 96GB），不得使用白名单外 GPU
- exp-ctrl-contam-pilot 的 4 个子实验（clean-s1/s2/contam-15/contam-50）registry 状态卡在 PREPARING，它们已合并到父实验 exp-ctrl-contam-pilot (DONE/success) 中，不要再试图推进这些子条目
- θ-fixed 分析中 θ_fixed = clean seeds 均值（目前 -0.0914 基于 s1/s2），clean_s3 结果出来后必须更新为 3-seed 均值
- ctrl-contam-pilot 结论是 partial（H1✓ H2✓ H3✗theta-free/✓theta-fixed H4✗），论文叙事必须走 θ-fixed 路线，不能只报 θ-free

### 2. 🖥️ 基础设施快照
- 服务器：westd-35694，工作目录 /root/autodl-tmp/ctrl_contam_pilot/
- Python：/root/miniconda3/bin/python（conda base），激活命令 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型 checkpoint：/root/autodl-tmp/ctrl_contam_pilot/checkpoints/{clean_s1,clean_s2,clean_s3,contam_15,contam_50}/
- 训练数据：/root/autodl-tmp/ctrl_contam_pilot/data/{condition}/train.jsonl
- Eval 数据：mmlu_items.json + mmlu_params.csv（4PL IRT 参数）
- 结果目录：/root/autodl-tmp/ctrl_contam_pilot/results/
- Log 目录：/root/runs/irt_personfit_contam/
- 磁盘充裕：根分区 97% 可用，autodl-pub 76% 可用
- 活跃进程：无（clean_s3 训练已完成，PID 29341 已退出）
- 活跃 Worker：worker_analysis_exp-ctrl-contam-pilot-clean-s3_20260520T191151（正在分析 clean_s3 结果，尚未回调）

### 3. 📊 当前状态
**刚做完**：收到 exp-ctrl-contam-pilot-clean-s3 的 cron 完成回调（进程正常退出），已将 registry 状态推进到 ANALYZING，已派 Worker 去 SSH 读日志 + 提取 eval 指标 + 计算 3-seed baseline。

**等待中**：
- Worker `worker_analysis_exp-ctrl-contam-pilot-clean-s3_20260520T191151` 回调——它会产出 clean_s3 的 lz*、accuracy、θ，以及更新后的 3-seed Cohen's d
- 无其他 RUNNING 实验，4 张 GPU 全空闲

**Registry 关键状态**：
- exp-ctrl-contam-pilot-clean-s3: ANALYZING（等 Worker 分析）
- exp-ctrl-contam-pilot: DONE/success（主实验，4 条件完整结果）
- 其余 20 个实验: 全部 DONE（14 success, 6 negative）
- 4 个子实验 (clean-s1/s2/contam-15/contam-50): PREPARING（遗留条目，已合并到父实验）

### 4. 📋 待办
- Worker clean_s3 分析回调 → 更新 registry metrics（lz*, accuracy, θ）→ 更新 3-seed baseline（mean/std）→ 重算 Cohen's d → 设 conclusion=success → 更新 report.md → 向 Director 汇报
- clean_s3 分析完成 → ROADMAP 说"clean_s3 完成后即可启动论文写作"→ 向 Director 请示启动 Paper Agent
- GPU 0-3 全空闲 → 向 Director 汇报资源状态，询问是否需要跑 exp-ctrl-contam (full) 或 exp-baseline-comparison，或释放 GPU
- 如果 Director 批准写论文 → Read paper-writing-norms skill + paper-plan skill → spawn Paper Agent Worker

### 5. 🎯 战略上下文
**项目核心**：用 IRT person-fit statistic (lz*) 做 LLM benchmark contamination detection，优势是 minimal-information（只需二值响应向量 + IRT 参数，不需训练数据或模型权重）。

**关键决策链**：
- D008: empirical null 校准良好，95% flagging 是真实信号不是 miscalibration
- D010: Leaderboard audit 降级为描述性，ctrl-contam 升为核心实验
- D011: v1-irt-refit NEGATIVE（a_r=0.127），Path D dead，Claim 3 走 PSN-IRT case study
- D014: Claim 结构重组——universal misfit 从 Claim 1 移至 Claim 3
- D015: ctrl-contam-pilot partial，θ-fixed 恢复单调性（ratio=2.93），这是论文的核心卖点

**易错点**：
- θ-shift 是本项目最微妙的发现——contamination 提升 θ → 吸收 lz* 信号 → theta-free 下 dose-response 非单调。论文必须把 θ-fixed 分析作为方法论贡献讲清楚，不能当作 limitation 处理
- Dream 模拟审稿 best=3.5/median=3.0，写作质量直接决定能否冲 4.0
- ARR Jun 15 cycle 是目标 DDL，时间紧
- seen/unseen split (lz*≈0 vs 3.1) 是最清晰的 contamination 指纹，论文要突出


---
