# diagnose cqa1 checkpoint v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cqa1-checkpoint-v2_20260521T230750_result.json`
- **Structured JSON:** [`2db0f5d771b7684ce9d5.json`](../../sessions/2d/2db0f5d771b7684ce9d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**根因确认。** cqa1 上之前的 baseline（无 pruning）也是 0% SR。结论文件明确记录：

> transformers_version: 4.53.2
> "Checkpoint produces 0% success rate on LIBERO-Object"

## 汇报

### 1. 主机名确认
`autodl-container-61bb4e82b9-0e2cbbac` — 确认连接到 cqa1-33015 ✓

### 2. Checkpoint MD5 对比
**完全一致 ✓**
| 文件 | cqa1 | westd-38929 |
|------|------|-------------|
| model.safetensors | `247eb4ca669c...` | `247eb4ca669c...` |
| postprocessor | `363ee2f7e8bb...` | `363ee2f7e8bb...` |
| preprocessor | `363ee2f7e8bb...` | `363ee2f7e8bb...` |

### 3. 各实验当前进度
| 实验 | PID | 运行时长 | SR |
|------|-----|---------|-----|
| random k=0.85 seed43 | 719440 | ~1h | **0%** (Task 0-3 全 0) |
| L2norm k=0.3 seed43 | 725484 | ~1h | **0%** (Task 0-2 全 0) |
| L2norm k=0.85 seed42 | 716056 | ~1h12m | **0%** (Task 0-3 全 0) |
| random k=0.3 seed43 | 716134 | ~1h12m | **0%** (Task 0-2 全 0) |

### 4. 结论：Checkpoint 正常，环境有问题

**Checkpoint 完全一致，不是 checkpoint 损坏。** 0% SR 的根因是 **cqa1 的 Python 环境与 westd-38929 不同：**

| 包 | cqa1-33015 (0% SR) | westd-38929 (正常) |
|---|---|---|
| transformers | **4.53.2** | **5.5.3** |
| lerobot | 0.5.1 (pip) | 0.5.2 (editable from source) |
| libero | 0.1.1 | 0.1.0 (editable from source) |

cqa1 上此前的 baseline（无 pruning）也是 0% SR（`eval_pi05_baseline.json` 记录了这一点），说明 `transformers 4.53.2 + lerobot 0.5.1` 组合下 PI05Policy 推理根本无法工作。

**建议：** 这 4 个实验全部在浪费 GPU。应尽快 kill 进程，升级 cqa1 环境（transformers 升级到 5.5.3、lerobot 安装 0.5.2 editable），然后重跑。

---
