# check exp 022 detailed progress

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp_022_detailed_progress_20260516T161525_result.json`
- **Structured JSON:** [`a54fc5b2988535aad0c4.json`](../../sessions/a5/a54fc5b2988535aad0c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_022 进度汇总

### 1. 已完成 (3/12)

| Generator | Scorer | K* | AUC(0v1) | AUC(1v2) |
|-----------|--------|-----|----------|----------|
| qwen_base | qwen_base | 2 | 0.987 | 0.626 |
| qwen_base | pythia | 2 | 0.962 | 0.617 |
| qwen_base | olmo | 2 | 0.960 | 0.605 |

### 2. 被跳过 (1/12) — 需重跑

- **qwen_base__qwen_instruct**: 脚本启动时 `config.json` 不存在被跳过，但模型现已就位（`/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct/config.json` 存在）

### 3. 当前正在跑 (1/12)

- **pythia_greedy__qwen_instruct**: Step 4 Feature Extraction，正在处理 depth 3（进度约 50%，日志时间 00:15 开始 depth 3）

### 4. 待跑 (7/12)

- pythia_greedy__qwen_base
- pythia_greedy__pythia
- pythia_greedy__olmo
- qwen_cont256__qwen_instruct
- qwen_cont256__qwen_base
- qwen_cont256__pythia
- qwen_cont256__olmo

### 5. OLMo generator 数据

不需要恢复。实验设计中 OLMo 仅作为 **scorer**（`/root/autodl-tmp/.hf_cache/allenai/OLMo-1B-hf`），不作为 generator。服务器上无 OLMo depth chain 数据，也无需生成。

### 6. 预估完成时间

- 每个 combo 约 18 分钟（6 depths × ~3 min/depth）
- 当前 combo 5 剩余 ~8 min
- Combos 6-12（7 个）：~126 min
- 总计：脚本自然结束约需 **2.2 小时**
- `qwen_base__qwen_instruct` 需额外手动重跑（~18 min）

---
