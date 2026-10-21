# OntoCoDec 代码架构调研：ACE05 Event Extraction 适配

## 1. 代码架构图

```
schema_semantic_constrained_ie/
├── compiler/                          # 核心约束编译层
│   ├── ontology_compiler.py           # Ontology JSON → ConstraintSpec + XGrammar CFG
│   ├── type_mask_processor.py         # Semantic Layer: domain/range LogitsProcessor
│   ├── beam_aware_processor.py        # Beam search 适配版 TypeConstraintProcessor
│   ├── beam_grammar_processor.py      # Beam search 适配版 Grammar processor
│   └── type_consensus_processor.py    # Layer 3: cross-field type consistency
├── run_constrained_extraction.py      # 主推理入口（greedy/beam, S1/S2 模式）
├── violation_checker.py               # SciERC violation 统计
├── violation_checker_docred.py        # DocRED violation 统计
├── unified_f1_eval.py                 # F1 评估
├── ontology_constraints.json          # SciERC ontology 定义
├── data/
│   ├── processed_data/                # SciERC train/dev/test
│   └── docred/                        # DocRED + ontology_constraints_docred.json
├── scripts/                           # SFT 数据准备 + LoRA 训练
└── outputs/                           # 推理结果 JSONL
```

### 数据流
```
ontology_constraints.json
    → OntologyCompiler._build_spec() → ConstraintSpec
    → compile_json_schema() → JSON Schema → XGrammar.compile_grammar() → CompiledGrammar (Layer 1)
    → compile_type_constraints() → entity_type_first_token map → TypeConstraintProcessor (Layer 2)
    
推理时: model.generate(logits_processor=[GrammarProcessor, TypeConstraintProcessor])
```

## 2. 各模块详细分析 & 需要修改的文件

### 2.1 Grammar Layer (`compiler/ontology_compiler.py`)

**当前逻辑**：
- `ConstraintSpec` 包含: `entity_types`, `relation_types`, `relation_constraints` (dict[str, RelationConstraint])
- `RelationConstraint` 存储 `valid_pairs: list[tuple[str, str]]` (head_type, tail_type)
- `compile_json_schema()` 生成 JSON Schema，enum 约束 entity_type 和 relation_type
- `compile_xgrammar()` 将 JSON Schema 编���为 XGrammar CFG

**Event Extraction 需要修改**：
- 新增 `EventConstraint` dataclass（类比 `RelationConstraint`）：
  ```python
  @dataclass
  class EventConstraint:
      event_type: str
      valid_argument_roles: list[str]  # 该 event type 允许的 role
      role_entity_constraints: dict[str, set[str]]  # role → 允许的 entity types
  ```
- `ConstraintSpec` 新增字段：`event_types: list[str]`, `event_constraints: dict[str, EventConstraint]`
- 新增 `compile_event_json_schema()` 方法，生成 event extraction 的 JSON Schema：
  ```json
  {
    "entities": [{"text": "...", "type": "<entity_type enum>"}],
    "events": [{
      "trigger": "...",
      "event_type": "<event_type enum>",
      "arguments": [{"text": "...", "role": "<role enum>", "entity_type": "<entity_type enum>"}]
    }]
  }
  ```
- **工作量**: 中等（~150行新增，复用现有 compile/xgrammar 流程）

### 2.2 Semantic Layer (`compiler/type_mask_processor.py`)

**当前逻辑**：
- `FieldPosition` enum: ENTITY_TYPE, RELATION_TYPE, RELATION_HEAD_TYPE, RELATION_TAIL_TYPE, FREE_TEXT
- `PositionDetector` 用 regex 检测当前 JSON 生成位置
- `EntityRegistry` 记录已生成的 entity text→type 映射
- `_mask_head_type()`: 根据 relation_type 约束 head 的 entity type
- `_mask_tail_type()`: 根据 (relation_type, head_type) 约束 tail 的 entity type
- **First-token masking**: 只 mask 每个 type string 的第一个 token（利用 XGrammar 保证后续 token）

**Event Extraction 需要修改**：
- `FieldPosition` 新增: `EVENT_TYPE`, `ARGUMENT_ROLE`, `ARGUMENT_ENTITY_TYPE`
- `PositionDetector` 新增 regex 检测 event JSON 中的字段位置:
  - `"event_type": "...` → EVENT_TYPE
  - `"role": "...` → ARGUMENT_ROLE
  - `"entity_type": "...`（在 arguments 内）→ ARGUMENT_ENTITY_TYPE
- 新增 mask 函数:
  - `_mask_event_type()`: 允许所有 event_type first tokens（类比现有 entity_type mask）
  - `_mask_argument_role(event_type)`: 根据当前 event_type 只允许合法的 role
  - `_mask_argument_entity_type(event_type, role)`: 根据 (event_type, role) 约束 entity_type
- `GenerationState` 新增: `current_event_type`, `current_argument_role`
- `EntityRegistry` **可以直接复用**（event arguments 也需要引用已提取的 entity）
- **工作量**: 较大（~200行新增 + 改动现有 detect/mask 逻辑）

### 2.3 推理脚本 (`run_constrained_extraction.py`)

**当前逻辑**：
- 5种模式: unconstrained, grammar_only, semantic_only, full_s1, full_s2
- S2 两阶段: Pass1 entity extraction → Pass2 relation extraction (entity-aware)
- `build_full_schema()` / `build_entity_only_schema()` / `build_relation_only_schema()` 构建 JSON Schema
- Prompt templates 硬编码 entity_types + relation_types

**Event Extraction 需要修改**：
- 新增数据加载: `load_ace05_data(data_path)` — ACE05 格式解析
- 新增 prompt template: 描述 event extraction 任务（entity types, event types, argument roles）
- 新增 JSON Schema 构建:
  - `build_event_schema(entity_types, event_types, role_enum)` — event extraction 输出结构
  - S2 模式: Pass1 entity+trigger → Pass2 arguments (entity-aware + event-type-aware)
- 新增 dataset 参数: `--dataset ace05`
- **工作量**: 中等（~200行新增，大部分是 prompt + schema + data loading）

### 2.4 Violation Checker

**当前 violation 类别（SciERC/DocRED）**：
| 类别 | 缩写 | 含义 |
|------|------|------|
| Entity Type | ET | entity type 不在 ontology |
| Relation Vocabulary | RV | relation 名不在 ontology |
| Domain/Range | DR | (head_type, tail_type) 不在 relation 的 valid_pairs |
| Cross-Field Consistency | CF | 同一 entity 在不同位置 type 不一致 |

**Event Extraction 的 violation 类别映射**：
| RE violation | EE violation | 缩写 | 含义 |
|---|---|---|---|
| ET | Entity Type | ET | entity type 不在 ontology（保留） |
| RV | Event Vocabulary | EV | event_type 不在 ontology |
| — | Role Vocabulary | RoV | argument role 不在该 event_type 允许的 roles |
| DR | Argument Constraint | AC | (event_type, role) → entity_type 约束违反 |
| CF | Cross-Field Consistency | CF | 同一 entity 跨 event type 不一致（保留逻辑） |

**需要新建**: `violation_checker_ace05.py`
- **工作���**: 中等（~200行，结构类似现有 checker，改 violation 定义）

### 2.5 评估脚本

**当前**: `compute_f1` 在 violation_checker 中，计算 entity F1 和 relation F1

**Event Extraction 评估指标**:
- Trigger Identification F1: (trigger_text, event_type) 匹配
- Argument Extraction F1: (trigger_text, event_type, arg_text, role) 匹配
- Entity F1: 保留

**需要新建**: 评估函数或扩展 `compute_f1`
- **工作量**: 小（~80行）

### 2.6 Ontology Constraints 文件

**需要���建**: `ontology_constraints_ace05.json`
```json
{
  "entity_types": ["PER", "ORG", "GPE", "LOC", "FAC", "VEH", "WEA"],
  "event_types": ["Life:Be-Born", "Life:Die", "Movement:Transport", ...],
  "event_constraints": {
    "Life:Be-Born": {
      "valid_roles": ["Person", "Time", "Place"],
      "role_entity_constraints": {
        "Person": ["PER"],
        "Time": ["TIME"],
        "Place": ["GPE", "LOC", "FAC"]
      }
    },
    ...
  }
}
```
- **工作量**: 中等（需要从 ACE05 annotation guidelines 提取完整约束）

## 3. 可以直接复用的模块

| 模块 | 复用度 | 说明 |
|------|--------|------|
| `EntityRegistry` | 100% | event arguments 同样需要 entity text→type 映射 |
| `compile_xgrammar()` | 100% | JSON Schema → CFG 的编译流程不变 |
| `compile_type_constraints()` / first-token mapping | 100% | 扩展到 event_type 即可 |
| `_apply_type_mask()` | 100% | mask 逻辑通用 |
| `BeamAwareTypeConstraintProcessor` 结构 | 90% | 只需继承并扩展 event 相关 mask |
| `BeamSearchGrammarProcessor` | 100% | 与 task 无关 |
| `parse_model_output()` | 100% | JSON 解析通用 |
| 推理框架（resume, batch, timing） | 95% | 只需加 dataset 分支 |
| `normalize_type()` / fuzzy matching | 90% | 可复用，加 event-specific aliases |
| CF violation 检查逻辑 | 80% | mention_types 字典收集方式相同 |

## 4. 预估工作量

| 优先级 | 任务 | 难度 | 预估时间 |
|--------|------|------|----------|
| P0 | ACE05 ontology constraints JSON 编写 | 中 | 2h |
| P0 | `ontology_compiler.py` 扩展 EventConstraint + event JSON Schema | 中 | 3h |
| P0 | `type_mask_processor.py` 扩展 event field detection + mask | 高 | 4h |
| P1 | `run_constrained_extraction.py` ACE05 data loading + prompts | 中 | 3h |
| P1 | `violation_checker_ace05.py` 新建 | 中 | 2h |
| P2 | 评估指标（trigger F1 + argument F1） | 低 | 1h |
| P2 | ACE05 SFT 数据准备脚本 | 中 | 2h |
| P3 | Beam search 适配 | 低 | 1h |

**总计: ~18h 开发时间**

## 5. 建议实现顺序

1. **Phase 1 — Ontology & Grammar (Day 1)**
   - 编写 `ontology_constraints_ace05.json`（从 ACE05 guidelines 提取 33 event types + roles + entity constraints）
   - 扩展 `ConstraintSpec` 和 `OntologyCompiler` 支持 event_types + event_constraints
   - 实现 `build_event_schema()` 并验证 XGrammar 能正确编译

2. **Phase 2 — Semantic Layer (Day 2)**
   - 扩展 `FieldPosition` 和 `PositionDetector` 识别 event JSON 字段
   - 实现 `_mask_event_type()`, `_mask_argument_role()`, `_mask_argument_entity_type()`
   - 单元测试确保 mask 正确

3. **Phase 3 — 推理流程 (Day 3)**
   - 实现 `load_ace05_data()` + event extraction prompt
   - 接入 `--dataset ace05` 到主推理脚本
   - 端到端验证: unconstrained → grammar_only → full_s1

4. **Phase 4 — 评估 (Day 4)**
   - 实现 `violation_checker_ace05.py`
   - 实现 trigger F1 / argument F1 评估
   - 跑 baseline 实验，验证 constraint 层的 violation 消除效果
