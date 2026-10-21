# code gemma2 check and launch

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gemma2_check_and_launch_20260522T162859_result.json`
- **Structured JSON:** [`b57dd9bb41c9473d96c4.json`](../../sessions/b5/b57dd9bb41c9473d96c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Full run 已启动并运行正常：

- **tmux session**: `gemma2_full` 已创建
- **模型加载中**: Gemma-2-9B-it 正在加载权重（~44%）
- **Skip existing**: 已识别 5 个 dry-run trace，将跳过，继续生成剩余 515 个
- **Phase**: `both`（生成 + 分析）

监控命令：
```bash
# 查进度
ssh_read_only: tail -20 /tmp/gemma2_full.log
# 查 trace 数量
ssh_read_only: ls /root/autodl-tmp/contrastive_trace_safety/artifacts/advbench_traces_gemma2/
```

---
