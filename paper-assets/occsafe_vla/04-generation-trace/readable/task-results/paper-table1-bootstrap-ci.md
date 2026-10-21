# paper table1 bootstrap ci

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_table1_bootstrap_ci_20260523T065221_result.json`
- **Structured JSON:** [`b23a6499aec019de959b.json`](../../sessions/b2/b23a6499aec019de959b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

变更总结：

1. **开头段落**（L8）：将"formal significance requires additional replications"替换为 bootstrap CI 方法描述。

2. **Table 1**（L20-37）：
   - 新增 `$95\%$ CI` 列，格式 `[.776, .817]`（省略前导零，紧凑）
   - Cutoff 行补充了 ±std（TSR ±0.004, CAR ±0.021）
   - Caption 加入 bootstrap 方法说明和 Cutoff † 脚注更新

3. **Gradient flow 段落**（L12）：
   - Full OCC vs Vanilla：明确 "$+$1.7pp is directionally positive but not statistically significant (bootstrap 95\% CI for the pairwise difference includes zero)"
   - Detach OCC：明确 "statistically significant degradation" + "bootstrap 95\% CIs for all pairwise differences... exclude zero"
   - 修复了 em-dash `---` 为括号格式

4. **Label content 段落**（L14）：补充 "whose bootstrap CI overlaps broadly"，修复 em-dash。

Mechanism analysis（L59-67）、Cutoff（L113-119）、Depth（L127-133）各段数值和措辞与 CI 结果一致，无需修改。

---
