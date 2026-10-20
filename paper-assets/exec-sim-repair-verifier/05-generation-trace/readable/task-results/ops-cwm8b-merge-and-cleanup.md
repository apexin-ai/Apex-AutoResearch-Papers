# ops cwm8b merge and cleanup

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cwm8b-merge-and-cleanup_20260516T055055_result.json`
- **Structured JSON:** [`0b4ef71d221248abdd05.json`](../../sessions/0b/0b4ef71d221248abdd05.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 张 GPU 已释放（0 MiB used）。Mutation breakdown 已在 merge 输出中，无需重新跑 GPU 任务。

---

## CWM 8B ckpt-400 TEST EVAL 最终结果

| 指标 | 值 |
|------|-----|
| **样本覆盖** | 9784/9784 (COMPLETE) |
| **Class balance** | pass=7138 (73.0%), fail=2646 (27.0%) |
| **Majority baseline** | 72.96% |
| **Overall accuracy** | **65.17%** (unparseable→pass) |
| **Gap vs majority** | **-7.79pp** |
| **Unparseable rate** | **73.81%** (7222/9784) |
| **Parseable-only accuracy** | 38.52% |

### Per-mutation breakdown

| Mutation | Count | Accuracy | ParseRate | ParseAcc |
|----------|------:|--------:|---------:|--------:|
| gold | 4633 | 80.06% | 23.89% | 16.53% |
| operator_swap | 3357 | 54.57% | 21.18% | 58.79% |
| boundary_removal | 1049 | 42.23% | 51.76% | 51.75% |
| return_value | 562 | 49.11% | 26.87% | 56.95% |
| off_by_one | 183 | 63.39% | 27.32% | 38.00% |

### 执行汇总
- Merge 完成，输出写入 `/root/autodl-tmp/eval_results/cwm_8b_ckpt400_test_merged/`
- PID 443221 (v3) 和 453335 (shard3) 已 kill，4 张 GPU 全部空闲
- Registry `cwm8b-ckpt400-test-eval` → DONE/success，metrics 已写入
- Cron `cwm8b-ckpt400-test-eval-v3` 已删除

**关键发现**: CWM 8B 的 73.81% unparseable rate 是致命问题——模型大量输出无法解析，默认 fallback 到 pass 后 overall accuracy (65.17%) 反而低于 majority baseline (72.96%)。Parseable-only accuracy 仅 38.52%，远低于 CLS 8B 的 84.48%。

---
