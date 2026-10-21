# code pi05 sync and smoke test

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_pi05-sync-and-smoke-test_20260521T012445_result.json`
- **Structured JSON:** [`472645f101c6b8985232.json`](../../sessions/47/472645f101c6b8985232.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改看起来完整正确。

---

## 总结

### 1. 代码同步状态
| 文件 | 状态 |
|------|------|
| `pi05_wrapper.py` | ✅ 同步到 bjb2 + 修复了两个问题 |
| `evaluate.py` | ✅ 同步到 bjb2（31667 bytes，完整匹配） |

### 2. GPU 可用性
- **GPU**: 单卡 4090 (24564 MiB)
- **占用**: 0 MiB（完全空闲，无其他进程）

### 3. Smoke Test — **PASSED**
| 指标 | 值 |
|------|-----|
| obs_features shape | (1, 2048) ✓ |
| samples shape | (1, 2, 50, 7) ✓ |
| GPU 占用 | 8.71GB → 8.72GB |
| 推理时间 (K=2) | 1.24s |
| 模型加载时间 | 238.2s |

### 4. 修复内容（pi05_wrapper.py on bjb2）
1. **Tokenizer**: PaliGemma 是 gated repo，无法直接下载。改为 fallback 到本地保存的 `unsloth/gemma-2b` tokenizer（同一 SentencePiece vocab，256K）
2. **Vision tower key mismatch**: transformers 5.8.0 将 `.vision_tower.vision_model.X` 改为 `.vision_tower.X`，导致 437 个 vision tower 权重加载失败。添加 `_fix_vision_tower_keys()` 方法做 key remapping + strict=False 加载

### 5. 待注意（未修复）
- **归一化不匹配**: 模型 config 显示训练时用 `MEAN_STD` 归一化，但 wrapper 代码用 `QUANTILES` (q01/q99)。这会导致实际评估时 state 输入和 action 输出的归一化方式与训练不一致。需要 Worker A 确认意图。

### 6. Baseline eval 命令
```bash
cd /root/acr-vla-conformal-refinement/src && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
CUDA_VISIBLE_DEVICES=0 python3 evaluate.py \
  --model pi05 \
  --pi05_path /root/autodl-tmp/models/pi05_libero_finetuned \
  --mode vla_only \
  --benchmark object \
  --seed 42 \
  --output_dir /root/acr-vla-conformal-refinement/logs
```

---
