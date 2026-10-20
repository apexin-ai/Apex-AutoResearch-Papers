## Entity Type Tokenization 分析

### 背景
WikiEvents 27 种 entity types（全大写 3-5 字母缩写）：
ABS, AML, BAL, BOD, COM, CRM, EVENT, FAC, GPE, INF, LAW, LOC, MHI, MON, NAT, ORG, PER, PLA, PTH, RES, SEN, SID, SIDE, TTL, VAL, VEH, WEA

---

### Mistral tokenizer (SentencePiece, LlamaTokenizerFast, vocab=32768)

| Entity Type | Bare 1st (token) | Gen-context 1st (token) | Match? |
|---|---|---|---|
| ABS | 1098 ('A') | 2960 ('AB') | MISMATCH |
| AML | 1098 ('A') | 3622 ('AM') | MISMATCH |
| BAL | 1133 ('B') | **29528 ('B')** | MISMATCH |
| BOD | 1133 ('B') | **29528 ('B')** | MISMATCH |
| COM | 16692 ('COM') | 19219 ('COM') | MISMATCH |
| CRM | 12775 ('CR') | 6496 ('CR') | MISMATCH |
| EVENT | 19461 ('EVENT') | 11953 ('EVENT') | MISMATCH |
| FAC | 1169 ('F') | 29533 ('F') | MISMATCH |
| GPE | 1188 ('G') | 29545 ('G') | MISMATCH |
| INF | 3461 ('IN') | 1543 ('IN') | MISMATCH |
| LAW | 16552 ('LA') | 9191 ('LA') | MISMATCH |
| LOC | 7575 ('LO') | 10436 ('LOC') | MISMATCH |
| MHI | 1119 ('M') | 29523 ('M') | MISMATCH |
| MON | 26027 ('MON') | 18117 ('MON') | MISMATCH |
| NAT | 25367 ('NAT') | 29527 ('N') | MISMATCH |
| ORG | 4762 ('OR') | 1785 ('OR') | MISMATCH |
| PER | 22783 ('PER') | 7280 ('PER') | MISMATCH |
| PLA | 1135 ('P') | 4666 ('PL') | MISMATCH |
| PTH | 1135 ('P') | 29521 ('P') | MISMATCH |
| RES | 21076 ('RES') | 9972 ('RES') | MISMATCH |
| SEN | 1086 ('S') | **29503 ('S')** | MISMATCH |
| SID | 1086 ('S') | **29503 ('S')** | MISMATCH |
| SIDE | 1086 ('S') | **29503 ('S')** | MISMATCH |
| TTL | 1088 ('T') | 29506 ('T') | MISMATCH |
| VAL | 19548 ('VAL') | 4436 ('VAL') | MISMATCH |
| VEH | 1318 ('V') | 4496 ('VE') | MISMATCH |
| WEA | 1162 ('W') | 7399 ('WE') | MISMATCH |

**ALL 27 entity types** have bare ≠ generation-context token IDs（SentencePiece 上下文依赖）。

### First-token collision 矩阵 (Mistral, generation context)

| First Token | Token ID | Colliding Entity Types |
|---|---|---|
| 'S' | 29503 | **SEN, SID, SIDE** |
| 'B' | 29528 | **BAL, BOD** |

2 个碰撞组，5/27 types 受影响。

### Bare encoding collision groups (compile_type_constraints 会崩溃)

| First Token | Token ID | Colliding Entity Types |
|---|---|---|
| 'A' | 1098 | ABS, AML |
| 'B' | 1133 | BAL, BOD |
| 'P' | 1135 | PLA, PTH |
| 'S' | 1086 | SEN, SID, SIDE |

4 个碰撞组，9/27 types。**`compile_type_constraints()` 在 Mistral 上抛 ValueError**。
`run_constrained_extraction.py` 通过 `ensure_first_token_map()` 绕过了碰撞检查。

### Prefix map 覆盖检查

- `_build_entity_type_prefix_map()` 做全词表扫描 → **所有 generation-context first tokens 都在 prefix map 中**
- D044 修复的方法（vocab scan）对 entity type 确实有效覆盖
- 问题不是 token 缺失，而是碰撞组内 token 共享

### 碰撞影响分析

**103/245 (42%)** 的 (event_type, role) 约束与碰撞组有 partial overlap：
- 51/56 event types 受影响
- 主要模式：SID 被允许但 SEN/SIDE 不被允许的 agent role（Attacker, Damager, Victor, Communicator, Destroyer 等等）
- 次要模式：BAL 被允许但 BOD 不被允许的 artifact role（Artifact, Instrument 等）

当约束说 "只允许 SID" 时：
1. Mask 看到 token 29503 ('S') 可达 {SEN, SID, SIDE}，SID ∈ allowed → 不阻塞
2. Model 生成 'S' 后，XGrammar 允许 'EN'/'ID'/'IDE' 三种延续
3. Semantic mask 只在 entity type 首 token 生效，对后续 token 无约束
4. → SEN 或 SIDE 可能生成 → AC violation

---

### Qwen tokenizer (BPE, Qwen2TokenizerFast, vocab=151643)

- **0 bare vs generation-context mismatches**
- **0 collision groups**
- BPE tokenizer 上下文无关 → entity type masking 完全有效

---

### Llama tokenizer (BPE, PreTrainedTokenizerFast, vocab=128256)

- **0 bare vs generation-context mismatches**
- **0 collision groups**
- `compile_type_constraints()` 不崩溃
- Entity type masking 正常工作

---

### 根因确认

Mistral AC=16.6% 根因是 **(A) first-token collision**：

- **不是 (B)**: in-context token 不在 prefix map → 已被 D044 全词表扫描方法解决
- **是 (A)**: SEN/SID/SIDE 和 BAL/BOD 碰撞组共享 generation-context 首 token → mask 无法区分组内 types → 42% 约束槽位失效
- 伴随问题: `compile_type_constraints()` 对 Mistral 崩溃（bare encoding 4 组碰撞），`ensure_first_token_map()` 绕过检查但不解决问题

Qwen AC=2.1%：BPE 无碰撞，残余 AC 来自其他因素（grammar-first fallback、position detection 边界情况）

Llama AC=3.4%：BPE 无碰撞，残余 AC 同上

---

### 修复建议

**方案 1（推荐）: 碰撞组专用 continuation mask**
在 `_apply_type_mask` 检测到碰撞组首 token 未被阻塞时，注册一个 continuation handler：下一步在碰撞组成员的第二 token 之间做 masking。例如 SID 允许时，下一步阻塞 'EN' (→SEN) 和 'IDE' (→SIDE) 的 token，只允许 'ID' (→SID)。

**方案 2: 多 token trie masking**
将 `_apply_type_mask` 从单步首 token 扩展为多步 trie 约束。每步检查已生成前缀 + 当前 token 是否仍可达任何 allowed type。需要跨步骤维护 partial match state。

**方案 3（最简单）: 重命名碰撞 entity types**
修改 ontology 中碰撞 types 的名称使首 token 唯一化：
- SEN → SENT（首 token 'S' → 'SE'... 仍碰撞 SID）
- 或 SEN → SENTENCE / SID → SIDEG / SIDE → SIDEA
- BAL → BALL / BOD → BODY
这需要同时修改 ontology JSON、prompt 模板和 violation checker。

**方案 4: 对 Mistral 禁用 semantic mask 对碰撞组的约束**
不修复碰撞，但准确报告 "semantic mask 覆盖率 = (245-103)/245 = 58%"，论文中标注此限制。
