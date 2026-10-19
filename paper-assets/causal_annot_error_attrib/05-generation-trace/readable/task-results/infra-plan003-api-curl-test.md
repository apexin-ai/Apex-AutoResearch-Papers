# infra plan003 api curl test

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_plan003-api-curl-test_20260520T112603_result.json`
- **Structured JSON:** [`7b06830abb1b3d6574bc.json`](../../sessions/7b/7b06830abb1b3d6574bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### API 端点测试

| 模型 | HTTP Status | 响应时间 | 超时 | 响应摘要 |
|------|------------|---------|------|---------|
| deepseek/deepseek-chat | **200** | 14.87s | 否 | `"Hello! 😊 How"` (provider: Novita) |
| meta-llama/llama-4-maverick | **200** | 6.83s | 否 | `"hello! How can I"` (provider: DeepInfra) |
| qwen/qwen3-235b-a22b | **200** | 6.33s | 否 | `"Hello! How can I assist"` (provider: Alibaba) |
| /v1/models (无 Auth) | **422** | 1.43s | 否 | 缺 Authorization header（预期） |

**三个模型端点全部正常可达，无超时。**

### 进程状态

- PID 401208：**仍在运行**，状态 S (sleeping)，已运行 20:32
- 日志最新进度：**[150/1500]**，已经从之前卡住的 100 条推进到了 150 条

**结论：API 端点无问题，进程已恢复推进（100 → 150）。之前的卡顿可能是临时网络延迟或 API 限流，现在已自行恢复。**

---
