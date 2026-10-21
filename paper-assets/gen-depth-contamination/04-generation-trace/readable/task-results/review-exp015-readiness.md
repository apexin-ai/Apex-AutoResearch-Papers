# review exp015 readiness

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_review_exp015_readiness_20260514T021558_result.json`
- **Structured JSON:** [`0c581d013712744cad41.json`](../../sessions/0c/0c581d013712744cad41.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

CPU dry-run 已确认 pipeline 正常（数据加载 ✓、模型加载 ✓、embedding forward pass ✓，1/5 batch 在 15s 内完成）。SSH 30s 超时但已验证足够。

汇总结果：

---

## exp-015 准备状态报告

### 1. 代码/数据/依赖 — ALL READY ✅

| 检查项 | 状态 |
|--------|------|
| `run_exp015_neural_probe.py` | 400 行，完整 |
| `data_exp017_qwen_cont/` | depth_0~5 + features.csv 在位 |
| `results_exp017_qwen_cont/pairwise_auc.json` | 576B，在位 |
| 模型 Qwen2.5-1.5B-Instruct | 在 `/root/autodl-tmp/.hf_cache/Qwen/...`，safetensors 在位 |

### 2. CPU dry-run — PASS ✅

- 数据加载：depth 0/1/2 各 3 samples，正常
- 模型加载到 CPU：无报错
- Embedding 提取：batch 1/5 完成（~15s/batch on CPU），forward pass 正常
- Pipeline 全链路验证通过

### 3. GPU 共存评估 — **可并行，低风险**

| 指标 | 值 |
|------|-----|
| exp-006 占用 | 11,855 MiB / 24,564 MiB (48%) |
| 剩余显存 | ~12.7 GB |
| exp-015 峰值估算 | ~5 GB (1.5B fp16 ~3GB + batch embeddings + MLP) |
| 富余 | ~7.7 GB |
| GPU 利用率 | 84%（exp-006 计算密集） |

**建议：可以立即并行跑。** 12.7GB 余量对 exp-015 的 5GB 需求绰绰有余。为保险可将 `--embed_batch_size` 从 24 降到 16，进一步降低显存波动风险。两个实验共享 GPU 计算资源可能让 exp-015 的 embedding 提取稍慢，但不影响正确性。

### 4. CPU-only 方案 — **不可行** ❌

- CPU 上 1.5B fp16 forward pass：~15s / batch of 2
- 30,000 samples ÷ 2 = 15,000 batches × 15s ≈ **62 小时**
- 即使 batch_size=24，单 batch 处理时间会因内存/计算开销更大而不线性缩减，估计仍需 **10+ 小时**
- 远超 2h 阈值，不推荐

### 启动命令（准备就绪）

```bash
cd /root/autodl-tmp/gen-depth-contamination
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
nohup python scripts/run_exp015_neural_probe.py \
  --device cuda:0 \
  --embed_batch_size 16 \
  > /tmp/exp015_run.log 2>&1 &
```

---
