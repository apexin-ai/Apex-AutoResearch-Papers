# agent / loop_5.md

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_5.md`
- **Structured JSON:** [`cbc8fb8ea88fcc0e7680.json`](../../sessions/cb/cbc8fb8ea88fcc0e7680.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: idle_timeout
updated: '2026-05-14T18:29:33+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-37397 的 cuda:0 和 cuda:1（config gpu_ids 白名单）
- Qwen/Llama/Mistral 现有结果**不要重跑**——bf16 截断 bug 仅影响 GQA≤2:1 模型（Gemma-2/Yi-1.5），GQA≥4:1 的 2-bit delta 足够大不触发截断（D046 确认）
- 论文正文表格统一使用 **standard profiling** 数据（MCKP PPL=11.23），hires profiling（10.91）只在 profiling resolution ablation 中展示（D033/D034）
- Table 1 使用 **per-model optimal k**（Qwen k=8, Llama k=2, Mistral k=4），不用 fixed k（D037）
- 禁止引用 exp_e 的绝对 PPL（eval pipeline 不一致，baseline 8.82 vs 统一 pipeline 9.81）——用 hires_mckp_reeval 的 10.9131
- ssh_execute 有 30 秒硬超时，模型下载等长操作必须用 tmux 脚本方案

### 2. 🖥️ 基础设施快照
- 服务器：westd-37397，2× RTX PRO 6000 96GB
- 工作目录：/root/ratekv
- Python：/root/miniconda3/bin/python（conda base 环境，不是 venv）
- 环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- HF cache：/root/autodl-tmp/.hf_cache（必须设 HF_HOME）
- 模型缓存：Qwen2.5-7B、Llama-3.1-8B、Mistral-7B-v0.3、Gemma-2-9B、Yi-1.5-9B 均在 /root/autodl-tmp/.hf_cache/
- W&B：本项目不使用 W&B（短 eval 实验，cron 用 sentinel file 检测完成）
- 活跃进程：qwen25-hires-profiling（PID 246442，cuda:0，tmux session）；yi15_9b_full_pipeline（PID 229912，cuda:1，但 D047 已有分析结果，大概率已完成待状态更新）
- Cron：当前无活跃 cron（reconcile 返回 0）
- Worker：当前无活跃 Worker

### 3. 📊 当前状态
**刚做完**：D047 Yi-1.5-9B 分析（GQA 8:1 FAIL，反证 GQA-ratio proxy，spike vs spread insight），D048 发现 Qwen hires profiler 有同样 bf16 bug。

**正在跑**：
- `qwen25-hires-profiling`（cuda:0，PREPARING 状态）：D048 紧急验证——hires_quant_profiler.py 修复 bf16 bug 后 float32 重跑。预计 ~60min。**这是 Claim 3 的生死验证**：如果 float32 concentration > 0.50 → 安全；< 0.50 → Claim 3 (0.50 threshold diagnostic) 崩溃
- `yi15_9b_full_pipeline`（cuda:1，registry 显示 RUNNING）：D047 已有完整分析结果，registry 状态可能未更新为 DONE

**等待中**：
- D048 结果回调（qwen25-hires-profiling 完成时）
- Group C 审稿报告回传
- yi15 registry 状态需更新（有结论但 status 仍 RUNNING）

**已 killed/deferred**：cross_domain_calibration_v2、greedy_constrained_ablation、qwen72b_profiling（磁盘不足）

### 4. 📋 待办（条件触发式）
- qwen25-hires-profiling 完成 → 读 float32 concentration 值：
  - concentration > 0.50 → Claim 3 安全，更新 paper_framing.md 用 float32 数字，minor wording fix
  - concentration < 0.50 → Claim 3 需重构（降阈值 / 换 metric / 连续关系 framing），产 Framing 提案给 Director
- yi15_9b_full_pipeline → 更新 registry status=DONE，conclusion=negative，写入 metrics（D047 已有数据：Top-5%=0.4934, MCKP PPL=7.31, uniform=7.22）
- D048 结果确定后 → 派 Worker patch 论文：D047 Yi-1.5 反例 + spike-vs-spread 分析 + D048 concentration 修正
- Group C 审稿报告到达 → 按意见排优先级处理
- report.md 需刷新（当前内容过时）

### 5. 🎯 战略上下文
**项目核心结论**：cardinality constraint（≤k heads at 2-bit）是唯一贡献——让 greedy 和 MCKP 产出完全相同的最优解（Δ=0.0000）。效果是 architecture-dependent：高 concentration 模型（Qwen）受益 27.3%，低 concentration 模型（Gemma-2/Mistral/Yi-1.5）无益。Top-5% concentration > 0.50 作为诊断指标 5/5 正确分类。

**决策链关键节点**：D007(pivot 放弃 eviction) → D009(cardinality constraint 提出) → D010(MVP PASS) → D019/D020(solver equivalence, constraint is THE contribution) → D047(Yi-1.5 反证 GQA proxy) → D048(concentration 可能被虚高)

**最容易判断错的事**：
1. **D048 是真正的 blocker**——不要在 D048 结果出来前动 paper 的 Claim 3 相关内容。float32 concentration 如果从 0.59 跌到 0.42，整个 0.50 threshold narrative 崩塌
2. **Yi-1.5 registry 状态落后**——看起来 RUNNING 但实际已完成分析（D047）。不要再派 Worker 去查它的进度，直接更新 registry
3. **不要混淆 standard vs hires profiling 数字**——论文主表用 standard（11.23），ablation 用 hires（10.91）。混用已被 Reviewer CRITICAL 过两次（D033/D034）
4. **deadline 紧迫**：EMNLP ARR May 25, 距今 11 天。全部 P0/P1 实验已完成，当前瓶颈是 D048 验证 + 论文 patch + Group C 审稿


---
