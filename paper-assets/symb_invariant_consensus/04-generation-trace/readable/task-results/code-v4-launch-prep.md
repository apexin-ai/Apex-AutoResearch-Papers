# code v4 launch prep

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_v4-launch-prep_20260515T185737_result.json`
- **Structured JSON:** [`9bbccff7a19e70bb4624.json`](../../sessions/9b/9bbccff7a19e70bb4624.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集。汇总如下：

---

## 代码就绪状态

| 修复项 | 状态 | 位置 |
|--------|------|------|
| extract_answer + fallback | ✅ 已合入 | `sica/trace_generator.py:69,91` |
| max_tokens=16384 默认值 | ✅ 已合入 | `run_full_mvp.py:214` |
| --save-intermediates | ✅ 已合入 | `run_full_mvp.py:216` |
| _unify_sorts_for_equiv (sort统一) | ✅ 已合入 | `sica/z3_maxsat.py:334` |
| --resume (断点续跑) | ✅ 已合入 | `run_full_mvp.py:211` |
| --retry-failed (选择性重跑) | ❌ 不存在 | — |

## 缺失项

1. **`--retry-failed` 不支持** — `--resume` 按 `problem_id` 跳过所有已完成题目，无法区分 truncated/0-vote。v4 需要在 v3 完成后写脚本从结果中提取需重跑题目，生成过滤数据文件。

2. **v3 结果尚未产出** — `results/` 下无 v3 文件，v4 启动依赖 v3 结果。

3. **eval_proofwriter.py 的 max_tokens 默认 4096**（非 16384）。ProofWriter 逻辑推理任务可能够用，但如需一致可加 `--max-tokens 16384`。

## 启动命令

### 1. v4 AIME re-run（需 v3 完成后执行）

**前置步骤**：从 v3 结果提取 truncated/0-vote 题目生成 `data/aime2024_v4_retry.json`：
```python
# 在服务器上运行一次性脚本
import json
with open("results/aime30_v3.json") as f:  # v3 结果文件名需确认
    v3 = json.load(f)
with open("data/aime2024_subset.json") as f:
    all_problems = {p["id"]: p for p in json.load(f)}

retry_ids = set()
for r in v3["results"]:
    if r.get("truncated_traces", 0) > 0 or r.get("sc_vote_count", 0) == 0:
        retry_ids.add(r["problem_id"])

retry_data = [all_problems[pid] for pid in retry_ids if pid in all_problems]
with open("data/aime2024_v4_retry.json", "w") as f:
    json.dump(retry_data, f, indent=2)
print(f"v4 retry: {len(retry_data)} problems")
```

**启动命令**：
```bash
cd /root/symb_invariant_consensus
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
python run_full_mvp.py \
  --mode vllm --k 12 \
  --max-tokens 16384 \
  --math-data data/aime2024_v4_retry.json \
  --no-proofwriter \
  --save-intermediates \
  --output results/aime30_v4.json \
  2>&1 | tee /tmp/aime30_v4.log
```

### 2. MATH-50 完整 MVP

```bash
cd /root/symb_invariant_consensus
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
python eval_math500.py \
  --mode vllm --k 12 \
  --max-tokens 16384 \
  --temperature 0.7 \
  --save-intermediates \
  --output results/math50_full.json \
  2>&1 | tee /tmp/math50.log
```

### 3. ProofWriter-10 sanity check

```bash
cd /root/symb_invariant_consensus
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
python eval_proofwriter.py \
  --n-problems 10 --k 12 \
  --max-tokens 16384 \
  --temperature 0.7 \
  --save-intermediates \
  --output results/proofwriter10.json \
  2>&1 | tee /tmp/proofwriter10.log
```

---
