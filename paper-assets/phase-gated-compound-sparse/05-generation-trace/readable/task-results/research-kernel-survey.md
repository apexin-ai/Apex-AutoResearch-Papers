# research kernel survey

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_kernel-survey_20260513T191213_result.json`
- **Structured JSON:** [`de6b87bb7a5611125964.json`](../../sessions/de/de6b87bb7a5611125964.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

# M4 Kernel Integration 调研报告

## 1. 现有实现清单

### 1.1 Attention Head Pruning

| 项目 | URL | 关键特性 | 匹配度 |
|------|-----|---------|--------|
| **Block-Sparse FlashAttention (BSFA)** | [arxiv 2512.07011](https://arxiv.org/abs/2512.07011) | 基于 block-mask 跳过计算块，50% 计算节省，Llama-3.1-8B 上 1.1-1.24x 加速 | **中**——block 粒度而非 head 粒度 |
| **aiha-lab/Attention-Head-Pruning** | [GitHub](https://github.com/aiha-lab/Attention-Head-Pruning) | Layer-wise head pruning for language modeling，训练时剪枝 | **低**——关注训练而非推理 kernel |
| **HiP Attention** | [arxiv 2406.09827](https://arxiv.org/html/2406.09827v1) | 层次化树搜索生成动态 sparse mask，sub-quadratic attention | **中**——动态稀疏但不是 head-level |
| **FlashAttention MQA/GQA** | [GitHub](https://github.com/Dao-AILab/flash-attention) | 原生支持 Q heads > KV heads，可传入 head 子集的 Q/K/V 切片 | **高**——可通过 tensor slicing 实现 head 子集计算 |

**关键发现**: FlashAttention 没有原生的 "head subset" 参数，但因为 Q/K/V 是按 `(batch, seqlen, nheads, headdim)` 传入的，**可以在调用前对 head 维度做 slicing/indexing**，只传入 active heads 的 Q/K/V。对于 GQA 模型，需要调整 head 映射关系。这是最简单的实现路径。

### 1.2 KV Cache Eviction

| 项目 | URL | 关键特性 | 匹配度 |
|------|-----|---------|--------|
| **MUSTAFAR** | [GitHub](https://github.com/dhjoo98/mustafar) | unstructured KV sparsity (70%)，Triton 压缩 kernel + CUDA batch SpMV kernel，bitmap sparse format | **高**——有完整的 sparse attention CUDA kernel |
| **PagedEviction** | [arxiv 2509.04377](https://arxiv.org/html/2509.04377v1) | block-level KV eviction，无需修改 attention kernel，proxy importance metric | **中**——避免改 kernel，与我们目标不同 |
| **NVIDIA kvpress** | [GitHub](https://github.com/NVIDIA/kvpress) | 20+ 压缩方法统一接口，prefill 阶段压缩，有 head-specific 请求 (issue #7) | **中**——Python 层面，非 kernel 层面 |
| **SGLang KV Pruning RFC** | [Issue #19887](https://github.com/sgl-project/sglang/issues/19887) | fast KV-cache pruning proposal，2026年3月提出，仍在开发中 | **低**——RFC 阶段 |
| **vLLM Sparse KV RFC** | [Issue #5751](https://github.com/vllm-project/vllm/issues/5751) | sparse KV cache framework proposal | **低**——RFC 阶段 |
| **TurboQuant-vLLM** | [GitHub](https://github.com/varjoranta/turboquant-vllm) | fused CUDA kernels for KV cache quantization，vLLM 集成 | **低**——量化而非 eviction |

**关键发现**: **MUSTAFAR 是最值得参考的实现**。它的 "load-as-compressed, compute-as-dense" pipeline（压缩数据从 global memory 加载到 registers → shared memory 解压 → Tensor Core 密集计算）与我们的 compound sparsity 目标高度吻合。

### 1.3 Compound Sparsity（Head Pruning + KV Eviction 联合）

**确认：没有找到 head pruning 与 KV eviction 联合执行的现成实现。** 这确实是我们的 novelty 点。

相关但不同的工作：
- **SparK** ([arxiv 2508.15212](https://arxiv.org/html/2508.15212))：Query-Aware Unstructured Sparsity + Recoverable KV Cache Channel Pruning，但是 channel 维度而非 head+token 维度
- **Write-Gated KV** ([arxiv 2512.17452](https://arxiv.org/html/2512.17452v1))：Admission + Selection + Eviction 三阶段 compound，概念上最接近但没有 head pruning
- **OBCache** ([arxiv 2510.07651](https://arxiv.org/abs/2510.07651))：Joint key-value pruning，per-token joint eviction 但不涉及 head pruning

## 2. API 可行性分析

### FlashAttention (v2/v3/v4)

| 能力 | 支持情况 | 备注 |
|------|---------|------|
| Head 子集计算 | **间接支持** | 调用前 slice Q/K/V 的 head 维度，不需要 API 改动 |
| Variable-length KV | **支持** | `flash_attn_varlen_func_with_kvcache` 支持 ragged KV |
| Paged KV cache | **支持** | `flash_attn_with_kvcache` 原生 page table |
| Block-sparse mask | **FA4 支持** | FA4 接受 block-mask metadata，最小块 256×128 (Blackwell) / 128×128 (Triton) |
| 跳过 evicted KV 位置 | **不直接支持** | 需要压实 KV cache（去除被 evict 的位置）后传入，或用 block-sparse mask |

### FlashInfer

| 能力 | 支持情况 | 备注 |
|------|---------|------|
| Ragged KV | **支持** | `BatchPrefillWithRaggedKVCacheWrapper`，indptr 数组管理变长序列 |
| Paged KV | **支持** | BSR 格式存储 |
| Block-sparse attention | **支持** | Variable block-sparse patterns |
| Head 子集 | **不直接支持** | 同 FA，需要 tensor slicing |
| Skip-softmax sparsity | **支持** | threshold 参数控制 |

### FlexAttention (PyTorch)

| 能力 | 支持情况 | 备注 |
|------|---------|------|
| Custom block mask | **支持** | `create_block_mask` + `score_mod` 回调 |
| Fused kernel | **支持** | torch.compile 自动生成 fused FA kernel |
| Head-specific mask | **支持** | mask_mod 接收 head index 参数 |
| 自动反向传播 | **支持** | 自动生成 backward |

**FlexAttention 是最灵活的 API**——可以用 `mask_mod(b, h, q_idx, kv_idx)` 同时编码 "哪些 head active" 和 "哪些 KV 位置被 evict"，torch.compile 会生成 fused kernel。但性能上限低于手写 CUDA。

## 3. 推荐路线

### 阶段一：快速原型（1-2 周）

**用 FlexAttention 做 compound sparsity 原型。**

理由：
- `mask_mod(b, h, q_idx, kv_idx)` 天然支持 per-head × per-position 的 2D 稀疏模式
- 不需要写 CUDA，torch.compile 自动优化
- 可以快速验证 compound sparsity 的 accuracy/perplexity 收益
- 支持自动 backward，方便做 fine-tuning 实验

```python
def compound_mask(b, h, q_idx, kv_idx):
    head_active = head_mask[b, h]        # head pruning
    kv_active = kv_mask[b, kv_idx]       # KV eviction
    return head_active & kv_active
```

### 阶段二：组合现有 API（2-3 周）

**用 FlashAttention head slicing + variable-length KV 组合。**

- 对 pruned 模型，只传入 active heads 的 Q/K/V（zero-copy view）
- 对 evicted KV，压实 KV cache（去除被 evict 的位置）后调用 `flash_attn_varlen_func`
- 优势：利用 FA 的极致性能，避免写 kernel
- 劣势：KV 压实有 memcpy 开销，head slicing 在 GQA 下需要额外映射逻辑

### 阶段三：Custom Triton Kernel（3-4 周）

**如果阶段二的压实开销不可接受，写 Triton kernel。**

参考 MUSTAFAR 的 bitmap sparse format：
- 用 bitmap 标记 active KV 位置，load-as-compressed → compute-as-dense
- 在 head 维度加入 skip 逻辑（inactive head 直接跳过 tile）
- Triton 优势：**自动编译到 sm_90/sm_100+**，无需为不同架构写不同 kernel

参考实现：
- [native-sparse-attention-triton](https://github.com/XunhaoLai/native-sparse-attention-triton)：完整的 Triton sparse attention，含 KV cache 管理
- [hbsattn](https://github.com/zhengqigao/hbsattn)：高性能 Block Sparse Attention Triton kernel
- MUSTAFAR 的 Triton 压缩 kernel（`/kernel` 目录）

### 阶段四：CUDA C++ Kernel（仅在必要时）

**仅当 Triton 无法达到 FA4 级性能时才考虑。**

FA4 在 Blackwell 上达到 1613 TFLOPS（71% utilization），Triton 被 FA4 超过 2.7x。如果我们的 benchmark 需要极致性能，可能需要基于 CuTeDSL 写 SM100 专用 kernel。但开发成本极高，建议先用 Triton 验证 idea。

## 4. 架构兼容性

| 架构 | FlashAttention | FlashInfer | Triton | 备注 |
|------|---------------|------------|--------|------|
| **sm_90 (Hopper, H100/H20)** | FA3 ✅ | ✅ | ✅ | 当前 benchmark 目标 |
| **sm_100 (Blackwell datacenter, B200)** | FA4 ✅ | ✅ (MLSys contest) | ✅ | FA4 用 CuTeDSL，利用 TMEM + tcgen05 |
| **sm_120/121 (Blackwell consumer, RTX 5090)** | FA4 ❌ (无 TMEM) | 待确认 | ✅ | Triton 自动适配 |

**关键风险**: FA4 仅支持 datacenter Blackwell (sm_100)，不支持 consumer Blackwell (sm_120)。Triton kernel 无此限制，自动编译到所有架构。FA4 的最小 sparse block 在 Blackwell 上是 256×128，比 Hopper 上的 128×128 更粗，对细粒度 KV eviction 不利。

## 5. 总结建议

| 维度 | 推荐 |
|------|------|
| **原型验证** | FlexAttention（最快出结果） |
| **生产 kernel** | Triton（跨架构 + 开发速度 + 足够的性能） |
| **性能极限** | FA4 CuTeDSL（仅 sm_100，开发成本高） |
| **最有价值的参考** | MUSTAFAR（bitmap sparse KV + Triton/CUDA kernel）、native-sparse-attention-triton |
| **novelty 确认** | compound sparsity (head pruning × KV eviction) 没有现成实现 ✅ |

Sources:
- [Block Sparse FlashAttention](https://arxiv.org/abs/2512.07011)
- [FlashAttention GitHub](https://github.com/Dao-AILab/flash-attention)
- [FlashAttention-4 Blackwell Guide](https://pytorch.org/blog/flexattention-flashattention-4-fast-and-flexible/)
- [FlashInfer GitHub](https://github.com/flashinfer-ai/flashinfer)
- [FlashInfer Paper](https://arxiv.org/pdf/2501.01005)
- [MUSTAFAR Paper](https://arxiv.org/abs/2505.22913)
- [MUSTAFAR GitHub](https://github.com/dhjoo98/mustafar)
- [native-sparse-attention-triton](https://github.com/XunhaoLai/native-sparse-attention-triton)
- [hbsattn (Block Sparse Attention Triton)](https://github.com/zhengqigao/hbsattn)
- [PagedEviction](https://arxiv.org/html/2509.04377v1)
- [NVIDIA kvpress](https://github.com/NVIDIA/kvpress)
- [SGLang KV Pruning RFC](https://github.com/sgl-project/sglang/issues/19887)
- [vLLM Sparse KV RFC](https://github.com/vllm-project/vllm/issues/5751)
- [FlexAttention PyTorch Blog](https://pytorch.org/blog/flexattention/)
- [Tencent flex-block-attn](https://github.com/Tencent-Hunyuan/flex-block-attn)
- [SparK](https://arxiv.org/html/2508.15212)
- [OBCache](https://arxiv.org/abs/2510.07651)
- [Write-Gated KV](https://arxiv.org/html/2512.17452v1)
- [HiP Attention](https://arxiv.org/html/2406.09827v1)
- [Awesome KV Cache Compression](https://github.com/October2001/Awesome-KV-Cache-Compression)
- [FA4 Blackwell sm_100 issue](https://github.com/Dao-AILab/flash-attention/issues/1853)
- [FlashInfer Attention API Docs](https://docs.flashinfer.ai/api/attention.html)

---
