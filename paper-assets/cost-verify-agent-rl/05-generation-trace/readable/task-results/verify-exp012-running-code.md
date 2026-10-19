# verify exp012 running code

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_exp012-running-code_20260514T062944_result.json`
- **Structured JSON:** [`2f590146eb1330338009.json`](../../sessions/2f/2f590146eb1330338009.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果

| # | 检查项 | 结果 |
|---|--------|------|
| 1 | env.py 无 valid-action bonus | ✅ 正确 — reward 仅为 `config.score * float(won)` (L195)，无 0.1 bonus |
| 2 | format_penalty = 0 | ✅ 正确 — yaml L74: `format_penalty: 0` |
| 3 | 加载了正确 config | ✅ 使用了 `_alfworld_exp012_reward_fix` |
| 4 | 进程存活 | ❌ **PID 221683 已死** |

## 结论：代码正确，但进程已崩溃

exp012 加载的代码和配置都是正确的，**但启动后立即报错退出**（EXIT_CODE=1）。

**崩溃原因**：vLLM 版本不兼容。
```
TypeError: EngineArgs.__init__() got an unexpected keyword argument 'disable_mm_preprocessor_cache'
```
当前安装的 vllm 版本不支持 `disable_mm_preprocessor_cache` 参数。需要升级 vllm 或从配置中移除该参数后重新提交。

---
