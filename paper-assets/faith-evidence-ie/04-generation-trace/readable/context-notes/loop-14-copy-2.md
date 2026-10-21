# reviewer / loop_14.md

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_14.md`
- **Structured JSON:** [`e3323663c6000c766388.json`](../../sessions/e3/e3323663c6000c766388.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 14
reason: max_wall_time
updated: '2026-05-17T16:44:41+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单 cuda:0-3（rtx5090-4x 四卡全可用），越界即 CRITICAL
- 提交任务必须 CUDA_VISIBLE_DEVICES=X 显式指定，禁止 device_map="auto"（C002/C003）
- no-evidence 模型 eval 必须传 --no_evidence 参数（C005），否则结果全部作废
- LLaMA base_model 路径是 `/root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B`（注意 meta-llama/ 子目录），本轮已因漏掉子目录导致 eval 崩溃一次
- Registry 标记 killed 时必须 kill -9 + ps 验证（C004）
- D076 eval 协议：batch_size=4, --no-quantize, max_new_tokens=1024, seed=42（seed variance 实验用 seed=43）

### 2. 🖥️ 基础设施快照
- 服务器：rtx5090-4x (root)，备用 bjb2-12179 (root)
- 工作目录：`/root/autodl-tmp/freige`
- Python：`/root/miniconda3/bin/python`，conda base 环境
- 模型路径：`/root/autodl-tmp/models/` 下 Qwen/Qwen3-{1.7B,4B,8B} 和 meta-llama/Meta-Llama-3.1-8B
- 数据集：`/root/autodl-tmp/data/docred/`（dev.json 998 docs → 985 eval docs，test.json）
- SFT checkpoints：`/root/autodl-tmp/sft_output_{qwen3_1_7b,qwen3_4b,qwen3_8b,llama_3_1_8b}_bf16`（或无 _bf16 后缀）
- RSFT checkpoints：`/root/autodl-tmp/rsft_output_{qwen3_1_7b,qwen3_4b→rsft_ced_s43,qwen3_8b,llama_3_1_8b_r3}/checkpoint-*`
- HF cache：`/root/autodl-tmp/.hf_cache`，离线模式 `HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1`
- 活跃进程（截至 handoff）：
  - 1.7B seed43 eval: PID 455637, cuda:2, nohup（221/247, ~15 min 完成）
  - LLaMA seed43 eval r2: PID 463080, cuda:0, tmux（刚启动 ~5 min）
  - 8B RSFT test eval: PID 460590, cuda:1, nohup
  - LLaMA RSFT test eval: PID 460164, cuda:3, nohup

### 3. 📊 当前状态
**本轮完成的审查（共 6 份报告）：**
1. lead2_ckpt20_eval [WARNING] — GRPO ckpt-20 rel_f1=0.4617 仅比 RSFT +0.16pp，噪声范围，不宜作正面证据
2. ROADMAP D094 [WARNING] — 4B "+6.1pp" 数据错误，实际 +5.52pp（上轮遗留）
3. fig_scaling.pdf [WARNING] — 8B no-evidence 数据占位符过时（上轮遗留）
4. fig_overview.png [WARNING] — "Select Top-1" 应为 "Top-K"（上轮遗留）
5. Scaling study 完整表 [PASS] — 4 模型全部核实
6. LLaMA seed43 eval [CRITICAL] — base_model 路径缺 meta-llama/ 子目录导致崩溃，已修复为 r2

**RUNNING 实验：**
- `plan_006_qwen3_1_7b_rsft_seed43_eval` — 1.7B seed variance 检查，221/247 (89%)，~15 min
- `plan_006_llama_rsft_seed43_eval_r2` — LLaMA seed variance 检查，刚启动，~2.5h
- `plan_006_qwen3_8b_rsft_test` — 8B test 预测（CodaLab 提交用）
- `plan_006_llama_rsft_test` — LLaMA test 预测（CodaLab 提交用）
- `plan_006_llama_rsft_seed43` — 训练已完成但 registry 仍标 RUNNING（需 Agent 关闭）

**Paper writing workers 已完成但未审查**（非实验，文献/写作类 worker，不需要实验审查）：
- worker_paper_writing_experiments, worker_paper_writing_method, worker_paper_research_*

### 4. 📋 待办（条件触发式）
- 1.7B seed43 eval 完成 → 读 metrics.json，对比 seed42 rel_f1=0.5219（期望 ±1pp 即 0.51-0.53），报告 seed robustness 结论
- LLaMA seed43 eval r2 完成 → 读 metrics.json，对比 seed42 rel_f1=0.5674（期望 ±1.5pp），报告跨架构 seed robustness
- 两个 test eval 完成 → 确认 predictions.json 存在（test 无 gold label 无 metrics），提醒 Director CodaLab 手动提交
- Paper 章节审查请求到达 → 按 §5 写作审查维度审查（claim 可信度 / 叙事逻辑 / 审稿人攻击面），先检查 Agent 是否遵循了 paper-writing-norms skill
- 所有 seed variance 完成 → 汇总 seed robustness 表给 Director（2 模型 × 2 seeds）

### 5. 🎯 战略上下文
**核心发现（Scaling Study C5，已验证完整表）：**

| Model | SFT rel_f1 | RSFT rel_f1 | Δ |
|-------|-----------|------------|------|
| Qwen3-1.7B | 0.4945 | 0.5219 | +2.74pp |
| Qwen3-4B | 0.4049 | 0.4601 | +5.52pp |
| Qwen3-8B | 0.5262 | 0.5606 | +3.44pp |
| LLaMA-8B | 0.5514 | 0.5674 | +1.60pp |

**关键叙事点：**
- Evidence Tax 非单调：1.7B 受益 +8.0pp，4B 付出 -7.5pp，8B ≈0，LLaMA -0.7pp
- RSFT gain 与 SFT baseline 强度负相关：弱模型获益更大
- 1.7B RSFT (0.5050 ign_f1) ≈ 8B SFT (0.5051 ign_f1) — "小模型+RSFT 追平大模型 SFT"
- Qwen 家族 1.7B > 4B 非单调——4B 是异常点，论文需谨慎处理
- GRPO 在 RSFT 之上仅 +0.16pp（噪声），当前只能作 future work
- BM25 post-hoc baseline 已验证：RSFT joint generation EDCR 比 oracle-k post-hoc 好 7.9pp

**易错点：**
- argparse default bug：inference.py line 382 hardcodes `--base_model` default 为 Qwen3-4B，当 model_path 是 full model 时无害（被忽略），但当 model_path 是 adapter 时会错用 base_model——LLaMA eval 必须显式传 `--base_model`
- Registry 中 ROADMAP 写的 4B gain "+6.1pp" 无法从任何数据复现，实际是 +5.52pp（rel_f1）或 +5.38pp（ign_f1），已报告但不确定是否已修正
- evi_f1 有两个定义：evi_f1（TP-only，~0.80+）和 evi_f1_joint（DREEAM protocol，含 FP/FN，~0.36-0.46），论文引用时必须区分


---
