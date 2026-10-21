# diagnose eval pi05 random k09 spatial seed43 postfix

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_random_k09_spatial_seed43_postfix_20260524T211525_result.json`
- **Structured JSON:** [`c6a74caaf400dfeae4d4.json`](../../sessions/c6/c6a74caaf400dfeae4d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 诊断结果

### 失败根因：网络不可达（Network is unreachable）

实验在模型加载后、创建 preprocessor 时崩溃。具体原因：

`lerobot` 的 `PolicyProcessorPipeline` 在初始化 tokenizer 步骤时尝试联网调用 `huggingface_hub.model_info("google/paligemma-3b-pt-224")`，服务器此时无外网访问，导致 `httpx.ConnectError: [Errno 101] Network is unreachable`。

调用链：
```
make_pre_post_processors() 
→ PolicyProcessorPipeline.from_pretrained() 
→ AutoTokenizer.from_pretrained("google/paligemma-3b-pt-224") 
→ GemmaTokenizer.__init__() 
→ _patch_mistral_regex() 
→ is_base_mistral() 
→ model_info()  ← 这里联网失败
```

### 为什么同服务器 goal_seed43_postfix 成功了？

`goal_seed43_postfix` 日志显示它正在正常跑（当前仍在运行中，已跑到 Task 3）。说明它启动时网络是通的（tokenizer 下载/验证通过了），而 `spatial_seed43_postfix` 启动时（04:54）刚好遇到了短暂网络中断。

`object_seed43_postfix` 同样失败于相同错误——确认是同一时段的网络问题影响了多个实验。

### GPU 状态

GPU 3（实验分配的物理 GPU）当前空闲（1MiB / 97887MiB），可以重跑。

### 修复方案

**可以直接重跑相同命令**，前提是确保网络通畅。但更稳妥的做法是设置 `HF_HUB_OFFLINE=1` 或 `TRANSFORMERS_OFFLINE=1`（如果 tokenizer 文件已缓存在本地）：

```bash
# 方案 1：直接重跑（网络恢复后）
CUDA_VISIBLE_DEVICES=3 python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.9 --suite libero_spatial --n_episodes 50 --seed 43 --gpu 0

# 方案 2：离线模式（推荐，避免再次被网络抖动影响）
HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 CUDA_VISIBLE_DEVICES=3 python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.9 --suite libero_spatial --n_episodes 50 --seed 43 --gpu 0
```

注意 `object_seed43_postfix` 也失败于同一原因，同样需要重跑。

---
