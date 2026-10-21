# agent / loop_15.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_15.md`
- **Structured JSON:** [`238c84cf4ce8605a795b.json`](../../sessions/23/238c84cf4ce8605a795b.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 15
reason: max_wall_time
updated: '2026-05-17T11:55:12+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：rtx5090-4x 的 cuda:0/1/2/3，无其他服务器
- 8B resume 用的是 checkpoint-750（非 Director 原始指令的 checkpoint-100，因 100 不存在）
- s43 eval 用的是 `rsft_output_ced_s43/checkpoint-510`（非 s44），这是 Lead 1 CED filtering 的前置
- freige 包有内外层嵌套问题（`/root/autodl-tmp/freige/freige/`），Worker 已用 symlink 修复，不要重建目录结构
- rsft_trainer.py 的 `--resume_from_checkpoint` 是本次 Worker 新加的参数，非原生支持

### 2. 🖥️ 基础设施快照
- 服务器：rtx5090-4x，工作目录 `/root/autodl-tmp/freige`
- Python：`/root/miniconda3/bin/python`（`source /root/miniconda3/bin/activate` 激活）
- 模型路径：`/root/autodl-tmp/models/` 下有 Qwen3-4B、Qwen/Qwen3-1.7B、Qwen/Qwen3-8B、meta-llama/Meta-Llama-3.1-8B
- SFT adapters：`sft_output`(4B)、`sft_output_qwen3_1_7b_bf16`、`sft_output_qwen3_8b_bf16`、`sft_output_llama_3_1_8b`
- RSFT checkpoints：`rsft_output_ced_s43/checkpoint-510`(4B)、`rsft_output_qwen3_1_7b/checkpoint-1698`、`rsft_output_llama_3_1_8b_r3/checkpoint-3312`、`rsft_output_qwen3_8b/checkpoint-750+`
- 合并模型：`/root/autodl-tmp/merged_sft_rsft_ced_s43`（Lead 2 GRPO 输入）
- CED filter 脚本：`/root/autodl-tmp/freige/eval/ced_evidence_filter.py`（Lead 1 核心）
- 磁盘：58GB 可用（清理后），250GB 总量
- HF_HUB_OFFLINE=1 环境，所有模型必须本地路径
- 活跃进程（提交于 08:38-08:40 UTC）：
  - rsft_s43_dev_eval_preds: PID 431308, cuda:0
  - plan_006_qwen3_1_7b_rsft_eval_r2: PID 431385, cuda:1
  - plan_006_llama_rsft_r3_eval: PID 432670, cuda:2
  - plan_006_qwen3_8b_rsft_train_r2: PID 431785, cuda:3

### 3. 📊 当前状态
我刚 spawn 了 `worker_ops_urgent_3h_status_check`（Director 紧急指令：3h 无回调，检查 4 GPU 状态 + 收集 eval 结果 + 提交 Lead 1）。这个 Worker 回调还没到。

Registry RUNNING（4 个）：
- `rsft_s43_dev_eval_preds` — 4B s43 eval, Lead 1 前置（应已完成，~1h 任务）
- `plan_006_qwen3_1_7b_rsft_eval_r2` — 1.7B scaling study 数据点（应已完成）
- `plan_006_llama_rsft_r3_eval` — LLaMA cross-arch 数据点（应已完成）
- `plan_006_qwen3_8b_rsft_train_r2` — 8B RSFT resume from 750/3393（预计还需 ~4h）

等待中：
- Worker `worker_ops_urgent_3h_status_check_20260517T115401` 的回调
- 该 Worker 会：检查进程、收集 metrics、如果 cuda:0 完成则提交 Lead 1 CED filter

### 4. 📋 待办
- Worker 回调到达 → 读取结果，更新 registry（完成的 eval 转 DONE + 记录 metrics），向 Director 汇报全面状态
- cuda:0 s43 eval 完成 + predictions.json 存在 → Lead 1 CED evidence filter 提交（Worker 应已做）
- cuda:1/2 eval 完成 → 收集 Ign-F1/Evi-F1，写入 report.md，向 Director 报 scaling study 结果
- cuda:3 8B training 完成 → 提交 8B eval（`--model_path rsft_output_qwen3_8b/&lt;final_ckpt> --base_model Qwen3-8B --sft_adapter sft_output_qwen3_8b_bf16`）
- Lead 1 CED filter 完成 → 分析 tau=0.3/0.5/0.7 的 EDCR 改善，汇报 Director（这是核心 story point）
- 如果任何 eval 又失败 → 检查是否磁盘问题（df -h），诊断后重提交

### 5. 🎯 战略上下文
- 项目目标：EMNLP 2026 Main（ARR July），证据接地的文档级关系抽取
- 核心 story：CED（Contrastive Evidence Discrimination）作为统一信号——训练时过滤 RSFT 数据 + 推理时过滤 distractor citations
- **Lead 1**（inference-time CED filtering）是最高优先级——如果 EDCR 从 0.63→0.80+ 就是强 claim
- **Lead 2**（RSFT→GRPO two-stage）step 30/50 时 reward 0.96→1.02 趋势好，但 checkpoint 已删（磁盘清理），需要重跑
- Scaling study（1.7B/4B/8B + LLaMA cross-arch）是支撑 story 的配角实验
- Evidence Tax 现象：1.7B +6.2pp, 4B -7.5pp, 8B ≈0——CED-RSFT 应该消除这个 tax
- 易错点：eval 命令必须带 `--sft_adapter`（漏掉 → rel_f1≈0）；GRPO 用 `--data_dir` 不是 `--data_path`；`--no-quantize` 对 5090 GPU 是必须的（bf16 原生比量化快）


---
