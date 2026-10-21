# preflight post exp001 scripts

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_preflight_post_exp001_scripts_20260517T105158_result.json`
- **Structured JSON:** [`e63b445d0eec2970c13e.json`](../../sessions/e6/e63b445d0eec2970c13e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部检查完毕。汇总如下：

---

## 预检结果

### 1. `analyze_phase0.py` — **就绪**
- **功能**: 从 `phase0_results.json` 读数据，执行 Go/No-go 三条件判定（单调下降、加速比 ≥1.5、PPL 增幅 >20%）+ τ/k 校准
- **输出**: 控制台报告 + `phase0_analysis_report.json` + `phase0_analysis_plots.png`（4 panel: rank、Δ_t、PPL、HellaSwag/distinct-4）
- **参数**:
  ```
  --results-path  (默认 results/phase0_results.json)
  --model-name    (默认 410M)
  --output-dir    (默认 results/)
  ```
- **dry-run `--help`**: 通过
- **依赖**: numpy 2.2.6, matplotlib 3.10.5, json — 全部已装

### 2. `scripts/plot_spectral_trajectory.py` — **就绪**
- **功能**: 生成 5-panel 论文级图（eff_rank、log_det、PPL、distinct-4、HellaSwag），自动从 `results/phase0_results.json` 加载数据（找不到则用硬编码 fallback）
- **输出**: `paper/figures/spectral_trajectory.pdf` + `.png`
- **参数**: 无 CLI 参数，直接 `python scripts/plot_spectral_trajectory.py`
- **注意**: hellaswag 数据在 fallback 值中只到 Gen 5，实际运行时会从 JSON 读取（但 JSON 中无 hellaswag 字段时 hellaswag panel 会用 fallback 值）

### 3. `auto_eval_hellaswag.sh` — **就绪，GPU 参数已修复**
- GPU 参数: `GPU="${1:-cuda:0}"` — 已正确参数化
- 用法: `bash auto_eval_hellaswag.sh [cuda:X]`
- 当前状态: gen0-gen7 已评估完成，gen8-10 待评

### 4. `results/` 目录现状
| 文件 | 说明 |
|------|------|
| `phase0_results.json` | 主结果文件 (4.0KB, 最后更新 17:37) |
| `phase0_analysis_report.json` | 上一次分析报告 (May 16 20:58) |
| `phase0_analysis_plots.png` | 上一次分析图 |
| `hellaswag_gen0/` ~ `hellaswag_gen7/` | Gen 0-7 HellaSwag 结果 |
| `phase1_adaptive_seed42_results.json` | Phase 1 自适应种子结果 |
| `phase0_1b/` | 1B 模型 Phase 0 结果 |

### 5. exp_001 完成后的执行命令

```bash
# 激活环境
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/spectral_collapse_ews

# 1) Go/No-go 分析
python analyze_phase0.py --results-path results/phase0_results.json --model-name 410M

# 2) 论文图
python scripts/plot_spectral_trajectory.py

# 3) HellaSwag 自动评估（如果还有未评估的 gen）
nohup bash auto_eval_hellaswag.sh cuda:0 > results/auto_eval.log 2>&1 &
```

所有脚本和依赖均可立即执行。

---
