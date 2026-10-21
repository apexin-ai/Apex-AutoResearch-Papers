# ssh exp008 sdgd launch

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp008-sdgd-launch_20260515T074315_result.json`
- **Structured JSON:** [`434b418a70da0a140648.json`](../../sessions/43/434b418a70da0a140648.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-008 已启动，汇总：

| 项目 | 状态 |
|------|------|
| GPU | RTX PRO 6000 Blackwell 98GB, cuda:0 空闲 ✓ |
| 代码 | 所有 SDGD 模块 + runner 就绪 ✓ |
| BCS 矩阵 | `artifacts/sim_matrix.pt` (66 types) ✓ |
| Dry-run | tau=0.8676, 8 batches [18,12,11,7,7,5,3,3] ✓ |
| PID | 241208, vLLM 正在加载模型 |
| 执行顺序 | sdgd_zero → single_pass → random_batch → per_type |
| 日志 | `artifacts/exp008_run.log` |
| 预计耗时 | ~3-4h 总计 |

查看进度：`tail -20 /root/schema-dag-extraction/artifacts/exp008_run.log`

---
