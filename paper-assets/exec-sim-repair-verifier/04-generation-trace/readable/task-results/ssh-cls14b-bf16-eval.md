# ssh cls14b bf16 eval

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cls14b-bf16-eval_20260523T023042_result.json`
- **Structured JSON:** [`3de37469df610b3252a5.json`](../../sessions/3d/3de37469df610b3252a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 都完成了。汇总：

## 量化消融结果

| Model | bf16 | NF4 | Delta |
|-------|------|-----|-------|
| **CLS 14B** | **89.21%** | 89.47% | -0.26pp |
| **CWM 14B** | 89.26% | **89.31%** | -0.05pp |

### 关键结论

1. **CLS 14B bf16 = 89.21%** vs NF4 89.47%：量化 *略微提高* 了 0.26pp（噪声范围内）
2. **CWM 14B NF4 = 89.31%** vs bf16 89.26%：量化 *略微提高* 了 0.05pp（噪声范围内）
3. **量化对 accuracy 的影响 < 0.3pp**，在统计噪声范围内，**不影响任何结论**
4. 在 bf16 精度一致的条件下：CLS 89.21% vs CWM 89.26%，gap 仅 0.05pp → **CLS 和 CWM 14B 表现几乎完全一致**，之前的 0.21pp gap 主要由量化 confound 造成

### 文件位置
- CLS bf16: `/root/autodl-tmp/eval_results/cls14b_func_s42_v2_bf16/eval_results.json`
- CWM NF4: `/root/autodl-tmp/eval_results/cwm14b_func_s42_nf4/eval_cwm_results.json`

---
