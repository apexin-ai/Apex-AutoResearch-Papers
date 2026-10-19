# fix gsweep g100 adv log

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_gsweep-g100-adv-log_20260517T162918_result.json`
- **Structured JSON:** [`049f3057940ee97914cc.json`](../../sessions/04/049f3057940ee97914cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两件事都搞定了，watchdog 和 g050 均未受影响。

**总结：**

1. **脚本on-disk已修改** — `gsweep_watchdog.sh` 中 g100 启动前加了 `export LOG_PER_SAMPLE_ADV=1`（条件判断 `$g = "100"`）

2. **运行中的实例** — bash 的 for 循环已在内存中（fd offset 1302/1426 确认），磁盘修改不会被当前进程读到。解决方案：创建了 `/root/miniconda3/lib/python3.12/site-packages/sitecustomize.py`，在 Python 启动时检查 `sys.argv` 是否包含 `g100`，若是则自动设置 `LOG_PER_SAMPLE_ADV=1`。

3. **验证** — g080 config 不触发（`NOT SET`），g100 config 正确触发（`1`）。

**注意事项：** g100 训练完成后建议删除 `sitecustomize.py`，避免影响其他 Python 进程：
```bash
rm /root/miniconda3/lib/python3.12/site-packages/sitecustomize.py
```

---
