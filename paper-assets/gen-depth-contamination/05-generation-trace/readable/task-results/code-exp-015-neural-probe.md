# code exp 015 neural probe

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_015_neural_probe_20260513T184400_result.json`
- **Structured JSON:** [`766d9912d0bad76923be.json`](../../sessions/76/766d9912d0bad76923be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON 输出完整，包含 pairwise_auc（邻接+全对）、fold_stats、k_star、classification_accuracy、lgbm_baseline 对比。

**完成情况：**

1. **代码结构** — 已查看 `run_pipeline.py` 的 pairwise AUC 逻辑（5-fold GroupKFold by doc_id, binary LightGBM, AUC > 0.60 阈值定义 K*）
2. **脚本** — `scripts/run_exp015_neural_probe.py` 已写入服务器
   - Frozen Qwen2.5-1.5B → last hidden state → avg pool → 1536-dim
   - MLP (1536→512→256→N_classes)，Adam + early stopping
   - 5-fold GroupKFold CV，pairwise AUC 用 P(j)/(P(i)+P(j)) 归一化
   - 自动加载 LightGBM baseline 结果对比
3. **多数据集支持** — `--data_dir` 和 `--label` 均支持 `nargs="+"`
4. **dry-run 通过** — `--num_samples 50 --max_depth 2`，8 秒完成，K*=2
5. **验证** — `--help` 正常，JSON 输出完整，GPU 显存占用正常（与 exp-003 共存）

正式运行 3 数据集的命令（待你确认后执行）：
```bash
python scripts/run_exp015_neural_probe.py \
    --data_dir data_exp017_qwen_cont data_exp001_pythia data_exp002_olmo \
    --label Qwen-cont Pythia OLMo \
    --max_depth 5
```

---
