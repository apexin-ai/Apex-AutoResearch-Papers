# ops m96 check and deploy v1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_m96_check_and_deploy_v1_20260522T092004_result.json`
- **Structured JSON:** [`9bcabf7c5ad7112385de.json`](../../sessions/9b/9bcabf7c5ad7112385de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

l2norm_k05_object_seed43 已经在 westd-27271 上完成了（SR=39.2%, 500ep）。不需要重新跑。汇报结果：

```
M96 训练: 仍在跑 (step 94700/100000, 94.7%, ETA ~3h, ~20:20)
l2norm_k0925_object_s43: PID 304198 不存在，log 文件也不存在——从未在 westd-41074 上运行过
westd-41074 GPU 0: PID 304126 — random k0.85 object seed43 eval (运行 1h13m)
westd-41074 GPU 1: PID 68539 — M96 训练
westd-41074 GPU 2: PID 59671 — M64 训练

westd-27271 GPU 0: 空闲
westd-27271 GPU 1: 空闲
l2norm_k05_object_s43: 已完成 (SR=39.2%, 196/500, 在 westd-27271 上)
```

**l2norm_k05_object_seed43 已经跑完**，无需重复部署。westd-27271 两个 GPU 都空闲，等你指示部署什么。候选：
- l2norm_k0925_object_seed43（从未运行过）
- M96 checkpoint 在 westd-41074 上，还没训完，暂时没法跑 M96 eval

---
