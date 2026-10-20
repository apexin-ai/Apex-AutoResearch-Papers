# ops cuda2 harvest and case study

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cuda2_harvest_and_case_study_20260519T110142_result.json`
- **Structured JSON:** [`2811139056177fcd3ce0.json`](../../sessions/28/2811139056177fcd3ce0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 任务 A：GRPO Standard fair v3
- **仍在运行**，PID 76392，进度 **156/164 (95.1%)**
- 中间 pass@1 约 **0.1143** (at problem 140)
- 预计 ~15 分钟完成
- 已更新 registry notes

### 任务 B：HumanEval Case Study (GRPO CKA-only vs GRPO RASP fair)
SFT CKA-only v2 (PID 78740) 仍在运行，按计划使用 GRPO CKA-only vs GRPO RASP fair 做对比。

**核心发现**：

| | CKA-only | RASP fair |
|---|---|---|
| 通过数 | 33/164 (20.12%) | 18/164 (10.98%) |
| CKA独有通过 | 28 | - |
| RASP独有通过 | - | 13 |
| 两者都通过 | 5 | 5 |

**失败模式对比**：
- **Reasoning-as-code**（输出自然语言推理而非代码）：CKA 47次 vs RASP 59次，RASP 更严重
- **Logic error**（代码能跑但答案错）：CKA 8次 vs RASP **27次**，RASP 的算法准确性受损更严重
- CKA 独有通过的 28 题中，RASP 失败原因：11个 reasoning-as-code + 8个 logic error
- RASP 独有通过的 13 题中，CKA 失败原因：6个 max length + 4个 reasoning-as-code（CKA 在简单题上随机陷入冗长推理）

报告已写入远程 `/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_case_study.md` 并注册为 artifact (`art_20260519_04604c`)。

---
