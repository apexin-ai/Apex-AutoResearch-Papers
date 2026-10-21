# ops post restart status check

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_post_restart_status_check_20260522T020901_result.json`
- **Structured JSON:** [`63001db33c9d2970184f.json`](../../sessions/63/63001db33c9d2970184f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### westd-45947

| 实验 | 状态 | 进度 | 备注 |
|------|------|------|------|
| **Baseline eval** (PID 300495) | ✅ 存活 | 刚启动 ~6min，正在加载 task 0 (safelibero_object level II) | GPU 1 占用 8271 MiB |
| **A3 spatial_bowl** (PID 191747) | ✅ 存活 | **13,756 / 30K (45.9%)** | 运行 ~9h，GPU 0 占用 23926 MiB，loss ~0.03，~4s/it |

### westd-35807

| 实验 | PID | 进度 | 运行时间 |
|------|-----|------|----------|
| **baseline_lora_spa_s0** | 281554 | **21,340 / 30K (71.1%)** | ~24h |
| **baseline_lora_obj_s0** | 281629 | **21,297 / 30K (71.0%)** | ~24h |
| **a1_lora_obj_s0** | 292258 | **19,699 / 30K (65.7%)** | ~21h |
| **a1_lora_spa_s0** | 299910 | **17,807 / 30K (59.4%)** | ~19h |

4 张 GPU 全部 100% 利用率，每张 ~23.9 GiB 显存。

### 磁盘
`/root/autodl-tmp`: 260G / 350G (**75%**)

### 异常
无异常。所有 6 个进程正常运行，loss 曲线正常下降。baseline eval 刚启动正在初始化环境。

### ETA 估算（~4s/step）
- baseline_lora_*: 剩余 ~8.7K steps → **~9.7h**
- a1_lora_obj: 剩余 ~10.3K steps → **~11.5h**
- a1_lora_spa: 剩余 ~12.2K steps → **~13.6h**
- A3 spatial_bowl: 剩余 ~16.2K steps → **~18h**

---
