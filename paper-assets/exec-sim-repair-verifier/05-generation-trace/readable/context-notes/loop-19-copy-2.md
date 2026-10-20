# agent / loop_19.md

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_19.md`
- **Structured JSON:** [`3d7cf4dce5006a672abb.json`](../../sessions/3d/3d7cf4dce5006a672abb.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 19
reason: idle_timeout
updated: '2026-05-16T02:12:58+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单: cuda:0/1/2/3 on seetacloud-westd-4x5090。home-1x5090 (sonny) 也可用但当前无 GPU 分配信息
- eval 禁止 `--max_samples`，必须评完整 test set (n=9784) / val set (n=9335)，否则与主表不可比
- 标 FAILED/DONE 前必须 `ps -p PID` 确认进程已退出（D085 事故教训：误标导致同 GPU OOM）
- CWM 8B val-best = ckpt-400（eval_loss 单调递增，无歧义），不要做 val sweep
- s42 resume checkpoints 从 ckpt-600 开始（`/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/`），不含 200/400
- `save_total_limit=5` 会删旧 checkpoint，提交 eval 前必须 `ls checkpoint-*` 确认存在
- 主表数字已锁定（D088），不要重跑已有结果

### 2. 🖥️ 基础设施快照
- **Westd**: seetacloud-westd-4x5090, account=root, workdir=/home/sonny/exec-sim-repair-verifier
  - Python: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
  - 8B 模型: `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/`
  - CLS 8B s42 resume ckpts: `/root/autodl-tmp/checkpoints_repo_cls_8b_s42_resume/`
  - CLS 8B seed123 backup: `/root/autodl-tmp/checkpoints_backup_cls_8b_seed123/checkpoint-3000/`
  - CWM 8B ckpts: `/root/autodl-tmp/checkpoints_repo_cwm_8b_conda/`
  - CWM 8B eval 脚本: `eval_repo_cwm.py`（不是 eval_repo_cls.py），max_new_tokens=1024, bs=1
  - CLS 8B eval 脚本: `eval_repo_cls.py`, max_new_tokens=8, bs=1, seq=8192
- **Home**: home-1x5090, account=sonny, workdir=/home/sonny/exec-sim-repair-verifier
  - 4B v5 ckpts: `/home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_v5/`
  - home 版 eval_repo_cls.py **不支持 --max_new_tokens**
- **活跃进程**: cwm8b-ckpt400-test-eval-v3 (PID 443221, cron 监控中, ~57% done)
- **Running Workers**: 0

### 3. 📊 当前状态
- **CWM 8B test eval (ckpt-400)** 是唯一仍在跑的实验 (cwm8b-ckpt400-test-eval-v3, pid=443221)，约 57% 完成。这是锁定 8B-8B gap 的最后一个数据点。
- Report 提到 cls8b-s42-resume-ckpt3600-test-v2、cwm8b-ckpt400-test-eval-shard2、cls8b-seed123-ckpt3000-mutation 为 running，但 registry 中未见 RUNNING 状态实验。cron reconcile 仅确认 cwm8b-ckpt400-test-eval-v3 在跑。**接手后优先 SSH 确认这些进程是否存活。**
- 主表 CLS 侧全部锁定：8B s42 test=84.48%, 8B seed123 test=85.60%, 4B s42 test=83.63%
- CWM 4B 已完成：s42=58.04%, seed123=59.09%
- 三个 claims (C1/C2/C3) 已确认，进入 Paper Writing 阶段
- DDL: **EMNLP 2026 ARR May 25（剩 9 天）**

### 4. 📋 待办（条件触发式）
- cwm8b-ckpt400-test-eval-v3 cron 回调到达 → 读 test accuracy + unparseable rate → 更新 registry + ROADMAP 主表 CWM 8B 行 → 计算 8B-8B gap → 汇报 Director
- CWM 8B test accuracy 出来后 → 若 <60%，gap >24pp，直接用；若异常高（>70%），检查 eval 是否有 bug
- CWM 8B unparseable rate 出来后 → 对比 4B 的 53.7%/67.2%，判断 8B 是否改善 → 影响 failure modes §2.3 claim 强度
- cls8b-seed123-ckpt3000-mutation 结果到达 → 对比 s42 的 boundary_removal=46.9%，验证跨 seed 一致性
- 所有 eval 完成 → cuda:0-3 全部空闲 → 向 Director 汇报资源释放 + 论文写作全力冲刺
- Paper Writing: intro/related/conclusion + figures 待完成（需 Director 分配 Worker）

### 5. 🎯 战略上下文
- **核心结论**: CLS reformulation 在 repo-level 上以 ~26pp gap 碾压 CWM，multi-seed 验证一致（s42: 26.44pp, seed123: 26.51pp）。TOST p=0.007 确认统计显著。
- **决策链**: D088(val-selected ckpt) → D093(multi-seed 锁定) → D094(seq_length confound 排除) → D095(审稿 action matrix) → D096(8B-8B 主表) → D097(rank ablation 完成) → D100(CWM relaxed matching 排除) → D102(CWM 8B bs=8 加速) → D103(seq8192 统一)
- **最容易判断错的事**: (1) registry 中很多 PREPARING 状态的实验实际已完成或 killed，notes 里有真实状态——不要被 status 字段误导。(2) report.md 里 "running" 的实验可能已经不在跑了，以 cron reconcile + SSH ps 为准。(3) CWM 8B eval 极慢（~37s/sample, SDPA），不要尝试加速或重启，让它跑完。
- **boundary_removal 46.9%** 是论文 discussion 的重要 failure mode。待 seed123 mutation 和 CWM 8B mutation 对比后决定 narrative 角度。
- **4B seed123 test=75.33% 是已知 negative**（D096 已处理），论文主表只用 4B s42，不用 4B seed123。


---
