# ssh sdgd cal impl

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_sdgd-cal-impl_20260515T082408_result.json`
- **Structured JSON:** [`9bbda9e66fefdab976b0.json`](../../sessions/9b/9bbda9e66fefdab976b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

---

## 代码结构

### 新文件
- **`src/sdgd/calibrate.py`** — SDGD-cal 核心模块
  - `build_confusion_matrix(predictions, gold_labels, type_list)` — 从 calibration 样本构建 empirical confusion matrix，基于 text overlap 匹配 gold↔pred entity
  - `confusion_to_similarity(C, normalize='symmetric')` — 将 confusion matrix 转为 [0,1] similarity matrix，对角线=0，格式与 cosine sim 一致
  - `run_calibration(...)` — 用 vLLM 在 calibration 样本上做 single-pass 推理，返回 `(confusion_matrix, similarity_matrix)`

### 修改文件
- **`src/sdgd/decompose.py`**
  - `sdgd_decompose()` — 新增 `confusion_matrix_path` 支持，优先加载 `.npz` confusion-based sim matrix
  - `sdgd_cal_extract()` — 新函数，完整 SDGD-cal pipeline：calibration → confusion → similarity → threshold → graph coloring → batched extraction → merge
- **`src/sdgd/__init__.py`** — 导出 `sdgd_cal_extract`, `build_confusion_matrix`, `confusion_to_similarity`, `run_calibration`
- **`src/run_sdgd_experiment.py`**
  - `--mode sdgd_cal` 新选项
  - `--cal_samples 100`（calibration 样本数）
  - `--confusion_matrix_path`（跳过 calibration，加载预计算的 confusion matrix）

### 验证结果
- `build_confusion_matrix`: gold org→pred person 正确记录为 C[org][person]=1 ✓
- `confusion_to_similarity`: symmetric normalization + rescaling 数值正确 ✓
- 所有 import 正常，experiment runner `--help` 显示新参数 ✓

---
