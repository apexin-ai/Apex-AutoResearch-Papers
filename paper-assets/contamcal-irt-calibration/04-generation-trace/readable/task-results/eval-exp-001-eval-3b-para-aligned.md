# eval exp 001 eval 3B para aligned

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp_001_eval_3B_para_aligned_20260514T161451_result.json`
- **Structured JSON:** [`68b62dd4b86192428ced.json`](../../sessions/68/68b62dd4b86192428ced.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前 0.5B d025 eval 正在跑 GSM8K（29%, 386/1319），约5s/item，GSM8K 还需 ~79分钟，之后还有 ARC 和 HumanEval。预计 cuda:3 还需 2-3 小时才空闲。

**cuda:5 完全空闲（0MiB, 0%）**，可以改用 cuda:5 提交 3B paraphrase eval。是否改用 cuda:5？

同时已确认：
- `evaluate.py` 位于 `/root/contamcal-irt-calibration/exp001/evaluate.py`
- paraphrase 参数是 `--paraphrase-dir /root/autodl-tmp/exp001/paraphrases/`
- paraphrase 数据完整（mmlu, gsm8k, arc_challenge, humaneval 四个 json 文件都在）

---
