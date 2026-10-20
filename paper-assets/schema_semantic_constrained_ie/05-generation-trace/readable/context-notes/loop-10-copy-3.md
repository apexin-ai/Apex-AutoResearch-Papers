# reviewer / loop_10.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_10.md`
- **Structured JSON:** [`62e68bda514844477d52.json`](../../sessions/62/62e68bda514844477d52.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: idle_timeout
updated: '2026-05-15T22:58:39+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：westd-16980 的 cuda:0 和 cuda:1，无其他可用卡
- submit_training_job 命令中**禁止硬编码 CUDA_VISIBLE_DEVICES**——必须由 wrapper 统一注入。今天刚因内层 `CUDA_VISIBLE_DEVICES=0` 覆盖外层 wrapper 的 `CUDA_VISIBLE_DEVICES=1` 导致级联 OOM 故障（两个进程挤 GPU 0，GPU 1 空转），已修复但需持续警惕
- Qwen DocRED 训练脚本是 `train_lora_docred.py`，Llama 是 `train_lora_docred_llama.py`——不要混
- 论文 claim "DR=0%" 需要下调为 "DR≤0.09%"，因 Llama LoRA constrained DR=0.09%（非零）。审稿人会攻击这个精确性问题

### 2. 🖥️ 基础设施快照
- 服务器：westd-16980(root)，工作目录 `/root/schema_semantic_constrained_ie`
- Python：`/root/miniconda3/bin/python3`，conda base 环境（非 venv）
- 激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型路径：
  - Qwen base: `/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B`
  - Llama base: `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B-Instruct`
  - Qwen LoRA SciERC merged: `checkpoints/qwen3_8b_lora_scierc_merged`
  - Llama LoRA SciERC merged: `/root/autodl-tmp/checkpoints/llama_lora_scierc_merged`
  - **Qwen LoRA DocRED merged: `/root/autodl-tmp/checkpoints/qwen_lora_docred_merged`** ← 刚完成
  - **Llama LoRA DocRED merged: `/root/autodl-tmp/checkpoints/llama_lora_docred_merged`** ← 刚完成
- 数据：SciERC `data/processed_data/test.json` (551), DocRED `data/docred/dev.json` (998)
- W&B: WANDB_MODE=disabled（本项目未配 W&B）
- 活跃进程（截至 handoff）：
  - Llama DocRED unconstrained eval: PID 303530, cuda:0
  - Qwen DocRED unconstrained eval: PID 304011, cuda:1

### 3. 📊 当前状态
**已完成审查：**
- 4 个 LoRA 训练全部 PASS（Qwen/Llama × SciERC/DocRED）
- GPU 级联故障发现→修复→验证闭环
- 论文数字一致性检查：Llama LoRA 8 个数字未入论文（已报 Director）

**Registry RUNNING/PREPARING：**
- `w5_llama_docred_lora_unconstrained_eval` — PREPARING, cuda:0 运行中, PID 303530
- `w5_qwen_docred_lora_unconstrained_eval` — RUNNING, cuda:1 运行中, PID 304011
- `w5_llama_docred_lora_constrained_eval` — PREPARING, 未提交（等 GPU 空出）
- `w5_qwen_docred_lora_constrained_eval` — PREPARING, 未提交（等 GPU 空出）

**等待：** 4 个 DocRED LoRA eval 的 on_complete 回调

### 4. 📋 待办（条件触发式）
- unconstrained eval 完成 → 审查 DR/R-F1 指标，确认残余 DR > 0%（composability 前提）
- constrained eval 完成 → 与 unconstrained 对比算 ΔDR / ΔR-F1，核实 composability claim
- 4 个 DocRED LoRA eval 全部完成 → 完整 4×2×2 composability matrix 可交付，触发论文全文数字更新审查
- Paper Agent 提交更新后 → 重点审查：Abstract/Intro/Limitations 的 "DR=0%" 是否已改为 "DR≤X%"，Table 3 是否扩展为双模型
- 如果 DocRED LoRA constrained 的 ΔR-F1 > 1pp（负向） → severity=warning，composability claim 需降级

### 5. 🎯 战略上下文
- **核心结论链**：OntoCoDec 两层约束解码消除 LLM IE 的 schema violations，且与 fine-tuning composable（Claim 3）
- **D028** 确认 Llama SciERC composability（ΔDR=-91.9%, ΔR-F1=+0.02pp），D025 确认 Qwen SciERC（ΔDR=-100%, ΔR-F1=-0.09pp）
- **当前关键路径**：DocRED LoRA eval → 完整 matrix → 论文更新 → May 19 内部稿 → May 25 EMNLP ARR
- **最易判断错的事**：Llama LoRA constrained DR=0.09%≠0%，不要像现有论文那样写 "DR elimination"——应写 "91.9-100% DR reduction"。Qwen SciERC 是唯一 DR=0% 的格子，其他都有微量残余
- **历史坑**：Agent 提交训练命令时会在 spec.command 里硬编码 CUDA_VISIBLE_DEVICES，与 wrapper 冲突。每次新训练提交后务必 `ps + nvidia-smi` 核实实际 GPU 分配


---
