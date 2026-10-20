# code plan 005 debugbench train dryrun

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_005_debugbench_train_dryrun_20260515T233228_result.json`
- **Structured JSON:** [`4677510067cc79f1778c.json`](../../sessions/46/4677510067cc79f1778c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Dry-run 结果

### 验证通过的部分
1. **脚本兼容性**: `debugbench_exception_only` 已在 `--condition` choices 中，无需修改脚本
2. **数据加载**: Train 1622, Eval 426 ✓
3. **数据格式**: `{"input": "...", "output": "pass"/"fail", "problem_id": "..."}` — 与主任务完全一致
4. **Tokenization**: 完成，无报错
5. **模型加载**: bf16 加载成功

### 未通过的部分
- **Forward pass OOM**: 两块 GPU 都被其他进程占满（GPU 0: ~92/98 GiB, GPU 1: ~77/98 GiB），无法执行实际 training step。这是资源问题，非代码问题。

### 完整训练命令（可直接用于 submit_training_job）

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/trace-verdict-study && python train/train_sft.py \
  --condition debugbench_exception_only \
  --gradient_checkpointing \
  --seed 42
```

默认参数已匹配主任务：LoRA r=16, alpha=32, lr=2e-4, epochs=3, max_length=2048, batch_size=4, grad_accum=8。output_dir 自动设为 `/root/autodl-tmp/trace-verdict-study-checkpoints/debugbench_exception_only`。

### 无需脚本修改
`train/train_sft.py` 已原生支持全部 5 个 debugbench 条件。等 GPU 空闲后可直接启动。

---
