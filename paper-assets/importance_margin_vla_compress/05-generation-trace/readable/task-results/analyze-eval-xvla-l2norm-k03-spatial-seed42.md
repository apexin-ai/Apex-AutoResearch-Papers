# analyze eval xvla l2norm k03 spatial seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_xvla_l2norm_k03_spatial_seed42_20260523T204234_result.json`
- **Structured JSON:** [`e8273500e8e68d0c7be4.json`](../../sessions/e8/e8273500e8e68d0c7be4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE (negative)。

## 分析总结

**X-VLA L2norm k=0.3 Spatial SR = 31.2%** [95% CI: 27.3%–35.4%]

### 对比

| 配置 | Spatial SR |
|------|-----------|
| L2norm k=0.5 | 58.8% |
| **L2norm k=0.3** | **31.2%** |
| Random k=0.5 | 71.4% |

- 从 k=0.5→k=0.3，L2norm 暴跌 27.6pp（58.8%→31.2%）
- 与 Object 套件模式一致：Object L2norm k=0.3 = 18.2%，同样在极端剪枝下严重退化

### Per-task 分布（方差极大）

高：task2=82%, task0=74%, task4=66%
中：task3=34%, task8=34%
低/崩溃：task7=8%, task1=6%, task6=4%, task9=4%, **task5=0%**

### Hypothesis 验证

**已验证** — L2norm 反转现象在 Spatial 上同样存在。极端剪枝（k=0.3, 70% token removed）下，L2norm 在两个套件上都严重退化（Object 18.2%, Spatial 31.2%），确认 L2norm 反转具有跨套件一致性。

---
