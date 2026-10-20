# KVTC 代码库深度调研报告

> 仓库: https://github.com/OnlyTerp/kvtc  
> 论文: arXiv 2511.01815 (ICLR 2026)  
> 调研日期: 2026-05-14  
> 目的: 为 CompressLink RABA 修改方案提供代码级依据

---

## 1. 仓库概览

### 1.1 项目结构

```
kvtc/
├── src/
│   ├── common.py              # 核心数据结构 (CalibrationData, CompressedKVCache, PCAEntry 等)
│   ├── pca.py                 # PCA transform, RoPE undo/reapply, PCACalibrator
│   ├── quantize.py            # DP bit allocation (精确版), uniform quantize/dequantize
│   ├── gpu_ops.py             # greedy bit allocation (近似版), batch quantize/dequantize
│   ├── entropy.py             # zlib DEFLATE + bit packing/unpacking
│   ├── ans_entropy.py         # rANS entropy coding (triple-mode picker: zlib/LZMA/rANS)
│   ├── adaptive_budget.py     # 基于 eigenvalue entropy 的 per-layer adaptive bit budget
│   ├── fused_ops.py           # Fused PCA+Quantize 单 pass kernel
│   ├── pipeline.py            # 参考 pipeline (CPU, ~160 行)
│   ├── pipeline_fast.py       # GPU 加速 pipeline (~233 行)
│   ├── triton_kernels.py      # Triton GPU kernels (bit packing)
│   ├── cache.py               # HuggingFace DynamicCache 包装
│   ├── calibrate.py           # PCA calibration (从模型+数据集)
│   ├── calibrate_vllm.py      # vLLM 专用 calibration
│   ├── vllm_backend.py        # vLLM attention backend
│   ├── vllm_triton.py         # Fused Triton decode attention kernel
│   ├── test_kvtc.py           # 38 个单元测试
│   └── test_real_model.py     # TinyLlama 集成测试
├── cuda/
│   ├── kvtc.h                 # CUDA kernel C API header
│   ├── kvtc_kernels.cu        # CUDA kernel 实现
│   └── CMakeLists.txt
├── benchmarks/
│   ├── benchmark_v1-v4.py     # 各版本 benchmark
│   ├── results_v1-v4.json     # 结果数据
│   └── benchmark_perplexity.py
└── setup.py
```

### 1.2 依赖

- **核心**: `torch`, `numpy`, `transformers`
- **开发**: `pytest`
- **可选**: `triton` (GPU bit packing), CUDA toolkit (原生 kernels)
- Python 3.10+, PyTorch 2.10+

### 1.3 支持模型

代码通过 HuggingFace `transformers` 加载模型，理论上支持所有 causal LM。已验证:
- Qwen2.5-7B-Instruct (主要 benchmark 模型, 28 layers, 4 KV heads, dim=128)
- Llama-3.1-8B-Instruct
- TinyLlama (测试用)
- Mistral-7B-Instruct

PCA calibration 按 `(layer, head_group, kind)` 存储，天然适配不同模型架构。

---

## 2. 数据流概览

```
原始 KV cache [layers, tokens, heads, dim] FP16
  │
  ├── 前 4 tokens → sink buffer (FP16 保留)
  ├── 后 128 tokens → window buffer (FP16 保留)
  └── 中间 tokens → 压缩流水线:
        │
        ▼
      RoPE Undo (仅 keys, 用 -sin 反转旋转)
        │
        ▼
      PCA Transform: centered = x - mean; coeffs = centered @ Vh.T
        │
        ▼
      DP Bit Allocation: eigenvalues + budget → per-component bit widths [0-16]
        │
        ▼
      Uniform Quantize: per-component affine 量化
        │
        ▼
      Bit Packing → Entropy Coding (zlib/LZMA/rANS triple picker)
        │
        ▼
      CompressedKVCache (bytes + metadata)
```

---

## 3. PCA Pipeline 详解

### 3.1 文件位置

- `src/pca.py`: PCA transform/inverse, RoPE 操作, `PCACalibrator` 类
- `src/calibrate.py`: `KVTCCalibrator` 高层封装

### 3.2 PCA 训练数据

**离线 one-time calibration**, 流程:
1. 选取 ~10 个文本样本
2. 前向传播获取 `past_key_values`
3. 对 keys 先做 RoPE inverse (消除位置旋转)
4. 按 `(layer, head_group, kind)` 分组拼接
5. 对每组做 SVD: `U, S, Vh = torch.linalg.svd(centered, full_matrices=False)`
6. `eigenvalues = S² / (n-1)`, `eigenvectors = Vh`

关键代码 (`pca.py:222-296`):
```python
def compute(self, bit_budget_ratio: float = 0.25) -> CalibrationData:
    data = torch.cat(sample_list, dim=0)  # [total_rows, dim]
    mean = data.mean(dim=0)
    centered = data - mean
    _, singular_values, vh = torch.linalg.svd(centered, full_matrices=False)
    eigenvalues = singular_values.square() / max(centered.shape[0] - 1, 1)
    # ...
    bit_widths = dp_bit_allocation(eigenvalues, bit_budget=total_bits, max_bits=16)
```

### 3.3 PCA 维度策略

- **每层每头独立 PCA** (默认 `head_group_size=1`)，最大化 per-head decorrelation
- 保留全部 dim 个 PCA component，但通过 DP bit allocation 将低方差 component 的 bits 设为 0（等效剪枝）
- 不做显式维度裁剪——裁剪由 DP 自动发现

### 3.4 RoPE 处理

- Keys: 压缩前 `apply_rope_inverse` (rotation by -θ)，解压后 `apply_rope` (rotation by θ)
- Values: 不使用 RoPE，无需处理
- 逆变换精确 (误差 < 1e-5，旋转矩阵的逆就是转置)

---

## 4. DP Bit Allocation Solver 详解

### 4.1 文件位置与行号

**精确 DP 版本**: `src/quantize.py:16-56` (41 行)  
**贪心近似版本**: `src/gpu_ops.py:10-57` (48 行)

### 4.2 精确 DP 版本 (`quantize.py:16-56`)

#### 输入
- `eigenvalues: Tensor[d]` — PCA eigenvalues (方差), 从 calibration 获取
- `bit_budget: int` — 总 bit 预算 (e.g., `dim * 16 * bit_budget_ratio`)
- `max_bits: int = 16` — 每 component 最大 bit 宽度
- `group_size: int = 1` — component 分组大小

#### 输出
- `widths: Tensor[d]` — per-component bit 分配, 每个值 ∈ [0, 16]

#### Error Function (核心)

```python
error = variance if bits == 0 else variance / (4 ** bits)
```

即: `E(i, b) = λ_i / 4^b`

- `λ_i` 是第 i 个 PCA component 的 eigenvalue (方差)
- `4^b` 是 b bits 量化带来的 MSE 降低因子 (每 bit 减半量化步长, MSE 减为 1/4)
- `bits == 0` 时 error 就是 variance 本身 (完全丢弃该 component)

#### DP 状态转移

```
dp[i][b] = min total MSE using components 0..i-1 with total budget b
```

转移:
```
dp[i][cost] = min over w in {0..16}:  dp[i-1][used] + λ_group / 4^w
              where cost = used + w * group_width
```

回溯得到每个 component 的 bit 分配。

#### 复杂度

`O(d × B × max_bits)` = O(128 × 512 × 16) ≈ 1M ops per entry. 足够快。

#### 完整代码

```python
def dp_bit_allocation(eigenvalues, bit_budget, max_bits=16, group_size=1):
    values = eigenvalues.detach().to(torch.float64).flatten()
    groups = _component_groups(values, group_size)
    max_budget = max(int(bit_budget), 0)
    num_groups = len(groups)
    inf = float("inf")
    dp = [[inf] * (max_budget + 1) for _ in range(num_groups + 1)]
    back = [[0] * (max_budget + 1) for _ in range(num_groups + 1)]
    dp[0][0] = 0.0
    for idx, group in enumerate(groups, start=1):
        variance = float(group.sum().item())
        width = group.numel()
        for used in range(max_budget + 1):
            if dp[idx - 1][used] == inf:
                continue
            for bits in range(0, max_bits + 1):
                cost = used + bits * width
                if cost > max_budget:
                    continue
                error = variance if bits == 0 else variance / (4 ** bits)
                candidate = dp[idx - 1][used] + error
                if candidate < dp[idx][cost]:
                    dp[idx][cost] = candidate
                    back[idx][cost] = bits
    best_budget = min(range(max_budget + 1), key=lambda b: dp[num_groups][b])
    # backtrack ...
    return widths
```

### 4.3 贪心近似版本 (`gpu_ops.py:10-57`)

生产管线 `pipeline_fast.py` 使用此版本。原理:

```
gain(i, b) = λ_i × 3 / 4^b
```

预计算所有 `(component, bit_level)` 的 marginal gain, flatten + topk 取 top-B 个, bincount 得 per-component bits。

复杂度 `O(B log(d × max_bits))`, 远快于精确 DP。

由于 gain 在 bit_level 上单调递减, 贪心解等价于最优解（标准可分离凸优化问题）。

### 4.4 调用链

1. **Calibration 时**: `pca.py:PCACalibrator.compute()` → `quantize.py:dp_bit_allocation()` → 存入 `PCAEntry.bit_widths`
2. **参考 pipeline**: `pipeline.py:compress()` → `quantize.py:dp_bit_allocation()` (每次压缩重新计算)
3. **GPU pipeline**: `pipeline_fast.py:compress()` → `gpu_ops.py:greedy_bit_allocation()` (用 calibration 的 bit_budget)

---

## 5. RABA 修改方案

### 5.1 RABA 核心思想

将 error function 从:
```
E(i, b) = λ_i / 4^b
```
修改为:
```
E(i, b, t) = (1 - p_r(t)) × λ_i / 4^b
```

其中 `p_r(t)` 是 token t 被 RAG cache 恢复的概率。对于高概率被恢复的 token，其量化误差在最终重建时会被精确值覆盖，因此可以分配更少的 bits。

### 5.2 需要修改的文件和函数

#### 修改 1: `src/quantize.py` — `dp_bit_allocation()`

**当前签名** (line 16):
```python
def dp_bit_allocation(eigenvalues, bit_budget, max_bits=16, group_size=1):
```

**RABA 签名**:
```python
def dp_bit_allocation(eigenvalues, bit_budget, max_bits=16, group_size=1, 
                      restoration_weights=None):
```

**修改位置** (line 42):
```python
# 当前:
error = variance if bits == 0 else variance / (4 ** bits)

# RABA:
if restoration_weights is not None:
    # weighted_variance = sum of (1 - p_r(t)) * lambda_i for tokens in group
    # 但注意: DP 是 per-component 的, p_r(t) 是 per-token 的
    # 这里需要将 per-token weights 聚合为 per-component weight
    weight = restoration_weights[idx - 1]  # 预计算的 weighted variance
    error = weight if bits == 0 else weight / (4 ** bits)
else:
    error = variance if bits == 0 else variance / (4 ** bits)
```

**关键设计问题**: DP 是 per-PCA-component 的, 但 `p_r(t)` 是 per-token 的。需要决定聚合方式:

- **方案 A (per-token DP)**: 将 DP 扩展为 per-token × per-component, 复杂度 O(T × d × B × 16), 对长序列不可行
- **方案 B (aggregate then DP)**: 将 weighted variance 预计算为 `weighted_λ_i = Σ_t (1 - p_r(t)) × pca_coeffs[t, i]²`, 替换 eigenvalue 输入 DP. 复杂度不变. **推荐方案**
- **方案 C (per-token bit allocation)**: 对每个 token 独立运行 DP (根据其 p_r), 复杂度 O(T × d × B × 16), 但 bit widths 变为 per-token, bit packing 变复杂

**推荐方案 B 的实现**:

```python
def compute_restoration_weighted_eigenvalues(
    pca_coeffs: torch.Tensor,      # [num_tokens, dim]
    restoration_probs: torch.Tensor, # [num_tokens]
) -> torch.Tensor:
    """计算 RABA weighted eigenvalues.
    
    weighted_λ_i = mean_t[(1 - p_r(t)) × pca_coeffs[t, i]²]
    """
    weights = (1 - restoration_probs).unsqueeze(1)  # [T, 1]
    weighted_var = (weights * pca_coeffs ** 2).mean(dim=0)  # [dim]
    return weighted_var
```

然后将 `weighted_eigenvalues` 传入 `dp_bit_allocation` 替代原始 `eigenvalues`。

#### 修改 2: `src/gpu_ops.py` — `greedy_bit_allocation()`

**当前签名** (line 10):
```python
def greedy_bit_allocation(eigenvalues, bit_budget, max_bits=16):
```

**RABA 修改**: 与精确 DP 类似, 传入 weighted eigenvalues 即可, gain 计算自动适配:
```python
gains_matrix = ev.unsqueeze(1) * 3.0 / (4.0 ** bit_levels.unsqueeze(0))
```
这里 `ev` 替换为 `weighted_ev` 即可。无需改内部逻辑。

#### 修改 3: `src/pipeline.py` 和 `src/pipeline_fast.py` — `compress()`

需要在 compress 方法中:
1. 新增 `restoration_probs` 参数 (per-token 概率向量)
2. 压缩前计算 `pca_coeffs`
3. 调用 `compute_restoration_weighted_eigenvalues` 得到 weighted eigenvalues
4. 将 weighted eigenvalues 传入 bit allocation

**`pipeline.py` 修改** (line 23):
```python
def compress(self, kv_cache, positions, restoration_probs=None):
```

在 line 68 附近, PCA transform 之后:
```python
pca_values = pca_transform(centered, entry.eigenvectors.to(rows.device))

# RABA: 如果提供了 restoration_probs, 用 weighted eigenvalues
if restoration_probs is not None:
    # restoration_probs shape: [middle_len]
    # rows shape: [middle_len * group_heads, dim]
    # 需要 expand p_r 到 group_heads
    pr_expanded = restoration_probs.repeat_interleave(group_heads)
    weighted_ev = compute_restoration_weighted_eigenvalues(pca_values, pr_expanded)
    bit_widths = dp_bit_allocation(weighted_ev, entry.bit_budget, group_size=1)
else:
    bit_widths = dp_bit_allocation(entry.eigenvalues.to(rows.device), entry.bit_budget, group_size=1)
```

**`pipeline_fast.py` 修改** (line 37): 同理, 但用 `greedy_bit_allocation`。

#### 修改 4: `src/calibrate.py` — 可选

Calibration 阶段不需要 RABA (p_r 在推理时才知道)。但可以在 calibration 时额外存储 PCA coefficient 统计, 以加速运行时的 weighted eigenvalue 计算。

### 5.3 额外传入参数

- `restoration_probs: torch.Tensor` — shape `[middle_len]`, 值域 [0, 1]
  - p_r(t) = 0: token t 不会被恢复, 正常压缩
  - p_r(t) = 1: token t 必定被恢复, 可分配 0 bits (极端情况)
  - p_r(t) ∈ (0, 1): 按概率加权降低该 token 的 error 权重

### 5.4 修改复杂度评估

| 文件 | 函数 | 改动行数 | 难度 |
|------|------|---------|------|
| `quantize.py` | `dp_bit_allocation` | ~10 行 (新增 weighted_ev 路径) | 低 |
| `gpu_ops.py` | `greedy_bit_allocation` | ~5 行 (传入 weighted_ev) | 低 |
| `pipeline.py` | `compress` | ~15 行 (参数 + weighted_ev 计算) | 低 |
| `pipeline_fast.py` | `compress` | ~15 行 (同上) | 低 |
| 新增 | `compute_restoration_weighted_eigenvalues` | ~10 行 | 低 |
| `common.py` | 数据结构 | 0 行 (不需要改) | — |
| `entropy.py` | — | 0 行 | — |

**总改动: ~55 行代码**, 主要集中在 bit allocation 调用处。不影响量化/编码/解码逻辑。

### 5.5 代码 Diff 草稿

```diff
--- a/src/quantize.py
+++ b/src/quantize.py
@@ -1,5 +1,6 @@
 """Quantization utilities for KVTC."""
 
+from __future__ import annotations
 from typing import List
 import torch
 from .common import QuantizationParams
@@ -12,6 +13,20 @@
     return [eigenvalues[i : i + group_size] for i in range(0, eigenvalues.numel(), group_size)]
 
 
+def compute_restoration_weighted_eigenvalues(
+    pca_coeffs: torch.Tensor,
+    restoration_probs: torch.Tensor,
+) -> torch.Tensor:
+    """Compute RABA weighted eigenvalues.
+    
+    weighted_lambda_i = mean_t[(1 - p_r(t)) * pca_coeffs[t, i]^2]
+    """
+    weights = (1 - restoration_probs).unsqueeze(1)  # [T, 1]
+    weighted_var = (weights * pca_coeffs ** 2).mean(dim=0)  # [dim]
+    return weighted_var
+
+
 def dp_bit_allocation(
     eigenvalues: torch.Tensor,
     bit_budget: int,
```

```diff
--- a/src/pipeline_fast.py
+++ b/src/pipeline_fast.py
@@ -37,7 +37,7 @@
-    def compress(self, kv_cache, positions):
+    def compress(self, kv_cache, positions, restoration_probs=None):
         # ... (unchanged until after PCA transform) ...
 
                         pca_values = pca_transform(centered, ev)
 
+                        # RABA: use weighted eigenvalues if restoration probs provided
+                        if restoration_probs is not None:
+                            pr = restoration_probs.to(pca_values.device)
+                            pr_expanded = pr.repeat_interleave(group_heads)
+                            weighted_ev = compute_restoration_weighted_eigenvalues(
+                                pca_values, pr_expanded
+                            )
+                            bit_widths = greedy_bit_allocation(weighted_ev, entry.bit_budget)
+                        else:
-                        bit_widths = greedy_bit_allocation(
-                            entry.eigenvalues.to(rows.device), entry.bit_budget,
-                        )
+                            bit_widths = greedy_bit_allocation(
+                                entry.eigenvalues.to(rows.device), entry.bit_budget,
+                            )
```

### 5.6 不影响的模块

- **PCA transform/inverse**: 不受影响, 仍用相同 eigenvectors
- **Quantization**: 不受影响, 仍用 uniform affine quantization
- **Entropy coding**: 不受影响, 仍对量化后的 bytes 做压缩
- **RoPE**: 不受影响
- **Token protection** (sink/window): 不受影响
- **Decompression**: 不受影响, metadata 中已存储 bit_widths

---

## 6. 压缩比评估

### 6.1 Benchmark 数据 (RTX 5090, Qwen2.5-7B)

| Config | K bits | V bits | 压缩比 | K Cosine | V Cosine | 质量 |
|--------|--------|--------|:------:|:--------:|:--------:|------|
| K1V2-FULL | 1 | 2 | **12.8x** | 0.9925 | 0.9120 | 低 |
| K1V3-FULL | 1 | 3 | **8.9x** | 0.9925 | 0.9874 | 可用 |
| K1V4-FULL | 1 | 4 | **7.1x** | 0.9925 | 0.9974 | 优 |
| K2V3-FULL | 2 | 3 | **7.2x** | 0.9970 | 0.9874 | 可用 |
| K2V4-FULL | 2 | 4 | **5.9x** | 0.9970 | 0.9974 | 优 |
| K3V4-FULL | 3 | 4 | **5.0x** | 0.9993 | 0.9974 | 优 |

### 6.2 8x 压缩比可达性评估

**K1V3 配置达到 8.9x**, cosine similarity 0.987-0.993, 质量为 "Good"。

**RABA 对 8x 目标的影响**:
- RABA 会让部分 token 分配更少 bits (高 p_r tokens) → 平均 bits 降低 → 压缩比提升
- 但总 bit budget 不变, 只是重分配: 高 p_r tokens 少分, 低 p_r tokens 多分
- 净效应: 如果大量 tokens 有高 p_r, 可以用更少的 bit budget 达到相同重建质量 → **提升有效压缩比**
- 在 K2V4 基础上 + RABA (假设 50% tokens 有 p_r > 0.5), 有效压缩比可达 7-9x 同时保持更高质量

**结论**: 8x 在 KVTC 可达范围内。K1V3 直接达到 8.9x, K2V4 + RABA 可在保持更高质量的同时逼近 8x。

### 6.3 Benchmark 脚本

```bash
# 完整 benchmark
python benchmarks/benchmark_v4.py --model Qwen/Qwen2.5-7B-Instruct --device cuda

# 指定配置
python benchmarks/benchmark_v3.py --model meta-llama/Llama-3.1-8B-Instruct --device cuda

# 单元测试 (无需 GPU)
pytest src/test_kvtc.py -v
```

---

## 7. Entropy Coding 流程

### 7.1 编码方法

三种编码器, triple-mode picker 选最小:

| 编码器 | 文件 | 说明 |
|--------|------|------|
| **zlib (DEFLATE)** | `entropy.py` | 默认, 压缩 level 6-9 |
| **LZMA2** | `ans_entropy.py:compress_best()` | Python `lzma` module |
| **rANS** | `ans_entropy.py:rans_encode()` | 纯 Python 实现, 16-bit precision |

Triple picker (`ans_entropy.py:184-230`):
```python
def compress_best(packed_bytes, level=6):
    candidates = []
    candidates.append((b"Z" + zlib.compress(packed_bytes, 9), "zlib"))
    candidates.append((b"L" + lzma.compress(packed_bytes, preset=6), "lzma"))
    candidates.append((b"A" + rans_encode(packed_bytes), "rans"))
    best = min(candidates, key=lambda x: len(x[0]))
    return best[0], ratio
```

1-byte tag 前缀标识编码器: `Z`=zlib, `L`=LZMA, `A`=rANS.

### 7.2 编解码 API

**编码**:
```python
from src.entropy import pack_bits, compress
from src.ans_entropy import compress_best

# Step 1: 将量化 indices 打包为 bytes
packed = pack_bits(indices_list, bit_widths)

# Step 2a: zlib 压缩
compressed, ratio = compress(packed, level=6)

# Step 2b: 或用 triple picker
compressed, ratio = compress_best(packed, level=6)
```

**解码**:
```python
from src.entropy import decompress, unpack_bits
from src.ans_entropy import decompress_best

# Step 1: 解压
packed = decompress(compressed, original_size)
# 或 triple picker
packed = decompress_best(compressed, original_size)

# Step 2: 解包
indices_list = unpack_bits(packed, bit_widths, lengths)
```

### 7.3 Bit Packing

`entropy.py:47-83`: 按 component 顺序逐个打包 (comp 0 所有 rows, 然后 comp 1, ...), 变宽 bit stream, 无对齐要求。

GPU 加速版在 `gpu_ops.py:fast_pack_bits()` 和 `triton_kernels.py:gpu_pack_variable_width()`。

---

## 8. Adaptive Budget (per-layer)

### 8.1 原理

`adaptive_budget.py`: 不同 layer 的 PCA eigenvalue spectrum "平坦度"不同:
- 平坦 (high Shannon entropy) → 难压缩 → 分配更多 bits
- 陡峭 (low entropy) → 易压缩 → 分配更少 bits

总预算守恒, 只做重分配。

### 8.2 API

```python
from src.adaptive_budget import apply_adaptive_budgets

key_diff, val_diff = apply_adaptive_budgets(
    calibration, key_bits_avg=2, value_bits_avg=4, strength=1.0
)
```

`strength=0` 为均匀分配, `strength=1` 为完全自适应。

---

## 9. 集成风险和注意事项

### 9.1 RABA 集成风险

| 风险 | 说明 | 缓解 |
|------|------|------|
| **DP 粒度不匹配** | DP 是 per-component, p_r 是 per-token | 用方案 B: 预聚合 weighted eigenvalues |
| **p_r 精度要求** | p_r 误估可能导致分配不当 | 加 clamp(0.01, 0.99) 防极端值 |
| **与 adaptive budget 交互** | RABA 和 adaptive budget 都改 bit allocation | 两者正交: adaptive 改 per-layer budget, RABA 改 per-component allocation |
| **解压不需要 p_r** | metadata 中已存 bit_widths | 正确, 解压路径零改动 |
| **Calibration 兼容** | RABA 修改运行时 bit allocation, 不改 calibration | 完全兼容, 无需重新 calibrate |

### 9.2 性能影响

- 压缩时增加 `weighted_eigenvalue` 计算: 一次矩阵乘 `O(T × d)`, 可忽略
- Bit allocation (贪心版) 运行时间不变
- 解压路径零开销

### 9.3 代码质量观察

- 代码组织清晰, pipeline → pca → quantize → entropy 模块化良好
- 两个 pipeline (参考 + GPU) 保持接口一致, 修改一个的经验可直接复用
- 38 个测试覆盖所有核心功能, 添加 RABA 后应增加对应测试
- `group_size=1` 默认设置意味着 per-head PCA, 对 RABA 的 per-token weight 聚合较友好

### 9.4 推荐实施顺序

1. 在 `quantize.py` 新增 `compute_restoration_weighted_eigenvalues()` 函数
2. 修改 `pipeline.py` (参考版) 的 `compress()` 方法, 添加 RABA 支持
3. 编写单元测试: weighted eigenvalues 计算正确性, RABA bit allocation 向后兼容 (p_r=0 时等价原版)
4. 验证: p_r=0 应产生与原版完全相同的 bit allocation
5. 修改 `pipeline_fast.py` (GPU 版)
6. 端到端测试: 带 RABA 的压缩-解压 roundtrip
