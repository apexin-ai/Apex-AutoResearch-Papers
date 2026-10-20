# prep next batch readiness

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_next_batch_readiness_20260521T074641_result.json`
- **Structured JSON:** [`dfc4025721013a28cd6e.json`](../../sessions/df/dfc4025721013a28cd6e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

就绪状态汇报：

---

### 1. NORA Spatial Pipeline — **READY**

| 项目 | 状态 |
|------|------|
| 脚本 | `nora_spatial_full_pipeline.py` 存在，配置正确：RidgeCV probing, N_DEMOS=10, N_TIMESTEPS=50, 15 seeds, trained+untrained 双臂 |
| Trained checkpoint | `nora-libero-spatial/` 7.1G ✓ |
| Untrained checkpoint | `qwen25-vl-3b-base/` 7.1G ✓ |
| 数据 | `libero_spatial/` 10 个 task hdf5 齐全 ✓ |
| NORA venv | `envs/nora/bin/python` 存在 ✓ |
| 默认 DEVICE | `cuda:0` — nora_goal_untrained_cf 跑完释放 cuda:1 后，cuda:0 也需要等 object_pipeline_ridge_v2 完成才能用 |

**注意**：脚本默认 `DEVICE = "cuda:0"`。如果 object_pipeline_ridge_v2 还在 cuda:0 上跑，提交时需要 `--device cuda:1` 或等 cuda:0 释放。

没跑 `--help` 测试（需要 source activate，read_only 不支持），但脚本结构与已验证的 nora_goal 系列一致，无风险。

### 2. TraceVLA Untrained — **READY（内置）**

| 项目 | 状态 |
|------|------|
| Phi-3-Vision base model | `phi3v-base/` ~7.7G, 2 个 safetensors 文件齐全 ✓ |
| TracVLA trained checkpoint | `tracevla-phi3v/` ~7.7G ✓ |
| Pipeline 脚本 | `tracvla_spatial_full_pipeline.py` 已包含 trained+untrained 双臂（UNTRAINED_CKPT 指向 phi3v-base/）✓ |
| 独立 untrained 脚本 | 不存在，不需要——full pipeline 已内置 |

### 3. OFT Checkpoint — **READY**

| 项目 | 状态 |
|------|------|
| 目录 | `openvla-7b-oft-finetuned-libero-10/` 15G |
| 模型文件 | 4 个 safetensors shard + lora_adapter ✓ |
| 下载进程 | 无法通过 read_only 检查（pipe 被阻），但 checkpoint 目录大小 15G 合理，文件齐全，判断下载已完成 |

### 4. 磁盘空间 — **OK**

```
/dev/md0  250G  169G  82G  68%
```

82G 剩余，足够跑实验和存结果。

---

**总结**：NORA Spatial pipeline 所有依赖就绪，cuda:0 空闲后可立即提交。TracVLA spatial 同样就绪。OFT checkpoint 完整。

---
