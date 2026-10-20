# code env setup deploy

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_env-setup-deploy_20260512T105955_result.json`
- **Structured JSON:** [`d7a98513438f34206a31.json`](../../sessions/d7/d7a98513438f34206a31.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

环境搭建全部完成。汇总：

---

### 完成状态

**1. 环境信息**
- Python: 3.12.3 (conda base, `/root/miniconda3`)
- torch: 2.10.0+cu128
- CUDA: 12.8 (driver 595.58.03)
- GPU: 2× NVIDIA RTX PRO 6000 Blackwell Server Edition, 96GB 显存
- 所有依赖已预装（transformers 4.57.6, datasets 4.8.4, sentence-transformers 5.4.1, sklearn 1.8.0, scipy 1.17.1, accelerate 1.13.0, wandb 0.26.0 等）

**2. 代码同步**
- 8 个文件全部创建成功：`requirements.txt`, `data_prep.py`, `generate.py`, `representation_monitor.py`, `diversity_selection.py`, `train_student.py`, `evaluate.py`, `run_mvp.py`
- 路径: `/root/div_cal_verify/`
- 额外创建 `env.sh` 供后续使用

**3. 数据准备**
- train_chunks: 242,666 chunks (350MB)
- ref_chunks: 512 chunks (validation set 较小，仅产出 512 个 512-token chunk)
- test_chunks: 583 chunks
- ref_rare_labels: 512 positives
- 路径: `/root/div_cal_verify/data/`

**4. 模型下载**
- Qwen3-1.7B: `/root/models/Qwen/Qwen3-1.7B` (1,721M params)
- Qwen3-4B: `/root/models/Qwen/Qwen3-4B` (4,022M params)
- Contriever: HF cache (已验证可加载)
- Qwen 模型通过 ModelScope 直连下载（~10-18MB/s），Contriever 通过 hf-mirror 代理下载

**5. 问题及解决方案**
- HuggingFace 直连不可达（需要代理），`network_turbo` 代理速度极慢（~400kB/s）
- **解决**: Qwen 模型改用 ModelScope 直连（不走代理，~10-18MB/s，快 25 倍），HF 请求通过 hf-mirror.com 镜像
- `SSL_CERT_FILE` 和 `REQUESTS_CA_BUNDLE` 环境变量需设置以避免 SSL 错误

**6. 运行实验的命令**
```bash
source /root/div_cal_verify/env.sh
cd /root/div_cal_verify
python run_mvp.py --method rgds --num_generations 4 --gpu_ids 0,1 \
  --student_model /root/models/Qwen/Qwen3-1.7B \
  --generator_model /root/models/Qwen/Qwen3-4B
```

---
