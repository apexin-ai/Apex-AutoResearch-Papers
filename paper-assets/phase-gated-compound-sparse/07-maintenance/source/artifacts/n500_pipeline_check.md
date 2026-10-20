# n=500 Pipeline Check — 2026-05-15 10:00 CST

## 1. 实验进度

### 已完成 (9/16 conditions)

| Condition | 完成时间 | 文件大小 | 路径 |
|-----------|---------|---------|------|
| ds_imp_s015 | 02:31 | 22MB | `profiling_output_n500_bf16_ds_imp_s015/profiling_results.json` |
| ds_imp_s020 | 06:55 | 22MB | `profiling_output_n500_bf16_ds_imp_s020/profiling_results.json` |
| ds_rand_s015 | 02:05 | 22MB | `profiling_output_n500_bf16_ds_rand_s015/profiling_results.json` |
| ds_rand_s020 | 06:30 | 22MB | `profiling_output_n500_bf16_ds_rand_s020/profiling_results.json` |
| qw_imp_s015 | 03:02 | 18MB | `profiling_output_n500_bf16_qw_imp_s015/profiling_results.json` |
| qw_imp_s020 | 06:27 | 18MB | `profiling_output_n500_bf16_qw_imp_s020/profiling_results.json` |
| qw_imp_s025 | 09:53 | 18MB | `profiling_output_n500_bf16_qw_imp_s025/profiling_results.json` |
| qw_rand_s015 | 03:11 | 18MB | `profiling_output_n500_bf16_qw_rand_s015/profiling_results.json` |
| qw_rand_s020 | 06:36 | 18MB | `profiling_output_n500_bf16_qw_rand_s020/profiling_results.json` |

所有路径相对于 `/root/autodl-tmp/pacs/`。

### 正在运行 (4 GPUs, 77-80% utilization)

| GPU | PID | Condition | 启动时间 | 预计完成 |
|-----|-----|-----------|---------|---------|
| 0 | 176592 | ds_imp_s025 | 06:55 | ~11:19 |
| 1 | 173536 | ds_rand_s025 | 06:30 | ~10:55 |
| 2 | 187225 | qw_imp_s030 | 09:53 | ~13:18 |
| 3 | 174641 | qw_rand_s025 | 06:37 | ~10:02 |

### 待启动 (自动接力, shell 脚本顺序执行)

| GPU | Condition | 预计启动 | 预计完成 |
|-----|-----------|---------|---------|
| 0 | ds_imp_s030 | ~11:19 | ~15:43 |
| 1 | ds_rand_s030 | ~10:55 | ~15:20 |
| 3 | qw_rand_s030 | ~10:02 | ~13:27 |

**全部 16 conditions 预计完成: May 15 ~15:45 CST** (瓶颈: DeepSeek s030, ~4h24m/condition)

Qwen 4 个 conditions 全部完成预计 ~13:27。

## 2. 分析 Pipeline 状态

**脚本:** `analyze_n500_unified.py` (676 行)

### D054 合规性 ✅
- 主指标: **median** II phase gradient (low − high), NOT mean
- Bootstrap 95% CI: B=10000, percentile method, seed=42

### D059 合规性 ✅
- Cohen's d_z: **仅 within-importance** 配对 (4 对: s015↔s020, s020↔s025, s025↔s030, s015↔s030)
- Random within-sparsity: Wilcoxon + median_diff only, **无 d_z**
- Imp-vs-rand: Wilcoxon + median_diff only, **无 d_z**

### 其他分析
- Mid-phase null rate per condition
- Dose-response permutation monotonicity test (N_perm=5000)
- Bonferroni correction on all p-values
- LaTeX table output (`--latex`), CSV export (`--csv`)

### 验证结果
- Dry-run (n=50): ✅ 全部输出正确, JSON + LaTeX 生成成功
- Partial n500 (DeepSeek only, 4 conditions): ✅ 缺失 condition 优雅降级 ("missing data")
- 完整运行命令: `python analyze_n500_unified.py --latex --csv`

## 3. 结论

- **Pipeline READY**: 全部 condition 完成后可立即运行分析, 无需任何代码修改
- **无阻塞问题**: 分析脚本已验证, D054/D059 合规
- **调度自动化**: shell 脚本 (`run_c2_n500_gpu{0,1}.sh`, `run_c2_qw_n500_gpu{2,3}.sh`) 顺序执行 s015→s020→s025→s030, 无需手动启动 s030
- **哨兵文件**: 完成后写入 `/tmp/agent-ml-exit/c2_qw_n500_r3.exit` (Qwen) 供 cron 监控
