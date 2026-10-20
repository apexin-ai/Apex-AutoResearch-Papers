# code server deploy mvp

**contrastive graph jailbreak detect** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_server-deploy-mvp_20260517T061617_result.json`
- **Structured JSON:** [`ba42ec4cdf0d855d0071.json`](../../sessions/ba/ba42ec4cdf0d855d0071.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

---

## 部署结果

| 项目 | 状态 |
|------|------|
| **Python** | 3.12.3 (miniconda3) |
| **CUDA** | 13.0, Driver 580.76.05 |
| **PyTorch** | 2.8.0+cu128, 2 GPUs 可用 |
| **PyG** | 2.7.0 |
| **依赖** | scikit-learn, pandas, torch-geometric, torch-scatter 已装; torch-sparse 后台编译中（当前代码不依赖） |

## prepare_data.py 输出
- Attack traces: 483
- Benign traces: 500
- Total graphs: 983
- Feature dim: 188
- Tool vocab size: 185
- Failure modes: 10 种攻击模式 + benign

## Dry-run 结果 (3 epochs, 2-fold CV)
- **Fold 0**: AUROC=0.8830, F1=0.7831
- **Fold 1**: AUROC=0.8093, F1=0.6667
- **Average**: AUROC=0.8462±0.0369, F1=0.7249±0.0582

## 修复的问题
- STAC 数据中 `arguments` 字段是双重编码 JSON 字符串，已在 `graph_construction.py` 和 `benign_generator.py` 中修复解析逻辑

## 已部署文件
- `src/graph_construction.py`, `src/augmentations.py`, `src/train_mvp.py`
- `src/data/benign_generator.py`
- `src/models/gin_encoder.py`, `src/models/supcon_loss.py`
- `src/baselines/random_forest.py`
- `prepare_data.py`
- `data/graphs.pt`, `data/tool_vocab.pt`

---
