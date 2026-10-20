# emergency westd16639 kill polluted

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_emergency_westd16639-kill-polluted_20260518T161516_result.json`
- **Structured JSON:** [`e39cf2f88755a86582c6.json`](../../sessions/e3/e39cf2f88755a86582c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集。有一个重要问题需要报告。

## 诊断报告

### 1. Kill 结果

| 实验 | 进程 | 状态 |
|------|------|------|
| exp-032 | PID 16922 (run_full_mvp) + SCREEN 15925 | 首轮 pkill 已 kill |
| exp-033 | PID 21125, 20113, 20110, 20109 | 二轮 kill -9 已 kill |
| vLLM :8000 | 已在 00:05:54 自行崩溃 | 无需 kill（进程已不存在） |
| vLLM :8001 | 同上，已崩溃 | 无需 kill |

**⚠️ 副作用：kill PID 20109（exp033 tmux）时，该 PID 是 tmux server（最先创建的 session），导致所有 tmux session 被终止，exp-034 和 exp-035 也被连带 kill。** nvidia-smi 确认 4 张 GPU 均已清空（0 MiB），无任何 GPU 进程。

### 2. 被污染文件 + 备份

| 文件 | 备份路径 |
|------|----------|
| `results/exp032_qwen25_14b_pw600/exp032_results.json` | `.polluted.bak` ✓ 已备份并删除 |
| `results/qwen3_14b_pw600_nonthinking/exp033_results.json` | `.polluted.bak` ✓ 已备份并删除 |

### 3. Intermediates（有效数据，可 resume）

| 实验 | 有效 intermediates | 总题数 | 可 resume |
|------|-------------------|--------|-----------|
| exp-032 (Qwen2.5-14B, PW600) | 509 个 JSON | 600 | 剩余 ~91 题 |
| exp-033 (Qwen3-14B, PW600, no-thinking) | 518 个 JSON | 600 | 剩余 ~82 题 |

intermediates 结构为 `{problem, sica_result}`，是 vLLM 崩溃前的有效推理结果。

### 4. 崩溃根因

**vLLM EngineCore 崩溃（非 OOM）。** dmesg 无 OOM 记录。

vLLM :8000 日志关键信息：
```
(EngineCore pid=16369) Shutdown initiated (timeout=0)
(EngineCore pid=16369) Aborting 1 requests
vllm.v1.engine.exceptions.EngineDeadError: EngineCore encountered an issue
```
崩溃时间：00:05:54。之后 vLLM 返回 500，实验脚本持续无限重试（每秒几次），写入的结果为垃圾数据。vLLM :8001 应有类似崩溃。

### 5. GPU 当前状态

| GPU | 型号 | 显存使用 | 温度 | 状态 |
|-----|------|----------|------|------|
| 0 | RTX PRO 6000 Blackwell 97GB | 0 MiB | 26°C | **空闲** |
| 1 | RTX PRO 6000 Blackwell 97GB | 0 MiB | 28°C | **空闲** |
| 2 | RTX PRO 6000 Blackwell 97GB | 0 MiB | 37°C | **空闲** |
| 3 | RTX PRO 6000 Blackwell 97GB | 0 MiB | 50°C | **空闲** |

系统内存：42Gi used / 1.0Ti total。

### 6. exp-035 状态

**❌ 已被意外终止。** kill exp-033 tmux PID 时连带杀死了 tmux server，exp-035 (ARC-60, port 8003) 和 exp-034 (StrategyQA-200, port 8002) 均被终止。需要重启。

---
