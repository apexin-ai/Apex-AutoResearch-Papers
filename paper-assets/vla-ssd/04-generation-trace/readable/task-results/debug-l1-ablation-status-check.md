# debug l1 ablation status check

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_l1_ablation_status_check_20260517T142634_result.json`
- **Structured JSON:** [`6d0be796f6ace392ad0d.json`](../../sessions/6d/6d0be796f6ace392ad0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态报告

### 1. 进程
PID 891475 已结束，无残留进程。

### 2. 结果文件
`results_v2.json` 已生成（1214 bytes, 21:11）。

### 3. 结果内容

**所有条件下、所有层的 probing accuracy 均为 1.0：**

| Condition | L1 | L8 | L16 | L31 |
|---|---|---|---|---|
| baseline | 1.0 | 1.0 | 1.0 | 1.0 |
| ablate_all24 (ablate 24 instruction heads) | 1.0 | 1.0 | 1.0 | 1.0 |
| ablate_top5 (heads 0,10,14,22,25) | 1.0 | 1.0 | 1.0 | 1.0 |
| ablate_control8 (8 non-instruction heads) | 1.0 | 1.0 | 1.0 | 1.0 |

**Metadata**: 50 images, 10 tasks, 10 instructions, 5 demos/task, label = instruction_id (0-9), train tasks 0-7, test tasks 8-9.

### 4. 目录下所有文件
- `test_results.json` (v1 test)
- `results.json` (v1)
- `test_v2.json` (v2 test)
- `results_v2.json` (v2)

### 5. GPU 状态
2× NVIDIA RTX PRO 6000 Blackwell (各 ~98GB VRAM)，空闲，0% 利用率，无运行进程。

### 关键发现
所有 ablation 条件的 accuracy 都是 1.0，说明 ablation 没有产生任何效果。这很可能意味着 **instruction identity 信息在 L1 层就已经完美可分，且 ablate L1 的 attention heads 后信息仍然完整保留**——probe 分类任务太简单（10-class, 50 images），或者 instruction 信息通过 residual stream 而非 attention heads 传递，ablation 未能阻断信息流。

---
