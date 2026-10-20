# diagnose post restart check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_post-restart-check_20260520T092329_result.json`
- **Structured JSON:** [`70baa1d6f38480f2416b.json`](../../sessions/70/70baa1d6f38480f2416b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-37389 迁移状态汇总

### 磁盘
- **总用量**: 41G / 350G (12%)
- rsync 进度: 14G → 26G → 41G，稳步增长

### 传输进程
| 进程 | 状态 |
|------|------|
| **rsync** (全量后台) | **运行中** — PID 5150/5152，从旧实例同步 |
| **SCP** (优先通道) | **运行中** — 正在传输 `meta-llama` 基础模型（17:01 开始，22 分钟仍在进行） |
| milestone_checker | 运行中 |
| rsync_monitor | 运行中 |

### 里程碑
- **Milestone A**: 未达成
- **Milestone B**: 未达成

### 关键文件完整性

| 资源 | 状态 |
|------|------|
| LLaMA-3.1-8B base shards | **3/4** (SCP 正在传输中) |
| LLaMA SFT adapter | **MISSING** (SCP 尚未到达此步) |
| Data (train_annotated.json) | **OK** |
| Code (freige) | **OK** |
| 14B SFT adapter | **MISSING** |
| 14B generations | **MISSING** |
| Qwen3-14B shards | **5/8** (rsync 部分完成) |

### GPU
| GPU | Util | VRAM |
|-----|------|------|
| 0 | 0% | 0 / 98GB |
| 1 | 0% | 0 / 98GB |
| 2 | 100% | 0 / 98GB |
| 3 | 100% | 0 / 98GB |

GPU 2/3 utilization 100% 但显存 0 — 可能是驱动初始化或后台任务，无实际负载。

### 结论
迁移进行中，SCP 优先通道正在传 meta-llama 基础模型（已完成 3/4 shards）。data 和 code 已就位。adapter 和 14B 相关文件尚未传输到位，需等 SCP 完成后续步骤。预计还需 30-60 分钟完成全部传输。

---
