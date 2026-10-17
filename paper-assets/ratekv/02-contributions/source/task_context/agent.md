---
loop: 12
reason: idle_timeout
updated: '2026-05-16T05:26:50+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 **仅 cuda:0, cuda:1**（westd-37397），其他设备号禁用
- 论文锁定值：Qwen concentration=0.61 (float32, commit bfaea4e)，Mistral concentration=0.24/t1t5=0.41 (hires, commit e52fb0e)——改这些数字需 Director 审批
- Diagnostic 分类条件：concentration ≥0.50 AND t1/t5 ≤0.70 → Spread，当前 **9/9 准确率**，修改规则需全量重验
- **W2/W9 系列 eval 必须用 WikiText-2 test set**，不用 calibration data（之前出过 eval data 污染 bug）
- hellaswag metric 统一为 **acc,none**（≈0.59），不是 acc_norm（≈0.77）
- Gemma-2 有 BOS cold-start bug（无 BOS 的 cold chunk PPL=780），Table 2 数字可能受影响，重跑前需用 sliding window + prepend BOS 修复
- submit_training_job 注入 CUDA_VISIBLE_DEVICES，脚本内 device 必须写 `cuda:0`（逻辑编号，不是物理编号）

### 2. 🖥️ 基础设施快照
- **服务器**：westd-37397，2× RTX PRO 6000 98GB
- **工作目录**：`/root/ratekv`
- **Python**：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- **环境激活**：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **HF cache**：`/root/autodl-tmp/.hf_cache`（如果是 AutoDL；westd 可能不同，需 Worker 确认）
- **Profile 文件路径约定**：Llama standard profile = `llama_profiling_results.json`（不是 `llama_ppl_profiles_hires.json`）
- **活跃进程**：无 GPU 训练在跑（report.md 运行中 = 无）
- **活跃 Worker**：`worker_ops_check_multiseed_status_20260516T052517`（running，12 turns，SSH 检查 multi-seed 状态，可能卡在 shell metacharacter 问题）
- **活跃 Cron**：无（reconcile 返回 0）

### 3. 📊 当前状态
**刚完成的**：CodeLlama constrained MCKP（negative，确认 Spike，9/9 diagnostic）+ Mistral 8K eval（negative，Flat 无 long-context benefit）。Dream 评分 best 3.5/6，Dream 后补实验冲刺已启动。

**Registry 概览**：119 DONE（65 success / 22 negative / 13 failed），4 PREPARING，1 PENDING。

**非 DONE 实验**：
| ID | 状态 | 摘要 |
|---|---|---|
| mistral_multi_seed_ppl | PENDING | Mistral 3-seed PPL，等人工审批 |
| mistral_multi_seed_ppl_v2 | PREPARING | Mistral 3-seed v2（修 CUDA_VISIBLE_DEVICES） |
| llama_multi_seed_ppl | PREPARING | Llama 3-seed PPL |
| yi_8k_eval | PREPARING | Yi-1.5-9B 8K long-context eval |
| phi3_medium_hires_profiling_check | PREPARING | Phi-3-medium hires profiling 验证 |

**等待中**：Worker 正在 SSH 检查 multi-seed 代码/环境状态（12 turns，可能遇到 shell metacharacter 阻塞）。无 Cron 回调待处理。两张 GPU 当前空闲。

### 4. 📋 待办（条件触发式）
- Worker `check_multiseed_status` 完成 → 根据结果决定：代码就绪则提交 mistral_multi_seed_ppl 审批 / 代码有问题则派修复 Worker
- mistral_multi_seed_ppl 审批通过 → submit_on_allocated 到 cuda:0 或 cuda:1
- Multi-seed PPL 全部完成（Mistral + Llama + Yi + Gemma-2）→ 更新 Table 2 error bars，向 Director 汇报统计显著性
- yi_8k_eval 就绪 → 提交到空闲 GPU，预期 negative（Spike 无 long-context benefit，作为 Spread-specific claim 的对照）
- **两张 GPU 空闲 = 失职**——接手后立即铺实验：ROADMAP Phase 2（4 models × 3-seed）优先，两卡并行跑不同模型
- Compounding sweeps（Yi/Gemma-2/CodeLlama/Phi-3/InternLM2）和 C4 cross-dataset（3 models）排在 multi-seed 之后
- 论文修复（理论 toy model §3.X、compounding figure 移入正文、symmetric-only deployment 举例）需 Director 确认优先级

### 5. 🎯 战略上下文
**核心结论链**：2-bit compounding 是跨架构通用失败模式 → cardinality constraint 是通用修复 → non-uniform allocation 仅对 Spread 模型（1/9）有效 → 大多数模型应直接用 uniform 4-bit。这是 "compounding-forward" framing（D068 Dream 确认优于旧 framing）。

**ARR May 25 倒计时 ~9 天**。Dream 评估 gap：multi-seed null results + CodeLlama E2E（已完成）+ Qwen-centric ablations + 无理论模型。Pipeline 估算 ~12h wall time（两卡并行），预算充裕但 GPU 空闲 = 浪费。

**易错点**：
- mistral_multi_seed_ppl 和 mistral_multi_seed_ppl_v2 是两个实验——v2 修了 CUDA_VISIBLE_DEVICES bug，v1 可能需要 cancel 或合并
- 非 Qwen 模型用 merged profile → 3-seed MCKP allocation 完全相同 → Table 4 不报 ±std（只有 Qwen 报，反映 calibration seed 方差）
- CodeLlama 是 MHA（1024 KV heads），concentration 高但 t1/t5=0.81 → Spike 不是 Spread。高 concentration + 高 t1/t5 = 单头主导
- Spread 模型搜索：少 KV heads + 高 GQA ratio 是关键。InternLM2-7B（GQA 4:1, 256 heads）是当前最佳候选但尚未验证
- 决策 D063：Table 4 统一用各模型 optimal k（与 Table 1 一致），否决了统一 k=8 方案
