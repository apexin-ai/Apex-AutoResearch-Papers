# agent / loop_13.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_13.md`
- **Structured JSON:** [`92cc50695117b6c20c47.json`](../../sessions/92/92cc50695117b6c20c47.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: idle_timeout
updated: '2026-05-15T01:56:41+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单: westd cuda:0/1/2/3 + home cuda:0。**不得用白名单外 GPU**
- **D088 约束**: checkpoint 选择必须在 val set (9335 samples) 上做，test set (9784) 只报最终数字。违反此规则的数字不可引用（D080 已废掉旧 ckpt-3000 89.50%）
- `checkpoints_repo_cls_8b/checkpoint-3000` 是 transformers 5.x 旧训练产物（peft 0.19.1），**不可使用**。合法 s42 checkpoint 在 `/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/`，seed123 在 `/root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/`
- eval_repo_cls.py 已内置 `enable_thinking=False`，但 home 服务器上 4B eval 仍会卡死（原因未查明，Worker 正在排查）。Home 上跑 eval 需监控是否 hang
- CLS 和 CWM 必须 apple-to-apple 对比：同 server (westd) / 同 conda env / 同数据

### 2. 🖥️ 基础设施快照
- **westd** (seetacloud-westd-4x5090, account=root):
  - 工作目录: `/home/sonny/exec-sim-repair-verifier`
  - Python: `/root/miniconda3/bin/python`（conda base env，不是 venv）
  - 激活: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
  - 模型: `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/`
  - Checkpoints:
    - s42 resume: `/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/` (ckpt-800 ~ 1600+, 每 200 step 存)
    - seed123: `/root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/` (到 ckpt-5200+)
    - CWM 8B: `/root/autodl-tmp/checkpoints_repo_cwm_8b_conda/` (到 ckpt-2800)
  - 数据: `/home/sonny/exec-sim-repair-verifier/data/swebench_full/`
- **home** (home-1x5090, account=sonny):
  - 工作目录: `/home/sonny/exec-sim-repair-verifier`
  - Python: `python3`（系统 Python 或 venv）
  - 4B v5 ckpts: `/home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_v5/`
- **活跃进程 (westd)**:
  - PID 266444 (tmux, cuda:3): CLS 8B seed123 训练, step ~5351/6633
  - PID 266816 (tmux, cuda:2): CWM 8B 训练, step ~2815/6633
  - PID 295794 (tmux, cuda:1): CLS 8B s42 resume 训练, step ~1797/6633
  - PID 312975 (tmux, cuda:0): CLS 8B s42 ckpt-1000 test@8192 eval（~15min 剩余, running_acc=82.7%）
- **Cron 监控中**: repo-level-cls-8b-seed123-conda-v3, repo-level-cwm-8b-conda-v4, repo-level-cls-8b-s42-resume, cls8b-s42-ckpt1000-test8192-eval, cls4b-v5-ckpt4400-val5120-eval-v2 (已完成/killed)

### 3. 📊 当前状态
**刚完成**: D088 val-selected 策略确认后，启动了 ckpt-1000 test@8192 eval 和 4B val sweep pipeline。两个 Worker 正在排查 home 服务器 4B eval 卡死问题 + kill 之前卡住的 sweep 进程。

**RUNNING (5)**:
| exp_id | GPU | 进度 | ETA |
|--------|-----|------|-----|
| cls8b-s42-ckpt1000-test8192-eval | westd:0 | 27.6% (acc=82.7%) | ~15min |
| repo-level-cls-8b-s42-resume | westd:1 | 27.1% (step 1797) | ~10.9h |
| repo-level-cwm-8b-conda-v4 | westd:2 | 42.4% (step 2815) | ~8.5h |
| repo-level-cls-8b-seed123-conda-v3 | westd:3 | 80.7% (step 5351) | ~3h |
| cls4b-v5-val-sweep-ckpt4400 | home:0 | 刚启动 | 未知 |

**QUEUED (2)**: cls4b-v5-val-sweep-ckpt4200, ckpt4600（等 home:0 空出后接力）

**PREPARING (3 有效)**: cls8b-s42-ckpt1200/1400/1600-val8192-eval（等 westd:0 空出后逐个跑）

**等待中**:
- Worker `fix_home-4b-enable-thinking-rootcause` 回调 → 确认 home 4B eval 卡死根因
- Worker `fix_home-kill-sweep-relay` 回调 → 确认旧 sweep 进程已 kill
- cls8b-s42-ckpt1000-test8192-eval cron 回调 → 即将到达，分析 test 结果
- seed123 训练 ~3h 完成 → cron 回调后启动 seed123 val sweep

### 4. 📋 待办（条件触发式）
- **ckpt-1000 test eval 完成** → 记录 test accuracy/F1，与 val-best (88.23%) 对比确认 reversal 程度，更新 ROADMAP headline 数字，汇报 Director
- **seed123 训练完成 (~3h)** → spawn Worker 跑 seed123 val sweep (ckpt-3000~6633, step=200, val@8192)，确认 8B multi-seed val-best
- **CWM 8B 训练完成 (~8.5h)** → spawn Worker 跑 CWM 8B test eval，获得 8B-8B CLS-CWM gap 最终数字
- **s42 resume 训练完成 (~10.9h)** → 新 checkpoint (1800~6633) 全部加入 val sweep queue
- **cls4b-v5-val-sweep-ckpt4400 完成** → 接力跑 ckpt4200, ckpt4600; 三者完成后确定 4B val-best
- **val sweep 全部完成** → 汇总 val curve (8B s42 + 8B seed123 + 4B v5), val-selected checkpoint 最终确认, 跑对应 test@8192 获取 headline 数字
- **home 4B eval 卡死根因查明** → 如果是 CUDA hang，需换 batch_size/seq_len 或改到 westd 跑
- **所有 headline 数字锁定** → 派 Worker 更新论文数字 (paper agent patch)，填 repo-level 结果 + error analysis

### 5. 🎯 战略上下文
**核心结论**: Task reformulation (generation → classification) 在 repo-level 代码验证上优势巨大。CLS 4B=82.35%, CLS 8B val-best=88.23% (ckpt-1000), CWM 4B≈58%, 低于 majority baseline (72.96%)。C1 (complexity-dependent advantage) 极度稳固，24-26pp gap。

**DDL**: EMNLP ARR May 25，**剩余 10 天**。当前处于 Paper Number Finalization 阶段——所有实验方向已验证，只需锁定最终数字。

**关键决策链**:
- D088: 主指标 = val-selected checkpoint (ML 社区规范)
- D087: val-test 分布偏移已确认（repo 不匹配 + mutation type 偏移），在 supplementary 报告
- D082: CWM error analysis 完成，parseable-only acc 仅 42%，38% "正确"来自 unparseable 默认归类
- D063: checkpoint 选择必须在 val 上做，这是整个 number finalization 阶段的驱动决策

**易错点**:
- **不要把旧 `checkpoints_repo_cls_8b/` 路径和新 `checkpoints_repo_cls_8b_s42_resume/` 混淆**——前者已废弃
- **不要直接对比不同 max_seq_length 的 eval 结果**（4B val@5120 vs 8B val@8192 不能直接比）
- **val-test reversal 是已知现象**，不要因为 test 数字低于 val 就怀疑模型有问题
- **home 服务器 4B eval 会卡死**，原因未查明，spawn eval Worker 时必须设超时/监控
- resume 训练每 ~40min 出新 checkpoint，val sweep 队列需要动态追加新 checkpoint


---
