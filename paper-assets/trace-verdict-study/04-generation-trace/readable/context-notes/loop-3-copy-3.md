# reviewer / loop_3.md

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_3.md`
- **Structured JSON:** [`198d25b35e5878d6631c.json`](../../sessions/19/198d25b35e5878d6631c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 3
reason: max_wall_time
updated: '2026-05-15T14:51:12+00:00'
---

### 1. 🔴 硬约束 / 红线
- 项目 GPU 白名单：westd-11235 的 cuda:0 和 cuda:1，不可使用其他 GPU
- DeepSeek 实验使用旧版 train_sft.py（无 load_best_model_at_end），Qwen 实验也是——两组实验必须在相同代码版本下对比，不可中途改训练配置
- evaluate.py 的 CVD guard 已修复（line 126-127），不可回退；同理 train_sft.py line 89-90、calibration.py line 278-279 和 345-346
- DeepSeek 预训练数据量是 **2T tokens**（不是 1.17T），5.5T vs 2T = 2.75x 差距。此数字已被我审查修正，不可再用错误数值

### 2. 🖥️ 基础设施快照
- 服务器：westd-11235 (root)，2× NVIDIA RTX PRO 6000 Blackwell 98GB，CUDA 12.8
- 工作目录：`/root/trace-verdict-study`（远程代码）；本地 workspace `/home/ubuntu/.agent-ml-research-idea_gen_0509_4/projects/trace-verdict-study/`
- Python：`/root/miniconda3/bin/python`，激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型路径：Qwen `/root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct`；DeepSeek `/root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct`
- 数据：`/root/autodl-tmp/trace-verdict-study-data/{condition}_{train,test}.jsonl`（4720 train / 1190 test）
- Checkpoints：`/root/autodl-tmp/trace-verdict-study-checkpoints/{condition}/`
- HF cache：`/root/autodl-tmp/.hf_cache`
- W&B project：`trace-verdict-study`

### 3. 📊 当前状态
**刚完成**：系统性审查 — 跨模型差异对 claim 结构的影响（已 post 给 Director），含 Q1/Q2/Q3 三问回答。

**RUNNING**：
- `deepseek_exception_only_seed42`（cuda:1，step ~224/444 epoch 2，~14s/step，预计 ~1h 内完成）——**最关键实验**，决定 Claim 1/3 措辞
- `deepseek_full_trace_seed42`（cuda:0，step ~129/444 epoch 1，~36s/step，预计 ~3-4h）

**PREPARING**：
- `vota_seed456`（等 GPU 空闲）

**已审查的 Worker 输出今日汇总**：CVD 修复 ✓、analysis.md 过拟合修正 ✓、文献扫描（26→31 篇）✓、作者/arXiv ID 补全 ✓、DeepSeek pairwise bootstrap ✓、epoch1 eval（78.2% < epoch3 84.5%）✓、eval_qwen_epochs.sh（有 bug 未修）、save_predictions 功能 ✓、孤儿进程清理 ✓

### 4. 📋 待办（条件触发式）
- `deepseek_exception_only_seed42` 完成 → **立即审查**。若 ≥95%：Claim 1 "exception dominance generalizes"；若 85-95%：需 qualify "model-dependent"；若 <85%：Claim 1/3 需 major revision。这是论文 framing 的关键决策点
- `deepseek_full_trace_seed42` 完成 → 审查跨模型 gradient（no_trace < full_trace < VOTA 排序是否在 DeepSeek 上复现）
- `eval_qwen_epochs.sh` 执行 → 审查结果前确认 bug 已修（`d['metrics']['accuracy']` 而非 `d['accuracy']`）
- Director 派 plan_005（第二任务）Worker → 审查数据集选择和 VOTA 格式适配
- Qwen epoch-level eval 完成 → 审查 eval_loss/accuracy 解耦是否在 Qwen 上也成立

### 5. 🎯 战略上下文
**核心结论链**：no_trace (75.1%) < full_trace (81.8%) < VOTA (99.2%) on Qwen。Exception_only (99.83%) 是主信号。ae_only (99.92%) 统计等价。Loop_only (85.6%) 是 Tier 2。Label-only loss 量化 gradient dilution 占 gap 的 26%。

**跨模型**：DeepSeek no_trace (73.4%) ≈ Qwen no_trace (75.1%)，但 DeepSeek VOTA (84.5%) << Qwen VOTA (99.2%)。差距来自 trace utilization efficiency，不是基础能力。假说是 pre-training data scale（5.5T vs 2T）+ CRUXEval gap（15-17pp ≈ VOTA gap 14.7pp），但**必须标记为 hypothesis**。

**最容易判断错的事**：
1. **eval_loss 不代表分类性能**——epoch 1 eval_loss 最低但 accuracy 最差（78.2% vs 84.5%）。不要用 eval_loss 选 checkpoint
2. **analysis.md 曾有错误的"过拟合"结论**——已修正，但如果看到旧版本不要信
3. **Qwen 实验的 paired bootstrap 和 DeepSeek 的 unpaired bootstrap 方法不一致**——论文里不能混用而不注明
4. **plan_007 (calibration) 其实已做完**（registry: calibration_analysis_seed42 DONE），只是 experiment_plan.yaml 里 registry_id=null 没绑定
5. **vota_seed123 failed 是 OOM（CVD bug 导致 GPU 碰撞）**，不是 seed 不稳定。修复后未重跑


---
