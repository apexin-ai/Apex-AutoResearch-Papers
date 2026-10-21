# diag s2 minkpp integrity check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_s2_minkpp_integrity_check_20260516T225939_result.json`
- **Structured JSON:** [`908bd8313d12dd128e40.json`](../../sessions/90/908bd8313d12dd128e40.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## s2_minkpp 诊断结果

### Merged files 是否包含 s2？
- Llama d005 MMLU: **有** s2_minkpp（值 = -1.690）
- Llama d005 ARC: **有** s2_minkpp（值 = -1.513）
- Llama d005 GSM8K: **有** s2_minkpp（值 = -1.506）
- Llama d000 MMLU: **有** s2_minkpp（值 = -1.665）
- Qwen 0.5B_d000_s42 MMLU: **有** s2_minkpp（值 = 1.781）
- Qwen 1.5B_d000_s42 MMLU: **有** s2_minkpp（值 = 1.924）

### 独立 s2 文件存在性
| 模型 | arc | gsm8k | mmlu |
|------|-----|-------|------|
| Llama d000 s42 | ✓ 250KB | ✓ 272KB | ✓ 2.8MB |
| Llama d005 s42 | ✓ 250KB | ✓ 272KB | ✓ 2.8MB |
| Llama d025 s42 | ✓ 250KB | ✓ 272KB | ✓ 2.8MB |
| Llama d100 s42 | ✓ 250KB | **缺失** | ✓ 2.8MB |
| Qwen 0.5B s42 (all doses) | 旧命名 `signal_minkpp_*` | 同左 | 同左 |
| Qwen 1.5B s42 (all doses) | 旧命名 `signal_minkpp_*` | 同左 | 同左 |
| Qwen 3B a32 s42 | ✓ | ✓ | ✓ |
| Qwen 0.5B s123 (all doses) | ✓ | ✓ | ✓ |
| Qwen 1.5B s123 (all doses) | ✓ | ✓ | ✓ |
| Qwen 0.5B-Instruct | ✓ | ✓ | ✓ |
| Qwen 1.5B-Instruct | ✓ | ✓ | ✓ |

### Bug 范围结论
- [x] **所有数据安全，s2 存在**（merged files 均含 s2_minkpp 字段）
- [ ] ~~仅影响 HF_OFFLINE 新提交~~
- [ ] ~~影响所有 Llama signals~~
- [ ] ~~影响 Qwen + Llama 全部~~

**唯一缺口**: Llama d100 s42 的 GSM8K 整体未计算（不止 s2，而是 s1/s2/s4/merged 全部缺失）。这是任务未完成，不是 s2 特定 bug。

### tokenizer 依赖分析

`s2_minkpp.py` 通过 `utils.load_model_and_tokenizer()` 加载 tokenizer：
- 调用 `AutoTokenizer.from_pretrained(model_path, cache_dir="/root/autodl-tmp/.hf_cache", trust_remote_code=True)`
- 代码中 **无** `HF_HUB_OFFLINE` 或 `local_files_only` 参数
- 模型文件在本地 cache (`/root/autodl-tmp/.hf_cache`)，tokenizer 从本地加载无网络依赖
- **不存在 HF_OFFLINE 导致 tokenizer 加载失败的风险**

### 结论
**假设不成立**。s2_minkpp 信号在所有已完成的 compute_signals 任务中都正常存在。Qwen s42 目录中的旧文件命名 (`signal_minkpp_*` vs `signal_s2_minkpp_*`) 不影响 merged 数据。需要补的仅有 Llama-3.2-3B_d100_s42 的 GSM8K 全部信号。

---
