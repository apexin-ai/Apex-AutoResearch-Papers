# submit sft 05B d025 v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_sft_05B_d025_v2_20260514T045403_result.json`
- **Structured JSON:** [`ad00fdb3fb232765c0d1.json`](../../sessions/ad/ad00fdb3fb232765c0d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**exp_001_sft_d025_05B_v2 已成功提交到 GPU 5，训练正在运行。**

- 根因修复：`train_sft.py:114` 会用 `--gpu` 参数覆盖 `CUDA_VISIBLE_DEVICES`。去掉 `--gpu 0` 后，外部设置的 `CUDA_VISIBLE_DEVICES=5` 正确生效
- GPU 5 占用 16.7 GB，进度 2/3384 steps，预估 ~4 小时完成
- Registry 已更新 spec（model_name, seed, data_path, data_count=54133）

---
