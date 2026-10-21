# ssh registry audit all gpus

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_registry_audit_all_gpus_20260523T234445_result.json`
- **Structured JSON:** [`f6ccfeb1eb2c691916a7.json`](../../sessions/f6/f6ccfeb1eb2c691916a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 6 个进程与 registry 完全匹配，无缺失、无多余。

## 核对结果

| Server:GPU | PID | 实验 | Registry 状态 | 备注 |
|---|---|---|---|---|
| westd:0 | 166245 | eval_math500_sft_standard_25_fixed_v2 | RUNNING ✓ | 16824 MiB, GPU 98% |
| westd:1 | 168524 | eval_math500_grpo_rasp_alpha2p0_20_fixed | RUNNING ✓ | 16984 MiB, GPU 99% |
| westd:2 | 171964 | eval_math500_sft_rasp_alpha2p0_20_fixed | RUNNING ✓ | 16984 MiB, GPU 91% |
| westd:3 | 168451 | eval_math500_grpo_cka_only_25_fixed | RUNNING ✓ | 16846 MiB, GPU 98% |
| westb:0 | 335348 | eval_math500_sft_random_20_fixed_v3 | RUNNING ✓ | 15354 MiB, GPU 99% |
| westb:1 | 330254 | eval_math500_grpo_random_20_fixed | RUNNING ✓ | 15354 MiB, GPU 99% |

## 缺失记录（需补）

无。

## 意外发现

无。所有 6 张 GPU 上的进程 PID 与 registry 预期一一对应，全部正常运行中。

---
