# ops audit westd38929

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_audit_westd38929_20260522T025729_result.json`
- **Structured JSON:** [`dd5a3a005f785238f588.json`](../../sessions/dd/dd5a3a005f785238f588.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 审计报告

### 网络状态
**正常** — pypi.org 可达

### GPU 实际状态

| GPU | 利用率 | 显存 | 实验 | PID | 进度 |
|-----|--------|------|------|-----|------|
| 0 | 0% | 加载中 | **[新部署]** random k=0.925 Spatial seed42 | 369704 | 模型加载中 |
| 1 | 30% | 20.9/97.9 GB | l2norm k=0.95 Spatial seed42 (v1) | 260899 | T6/10, ~97% SR |
| 1 | — | — | l2norm k=0.95 Spatial seed42 (v2) | 293268 | T3/10, ~97% SR |
| 2 | 43% | 21.1/97.9 GB | random k=0.95 Spatial seed42 v3 | 293413 | T2/10, ~94% SR |
| 2 | — | — | l2norm k=0.7 Object seed43 v3 | 348884 | 刚启动 |
| 3 | 67% | 16.0/97.9 GB | OpenVLA l2norm k=0.5 Object seed42 v5 | 311261 | T1 ep20/50, ~60% SR |

**注意**: GPU 1 上有两个重复的 l2norm k=0.95 Spatial 实验。v1 (T6) 更快，v2 (T3) 冗余。

### 已收割的实验结果（12个完成，EXIT_CODE=0）

| 实验 | Suite | Prune | k | SR |
|------|-------|-------|---|-----|
| baseline_spatial_seed42 | Spatial | none | 1.0 | **97.2%** |
| l2norm_k09_spatial | Spatial | l2norm | 0.9 | **95.0%** |
| l2norm_k085_spatial | Spatial | l2norm | 0.85 | **90.4%** |
| l2norm_k07_spatial | Spatial | l2norm | 0.7 | 67.0% (旧结果) |
| l2norm_k05_spatial | Spatial | l2norm | 0.5 | 55.6% |
| l2norm_k03_spatial | Spatial | l2norm | 0.3 | 57.2% |
| l2norm_k0925_object | Object | l2norm | 0.925 | **99.2%** |
| random_k09_spatial | Spatial | random | 0.9 | 54.6% |
| random_k085_spatial | Spatial | random | 0.85 | 58.4% |
| random_k07_spatial | Spatial | random | 0.7 | 74.4% |
| random_k05_spatial | Spatial | random | 0.5 | 71.6% |
| random_k03_spatial | Spatial | random | 0.3 | 49.6% |
| random_k0925_object_seed43 | Object | random | 0.925 | 30.0% |

### Registry 更新
- **eval_pi05_l2norm_k085_spatial_seed42**: RUNNING → DONE (success, SR=90.4%)
- **eval_pi05_l2norm_k085_spatial_seed42_v2**: RUNNING → DONE (failed, 进程静默死亡)
- **5个活跃实验**: PREPARING → QUEUED → RUNNING
- **eval_pi05_random_k0925_spatial_seed42**: PREPARING → RUNNING (新部署 GPU 0)
- Director 标记的4个实验已经是 DONE 状态，无需更新

### 新部署
- **GPU 0**: random k=0.925 Spatial seed42 (PID 369704) — Spatial random cliff 边界点

### 待关注
- GPU 1 有重复实验 (l2norm k=0.95 spatial v1+v2)，建议 kill v2 (PID 293268) 释放资源
- Spatial 曲线在 k=0.95 完成后将全部齐全

---
