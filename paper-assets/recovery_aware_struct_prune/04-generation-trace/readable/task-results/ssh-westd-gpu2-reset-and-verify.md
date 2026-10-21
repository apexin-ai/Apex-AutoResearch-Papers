# ssh westd gpu2 reset and verify

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd_gpu2_reset_and_verify_20260523T152407_result.json`
- **Structured JSON:** [`d560a1c27fad5af669c0.json`](../../sessions/d5/d560a1c27fad5af669c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果汇总：**

### GPU 状态（全部正常，无需重置）

| GPU | Util | Memory | 状态 |
|-----|------|--------|------|
| 0 | 99% | 29659/97887 MiB | floor_0p6 运行中 |
| 1 | 0% | 0 MiB | 空闲 |
| 2 | 97% | 16767/97887 MiB | grpo_standard_20_fixed 运行中 |
| 3 | 97% | 16767/97887 MiB | sft_standard_20_fixed 运行中 |

### 进程状态

| 实验 | PID | 状态 |
|------|-----|------|
| grpo_standard_20_fixed | 142477 | **存活** |
| sft_standard_20_fixed | 142638 | **存活** |
| floor_0p6 | 132494 | **存活** |

### grpo_standard_20_fixed 进度

- 25/500 (5%)，启动于 23:04，平均 ~40-55s/it
- 预计剩余 ~5-7 小时完成
- 模型已正确加载，检测到 non-uniform MLP（intermediate_size range [8128, 18944]）

GPU 2 状态完全正常，三个实验均正常运行，无需任何干预。

---
