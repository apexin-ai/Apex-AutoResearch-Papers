# agent / loop_7.md

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_7.md`
- **Structured JSON:** [`b473891eb5543d0c4f53.json`](../../sessions/b4/b473891eb5543d0c4f53.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: idle_timeout
updated: '2026-05-16T16:55:29+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单仅 westd-34887 的 **cuda:0 + cuda:1**，绝不能用其他卡
- 所有训练命令必须带 `WANDB_MODE=offline`（服务器无 wandb API key，不加直接崩）
- KL PPL 论文引用统一用 **4-seed mean 12.00±0.07**，禁用单 seed 最佳值 11.91
- BCE framing 禁止用 "anti-learning"，必须用 **"objective mismatch"**
- SPON framing 禁止 "KL subsumes SPON"，用 **"marginal complement"**
- D032 TEAL 30% PPL = **8.98** 是正确值，13.63 是 50% target 错误修正已撤回
- submit_training_job 必须自带环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`

### 2. 🖥️ 基础设施快照
- **服务器**: westd-34887，工作目录 `/root/distill_sparse_swiglu/`
- **Python**: `/root/miniconda3/bin/python`（conda base，不是 venv）
- **模型**: Llama-3.1-8B at `/root/autodl-tmp/models/llama-3.1-8b/`，Mistral-7B at `/root/autodl-tmp/models/mistral-7b/`
- **Checkpoints**: KL30%=`checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt`，KL40%=`checkpoints/kl_sparsity40_s42/predictor_kl_normalized.pt`，KL50%=`checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt`
- **活跃进程**:
  - bench_kl50_uniform: PID 229957, cuda:0, 50% KL uniform benchmark eval
  - bench_kl40_global: PID 230101, cuda:1, 40% KL global benchmark eval
- **提交时间**: 12:20 UTC，预计 75-120min 完成（约 13:35-14:20 UTC）
- **累计 GPU·h**: ~92h / 预算 ~196h

### 3. 📊 当前状态
刚完成 bench_teal30 + bench_teal50 的分析和 Director 汇报。已向 Director 发送完整 Table 1 对比表（8/10 格已填），请求下一批实验优先级。

- **RUNNING (2)**: bench_kl50_uniform (cuda:0), bench_kl40_global (cuda:1)
- **PREPARING (7)**: kl_lagrangian_v2, kl_norm_v3_quicktest, mvp_kl_norm_s456, spon_kl_s42, diag_30pct_downstream, diag_gsm8k_gencomp, diag_teal_downstream
- **等待**: Director 回复下一批实验优先级；两个 bench 的 cron 回调

### 4. 📋 待办
- bench_kl50_uniform 完成 → 记录 metrics → Table 1 uniform 列完整（预期：50% uniform 仍 catastrophic）
- bench_kl40_global 完成 → 记录 metrics → Table 1 global 列完整 → **3×2 matrix 全部齐备**
- 两个都完成 → 两块 GPU 空闲 → 等 Director 指示下一批（已发请求）
- Director 回复 → 从 PREPARING 中选实验提交（建议 P0: diag_30pct_downstream / diag_teal_downstream）
- 全 matrix 齐备 + Director 同意 → spawn Worker 开始写 Results section

### 5. 🎯 战略上下文
**Table 1 已收集数据**:
| 条件 | PPL | ARC | WG | MMLU | GSM8K |
|------|-----|-----|-----|------|-------|
| Dense | 6.12 | 58.3 | 78.1 | 65.3 | 48.8 |
| TEAL 30% | 10.97 | 42.3 | 66.1 | 38.6 | 7.9 |
| TEAL 50% | 23.31 | 28.4 | 53.0 | 28.3 | 2.0 |
| KL 30% global | 8.98 | 39.7 | 70.2 | 25.3 | 8.8 |
| KL 30% uniform | 8.82 | 40.8 | 68.6 | 40.6 | 7.4 |
| KL 40% uniform | 8.36 | 41.8 | 67.2 | 30.7 | 3.9 |
| KL 50% global | 11.79 | 32.9 | 63.5 | 27.9 | 1.3 |
| BCE 50% | 22.51 | 24.0 | 50.6 | 30.0 | 4.9 |

**核心结论链**: KL>>TEAL on PPL → uniform 修复 MMLU at 30% → 40% phase transition → 50% 不可救

**易踩坑**:
1. global top-k 和 uniform allocation 的结果不能混在一起比——它们是不同推理协议
2. TEAL vanilla 30% MMLU=38.6% 比预想好——但 PPL 差距仍然显著（10.97 vs 8.82）
3. 50% 不要再试任何 allocation 方法——已验证三种方法全部崩溃
4. DDL 2026-05-25（剩 9 天），Table 1 完成后立即转论文写作
5. Mistral 数据疑似污染（D032），暂不引用


---
