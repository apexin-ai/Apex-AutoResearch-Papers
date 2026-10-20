# experiment r1 distill fix v2

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_r1-distill-fix-v2_20260521T145252_result.json`
- **Structured JSON:** [`00b2aa29ced82196b18b.json`](../../sessions/00/00b2aa29ced82196b18b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Re-extraction 稳定运行。所有问题（除前两个外）都达到 12/12 traces 成功提取。ETA ~28 分钟。

**汇报：**

1. **vLLM 重启** ✓
   - 旧进程 441147 已 kill
   - 新 PID: 449110, GPU 3: 88237/97887 MiB
   - max_model_len=16384 + VLLM_USE_FLASHINFER_SAMPLER=0（Blackwell GPU 兼容）
   - model id: `/root/autodl-tmp/models/deepseek-ai/DeepSeek-R1-Distill-Llama-8B`

2. **发现额外问题**：vLLM 0.21.0 + R1-Distill 存在 BPE 编码 bug——输出包含原始 BPE 字符（Ġ=空格, Ċ=换行），导致 extraction JSON 解析全部失败。原始 pipeline 只完成 94/204 个问题（vLLM 重启期间丢失 110 个）。

3. **Extraction 修复方案**：
   - 写了 `reextract_bpe_fix.py`：先 BPE 解码 R1-Distill 的 traces，然后用 **Mistral-7B**（port 8000）做 extraction（R1-Distill 本身因 reasoning-first 特性无法直接输出 JSON）
   - Dry-run 验证通过：folio_0 从 0 constraints → **66 constraints (8/12 traces)**
   - 后续问题稳定达到 **12/12 traces，36-73 constraints/problem**

4. **Re-extraction 正在后台运行**
   - PID: 451915
   - 进度: 8/93，ETA ~28 分钟
   - 输出目录: `results/exp_r1_distill_8b_sica/per_trace_constraints_v2/`
   - 日志: `/tmp/reextract_r1_distill.log`
   - 完成后会生成 `reextraction_summary.json` 包含 extraction_rate

5. **缺失数据**：110/204 个问题没有 SC traces（pipeline 在 vLLM 重启期间未生成）。如需完整 204 问题的结果，需要重跑完整 pipeline（trace 生成 + extraction）。

---
