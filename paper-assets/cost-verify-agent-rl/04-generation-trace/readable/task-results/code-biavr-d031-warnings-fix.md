# code biavr d031 warnings fix

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_biavr_d031_warnings_fix_20260515T151905_result.json`
- **Structured JSON:** [`3d30a0b7624d5c515848.json`](../../sessions/3d/3d30a0b7624d5c515848.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 修复报告

### Warning 1: `&lt;VERIFY>` special token 注册

**问题**：tokenizer 会将 `&lt;VERIFY>` 拆成 ~8 个子 token（如 `<`, `V`, `ER`, `IF`, `Y`, `>`），模型需要学习产生精确的子 token 序列才能触发验证，显著增加学习难度。

**修复**：在 `verify_mechanism.py` 新增两个函数：
- `register_verify_special_token(tokenizer, model=None)` — Phase B 训练前调用，将 `&lt;VERIFY>` 注册为 special token 并 resize embedding。幂等（已注册则跳过）。
- `get_verify_token_id(tokenizer)` — 返回 token id，未注册时抛 RuntimeError 提示调用注册函数。

### Warning 2: `a_pre` 推理开销量化

**问题**：每次 verify step 额外一次 greedy decode 生成 `a_pre`，估计增加 15-30% 步耗时，需 dry run 量化。

**修复**：在 `pre_action.py` 新增 `PreActionProfiler` dataclass：
- `record_pre_action(latency_s)` / `record_main_action(latency_s)` — 记录每次调用耗时
- `overhead_ratio` — 自动计算 `a_pre` 占主 action 的比例
- `get_metrics()` — 返回 W&B 可直接 log 的指标 dict
- `summary()` — 人可读的单行摘要

Phase B 集成时在 rollout loop 中插桩 `time.time()` 调用 profiler，前 N 步即可得到开销数据。

### 修改文件
| 文件 | 变更 |
|------|------|
| `artifacts/biavr/verify_mechanism.py` | +`register_verify_special_token`, +`get_verify_token_id` |
| `artifacts/biavr/pre_action.py` | +`PreActionProfiler` dataclass |
| `artifacts/biavr/__init__.py` | 导出新增 API |
| `artifacts/biavr/tests/test_biavr.py` | +11 个新测试（W1: 5, W2: 6） |

全部测试通过。

---
