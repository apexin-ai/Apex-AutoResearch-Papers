"""redirecting variables"""

# string domain into domain assistant file
from env.domains.bank import bank_assistant
from env.domains.online_market import online_market_assistant
from env.domains.healthcare import healthcare_assistant
from env.domains.dmv import dmv_assistant
from env.domains.library import library_assistant
from env.domains.hotel import hotel_assistant
from env.domains.university import university_assistant

domain_assistant_keys = {
    "bank": bank_assistant,
    "online_market": online_market_assistant,
    "dmv": dmv_assistant,
    "healthcare": healthcare_assistant,
    "library": library_assistant,
    "hotel": hotel_assistant,
    "university": university_assistant,
}

from env.domains.bank.bank import Bank, Bank_Strict
from env.domains.dmv.dmv import DMV, DMV_Strict
from env.domains.healthcare.healthcare import Healthcare, Healthcare_Strict
from env.domains.online_market.online_market import OnlineMarket, OnlineMarket_Strict
from env.domains.library.library import Library, Library_Strict
from env.domains.hotel.hotel import Hotel, Hotel_Strict
from env.domains.university.university import University, University_Strict

domain_keys = {
    "bank": Bank,
    "bank_strict": Bank_Strict,
    "dmv": DMV,
    "dmv_strict": DMV_Strict,
    "healthcare": Healthcare,
    "healthcare_strict": Healthcare_Strict,
    "library": Library,
    "library_strict": Library_Strict,
    "online_market": OnlineMarket,
    "online_market_strict": OnlineMarket_Strict,
    "hotel": Hotel,
    "hotel_strict": Hotel_Strict,
    "university": University,
    "university_strict": University_Strict,
}


"""general variables"""

# model costs as of 20241023
OPENAI_MODEL_COST_PER_1M_TOKENS = {
    "gpt-3.5-turbo-1106":               1,
    "gpt-3.5-turbo-1106-completion":    2,
    "gpt-4-1106-preview":               10,
    "gpt-4-1106-preview-completion":    30,
    "gpt-4o-mini":                      0.15,
    "gpt-4o-mini-completion":           0.60,
    "gpt-4o":                           2.50,
    "gpt-4o-completion":                10,
    "o1-preview":                       15,
    "o1-preview-completion":            60,
    "o3":                               10,
    "o3-completion":                    40,
    "gpt-4.1":                          2,
    "gpt-4.1-completion":               8,
    "gpt-4.1-mini":                     0.1,
    "gpt-4.1-mini-completion":          0.4,
}