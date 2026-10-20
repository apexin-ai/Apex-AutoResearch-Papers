# exp critical fix and restart

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_critical-fix-and-restart_20260512T131249_result.json`
- **Structured JSON:** [`80650a9faccd0876e880.json`](../../sessions/80/80650a9faccd0876e880.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成，汇报如下：

## 产出

1. **behavioral_fingerprint.py 部署验证**：`grep -c "MODAL_REQUEST"` = 2，`_is_modal_request` = 2。Bug 1 修复已部署。

2. **vLLM max_model_len**：**32768**（成功，无需 fallback）。运行在 GPU 1（GPU 2 被其他进程占满，改用空闲 GPU 1）。

3. **run_mvp_experiment.py context overflow 处理修改**：
   - 新增 `_is_context_overflow(result)`: 检查 result.info 是否含 `ContextWindowExceededError` 或 `context_length_exceeded`
   - 新增 `filter_context_overflow(results, label)`: 过滤掉 overflow 的 task，返回 `(valid_results, skipped_count)`，并对每个跳过的 task 打 warning 日志
   - Phase 1 (baseline) 和 Phase 2 (variants) 在 `run_tau_bench_experiment` 返回后、计算 completion rate 前调用 filter，H3 的 `task_completion_rate = successful / (total - skipped)`
   - 额外修复：`PROMPTS_DIR_DEFAULT` 路径修正（`SCRIPT_DIR / "prompts"` → 正确指向 `/root/democalib/prompts`）、添加 CLI 别名 `--num-tasks`/`--gpu-id`/`--port`/`--log-dir`

4. **实验新 PID**：**107949**

5. **部署文件验证**：
   - `behavioral_fingerprint.py` — 300 lines
   - `h_gate_evaluator.py` — 201 lines
   - `prompt_loader.py` — 131 lines
   - `run_mvp_experiment.py` — 514 lines
   - `prompts/base_user_simulator.txt`, `bcp_user_simulator.txt`, `bcp_variants.yaml` — 全部就位
   - 实验已在运行，LiteLLM 正常向 vLLM 发请求

---
