# agent / loop_10.md

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_10.md`
- **Structured JSON:** [`c4c10ec43174a86b5b5d.json`](../../sessions/c4/c4c10ec43174a86b5b5d.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: idle_timeout
updated: '2026-05-17T17:32:08+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-34887 cuda:0 + cuda:1（RTX PRO 6000 Blackwell, 95GB each），绝对不能用其他卡
- W&B 被禁用（WANDB_MODE=disabled），所有指标从日志文件读取，不要尝试 fetch_wandb_metrics
- HF_HUB_OFFLINE=1 + HF_DATASETS_OFFLINE=1，模型和数据集必须用本地缓存，不能在线下载
- benchmark_eval.py 的 `--gpu 0` 始终指逻辑 GPU 0（框架映射物理卡），不要改成物理卡号
- 论文数字必须有代码来源（约束 C003），不可凭记忆填数

### 2. 🖥️ 基础设施快照
- 服务器：westd-34887，工作目录 /root/distill_sparse_swiglu
- Python：/root/miniconda3/bin/python（命令前 `cd /root/distill_sparse_swiglu &&` 开头）
- 模型：/root/autodl-tmp/models/llama-3.1-8b
- 数据集：wikitext-103 local, wikitext-2 local, lm-eval cached（HF cache at /root/autodl-tmp/.hf_cache/datasets）
- Checkpoint 目录：/root/distill_sparse_swiglu/checkpoints/kl_30pct_{s42,s123,s456}/
- 日志目录：~/runs/distill_sparse_swiglu/
- 活跃进程：无（双卡空闲）
- Cron：无活跃 cron（reconcile 清理完毕）

### 3. 📊 当前状态
**刚发生**：两个实验同时完成，均转入 ANALYZING：
1. `kl30_s456_train` — seed 456 的 KL 30% predictor 训练（1000 steps）。期望 PPL≈8.97-8.98（对标 s42=8.98, s123=8.97）
2. `kl30_s123_eval` — seed 123 predictor 的 uniform allocation downstream eval（MMLU/ARC/WinoGrande/GSM8K）。期望 MMLU≈0.40（对标 s42 uniform=0.4061）

**正在等**：Worker `worker_analysis_kl30_s456_train_and_s123_eval_20260517T133046` 正在 SSH 读取两个日志提取指标，尚未回调。

**PREPARING 队列**（等 s456 train 确认 success 后链式触发）：
- kl30_s456_uniform_eval — s456 uniform allocation eval
- kl30_s456_global_eval — s456 global allocation eval
- kl50_s456_train / kl50_s456_train_eval / kl50_s123_eval — 50% 的多 seed 补充
- mag_preservation_reg, longbench_dense_v5, kl_lagrangian_v2, kl_norm_v3_quicktest 等

### 4. 📋 待办
- Worker 回调到达（含 PPL/MMLU 指标）→ update_registry(conclusion=success/negative) + 设 checkpoint_path/log_path → 刷新 report.md → 汇报 Director
- kl30_s456_train PPL≈8.97-8.98 confirmed → 立即提交 kl30_s456_uniform_eval + kl30_s456_global_eval（双卡并行，cuda:0 和 cuda:1 各一个）
- kl30_s123_eval MMLU≈0.40 confirmed → 更新论文 Table 5 的 3-seed mean±std 数据，汇报 Director 多 seed 验证完成情况
- 若 s456 PPL 异常偏离（>9.5 或 <8.5）→ 检查训练日志排查问题，negative 走证伪推导流程
- 所有 3 seed eval 完成（s42+s123+s456）→ 计算 mean±std，更新论文 Table 2/5，完成 Claim 3 的多 seed 证据

### 5. 🎯 战略上下文
- **核心 story**：KL distillation 使 SwiGLU LLM 的 contextual sparsity prediction 不需要 error compensation，实现最简推理管线
- **当前阶段**：论文质量提升，EMNLP 2026 ARR May DDL = 2026-05-25（剩 8 天）
- **多 seed 验证目的**：论文 Table 2 和 Table 5 需要 3-seed mean±std 来证明 uniform allocation 的优势不是 seed variance artifact
- **关键数字锚点**：30% KL PPL baseline = s42:8.98, s123:8.97 | 30% uniform MMLU = s42:0.4061, global = s42:0.2527, s123:0.3807
- **易错点**：kl30_s123_eval 用的是 `--allocation uniform`，对比时不要和 global 的结果搞混；Table 2 的 30% KL MMLU 行要同步到 Table 5 的 3-seed 值
- **决策链**：D047 reframe 后 Claim 3 升级为三相框架（budget-surplus/budget-neutral/budget-deficit），uniform vs global 的 MMLU 差异是核心证据
- **Round 1 审稿**：3.0/5，4 critical 已 resolved，2 warning in-progress（SNR patch + λ curve）


---
