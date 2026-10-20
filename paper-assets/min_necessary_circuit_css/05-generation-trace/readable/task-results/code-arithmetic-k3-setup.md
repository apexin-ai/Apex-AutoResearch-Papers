# code arithmetic k3 setup

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_arithmetic-k3-setup_20260513T012815_result.json`
- **Structured JSON:** [`5ab11c6c551dafa3ac01.json`](../../sessions/5a/5ab11c6c551dafa3ac01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已注册并运行中。总结：

- **脚本**: `/root/min_necessary_circuit_css/run_arithmetic.py` — 已创建并通过 dry-run 验证
- **模型**: GPT-2 small 从 ModelScope 下载完成 (548MB)，加载正常
- **数据集**: Greaterthan 1000 prompts JSON，取 100 samples
- **运行状态**: ACDC 正在处理 32,491 edges (5 thresholds)，EAP-IG 和 EP 已完成并缓存
- **进程**: nohup PID 900223，日志 `/tmp/arithmetic.log`
- **Registry**: `mvp_arithmetic_gpt2_k3` 状态 RUNNING
- **预计总时长**: ~8h（ACDC 主导）

可用 `cat /tmp/arithmetic.log | tail -20` 查看进度。

---
