# deploy openvla random k07 seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_openvla-random-k07-seed42_20260521T221510_result.json`
- **Structured JSON:** [`3cce582cf112cf02219c.json`](../../sessions/3c/3cce582cf112cf02219c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验 `eval_openvla_random_k07_object_seed42_v2` **已经存在且已完成**（status=DONE, conclusion=success）。

结果：
- **Overall SR: 44.4%** (222/500)
- 服务器: westd-38929，完成时间: 2026-05-21T11:59
- Per-task: alphabet_soup 72%, cream_cheese 20%, salad_dressing 56%, bbq_sauce 38%, ketchup 64%, tomato_sauce 52%, butter 20%, milk 24%, chocolate_pudding 34%, orange_juice 64%

**汇总**:
1. GPU0 PID 360412 已 kill，GPU0 已释放（0 MiB）
2. `eval_openvla_random_k09_object_seed42` → DONE/killed
3. D125 env.seed bug **已修复** — 第 219 行 `env.seed(args.seed)` 正确使用命令行参数，不再硬编码
4. `eval_openvla_random_k07_object_seed42_v2` 已有完成结果（44.4%），无需重新部署

对比: L2norm k=0.7 (49.8%) vs random k=0.7 (44.4%)，L2norm 在 k=0.7 下有 +5.4pp 优势。是否还需要在 GPU0 上部署其他实验？

---
