"""
Docstring for ComplianceQAPipeline.backend.src.graph.state
This file defines the state management for the graph pipeline

"""

import operator
from typing import TypedDict,Optional,Dict,Any,Annotated, List

# Define schema for a compliance state
class ComplianceState(TypedDict):
    category: str
    description: str
    severity: str
    timestamp: str

class VideoState(TypedDict):
    video_url: str
    video_id: str

    video_meta_data:Dict[str, Any]
    transcript: Optional[str]
    ocr_text: List[str]

    compliance_report: Annotated[ComplianceState, operator.add]


    final_status: str
    final_report: str

    error_report: Annotated[List[str], operator.add]





