# code gsm8k eval prep v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gsm8k-eval-prep-v2_20260519T174112_result.json`
- **Structured JSON:** [`c0e9a435928fd4c4797e.json`](../../sessions/c0/c0e9a435928fd4c4797e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. evaluate.py 结构与 GSM8K 支持

**已完全支持，无需修改代码。** evaluate.py 内置 4 个 benchmark（MMLU、ARC-Challenge、GSM8K、HumanEval），通过 `--benchmarks gsm8k` 即可单独跑。

GSM8K 评估方式：
- 8-shot CoT（从 train split 取前 8 个 example）
- Generation-based：`model.generate(max_new_tokens=256, do_sample=False)`
- 答案提取：regex 抽最后一个数字，与 gold answer（`####` 后的数字）做 exact match
- 输出：per-item correctness JSON，与 MMLU/ARC 格式一致，可直接用于 IRT

### 2. 推荐路径

**路径 A（直接用 evaluate.py）**，零额外开发工作量。不需要 lm-eval-harness，不需要写新脚本。

### 3. Checkpoint 确认

25 个 seed=42 checkpoint 全部就绪：

| Model | d000 | d005 | d025 | d050 | d100 |
|-------|------|------|------|------|------|
| Qwen2.5-7B | ✓ | ✓ | ✓ | ✓ | ✓ |
| Qwen2.5-14B | ✓ | ✓ | ✓ | ✓ | ✓ |
| gemma-2-9b | ✓ | ✓ | ✓ | ✓ | ✓ |
| phi-4 | ✓ | ✓ | ✓ | ✓ | ✓ |
| OLMo-2-7B | ✓ | ✓ | ✓ | ✓ | ✓ |

Base models: `/root/autodl-tmp/models/{Qwen2.5-7B, Qwen2.5-14B, gemma-2-9b, phi-4, OLMo-2-1124-7B}`

### 4. 已有结果

`Qwen2.5-7B_d000_s42` 已有 GSM8K 结果（71.04%, 937/1319），脚本会自动跳过（`.done` 检测）。

### 5. 脚本与执行命令

脚本已保存到本地：`scripts/run_gsm8k_eval_s42.sh`

需先 sync 到服务器后执行：
```bash
# 单 GPU 顺序跑全部 25 个 checkpoint
bash /root/contamcal-irt-calibration/scripts/run_gsm8k_eval_s42.sh 0

# 或用 nohup 后台跑
nohup bash /root/contamcal-irt-calibration/scripts/run_gsm8k_eval_s42.sh 0 > /root/autodl-tmp/exp001/gsm8k_eval.log 2>&1 &
```

结果输出到：`/root/autodl-tmp/exp001/eval_results_gsm8k/{model}_{dosage}_s42/`

### 6. 时间预估

GSM8K test set = 1319 items，generation-based（每题 ~256 tokens），batch_size=8：

| Model | 预估单 checkpoint | 来源 |
|-------|-------------------|------|
| 7B 级（Qwen-7B, OLMo-7B） | ~15-20 min | 类推 |
| 9B 级（gemma-2-9b） | ~20-25 min | 类推 |
| 14B（Qwen-14B, phi-4） | ~30-45 min | 类推 |

- 全部 25 个 checkpoint 单 GPU 顺序跑：**~10-15 小时**
- 如果用 2 个 GPU 并行（分两个脚本或 split batch）：**~5-8 小时**

**当前 4 个 GPU 都在使用中**（58-64GB occupied），需等 GPU 空闲后再提交。

---
