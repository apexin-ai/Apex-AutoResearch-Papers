# exp gemma float32 restart

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_gemma_float32_restart_20260521T022454_result.json`
- **Structured JSON:** [`15eaff620e37843ba564.json`](../../sessions/15/15eaff620e37843ba564.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部启动完成。汇报：

**GPU 状态**: 4 GPU 全部已加载模型，各占用 ~35.9 GB 显存
- GPU 0: 35925 MiB | PID 71647
- GPU 1: 35925 MiB | PID 71648
- GPU 2: 35925 MiB | PID 71649
- GPU 3: 35925 MiB | PID 71650

**Shard 设计**: 432 float32 conditions → 4 shards × 108 conditions

**完成监控**: PID 74625，完成后写入 `/tmp/gemma_fp32_results.txt`

**预计运行时间**: 108 conditions × 200 items/condition per GPU。参考 bfloat16 批次（432 conditions 用 4 GPU 完成了 86,400 records），float32 同等规模，预计产出 86,400 records。float32 推理比 bfloat16 慢约 1.5-2x（显存带宽瓶颈更大），估计需要 **3-5 小时**。

---
