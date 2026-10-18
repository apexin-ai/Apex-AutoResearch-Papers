# ssh sdgd framework impl

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_sdgd-framework-impl_20260515T065822_result.json`
- **Structured JSON:** [`b0f056bbd801bc5273a4.json`](../../sessions/b0/b0f056bbd801bc5273a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

### 结果汇总

**文件清单** (服务器 `/root/schema-dag-extraction/src/`):
| 文件 | 状态 |
|------|------|
| `sdgd/__init__.py` | ✓ 已有 |
| `sdgd/similarity.py` | ✓ 已有 |
| `sdgd/graph.py` | ✓ 已有 |
| `sdgd/decompose.py` | ✓ 已有 |
| `sdgd/merge.py` | ✓ 已有 |
| `sdgd/evaluate.py` | ✓ 已有 |
| `run_sdgd_experiment.py` | ✓ 新建 |

**Coloring 测试结果** (66 Few-NERD types, `type_embeddings.pt`):
- `tau = 0.8684`
- `n_batches = 9`
- `batch_sizes = [19, 13, 10, 8, 5, 4, 4, 2, 1]`

**CLI**: 4 种模式 `sdgd_zero | single_pass | per_type | random_batch`，支持 `--decompose_only` 仅运行分解（无 GPU）。

---
