# code exp57 svd iid only

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp57_svd_iid_only_20260522T132458_result.json`
- **Structured JSON:** [`e5d541c28d2deb4431ec.json`](../../sessions/e5/e5d541c28d2deb4431ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果如下：

## IID-only SVD vs All-data SVD — F1 对比

| Condition | IID_test | DD | AA | FITD |
|---|---|---|---|---|
| **svd_iid_only_top3** | 1.0000 | **1.0000** | **0.9474** | 1.0000 |
| svd_all_data_top3 | 1.0000 | 0.9937 | 0.9041 | 1.0000 |
| **svd_iid_only_top5** | 1.0000 | **1.0000** | **0.9333** | 1.0000 |
| svd_all_data_top5 | 1.0000 | 0.9937 | 0.8966 | 1.0000 |
| **svd_iid_only_top10** | 1.0000 | **1.0000** | **0.9333** | 1.0000 |
| svd_all_data_top10 | 1.0000 | 0.9937 | 0.8966 | 1.0000 |
| random_3 | 1.0000 | 1.0000 | 0.9542 | 1.0000 |
| full_768 | 1.0000 | 1.0000 | 0.9333 | 1.0000 |

**结论：数据泄漏顾虑消除。** IID-only SVD 在所有 OOD 测试集上表现等于或优于 all-data SVD：
- DD: 1.000 vs 0.9937（IID-only 更好）
- AA: 0.9474 vs 0.9041（IID-only 高 +4.3pp）
- FITD: 1.000 vs 1.000（持平）

子空间对齐分析显示 top-3 方向高度一致（mean cos=0.9739, min cos=0.9332），说明 OOD 数据对 SVD 方向的影响很小。IID train 的 top-3 方向已捕获 96.78% 方差，足以支撑 OOD 泛化。

---
