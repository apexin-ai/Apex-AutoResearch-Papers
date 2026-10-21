# diagnose s4 ext exit

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_s4_ext_exit_20260519T230225_result.json`
- **Structured JSON:** [`c8765cf42475b89d35d2.json`](../../sessions/c8/c8765cf42475b89d35d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**状态**: SUCCESS — 训练完成 520000 steps（目标 505000），无 error/OOM。

**最终 metrics**: final_step=520000, final_eval_return=938.86 (step 512000)

**完整 eval profile** (52 checkpoints):

| Step | eval_return | | Step | eval_return |
|--------|------------|---|--------|------------|
| 5000 | 33.2 | | 272000 | 927.5 |
| 15000 | 108.8 | | 282000 | 942.6 |
| 25000 | 361.2 | | 292000 | 945.7 |
| 35000 | 279.3 | | 302000 | 940.8 |
| 45000 | 462.6 | | 312000 | 941.7 |
| 55000 | 595.3 | | 322000 | 934.8 |
| 65000 | 698.9 | | 332000 | 954.2 |
| 75000 | 802.0 | | 342000 | 941.0 |
| 85000 | 882.5 | | 352000 | 938.9 |
| 95000 | 819.1 | | 362000 | 939.0 |
| 105000 | 922.8 | | 372000 | 931.2 |
| 112000 | 888.5 | | **382000** | **647.3** |
| 122000 | 905.9 | | 392000 | 931.9 |
| 132000 | 942.2 | | 402000 | 935.0 |
| 142000 | 933.2 | | 412000 | 929.7 |
| 152000 | 891.9 | | 422000 | 930.5 |
| 162000 | 942.5 | | 432000 | 942.5 |
| 172000 | 927.9 | | 442000 | 945.1 |
| 182000 | 926.6 | | 452000 | 960.6 |
| 192000 | 922.3 | | 462000 | 941.5 |
| 202000 | 930.2 | | 472000 | 940.1 |
| 212000 | 938.5 | | 482000 | 958.3 |
| 222000 | 940.4 | | 492000 | 929.3 |
| 232000 | 864.2 | | 502000 | 949.5 |
| 242000 | 933.3 | | 512000 | 938.9 |
| 252000 | 926.6 | | |  |
| 262000 | 942.4 | | | |

**NVE 关注点**: step 382000 出现明显 dip（647.3），之后恢复到 ~930-960 区间。step 232000 也有一次小幅 dip（864.2）。从 ~105k 步后 eval_return 稳定在 920-960 高原区间，确认已收敛。

Registry 已更新为 DONE/success，cron 已删除。

---
