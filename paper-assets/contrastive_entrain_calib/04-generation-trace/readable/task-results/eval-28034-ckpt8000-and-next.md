# eval 28034 ckpt8000 and next

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_28034-ckpt8000-and-next_20260523T022308_result.json`
- **Structured JSON:** [`a8273a59d1ad049c7577.json`](../../sessions/a8/a8273a59d1ad049c7577.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 路 eval 已启动，等待结果中。当前状态：

| GPU | 任务 | PID | 状态 |
|-----|------|-----|------|
| GPU0 | reduced-lora ckpt-4500 eval | 153655 | 运行中 (362 pairs) |
| GPU1 | reduced-lora 训练 | 30011 | step 4900, 接近 ckpt-5000 |
| GPU2 | ACT s2 ckpt-3000 eval | 154152 | 运行中 (362 pairs) |
| GPU3 | ACT s2 ckpt-8000 eval | 153143 | 运行中 (20/362) |

**与任务指令的差异**：
- ckpt-2500 不存在于任何 s2 路径，改用 ckpt-3000（`/root/autodl-tmp/checkpoints/exp004s2_act_baseline_s2/checkpoint-3000`）
- ckpt-5000 未产出，改用 ckpt-4500（reduced-lora 当前 step 4900）
- eval 脚本路径是 `eval/eval_unified_preset.py`（不是 `evaluation/`）
- 基础模型是 Qwen3-8B（不是 Qwen2.5-7B-Instruct）

---
