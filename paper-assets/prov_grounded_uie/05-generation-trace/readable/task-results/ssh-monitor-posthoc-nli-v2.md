# ssh monitor posthoc nli v2

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_monitor-posthoc-nli-v2_20260512T232609_result.json`
- **Structured JSON:** [`17520198da83ebfac5aa.json`](../../sessions/17/17520198da83ebfac5aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. cuda:1 已清理
- **GPU 0** (PID 40397): `evaluate.py` → 29984 MiB — 这个不是目标进程
- **GPU 1** (PID 64955): `rerank_nli.py` (posthoc_nli_v2) → 19878 MiB — **唯一进程，确认已释放**
- grpo_pilot_v1 (64374) 和 test_gen.py (65730) 已不在进程列表中

### 2. posthoc_nli_v2 进度
- 当前：**batch 8/124，64/985 样本**，稳步推进
- 模型加载正常（Mistral-Small-3.1-24B merged checkpoint）

### 3. 截断率 — 暂无法评估
- **脚本不记录截断信息**：`rerank_nli.py` 生成时用 `max_new_tokens=1024`，但不检测/不记录生成长度是否触达上限
- **输出文件尚不存在**：脚本在全部 124 batch 生成完 + NLI 评分后才写 `./outputs/posthoc_nli_v2/nli_reranking_results.json`
- **无历史对照**：`outputs/` 下没有先前 eval_results.json 可参考

### 4. 显存
| GPU | 占用 | 总量 | 利用率 |
|-----|------|------|--------|
| 0 | 29.3 GB | 95.6 GB | 30.6% |
| 1 | 19.4 GB | 95.6 GB | 20.3% |

GPU 1 显存已从多进程共占降到 ~19.4 GB（仅 posthoc_nli_v2）。

### 建议
截断率需等生成阶段完成后从输出文件检查。按当前速度（~8 samples/batch），124 batch 全跑完预计还需一段时间。到时可用：
```python
# 检查 completion 是否达到 max_new_tokens=1024 的 token 上限
truncated = sum(1 for s in data["per_sample"] if len(tokenizer.encode(s["completion"])) >= 1020)
```

---
