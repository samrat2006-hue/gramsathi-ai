"""Scalable catalog for GramSathi AI business advisory plans.

18 base businesses × 4 investment scales × 15 target markets = 1,080 plans.

"""

BASE_BUSINESSES = [

    ("মাশরুম চাষ", "কৃষিভিত্তিক", 30000, 8000, ["কৃষি", "খাদ্য তৈরি"], "কম জায়গায় দ্রুত উৎপাদন করে স্থানীয় বাজার ও হোটেলে বিক্রি করা যায়।", "mushroom, মাশরুম"),

    ("ছাগল পালন", "পশুপালন", 45000, 6500, ["পশুপালন", "কৃষি"], "অল্প জায়গায় শুরু করা যায় এবং স্থানীয় বাজারে নিয়মিত চাহিদা থাকে।", "goat, ছাগল"),

    ("দেশি মুরগি পালন", "পশুপালন", 25000, 7000, ["পশুপালন", "কৃষি"], "ডিম ও দেশি মুরগির স্থানীয় চাহিদা ব্যবহার করা যায়।", "poultry, মুরগি, egg"),

    ("দুগ্ধজাত পণ্য", "খাদ্য প্রক্রিয়াজাতকরণ", 35000, 9000, ["পশুপালন", "খাদ্য তৈরি"], "দুধ, দই ও ঘি বিক্রি করে মূল্য সংযোজন করা যায়।", "dairy, দুধ, ঘি"),

    ("মশলা ও আচার প্রক্রিয়াজাতকরণ", "খাদ্য প্রক্রিয়াজাতকরণ", 35000, 7500, ["খাদ্য তৈরি", "বিক্রয়"], "ঘরে বসে তৈরি করে দোকান ও online channel-এ বিক্রি করা যায়।", "pickle, আচার, মশলা, food"),

    ("বেকারি ও স্ন্যাকস", "খাদ্য প্রক্রিয়াজাতকরণ", 40000, 9000, ["খাদ্য তৈরি", "বিক্রয়"], "চা-দোকান, স্কুল ও হাটে প্রতিদিনের বিক্রির সুযোগ আছে।", "bakery, snack, কেক, খাবার"),

    ("সেলাই ও পোশাক তৈরির কেন্দ্র", "হস্তশিল্প", 40000, 9000, ["সেলাই/হস্তশিল্প", "বিক্রয়"], "স্কুল ইউনিফর্ম, ব্লাউজ ও ছোট পোশাকের স্থানীয় চাহিদাকে কাজে লাগানো যায়।", "tailoring, সেলাই, পোশাক"),

    ("জুট ও বাঁশের হস্তশিল্প", "হস্তশিল্প", 20000, 6000, ["সেলাই/হস্তশিল্প", "বিক্রয়"], "পরিবেশবান্ধব পণ্য স্থানীয় মেলা ও online-এ বিক্রি করা যায়।", "jute, bamboo, বাঁশ, হস্তশিল্প"),

    ("ডিজিটাল সেবা কেন্দ্র", "সেবা", 55000, 10000, ["ডিজিটাল সেবা", "বিক্রয়"], "online form, print, bill payment ও সরকারি পরিষেবা দেওয়া যাবে।", "digital, print, photocopy, online"),

    ("মোবাইল মেরামত কেন্দ্র", "সেবা", 30000, 8500, ["মেরামত", "ডিজিটাল সেবা"], "গ্রামে মোবাইল servicing ও accessories বিক্রি করা যায়।", "mobile repair, মোবাইল, repair"),

    ("কৃষি যন্ত্র ভাড়া পরিষেবা", "কৃষিভিত্তিক", 100000, 14000, ["কৃষি", "মেরামত"], "কৃষকদের কাছে sprayer ও ছোট কৃষিযন্ত্র ভাড়া দিয়ে আয় করা যায়।", "farm machine, sprayer, কৃষি যন্ত্র"),

    ("জৈব সার ও ভার্মি কম্পোস্ট", "কৃষিভিত্তিক", 18000, 5500, ["কৃষি"], "কৃষকদের জন্য কম খরচের জৈব সার তৈরি ও বিক্রি করা যায়।", "compost, fertilizer, সার"),

    ("মাছ চাষ", "পশুপালন", 70000, 12000, ["কৃষি", "পশুপালন"], "পুকুর বা leased জলাশয়ে মাছ চাষ করে বাজারে বিক্রি করা যায়।", "fish, মাছ"),

    ("নার্সারি ও চারা বিক্রি", "কৃষিভিত্তিক", 20000, 6500, ["কৃষি"], "সবজি, ফল ও ফুলের চারা স্থানীয় কৃষক ও বাড়িতে বিক্রি করা যায়।", "nursery, plant, চারা"),

    ("কিরানা ও দৈনন্দিন পণ্যের দোকান", "খুচরা বিক্রয়", 50000, 8000, ["বিক্রয়"], "দৈনন্দিন প্রয়োজনের পণ্যে নিয়মিত customer পাওয়া যায়।", "kirana, grocery, দোকান"),

    ("সৌর আলো ও ছোট electrical service", "সেবা", 45000, 9500, ["মেরামত", "ডিজিটাল সেবা"], "solar light, wiring ও ছোট electrical repair-এর পরিষেবা দেওয়া যায়।", "solar, electrical, বিদ্যুৎ"),

    ("টিউশন ও skill training centre", "সেবা", 10000, 7000, ["শিক্ষাদান", "ডিজিটাল সেবা"], "স্কুলপড়ুয়া ও যুবকদের জন্য tuition বা computer skill class চালানো যায়।", "tuition, coaching, শিক্ষা"),

    ("বিউটি ও wellness service", "সেবা", 25000, 8000, ["সেলাই/হস্তশিল্প", "বিক্রয়"], "বাড়ি বা ছোট salon থেকে appointment-based পরিষেবা দেওয়া যায়।", "beauty, salon, parlour"),

]

SCALES = [("Starter", 0.45), ("Small", 0.75), ("Standard", 1.0), ("Growth", 1.6)]

MARKETS = [

    "স্থানীয় হাট", "গ্রামের পরিবার", "নিকটবর্তী স্কুল", "চা-দোকান", "স্থানীয় দোকান", "হোটেল/রেস্তোরাঁ",

    "SHG group", "কৃষক group", "সাপ্তাহিক বাজার", "WhatsApp customer", "পাশের গ্রাম", "block market",

    "মহিলা customer", "যুব customer", "উৎসবের বাজার",

]


def generate_business_catalog(language: str = "বাংলা") -> list[dict]:

    catalog = []

    english_names = {
        "মাশরুম চাষ": "Mushroom farming",
        "ছাগল পালন": "Goat rearing",
        "দেশি মুরগি পালন": "Indigenous poultry farming",
        "দুগ্ধজাত পণ্য": "Dairy products",
        "মশলা ও আচার প্রক্রিয়াজাতকরণ": "Spice and pickle processing",
        "বেকারি ও স্ন্যাকস": "Bakery and snacks",
        "সেলাই ও পোশাক তৈরির কেন্দ্র": "Tailoring and garment unit",
        "জুট ও বাঁশের হস্তশিল্প": "Jute and bamboo handicraft",
        "ডিজিটাল সেবা কেন্দ্র": "Digital service centre",
        "মোবাইল মেরামত কেন্দ্র": "Mobile repair centre",
        "কৃষি যন্ত্র ভাড়া পরিষেবা": "Farm equipment rental service",
        "জৈব সার ও ভার্মি কম্পোস্ট": "Organic fertiliser and vermicompost",
        "মাছ চাষ": "Fish farming",
        "নার্সারি ও চারা বিক্রি": "Nursery and sapling sales",
        "কিরানা ও দৈনন্দিন পণ্যের দোকান": "Kirana and daily essentials store",
        "সৌর আলো ও ছোট electrical service": "Solar lighting and small electrical service",
        "টিউশন ও skill training centre": "Tuition and skill training centre",
        "বিউটি ও wellness service": "Beauty and wellness service",
    }

    english_summaries = {
        "কম জায়গায় দ্রুত উৎপাদন করে স্থানীয় বাজার ও হোটেলে বিক্রি করা যায়।": "Fast production is possible in a small space, with sales to local markets and hotels.",
        "অল্প জায়গায় শুরু করা যায় এবং স্থানীয় বাজারে নিয়মিত চাহিদা থাকে।": "It can start in a small space and has steady demand in local markets.",
        "ডিম ও দেশি মুরগির স্থানীয় চাহিদা ব্যবহার করা যায়।": "Local demand for eggs and indigenous poultry can be served.",
        "দুধ, দই ও ঘি বিক্রি করে মূল্য সংযোজন করা যায়।": "Value can be added by selling milk, yogurt and ghee.",
        "ঘরে বসে তৈরি করে দোকান ও online channel-এ বিক্রি করা যায়।": "Products can be made at home and sold through shops and online channels.",
        "চা-দোকান, স্কুল ও হাটে প্রতিদিনের বিক্রির সুযোগ আছে।": "There is daily sales potential in tea shops, schools and local markets.",
        "স্কুল ইউনিফর্ম, ব্লাউজ ও ছোট পোশাকের স্থানীয় চাহিদাকে কাজে লাগানো যায়।": "Local demand for school uniforms, blouses and small garments can be served.",
        "পরিবেশবান্ধব পণ্য স্থানীয় মেলা ও online-এ বিক্রি করা যায়।": "Eco-friendly products can be sold at local fairs and online.",
        "online form, print, bill payment ও সরকারি পরিষেবা দেওয়া যাবে।": "Online forms, printing, bill payment and government services can be offered.",
        "গ্রামে মোবাইল servicing ও accessories বিক্রি করা যায়।": "Mobile servicing and accessories can be sold in the village.",
        "কৃষকদের কাছে sprayer ও ছোট কৃষিযন্ত্র ভাড়া দিয়ে আয় করা যায়।": "Income can be earned by renting sprayers and small farm tools to farmers.",
        "কৃষকদের জন্য কম খরচের জৈব সার তৈরি ও বিক্রি করা যায়।": "Low-cost organic fertiliser can be produced and sold to farmers.",
        "পুকুর বা leased জলাশয়ে মাছ চাষ করে বাজারে বিক্রি করা যায়।": "Fish can be farmed in ponds or leased water bodies and sold in markets.",
        "সবজি, ফল ও ফুলের চারা স্থানীয় কৃষক ও বাড়িতে বিক্রি করা যায়।": "Seedlings for vegetables, fruits and flowers can be sold to local farmers and households.",
        "দৈনন্দিন প্রয়োজনের পণ্যে নিয়মিত customer পাওয়া যায়।": "Everyday essential products can attract regular customers.",
        "solar light, wiring ও ছোট electrical repair-এর পরিষেবা দেওয়া যায়।": "Solar lighting, wiring and small electrical repair services can be offered.",
        "স্কুলপড়ুয়া ও যুবকদের জন্য tuition বা computer skill class চালানো যায়।": "Tuition or computer skills classes can be offered to students and young people.",
        "বাড়ি বা ছোট salon থেকে appointment-based পরিষেবা দেওয়া যায়।": "Appointment-based services can be provided from home or a small salon.",
    }

    english_categories = {
        "কৃষিভিত্তিক": "Agri-based",
        "পশুপালন": "Livestock",
        "খাদ্য প্রক্রিয়াজাতকরণ": "Food processing",
        "হস্তশিল্প": "Handicraft",
        "সেবা": "Service",
        "খুচরা বিক্রয়": "Retail sales",
    }

    english_risks = {
        "কম": "Low",
        "মাঝারি": "Moderate",
        "মাঝারি থেকে বেশি": "Moderate to high",
    }

    english_skills = {
        "কৃষি": "Agriculture",
        "পশুপালন": "Livestock",
        "সেলাই/হস্তশিল্প": "Tailoring/Handicraft",
        "খাদ্য তৈরি": "Food processing",
        "মেরামত": "Repair",
        "ডিজিটাল সেবা": "Digital service",
        "বিক্রয়": "Sales",
        "শিক্ষাদান": "Teaching",
    }

    market_translations = {
        "English": {
            "স্থানীয় হাট": "Local market",
            "গ্রামের পরিবার": "Village households",
            "নিকটবর্তী স্কুল": "Nearby schools",
            "চা-দোকান": "Tea shops",
            "স্থানীয় দোকান": "Local shops",
            "হোটেল/রেস্তোরাঁ": "Hotels/restaurants",
            "SHG group": "SHG groups",
            "কৃষক group": "Farmer groups",
            "সাপ্তাহিক বাজার": "Weekly market",
            "WhatsApp customer": "WhatsApp customers",
            "পাশের গ্রাম": "Nearby villages",
            "block market": "Block market",
            "মহিলা customer": "Women customers",
            "যুব customer": "Youth customers",
            "উৎসবের বাজার": "Festival market",
        },
        "हिंदी": {
            "স্থানীয় হাট": "स्थानीय बाजार",
            "গ্রামের পরিবার": "गांव के परिवार",
            "নিকটবর্তী স্কুল": "नजदीकी स्कूल",
            "চা-দোকান": "चाय की दुकानें",
            "স্থানীয় দোকান": "स्थानीय दुकानें",
            "হোটেল/রেস্তোরাঁ": "होटल/रेस्तरां",
            "SHG group": "स्वयं सहायता समूह",
            "কৃষক group": "किसान समूह",
            "সাপ্তাহিক বাজার": "साप्ताहिक बाजार",
            "WhatsApp customer": "WhatsApp ग्राहक",
            "পাশের গ্রাম": "आसपास के गांव",
            "block market": "ब्लॉक बाजार",
            "মহিলা customer": "महिला ग्राहक",
            "যুব customer": "युवा ग्राहक",
            "উৎসবের বাজার": "त्योहार बाजार",
        },
    }

    for base_name, category, investment, profit, skills, summary, keywords in BASE_BUSINESSES:

        for scale_name, multiplier in SCALES:

            for market in MARKETS:
                display_market = market_translations.get(language, {}).get(market, market)
                display_name = base_name
                display_category = category
                display_risk = "কম" if multiplier <= 0.75 else "মাঝারি" if multiplier <= 1 else "মাঝারি থেকে বেশি"
                display_skills = skills
                display_summary = f"{summary} এই plan-টি {display_market} target করে তৈরি করা হয়েছে।"

                if language == "English":
                    display_name = english_names.get(base_name, base_name)
                    display_category = english_categories.get(category, category)
                    display_risk = english_risks.get(display_risk, display_risk)
                    display_skills = [english_skills.get(skill, skill) for skill in skills]
                    translated_summary = english_summaries.get(summary, summary)
                    display_summary = f"{translated_summary} This plan is oriented toward {display_market}."

                if language == "हिंदी":
                    display_summary = f"यह योजना {display_market} को ध्यान में रखकर बनाई गई है।"

                catalog.append({
                    "name": f"{display_name} — {scale_name} plan ({display_market})" if language == "English" else f"{base_name} — {scale_name} plan ({display_market})",
                    "category": display_category,
                    "investment": max(5000, round(investment * multiplier / 500) * 500),
                    "monthly_profit": max(2500, round(profit * multiplier / 500) * 500),
                    "risk": display_risk,
                    "skills": display_skills,
                    "summary": display_summary,
                    "keywords": f"{base_name} {category} {keywords} {market} {display_market} {scale_name}".lower(),
                })

    return catalog