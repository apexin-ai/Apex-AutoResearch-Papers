# code prep inference bench cka only

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_inference_bench_cka_only_20260518T065319_result.json`
- **Structured JSON:** [`8664e3b82a17720ea6b6.json`](../../sessions/86/8664e3b82a17720ea6b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本只支持 `--dense_path` / `--rasp_path` / `--standard_path` 三个固定 slot，没有额外参数。CKA-only SFT 模型在 `/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20`。

最简方案：把 CKA-only 塞进 `--standard_path` slot，其余保持不变（重跑 dense + RASP 保证同条件对比）。输出 JSON 中 `standard_20` key 实际对应 CKA-only。

命令：

```bash
CUDA_VISIBLE_DEVICES=0 python src/benchmark_inference.py \
  --dense_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B \
  --rasp_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20 \
  --standard_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 \
  --n_prompts 50 \
  --max_new_tokens 512 \
  --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/inference_benchmark_with_cka.json
```

要点：
- GPU: `CUDA_VISIBLE_DEVICES=0` (westb cuda:0)
- `--standard_path` 替换为 CKA-only SFT 模型路径
- output 写到新文件避免覆盖之前结果
- 结果中 `standard_20` 实际是 CKA-only 的数据，读结果时注意映射

需要我提交执行吗？

---
