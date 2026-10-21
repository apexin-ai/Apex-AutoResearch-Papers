# code d023 reeval westd gpu

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d023-reeval-westd-gpu_20260515T091952_result.json`
- **Structured JSON:** [`da5cf34c3287f9052a5d.json`](../../sessions/da/da5cf34c3287f9052a5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 当前状态报告

### Standard re-eval (pruned_standard_20)
- **PID**: 18580（Python 子进程），18573（bash wrapper）
- **服务器**: westd-11672, cuda:1
- **进度**: 8/100 at 3:31 elapsed
- **GPU**: 12958 MiB on GPU 1 (与 SFT 训练共享，总占用 ~64GB/98GB)
- **进程状态**: Running, 234% CPU, GPU 1 utilization 95%

### 速度问题
退化模型（1% accuracy）每个样本生成最多 4096 token 的垃圾（重复 "10 years" 或 "000..."），导致推理速度非常不均匀：
- 快样本: ~10s（模型碰巧早 EOS）
- 慢样本: ~60-90s（生成满 4096 token）
- 平均: ~26s/sample
- **预计总时间**: ~40-60 min，完成约 **18:10-18:30 UTC**

### RASP eval 尚未启动
等 Standard 完成后再启动 RASP eval。

### 模型加载方式
`load_pruned_model` → `AutoConfig.from_pretrained` 检测 `per_layer_intermediate_size`，创建最大维度模型 shell，然后逐层截断权重。

### 已确认的原始结果

| 模型 | 原始 accuracy | 样本数 |
|------|-------------|--------|
| pruned_standard_20 | **1%** (1/100) | 100 |
| pruned_rasp_20 | **29%** (29/100) | 100 |

原始 eval 输出显示 standard 模型完全退化（输出 "10 years" 重复或无穷 "0"）。1% 大概率不是 artifact，但 re-eval 会确认。

进程在后台运行中，等 Standard 完成后我会启动 RASP eval 并报告最终结果。

---
