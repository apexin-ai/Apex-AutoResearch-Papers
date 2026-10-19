# fix hdf5 corruption repair retrain

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_hdf5-corruption-repair-retrain_20260517T155835_result.json`
- **Structured JSON:** [`44b9af88e85cd29034da.json`](../../sessions/44/44b9af88e85cd29034da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**情况汇总：**

1. **HDF5 文件完好**：10 个文件 md5 完全一致，h5py 全部正常打开（各 50 demos）
2. **已有训练在运行**：`train-crm-k1-accg-object-seed42-v2` (PID 436926) 正在 CUDA:0 上 precompute K=1 features，进度 7500/72507 (~14.3 samples/s)，预计还需约 75 分钟完成 precompute
3. **Cache 正在被写入**：`/root/autodl-tmp/crm_cache_k1/object/` 是该运行进程的输出目录

这个 v2 运行的参数与你要求提交的 `train-crm-k1-accg-object-seed42-multiscale` 完全一致（epochs=50, batch_size=512, lr=1e-3, loss_mode=multi, 相同的 lambda 参数和 max_correction_norm=0.2）。

**不应执行的操作**：
- 删除 cache（会破坏正在运行的 v2 训练）
- 在 CUDA:0 上提交新任务（已被占用）

v2 训练已经成功通过了 HDF5 读取阶段，说明之前的损坏问题已自行解决（可能是重启了数据传输或服务器重启清理了损坏状态）。是否继续等待 v2 完成，还是需要 kill v2 并按新的 exp_id 重启？

---
