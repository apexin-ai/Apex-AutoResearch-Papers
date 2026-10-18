# agent / loop_10.md

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_10.md`
- **Structured JSON:** [`67e7862ce03b618ab352.json`](../../sessions/67/67e7862ce03b618ab352.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 10
reason: max_wall_time
updated: '2026-05-15T19:40:48+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-37397 的 cuda:0 和 cuda:1，绝对不用其他 GPU
- 论文锁定值：Qwen concentration=0.61 (float32, commit bfaea4e)，Mistral concentration=0.24/t1t5=0.41 (hires, commit e52fb0e)
- W2/W9 PPL 评估必须用 WikiText-2 test set，禁止用 calibration data（之前 baseline PPL 偏低的教训）
- Flat 分类诊断条件硬编码：concentration ≥0.50 AND t1/t5 ≤0.70
- ARR May 25, 2026 截止（距今 10 天），Round 2 审稿响应阶段
- Qwen compounding sweep 必须用 bf16_2bitonly profile（D066/D067），不用 full profile

### 2. 🖥️ 基础设施快照
- 服务器：westd-37397，2× RTX PRO 6000 98GB
- 工作目录：/root/ratekv
- Python：/root/miniconda3/bin/python，激活方式 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- HF cache：/root/autodl-tmp/.hf_cache/
- CodeLlama 模型路径：/root/autodl-tmp/.hf_cache/AI-ModelScope/CodeLlama-7b-hf/
- 活跃进程：codellama_hires_profiling PID=362945（cron 监控中，reconcile 确认 still running）
- phi3_medium_hires_profiling 也标记 RUNNING（但无 PID 记录，需要 SSH 确认实际状态）

### 3. 📊 当前状态
**刚完成的关键工作：**
- 全面 claim-strength reframing 已完成并提交 (d96d7da)：abstract 重组、contributions 降级、formal definitions、limitations 扩展
- Qwen compounding sweep v2 成功（bf16_2bitonly profile，D066）
- 实验计划 18 个中已完成 18 个（但 Round 2 新增实验在 registry 中单独追踪）

**RUNNING (2)：**
- `codellama_hires_profiling`：CodeLlama-7b hires profiling，cuda:0，PID 362945，cron 活跃。retry_count=1（首次失败后重跑）
- `phi3_medium_hires_profiling`：Phi-3-medium profiling，状态不明（无 PID），可能已挂但 cron 没清理

**QUEUED (2，等 GPU)：**
- `gemma2_downstream_k8_4task_v2`：Gemma-2 downstream eval k=8（修复 head_dim bug）
- `qwen_3seed_downstream_ci`：Qwen 3-seed downstream CI（Table 4 error bars）

**PREPARING (2，可能是废弃条目)：**
- `codellama_7b_hires_profiling`、`phi3_medium_hires_profiling_check`——conclusion=failed，看起来是旧版本被 retry 替代

**Worker 池 = 0**（空！违反 L1 红线 #4，但当前两 GPU 都有实验跑着，非 GPU Worker 也应该铺起来）

### 4. 📋 待办（条件触发式）
- `codellama_hires_profiling` cron 回调到达 → 分析 profiling 结果（concentration + t1/t5），判断 CodeLlama 是 Spread/Spike/Flat → 更新 registry + report.md + 汇报 Director
- `phi3_medium_hires_profiling` 需要 SSH 确认实际状态 → 如果已死则标记 failed 并重跑（Phi-3 下载曾失败过，shard 不全）
- CodeLlama profiling 完成释放 cuda:0 → 立即提交 QUEUED 中优先级最高的实验（gemma2_downstream_k8_4task_v2 或 qwen_3seed_downstream_ci）
- 两个 GPU 都空出 → compounding curves（Llama sweep cuda:0 + Mistral sweep cuda:1 并行，ROADMAP 优先级 2）
- 所有 profiling + compounding 数据就绪 → 派 Paper Worker 集成到论文（compounding figure + downstream CI table）
- Round 2 提交前 → 全文一致性检查 + reference audit + visual review

### 5. 🎯 战略上下文
- **核心结论**：non-uniform KV cache quantization 只在 Spread 模型（Qwen）上有效，Spike（Yi/Llama）和 Flat（Mistral/Gemma）无效。论文 framing 已从"universal benefit"转为"concentration-dependent benefit + diagnostic rule"
- **Round 2 关键策略 (D062)**：全面 reframing（claim 降级而非补更多 positive evidence）+ spread 模型搜索（从 N=1 Qwen 扩展到 N≥2）。CodeLlama 和 Phi-3 是 spread 候选
- **最容易判断错的事**：phi3_medium_hires_profiling 的真实状态——它 RUNNING 但没有 PID 记录，很可能已经死了。新 session 第一件事应该 SSH 确认
- **Compounding curves 是论文关键缺口**：reframing 已完成但 Items 9-11（compounding figure、downstream CI、data integration）依赖实验数据。Llama + Mistral compounding sweep 还没跑
- **时间压力**：10 天内必须完成所有补实验 + 论文集成 + 提交。profiling ~6h，compounding ~6h，downstream CI ~12h，paper integration ~1 day
- **决策链关键节点**：D050（诊断升级为 concentration+t1/t5）→ D059（修正分类）→ D062（Round 2 策略）→ D066/D067（compounding 用 bf16_2bitonly）


---
