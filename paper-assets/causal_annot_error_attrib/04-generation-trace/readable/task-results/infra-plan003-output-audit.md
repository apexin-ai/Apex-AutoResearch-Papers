# infra plan003 output audit

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_plan003-output-audit_20260520T135325_result.json`
- **Structured JSON:** [`831ca2dd68098ab276fe.json`](../../sessions/83/831ca2dd68098ab276fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整代码已读取，结论如下：

## 写入模式：**逐组合**，非逐 sample

关键代码路径：

1. **`annotate_batch`** (L350): 所有 sample 结果积累在内存 list 中，batch 完成后才 return
2. **`run_single`** (L524): 调 `annotate_batch` 拿到全部结果后，才调一次 `save_results`
3. **`save_results`** (L499): 此时才 `mkdir` + 写 JSONL + 写 NPZ

即：每个 (dataset × model × prompt) 组合的 1500 个 sample 全部标注完，才写一次磁盘。中途无 checkpoint。

## 输出路径

`results/{dataset}/{model}_{prompt}.jsonl` + `results/{dataset}/{model}_{prompt}_confusion_matrix.npz`

代码有 resume 机制（`load_existing_results` L485），但只从已写完的 JSONL 文件加载——组合内中断无法 resume。

## 当前状态：**PID 401208 已不存在，results/ 目录不存在**

进程已终止，且没有任何输出文件。如果它确实跑到了第一个组合的 1000/1500，**这 1000 条结果全部丢失**。

## 数据丢失风险：**高**

- 每组合 1500 样本 × 0.5s delay ≈ 12.5 分钟/组合，27 组合 ≈ 5.6 小时（纯 API 时间）
- 中间任何中断（进程 kill、SSH 断开、API 持续 5xx）= 该组合全部重来
- 没有逐 sample 落盘，没有 checkpoint

## 修复方案

在 `annotate_batch` 中加 **streaming write**——每个 sample 完成后立即 append 到 JSONL：

```python
def annotate_batch(self, samples, config, prompt_type, batch_delay=0.5, output_path=None):
    # ...
    for i, sample in enumerate(samples):
        # ... annotate_single ...
        results.append(result)
        if output_path:
            with open(output_path, "a") as f:
                f.write(json.dumps(result, ensure_ascii=False) + "\n")
        # ...
```

这样配合已有的 `load_existing_results` resume 逻辑，即使中断也只丢当前 1 条。混淆矩阵仍在组合完成后计算，不受影响。

---
