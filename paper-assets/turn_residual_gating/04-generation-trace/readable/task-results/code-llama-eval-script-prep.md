# code llama eval script prep

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama_eval_script_prep_20260521T015535_result.json`
- **Structured JSON:** [`e5623e820fa0ff831d53.json`](../../sessions/e5/e5623e820fa0ff831d53.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已就绪。

**脚本**: `/root/turn_residual_gating/scripts/eval_llama_tg_s42.sh`

**评估内容（8 runs）**:

| # | 条件 | GAR 变体 | 模式 |
|---|------|----------|------|
| 1-4 | Base / TG | ours / dongre | Teacher-Forced（固定对话） |
| 5-8 | Base / TG | ours / dongre | Autoregressive（模型生成） |

PPL 在每个 run 中自动计算，包含在输出 JSON 的 `avg_ppl` 字段。

**关键设计**:
- 自动检测最新 epoch checkpoint（优先 epoch_2 → epoch_1 → epoch_0 → 根目录）
- 实际 TG 训练输出在 `runs/phase2_llama_tg_s42/`（不是 `checkpoints/llama_tg_s42/`）
- LoRA-only baseline 未包含（训练还没启动）
- 结果输出到 `runs/eval_llama_tg_s42/`

**使用**:
```bash
# 训练完成后
bash scripts/eval_llama_tg_s42.sh 2>&1 | tee runs/eval_llama_tg_s42.log
```

**看 training-inference GAR gap**: 对比 `tf_tg_ours` vs `ar_tg_ours` 结果中的 `mid_turns_avg_gar`，Qwen 上该 gap 为 20-33×。

---
