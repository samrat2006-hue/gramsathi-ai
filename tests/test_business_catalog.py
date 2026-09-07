from business_catalog import generate_business_catalog


def test_generate_business_catalog_english_mode_uses_english_labels():
    catalog = generate_business_catalog("English")
    assert catalog
    assert "ছাগল" not in catalog[0]["name"]
    assert "Goat" in catalog[0]["name"] or "Livestock" in catalog[0]["category"]
