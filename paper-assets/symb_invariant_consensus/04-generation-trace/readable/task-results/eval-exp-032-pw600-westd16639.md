# eval exp 032 pw600 westd16639

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp-032-pw600-westd16639_20260518T153636_result.json`
- **Structured JSON:** [`8746f995dc7442e3047b.json`](../../sessions/87/8746f995dc7442e3047b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已在运行中。

**状态汇总:**
- **服务器**: westd-16639, GPU 0 (RTX PRO 6000 Blackwell 98GB)
- **vLLM**: 46秒启动完成, PID 15937, GPU 占用 88233 MiB
- **SICA pipeline**: 已开始处理 600 个 ProofWriter 问题 (K=12, T=0.7, seed=42)
- **Screen session**: `exp032` (PID 15925), detached
- **进度**: 1/600 正在处理
- **日志**: `/tmp/exp032_screen.log`, `/tmp/vllm_exp032.log`
- **结果输出**: `results/exp032_qwen25_14b_pw600/exp032_results.json`
- **预计时间**: 2-4 小时

监控命令（通过 westd-25068 代理）:
```bash
ssh -p 16639 root@connect.westd.seetacloud.com "tail -5 /tmp/exp032_screen.log"
```

---
