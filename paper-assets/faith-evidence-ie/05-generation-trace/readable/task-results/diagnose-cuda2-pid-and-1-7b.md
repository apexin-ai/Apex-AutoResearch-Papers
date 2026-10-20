# diagnose cuda2 pid and 1 7b

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cuda2-pid-and-1_7b_20260522T020257_result.json`
- **Structured JSON:** [`fd5184da70ed1e8e31be.json`](../../sessions/fd/fd5184da70ed1e8e31be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

纠正：`21:15` 是 21 分 15 秒，不是 21 小时。8B no_evi 刚启动不久。

## PID 152873 身份
- 进程: `test_eval_8b_sft_s42_no_evi` — Qwen3-8B SFT, `--no_evidence`, test_revised split, seed 42
- 进度: 46/500 (9%), ~32s/it, 预计 ~4h 完成
- 有价值: ✅ （8B SFT no-evidence test eval，参数正确含 `--no_evidence`）
- Registry: 已推进到 RUNNING

## 1.7B SFT Test (`test_eval_1_7b_sft_s42`, PID 140534)
- 状态: **RUNNING**（3h14m，无 `--no_evidence`，即 with-evidence 版本）
- Output dir 为空，无 log 文件（脚本可能只在结束时写入，或日志去了 tmux stdout）
- 估算进度: ~430/500 based on ~27s/doc，预计 ~30min 内完成
- Registry: **不存在**，无 log_path

## 完整 GPU 占用

| PID | GPU | VRAM | Eval ID | Model | 运行时间 | --no_evidence |
|-----|-----|------|---------|-------|---------|------|
| 140534 | cuda:0 | 6 GB | test_eval_1_7b_sft_s42 | 1.7B | 3h14m | ❌ |
| 147596 | cuda:1 | 6 GB | test_eval_1_7b_sft_s42_no_evi | 1.7B | 1h47m (244/500) | ✅ |
| 152873 | cuda:2 | 19.6 GB | test_eval_8b_sft_s42_no_evi | 8B | 21min (46/500) | ✅ |
| 143166 | cuda:3 | 32.5 GB | test_eval_14b_sft_s42_no_evi | 14B | 2h50m | ✅ |

4 个 GPU 全满，均为有效 eval 任务。1.7B SFT test (with evidence) 最快完成，完成后需要更新 registry 和收集 metrics。

---
