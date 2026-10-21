# agent / loop_15.md

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_15.md`
- **Structured JSON:** [`7ba6af613d7081fedbd7.json`](../../sessions/7b/7ba6af613d7081fedbd7.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 15
reason: idle_timeout
updated: '2026-05-21T01:38:17+00:00'
---

### 1. 🔴 硬约束 / 红线
- westd-17855 GPU 白名单: cuda:0-5（6卡全分配）；westd-19828 GPU 白名单: cuda:0-1（2卡）
- 所有训练必须 fp32（D079: 小模型≤3B fp32），bf16 仅用于特定已批准实验
- 分析管线硬约束: D105 全局 true 3σ + D086 BH FDR n_perm=5000 + D102 统一 8-pair + D111 peak_lag<0
- submit_training_job 命令必须自带环境激活: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- GPU 编号始终从 0 开始（框架自动注入 CUDA_VISIBLE_DEVICES）
- v3_d080 变体数据已从 dose-response 主图排除（D125）

### 2. 🖥️ 基础设施快照
- **westd-17855**: 6× RTX PRO 6000 Blackwell (98GB)，工作目录 `/root/autodl-tmp/distrib_canary_collapse`
  - Python: `/root/miniconda3/bin/python`，conda base 环境
  - 活跃进程: smollm3_3b_s43(cuda:3,PID211078), alpha_sweep_a045_s43(cuda:0,PID280215), alpha_sweep_a060_v4(cuda:5,PID295535), t20_a100_s42(cuda:2,PID301936), t20_a050_s42(cuda:1,PID302503), t20_a060_s42(cuda:4,PID311201)
- **westd-19828**: 2× RTX PRO 6000 Blackwell (98GB)，同路径
  - 活跃进程: scale_14b_a050_s42(cuda:1,PID538774)
  - cuda:0 刚释放（data_strategy_ablation_s43 完成）
- HF cache: `/root/autodl-tmp/.hf_cache`，TRANSFORMERS_OFFLINE=1
- 磁盘: 两台服务器 /usr/bin/nvidia-smi 分区 ~816-817GB 可用（3% 已用）

### 3. 📊 当前状态
**刚做的**: data_strategy_ablation_s43 (accumulate α=0.50 s43) CRON 回调到达，已派 Worker `worker_analysis_data_strategy_ablation_s43_20260520T092916` 去 westd-19828 分析结果。**Worker 尚未回调**。

**RUNNING 实验** (7个):
| exp_id | server:gpu | 摘要 |
|--------|-----------|------|
| smollm3_3b_wiki_a100_s43_fp32 | 17855:cuda:3 | SmolLM3-3B cross-seed s43, Table 7 |
| scale_14b_a050_s42_fp32 | 19828:cuda:1 | Pythia-1.4B α=0.50 boundary regime |
| alpha_sweep_a045_s43_fp32 | 17855:cuda:0 | onset boundary cross-seed |
| alpha_sweep_a060_s42_fp32_v4 | 17855:cuda:5 | D125 替代 v3_d080 |
| t20_a100_s42_fp32 | 17855:cuda:2 | T=20 extended α=1.0 |
| t20_a050_s42_fp32 | 17855:cuda:1 | T=20 extended α=0.50 onset |
| t20_a060_s42_fp32 | 17855:cuda:4 | T=20 extended α=0.60 dip |

**PREPARING** (7个): generalize_pythia1b_c4_a100_s43_v2, alpha_sweep_a010_s42_bf16, scale_14b_a050_s42_bf16, interv_react_s43, gen_gpt2m_a100_s43, qwen35_dryrun_launch, scale_69b_a100_s43_fp32

**等待中**:
- Worker `worker_analysis_data_strategy_ablation_s43` 回调 → 分析 accumulate s43 结果
- 7 个 RUNNING 实验的 cron 监控（reconcile 确认全部 still running）

### 4. 📋 待办（条件触发式）
- Worker analysis s43 回调 → 读分析报告 → update_registry(conclusion=success/negative, metrics) → 与 s42 对比 → 汇报 Director（s42: accumulate PermG=0/8 vs replace 6/8，核心问题是 s43 是否一致）
- alpha_sweep_a045_s43 完成 → 分析 onset boundary cross-seed → 更新 Table 7 dose-response
- alpha_sweep_a060_v4 完成 → 替代 v3_d080 → 补 dose-response α=0.60 数据点
- t20 三个实验完成 → D127 Track G TE reanalysis + 检验 PermG 在长序列下是否保持/增强
- smollm3_3b_s43 完成 → Table 7 SmolLM3 cross-seed 行
- scale_14b_a050 完成 → 1.4B scale boundary regime 验证
- westd-19828:cuda:0 已空闲 → 可排 PREPARING 队列中的实验（优先 scale_69b_a100_s43_fp32 或 interv_react_s43）
- D127 A-G 分析战线完成 → 整合到论文 narrative

### 5. 🎯 战略上下文
- **目标**: EMNLP 2026 ARR June cycle，~24 天
- **核心 framing**: PermG-primary + mechanistic explanation + predict-then-verify。PermG null FPR=0/24(唯一0%)是最强卖点
- **Dose-response 4-regime**: Blind(≤0.45)→Onset(0.50)→Sync collapse(~0.60 dip)→Detection(≥0.75)。α=0.60 的 PermG 非单调 dip 是 D108/D119 确认的 robust 现象
- **D128**: Dual-Canary Detection Hierarchy 框架 — data_strategy_ablation 是其中关键证据（accumulate 抑制 lead-lag = V-shape recovery breaks temporal coupling）
- **Table 7 状态**: 14/17 行完成，SmolLM3 s43 + 1.4B boundary 在跑
- **易错点**:
  - data_strategy_ablation 对比时注意：s43 的 replace 基线是 alpha_sweep_a050_s43_fp32（PermG=6/8），不是 s42 的 replace
  - SmolLM3 是已知 failure mode（entropy-diversity decoupling），不要按正常模型解读
  - TY Granger 已降级为 supplementary（D121/D123），PermG 是 primary
  - v3_d080 数据已排除（D125），不要引用


---
