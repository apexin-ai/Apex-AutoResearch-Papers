# ops registry repair running 14b

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_registry-repair-running-14b_20260522T232103_result.json`
- **Structured JSON:** [`5470781412c8a4f784e2.json`](../../sessions/54/5470781412c8a4f784e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

8/8 registry 条目全部创建成功，hypothesis 已更新。汇总：

| exp_id | Server:GPU | PID | Progress | Status |
|---|---|---|---|---|
| scale_14b_t10_a045_s42_fp32 | 17855:cuda:4 | 679204 | **10/10 gen** (可能已完成) | RUNNING |
| scale_14b_t15_a060_s42_fp32_v2 | 17855:cuda:0 | 679656 | 14/15 gen | RUNNING |
| scale_14b_t15_a050_s42_fp32_v3 | 17855:cuda:1 | 680095 | 14/15 gen | RUNNING |
| scale_14b_t15_a045_s42_fp32 | 17855:cuda:5 | 680608 | 12/15 gen | RUNNING |
| scale_14b_t10_a075_s43_fp32 | 17855:cuda:2 | 719178 | 4/10 gen | RUNNING |
| scale_14b_t10_a060_s43_fp32 | 17855:cuda:3 | 719252 | 4/10 gen | RUNNING |
| scale_14b_t15_a075_s42_fp32 | 19828:cuda:0 | 793171 | 10/15 gen | RUNNING |
| scale_14b_t10_a050_s43_fp32 | 19828:cuda:1 | 822048 | 4/10 gen | RUNNING |

注意：`scale_14b_t10_a045_s42_fp32` 已有 gen_0-9 共 10 个 gen 目录（目标 10），可能已完成或正在收尾。

---
