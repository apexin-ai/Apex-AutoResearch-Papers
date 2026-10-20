# code exp021 real data control

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp021-real-data-control_20260523T220723_result.json`
- **Structured JSON:** [`62d0a15f5c638c45c637.json`](../../sessions/62/62d0a15f5c638c45c637.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。汇报如下：

**脚本路径**: `/root/spectral_collapse_ews/run_gpt2m_realdata_control.py`

**Dry-run 结果**: 通过
- `--help` 正常解析
- 所有 imports (Config, pipeline) 正常
- 数据文件就位：train 418MB, eval 42MB, spectral 8.4MB

**训练超参（与 exp_020 完全一致）**:
- lr=5e-5, batch_size=8, grad_accum=4 (effective batch=32)
- 1 epoch/gen, warmup=5%
- 总训练量 = 50K samples/gen（全部真实数据）

**关键差异 vs exp_020**:
| | exp_020 | exp_021 |
|---|---|---|
| ratio | r=0.0 (纯合成) | r=1.0 (纯真实) |
| generations | 10 | 3 |
| 合成数据生成 | 每代 50K | 无 |

**预计运行时间**: ~2-3 小时。exp_020 跑 5 代花了 ~7 小时，但每代包含 50K 样本的合成数据生成（GPT-2-medium 生成很慢）。exp_021 跳过生成步骤，只有训练 + eval，因此快很多。

**运行命令**:
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/spectral_collapse_ews
nohup python run_gpt2m_realdata_control.py --seed 42 --gpu 0 > logs/exp_021_seed42.log 2>&1 &
```

等 Director 批准后启动。

---
