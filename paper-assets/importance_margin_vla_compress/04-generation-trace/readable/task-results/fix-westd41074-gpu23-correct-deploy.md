# fix westd41074 gpu23 correct deploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_westd41074_gpu23_correct_deploy_20260526T003618_result.json`
- **Structured JSON:** [`a3cab86d9ccc9ec4ae0a.json`](../../sessions/a3/a3cab86d9ccc9ec4ae0a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

rsync 正在以 ~300MB/s 传输，15GB 预计约 50 秒完成。

---

## 汇报

### 1. 初始 GPU 状态

| GPU | PID | 实验 | 显存 | GPU利用率 |
|-----|-----|------|------|----------|
| 0 | 76334 | random_prune k=0.5 object | 15961MiB | 69% |
| 1 | 76492 | l2norm_prune k=0.5 object | 15961MiB | 80% |
| 2 | 259181 | attention_prune k=0.7 object | 15961MiB | 69% |
| 3 | 259256 | random_prune k=0.7 object | 15961MiB | 76% |

**全部是 Object suite 实验，无 Long 实验。**

### 2. Kill 操作
无。GPU2/3 已被之前的操作替换为正确的 Object 实验。

### 3. 可用模型
- `openvla-libero-object/` — ✅ 完整
- `openvla-libero-goal/` — ❌ 不完整（缺 model-00001、model-00002，HF 下载超时中）
- `pi05_libero_finetuned/` — ✅ 存在
- `openvla-7b-finetuned-libero-10` — ❌ 不存在（rsync 传输中）

### 4. 已部署实验
GPU2/3 已在运行 Step 4 要求的实验，无需重新部署：
- GPU2: `eval_openvla_attn_k07_object_seed42` (PID 259181) — registry RUNNING
- GPU3: `eval_openvla_random_k07_object_seed42_v3` (PID 259256) — registry RUNNING

### 5. nvidia-smi 验证
4 GPU 均满载运行（~16GB 显存，69-80% GPU 利用率）。

### 6. rsync 状态
**已启动** (PID 270144)，westd-38929 → westd-41074 直连成功，传输速度 ~300MB/s，预计 ~50 秒完成。

### 7. 磁盘
`/root/autodl-tmp/`: 250GB 总量，72GB 已用，**179GB 可用**。

### 附注
Goal 模型下载（PID 228885）持续超时，原因是未使用 `source /etc/network_turbo` 启用代理。如需修复需 kill 当前下载进程并用正确的网络配置重启。

---
