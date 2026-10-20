# code gradient analysis v2 prep

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gradient_analysis_v2_prep_20260527T045624_result.json`
- **Structured JSON:** [`e985bec0c7e249008b7c.json`](../../sessions/e9/e985bec0c7e249008b7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本部署完成，dry-run `--help` 通过。

---

**现有代码发现：**
- `scripts/run_gradient_analysis_v2.py` — 单条件 per-layer 分析，用真实 RLDS 数据，但只支持逐个条件运行，无 gradient variance 指标
- `artifacts/v2_gradient_analysis.py` — 多条件对比，但用合成数据（随机 pixel_values），只跑在 `_cached_patch_features` 上
- `analysis/gradient_analysis.py` — v1 版本，含 per-layer 分组和 plotting

**新脚本 `scripts/gradient_analysis_v2.py` 设计：**

| 特性 | 说明 |
|------|------|
| 多条件统一运行 | `--config` 传入 JSON 配置，一次跑 5 个条件，顺序加载/卸载模型 |
| 单条件模式 | `--checkpoint_dir` + `--condition_name` 跑单个条件 |
| 真实 eval 数据 | 使用 RLDS pipeline，默认 200 batches × bs=4 = 800 samples |
| 聚合 encoder 级指标 | cosine similarity / L2 norm / variance 在整个 vision backbone 参数上计算 |
| Per-layer 指标 | 按 DINOv2/SigLIP block 分组，同样计算 norm/cosine/conflict/variance |
| Edge case 处理 | Detach 条件：OCC gradient 不经过 encoder → cosine=N/A；Vanilla：无 OCC head → 只有 action grad |
| 自动检测 | 从 condition name + checkpoint 文件自动推断 occ_detach / occ_norm / is_vanilla |
| 输出 | 每条件独立 JSON + 全条件合并 JSON + 打印 summary table（含 variance ratio 分析） |

运行环境：`conda activate occsafe`，Python 路径 `/root/miniconda3/envs/occsafe/bin/python`。

训练完成后，准备一个 `conditions.json` 指向 5 个 50000_chkpt 路径即可启动：
```bash
python scripts/gradient_analysis_v2.py \
  --config conditions.json \
  --output_dir /root/occsafe_vla/artifacts/gradient_v2/ \
  --gpu 0
```

---
