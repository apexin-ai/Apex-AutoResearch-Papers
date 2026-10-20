# ssh westd olmo final check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-olmo-final-check_20260519T122739_result.json`
- **Structured JSON:** [`d567c2ac4cd3127db9b5.json`](../../sessions/d5/d567c2ac4cd3127db9b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. OLMo-2 完成状况

| Dosage | Status | 备注 |
|--------|--------|------|
| d000 | **DONE** | |
| d005 | **RUNNING** | GPU 0, MMLU 已完成，ARC 进行中 |
| d025 | **DONE** | |
| d050 | **RUNNING** | **⚠️ C001 违规：2 个进程写同一 output dir** |
| d100 | **DONE** | |

**d050 重复进程问题：**
- PID 169634 (GPU 3, started 20:23, 运行 ~5min)
- PID 170801 (GPU 1, started 20:27, 运行 ~1min)
- 两个进程都写入 `olmo2_d050/`，会导致数据污染。需要 kill 一个（建议 kill 较晚的 PID 170801，保留 169634）。

### 2. OLMo-2 已完成结果

| Dosage | MMLU | ARC |
|--------|------|-----|
| d000 | 0.5379 | 0.7611 |
| d025 | 0.5617 | 0.7816 |
| d100 | 0.5700 | 0.8003 |

### 3. 完整 5×5 表

| Family | d000 MMLU/ARC | d005 MMLU/ARC | d025 MMLU/ARC | d050 MMLU/ARC | d100 MMLU/ARC |
|--------|---------------|---------------|---------------|---------------|---------------|
| gemma2 | .6186/.8601 | .6342/.7782 | .6456/.8737 | .6401/.7108 | .6562/.8481 |
| phi4 | .7644/.9206 | .7636/.9181 | .7698/.9232 | .7675/.9241 | .7627/.9266 |
| qwen14b | .6944/.9104 | .6901/.9036 | .6204/.8891 | .5941/.8763 | .6007/.8848 |
| qwen7b | .6611/.8788 | .6474/.8609 | .6298/.8404 | .6307/.8456 | .6433/.8498 |
| olmo2 | .5379/.7611 | RUNNING | .5617/.7816 | RUNNING | .5700/.8003 |

23/25 完成，剩余 olmo2_d005 和 olmo2_d050。

### 4. 待处理

- **紧急**：olmo2_d050 的重复进程需要处理。建议 kill PID 170801（后启动的），清空 output dir，让 PID 169634 独占完成。或 kill 两个都重跑。是否执行？
- 所有 OLMo-2 adapter 确认 lora_alpha=32（C006 合规）。
- 模型路径：`/root/autodl-tmp/models/OLMo-2-1124-7B`，adapter 路径：`/root/autodl-tmp/exp001/checkpoints/OLMo-2-7B_d{dose}_s42/lora_adapter`

---
