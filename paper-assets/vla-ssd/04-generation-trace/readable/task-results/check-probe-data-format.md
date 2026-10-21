# check probe data format

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_probe_data_format_20260522T140423_result.json`
- **Structured JSON:** [`dfe0f8f30682b722eb9a.json`](../../sessions/df/dfe0f8f30682b722eb9a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据全部查完，结论如下：

---

## 结论

### Q1: 现有 R² JSON 是 per-demo 还是 aggregate？

**全部是 aggregate。** 所有 `action_r2_probing.json`（OpenVLA/TracVLA/NORA 三种架构）格式一致：

```json
"L0_image_mean": {"mean": 0.8733, "std": 0.0, "values": [0.8733]}
```

每个 layer×position 只有一个标量 R²，是把所有 demo 的所有 timestep 池化后（10 tasks × 10 demos × 50 timesteps = 5000 samples），做一次 80/20 random split 的 RidgeCV 拟合结果。**没有 per-demo R² 值。**

### Q2: hidden state features 是否保存了？

**没有。** 整个 `results/` 目录下只有一个 `.pt` 文件（`l1_attention_cache.pt`，是 head ablation 用的），没有任何 `.npy` 文件。probing 脚本在内存中提取 features、跑完 Ridge 后就 `del reps, actions` 了，没有持久化。

### Q3: train/test split 方式？

**random permutation，非 per-demo split。** 源码（`tracvla_spatial_probing_only.py` line 和 `libero_goal_full_pipeline.py` line 214）：
```python
perm = np.random.RandomState(42).permutation(n)
Xtr, ytr = X[perm[:nt]], y[perm[:nt]]  # 80%
Xv, yv = X[perm[nt:]], y[perm[nt:]]    # 20%
```
这是 sample-level random split——同一个 demo 的不同 timestep 会分散到 train 和 test 中，导致 **temporal leakage**（同 demo 相邻帧的 hidden state 高度相关）。

### 唯一的例外

`unified_action_probe.json` 记录了 `split: "80/20_per_task_by_demo_index"`，并有 per-task R²（10 个 task 各一个值）和 bootstrap pairwise CI。但这是 task-level bootstrap（n=10 tasks），不是 demo-level clustered bootstrap。

---

## 对 clustered bootstrap 的影响

**不能直接重分析，必须重跑 probing。** 需要：

1. **重新提取 hidden states** 并保存（按 demo 索引），因为没有缓存的特征文件
2. **改 split 策略**为 leave-demos-out（按 demo 聚类），消除 temporal leakage
3. **在 bootstrap 中按 demo resample**，计算每个 bootstrap 样本的 R²，得到 R² Δ 的 95% CI

每个 architecture × condition（trained/untrained）需要一次完整的模型推理 pass（~30-60 min per condition on single GPU），总计约 6 个 condition（OpenVLA trained/untrained, TracVLA trained/untrained, NORA trained/untrained）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "mean": 0.8733,
    "std": 0.0,
    "values": [
      0.8733
    ]
  }
}
```

</details>

---
