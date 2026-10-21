# submit detect remove cuda3 and eval grid b05

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_detect_remove_cuda3_and_eval_grid_b05_20260516T013525_result.json`
- **Structured JSON:** [`a8cfafe84b941c94ea0f.json`](../../sessions/a8/a8cfafe84b941c94ea0f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

detect_remove 速度正在快速恢复：3.22 → 2.20s/it，即将稳定到 ~2.1s/it。

---

## 总结

| 项目 | 结果 |
|------|------|
| **cuda:3 验证** | 清空 → detect_remove 正常启动（PID 276739, 46514 MiB） |
| **cuda:1 grid_b0_3 恢复** | 杀掉残留 detect_remove (PID 275277) 后，速度从 4.51s/it → **2.11s/it** |
| **detect_remove 启动** | PID 276739, step 101/6103, 速度 ~2.2s/it（已恢复） |
| **contamination_60_grid_b0_5 eval** | **Loss=2.8738, PPL=17.70**, 4,077,068 tokens, 283s |
| **Registry** | metrics 已更新（eval_ppl_holdout=17.7, eval_loss_holdout=2.8738） |

**全 4 卡 GPU 状态**：
| GPU | PID | 显存 | 利用率 | 实验 |
|-----|-----|------|--------|------|
| 0 | 257982 | 46.5/98 GB | 80% | (其他实验) |
| 1 | 274309 | 46.5/98 GB | 99% | grid_b0_3_seed42 (2.11s/it) |
| 2 | 265017 | 46.5/98 GB | 95% | (其他实验) |
| 3 | 276739 | 46.5/98 GB | 54%→恢复中 | detect_remove_baseline_seed42 (2.2s/it) |

额外处理：杀掉了 4 个重复 eval 进程（疑似其他 agent 提交），避免资源浪费。

---
