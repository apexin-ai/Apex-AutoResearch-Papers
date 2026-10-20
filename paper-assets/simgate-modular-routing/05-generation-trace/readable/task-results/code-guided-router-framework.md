# code guided router framework

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_guided-router-framework_20260516T132121_result.json`
- **Structured JSON:** [`caa3cba7b5d3b6290d98.json`](../../sessions/ca/caa3cba7b5d3b6290d98.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。代码框架已创建并通过验证。

## 结果

```
guided_router/
├── __init__.py
├── config.py          # 11 tasks death risk labels
├── router.py          # GuidedRouter (oracle + learned)
├── eval_episode.py    # Episode-level balanced_acc evaluation
├── run_guided_router.py  # Main entry
└── README.md
```

**评估结果 (245 episodes, 95 有区分度)**:

| Method | Episode bal_acc |
|--------|----------------|
| always-deterministic | 50.00% |
| trained 1.7B | 47.10% |
| trained 4B | 58.96% |
| **guided oracle** | **62.92%** |
| **guided learned** | **62.92%** |

Oracle 和 learned 在这个数据集上表现一致（因为 learned 的 task_type 字符串模式匹配在 11 个已知任务上等价于 oracle）。两者都超过 4B trained router (+3.96pp)。

关键细节：
- det_recall = 81.4%, internal_recall = 44.4%
- 150/245 episodes 是 "no-preference"（两条路都死或 tie），被排除
- `find-non-living-thing` 是唯一被路由到 internal 的 task，它的 internal_recall=100%（正确），但一些 death-risk task 中有 internal-preferred 的 episode 被误分类为 det-preferred

---
