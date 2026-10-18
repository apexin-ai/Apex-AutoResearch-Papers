# diagnose eval pi05 random k05 object seed42 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_random_k05_object_seed42_v2_20260524T002036_result.json`
- **Structured JSON:** [`093fa2a2d2ad012cff7f.json`](../../sessions/09/093fa2a2d2ad012cff7f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

**实验并未失败，已成功完成。**

日志显示 `eval_pi05_random_k05_object_seed42_v2` 于 2026-05-24 05:59 启动，08:08 正常结束，耗时 127 分钟。10 个 task 全部跑完（每个 50 episodes），最终结果：

```
libero_object prune=random keep=0.5 SR=68.2%
```

各 task 成功率：
| Task | 内容 | SR |
|------|------|----|
| T0 | alphabet soup | 96% |
| T1 | cream cheese | 74% |
| T2 | salad dressing | 60% |
| T3 | bbq sauce | 70% |
| T4 | ketchup | 70% |
| T5 | tomato sauce | 48% |
| T6 | butter | 84% |
| T7 | milk | 56% |
| T8 | chocolate pudding | 66% |
| T9 | orange juice | 58% |

结果已保存至 `/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_random_k0.50_libero_object_seed42.json`。

**GPU 3 当前状态**：空闲（1MiB 显存，0% 利用率，P8 省电模式），无进程占用。GPU 0-2 各有一个 python 进程在跑（各占 ~10GB）。

**磁盘空间**：根分区 29%（22GB 可用），数据盘 55%（115GB 可用），均正常。

**结论**：实验已正常完成，不存在失败。如果之前观察到"进程异常退出"，可能是之前的 v1 尝试失败后重跑的 v2 已经成功了。

---
