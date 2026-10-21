# code exp scripts prep

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_scripts_prep_20260516T052628_result.json`
- **Structured JSON:** [`ce46982a96964cb3419e.json`](../../sessions/ce/ce46982a96964cb3419e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部脚本已部署。汇总：

### 产出文件

| 文件 | 用途 |
|------|------|
| `scripts/run_k_ablation.py` (329行) | K sensitivity 主脚本，CachedGenerator 复用 pipeline |
| `scripts/start_vllm_7b.sh` | 启动 7B vLLM (含 AutoDL 环境配置) |
| `scripts/start_vllm_72b_awq.sh` | 启动 72B-AWQ vLLM (含 `--quantization awq`) |
| `scripts/README_experiments.md` | 每个实验的运行步骤 |
| `data/empty.json` | 空 JSON `[]`，用于跳过 MATH 数据 |

### run_k_ablation.py 设计要点

- **CachedGenerator** 继承 `TraceGenerator`，从缓存中返回前 K 条 traces，直接接入 `SICAPipeline`，复用全部 pipeline 逻辑（answer assertion injection、mutual exclusion hard constraints、scoring），无需重新实现
- 两阶段：Phase 1 生成 K_max=20 traces 并持久化（带 checkpoint），Phase 2 对每个 K 子采样+评估
- `--resume` 跳过 trace 生成直接评估

### 发现的潜在问题

1. **`run_full_mvp.py` 的 `--math-data` 是必需的**：`load_all_problems` 在文件不存在时 `sys.exit(1)`，即使只跑 logic 任务也不能省略。已创建 `data/empty.json` 解决。
2. **D012 未保存 trace 原文**：`--save-intermediates` 只保存 `per_trace` 元数据（trace_len, answer），不含 trace text。因此 K=6,8 无法从已有结果 subsample，必须重新生成 traces。K ablation 脚本统一生成 K=20 traces 再子采样，保证一致性。
3. **72B-AWQ 内存**：AWQ 4-bit weights ~36GB + KV cache (8192 tokens)，98GB 卡够用，但如果生成长 traces (>4096 tokens) 可能需要降低 `--max-model-len`。

---
