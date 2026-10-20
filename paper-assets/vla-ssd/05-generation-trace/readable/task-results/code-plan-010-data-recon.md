# code plan 010 data recon

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_010_data_recon_20260516T045444_result.json`
- **Structured JSON:** [`cb3d1833df9a8bb23505.json`](../../sessions/cb/cb3d1833df9a8bb23505.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部侦察完成。下面是报告。

---

## LIBERO-Spatial 侦察报告

### 1. 数据状态

**LIBERO-Spatial 数据不存在。** `/root/autodl-tmp/vla-ssd/data/libero/` 下只有：
- `libero_10/`、`libero_90/`、`libero_goal/`（10 tasks × 50 demos，6.0GB）

需要下载 LIBERO-Spatial 数据到 `/root/autodl-tmp/vla-ssd/data/libero/libero_spatial/`。

下载命令（AutoDL 需先 `source /etc/network_turbo`）：
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
source /etc/network_turbo && \
HF_HUB_DISABLE_XET=1 \
REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt \
SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt \
python -c "
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id='libero-project/LIBERO',
    repo_type='dataset',
    allow_patterns='libero_spatial/*',
    local_dir='/root/autodl-tmp/vla-ssd/data/libero/'
)
"
```

预估大小：~6GB（与 libero_goal 规模相当，10 tasks × 50 demos）。

### 2. Checkpoint 状态

| 类型 | 路径 | 状态 |
|------|------|------|
| Trained (OpenVLA-7B) | `/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b/` | ✓ 存在 (3 shards) |
| Untrained (LLM reinitialized) | `/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-untrained/` | ✓ 存在 (4 shards) |

### 3. 脚本状态

**无需新脚本。** `extract_features.py` 已支持 `--data_dir` 参数，可直接指向 LIBERO-Spatial 目录。文件名解析也兼容 Spatial 格式（`LIVING_ROOM_SCENE2_put_the_red_mug_...` → regex 提取 task description）。

参考现有 LIBERO-Goal 特征格式：`(T, 33, 4096)` float16，含 `last_preaction` + `image_mean`，gzip 压缩。

### 4. 运行命令

**Trained extraction (cuda:0):**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/vla-ssd && \
CUDA_VISIBLE_DEVICES=0 HDF5_USE_FILE_LOCKING=FALSE python scripts/extract_features.py \
  --model_path /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b \
  --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_spatial/ \
  --output_dir /root/autodl-tmp/vla-ssd/features/trained_libero_spatial/ \
  --mode trained --gpu 0 --batch_size 4 --max_demos 50
```

**Untrained extraction (cuda:1):**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/vla-ssd && \
CUDA_VISIBLE_DEVICES=1 HDF5_USE_FILE_LOCKING=FALSE python scripts/extract_features.py \
  --model_path /root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-untrained \
  --data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_spatial/ \
  --output_dir /root/autodl-tmp/vla-ssd/features/untrained_libero_spatial/ \
  --mode trained --gpu 0 --batch_size 4 --max_demos 50
```

注意 untrained 用 `--mode trained`（使用预保存的 untrained checkpoint，避免每次随机重初始化，保证与 LIBERO-Goal untrained 特征一致）。

### 5. 预估

| 项目 | 估计值 |
|------|--------|
| 每个模型 extraction 时间 | ~100-150 min（参考 LIBERO-Goal：10 tasks × 50 demos，RTX PRO 6000 98GB VRAM） |
| 两个可并行 | 是（双 GPU），总墙钟 ~2-2.5h |
| 特征输出大小 | ~25GB/模型（参考 trained_libero_goal） |

### 6. 磁盘风险

**数据盘剩余 54GB，预计需要 ~56GB**（数据 6GB + trained features 25GB + untrained features 25GB）。非常紧张。建议：
- 先清理不需要的特征目录（如 `trained_libero_goal_no_inst`、`trained_libero_goal_shuffled` 等实验性目录）
- 或串行 extraction（先跑 trained，分析后再决定是否跑 untrained）

---
