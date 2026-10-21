# audit westd27271 full

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_westd27271_full_20260522T200543_result.json`
- **Structured JSON:** [`c7371a5028944c2e9a78.json`](../../sessions/c7/c7371a5028944c2e9a78.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 审计结果

### 两卡状态

| GPU | VRAM Used | Session | 当前任务 | 状态 |
|-----|-----------|---------|---------|------|
| cuda:0 | 4840 MiB | `xvla_random_goal` | k=0.9, Task 2/10 进行中 | **运行中** |
| cuda:1 | 4938 MiB | `xvla_random_spatial` | k=0.9, Task 2/10 进行中 | **运行中** |

### X-VLA Random Chain 进度

| k值 | Goal | Spatial |
|-----|------|---------|
| 0.95 | **54.0%** (270/500) | **70.2%** (351/500) |
| 0.9 | 运行中 (T0: 100%, T1: 88%, T2+待跑) | 运行中 (T0: 100%, T1: 64%, T2 刚开始) |
| 0.7 | 排队中 | 排队中 |

### k=0.95 已完成的逐 Task 结果

**Goal k=0.95 — 54.0%**
| Task | SR | Description |
|------|-----|-------------|
| T0 | 100% | open the middle drawer of the cabinet |
| T1 | 38% | put the bowl on the stove |
| T2 | 92% | put the wine bottle on top of the cabinet |
| T3 | 24% | open the top drawer and put the bowl inside |
| T4 | 14% | put the bowl on top of the cabinet |
| T5 | 0% | push the plate to the front of the stove |
| T6 | 72% | put the cream cheese in the bowl |
| T7 | 100% | turn on the stove |
| T8 | 4% | put the bowl on the plate |
| T9 | 96% | put the wine bottle on the rack |

**Spatial k=0.95 — 70.2%**
| Task | SR | Description |
|------|-----|-------------|
| T0 | 100% | bowl between plate and ramekin → plate |
| T1 | 44% | bowl next to ramekin → plate |
| T2 | 100% | bowl from table center → plate |
| T3 | 98% | bowl on cookie box → plate |
| T4 | 70% | bowl in top drawer → plate |
| T5 | 6% | bowl on ramekin → plate |
| T6 | 100% | bowl next to cookie box → plate |
| T7 | 18% | bowl on stove → plate |
| T8 | 90% | bowl next to plate → plate |
| T9 | 76% | bowl on wooden cabinet → plate |

### 部署

**两卡均满载，无空闲卡。** k=0.9 每条 chain 约还需 ~55 分钟完成剩余 8 个 task，之后自动启动 k=0.7。预计全部 chain 完成还需 ~2.5 小时。

---
