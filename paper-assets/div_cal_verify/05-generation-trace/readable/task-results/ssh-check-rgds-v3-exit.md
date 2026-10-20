# ssh check rgds v3 exit

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-rgds-v3-exit_20260512T143632_result.json`
- **Structured JSON:** [`e154f1e836d0307761b4.json`](../../sessions/e1/e154f1e836d0307761b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验结果：Gen 3 磁盘满崩溃

**状态：失败 — 跑完 3 代（gen_0~2），第 4 代（gen_3）训练完成后保存 checkpoint 时根分区满了。**

### 失败原因

```
safetensors_rust.SafetensorError: Error while serializing: I/O error: No space left on device (os error 28)
```

根分区 30G 已 100% 占满（剩余 3MB）。崩溃点在 `run_mvp.py:137` — `student_model.save_pretrained(checkpoint_dir)`，即 gen_3 训练已完成（loss 正常），但 checkpoint 写不进去。

### Gen 0~2 指标（均已保存）

| 指标 | Gen 0 | Gen 1 | Gen 2 |
|------|-------|-------|-------|
| held_out_perplexity | 16.63 | 16.84 | **16.35** |
| rankme | 971.52 | 965.20 | 966.02 |
| knn_probe_accuracy | 0.991 | 0.991 | 0.991 |
| rare_ngram_survival | 0.0303 | 0.0302 | 0.0306 |
| rank_correlation | -0.373 | -0.384 | -0.383 |
| train_loss | 0.884 | 0.848 | 0.869 |
| elapsed_seconds | 1704 | 1698 | 1696 |

### Gen 3 状态

gen_3 目录存在但缺少 metrics.json。训练本身完成了（日志显示 data selection 和 training 都跑完），仅在 `save_pretrained` 时因磁盘满失败。

### 日志最后 20 行

```
  Selected 400/488
  Selected 488/977 sequences

[3/5] Training student (lr=2e-05, epochs=1)...
Traceback (most recent call last):
  File "/root/div_cal_verify/run_mvp.py", line 286, in &lt;module>
    main()
  File "/root/div_cal_verify/run_mvp.py", line 241, in main
    avg_loss = run_training(student_model, tokenizer, selected_data, str(ckpt_dir),
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/div_cal_verify/run_mvp.py", line 137, in run_training
    student_model.save_pretrained(checkpoint_dir)
  File ".../transformers/modeling_utils.py", line 4173, in save_pretrained
    safe_save_file(shard, os.path.join(save_directory, shard_file), metadata=metadata)
  File ".../safetensors/torch.py", line 307, in save_file
    serialize_file(_flatten(tensors), filename, metadata=metadata)
safetensors_rust.SafetensorError: Error while serializing: I/O error: No space left on device (os error 28)
```

### 下一步建议

需要清理根分区空间后重跑 gen_3。可以考虑：把 checkpoint 保存路径改到数据盘 `/root/autodl-tmp/`，或清理旧的 checkpoint/模型缓存释放空间。

---
