# ssh training status and eval prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_training-status-and-eval-prep_20260520T101312_result.json`
- **Structured JSON:** [`b24896ff2c915fb6d2e3.json`](../../sessions/b2/b24896ff2c915fb6d2e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练状态汇总

| GPU | 任务 | 当前 step / 总 step | 进度 | 速度 | 预估剩余 | ETA |
|-----|------|---------------------|------|------|----------|-----|
| 0 | Qwen s123 | 1326 / 6633 | 20% | ~12.2s/it | ~18h | **5/21 ~12:30** |
| 1 | DeepSeek s456-v2 | 468 / 12627 | 3.7% | ~8.0s/it | ~27h | **5/21 ~21:30** |
| 2 | DeepSeek s123-v2 | 1965 / 12627 | 15.6% | ~8.2s/it | ~24.3h | **5/21 ~18:30** |
| 3 | Qwen s456 | 1365 / 6633 | 20.6% | ~11.9s/it | ~17.5h | **5/21 ~12:00** |

4 张 5090 全部满载（89-99% util, 72-75°C）。

## save_strategy 确认

- `save_strategy = "epoch"`（line 375），`save_total_limit = 2`（line 377）
- 只保留最后 2 个 epoch checkpoint
- DeepSeek 12627 total steps / 3 epochs → epoch checkpoint 约在 step 4209, 8418, 12627
- 参考 s42：checkpoint-8844 (epoch 2) + checkpoint-13266 (epoch 3/final)
- eval 脚本用 `sort -t'-' -k2 -n | tail -1` 自动取最大编号 checkpoint

## Eval 脚本已写入

- `/home/sonny/exec-sim-repair-verifier/eval_deepseek_cwm_s123_v2.sh` — GPU 2, `--batch_size 4 --max_seq_length 4096`
- `/home/sonny/exec-sim-repair-verifier/eval_deepseek_cwm_s456_v2.sh` — GPU 1, 同参数

两个脚本已 `chmod +x`，训练完成后直接执行即可。

---
