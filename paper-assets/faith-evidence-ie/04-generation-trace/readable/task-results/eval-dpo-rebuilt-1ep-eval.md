# eval dpo rebuilt 1ep eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_dpo_rebuilt_1ep_eval_20260523T034757_result.json`
- **Structured JSON:** [`5e2c0e681106a49425e7.json`](../../sessions/5e/5e2c0e681106a49425e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 占用情况汇总：

| GPU | 显存 | 进程 | 运行时间 |
|-----|------|------|---------|
| 0 | 26.8GB | 8B RSFT no-evi test eval (batch=16) | 55 min |
| 1 | 32.5GB | 14B RSFT generation (8 gens) | 9.5h |
| 2 | 11.5GB | **DPO rebuilt 1ep dev eval** (batch=4, 9%) | 20 min |
| 3 | 6.1GB | 1.7B RSFT test eval | 2h40m |

**所有 4 卡都被占用，C001 约束阻止提交。**

额外问题：cuda:2 的 dev eval 输出目录 `/root/autodl-tmp/eval_results/dpo_rebuilt_1ep_eval` 与 test eval 目标目录冲突。

选项：
1. 等 cuda:2 dev eval 结束（预计还需 ~3h），然后提交 test eval（需换 output_dir）
2. 等 GPU 0 或 3 的 eval 先结束，改用那张卡
3. Kill cuda:2 的 dev eval，立即提交 test eval（你说了 test eval 最高优先级）

需要你决定。

---
