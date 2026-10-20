# infra disk and download

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_disk-and-download_20260519T164506_result.json`
- **Structured JSON:** [`92a4c6308d8ca74e9d3f.json`](../../sessions/92/92a4c6308d8ca74e9d3f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Qwen3 已完成 shard-4 和 shard-5，正在下载 shard-2 (12%)。所有下载都是长时间任务。

提供当前状态报告：

---

## 下载状态报告

### 1. 磁盘状态
- **数据盘**: `/root/autodl-tmp` — 350GB 总量, 338GB 可用
- **根分区**: 30GB 总量, 25GB 可用
- **HF_HOME**: `/root/autodl-tmp/.hf_cache`
- 磁盘充裕，无 DISK_CRITICAL

### 2. 服务器环境
- 4x NVIDIA RTX PRO 6000 Blackwell (94GB VRAM each, 376GB total)
- torch 2.8.0+cu128, transformers 4.40.1, flash_attn 2.8.3
- conda base 环境 (miniconda3)

### 3. 下载项状态

| 项目 | 路径 | 当前大小 | 目标 | 状态 | 速度 |
|------|------|----------|------|------|------|
| OpenVLA-7B | `/root/autodl-tmp/openvla-7b/` | ~6GB | ~14GB | 进行中 (shard-3 done, shard-1/2 downloading) | ~0.3MB/s total |
| LIBERO hdf5 | `/root/autodl-tmp/LIBERO-datasets/` | 2.4GB | 未知 | 进行中 (3/132 files) | ~0.5MB/s |
| LIBERO RLDS | `/root/autodl-tmp/modified_libero_rlds/` | 320MB | ~10GB | 等待中 (排在 hdf5 之后) | - |
| Qwen3-8B | `/root/autodl-tmp/models/` | 5.6GB | ~16.5GB | 进行中 (shard-4/5 done, shard-2 at 12%) | ~0.6MB/s |

### 4. 下载方式
- **OpenVLA-7B**: wget 并行3路 from hf-mirror.com (shard-3 已完成)
- **LIBERO hdf5 + RLDS**: wget 串行 from hf-mirror.com
- **Qwen3-8B**: ModelScope CDN (国内镜像)

### 5. 需要后续处理
- 所有下载预计需要 **3-6 小时**完成（受网络带宽限制 ~0.3-0.6MB/s）
- 下载进程都在 nohup 后台运行，不受 SSH 断连影响
- 下载完成后需验证文件完整性
- LIBERO RLDS 数据排在 hdf5 之后串行下载
- **可通过以下命令监控进度**:
  ```bash
  du -sh /root/autodl-tmp/openvla-7b /root/autodl-tmp/LIBERO-datasets /root/autodl-tmp/modified_libero_rlds /root/autodl-tmp/models
  tail -5 /tmp/wget_mirror_openvla.log /tmp/wget_mirror_libero.log /tmp/download_qwen3_ms.log
  ```

### 6. 异常记录
- HuggingFace 官方下载在 AutoDL 上因 XET bridge 超时完全不可用
- `HF_HUB_DISABLE_XET=1` 对 huggingface_hub 0.36.2 无效
- hf_transfer 同样因 XET 失败
- 最终方案：hf-mirror.com 直连 + ModelScope 中国 CDN

---
