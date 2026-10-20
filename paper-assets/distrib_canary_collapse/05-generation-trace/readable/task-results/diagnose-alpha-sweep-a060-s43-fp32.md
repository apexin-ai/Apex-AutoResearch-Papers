# diagnose alpha sweep a060 s43 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_alpha_sweep_a060_s43_fp32_20260519T184402_result.json`
- **Structured JSON:** [`269658e9913a6f1666e8.json`](../../sessions/26/269658e9913a6f1666e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 完成进度：9/10 iterative generations

- gen_0 (baseline) 至 gen_9 全部完成，metrics.json 均已保存
- gen_10/10 刚进入 "Generating synthetic data" 阶段即被 timeout (EXIT_CODE=124) 杀掉
- gen_10 目录已创建但为空

### 各代 metrics（ppl 趋势）

| Gen | PPL | Entropy | Eff Rank | MAUVE |
|-----|-----|---------|----------|-------|
| 0 (baseline) | 26.95 | 3.2342 | 46.6 | — |
| 1 | 29.67 | 2.1945 | 68.2 | 0.0313 |
| 2 | 35.22 | 2.1745 | 74.0 | 0.0323 |
| 3 | 38.31 | 2.1749 | 75.6 | 0.0311 |
| 4 | 41.09 | 2.2037 | 75.8 | 0.0302 |
| 5 | 43.72 | 2.1951 | 76.5 | 0.0308 |
| 6 | 46.07 | 2.2344 | 76.2 | 0.0289 |
| 7 | 48.62 | 2.2237 | 76.1 | 0.0294 |
| 8 | 50.40 | 2.2811 | 75.5 | 0.0284 |
| 9 | 49.88 | 2.3089 | 75.0 | 0.0280 |

### Checkpoint 状态

- gen_0 ~ gen_9：完整（synthetic_data + metrics.json；gen_8/gen_9 还有 checkpoint 模型文件）
- gen_10：空目录
- **无 all_metrics.json**（运行未完成，未写入汇总文件）
- **无 W&B**：日志中无任何 wandb 相关输出

### 失败根因

**Timeout 设置过紧。** 训练本身无异常（无 OOM、无 ERROR）。每个 generation 约 40-45 分钟，10 个 iterative generation + baseline ≈ 7h+，而 timeout 仅 ~6h。s42 在 ~4.92h 完成说明不同 seed 的训练耗时存在波动，s43 整体慢约 22%。

### 重跑建议

1. **加大 timeout 至 8h**（28800s），留足余量
2. 可考虑从 gen_9 checkpoint 恢复（如果 `iterative_train.py` 支持 `--resume` 参数），只需跑最后 1 个 generation 即可完成
3. 现有 gen_0-gen_9 数据完整，不要删除

---
