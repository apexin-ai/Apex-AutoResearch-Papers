# code plan001 vota no actual expected

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan001-vota-no-actual-expected_20260515T015508_result.json`
- **Structured JSON:** [`bdd7215880b22bd05eb4.json`](../../sessions/bd/bdd7215880b22bd05eb4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

## VOTA 格式分析
- actual/expected 在 VOTA 中的格式：`[ASSERT] raw_assertion_line | actual=X, expected=Y`，另有 fallback 格式 `[ASSERT] raw_line | [fallback: full locals] k1=v1, k2=v2`
- 去除方案：**方案 B**（已有脚本 `prepare_ablation_data.py`）。从已格式化的 vota 数据后处理，找 ` | actual=` 截断值，找 ` | [fallback:` 删除整行。保留 `[ASSERT]` 行号/assertion text、`[ERROR]`、`[LOOP]` 不变

## 数据生成
- `vota_no_ae_train.jsonl`：n=4720，12.5MB
- `vota_no_ae_test.jsonl`：n=1190，3.3MB

## 验证
- `actual=`/`expected=` 残留：**0 条**（train+test 全清）
- `[fallback` 残留：2 条，均为截断位置产物（无变量值泄露）
- 标签保留：`[ASSERT]` 4041 行、`[ERROR]` 382 行、`[LOOP]` 3061 行（train 文件）
- label 完整：100%（5910 条均有 pass/fail）
- pass/fail 分布：3958/1952（66.97%/33.03%）
- Token 统计（after chat template）：

| 条件 | min | max | avg | median | over_2048 |
|------|-----|-----|-----|--------|-----------|
| vota | 143 | 2048 | 1925.6 | 2048.0 | 0 |
| vota_no_ae | 113 | 2048 | 831.2 | 677.0 | 0 |

去除 actual/expected 后平均 token 下降 57%（1925.6 → 831.2），符合预期。

## 训练命令
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/trace-verdict-study && CUDA_VISIBLE_DEVICES=0 python train/train_sft.py --condition vota_no_ae --gpu 0 --wandb_run_name vota_no_ae_seed42"
```

---
