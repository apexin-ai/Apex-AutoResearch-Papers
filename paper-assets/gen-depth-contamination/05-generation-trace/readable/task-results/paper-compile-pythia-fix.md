# paper compile pythia fix

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_compile_pythia_fix_20260523T075536_result.json`
- **Structured JSON:** [`57b800f510ee424d665f.json`](../../sessions/57/57b800f510ee424d665f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇报：

**编译状态**：0 errors，PDF 生成成功（18 页总计）。

**Pythia-1.4B AUC 数据一致性**：Table 2 与 Table 10 完全一致 ✓

| Depth Pair | Table 2 | Table 10 | 匹配 |
|---|---|---|---|
| 0v1 | .9722 | .9722 | ✓ |
| 1v2 | .6074 | .6074 | ✓ |
| 2v3 | .5440 | .5440 | ✓ |
| 3v4 | .5051 | .5051 | ✓ |
| 4v5 | .5079 | .5079 | ✓ |

与预期值完全吻合：0v1=.9722, 1v2=.6074, 2v3=.5440, 3v4=.5051, 4v5=.5079 ✓

**CI 一致性**：
- 1v2 CI：两表均为 [.598, .617] ✓
- 2v3 CI：两表均为 [.534, .554] ✓

**页数**：正文 8 页（pages 1-8），Limitations 从第 9 页开始（不计入页数限制），符合 EMNLP 2026 要求 ✓

---
