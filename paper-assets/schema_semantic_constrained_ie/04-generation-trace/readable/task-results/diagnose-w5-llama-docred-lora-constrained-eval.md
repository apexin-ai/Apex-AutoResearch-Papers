# diagnose w5 llama docred lora constrained eval

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_w5_llama_docred_lora_constrained_eval_20260516T002726_result.json`
- **Structured JSON:** [`b84818fbcbbb56822703.json`](../../sessions/b8/b84818fbcbbb56822703.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 根因：误报 — 进程实际仍在运行

**EXIT_CODE=143 来自 job wrapper/SSH 会话层，而非 Python 推理进程本身。** 实际的 constrained eval 进程（PID 317469）当前正在 GPU 0 上正常运行并产出结果。

### 证据

| 项目 | 状态 |
|------|------|
| PID 317469 | 正在运行，cmdline 完全匹配 constrained eval 命令 |
| GPU 0 | 16GB/98GB VRAM，88% 利用率，无 OOM |
| 输出文件 | 2分钟内从 3 行 → 11 行，持续增长 |
| 磁盘 | 根分区 47%，数据盘 48%，无空间问题 |
| dmesg/kill 记录 | 无 OOM-killer 或异常 kill 痕迹 |

### 时间线

```
08:17:23  log 文件创建（进程启动）
08:17~08:27  模型加载(~3s) + 约束语法编译初始化(~9min)
           ← 96种关系类型的 grammar 编译耗时较长
08:27:10  output 文件创建（首个样本写入）
08:27:56  log 显示 3 个 pad_token_id 警告
  ↑ 大约此时 job wrapper 报告 EXIT_CODE=143
08:29:45  output 已增长到 11 行 / 104KB
08:30+    进程继续运行中...
```

### 日志关键片段（最后输出）

```
Setting `pad_token_id` to `eos_token_id`:128001 for open-end generation.
Setting `pad_token_id` to `eos_token_id`:128001 for open-end generation.
Setting `pad_token_id` to `eos_token_id`:128001 for open-end generation.
```
无错误、无 Traceback、无 Terminated 字样。

### 输出状态

- 已处理 **11/998** 样本，速度约 14s/样本
- 预计总耗时 **~3.8 小时**
- 输出文件持续增长中

### 关于 unconstrained eval 的 SIGTERM

`w5_llama_docred_lora_unconstrained_eval` 也是同样模式：首次运行被 wrapper SIGTERM 杀掉（已处理 775/998），后通过 resume 成功完成全部 998 样本。这确认了 SIGTERM 来自 job 管理层，非程序自身问题。

### 建议

1. **无需干预** — 当前进程正常运行中，等待完成即可
2. 定期监控进度：`wc -l outputs/w5_llama_docred_lora_constrained_eval.jsonl`
3. 如果后续确实被 kill，脚本支持 resume（已在 unconstrained eval 上验证过）
4. 考虑将 job wrapper 的超时阈值调大，避免 constrained eval 的长初始化时间（~10min 编译语法）触发误报

---
