# analysis collect supplementary results

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_collect_supplementary_results_20260522T182558_result.json`
- **Structured JSON:** [`8a5b6f7a02f41a3137a0.json`](../../sessions/8a/8a5b6f7a02f41a3137a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Worker A — 跨架构 Cosine Profile 图 ✅ 完成

**文件生成：**
- `fig_cosine_cross_arch.pdf` (20K)
- `fig_cosine_cross_arch.png` (235K)
- 时间：May 23 02:22

**R1-8B Cosine Compression 关键数据：**
- 520 traces, 403,776 step pairs, 32 layers
- Shallow (L0-L5) mean cosine dist: **0.3792**
- Deep (L24-L31) mean cosine dist: **0.3834**
- **Shallow/Deep ratio: 0.9889** → compression confirmed, magnitude 1.1%
- Profile 峰值在 L7-L8 (~0.56)，之后单调递减到 deep layers (~0.36-0.39)

---

### Worker B — Bootstrap CI ⏳ 运行中

- PID 93618, 启动 02:22, 已消耗 ~50 min CPU (1067%)
- 日志停在 "Finding reference layers on full data..." — 正在执行 1000 次 bootstrap 计算
- 无需干预，等待完成即可

---

### Worker C — 分类器敏感性 ⏳ 运行中

- PID 93351, 启动 02:21, 已消耗 ~59 min CPU (1171%)
- 日志停在 "Threshold >= 1: 159 JB / 361 safe (30.6%)" — 正在对每个 threshold 做全量分析
- 无需干预，等待完成即可

---

两个脚本都在高 CPU 利用率下正常运行，未 hang。由于使用 nohup 后台执行，会自动写 JSON 结果到 `artifacts/` 目录。建议 20-30 分钟后再查一次。

---
