# check bootstrap speed and optimize

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bootstrap_speed_and_optimize_20260522T154638_result.json`
- **Structured JSON:** [`fa5a2ab5e766badab651.json`](../../sessions/fa/fa5a2ab5e766badab651.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

日志行数没变，两个 GPU 的 bootstrap 都还没完成第一个 1000 iteration 进度报告。

## 分析结果

### 当前状态
- **GPU 0** (openvla goal trained): bootstrap 已运行 **~52 分钟**，<1000/10000 iterations 完成（0 进度报告）
- **GPU 1** (tracvla goal trained): bootstrap 已运行 **~10 分钟**，同样 <1000/10000
- **结果文件**：0 个完成（`results/clustered_bootstrap/` 目录不存在）
- **CPU**：208 核，BLAS 使用 ~28 线程并行

### 瓶颈分析

`clustered_bootstrap_r2` 的核心循环：
```
for b in range(10000):       # 10000 iterations
    for l in range(32):       # 32 layers
        K_tr = kernels[l][np.ix_(tr_idx, tr_idx)]   # 4000×4000 fancy indexing (慢)
        np.linalg.solve(K_tr, y_tr)                  # O(n³) dense solve
```

- N=5000 samples → 80/20 split → K_tr ≈ 4000×4000
- 每次 solve: O(4000³) ≈ 21B FLOPs
- 每 run 总计: 10000 × 32 × solve = 320,000 次 dense solve
- **无并行** (纯串行 for 循环，无 joblib)

### 耗时预估

| 阶段 | 每 run 耗时 |
|------|------------|
| Feature extraction (GPU) | ~5 min |
| Canonical fit + kernel | ~5 min |
| **Bootstrap 10000 iter** | **~9-11 hours** |
| **Total per run** | **~10 hours** |

### 总完成时间 @ n_bootstrap=10000

| GPU | 任务数 | 总耗时 | 预计完成 |
|-----|--------|--------|---------|
| GPU 0 | 10 runs (6 openvla + 4 nora) | ~105 hours | **5/27 03:00** |
| GPU 1 | 8 runs (8 tracvla) | ~84 hours | 5/26 11:30 |

**GPU 0 超时，无法在 5/26 前完成。**

### 建议：降到 n_bootstrap=1000

| 指标 | n=10000 | n=1000 |
|------|---------|--------|
| Bootstrap 耗时/run | ~10h | **~65 min** |
| GPU 0 总时间 | 105h | **~11h** |
| GPU 1 总时间 | 84h | **~9h** |
| 95% CI 相对误差 | ~1% | ~3% |

1000 bootstrap 对 95% CI 完全够用。需要 kill 当前进程并用 `--n_bootstrap 1000` 重启。

### 脚本优化空间（如果坚持 10000）

1. `np.linalg.solve` → `cholesky` + `cho_solve`（K_tr 是 SPD，可 2× 加速）
2. 预分配 K_tr buffer，避免每次迭代 128MB 内存分配
3. 但即使 2× 加速仍需 ~50h for GPU 0，依然紧张

**建议立即 kill 并以 n_bootstrap=1000 重启，12 小时内全部跑完。** 是否执行？

---
