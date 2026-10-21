# code exp013 cross transfer

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp013_cross_transfer_20260512T205129_result.json`
- **Structured JSON:** [`4b3ae59065251695700e.json`](../../sessions/4b/4b3ae59065251695700e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已写入 `scripts/run_cross_transfer.py`（333 行），语法验证通过。

结构：
- `load_features()` — 读 CSV，自动检测特征列，NaN 列均值填充
- `compute_pairwise_auc_cross()` — 跨模型 pairwise AUC（100% train → 100% test）
- `compute_pairwise_auc_self()` — 同模型 GroupKFold(5) pairwise AUC
- `compute_ordinal_cross/self()` — 多分类 accuracy/MAE
- `compute_k_star()` — max k where AUC > 0.60
- LightGBM 参数与 `run_pipeline.py` Step 5 完全一致
- 终端输出 transfer matrix + 自动判断 depth signal 是 text-intrinsic 还是 model-specific

用法示例：
```bash
python scripts/run_cross_transfer.py \
  --data_dirs data_exp001_pythia data_exp002_olmo data \
  --labels Pythia-1.4B OLMo-1B Qwen-1.5B \
  --results_dir results_exp013
```

---
