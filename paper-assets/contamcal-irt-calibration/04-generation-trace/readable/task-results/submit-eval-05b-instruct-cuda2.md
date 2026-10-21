# submit eval 05B instruct cuda2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_eval_05B_instruct_cuda2_20260516T143946_result.json`
- **Structured JSON:** [`ea2c2f066ca07d08141e.json`](../../sessions/ea/ea2c2f066ca07d08141e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已提交并注册完成。

**提交状态**: 成功运行中

| 项目 | 详情 |
|------|------|
| exp_id | `exp_001_eval_05B_instruct` |
| PID | 797754 (子进程, cuda:2 确认) |
| GPU | cuda:2, 1302 MiB 已占用 |
| 模型 | `/root/autodl-tmp/models/Qwen/Qwen2.5-0.5B-Instruct-hf` |
| 输出 | `/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B-Instruct/` |
| 日志 | `/tmp/eval_05B_instruct.log` |

**完整命令**:
```bash
CUDA_VISIBLE_DEVICES=2 python3 /root/contamcal-irt-calibration/exp001/evaluate.py \
  --model-path /root/autodl-tmp/models/Qwen/Qwen2.5-0.5B-Instruct-hf \
  --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B-Instruct/ \
  --mc-format aligned --instruct \
  --benchmarks mmlu gsm8k humaneval
```

**预计完成时间**: 0.5B 模型很小，3 个 benchmark 预计 15-30 分钟内完成（参考 3B 用时按模型大小缩放）。

---
