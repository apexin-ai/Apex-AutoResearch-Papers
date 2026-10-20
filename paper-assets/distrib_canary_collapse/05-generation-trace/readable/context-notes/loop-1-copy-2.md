# agent / loop_1.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`111e41ef248b2e757053.json`](../../sessions/11/111e41ef248b2e757053.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-14T14:51:17+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器名是 `westd-19828`，不是 `autodl-rtx6000`。submit_training_job 必须用 `westd-19828`，否则 GPU 检测失败返回 "Available: []"
- GPU 白名单：cuda:0, cuda:1（仅两卡）
- rep44 是 nohup 启动的（非 submit_training_job），没有 cron 监控。完成后不会自动回调，需要手动 SSH 检查或 Monitor 轮询
- 2-seed STRONG PASS 是 **PRELIMINARY**，不可作为最终结论。必须等 rep44 完成跑 3-seed 分析才出正式 verdict
- **Narrative 约束**：canary 仅 lead distinct_n (diversity)，不能 lead perplexity (quality)。论文 claim 范围受限，Director 已确认。Research 阶段需低 synthetic ratio (0.3/0.5) 重新验证

### 2. 🖥️ 基础设施快照
- 服务器：westd-19828，工作目录 `/root/autodl-tmp/distrib_canary_collapse`
- Python：`/root/miniconda3/bin/python`（conda base，Python 3.12.3，PyTorch 2.10.0+cu128）
- 环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 数据：`/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k`（5000 prompts）
- HF cache：`/root/autodl-tmp/.hf_cache`，HF_ENDPOINT=`https://hf-mirror.com`
- 模型：EleutherAI/pythia-410m（从 HF mirror 下载，已缓存）
- 活跃进程：
  - rep44: PID 30672, cuda:0, nohup 启动, log `~/runs/distrib_canary_collapse/mvp_v4_rep44.log`
  - rep45: PID 31425, cuda:1, tmux=mvp_v4_rep45, log `~/runs/distrib_canary_collapse/mvp_v4_rep45.log`
- analyze_mvp.py 已同步到服务器（含 6 项评估检查的升级版）

### 3. 📊 当前状态
刚完成 Reviewer 反馈处理：registry 全部修正（server→westd-19828, 状态同步）、report.md 刷新、memory.md 记录 narrative 约束。

Registry 活跃实验：
- **mvp_v4_rep44**: RUNNING, seed=44, cuda:0, ~Gen 2-3/10（启动约 30 min 前）
- **mvp_v4_rep45**: RUNNING, seed=45, cuda:1, ~Gen 0/10（刚启动）
- **mvp_v4_rep42**: DONE(success), 10 gen 完成, ppl 26.9→1003.7
- **mvp_v4_rep43**: DONE(success), 10 gen 完成, ppl 26.9→1014.7

2-seed 预分析已跑完：STRONG PASS（ECE + token_entropy 各有 SIGNIFICANT LEAD against distinct_n）。

无等待中的 Worker 回调。rep45 有 cron 监控，rep44 没有（nohup）。

### 4. 📋 待办
- rep44 完成（检查 `results/mvp/rep_44/all_metrics.json` 存在）→ 立即跑 `analyze_mvp.py --seeds 42 43 44 --n_permutations 10000`，出 3-seed 正式 verdict，汇报 Director
- rep45 cron 回调 / 完成 → 追加 `analyze_mvp.py --seeds 42 43 44 45`，4-seed 稳健性验证
- 3-seed verdict = PASS 或更好 → 按 on-experiment-done skill 走 success 分支：更新 report.md、与 experiment-matrix 对标、文献联动、反思实验计划、向 Director 汇报下一步（synthetic ratio sweep）
- 3-seed verdict = FAIL → 走 negative 分支：red-section framing 调整提案
- Director 可能指示进入 Research 阶段 → 需要设计 synthetic ratio gradient 实验 (0.3/0.5/0.7/1.0)

### 5. 🎯 战略上下文
- 核心发现：ECE 和 token_entropy 是有效 canary，但**仅对 diversity collapse (distinct_n)**，不对 quality collapse (perplexity)。100% SC 下 perplexity 上升太快（37x），canary 与 perplexity 几乎同步
- 这意味着论文 story 需要聚焦 "diversity collapse early warning"，而非 "general model degradation prediction"。低 synthetic ratio 实验可能改变这个结论
- MAUVE 在本 setup 下完全不可用（floor effect, Gen 0=0.034），已 demote。effective_rank 非单调（先升后降），标记 inconclusive。self_bleu 变化太小无效
- 最近竞争者 chen2025scales 做了 ECE-as-canary 但没做 lead-lag 因果分析——我们的 Granger causality 方法论是核心 novelty 壁垒
- 易错点：(1) 不要用 `autodl-rtx6000` 提交 job (2) 不要把 2-seed 结果当最终结论 (3) rep44 没有 cron，需要手动检查完成状态 (4) `pgrep -a iterative_train` 匹配不到进程，用 `nvidia-smi` 或 `ps aux | grep python`


---
