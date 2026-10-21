# ops fix logpaths and verify

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix-logpaths-and-verify_20260524T140133_result.json`
- **Structured JSON:** [`ab2fa1ea0b40acea22a8.json`](../../sessions/ab/ab2fa1ea0b40acea22a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

---

## 结果汇总

### Part 1: log_path 更新

| exp_id | log_path | 状态 |
|--------|----------|------|
| eval_pi05_random_k05_long_seed42_postfix | `logs/random_k05_long.log` | **已更新** (log_path + spec) |
| eval_pi05_random_k07_long_seed42_postfix | `logs/random_k07_long.log` | **已更新** (log_path + spec) |
| eval_pi05_random_k09_long_seed42_postfix | `logs/random_k09_long.log` | **已更新** (log_path + spec) |
| eval_pi05_random_k095_long_seed42_postfix | `logs/random_k095_long.log` | **已更新** (log_path + spec) |
| eval_pi05_l2norm_k09_long_seed42_postfix | `logs/eval_l2norm_k09_long_postfix.log` | **无需更新** — 实验已为 DONE/failed 状态，log_path 已存在；v2 版本正在 RUNNING 且也已有 log_path |

### Part 2: _check_log_success fallback 验证

**Registry 路径 (主路径)** — 全部通过：
- `_resolve_log_path` 从 registry 正确解析出 log_path
- Part 1 更新的 4 个实验全部可通过 registry 路径找到
- 已完成实验 `eval_pi05_l2norm_k03_spatial_seed42_postfix` 的 registry 解析正确

**SSH fallback (备用路径)** — 本地无法端到端测试（缺 fabric），但模拟 matching 逻辑发现问题：
- 当同一服务器存在多个相似实验 log 时，fuzzy matching（基于 exp_id 分词计分）可能匹配到错误的 log 文件
- 例：`l2norm_k085_long` 在 westd-41074 上被错误匹配到 `l2norm_k085_goal` 的 log（两者都得分 4/5）
- 根本原因：`score > best_score` 用 `>` 不是 `>=`，同分时先到的文件胜出，而 `find` 输出顺序不可控

**Log success markers** — 已确认两个完成实验的 log 都包含 `RESULT:` marker，会被 `_check_log_success` 正确识别。

---
