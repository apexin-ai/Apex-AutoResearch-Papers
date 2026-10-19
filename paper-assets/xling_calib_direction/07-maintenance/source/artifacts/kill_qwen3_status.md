# Kill Qwen3 & 服务器状态报告
**时间**: 2026-05-21 09:33 UTC

## 1. Qwen3 Kill + 清理

| 步骤 | 结果 |
|------|------|
| kill 36611 | exit code 0, 进程确认终止 (KILLED_OK) |
| 删除模型文件 `/root/autodl-tmp/models/Qwen3-235B*` | QWEN3_CLEANED |
| 删除 HF cache `models--Qwen--Qwen3-235B*` | CACHE_CLEANED |

**结论**: Qwen3-235B 下载进程已终止，所有部分文件已清理。

## 2. Llama4 下载进度

**状态: 下载已停止（无活跃进程）**

- 目录: `/root/autodl-tmp/models/Llama4-Scout-W4A16/`
- 总大小: 43G
- 已下载 shard: **7 / 14** (model-00002, 00003, 00005, 00006, 00007, 00008, 00010)
- 每个 shard: ~4.7G
- 最后写入: model-00010 @ 09:32
- **无下载进程在运行**
- 缺失 shard: 00001, 00004, 00009, 00011, 00012, 00013, 00014

⚠️ 需要重新启动下载以完成剩余 7 个 shard。

## 3. 磁盘空间

```
/dev/md0  350G  131G  220G  38%  /root/autodl-tmp
```

| 目录 | 大小 |
|------|------|
| Llama4-Scout-W4A16 | 43G |
| LLM-Research (Qwen2.5-7B-Instruct) | 15G |
| Qwen | 15G |
| .hf_cache | 482M |
| **总计** | ~73.5G |

剩余可用: 220G，空间充裕。

## 4. Procrustes Sensitivity 结果

### 文件清单 (`/root/xling_calib_direction/results/`)

| 文件 | 大小 | 修改时间 |
|------|------|----------|
| linproj_procrustes_sensitivity.csv | 30KB | 09:29 |
| linproj_sensitivity.csv | 23KB | 07:39 |
| probing_controls.csv | 457B | 08:04 |
| cka_results.csv | 604B | 04:22 |
| transfer_results.csv | 4.7KB | 02:49 |

### linproj_procrustes_sensitivity.csv

- **行数**: 281 (1 header + 280 data)
- **列**: layer, language, n_pairs, auroc_zs, auroc_proc_mean, auroc_proc_std, ece_zs, ece_proc_mean, ece_proc_std, brier_zs, brier_proc_mean, brier_proc_std, delta_auroc, delta_ece
- **语言**: zh, ar, hi, sw, ko (5种)
- **n_pairs**: 10, 20, 50, 100, 200, 500, 1000 (7级)
- **层数**: 8层 (280 / 5 / 7 = 8)
- **数据完整性**: 280 = 8 layers × 5 langs × 7 n_pairs ✓ 无缺失行
- **重复行风险**: 无（行数精确匹配预期组合数）
- **截断**: 无（所有行列数完整）

### linproj_sensitivity.csv

- **列**: layer, language, n_pairs, ece_zs, ece_ms_mean, ece_ms_std, brier_zs, brier_ms_mean, brier_ms_std, delta_ece
- **语言**: zh, ar, hi, sw, ko (5种)
- **n_pairs**: 10, 20, 50, 100, 200, 500, 1000, 14042 (8级，含全量)
- 数据结构完整

## 5. 活跃进程

- **PID 47972**: `probing_controls_v2.py`，08:56 启动，CPU 89.8%，仍在运行
