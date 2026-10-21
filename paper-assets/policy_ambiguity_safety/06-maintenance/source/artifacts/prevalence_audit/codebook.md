# Codebook: Policy Ambiguity Annotation

## Task
For each policy clause, determine whether it contains ambiguity that could cause an LLM agent to misinterpret the intended policy, and if so, classify the ambiguity type.

## Definitions

**Operational clause**: A sentence or multi-sentence block from a company policy document that prescribes, constrains, or conditions a specific agent action or decision.

**Ambiguity** (for this task): A clause is ambiguous if a reasonable LLM agent, following the clause literally, could arrive at two or more materially different interpretations of what action to take or what constraint applies.

## Ambiguity Types

| Type | Definition | Example |
|------|-----------|---------|
| **Scopal** | Modifier or quantifier attachment is unclear — it is ambiguous which part of the sentence a modifier, "only," "all," or negation applies to. | "Customers can only return items purchased with a credit card within 30 days" — does "only" scope over the payment method or the time window? |
| **Lexical** | A word or phrase has multiple plausible meanings in context — polysemy or domain-specific usage creates divergent interpretations. | "Reasonable wear" — what threshold distinguishes reasonable from unreasonable? |
| **Coreferential** | A pronoun, demonstrative ("this," "that," "it"), or noun phrase refers ambiguously to multiple possible antecedents. | "If the item was purchased with a gift card and returned, it will be refunded to the original method" — does "it" refer to the item's value or the gift card balance? |
| **Incompleteness** | The clause omits information necessary to determine the correct action — a decision-relevant parameter is left unspecified. | "Electronics have a different return window" — what is the window? |
| **Authorization scope** | It is unclear who has permission to perform an action, or what the boundaries of a granted permission are. | "Managers may approve exceptions" — which managers? For which exception types? Up to what value? |
| **Conditional precedence** | Multiple conditions or rules could apply simultaneously, and the clause does not specify which takes priority or how they interact. | "Items must be returned within 30 days. Members get an extra 15 days. Holiday purchases have until January 31." — if a member buys during the holidays, which deadline applies? |

## Annotation Instructions

1. Read the clause and its context carefully.
2. **Is this clause ambiguous?** Answer YES only if you can articulate two distinct, plausible interpretations that would lead an LLM agent to take materially different actions. Complexity alone is not ambiguity.
3. **If YES, select the best-fitting type** from the six categories above. If multiple types apply, choose the most prominent one.
4. **Write a brief note** (1-2 sentences) explaining the ambiguity or why the clause is not ambiguous.

## Decision Rules

- **Not ambiguous**: The clause is precise enough that a competent LLM agent would reliably arrive at the same interpretation. Minor stylistic issues or imperfect grammar do not count.
- **Ambiguous**: Two reasonable LLM agents, each following the clause literally, could take meaningfully different actions.
- When in doubt, lean toward "not ambiguous" — we want high precision.

## Fields to Fill

| Column | Instructions |
|--------|-------------|
| `human_is_ambiguous` | `TRUE` or `FALSE` |
| `human_ambiguity_type` | One of: `scopal`, `lexical`, `coreferential`, `incompleteness`, `authorization_scope`, `conditional_precedence`, or `none` |
| `human_notes` | 1-2 sentence justification |

## Quality Checks
- Annotate all 50 rows; do not skip any.
- If unsure, mark as `FALSE` and note your uncertainty in `human_notes`.
- Do not look at the judge columns (judge1_*, judge2_*) before making your own annotation to avoid anchoring bias. Fill them in independently first, then compare.
