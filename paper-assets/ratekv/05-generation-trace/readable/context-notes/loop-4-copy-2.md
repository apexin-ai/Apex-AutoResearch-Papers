# agent / loop_4.md

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_4.md`
- **Structured JSON:** [`eae0e79092f0df0a1458.json`](../../sessions/ea/eae0e79092f0df0a1458.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 4
reason: idle_timeout
updated: '2026-05-14T15:03:04+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-37397 上只有 cuda:0 和 cuda:1（2× RTX PRO 6000 96GB）。不得使用其他 GPU
- qwen72b_profiling 已被 D043 正式 defer（磁盘空间不足），不要尝试重启
- 所有 eval 必须用 bf16，禁止 fp16（大模型 fp16 overflow 导致无效 PPL）
- 论文数字必须来自统一 pipeline，不引用 exp_e 的绝对 PPL
- submit_training_job 的 command 必须自带环境激活（source conda），不要假设 .venv 存在
- HF_HOME 必须显式设为 `/root/autodl-tmp/.hf_cache`

### 2. 🖥️ 基础设施快照
- 服务器：westd-37397，2× RTX PRO 6000 96GB
- 工作目录：/root/ratekv/
- Python：/root/miniconda3/bin/python（conda base 环境），激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- HF cache：/root/autodl-tmp/.hf_cache
- 数据：WikiText-2 缓存在 /root/autodl-tmp/.hf_cache/datasets/wikitext/wikitext-2-raw-v1/
- cuda:0 → gemma2_9b_full_pipeline (RUNNING，模型 ~36GB 可能仍在下载，pipeline 下载完成后自动启动)
- cuda:1 → yi15_9b_full_pipeline (ALLOCATED，pid 229912，tmux session，wait_and_run_yi15.sh 脚本提交)
- Cron：reconcile 返回 0 个活跃 cron（两个实验可能没挂 cron 监控，需要确认）

### 3. 📊 当前状态
- **论文阶段**：Paper Final Polish，EMNLP 2026 ARR May 25 截止（距今 11 天）。全章节完成 + refinement round 2 已提交。D040 patch 全部入稿。Group C 审稿团队独立审稿中
- **P0 (8/8) ✅ + P1 (7/7) ✅ 全部完成**，P2 deferred
- **RUNNING**: gemma2_9b_full_pipeline（cuda:0，GQA 2:1，336 heads，测试低 GQA ratio 异质性）
- **ALLOCATED**: yi15_9b_full_pipeline（cuda:1，pid 229912，wait_and_run 脚本已提交，之前 Agent 在修复 tmux 问题）
- **待清理**: multi_seed_lowres (PENDING，可能被 plan_017 覆盖)、greedy_constrained_ablation (PREPARING/killed)、cross_domain_calibration_v2 (PREPARING)、qwen72b_profiling (ALLOCATED/killed/deferred D043)
- **无活跃 cron**：gemma2 和 yi15 都没有 cron 监控，需要补挂或手动轮询

### 4. 📋 待办（条件触发式）
- gemma2_9b_full_pipeline 完成 → 分析结果（Top-5% concentration, k ablation, MCKP vs uniform）→ 结果入稿 → 论文扩展到 5 模型
- yi15_9b_full_pipeline 完成 → 同上分析 → 结果入稿
- 两个实验都完成 → generalizability claim 从 3 模型升级到 5 模型，更新 §4 表格和 discussion
- gemma2/yi15 任一 negative → 按 red-section 产 Framing 提案，但不太可能影响核心 claims（这两个是加固实验）
- Group C 审稿报告回传 → 按 reviewer 意见修改论文
- 清理冗余实验：multi_seed_lowres 确认被 plan_017 覆盖后关闭；greedy_constrained_ablation 确认被 plan_016 覆盖后关闭

### 5. 🎯 战略上下文
- **核心发现**：per-KV-head 非均匀 bit-width 分配中，cardinality constraint 是唯一贡献（greedy=MCKP，Δ=0.0000）。异质性由 GQA ratio 决定：高 GQA (Qwen 7:1) → 高异质性 → MCKP 优势大；低 GQA (Llama/Mistral 4:1) → 低异质性 → MCKP 优势薄
- **3 个 core claims 均有充分证据**：(1) heterogeneity-dependent (2) constraint is THE contribution (3) practical diagnostic (Top-5% > 0.50 rule)
- **Gemma-2/Yi-1.5 是论文加固**：从 3→5 模型覆盖，增强 generalizability。Gemma-2 是 GQA 2:1（预期低异质性，类似 Llama/Mistral 模式）
- **易错点**：(1) Gemma-2 有 attn_logit_softcapping=50，profiling 可能受影响，注意分析时区分 (2) yi15 的 wait_and_run 脚本是等 gemma2 下载完腾出带宽后再下载 Yi 模型，不是等 GPU (3) 两个实验没有 cron，需要手动检查或补挂 (4) qwen72b_profiling 虽然 status=ALLOCATED 但 conclusion=killed，是 D043 defer 的结果，不要尝试重启
- **决策链关键节点**：D037 (per-model optimal k) → D040 (patch 批次入稿) → D043 (72B defer) 是最近的关键决策脉络


---
