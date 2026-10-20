# ssh disk check urgent

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_disk_check_urgent_20260522T074029_result.json`
- **Structured JSON:** [`7a944170e5695f70735e.json`](../../sessions/7a/7a944170e5695f70735e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息到齐，汇总如下：

---

## 磁盘状况总览

| 分区 | 大小 | 已用 | 可用 | 用途 |
|------|------|------|------|------|
| **overlay (/)** | 30G | 25G (83%) | **5.2G** | 系统 + 代码 |
| **/dev/md0 → /root/autodl-tmp/** | 250G | 178G (72%) | **73G** | 数据盘（模型/checkpoints） |

**根分区偏紧（5.2G），数据盘尚可（73G）。** Checkpoints 全部在数据盘，不影响根分区。

## Checkpoint 存储结构

项目目录通过 **symlink** 指向数据盘：
- `checkpoints` → `autodl-tmp/.../checkpoints_410m/` (17G)
- `checkpoints_1b` → `autodl-tmp/.../checkpoints_1b/` (16G)
- `models` → `autodl-tmp/.../models/` (4.8G)
- `checkpoints_phase1/` (60G) — 数据盘上独立目录

## Checkpoint 保存策略：**累积式**

每个实验保存**每一代的完整模型**（~1.6G/代 for 410M, ~3.8G/代 for 1B），不覆盖。

### 数据盘各目录明细 (96G 总计)

| 目录 | 大小 | 内容 |
|------|------|------|
| `checkpoints_410m/` | 17G | gen_0 ~ gen_10，11代 × 1.6G |
| `checkpoints_1b/` | 16G | gen_0 ~ gen_3，4代 × 3.8G |
| **`checkpoints_phase1/`** | **60G** | 5 个实验 run，详见下 |
| `models/` | 4.8G | 基座模型 |

### checkpoints_phase1 明细 (60G)

| 实验 | 大小 | 代数 |
|------|------|------|
| `fixed_mix_r025_seed42` | 17G | 11代 (gen_0~10) |
| `fixed_mix_r025_seed43` | 17G | 11代 |
| `fixed_mix_r025_seed44` | 17G | 11代 |
| `fixed_mix_r02_seed43` | 1.6G | 1代 |
| `fixed_mix_r03_seed44` | 7.6G | 5代 (gen_0~4) |

## 可清理建议

**数据盘 73G 可用，不算紧急**，但如果需要腾空间：

1. **`checkpoints_410m/`（17G）** — 这是 `checkpoints` symlink 指向的 phase0 实验。如果 phase0 数据已全部提取到 results/ 且不再需要从这些 checkpoint 跑新分析，可清理。
2. **`checkpoints_1b/`（16G）** — 1B 模型 phase0，仅 4 代。同上，确认数据已提取后可清。
3. **phase1 中已完成且结果已集成的 run** — 三个 r025 seed（共 51G）如果实验数据已集成到论文，只需保留最终代或全部清理。

**不建议清理**：`models/`（4.8G，基座模型，重新下载慢）。

**根分区 5.2G** 的压力主要来自系统包和 miniconda（13G），与项目 checkpoints 无关。如果根分区也需要清理，查 pip cache (`pip cache purge`) 和 conda cache (`conda clean --all`) 是最有效的。

---
