# agent / loop_7.md

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_7.md`
- **Structured JSON:** [`f9b85e6ef1a3f3012527.json`](../../sessions/f9/f9b85e6ef1a3f3012527.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: idle_timeout
updated: '2026-05-16T14:31:25+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单: autodl-5090 上 cuda:0/1/2/3 均已分配给本项目（get_project_resource_usage 确认）
- LLaMA-3.1-8B 训练必须用 swift sft（不是 transformers Trainer），模型路径 `/root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct`
- 数据路径固定 `/root/autodl-tmp/tax_error_inject_agent/data/mini_pipeline_v4/sft_{vanilla,taxei,random}_v4.jsonl`
- conda 环境：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，不要创建 venv
- Scale-up 数据收集已暂停又撤销（D044→D046），但统计口径问题未完全解决，谨慎处理

### 2. 🖥️ 基础设施快照
- 服务器：autodl-5090，工作目录 `/root/autodl-tmp/tax_error_inject_agent`
- Python：`/root/miniconda3/bin/python`（conda base）
- 模型：`/root/autodl-tmp/models/Meta-Llama-3.1-8B-Instruct`
- 数据：`data/mini_pipeline_v4/sft_{vanilla,taxei,random}_v4.jsonl`
- Output：`/root/autodl-tmp/tax_error_inject_agent/output/llama31-{vanilla,taxei,random}-s0`
- W&B：配置存在（CRON 报告 W&B data available）
- 活跃进程：llama31-random-s0 仍在 RUNNING（reconcile_crons 确认，cuda:2）

### 3. 📊 当前状态
**刚收到 CRON 回调**：llama31-vanilla-s0 训练完成（cuda:0），已派 Worker 分析日志+更新 registry。

**已派出 Worker（等待回调）**：
- `worker_analyze_llama31-vanilla-s0_20260516T102750`：读日志、提取 metrics、更新 registry→DONE
- `worker_diagnose_llama31-taxei-s0_20260516T102807`：诊断 EXIT_CODE=129 失败原因

**Registry 关键状态**：
- `llama31-vanilla-s0`: PREPARING（实际已完成，Worker 正在分析后会转 DONE）
- `llama31-taxei-s0`: PREPARING（failed，EXIT_CODE=129，Worker 正诊断）
- `llama31-random-s0`: PREPARING（仍在跑，cuda:2）
- 另有 3 个 QUEUED 的 v4 dose-response 实验等 GPU

**整体进度**：164 实验中 111 DONE（98 success），50 PREPARING，3 QUEUED。

### 4. 📋 待办
- Worker analyze llama31-vanilla-s0 回调 → 确认 metrics，向 Director 汇报 LLaMA vanilla s0 结果
- Worker diagnose llama31-taxei-s0 回调 → 根据原因决定重试策略（可能 OOM 需降 batch_size 或换 GPU）
- llama31-random-s0 cron 完成回调 → 同样分析+更新 registry
- LLaMA 三条件 s0 全部 DONE → 启动 eval（用 ALFWorld 47 clean tasks），然后启动 s123 训练
- 若 cuda:0 空出（vanilla 完成后）→ 可立即重跑 taxei-s0 或启动 QUEUED 中的 dose-response 实验
- TaxEI-RP s7 eval 应在 RP s7 训练完成后安排

### 5. 🎯 战略上下文
- **项目核心**：Taxonomy-guided error injection → embodied planning 的 negative result paper（EMNLP 2026 Findings 8页长文）
- **关键结论**：Qwen3-8B 5-seed 已证明 TaxEI ≈ Random（均 58.3%），TaxEI-RP 更差（47.9%）。现在做 LLaMA-3.1-8B 跨模型验证（D042/D045）
- **LLaMA 实验设计**：3-seed (s42已完成, s0进行中, s123待做) × 3条件 (Vanilla/TaxEI/Random)，s42 结果尚未 eval
- **易错点**：
  - llama31-taxei-s0 的 EXIT_CODE=129 可能是被其他进程挤掉（5090 上 4 个同时跑），重试前确认 GPU 显存够
  - registry 状态显示 PREPARING 但实际有些已完成——这是因为 cron 系统标记了 finished_at 但没转 status，Worker 需要手动转
  - ROADMAP 说"4 GPU 满载"但实际 vanilla 已完成+taxei 失败，只有 random 还在跑，空出 2 张 GPU 应立即利用


---
