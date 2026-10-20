# code seed0 analysis prep

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_seed0_analysis_prep_20260514T091216_result.json`
- **Structured JSON:** [`38bd835b4ae6fc22383d.json`](../../sessions/38/38bd835b4ae6fc22383d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

---

## 进度报告

| 项目 | 状态 |
|------|------|
| 进程 | PID 122208 存活，已运行 8h28m |
| 当前阶段 | **G0 完成** → 正在为 G1 生成合成数据 (291/306, **95%**) |
| 预计生成完成 | ~20 分钟后 |
| 预计全部完成 | 还需 **~10-11 小时**（G1 训练+评估+生成 + G2 训练+评估） |
| 磁盘 | 134G/250G (54%)，空间充足 |

**G0 seed0 vs v7 初步对比（final_model）：**

| 指标 | v7 (seed=42) | seed0 (seed=0) | 差异 |
|------|-------------|---------------|------|
| eff_rank | 676.96 | 676.89 | -0.01% |
| ppl | 13.27 | 13.27 | +0.01% |
| vocab_cov | 0.469 | 0.468 | -0.24% |

G0 阶段两个 seed 的 metrics 高度一致，复现性良好。

## 产出

`analyze_seed0_vs_v7.py` 已部署到服务器 `/root/collapse-aware-mixing/`，语法验证通过，dry-run 输出正常。G1/G2 完成后直接运行即可得到最终判定。

---
