real_estate_memo_structure = {
    "name": "real_estate_memo_structure",
    "description": "Extracts structured data from a real estate investment memorandum or raw project data to populate an Investment Committee report.",
    "input_schema": {
        "type": "object",
        "properties": {
            "project_name": {
                "type": ["string"],
                "description": "Real estate project name. Returns 'Real estate project' if no name is found.",
            },
            "project_type": {
                "type": ["string"],
                "enum": ["Desarrollo", "Adquisición", "Value-Add"],
                "description": "Project strategy type (Development, Acquisition, Value-Add). Return 'N/D' if not specified.",
            },
            "equity_required": {
                "type": ["string"],
                "description": "Required equity amount, including currency (e.g., 50,000 USD). Return 'N/D' if not available.",
            },
            "total_project_cost": {
                "type": ["string"],
                "description": "Total project cost, including currency. (e.g., 75 MM COP). Return 'N/D' if not available.",
            },
            "ltv": {
                "type": ["string"],
                "description": "Loan to Value (LTV) ratio as a percentage (e.g, 50%). Return 'N/D' if not available.",
            },
            "location": {
                "type": ["string"],
                "description": "City and area of the project. Maximum 4 words. Return 'N/D' if not available.",
            },
            "recommendation_summary": {
                "type": ["string"],
                "enum": ["INVERTIR", "PASAR", "MÁS DD"],
                "description": "Give an opinion based on the data on whether it's a good idea to invest, pass, or ask for more information.",
            },
            "executive_summary": {
                "type": ["string"],
                "description": "Executive summary of 2-3 paragraphs consolidating the deal. Project type and location, Required investment and structure, Projected returns, Main risks",
            },
            "highlights": {
                "type": ["array"],
                "items": {"type": "string"},
                "description": "3 to 5 items highlighting or unique selling points. REQUIRED: Must return a JSON array of strings. DO NOT return a single string with line breaks.",
            },
            "location_qualities": {
                "type": ["string", "null"],
                "description": "Analysis of location, access, and connectivity. Maximum one paragraph",
            },
            "asset_type": {
                "type": ["string", "null"],
                "description": "Asset class (e.g., Office, Retail, Industrial, Residential). Maximum one word. Return null if not available.",
            },
            "total_area": {
                "type": ["number", "null"],
                "description": "Total area in square meters. Return null if not available.",
            },
            "units": {
                "type": ["string", "null"],
                "description": "Number of units (e.g., '50 apartments' or '1 warehouse'). Return null if not available.",
            },
            "zoning": {
                "type": ["string", "null"],
                "description": "Zoning or land use. Maximum 3 keywords. Return null if not available.",
            },
            "build_year": {
                "type": ["string", "null"],
                "description": "Year of construction or indicate if new. Return null if not available.",
            },
            "asset_status": {
                "type": ["string", "null"],
                "description": "Stabilized, In development, Renovation. Return null if not available.",
            },
            "current_occupancy": {
                "type": ["number", "null"],
                "description": "Current occupancy percentage (number only). Return null if not available.",
            },
            "value_add_plan": {
                "type": ["string", "null"],
                "description": "Description of the value-add plan or development timeline. Maximum one paragraph. Return null if not applicable or not available.",
            },
            "market_fundamentals": {
                "type": ["string", "null"],
                "description": "Analysis of local market fundamentals (vacancy, rents, absorption). Maximum one paragraph. Return null if not available.",
            },
            "comparables": {
                "type": ["array", "null"],
                "maxItems": 3,
                "items": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Name of the comparable project. MANDATORY: If not explicitly stated, exactly return 'N/D'.",
                        },
                        "location": {
                            "type": "string",
                            "description": "Location, neighborhood, or address. MANDATORY: If not explicitly stated, exactly return 'N/D'.",
                        },
                        "rent": {
                            "type": "string",
                            "description": "Rent price per square meter (Renta/m2). Include currency. MANDATORY: If not explicitly stated, exactly return 'N/D'.",
                        },
                        "cap_rate": {
                            "type": "string",
                            "description": "Capitalization Rate (Cap Rate). Include the '%' symbol. MANDATORY: If not explicitly stated, exactly return 'N/D'.",
                        },
                        "year": {
                            "type": "string",
                            "description": "Year of construction or reference. MANDATORY: If not explicitly stated, exactly return 'N/D'.",
                        },
                    },
                    "additionalProperties": False,
                    "required": ["name", "location", "rent", "cap_rate", "year"],
                },
                "description": "Table of comparable projects. MANDATORY: Return a JSON array of objects or null. STRICT LIMIT: Extract a MAXIMUM of 3 comparables. If more exist, pick the 3 most relevant. If any data point is missing, use 'N/D'.",
            },
            "competitive_advantages": {
                "type": ["string", "null"],
                "description": "Competitive advantages of the asset compared to alternatives. Return null if not available.",
            },
            "acquisition_costs": {
                "type": "object",
                "properties": {
                    "acquisition_land": {
                        "type": "object",
                        "properties": {
                            "amount": {
                                "type": "string",
                                "description": "Amount in COP. MANDATORY: If not explicitly stated, exactly return 'N/D'.",
                            },
                            "percentage": {
                                "type": "string",
                                "description": "Percentage (%). MANDATORY: If not explicitly stated, exactly return 'N/D'.",
                            },
                        },
                        "required": ["amount", "percentage"],
                        "additionalProperties": False,
                    },
                    "hard_costs": {
                        "type": "object",
                        "properties": {
                            "amount": {
                                "type": "string",
                                "description": "Amount in COP. MANDATORY: If not explicitly stated, exactly return 'N/D'.",
                            },
                            "percentage": {
                                "type": "string",
                                "description": "Percentage (%). MANDATORY: If not explicitly stated, exactly return 'N/D'.",
                            },
                        },
                        "required": ["amount", "percentage"],
                        "additionalProperties": False,
                    },
                    "soft_costs": {
                        "type": "object",
                        "properties": {
                            "amount": {
                                "type": "string",
                                "description": "Amount in COP. MANDATORY: If not explicitly stated, exactly return 'N/D'.",
                            },
                            "percentage": {
                                "type": "string",
                                "description": "Percentage (%). MANDATORY: If not explicitly stated, exactly return 'N/D'.",
                            },
                        },
                        "required": ["amount", "percentage"],
                        "additionalProperties": False,
                    },
                    "contingency": {
                        "type": "object",
                        "properties": {
                            "amount": {
                                "type": "string",
                                "description": "Amount in COP. MANDATORY: If not explicitly stated, exactly return 'N/D'.",
                            },
                            "percentage": {
                                "type": "string",
                                "description": "Percentage (%). MANDATORY: If not explicitly stated, exactly return 'N/D'.",
                            },
                        },
                        "required": ["amount", "percentage"],
                        "additionalProperties": False,
                    },
                    "financing_costs": {
                        "type": "object",
                        "properties": {
                            "amount": {
                                "type": "string",
                                "description": "Amount in COP. MANDATORY: If not explicitly stated, exactly return 'N/D'.",
                            },
                            "percentage": {
                                "type": "string",
                                "description": "Percentage (%). MANDATORY: If not explicitly stated, exactly return 'N/D'.",
                            },
                        },
                        "required": ["amount", "percentage"],
                        "additionalProperties": False,
                    },
                    "leasing_costs": {
                        "type": "object",
                        "properties": {
                            "amount": {
                                "type": "string",
                                "description": "Amount in COP. MANDATORY: If not explicitly stated, exactly return 'N/D'.",
                            },
                            "percentage": {
                                "type": "string",
                                "description": "Percentage (%). MANDATORY: If not explicitly stated, exactly return 'N/D'.",
                            },
                        },
                        "required": ["amount", "percentage"],
                        "additionalProperties": False,
                    },
                    "total": {
                        "type": "object",
                        "properties": {
                            "amount": {
                                "type": "string",
                                "description": "Total Budget Amount in COP. MANDATORY: If not explicitly stated, exactly return 'N/D'.",
                            },
                            "percentage": {
                                "type": "string",
                                "description": "Total Percentage (usually 100%). MANDATORY: If not explicitly stated, exactly return 'N/D'.",
                            },
                        },
                        "required": ["amount", "percentage"],
                        "additionalProperties": False,
                    },
                },
                "required": [
                    "acquisition_land",
                    "hard_costs",
                    "soft_costs",
                    "contingency",
                    "financing_costs",
                    "leasing_costs",
                    "total",
                ],
                "additionalProperties": False,
                "description": "Table breaking down the development budget. MANDATORY: You must extract data for every single category. If a specific cost is missing from the text, you MUST populate its fields with 'N/D'.",
            },
            "financing_structure": {
                "type": "object",
                "properties": {
                    "senior_debt": {
                        "type": "object",
                        "properties": {
                            "amount": {
                                "type": "string",
                                "description": "Amount in COP. MANDATORY: If not explicitly stated, exactly return 'N/D'.",
                            },
                            "terms": {
                                "type": "string",
                                "description": "Percentage and/or terms. MANDATORY: If not explicitly stated, exactly return 'N/D'.",
                            },
                        },
                        "required": ["amount", "terms"],
                        "additionalProperties": False,
                    },
                    "equity": {
                        "type": "object",
                        "properties": {
                            "amount": {
                                "type": "string",
                                "description": "Amount in COP. MANDATORY: If not explicitly stated, exactly return 'N/D'.",
                            },
                            "terms": {
                                "type": "string",
                                "description": "Percentage and/or terms. MANDATORY: If not explicitly stated, exactly return 'N/D'.",
                            },
                        },
                        "required": ["amount", "terms"],
                        "additionalProperties": False,
                    },
                },
                "required": [
                    "senior_debt",
                    "equity",
                ],
                "additionalProperties": False,
                "description": "Table detailing the financing structure. MANDATORY: You must extract data for every funding source. If a specific source is missing, you MUST populate its fields with 'N/D'.",
            },
            "income_projection": {
                "type": "object",
                "properties": {
                    "potential_gross_income": {
                        "type": "object",
                        "properties": {
                            "amount": {
                                "type": "string",
                                "description": "Annual amount in COP. MANDATORY: If not explicitly stated, exactly return 'N/A'.",
                            },
                            "percentage": {
                                "type": "string",
                                "description": "Percentage of EGI. MANDATORY: If not explicitly stated, exactly return 'N/A'.",
                            },
                        },
                        "required": ["amount", "percentage"],
                        "additionalProperties": False,
                    },
                    "vacancy_loss": {
                        "type": "object",
                        "properties": {
                            "amount": {
                                "type": "string",
                                "description": "Annual amount in COP. MANDATORY: If not explicitly stated, exactly return 'N/A'.",
                            },
                            "percentage": {
                                "type": "string",
                                "description": "Percentage of EGI. MANDATORY: If not explicitly stated, exactly return 'N/A'.",
                            },
                        },
                        "required": ["amount", "percentage"],
                        "additionalProperties": False,
                    },
                    "effective_gross_income": {
                        "type": "object",
                        "properties": {
                            "amount": {
                                "type": "string",
                                "description": "Annual amount in COP. MANDATORY: If not explicitly stated, exactly return 'N/A'.",
                            },
                            "percentage": {
                                "type": "string",
                                "description": "Percentage of EGI (usually 100%). MANDATORY: If not explicitly stated, exactly return 'N/A'.",
                            },
                        },
                        "required": ["amount", "percentage"],
                        "additionalProperties": False,
                    },
                    "operating_expenses": {
                        "type": "object",
                        "properties": {
                            "amount": {
                                "type": "string",
                                "description": "Annual amount in COP. MANDATORY: If not explicitly stated, exactly return 'N/A'.",
                            },
                            "percentage": {
                                "type": "string",
                                "description": "Percentage of EGI. MANDATORY: If not explicitly stated, exactly return 'N/A'.",
                            },
                        },
                        "required": ["amount", "percentage"],
                        "additionalProperties": False,
                    },
                    "net_operating_income": {
                        "type": "object",
                        "properties": {
                            "amount": {
                                "type": "string",
                                "description": "Annual amount in COP. MANDATORY: If not explicitly stated, exactly return 'N/A'.",
                            },
                            "percentage": {
                                "type": "string",
                                "description": "Percentage of EGI. MANDATORY: If not explicitly stated, exactly return 'N/A'.",
                            },
                        },
                        "required": ["amount", "percentage"],
                        "additionalProperties": False,
                    },
                    "noi_margin": {
                        "type": "object",
                        "properties": {
                            "amount": {
                                "type": "string",
                                "description": "Annual amount or leave as 'N/A' if it's only a percentage. MANDATORY: If not explicitly stated, exactly return 'N/A'.",
                            },
                            "percentage": {
                                "type": "string",
                                "description": "NOI Margin Percentage. MANDATORY: If not explicitly stated, exactly return 'N/A'.",
                            },
                        },
                        "required": ["amount", "percentage"],
                        "additionalProperties": False,
                    },
                },
                "required": [
                    "potential_gross_income",
                    "vacancy_loss",
                    "effective_gross_income",
                    "operating_expenses",
                    "net_operating_income",
                    "noi_margin",
                ],
                "additionalProperties": False,
                "description": "Table detailing the stabilized income projection (P&L for Real Estate). MANDATORY: You must extract data for every row. If a specific metric is missing, you MUST populate its fields with 'N/A'.",
            },
            "returns_notes": {
                "type": ["string"],
                "description": "Notes on exit strategy, hold period, or assumed cap rate. Return 'N/D' if not available.",
            },
            "return_analysis": {
                "type": "object",
                "properties": {
                    "irr_levered": {
                        "type": "object",
                        "properties": {
                            "bear": {
                                "type": "string",
                                "description": "IRR for Bear scenario. Include '%' symbol. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "base": {
                                "type": "string",
                                "description": "IRR for Base scenario. Include '%' symbol. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "bull": {
                                "type": "string",
                                "description": "IRR for Bull scenario. Include '%' symbol. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "notes": {
                                "type": "string",
                                "description": "Any brief note or condition. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                        },
                        "required": ["bear", "base", "bull", "notes"],
                        "additionalProperties": False,
                    },
                    "equity_multiple": {
                        "type": "object",
                        "properties": {
                            "bear": {
                                "type": "string",
                                "description": "Equity Multiple (MOIC) for Bear scenario. Include 'x' symbol (e.g., '1.5x'). MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "base": {
                                "type": "string",
                                "description": "Equity Multiple for Base scenario. Include 'x' symbol. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "bull": {
                                "type": "string",
                                "description": "Equity Multiple for Bull scenario. Include 'x' symbol. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "notes": {
                                "type": "string",
                                "description": "Any brief note. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                        },
                        "required": ["bear", "base", "bull", "notes"],
                        "additionalProperties": False,
                    },
                    "cash_on_cash": {
                        "type": "object",
                        "properties": {
                            "bear": {
                                "type": "string",
                                "description": "Cash-on-Cash return for Bear scenario (usually Yr 3 or stabilized). Include '%' symbol. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "base": {
                                "type": "string",
                                "description": "Cash-on-Cash return for Base scenario. Include '%' symbol. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "bull": {
                                "type": "string",
                                "description": "Cash-on-Cash return for Bull scenario. Include '%' symbol. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "notes": {
                                "type": "string",
                                "description": "Any brief note. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                        },
                        "required": ["bear", "base", "bull", "notes"],
                        "additionalProperties": False,
                    },
                },
                "required": ["irr_levered", "equity_multiple", "cash_on_cash"],
                "additionalProperties": False,
                "description": "Table detailing the return metrics across different scenarios. MANDATORY: You must extract data for every row and column. If a scenario or metric is missing, populate with 'N/A'.",
            },
            "gp_lp_structure": {
                "type": "object",
                "properties": {
                    "gp_sponsor": {
                        "type": "object",
                        "properties": {
                            "capital": {
                                "type": "string",
                                "description": "Capital contribution. MANDATORY: If missing or not applicable, exactly return 'N/A'.",
                            },
                            "terms": {
                                "type": "string",
                                "description": "Terms. MANDATORY: If missing or not applicable, exactly return 'N/A'.",
                            },
                        },
                        "required": ["capital", "terms"],
                        "additionalProperties": False,
                    },
                    "lp_us": {
                        "type": "object",
                        "properties": {
                            "capital": {
                                "type": "string",
                                "description": "Capital contribution. MANDATORY: If missing or not applicable, exactly return 'N/A'.",
                            },
                            "terms": {
                                "type": "string",
                                "description": "Terms. MANDATORY: If missing or not applicable, exactly return 'N/A'.",
                            },
                        },
                        "required": ["capital", "terms"],
                        "additionalProperties": False,
                    },
                    "preferred_return": {
                        "type": "object",
                        "properties": {
                            "capital": {
                                "type": "string",
                                "description": "Capital hurdle. MANDATORY: If missing or not applicable, exactly return 'N/A'.",
                            },
                            "terms": {
                                "type": "string",
                                "description": "Hurdle rate. MANDATORY: If missing or not applicable, exactly return 'N/A'.",
                            },
                        },
                        "required": ["capital", "terms"],
                        "additionalProperties": False,
                    },
                    "promote_carry": {
                        "type": "object",
                        "properties": {
                            "capital": {
                                "type": "string",
                                "description": "Profit split tier. MANDATORY: If missing or not applicable, exactly return 'N/A'.",
                            },
                            "terms": {
                                "type": "string",
                                "description": "Promote percentage. MANDATORY: If missing or not applicable, exactly return 'N/A'.",
                            },
                        },
                        "required": ["capital", "terms"],
                        "additionalProperties": False,
                    },
                },
                "required": [
                    "gp_sponsor",
                    "lp_us",
                    "preferred_return",
                    "promote_carry",
                ],
                "additionalProperties": False,
                "description": "Table detailing the GP/LP joint venture structure. MANDATORY: You must extract data for every row. If there is NO GP/LP structure in the deal, you MUST still return this object and populate EVERY single field with 'N/A'.",
            },
            "business_timeline": {
                "type": ["string", "null"],
                "description": "Business timeline and capital calls. Return null if not available.",
            },
            "governance": {
                "type": ["string", "null"],
                "description": "Decision rights and corporate governance. Return null if not available.",
            },
            "risks": {
                "type": "object",
                "properties": {
                    "market_risk": {
                        "type": "object",
                        "properties": {
                            "severity": {
                                "type": "string",
                                "enum": ["Crítica", "Alta", "Media", "Baja", "N/A"],
                                "description": "Severity. MANDATORY: Use predefined Spanish levels. If missing, exactly return 'N/A'.",
                            },
                            "probability": {
                                "type": "string",
                                "enum": ["Alta", "Media", "Baja", "N/A"],
                                "description": "Probability. MANDATORY: Use predefined Spanish levels. If missing, exactly return 'N/A'.",
                            },
                            "mitigant": {
                                "type": "string",
                                "description": "Mitigation strategy. Concise and direct. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                        },
                        "required": ["severity", "probability", "mitigant"],
                        "additionalProperties": False,
                    },
                    "construction_risk": {
                        "type": "object",
                        "properties": {
                            "severity": {
                                "type": "string",
                                "enum": ["Crítica", "Alta", "Media", "Baja", "N/A"],
                                "description": "Severity. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "probability": {
                                "type": "string",
                                "enum": ["Alta", "Media", "Baja", "N/A"],
                                "description": "Probability. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "mitigant": {
                                "type": "string",
                                "description": "Mitigation strategy. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                        },
                        "required": ["severity", "probability", "mitigant"],
                        "additionalProperties": False,
                    },
                    "leasing_risk": {
                        "type": "object",
                        "properties": {
                            "severity": {
                                "type": "string",
                                "enum": ["Crítica", "Alta", "Media", "Baja", "N/A"],
                                "description": "Severity. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "probability": {
                                "type": "string",
                                "enum": ["Alta", "Media", "Baja", "N/A"],
                                "description": "Probability. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "mitigant": {
                                "type": "string",
                                "description": "Mitigation strategy. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                        },
                        "required": ["severity", "probability", "mitigant"],
                        "additionalProperties": False,
                    },
                    "exit_risk": {
                        "type": "object",
                        "properties": {
                            "severity": {
                                "type": "string",
                                "enum": ["Crítica", "Alta", "Media", "Baja", "N/A"],
                                "description": "Severity. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "probability": {
                                "type": "string",
                                "enum": ["Alta", "Media", "Baja", "N/A"],
                                "description": "Probability. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "mitigant": {
                                "type": "string",
                                "description": "Mitigation strategy. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                        },
                        "required": ["severity", "probability", "mitigant"],
                        "additionalProperties": False,
                    },
                    "regulatory_risk": {
                        "type": "object",
                        "properties": {
                            "severity": {
                                "type": "string",
                                "enum": ["Crítica", "Alta", "Media", "Baja", "N/A"],
                                "description": "Severity. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "probability": {
                                "type": "string",
                                "enum": ["Alta", "Media", "Baja", "N/A"],
                                "description": "Probability. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "mitigant": {
                                "type": "string",
                                "description": "Mitigation strategy. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                        },
                        "required": ["severity", "probability", "mitigant"],
                        "additionalProperties": False,
                    },
                    "legal_risk": {
                        "type": "object",
                        "properties": {
                            "severity": {
                                "type": "string",
                                "enum": ["Crítica", "Alta", "Media", "Baja", "N/A"],
                                "description": "Severity. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "probability": {
                                "type": "string",
                                "enum": ["Alta", "Media", "Baja", "N/A"],
                                "description": "Probability. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "mitigant": {
                                "type": "string",
                                "description": "Mitigation strategy. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                        },
                        "required": ["severity", "probability", "mitigant"],
                        "additionalProperties": False,
                    },
                    "other_risks": {
                        "type": "object",
                        "properties": {
                            "severity": {
                                "type": "string",
                                "enum": ["Crítica", "Alta", "Media", "Baja", "N/A"],
                                "description": "Severity. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "probability": {
                                "type": "string",
                                "enum": ["Alta", "Media", "Baja", "N/A"],
                                "description": "Probability. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "mitigant": {
                                "type": "string",
                                "description": "Mitigation strategy. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                        },
                        "required": ["severity", "probability", "mitigant"],
                        "additionalProperties": False,
                    },
                },
                "required": [
                    "market_risk",
                    "construction_risk",
                    "leasing_risk",
                    "exit_risk",
                    "regulatory_risk",
                    "legal_risk",
                    "other_risks",
                ],
                "additionalProperties": False,
                "description": "Table detailing core risks and mitigants. MANDATORY: You must evaluate every single predefined risk category. If a specific risk is not mentioned or not applicable to the deal, populate its fields with 'N/A'.",
            },
            "dd_legal": {
                "type": ["string", "null"],
                "description": "Status of Legal/Title Due Diligence. maximum one paragraph Return null if not available.",
            },
            "dd_technical": {
                "type": ["string", "null"],
                "description": "Status of Technical/Structural Due Diligence. maximum one paragraph Return null if not available.",
            },
            "dd_environmental": {
                "type": ["string", "null"],
                "description": "Status of Environmental Due Diligence. maximum one paragraph Return null if not available.",
            },
            "dd_zoning": {
                "type": ["string", "null"],
                "description": "Status of Zoning/Permits Due Diligence. maximum one paragraph Return null if not available.",
            },
            "dd_financial": {
                "type": ["string", "null"],
                "description": "Status of Financial/Rents Due Diligence. maximum one paragraph Return null if not available.",
            },
            "rationale": {
                "type": ["array"],
                "items": {"type": "string"},
                "description": "Main reasons justifying the recommendation. 1 to 4 bullet max. MANDATORY: You MUST return a JSON array",
            },
            "critical_conditions": {
                "type": ["array"],
                "items": {"type": "string"},
                "description": "Critical conditions precedent to investment. 1 to 4 bullet max MANDATORY: You MUST return a JSON array of strings or null.",
            },
            "next_steps": {
                "type": ["string"],
                "description": "Next operational steps to follow if approved. maximum two paragraph",
            },
        },
        "required": [
            "project_name",
        ],
    },
}

operating_business_memo_structure = {
    "name": "operating_business_memo_structure",
    "description": "Extracts structured data from an investment memorandum or raw data regarding an operating business or startup to populate an Investment Committee report.",
    "input_schema": {
        "type": "object",
        "properties": {
            "project_name": {
                "type": ["string"],
                "description": "Company or startup name. Returns a brief description of the company in a maximum of 3 keywords if the name is not available",
            },
            "business_type": {
                "type": ["string"],
                "enum": ["Equity", "Debt", "Convertible", "SAFE"],
                "description": "Type of instrument or nature of the business.",
            },
            "investment_amount": {
                "type": ["string"],
                "description": "Total suggested investment amount, including currency (e.g., $500,000 USD). Return 'N/D' if not available",
            },
            "ownership": {
                "type": ["number", "null"],
                "description": "Percentage of ownership obtained post-investment (number only). Return null if not available",
            },
            "sector": {
                "type": ["string"],
                "description": "Industry sector or niche (e.g., Fintech, SaaS, Agro, Logistics)",
            },
            "recommendation_summary": {
                "type": ["string"],
                "enum": ["INVERTIR", "PASAR", "MÁS DD"],
                "description": "Recommendation based on the information on what action to take, invest, pass, or more information",
            },
            "executive_summary": {
                "type": ["string"],
                "description": "2-3 paragraphs describing: What the company does, The investment opportunity, Why it is attractive, Main risks",
            },
            "investment_thesis": {
                "type": ["array"],
                "items": {"type": "string"},
                "description": "Return 2 to 5 key points that make up the investment thesis. REQUIRED: Must return a JSON array of strings or null. DO NOT return a single string with numbered lists.",
            },
            "business_model": {
                "type": ["string", "null"],
                "description": "Explanation of the business model, revenue generation, and cost structure. Return null if not available.",
            },
            "products_services": {
                "type": ["string", "null"],
                "description": "Product lines, value proposition, and customer segments. Return null if not available.",
            },
            "management_team": {
                "type": ["string", "null"],
                "description": "Description of the founding and management team (experience, background). Return null if not available.",
            },
            "market_size": {
                "type": ["string", "null"],
                "description": "Market data, TAM, SAM, SOM, and growth projections. Maximum 2 paragraphs. Return null if not available.",
            },
            "competitors": {
                "type": "object",
                "properties": {
                    "competitor_1": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string",
                                "description": "Name of the #1 competitor. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "market_share": {
                                "type": "string",
                                "description": "Market share percentage or description. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "strengths": {
                                "type": "string",
                                "description": "Core strengths. Keep it concise. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "weaknesses": {
                                "type": "string",
                                "description": "Core weaknesses. Keep it concise. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                        },
                        "required": ["name", "market_share", "strengths", "weaknesses"],
                        "additionalProperties": False,
                    },
                    "competitor_2": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string",
                                "description": "Name of the #2 competitor. MANDATORY: If missing or < 2 competitors exist, exactly return 'N/A'.",
                            },
                            "market_share": {
                                "type": "string",
                                "description": "Market share percentage. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "strengths": {
                                "type": "string",
                                "description": "Core strengths. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "weaknesses": {
                                "type": "string",
                                "description": "Core weaknesses. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                        },
                        "required": ["name", "market_share", "strengths", "weaknesses"],
                        "additionalProperties": False,
                    },
                    "competitor_3": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string",
                                "description": "Name of the #3 competitor. MANDATORY: If missing or < 3 competitors exist, exactly return 'N/A'.",
                            },
                            "market_share": {
                                "type": "string",
                                "description": "Market share percentage. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "strengths": {
                                "type": "string",
                                "description": "Core strengths. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "weaknesses": {
                                "type": "string",
                                "description": "Core weaknesses. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                        },
                        "required": ["name", "market_share", "strengths", "weaknesses"],
                        "additionalProperties": False,
                    },
                },
                "required": ["competitor_1", "competitor_2", "competitor_3"],
                "additionalProperties": False,
                "description": "Table detailing the top 3 competitors in the market. MANDATORY: You must return all 3 competitor objects. If the text mentions fewer than 3 competitors, you MUST populate the remaining slots entirely with 'N/A'.",
            },
            "historical_performance": {
                "type": "object",
                "properties": {
                    "revenue": {
                        "type": "object",
                        "properties": {
                            "year_minus_2": {
                                "type": "string",
                                "description": "Amount for Year -2. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "year_minus_1": {
                                "type": "string",
                                "description": "Amount for Year -1. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "year_0": {
                                "type": "string",
                                "description": "Amount for Year 0 (Current/Most recent). MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "growth": {
                                "type": "string",
                                "description": "Growth metric (e.g., CAGR or YoY). MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "margin": {
                                "type": "string",
                                "description": "Margin percentage (if applicable, else 'N/A'). MANDATORY: If missing, exactly return 'N/A'.",
                            },
                        },
                        "required": [
                            "year_minus_2",
                            "year_minus_1",
                            "year_0",
                            "growth",
                            "margin",
                        ],
                        "additionalProperties": False,
                    },
                    "cogs": {
                        "type": "object",
                        "properties": {
                            "year_minus_2": {
                                "type": "string",
                                "description": "COGS for Year -2. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "year_minus_1": {
                                "type": "string",
                                "description": "COGS for Year -1. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "year_0": {
                                "type": "string",
                                "description": "COGS for Year 0. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "growth": {
                                "type": "string",
                                "description": "Growth metric. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "margin": {
                                "type": "string",
                                "description": "Margin percentage. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                        },
                        "required": [
                            "year_minus_2",
                            "year_minus_1",
                            "year_0",
                            "growth",
                            "margin",
                        ],
                        "additionalProperties": False,
                    },
                    "gross_profit": {
                        "type": "object",
                        "properties": {
                            "year_minus_2": {
                                "type": "string",
                                "description": "Gross Profit for Year -2. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "year_minus_1": {
                                "type": "string",
                                "description": "Gross Profit for Year -1. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "year_0": {
                                "type": "string",
                                "description": "Gross Profit for Year 0. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "growth": {
                                "type": "string",
                                "description": "Growth metric. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "margin": {
                                "type": "string",
                                "description": "Gross Margin percentage. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                        },
                        "required": [
                            "year_minus_2",
                            "year_minus_1",
                            "year_0",
                            "growth",
                            "margin",
                        ],
                        "additionalProperties": False,
                    },
                    "opex": {
                        "type": "object",
                        "properties": {
                            "year_minus_2": {
                                "type": "string",
                                "description": "Operating Expenses for Year -2. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "year_minus_1": {
                                "type": "string",
                                "description": "Operating Expenses for Year -1. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "year_0": {
                                "type": "string",
                                "description": "Operating Expenses for Year 0. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "growth": {
                                "type": "string",
                                "description": "Growth metric. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "margin": {
                                "type": "string",
                                "description": "Margin percentage. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                        },
                        "required": [
                            "year_minus_2",
                            "year_minus_1",
                            "year_0",
                            "growth",
                            "margin",
                        ],
                        "additionalProperties": False,
                    },
                    "ebitda": {
                        "type": "object",
                        "properties": {
                            "year_minus_2": {
                                "type": "string",
                                "description": "EBITDA for Year -2. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "year_minus_1": {
                                "type": "string",
                                "description": "EBITDA for Year -1. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "year_0": {
                                "type": "string",
                                "description": "EBITDA for Year 0. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "growth": {
                                "type": "string",
                                "description": "Growth metric. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "margin": {
                                "type": "string",
                                "description": "EBITDA Margin percentage. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                        },
                        "required": [
                            "year_minus_2",
                            "year_minus_1",
                            "year_0",
                            "growth",
                            "margin",
                        ],
                        "additionalProperties": False,
                    },
                },
                "required": ["revenue", "cogs", "gross_profit", "opex", "ebitda"],
                "additionalProperties": False,
                "description": "Table detailing historical financial performance (P&L). MANDATORY: Extract data for every row and column. If a specific year, growth metric, or margin is missing, populate with 'N/A'.",
            },
            "projections": {
                "type": ["string", "null"],
                "description": "Analysis of 3-5 year projections and key assumptions. Return null if not available.",
            },
            "unit_economics": {
                "type": ["string", "null"],
                "description": "Unit metrics of the business (CAC, LTV, payback period, churn). Return null if not available.",
            },
            "investment_terms": {
                "type": "object",
                "properties": {
                    "amount": {
                        "type": "string",
                        "description": "Investment amount. Include currency (e.g., '$XXX millones'). MANDATORY: If missing, exactly return 'N/A'.",
                    },
                    "instrument": {
                        "type": "string",
                        "description": "Investment instrument (e.g., Acciones preferentes, Deuda, SAFE). MANDATORY: If missing, exactly return 'N/A'.",
                    },
                    "pre_money_valuation": {
                        "type": "string",
                        "description": "Pre-Money Valuation. Include currency. MANDATORY: If missing, exactly return 'N/A'.",
                    },
                    "ownership": {
                        "type": "string",
                        "description": "Ownership percentage (e.g., '20%'). MANDATORY: If missing, exactly return 'N/A'.",
                    },
                    "liquidation_preference": {
                        "type": "string",
                        "description": "Liquidation preference multiplier (e.g., '1x', '2x participating'). MANDATORY: If missing, exactly return 'N/A'.",
                    },
                    "board_seats": {
                        "type": "string",
                        "description": "Board seats condition (e.g., '1 de 3 asientos'). MANDATORY: If missing, exactly return 'N/A'.",
                    },
                },
                "required": [
                    "amount",
                    "instrument",
                    "pre_money_valuation",
                    "ownership",
                    "liquidation_preference",
                    "board_seats",
                ],
                "additionalProperties": False,
                "description": "Table detailing the core investment terms (Term Sheet). MANDATORY: Extract data for every single field. If a specific term is not mentioned or not applicable, you MUST populate its field with 'N/A'.",
            },
            "use_of_funds": {
                "type": ["array", "null"],
                "items": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": ["string", "null"],
                            "description": "The specific category for the use of funds (e.g., 'Marketing', 'R&D', 'Working Capital', 'CAPEX'). MANDATORY: Keep it short and punchy. DO NOT use long sentences. Return null if not stated.",
                        },
                        "amount": {
                            "type": ["string", "null"],
                            "description": "The allocated amount. MANDATORY: Express clearly with currency, prioritizing COP or USD depending on the text (e.g., '$1.5 MM USD' or 'COP 500,000,000'). Return null if not found.",
                        },
                    },
                    "additionalProperties": False,
                    "required": ["category", "amount"],
                },
                "description": "Breakdown of how the requested investment capital will be allocated. MANDATORY: You MUST return a JSON array of objects or null.",
            },
            "cap_table": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "shareholder": {
                            "type": "string",
                            "description": "Name of the shareholder, group, or 'Option Pool'. MANDATORY: If missing, exactly return 'N/A'.",
                        },
                        "pre_money_shares": {
                            "type": "string",
                            "description": "Number of shares pre-investment. MANDATORY: If missing or unknown, exactly return 'N/A'.",
                        },
                        "pre_money_ownership": {
                            "type": "string",
                            "description": "Pre-money ownership percentage (e.g., '60%'). MANDATORY: If missing, exactly return 'N/A'.",
                        },
                        "post_money_shares": {
                            "type": "string",
                            "description": "Number of shares post-investment. MANDATORY: If missing or unknown, exactly return 'N/A'.",
                        },
                        "post_money_ownership": {
                            "type": "string",
                            "description": "Post-money ownership percentage (e.g., '45%'). MANDATORY: If missing, exactly return 'N/A'.",
                        },
                    },
                    "required": [
                        "shareholder",
                        "pre_money_shares",
                        "pre_money_ownership",
                        "post_money_shares",
                        "post_money_ownership",
                    ],
                    "additionalProperties": False,
                },
                "description": "Array of objects representing the Cap Table pre and post investment. MANDATORY: Extract all shareholders. You MUST always include a final object at the end of the array where 'shareholder' is 'TOTAL' and the ownerships sum to 100%.",
            },
            "operating_risks": {
                "type": "object",
                "properties": {
                    "risk_1": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string",
                                "description": "The specific risk identified (e.g., 'Riesgo Tecnológico', 'Riesgo de Liquidez'). MANDATORY: Keep it extremely short, 1 to 3 words max. If missing or not applicable, exactly return 'N/A'.",
                            },
                            "severity": {
                                "type": "string",
                                "enum": ["Crítica", "Alta", "Media", "Baja", "N/A"],
                                "description": "The severity level of the risk. MANDATORY: Strictly use predefined Spanish levels. If missing, return 'N/A'.",
                            },
                            "impact": {
                                "type": "string",
                                "description": "The potential business or financial consequence. MANDATORY: Be extremely concise and punchy. DO NOT write long paragraphs. If missing, return 'N/A'.",
                            },
                            "mitigant": {
                                "type": "string",
                                "description": "The proposed mitigation strategy. Keep it professional, direct, and concise. MANDATORY: If missing, return 'N/A'.",
                            },
                        },
                        "required": ["name", "severity", "impact", "mitigant"],
                        "additionalProperties": False,
                    },
                    "risk_2": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string",
                                "description": "The specific risk identified. 1 to 3 words max. If missing or < 2 risks exist, exactly return 'N/A'.",
                            },
                            "severity": {
                                "type": "string",
                                "enum": ["Crítica", "Alta", "Media", "Baja", "N/A"],
                                "description": "Severity level. If missing, return 'N/A'.",
                            },
                            "impact": {
                                "type": "string",
                                "description": "Concise and punchy consequence. If missing, return 'N/A'.",
                            },
                            "mitigant": {
                                "type": "string",
                                "description": "Concise mitigation strategy. If missing, return 'N/A'.",
                            },
                        },
                        "required": ["name", "severity", "impact", "mitigant"],
                        "additionalProperties": False,
                    },
                    "risk_3": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string",
                                "description": "The specific risk identified. 1 to 3 words max. If missing or < 3 risks exist, exactly return 'N/A'.",
                            },
                            "severity": {
                                "type": "string",
                                "enum": ["Crítica", "Alta", "Media", "Baja", "N/A"],
                                "description": "Severity level. If missing, return 'N/A'.",
                            },
                            "impact": {
                                "type": "string",
                                "description": "Concise and punchy consequence. If missing, return 'N/A'.",
                            },
                            "mitigant": {
                                "type": "string",
                                "description": "Concise mitigation strategy. If missing, return 'N/A'.",
                            },
                        },
                        "required": ["name", "severity", "impact", "mitigant"],
                        "additionalProperties": False,
                    },
                    "risk_4": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string",
                                "description": "The specific risk identified. 1 to 3 words max. If missing or < 4 risks exist, exactly return 'N/A'.",
                            },
                            "severity": {
                                "type": "string",
                                "enum": ["Crítica", "Alta", "Media", "Baja", "N/A"],
                                "description": "Severity level. If missing, return 'N/A'.",
                            },
                            "impact": {
                                "type": "string",
                                "description": "Concise and punchy consequence. If missing, return 'N/A'.",
                            },
                            "mitigant": {
                                "type": "string",
                                "description": "Concise mitigation strategy. If missing, return 'N/A'.",
                            },
                        },
                        "required": ["name", "severity", "impact", "mitigant"],
                        "additionalProperties": False,
                    },
                },
                "required": ["risk_1", "risk_2", "risk_3", "risk_4"],
                "additionalProperties": False,
                "description": "Table detailing the core risks of the startup. MANDATORY: Extract up to 4 risks. If the document has fewer than 4 risks, you MUST populate the remaining risk slots entirely with 'N/A'.",
            },
            "exit_scenarios": {
                "type": "object",
                "properties": {
                    "bear": {
                        "type": "object",
                        "properties": {
                            "exit_value": {
                                "type": "string",
                                "description": "Exit value or valuation. Include currency. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "moic": {
                                "type": "string",
                                "description": "Multiple on Invested Capital (e.g., '1.5x'). MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "irr": {
                                "type": "string",
                                "description": "Internal Rate of Return (e.g., '10%'). MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "years": {
                                "type": "string",
                                "description": "Time to exit in years (e.g., '5'). MANDATORY: If missing, exactly return 'N/A'.",
                            },
                        },
                        "required": ["exit_value", "moic", "irr", "years"],
                        "additionalProperties": False,
                    },
                    "base": {
                        "type": "object",
                        "properties": {
                            "exit_value": {
                                "type": "string",
                                "description": "Exit value or valuation. Include currency. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "moic": {
                                "type": "string",
                                "description": "Multiple on Invested Capital (e.g., '3.0x'). MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "irr": {
                                "type": "string",
                                "description": "Internal Rate of Return (e.g., '25%'). MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "years": {
                                "type": "string",
                                "description": "Time to exit in years. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                        },
                        "required": ["exit_value", "moic", "irr", "years"],
                        "additionalProperties": False,
                    },
                    "bull": {
                        "type": "object",
                        "properties": {
                            "exit_value": {
                                "type": "string",
                                "description": "Exit value or valuation. Include currency. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "moic": {
                                "type": "string",
                                "description": "Multiple on Invested Capital (e.g., '5.0x'). MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "irr": {
                                "type": "string",
                                "description": "Internal Rate of Return (e.g., '45%'). MANDATORY: If missing, exactly return 'N/A'.",
                            },
                            "years": {
                                "type": "string",
                                "description": "Time to exit in years. MANDATORY: If missing, exactly return 'N/A'.",
                            },
                        },
                        "required": ["exit_value", "moic", "irr", "years"],
                        "additionalProperties": False,
                    },
                },
                "required": ["bear", "base", "bull"],
                "additionalProperties": False,
                "description": "Table detailing the exit scenarios and return metrics. MANDATORY: You must extract data for every scenario. If a specific metric or scenario is missing from the text, you MUST populate its fields entirely with 'N/A'.",
            },
            "dd_legal": {
                "type": ["string", "null"],
                "description": "Findings or pending items in Legal Due Diligence. Return null if not available.",
            },
            "dd_financial": {
                "type": ["string", "null"],
                "description": "Findings or pending items in Financial Due Diligence. Return null if not available.",
            },
            "dd_technical": {
                "type": ["string", "null"],
                "description": "Findings or pending items in Technical Due Diligence (code, infrastructure). Return null if not available.",
            },
            "dd_commercial": {
                "type": ["string", "null"],
                "description": "Findings or pending items in Commercial Due Diligence. Return null if not available.",
            },
            "dd_operational": {
                "type": ["string", "null"],
                "description": "Findings or pending items in Operational Due Diligence. Return null if not available.",
            },
            "rationale": {
                "type": ["array", "null"],
                "items": {"type": "string"},
                "description": "List of reasons (maximum 5 bullet points) that justify the decision. REQUIRED: Return a JSON array of strings or null.",
            },
            "conditions": {
                "type": ["array", "null"],
                "items": {"type": "string"},
                "description": "Maximum 5 preconditions required (PCs) for investment approval. REQUIRED: Return a JSON array of strings or null.",
            },
            "next_steps": {
                "type": ["string", "null"],
                "description": "Next operational steps in the pipeline. MANDATORY: Return a JSON array of strings or null.",
            },
        },
        "required": [
            "project_name",
        ],
    },
}


tools_structures = [real_estate_memo_structure, operating_business_memo_structure]
