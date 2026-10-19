# exp pca artifact verification

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_pca_artifact_verification_20260520T043922_result.json`
- **Structured JSON:** [`f7aebc69e87671df51d8.json`](../../sessions/f7/f7aebc69e87671df51d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

正常推进。W1 ~0.8s, W3 ~2.2s。估算 25 layers × 4 windows ≈ 100 combos，主 sweep 约 15-30 分钟，bootstrap 额外 1-2 小时。

实验已提交运行中：
- **Job**: `pca_artifact_verification` on `autodl-rtx6000:cuda:0`
- **内容**: 25 layers × 4 windows × 5 metrics，PCA-100d，bootstrap 1000×
- **输出**: `artifacts/pca_artifact_verification/pca_layer_sweep_results.json` + `comparison_summary.json`
- **基线对比**: 自动读取 `r1_8b_full_layer_sweep/layer_sweep_results.json`（无 PCA）做 per-window best layer 对比
- **预估时间**: 1-3 小时

Dry-run 初步观察（仅 L0 W3）：PCA 后 ba 从 0.79→0.73、precision 从 0.73→0.49，crossing_rate 保持 0.44 不变——说明 PCA 降低了 probe 精度但不影响 crossing_rate（因为 L0 的 crossing_rate 本来就高）。完整 sweep 将揭示 PCA 是否让其他 metrics 也虚假偏向 L0。

---
