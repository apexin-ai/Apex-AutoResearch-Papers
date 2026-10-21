# Retail Policy Collection Log

Date: 2026-05-23

## Successfully Collected Documents (11)

| # | File | Company | Policy Type | Source URL | ~Words | ~Clauses |
|---|------|---------|-------------|-----------|--------|----------|
| 1 | retail_target_return_policy.txt | Target | Return Policy | https://www.target.com/returns | 198 | 8 |
| 2 | retail_ikea_return_policy.txt | IKEA | Return/Refund Policy | https://www.ikea.com/us/en/customer-service/returns-claims/ | 220 | 7 |
| 3 | retail_ikea_terms_conditions.txt | IKEA | Terms & Conditions | https://www.ikea.com/us/en/customer-service/terms-conditions/ | 1161 | 21 |
| 4 | retail_ikea_shipping_policy.txt | IKEA | Shipping/Delivery Policy | https://www.ikea.com/us/en/customer-service/services/delivery/ | 385 | 12 |
| 5 | retail_nordstrom_return_policy.txt | Nordstrom | Return/Exchange Policy | https://www.nordstrom.com/browse/customer-service/return-policy | 219 | 8 |
| 6 | retail_zappos_return_shipping_policy.txt | Zappos | Shipping & Returns Policy | https://www.zappos.com/c/shipping-and-returns | 217 | 7 |
| 7 | retail_zappos_terms_of_use.txt | Zappos | Terms of Use / Dispute Resolution | https://www.zappos.com/c/terms-of-use | 255 | 6 |
| 8 | retail_zappos_loyalty_program.txt | Zappos | Loyalty Program Rules | https://www.zappos.com/c/vip | 155 | 6 |
| 9 | retail_apple_return_refund_policy.txt | Apple | Return/Refund Policy | https://www.apple.com/shop/help/returns_refund | 249 | 7 |
| 10 | retail_apple_media_services_terms.txt | Apple | Media Services Terms (Refunds/Cancellations/Complaints) | https://www.apple.com/legal/internet-services/itunes/us/terms.html | 328 | 7 |
| 11 | retail_apple_payment_refund_policy.txt | Apple | Payment, Financing & Refund Policy | https://www.apple.com/shop/help/payments | 646 | 14 |

## Policy Type Coverage

- Return/Refund: 5 docs (Target, IKEA, Nordstrom, Apple x2)
- Shipping/Delivery: 2 docs (IKEA, Zappos)
- Terms & Conditions / Terms of Use: 2 docs (IKEA, Zappos)
- Loyalty Program: 1 doc (Zappos VIP)
- Media Services / Subscription Terms: 1 doc (Apple)

## Companies Covered (5)

Target, IKEA, Nordstrom, Zappos, Apple

## Skipped Companies (10) and Reasons

| Company | Reason |
|---------|--------|
| Amazon | HTTP 503 (service unavailable / bot detection) |
| Walmart | CAPTCHA wall (robot detection on all pages) |
| Costco | Timeout (60s) on multiple page variants |
| Best Buy | Timeout (60s) on return policy page |
| Home Depot | HTTP 403 (access forbidden) |
| Macy's | HTTP 403 (access forbidden) |
| Sephora | HTTP 403 (access forbidden) |
| Nike | HTTP 403 (access forbidden) |
| Lowe's | HTTP 403 (access forbidden) |
| REI | Timeout (60s) on multiple page variants |

## Notes

- Most failed companies use aggressive bot detection (CAPTCHA, 403, WAF) that blocks programmatic access
- All collected documents are from publicly accessible pages, no login required
- IKEA was the most accessible, yielding 3 distinct policy documents
- Apple pages loaded but served Education Store variant; content still contains standard return/refund terms
- Nordstrom Nordy Club loyalty page returned empty content despite successful HTTP response
