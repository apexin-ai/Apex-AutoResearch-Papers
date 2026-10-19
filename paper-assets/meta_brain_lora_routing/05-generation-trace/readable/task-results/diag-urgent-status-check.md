# diag urgent status check

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_urgent_status_check_20260516T134551_result.json`
- **Structured JSON:** [`1374dc369e52c9291d38.json`](../../sessions/13/1374dc369e52c9291d38.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 1. 四路 v2 LoRA 训练（全部 target 10,000 steps）

| Expert | Step | Loss | GPU | 预计剩余 |
|--------|------|------|-----|----------|
| **visual** | 6400/10000 | 0.7566 | GPU 2 (12.7GB, 99%) | ~61 min |
| **physical** | 6350/10000 | 0.7422 | GPU 1 (12.7GB, 99%) | ~62 min |
| **spatial (restart)** | 1150/10000 | 0.8528 | GPU 0 (68GB, 99%) | **~3.1 hrs** |
| **universal** | 4850/10000 | 0.7720 | GPU 3 (12.8GB, 99%) | ~88 min |

### 2. Spatial 训练状态

- **原始 spatial** 崩溃：`No space left on device (os error 28)` — 根分区 27/30GB = 88%，保存 checkpoint 时磁盘满
- **restart 版本在跑**，output_dir 已改到 `/root/autodl-tmp/checkpoints/v2_lora_spatial_r16`（数据盘），step 1150，进度 11.5%，落后其他三路很多

### 3. openpi 原生 eval — 无法执行

`examples/libero/main.py` 是 **WebSocket 客户端**（`openpi_client.websocket_client_policy`），需要先启动 openpi model server（占一整张 GPU）。当前 4 GPU 全满跑训练，**无法启动 server**。openpi 也没有其他 standalone eval 入口（`find` 未找到 eval*.py）。

需要等至少一路训练完成释放 GPU 后才能跑。

### 4. debug_eval.py 结果

- **MetaBrain 加载成功**：actions shape (50, 7)，无 NaN，range [-1.02, 1.06]，mean=0.028
  - 各维度 stats 合理，dim6（gripper）std=0.96 符合预期
- **openpi policy 对比加载失败**：`policy_config.create_trained_policy()` 报错，traceback 被截断，末尾是大量 model weight key 列表 — 大概率是 checkpoint 格式/key 不匹配导致的 state_dict 加载错误

### 5. eval_openpi_norm_fixed.log（之前的 wrapper eval）

```
routing=none, libero_spatial: 0/5 = 0.0%（全部 FAIL）
```

5 个 episode 全部走满 220 步超时未完成。

### 关键问题

1. **根分区只剩 3.8GB**，visual/physical/universal 的 checkpoint 还在写根分区，后续保存可能再次磁盘满
2. **spatial restart 落后 ~5000 steps**，比其他三路晚约 2.5 小时完成
3. **openpi 原生 eval 无法在训练期间执行**，需要空闲 GPU

---
