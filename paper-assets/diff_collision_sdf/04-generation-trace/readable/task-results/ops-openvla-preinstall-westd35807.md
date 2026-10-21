# ops openvla preinstall westd35807

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_openvla_preinstall_westd35807_20260525T062503_result.json`
- **Structured JSON:** [`aa0edfcbc8ae7283795b.json`](../../sessions/aa/aa0edfcbc8ae7283795b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载速度 ~1 MB/s，第一个分片 6.5GB 预计 ~90 分钟。三个分片串行下载总计约 3-4 小时。

我汇报当前状态：

**汇报**

| 项目 | 状态 |
|------|------|
| **脚本同步** | `/root/diff_collision_sdf/scripts/eval_safelibero_openvla.py` (626 行) |
| **依赖安装** | |
| - torch 2.8.0+cu128 | 已有 |
| - torchvision 0.23.0+cu128 | 已有 |
| - transformers 4.53.2 | 已有 |
| - pillow 11.3.0 | 已有 |
| - scipy 1.17.1 | 已有 |
| - tokenizers 0.21.1 | 已有 |
| - timm 1.0.27 | **新装** |
| - flash-attn 2.8.3 | **新装** |
| - huggingface_hub 0.36.2 | 已有（从 0.30.2 经历了 xet bug 处理后恢复） |
| **模型下载** | **进行中** — aria2c 16 线程从 hf-mirror.com 下载，速度 ~1 MB/s |
| - processor | 已缓存 (`/root/autodl-tmp/.hf_cache/hub/models--openvla--openvla-7b/`) |
| - model shard 1/3 (6.5GB) | 下载中 (~288MB/6.5GB)，PID=58256 |
| - model shard 2/3 + 3/3 | 排队中 |
| **磁盘** | 根分区 30G 用了 20G (11G 余)；数据盘 `/root/autodl-tmp/` 350G 用了 168G (183G 余，模型放这里) |

**问题**：AutoDL 代理下载 HuggingFace 大文件极慢（xet CDN 在美国），三个分片串行下载预计 **3-4 小时**。

**后台进程**：
- 主进程 PID=58253（bash wrapper）
- aria2c PID=58256（正在下载 shard 1）
- 日志：`/tmp/openvla_aria2.log`
- 模型原始文件：`/root/autodl-tmp/openvla-7b-raw/`
- HF cache（processor等）：`/root/autodl-tmp/.hf_cache/hub/models--openvla--openvla-7b/`

**下载完成后需要做**：
1. 将原始文件注册到 HF cache 或 `from_pretrained` 时指定 `--model_path /root/autodl-tmp/openvla-7b-raw/`
2. 运行验证脚本确认模型可加载

下载已在后台运行，无需干预。可稍后用以下命令检查状态：
```bash
# 检查是否完成
ls /root/autodl-tmp/openvla-7b-raw/*.aria2 && echo "STILL_DOWNLOADING" || echo "DONE"
tail -20 /tmp/openvla_aria2.log
ls -lh /root/autodl-tmp/openvla-7b-raw/
```

---
