# diagnose exp 002 signals 15B instruct arc

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_002_signals_15B_instruct_arc_20260516T185020_result.json`
- **Structured JSON:** [`32949d2661f056cd9d29.json`](../../sessions/32/32949d2661f056cd9d29.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

### 根本原因：**模型路径错误 + HF Hub 不可达**

两个实验都不是 OOM 或人为 kill。

**exp_002_signals_15B_instruct_arc (原始)**:
- s1 (embedding) 成功完成（不需要加载目标模型，用的是 sentence-transformers）
- s2 (minkpp) 启动时调用 `AutoTokenizer.from_pretrained("/root/autodl-tmp/models/Qwen2.5-1.5B-Instruct")` 崩溃
- **该路径不存在**。`tokenizer_config.json` 缺失，实际模型位于 `/root/autodl-tmp/models/Qwen/Qwen2.5-1.5B-Instruct`
- transformers 发现本地路径不存在后，尝试当 HF repo ID 解析，但 `/root/autodl-tmp/...` 不是合法 repo ID → `HFValidationError`
- EXIT_CODE=129 是 SIGHUP，可能是 wrapper/tmux 在异常退出后发出的

**exp_002_signals_15B_instruct_arc_v2**:
- s1 阶段就卡在 HF Hub 连接重试（sentence-transformers/all-MiniLM-L6-v2），AutoDL 网络不通
- 最终被 Terminated (SIGHUP)

**gsm8k 实验**：日志目录中没有 `*15B_instruct_gsm8k*` 文件，可能未实际启动或日志名不同。

### 部分结果

输出目录 `/root/autodl-tmp/exp002/signals/Qwen2.5-1.5B-Instruct/` 有来自 **早期成功运行**（May 16 23:35-02:01）的完整信号文件：
- s1_embedding, s2_minkpp, s4_selfcritique, signals_merged（arc/gsm8k/mmlu 三个 benchmark 都有）
- 本次失败运行仅覆盖了 s1_embedding_arc_challenge.json（02:45）

### 修复方案

1. **修正 `--model-path`**：改为 `/root/autodl-tmp/models/Qwen/Qwen2.5-1.5B-Instruct`
2. **设置 `HF_HUB_OFFLINE=1`**：所有模型和数据集都已有本地缓存，避免 HF Hub 连接超时浪费时间
3. **启动前 `source /etc/network_turbo`**：如果确实需要联网（AutoDL 规范要求）
4. 可以安全重试，cuda:2 当前空闲（0 MiB）

---
