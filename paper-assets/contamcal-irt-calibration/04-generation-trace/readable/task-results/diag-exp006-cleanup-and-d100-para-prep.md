# diag exp006 cleanup and d100 para prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp006_cleanup_and_d100_para_prep_20260514T151047_result.json`
- **Structured JSON:** [`07e9232771fb91954d28.json`](../../sessions/07/07e9232771fb91954d28.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## Part 1: exp_006 目录状态

`/root/autodl-tmp/exp006/results_05B/` **几乎为空**：
- 仅有一个空的 `mmlu/` 子目录（0 个文件）
- 没有任何结果文件

**日志分析**（`exp006_irt_05B.log` 最后 50 行）：
- Stan NUTS IRT fitting 启动成功，开始拟合 mmlu（9 models × 14042 items，4 chains × 1000 samples）
- 进程在 warmup 阶段被 killed：chain 3 完成 ~10% warmup，chain 4 完成 ~5% warmup
- chain 3 的 100 步 warmup 耗时约 27 分钟，说明 14042 items 的规模导致每步极慢（~16s/it）
- **结论：没有产出任何结果，需要从头重跑**

## Part 2: d100 paraphrase eval 脚本

**evaluate.py 参数**（实际参数名与任务描述有差异）：

| 参数 | 说明 |
|------|------|
| `--model-path` | 基础模型路径（required） |
| `--adapter-path` | LoRA adapter 路径 |
| `--benchmarks` | 评测基准列表（nargs="+"） |
| `--paraphrase-dir` | paraphrase JSON 目录（**非 `--paraphrase`**） |
| `--output-dir` | 输出目录（required） |
| `--mc-format` | MC 格式，default="aligned" |
| `--batch-size` | default=8 |
| `--max-samples` | 采样上限 |
| `--cache-dir` | default="/root/autodl-tmp/.hf_cache" |

**Paraphrase 数据已确认存在**：`/root/autodl-tmp/exp001/paraphrases/`
- `mmlu_paraphrases.json`
- `gsm8k_paraphrases.json`
- `arc_challenge_paraphrases.json`
- `humaneval_paraphrases.json`

**脚本已写入**：`/root/contamcal-irt-calibration/exp001/run_d100_para_eval.sh`（已 chmod +x）

PID 389866 d100 original eval 完成后，直接执行：
```bash
bash /root/contamcal-irt-calibration/exp001/run_d100_para_eval.sh
```

---
