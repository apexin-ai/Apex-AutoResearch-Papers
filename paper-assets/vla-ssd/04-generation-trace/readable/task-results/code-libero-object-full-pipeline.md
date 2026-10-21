# code libero object full pipeline

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_libero_object_full_pipeline_20260520T230021_result.json`
- **Structured JSON:** [`1d94a44d153b3ab32fdf.json`](../../sessions/1d/1d94a44d153b3ab32fdf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**磁盘空间不足，无法直接执行。** 汇总如下：

### 磁盘状况
| 项目 | 大小 |
|------|------|
| checkpoints/ | 53GB |
| features/ | 141GB |
| data/libero | 30GB |
| results/ | 18GB |
| .hf_cache | 7.2GB |
| **可用** | **4.1GB** |

### 需要下载
- `openvla-7b-finetuned-libero-object` checkpoint: ~14GB
- `libero_object` 数据: ~6GB
- 结果存储空间: ~5GB
- **合计需腾出至少 25GB**

### 建议清理（最小侵入方案）
| 可删除项 | 大小 | 理由 |
|----------|------|------|
| `.hf_cache/` | 7.2GB | 模型已在 checkpoints/ 本地，缓存冗余 |
| `features/llama2base_libero_goal/` | 25GB | LLaMA2 对比实验已完成，结果已保存 |
| `checkpoints/openvla-7b-llama2base/` | 15GB | 同上 |
| **合计** | **47.2GB** | 清理后可用 ~51GB |

另外，我会设计**磁盘高效的 pipeline**：不预存 features 到磁盘（现有 Goal/Spatial 的 features 占了 141GB），而是模型加载后在内存中完成 extraction → probing → 保存结果 JSON 的完整流程。

**请确认是否可以删除上述三项。** 确认后我立即开始。

---
