# code qwen25 14b multistrategy prep

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen25_14b_multistrategy_prep_20260519T025659_result.json`
- **Structured JSON:** [`d64d1132e97e117df753.json`](../../sessions/d6/d64d1132e97e117df753.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

topk50 中无 top_p 残留，确认干净。

---

## 报告

### 1. 原 scale_002 脚本关键参数

| 类别 | 参数 |
|------|------|
| **Generation** | `do_sample=True, top_p=0.95, temperature=1.0, max_new_tokens=512` |
| **LoRA** | `r=16, lora_alpha=32, target_modules=[q_proj, k_proj, v_proj], dropout=0.05` |
| **Training** | `epochs=3, bs=4, grad_accum=4, lr=2e-4, bf16=True, gradient_checkpointing=True` |
| **Data** | `NUM_SAMPLES=5000, MAX_DEPTH=3 (d0-d3), NUM_FOLDS=5` |

### 2. 新脚本路径

| 脚本 | Shell | Python |
|------|-------|--------|
| **temp09** | `scripts/run_qwen25_14b_temp09.sh` | `scripts/qwen25_14b_temp09.py` |
| **topk50** | `scripts/run_qwen25_14b_topk50.sh` | `scripts/qwen25_14b_topk50.py` |

### 3. 修改内容

**temp09**:
- `top_p=0.95` → `top_p=1.0`（禁用 nucleus）
- `temperature=1.0` → `temperature=0.9`
- 数据/检查点/结果目录后缀 `_temp09`

**topk50**:
- `top_p=0.95` → `top_k=50`（替换为 top-k 采样）
- `temperature=1.0` 保持不变
- 数据/检查点/结果目录后缀 `_topk50`

两个脚本的 LoRA 配置、训练参数、样本数完全不变。

### 4. 语法检查

- `bash -n` shell 脚本：**2/2 通过**
- `py_compile` Python 脚本：**2/2 通过**

### 5. 模型权重状态

8/8 shards 完整存在于 `/root/autodl-tmp/models/qwen25_14b/`，无需重新下载。

### 6. 启动命令

**temp09:**
```bash
bash -c "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/recursive_gen_depth_est && bash scripts/run_qwen25_14b_temp09.sh"
```

**topk50:**
```bash
bash -c "source /root/miniconda3/bin/activate && cd /root/autodl-tmp/recursive_gen_depth_est && bash scripts/run_qwen25_14b_topk50.sh"
```

注意：两个实验都需要完整 GPU 显存（14B FP16），不能同时跑，需要串行提交。

---
