# ssh check exp001 injection exit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-exp001-injection-exit_20260513T205304_result.json`
- **Structured JSON:** [`d2245c1c7d550b5e5402.json`](../../sessions/d2/d2245c1c7d550b5e5402.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 1. 进程状态

| Benchmark | PID | 状态 |
|-----------|-----|------|
| MMLU (GPU 0) | 204467 | **仍在运行**，elapsed 01:38:33 |
| GSM8K (GPU 1) | 189361 | 已退出 |
| ARC (GPU 2) | 190712 | 已退出 |

### 2. Paraphrase 输出文件

| Benchmark | 文件 | 条目数 | 大小 | 修改时间 | QC 通过 |
|-----------|------|--------|------|----------|---------|
| GSM8K | `gsm8k_paraphrases.json` | 1319 | 2.1MB | May 14 04:11 | 228/1319 (17.3%) |
| ARC | `arc_challenge_paraphrases.json` | 1172 | 1.7MB | May 14 03:52 | 697/1172 (59.5%) |
| MMLU | **不存在** | — | — | — | — |

### 3. 日志关键信息

**GSM8K**: vLLM 初始化失败（GPU 显存不足 8.37/23.52 GiB），自动回退到 transformers。36 batches 全部完成，保存成功。

**ARC**: 同样 vLLM 回退 transformers。17 batches 全部完成，保存成功。

**MMLU (v3)**: 正在用 vLLM 运行，当前进度 **100/621 batches (16%)**，速度 ~2.6-6.8s/batch。

### 4. GPU 状态

```
GPU 0: 100%, 23132 MiB  ← MMLU 仍在跑
GPU 1: 100%, 21061 MiB
GPU 2:  57%, 15307 MiB
GPU 3:  33%, 17327 MiB
GPU 4:  69%, 21561 MiB
GPU 5:  61%, 18663 MiB
```

### 5. 判断

**GSM8K: SUCCESS** — 正常完成，1319 条 paraphrases 已保存。
**ARC: SUCCESS** — 正常完成，1172 条 paraphrases 已保存。
**MMLU: STILL RUNNING** — 进度 16%，预计还需 ~45-55 分钟完成。

⚠️ 需要关注的问题：
- **GSM8K QC 通过率极低 (17.3%)**，远低于 ARC (59.5%)，可能需要调整 paraphrase 质量参数或重新生成
- GSM8K 和 ARC 都未能使用 vLLM（GPU 显存被占用），回退到 transformers 后速度慢很多
- MMLU 文件尚未生成，需等待进程完成后再确认

---
