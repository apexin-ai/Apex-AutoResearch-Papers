## Constraint Extraction Prompt Template

SICA uses two domain-specific prompt templates for constraint extraction: one for mathematical reasoning (MATH, GSM8K, AIME) and one for logical reasoning (ProofWriter, FOLIO). Both share the same system prompt.

Source file: `/root/symb_invariant_consensus/sica/constraint_extractor.py`

---

### System Prompt

Used by `VLLMBackend._SYSTEM_MSG` (line 167):

```
You are a constraint extraction tool. Output ONLY valid JSON. Do NOT solve problems, reason about correctness, or think step-by-step. Extract constraints from the given trace exactly as stated.
```

---

### Mathematical Constraint Extraction Prompt (EXTRACTION_PROMPT)

Used for datasets: MATH-500, GSM8K, AIME

```
Extract mathematical constraints from this reasoning trace as a JSON object.

Rules:
- type: "equation", "inequality", or "predicate"
- expression: human-readable, e.g. "x + y == 14"
- z3_formula: a single comparison expression in Python Z3 syntax
- source_step: step number where the constraint appears
- Use variable names from the trace

z3_formula MUST follow these rules:
- Allowed operators: ==, !=, <, >, <=, >=, +, -, *, /, **, %
- Use individual named variables: a1, a2, a3... NOT arrays a[1] or sets A
- Expand all sums explicitly: "a1 + a2 + a3 == 55" NOT "sum([a1,a2,a3])"
- NO Python builtins: sum(), len(), max(), min(), list(), set(), range(), int()
- Each z3_formula must be exactly ONE comparison (==, !=, <, >, <=, >=)
- For multiple values, write separate constraints for each

Example for combinatorics (set A = {11, 10, 9, 8, 7, 6, 4}, sum = 55):
{"constraints": [
  {"type": "equation", "expression": "a1 = 11", "z3_formula": "a1 == 11", "source_step": 5},
  {"type": "equation", "expression": "a2 = 10", "z3_formula": "a2 == 10", "source_step": 5},
  {"type": "equation", "expression": "sum of elements = 55", "z3_formula": "a1 + a2 + a3 + a4 + a5 + a6 + a7 == 55", "source_step": 6},
  {"type": "equation", "expression": "total sets = 2024", "z3_formula": "2**(a1 - 1) + 2**(a2 - 1) + 2**(a3 - 1) + 2**(a4 - 1) + 2**(a5 - 1) + 2**(a6 - 1) + 2**(a7 - 1) == 2024", "source_step": 2},
  {"type": "inequality", "expression": "a1 > a2", "z3_formula": "a1 > a2", "source_step": 5},
  {"type": "equation", "expression": "answer is 55", "z3_formula": "answer == 55", "source_step": 6}
]}

Output ONLY the JSON below, nothing else:
{"constraints": [{"type": "equation", "expression": "x + y == 14", "z3_formula": "x + y == 14", "source_step": 1}], "answer": "final_answer", "variables": ["x", "y"]}

Trace:
{trace}
```

Valid constraint types (math): `equation`, `inequality`, `predicate`

---

### Logical Constraint Extraction Prompt (LOGIC_EXTRACTION_PROMPT)

Used for datasets: ProofWriter, FOLIO

```
IMPORTANT: You are an EXTRACTION tool, NOT a problem solver.
- Do NOT re-solve or re-reason about the problem.
- Do NOT verify whether the trace's reasoning is correct.
- ONLY extract the logical constraints that are explicitly stated or used in the trace below.
- Output ONLY the JSON object, nothing else — no explanation, no commentary.

Extract logical constraints from this reasoning trace about a logic problem.

The problem has facts (base assertions), rules (grounded implications), and derived conclusions.
Convert each into a Z3 boolean formula.

Variable naming:
- Unary property: property_entity (e.g., kind_anne, red_charlie, round_fiona)
- Binary relation: relation_subject_object (e.g., eats_bear_squirrel, likes_lion_cat)
- Use lowercase with underscores only, no spaces or special characters

Constraint types:
- "fact": a given assertion, e.g., kind_anne == True
- "rule": a grounded implication over specific entities, e.g., Implies(kind_anne, nice_anne)
- "derived": an inferred conclusion from facts + rules, e.g., nice_anne == True

Z3 operators:
- Implies(a, b) for if-then rules
- And(a, b, ...) for conjunctive conditions
- Or(a, b, ...) for disjunctive conditions
- Not(a) for negation
- == True / == False for boolean assertions

Output ONLY the JSON below, nothing else:
{"constraints": [{"type": "fact", "expression": "kind(anne)", "z3_formula": "kind_anne == True", "source_step": 1}], "answer": "True or False or Unknown", "variables": ["kind_anne"]}

Example 1:
Trace: "Anne is kind. Kind things are nice. Therefore Anne is nice. The answer is True."
Output:
{"constraints": [
  {"type": "fact", "expression": "kind(anne)", "z3_formula": "kind_anne == True", "source_step": 1},
  {"type": "rule", "expression": "kind(X) -> nice(X)", "z3_formula": "Implies(kind_anne, nice_anne)", "source_step": 2},
  {"type": "derived", "expression": "nice(anne)", "z3_formula": "nice_anne == True", "source_step": 3}
], "answer": "True", "variables": ["kind_anne", "nice_anne"]}

Example 2:
Trace: "The bear eats the squirrel. If someone eats the squirrel then the squirrel is red. So the squirrel is red. The answer is True."
Output:
{"constraints": [
  {"type": "fact", "expression": "eats(bear, squirrel)", "z3_formula": "eats_bear_squirrel == True", "source_step": 1},
  {"type": "rule", "expression": "eats(X, squirrel) -> red(squirrel)", "z3_formula": "Implies(eats_bear_squirrel, red_squirrel)", "source_step": 2},
  {"type": "derived", "expression": "red(squirrel)", "z3_formula": "red_squirrel == True", "source_step": 3}
], "answer": "True", "variables": ["eats_bear_squirrel", "red_squirrel"]}

Example 3 (multi-condition rule):
Trace: "Gary is big. Gary is quiet. Big things are smart. Quiet, cold things are white. Gary is smart. But Gary is not cold. So we cannot determine if Gary is furry. The answer is Unknown."
Output:
{"constraints": [
  {"type": "fact", "expression": "big(gary)", "z3_formula": "big_gary == True", "source_step": 1},
  {"type": "fact", "expression": "quiet(gary)", "z3_formula": "quiet_gary == True", "source_step": 2},
  {"type": "rule", "expression": "big(X) -> smart(X)", "z3_formula": "Implies(big_gary, smart_gary)", "source_step": 3},
  {"type": "rule", "expression": "quiet(X) & cold(X) -> white(X)", "z3_formula": "Implies(And(quiet_gary, cold_gary), white_gary)", "source_step": 4},
  {"type": "derived", "expression": "smart(gary)", "z3_formula": "smart_gary == True", "source_step": 5}
], "answer": "Unknown", "variables": ["big_gary", "quiet_gary", "smart_gary", "cold_gary", "white_gary"]}

Trace:
{trace}
```

Valid constraint types (logic): `fact`, `rule`, `derived`

---

### Expected Output Format

Both prompts expect a JSON object with the following schema:

```json
{
  "constraints": [
    {
      "type": "<equation|inequality|predicate> or <fact|rule|derived>",
      "expression": "<human-readable description>",
      "z3_formula": "<Z3-compatible Python expression>",
      "source_step": <integer>
    }
  ],
  "answer": "<final answer string>",
  "variables": ["<var1>", "<var2>", "..."]
}
```

The pipeline also injects an `answer_assertion` constraint per trace (added in `pipeline.py`, not by the LLM):
```json
{"type": "answer_assertion", "expression": "answer is <ans>", "z3_formula": "__sica_answer_<ans> == True", "source_step": -1}
```

---

### Example 1: Mathematical Reasoning (GSM8K)

**Problem:**
> Christina records her mood every day on a calendar. Over the past thirty days of moods, she had twelve good days and eight bad days and the rest were neutral. Her first eight days were good, her second eight days were bad, and her third eight days were neutral. If the next three days were good, neutral, and good, how many good days were left in the month?

**Input prompt sent to LLM** (system + user):

System: `You are a constraint extraction tool. Output ONLY valid JSON. Do NOT solve problems, reason about correctness, or think step-by-step. Extract constraints from the given trace exactly as stated.`

User: `EXTRACTION_PROMPT.format(trace=<reasoning_trace>)`, where `{trace}` is replaced with the actual reasoning trace from the trace generator.

**Model output (after deduplication across 12 traces, 16 unique constraints):**

```json
[
  {"expression": "answer is 2", "z3_formula": "__sica_answer_2 == True", "weight": 11, "source_traces": [0,1,2,4,5,6,7,8,9,10,11]},
  {"expression": "12 = good days total", "z3_formula": "good_days_total == 12", "weight": 3, "source_traces": [2,6,10]},
  {"expression": "8 = bad days total", "z3_formula": "bad_days_total == 8", "weight": 3, "source_traces": [2,6,10]},
  {"expression": "10 = neutral days total", "z3_formula": "neutral_days_total == 10", "weight": 3, "source_traces": [2,6,10]},
  {"expression": "8 = good days in first period", "z3_formula": "good_days_first_period == 8", "weight": 1, "source_traces": [2]},
  {"expression": "8 = bad days in second period", "z3_formula": "bad_days_second_period == 8", "weight": 1, "source_traces": [2]},
  {"expression": "8 = neutral days in third period", "z3_formula": "neutral_days_third_period == 8", "weight": 1, "source_traces": [2]},
  {"expression": "1 = good day on day 25", "z3_formula": "good_day_day_25 == 1", "weight": 1, "source_traces": [2]},
  {"expression": "1 = neutral day on day 26", "z3_formula": "neutral_day_day_26 == 1", "weight": 1, "source_traces": [2]},
  {"expression": "1 = good day on day 27", "z3_formula": "good_day_day_27 == 1", "weight": 1, "source_traces": [2]},
  {"expression": "good_days_first_8 = 8", "z3_formula": "good_days_first_8 == 8", "weight": 2, "source_traces": [6,10]},
  {"expression": "good_days_later_specified = 2", "z3_formula": "good_days_later_specified == 2", "weight": 1, "source_traces": [6]},
  {"expression": "remaining_good_days = 2", "z3_formula": "remaining_good_days == 2", "weight": 2, "source_traces": [6,10]},
  {"expression": "good_days_later = 2", "z3_formula": "good_days_later == 2", "weight": 1, "source_traces": [10]},
  {"expression": "answer is 10", "z3_formula": "__sica_answer_10 == True", "weight": 1, "source_traces": [3]},
  {"expression": "x + y == 14", "z3_formula": "x + y == 14", "weight": 1, "source_traces": [1]}
]
```

SICA answer: **2** (correct). 11/12 traces agreed; constraint weights strongly favored answer "2".

---

### Example 2: Logical Reasoning (ProofWriter)

**Problem (ProofWriter_AttNoneg-OWA-D5-1041_Q1):**
> Charlie is red. Dave is red. Dave is rough. Dave is round. Dave is young. Fiona is quiet. Fiona is red. Harry is furry. Harry is kind. Harry is young. All rough things are round. All round, rough things are young. All red things are young. If Fiona is young and Fiona is not furry then Fiona is kind. If something is furry then it is rough. Quiet, kind things are rough. All quiet, young things are kind. Young things are quiet.
>
> Determine whether the following statement is true, false, or unknown: Fiona is round.

**Per-trace constraint extraction output (from one trace):**

```json
{"constraints": [
  {"type": "fact", "expression": "kind(charlie)", "z3_formula": "kind_charlie == True", "source_step": 5},
  {"type": "fact", "expression": "quiet(charlie)", "z3_formula": "quiet_charlie == True", "source_step": 6},
  {"type": "fact", "expression": "red(charlie)", "z3_formula": "red_charlie == True", "source_step": 7},
  {"type": "fact", "expression": "rough(charlie)", "z3_formula": "rough_charlie == True", "source_step": 8},
  {"type": "rule", "expression": "quiet(X) & cold(X) -> smart(X)", "z3_formula": "Implies(And(quiet_charlie, cold_charlie), smart_charlie)", "source_step": 9},
  {"type": "rule", "expression": "red(X) & cold(X) -> round(X)", "z3_formula": "Implies(And(red_charlie, cold_charlie), round_charlie)", "source_step": 10},
  {"type": "rule", "expression": "kind(X) & rough(X) -> red(X)", "z3_formula": "Implies(And(kind_charlie, rough_charlie), red_charlie)", "source_step": 11},
  {"type": "rule", "expression": "quiet(X) -> rough(X)", "z3_formula": "Implies(quiet_charlie, rough_charlie)", "source_step": 12},
  {"type": "rule", "expression": "cold(X) & smart(X) -> red(X)", "z3_formula": "Implies(And(cold_charlie, smart_charlie), red_charlie)", "source_step": 13},
  {"type": "rule", "expression": "rough(X) -> cold(X)", "z3_formula": "Implies(rough_charlie, cold_charlie)", "source_step": 14},
  {"type": "rule", "expression": "red(X) -> rough(X)", "z3_formula": "Implies(red_charlie, rough_charlie)", "source_step": 15},
  {"type": "rule", "expression": "smart(dave) & kind(dave) -> quiet(dave)", "z3_formula": "Implies(And(smart_dave, kind_dave), quiet_dave)", "source_step": 16}
], "answer": "True", "variables": ["kind_charlie", "quiet_charlie", "red_charlie", "rough_charlie", "cold_charlie", "smart_charlie", "round_charlie", "smart_dave", "kind_dave", "quiet_dave"]}
```

---

### LLM Call Configuration

From `VLLMBackend` (constraint_extractor.py line 170-185):
- **Temperature:** 0.1
- **Max tokens:** 1024
- **Response format:** `{"type": "json_object"}` (structured JSON mode)
- **Concurrency:** up to 6 parallel calls via `ThreadPoolExecutor`
- **Retry:** up to 2 retries with exponential backoff (base 0.5s)

From `ConstraintExtractor.__init__`:
- **Parse retries:** 1 (re-extract if JSON parsing fails)
- **Domain:** auto-detected from dataset field (`"math"` or `"logic"`)

### Prompt Selection Logic

```python
def _build_prompt(self, trace: str) -> str:
    template = LOGIC_EXTRACTION_PROMPT if self.domain == "logic" else EXTRACTION_PROMPT
    return template.format(trace=trace)
```

Domain is set in `pipeline.py`:
```python
domain = "folio" if dataset == "folio" else "logic" if dataset == "proofwriter" else "math"
self.constraint_extractor.domain = "logic" if domain in ("logic", "folio") else "math"
```
