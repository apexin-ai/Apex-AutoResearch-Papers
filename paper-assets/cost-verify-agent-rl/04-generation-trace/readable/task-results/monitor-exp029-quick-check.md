# monitor exp029 quick check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp029_quick_check_20260516T201037_result.json`
- **Structured JSON:** [`205e6644f1e588e4db77.json`](../../sessions/20/205e6644f1e588e4db77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

```
DEAD
---GPU---
0 %, 0 MiB
0 %, 0 MiB
---LOG---
usage: train.py [--help] [--hydra-help] [--version] [--cfg {job,hydra,all}]
                [--resolve] [--package PACKAGE] [--run] [--multirun]
                [--shell-completion] [--config-path CONFIG_PATH]
                [--config-name CONFIG_NAME] [--config-dir CONFIG_DIR]
                [--experimental-rerun EXPERIMENTAL_RERUN]
                [--info [{all,config,defaults,defaults-tree,plugins,searchpath}]]
                [overrides ...]
train.py: error: ambiguous option: --config could match --config-path, --config-name, --config-dir
WARNING: kimina-client is not installed or failed to import. Lean environments will not be loaded.
EXIT_CODE=2
```

PID 901567 已死亡。两块 GPU 空闲（0% 利用率，0 MiB 显存）。日志显示 exp029 因 Hydra 参数解析错误退出（`--config` 有歧义，需改为 `--config-name` 或 `--config-path`），exit code 2。

---
