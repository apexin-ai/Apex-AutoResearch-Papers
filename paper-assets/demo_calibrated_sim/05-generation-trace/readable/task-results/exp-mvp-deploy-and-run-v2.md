# exp mvp deploy and run v2

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_mvp-deploy-and-run-v2_20260512T111221_result.json`
- **Structured JSON:** [`d9b1ee352e96687b5574.json`](../../sessions/d9/d9b1ee352e96687b5574.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整 20-task 实验已成功启动。

## 汇报

### 1. 文件部署状态
全部 7 个文件部署成功：
- `code/run_mvp_experiment.py` (含修复：`--enable-auto-tool-choice --tool-call-parser hermes` + `max_model_len=16384`)
- `code/h_gate_evaluator.py`
- `code/behavioral_fingerprint.py`
- `prompts/base_user_simulator.txt`
- `prompts/bcp_user_simulator.txt`
- `prompts/bcp_variants.yaml`
- `prompts/prompt_loader.py`

### 2. 验证清单（6/6 PASS）
| 检查项 | 结果 |
|--------|------|
| 2a. `###STOP###` in prompts | PASS |
| 2b. indian_english_target rates (q=10, p=20) | PASS |
| 2c. `RunConfig` 用法 | PASS |
| 2d. `patched_build_system_prompt(self, instruction=None)` | PASS |
| 2e. `--help` dry-run (含 `--end-index`) | PASS |
| 2f. `###STOP###` in prompt_loader | PASS |

### 3. 3-task 快速验证结果：成功
- Baseline: question_rate=0.650, politeness_rate=0.450, completion=33%
- aave_target: question_rate=0.739, politeness_rate=0.656, completion=0%
- H1=PASS, H2=FAIL, H3=FAIL（预期：小样本 + 7B 模型）
- **无崩溃，框架完整跑通**

### 4. 完整实验
- **PID**: 75855
- **日志**: `/root/democalib/results/full_experiment.log`
- **配置**: 20 tasks, 所有 5 variants, dev split
- 预计运行时间：2-3 小时（20 tasks × 6 runs × ~3 min/task）

### 部署中修复的 2 个问题
1. vLLM 缺少 `--enable-auto-tool-choice --tool-call-parser hermes`（τ-Bench agent 需要 tool calling）
2. `max_model_len` 从 4096 增大到 16384（τ-Bench 的 tool definitions + 多轮对话超出 4096 上下文）

---
