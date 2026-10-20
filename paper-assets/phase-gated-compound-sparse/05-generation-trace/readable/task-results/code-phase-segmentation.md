# code phase segmentation

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase_segmentation_20260513T174515_result.json`
- **Structured JSON:** [`6565bb34280e9a2aff88.json`](../../sessions/65/6565bb34280e9a2aff88.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件已创建并注册：

**`profiling/phase_segmentation.py`** — 核心模块：
- `compute_attention_sparsity`: 逐 head 计算 row-wise max * 1% 阈值下的 sparse 比例，跨 head 平均
- `fit_kde`: Gaussian KDE 拟合，bandwidth 支持 scott/silverman/自定义浮点
- `find_phase_boundaries`: `argrelmin` 检测密度曲线 local minima，渐进式 order 扩大 (5→10→20)，失败时 fallback 等分
- `segment`: 主入口，短序列 (<50) 直接返回单 phase，正常流程输出 `PhaseAnnotation`
- 短 phase 合并逻辑 (`min_phase_length`)

**`profiling/run_profiling.py`** — 流水线脚本：
- `attn_implementation="eager"` 确保拿到完整 attention weights
- 取 prefill pass 的 last-layer attention 做 profiling（MVP 策略）
- CLI 参数：`--model_path`, `--data_path`, `--output_dir`, `--max_new_tokens`, `--batch_size`, `--kde_bandwidth`, `--min_phase_length`
- 输出 `profiling_results.json`，含 phase 标注 + sparsity 统计 + 生成文本

---
