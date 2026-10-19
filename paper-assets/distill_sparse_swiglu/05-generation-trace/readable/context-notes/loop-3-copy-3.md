# reviewer / loop_3.md

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_3.md`
- **Structured JSON:** [`adda82128c53c1c6e2d8.json`](../../sessions/ad/adda82128c53c1c6e2d8.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-05-15T22:51:29+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-34887 的 cuda:0 和 cuda:1（`execution.gpu_ids=[0,1]`）
- eval_benchmark.py 中 TEAL/WINA baseline 实现有 critical bug（已报告 Director）：TEAL 调用了 `teal_activation_magnitude_masks`（greedy，PPL=48715）而非 `vanilla_teal_global_masks`（global，PPL=23.31）；WINA 调用了 `wina_greedy_allocation_masks`（inverted bug，PPL=2126）而非 `wina_global_masks`（PPL=27.93）。**在确认修复前，eval_benchmark.py 输出的 training-free baseline 数字不可引用**
- Mistral 模型路径是 `/root/autodl-tmp/models/mistral-7b/`（实际为 Mistral-7B-v0.3，config 可验证 `rope_theta=1000000, vocab_size=32768`）

### 2. 🖥️ 基础设施快照
- 服务器：westd-34887(root)，工作目录 `/root/distill_sparse_swiglu/`
- Python：`/root/miniconda3/bin/python`（conda base 环境，非 venv）
- Llama 模型：`/root/autodl-tmp/models/llama-3.1-8b/`
- Mistral 模型：`/root/autodl-tmp/models/mistral-7b/`
- HF cache：`/root/autodl-tmp/.hf_cache/`（datasets 子目录有 wikitext, ai2_arc, winogrande, cais/mmlu, gsm8k；C4 validation 下载未完成，仅 1/8 分片）
- wandb：offline 模式，本地 `/root/distill_sparse_swiglu/wandb/`
- 两套 eval 脚本共存：`src/eval_benchmark.py`（有 baseline bug）和 `src/benchmark_eval.py`（lm-eval-harness 集成，imports 正确的 global 函数）
- 活跃进程（截至 handoff 前）：GPU 0 上有 eval 进程（PIDs 164139/163723），Mistral 训练已完成释放 GPU 1

### 3. 📊 当前状态
本轮审查了 4 个 worker + 1 个 cron 回调：
- **plan_007 eval prep**：eval 基础架构就绪但 TEAL/WINA baseline 实现错误 → 已 CRITICAL 报告 Director
- **dataset precache**：MMLU/ARC/WinoGrande/GSM8K 已缓存，C4 validation 下载未完成
- **stale process cleanup**：旧卡死进程（10h+ wikitext、stuck C4 streaming）已清理
- **mistral_kl_s42 训练完成**：1000 步完成，final loss=0.2188，sparsity=0.48，checkpoint 已保存（152MB）。Registry 状态 ANALYZING。
- Registry 中 PREPARING 的：`lm_eval_dense`、`lm_eval_kl_s42`、`lm_eval_dense_test`（plan_007 lm-eval 相关）
- kl_sparsity30_s42_v3 DONE 但备注"TEAL sparse PPL 因 GPU 并发 OOM 未获取"

### 4. 📋 待办
- mistral_kl_s42 ANALYZING → DONE 时 → 核实 eval metrics（PPL + sparsity），与 Llama KL 对比确认跨架构泛化（Llama PPL=12.00 @ 50% sparsity，Mistral 应在合理范围内）
- eval_benchmark.py TEAL/WINA 修复确认 → 重跑 consolidated results，验证 PPL 与 registry headline 数字一致（Dense=6.12, KL=12.00, TEAL=23.31, WINA=27.93）
- lm_eval_dense / lm_eval_kl_s42 完成 → 审查 ARC-c/WinoGrande/MMLU/GSM8K 数字，确认 downstream accuracy 支持 Claim 1
- C4 validation 下载完成 → 确认 C4 PPL 评估可用
- plan_008 sparsity70 eval 若有结果 → 审查 sparsity scaling trend（30%/50%/70% KL-BCE delta）

### 5. 🎯 战略上下文
- **核心 story**：KL distillation 使 SwiGLU contextual sparsity prediction 不需要 error compensation，实现最简推理管线
- **三层梯队已确认**：KL PPL 12.00 >> training-free (TEAL 23.31) >> BCE iso-compute 54.84
- **Claim 2 已 reframe**：不再是"KL subsumes SPON"，而是"SPON orthogonal 且量级小"（predictor effect 482 vs SPON 76）
- **Claim 3 (sparsity scaling)** 正在收集数据点：30% 已有（PPL 7.30 @ 28.5% achieved），50% 已有，70% eval 进行中
- **DDL**：EMNLP 2026 ARR May，截稿 2026-05-25（还剩 10 天）
- **最容易判断错的事**：eval_benchmark.py 和 benchmark_eval.py 是两个不同脚本，前者有 baseline bug 后者没有。不要看到 benchmark 结果就信——先确认是哪个脚本产出的
- **易踩坑**：Dense PPL 在不同 eval 路径下有 6.12 vs 6.48 的偏差，可能是 sample 数量差异（20 vs 141+），引用论文数字前必须确认 eval 配置一致


---
