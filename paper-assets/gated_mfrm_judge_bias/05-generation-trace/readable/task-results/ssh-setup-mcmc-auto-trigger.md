# ssh setup mcmc auto trigger

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_setup-mcmc-auto-trigger_20260524T180838_result.json`
- **Structured JSON:** [`7017fbc86d4cd9cf328f.json`](../../sessions/70/7017fbc86d4cd9cf328f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

监控脚本正在运行（PID 605265）。

---

**汇报：**

| 项目 | 状态 |
|------|------|
| **Sonnet/Gemini 进程** | 已停，无残留 |
| **活跃采集进程** | Qwen local (584197) ETA ~43min, Qwen3 (592432) ETA ~154min, DeepSeek (592328) ETA ~507min |
| **Judge 行数** | `data/arena_hard/` 下目前只有 prompts.jsonl(500) 和 question.jsonl(500)；judge 输出在 `exp001/results/*/arena_hard_judgments.jsonl` |
| **GPU 0** | 空闲（0 MiB），GPU 2,3 被 vLLM 占用 |
| **auto_mcmc_phase1.sh** | PID 605265，日志 `/root/gated_mfrm_judge_bias/logs/auto_mcmc_phase1.log`，已确认正在轮询 |
| **MCMC 启动命令** | `CUDA_VISIBLE_DEVICES=0 python run_mcmc_n17_exp020.py --output-dir /root/gated_mfrm_judge_bias/exp003/output_n17_phase1` |

**注意**：DeepSeek (PID 592328) 也在采集中（ETA ~8.4h），但不在监控脚本的触发条件里。如需也等 DeepSeek 完成再触发 MCMC，需更新脚本。

---
