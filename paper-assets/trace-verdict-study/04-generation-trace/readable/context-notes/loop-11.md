# agent / loop_11.md

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_11.md`
- **Structured JSON:** [`4261911bad17bbd526c3.json`](../../sessions/42/4261911bad17bbd526c3.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: idle_timeout
updated: '2026-05-16T11:10:29+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-11235 的 cuda:0 和 cuda:1（`get_project_resource_usage` 白名单）
- westd-11235 用 conda 环境（`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`），**不存在 .venv**
- DeepSeek 系列 eval 时 max_length 必须匹配训练值 2048，用 16384 会 OOD 崩溃（28.5%）——Qwen 不受影响
- 模型/数据/checkpoint 必须放 `/root/autodl-tmp/`，根分区只有 ~30GB
- HF_HOME 必须设 `/root/autodl-tmp/.hf_cache`
- ARR May 25 提交，距今 9 天，不能拖

### 2. 🖥️ 基础设施快照
- **服务器**: westd-11235，工作目录 `/root/trace-verdict-study`
- **Python**: `/root/miniconda3/bin/python`（conda base env）
- **模型路径**: `/root/autodl-tmp/models/Qwen2.5-Coder-7B-Instruct`、`Qwen2.5-Coder-1.5B-Instruct`、`DeepSeek-Coder-6.7B-Instruct`
- **Checkpoint**: `/root/autodl-tmp/trace-verdict-study-checkpoints/{exp_id}/final/`
- **W&B project**: `trace-verdict-study`
- **代码 commit**: `e404237ccc765768e267d4d6fd3c89549dcf41a4`
- **活跃进程**:
  - `loop_only_seed123`: PID 261213, tmux=loop_only_seed123, cuda:1, cron 监控中
  - `qwen15b_vota_seed42`: PID 265006, cuda:0, **已完成→ANALYZING**，on_complete hook 已触发（11:07 UTC），等你处理

### 3. 📊 当前状态
- **刚发生**: `qwen15b_vota_seed42`（Qwen-1.5B VOTA）训练+eval 完成，状态 ANALYZING，on_complete hook 已 fire。**下一个"你"第一件事就是处理这个回调**——spawn worker 读 eval 结果、更新 registry、汇报 Director。
- **仍在跑**: `loop_only_seed123`（cuda:1），seed robustness 验证，预计 ~1h 完成。
- **QUEUED (15)**:
  - CodeLlama-7B: vota/no_trace/exception_only（3 个，跨模型家族验证）
  - CodeLlama-13B: vota/no_trace/exception_only（3 个）
  - Qwen-1.5B: full_trace/vota/no_trace/exception_only（4 个，但 vota 正在 ANALYZING，exception_only 已 DONE 99.83%，no_trace 已 DONE 67.31%——registry 里有重复 exp_id 可能）
  - loop_only_seed456、exception_only_nomarker ×3（format marker ablation）
- **等待**: 无活跃 Worker 回调；qwen15b_vota_seed42 的 on_complete hook 等你处理
- **Paper 状态**: 初稿进行中，图表 fig2/fig3 已完成，trace_length_ablation 图和 fig1 绘制中。正文 13 页需压到 8 页。

### 4. 📋 待办（条件触发式）
- **立即**: qwen15b_vota_seed42 ANALYZING → spawn worker 读 `/root/autodl-tmp/trace-verdict-study-checkpoints/qwen15b_vota_seed42/final/eval_results.json` → 更新 registry → 汇报 Director → cuda:0 空出后提交下一个 QUEUED 实验
- loop_only_seed123 cron 回调到 → 读 eval 结果 → 更新 registry → cuda:1 空出后提交下一个 QUEUED 实验
- 两卡都空出后 → 按优先级提交 QUEUED（CodeLlama 跨家族 > nomarker ablation > 剩余 seed）
- Paper Agent patch 就绪 → regex baseline + DebugBench + 1.5B 数据整合进初稿
- 初稿完成 → 启动 Reviewer 对抗（3 轮，5/18-20 窗口）
- CodeLlama 实验需要先确认模型已下载到 westd-11235，可能需要 spawn worker 下载

### 5. 🎯 战略上下文
- **核心发现**: Exception events 是 verdict prediction 最有效的 trace 组件。Qwen-7B/1.5B exception_only 99.83%，DeepSeek 99.33%（1 seed 离群 91.09% 因 LoRA 初始化敏感性）。DebugBench 跨任务 100%。
- **决策链**: D044 补 regex baseline → D045/D046 确认 SFT 必要性（regex 93.61% vs SFT 99.83%, p=0.041）→ D047 DebugBench + regex 全部完成 → 现在收官 seed robustness + paper draft
- **Paper framing v3.0**: 3 core claims 全部 FINALIZED（exception dominance / cross-model generalization / DebugBench cross-task）
- **易错点**:
  - QUEUED 里的 `qwen1.5b_*` 和 `qwen15b_*` 是同一模型（Qwen-2.5-Coder-1.5B）的不同命名，注意 registry 里可能有重复
  - CodeLlama 实验还没跑过，模型可能未下载——提交前先确认模型在 `/root/autodl-tmp/models/` 下
  - 论文 13 页→8 页压缩还未完成（D042/D043 决策：Discussion 移入 appendix）
  - Cron 有误判历史（ae_only_seed123、vota_ae_only_seed42 都被误判为 failed），收到 cron failed 回调时要让 Worker 实际 SSH 验证


---
