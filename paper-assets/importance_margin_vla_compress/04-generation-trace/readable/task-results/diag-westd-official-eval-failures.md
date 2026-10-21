# diag westd official eval failures

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_westd_official_eval_failures_20260518T162727_result.json`
- **Structured JSON:** [`faa4b912efb39c0c7ef3.json`](../../sessions/fa/faa4b912efb39c0c7ef3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 结论：两个实验**没有崩溃**，cron 误判

两个进程都还活着，正常运行中：

| 实验 | PID | GPU | 进度 | 当前状态 |
|------|-----|-----|------|----------|
| k09 (k_ratio=0.9) | 247752 | cuda:0 | 6/10 tasks 完成，Task 6 进行中 | 运行中 |
| k095 (k_ratio=0.95) | 247606 | cuda:1 | 6/10 tasks 完成，Task 6 进行中 | 运行中 |

### 已完成的结果

**两个实验到目前为止全部 0% 成功率**（Task 0-5 各 0/50 episodes），每个 episode 都跑满 280 steps 后失败。

这和已完成的 **k05 (k_ratio=0.5)** 一致：也是 10/10 tasks 全 0%。

对比 baseline（无 pruning）：overall_success_rate = **59.2%**。

### 关键发现

`true_removal` random pruning 在 k=0.5/0.9/0.95 三个比例下都是 **0%**，完全摧毁了模型能力。这说明：
1. 随机 pruning + true_removal 对官方 SmolVLA 极其破坏性，即使只移除 5% 的 token (k=0.95) 也彻底失效
2. 两个实验预计还需 ~20 分钟跑完剩余 4 个 tasks，但结果几乎肯定仍是 0%
3. 无需重启，让它们跑完即可

### 不需要操作
进程正常，等待自然结束。最终 JSON 结果文件会自动生成。

---
