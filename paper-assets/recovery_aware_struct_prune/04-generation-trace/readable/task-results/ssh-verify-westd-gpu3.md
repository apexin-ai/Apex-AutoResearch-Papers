# ssh verify westd gpu3

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify_westd_gpu3_20260523T223742_result.json`
- **Structured JSON:** [`19b35e2b635225cc50ed.json`](../../sessions/19/19b35e2b635225cc50ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### GPU 3 竞争检查：**无竞争，无需 kill**

GPU 3 只有 PID 168451（grpo_cka_only_25_fixed eval），没有 sft_rasp_alpha0p5 或其他额外进程。Director 报告的竞争可能已自行结束。

### 4 张 GPU 当前进程

| GPU | PID | 进程 | 显存 | 利用率 |
|-----|-----|------|------|--------|
| 0 | 166245 | eval_math500 **sft_standard_25** (fixed_v2, seed42, bf16) | 16824 MiB | 96% |
| 1 | 168524 | eval_math500 **grpo_rasp_alpha2p0_20** (fixed) | 16732 MiB | 98% |
| 2 | 171964 | eval_math500 **sft_rasp_alpha2p0_20** (fixed) | 16732 MiB | 96% |
| 3 | 168451 | eval_math500 **grpo_cka_only_25** (fixed) | 16846 MiB | 98% |

4 张卡都满载运行 eval_math500，各自独占一张卡。

### 最新已完成的 eval 结果（May 24）

| 文件 | 时间 | Accuracy | N_correct/Total |
|------|------|----------|-----------------|
| grpo_standard_20_fair_fixed | 06:09 | **27.0%** | 135/500 |
| grpo_rasp_alpha1p0_20_fixed | 05:21 | **23.0%** | 115/500 |
| sft_rasp_alpha1p0_20_fixed | 02:33 | **21.6%** | 108/500 |

---
