# run conll t ablation s456

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_conll_t_ablation_s456_20260521T004153_result.json`
- **Structured JSON:** [`426b98ec0985a6328325.json`](../../sessions/42/426b98ec0985a6328325.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个实验全部 RUNNING，registry 更新完成。

**汇总：**

| 实验 | GPU | PID | 进度 |
|------|-----|-----|------|
| `exp_conll_t05_s456` (T=0.5) | cuda:1 | 253823 | ~21% (5928/27624) |
| `exp_conll_t08_s456` (T=0.8) | cuda:2 | 254524 | ~11% (3088/27624) |
| `exp_conll_t12_s456` (T=1.2) | cuda:3 | 255217 | ~5% (1408/27624) |

- cuda:0 未碰（14B inference 继续运行）
- 模型：`qwen3-8b-conll2003-merged`，数据集：CoNLL-2003，N=8，seed=456
- 日志文件：`output/exp_conll_t{05,08,12}_seed456.log`
- 每个跑 27624 prompts（3453 × 8），按当前速度估计各需 ~5-8 小时完成

---
