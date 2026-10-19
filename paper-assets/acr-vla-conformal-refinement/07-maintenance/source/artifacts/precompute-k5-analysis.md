# Precompute K=5 实验结果分析

## 完成状态: SUCCESS

EXIT_CODE=0，无 error/warning/exception。

## 样本数

| Benchmark | 样本数 | 轨迹数 |
|-----------|--------|--------|
| spatial   | 12,167 | 100    |
| object    | 14,570 | —      |
| **总计**  | **26,737** | — |

样本数与 K=10 cache 完全一致（预期行为：相同 demo 数据，K 只影响候选动作数）。

## Cache 文件与大小对比

### Merged 文件

| 文件 | K=5 spatial | K=10 spatial | K=5 object | K=10 object |
|------|------------|-------------|------------|-------------|
| obs_features.pt | 44.6MB | 44.6MB | 53.3MB | 53.3MB |
| k_samples.pt | 7.0MB | 13.9MB | 8.3MB | 16.7MB |
| expert_actions.pt | 1.4MB | 1.4MB | 1.7MB | 1.7MB |
| manifest.json | 111B | 112B | 110B | 111B |

### 目录总大小

| Benchmark | K=5 | K=10 | 比率 |
|-----------|-----|------|------|
| spatial   | 106MB | 120MB | 88% |
| object    | 127MB | 144MB | 88% |
| **总计**  | **233MB** | **264MB** | **88%** |

### 大小差异分析

- `obs_features.pt` 和 `expert_actions.pt` 完全一致（不依赖 K）
- `k_samples.pt` K=5 约为 K=10 的 50%（7.0MB vs 13.9MB, 8.3MB vs 16.7MB），符合预期
- 总目录含 partial 文件：K=10 有 3 shard，K=5 有 1 shard

## Manifest

```json
// spatial
{"benchmark": "spatial", "n_samples": 12167, "K": 5, "obs_dim": 960, "action_dim": 6, "h_eff": 5}

// object
{"benchmark": "object", "n_samples": 14570, "K": 5, "obs_dim": 960, "action_dim": 6, "h_eff": 5}
```

## 运行参数

- K=5, num_shards=1, shard_id=0
- precompute_batch_size=4, ~0.25s/sample
- spatial ~47min, object ~60min, 总耗时 ~107min

## 异常

无。
