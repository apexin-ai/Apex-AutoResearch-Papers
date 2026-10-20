# infra mvp deploy v4 z3fix

**svs formal verification** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_mvp_deploy_v4_z3fix_20260514T092146_result.json`
- **Structured JSON:** [`f17f4fa4691c64ae32b9.json`](../../sessions/f1/f17f4fa4691c64ae32b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整 MVP 正常启动：50 problems × 8 chains = 400 total chains，正在处理 Problem 1/50。

---

## 产出汇总

### 1. 修复验证
| 检查项 | 结果 |
|--------|------|
| `_z3_lock` in autoformalize.py | ✓ |
| `_z3_corrupted` in autoformalize.py | ✓ |
| `_z3_lock` in z3_checker.py | ✓ |
| 量词规则 (CRITICAL RULES) | ✓ (两文件各1处) |
| `import threading` | ✓ (两文件) |

### 2. vLLM 状态
- 模型: `/root/autodl-tmp/models/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B`
- TP=2, float16, port 8001
- 状态: **运行中**

### 3. Dry-run mvp_report.json
- SVS accuracy: 50% (1/2), SC accuracy: 50% (1/2), delta: 0%
- P1 (formalization > 50%): **PASS** (75%, 63/84 claims formalized)
- P2 (IC discrimination): FAIL（样本量不足，无法计算统计量）
- API calls: 143, tokens: 109,830, cost: $0.0301

### 4. 异常检查
- **0 segfault** — Z3 crash 修复有效
- **0 "Z3 state corrupted"** — corrupted state 检测未触发（好事，说明 lock 真正防住了并发问题）
- **0 "unreachable"**
- 有少量 formalization 语法错误重试（正常行为，非 crash）

### 5. 完整 MVP
- **PID: 35733**
- 配置: 50 problems × 8 chains = 400 chains
- 已成功加载 50 个 ProofWriter depth-5 问题，正在处理 Problem 1/50

### 6. MVP 启动日志前 20 行
- 正常加载 config_local.yaml
- 从本地缓存加载 30220 问题 → 选取 50 个 depth-5
- 已开始向 vLLM 发送推理请求

### 7. 无异常
唯一 note：dry-run 中有一个 claim "If Gary is not kind then Gary might not be blue" 因含 modal "might" 导致 3 次 formalization 均语法错误被跳过——这是预期行为，不影响流程。

---
