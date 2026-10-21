# reviewer / loop_7.md

**When the Most Disruptive Messages Are Safe to Prune in Aggregate: Functional Analysis of Communication Pruning in Two-Agent LLM Systems** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_7.md`
- **Structured JSON:** [`c1c728447665de02d5e1.json`](../../sessions/c1/c1c728447665de02d5e1.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_wall_time
updated: '2026-04-27T17:36:29+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 **cuda:1**（gpu_ids=[1]）。服务器上 cuda:0 属于其他项目（reasoning_trace_anatomy / fewshot_spurious_mechanism）。之前多次发生 vLLM 未指定 CUDA_VISIBLE_DEVICES 默认跑 cuda:0 的事故。
- vLLM 端口：当前 Qwen2.5-7B 在 **port 8000**（非之前的 8001）。切换模型前必须确认端口和 PID。
- P1 Oracle 实验使用 **GPT-4o-mini**（非 GPT-4o，非 DeepSeek）。D195 已验证 κ=0.822。之前 DeepSeek 替代被 kill（κ=0.0 不可用）。
- 论文 Qwen3 boundary 已重写为 "heuristic non-transferability"（不再是 "cross-generational failure"）。不要回退到旧叙事。

### 2. 🖥️ 基础设施快照
- 服务器：**westb-4x6000-a(comm_gate)**，工作目录 `/root/autodl-tmp/comm_gate_mas`
- Python：`/root/miniconda3/bin/python`（conda base 环境，不用 venv）
- 模型路径：`/root/autodl-tmp/models/Qwen2.5-7B-Instruct`（当前活跃）、`/root/autodl-tmp/models/Qwen3-8B`、Llama 在同目录
- HF cache：`/root/autodl-tmp/.hf_cache`
- 活跃 vLLM：PID 782436，Qwen2.5-7B，port 8000，CUDA_VISIBLE_DEVICES=1
- 活跃实验：PID 786961，prompt_mod baseline（~86/100 截至最后检查）
- 无 wandb 配置（本项目不用 wandb）
- 输出路径 bug 反复出现：结果常写到 `outputs/v7_analysis/pruning_validation.json` 而非实验专属目录

### 3. 📊 当前状态
**刚完成**：Qwen3 boundary 重写审查（通过，两个 info-level 小问题已反馈）。

**RUNNING**：
- `prompt_mod_qwen25_gsm8k`：prompt 修改消融（移除 "confirm" 指令）。关键发现：**86/100 tasks 全部 suppressed=0/5（零 heuristic 检测）**。原始 prompt 下 heuristic 检测率 ~42%。baseline.json 是第一次坏运行残留（0% accuracy, 10.5s），当前运行会覆盖。注意：`--pruning-mode none`，仅检测率测量。

**BLOCKED**：
- P1 Oracle precompute：OpenAI API 连接问题未解。需要在服务器上 `source /etc/network_turbo` + SSL 证书 env vars。

**PREPARING**：
- `llama_length_only_gsm8k_5seed`：等待资源

### 4. 📋 待办
- prompt_mod PID 786961 完成 → 检查最终 baseline.json（确认覆盖了坏文件）→ 核实 100 tasks 的 accuracy 和 suppress_pct=0 → registry 应更新为 DONE → 发审查报告
- 如果 prompt_mod 确认 suppress=0%：需要追问 **oracle annotation**（char<30 检测不到 ≠ 真 ack 不存在）。Checker 可能仍产生功能性 ack 但格式更长。论文叙事取决于 oracle 结果：oracle ack 率也降 → ack 是 prompt-induced（需 qualify dissociation）；oracle ack 率不变 → 只是格式变了（heuristic 失效，dissociation 成立）
- P1 Oracle 连接修复后 → 验证用 GPT-4o-mini（不是其他模型），κ=0.822 已验证
- 任何新实验启动 → 检查 CUDA_VISIBLE_DEVICES=1 + 端口不冲突

### 5. 🎯 战略上下文
- **核心结论**：perturbation sensitivity 和 informational importance 在 LLM MAS 中 dissociated。ack 个体删除破坏性极高（91%），但聚合删除安全（Δ≈0）。
- **prompt_mod 是最危险的实验**：如果 oracle 也确认 ack 消失，审稿人的 "ack is prompt-induced" 批评成立。但即使成立，dissociation 的科学价值不变（prompt-induced ack 仍然展示了 perturbation-safety dissociation）——只是 "emergent" 叙事需要 qualify。
- **Qwen3 易错点**：EXP-3（-14pp）vs P5（-1pp）的差异是 **char_threshold**（80 vs 30），不是 thinking mode。我之前分析错了已修正。两者都用了 `/no_think`。关键是 Qwen3 的 `&lt;think>&lt;/think>` 前缀导致 keyword 规则 `re.match(r"^(the answer is|...)")` 完全失效。
- **双默认值陷阱**：`heuristic_ack_detector.py` 默认 threshold=80，`pruning_validation.py` 默认 30。EXP-3 走了前者路径，P5 走了后者。代码级证据在 handoff 之前的审查中已详细记录。
- **paper_provenance.yaml 覆盖率不足**：length-only 结果和 heuristic cross-domain F1 未被 provenance 追踪。


---
