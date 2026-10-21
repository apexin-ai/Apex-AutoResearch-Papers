# deploy xvla random k095 object redeploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_xvla_random_k095_object_redeploy_20260522T230645_result.json`
- **Structured JSON:** [`c5bba17bea4cb3311f94.json`](../../sessions/c5/c5bba17bea4cb3311f94.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署成功，进程运行正常。

## 报告

### 1. 崩溃原因
transformers 5.5.4 的 `get_expanded_tied_weights_keys()` 要求 `_tied_weights_keys` 为 dict 格式，但 X-VLA 使用的 Florence2 模型代码（旧版）定义为 list。调用 `.keys()` 时触发 `AttributeError: 'list' object has no attribute 'keys'`。

**修复**：将 `/root/autodl-tmp/X-VLA-Libero/modeling_florence2.py` 中三处 `_tied_weights_keys = [...]` 改为 `_tied_weights_keys = None`（line 1934, 2057, 2532）。

### 2. 重部署信息
- 服务器：**westd-27271**
- tmux session：`eval_xvla_random_k095_object_v2`
- GPU：cuda:0（PID 950819，占用 4853 MiB）
- 日志：`~/runs/importance_margin_vla_compress/eval_xvla_random_k095_object_seed42_v2.log`

### 3. 验证结果
- tmux session 存在 ✓
- GPU 进程存在（PID 950819） ✓
- 模型加载成功（879.5M params），vision pruning 安装完成（keep 47/50 tokens = 95%） ✓
- Task 0 已开始执行，前 7 个 episode 全部 SUCCESS ✓

---
