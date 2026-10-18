# reviewer / loop_11.md

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_11.md`
- **Structured JSON:** [`7cd98d83300a743f3ab9.json`](../../sessions/7c/7cd98d83300a743f3ab9.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: max_wall_time
updated: '2026-05-15T22:54:09+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 westd-37397 无显式 gpu_ids 约束，但当前惯例是 CUDA_VISIBLE_DEVICES 隔离（一个实验一张卡），**不要同时两个进程用同一张 GPU**
- **eval_ppl.patch_attention 只兼容 separate q_proj/k_proj/v_proj 的模型**（Llama/Qwen/Yi/Mistral/Gemma-2）。Phi-3（fused `qkv_proj`）和 InternLM2（fused `wqkv`）需 custom patch_attention，**直接用标准版会 crash**。我已发 CRITICAL 审查，Agent 尚未修复——下一个我必须在实验启动前再次确认修复状态
- Llama 3-seed CI 的 ±std 全为 0（确定性 eval + 固定 allocation），**不要在 Table 4 加 ±0.0**

### 2. 🖥️ 基础设施快照
- 服务器：westd-37397(root)，2× NVIDIA RTX PRO 6000 Blackwell（97887 MiB each）
- 远程代码：`/root/ratekv`，Python：`/root/miniconda3/bin/python`（conda base）
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/`
- HF cache：`/root/autodl-tmp/.hf_cache`，数据盘：`/root/autodl-tmp/`（83G 可用/250G）
- 模型路径：Llama `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B`，Qwen `/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-7B`，CodeLlama `/root/autodl-tmp/.hf_cache/AI-ModelScope/CodeLlama-7b-hf/`
- 活跃进程：**两张 GPU 均空闲**（0%/0MiB）。Phi-3-medium 下载中（PID 379202, ModelScope, ~43%）。InternLM2-7B 下载卡住（PID 379330, xethub 超时，建议改 ModelScope）
- 日志：codellama profiling → `/root/runs/ratekv/codellama_hires_profiling.log`，llama 3seed → `/root/ratekv/llama_3seed_downstream_ci.log`

### 3. 📊 当前状态
**已完成审查**：
- codellama_hires_profiling → **Spike**（c=0.80, t1/t5=0.81, L1H1 delta=22.998）。不是 Spread，搜索继续
- llama_3seed_downstream_ci → 完成，3 seed 结果完全相同（std=0.0），数据与 Table 4 一致。Registry 仍显示 RUNNING，Agent 需更新
- hellaswag metric 审计 → PASS，所有脚本一致用 acc,none
- Gemma-2 downstream v2 → PASS（之前 session 完成）
- 磁盘清理（prov_grounded_uie 68G 删除）→ PASS
- InternLM2/Phi-3 profiling 脚本 → **CRITICAL**（fused QKV 不兼容 eval_ppl.patch_attention）

**Registry RUNNING**：llama_3seed_downstream_ci（实际已完成，待 Agent 更新）

**等待中**：
- Phi-3-medium 下载（ETA ~1h）
- InternLM2-7B 下载修复（需改 ModelScope）
- Agent 修复 InternLM2/Phi-3 profiling 脚本的 fused QKV 问题

### 4. 📋 待办
- InternLM2/Phi-3 profiling 脚本更新通知 → **验证是否使用了 custom patch_attention 处理 fused QKV**，未修复则再发 CRITICAL 拦截
- InternLM2 profiling 完成 → 检查 concentration + t1/t5 → Spread? 若是则是论文最高价值数据点；若 Spike/Flat 则 N=1 困局确认
- Phi-3-medium profiling 完成 → 同上检查 shape 分类
- 若两个都非 Spread → 建议 Director 评估"N=1 是否足够支撑投稿"或继续扩大搜索（OLMo/Baichuan 等）
- 论文章节审查请求到达 → 按 §5 模板执行，先检查 red-section skill 合规

### 5. 🎯 战略上下文
- **核心问题**：论文 7+1 个模型中仅 Qwen-7B 展示 Spread pattern 和 MCKP 有效性（N=1）。Decision rule（c≳0.50 AND t1/t5≲0.70）准确率 8/8 但正样本只有 1 个。审稿人 R1/R2 已给 2.75/5（weak reject），核心攻击点就是 N=1
- **Spread 搜索是最高 ROI 实验**：CodeLlama 已失败（Spike），InternLM2 和 Phi-3 是仅剩机会。10 天内截稿（ARR May 25），GPU 充裕但试错窗口在收窄
- **易错判断**：
  1. 不要因为 concentration 高就预测 Spread——Yi(0.71) 和 CodeLlama(0.80) 都是高 concentration 但 Spike。**必须同时看 t1/t5**
  2. Llama 的 concentration 在 paper_framing.md(0.34) 和 experiments.tex(0.57) 不一致——已发 warning，待 Agent 统一
  3. Greedy = MCKP（delta=0.0000）是论文已承认的事实——贡献是 cardinality constraint 发现，不是 solver 本身
  4. 不要用人类工时直觉判断 deadline 风险——只看 GPU-hours 是否够


---
