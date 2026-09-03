import streamlit as st
import math

from database import get_dashboard_stats, initialise_database, save_market_survey, save_profile

BUSINESSES = [
    {
        "name": "ছাগল পালন", "category": "পশুপালন", "investment": 45000,
        "monthly_profit": 6500, "risk": "মাঝারি", "skills": ["পশুপালন", "কৃষি"],
        "summary": "কম জায়গায় শুরু করা যায় এবং স্থানীয় বাজারে নিয়মিত চাহিদা থাকে।",
    },
    {
        "name": "মাশরুম চাষ", "category": "কৃষিভিত্তিক", "investment": 30000,
        "monthly_profit": 8000, "risk": "কম", "skills": ["কৃষি", "খাদ্য তৈরি"],
        "summary": "অল্প জায়গা ও কম পুঁজিতে দ্রুত উৎপাদন সম্ভব; হোটেল ও বাজারে বিক্রি করা যায়।",
    },
    {
        "name": "মশলা ও আচার প্রক্রিয়াজাতকরণ", "category": "খাদ্য প্রক্রিয়াজাতকরণ", "investment": 35000,
        "monthly_profit": 7500, "risk": "কম", "skills": ["খাদ্য তৈরি", "বিক্রয়"],
        "summary": "ঘরে বসে শুরু করা যায় এবং স্থানীয় দোকান ও online channel-এ বিক্রির সুযোগ আছে।",
    },
    {
        "name": "সেলাই ও পোশাক তৈরির কেন্দ্র", "category": "হস্তশিল্প", "investment": 40000,
        "monthly_profit": 9000, "risk": "কম", "skills": ["সেলাই/হস্তশিল্প", "বিক্রয়"],
        "summary": "স্কুল ইউনিফর্ম, ব্লাউজ ও ছোট পোশাকের স্থানীয় চাহিদাকে কাজে লাগানো যায়।",
    },
    {
        "name": "ডিজিটাল সেবা কেন্দ্র", "category": "সেবা", "investment": 55000,
        "monthly_profit": 10000, "risk": "মাঝারি", "skills": ["ডিজিটাল সেবা", "বিক্রয়"],
        "summary": "Online form, print, photocopy, bill payment ও সরকারি পরিষেবা দেওয়া যাবে।",
    },
    {
        "name": "কৃষি যন্ত্র ভাড়া পরিষেবা", "category": "কৃষিভিত্তিক", "investment": 100000,
        "monthly_profit": 14000, "risk": "মাঝারি", "skills": ["কৃষি", "মেরামত"],
        "summary": "কৃষকদের কাছে sprayer ও ছোট কৃষিযন্ত্র ভাড়া দিয়ে নিয়মিত আয় করা যায়।",
    },
]


st.set_page_config(
    page_title="GramSathi AI",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded",
)


def inject_css() -> None:
    st.markdown(
        """
        <style>
            .stApp { background: #f7faf5; color: #1d2b20; }
            [data-testid="stSidebar"] { background: #123b2a; }
            [data-testid="stSidebar"] * { color: #f7fff6 !important; }
            .hero {
                padding: 2rem; border-radius: 18px;
                background: linear-gradient(120deg, #123b2a, #28734c);
                color: white; margin-bottom: 1.5rem;
            }
            .hero h1 { margin: 0; font-size: 2.3rem; color: white !important; }
            .hero p { margin: .5rem 0 0; font-size: 1.05rem; opacity: .92; color: white !important; }
            .metric-card {
                background: white; border-radius: 14px; padding: 1.1rem;
                border: 1px solid #e2eadf; min-height: 105px;
            }
            .metric-card h3 { color: #28734c; margin: 0 0 .35rem; }
            .metric-card p { color: #516156; margin: 0; }
            .stButton > button {
                background: #e4a83c; color: #1c2c20; border: none;
                border-radius: 8px; font-weight: 700; padding: .55rem 1rem;
            }
            .stButton > button p { color: #1c2c20 !important; }
        </style>
        """,
        unsafe_allow_html=True,
    )


def initialise_state() -> None:
    if "profile" not in st.session_state:
        st.session_state.profile = None
    if "selected_business" not in st.session_state:
        st.session_state.selected_business = None
    if "market_data" not in st.session_state:
        st.session_state.market_data = None


def show_home() -> None:
    st.markdown(
        """
        <div class="hero">
            <h1>🌾 GramSathi AI</h1>
            <p>গ্রামীণ ক্ষুদ্র উদ্যোক্তার জন্য স্থানীয় ব্যবসা পরামর্শ ও আর্থিক পরিকল্পনা সহকারী</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("আপনার ব্যবসার সঙ্গী")
    st.write(
        "আপনার দক্ষতা, বাজেট ও এলাকার তথ্য ব্যবহার করে GramSathi AI উপযুক্ত ব্যবসার ধারণা, "
        "বিনিয়োগ পরিকল্পনা, লাভের পূর্বাভাস এবং loan guidance দেবে।"
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="metric-card"><h3>💡 ব্যবসার ধারণা</h3><p>স্থানীয় চাহিদা ও আপনার দক্ষতার সাথে মিলিয়ে পরামর্শ।</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><h3>📊 আর্থিক পরিকল্পনা</h3><p>খরচ, বিক্রয়, লাভ, break-even এবং cash-flow হিসাব।</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><h3>🏦 Loan সহায়তা</h3><p>ঋণের পরিমাণ, EMI এবং উপযুক্ত সরকারি scheme-এর দিকনির্দেশ।</p></div>', unsafe_allow_html=True)

    st.divider()
    stats = get_dashboard_stats()
    st.subheader("Live Platform Overview")
    stat_1, stat_2, stat_3 = st.columns(3)
    stat_1.metric("Saved entrepreneur profiles", stats["profiles"])
    stat_2.metric("Local market surveys", stats["surveys"])
    stat_3.metric("AI advisory status", "Active" if st.session_state.profile else "Ready")
    st.divider()
    if st.session_state.profile:
        st.success(f"স্বাগতম, {st.session_state.profile['name']}! আপনার profile প্রস্তুত আছে।")
        st.info("Sidebar থেকে ‘Business Advisory’ নির্বাচন করে পরবর্তী ধাপে যান।")
    else:
        st.info("শুরু করতে Sidebar থেকে ‘My Profile’ নির্বাচন করুন।")


def show_profile() -> None:
    st.title("👤 উদ্যোক্তার প্রোফাইল")
    st.caption("এই তথ্য শুধু আপনার জন্য বেশি প্রাসঙ্গিক business plan তৈরিতে ব্যবহৃত হবে।")

    previous = st.session_state.profile or {}
    with st.form("profile_form"):
        left, right = st.columns(2)
        with left:
            name = st.text_input("আপনার নাম *", value=previous.get("name", ""))
            age = st.number_input("বয়স", min_value=18, max_value=80, value=int(previous.get("age", 25)))
            state = st.text_input("রাজ্য *", value=previous.get("state", ""), placeholder="যেমন: West Bengal")
            district = st.text_input("জেলা *", value=previous.get("district", ""))
        with right:
            village = st.text_input("গ্রাম/ব্লক", value=previous.get("village", ""))
            education = st.selectbox("শিক্ষাগত যোগ্যতা", ["বিদ্যালয়", "উচ্চ মাধ্যমিক", "স্নাতক", "ডিপ্লোমা/ITI", "অন্যান্য"], index=["বিদ্যালয়", "উচ্চ মাধ্যমিক", "স্নাতক", "ডিপ্লোমা/ITI", "অন্যান্য"].index(previous.get("education", "উচ্চ মাধ্যমিক")))
            budget = st.number_input("নিজের বিনিয়োগের বাজেট (₹) *", min_value=0, step=5000, value=int(previous.get("budget", 50000)))
            experience = st.selectbox("ব্যবসার অভিজ্ঞতা", ["নেই", "0–1 বছর", "1–3 বছর", "3+ বছর"], index=["নেই", "0–1 বছর", "1–3 বছর", "3+ বছর"].index(previous.get("experience", "নেই")))

        skills = st.multiselect(
            "আপনার দক্ষতা", 
            ["কৃষি", "পশুপালন", "সেলাই/হস্তশিল্প", "খাদ্য তৈরি", "মেরামত", "ডিজিটাল সেবা", "বিক্রয়", "শিক্ষাদান"],
            default=previous.get("skills", []),
        )
        interests = st.multiselect(
            "কোন ধরনের ব্যবসায় আগ্রহী?",
            ["কৃষিভিত্তিক", "খাদ্য প্রক্রিয়াজাতকরণ", "হস্তশিল্প", "খুচরা বিক্রয়", "সেবা", "পশুপালন"],
            default=previous.get("interests", []),
        )
        submitted = st.form_submit_button("প্রোফাইল সংরক্ষণ করুন →")

    if submitted:
        if not name.strip() or not state.strip() or not district.strip() or budget <= 0:
            st.error("নাম, রাজ্য, জেলা এবং শূন্যের বেশি বাজেট দেওয়া বাধ্যতামূলক।")
        else:
            st.session_state.profile = {
                "name": name.strip(), "age": age, "state": state.strip(), "district": district.strip(),
                "village": village.strip(), "education": education, "budget": budget,
                "experience": experience, "skills": skills, "interests": interests,
            }
            save_profile(st.session_state.profile)
            st.success("প্রোফাইল সফলভাবে সংরক্ষণ করা হয়েছে! এখন Business Advisory পেজে যান।")


def get_recommendations(profile: dict) -> list[tuple[int, dict]]:
    recommendations = []
    for business in BUSINESSES:
        score = 0
        if business["investment"] <= profile["budget"]:
            score += 45
        else:
            score += max(0, 25 - int((business["investment"] - profile["budget"]) / 10000) * 5)
        score += 25 * len(set(profile["skills"]).intersection(business["skills"]))
        if business["category"] in profile["interests"]:
            score += 25
        if profile["experience"] != "নেই":
            score += 5
        recommendations.append((min(score, 100), business))
    return sorted(recommendations, key=lambda item: item[0], reverse=True)[:3]


def show_business_advisory() -> None:
    st.title("💡 আপনার জন্য ব্যবসার পরামর্শ")
    if not st.session_state.profile:
        st.warning("আগে ‘My Profile’ পেজ থেকে প্রোফাইল সম্পূর্ণ করুন।")
        return

    profile = st.session_state.profile
    st.write(f"**{profile['name']}**, {profile['district']}, {profile['state']} এবং আপনার ₹{profile['budget']:,} বাজেট অনুযায়ী সেরা তিনটি পরামর্শ:")
    st.caption("Match score নির্ধারিত হয়েছে আপনার বাজেট, দক্ষতা, আগ্রহ এবং ব্যবসার অভিজ্ঞতা থেকে।")

    for index, (score, business) in enumerate(get_recommendations(profile), start=1):
        with st.container(border=True):
            title_col, score_col = st.columns([4, 1])
            with title_col:
                st.subheader(f"{index}. {business['name']}")
                st.write(business["summary"])
            with score_col:
                st.metric("Match score", f"{score}%")
            c1, c2, c3 = st.columns(3)
            c1.write(f"**প্রাথমিক বিনিয়োগ:** ₹{business['investment']:,}")
            c2.write(f"**সম্ভাব্য মাসিক লাভ:** ₹{business['monthly_profit']:,}")
            c3.write(f"**ঝুঁকি:** {business['risk']}")
            if st.button(f"এই ব্যবসাটি বেছে নিন", key=f"select_{index}"):
                st.session_state.selected_business = business
                st.success(f"‘{business['name']}’ নির্বাচন করা হয়েছে। এবার Financial Plan খুলুন।")


def show_market_analysis() -> None:
    st.title("📍 Hyper-Local Market Analysis")
    if not st.session_state.profile or not st.session_state.selected_business:
        st.warning("আগে Profile পূরণ করে একটি business নির্বাচন করুন।")
        return

    business = st.session_state.selected_business
    previous = st.session_state.market_data or {}
    st.write(f"**{business['name']}**-এর জন্য {st.session_state.profile['district']} এলাকার বাজারের তথ্য দিন।")
    st.caption("এগুলো demo survey data। বাস্তবে স্থানীয় customer ও দোকানদারের কাছ থেকে তথ্য সংগ্রহ করা হবে।")

    with st.form("market_form"):
        potential_customers = st.number_input("প্রতি মাসে সম্ভাব্য customer সংখ্যা", min_value=1, value=int(previous.get("potential_customers", 40)), step=5)
        competitors = st.number_input("একই ধরনের প্রতিযোগীর সংখ্যা", min_value=0, value=int(previous.get("competitors", 3)), step=1)
        average_spend = st.number_input("প্রতি customer-এর আনুমানিক খরচ (₹)", min_value=1, value=int(previous.get("average_spend", 250)), step=50)
        demand = st.select_slider("স্থানীয় demand কেমন?", options=["কম", "মাঝারি", "ভালো", "খুব ভালো"], value=previous.get("demand", "ভালো"))
        notes = st.text_area("Customer বা দোকানদারের মতামত (ঐচ্ছিক)", value=previous.get("notes", ""), placeholder="যেমন: সাপ্তাহিক হাটে এই পণ্যের চাহিদা বেশি")
        submitted = st.form_submit_button("বাজার বিশ্লেষণ করুন →")

    if submitted:
        st.session_state.market_data = {
            "potential_customers": potential_customers, "competitors": competitors,
            "average_spend": average_spend, "demand": demand, "notes": notes,
        }
        save_market_survey(
            st.session_state.profile["name"],
            business["name"],
            st.session_state.market_data,
        )

    data = st.session_state.market_data
    if data:
        demand_points = {"কম": 25, "মাঝারি": 50, "ভালো": 75, "খুব ভালো": 100}[data["demand"]]
        competition_penalty = min(data["competitors"] * 5, 35)
        opportunity_score = min(100, max(0, demand_points + min(data["potential_customers"], 100) // 4 - competition_penalty))
        opportunity = "উচ্চ" if opportunity_score >= 70 else "মাঝারি" if opportunity_score >= 45 else "সতর্কতার সাথে"
        market_size = data["potential_customers"] * data["average_spend"]

        st.divider()
        a, b, c = st.columns(3)
        a.metric("Market opportunity score", f"{opportunity_score}%")
        b.metric("সম্ভাব্য মাসিক বাজার", f"₹{market_size:,}")
        c.metric("প্রতিযোগী", data["competitors"])
        st.success(f"মূল্যায়ন: **{opportunity} সুযোগ**। Demand: {data['demand']}।")
        if data["competitors"] >= 5:
            st.info("প্রতিযোগী বেশি। আলাদা quality, home delivery বা introductory offer দিয়ে শুরু করুন।")
        else:
            st.info("প্রতিযোগী তুলনামূলক কম। দ্রুত customer feedback সংগ্রহ করে ছোট pilot শুরু করা ভালো হবে।")
        if data["notes"]:
            st.write(f"**Survey note:** {data['notes']}")


def calculate_emi(principal: float, annual_rate: float, months: int) -> float:
    if principal <= 0:
        return 0
    monthly_rate = annual_rate / 12 / 100
    if monthly_rate == 0:
        return principal / months
    return principal * monthly_rate * (1 + monthly_rate) ** months / ((1 + monthly_rate) ** months - 1)


def build_report(profile: dict, business: dict) -> str:
    investment = business["investment"]
    own_fund = min(profile["budget"], investment)
    loan_needed = max(0, investment - own_fund)
    break_even = math.ceil(investment / business["monthly_profit"])
    return f"""GRAMSATHI AI — BUSINESS ADVISORY REPORT
========================================

Entrepreneur profile
Name: {profile['name']}
Location: {profile['village'] or 'Not specified'}, {profile['district']}, {profile['state']}
Age: {profile['age']}
Skills: {', '.join(profile['skills']) or 'Not specified'}
Own investment capacity: Rs. {profile['budget']:,}

Recommended business
Business: {business['name']}
Category: {business['category']}
Why this fits: {business['summary']}

Financial estimate
Initial investment: Rs. {investment:,}
Own contribution: Rs. {own_fund:,}
Estimated loan requirement: Rs. {loan_needed:,}
Estimated monthly net profit: Rs. {business['monthly_profit']:,}
Estimated break-even: {break_even} months
Risk level: {business['risk']}

Suggested next steps
1. Speak to 10 potential local customers and 3 suppliers.
2. Start with a small pilot before using the full budget.
3. Record all sales and expenses every day.
4. Check PMEGP, SVEP/DAY-NRLM and bank MUDRA-loan eligibility through official channels.

Disclaimer: These are indicative estimates generated by GramSathi AI, not a loan approval or financial guarantee.
"""


def get_gemini_advice(profile: dict, business: dict) -> str:
    """Generate contextual, Bengali business guidance without exposing the API key."""
    from google import genai

    api_key = st.secrets.get("GEMINI_API_KEY")
    if not api_key or api_key == "PASTE_YOUR_KEY_HERE":
        raise ValueError("Gemini API key পাওয়া যায়নি। .streamlit/secrets.toml file-টি দেখুন।")

    prompt = f"""
You are GramSathi AI, a practical, ethical business advisor for rural Indian micro-entrepreneurs.
Reply entirely in clear Bengali. Do not claim to guarantee profits, loans, or government-scheme approval.

Entrepreneur: {profile['name']}, age {profile['age']}
Location: {profile['village'] or 'rural area'}, {profile['district']}, {profile['state']}
Skills: {', '.join(profile['skills']) or 'not specified'}
Available own budget: INR {profile['budget']}
Selected business: {business['name']}
Business summary: {business['summary']}
Estimated initial investment: INR {business['investment']}
Estimated monthly profit: INR {business['monthly_profit']}

Create a concise, action-oriented advisory using these four markdown headings:
1. স্থানীয় সুযোগ
2. প্রথম 30 দিনের পরিকল্পনা
3. বিক্রি ও customer পাওয়ার উপায়
4. ঝুঁকি ও সতর্কতা
Give specific but realistic advice. Mention that local prices and scheme eligibility must be verified.
"""
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt,
    )
    if not response.text:
        raise RuntimeError("Gemini কোনো response দেয়নি। আবার চেষ্টা করুন।")
    return response.text


def show_financial_plan() -> None:
    st.title("📊 Financial Plan")
    business = st.session_state.selected_business
    profile = st.session_state.profile
    if not profile:
        st.warning("আগে ‘My Profile’ পেজ থেকে প্রোফাইল সম্পূর্ণ করুন।")
        return
    if not business:
        st.warning("আগে Business Advisory থেকে একটি ব্যবসা বেছে নিন।")
        return

    st.subheader(f"নির্বাচিত ব্যবসা: {business['name']}")
    st.caption("নিচের হিসাবগুলি প্রাথমিক অনুমান। স্থানীয় বাজারদর অনুযায়ী পরে পরিবর্তন করা যাবে।")

    investment = business["investment"]
    own_fund = min(profile["budget"], investment)
    default_loan = max(0, investment - own_fund)
    monthly_profit = business["monthly_profit"]
    monthly_cost = round(monthly_profit * 1.4)
    monthly_revenue = monthly_profit + monthly_cost
    break_even_months = math.ceil(investment / monthly_profit)

    a, b, c, d = st.columns(4)
    a.metric("মোট প্রাথমিক বিনিয়োগ", f"₹{investment:,}")
    b.metric("নিজের অর্থ", f"₹{own_fund:,}")
    c.metric("সম্ভাব্য মাসিক বিক্রয়", f"₹{monthly_revenue:,}")
    d.metric("সম্ভাব্য মাসিক লাভ", f"₹{monthly_profit:,}")

    st.subheader("প্রাথমিক বিনিয়োগের বিভাজন")
    equip = round(investment * 0.50)
    raw_material = round(investment * 0.30)
    working_capital = investment - equip - raw_material
    table_data = {
        "খাত": ["যন্ত্রপাতি/সেটআপ", "কাঁচামাল/প্রথম stock", "Working capital", "মোট"],
        "আনুমানিক পরিমাণ (₹)": [equip, raw_material, working_capital, investment],
    }
    st.table(table_data)

    st.subheader("Loan ও EMI Calculator")
    l1, l2, l3 = st.columns(3)
    with l1:
        loan_amount = st.number_input("Loan-এর পরিমাণ (₹)", min_value=0, max_value=500000, value=int(default_loan), step=5000)
    with l2:
        interest_rate = st.number_input("বার্ষিক সুদের হার (%)", min_value=0.0, max_value=25.0, value=10.0, step=0.5)
    with l3:
        tenure_years = st.selectbox("Loan-এর সময়কাল", [1, 2, 3, 4, 5], index=2, format_func=lambda x: f"{x} বছর")

    emi = calculate_emi(loan_amount, interest_rate, tenure_years * 12)
    total_payment = emi * tenure_years * 12
    e1, e2, e3 = st.columns(3)
    e1.metric("মাসিক EMI", f"₹{emi:,.0f}")
    e2.metric("মোট পরিশোধ", f"₹{total_payment:,.0f}")
    e3.metric("EMI-এর পর অবশিষ্ট মাসিক লাভ", f"₹{monthly_profit - emi:,.0f}")

    if monthly_profit - emi < 0:
        st.error("এই loan EMI সম্ভাব্য মাসিক লাভের চেয়ে বেশি। Loan-এর পরিমাণ বা সময়কাল পরিবর্তন করুন।")
    else:
        st.success(f"আনুমানিক break-even সময়: {break_even_months} মাস। এই পরিকল্পনায় EMI দেওয়ার পরেও লাভ থাকবে।")


def show_schemes_loan() -> None:
    st.title("🏦 Schemes & Loan Guidance")
    profile = st.session_state.profile
    business = st.session_state.selected_business
    if not profile:
        st.warning("আগে ‘My Profile’ পেজ থেকে প্রোফাইল সম্পূর্ণ করুন।")
        return

    project_cost = business["investment"] if business else profile["budget"]
    st.write(f"আপনার ₹{project_cost:,} আনুমানিক project cost এবং rural location-এর ভিত্তিতে নিচের scheme-গুলি প্রাসঙ্গিক হতে পারে।")

    with st.container(border=True):
        st.subheader("1. PMEGP — Prime Minister's Employment Generation Programme")
        st.write("নতুন viable micro-enterprise-এর জন্য bank-linked subsidy scheme। আপনার নির্বাচিত ব্যবসাটি নতুন unit হলে এটি বিবেচনা করতে পারো।")
        st.write("**প্রাথমিক match:** ভালো — project cost ₹50 lakh-এর অনেক কম।")
        st.write("**খেয়াল রাখবে:** আবেদনকারীকে 18+ হতে হয়; নতুন unit হতে হয়। নির্দিষ্ট project size-এর উপরে শিক্ষাগত যোগ্যতার শর্ত প্রযোজ্য হতে পারে।")
        st.link_button("Official PMEGP portal খুলুন ↗", "https://www.kviconline.gov.in/pmegpeportal/pmegphome/index.jsp")

    with st.container(border=True):
        st.subheader("2. SVEP under DAY-NRLM")
        st.write("গ্রামীণ দরিদ্র পরিবারের enterprise শুরু ও স্থিতিশীল করার জন্য business-management support, training এবং financial assistance-এর ecosystem।")
        st.write("**প্রাথমিক match:** ভালো — আপনার উদ্যোগটি rural micro-enterprise হওয়ায় স্থানীয় SHG/Block Mission Management Unit-এ খোঁজ নিতে পারো।")
        st.link_button("Official SVEP information খুলুন ↗", "https://www.svep.nrlm.gov.in/landing")

    with st.container(border=True):
        st.subheader("3. MUDRA loan — Bank থেকে জেনে নিন")
        st.write("ছোট ব্যবসার working capital বা term-loan-এর জন্য কাছের bank branch-এ MUDRA loan-এর availability ও বর্তমান eligibility জেনে নাও।")
        st.write("**প্রাথমিক match:** ₹50,000–₹1 lakh-এর মতো ছোট project-এর জন্য উপযোগী হতে পারে।")

    st.warning("এটি eligibility prediction, অনুমোদনের নিশ্চয়তা নয়। আবেদন করার আগে official portal, bank বা জেলা শিল্পকেন্দ্রে বর্তমান নিয়ম যাচাই করো।")


def show_ai_business_plan() -> None:
    st.title("🤖 AI Business Plan")
    profile = st.session_state.profile
    business = st.session_state.selected_business
    if not profile or not business:
        st.warning("আগে প্রোফাইল save করে Business Advisory থেকে একটি ব্যবসা নির্বাচন করুন।")
        return

    if not st.button("✨ আমার Business Plan তৈরি করুন"):
        st.info("উপরের button-এ click করলে আপনার তথ্য অনুযায়ী পরিকল্পনা তৈরি হবে।")
        return

    investment = business["investment"]
    monthly_profit = business["monthly_profit"]
    st.success(f"{profile['name']}-এর জন্য personalised plan তৈরি হয়েছে।")
    st.subheader(f"{business['name']} — এক নজরে")
    st.write(f"{profile['district']}, {profile['state']}-এ ₹{investment:,} দিয়ে এই ব্যবসা শুরু করা বাস্তবসম্মত। লক্ষ্য রাখুন, প্রথম 6 মাসে মাসিক ₹{monthly_profit:,} আনুমানিক নিট লাভে পৌঁছানো।")

    left, right = st.columns(2)
    with left:
        st.subheader("প্রথম 30 দিনের Action Plan")
        st.markdown(
            f"""
            1. **দিন 1–7:** স্থানীয় বাজারে 10 জন সম্ভাব্য customer ও 3 জন supplier-এর সঙ্গে কথা বলুন।
            2. **দিন 8–15:** ₹{round(investment * 0.50):,} পর্যন্ত প্রয়োজনীয় setup/যন্ত্রপাতি কিনুন।
            3. **দিন 16–22:** ছোট আকারে উৎপাদন বা পরিষেবা শুরু করে feedback নিন।
            4. **দিন 23–30:** WhatsApp, স্থানীয় দোকান ও সাপ্তাহিক হাটে বিক্রি শুরু করুন।
            """
        )
    with right:
        st.subheader("বিক্রির কৌশল")
        st.markdown(
            """
            - প্রথম 20 জন customer-কে introductory offer দিন।
            - একই এলাকার দোকানদার বা SHG-এর সঙ্গে অংশীদারিত্ব করুন।
            - প্রতিটি বিক্রি ও খরচ খাতায় বা মোবাইলে লিখে রাখুন।
            - ভালো customer feedback-এর ছবি/বার্তা WhatsApp status-এ শেয়ার করুন।
            """
        )

    st.subheader("ঝুঁকি কমানোর পরামর্শ")
    st.write("একবারে সব টাকা খরচ করবেন না। মোট বিনিয়োগের অন্তত 20% emergency working capital হিসেবে রাখুন। প্রথম মাসে ছোট scale-এ বিক্রি পরীক্ষা করে তারপর উৎপাদন বাড়ান।")
    st.subheader("আজকের পরবর্তী কাজ")
    st.info("নিকটবর্তী বাজারে 3 জন customer-এর সাথে কথা বলুন এবং তাদের প্রয়োজন/দাম একটি খাতায় লিখুন। এই তথ্য পরের version-এ local demand analysis-এর জন্য ব্যবহার হবে।")

    st.divider()
    st.subheader("✨ Gemini AI-এর ব্যক্তিগত পরামর্শ")
    try:
        with st.spinner("আপনার profile অনুযায়ী Gemini AI পরামর্শ তৈরি করছে..."):
            ai_advice = get_gemini_advice(profile, business)
        st.markdown(ai_advice)
        st.caption("AI-এর পরামর্শ ব্যবহারের আগে স্থানীয় বাজারদর ও সরকারি নিয়ম যাচাই করুন।")
    except Exception as error:
        st.error("AI পরামর্শ এই মুহূর্তে তৈরি করা যায়নি। API key, internet connection এবং Gemini quota যাচাই করুন।")
        st.caption(f"Technical detail: {error}")

    report = build_report(profile, business)
    st.download_button(
        "⬇️ Business Report Download করুন",
        data=report,
        file_name="gramsathi_business_report.txt",
        mime="text/plain",
    )


def show_coming_soon(title: str, description: str) -> None:
    st.title(title)
    if not st.session_state.profile:
        st.warning("আগে ‘My Profile’ পেজ থেকে প্রোফাইল সম্পূর্ণ করুন।")
    else:
        st.success(f"প্রোফাইল পাওয়া গেছে: {st.session_state.profile['name']} — {st.session_state.profile['district']}, {st.session_state.profile['state']}")
    st.info(description + " এই অংশটি পরের ধাপে তৈরি করব।")


def main() -> None:
    initialise_database()
    inject_css()
    initialise_state()
    with st.sidebar:
        st.title("🌾 GramSathi AI")
        st.caption("Rural Enterprise Navigator")
        page = st.radio("Menu", ["Home", "My Profile", "Business Advisory", "Local Market Analysis", "Financial Plan", "Schemes & Loan", "AI Business Plan"])
        st.divider()
        st.caption("SIH 2026 • Python + Streamlit")

    if page == "Home":
        show_home()
    elif page == "My Profile":
        show_profile()
    elif page == "Business Advisory":
        show_business_advisory()
    elif page == "Local Market Analysis":
        show_market_analysis()
    elif page == "Financial Plan":
        show_financial_plan()
    elif page == "Schemes & Loan":
        show_schemes_loan()
    else:
        show_ai_business_plan()


if __name__ == "__main__":
    main()
