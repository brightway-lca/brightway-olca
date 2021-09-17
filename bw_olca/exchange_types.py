from enum import Enum


class ExchangeType(Enum):
    ACTOR = {"olca": "Actor", "bw": "actors"}
    CATEGORY = {"olca": "Category", "bw": "categories"}
    CURRENCY = {"olca": "Currency", "bw": None}
    DQ_SYSTEM = {"olca": "DQSystem", "bw": "dq_system"}
    FLOW = {"olca": "Flow", "bw": "flows"}
    FLOW_PROPERTY = {"olca": "FlowProperty", "bw": "flow_properties"}
    IMPACT_CATEGORY = {"olca": "ImpactCategory", "bw": None}
    IMPACT_METHOD = {"olca": "ImpactMethod", "bw": None}
    LOCATION = {"olca": "Location", "bw": "locations"}
    PARAMETER = {"olca": "Parameter", "bw": None}
    PROCESS = {"olca": "Process", "bw": "processes"}
    PRODUCT_SYSTEM = {"olca": "ProductSystem", "bw": None}
    PROJECT = {"olca": "Project", "bw": None}
    SOCIAL_INDICATOR = {"olca": "SocialIndicator", "bw": None}
    SOURCE = {"olca": "Source", "bw": "sources"}
    UNIT = {"olca": "Unit", "bw": None}
    UNIT_GROUP = {"olca": "UnitGroup", "bw": "unit_groups"}
