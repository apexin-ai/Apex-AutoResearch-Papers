# agent / loop_17.md

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_17.md`
- **Structured JSON:** [`b0a719186c323bbca031.json`](../../sessions/b0/b0a719186c323bbca031.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 17
reason: idle_timeout
updated: '2026-05-21T21:04:10+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-11235:cuda:0, westd-11235:cuda:1，禁止用其他 GPU
- EMNLP ARR DDL 2026-05-25（4 天），论文已 pre-submission PASS，不要启动新方向实验
- DeepSeek VOTA seed42=84.45% 是已确认 outlier（seed123=99.16%, seed456=99.33% 仲裁），报告时必须排除，写 "99.25±0.12% (2s, excl seed42 outlier)"
- Qwen-1.5B 实验命名用 `qwen15b_*`（不是 `qwen1.5b_*`），QUEUED 里的 `qwen1.5b_*` 是旧命名
- westd-11235 根分区 100% 满，提交新实验前必须先清理磁盘

### 2. 🖥️ 基础设施快照
- 服务器：westd-11235，工作目录 /root/trace-verdict-study
- Python：/root/miniconda3/bin/python（conda base），激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型：/root/autodl-tmp/models/（Qwen2.5-Coder-1.5B-Instruct, Qwen2.5-Coder-7B-Instruct, deepseek-coder-6.7b-instruct, CodeLlama-13b-Instruct-hf）
- 数据：/root/autodl-tmp/trace-verdict-study-data/
- Checkpoint：/root/autodl-tmp/trace-verdict-study-checkpoints/
- HF_HOME：/root/autodl-tmp/.hf_cache
- wandb project：trace-verdict-study
- 活跃进程：无（两张 GPU 均空闲）
- 活跃 cron：无（reconcile_crons 返回 0）

### 3. 📊 当前状态
项目处于投稿等待状态。所有核心实验完成（109 success），论文 pre-submission Reviewer PASS（0 critical, 0 warning）。

- RUNNING/ANALYZING：无
- ALLOCATED：qwen1.5b_no_trace_seed42（等 GPU 释放 + 磁盘清理）
- QUEUED：6 个 rebuttal 储备（qwen1.5b_full_trace/no_trace/vota/exception_only + codellama_no_trace/vota/exception_only，均 seed42）
- PREPARING：3 个（qwen15b_label_only_seed42, codellama13b_label_only_seed42, deepseek_exception_only_seed123）

等待中：无 Worker 回调、无 cron 回调、无 Director 决策。已向 Director 汇报 Session #17 启动状态，询问是否推进 rebuttal 储备。

### 4. 📋 待办（条件触发式）
- Director 指示推进 rebuttal 储备 → 先派 Worker 清理磁盘根分区 → 提交 qwen1.5b_no_trace_seed42（已 ALLOCATED）
- Director 指示维持现状 → 等用户 scp PDF + 视觉检查 + resubmit
- 用户确认 PDF 视觉无问题 → 论文可提交
- 磁盘清理完成 → 可按优先级依次提交 QUEUED 实验（rebuttal 储备，不阻塞投稿）

### 5. 🎯 战略上下文
- 核心结论：Information density determines learning efficiency for trace-based verdict prediction。4 Core Claims 全部强证据（C1 ★★★★★, C2 ★★★★, C3 ★★★★★, C4 ★★★★）
- 当前阶段是收尾投稿，不是探索。QUEUED 实验全是 rebuttal 储备，DDL 前优先保证论文提交
- 关键决策链：D100（C4 Option C wording）、D103-D104（DeepSeek VOTA outlier 仲裁）、D107（全 Claims 强证据达成）、D108（C2 维持 ★★★★）
- 易错点：不要为了跑完 QUEUED 而拖延投稿；codellama13b_label_only_seed123_v2 的 conclusion=success 实际是 collapsed（registry 标注 accuracy='collapsed'），不要当作正常 success 引用
- loop_only 是 Tier 2 信号，variance 最大（跨模型 76-86%），多 seed 数据：CL-13B 3-seed (77.06/86.39/79.08), Qwen-1.5B 2-seed (78.32/81.09)，是 reviewer 最可能挑战的点


---
