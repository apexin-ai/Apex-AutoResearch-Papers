# agent / loop_10.md

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_10.md`
- **Structured JSON:** [`d24f50873a84839522f3.json`](../../sessions/d2/d24f50873a84839522f3.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_messages
updated: '2026-05-15T22:58:58+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单: westd-16980:cuda:0, westd-16980:cuda:1，不得用其他 GPU
- w1_cf_fallback_docred 已被 Director 杀掉 (D027)，不要重启或重建类似实验
- CF fallback 已定性为 analytical finding (D020)，不需要再跑实验验证
- Negative 结果不得默默跑下一个实验——必须先产出 Framing 提案经 Director 审批
- DocRED SFT 数据生成用的是 Qwen3-8B tokenizer (`/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B`)，后续 Llama fine-tune 需要用 Llama tokenizer 重新生成

### 2. 🖥️ 基础设施快照
- 服务器: westd-16980，工作目录 `/root/schema_semantic_constrained_ie`
- Python: `/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- 激活: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型路径: `/root/autodl-tmp/models/Qwen3-8B-ms/Qwen/Qwen3-8B`（Qwen），Llama 路径需确认
- 数据: `/root/schema_semantic_constrained_ie/data/docred/` (train_annotated.json, dev.json, sft_*.jsonl)
- 活跃进程: w5_llama_lora_scierc_constrained_eval (PID 290317, cuda:1, tmux session)
- Cron: w5_llama_lora_scierc_constrained_eval 正在监控中

### 3. 📊 当前状态
**刚做完**: 收到 w5_docred_sft_data_gen cron 回调（进程正常退出），已 spawn Worker `worker_analysis_w5_docred_sft_data_gen_20260515T175244` 去读日志 + 检查生成的 sft_train.jsonl / sft_dev.jsonl 数据质量。**Worker 回调还没到**，registry 状态仍为 PREPARING（需更新到 ANALYZING→DONE）。

- **RUNNING**: w5_llama_lora_scierc_constrained_eval (cuda:1) — Fine-tuned Llama SciERC constrained eval，完成 Llama SciERC 2×2 matrix
- **PREPARING**: w5_docred_sft_data_gen (进程已完成，等 Worker 分析), w5_qwen_docred_lora_training, w1_cf_fallback_llama_docred, w1_cf_fallback_llama_scierc
- **等待中**: Worker 分析回调 (w5_docred_sft_data_gen)；w5_llama_lora_scierc_constrained_eval cron 回调

### 4. 📋 待办
- Worker `worker_analysis_w5_docred_sft_data_gen_20260515T175244` 回调到达 → 读取分析结果 → update_registry(DONE, success/failed) → 如果数据生成成功且质量 OK，向 Director 汇报并建议启动 w5_qwen_docred_lora_training (cuda:0 空闲可用)
- w5_llama_lora_scierc_constrained_eval cron 回调到达 → spawn Worker 分析 → 计算 Llama SciERC 2×2 matrix (对标 Qwen SciERC 2×2) → update_registry → 向 Director 汇报（这是关键路径第 4 步）
- Llama SciERC 2×2 matrix 完成后 → Paper Agent 写入 Llama 结果 → 推进关键路径第 5-6 步（全文编译 → Round 2 review）
- cuda:0 空闲 → 如果 DocRED SFT 数据 OK，提议给 Director 启动 Qwen DocRED LoRA training

### 5. 🎯 战略上下文
- **目标**: EMNLP ARR May 25 提交，May 19 内部稿交付
- **核心结论**: OntoCoDec composability 已在 Qwen SciERC 上确认 (DR=0%, F1 -0.09pp)。Llama SciERC 是跨模型验证，成功则 target score 4.0/5+
- **2×2 Composability Matrix** 是论文核心证据: {Zero-shot, Fine-tuned} × {Unconstrained, Constrained}。Qwen SciERC ✅ 完整，Llama SciERC 差 constrained eval 一格（正在跑），DocRED 只有 zero-shot
- **决策链**: D020(CF analytical finding) → D025(W5 composability 确认) → D027(杀 w1_cf_fallback_docred) → 当前聚焦 Llama + DocRED 扩展
- **易错点**: (1) DocRED SFT 数据是用 Qwen tokenizer 生成的，Llama DocRED fine-tune 需要重新生成；(2) w1_cf_fallback_llama_docred 和 w1_cf_fallback_llama_scierc 在 PREPARING 但 CF fallback 实验方向已被 D020/D027 基本否定，不要贸然启动——需 Director 确认；(3) cuda:0 当前空闲，应尽快利用


---
