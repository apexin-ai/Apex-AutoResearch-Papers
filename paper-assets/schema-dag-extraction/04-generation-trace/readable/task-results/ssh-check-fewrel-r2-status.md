# ssh check fewrel r2 status

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-fewrel-r2-status_20260515T165333_result.json`
- **Structured JSON:** [`a04c2de8e8449d00047d.json`](../../sessions/a0/a04c2de8e8449d00047d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 进程状态
- **PID 299625: DEAD**
- tmux sessions: 无法通过 ssh_read_only 查询（命令被屏蔽）
- GPU 使用: 无（无进程占用 GPU）

## 日志
最后输出显示 **两次连续崩溃**，都是 vLLM 初始化失败：

1. **第一次**：主进程直接调 `LLM()` 加载 Qwen3-32B-FP8 → vLLM EngineCore 初始化失败 → `RuntimeError: Engine core initialization failed`
2. **第二次**：主进程 fallback 到 subprocess 调自己 `--stage extract` → 子进程同样在 vLLM 初始化阶段被 **SIGKILL (9)** 杀掉

**根因**：加载 Qwen3-32B-FP8 时，模型 checkpoint 32GB + vLLM KV cache (`gpu_memory_utilization=0.95`) 超出单卡显存。EngineCore 子进程在加载 safetensors shard 1/7 (14%) 时就被 OOM Killer 杀了（SIGKILL）。

## 脚本路径确认
- `scripts/run_fewrel_40rel.sh`: **存在** (624 bytes)
- `run_fewrel_40rel.py`: **不存在**
- `src/run_fewrel_40rel.py`: **存在** (16904 bytes)

## 结论

实验已崩溃，原因是 **Qwen3-32B-FP8 在单卡上 OOM**。需要：
- 降低 `gpu_memory_utilization`（但 32B FP8 模型本身就需要 ~32GB，单张 A6000 48GB 勉强够，KV cache 空间不足）
- 或改用更小模型 / 降低 `max_model_len`（当前 4096）
- 或使用多卡 tensor parallel

---
