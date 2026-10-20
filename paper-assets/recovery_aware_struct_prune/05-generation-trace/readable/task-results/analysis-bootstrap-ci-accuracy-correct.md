# analysis bootstrap ci accuracy correct

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap_ci_accuracy_correct_20260519T035328_result.json`
- **Structured JSON:** [`1d9681350296b093f716.json`](../../sessions/1d/1d9681350296b093f716.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

**16 个方法加载成功**（全部 N=1319，i.i.d. binary outcomes）

### 7B 20% sparsity (核心结果)

| 比较 | Gap | 95% CI | 显著性 |
|------|-----|--------|--------|
| SFT CKA-only vs SFT Standard | +4.6% | [+1.7%, +7.5%] | **p=0.002** |
| SFT CKA-only vs SFT RASP | +2.4% | [-0.5%, +5.2%] | n.s. |
| SFT Standard vs SFT RASP | -2.3% | [-5.0%, +0.6%] | n.s. |
| GRPO CKA-only vs SFT CKA-only | +0.5% | [-0.8%, +1.7%] | n.s. |
| GRPO CKA-only vs SFT Standard | +5.1% | [+2.1%, +8.0%] | **p<0.001** |
| GRPO CKA-only vs SFT RASP | +2.8% | [-0.1%, +5.6%] | n.s. (borderline) |

### 7B 25% sparsity
所有 pairwise 比较均不显著（Standard/RASP, GRPO/SFT 之间差异不大）。

### 1.5B 20% sparsity
CKA-only 显著优于所有其他方法（gap 8-13%，p<0.001）。GRPO/SFT 同方法间差异不显著。

### 缺失数据
- `grpo_standard_20` 和 `grpo_rasp_20` 无 N=1319 的 eval（只有 25% sparsity 版本）。

结果 JSON 已保存到 `artifacts/bootstrap_ci_accuracy/bootstrap_ci_accuracy_v2.json`。

---
