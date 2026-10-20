# diagnose scaleup failure

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_scaleup-failure_20260516T071954_result.json`
- **Structured JSON:** [`efde32d615f194c2e1fc.json`](../../sessions/ef/efde32d615f194c2e1fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。结论非常明确。

---

## 诊断报告

### 1. 失败主因：**不是真的低成功率，是统计口径错误**

| 指标 | 表观值 | 实际值 |
|------|--------|--------|
| 总条目 | 818 | 104 (真正尝试) |
| 失败 | 737 | 23 |
| 成功 | 81 | 81 |
| **成功率** | **9.9%** | **77.9%** |

737 条"失败"中有 **714 条是 exclusion stubs**——phase 0 已尝试过的任务的去重标记（`task_type: "exclude"`, `error: "exclusion stub from phase 0"`），写入 failed 文件只是为了记录跳过了哪些任务。

### 2. Task Type 分布

**成功 (81 条)**：6 类均衡覆盖，pick_two_obj_and_place 最多(19)，pick_heat 最少(10)

**真正失败 (23 条)**：
- 15 条达到 MAX_STEPS=50 超时（模型在步数预算内未能完成）
- `pick_cool_then_place_in_recep`(8) 和 `pick_heat_then_place_in_recep`(5) 失败最多——涉及多步交互(开冰箱/微波炉)的任务最难

### 3. 81 条成功数据质量

质量**优秀**：
- 步数: min=3, max=41, avg=11.5
- 含完整 think/action/observation 轨迹
- 6 类 task 均有覆盖
- 平均成本 $0.034/条

### 4. 为什么只有 81 条

进程仅运行了 **~51 分钟**就被 kill。吞吐量 127.5 条/小时（4 workers），需要 ~5 小时才能达到 500 成功的目标。被 kill 时只完成了 17% 的工作量。

### 5. 建议

**无需修复代码。** 直接重启进程让它跑完即可。已有的 81 条会被自动跳过（resume 机制），再跑 ~4 小时可收集满 500 条。Phase 0 成功率 70.2%，scaleup 成功率 77.9%——模型表现很好。

如果想进一步提升效率：
- 增加 `--workers 8`（当前 4）可提升吞吐
- 对 `pick_cool/heat` 类任务可考虑增加 MAX_STEPS 到 60-70，减少超时失败

---
