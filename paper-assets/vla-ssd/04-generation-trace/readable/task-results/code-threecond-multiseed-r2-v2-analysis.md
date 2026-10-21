# code threecond multiseed r2 v2 analysis

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_threecond_multiseed_r2_v2_analysis_20260518T084856_result.json`
- **Structured JSON:** [`151a0fa83dbc676180dc.json`](../../sessions/15/151a0fa83dbc676180dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐了。以下是完整分析。

```
=== threecond_multiseed_r2_v2 分析 ===

注：L0 三条件完全相同（共享 vision encoder 输出），下表 Peak Layer 排除 L0。

条件       | Peak Layer | Peak R² (mean±std)  | L0 R² (shared)
-----------|-----------|---------------------|----------------
trained    | L9        | 0.6434 ± 0.0137     | 0.6451 ± 0.0084
llama2base | L12       | 0.6344 ± 0.0131     | 0.6451 ± 0.0084
untrained  | L32       | 0.5885 ± 0.0071     | 0.6451 ± 0.0084

（untrained 若排除 L32 异常值，次高 peak = L1: 0.5470 ± 0.0080）

--- vs v1 对比 ---
- trained peak: v1 = L10, 0.548±0.012 → v2 = L9, 0.6434±0.0137 (+17.4%)
- split 修复效果确认，v1 的 random shuffle 导致系统性低估

--- 层级 profile 特征 ---
- trained: L0-L15 高位平台 (~0.62-0.65)，L16+ 渐降至 ~0.47-0.52。非尖锐 inverted-U，更接近 plateau-then-decline
- llama2base: 全 33 层极其稳定 (~0.56-0.64)，std 全部 < 0.03
- untrained: L0 后迅速退化，L10-L13 出现负 R²（mean -0.09 to 0.22），L14+ 大幅震荡，L32 异常回升至 0.5885

--- Hypothesis 验证 ---
- trained > llama2base > untrained（at peaks excl L0）: YES
  0.6434 > 0.6344 > 0.5885（或 0.5470 若排除 L32）
- layer-by-layer gradient (L1-L20): 大部分层成立
  例外：L12 llama2base(0.6344) > trained(0.6205)
  L25+ llama2base 有时 > trained
  L32: untrained(0.5885) > llama2base(0.5513) > trained(0.5240) — 完全反转
- seed variance 低 (std < 0.03):
  - trained: 27/33 层 < 0.03，但 L23(0.080) L27(0.068) L31(0.067) 偏高
  - llama2base: 33/33 层 < 0.03 ✓
  - untrained: 大量层 std > 0.1，最高 0.377 ✗
  → PARTIAL — trained 和 llama2base 低方差，untrained 极高方差
- max std across all: 0.377 (untrained L22)

--- vs 原始单 seed 参考值 ---
                    原始单seed    v2 multi-seed (excl L0)
trained peak:       ~0.655        0.6434 (接近，合理)
llama2base peak:    ~0.53-0.54    0.6344 (显著更高!)
untrained peak:     ~0.49-0.53    0.5470 (L1, 一致) / 0.5885 (L32, 异常)

llama2base 原始参考值偏低原因待查（可能原始单 seed 也用了 shuffle split）

--- 关键发现 ---
1. L0 完全相同 = 三模型共享 vision encoder，vision-only baseline R²=0.645
2. trained-llama2base gap 极小（peak diff = 0.009），robot fine-tuning 对 action encoding 增益有限
3. llama2base 全层稳定 ~0.60，说明 Llama2 pretrained representations 本身已保留大量 action-relevant 信息
4. untrained 中间层崩溃（负 R² + 巨大方差）= 随机权重破坏信息流
5. untrained L32 异常高且低方差（0.5885±0.007）— 可能 final layer norm / projection 恢复了部分结构，需调查

--- 结论 ---
建议 conclusion: partial success
- gradient 在 peak 层成立 ✓，但 trained-llama2base 间距极小（not statistically significant at 0.009 diff）
- untrained 高方差是最强信号（random weights → chaotic representations）
- 主要故事可能不是 "trained 编码了更好的 action info"，而是 "pretrained LLM 已经保留了 vision encoder 的 action info，fine-tuning 只是微调"

建议 notes:
- trained vs llama2base 差异可能需要统计检验（paired t-test across layers）确认是否显著
- untrained L32 anomaly 需要单独调查
- 考虑是否需要更多 seeds（当前 3 seeds 统计力有限）
```

---
