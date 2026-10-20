# agent / loop_16.md

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_16.md`
- **Structured JSON:** [`e34bb00b13d22c21f236.json`](../../sessions/e3/e34bb00b13d22c21f236.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 16
reason: idle_timeout
updated: '2026-05-21T04:59:26+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：westd-11235:cuda:0, westd-11235:cuda:1，禁止用其他 GPU
- EMNLP ARR DDL 2026-05-25（4 天），论文已进入最终审稿准备阶段，不要启动新方向实验
- DeepSeek VOTA seed42=84.45% 是已确认的 outlier（seed123=99.16%, seed456=99.33% 仲裁），报告时必须排除，写 "99.25±0.12% (2s, excl seed42 outlier)"
- Qwen-1.5B 实验命名用 `qwen15b_*`（不是 `qwen1.5b_*`），QUEUED 里的 `qwen1.5b_*` 是旧命名，提交时注意保持一致

### 2. 🖥️ 基础设施快照
- 服务器：westd-11235，工作目录 /root/trace-verdict-study
- Python：/root/miniconda3/bin/python（conda base 环境），激活命令 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型路径：/root/autodl-tmp/models/（Qwen2.5-Coder-1.5B-Instruct, Qwen2.5-Coder-7B-Instruct, deepseek-coder-6.7b-instruct, CodeLlama-13b-Instruct-hf）
- 数据路径：/root/autodl-tmp/trace-verdict-study-data/（各 condition 的 train/test jsonl）
- Checkpoint 路径：/root/autodl-tmp/trace-verdict-study-checkpoints/
- HF_HOME：/root/autodl-tmp/.hf_cache
- wandb project：trace-verdict-study
- 活跃进程：codellama13b_loop_only_seed456（PID 609613, cuda:0, RUNNING）
- 活跃 cron：codellama13b_loop_only_seed456 监控中

### 3. 📊 当前状态
**刚做完**：收到 qwen15b_loop_only_seed123 完成回调，将其状态从 PREPARING 补推到 ANALYZING，已派 Worker（worker_analysis_qwen15b_loop_only_seed123_20260520T124327）SSH 读取 eval 结果并分析。

**正在等**：
- Worker 回调：qwen15b_loop_only_seed123 分析 Worker（读 eval_results.json、更新 registry metrics、写分析报告、设 conclusion）
- Worker 回调：paper:final_sync_compile_urgent（论文最终 sync + compile）
- Cron 回调：codellama13b_loop_only_seed456（CL-13B loop_only 第 3 seed，cuda:0 RUNNING）

**Registry 摘要**：
- RUNNING：无（qwen15b_loop_only_seed123 在 ANALYZING）
- ANALYZING：qwen15b_loop_only_seed123（等 Worker 结果）
- codellama13b_loop_only_seed456 cron 显示仍在跑（PID 609613）但 registry 可能还是旧状态
- QUEUED：6 个（qwen1.5b_full_trace/no_trace/vota/exception_only + codellama_no_trace/vota/exception_only 各 seed42）—— 均为 rebuttal 储备
- ALLOCATED：qwen1.5b_no_trace_seed42（等 GPU 释放）

### 4. 📋 待办（条件触发式）
- qwen15b_loop_only_seed123 分析 Worker 回调 → 读 conclusion，按 on-experiment-done 处理（success 则更新 report.md + 计算 1.5B loop_only 2-seed mean±std + 汇报 Director；negative 则走证伪推导）
- codellama13b_loop_only_seed456 cron 回调 → 派分析 Worker，完成后 CL-13B loop_only 有 3-seed 数据，更新 MF2 表格
- 两个 loop_only seed 实验都完成后 → cuda:0 和 cuda:1 释放，可提交 QUEUED 中的下一批实验（优先 qwen1.5b_no_trace_seed42 已 ALLOCATED）
- paper final_sync_compile Worker 回调 → 检查编译结果，确认论文可提交状态
- DDL 前（05-25）→ 确保最终论文 PDF 编译通过 + 所有 Core Claims 证据表更新

### 5. 🎯 战略上下文
- 项目核心结论：Information density determines learning efficiency for trace-based verdict prediction。4 个 Core Claims 全部有强证据（C1 ★★★★★, C2 ★★★★, C3 ★★★★★, C4 ★★★★）
- 当前阶段是论文最终审稿准备 + 收尾 seed 实验（loop_only 跨 seed 稳定性数据），不是探索新方向
- loop_only 是 Tier 2 信号，variance 最大（跨模型 76-86%），是 reviewer 最可能挑战的点。多 seed 数据越多越好
- 易错点：QUEUED 里的实验是 rebuttal 储备（不是必须跑完才能投稿），DDL 前优先保证论文 compile + 提交，不要为了跑完所有 QUEUED 而拖延提交
- 决策链关键节点：D100（C4 wording 采纳 Option C）、D103-D104（DeepSeek VOTA outlier 仲裁）、D107（全 Core Claims 强证据达成）


---
