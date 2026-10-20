# diag temp urgent v5

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_temp-urgent-v5_20260518T192618_result.json`
- **Structured JSON:** [`e8840f9891af6bd031c7.json`](../../sessions/e8/e8840f9891af6bd031c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 全部温度实验状态汇总

### 数据生成进度

| 数据集 | Seeds | Lines | 状态 |
|--------|-------|-------|------|
| olmo-2-1b-t05 | 995 | 4,858 | **完成** |
| olmo-2-1b-t09 | 995 | 4,673 | **完成** |
| qwen3-0.6b-t05 | 996 | 4,714 | **完成** |
| qwen3-0.6b-t09 | 831 | 3,760 | **运行中 83%**，GPU 3 |

### GPU 状态

- GPU 0-2：空闲 (3 MiB)
- GPU 3：Qwen t=0.9 生成中 (1,827 MiB, 32% util)

### Pipeline 分类结果

| 文件 | Model | Temp | Binary F1 | 3-class F1 | 备注 |
|------|-------|------|-----------|------------|------|
| `temp_olmo-2-1b_t0.5_eval.json` | olmo-2-1b | 0.5 | **0.9844** | 0.8531 | 有 temperature 字段 |
| `temp_olmo-2-1b_t05_eval.json` | olmo-2-1b | 0.5 | 0.7826 | 0.8425 | 无 temperature 字段（可能重跑版） |
| `temp_olmo-2-1b_t09_eval.json` | olmo-2-1b | 0.9 | **0.4532** | 0.5631 | 03:01 刚完成 |
| `temp_qwen3-0.6b_t05_eval.json` | qwen3-0.6b | 0.5 | 0.7111 | 0.8019 | |
| `temp_qwen3-0.6b_t09_eval.json` | — | — | — | — | **待生成完后自动触发** |

### OLMo t=0.9 详细结果（03:01 完成）

- Binary F1: 0.4532, CI: [0.4371, 0.4693]
- 3-class F1: 0.5631, CI: [0.5493, 0.5765]
- Spearman rho: -0.2607 (p=1.93e-73)

### 关键发现

**温度越高，分类性能越低**——符合预期：
- OLMo t=0.5 binary F1: 0.98 → OLMo t=0.9 binary F1: 0.45（暴跌）
- 高温采样模糊了生成器指纹信号

### 当前状态

- **OLMo t=0.9 pipeline 已自动完成**，无需手动干预
- **Qwen t=0.9 还需 ~170 seeds**，按当前速度（~11 seeds/2min）预计约 **30 分钟后完成**
- Monitor 脚本正常运行，每 120s 轮询，到 990 seeds 会自动触发 pipeline
- 1 个 zombie 进程 (PID 27228)，是已完成的旧 OLMo 生成进程，无影响

### 注意

OLMo t=0.5 有两份结果文件（`t0.5` 和 `t05`），binary F1 差异很大（0.98 vs 0.78），需要确认哪份是最终有效结果。

---
