## CWM 8B Eval Shard Progress (检查时间: 2026-05-16 04:31 UTC / 12:31 CST)

| Shard | GPU | Output Dir | Index Range | Expected | Completed | % | PID Status |
|-------|-----|-----------|------------|----------|-----------|---|------------|
| v3    | cuda:0 | cwm_8b_ckpt400_test/ | 0→全量(9784) | 9784 | 7208 | 73.7% | alive (443221) |
| shard3| cuda:0* | cwm_8b_ckpt400_test_shard3/ | 6200-7680 | 1480 | 952 | 64.3% | alive (453335) |
| shard2| cuda:1 | cwm_8b_ckpt400_test_shard2/ | 7680-9784 | 2104 | 1592 | 75.7% | alive (448094) |
| shard4| cuda:2 | cwm_8b_ckpt400_test_shard4/ | 9100-9783 | 684 | 688 | 100% | completed |

### 注意事项

1. **v3 无分片限制**: PID 443221 的命令行无 `--start_idx`/`--end_idx`，正在跑全量 test set（9784 samples）。当前已到 index 7207，已越过 shard3 范围（6200-7680），后续会与 shard2 范围重叠。
2. **v3 实际用 cuda:0**（非 cuda:3），输出目录是 `cwm_8b_ckpt400_test/`（非 `_v3`）。
3. **shard4 多出 4 行**: 688 vs 预期 684，可能包含边界样本。

### ETA 估算

| Shard | 速率 (samples/min) | 剩余 | 预计完成 (CST) |
|-------|--------------------|------|---------------|
| v3    | ~7.4 | 2576 | ~18:20 (约5.8h后) |
| shard3| ~8.6 | 528  | ~13:32 (约1h后) |
| shard2| ~8.7 | 512  | ~13:29 (约1h后) |
| shard4| — | 0 | ✅ 已完成 |

**shard2 和 shard3 约 1 小时内完成。v3 因跑全量集还需约 5.8 小时。**

由于 shard2+shard3+shard4 覆盖了 idx 6200-9783，v3 覆盖 idx 0-9783，所以 shard2/3 完成后 idx 6200-9783 的结果即可用（无需等 v3）。v3 独占覆盖 idx 0-6200 需等到 ~18:20 CST——但 v3 当前已到 7208，所以 idx 0-6200 的结果已在 v3 输出中。**实际上全量结果现在就可拼接**（v3 的前 6200 行 + shard3 + shard2 的去重合并），只需等 shard2/3 完成约 1 小时。
