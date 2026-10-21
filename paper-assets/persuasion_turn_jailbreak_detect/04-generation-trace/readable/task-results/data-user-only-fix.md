# data user only fix

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_user-only-fix_20260517T063114_result.json`
- **Structured JSON:** [`1028e09fc1ad05659c19.json`](../../sessions/10/1028e09fc1ad05659c19.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

处理完成。汇总：

| 指标 | 值 |
|------|-----|
| 总对话数 | 500 |
| train / val / test | 350 / 75 / 75 |
| 含 assistant turn 的对话 | **0**（全部清除） |

**各 attack_type avg user turns：**
- cipher-based (tom-gibbs, 115条): 10.43
- persuasion-based (safemtdata, 135条): 5.00
- benign (wildchat, 250条): 7.47

**全集 user turns：** avg=7.48, median=6.0, min=3, max=36

attack_type 分布和 split 条数均保持不变。结构性 shortcut 已消除——所有数据集现在统一为 user-only turn sequences。

---
