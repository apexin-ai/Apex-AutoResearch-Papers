# code exp 007 data collection script

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-007-data-collection-script_20260519T170803_result.json`
- **Structured JSON:** [`5aa823e274bf1963533a.json`](../../sessions/5a/5aa823e274bf1963533a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**产出：**
1. `/root/entrainment_gated_ft/run_exp007_logsamples.sh` — 批处理脚本，27 个模型（16×340M + 11×1.3B）
2. `/root/entrainment_gated_ft/run_lm_eval_fla.py` — 统一 Python wrapper（预注册 fla auto classes + HGRN2 monkey-patch）
3. 报告已注册为 artifact `art_20260519_8eb8cf`

**关键发现：** 所有 fla 模型（不只 HGRN2）都需要通过 Python wrapper 运行，因为模型目录中没有 `modeling_*.py`，直接 `lm_eval` CLI + `trust_remote_code=True` 会报 `model_type` 未注册。

**Dry-run 验证通过：** 340M GDN-pure，acc=0.3435，~3.5 min。预估全部跑完约 2 小时。

**启动：** `tmux new -s exp007 && bash /root/entrainment_gated_ft/run_exp007_logsamples.sh 2>&1 | tee /tmp/exp007_batch.log`

---
