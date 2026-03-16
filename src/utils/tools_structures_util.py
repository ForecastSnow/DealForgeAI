
real_estate_memo_structure = {
    "name": "real_estate_memo_structure",
    "description": "Extracts structured data from a real estate investment memorandum or raw project data to populate an Investment Committee report.",
    "input_schema": {
        "type": "object",
        "properties": {
            "project_name": {
                "type": ["string", "null"],
                "description": "Name of the real estate project. Return null if not available.",
            },
            "date": {
                "type": ["string", "null"],
                "description": "Date of the document or analysis. Return null if not available.",
            },
            "analyst_name": {
                "type": ["string", "null"],
                "description": "Name of the analyst preparing the report. Return null if not available.",
            },
            "project_type": {
                "type": ["string", "null"],
                "enum": ["Desarrollo", "Adquisición", "Value-Add", None],
                "description": "Project strategy type (Development, Acquisition, Value-Add). Return null if not specified.",
            },
            "equity_required": {
                "type": ["string", "null"],
                "description": "Required equity amount, including currency (e.g., 50,000 USD). Return null if not available.",
            },
            "total_project_cost": {
                "type": ["string", "null"],
                "description": "Total project cost, including currency. Return null if not available.",
            },
            "ltv": {
                "type": ["number", "null"],
                "description": "Loan-to-Value (LTV) ratio as a percentage (number only). Return null if not available.",
            },
            "location": {
                "type": ["string", "null"],
                "description": "City and area of the project. Return null if not available.",
            },
            "recommendation_summary": {
                "type": ["string", "null"],
                "enum": ["INVERTIR", "PASAR", "MÁS DD", None],
                "description": "Main recommendation. Return null if not available.",
            },
            "executive_summary": {
                "type": ["string", "null"],
                "description": "Executive summary of 2-3 paragraphs consolidating the deal. Return null if not available.",
            },
            "highlights": {
                "type": ["array", "null"],
                "items": {"type": "string"},
                "description": "Key highlights or unique selling points. MANDATORY: You MUST return a JSON array of strings or null. DO NOT return a single string with line breaks.",
            },
            "location_qualities": {
                "type": ["string", "null"],
                "description": "Analysis of location, access, and connectivity. Return null if not available.",
            },
            "asset_type": {
                "type": ["string", "null"],
                "description": "Asset class (e.g., Office, Retail, Industrial, Residential). Return null if not available.",
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
                "description": "Zoning or land use. Return null if not available.",
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
                "description": "Description of the value-add plan or development timeline. Return null if not applicable or not available.",
            },
            "market_fundamentals": {
                "type": ["string", "null"],
                "description": "Analysis of local market fundamentals (vacancy, rents, absorption). Return null if not available.",
            },
            "comparables": {
                "type": ["array", "null"],
                "items": {
                    "type": "object",
                    "properties": {
                        "name": {"type": ["string", "null"]},
                        "location": {"type": ["string", "null"]},
                        "rent": {"type": ["string", "null"]},
                        "cap_rate": {"type": ["string", "null"]},
                        "year": {"type": ["string", "null"]},
                    },
                },
                "description": "Table of comparable projects in the area. MANDATORY: You MUST return a JSON array of objects or null. DO NOT narrate or stringify.",
            },
            "competitive_advantages": {
                "type": ["string", "null"],
                "description": "Competitive advantages of the asset compared to alternatives. Return null if not available.",
            },
            "acquisition_costs": {
                "type": ["array", "null"],
                "items": {
                    "type": "object",
                    "properties": {
                        "concept": {"type": ["string", "null"]},
                        "amount": {"type": ["string", "null"]},
                        "percentage": {"type": ["string", "null"]},
                    },
                },
                "description": "Table breaking down acquisition costs or budget. MANDATORY: You MUST return a JSON array of objects or null.",
            },
            "financing_structure": {
                "type": ["array", "null"],
                "items": {
                    "type": "object",
                    "properties": {
                        "source": {"type": ["string", "null"]},
                        "amount": {"type": ["string", "null"]},
                        "terms": {"type": ["string", "null"]},
                    },
                },
                "description": "Financing structure (Debt vs Equity). MANDATORY: You MUST return a JSON array of objects or null.",
            },
            "projected_income": {
                "type": ["array", "null"],
                "items": {
                    "type": "object",
                    "properties": {
                        "concept": {"type": ["string", "null"]},
                        "annual": {"type": ["string", "null"]},
                        "percentage_egi": {"type": ["string", "null"]},
                    },
                },
                "description": "Stabilized projected income (NOI, Gross Income, etc.). MANDATORY: You MUST return a JSON array of objects or null.",
            },
            "returns_notes": {
                "type": ["string", "null"],
                "description": "Notes on exit strategy, hold period, or assumed cap rate. Return null if not available.",
            },
            "returns_analysis": {
                "type": ["array", "null"],
                "items": {
                    "type": "object",
                    "properties": {
                        "metric": {"type": ["string", "null"]},
                        "base": {"type": ["string", "null"]},
                        "bull": {"type": ["string", "null"]},
                        "bear": {"type": ["string", "null"]},
                        "notes": {"type": ["string", "null"]},
                    },
                },
                "description": "Projected return metrics (IRR, Equity Multiple, Cash-on-Cash). MANDATORY: You MUST return a JSON array of objects or null.",
            },
            "gp_lp_structure": {
                "type": ["array", "null"],
                "items": {
                    "type": "object",
                    "properties": {
                        "role": {"type": ["string", "null"]},
                        "capital": {"type": ["string", "null"]},
                        "terms": {"type": ["string", "null"]},
                    },
                },
                "description": "Deal structure between GP and LP. MANDATORY: You MUST return a JSON array of objects or null.",
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
                "type": ["array", "null"],
                "items": {
                    "type": "object",
                    "properties": {
                        "name": {"type": ["string", "null"]},
                        "severity": {"type": ["string", "null"]},
                        "probability": {"type": ["string", "null"]},
                        "mitigant": {"type": ["string", "null"]},
                    },
                },
                "description": "Matrix of identified risks and mitigants. MANDATORY: You MUST return a JSON array of objects or null.",
            },
            "dd_legal": {
                "type": ["string", "null"],
                "description": "Status of Legal/Title Due Diligence. Return null if not available.",
            },
            "dd_technical": {
                "type": ["string", "null"],
                "description": "Status of Technical/Structural Due Diligence. Return null if not available.",
            },
            "dd_environmental": {
                "type": ["string", "null"],
                "description": "Status of Environmental Due Diligence. Return null if not available.",
            },
            "dd_zoning": {
                "type": ["string", "null"],
                "description": "Status of Zoning/Permits Due Diligence. Return null if not available.",
            },
            "dd_financial": {
                "type": ["string", "null"],
                "description": "Status of Financial/Rents Due Diligence. Return null if not available.",
            },
            "recommendation": {
                "type": ["string", "null"],
                "enum": ["INVERTIR", "PASAR", "MÁS DD", None],
                "description": "Final recommended decision. Return null if not available.",
            },
            "rationale": {
                "type": ["array", "null"],
                "items": {"type": "string"},
                "description": "Main reasons justifying the recommendation. MANDATORY: You MUST return a JSON array of strings or null.",
            },
            "critical_conditions": {
                "type": ["array", "null"],
                "items": {"type": "string"},
                "description": "Critical conditions precedent to investment. MANDATORY: You MUST return a JSON array of strings or null.",
            },
            "next_steps": {
                "type": ["array", "null"],
                "items": {"type": "string"},
                "description": "Next operational steps to follow. MANDATORY: You MUST return a JSON array of strings or null.",
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
                "type": ["string", "null"],
                "description": "Name of the company or startup. Return null if not available.",
            },
            "date": {
                "type": ["string", "null"],
                "description": "Date of the document or analysis. Return null if not available.",
            },
            "analyst_name": {
                "type": ["string", "null"],
                "description": "Name of the analyst preparing the report. Return null if not available.",
            },
            "business_type": {
                "type": ["string", "null"],
                "enum": ["Equity", "Debt", "Convertible", "SAFE", None],
                "description": "Type of instrument or nature of the business. Return null if not clearly specified.",
            },
            "investment_amount": {
                "type": ["string", "null"],
                "description": "Total suggested investment amount, including currency (e.g., $500,000 USD). Return null if not available.",
            },
            "ownership": {
                "type": ["number", "null"],
                "description": "Percentage of ownership obtained post-investment (number only). Return null if not available.",
            },
            "sector": {
                "type": ["string", "null"],
                "description": "Industry sector or niche (e.g., Fintech, SaaS, Agro, Logistics). Return null if not available.",
            },
            "recommendation_summary": {
                "type": ["string", "null"],
                "enum": ["INVERTIR", "PASAR", "MÁS DD", None],
                "description": "Main recommendation of the memo. Return null if not available.",
            },
            "executive_summary": {
                "type": ["string", "null"],
                "description": "Executive summary detailing what the company does, the opportunity, and risks. Return null if not available.",
            },
            "investment_thesis": {
                "type": ["array", "null"],
                "items": {"type": "string"},
                "description": "Key points forming the investment thesis. MANDATORY: You MUST return a JSON array of strings or null. DO NOT return a single string with numbered lists.",
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
                "description": "Market data, TAM, SAM, SOM, and growth projections. Return null if not available.",
            },
            "competitors": {
                "type": ["array", "null"],
                "items": {
                    "type": "object",
                    "properties": {
                        "name": {"type": ["string", "null"]},
                        "market_share": {"type": ["string", "null"]},
                        "strengths": {"type": ["string", "null"]},
                        "weaknesses": {"type": ["string", "null"]},
                    },
                },
                "description": "Table of direct or indirect competitors. MANDATORY: You MUST return a JSON array of objects or null. DO NOT narrate or stringify.",
            },
            "historical_performance": {
                "type": ["array", "null"],
                "items": {
                    "type": "object",
                    "properties": {
                        "metric": {"type": ["string", "null"]},
                        "year_minus_2": {"type": ["string", "null"]},
                        "year_minus_1": {"type": ["string", "null"]},
                        "year_0": {"type": ["string", "null"]},
                        "growth": {"type": ["string", "null"]},
                        "margin": {"type": ["string", "null"]},
                    },
                },
                "description": "Table of historical financial performance (Revenue, EBITDA, etc.). Return null if not available.",
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
                "type": ["object", "null"],
                "properties": {
                    "amount": {"type": ["string", "null"]},
                    "instrument": {"type": ["string", "null"]},
                    "pre_money_valuation": {"type": ["string", "null"]},
                    "ownership": {"type": ["string", "null"]},
                    "liquidation_preference": {"type": ["string", "null"]},
                    "board_seats": {"type": ["string", "null"]},
                },
                "description": "Detailed terms and conditions of the investment round. Return null if not available.",
            },
            "use_of_funds": {
                "type": ["array", "null"],
                "items": {
                    "type": "object",
                    "properties": {
                        "category": {"type": ["string", "null"]},
                        "amount": {"type": ["string", "null"]},
                    },
                },
                "description": "Breakdown of fund allocation (Marketing, R&D, Capex, etc.). Return null if not available.",
            },
            "cap_table": {
                "type": ["string", "null"],
                "description": "Description or summary of the Cap Table pre and post-investment. Return null if not available.",
            },
            "risks": {
                "type": ["array", "null"],
                "items": {
                    "type": "object",
                    "properties": {
                        "name": {"type": ["string", "null"]},
                        "severity": {"type": ["string", "null"]},
                        "impact": {"type": ["string", "null"]},
                        "mitigant": {"type": ["string", "null"]},
                    },
                },
                "description": "Matrix of operational, financial, or market risks, and their mitigants. Return null if not available.",
            },
            "exit_scenarios": {
                "type": ["string", "null"],
                "description": "Possible exit routes or liquidity events (IPO, M&A, Secondary). Return null if not available.",
            },
            "projected_returns": {
                "type": ["array", "null"],
                "items": {
                    "type": "object",
                    "properties": {
                        "scenario": {"type": ["string", "null"]},
                        "exit_value": {"type": ["string", "null"]},
                        "moic": {"type": ["string", "null"]},
                        "irr": {"type": ["string", "null"]},
                        "years": {"type": ["string", "null"]},
                    },
                },
                "description": "Return metrics in different scenarios (Base, Bull, Bear). Return null if not available.",
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
            "recommendation": {
                "type": ["string", "null"],
                "enum": ["INVERTIR", "PASAR", "MÁS DD", None],
                "description": "Final decision suggested to the committee. Return null if not available.",
            },
            "rationale": {
                "type": ["array", "null"],
                "items": {"type": "string"},
                "description": "List of reasons (bullets) justifying the decision. MANDATORY: Return a JSON array of strings or null.",
            },
            "conditions": {
                "type": ["array", "null"],
                "items": {"type": "string"},
                "description": "Necessary conditions precedent (CPs) if the investment is approved. MANDATORY: Return a JSON array of strings or null.",
            },
            "next_steps": {
                "type": ["array", "null"],
                "items": {"type": "string"},
                "description": "Next operational steps in the pipeline. MANDATORY: Return a JSON array of strings or null.",
            },
        },
        "required": [
            "project_name",
        ],
    },
}


tools_structures = [real_estate_memo_structure, operating_business_memo_structure]
