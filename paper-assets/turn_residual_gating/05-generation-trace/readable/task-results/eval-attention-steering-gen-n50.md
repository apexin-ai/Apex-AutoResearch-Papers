# eval attention steering gen n50

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_attention_steering_gen_n50_20260520T190534_result.json`
- **Structured JSON:** [`a5d451eb2ad5f2dd4d95.json`](../../sessions/a5/a5d451eb2ad5f2dd4d95.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已提交并注册。汇总：

1. **PID**: 196319（GPU 进程），tmux session: `att_steer_gen50`
2. **数据文件**: `/root/turn_residual_gating/data/eval_200/eval_200.json`（取前 50 条）
3. **Checkpoint**: `/root/turn_residual_gating/runs/phase2_tg_s42_v7/`（含 gate_params.pt + lora/）
4. **结果输出**: `/root/turn_residual_gating/runs/attention_steering/attention_steering_gen_n50.json`
5. **日志**: `/root/turn_residual_gating/runs/attention_steering/gen_n50.log`

**命令**:
```
CUDA_VISIBLE_DEVICES=0 python src/eval_attention_steering.py \
  --checkpoint runs/phase2_tg_s42_v7 \
  --mode gen \
  --data-file data/eval_200/eval_200.json \
  --max-convs 50 \
  --beta 0 2 3 4 5 10 \
  --output-dir runs/attention_steering/ \
  --output-name attention_steering_gen_n50
```

已设 12 分钟 cron 监控（job `c97b56a4`），完成后会自动通知并注册 artifact。

---
