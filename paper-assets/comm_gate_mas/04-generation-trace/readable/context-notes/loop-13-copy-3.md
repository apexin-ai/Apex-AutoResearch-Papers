# reviewer / loop_13.md

**When the Most Disruptive Messages Are Safe to Prune in Aggregate: Functional Analysis of Communication Pruning in Two-Agent LLM Systems** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_13.md`
- **Structured JSON:** [`32c909e193049ec5b8d3.json`](../../sessions/32/32c909e193049ec5b8d3.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 13
reason: max_wall_time
updated: '2026-04-29T18:38:49+00:00'
---

### 1. 🔴 硬约束 / 红线
- bjb2-4x5090-b 项目只能用 cuda:0 / cuda:1（root 账户分配）。GPU 2/3 属于 pseudo_label_bias_decomp 项目（OfficeHome 训练），绝对不能碰
- westb-4x6000-a 账户有两个：comm_gate 用 caoxiaoyu（部分旧实验），root（大部分新实验）。提交任务前确认用对账户
- vLLM 启动后必须发送真实 prompt 验证推理可行，不能仅检查 HTTP 200。刚刚发生的 critical：max_model_len=2048 + max_tokens=2048 = 0 input 空间，100% task 静默失败但脚本标记为 "completed"
- 脚本将 API 400 错误记录为 task failure 而非 infra_error，output 文件看似完整实则全废。审查时必须检查 baseline accuracy 是否在合理范围（GSM8K ~78-82%, StratQA ~57-65%），0% = 数据无效

### 2. 🖥️ 基础设施快照
**bjb2-4x5090-b** (RTX 5090 x4, 32GB each)
- 工作目录：/root/autodl-tmp/comm_gate_mas
- Python：/root/miniconda3/bin/python（conda base）
- 模型：/root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-8B-Instruct
- 环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- PyTorch 2.10.0+cu128, vLLM 0.18.1 (enforce_eager=True)
- 截至 handoff 时 GPU 0/1 各有一个 vLLM EngineCore（PID 23066/24849），**但 max_model_len=2048 有 bug，需 kill 重启为 8192**
- GPU 2/3：pseudo_label_bias_decomp 的 OfficeHome 训练（PID 20155/20330），不归我们管

**westb-4x6000-a** (A6000 x4, 48GB each)
- 工作目录：/root/autodl-tmp/comm_gate_mas
- 当前空闲（cuda:0-3 全空）

### 3. 📊 当前状态
**刚完成的审查**：
1. worker_diag_bjb2_cuda0 → [warning] 环境搭建完成但 vLLM 只启动了 GPU 1，GPU 0 空
2. worker_exp_stratqa_4seed_gpu0 → **[CRITICAL]** 启动了两个 GPU 的 vLLM + 跑了 seed_4，但 vLLM max_model_len=2048 导致 200/200 tasks 全部 400 报错，baseline=0%, pruned=0%。已上报 Director 要求 kill + 重启 + 重跑

**Registry 状态**：
- stratqa_llama_heuristic_4seed_v2: QUEUED（parent，4 seeds 3/4/5/6）
- stratqa_4seed_v2_gpu1: QUEUED（子实验，seeds 4+6 on cuda:1）
- seed_4.json 已生成但**数据全废**（0% accuracy），需删除重跑
- 其余近期实验（e2e_llama_arc_rr, distilbert_classifier, e2e_gemma_arc_rr）均 DONE/success，已审过

**等待中**：Director 对 vLLM critical 的响应 → Agent 应 kill 进程 + 以 --max-model-len 8192 重启 + 重跑全部 4 seeds

### 4. 📋 待办
- Agent 重启 vLLM + 重跑 stratqa seeds → 验证新 vLLM 的 max_model_len 是否正确（检查 `/v1/models` 返回 + 一条真实 prompt 测试），再验证首批 task 的 baseline accuracy 是否在 57-65% 合理范围
- stratqa 4-seed 全部完成 → 核验：(1) 每 seed baseline 在 57-65%，(2) suppress rate ~50%（与之前 4-seed 一致），(3) 8-seed 均值是否仍全正向，(4) seed_4.json 是新数据不是旧废数据
- 若 8-seed 中出现 negative delta → 立即评估是否改变论文 claim（当前 claim: "all seeds positive"）
- 若 Director 派发论文章节审查 → 必做合规检查（Agent 是否看过 red-section skill）+ 四维度写作审查

### 5. 🎯 战略上下文
- 项目处于 R1 rebuttal 阶段（5/10 borderline accept，D235）。核心修改是 CI reframing + 匿名代码仓库 + 统计 claim 校准
- StratQA 8-seed 补种是当前最高优先级实验（D238）：消除 discovery seed=42 选择偏差。当前 4-seed mean=+4.9pp 全正向，如果 8-seed 仍全正向则彻底消除审稿人攻击面
- 论文关键弱点（memory.md R12 清单）：C1 72B 单 seed、C2 双 backbone 5x 效果差异、M2 greedy decoding 限制、M6 Gemma κ=0.35
- **最易判断错的事**：seed_4.json 已存在且显示 200/200 completed — 但数据是废的（0% accuracy）。Agent 可能声称"seed_4 已完成"，必须核对 accuracy 数字
- **另一个坑**：检查远程文件时注意区分 westb 和 bjb2 两台服务器，论文/文档在本地 workspace，训练代码/数据在远程。之前出过只查一边误判的事故（见 MEMORY.md feedback_agent_hallucinated_results.md）


---
