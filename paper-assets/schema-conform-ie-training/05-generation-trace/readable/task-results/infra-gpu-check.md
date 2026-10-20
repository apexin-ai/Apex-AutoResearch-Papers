# infra gpu check

**schema conform ie training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu_check_20260513T231408_result.json`
- **Structured JSON:** [`f868837bcbc950def5ed.json`](../../sessions/f8/f868837bcbc950def5ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态报告

### GPU 0 (cuda:0)
- **型号**: NVIDIA RTX PRO 6000 Blackwell (98GB)
- **利用率**: 60%
- **显存**: 22,085 MiB / 97,887 MiB (22.6%)
- **温度/功耗**: 47°C, 232W/600W
- **进程**: PID 118930 — eval 进程正在运行：
  ```
  python -m src.evaluate \
    --model_path /root/autodl-tmp/output/formal_A_continued/merged \
    --data_dir /root/autodl-tmp/data \
    --eval_datasets scierc_test crossner_politics crossner_science \
    --output_dir /root/autodl-tmp/output/eval_A_continued_final \
    --max_new_tokens 1024
  ```
  已运行约 31 分钟，CPU 占用 100%。通过 tmux session `train_a_continued` 中的脚本 `/tmp/run_eval_a_continued.sh` 启动。

### GPU 1 (cuda:1)
- **利用率**: 0%
- **显存**: 0 MiB / 97,887 MiB
- **温度/功耗**: 30°C, 36W/600W
- **进程**: 无

**cuda:1 完全空闲，可用。**

---
