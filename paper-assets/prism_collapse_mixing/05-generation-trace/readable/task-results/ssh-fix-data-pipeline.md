# ssh fix data pipeline

**prism collapse mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-data-pipeline_20260515T181429_result.json`
- **Structured JSON:** [`fb18d42e054c03807480.json`](../../sessions/fb/fb18d42e054c03807480.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。修改总结：

### 修改位置

**1. 新增 `split_real_pool()` 函数（第93行）**
- 从 `data/real_pool.jsonl`（579,255行）按行数均匀三等分，写出 `real_train_gen{1,2,3}.jsonl`
- Gen 1: 行 0–193,084（193,085 样本）
- Gen 2: 行 193,085–386,169（193,085 样本）
- Gen 3: 行 386,170–579,254（193,085 样本，末代吃余数）
- 已有文件时跳过，幂等

**2. `main()` 中调用 `split_real_pool()`（第178行）**
- 在 `prepare_data` 之后、pipeline 循环之前，**无条件执行**（不受 `--skip_data_prep` 影响）
- 两个 seed 共享同一份 real data 切分

**3. `prepare_data()` 瘦身**
- 移除 `num_gens` 参数
- `expected` 只检查 `probe_set.jsonl` + `val_set.jsonl`
- 删除了 FineWeb 流式下载 per-gen real data 的循环

**4. `make_env()` 增加 `HF_HUB_OFFLINE=1`（第147行）**
- 所有子进程（generate_synthetic, train, compute_signals）都不会触发 HuggingFace 下载

### Step 2 混合逻辑无需改动
`real_path = os.path.join(base, "data", f"real_train_gen{gen}.jsonl")` 路径与 split 产出一致，自然衔接。

---
