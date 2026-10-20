# MMCT α=0.10 矛盾调查

## 可用实验

| exp_id | seed | precision | 数据位置 | MMCT v2 数据 | 状态 |
|--------|------|-----------|----------|-------------|------|
| a010_s42 | 42 | pre-D080 (可能 bf16) | results/alpha_sweep/a010_s42/ | unified_data/a010_s42.json | MMCT v2 已跑 |
| a010_s43 | 43 | bf16 | 已删除/不在 results/ | 无 | 仅有 artifact 分析报告 |
| a010_s43_fp32 | 43 | fp32 | 不在 results/alpha_sweep/ | 无 | 有 artifact 分析报告，未入 MMCT pipeline |
| a010_s42_fp32 | 42 | fp32 | - | - | RUNNING (17855:cuda:5) |

## 各实验 MMCT 结果

| exp_id | precision | 方法 | wpair_fwd | wpair_bidir | 具体 pairs |
|--------|-----------|------|-----------|-------------|------------|
| a010_s42 | pre-D080 | **MMCT v2** (置换检验+null分布) | **1/8** | 1/8 | ece->distinct_2 (p=0.04) |
| a010_s43_fp32 | fp32 | **简单共识** (k>=4/5, 无null分布) | **4/8** | - | token_entropy->{d1,d2,d3,mauve} (均依赖TY作为第4票) |
| a010_s43_fp32 | fp32 | C003修正后 (排除TY) | **0/8** | - | 全部降至k=3 |
| a010_s43 | bf16 | 简单共识 (k>=4/5) | 0/8 | - | 最高k=3 (naive+diff+thresh) |

## 矛盾根因

**4/8 来源**: `artifacts/alpha_sweep_a010_s43_fp32/report/analysis_2d0093.md` 第57-58行:
```
### MMCT
- Mode: weighted_pair_forward (simple consensus, no null distribution)
- Detection rate: 0.5 (4/8 pairs)
```
该报告将 consensus_k4 计数**误标为 "MMCT"**，但实际上:
1. 没有使用 MMCT 置换检验和 null 分布校准
2. 4/8 的 4 个 pair 全部依赖 TY Granger 作为第 4 票 (naive+diff+thresh+**ty**)
3. C003 约束明确排除 α≤0.50 下的 TY Granger (d_max 跨 seed 不稳定)
4. 排除 TY 后, 4 个 pair 均降至 k=3, consensus_k4 = **0/8**

**1/8 来源**: 正式 MMCT v2 分析 (`mmct_results_v2.json`), 使用 a010_s42 数据, 通过置换检验对比 null 分布。仅 ece->distinct_2 显著 (p=0.04)。

**根因总结**: 
- 分析报告将简单共识计数误标为 "MMCT"，产生了 4/8 的虚高数字
- 该 4/8 完全依赖 C003 排除的 TY Granger，修正后为 0/8
- 正式 MMCT v2 只有 a010_s42 的 1/8 是经过 null 分布校准的真实结果

## 附加问题

1. **a010_s42 provenance**: 此实验为 pre-D080 数据，可能实际为 bf16 (D080 dtype bug)。a010_s42_fp32 正在运行中
2. **a010_s43_fp32 未入 MMCT pipeline**: 该实验结果不在 `results/alpha_sweep/` 中，未被 MMCT v2 脚本处理。即使入 pipeline，C003 修正后预期结果仍为 0/8 或接近 0/8
3. **a010_s43 bf16 已删除**: 结果目录不在服务器上，仅有 artifact 分析报告

## 建议

1. **dose-response 表当前应使用 1/8 (12.5%)** 来自 a010_s42 MMCT v2，标注 "single seed, pre-D080 provenance"
2. 待 a010_s42_fp32 完成后，用 fp32 数据重跑 MMCT 作为权威值
3. 分析报告中的 "MMCT 4/8" 标注应更正为 "simple consensus k4 (pre-C003)"，避免后续混淆
4. ROADMAP 和 reviewer.md 中的 "4/8 vs 1/8 矛盾" 条目可关闭：两个数字来自不同方法，不存在真正矛盾
