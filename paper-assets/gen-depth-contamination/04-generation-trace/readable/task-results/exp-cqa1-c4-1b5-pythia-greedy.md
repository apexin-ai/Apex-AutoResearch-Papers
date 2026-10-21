# exp cqa1 c4 1b5 pythia greedy

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_cqa1-c4-1b5-pythia-greedy_20260519T230250_result.json`
- **Structured JSON:** [`6e72852effcc07183b6f.json`](../../sessions/6e/6e72852effcc07183b6f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已正常运行：

- **cuda:0**: 99% 利用率，19629 MiB 显存占用
- **cuda:1/2/3**: 不受影响，cross-transfer 继续运行
- **tmux session**: `deberta_c4_1b5_pythia`
- **日志**: `/root/autodl-tmp/gen-depth-contamination/logs/deberta_c4_1b5_pythia.log`
- **config**: pythia_greedy, 5-fold GroupKFold, 30000 samples (5000 docs x 6 depths)

第一次启动因 `transformers` 尝试在线查 adapter config 而崩溃（AutoDL 网络不通），加 `HF_HUB_OFFLINE=1` + `TRANSFORMERS_OFFLINE=1` 后解决。

---
