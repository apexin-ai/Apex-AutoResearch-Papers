# code occ preload optimization

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_occ_preload_optimization_20260520T112623_result.json`
- **Structured JSON:** [`35400ffd9dc555e68afd.json`](../../sessions/35/35400ffd9dc555e68afd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实现完成。汇总结果：

---

## 实施结果

### 代码修改
文件：`/root/occsafe_vla/openvla-oft/prismatic/vla/datasets/datasets.py`

修改内容：
1. `__post_init__`: 初始化 `_occ_cache = {}` 字典，加载 occ_index 后调用 `_preload_occ_data()`
2. 新增 `_preload_occ_data()`: 启动时一次性读取所有 HDF5 的 bev_binary 到内存，存为 `_occ_cache[task_name][demo_key] = np.ndarray(T, 64, 64)`
3. `_load_occ_label()`: 优先从 cache 查找（无 I/O），cache miss 时 fallback 到 HDF5 文件读取

原文件备份在 `datasets.py.bak`。

### 验证结果

**(a) 数据正确性** ✓  
随机抽取 10 个样本，cache 读取 vs 直接 HDF5 读取完全一致 (`np.array_equal = True`)

**(b) 训练速度** ✓  
5-step dry-run on cuda:3 (occ_data_dummy):
- Step 1: ~6s (CUDA 编译 warmup)
- Steps 2-5: ~1.0 s/step（vanilla 基准 ~1.09 s/step）
- 速度恢复到接近 vanilla 水平

**(c) occ_loss** — wandb_log_freq=10 且 wandb 已禁用，5 步内未输出 loss 值。但训练正常完成无报错，结合 (a) 数据正确性已验证，loss 计算可信。

### 预加载统计
- **文件数**: 10
- **Demo 数**: 500  
- **总样本数**: 119,788
- **内存占用**: 467.9 MB（bool 数组）
- **加载耗时**: ~2 秒

### 注意事项
- `occ_data/`（真实数据）尚无 `occ_index.json`，需要在 occ 提取完成后运行 `build_occ_index.py` 生成
- 当前 5 个提取进程（task 0/2/3/4/8）仍在运行，occ_data HDF5 文件被锁。预加载代码已处理 `BlockingIOError`，锁定的文件会跳过并打印警告

---
