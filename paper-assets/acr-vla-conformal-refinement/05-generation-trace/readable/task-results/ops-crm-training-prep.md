# ops crm training prep

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_crm-training-prep_20260521T160425_result.json`
- **Structured JSON:** [`510d642e6fc2a8b2f188.json`](../../sessions/51/510d642e6fc2a8b2f188.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. Merge 逻辑分析（src/train_crm.py:219）

**自动 vs 手动**：`_try_merge()` 在 `precompute_features()` 末尾自动调用——但**只对当前进程能看到的本地 cache_dir 生效**。跨服务器的 partial 文件必须先 rsync 到同一台机器，然后才能触发合并。

**触发条件**（line 220-232）：
- 对每个 `shard_id ∈ [0, num_shards)`，glob `partial_s{sid}_*.pt` 找最大 `end_idx`
- `expected = len(range(sid, total_samples, num_shards))`，若任一 shard 的 `done < expected` 直接 return
- 所有 shard 完整后：按 `start_idx` 排序，对每个 shard 拼接所有 partial → 交错回填到 `obs_merged[range(sid, n, num_shards)]`
- 落盘 `obs_features.pt` / `k_samples.pt` / `expert_actions.pt` + `manifest.json`

**Training 加载逻辑**（train()，line 316）：必须有 `manifest.json` 才能启动训练，否则 `FileNotFoundError`。读 `obs_features.pt` / `k_samples.pt` / `expert_actions.pt`，按 `manifest["obs_dim"]` 构建 CRM。

**Tensor shape**（已从 spatial s6_0_500.pt 验证）：
- `obs_features`: (N, **2048**) — pi05 hidden_size，**不是 SmolVLA 的 960**
- `k_samples`: (N, K=10, H_EFF=5, CORRECTION_DIM=6)
- `expert_actions`: (N, 5, 6)

### 2. ⚠️ 关键问题：原 `_try_merge` 无法处理跨 save_every 的重叠文件

**确认的重叠**（bjb2-40593 shard 0，43 个文件中 10 处区间重叠）：
- 同时存在 `partial_s0_1500_2000.pt`（save_every=500，4.7MB）和 `partial_s0_1500_1600.pt` ... `partial_s0_1900_2000.pt`（save_every=100，每 953KB）
- 原 `_try_merge` 会把这两批文件都 cat 起来 → **重复数据，merged tensor 损坏**

**跨服务器同 shard_id 冲突**：bjb1-32546 的 s1（save_every=500，max=2500）和 bjb1-18228 的 s1（save_every=100，max=5300）若 rsync 到同一目录会产生 0-2500 范围的重叠。

### 3. 已写：`scripts/merge_precompute_cache.py`（bjb1-18228，259 行）

核心策略：贪心覆盖（greedy cover），从 start=0 开始每步选择 `start==cur` 的最长 partial，跳过被它覆盖的更小段。已在 bjb2-40593 shard 0 验证：
```
shard 0: 43 files → 33 segments, covers [0, 4100]
  [1500, 2000] → partial_s0_1500_2000.pt  ← 自动选了长段
  [2000, 2500] → partial_s0_2000_2500.pt  ← 跳过中间小段
  [2500, 2600] → partial_s0_2500_2600.pt  ← 之后继续 save_every=100
```
支持 `--dry_run`、`--allow_partial`、`--total_samples` 推断、overlap 报告。

### 4. bjb1-32546 partial 文件统计（object，截止 ~00:04）

| Shard | 文件数 | save_every | max_end | 状态 |
|---|---|---|---|---|
| s1 | 5 | 500 | 2500 | 进行中 |
| s2 | 6 | 500 | 3000 | 进行中 |
| s3 | 6 | 500 | 3000 | 进行中 |
| s4 | 6 | 500 | 3000 | 进行中 |
| s5 | 36 | 100 | 3600 | 进行中 |
| s6 | 32 | 100 | 3200 | 进行中 |
| s7 | 36 | 100 | 3600 | 进行中 |
| s8 | 37 | 100 | 3700 | 进行中 |
| s9 | 36 | 100 | 3600 | 进行中 |

注：s1-s4 是 save_every=500 的旧运行，s5-s9 是 save_every=100 的新运行。s3/s4/s6 有 `-r2` 重启进程，预计后续会写更多文件。

bjb2-40593 shard 0：43 文件，max_end=4100，**save_every 混用**（含 10 处区间重叠）。
bjb2-28827 spatial s0-s5：每 shard 7 文件（save_every=500），max_end=3500。
bjb1-18228 spatial s6：9 文件（save_every=500），max_end=4500。

### 5. bjb1-18228 环境就绪状态

- Python 3.12.3 / torch 2.10.0+cu128 / 4× RTX 4090 24GB
- conda base 已激活（`/root/miniconda3`）
- 磁盘 `/root/autodl-tmp`：91GB available
- 代码：`src/train_crm.py`、`utils.py`、`crm.py`、`cgs.py` 全部就绪
- LIBERO 数据：`/root/autodl-tmp/libero_data/{libero_object,libero_spatial,...}` 齐全
- 模型：`/root/autodl-tmp/models/pi05_libero_finetuned/` 齐全
- imports 验证通过
- 当前占用：cuda:3 跑 spatial shard 6（PID 781280，~10GB），**cuda:0/1/2 空闲**
- cache 目录：`/root/autodl-tmp/crm_cache_pi05/{object,spatial}/` 已存在
- ⚠️ bjb1-18228 的 object dir 已经有大量历史 partial 文件（s1/s2/s3/s4/s7/s8/s9，全部 save_every=100），最新 mtime 23:58，对应一个已停止的 object 任务。这些文件未必和当前主跑的 bjb1-32546 一致，**rsync 前需要清空 bjb1-18228 的 object dir**，否则会产生跨服务器 shard 冲突。

### 6. 推荐操作步骤（precompute 完成后 → CRM training）

```bash
# === Step A：清理 bjb1-18228 object dir 的历史 partial（避免冲突）===
ssh bjb1-18228 'rm /root/autodl-tmp/crm_cache_pi05/object/partial_s*.pt'

# === Step B：rsync 所有 partial 到 bjb1-18228 ===
# Object（10 shards）：
#   s0 from bjb2-40593, s1-s9 from bjb1-32546
ssh bjb2-40593 'rsync -av /root/autodl-tmp/crm_cache_pi05/object/partial_s0_*.pt \
  bjb1-18228:/root/autodl-tmp/crm_cache_pi05/object/'
ssh bjb1-32546 'rsync -av /root/autodl-tmp/crm_cache_pi05/object/partial_s*.pt \
  bjb1-18228:/root/autodl-tmp/crm_cache_pi05/object/'

# Spatial（7 shards）：s0-s5 from bjb2-28827, s6 已在 bjb1-18228
ssh bjb2-28827 'rsync -av /root/autodl-tmp/crm_cache_pi05/spatial/partial_s*.pt \
  bjb1-18228:/root/autodl-tmp/crm_cache_pi05/spatial/'

# === Step C：先 dry-run merge 检查覆盖完整性 ===
ssh bjb1-18228
cd /root/acr-vla-conformal-refinement
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
python scripts/merge_precompute_cache.py \
    --cache_dir /root/autodl-tmp/crm_cache_pi05/object \
    --num_shards 10 --dry_run
python scripts/merge_precompute_cache.py \
    --cache_dir /root/autodl-tmp/crm_cache_pi05/spatial \
    --num_shards 7 --dry_run

# === Step D：执行 merge（产出 obs_features.pt / k_samples.pt / 
#     expert_actions.pt / manifest.json 到 cache_dir）===
python scripts/merge_precompute_cache.py \
    --cache_dir /root/autodl-tmp/crm_cache_pi05/object --num_shards 10
python scripts/merge_precompute_cache.py \
    --cache_dir /root/autodl-tmp/crm_cache_pi05/spatial --num_shards 7

# === Step E：训练 CRM（cuda:0-2 任选）===
CUDA_VISIBLE_DEVICES=0 python src/train_crm.py \
    --model pi05 --benchmark object spatial \
    --cache_dir /root/autodl-tmp/crm_cache_pi05/ \
    --output_dir /root/autodl-tmp/checkpoints/crm_pi05/ \
    --epochs 50 --batch_size 32 --lr 1e-3 --seed 42 \
    --obs_dim 2048
```

**注意事项**：
1. **绝对不要用 `train_crm.py --auto`** —— 它会触发原 `_try_merge`，无法处理重叠文件。必须用新写的 `merge_precompute_cache.py`。
2. **`--obs_dim 2048`** —— pi05 feature dim 是 2048（不是默认的 960）；不传也能跑因为 train 从 manifest 读 obs_dim，但显式更稳。
3. Dry-run train_crm.py 只解析参数（不实际启动训练）需要 manifest 已存在，否则会 raise FileNotFoundError；当前条件不满足，**只能等 merge 完成后再做真正 dry-run**。

---
