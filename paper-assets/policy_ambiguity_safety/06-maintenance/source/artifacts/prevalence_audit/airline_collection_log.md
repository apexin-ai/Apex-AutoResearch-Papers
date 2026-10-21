# Airline Policy Collection Log

**Date:** 2026-05-23
**Total documents collected:** 13
**Airlines covered:** Delta Air Lines, Emirates, Frontier Airlines, Southwest Airlines

## Collected Documents

### Delta Air Lines (7 documents)

| File | Source URL | Type | Words | Key Clauses |
|------|-----------|------|-------|-------------|
| `airline_delta_baggage_policy.txt` | https://www.delta.com/us/en/baggage/overview | Checked Baggage Policy | ~254 | Fees ($45/$55), weight limits (50/70 lb), size limits (62 in), Key West restriction, military exceptions |
| `airline_delta_carryon_policy.txt` | https://www.delta.com/us/en/baggage/carry-on-baggage | Carry-On Baggage Policy | ~238 | Size limits (45 linear in), personal item rules, prohibited items (inflatable devices, knee defenders), 50-seat aircraft restrictions |
| `airline_delta_cancellation_policy.txt` | https://www.delta.com/us/en/change-cancel/cancel-flight | Cancellation/Refund Policy | ~245 | Non-refundable vs refundable, 24-hour risk-free cancellation, eCredits, disruption refunds (3+/6+ hrs), processing times (7 biz days) |
| `airline_delta_rebooking_policy.txt` | https://www.delta.com/us/en/change-cancel/change-flight | Change/Rebooking Policy | ~234 | Eliminated domestic change fees, $0-400 international fees, Basic exclusion, $50 third-party handling charge, 1-year ticket validity |
| `airline_delta_customer_service_plan.txt` | https://www.delta.com/us/en/legal/customer-commitment | Customer Service Plan | ~352 | 12 commitments: lowest fare, 30-min delay notification, 12-hr baggage return, 24-hr cancellation, 7 biz day refunds, tarmac delay needs, oversold procedures, complaint resolution (30/60 days) |
| `airline_delta_accessible_travel_policy.txt` | https://www.delta.com/us/en/accessible-travel-services/overview | Accessible Travel / Disability Services | ~180 | Wheelchair assistance, CROs at all airports, service animals, medical devices, sensory impairment support |
| `airline_delta_checkin_policy.txt` | https://www.delta.com/us/en/check-in-security/overview | Check-In Policy | ~222 | 24-hr online check-in, ID requirements, app auto check-in, kiosk/curbside options, Sky Priority lanes |

### Emirates (2 documents)

| File | Source URL | Type | Words | Key Clauses |
|------|-----------|------|-------|-------------|
| `airline_emirates_baggage_policy.txt` | https://www.emirates.com/english/before-you-fly/baggage/checked-baggage/ | Checked Baggage Policy | ~257 | Weight concept (20-50 kg by class) vs piece concept (Americas/Africa), 32 kg max per piece, 300 cm max dimensions, Skywards member extras, 15-piece delivery limit |
| `airline_emirates_cancellation_policy.txt` | https://www.emirates.com/english/help/faq-topics/cancelling-or-changing-a-booking/ | Cancellation/Change Policy | ~221 | Fare-dependent refund eligibility, online change rules, 72-hr advance online processing, EMD credits valid 1 year, chauffeur-drive rebooking |

### Frontier Airlines (2 documents)

| File | Source URL | Type | Words | Key Clauses |
|------|-----------|------|-------|-------------|
| `airline_frontier_baggage_policy.txt` | https://www.flyfrontier.com/travel/travel-info/bag-options/ | Baggage Policy | ~228 | Personal item (14x18x8), carry-on (24x16x10, <35 lb), checked bag (62 in, <40 lb), Board First option, weight upgrades |
| `airline_frontier_contract_of_carriage.txt` | https://f9prodcdn.azureedge.net/media/11004/coc_r1_english.pdf | Contract of Carriage (R1, 05/05/2026) | ~1924 | 21 sections covering: definitions, refusal to transport (20 grounds), tickets, 24-hr cancellation, checked baggage (40 lb standard), denied boarding compensation (200%/400%), No-Show Cancellation service charge, force majeure, city-group diversions, 6-month action limit, jury waiver |

### Southwest Airlines (2 documents)

| File | Source URL | Type | Words | Key Clauses |
|------|-----------|------|-------|-------------|
| `airline_southwest_contract_of_carriage.txt` | https://www.southwest.com/swa-resources/pdfs/corporate-commitments/contract-of-carriage.pdf | Contract of Carriage (55th Revised, 01/27/2026) | ~2544 | Definitions (Force Majeure, Significantly Delayed = 3hr dom/6hr intl), reservations, no-show policy (Basic/Choice/Choice Extra differentiation), prohibited booking practices (hidden city, back-to-back), fare guarantees, non-transferable tickets, refundable vs nonrefundable, adjacent seat purchase |
| `airline_southwest_customer_service_plan.txt` | https://www.southwest.com/assets/pdfs/corporate-commitments/customer-service-plan.pdf | Customer Service Plan (Rev 25-03, 09/10/2025) | ~1835 | 14 commitments: lowest fare, 30-min delay notification, 12/15-30 hr baggage return, 24-hr cancellation, 7 biz day/20 calendar day refunds, refund alternative disclosure, disability accommodations, tarmac delay plan, oversale procedures (volunteer then involuntary with Notice of Denied Boarding), complaint resolution (30/60 days), irregular operations (meals/lodging for controllable delays, $75 min LUV Voucher for 3+ hr delays) |

## Skipped Airlines and Reasons

| Airline | Attempted URLs | Reason |
|---------|---------------|--------|
| United Airlines | united.com/ual/en/us/fly/travel/baggage.html, united.com/en/us/fly/travel/baggage/*, united.com/ual/en/us/fly/contract-of-carriage.html | Timeout on all attempts (60s exceeded); likely heavy JavaScript rendering |
| American Airlines | aa.com/i18n/travel-info/baggage/baggage.jsp, aa.com/i18n/customer-service/support/* | HTTP 403 Forbidden on all attempts; WAF/bot protection |
| JetBlue | jetblue.com/help/baggage, jetblue.com/baggage, jetblue.com/legal/contract-of-carriage, jetblue.com/customer-service-plan | HTTP 404 on all URL variants tested |
| Spirit Airlines | spirit.com/baggage → redirected to spiritrestructuring.com | Airline in bankruptcy restructuring; all customer-facing pages redirected |
| British Airways | britishairways.com/en-gb/information/baggage-essentials, /conditions-of-carriage | "High demand" holding page returned on all attempts |
| Lufthansa | lufthansa.com/us/en/baggage-overview, /cancellation-and-refund, /conditions-of-carriage | HTTP 403 Forbidden; bot protection |
| Singapore Airlines | singaporeair.com/en_UK/us/travel-info/baggage/* | HTTP 404 on multiple URL patterns |
| Qantas | qantas.com/au/en/travel-info/baggage/*, /customer-charter* | Timeout on all attempts (60s exceeded) |
| Air Canada | aircanada.com/en-ca/fly/baggage, /customer-support/* | Timeout on all attempts (60s exceeded) |
| Alaska Airlines | alaskaair.com/content/travel-info/baggage/*, /policies/* | Content truncated on successful loads; 404 on alternative URLs |
| Air France | airfrance.us/US/en/common/guidevoyageur/pratique/* | Timeout on all attempts (60s exceeded) |

## Coverage Summary

**Policy types collected:**
- Baggage (checked + carry-on): 5 documents
- Cancellation/Refund: 2 documents
- Rebooking/Change: 1 document
- Contract of Carriage: 2 documents
- Customer Service Plan: 2 documents
- Accessible Travel/Passenger Rights: 1 document
- Check-In: 1 document

**Airline diversity:**
- US Full-service: Delta (7 docs)
- US Ultra-low-cost: Frontier (2 docs), Southwest (2 docs)
- International full-service: Emirates (2 docs)

**Note:** Many airlines deploy aggressive bot protection (WAF, Cloudflare), JavaScript-heavy SPAs, or rate limiting that prevents automated scraping. The 4 airlines successfully collected represent a mix of full-service and low-cost carriers across US domestic and international markets, with good policy type diversity.
