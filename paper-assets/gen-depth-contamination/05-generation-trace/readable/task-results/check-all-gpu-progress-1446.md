# check all gpu progress 1446

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_all_gpu_progress_1446_20260516T144801_result.json`
- **Structured JSON:** [`a8afd9ed43170292a0f4.json`](../../sessions/a8/a8afd9ed43170292a0f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度汇总

| 实验 | GPU | 状态 | 进度 | 说明 |
|------|-----|------|------|------|
| **exp-018** Llama 8B depth | cuda:0 | 🟢 运行中 | ~88% | depth 5 生成中: 1044/1250 batches, ~6s/it |
| **exp-023** Wiki domain | cuda:1 | ✅ 完成 | 100% | EXIT_CODE=0, K*=2 |
| **exp-024** arXiv domain | cuda:2 | ❌ 失败 | 启动即崩 | `HF_HUB_OFFLINE` 导致无法加载 C4 数据集 |
| **exp-021** Length ablation | cuda:3 | ✅ 完成 | 100% | EXIT_CODE=0, 512 token 配置完成, K*=2 |

### exp-018 详情
- 已运行 9h47m，depth 0-4 数据已生成完毕（每个 depth 约 2 小时）
- 当前：**depth 5 生成阶段，1044/1250 batches (83%)**，~6s/batch
- 剩余生成：206 batches × 6s ≈ **20 分钟**完成 depth 5 生成
- 生成完后还需跑特征提取 + 分析，预计再 **30-60 分钟**
- GPU 利用率 96%，显存 16GB/24GB，**正常推进，未卡住**

### exp-024 失败原因
脚本启动时 `HF_HUB_OFFLINE=1` 环境变量生效，`load_dataset("allenai/c4")` 无法联网下载数据。需要 `unset HF_HUB_OFFLINE` 或确保 C4 数据已缓存到本地后重跑。

### 已完成实验结果速览
- **exp-023** (Wiki domain): K*=2, top feature=freq_entropy, ordinal accuracy=37.7%
- **exp-021** (512 token): K*=2, top feature=freq_entropy, ordinal accuracy=37.5%, JSD(d0→d1)=0.267

---
