# exp-007 LAMBADA log_samples 批处理脚本

## 脚本路径

| 文件 | 路径 | 说明 |
|------|------|------|
| 批处理脚本 | `/root/entrainment_gated_ft/run_exp007_logsamples.sh` | 主入口，tmux 中运行 |
| fla wrapper | `/root/entrainment_gated_ft/run_lm_eval_fla.py` | 预注册 fla auto classes + HGRN2 monkey-patch |

## 模型列表

### 340M (16 个，全部需跑)

| # | 模型目录 | 输出目录名 |
|---|---------|-----------|
| 1 | 340M-20B-GatedDeltaNet-pure-baseline | GDN-pure |
| 2 | 340M-20B-GatedDeltaNet-hybrid-3-1 | GDN-h3-1 |
| 3 | 340M-20B-GatedDeltaNet-hybrid-6-1 | GDN-h6-1 |
| 4 | 340M-20B-GatedDeltaNet-hybrid-12-1 | GDN-h12-1 |
| 5 | 340M-20B-GatedDeltaNet-New-hybrid-24-1 | GDN-h24-1 |
| 6 | 340M-20B-RetNet-pure | RetNet-pure |
| 7 | 340M-20B-RetNet-hybrid-3-1 | RetNet-h3-1 |
| 8 | 340M-20B-RetNet-hybrid-6-1 | RetNet-h6-1 |
| 9 | 340M-20B-RetNet-hybrid-12-1 | RetNet-h12-1 |
| 10 | 340M-20B-RetNet-hybrid-24-1 | RetNet-h24-1 |
| 11 | 340M-20B-HGRN2-pure-baseline | HGRN2-pure |
| 12 | 340M-20B-HGRN2-hybrid-3-1 | HGRN2-h3-1 |
| 13 | 340M-20B-HGRN2-hybrid-6-1 | HGRN2-h6-1 |
| 14 | 340M-20B-HGRN2-hybrid-12-1 | HGRN2-h12-1 |
| 15 | 340M-20B-HGRN2-hybrid-24-1 | HGRN2-h24-1 |
| 16 | transformer_340M_baseline | Transformer |

### 1.3B (11 个补跑)

| # | 模型目录 | 输出目录名 |
|---|---------|-----------|
| 1 | 1.3B-100B-GatedDeltaNet-pure | GDN-pure |
| 2 | 1.3B-100B-GatedDeltaNet-hybrid-12-1 | GDN-h12-1 |
| 3 | 1.3B-100B-RetNet-hybrid-3-1 | RetNet-h3-1 |
| 4 | 1.3B-100B-RetNet-hybrid-6-1 | RetNet-h6-1 |
| 5 | 1.3B-100B-RetNet-hybrid-12-1 | RetNet-h12-1 |
| 6 | 1.3B-100B-RetNet-hybrid-24-1 | RetNet-h24-1 |
| 7 | 1.3B-100B-HGRN2-pure | HGRN2-pure |
| 8 | 1.3B-100B-HGRN2-hybrid-3-1 | HGRN2-h3-1 |
| 9 | 1.3B-100B-HGRN2-hybrid-6-1 | HGRN2-h6-1 |
| 10 | 1.3B-100B-HGRN2-hybrid-12-1 | HGRN2-h12-1 |
| 11 | 1.3B-100B-HGRN2-hybrid-24-1 | HGRN2-h24-1 |

## 预估时间

- 340M × 16: ~3.5 min/model → ~56 min
- 1.3B × 11: ~6 min/model → ~66 min
- **总计: ~2 小时**

## Dry-run 结果

- 模型: 340M GDN-pure
- 结果: acc=0.3435, perplexity=30.898
- 输出: `/root/entrainment_gated_ft/lm_eval_clean/exp007/340m/GDN-pure/__root__autodl-tmp__models__340M-20B-GatedDeltaNet-pure-baseline/samples_lambada_openai_2026-05-20T01-17-21.574576.jsonl`
- 耗时: ~3.5 min (含模型加载)

## 技术细节

- 所有 fla 模型（GatedDeltaNet, RetNet, HGRN2, Transformer）均需通过 `run_lm_eval_fla.py` 运行，因为模型目录中无 `modeling_*.py`，`trust_remote_code=True` 不够
- `import fla` 自动注册所有 auto classes
- HGRN2 额外需要 `_tied_weights_keys = {}` monkey-patch
- 脚本自动跳过已有 `samples_lambada_openai*.jsonl` 的目录

## 启动方式

```bash
tmux new -s exp007
bash /root/entrainment_gated_ft/run_exp007_logsamples.sh 2>&1 | tee /tmp/exp007_batch.log
```
