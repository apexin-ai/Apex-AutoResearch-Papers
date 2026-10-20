# code exp 012 script verify

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_012_script_verify_20260515T151147_result.json`
- **Structured JSON:** [`6c7f12e9a817b00826d2.json`](../../sessions/6c/6c7f12e9a817b00826d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Dry-run 完全通过。** 全部 3 个模型加载、推理、分析、可视化均无报错。

## 结果汇总

### 1. 脚本路径和修改
- **路径**: `/root/autodl-tmp/gen-depth-contamination/scripts/exp012_ppl_depth_correlation.py`
- **主要修改**:
  - 新增 `--device` 参数（支持 `cuda` / `cpu` / 自动检测）
  - `--max_samples` 改名为 `--n_samples`
  - 输出路径改为 `artifacts/exp012_results.json` 和 `artifacts/exp012_confidence_vs_depth.pdf`
  - 新增 `make_plots()` 函数：4×3 scatter plot（4 model conditions × 3 methods），每个子图标注 Spearman ρ
  - Binoculars performer 修正为 `allenai/OLMo-1B-0724-hf`（原 `allenai/OLMo-1B-0724` 已下架）
  - 删除旧的 `--dry_run` 纯数据加载模式，改为直接用 `--n_samples 5` 做端到端验证
  - 有一个 deprecation warning `torch_dtype` → `dtype`，不影响运行

### 2. Dry-run 结果
- **设备**: GPU (CUDA), RTX 4090 D
- **参数**: `--n_samples 5 --batch_size 2`
- **状态**: 通过，全部 3 个产出文件生成
  - `exp012_results.json` (4KB)
  - `exp012_per_sample_scores.json` (5.8KB)
  - `exp012_confidence_vs_depth.pdf` (54KB)

### 3. 正式运行时间预估
- Dry-run 120 texts（5 samples × 6 depths × 4 conditions）
- 正式运行 12000 texts（500 samples × 6 depths × 4 conditions）→ 100× 数据量
- 3 个模型各跑一遍 × 100 倍数据 → 预估 **~60-90 分钟** on GPU

---
