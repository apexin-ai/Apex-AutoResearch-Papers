# research wang fla version

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_wang-fla-version_20260518T122417_result.json`
- **Structured JSON:** [`91da60ae6283095e540b.json`](../../sessions/91/91da60ae6283095e540b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Wang et al. (arXiv 2507.06457) 使用的 fla 版本调查结果

### 1. 版本推断

论文提交日期：**2025-07-08**。模型 config.json 中 `transformers_version: "4.51.3"`。

fla 版本时间线：

| 版本 | 发布日期 | 与论文关系 |
|---|---|---|
| 0.2.0 | 2025-04-11 | 训练前 |
| 0.2.1 | 2025-04-23 | 训练中 |
| **0.2.2** | **2025-06-05** | **✅ 论文提交前最后一个发布版** |
| 0.3.0 | 2025-07-14 | 论文提交后 6 天才发布，**不可能用** |
| 0.3.1 | 2025-08-26 | — |
| 0.4.0 | 2025-10-27 | — |
| 0.5.0 | 2026-04-21 | — |

**结论：Wang et al. 训练时最可能用的是 fla 0.2.2**（或紧邻该版本的 main 分支 commit）。无显式 pin。

### 2. m-a-p config 中的实际 attn 字段

`m-a-p/1.3B-100B-GatedDeltaNet-hybrid-6-1/config.json` 的 `attn`:

```json
{
  "layers": [6, 11, 17, 23],
  "num_heads": 32,
  "num_kv_heads": 8,
  "qkv_bias": false,
  "rope_theta": 10000.0,
  "window_size": null
}
```

**没有 `D` 字段。** 在 0.2.2 / 0.3.0 / 0.5.0 / main 各版本的 `Attention.__init__` 中均无 `D` 参数，`GatedDeltaNetBlock` 从 `config.attn` 只读取上述 6 个 key。

> 你说的 "attn.D parameter" 不是 fla 的真实字段。如果运行报 `unexpected keyword argument 'D'` 或类似错误，应贴出完整 traceback 重新定位 —— 大概率不是 fla 版本问题本身，而是 GatedDeltaNet 层（不是 attn）的某个内部张量 `D`（如 mamba-style skip 项）在新版本被重命名/删除。

### 3. 主要 breaking changes

**0.2.x → 0.3.0**
- 多个 op 删除 `head_first` 参数（#337–#347）
- 注意力相关 op 中 `offsets` 重命名为 `cu_seqlens`
- GatedDeltaNet kernel 重构以去掉一次矩阵求逆（#433）

**0.3.x → 0.4.0**
- 引入 backend 调度系统（#741, #742）
- 引入 KDA (Kimi Delta Attention)
- GDN 增加 native GVA 支持，移除冗余 Q/K repeat（#812）
- GDN 增加 `use_gate_in_kernel` 融合 gate kernel（#813）

**0.4.x → 0.5.0**
- PyTorch 最低 2.7.0
- Triton-only → 多后端（TileLang, FlashKDA），新增 `FlashKDA` 后端
- 公开 op 中彻底删除 deprecated `head_first`（#853）
- MoBA / FlashMoBA 集成

### 4. 降级建议

```bash
pip install flash-linear-attention==0.2.2
```

或固定到论文提交前的 main 分支：

```bash
pip install "git+https://github.com/fla-org/flash-linear-attention.git@v0.2.2"
```

如需更精确复现，可用 2025-06-05 ~ 2025-07-08 之间的 commit。注意 0.3.2 之后 PyPI 拆分成 `fla-core` + `flash-linear-attention` 两个包，0.2.2 仍是单包，安装更简单。

### 5. 下一步建议

如果当前问题是加载 m-a-p checkpoint 失败：
1. 先 `pip install flash-linear-attention==0.2.2` 测试 checkpoint 是否能直接 load
2. 如果仍报 `D` 字段错误，把完整 traceback 贴出来 —— 多半是 GatedDeltaNet 内部 state_dict key 不匹配（如 `A_log`, `D`, `dt_bias` 等 mamba-lineage 张量），而不是 config dict 不匹配
3. 0.2.2 对应 transformers `>=4.45,<=4.51.x` 范围，建议同时 pin `transformers==4.51.3`

Sources:
- [arXiv 2507.06457 - Wang et al.](https://arxiv.org/abs/2507.06457)
- [m-a-p Hybrid Linear Attention collection](https://huggingface.co/collections/m-a-p/hybrid-linear-attention-research-686c488a63d609d2f20e2b1e)
- [flash-linear-attention PyPI](https://pypi.org/project/flash-linear-attention/)
- [fla-org/flash-linear-attention GitHub](https://github.com/fla-org/flash-linear-attention)
- [fla releases](https://github.com/fla-org/flash-linear-attention/releases)
- [fla FAQs](https://github.com/fla-org/flash-linear-attention/blob/main/FAQs.md)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "layers": [
      6,
      11,
      17,
      23
    ],
    "num_heads": 32,
    "num_kv_heads": 8,
    "qkv_bias": false,
    "rope_theta": 10000.0,
    "window_size": null
  }
}
```

</details>

---
