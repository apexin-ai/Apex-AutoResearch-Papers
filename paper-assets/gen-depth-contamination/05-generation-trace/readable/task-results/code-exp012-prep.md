# code exp012 prep

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp012_prep_20260515T151342_result.json`
- **Structured JSON:** [`af22c526a810e04f2ec5.json`](../../sessions/af/af22c526a810e04f2ec5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 脚本状态
- 存在: yes (`scripts/exp012_ppl_depth_correlation.py`, 438 行)
- 语法/import: OK (torch 2.10.0+cu128, transformers 4.57.6, scipy, sklearn, numpy, matplotlib 全部就绪)
- 需要修改: **已修复** — `allenai/OLMo-1B-0724` → `allenai/OLMo-1B-0724-hf`（原 ID 404 不存在）

## 数据路径
- data_exp001_pythia: 6 files (depth_0..5.jsonl, 5000 samples each) ✅
- data_exp002_olmo: 6 files ✅
- data: 6 files ✅
- data_exp017_qwen_cont: 6 files ✅

## 模型缓存
- **Qwen/Qwen2.5-1.5B-Instruct**: cached ✅（已修复 hub 缓存位置，`AutoConfig.from_pretrained` 验证通过）
- **EleutherAI/pythia-1.4b**: 下载中 🔄（1.2GB/2.9GB，~3 min，另有完整 ModelScope 副本可备用）
- **allenai/OLMo-1B-0724-hf**: 下载中 🔄（shard1 完成，shard2 755MB/4.7GB，~12 min）

## 修复项
1. 脚本默认 `--bino_performer` 从 `allenai/OLMo-1B-0724` 改为 `allenai/OLMo-1B-0724-hf`
2. Qwen hub cache 从 `$HF_HOME/models--Qwen--*` 移至 `$HF_HOME/hub/models--Qwen--*`
3. 清除了旧进程遗留的 pythia lock 文件

## 启动命令
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
source /etc/network_turbo 2>/dev/null && \
export HF_HOME=/root/autodl-tmp/.hf_cache && \
export HF_ENDPOINT=https://hf-mirror.com && \
export HF_HUB_DISABLE_XET=1 && \
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && \
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt && \
cd /root/autodl-tmp/gen-depth-contamination && \
python scripts/exp012_ppl_depth_correlation.py \
  --device cuda:0 \
  --n_samples 500 \
  --output_dir artifacts/exp012_results
```

注意：启动前需确认模型下载完成：
```bash
ls /root/autodl-tmp/.hf_cache/hub/models--allenai--OLMo-1B-0724-hf/blobs/*.incomplete 2>/dev/null && echo "STILL_DOWNLOADING" || echo "READY"
ls /root/autodl-tmp/.hf_cache/hub/models--EleutherAI--pythia-1.4b/blobs/*.incomplete 2>/dev/null && echo "STILL_DOWNLOADING" || echo "READY"
```

## 预估运行时间
- GPU: RTX 4090 D (24GB)
- 数据量: 4 conditions × 6 depths × 500 samples × 3 models = 36,000 次 PPL 推理
- 预估: **60-90 分钟**（模型顺序加载/释放，峰值 VRAM ~5GB）

---
