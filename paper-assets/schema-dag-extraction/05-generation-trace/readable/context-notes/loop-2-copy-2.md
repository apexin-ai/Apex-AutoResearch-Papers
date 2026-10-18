# agent / loop_2.md

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_2.md`
- **Structured JSON:** [`00fa6d1a2e7e5e63a092.json`](../../sessions/00/00fa6d1a2e7e5e63a092.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 2
reason: max_wall_time
updated: '2026-05-15T12:58:54+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只有 cqa1-38874 的 cuda:0（gpu_ids 白名单），不可用其他 GPU
- submit_training_job 命令必须 `bash -c "..."` 包裹（tmux 用 sh 不是 bash）
- run_fewrel_formal.py 必须传 `--mode exp1/exp2`，否则 argparse 报错立即退出（已踩过）
- vLLM 脚本禁止在 vLLM 初始化前 import torch/networkx，否则 EngineCore fork 死锁（已发生两次，所有 SDGD 脚本已拆成 CPU+GPU 两阶段）
- LLaMA 模型必须用 nvidia/ repo（不是 neuralmagic/），路径 `/root/autodl-tmp/.hf_cache/llama-3.3-70b-instruct-fp8/`
- FewRel 80-rel 实验必须传 `--use_all`，否则只用 val 16 relations，count curve 缺 [32,64,80]

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-38874 (root)，RTX PRO 6000 Blackwell 98GB
- 工作目录：`/root/schema-dag-extraction`
- Python：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`（Python 3.12.3, vLLM 0.20.2, torch 2.10.0+cu128）
- Qwen3-32B-FP8：`/root/autodl-tmp/.hf_cache/qwen3-32b-fp8/`
- LLaMA-3.3-70B-FP8：`/root/autodl-tmp/.hf_cache/llama-3.3-70b-instruct-fp8/`（15/15 shards, 72.7GB 已验证）
- 活跃进程：**exp_fewrel_formal_80rel** (PID 267149, tmux=exp_fewrel_formal_80rel, cuda:0, cron 监控中)
- 无 W&B 集成，所有指标从结果 JSON 提取

### 3. 📊 当前状态
**刚完成**：SDGD-zero v2 代码集成（min_batch_size=8 + confidence-gated merge）、FewRel 16-rel sanity check (DONE/success)、exp-008 诊断分析。

**RUNNING**：
- `exp_fewrel_formal_80rel` — FewRel 80 relations, exp1 (count curve [1..80]) + exp2 (BCS controlled), PID 267149, 预估 ~5h

**DONE (本 session)**：
- `exp008_sdgd_zero_fewnerd_r2` — NEGATIVE. SDGD-zero F1=0.2514 < single_pass 0.4451. 根因：merge amplification
- `exp_fewrel_formal` — SUCCESS (16-rel sanity). BCS effect Δ=-9.1pp confirmed
- `fewrel_pilot` — SUCCESS. Δ=21-50pp

**等待中**：exp_fewrel_formal_80rel cron 完成回调。无活跃 Worker。

### 4. 📋 待办
- **80-rel cron 回调到达** → 分析 exp1 count curve + exp2 BCS correlation → update_registry DONE → 向 Director 汇报三层分析结果
- **80-rel 完成后** → 立即 submit exp-012 LLaMA (`bash /root/schema-dag-extraction/scripts/submit_exp012.sh` 但需通过 submit_training_job 提交，脚本: `scripts/run_exp012_llama.sh`)，预估 ~8h
- **exp-012 完成后** → SDGD-zero v2 Few-NERD (`scripts/run_sdgd_v2_fewnerd.sh`) + SDGD-zero v2 MAVEN MiniLM (`scripts/run_sdgd_v2_maven_minilm.sh`)
- **FewRel 80-rel 如果 negative**（BCS effect 不显著）→ 按 red-section skill 产 Framing 调整提案，禁止默默跑下一个
- **Director 未决策**：Claim 3 (SDGD framework) framing 调整等全部实验完成后统一处理

### 5. 🎯 战略上下文
- **目标**：EMNLP 2026 ARR May 25（距今 ~10 天）
- **核心 narrative (D013)**：pairwise confusability 是主要证据（r=0.156, p=4.6e-12），per-type 在 cross-domain 有效但 same-domain 有 centrality confound。5 层证据层级：pairwise → FewRel batch → Few-NERD per-type → MAVEN centrality (discussion) → error taxonomy
- **SDGD Claim 3 悬而未决**：v1 失败（merge amplification），v2 已准备但未验证。诊断结论本身是独立贡献（"小 batch over-prediction + union merge amplification 是 training-free decomposition 通用瓶颈"）
- **易错点**：
  - FewRel `--use_all` 容易忘，没有它只有 16 relations，count curve 截断
  - SDGD MAVEN 必须用 MiniLM embedding（Qwen3 pairwise 在 MAVEN 上 r=-0.007 无信号）
  - exp-012 LLaMA 用 `run_experiment.py`（不是 run_fewrel_formal.py），无 vLLM fork 风险（已验证）
  - Qwen3 embedding 元数据曾标错为 "Qwen3-Embedding-0.6B"，实际是 Qwen3-32B mean-pooled (dim=5120)


---
