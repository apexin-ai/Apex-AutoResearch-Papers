# agent / loop_12.md

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_12.md`
- **Structured JSON:** [`35a060ae4d6c56ce8175.json`](../../sessions/35/35a060ae4d6c56ce8175.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 12
reason: idle_timeout
updated: '2026-05-16T05:26:23+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 **只有** westd-37397 的 cuda:0 和 cuda:1（RTX PRO 6000 96GB×2）。不可用其他设备
- PPL 评估 **必须用 WikiText-2 test set**，不用 calibration data（W2/W9 事故教训）
- 论文锁定值：Qwen concentration=0.61 (float32, commit bfaea4e)，Mistral concentration=0.24/t1t5=0.41 (hires, commit e52fb0e)
- Diagnostic 分类规则：concentration ≥0.50 AND t1/t5 ≤0.70 → Spread。当前 9/9 准确率，**不可随意改阈值**
- Table 4 error bar：只有 Qwen 行报 ±std（calibration seed 方差），其他模型报单值（deterministic allocation）
- hellaswag metric 统一用 `acc,none`（≈0.59），不是 `acc_norm`（≈0.77）
- Gemma-2 eval 必须 prepend BOS + overlapping sliding window（cold-start bug），旧 constrained 数字可能需重验
- submit_training_job 脚本内 device 写 `cuda:0`（框架注入 CUDA_VISIBLE_DEVICES 做物理→逻辑映射）

### 2. 🖥️ 基础设施快照
- 服务器：**westd-37397**，工作目录 `/root/ratekv`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- 环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型缓存：服务器上（具体路径需 SSH 确认，HF cache 在 `/root/.cache/huggingface` 或类似）
- W&B：已配置（项目内多个实验有 W&B metrics）
- 活跃进程：**无**（所有实验已完成或停止，0 running，0 cron，0 worker）
- 本地代码仓：`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/`
- 论文目录：`docs/paper/`（LaTeX，main.tex 为主文件）

### 3. 📊 当前状态
**所有 GPU 空闲，所有 Worker 已销毁，无 cron 监控。** 这是 handoff 前的静止状态。

Registry 总览：119 实验（65 success / 22 negative / 13 failed），**0 RUNNING**。

PREPARING 但未提交的实验（需要接手推进）：
- `mistral_multi_seed_ppl_v2`：Mistral 3-seed PPL 重试（v1 因 CUDA_VISIBLE_DEVICES 映射失败）
- `llama_multi_seed_ppl`：Llama 3-seed PPL
- `yi_8k_eval`：Yi-1.5-9B 8K long-context eval（Spike 控制组）
- `phi3_medium_hires_profiling_check`：已 killed，忽略

PENDING（卡住）：
- `mistral_multi_seed_ppl`：failed，已被 v2 替代

**距 ARR May 25 投稿约 9 天**。Dream 评分 best 3.5/6，核心差距：multi-seed null results + compounding sweeps（5架构）+ C4 cross-dataset（3模型）+ Llama budget sweep + 论文理论 toy model。

### 4. 📋 待办（条件触发式）
- **立即**（无阻塞）→ 并行 spawn Workers 提交 mistral_multi_seed_ppl_v2 + llama_multi_seed_ppl + yi_8k_eval 到 cuda:0/1，两卡流水线排满
- multi-seed PPL 完成（Mistral/Llama）→ 继续 Yi/Gemma-2 multi-seed → 汇总 Table 2 seed std 确认 null results 统计鲁棒
- yi_8k_eval 完成 → 对比 Qwen 8K/Llama 8K，确认 Spike 无 long-context MCKP 收益 → 更新论文 long-context section
- 4 模型 multi-seed 全部完成 → 启动 5 架构 compounding sweeps（Yi/Gemma-2/CodeLlama/Phi-3/InternLM2）
- compounding sweeps 完成 → C4 cross-dataset（3 models）+ Llama budget sweep（2×/4×/8×）
- 所有实验完成 → 论文修复（理论 toy model §3.X / compounding figure 移正文 / symmetric-only deployment 举例 / solver equivalence 扩展到 Yi/Gemma-2）
- **Negative 结果**出现 → 必须产 Framing 提案，不可默默跑下一个

### 5. 🎯 战略上下文
**核心 framing（compounding-forward）**：2-bit compounding 是跨架构通用失败模式（8/8 unconstrained solver 全 fail），cardinality constraint 是通用修复（greedy=MCKP，Δ=0.0000），non-uniform allocation 仅 1/9 模型（Qwen Spread）有效。

**关键决策链**：
- D062：Round 2 审稿后全面 reframing（claim 降级为 diagnostic + compounding discovery）
- D068：Dream 确认 compounding-forward framing 优于旧 framing
- D069：CodeLlama 确认 Spike → 9/9 diagnostic accuracy（从 8/8+1predicted 升级为全实验确认）

**最容易判断错的事**：
1. **不要以为 concentration 高就是 Spread**。CodeLlama concentration=0.80 但 t1/t5=0.81 → Spike（单头主导）。必须两个维度同时满足
2. **不要给非 Qwen 模型加 ±std error bar**。它们的 MCKP allocation 是 deterministic（单次 profiling → 固定分配），seed 只影响 eval 噪声
3. **48h pipeline 估算约 12h wall time（两卡并行）**，距 deadline 9 天，时间充裕但不能拖——Dream 评分只有 3.5/6，每一格 coverage 都影响接受率
4. **Gemma-2 数据有 BOS bug 隐患**，旧 constrained 实验可能需要用修复后的 eval 重验
5. **Spread 模型搜索**：Qwen-7B 是唯一确认 Spread。寻找第二个应看少 KV heads + 高 GQA ratio 架构（InternLM2-7B GQA 4:1, 256 heads 是最佳候选），但这是观察项不是必做项


---
