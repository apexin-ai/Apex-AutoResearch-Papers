# LIBERO 数据格式需求与下载状态报告

**日期**: 2026-05-20
**服务器**: westd-19957

## 1. OpenVLA-OFT 数据格式需求

**结论: 训练需要 RLDS 格式（tfrecord），HDF5 为中间/原始格式**

- 训练管道: `finetune.py` → `RLDSDataset` → `tensorflow_datasets` → tfrecord 文件
- 训练参数: `--data_root_dir /PATH/TO/RLDS/DATASETS/DIR/ --dataset_name libero_spatial_no_noops`
- 数据流: 原始 HDF5 → `regenerate_libero_dataset.py`（去 no-op + 256px）→ 转 RLDS tfrecord

### 需要的 RLDS 数据集（4 个 suite）
| 数据集名 | 用途 | 来源 |
|----------|------|------|
| `libero_spatial_no_noops` | 空间关系任务训练 | `openvla/modified_libero_rlds` (HF) |
| `libero_object_no_noops` | 物体操作任务训练 | 同上 |
| `libero_goal_no_noops` | 目标达成任务训练 | 同上 |
| `libero_10_no_noops` | 混合任务训练 | 同上 |
| `libero_4_task_suites_no_noops` | 四合一训练（可选） | 同上（mixtures.py 中定义） |

### 关键代码路径
- 训练入口: `openvla-oft/vla-scripts/finetune.py` (L74: `data_root_dir`)
- 数据加载: `openvla-oft/prismatic/vla/datasets/datasets.py` → RLDS batch transform
- OXE 配置: `openvla-oft/prismatic/vla/datasets/rlds/oxe/configs.py` (L644-680)
- Mixtures: `openvla-oft/prismatic/vla/datasets/rlds/oxe/mixtures.py` (L196-214)
- HDF5 再生成: `openvla-oft/experiments/robot/libero/regenerate_libero_dataset.py`

## 2. 下载状态

### RLDS 数据（优先级高 - 训练直接需要）
- **来源**: `openvla/modified_libero_rlds` (HuggingFace, ~10GB)
- **目标目录**: `/root/autodl-tmp/modified_libero_rlds/`
- **下载进程**: PID 8365（Python snapshot_download）
- **当前进度**: libero_10_no_noops 16/32 shards 完成，其余 3 suite 待下载
- **已下载大小**: ~2.2G（主目录）+ ~523M（cache 中）
- **预计剩余时间**: ~1.5-2 小时

### HDF5 原始数据（优先级低 - 备份/重生成用）
- **来源**: `yifengzhu-hf/LIBERO-datasets` (HuggingFace)
- **目标目录**: `/root/autodl-tmp/LIBERO-datasets/`
- **下载进程**: PID 8758（Python snapshot_download, allow_patterns 限制只下载 4 suite）
- **当前进度**: libero_10 4/10 files (5.2G), libero_goal 0/10 (in cache)
- **未开始**: libero_spatial, libero_object
- **已下载大小**: ~8.4G（主目录）+ ~3.2G（cache 中）
- **预计剩余时间**: ~3-6 小时

### 限制因素
- **未认证 HuggingFace 请求**: 无 HF_TOKEN，下载限速严重
- **AutoDL 代理**: xet 协议超时，部分连接需要重试
- **建议**: 设置 HF_TOKEN 可显著加速下载

## 3. 数据路径汇总

| 数据 | 路径 | 状态 |
|------|------|------|
| RLDS 训练数据 | `/root/autodl-tmp/modified_libero_rlds/` | 下载中 |
| 原始 HDF5 | `/root/autodl-tmp/LIBERO-datasets/` | 下载中 |
| 磁盘剩余 | 321G (`/root/autodl-tmp`) | 充足 |

## 4. 训练时的数据引用

```bash
# 训练命令中的数据参数
torchrun --standalone --nnodes 1 --nproc-per-node X vla-scripts/finetune.py \
  --data_root_dir /root/autodl-tmp/modified_libero_rlds/ \
  --dataset_name libero_spatial_no_noops \
  ...
```

## 5. 异常记录
- HDF5 下载中的 `libero_90` 目录已手动删除（不需要）
- 旧的冲突下载进程（PID 8414, 6224）已杀掉
- Qwen3-8B 模型下载进程（PID 6028, 8127）仍在运行，占用部分带宽
