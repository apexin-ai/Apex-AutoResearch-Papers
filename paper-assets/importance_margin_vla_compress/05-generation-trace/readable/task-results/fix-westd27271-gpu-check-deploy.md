# fix westd27271 gpu check deploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_westd27271_gpu_check_deploy_20260527T061429_result.json`
- **Structured JSON:** [`e753ea7e9f18919207ce.json`](../../sessions/e7/e753ea7e9f18919207ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两张 GPU 均已确认在跑：

| GPU | 显存 | 利用率 | 实验 |
|-----|------|--------|------|
| GPU0 | 15964 MiB | 66% | OV Attn k=0.95 Goal v3 (Task 1/10 进行中) |
| GPU1 | 15980 MiB | 76% | OV L2norm k=0.85 Object (刚启动，模型已加载) |

完成的结果：**OV Attn k=0.95 Object = 71.2%** (已注册)。

新部署：**OV L2norm k=0.85 Object** — 填补 Object L2norm 曲线关键缺口 (k=0.9=70.6% → k=0.85=? → k=0.75=57.4%)，验证前次可疑值 55.2%。预计 ~4.5h 完成。

---
