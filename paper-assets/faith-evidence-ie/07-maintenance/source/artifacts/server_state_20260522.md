# rtx5090-4x 服务器状态报告 (2026-05-22 09:38 UTC)

## GPU 占用

| GPU | 显存占用 | GPU-Util | PID | 实验名 |
|-----|---------|----------|-----|--------|
| 0 | 6071 / 97887 MiB | 50% | 140534 | test_eval_1_7b_sft_s42 (with_evi) |
| 1 | 6071 / 97887 MiB | 51% | 147596 | test_eval_1_7b_sft_s42_no_evi |
| 2 | 0 / 97887 MiB | 0% | — | **空闲** |
| 3 | 32503 / 97887 MiB | 91% | 143166 | test_eval_14b_sft_s42_no_evi |

## 仍在运行的实验

| PID | 实验名 | GPU | 运行时长 | 进度 | 预计剩余 |
|-----|--------|-----|---------|------|---------|
| 140534 | test_eval_1_7b_sft_s42 | 0 | 2h47m | 未知(输出目录为空) | ~1h（参照 no_evi 速度） |
| 147596 | test_eval_1_7b_sft_s42_no_evi | 1 | 1h20m | 185/500 (37%) | ~2h21m |
| 143166 | test_eval_14b_sft_s42_no_evi | 3 | 2h23m | 221/500 (44%) | ~3-4h |

## 已完成的 test_eval（有 test_summary.json）

| 实验名 | F1 | ign_F1 | evi_F1 | EDCR |
|--------|-----|--------|--------|------|
| test_eval_14b_sft_s42 | 0.3886 | 0.3886 | 0.5912 | 0.8367 |
| test_eval_14b_rsft_s42 | 0.3849 | 0.3849 | 0.6025 | 0.7865 |
| test_eval_llama_rsft_s42 | 0.3599 | 0.3599 | 0.5447 | 0.8391 |
| test_eval_llama_sft_s42 | 0.3420 | 0.3420 | 0.5819 | 0.8403 |
| test_eval_8b_rsft_s42 | 0.3353 | 0.3353 | 0.6037 | 0.7993 |
| test_eval_8b_sft_s42 | 0.3106 | 0.3106 | 0.5949 | 0.8432 |
| test_eval_1_7b_rsft_s42 | 0.2933 | 0.2933 | 0.6196 | 0.8169 |
| test_eval_4b_rsft_s42_v2 | 0.2501 | 0.2501 | 0.6237 | 0.8288 |
| test_eval_4b_sft_s42 | 0.2232 | 0.2232 | 0.6121 | 0.8652 |

## 未完成 / 失败的 test_eval

| 目录 | 状态 | 说明 |
|------|------|------|
| test_eval_1_7b_sft_s42 | 运行中 | PID 140534，输出目录为空，仍在推理 |
| test_eval_1_7b_sft_s42_no_evi | 运行中 | PID 147596，有 log.txt，37% 进度 |
| test_eval_14b_sft_s42_no_evi | 运行中 | PID 143166，输出目录为空，44% 进度 |
| test_eval_4b_rsft_s42 | 失败/未启动 | 空目录，PID 151217 已死 |

## 已死 PID（需清理 registry）

| PID | 实验名 | 完成状态 |
|-----|--------|---------|
| 87302 | d140_8b_sft_s42_no_evi_2048_fix | ✅ 已完成（有 metrics.json） |
| 87382 | d140_1_7b_sft_s42_no_evi_2048_fix | ✅ 已完成（有 metrics.json） |
| 88987 | d140_4b_sft_s42_no_evi_2048_fix | ✅ 已完成（有 metrics.json） |
| 93402 | d140_4b_sft_s42_with_evi_2048 | ✅ 已完成（有 metrics.json） |
| 95606 | eval_llama_rsft_s42_no_evi_2048 | ✅ 已完成（有 metrics.json） |
| 97434 | test_eval_14b_rsft_s42 | ✅ 已完成（有 test_summary.json） |
| 151217 | test_eval_4b_rsft_s42_v3 | ❌ 失败（output 目录 test_eval_4b_rsft_s42 为空） |

## 总结

- **3 个 eval 仍在运行**：1.7B SFT with_evi (GPU0)、1.7B SFT no_evi (GPU1)、14B SFT no_evi (GPU3)
- **GPU 2 空闲**，可用于新任务
- **7 个旧 PID 已死**，其中 6 个正常完成，1 个（test_eval_4b_rsft_s42_v3/PID 151217）失败需重跑
- **9 个 test_eval 已完成**，最高 F1 为 14B SFT (0.3886)，14B RSFT 紧随 (0.3849)
