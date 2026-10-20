# ssh 403 diag fix gpu release

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_403-diag-fix-gpu-release_20260524T174131_result.json`
- **Structured JSON:** [`6530652c8962177d4b0f.json`](../../sessions/65/6530652c8962177d4b0f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 0,1 已完全释放（0MiB）。GPU 2,3 仍运行 Qwen2.5-72B vLLM。

```
=== 403 诊断 ===
Sonnet 4.6:
  错误原文: Error code: 403 - {'error': {'message': 'This model is not available in your region.', 'code': 403}}
  原因: IP 地域封锁（AutoDL 中国 IP 被 OpenRouter 拒绝访问 Anthropic 模型）
  可修复性: 否（需换非中国 IP 的服务器，或走代理）

Gemini 2.5 Pro:
  错误原文: Error code: 403 - {'error': {'message': 'This model is not available in your region.', 'code': 403}}
  原因: IP 地域封锁（同上，Google 模型同样被限制）
  可修复性: 否（同上）

注：sonnet_n17_autodl.log 实际崩溃原因是 FileNotFoundError (mixtral-8x22b-instruct-v0.1.jsonl)，
    _fixed.log 修复了文件问题但遇到了 403 地域封锁。
    两个 judge 的脚本目前仍在运行但几乎每个请求都 403，仅偶尔成功（进度极慢 ~0.9 items/s 含大量重试）。

=== LLaMA GPU 释放 ===
操作: kill PID 582372 (APIServer) + 582917 (Worker_TP0) + 582918 (Worker_TP1)
GPU 0,1 状态: 已释放（0MiB / 97887MiB）

=== DeepSeek 加速 ===
当前速率: 0.3 items/s（[2800/12057]，ETA ~538min ≈ 9h）
瓶颈: API 响应延迟 + 单 worker 串行
  - config: rpm=100, max_workers=1（默认）
  - 每个请求耗时 ~3.3s（DeepSeek-V4-Pro 生成延迟）
  - 1 worker 串行 → 实际吞吐 ~18 req/min，远低于 rpm=100 的上限
可加速: 是
  方案: 重启采集脚本，加 --workers 10（或在 YAML 加 max_workers: 10）
  预期效果: 10 并发 → 可达 ~3 items/s（10x），ETA 从 9h 降到 ~1h
  风险: DeepSeek API 实际并发限制需确认，超限会触发 429
```

---
