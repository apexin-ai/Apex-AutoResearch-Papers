# reviewer / loop_5.md

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_5.md`
- **Structured JSON:** [`25d89a45fe9f8507fddb.json`](../../sessions/25/25d89a45fe9f8507fddb.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_wall_time
updated: '2026-05-16T09:42:38+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 westd-34887 的 cuda:0 和 cuda:1（C001），越界立即 CRITICAL
- 长时间 GPU 实验必须 nohup 启动（C002），禁止裸 tmux
- evaluate.py 默认 sparsity_target=0.5，所有非 50% 评估必须显式传 --sparsity_target
- WANDB_MODE=offline 必须设置（服务器离线，d030_kl40_uniform 因此失败过一次）
- 论文 KL PPL 引用统一用 4-seed mean 12.00±0.07，不用单 seed 最佳值
- BCE framing 必须用 "objective mismatch"，禁止 "anti-learning"
- SPON framing 必须用 "marginal complement"，禁止 "KL subsumes SPON"

### 2. 🖥️ 基础设施快照
- 服务器：westd-34887(root)，工作目录 /root/distill_sparse_swiglu/
- Python：/root/miniconda3/bin/python（conda base 环境，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- 模型：Llama-3.1-8B @ /root/autodl-tmp/models/llama-3.1-8b，Mistral-7B @ /root/autodl-tmp/models/mistral-7b
- HF cache：/root/autodl-tmp/.hf_cache（HF_HOME 必须指向这里）
- W&B：offline 模式，日志在 /root/distill_sparse_swiglu/wandb/
- Checkpoints：/root/distill_sparse_swiglu/checkpoints/（KL 各 seed、BCE v3、Mistral 等）
- 活跃进程：最后 GPU check 时 cuda:0 和 cuda:1 均空闲，无活跃训练

### 3. 📊 当前状态
刚审查完一批实验结果，关键产出：
- **bce_isocompute_v3_s42**: DONE — PPL 27.97 (KL 优 2.33×) + downstream 灾难性（ARC 0.24, MMLU 0.30, GSM8K 0.05）
- **d030_kl40_uniform**: DONE — MMLU=0.3068，确认 threshold 在 30-40% 之间
- **bench_dense**: DONE — 完整 few-shot baseline（PPL 6.12, ARC 0.58, MMLU 0.65, GSM8K 0.49）
- **eval_kl30_teal_30pct**: DONE — 确认 teal_sparse_ppl=8.98（D032 "污染" 诊断是误报，原值正确）
- **bench_kl50_global**: QUEUED — KL 50% few-shot downstream 尚未跑，这是论文 KL vs BCE downstream 公平对比的缺失数据
- **bench_kl30_uniform**: DONE（与 d030 一致，可复现）
- 多个 paper_research worker 完成文献补充（PowerInfer、Polar Sparsity、MiniLLM、DistiLLM 等）

### 4. 📋 待办（条件触发式）
- bench_kl50_global 提交并完成 → 可在论文中公平对比 KL vs BCE downstream（同协议 few-shot）
- paper_framing.md Claim 3 已更新为 phase transition → 确认论文 Experiments section 与新 framing 对齐
- 70% TEAL 数据完整（vanilla=100.11, predictor-TEAL=17.91）→ 论文主表用 predictor-TEAL vs vanilla-TEAL 同协议对比（不要混用 hard_mask 13.84）
- 文献中 Ma et al. (npj AI 2026) + Týr + GISP 无 arXiv ID → Agent 引用前必须 WebSearch 验证，否则标 CRITICAL
- CATS "50% works fine" 与我们 "50% collapses" 表面矛盾 → 论文 Related Work 必须解释差异（PPL vs downstream、exact threshold vs predictor）

### 5. 🎯 战略上下文
- **DDL**: EMNLP 2026 ARR May, 2026-05-25（剩 9 天）
- **核心结论链**: D007(MVP PASS) → D028(50% collapse universal) → D030(per-layer imbalance是根因) → D031(BCE iso-compute封堵Concern#2) → 40% threshold确认在30-40%之间
- **三个 Claim 强度**: Claim 1 (KL>>baselines) STRONG; Claim 2 (SPON orthogonal) ADEQUATE; Claim 3 (sparsity regime) 数据已完整但 framing 刚更新需要论文对齐
- **最容易判断错的事**:
  1. 70% 对比中 KL 端应用 predictor_teal_sparse_ppl=17.91（不是 hard_mask=13.84），三个 level 必须同协议
  2. D032 "数据污染" 已被证伪——kl_sparsity30_s42_v3 的 teal_sparse_ppl=8.98 是正确值（巧合与 Mistral 相同）
  3. BCE iso-compute PPL 从 MVP 44.05 降到 27.97 说明更多 compute 确实有帮助，但不够——不能 claim "compute 完全无用"，正确 claim 是 "structural mismatch 无法被 compute scaling 弥补"
  4. 文献 worker 产出的引用有幻觉风险（Ma et al. 无 arXiv ID），不可直接放入论文


---
