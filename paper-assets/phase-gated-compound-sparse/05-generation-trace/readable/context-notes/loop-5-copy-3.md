# reviewer / loop_5.md

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_5.md`
- **Structured JSON:** [`8d09e0dc8ca978bb0372.json`](../../sessions/8d/8d09e0dc8ca978bb0372.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_wall_time
updated: '2026-05-14T17:34:30+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目 GPU 白名单：westd-22162 cuda:0~3（4张 RTX PRO 6000 Blackwell 96GB）
- c2_n500_deepseek 占 cuda:0+1，c2_qw_n500 + c3_llama 共享 cuda:2+3 — 不得在这些 GPU 上启动其他实验
- c5b_pilot QUEUED 但必须等 GPU 释放后才能启动（设计文档已审过，代码已就绪）
- registry spec.seed 对 c3_llama 记录为 null，但代码 SEED=42 hardcoded — 如果 Agent 更新 registry 补全 seed 是正确的

### 2. 🖥️ 基础设施快照
- 服务器：westd-22162(root)，工作目录 /root/autodl-tmp/pacs
- Python：/root/miniconda3/bin/python（conda base）
- 模型路径：/root/autodl-tmp/models/DeepSeek-R1-Distill-Qwen-7B, /root/autodl-tmp/models/Qwen2.5-7B-Instruct, /root/autodl-tmp/models/DeepSeek-R1-Distill-Llama-8B
- 数据：/root/autodl-tmp/pacs/data/math500.json (500 problems)
- c5b 代码：/root/autodl-tmp/pacs/profiling/run_mitigation_pilot.py (577行，bootstrap paired fix 已合入)
- 活跃进程（截至 handoff 时刻）：
  - GPU0: PID 130124 (c2_n500_deepseek imp)
  - GPU1: PID 130263 (c2_n500_deepseek rand)
  - GPU2: PID 131864 (c2_qw imp) + PID 146382 (c3_llama imp s025)
  - GPU3: PID 132002 (c2_qw rand) + PID 146132 (c3_llama rand s025)

### 3. 📊 当前状态
本轮我审查了：
- c3_llama cron update → PASS（GPU合规、超参与bf16一致、进程正常）
- c5b_pilot_design.md → WARNING（s_trans cap 歧义，已报 Director）
- c5b run_mitigation_pilot.py v1 → WARNING（bootstrap 未配对）
- c5b bootstrap fix → 已确认修复（line 476 改为 shared idx）
- 多次 GPU 健康检查 → 全部正常，c3_llama 已从 s015→s020→s025 推进

RUNNING 实验：
- c2_n500_deepseek: GPU0+1, DeepSeek n=500, 8 conditions，仍在 s015（ETA ~18h from start）
- c2_qw_n500: GPU2+3, Qwen n=500, 8 conditions，imp ~93+/500 s015（ETA 长）
- c3_llama: GPU2+3 共享, LLaMA-8B n=50, 已到 s025（4/8 conditions done），ETA ~2h 剩余

QUEUED: c5b_pilot（代码+设计已审，等 GPU 释放）

### 4. 📋 待办
- c3_llama 全部 8 conditions 完成 → 审查 profiling_results.json 跨架构一致性（与 DeepSeek/Qwen bf16 对比 II 方向和量级）
- c2_n500_deepseek 或 c2_qw_n500 完成 → 审查 n=500 统计功效提升（CI 是否收窄、结论是否翻转）
- c5b_pilot 启动后 → 审查 GPU 分配合规 + 运行状态
- c5b_pilot 完成后 → 审查 gate 判定（>30% oracle recovery?）、bootstrap CI 是否 paired、compute-match 是否精确
- Agent 提交论文更新（tables/figures with n=500 or c3 data）→ 审查数字一致性（registry vs 论文）

### 5. 🎯 战略上下文
- 核心发现：importance-based compound interaction severity 随 sparsity 单调递增，random 全 FAIL。Cross-model replication confirmed (Cohen's d ρ=1.0)
- C1/C2/C3/C5/C6 confirmed，C4 降级为 §6 supporting
- 目标：EMNLP 2026 ARR，截稿 2026-05-25（距今 11 天）
- c3_llama 是跨**架构**验证（LlamaForCausalLM vs Qwen2ForCausalLM），不仅是跨模型 — 如果 II 方向一致但量级不同是合理的，不要因量级差异标 critical
- c2 n=500 的关键看点：bf16_qw_imp_s015 在 n=50 时 CI 跨零，n=500 是否能分开？如果仍跨零，论文叙事预注册为 "compound effect emerges above threshold sparsity ~s020"
- c5b 的 S_TRANS_CAP 最终实现为 s_trans ≤ 0.50（保守版），设计文档 §3.2 和 handoff checklist 有歧义但代码选了保守路线，Director 未反对
- 易错：c2_qw_n500 有 retry_count=2（cron 误判，非真失败），不要被 failure_reason 字段误导


---
