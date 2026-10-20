# analysis run statistical tests

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_run_statistical_tests_20260527T194600_result.json`
- **Structured JSON:** [`c6b550720d6deb7c646f.json`](../../sessions/c6/c6b550720d6deb7c646f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本仅输出到 stdout，未生成新文件。`factorial_data.json` 是之前已存在的（May 27 20:20）。

数值验证结果：

```
脚本执行: 成功（return_code=0）
输出文件: 无新文件生成（仅 stdout 输出）
数值验证: 全部一致
```

逐项对比：

| 指标 | 预期值 | 脚本输出 | 匹配 |
|------|--------|----------|------|
| Cell 1 Full OCC BN mean | ~0.725 | 0.7253 | ✓ |
| Cell 1 数据 | [0.746, 0.654, 0.776] n=3 | 同上 | ✓ |
| Cell 2 Full OCC LN mean | ~0.777 | 0.7767 | ✓ |
| Cell 2 数据 | [0.740, 0.792, 0.798] n=3 | 同上 | ✓ |
| Cell 3 Detach BN mean | ~0.767 | 0.7665 | ✓ |
| Cell 3 数据 | [0.774, 0.736, 0.762, 0.794] n=4 | 同上 | ✓ |
| Cell 4 Detach LN mean | 0.826 | 0.8260 | ✓ |
| Cell 4 数据 | [0.826] n=1 | 同上 | ✓ |
| Vanilla mean | ~0.745 | 0.7453 | ✓ |
| Vanilla 数据 | [0.768, 0.748, 0.720] n=3 | 同上 | ✓ |
| Gradient flow main effect Δ | ≈-0.027 | -0.0274 | ✓ |
| Gradient flow p | ≈0.396 | 0.3961 | ✓ |
| Gradient flow Cohen's d | ≈-0.60 | -0.602 | ✓ |
| Cell 1 vs Cell 3 Cohen's d | ≈-0.93 | -0.928 | ✓ |

所有数值与预期完全一致，无差异。

---
