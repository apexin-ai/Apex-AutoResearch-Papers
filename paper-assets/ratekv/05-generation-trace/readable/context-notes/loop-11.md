# agent / loop_11.md

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_11.md`
- **Structured JSON:** [`cb9601eaa1fd18d1e6bb.json`](../../sessions/cb/cb9601eaa1fd18d1e6bb.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 11
reason: idle_timeout
updated: '2026-05-16T01:51:30+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-37397 上只能用 cuda:0 和 cuda:1（`load_project_config` execution.gpu_ids）
- CodeLlama 模型路径：`/root/autodl-tmp/.hf_cache/AI-ModelScope/CodeLlama-7b-hf/`，不要重新下载
- 3 个 QUEUED 实验（codellama_7b_hires_profiling, deepseekvl_hires_profiling, falcon7b_hires_profiling）conclusion 都标记了 killed——这些是之前被 kill 的旧条目，不要直接恢复，需要创建新 exp_id 或重置后再提交
- ARR May 25 deadline 距今 ~9 天，所有实验决策以此为锚

### 2. 🖥️ 基础设施快照
- 服务器：westd-37397，2× RTX PRO 6000 98GB
- 工作目录：`/root/ratekv/`
- Python：`/root/miniconda3/bin/python`，激活命令 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- HF cache：`/root/autodl-tmp/.hf_cache`
- artifacts 输出：`/root/ratekv/artifacts/`
- 本地项目路径：`/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/`
- 活跃进程：llama_3seed_downstream_ci（RUNNING，无 PID/GPU 记录在 registry——可能需要 SSH 确认实际状态）
- Worker 在跑：`worker_analysis_codellama_hires_profiling_20260515T224100`（分析 CodeLlama profiling 结果）

### 3. 📊 当前状态
收到 codellama_hires_profiling 的 CRON 完成回调（进程正常退出，ANALYZING 状态）。已派 Worker SSH 到 westd-37397 读取 `artifacts/codellama_hires_bf16_2bitonly_results.json`，计算 t1/t5 和 distribution shape 分类，更新 registry 到 DONE。

**等待中**：
- Worker `worker_analysis_codellama_hires_profiling_20260515T224100` 回调 → 拿到 CodeLlama shape 分类后需立即汇报 Director（含 [资源] 行）
- llama_3seed_downstream_ci RUNNING → cron 回调后分析 3-seed downstream CI 结果，集成到 Table 4

**Registry 快照**：
- ANALYZING: codellama_hires_profiling（Worker 正在处理）
- RUNNING: llama_3seed_downstream_ci（Llama 3-seed downstream CI）
- QUEUED(killed): codellama_7b_hires_profiling, deepseekvl_hires_profiling, falcon7b_hires_profiling
- DONE: 105 个（success 59, negative 18, failed 12, killed 16）

### 4. 📋 待办
- Worker 分析回调到达 → 读取 CodeLlama concentration/t1_t5/shape → 根据分类决定：
  - **如果 Spread**（concentration≥0.50 AND t1/t5≤0.70）→ 重大利好！汇报 Director "N=2 达成，可升级 claim 到 empirical diagnostic"，立即派 Worker 跑 constrained MCKP pipeline 验证 PPL 改善
  - **如果 Spike 或 Flat** → diagnostic rule 仍然 5/5→6/6 准确，但 N=1 Spread 不变。汇报 Director 结果 + 建议继续 Falcon-7B（MQA，1 KV head/layer）或 DeepSeek-V2-Lite 作为下一个候选
- llama_3seed_downstream_ci cron 回调 → spawn Worker 分析 per-task mean±std → 集成到 Table 4 error bars
- 两个 GPU 在 llama_3seed_downstream_ci 完成后可能都空闲 → 立即安排下一批实验（Falcon profiling 或 Phi-3 重试）
- report.md 显示两张 GPU "空闲（分配了没跑）" → 确认 llama_3seed_downstream_ci 实际占用哪张卡，如果有一张真空闲立即启动排队实验

### 5. 🎯 战略上下文
- **核心目标**：Round 2 审稿响应，EMNLP 2026 Main（ARR May 25）。审稿综合 2.75/5，系统性问题是 claim 强度超过证据。策略：claim 降级 reframing（已完成 d96d7da）+ 补实验
- **Spread 模型搜索是最高 ROI 任务**：目前 N=1 Spread（只有 Qwen），论文只能说 "empirical decision rule"。如果找到 N=2 可升级为 "empirical diagnostic"，大幅增强 Claim 3
- **CodeLlama-7b 是 MHA（32:32，GQA 1:1）**，与已有模型都不同（Qwen GQA 7:1, Yi 8:1, Llama-3 4:1, Mistral 4:1, Gemma-2 2:1）。MHA 意味着 1024 total KV heads，concentration 计算的 top-5% = 51 heads，分布特征可能与 GQA 模型截然不同
- **易错点**：CodeLlama 基于 Llama 2 架构，不要与 Llama-3.1-8B（已有数据，GQA 4:1）混淆。CodeLlama 的 MHA 特性使其 profiling 结果不能简单类比 Llama-3
- **决策链关键节点**：D062（Round 2 策略）→ D063（Table 4 统一 optimal k）→ D066/D067（compounding sweep bf16 统一）


---
