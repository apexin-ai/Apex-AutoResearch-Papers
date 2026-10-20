# fix hellaswag checkpoint verify

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_hellaswag_checkpoint_verify_20260517T054643_result.json`
- **Structured JSON:** [`8805e9fdf4faef4de2c6.json`](../../sessions/88/8805e9fdf4faef4de2c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 问题 1：Gen 5 HellaSwag eval 有效

**证据**：
- Gen 5 checkpoint `model.safetensors` — Birth: `2026-05-17 12:23:31 +0800` (04:23 UTC)
- hellaswag_gen5 eval 目录创建时间: `2026-05-17 12:31 +0800` (04:31 UTC)
- 训练日志 line 3628: `[Gen 5] Saved checkpoint to .../checkpoints/gen_5`
- auto_eval 脚本通过 `while [ ! -f "${CKPT}/config.json" ]` 轮询，checkpoint 完成后才启动 eval

**结论**：checkpoint 在 eval 启动前 **8 分钟**已完整写入。Reviewer 担忧的 "Step 3200 重叠" 应该是 Gen 6 的数据生成阶段（与 eval 并行运行在不同 GPU），不是 Gen 5 训练。

Gen 5 HellaSwag 结果：`acc_norm = 0.3439`，`acc = 0.3099`

### 问题 2：GPU 硬编码已修复

`auto_eval_hellaswag.sh` 第 9 行：`GPU="cuda:1"` → `GPU="${1:-cuda:0}"`

用法：`bash auto_eval_hellaswag.sh cuda:1`（默认 cuda:0）

### exp_001 当前进度

Gen 5 训练已完成。当前正在执行 **Gen 6 数据生成**，进度约 30400/50000 samples（日志 line 3671+）。

---
