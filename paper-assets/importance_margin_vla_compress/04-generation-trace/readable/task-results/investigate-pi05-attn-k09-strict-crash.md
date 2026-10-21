# investigate pi05 attn k09 strict crash

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_pi05_attn_k09_strict_crash_20260527T063806_result.json`
- **Structured JSON:** [`0f37ff3de5dc7ca151dc.json`](../../sessions/0f/0f37ff3de5dc7ca151dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验**没有崩溃，已正常完成**。

日志显示全部 10 个 tasks (T0-T9) 均跑完 50 episodes，最终结果：

```
RESULT: libero_10 prune=attention keep=0.9 SR=64.0%
Saved: /root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_attention_k0.90_libero_10_seed42.json
```

各 task 成绩：
| Task | SR |
|------|-----|
| T0 | 36% |
| T1 | 92% |
| T2 | 44% |
| T3 | 96% |
| T4 | 52% |
| T5 | 88% |
| T6 | 56% |
| T7 | 60% |
| T8 | 20% |
| T9 | 96% |
| **Total** | **64.0%** |

运行时间 170.7 分钟，于 14:35 正常退出。Cron 检测到"进程消失"是因为实验已完成，不是崩溃。GPU2 当前空闲可用。

同服务器的 attn k=0.85 strict 实验仍在运行中（T9 ep=20 at 14:38），也接近完成。

---
