# research paraphrase eval plan

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paraphrase-eval-plan_20260514T075524_result.json`
- **Structured JSON:** [`911b373fc7f5e3f8480b.json`](../../sessions/91/911b373fc7f5e3f8480b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息收集完毕，以下是调研报告。

---

## Paraphrase Eval 调研报告

### 1. 运行方式

`evaluate.py` 已支持 paraphrase eval，通过 `--paraphrase-dir` 参数触发。命令格式：

```bash
python evaluate.py \
  --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B \
  --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter \
  --paraphrase-dir /root/autodl-tmp/exp001/paraphrases/ \
  --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d000_s42_para \
  --benchmarks mmlu gsm8k arc_challenge humaneval
```

当 `--paraphrase-dir` 设置后，每个 benchmark 会：
1. 从 `{paraphrase_dir}/{benchmark}_paraphrases.json` 加载数据
2. 过滤 `passed_qc: true` 的项
3. 用 `evaluate_paraphrased()` 函数评估（复用 MCQ/GSM8K/HumanEval 逻辑）

### 2. 输入数据状态

4 个 paraphrase 文件已就绪：

| 文件 | 大小 |
|------|------|
| `mmlu_paraphrases.json` | 27MB (407k lines) |
| `arc_challenge_paraphrases.json` | 1.7MB (34k lines) |
| `gsm8k_paraphrases.json` | 2.2MB (24k lines) |
| `humaneval_paraphrases.json` | 500KB (3k lines) |

数据结构包含 `original`、`paraphrase_parsed`、`similarity`、`bleu`、`passed_qc` 等字段。

### 3. ConStat 信号要求

`signal_constat.py` 需要：
- `--original-eval-paths`: 原始 eval 的 `eval_results.json`（每 seed 一个）
- `--paraphrase-eval-paths`: paraphrase eval 的 `eval_results.json`（每 seed 一个）
- **原始和 paraphrase 的 seed 数必须相等**
- 读取格式：`data["benchmarks"][benchmark]["per_item"][i]["correct"]`

### 4. 已有 eval 和需要补跑的 paraphrase eval

已有原始 eval 结果：

| 模型 | Dosage | Seeds | 原始 eval | para eval |
|------|--------|-------|-----------|-----------|
| 0.5B | d000 | s42, s123 | ✅ | ❌ (空目录) |
| 0.5B | d005 | s42 | ✅ | ❌ |
| 0.5B | d100 | s42 | ✅ | ❌ |
| 0.5B | raw | - | ✅ | ❌ |
| 1.5B | d000 | s42, s123 | ✅ | ❌ |
| 1.5B | d100 | s42 | ✅ | ❌ |
| 3B | d000 | s42, s123 | ✅ | ❌ |
| 3B | raw | - | ✅ | ❌ |

### 5. 时间估算

从成功的 v5 日志（0.5B, d000_s42, 全 4 个 benchmark）：
- 开始 10:39 → 结束 15:29 = **约 4h50m**（含 HF 下载超时重试）
- Paraphrase eval 从本地 JSON 读取，不需要 HF 下载，实际推理时间应**显著更短**

单 benchmark 估算（0.5B）：
- MMLU: ~14k items @ ~50 it/s → **~5 min**
- ARC: ~1k items @ ~55 it/s → **~20 sec**
- GSM8K: 生成式，较慢 → **~30-60 min**（估计）
- HumanEval: ~164 items @ ~5.4 s/it → **~15 min**

**单个 0.5B checkpoint 全 benchmark paraphrase eval 估计 ~50-80 min**。1.5B/3B 会按模型大小成比例变慢。

### 6. 执行计划建议

**最小 ConStat 需求**：每个 dosage 至少 1 seed 的 paraphrase eval。优先跑 d000 的两个 seed（s42, s123），因为这是 ConStat 差异计算的基线。

**执行顺序**：

| 优先级 | 任务 | 原因 |
|--------|------|------|
| P0 | 0.5B d000 s42 para | 最小模型，验证管线正确性 |
| P0 | 0.5B d000 s123 para | 凑齐 d000 两个 seed |
| P1 | 0.5B d100 s42 para | d100 vs d000 的 ConStat gap |
| P1 | 0.5B d005 s42 para | d005 vs d000 的 ConStat gap |
| P2 | 1.5B/3B 同理 | 跨模型尺寸对比 |

**串并行关系**：
- Paraphrase eval 与其他信号计算（S1 IRT、S2 membership inference）**完全独立**，可并行
- 但 ConStat 信号计算依赖 paraphrase eval 输出，必须**先完成 para eval，再跑 signal_constat.py**
- 不同 checkpoint 的 para eval 之间互相独立，如果有多 GPU 可并行

---
