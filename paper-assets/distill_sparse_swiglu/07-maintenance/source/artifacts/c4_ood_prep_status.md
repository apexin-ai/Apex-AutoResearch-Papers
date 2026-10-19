# C4 OOD 评估数据准备状态报告

**日期**: 2026-05-17

## 1. 数据存在状态

### westd-34887 ✅ 数据完备

| 路径 | 大小 | 内容 |
|------|------|------|
| `/root/autodl-tmp/c4_validation/` | 311M | 8个 json.gz 分片 (原始格式) |
| `/root/autodl-tmp/c4_validation_arrow/` | 783M | Arrow 格式缓存 |
| `/root/autodl-tmp/data/c4_val/` | ~783M | load_from_disk 格式 (2个 arrow + state.json)，**代码直接读取此路径** |

### westd-41718 ⚠️ 部分缺失

| 路径 | 大小 | 内容 |
|------|------|------|
| `/root/autodl-tmp/.hf_cache/hub/datasets--allenai--c4/` | 419M | HF Hub 缓存 (含8个 json.gz validation 分片) |
| `/root/autodl-tmp/data/c4_val/` | **不存在** | 代码要求的 load_from_disk 路径缺失 |

westd-41718 有原始 json.gz 数据但缺少预处理后的 Arrow 目录。代码 `data_utils.py:103` 优先读取 `/root/autodl-tmp/data/c4_val`，不存在时会 fallback 到 HF streaming 加载（需关闭离线模式）。

## 2. 磁盘空间

| 服务器 | 系统盘 | 数据盘 (/dev/sda2) |
|--------|--------|---------------------|
| westd-34887 | 30G (81% used, 5.8G free) | 879G (3% used, 817G free) |
| westd-41718 | 30G (8% used, 28G free) | 879G (9% used, 764G free) |

两台机器数据盘空间充裕，C4 validation 约需 ~1GB，无空间问题。

## 3. 评估代码支持

### benchmark_eval.py ✅ 已支持 C4

- `run_c4_ppl()` (line 247): 调用 `get_eval_dataset("c4", ...)` 加载数据，用 `evaluate_perplexity()` 计算 PPL
- 命令行参数 `--tasks c4` 即可触发
- 支持 `--max_eval_samples` 控制样本数

### 专用脚本 ✅ 已存在

| 脚本 | 功能 |
|------|------|
| `src/eval_c4_ood.py` | 完整对比: Dense vs KL-Predictor-50% vs TEAL-50% |
| `src/eval_c4_predictor.py` | 单个 predictor checkpoint 的 C4 PPL 评估 (接受 --ckpt 参数) |

### data_utils.py 中的 C4 加载逻辑

```python
# Line 102-108
elif name == "c4":
    _c4_local = "/root/autodl-tmp/data/c4_val"
    if os.path.isdir(_c4_local):
        ds = load_from_disk(_c4_local)
    else:
        ds = load_dataset("allenai/c4", "en", split="validation", streaming=True)
```

## 4. 已有结果

### c4_ood_ppl.json (westd-34887, 50% sparsity)

| Condition | C4 PPL | Δ vs Dense |
|-----------|--------|------------|
| Dense | 9.2075 | baseline |
| KL Predictor 50% | 18.401 | +99.8% |
| TEAL Vanilla 50% | 38.7503 | +320.9% |

### 其他 C4 eval 日志

| Predictor | C4 PPL | 样本数 |
|-----------|--------|--------|
| JSD (50%) | 26.1624 | 132 |
| ReverseKL (50%) | 19.9316 | 132 |

### westd-41718: c4_ood_kl30_s42

已开始运行但 `metrics` 为空 (可能 eval 失败或正在进行中)。配置: KL 30% sparsity, seed 42。

## 5. 如需在 westd-41718 准备 C4 数据

```bash
# 方案1: 从 westd-34887 rsync (推荐，最快)
rsync -avz root@westd-34887:/root/autodl-tmp/data/c4_val/ /root/autodl-tmp/data/c4_val/

# 方案2: 从已有 HF cache 构建 (需写脚本解压 json.gz → tokenize → save_to_disk)
python -c "
from datasets import load_dataset
ds = load_dataset('allenai/c4', 'en', split='validation',
                  cache_dir='/root/autodl-tmp/.hf_cache/hub')
ds.save_to_disk('/root/autodl-tmp/data/c4_val')
"
# 注意: 方案2需临时关闭 HF_DATASETS_OFFLINE=1

# 方案3: 从 json.gz 直接构建
python -c "
from datasets import load_dataset
ds = load_dataset('json', data_files='/root/autodl-tmp/.hf_cache/hub/datasets--allenai--c4/snapshots/*/en/c4-validation.*.json.gz')
ds['train'].save_to_disk('/root/autodl-tmp/data/c4_val')
"
```

## 6. 总结

| 项目 | 状态 |
|------|------|
| westd-34887 C4 数据 | ✅ 完备，代码可直接读取 |
| westd-41718 C4 数据 | ⚠️ 有原始文件，缺 Arrow 目录 |
| benchmark_eval.py 支持 | ✅ `--tasks c4` |
| 专用 eval 脚本 | ✅ eval_c4_ood.py + eval_c4_predictor.py |
| 50% sparsity 结果 | ✅ 已有 (KL/JSD/ReverseKL) |
| 30% sparsity 结果 | ⚠️ westd-41718 上运行，metrics 为空 |
| 磁盘空间 | ✅ 两台均充裕 |
