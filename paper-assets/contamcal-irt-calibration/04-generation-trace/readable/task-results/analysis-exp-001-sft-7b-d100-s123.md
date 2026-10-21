# analysis exp 001 sft 7b d100 s123

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_001_sft_7b_d100_s123_20260518T194313_result.json`
- **Structured JSON:** [`d718e6c3b02980faf736.json`](../../sessions/d7/d718e6c3b02980faf736.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Summary:

## 结果
- train_loss: 0.988 (avg over 415 logged steps)
- mean_token_accuracy: 0.766
- steps: 4159
- train_runtime_seconds: N/A (log file 未生成，registry 记录 wall_clock=9289s 含排队等待)
- checkpoint_verified: true
- lora_alpha: 32 ✓
- lora_adapter_path: `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-7B_d100_s123/lora_adapter`

## 与 seed=42 对比
| 指标 | s123 | s42 | diff |
|------|------|-----|------|
| train_loss | 0.988 | 0.987 | +0.001 |
| mean_token_accuracy | 0.766 | 0.745 | +0.021 |
| steps | 4159 | 4159 | 0 |

- accuracy 差异 +2.1% 来自早期训练阶段的 seed 效应，后期 (step 4100+) 两个 seed 的 accuracy 均收敛到 ~0.76
- 结论: 跨 seed 一致性 **好** (loss 几乎相同，最终收敛一致)

## Conclusion
- **success** — 训练正常完成 (epoch=1.0, 4159 steps)，与 s42 收敛一致

## 备注
- W&B: `list_wandb_runs` 工具有 bug (`wandb_project` 参数报错)，未能获取 W&B run
- Log: `/root/autodl-tmp/logs/train_7b_d100_s123.log` 文件不存在，指标从 `trainer_state.json` 提取

---
