# code phase b readiness

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase-b-readiness_20260514T043410_result.json`
- **Structured JSON:** [`c36cc3417c7f74702aa1.json`](../../sessions/c3/c36cc3417c7f74702aa1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审查完成。核心结论：

**B-IAVR 代码就绪**，61/61 测试通过，4 个核心模块 + 3 处集成点（agent_proxy、ctx_manager、agent_trainer）全部到位。

**启动前需处理 3 件事**：
1. **FSDP→HF 转换**：exp010 checkpoint 是 FSDP 分片格式，Phase B 的 `model_path` 需要 HuggingFace 格式。用 `FSDPModelMerger` 转换。
2. **更新 `_alfworld_phase_b.yaml`**：`model_path`（当前 `TO_BE_SET`）、`experiment_name`（当前指向 exp003）、`local_log_dir`（当前指向 exp_003 目录）。
3. **exp010 尚未产出 checkpoint**（目录不存在），需等待训练完成。

**注意风险**：Phase B config 的 `max_model_len: 32768` 比 exp008 的 `8192` 大 4 倍，需确认 vLLM 在 `gpu_memory_utilization: 0.4` 下能容纳。

---
