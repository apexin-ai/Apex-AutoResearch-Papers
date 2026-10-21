# code qwen32b bt and decomp

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen32b_bt_and_decomp_20260521T042835_result.json`
- **Structured JSON:** [`aa43f643279fd4b0278b.json`](../../sessions/aa/aa43f643279fd4b0278b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

```
| Analysis           | Metric           | Value    | 95% CI               | p          |
|--------------------|------------------|----------|----------------------|------------|
| BT Formality       | P(formal)        | 0.6647   | [0.5852, 0.7386]     | < 0.0001   |
| BT Verbosity       | P(verbose)       | 0.7732   | [0.7034, 0.8429]     | < 0.0001   |
| GEE Register       | academic OR      | 1.9053   | [1.0131, 3.5834]     | 0.0455     |
| GEE Register       | originality OR   | 5.7181   | [3.0207, 10.8244]    | < 0.0001   |
| GEE Formality      | formal OR        | 4.2008   | [1.9893, 8.8707]     | 0.0002     |
| GEE Formality      | originality OR   | 4.7041   | [2.2228, 9.9552]     | < 0.0001   |
```

关键发现：

- **BT**: Formality (66.5%) 和 verbosity (77.3%) 偏差均高度显著，verbosity 效应更强
- **GEE Register**: academic 偏好勉强显著 (OR=1.91, p=0.046)，但 originality bias 极强 (OR=5.72, p<0.0001) — 与之前方向分析一致（academic→conv 89.3% prefer original）
- **GEE Formality**: formal 偏好 (OR=4.20, p=0.0002) 和 originality bias (OR=4.70, p<0.0001) 都高度显著且效应量相近。对比 GPT-4o (formal OR=2.21, originality OR=1.82)，Qwen3-32B 两个效应都更强约 2 倍

脚本已保存在服务器 `csd_pipeline/qwen32b_analysis.py`，本地同步在 `csd_pipeline/qwen32b_analysis.py`。

---
