# investigate c4 data authenticity

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_c4_data_authenticity_20260514T085841_result.json`
- **Structured JSON:** [`977bf664e7f16bb2ede6.json`](../../sessions/97/977bf664e7f16bb2ede6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 调查报告

### 1. 结论：c4_calibration.json 是 WikiText 冒充 C4

**铁证：**
- 第一条数据是 `= Valkyria Chronicles III =`，这是 WikiText-2/WikiText-103 的标志性开头文章
- 包含 WikiText 特有的 `@-@` tokenization 标记
- 服务器 HF 缓存 (`/root/autodl-tmp/.hf_cache/datasets/`) 中**完全没有 C4 数据集**，只有 `wikitext` 目录
- WikiText 缓存创建时间 `03:54`，`c4_calibration.json` 创建时间 `03:55`——相隔仅 1 分钟，强烈指向从 WikiText 生成后误命名为 C4
- 代码库中**没有任何脚本负责生成 `c4_calibration.json`**——文件来源不可追溯

### 2. plan_007 影响：全部 C4 相关结果无效

受影响的脚本和结果：

| 脚本 | 用途 | 引用位置 |
|------|------|----------|
| `run_c4_cross_dataset.py` (plan_007) | C4 calibration profiling + MCKP | `C4_CALIBRATION = "c4_calibration.json"` (line 13) |
| `run_c4_phase2_4.py` | 加载 c4_profiling_results.json | 依赖 plan_007 产出 |
| `run_cross_domain.py` (plan_010) | Cross-domain robustness | `C4_CAL_PATH = "/root/ratekv/c4_calibration.json"` (line 35) — 用于 calibration 和 eval |
| `run_mvp.py` | MVP 实验 | `--calibration_data` 默认值是 `c4_calibration.json` |

**受污染的结果文件：**
- `c4_profiling_results.json` — profiling 用的实际是 WikiText
- `c4_eval_results.json` — "C4 cross-dataset eval" 实际是 WikiText-on-WikiText（同域）

**核心问题**：`run_cross_domain.py` 声称 "Condition A: Calibrate on C4 → eval on WikiText-2"，实际是 WikiText-on-WikiText，所以 cross-domain robustness 的 claim 完全无效——calibration 和 evaluation 来自同一数据分布。

### 3. 真 C4 数据状态

已下载成功：
- **路径**：`/root/ratekv/c4_calibration_real.json`
- **大小**：371 KB，200 条真实 C4 validation 数据
- **WikiText 标记检测**：0/200（确认无 WikiText 污染）
- **来源**：HuggingFace `allenai/c4` en validation split（shard 0）

### 4. 建议后续操作

1. **备份旧文件**：`mv c4_calibration.json c4_calibration_WIKITEXT_WRONG.json`
2. **替换为真数据**：`mv c4_calibration_real.json c4_calibration.json`
3. **重跑 plan_007**：用真正的 C4 数据重新 profiling + MCKP + eval
4. **重跑 plan_010**（cross-domain）：用真 C4 数据验证 cross-domain robustness claim
5. **审查论文稿中所有引用 C4 结果的段落**——当前数据不支持 cross-domain 结论

---
