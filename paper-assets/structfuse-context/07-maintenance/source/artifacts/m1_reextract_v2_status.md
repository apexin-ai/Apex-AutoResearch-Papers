# M1 Reextract V2 Status Report

**检查时间**: 2026-05-15 05:10 CST

## 状态：仍在运行

| 指标 | 值 |
|------|-----|
| 开始时间 | 2026-05-14 03:59 CST |
| 已运行 | ~25 小时 |
| 总 instances | 28,276 |
| 已完成 call_graph 提取 | 22,260 (78.7%) |
| 跳过 (already_exists) | 582 |
| 合计进度 | 22,842 / 28,276 (80.8%) |
| 剩余 | ~5,434 |
| ERROR 数 | 0 |
| 当前处理中的 repos | mozilla__bleach, sqlfluff, conan-io, Project-MONAI |
| 磁盘剩余 | 98GB (健康) |

## 速率与 ETA

- 近 3 小时平均速率：~560 instances/hour（早期更快 ~1000/hr，后期 repo 更大更慢）
- 预计剩余时间：~9-10 小时
- 预计完成时间：**2026-05-15 ~15:00 CST**

## 现有数据基线

- `all.jsonl`：44,173 行，6.2GB（May 13 合并，rerun 产出尚未合并）
- 之前 structural data 覆盖率：15,897 / 44,173 (36.0%)
- Rerun 产出以单独 .json 文件存放于 `/root/autodl-tmp/structfuse/full_m1_data/`

## 对 M2 训练的影响评估

### 数据增量预估

若 28,276 个 reextract 全部成功：
- Structural data 覆盖率：(15,897 + 28,276) / 44,173 = ~100%（理论上限）
- 实际保守估计 85-95%（部分小 repo 可能无 dataflow/call_graph）
- 相比之前 36% → 85-95%，增量巨大

### 是否值得用新数据重跑 M2？

**值得。** 理由：
1. Structural data 覆盖率从 ~36% 提升到 ~85-95%，是量级变化
2. 之前 M2 只能在 36% 的数据上学习 structural context fusion，现在几乎全量数据都有
3. 训练信号更充分、分布更均匀（之前 64% 无 structural data 的 instance 相当于噪声）
4. 0 ERROR 说明数据质量可靠

**建议**：等 rerun 完成后合并 all.jsonl，用新数据重跑 M2。
