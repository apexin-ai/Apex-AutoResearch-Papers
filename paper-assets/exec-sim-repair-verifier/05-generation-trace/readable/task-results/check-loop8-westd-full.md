# check loop8 westd full

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_loop8-westd-full_20260514T052402_result.json`
- **Structured JSON:** [`cb1b9afa6c4e66cef0fc.json`](../../sessions/cb/cb1b9afa6c4e66cef0fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== 服务器: westd-48478 ===
GPU 0: [运行中] CWM seed123 eval - 12997/32607 MiB, 88% util
GPU 1: [运行中] CWM v12 eval    - 12997/32607 MiB, 100% util
GPU 2: [空闲] 0 MiB
GPU 3: [空闲] 0 MiB

=== CWM eval（进行中）===
CWM seed123: 2448/9784 (25.0%), running_acc=57.2%
CWM v12:     2472/9784 (25.3%), running_acc=58.5%

速度 ~8 samples/52s ≈ 每样本 6.5s，剩余 ~13.2h 完成

=== CLS eval 结果汇总 ===

| 模型 | Checkpoint | Accuracy | F1_macro | F1_fail | F1_pass | Gap vs Majority |
|------|-----------|----------|----------|---------|---------|-----------------|
| CLS 8B  | ckpt-200 | 70.22% | 68.21% | 60.23% | 76.19% | -2.74pp |
| CLS 8B  | **ckpt-400** | **84.52%** | **80.89%** | **72.57%** | **89.21%** | **+11.56pp** |
| CLS 8B  | ckpt-600 | 78.51% | 74.56% | 64.53% | 84.58% | +5.55pp |
| CLS 4B (v5) | ckpt-200 | 52.96% | 52.89% | 51.02% | 54.76% | -19.99pp |
| CLS 4B (v5) | ckpt-400 | 78.43% | 68.41% | 50.61% | 86.21% | +5.48pp |
| CLS 4B (v5) | ckpt-600 | 76.37% | 71.17% | 58.93% | 83.41% | +3.41pp |

| CWM 4B (v10) | ckpt-400 | 69.91% | 46.71% | 11.54% | 81.87% | -3.05pp |

=== 关键发现 ===
- **CLS 8B ckpt-400 是目前最佳**：accuracy 84.52%, f1_macro 80.89%, 超 majority baseline 11.56pp
- CLS 8B 过拟合明显：ckpt-600 比 ckpt-400 下降 6pp accuracy
- CLS 4B (v5) 最佳在 ckpt-400 (accuracy 78.43%) 但 f1_macro 只有 68.41%（fail recall 低至 40.85%）
- CWM v10 有严重 parse 问题（9102/9784 unparseable），f1_fail 仅 11.54%
- CWM seed123/v12 正在评估中（max_new_tokens=1024 vs v10 的 64），预计明日凌晨完成

---
