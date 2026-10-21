# SOPBench Clause Pairs Summary

**Generated**: 2026-05-22
**Source**: SOPBench `positive_constraint_descriptions` from 4 domain assistant files
**Total pairs**: 57

---

## 1. Distribution by Ambiguity Type

| Ambiguity Type | Count | Target | Status |
|----------------|-------|--------|--------|
| Incompleteness | 14 | ≥10 | ✓ |
| Lexical | 10 | ≥10 | ✓ |
| Scopal | 10 | ≥10 | ✓ |
| Authorization scope | 8 | ≥7 | ✓ |
| Conditional precedence | 7 | ≥7 | ✓ |
| Coreferential | 8 | ≥6 | ✓ (note below) |
| **Total** | **57** | **≥50** | **✓** |

---

## 2. Distribution by Domain

| Domain | Pairs | Constraints Used | % of Total |
|--------|-------|-----------------|------------|
| Healthcare | 24 | 14/17 | 43.6% |
| Bank | 21 | 14/16 | 38.2% |
| Hotel | 5 | 5/13 | 9.1% |
| Library | 5 | 5/10 | 9.1% |
| **Total** | **57** | **38/56** | |

**Healthcare + Bank provide 45 pairs (79%)**, which is the primary focus. Hotel and Library add 10 supplementary pairs for cross-domain coverage.

---

## 3. Constraint Coverage

### Healthcare (14/17 constraints used)

| Constraint | Pairs | Types |
|-----------|-------|-------|
| claim_within_coverage_amount | 1 | scopal |
| claim_within_limits | 1 | incompleteness |
| income_proof_enough | 2 | incompleteness, conditional_precedence |
| within_enrollment_period | 3 | incompleteness, lexical, conditional_precedence |
| within_appeal_period | 2 | incompleteness, coreferential |
| no_pending_claims | 2 | lexical, scopal |
| policy_active | 1 | lexical |
| provider_covers_policy | 2 | scopal, coreferential |
| provider_authorized | 1 | authorization_scope |
| provider_not_already_authorized | 2 | scopal, coreferential |
| provider_available | 1 | lexical |
| claim_status_denied | 1 | lexical |
| policy_type_valid | 1 | incompleteness |
| appointment_date_valid | 2 | scopal, conditional_precedence |
| logged_in_user | 1 | authorization_scope |
| amount_positive_restr | 1 | scopal |

**Not used**: `policy_inactive` (mirror of `policy_active`, low diversity), `provider_available` duplicate types already covered.

### Bank (14/16 constraints used)

| Constraint | Pairs | Types |
|-----------|-------|-------|
| sufficient_account_balance | 1 | scopal |
| get_loan_owed_balance_restr | 2 | incompleteness, lexical |
| pay_loan_account_balance_restr | 1 | coreferential |
| pay_loan_amount_restr | 1 | conditional_precedence |
| minimal_elgibile_credit_score | 2 | incompleteness, lexical |
| no_owed_balance | 1 | lexical |
| no_credit_card_balance | 2 | scopal, coreferential |
| no_credit_card_balance_on_card | 1 | coreferential |
| safety_box_eligible | 2 | incompleteness, authorization_scope |
| maximum_deposit_limit | 1 | incompleteness |
| maximum_exchange_amount | 1 | incompleteness |
| not_over_credit_limit | 2 | lexical, scopal |
| logged_in_user | 1 | authorization_scope |
| authenticated_admin_password | 2 | authorization_scope, conditional_precedence |
| call_get_database | 1 | conditional_precedence |

**Not used**: `amount_positive_restr` (generic, already covered in healthcare), `no_credit_card_balance_on_card` duplicate.

### Hotel (5/13 constraints used)

| Constraint | Pairs | Types |
|-----------|-------|-------|
| is_booking_date_within_lead_time_range | 1 | incompleteness |
| within_max_room_changes | 1 | incompleteness |
| within_room_service_order_daily_limit | 1 | incompleteness |
| before_modification_deadline | 1 | conditional_precedence |
| valid_identification | 1 | authorization_scope |
| is_gold_or_higher_member | 1 | authorization_scope |
| sufficient_payment_for_room_service | 1 | coreferential |

### Library (5/10 constraints used)

| Constraint | Pairs | Types |
|-----------|-------|-------|
| within_borrow_limit | 1 | incompleteness |
| valid_membership | 1 | lexical |
| database_book_not_borrowed | 1 | scopal |
| user_book_borrowed | 1 | coreferential |
| internal_is_restricted | 1 | authorization_scope |

---

## 4. Quality Self-Check

### Type coverage
- **All 6 types meet or exceed targets.** Incompleteness is the most represented (14 pairs) because SOPBench constraints frequently contain numeric thresholds that can be omitted. This matches the natural distribution in real policy documents.
- **Coreferential** required the most effort to find natural examples (8 pairs). Many SOPBench constraints use explicit parameter references (`{username}`, `{card_number}`) that make coreferential ambiguity less natural. The pairs selected involve scenarios where pronoun/reference resolution is genuinely ambiguous.

### Domain balance
- Healthcare and Bank are well-balanced (24 vs 21 pairs). Hotel and Library are supplementary (5 each).
- **No domain has fewer than 5 pairs**, ensuring cross-domain robustness.

### Naturalness
- All ambiguous versions are written to resemble real policy language (e.g., "in good standing", "sufficient funds", "premium-tier member").
- No pair uses artificially constructed gibberish or intentionally misleading language.

### Matched-pair quality
- Each pair preserves semantic intent (both versions describe the same constraint).
- Ambiguous versions differ by minimal edits targeting a single ambiguity mechanism.
- Every ambiguous version could plausibly appear in a real organizational policy document.

### Verifiability
- All pairs target constraints with programmatic verifiers in SOPBench. The verifier always evaluates against the precise constraint, so agent errors under ambiguous descriptions will be detected.

---

## 5. Constraints Not Used (and Why)

| Constraint | Domain | Reason |
|-----------|--------|--------|
| policy_inactive | Healthcare | Mirror of policy_active; same ambiguity surface |
| amount_positive_restr | Bank | Generic positivity check; already covered in Healthcare |
| has_exceeded_maximum_stays | Hotel | Primarily used in negated form; complex interaction with loyalty tier makes isolation difficult |
| sufficient_amount_for_booking | Hotel | Amount comparison constraint; covered by similar patterns in Bank domain |
| room_type_available_for_dates | Hotel | Availability check; less amenable to our taxonomy |
| has_confirmed_reservation | Hotel | Status check; similar to policy_active pattern |
| after_check_in_time / before_check_out_time | Hotel | Time constraints; similar patterns covered by appointment_date_valid |
| within_room_service_hours | Hotel | Time window; similar to enrollment period pattern |
| sufficient_account_balance_for_late_fee | Library | Balance check; similar to Bank domain patterns |
| sufficient_account_balance_for_membership | Library | Balance check; similar to Bank domain patterns |
| within_max_reservation_slots | Library | Slot limit; similar to borrow_limit pattern |

---

## 6. Notes for Phase 2B (Injection Pipeline)

1. **Template variables**: Unambiguous versions retain `{variable}` placeholders matching SOPBench's `positive_constraint_descriptions` format. The injection pipeline should fill these from task `constraint_parameters` as usual.

2. **Ambiguous versions have no template variables**: They are complete NL strings that replace the entire constraint description. No parameter substitution needed.

3. **One constraint → multiple pairs**: Several constraints generate 2-3 pairs with different ambiguity types (e.g., `within_enrollment_period` → incompleteness, lexical, conditional_precedence). When running experiments, use one pair at a time per constraint per task to isolate single ambiguity effects.

4. **Negated constraints**: Some constraints appear in negated form in dependency trees (e.g., `not has_exceeded_maximum_stays`). The clause pairs target the base constraint; the injection pipeline must handle negation appropriately.
