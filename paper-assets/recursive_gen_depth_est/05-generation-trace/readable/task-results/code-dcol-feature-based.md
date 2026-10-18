# code dcol feature based

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dcol_feature_based_20260514T161727_result.json`
- **Structured JSON:** [`4ec655725a1e00ee9c6f.json`](../../sessions/4e/4ec655725a1e00ee9c6f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 完成，全部通过：

- 数据加载正常：20000 样本（4×5000），train=16000, test=4000
- Loss 数值合理：epoch 1 总 loss=1.53（attract=0.27, repulse=0.51, ce=0.76），无 NaN/Inf
- Loss 下降正常：epoch 2 降到 1.25
- 2 个 epoch 已达 73.9% accuracy（对比 RF baseline 78.2%，训练充分后应可超越）
- 所有评估指标输出正常：4-class acc + CI、3-class acc、per-class recall、pairwise AUC、confusion matrix
- 可视化生成正常：t-SNE、PCA、confusion matrix PNG 均成功保存
- Checkpoint 保存正常（含 scaler 参数、feature names）

文件位置：`/root/autodl-tmp/recursive_gen_depth_est/src/dcol_train.py`（服务器上已就绪），本地副本在 `artifacts/dcol_train.py`。

---
