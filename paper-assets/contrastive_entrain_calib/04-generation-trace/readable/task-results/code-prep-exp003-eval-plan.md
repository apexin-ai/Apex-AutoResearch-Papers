# code prep exp003 eval plan

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-exp003-eval-plan_20260519T102720_result.json`
- **Structured JSON:** [`05c7c3c53e0f6ef95763.json`](../../sessions/05/05c7c3c53e0f6ef95763.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已创建。环境状态汇总：

### westd-29046 eval 准备状态

| 项目 | 状态 | 路径 |
|------|------|------|
| eval_unified_preset.py | ✓ | `/root/contrastive_entrain_calib/eval/eval_unified_preset.py` |
| 基座模型 Qwen3-8B | ✓ | `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B` |
| NLI 模型 | ✓ | HF cache 已有 |
| calibration 数据 | ✓ | `/root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl` |
| 已有 checkpoints | ✓ | 500, 1000, 1500, 2000 (训练中，save_steps=500) |
| eval 脚本 | ✓ | `/root/contrastive_entrain_calib/eval/run_exp003_unified_eval.sh` |
| 输出目录 | ✓ | `/root/contrastive_entrain_calib/results/exp003_unified_eval/` |

### 关键信息
- exp-003 是 **LoRA** 训练（r=64, q/v/k/o_proj），eval 时用 `--lora_path`
- 训练 max_steps=8000，当前约 step 1894，save_steps=500
- **注意**：eval 脚本的 DEFAULT_DATA 指向 `contrastive_entrain_calib/data/` 下的文件（不存在），eval shell 脚本已显式传 `--data_path` 指向实际路径

### 运行方式
```bash
CUDA_VISIBLE_DEVICES=1 bash /root/contrastive_entrain_calib/eval/run_exp003_unified_eval.sh
```

脚本会自动跳过不存在的 checkpoint 和已评估过的 checkpoint，训练完成后可直接运行。无缺失依赖。

---
