# code fix icg pipeline

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-icg-pipeline_20260519T170651_result.json`
- **Structured JSON:** [`7ebcc346715f0a646491.json`](../../sessions/7e/7ebcc346715f0a646491.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**所有 5 题全部 10/10 采样成功！non_empty rate = 100%**

对比：
| | 修复前 (K=6) | 修复后 (K=10) |
|---|---|---|
| folio_0 | 5/6 (83%) | **10/10 (100%)** |
| folio_1 | 2/6 (33%) | **10/10 (100%)** |
| folio_2 | 4/6 (67%) | **10/10 (100%)** |
| folio_3 | **0/6 (0%)** | **10/10 (100%)** |
| folio_4 | 1/6 (17%) | **10/10 (100%)** |
| **总计** | **12/30 (40%)** | **50/50 (100%)** |

## 汇报

### 根因分析
- **主因**：零样本 prompt 对 7B 模型太难——模型不知道期望的 JSON + Z3 格式，产出的 z3_formula 无法通过 `parse_z3_formula` 的 `eval()` 验证
- folio_3 完全失败（0/6）：模型生成了 valid JSON，但所有 z3_formula 都无法解析（"JSON ok but 0/7 constraints parsed"）
- folio_4 仅 1/6 成功：同样是 z3_formula 格式问题
- 没有 retry 机制导致失败不可恢复

### 修改内容

**run_icg.py**（4 项改动）:
1. **Few-shot ICG prompt** — 加了 2 个示例展示精确的 JSON + Z3 格式（最高影响）
2. **`_normalize_z3_formula`** — 新增静态方法，处理 Unicode 逻辑符号、量词剥离、函数名大小写（`implies(` → `Implies(`）、`~x` → `Not(x)`
3. **Retry 逻辑** — `_generate_single` 中空结果最多重试 3 次（`--max-retries` 参数）
4. **K_icg 默认值** 6 → 10；`_extract_json` 增加 markdown code fence 剥离

**sica/z3_maxsat.py**（1 项改动）:
- `_preprocess_formula` 增加 Unicode `¬` → `Not `、量词剥离（`∀x:`）、`~x` → `Not(x)`

### 修复后 dry-run 结果
- **non_empty rate: 100%**（50/50，目标 ≥80%）
- ICG accuracy: 0.60 (3/5) vs SC accuracy: 0.40 (2/5)，Delta: +0.20

---
