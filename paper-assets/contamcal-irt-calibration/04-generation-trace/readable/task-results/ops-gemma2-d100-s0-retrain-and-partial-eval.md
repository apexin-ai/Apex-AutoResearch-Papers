# ops gemma2 d100 s0 retrain and partial eval

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gemma2-d100-s0-retrain-and-partial-eval_20260520T220154_result.json`
- **Structured JSON:** [`e5c24971dd2f168ed454.json`](../../sessions/e5/e5c24971dd2f168ed454.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部启动成功，3 个任务都在加载模型中。

**状态汇总：**

| 任务 | GPU | tmux session | 状态 |
|------|-----|-------------|------|
| d100 重训练 (+ gradient_checkpointing) | cuda:0 | `gemma2_d100_retrain` | 加载模型中 |
| MMLU eval d000-d050 | cuda:1 | `gemma2_mmlu_s0` | 开始 d000 eval |
| ARC eval d000-d050 | cuda:2 | `gemma2_arc_s0` | 开始 d000 eval |
| Qwen-14B s0 (已有) | cuda:3 | - | 运行中 |

**OOM 修复**：d100 重训加了 `--gradient-checkpointing`。原 sweep 使用 `batch_size=2, grad_accum=8` 无 gradient checkpointing，d050 (58266 samples) 通过但 d100 (66533 samples) OOM。

**Sweep 脚本修复**：在每个 dosage 训练完成后加入 `adapter_model.safetensors` 存在检查，不存在则 `exit 1`。d100 自动启用 gradient checkpointing。

**预计完成时间**：
- Eval (MMLU/ARC)：~1 小时
- d100 重训练：~4-5 小时（gradient checkpointing 有 ~30% 速度开销）

**日志路径**：
- `/root/contamcal-irt-calibration/logs/retrain_gemma2_d100_s0.log`
- `/root/contamcal-irt-calibration/logs/eval_gemma2_s0_mmlu.log`
- `/root/contamcal-irt-calibration/logs/eval_gemma2_s0_arc.log`

---
