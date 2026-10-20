# diag occ prep status

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_occ_prep_status_20260520T093127_result.json`
- **Structured JSON:** [`d15858afda9d28b0eea9.json`](../../sessions/d1/d15858afda9d28b0eea9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已足够，以下是完整报告。

---

## A. Occ GT 数据提取进度

**脚本**：`/root/occsafe_vla/occ_pipeline/extract_occupancy.py`
- 目标：`libero_spatial` benchmark，10 个 task，每 task 50 demos
- 产出：`occ_{task}.hdf5`（bev_binary 64x64 bool + bev_semantic 64x64 uint8）

**产出状态**：

| # | 文件 | 大小 | 状态 |
|---|------|------|------|
| 1-9 | 9 个 task 的 HDF5 | 2.3-2.6 MB | 正常 |
| 10 | wooden_cabinet | **1.3 MB** | **可疑（约为正常值一半）** |

- `occ_index.json` 已生成，覆盖全部 10 task × 50 demos
- 文件时间戳：全部 May 20 17:24-17:28

**完成度估计：~95%**（9/10 完整，wooden_cabinet 需验证是否 demo 不全）

**SIGSTOP 进程**：10 个 python 进程处于 `T`（stopped）状态，GPU 0 占用 68.7 GB 显存。

---

## B. BEV Aux Head 代码就绪状态

**全部已实现，无缺失模块。** 详细清单：

| 组件 | 文件 | 行号 | 状态 |
|------|------|------|------|
| BEVOccupancyHead 模型 | `prismatic/models/occ_head.py` | 全文 | Done |
| FocalLoss (alpha=0.25, gamma=2.0) | `prismatic/models/occ_head.py` | 全文 | Done |
| 训练配置项 (use_occ_head, occ_loss_weight, occ_detach 等) | `finetune.py` | L90-95 | Done |
| 训练循环 loss 计算 | `finetune.py` | L464-473 | Done |
| Loss weight 指数衰减 | `finetune.py` | L1107-1109 | Done |
| Occ head 初始化 + DDP 封装 | `finetune.py` | L970-987 | Done |
| Optimizer 参数注册 | `finetune.py` | L997-998 | Done |
| Checkpoint 保存 | `finetune.py` | L684-685 | Done |
| Dataset occ label 加载 | `datasets.py` | L41-205 | Done |
| occ_index.json 构建脚本 | `build_occ_index.py` | 全文 | Done |
| 单元测试 | `test_occ_loader.py`, `verify_occ_fix.py` | 全文 | Done |

---

## C. 阻塞项清单

1. **wooden_cabinet HDF5 可能不完整** — 1.3MB vs 其他 2.3-2.6MB，无法在 read-only 下运行 h5py 验证 demo 数量（conda env python3.10 不在白名单）
2. **GPU 0 被 10 个 SIGSTOP 进程锁住 68.7GB 显存** — 数据已基本提取完毕，这些进程只是占着内存
3. **无代码缺失** — 模型、数据管道、训练循环、配置项全部就绪

---

## 建议

- **Kill GPU 0 的 10 个 SIGSTOP 进程**，释放 68.7GB 显存。数据已产出，无需 SIGCONT。
- **验证 wooden_cabinet 文件**：用 `conda activate occsafe && python -c "import h5py; f=h5py.File('...wooden_cabinet...','r'); print(len(f['data'].keys()))"` 确认 demo 数量。如果不完整，在 GPU 3 上 `python extract_occupancy.py --task_id 9` 单独补跑（几分钟即可）。
- **Vanilla 训练完成后**，直接启动 mvp_occ：`--use_occ_head --occ_data_dir /root/occsafe_vla/occ_data`，无需额外代码开发。

---
