# code llm judge baseline

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llm_judge_baseline_20260514T102134_result.json`
- **Structured JSON:** [`ab037a5e70aae92d5d11.json`](../../sessions/ab/ab037a5e70aae92d5d11.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全量 test set 评估已启动（PID=27419），1824 windows，预算 $50。按 $0.0066/window 估计约 $12，3 rps 需约 10 分钟完成 API 调用（加上数据加载约 1 分钟）。

进度在 `logs/llm_judge_full.log`，结果输出到 `results/llm_judge_full_zeroshot.json`。预计 15-20 分钟完成。

## 当前状态总结

1. **代码** `artifacts/baseline_llm_judge.py` 已创建并部署到服务器
2. **Pilot 完成** (50 windows): macro_f1=0.4286, $0.33 费用, 0 parse failures
3. **全量评估已启动**: 1824 windows, zero-shot, claude-sonnet-4.6, 预估 $12, ~15min
4. 全量 test set label 分布更平衡（pilot 前 50 个极不平衡 46:4），全量结果会更有参考价值

可以稍后查看 `tail -20 /root/autodl-tmp/agent_progress_probe/logs/llm_judge_full.log` 追踪进度。完成后我来读取最终结果。

---
