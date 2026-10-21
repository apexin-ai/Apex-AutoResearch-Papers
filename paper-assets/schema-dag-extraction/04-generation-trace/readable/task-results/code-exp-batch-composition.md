# code exp batch composition

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_batch_composition_20260516T045257_result.json`
- **Structured JSON:** [`74b1b2496de7ebc3f55a.json`](../../sessions/74/74b1b2496de7ebc3f55a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

代码完成，dry-run 验证通过。

**总结：**

- 代码文件：`/root/schema-dag-extraction/src/run_batch_composition.py`
- 三种 mode 均可正常运行（dry-run 验证）
- 分区结果对比（K=8, 80 types）：

| Mode | Mean BCS | BCS Range | Batch Sizes |
|------|----------|-----------|-------------|
| single_pass | 0.5572 | — | [80] |
| random_batch | 0.5621 | [0.5268, 0.6262] | 8×10 |
| **confusability_aware** | **0.5524** | [0.4762, 0.6192] | 8×10 |

- Confusability-aware 的 mean BCS (0.5524) < random (0.5621) < single_pass baseline (0.5572)
- Graph coloring 产生 19 colors → 合并+平衡后得到 8 个均匀 batch（各 10 types）
- 自适应 threshold = 75th percentile SCS = 0.6229，产生 790 edges

运行实验时用 `--stage all --mode &lt;mode>` 不加 `--dry_run` 即可。

---
