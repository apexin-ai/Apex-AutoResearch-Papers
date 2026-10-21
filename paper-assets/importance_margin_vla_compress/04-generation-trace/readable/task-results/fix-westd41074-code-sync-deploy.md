# fix westd41074 code sync deploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_westd41074_code_sync_deploy_20260527T074153_result.json`
- **Structured JSON:** [`76ffce72d7b33bfedd68.json`](../../sessions/76/76ffce72d7b33bfedd68.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**全部 4 GPU 已被占用，无法部署新实验。**

## 执行结果

### Step 1-2: 代码同步 ✅
- westd-41074 文件已从 426 行更新至 **464 行**
- SHA256 一致：`c630bd80951efbf2a71c6094529b6b7f9d6bf6fe4b837f3ff303ba20b762f320`
- 旧版备份：`eval_pi05_pruning_libero.py.bak426`

### Step 3: 可用模型
- `/root/autodl-tmp/openvla-libero-goal` ✅
- `/root/autodl-tmp/pi05_libero_finetuned` ✅
- 还有 `openvla-7b-finetuned-libero-10`, `openvla-libero-object` 等

### Step 4: GPU2/3 部署 ❌ — 全部 GPU 已占用

| GPU | PID | 实验 | 运行时间 |
|-----|-----|------|---------|
| 0 | 32184 | eval_openvla_random_k095_long_seed42 | 自 08:29 |
| 1 | 177597 | eval_pi05_random_k075_long_seed42_strict | 自 13:36 |
| 2 | 262137 | pi0.5 random k=0.95 Long strict (libero_10) | 36 min |
| 3 | 262473 | pi0.5 l2norm k=0.95 Long strict (libero_10) | 36 min |

GPU 2/3 在 ~36 分钟前已被部署了新的 pi0.5 strict 实验。需要等现有实验完成或手动决定是否终止某个实验后才能部署 OpenVLA Goal 备份任务。

---
