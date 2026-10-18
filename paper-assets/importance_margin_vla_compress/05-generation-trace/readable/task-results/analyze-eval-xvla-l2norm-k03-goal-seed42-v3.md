# analyze eval xvla l2norm k03 goal seed42 v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_xvla_l2norm_k03_goal_seed42_v3_20260524T040047_result.json`
- **Structured JSON:** [`158eef44e3e6f96f4731.json`](../../sessions/15/158eef44e3e6f96f4731.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估**已完成**，全部 500 episodes 跑完，进程正常退出 (EXIT_CODE=0)。Registry 标记 failed 是误判。

## 结果

**Overall SR: 188/500 (37.6%)**，95% Wilson CI: [33.5%, 41.9%]

| Task | SR | Description |
|------|-----|-------------|
| 0 | 42% (21/50) | open the middle drawer of the cabinet |
| 1 | **94%** (47/50) | put the bowl on the stove |
| 2 | 16% (8/50) | put the wine bottle on top of the cabinet |
| 3 | 24% (12/50) | open the top drawer and put the bowl inside |
| 4 | **98%** (49/50) | put the bowl on top of the cabinet |
| 5 | 0% (0/50) | push the plate to the front of the stove |
| 6 | 2% (1/50) | put the cream cheese in the bowl |
| 7 | 20% (10/50) | turn on the stove |
| 8 | **80%** (40/50) | put the bowl on the plate |
| 9 | 0% (0/50) | put the wine bottle on the rack |

## 对比分析

| 配置 | Goal SR |
|------|---------|
| X-VLA baseline | ~74% |
| X-VLA L2norm k=0.5 | 68.6% |
| **X-VLA Random k=0.3** | **50.6%** |
| **X-VLA L2norm k=0.3** | **37.6%** ← 本次 |
| X-VLA L2norm k=0.3 Object | 18.2% |

## 结论：**negative**

- 评估成功完成，不是 failed，但结果很差
- **L2norm k=0.3 (37.6%) 显著低于 Random k=0.3 (50.6%)**——L2norm 在同等压缩率下比随机裁剪还差 13 个百分点，说明 L2norm 作为 importance metric 在高压缩率下不仅无效，还起到了反向选择的效果
- 相比 baseline (74%) 下降约 49%（相对），相比 L2norm k=0.5 (68.6%) 下降 31 个百分点
- 任务方差极大：简单放置任务 (Task 1/4/8) 仍保持 80-98%，但精细操作任务 (Task 5/6/9) 完全崩溃至 0-2%
- L2norm 在 Object suite 也只有 18.2%，进一步确认该 metric 在高压缩率下系统性失败

Registry 应从 `conclusion=failed` 更正为 `conclusion=negative`。

---
