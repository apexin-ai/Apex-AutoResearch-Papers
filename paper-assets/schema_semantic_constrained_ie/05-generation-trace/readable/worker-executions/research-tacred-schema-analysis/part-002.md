# research tacred schema analysis — Part 2 of 2

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../research-tacred-schema-analysis.md) · [Structured JSON](../../../sessions/95/950d7647cf6311fec9a7.json)

## Round 3

### Task result

_source line 367_

报告已生成并注册为 artifact。核心发现：

### Constraint Tightness 对比

| Dataset | Entity Types | Relations | Avg τ |
|---------|-------------|-----------|-------|
| SciERC | 6 | 7 | 0.333 |
| DocRED | 6 | 96 | 0.842 |
| **TACRED** | **17** | **41** | **0.994** |

TACRED 是极端紧约束——41 个 relation 中 20 个只有 1 个 valid pair。

### 关键判断

1. **格式兼容**: TACRED schema 可直接转为 `ontology_constraints.json`，无需改 OntologyCompiler
2. **核心风险**: τ≈0.994 意味着 grammar-first fallback 几乎 100% 触发，semantic constraint layer 形同虚设
3. **First-token 冲突**: 17 entity types 中 11 个有首字符冲突（C×4, P×2, N×2 等），TypeConstraintProcessor 需要扩展 multi-token masking 或重命名类型
4. **no_relation 无需特殊处理**: OntoCoDec 不在 schema 中定义 no_relation，生成式框架通过"不输出 triple"隐式表达
5. **数据集推荐**: 首选 TACREV（schema 不变 + 修正标注），三个版本都需要 LDC 原版数据（$25）

### 战略建议

如果目标是 **tightness spectrum 验证**（论文 §5 的 cross-dataset analysis），TACRED 是理想的极端数据点，构成 0.333→0.842→0.994 的完整谱系。如果目标是 **展示实用价值**，TACRED 不适合——约束太紧，OntoCoDec 的 semantic layer 无法生效。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 722139,
  "duration_api_ms": 860110,
  "num_turns": 8,
  "stop_reason": "end_turn",
  "session_id": "19e390c5-d686-4b51-bf3c-108389a72194",
  "total_cost_usd": 3.938360499999999,
  "usage": {
    "input_tokens": 12,
    "cache_creation_input_tokens": 34075,
    "cache_read_input_tokens": 235326,
    "output_tokens": 9487,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 34075,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 535,
        "cache_read_input_tokens": 38268,
        "cache_creation_input_tokens": 7648,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 7648
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1387899,
      "outputTokens": 31159,
      "cacheReadInputTokens": 2124985,
      "cacheCreationInputTokens": 122482,
      "webSearchRequests": 45,
      "costUSD": 2.3592950000000004,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9964,
      "outputTokens": 18103,
      "cacheReadInputTokens": 1093791,
      "cacheCreationInputTokens": 84764,
      "webSearchRequests": 0,
      "costUSD": 1.5790655000000002,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "2f5cfa7e-2731-4f54-a7f1-f7bb1a44251b"
}
```

</details>

---
