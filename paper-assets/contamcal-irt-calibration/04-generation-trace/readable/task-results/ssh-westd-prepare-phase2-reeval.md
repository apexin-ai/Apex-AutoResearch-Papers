# ssh westd prepare phase2 reeval

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-prepare-phase2-reeval_20260519T102856_result.json`
- **Structured JSON:** [`734e2688f30065c90009.json`](../../sessions/73/734e2688f30065c90009.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Summary:

### evaluate.py 修复确认
`mc_suffix` ("The answer is ") 在 chat template 模式下已移至 model turn（`format_as_chat()` 之后），`evaluate_mcq` 和 `evaluate_paraphrased` 两处均已修复。

### Checkpoint 路径确认
25 个 adapter 全部在 `lora_adapter/` 子目录下，**除了 phi-4_d100_s42 — adapter 为空**（训练可能仍在进行中）。脚本中已加了 `adapter_config.json` 存在性检查，缺失时会 SKIP 并继续。

### 脚本已就绪

| 脚本 | GPU | 模型 | 数量 |
|------|-----|------|------|
| `phase2_eval_gpu0.sh` | cuda:0 | Phi-4 d000-d100 | 5 (d100 可能 skip) |
| `phase2_eval_gpu1.sh` | cuda:1 | Qwen2.5-14B d000-d100 | 5 |
| `phase2_eval_gpu2.sh` | cuda:2 | Qwen2.5-7B d000-d100 + Gemma-2 d000 | 6 |
| `phase2_eval_gpu3.sh` | cuda:3 | Gemma-2 d005-d100 + OLMo-2 d000-d100 | 9 |
| `phase2_sanity_check.sh` | cuda:0 | Gemma-2 d005 ARC only | 1 |

注意 gpu0/gpu1 的 `run_eval` 只接 3 个参数（model 固定为脚本顶部变量），gpu2/gpu3 接 4 个参数（因为要切换 base model）。所有脚本均设置了 `CUDA_VISIBLE_DEVICES=$GPU_ID`，输出到 `eval_results_v2/{family}_{dosage}/`。

---
