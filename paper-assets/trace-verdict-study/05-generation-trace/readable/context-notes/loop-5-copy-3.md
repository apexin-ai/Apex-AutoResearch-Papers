# reviewer / loop_5.md

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_5.md`
- **Structured JSON:** [`abd7797568ae0fa4394f.json`](../../sessions/ab/abd7797568ae0fa4394f.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 5
reason: max_wall_time
updated: '2026-05-16T00:07:11+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-11235 的 cuda:0 和 cuda:1（`get_project_resource_usage` 确认）
- DeepSeek 模型评估必须用 max_length=16384（不截断），否则会重现 D030 的 16% accuracy 假象（evaluate.py 默认 max_length=2048 会截断 DeepSeek 输入的 question suffix）
- DebugBench 数据只有 2048 样本（1622 train / 426 test），远小于 HumanEval+MBPP 的 4720——对比结论时注意统计功效差异
- `debugbench_format_data.py` 的 exception fallback 只注入到 exception_only 和 vota 条件，full_trace/ae_only 不受影响——审查时不要误判这些条件的 empty trace 为 bug

### 2. 🖥️ 基础设施快照
- 服务器：westd-11235(root)，工作目录 `/root/trace-verdict-study`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型路径：Qwen `/root/trace-verdict-study/models/Qwen2.5-Coder-7B-Instruct`；DeepSeek `/root/autodl-tmp/models/deepseek-coder-6.7b-instruct/deepseek-ai/deepseek-coder-6___7b-instruct`
- 数据：`/root/autodl-tmp/trace-verdict-study-data/`（含 debugbench_*.jsonl）
- Checkpoints：`/root/autodl-tmp/trace-verdict-study-checkpoints/`
- HF cache：`/root/autodl-tmp/.hf_cache`
- W&B project：`trace-verdict-study`
- 活跃进程：PID 197608 (full_trace_512tok, cuda:0)；PID 211253/211263 (debugbench_vota, cuda:1)

### 3. 📊 当前状态
**我刚完成的审查**：
- debugbench_exception_bug_fix → PASS（fix 逻辑正确，100% fail 覆盖确认）
- full_trace_256tok_seed42 → PASS（accuracy 78.82%，conclusion=negative，+7.31pp lift）
- deepseek_full_trace_v3 eval → 确认 79.16% accuracy（+7.65pp）
- GPU 边界多次核查均无违规

**Registry RUNNING**：
- `full_trace_512tok_seed42`：cuda:0，plan_006 trace length ablation 512 tokens，~60% 完成
- `debugbench_vota_seed42`：cuda:1，plan_005 DebugBench VOTA，刚启动

**Registry QUEUED**：
- `debugbench_no_trace_seed42`、`debugbench_exception_only_seed42`（plan_005）
- `full_trace_1024tok_seed42`、`full_trace_2048tok_seed42`（plan_006）

### 4. 📋 待办
- full_trace_512tok_seed42 on_complete cron 触发 → 审查 eval 结果，与 256tok (78.82%) 对比看是否有提升；检查 epoch overfitting 模式
- debugbench_vota_seed42 完成 → 审查 accuracy，与 HumanEval+MBPP VOTA (99.2%) 对比；注意 DebugBench 是 logic-error dominated，VOTA 优势可能更小
- debugbench_exception_only_seed42 完成 → **关键审查**：这是 paper 核心 claim "exception dominance" 能否泛化到新 benchmark 的直接证据
- 如果 trace length ablation 全部完成（256/512/1024/2048）→ 检查是否形成单调递增曲线；如果 512≈256（没显著提升），应建议 Director 聚焦 exception_only 而非 full_trace

### 5. 🎯 战略上下文
**核心 story**：exception_only (仅错误信息) 在 verdict prediction 上压倒性优于 full_trace 和 VOTA。Qwen exception_only=99.83%，VOTA=99.2%，full_trace≈91%。这个 "less is more" 结论是论文主打。

**已确认决策链**：
- D030：evaluate.py max_length bug 已关闭（DeepSeek VOTA 84.45% 确认可复现）
- DeepSeek exception_only seed robustness：seed42=99.33%, seed456=99.33%, seed123=91.09%（离群值）——2/3 robust
- DeepSeek full_trace v3: 79.16%——远弱于 exception_only，支撑 "exception dominance" cross-model

**易错点**：
- `full_trace_512tok_seed42` registry 的 `reproduce.pid=197608` 但 nvidia-smi 显示同 PID——是正确的（不是遗留进程）
- eval_loss 上升模式（epoch2→epoch3）在 256tok 已出现，512tok 可能也有——如果全系列都有，这是系统性问题不是单次异常
- DebugBench label 平衡（50.9% pass / 49.1% fail）与 HumanEval+MBPP（71.5% pass / 28.5% fail）不同——majority baseline 不同，lift 数字不能直接对比


---
