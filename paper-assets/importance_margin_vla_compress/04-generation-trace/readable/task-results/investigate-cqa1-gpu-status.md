# investigate cqa1 gpu status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_cqa1_gpu_status_20260525T051435_result.json`
- **Structured JSON:** [`cfec395458d9cfabead4.json`](../../sessions/cf/cfec395458d9cfabead4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## cqa1-33015 状态汇报

### GPU 状态
4× RTX 4090D **全部空闲**，0MiB 显存占用，0% 利用率，无任何 GPU 进程。

### 进程状态
4 个 PID (68723, 70466, 70539, 70613) **均已不存在**，进程已终止。

### 日志分析
带 `_v2` 后缀的日志文件不存在（任务可能用了不带 `_v2` 的名字实际运行）。最近的 4 个 postfix 日志（最后修改时间 May 25 12:36-12:40）**全部以相同错误崩溃**：

```
ValueError: Failed to instantiate processor step 'tokenizer_processor' with config: 
  {'tokenizer_name': 'google/paligemma-3b-pt-224'}. 
  Error: [Errno 99] Cannot assign requested address
```

**根因**：`[Errno 99] Cannot assign requested address` — 网络不可达。tokenizer 初始化时尝试从 `google/paligemma-3b-pt-224` 下载，但服务器网络（可能未 `source /etc/network_turbo`）无法连接外网，导致 4 个实验在启动阶段就全部失败。

### 结论
4 个实验均在启动初期因网络问题崩溃，未进入实际评估。4 块 GPU 当前完全空闲可用。重跑前需确保 tokenizer 已本地缓存或启用网络代理。

---
