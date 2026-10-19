# code e2e dryrun verified

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_e2e-dryrun-verified_20260515T201940_result.json`
- **Structured JSON:** [`3d06086b5e03cf04f0ce.json`](../../sessions/3d/3d06086b5e03cf04f0ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

100-instance full run 正常启动：
- 加载了 100 个 SWE-bench instances
- Retriever 模型已加载到 GPU
- 开始评估

**Dry-run 总结：**

| 指标 | 值 |
|---|---|
| results.jsonl 行数 | 5 ✅ |
| 非空 patch | 2/5（instance 1 & 2） |
| 空 patch（API 正常） | 0/5 |
| git fetch 失败 | 3/5（无网络，现已用 network_turbo 修复） |
| 401 错误 | 0 ✅ |

**Full run 启动确认：**
- PID: 94869（bash 包装）→ 子进程 Python
- 日志路径: `/tmp/e2e_100.log`
- 输出目录: `/root/autodl-tmp/structfuse/eval_results/e2e_100`
- 网络代理: 已开启（`source /etc/network_turbo`），git fetch 应能正常工作
- 预估耗时: ~5 min/instance × 100 = ~8-9 小时（因 GPU 竞争可能更久）

---
