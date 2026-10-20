# ssh mmlu paraphrase phases

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_mmlu-paraphrase-phases_20260513T205451_result.json`
- **Structured JSON:** [`bea3093db0287e04a456.json`](../../sessions/be/bea3093db0287e04a456.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 1. 脚本结构

`paraphrase_gen.py` **没有内部 phase/stage 划分**。每次调用处理**一个 benchmark**（通过 `--benchmark` 参数指定）。所谓"阶段"是外部多次调用：

| 调用 | benchmark | 状态 | output |
|------|-----------|------|--------|
| 1 | humaneval | 已完成 | `humaneval_paraphrases.json` (500KB) |
| 2 | arc_challenge | 已完成 | `arc_challenge_paraphrases.json` (1.7MB) |
| 3 | gsm8k | 已完成 | `gsm8k_paraphrases.json` (2.2MB) |
| 4 | **mmlu** | **运行中** | 尚未生成 |

### 2. 单次调用内部流程

每个 benchmark 调用内有 **1 + max_retries = 3 次 attempt**（max_retries 默认 2）：
- Attempt 1: 全量 items → vLLM 批量生成 → QC（cosine sim ≥ 0.85 AND BLEU ≤ 0.3）
- Attempt 2: QC 失败的 items 重试
- Attempt 3: 仍失败的 items 再试
- **输出在所有 attempt 结束后一次性写出** `mmlu_paraphrases.json`

### 3. MMLU 当前进度

| Attempt | Items | Batches (×16) | 状态 |
|---------|-------|---------------|------|
| 1 | 14042 | 878 | **已完成** — 4112/14042 passed QC (29.3%) |
| 2 | 9930 | 621 | **进行中** — 121/621 (19.5%) |
| 3 | ? | ? | 待定 |

- Attempt 1: 03:15 → 04:45，耗时 ~90 min
- Attempt 2: 04:45 开始，当前 121/621，tqdm ETA ~1h45m（约到 06:42）
- Attempt 3: 预计 ~5000-7000 items（取决于 attempt 2 pass rate），估计 ~40-60 min

### 4. ETA 估算

- Attempt 2 剩余: ~1h45m（到 ~06:42 北京时间）
- Attempt 3: ~40-60min
- QC 计算 + 写文件: ~5min
- **总计: 预计还需 ~2.5-3 小时，约 07:30-08:00 北京时间完成**

---
