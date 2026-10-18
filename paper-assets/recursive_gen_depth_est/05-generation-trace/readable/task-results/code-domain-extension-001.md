# code domain extension 001

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_domain_extension_001_20260516T071538_result.json`
- **Structured JSON:** [`3d46c865e1af13bd7173.json`](../../sessions/3d/3d46c865e1af13bd7173.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已启动，正在通过 arXiv API 下载 seed data。

**已完成：**
- `scripts/prepare_arxiv_seeds.py` — arXiv API 下载 abstracts，清洗过滤，输出 JSONL（depth_0）
- `scripts/run_domain_extension_arxiv.sh` — 完整 pipeline：seed 准备 → QLoRA finetune×3 → generate d1-d3 → feature extraction → 标准分类 + 5-fold CV
- Registry 已更新为 RUNNING（PID=528179，cuda:1）

**Pipeline 流程：**
1. arXiv API → 500 abstracts → `data/domain_extension/depth_0.jsonl`
2. depth 0→3 循环：QLoRA finetune → nucleus generate（500 samples/depth）
3. Feature extraction（Pythia-1.4B reference）
4. `train_classifier.py`（单 split baseline）+ inline 5-fold CV（RF）
5. 结果输出 `results/domain_extension_001/`，含 `cv_results.json`

**预计用时：** arXiv 下载 ~2min + 3×(finetune ~10min + generate ~15min) + feature extraction ~10min ≈ 1.5-2h。

---
