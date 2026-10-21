# research data count check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_data-count-check_20260523T181149_result.json`
- **Structured JSON:** [`bd707ff1c2331c27036d.json`](../../sessions/bd/bd707ff1c2331c27036d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

### 1. 文件行数

| 文件 | 行数 |
|------|------|
| `data/train.jsonl` | 15,290 |
| `data/traj_train.jsonl` | 8,052 |
| `data/test.jsonl` | 1,890 |
| `data/traj_test.jsonl` | 1,032 |
| `data/train_downsampled_400.jsonl` | 447 |
| **总计** | **26,264**（不含 downsampled） |

### 2. CLS train.jsonl

- **Keys**: `code`, `test`, `label`, `source`, `problem_id`, `mutation_type`
- **Unique problem_ids**: 906
- **Unique variants** (problem_id + code[:100]): **3,596**
- **Total samples**: 15,290
- **Tests per variant**: **4.25**

每行 = 1 个 (variant, single_test) 对，每个 variant 平均展开为 ~4.25 个测试样本。

### 3. TRAJ traj_train.jsonl

- **Keys**: `code`, `test_summary`, `label`, `source`, `problem_id`, `mutation_type`, `num_tests`, `num_pass`, `num_fail`
- **Total samples**: 8,052
- 每行是 **variant 级别**，`test_summary` 字段包含该 variant 对应的所有测试摘要（非逐条展开）
- 没有 `test` / `tests` 字段，测试信息聚合在 `test_summary` 中

### 4. Test set

| 数据集 | 样本数 | Variants | Tests/Variant |
|--------|--------|----------|---------------|
| CLS test | 1,890 | 479 | 3.95 |
| TRAJ test | 1,032 | — (variant 级) | — |

### 5. 下采样数据

- `train_downsampled_400.jsonl`: **447 行**

**关键结论**：CLS 数据是 test-level（每行一个测试），TRAJ 数据是 variant-level（每行一个 variant，测试聚合）。CLS train 共 3,596 个 unique variants，TRAJ train 共 8,052 个 variants。

---
