# diagnose bjb1 cuda0 process

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_bjb1_cuda0_process_20260514T151757_result.json`
- **Structured JSON:** [`1626678f8cf1f06e6ce5.json`](../../sessions/16/1626678f8cf1f06e6ce5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查结果如下：

## 调查结论

### 关键发现：bjb1-21071 和 autodl-5090 是同一台机器
两台服务器 hostname 均为 `autodl-container-31eb41bf76-61568de9`，是同一 AutoDL 实例的不同 SSH 别名。

### 进程详情
| 项目 | 值 |
|------|-----|
| PID | 81201 |
| 启动时间 | 2026-05-14 22:39:42 (+0800) |
| 命令 | `llamafactory-cli train train_config_llama_conll2003.yaml` |
| 工作目录 | `/root/autodl-tmp/struct_self_consist_ie` |
| GPU 显存 | 24718 MiB (cuda:0) |
| 模型 | Meta-Llama-3.1-8B-Instruct (LoRA r=32, α=64) |
| 数据集 | conll2003_uie_train |
| 输出目录 | `checkpoints/llama3.1-8b-conll2003-lora` |
| 训练进度 | checkpoint-1200（最新，23:18），每 ~6.5 分钟一个 checkpoint |

### 判断：这就是 exp_017_llama_conll

Registry 中 `exp_017_llama_conll` 确实存在且状态为 RUNNING，注册在 `autodl-5090` 的 cuda:0 上，命令完全匹配 `llamafactory-cli train train_config_llama_conll2003.yaml`。

**不存在"未注册进程"问题。** Director 看到 bjb1-21071 上有进程以为没注册，实际上 bjb1-21071 = autodl-5090，该进程就是已注册的 exp_017_llama_conll。

### 建议
- **保留，无需操作。** 进程正常运行，已注册。
- 建议统一服务器别名，避免后续混淆——registry 和操作都用同一个名称（autodl-5090 或 bjb1-21071，二选一）。

---
