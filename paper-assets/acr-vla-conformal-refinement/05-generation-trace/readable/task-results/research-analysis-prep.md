# research analysis prep

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_analysis-prep_20260515T052922_result.json`
- **Structured JSON:** [`c40a25c724cdb16037ee.json`](../../sessions/c4/c40a25c724cdb16037ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

VLA-mean 现在正确显示 10/10 tasks, 32%。三个脚本全部正常工作。

## 产出总结

创建了 3 个分析脚本在 `artifacts/` 下：

### 1. `analysis_magnitude_sweep.py`
- 读 registry 中 `eval-mag-perdof-norm*` 和 `eval-mag-obsonly-norm*` 实验
- 自动合并 norm=0.1 的原始 spatial eval 数据作为已知点
- 输出 PDF 曲线图（x=norm log scale, y=SR%, perdof vs obs_only + 三条 baseline 水平线）
- 输出 `figures/magnitude_sweep_summary.json`
- 当前状态：magnitude sweep 实验还没出结果，只有 norm=0.1 一个点。实验完成后重跑即可自动填充

### 2. `analysis_object_benchmark.py`
- 读 6 个 object 实验（VLA-only / VLA-mean / ReconVLA / perdof / obs_only / scalar）
- 输出 grouped bar chart PDF（每个 task 一组 bars）
- 输出 LaTeX table + JSON
- 当前状态：只有 VLA-only 有完整 10 task 数据，其他只有 1/10 (alphabet_soup)

### 3. `analysis_spatial_final.py`
- 自动合并 base + restart 实验的 partial results
- 处理 T1-T10 格式、`T{n}_{task}` 格式、full task name 等各种 metrics 格式
- 输出 LaTeX table（`\textbf` 标注 per-task best）+ JSON
- 当前状态：VLA-only/VLA-mean/ReconVLA 完整，ACR 方法等待 restart 完成

### 使用方式
```bash
cd artifacts/
python3 analysis_magnitude_sweep.py   # → figures/magnitude_sweep_spatial.pdf + .json
python3 analysis_object_benchmark.py  # → figures/object_benchmark.pdf + .tex + .json
python3 analysis_spatial_final.py     # → figures/spatial_final_table.tex + .json
```

实验跑完后直接重跑对应脚本，会自动从 registry.yaml 读取最新数据。

---
