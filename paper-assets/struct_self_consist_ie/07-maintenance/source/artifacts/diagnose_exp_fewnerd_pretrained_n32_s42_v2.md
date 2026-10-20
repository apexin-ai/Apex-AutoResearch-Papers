# 诊断报告: exp_fewnerd_pretrained_n32_s42_v2

**日期**: 2026-05-23  
**结论**: ✅ 实验已成功完成，cron 监控误判为失败

## Root Cause

实验未失败。Cron 监控系统 5 次检查均未发现 sentinel 文件或 W&B 记录，因此误报为失败。实际上实验正常运行并完成了全部处理。

- 无 sentinel 文件写入 `/root/runs/struct_self_consist_ie/`
- 无 W&B 集成

## 运行时间线

- 启动: 2026-05-23 00:15:18
- 完成: 2026-05-23 19:28:53
- 总耗时: ~19 小时 13 分钟
- 进度: 37648/37648 (100%)，吞吐 ~17.4 it/s

## 产出文件

| 文件 | 大小 | 状态 |
|------|------|------|
| `output/fewnerd_pretrained_n32_seed42/samples.jsonl` | 7.2 GB (37648 行) | ✅ 完整 |
| `output/fewnerd_pretrained_n32_seed42/report.json` | 1.7 KB | ✅ 完整 |
| `output/fewnerd_pretrained_n32_seed42/n32_analysis.json` | 528 B | ✅ 完整 |

## 关键指标

### report.json
- greedy_f1: **0.5125**
- oracle_f1: **0.6674** (headroom: +15.5pp)
- Soft Jaccard ρ(SJ, F1): **+0.4528** (conditional, p=0)
- Fleiss κ mean: 0.5755
- Logprob ρ: +0.1981, AUROC: 0.6006
- structural_beats_surface: **true** (ρ advantage: +0.0515)
- verdict: **PASS**

### n32_analysis.json
- greedy_f1: 0.5390
- mv_f1: **0.5775** (+3.85pp over greedy)
- lp_f1: 0.5287 (-1.03pp, worse than greedy)
- oracle_f1: 0.7046 (+16.6pp headroom)
- degen_rate: 5.42%
- capture_rate: 19.04%
- mv_ci: [2.64, 2.92] pp

## 系统状态

- **GPU**: 4× RTX 5090, 全部空闲 (0% util, 无进程)
- **磁盘**: /root/autodl-tmp 250GB, 已用 238GB (96%) — 剩余 13GB，偏紧
- **进程**: 无 run_mvp_pilot 残留进程

## 建议

1. **无需修复** — 实验已完成且 verdict=PASS
2. **监控侧修复**: 脚本应检查 output 目录下的 report.json 是否存在作为完成标志，而非仅依赖 sentinel 文件
3. **磁盘注意**: 数据盘已用 96%，后续实验前清理旧输出或扩容
