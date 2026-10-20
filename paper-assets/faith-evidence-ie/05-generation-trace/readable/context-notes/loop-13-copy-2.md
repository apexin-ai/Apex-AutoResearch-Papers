# reviewer / loop_13.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_13.md`
- **Structured JSON:** [`fc853b8dbc4f1fd56899.json`](../../sessions/fc/fc853b8dbc4f1fd56899.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: max_wall_time
updated: '2026-05-17T08:05:29+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单: rtx5090-4x 的 cuda:0-3（物理卡 0/1/2/3），越界即 critical
- D076 eval 协议: batch_size=4, --no-quantize, --sft_adapter, max_new_tokens=1024, seed=42
- D077: plan_006 系列必须用 bf16 LoRA，禁止 QLoRA
- 3-param loading pattern: `--model_path &lt;rsft_ckpt> --base_model &lt;base> --sft_adapter &lt;sft_output>`
- **磁盘已满** `/dev/md0 250G 100%` — 任何新 checkpoint/eval 写入都会失败，清理前不可重提交训练

### 2. 🖥️ 基础设施快照
- 服务器: rtx5090-4x (root)，代码根: `/root/autodl-tmp/freige`
- Python: `/root/miniconda3/bin/python`，conda base
- 模型路径: `/root/autodl-tmp/models/Qwen/Qwen3-{1.7B,4B,8B}`, `/root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B`
- SFT outputs: `sft_output`(4B), `sft_output_qwen3_1_7b_bf16`, `sft_output_qwen3_8b_bf16`, `sft_output_llama_3_1_8b`
- RSFT outputs: `rsft_output_s44`(4B best), `rsft_output_qwen3_1_7b`, `rsft_output_llama_3_1_8b_r3/checkpoint-3312`, `rsft_output_qwen3_8b/checkpoint-100`(8B 崩溃前最后好 ckpt)
- Merged model: `/root/autodl-tmp/merged_sft_rsft_ced_s43` (4B, lead2 用)
- NLI model: `/root/autodl-tmp/.hf_cache/models--cross-encoder--nli-deberta-v3-base/snapshots/6c749ce3425cd33b46d187e45b92bbf96ee12ec7`
- 数据: `/root/autodl-tmp/data/docred/` (train_annotated.json, dev.json, test.json)
- 活跃进程 (last known): GPU 0 PID 414837 (rsft_s44_dev_eval_preds), GPU 1 PID 420018 (1.7B eval)
- GPU 2/3: 空闲（两个训练都因磁盘满崩溃）
- HF 离线模式: 需设 `HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1`
- Logs: `/root/runs/faith-evidence-ie/` 和 `/root/autodl-tmp/logs/`

### 3. 📊 当前状态
**刚发生**: 磁盘 100% 满导致 GPU 2 (lead2_r2 GRPO) 和 GPU 3 (8B RSFT) 同时崩溃于 torch.save() checkpoint。已报 critical 给 Director。

**Registry RUNNING（可能 stale）**:
- `rsft_s44_dev_eval_preds` (GPU 0) — 4B dev 推理，为线索1 CED filtering 准备 predictions。跑了 >3h，可能因磁盘满无法写结果
- `plan_006_qwen3_1_7b_rsft_eval` (GPU 1) — 1.7B RSFT dev eval，scaling study 数据点
- `lead2_rsft_grpo_ced_r2` (GPU 2) — 已崩溃 step 30/50，registry 可能未更新
- `plan_006_qwen3_8b_rsft_train` (GPU 3) — 已崩溃 step 1000/3393，registry 可能未更新

**已完成未更新 registry**:
- `plan_016_llama_rsft_train_r3` — LLaMA 8B RSFT 训练完成 3312/3312 steps，output 在 `rsft_output_llama_3_1_8b_r3/`

**等待**: Director 决策磁盘清理策略

### 4. 📋 待办
- 磁盘清理完成 → 验证 df 有足够空间 → 8B RSFT 可从 checkpoint-100 resume
- 磁盘清理完成 → lead2_r2 可从 checkpoint-20 resume（加 `--resume_from_checkpoint`），或直接用 ckpt-20 做 eval（只差 20 steps 且已证明 CED reward 上升）
- rsft_s44_dev_eval_preds 完成（或因磁盘满失败）→ 检查 `/root/autodl-tmp/eval_results/rsft_s44_dev_with_preds/` 是否有 predictions.jsonl
- 1.7B eval 完成 → 验证 metrics，对比 SFT baseline（D083 数据），填入 scaling study
- LLaMA r3 eval 需要提交（训练已完成但 eval 未跑）
- **GRPO data_dir bug**: `grpo_trainer.py` 必须传 `--data_dir /root/autodl-tmp/data/docred`，否则 fallback Hub 下载失败
- **可删 checkpoint 释放空间**: LLaMA r3 的 checkpoint-3150/3200/3250 各 1.9GB（保留 3300+3312 即可）

### 5. 🎯 战略上下文
- **Paper framing**: FaithExtract — 用 CED (NLI-based scoring) 进行 evidence-aware RE 训练。Core claims: C1(feasibility), C2(decoupling spectrum), C3(NLI scoring), C4(EDCR diagnostic), C5(scaling)
- **Scaling study (C5)**: 1.7B/4B/8B × SFT/RSFT 矩阵。4B 数据完整；1.7B RSFT 训练完、eval 进行中；8B RSFT 崩溃在 29%
- **Evidence Tax pattern**: 1.7B 受益(+6.2pp), 4B 付出代价(-7.5pp), 8B 预期 neutral
- **Decoupling Spectrum (C2)**: GRPO-QLoRA 灾难性 > GRPO-bf16 轻微 > DPO 渐进 > RSFT 无
- **lead2 关键发现**: RSFT→short GRPO 的 CED reward 30 步内从 0.438→0.540 (+23%)，KL 极低，证实线索2 可行性。即使只有 30 steps 数据，这已是有价值的 evidence for C2
- **易错点**:
  - 不要以为 registry RUNNING 就代表进程活着——磁盘满后进程已死但 registry 未更新
  - `docred_processor.py` 有 Hub fallback（line 135），GRPO 路径必须传 `--data_dir`
  - 8B RSFT VRAM 97.9% 很紧张，但 OOM 不是崩溃原因（是磁盘满）
  - Tokenizer Mistral regex 警告是 cosmetic，不影响功能
  - DocRED test 是 blind eval（需 CodaLab 提交），不能本地算 F1


---
