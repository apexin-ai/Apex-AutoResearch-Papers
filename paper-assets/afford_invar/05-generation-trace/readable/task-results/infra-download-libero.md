# infra download libero

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_download-libero_20260519T171147_result.json`
- **Structured JSON:** [`06d9108afc067d178cf1.json`](../../sessions/06/06d9108afc067d178cf1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载持续运行中，但 AutoDL 代理 + HuggingFace 无认证限速 + Qwen3 下载抢带宽导致速度很慢。

---

**产出报告已写入**: `/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/afford_invar/artifacts/data_format_and_download_status.md`

## 执行结果汇总

### 1. OpenVLA-OFT 数据格式需求
**训练需要 RLDS 格式**（tfrecord），不直接用 HDF5。
- 训练入口 `finetune.py` 参数 `--data_root_dir` 指向 RLDS 目录
- RLDS 数据集来自 HF `openvla/modified_libero_rlds`（~10GB）
- HDF5 是原始/中间数据，通过 `regenerate_libero_dataset.py` 转为 RLDS

### 2. 下载状态（后台运行中）

| 数据 | PID | 进度 | 大小 |
|------|-----|------|------|
| RLDS | 8365 | libero_10_no_noops 16/32 shards, 其余 3 suite 未开始 | ~2.5G / ~10G |
| HDF5 | 8758 | libero_10 4/10 files, libero_goal 下载中 | ~8.2G / ~60G |

### 3. 速度瓶颈
- **无 HF_TOKEN**: 限速严重
- **2 个 Qwen3-8B 下载**（PID 6028, 8127）占用 ~1.1MB/s 带宽
- **AutoDL 代理**: xet 协议超时，部分下载重试

### 4. 数据路径
- RLDS: `/root/autodl-tmp/modified_libero_rlds/`
- HDF5: `/root/autodl-tmp/LIBERO-datasets/`
- 磁盘: 321G 剩余

### 5. 下一步建议
- 如果 Qwen3 下载已不需要，可杀掉（PID 6028, 8127）释放带宽
- 设置 `HF_TOKEN` 可大幅提升下载速度
- 下载预计还需 RLDS ~1-2h, HDF5 ~6-10h

---
