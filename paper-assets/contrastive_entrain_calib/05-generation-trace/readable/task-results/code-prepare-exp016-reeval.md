# code prepare exp016 reeval

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare-exp016-reeval_20260519T084231_result.json`
- **Structured JSON:** [`5c3ef11dfac803e5833a.json`](../../sessions/5c/5c3ef11dfac803e5833a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 汇报

### 1. exp-016 输出位置和内容

| 项目 | 值 |
|---|---|
| 服务器 | westd-28034 |
| 目录 | `/root/contrastive_entrain_calib/checkpoints/exp016_actadd/` |
| 文件 | `results_summary.json` (1.5KB) + `results_detailed.json` (2.4MB) |
| 运行时间 | v2 run, 2026-05-19 10:07 → 13:08 |
| 保存内容 | 完整生成文本 (`initial_response` + `generated_response`) + `stance_consistent` + `condition` |
| 原始eval数据 | `/root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl` (362 样本, 181 对) |
| westd-29046 | 无 exp-016 数据 |

### 2. Re-eval 策略：重跑推理

**不能只重新评分**。NLI 判定逻辑相同 (`ent > con`)，重新评分结果不变。28.7pp 差异来自生成侧：
- exp-016 无 `enable_thinking=False` → thinking tokens 污染 NLI 输入
- exp-016 无 `&lt;think>` 标签剥离
- exp-016 `max_new_tokens=256` vs eval_pipeline 512

**eval_pipeline.py 不直接支持 ActAdd**（无 hook 代码），且数据格式不兼容（SyconBench 期望 `{initial_question, pressure_prompts}`，校准数据是 `{turns: [...]}`）。

→ 写了 wrapper 脚本 `run_exp016_reeval.py`，集成 ActAdd hooks + eval_pipeline 的生成/评分逻辑。

### 3. 脚本路径

**本地**: `artifacts/run_exp016_reeval.py`

**运行命令**（待 GPU 3 空闲后）:
```bash
CUDA_VISIBLE_DEVICES=3 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
/root/miniconda3/bin/python /root/contrastive_entrain_calib/results/exp016_reeval/run_exp016_reeval.py \
  --eval_data /root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl
```

需要先将脚本 scp 到 westd-28034（或 westd-29046）。

**输出目录**: `/root/contrastive_entrain_calib/results/exp016_reeval/`

### 4. directions.pt

两台服务器均有 `/root/contrastive_entrain_calib/results/exp001/directions.pt`（2.3MB, 181 对, May 18）。脚本已硬编码此路径。

### 5. 预估运行时间

原始 exp-016 v2: 每个 alpha ~37 分钟，5 个 alpha 共 ~3 小时。Re-eval 使用 `max_new_tokens=512`（原为 256），预估 **~3.5-4 小时**。

### 6. 指标变化

Re-eval 将输出 eval_pipeline 标准指标：`tof`, `nof`, `sycon_score`, `rc_auc`，替代原始的 `NoF`/`WRR`。

---
