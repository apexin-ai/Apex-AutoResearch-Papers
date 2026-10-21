# agent / loop_1.md

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_1.md`
- **Structured JSON:** [`92913ef7c74eac3c84d8.json`](../../sessions/92/92913ef7c74eac3c84d8.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: idle_timeout
updated: '2026-05-15T15:28:59+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：只能用 westd-34887 的 cuda:0 和 cuda:1（config gpu_ids=[0,1]）
- submit_training_job 命令必须自带环境激活：`source /root/distill_sparse_swiglu/setup_env.sh`（不是 conda activate，不是 .venv）
- GPU 编号脚本内始终用 `--gpu 0`（框架自动映射 CUDA_VISIBLE_DEVICES）
- WANDB_MODE=disabled（当前所有实验都禁用了 W&B，指标只能从日志读取）
- KL 系列实验必须用 batch_size=2 + gradient_accumulation_steps=2（有效 batch=4），否则 OOM（88.4/95GB）

### 2. 🖥️ 基础设施快照
- 服务器：westd-34887，account=root
- 工作目录：/root/distill_sparse_swiglu/
- 环境激活：`source /root/distill_sparse_swiglu/setup_env.sh`（具体内容未知，Worker 创建的）
- 模型路径：/root/autodl-tmp/models/llama-3.1-8b
- 数据集：wikitext-103（D002 决策：从 SlimPajama-627B 改为 wikitext-103，因 SlimPajama 在 HF Hub 不可用）
- Checkpoint 目录模板：/root/distill_sparse_swiglu/checkpoints/{exp_id}
- 日志目录模板：~/runs/distill_sparse_swiglu/{exp_id}.log
- GPU：2× RTX PRO 6000 Blackwell (98GB each, compute cap 12.0)
- 活跃进程：无（mvp_bce_s42 刚退出，mvp_kl_s42 未在跑）

### 3. 📊 当前状态
**刚做完**：收到 mvp_bce_s42 的 CRON 完成回调（进程正常退出），已派 Worker `worker_analyze_mvp_bce_s42_20260515T122609` 去读日志分析结果，Worker 状态=running。

**正在跑的 Worker**：
- `worker_analyze_mvp_bce_s42_20260515T122609`（running）— 分析 mvp_bce_s42 日志和 checkpoint
- `worker_fix_mvp_kl_oom_20260515T122135`（running）— 修复 KL loss 的 OOM 问题（加 gradient checkpointing 或 batch_size=1+grad_accum=4）

**Registry 状态**：
| exp_id | status | 摘要 |
|--------|--------|------|
| mvp_bce_s42 | ANALYZING | 进程已退出，等分析 Worker 返回结果 |
| mvp_kl_s42 | PREPARING | retry=2, OOM 修复 Worker 在跑 |
| mvp_kl_s123 | QUEUED | 等 KL OOM 修复后提交 |
| mvp_bce_s123 | QUEUED | 可立即提交（cuda:1） |
| mvp_kl_s456 | QUEUED | 等 KL OOM 修复后提交 |
| mvp_bce_s456 | QUEUED | 可立即提交（cuda:1，排在 bce_s123 后） |

**等待中**：2 个 Worker 回调（analyze + fix_oom），无 Director 决策待回复。

**两块 GPU 都空闲** — analyze Worker 回调后应立即提交 mvp_bce_s123（cuda:1），fix_oom Worker 回调后提交 mvp_kl_s42 retry（cuda:0）。

### 4. 📋 待办
- analyze Worker 返回 mvp_bce_s42 成功 → update_registry(status=DONE, conclusion=success) + 记录 metrics + 立即 submit mvp_bce_s123 到 cuda:1 + 汇报 Director
- analyze Worker 返回 mvp_bce_s42 失败（EXIT_CODE=1）→ update_registry(conclusion=failed) + 诊断原因 + 汇报 Director
- fix_oom Worker 完成 → 用修复后的代码 submit mvp_kl_s42 到 cuda:0（batch_size=2, grad_accum=2）
- mvp_kl_s42 成功 → 提交 mvp_kl_s123 和 mvp_kl_s456（串行共用 cuda:0）
- 6 个实验全部 DONE → 计算 3-seed 均值对比（KL ppl vs BCE ppl），按 ROADMAP pass/fail 标准判定 MVP 结果
- MVP PASS（KL ppl < BCE ppl ≥ 0.3）→ 写 paper_framing.md + experiment_plan.yaml，进入 Post-MVP Phase 1
- MVP FAIL → 产出 Framing 调整提案，等 Director 决策

### 5. 🎯 战略上下文
- **核心假设**：KL 训练的 predictor 通过端到端梯度流捕获联合神经元交互，在 50% sparsity 下优于 BCE 的逐神经元独立目标
- **D001**：MVP 设计确定（KL vs BCE @ 50% sparsity, Llama 3.1 8B）
- **D002**：数据集从 SlimPajama-627B 改为 WikiText-103（SlimPajama 不可用）
- **DDL**：EMNLP 2026 ARR 截止 2026-05-25，还剩 10 天
- **易踩坑**：
  - registry 里 mvp_bce_s42 的 `failure_reason` 字段是第一次失败（DatasetNotFoundError）的残留，不代表当前 run 的状态。当前 run 的真实结果要看日志
  - KL 实验 OOM 是已知问题（端到端反向传播存储 32 层激活），修复方案是 gradient checkpointing + 小 batch。QUEUED 的 KL 实验 spec 里 batch_size=4 是旧值，提交时必须用修复后的参数
  - BCE 实验可以 batch_size=4 正常跑，KL 不行——两者资源需求不对称


---
