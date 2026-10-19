# prep object benchmark readiness

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_object-benchmark-readiness_20260514T031603_result.json`
- **Structured JSON:** [`f4ce41e8742dcda951ef.json`](../../sessions/f4/f4ce41e8742dcda951ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成，结果如下：

### 验证状态

| 项目 | 状态 |
|------|------|
| Object 数据（10 tasks × 两台服务器） | ✅ 就绪 |
| evaluate.py 支持 `--benchmark object` | ✅ 无需修改 |
| CRM cache/object（14570 samples） | ✅ bjb1 有，bjb2 空（eval 不需要 cache） |
| per-DOF CRM checkpoint | ✅ bjb1 有，❌ bjb2 仅有 spatial-only |
| scalar CRM checkpoint | ✅ bjb1 有，❌ bjb2 无 |

### 关键问题

**bjb2 缺 CRM checkpoints**：bjb2 的 `crm_spatial_only/crm_best.pt` 只在 spatial 数据上训练，不适合 object eval。bjb2 只能跑 vla_only / vla_mean / reconvla。

### GPU 分配方案

5 个方法全部并行：
- **bjb1** GPU 0-3：ACR-VLA、Scalar CRM、ReconVLA、VLA Only
- **bjb2** GPU 0：VLA Mean（不需要 CRM）

5 套精确启动命令已写入 memory.md（`Object Benchmark 评估就绪验证` 段落），spatial 跑完后直接复制执行。

---
