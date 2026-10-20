# code cuda3 utilization

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cuda3_utilization_20260522T174219_result.json`
- **Structured JSON:** [`51048ae14f472fdb3a9d.json`](../../sessions/51/51048ae14f472fdb3a9d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已启动并注册。汇报如下：

---

## 选择：Gemma-2B 10K 样本量稳定性实验

### 选择原因
1. **10K robustness table (Table 28)** 当前有 2 个 pending 条目（Qwen-1.5B 数据已有但未填入，LLaMA-8B 在 cuda:2 上跑）
2. 现有 10K 实验全是 K*=2 的 config（Pythia-1.4B、Qwen-cont）。**Gemma-2B 是最有价值的补充**：5K 结果 1v2 AUC=0.5981，刚好低于 θ=0.60 阈值，是最 borderline 的 K*=1 case
3. 10K 实验如果确认 Gemma-2B 仍然 K*=1，就证明 borderline verdict 也具有 sample-size stability

### 实验状态
- **实验 ID**: `exp_gemma2b_10k`
- **GPU**: cuda:3 (6.4GB VRAM, 61% util)
- **tmux session**: `exp_gemma2b_10k`
- **Generation speed**: ~5.3s/batch (batch_size=16)
- **预计时长**:
  - Depth 1-2 生成完成（足以判断 K*）: ~2h
  - 完整 pipeline（5 depths + feature extraction + analysis）: ~5-6h

### 注意事项
- 完整 pipeline 超过 3h 窗口。但 Gemma-27B Phase 2 实际在 `run_gemma27b_c4.sh` 中设定为 `CUDA_VISIBLE_DEVICES=0`，Phase 2 会用 cuda:0 而非 cuda:3，所以 **不冲突**
- cuda:1 也完全空闲，如需要可随时迁移 Phase 2

### 额外发现
- `results/exp_qwen_cont_10k/summary.txt` 已有完整结果（K*=2, AUC 0v1=0.9875, 1v2=0.6346, 2v3=0.5616），但论文 `appendix_extended.tex:213` 仍标记为 *pending*。**这个数据可以立即填入论文。**

---
