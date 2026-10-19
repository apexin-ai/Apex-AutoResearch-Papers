# research scorer analysis v2

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_scorer-analysis-v2_20260516T050757_result.json`
- **Structured JSON:** [`c9e9aa2726b7e07a77b0.json`](../../sessions/c9/c9e9aa2726b7e07a77b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成，结果写入 `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/action_cond_info_bottleneck/artifacts/scorer_analysis_seed1_step5000.md`。

**核心结论**：

- **分布**: 强 bimodal（U 型）。BC=**0.937**（阈值 0.556），frac<0.2=**41.4%**，frac>0.8=**49.2%**，中间 0.4-0.6 仅 **1.5%**
- **判别度**: within-sample top10/bottom10 = **22.59×**；per-token = 20.24×
- **Logit**: mean=1.45, **std=3.76**（远离 0，sigmoid 推至两端饱和）
- **对比**: v4 collapse 到 std=0.009，v5_stopgrad collapse 到 0，本版 **std=0.440 健康双峰** — diversity 正则有效
- **MVP 判定**: **PASS**（脚本自动判定一致）

**遗留风险**: 空间分布需人工核对 PNG 才能确认热区落在任务区域而非背景。文件路径：
- `/root/acib/outputs/scorer_analysis_seed1_step5000/token_importance_heatmap.png`
- `/root/acib/outputs/scorer_analysis_seed1_step5000/avg_importance_per_camera.png`
- `/root/acib/outputs/scorer_analysis_seed1_step5000/scorer_weight_histogram.png`

注：此次复用了已存在的 `scorer_analysis_seed1_step5000/` 完整结果（生成于 2026-05-16 12:59，4 batch × 8 sample = 32 samples），未重新跑 GPU。脚本本身已完整实现 task 要求的 A/B 两类分析。

---
