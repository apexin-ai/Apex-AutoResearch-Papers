# status loop6 check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_loop6-check_20260515T011131_result.json`
- **Structured JSON:** [`cdb6d485d765edb7854f.json`](../../sessions/cd/cdb6d485d765edb7854f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器状态汇报

### GPU 占用

| GPU | 进程 | 显存 | 利用率 |
|-----|------|------|--------|
| GPU 0 | GRPO trainer (pid 90085) — `grpo-s3-ced-lr5e6-r1` | 13.6G / 32.6G | 58% |
| GPU 1 | RSFT generate (pid 122149) — `rsft_generate` | 23.2G / 32.6G | 88% |
| GPU 2 | **空闲** | 0 / 32.6G | 0% |
| GPU 3 | Eval ckpt-100 (pid 117640) — `inference ckpt-100` | 11.2G / 32.6G | 82% |

另有 `rsft_ced_analysis.py` (pid 126986) 在 CPU 上运行。

### RSFT Generate 进度

- **运行中**，113/1514 batches（~7%），已跑 ~1 小时
- 平均 ~33s/batch，预计还需 **~13 小时**
- 已生成 **1824 行** JSONL（17.5MB），覆盖 ~228 个 doc（progress.json 有 228 个 completed_doc_ids）
- 每 100 docs 输出一次 monitor 日志：format_ok_rate 99.8%，truncation_rate 9.9%，mean_diversity 1.0/8

**输出格式**（generations.jsonl 每行）：
```
{doc_id, generation_idx, prompt, output, raw_text, format_ok, truncated, gold_triples, sents}
```
每个 doc 生成 8 个候选（num_generations=8），batch_size=2。

### Eval ckpt-100 进度

- **运行中**，57/62 batches（~92%），还剩 5 个 batch
- 预计 **~8 分钟后完成**
- 输出目录 `/root/autodl-tmp/eval_results/lr5e6_r1_ckpt100/checkpoint-100/` **目前为空**（结果应在推理全部完成后写入）

### NLI 模型

**已下载**，路径：`/root/autodl-tmp/.hf_cache/hub/models--cross-encoder--nli-deberta-v3-base/`，包含 blobs/refs/snapshots。

### RSFT 代码输入输出格式

**rsft_score_filter.py**（Step 2: 打分+筛选）：
- **输入**：`generations.jsonl`（rsft_generate 的输出）
- **输出**：
  - `rsft_train.json` — 筛选后的 SFT 训练数据
  - `rsft_scores.jsonl` — 带分数的完整记录
  - `rsft_report.json` — 统计报告
- 计算 3 种奖励：format_reward、f1_reward、ced_reward
- 策略：top_pct 25%

**rsft_trainer.py**（Step 3: 训练）：
- **输入**：JSONL，每行 `{doc_id, input, output, ced_score, ...}`
- **输出**：QLoRA adapter checkpoint
- 基于 `input` 和 `output` 字段构建 chat template，用 SFTTrainer 训练

**格式差异**：rsft_generate 输出的字段是 `prompt` + `output`，而 rsft_trainer 期望的是 `input` + `output`。rsft_score_filter 负责做这个字段转换。

---
