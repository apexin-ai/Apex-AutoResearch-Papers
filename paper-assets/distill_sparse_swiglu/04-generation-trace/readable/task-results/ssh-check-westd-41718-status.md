# ssh check westd 41718 status

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_westd_41718_status_20260520T124811_result.json`
- **Structured JSON:** [`83aa496d968ab1618e8c.json`](../../sessions/83/83aa496d968ab1618e8c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-41718 状态报告

### GPU 占用

| GPU | PID | 显存 | 利用率 | 温度 |
|-----|-----|------|--------|------|
| cuda:0 | 249688 | 66,092 / 97,887 MiB (68%) | 98% | 80°C |
| cuda:1 | 254228 | 46,190 / 97,887 MiB (47%) | 0% (刚完成 tokenization) | 35°C |

### PID 249688 — BCE+STE downstream eval (运行 55 min)

- **命令**: `benchmark_eval.py --exp_id bce_ste_s42_eval --checkpoint checkpoints/bce_ste_s42/predictor_bce.pt --sparsity_target 0.5 --tasks wikitext2,arc_challenge,winogrande,mmlu,gsm8k,hellaswag,piqa --gpu 0`
- **日志**: `/tmp/bce_ste_s42_eval.log`
- **当前进度**: MMLU loglikelihood 18,881/40,168 (47%), ~21.8 it/s, ETA ~16 min
- **已完成**: arc_challenge (4,687 requests)
- **待运行**: MMLU 完成后还有 winogrande, gsm8k, hellaswag, piqa
- **结果文件**: 空（`results/benchmark/bce_ste_s42_eval/` 无内容）
- **预计总剩余**: ~30-40 min

### PID 254228 — C4 OOD downstream eval (运行 6 min)

- **命令**: `benchmark_eval.py --exp_id c4_ood_downstream_kl30 --checkpoint checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt --sparsity_target 0.3 --calibration_data c4 --tasks arc_challenge,winogrande,mmlu,gsm8k,hellaswag,piqa --gpu 0`（实际跑在 cuda:1）
- **日志**: `/root/distill_sparse_swiglu/logs/c4_ood_downstream_kl30.log`
- **当前进度**: loglikelihood 2,721/58,702 (4.6%), ~43 it/s
- **已完成**: arc_challenge (4,687 requests), tokenization 完成
- **结果文件**: 空
- **预计总剩余**: ~40-50 min

### tmux

无法通过 `ssh_read_only` 检查（tmux 不在白名单中）。

### 小结

两张 GPU 都被占满，两个 downstream eval 都在正常推进，无报错。BCE+STE 已跑过半，C4 OOD 刚起步。预计两个 job 都在 ~1 小时内完成。

---
