# code hgrn2 diagnose

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_hgrn2_diagnose_20260518T155822_result.json`
- **Structured JSON:** [`f4d7db96d13ea9486259.json`](../../sessions/f4/f4d7db96d13ea9486259.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

### 评测完成！全部 6 个 task 结果：

| Task | acc | acc_norm |
|---|---|---|
| lambada_openai | 0.5030 | - |
| hellaswag | 0.4637 | 0.6054 |
| winogrande | 0.6054 | - |
| arc_easy | 0.7323 | 0.6696 |
| arc_challenge | 0.3933 | 0.4044 |
| mmlu | 0.2344 | - |

结果已保存到 `/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-HGRN2-hybrid-12-1.json`

---

## 诊断总结

### 问题根因
1. **网络不可达**：服务器无法访问 HuggingFace Hub，每个数据集下载尝试 5 次重试后超时。MMLU 有 57 个子任务，导致重试时间极长（进程卡在数据集下载阶段 5+ 分钟无进展）
2. **autoregressive generate 有 bug**：HGRN2 hybrid 模型的 attention 层在 KV cache 模式下调用 `flash_attn_varlen_func` 时索引越界（CUDA assert error），但这不影响 lm_eval（只用 forward pass/loglikelihood）

### 解决方法
- 设置 `HF_DATASETS_OFFLINE=1` 和 `HF_HUB_OFFLINE=1` 强制使用本地缓存，跳过所有网络请求
- 之前的连续失败很可能是进程在网络重试中耗尽时间或被超时杀掉

### GPU 残留
- 清理前有 2 个 python 进程残留（各 ~3182 MiB）
- 另外发现有第二个评测进程 (HGRN2-hybrid-24-1) 也在运行

---
